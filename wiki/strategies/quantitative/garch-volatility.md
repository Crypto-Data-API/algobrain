---
title: "GARCH Volatility Timing (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [quantitative, volatility, crypto, position-sizing, risk-management, backtesting, machine-learning]
aliases: ["GARCH Volatility Forecasting", "GARCH Position Scaling", "Volatility-Managed Crypto Book", "Conditional Heteroskedasticity Timing", "Crypto Vol Targeting"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested

# Edge characterization
edge_source: [analytical, structural, behavioral]
edge_mechanism: "Volatility is persistent and forecastable while next-period returns are not; a GARCH-scaled crypto book cuts exposure before the low-Sharpe high-vol regime that constant-notional retail leverage rides down into liquidation, harvesting the volatility-managed-portfolio premium and avoiding forced deleveraging."

# Data and infrastructure requirements
data_required: [ohlcv-daily, ohlcv-hourly, realized-vol, funding-rates, perp-price]
min_capital_usd: 5000
capacity_usd: 500000000
crowding_risk: low

# Performance expectations (net of rebalance costs, applied as an overlay on a BTC/ETH book)
expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 15

# Decay history
decay_evidence: "Volatility clustering is the most stable stylised fact in markets, so the forecast itself does not decay; but the incremental Sharpe from vol-targeting has compressed as crypto funds industrialised vol-targeting overlays post-2021, and crypto's asymmetry term is unstable — BTC has repeatedly shown an INVERSE leverage effect (upside vol > downside vol) in bull phases, so GJR/EGARCH specifications tuned on equity intuition misfire and naive constant-parameter GARCH degrades across regime boundaries."

# Lifecycle
kill_criteria: |
  - realised out-of-sample QLIKE/MSE of the GARCH forecast underperforms a trailing-EWMA baseline for 90 days
  - vol-scaled book Sharpe (rolling 6-month) falls below the unscaled buy-and-hold benchmark it overlays
  - alpha+beta persistence estimate exceeds 0.999 (integrated/degenerate fit — model unstable)
  - realised vol repeatedly exceeds the 99% GARCH forecast band (fat-tail/jump regime the model cannot see)

related: ["[[volatility-clustering]]", "[[realized-volatility]]", "[[historical-volatility]]", "[[volatility-targeting]]", "[[position-sizing]]", "[[funding-aware-position-sizing]]", "[[atr-position-sizing]]", "[[regime-detection]]", "[[vol-regime-detection]]", "[[volatility-regime]]", "[[leverage-effect]]", "[[tail-risk-hedging]]", "[[maximum-drawdown]]", "[[kelly-criterion]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[skew-trading]]", "[[volatility-carry]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[deflated-sharpe-ratio]]", "[[cryptodataapi]]"]
---

# GARCH Volatility Timing (Crypto)

GARCH volatility timing uses a **Generalised Autoregressive Conditional Heteroskedasticity** model to forecast the next-period [[realized-volatility|realised volatility]] of BTC, ETH, or a basket of [[perpetual-futures|crypto perps]], then **scales exposure inversely to that forecast** — cutting size before forecast vol rises and re-levering as it falls. It is not a directional alpha strategy; it is a *risk-timing overlay* that improves the risk-adjusted return of whatever underlying book it sits on (trend, carry, or simple long-BTC) by exploiting the fact that crypto volatility is strongly persistent and forecastable while returns are close to a random walk. The core equation, GARCH(1,1), models tomorrow's variance as a weighted sum of a long-run variance, today's squared return, and today's variance: **σ²_t = ω + α·r²_(t-1) + β·σ²_(t-1)**.

## Edge source

Mapping to [[edge-taxonomy]], GARCH timing is an analytical/structural overlay, not a behavioural alpha:

- **Analytical (primary).** The edge is a *modelling* edge over the naive trader who assumes constant volatility. Crypto vol clusters violently — a 8% BTC day is far more likely to be followed by another large move than by a 0.5% day. GARCH quantifies the conditional variance and lets you pre-position risk. The operator who does the estimation carefully (right training window, right specification, out-of-sample validation) beats the one who uses a fixed stop or fixed notional.
- **Structural.** [[volatility-targeting|Volatility-managed portfolios]] earn a documented premium (Moreira & Muir, 2017): scaling down in high-vol regimes improves Sharpe because high realised vol predicts *low* risk-adjusted returns. In crypto this is amplified because the highest-vol regimes coincide with [[liquidation]] cascades where constant-leverage participants are *forced* to sell — a structural flow the vol-timer sidesteps.
- **Behavioural (secondary).** Retail crypto uses fixed high leverage (10-100x) regardless of regime. When vol spikes, their maintenance margin is breached and they are liquidated into the move. The GARCH book is on the other side of that behaviour: de-risked before the flush, with dry powder to re-lever after.

The strategy explicitly does **not** claim to predict direction. Its expected return comes from *better risk shaping*, not from a return forecast.

## Why this edge exists

1. **Volatility is forecastable; returns are not.** Autocorrelation of squared returns (vol) is strongly positive and slow-decaying (α+β near 1). Autocorrelation of raw returns is ~0. This asymmetry is the single most robust regularity in crypto price data and it is what makes conditional-variance timing work when return timing does not.
2. **High-vol regimes carry poor risk-adjusted returns.** Empirically, the Sharpe of holding BTC through its highest-vol deciles is far below its low-vol deciles. Cutting exposure in the top vol decile removes the worst risk-adjusted exposure while keeping most of the upside — a mechanical Sharpe improvement.
3. **Forced-leverage flows make crypto vol especially punishing.** Because so much crypto exposure is leveraged perps, high-vol episodes trigger [[liquidation]] cascades that overshoot. A book that is already de-risked avoids being the marginal liquidated long and can provide liquidity into the overshoot.

## Null hypothesis

Under a no-edge world, conditional volatility is unforecastable beyond a trailing simple average, and vol-scaling adds nothing:

- The GARCH one-step forecast would not beat a naive trailing-window or EWMA vol estimate out-of-sample (equal QLIKE/MSE).
- A vol-scaled book would have the *same* Sharpe as the unscaled book — scaling would only relabel the same risk-adjusted return.
- High-vol regimes would carry the *same* forward Sharpe as low-vol regimes, so cutting exposure in high vol would sacrifice return one-for-one.
- α+β would be statistically indistinguishable from 0 (no persistence).

Empirically for BTC/ETH 2017-2025 the null is rejected: GARCH (and its GJR/EGARCH variants) beat trailing-window vol out-of-sample on QLIKE at daily and hourly horizons; α+β sits ~0.95-0.99 (strong persistence); and vol-scaled BTC has historically improved Sharpe ~0.1-0.4 and roughly halved max drawdown versus buy-and-hold. **But** the null is *not* rejected during pure jump events — a single overnight gap (exchange hack, depeg, 2025-10-10) is a discontinuity GARCH cannot forecast, and in those windows the model's forecast band is useless. GARCH times *diffusive* vol well and *jump* vol not at all.

## Rules

### Model

1. **Specification.** Fit **GJR-GARCH(1,1)** (asymmetric) as the default, with plain GARCH(1,1) and EGARCH(1,1) as challengers. Re-estimate the asymmetry sign every refit — do **not** hard-code equity-style negative leverage effect; BTC frequently shows the inverse.
2. **Estimation window.** 500-750 daily observations (~1.5-2 years) for the daily model; 1,500-2,000 hourly bars for an intraday model. Re-fit weekly (daily model) or daily (hourly model) via maximum likelihood.
3. **Forecast.** Produce a one-step-ahead σ_t and annualise (`σ_daily × √365`). For multi-horizon risk, use the GARCH mean-reversion path but cap horizon at 5 days (multi-step decays fast).

### Position scaling (the core rule)

4. **Target-vol sizing.** Choose a target annualised vol for the book (e.g. **40%** for a BTC-centric sleeve). Set exposure = `target_vol / forecast_vol`, capped at a max leverage (e.g. 2.0x) and floored at 0.
5. **Rebalance band.** Only rebalance when target exposure differs from current by > **15%** (avoids churn and rebalance-cost bleed).
6. **Vol floor/ceiling.** Clamp forecast vol to a sane range (e.g. 20%-200% annualised) to avoid degenerate leverage when the fit misbehaves.

### Overlay uses

7. **Dynamic stops.** Set stop distance = `k · σ_t` (k = 2-3) instead of a fixed %. Wide stops in high vol, tight in low vol.
8. **Regime gate.** When forecast vol enters the top decile of its 1-year range, additionally hard-cap leverage at 0.5x regardless of the target-vol formula (jump-risk guard).
9. **Funding overlay.** For perp exposure, net the [[funding-rate|funding]] carry against the vol-scaled size — see [[funding-aware-position-sizing]].

## Implementation pseudocode

```python
# garch_vol_timing.py — daily GJR-GARCH inverse-vol position scaling on a crypto book
from arch import arch_model   # Python 'arch' library
import numpy as np

TARGET_VOL   = 0.40    # 40% annualised target for the book
MAX_LEV      = 2.0
REBAL_BAND   = 0.15    # rebalance only if |new-old|/old > 15%
VOL_FLOOR    = 0.20
VOL_CEIL     = 2.00
TOPDECILE_CAP = 0.50   # hard leverage cap when forecast vol in top 1y decile

def forecast_vol(daily_returns):
    # GJR-GARCH(1,1); returns in % (arch expects scaled)
    am  = arch_model(daily_returns * 100, vol="Garch", p=1, o=1, q=1, dist="skewt")
    res = am.fit(disp="off")
    persistence = res.params.get("alpha[1]",0) + res.params.get("beta[1]",0) \
                  + 0.5*res.params.get("gamma[1]",0)
    fc  = res.forecast(horizon=1, reindex=False)
    sigma_daily = np.sqrt(fc.variance.values[-1,0]) / 100.0
    sigma_ann   = sigma_daily * np.sqrt(365)
    return sigma_ann, persistence

def target_exposure(sigma_ann, vol_pctl_1y, current_expo):
    sigma_ann = min(max(sigma_ann, VOL_FLOOR), VOL_CEIL)
    expo = TARGET_VOL / sigma_ann
    if vol_pctl_1y > 0.90:              # jump-risk regime
        expo = min(expo, TOPDECILE_CAP)
    expo = min(expo, MAX_LEV)
    # rebalance band: hold if change is small
    if current_expo > 0 and abs(expo - current_expo)/current_expo < REBAL_BAND:
        return current_expo, "HOLD"
    return expo, "REBALANCE"

# daily loop
sigma_ann, persistence = forecast_vol(returns_750d)
if persistence > 0.999:
    signal = ("FLATTEN", "degenerate/integrated GARCH fit — model unstable")
else:
    expo, action = target_exposure(sigma_ann, vol_pctl_1y, book.exposure)
    signal = (action, f"target exposure {expo:.2f}x at forecast vol {sigma_ann:.0%}")
```

Production adds: out-of-sample QLIKE tracking versus an EWMA baseline (kill trigger), a walk-forward refit schedule, jump detection (bipower variation) to flag forecast-invalid days, and a funding-cost overlay for the perp leg.

## Indicators / data used

- **Daily/hourly OHLCV returns** — the GARCH input; close-to-close log returns of BTC/ETH perps or spot.
- **[[realized-volatility|Realised vol]]** — high-frequency realised variance (5-min sampled) as the out-of-sample forecast target and QLIKE benchmark.
- **[[volatility-regime|Vol-regime]] label** — CryptoDataAPI's compressed/expanding/vol_shock classification as an independent cross-check on the GARCH state.
- **[[funding-rate|Funding]]** — carry overlay on the perp exposure; see [[funding-aware-position-sizing]].
- **1-year vol percentile** — for the top-decile jump-risk cap.
- **Bipower / jump indicator** — flags days where a discontinuity means the GARCH band is invalid.

## Example trade

**Setup (BTC daily GJR-GARCH, book target vol 40%):**

1. Model fit on 2024-06 → 2026-06 daily returns. Parameters: ω ≈ 3e-5, α ≈ 0.10, γ (asymmetry) ≈ **-0.03** (mild *inverse* leverage effect — upside vol slightly exceeds downside, the crypto quirk), β ≈ 0.86. Persistence α+β+0.5γ ≈ 0.945.
2. **Calm regime (2026-06-20):** forecast annualised vol = 38%. Target exposure = 0.40 / 0.38 = **1.05x**. Book runs ~1x long BTC perp.
3. **Vol shock (2026-06-28):** BTC drops 6% on a macro headline; GARCH ratchets next-day forecast to 72%. Target exposure = 0.40 / 0.72 = **0.56x**. Also, vol enters the top 1y decile → top-decile cap 0.50x binds → book cut to **0.50x**. Exposure roughly halved *before* the follow-through day.
4. **Follow-through (2026-06-29):** BTC falls another 5% (the clustered second move GARCH anticipated). The de-risked book loses ~2.5% instead of ~5%. Leveraged constant-notional longs are liquidated into it.
5. **Normalisation (2026-07-10):** vol decays toward the long-run mean; forecast back to 45%; exposure re-levers to 0.89x, buying back exposure at a lower price.

**Outcome:** across the episode the vol-scaled book gives up a little upside in calm periods but avoids the worst of the clustered drawdown and re-levers cheaper — the mechanical Sharpe improvement the strategy exists to capture.

## Performance characteristics

Realistic, cost-corrected expectations for the overlay applied to a long-BTC/ETH sleeve (2019-2026 backtest character; **naive-backtested** — see caveat):

| Metric | Vol-scaled book | Unscaled buy-and-hold | Note |
|---|---|---|---|
| Sharpe | ~0.9 | ~0.6 | +0.2-0.4 improvement is the edge. |
| Max drawdown | ~25% | ~55-75% | Roughly halved; the headline benefit. |
| Annual turnover | 4-8x | ~0 | Source of rebalance cost. |
| Rebalance cost drag | ~10-25 bps/yr | 0 | Daily perp rebalances at ~5 bps taker, damped by the 15% band. |
| Breakeven cost budget | ~15 bps per rebalance | — | Comfortably met on liquid majors. |

**Cost overlay:** the only material cost is rebalance turnover. With a 15% no-trade band, BTC/ETH perp rebalances run ~5 bps taker (or a maker rebate if worked), and turnover of 4-8x/yr implies ~10-25 bps annual drag — small relative to the Sharpe gain. The strategy is *cheap* precisely because it trades the most liquid instruments infrequently.

**Honesty caveat:** the improvement numbers come from historical simulation, not a deflated, walk-forward, cost-corrected production record — hence `naive-backtested`. The vol-clustering effect is robust, but the *magnitude* of Sharpe uplift is regime-dependent and is exactly the thing crowding erodes. Validate with [[deflated-sharpe-ratio]] before trusting a specific number.

## Capacity limits

Because the overlay trades only the most liquid instruments (BTC/ETH perps and spot) infrequently, capacity is **high** — on the order of **$100M-$1B+** before rebalance market impact matters, far above any single-name crypto strategy. The binding constraint is the capacity of the *underlying* book it overlays (a trend or carry sleeve), not the vol-timing itself. On smaller-cap perps capacity drops sharply and the jump component of vol grows, degrading the forecast.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Jump risk / tail realised (Failure Mode #6).** GARCH models *diffusive* vol. Overnight gaps (exchange hack, stablecoin depeg, 2025-10-10 cascade) are discontinuities it cannot forecast; the scaled position can still be caught full-size into a gap that no conditional-variance model saw.
2. **Regime change / asymmetry flip (Failure Mode #5).** Crypto's leverage-effect sign is unstable. A GJR/EGARCH fit with a stale asymmetry sign mis-scales at exactly the regime turn. Continuous re-estimation is mandatory.
3. **Model misspecification / overfitting (Failure Mode #2).** The GARCH family has dozens of variants; cherry-picking the best in-sample specification invites overfit. Multi-step forecasts degrade fast. Integrated fits (α+β→1) are degenerate.
4. **Crowding (Failure Mode #4).** Vol-targeting is now industry-standard among crypto funds; when everyone de-risks on the same vol spike, the mechanical selling amplifies the very drawdown the model tries to avoid (a vol-targeting feedback loop, as seen in the 2018 equity "Volmageddon" analogue).
5. **Estimation-window sensitivity.** Too short a window chases noise; too long carries stale regimes. There is no window that is right in all regimes.
6. **Funding drag.** Constantly holding/rolling perp exposure incurs [[funding-rate|funding]]; in high-funding regimes this can erode the modest Sharpe uplift if not netted out.

## Kill criteria

Pause and re-validate the model on any of:

1. **Forecast underperforms EWMA baseline** on out-of-sample QLIKE/MSE for 90 consecutive days.
2. **Vol-scaled Sharpe (rolling 6-month) < unscaled benchmark** it overlays — the overlay is subtracting value.
3. **Persistence α+β > 0.999** (integrated/degenerate fit) — model is unstable; revert to EWMA until re-fit.
4. **Realised vol pierces the 99% GARCH band repeatedly** — a jump/fat-tail regime the model structurally cannot see.

See [[when-to-retire-a-strategy]]. GARCH timing is pausable, not retirable — vol clustering does not disappear; only the current specification's edge degrades.

## Advantages

- **Improves Sharpe and roughly halves drawdown** on any underlying book, cheaply.
- **Exploits the most robust regularity in markets** (vol clustering) rather than a fragile return anomaly.
- **Forward-looking** unlike backward-looking [[atr]]/[[historical-volatility]] stops.
- **High capacity, low turnover** — trades only liquid majors, infrequently.
- **Composable** — works as an overlay on trend, carry, or long-only crypto exposure.
- **Well-tooled** — robust MLE estimation in Python `arch` / R `rugarch`.

## Disadvantages

- **Not a standalone alpha** — it shapes risk, it does not predict direction; return depends on the underlying book.
- **Blind to jumps** — the largest crypto losses are discontinuities GARCH cannot forecast.
- **Parametric tail underestimation** — Gaussian/Student-t innovations understate true crypto tails; use skew-t and jump overlays.
- **Specification and window risk** — overfitting and stale regimes are live failure modes.
- **Crowding feedback** — synchronized vol-targeting can amplify drawdowns.
- **Modest, regime-dependent uplift** — the Sharpe gain is real but small and shrinking; easy to over-trust from a benign backtest.

## Sources

- Bollerslev, T. (1986), *Generalized Autoregressive Conditional Heteroskedasticity*, Journal of Econometrics — the GARCH(1,1) model. Engle, R. (1982) — the ARCH precursor.
- Glosten, Jagannathan, Runkle (1993) and Nelson (1991, EGARCH) — the asymmetric extensions; the asymmetry sign is what flips in crypto.
- Moreira, A. & Muir, T. (2017), *Volatility-Managed Portfolios*, Journal of Finance — establishes that scaling exposure inversely to volatility improves Sharpe; the structural basis for the timing edge.
- Katsiampa, P. (2017) and subsequent crypto-GARCH literature — document strong vol persistence and specification sensitivity for BTC; several papers report an inverse/positive leverage effect for Bitcoin, unlike equities.
- Deribit/CoinMetrics realised-vs-implied vol studies — context for combining GARCH forecasts with the options [[variance-risk-premium|VRP]] (see [[skew-trading]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed/expanding/vol_shock/mean_reverting/normal); independent cross-check on the GARCH state
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — latest price for the live return
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding carry overlay on perp exposure

**Historical data (GARCH estimation + backtest):**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — daily OHLCV for daily-model fitting
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — hourly bars for the intraday model
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC history + 200D MA
- `GET /api/v1/volatility/regime/BTC` — per-asset vol-regime detail + 60d history
- `GET /api/v1/backtesting/klines` — deep OHLCV archive (from 2020) for full walk-forward

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-regimes]], [[cryptodataapi-backtesting]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this overlay end-to-end:

- **Compute** — fit the weekly GJR-GARCH on `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` and the intraday model on `interval=1h`; `GET /api/v1/market-data/ticker/price` supplies the live return for the daily forecast step
- **Regime gate** — `GET /api/v1/volatility/regime` as the independent cross-check: if the classifier reads `vol_shock` while the GARCH forecast is still calm, trust the classifier and apply the top-decile leverage cap (jumps are exactly what GARCH cannot see)
- **Carry overlay** — `GET /api/v1/derivatives/funding-rates?coin=BTC` to net funding against the vol-scaled perp exposure ([[funding-aware-position-sizing]])
- **Backtest** — `GET /api/v1/backtesting/klines` — Binance spot 1h/4h/1d back to 2017-08 spans multiple vol regimes for out-of-sample QLIKE validation against the EWMA baseline; pair exposure decisions with point-in-time regimes from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) rather than today's labels
- **Tips** — log persistence (α+β) at every refit and auto-revert to EWMA above 0.999; the 15% rebalance band means the agent should *decide* daily but *trade* only a few times a month

## Related

- [[volatility-clustering]] — the empirical fact GARCH formalises
- [[realized-volatility]], [[historical-volatility]] — the forecast target and the backward-looking baseline
- [[volatility-targeting]], [[position-sizing]], [[funding-aware-position-sizing]], [[atr-position-sizing]] — how the forecast is used
- [[regime-detection]], [[vol-regime-detection]], [[volatility-regime]] — complementary state classification
- [[leverage-effect]] — the asymmetry term (unstable sign in crypto)
- [[tail-risk-hedging]] — protection for the jumps GARCH cannot see
- [[maximum-drawdown]], [[kelly-criterion]] — risk framing and sizing
- [[perpetual-futures]], [[funding-rate]] — the exposure instrument and its carry
- [[skew-trading]], [[volatility-carry]] — compare GARCH forecast vs implied for a VRP trade
- [[deflated-sharpe-ratio]] — validate the Sharpe uplift before trusting it
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] — methodology
</content>
