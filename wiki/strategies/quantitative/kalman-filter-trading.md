---
title: "Kalman Filter Trading"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [kalman-filter, adaptive, signal-processing, noise-reduction, quantitative, pairs-trading, dynamic-estimation, crypto]
aliases: ["Kalman Filter Strategy", "Adaptive Filter Trading", "KF Signal Extraction"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [analytical, behavioral, risk-bearing]
edge_mechanism: "The Kalman filter tracks a drifting hidden state (a crypto hedge ratio or 'true' price) online; the edge is capturing structural drift in a relationship faster than a fixed-window regression, then trading the reversion of the filtered residual against the flow that displaced it."
data_required: [ohlcv-1h, ohlcv-daily, funding-rates, cointegration-window]
min_capital_usd: 5000
capacity_usd: 20000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 30
decay_evidence: "A Kalman filter is an estimation layer over [[pairs-trading]]/[[statistical-arbitrage]] and inherits their decay. Its advantage over static OLS shrinks when a relationship breaks structurally (unlock, delisting) rather than drifting smoothly — the Gaussian filter tracks the break as if it were signal and generates confident losing residuals."
kill_criteria: |
  - strategy-level drawdown > 20% from high-water mark
  - rolling 12-month net Sharpe < 0
  - filter innovation sequence fails whiteness test (autocorrelated residuals) on tracked spreads
  - realized half-life of the filtered residual > 2x modeled over a 40-trade sample
  - median realized round-trip cost > 30 bps for a full month
related: ["[[pairs-trading]]", "[[mean-reversion]]", "[[statistical-arbitrage]]", "[[ornstein-uhlenbeck]]", "[[moving-averages]]", "[[regime-detection]]", "[[cointegration]]", "[[cryptodataapi]]"]
---

# Kalman Filter Trading

The Kalman filter is a recursive Bayesian estimation algorithm that extracts a hidden state — a "true" price, trend slope, or hedge ratio — from noisy market data. Developed by Rudolf Kalman in 1960 for aerospace navigation, it is a cornerstone of quantitative signal processing. Unlike [[moving-averages]] with fixed lookback windows, the Kalman filter **adapts online**: it updates its state estimate as each observation arrives, weighting recent data more heavily when the signal is clear and smoothing harder when noise dominates. In crypto its killer application is a **dynamic hedge ratio** for [[pairs-trading]] — capturing the structural drift in a relationship (β between two coins moves as BTC-dominance rotates) that a fixed-window OLS regression misses.

The filter maintains a **state estimate** and an **uncertainty estimate**, blending prediction and observation each step via the **Kalman gain** — a ratio that balances process noise (how fast the true state changes) against observation noise (how much microstructure distorts the tape). High process/observation noise → the filter tracks price closely; the reverse → it smooths aggressively.

## Edge source

Per [[edge-taxonomy]], Kalman-filter trading is primarily **analytical**, secondarily **behavioral / risk-bearing** — it inherits its edge from [[statistical-arbitrage]]:

- **Analytical** — the edge is estimation quality: tracking a drifting hedge ratio (or fair-value state) faster and more stably than a static regression, and reading the filter's innovation (residual) as a mean-reverting trading signal with a calibrated uncertainty band.
- **Behavioral / risk-bearing** — the residual the filter trades is displaced by the same non-fundamental crypto flow (listings, unlocks, single-coin liquidations) that drives all relative-value trades; the trader supplies liquidity against it and is paid the reversion.

The filter is not itself an edge — it is a better *lens*. On a relationship that is not genuinely cointegrated, a Kalman filter tracks noise beautifully and loses money confidently.

## Why this edge exists

A static OLS hedge ratio assumes the relationship between two coins is constant over the lookback window. In crypto it is not: as capital rotates between BTC, ETH, and alts, the β that dollar-neutralizes a pair drifts continuously. A fixed 90-day OLS is always stale — it averages the old and new regimes. The Kalman filter updates β every bar, so the *residual* it computes (observed spread minus filter-estimated spread) is a cleaner measure of genuine, tradeable dislocation. Who is on the other side? The same actors as in [[pairs-trading]]: momentum chasers, forced sellers, and single-name-narrative traders whose flow the filter isolates from the slowly-drifting fair relationship. The edge persists because most participants use static windows and either lag the drift or mistake it for signal.

## Null hypothesis

If the relationship is a random walk with no stable cointegration, the filter's innovation sequence is itself a random walk: the residual does not mean-revert, entries at ±2 innovation-σ diverge as often as they converge, and P&L equals the negative of fees plus funding carry. The null is testable: on the null, the filtered residual fails an [[augmented-dickey-fuller]] stationarity test and the innovation sequence is *not* white (a correctly-specified filter on a real relationship produces white, uncorrelated innovations). A real edge requires a stationary, mean-reverting filtered residual whose innovations pass a whiteness test out-of-sample and revert fast enough to beat crypto carry and cost.

## How it works

The filter runs a two-step **predict–update** cycle:

1. **Predict:** project the state forward. For a hedge-ratio filter, the state is β (modeled as a slow random walk): β_predicted = β_last.
2. **Update:** on the new observation, compute the **Kalman gain** K = predicted_uncertainty / (predicted_uncertainty + observation_noise), then β_new = β_predicted + K · (observed − predicted). K ∈ [0,1]: near 1 the filter trusts the observation (fast adaptation), near 0 it trusts its model (heavy smoothing).

For [[pairs-trading]], the hedge ratio *is* the hidden state; the filter updates it each bar and the **innovation** (observed spread − predicted spread), normalized by its own variance, is the trading signal.

## Rules

### Dynamic hedge-ratio pairs (primary application)
1. Confirm the pair is cointegrated ([[cointegration]] test, p < 0.05) before trusting any filter output.
2. Model the spread with β as the hidden state; tune **Q** (process noise — how fast β drifts) and **R** (observation noise) by maximum likelihood on history, then validate out-of-sample.
3. Compute the normalized innovation z = innovation / sqrt(innovation_variance).
4. **Enter** long the spread when z ≤ −2.0, short the spread when z ≥ +2.0.
5. **Exit** when z returns to 0 (partial at ±0.5).
6. **Stop:** |z| ≥ 3.0–3.5, or the innovation sequence fails a rolling whiteness test (filter mis-specified / relationship broken), or a 2× half-life time stop.

### As an adaptive moving average (secondary)
1. Configure a random-walk (or random-walk-with-drift) state; high Q/R = fast (short-EMA-like), low Q/R = smooth (long-EMA-like).
2. Long when price crosses above the Kalman estimate; short when below; read the estimate's slope as a trend gauge. Treat this as a trend/momentum tool, gated by [[regime-detection]] — it is not the relative-value edge above.

### Sizing
- Use the filter's uncertainty estimate for confidence-scaled sizing: wider posterior variance → smaller position. Risk ≤ 0.5–1% of equity per spread; modest gross leverage.

## Implementation pseudocode

```python
# Kalman dynamic hedge-ratio pairs trade (crypto perps)
import numpy as np

def kalman_pairs(prices_A, prices_B, Q=1e-5, R=1e-3):
    beta = 0.0                       # hidden state: hedge ratio
    P    = 1.0                       # state variance
    signals = []
    for a, b in zip(prices_A, prices_B):
        # predict (beta ~ slow random walk)
        P = P + Q
        # observe: a ≈ beta * b + noise
        pred     = beta * b
        innov    = a - pred          # innovation / residual
        S        = b * P * b + R     # innovation variance
        K        = P * b / S         # Kalman gain
        beta     = beta + K * innov  # update state
        P        = (1 - K * b) * P
        z        = innov / np.sqrt(S)
        signals.append((beta, innov, z))
    return signals                   # trade on z: enter |z|>=2, exit z~0, stop |z|>=3

# gate: only act if the pair is cointegrated and innovations are white (well-specified)
```

Model risk note: Q and R are the whole ballgame. Estimate them by MLE on out-of-sample data; a filter tuned too "fast" (high Q/R) chases noise and over-trades, while one tuned too "slow" lags the very β-drift it exists to capture. Re-validate the innovation whiteness weekly — autocorrelated innovations mean the model is mis-specified or the relationship has broken.

## Indicators / data used

- **Filtered hidden state** (dynamic hedge ratio β, or adaptive fair value) and its **uncertainty**.
- **Innovation / residual sequence** and its normalized z-score — the actual trading signal.
- **[[cointegration]]** and **[[augmented-dickey-fuller]]** tests — to qualify the pair before filtering; a whiteness test on innovations to confirm the filter is well-specified.
- **[[ornstein-uhlenbeck]] half-life** of the filtered residual — sets the time stop.
- **Perp [[funding-rate]]** on the short leg — carry cost on the hold.
- Clean 1h/1d OHLCV for both legs.

## Example trade

**Setup:** ETH/BTC pairs trade on 1h bars, Kalman dynamic hedge ratio.
1. Initialize the filter with β = 15.0 (ETH per BTC) from OLS; Q/R tuned by MLE on 6 months of data.
2. At hour 100 the filter has adapted β to 14.8 as the relationship drifted; the normalized innovation is +2.3σ — ETH is relatively cheap vs BTC on the *current* relationship.
3. **Enter:** short 0.1 BTC-perp (~$6,500), long 1.48 ETH-perp (~$6,500), dollar-neutral at the Kalman β. Entry cost ~10 bps taker.
4. Over 18 hours the residual mean-reverts; the normalized innovation returns to ~0.
5. **Exit** both legs. Convergence P&L ≈ +$340 net after four-fill fees and a small funding carry.
6. A **static** OLS β = 15.0 would have produced a delayed, weaker signal (it lagged the drift to 14.8) and captured roughly $80 less — the filter's advantage is entirely in tracking the drift, not in creating edge.

## Performance characteristics

Kalman-filter pairs inherit the [[statistical-arbitrage]] profile: net Sharpe ~0.4–0.8 for a diversified crypto book (frontmatter assumes 0.6), negatively skewed. The filter's contribution is a modest, real improvement in *residual quality* over static OLS — sharper entries, fewer false signals from stale β — worth perhaps 0.1–0.2 of Sharpe on genuinely-drifting relationships, and nothing on relationships that break rather than drift.

**Cost overlay (crypto pair, per completed round trip = 4 fills):**

| Component | Magnitude | Note |
|---|---|---|
| Taker fees, both legs, entry + exit | ~16–22 bps | Four fills per completed trade |
| Slippage | ~4–20 bps | Wider on loose alt legs |
| Funding carry over the hold | ±1–4 bps/day | Short-leg funding |
| Gross edge per converged trade | ~80–200 bps | Costs consume 20–40% |
| **Breakeven (frontmatter)** | **~30 bps** | Edge must clear this before carry |

The filter does not reduce costs; it improves signal quality so more converged trades clear the same cost hurdle.

## Capacity limits

Bounded by the thinner leg of each pair, as in [[pairs-trading]]/[[statistical-arbitrage]]: liquid majors (ETH/BTC) absorb low tens of millions; loose alt pairs far less. Frontmatter assumes **$20M** blended. Crowding is **high** — Kalman-filtered pairs are a standard quant technique on the same obvious majors everyone trades.

## What kills this strategy

- **Structural break vs smooth drift.** The filter's premise is that β *drifts*; when a relationship *breaks* (unlock, delisting, migration, depeg), the filter tracks the break as if it were signal and generates confident losing residuals. This is the dominant failure mode.
- **Parameter (Q/R) misspecification.** Too-fast → chases noise, over-trades, bleeds cost; too-slow → lags the drift it exists to capture. Both destroy the edge.
- **Non-Gaussian tails.** Extreme crypto moves violate the filter's Gaussian noise assumption and can cause the state estimate to diverge.
- **Innovation autocorrelation.** When innovations stop being white, the model is mis-specified or the market regime changed — a leading kill signal.
- **Cost creep.** Adverse funding plus slippage pushing net edge below the ~30 bps breakeven.

## Kill criteria

- Strategy-level drawdown > 20% from high-water mark.
- Rolling 12-month net Sharpe < 0.
- Filter innovation sequence fails a rolling whiteness test on tracked spreads (autocorrelated residuals) → mis-specified, halt those spreads.
- Realized half-life of the filtered residual > 2× modeled over a 40-trade sample.
- Median realized round-trip cost > 30 bps for a full month.

See [[when-to-retire-a-strategy]].

## Advantages

- **Adaptive:** automatically adjusts to a drifting relationship — no fixed-window tuning, captures structural β-drift a static OLS misses.
- Provides **uncertainty estimates** alongside the state, enabling confidence-based [[position-sizing]].
- Superior to fixed-window methods for crypto hedge-ratio estimation, where β genuinely moves week to week.
- Computationally trivial: O(1) per update, runs in real time even at tick frequency.
- Theoretically optimal under linear-Gaussian assumptions, and reasonably robust when they are mildly violated.

## Disadvantages

- **Parameter sensitivity:** Q/R tuning dominates performance; poor calibration yields laggy or noisy estimates.
- Assumes **linear dynamics** — nonlinear crypto behavior may need extended/unscented Kalman filters, adding complexity.
- The **Gaussian noise assumption** is violated by fat-tailed crypto returns; extreme moves can cause divergence.
- More complex to implement and debug than [[moving-averages]] or [[bollinger-bands]].
- **Overfitting risk:** MLE parameter optimization can overfit in-sample.
- Does not model [[regime-detection]] — a single filter struggles across fundamentally different states; a broken (not drifting) relationship fools it.

## Sources

- Kalman, R. E. (1960). "A New Approach to Linear Filtering and Prediction Problems." *Journal of Basic Engineering* — the original filter.
- [[book-algorithmic-trading-ernest-chan]] — practical Kalman hedge-ratio and mean-reversion implementations directly usable on crypto pairs.
- Avellaneda, M. & Lee, J.-H. (2010). "Statistical Arbitrage in the US Equities Market." *Quantitative Finance* — dynamic residual estimation at portfolio scale.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000` — OHLCV for each leg (feed the filter)
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — HL perp OHLCV for the second leg
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — short-leg funding carry

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for filter tuning (Q/R MLE) and backtests
- `GET /api/v1/backtesting/funding` — funding history for the carry overlay
- `GET /api/v1/backtesting/symbols` — symbols with backtest-grade history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

## Related

- [[pairs-trading]] — the primary application of Kalman filters in crypto (dynamic hedge ratio)
- [[statistical-arbitrage]] — the broader framework where the filter provides signal extraction
- [[ornstein-uhlenbeck]] — the reversion model the filtered residual is traded against
- [[cointegration]] — the property a pair must have before the filter is meaningful
- [[moving-averages]] — the simpler, fixed-window alternative the filter improves upon
- [[regime-detection]] — can gate the filter's adaptive-MA mode by market state
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
