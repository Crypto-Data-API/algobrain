---
title: "Regime Detection"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [regime-detection, hidden-markov-model, hmm, clustering, market-regimes, quantitative, adaptive-allocation, crypto]
aliases: ["Regime Switching", "Market Regime Detection", "HMM Trading", "Regime-Based Allocation"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [analytical, structural]
edge_mechanism: "Crypto returns are a mixture of persistent states (trend, chop, vol-shock); the overlay infers the current state and switches sub-strategies so you stop running mean-reversion into a trend or trend-following into chop — harvesting regime persistence and avoiding the strategy-regime mismatch that bleeds undisciplined books."
data_required: [ohlcv-1h, ohlcv-daily, funding-rates, open-interest, volatility-regime, liquidations]
min_capital_usd: 10000
capacity_usd: 100000000
crowding_risk: low
expected_sharpe: 0.7
expected_max_drawdown: 0.25
breakeven_cost_bps: 40
decay_evidence: "Regime detection is a lagging classifier: by the time an HMM confirms a new crypto regime with high posterior probability, the fast transition (which in crypto can be a 60-second liquidation cascade — 2025-10-10) is already over. Its value is in the persistent phases (multi-week bull/bear/chop), not the turns, and whipsaw in choppy transition zones can erase the benefit."
kill_criteria: |
  - overlay's realized Sharpe < the equal-weight blend of its sub-strategies over trailing 12 months
  - regime-switch turnover cost exceeds the drawdown reduction it buys (net negative)
  - drawdown > 25% (the overlay failed to detect the crisis regime in time)
  - regime label disagreement across models/horizons > 50% for a sustained period (unstable classification)
related: ["[[trend-following]]", "[[mean-reversion]]", "[[momentum]]", "[[volatility]]", "[[kalman-filter-trading]]", "[[market-regime]]", "[[liquidation-cascade-fade]]", "[[funding-rate-arbitrage]]", "[[risk-budgeting]]", "[[book-the-man-who-solved-the-market]]", "[[book-probabilistic-ml-for-finance]]", "[[cryptodataapi]]"]
---

# Regime Detection

Regime detection uses statistical models — primarily **Hidden Markov Models (HMMs)** and clustering — to infer the current market state and switch strategies accordingly. Crypto does not behave uniformly: it alternates between distinct **regimes** — low-vol trending, high-vol chop, squeeze/compression, and vol-shock/capitulation — and a strategy that thrives in one bleeds in another. A [[trend-following]] book that prints in a BTC bull impulse gets chopped to death in a range; a [[mean-reversion]] book that harvests a range gets run over the moment BTC breaks out. Regime detection is a **meta-strategy** — a strategy-of-strategies — that allocates capital to whichever sub-strategy fits the detected state. It is the on/off switch behind the regime gates referenced throughout this wiki's reversion and trend pages.

## Edge source

Per [[edge-taxonomy]], regime detection is primarily **analytical**, secondarily **structural**:

- **Analytical** — the edge is classification skill: modeling crypto returns as a mixture of states and inferring the current one faster and more stably than a naive "eyeball the chart" approach, then mapping each state to its best sub-strategy.
- **Structural** — regimes **persist** (crypto trends and ranges last weeks, not minutes); an HMM's transition matrix explicitly captures that persistence. The overlay harvests it by staying aligned with the dominant state rather than fighting it.

The overlay does not itself have a market counterparty — it is a risk-and-allocation layer. Its "edge" is negative: it removes the recurring drag of running the wrong sub-strategy, which is one of the most reliable ways undisciplined crypto books lose money.

## Why this edge exists

Crypto return distributions are genuinely **mixtures** — a bull impulse (positive drift, moderate vol), a range (zero drift, low vol), and a shock (large negative drift, extreme vol) are drawn from different distributions with different optimal strategies. Most participants apply one strategy across all of them and accept the mismatch, either from inertia or because they cannot tell which regime they are in until it is obvious (i.e., too late). The overlay's advantage is that regimes persist long enough that a probabilistic, slightly-lagging classifier still captures most of each phase. It works because the persistence is real (the structural component) and because most traders do not systematically switch (the behavioral gap it exploits indirectly). It is weakest precisely at the turns, where the lag bites — which is why it adds value on the multi-week phases, not the 60-second cascades.

## Null hypothesis

If crypto returns were i.i.d. (no persistent regimes — the transition matrix is uniform and every bar is drawn from the same distribution), regime detection would add nothing: switching sub-strategies would only incur turnover cost, and a static equal-weight blend of the sub-strategies would match or beat the overlay net of costs. The null is directly testable: fit an HMM and check whether the estimated transition matrix is significantly diagonal-dominant (regimes persist) and whether regime labels have out-of-sample predictive power for the *next* period's volatility and sign. On the null, the overlay's realized Sharpe ≤ the equal-weight blend after switching costs. A real edge requires persistent, predictive regimes and switching rules whose benefit exceeds their turnover cost.

## How it works

### Hidden Markov Models
An HMM assumes the market is in one of N hidden states, each with its own return distribution (Source: [[book-the-man-who-solved-the-market]]; [[book-probabilistic-ml-for-finance]]). It estimates:
- **Transition probabilities** — the chance of switching states (e.g., 95% stay in trend, 5% flip to chop).
- **Emission parameters** — each regime's return distribution (mean, variance).
- **Current-state posterior** — given recent observations, the probability of being in each regime.

Baum-Welch trains the model on history; the forward/Viterbi algorithm infers the current regime online.

### Clustering
An alternative uses **k-means** or **Gaussian mixture models** on feature vectors (rolling returns, realized vol, funding, OI change, liquidation intensity) to group periods into regimes. Simpler, but it loses the temporal transition structure HMMs capture.

CryptoDataAPI exposes a production version of exactly this: a 6-regime HMM engine (`strong_trend_bull`, `strong_trend_bear`, `range_low_vol`, `choppy_high_vol`, `vol_spike`, `squeeze`) with a 15-minute refresh, plus a 10-state long-horizon market-regime taxonomy — so the classification layer can be consumed directly rather than trained from scratch.

## Rules

1. **Define regimes.** 3–6 states. A workable crypto three-state model: (a) trend (positive/negative drift, moderate vol), (b) range/chop (zero drift, low-moderate vol), (c) vol-shock/crisis (large negative drift, extreme vol). Or consume the CDA 6-regime taxonomy directly.
2. **Train / source the classifier.** Train an HMM on 3–5 years of daily (and 1h) crypto returns with Gaussian emissions, or read live probabilities from `/api/v1/quant/market`.
3. **Infer the current regime** each period via the forward algorithm; take the highest-posterior state.
4. **Strategy mapping:**
   - **Trend regime →** deploy [[trend-following]] / [[momentum]]; raise directional exposure.
   - **Range/chop regime →** deploy [[mean-reversion]], [[pairs-trading]], [[bollinger-band-reversion]]; cut size.
   - **Vol-shock/crisis regime →** de-risk to stablecoins, hedge, or arm [[liquidation-cascade-fade]] for the snapback; stand down directional books.
5. **Switch with hysteresis.** Only rebalance when the new regime's posterior exceeds a threshold (e.g., > 70%) for ≥ 2 consecutive periods — this suppresses whipsaw in transition zones, the overlay's biggest cost.
6. **Retrain** quarterly on rolling/expanding windows to track evolving crypto microstructure.

## Implementation pseudocode

```python
# Crypto regime-switching allocation overlay
STATE_TO_BOOK = {
    "strong_trend_bull": "trend_following",
    "strong_trend_bear": "trend_following",   # short/defensive side
    "range_low_vol":     "mean_reversion",
    "choppy_high_vol":   "reduce_size",       # smaller mean-reversion, wider stops
    "squeeze":           "flat_await_break",  # compression precedes a move
    "vol_spike":         "derisk_or_fade",    # cash + arm liquidation-cascade-fade
}

def regime_overlay(prev_state, confirm_count):
    r = get_regime()                          # CDA /quant/market: label + posteriors
    new_state = r["label"]
    p         = r["prob"][new_state]

    # hysteresis: require >70% posterior for >=2 consecutive refreshes before switching
    if new_state != prev_state and p > 0.70:
        confirm_count += 1
        if confirm_count >= 2:
            allocate_to(STATE_TO_BOOK[new_state])
            return new_state, 0
    else:
        confirm_count = 0
    return prev_state, confirm_count
```

## Indicators / data used

- **Regime posteriors** from an HMM (or the CDA `/quant/market` engine) — the core signal.
- **Realized [[volatility]]** and the CDA vol-regime label — a primary emission feature and a fast crisis flag.
- **[[funding-rate]]** and **[[open-interest]]** — positioning features that lead regime turns (crowded longs precede vol-shocks).
- **[[liquidation]] intensity** — the fingerprint of a vol-shock/capitulation regime.
- **[[market-regime]]** long-horizon state (CDA 10-state taxonomy) — the slow backdrop the fast HMM sits inside.
- 3–5 years of daily + 1h OHLCV for training; point-in-time regime history for leak-free backtests.

## Example trade

**Market:** BTC-centric book, three-regime overlay (trend / range / shock), consuming the CDA HMM.
1. Through a calm stretch the model assigns ~90% to `range_low_vol`. The overlay runs [[mean-reversion]] and [[pairs-trading]] at moderate size; directional exposure is low.
2. BTC breaks a multi-week range on rising OI and funding; `strong_trend_bull` posterior climbs to 78% and holds two refreshes. The overlay switches to [[trend-following]] and raises directional exposure — and, crucially, *turns off* the mean-reversion book that would otherwise short the breakout.
3. Weeks later a macro shock (tariff headline) triggers a liquidation cascade; `vol_spike` hits 85%. The overlay de-risks directional books to stablecoins and arms [[liquidation-cascade-fade]] for the snapback rather than holding trend longs into the flush.
4. The shock fades; `range_low_vol` re-confirms > 70% for two refreshes and the overlay rotates back to reversion.
5. **Result:** the regime-aware book sidesteps the worst of the cascade drawdown and avoids fading the breakout — the two most common ways a single-strategy crypto book bleeds. It gives back some edge at each turn to lag (the cost of confirmation).

## Performance characteristics

Regime detection is an **overlay**, so its performance is measured against the counterfactual of running its sub-strategies statically:

- **Value delivered:** primarily **drawdown reduction** and avoidance of strategy-regime mismatch, not raw return. A well-tuned overlay can lift a multi-strategy book's net Sharpe by ~0.1–0.3 and cut max drawdown by a third to a half versus a static blend — *if* switching costs are contained.
- **Realistic net Sharpe of the blended, regime-switched book:** ~0.6–0.9 (frontmatter assumes 0.7), dominated by the quality of the underlying sub-strategies.
- **The cost is turnover.** Every switch rebalances real positions; whipsaw in transition zones is the killer.

**Cost overlay (the switching cost, not per-trade):**

| Component | Magnitude | Note |
|---|---|---|
| Rebalance cost per switch | ~10–30 bps of the reallocated notional | Liquidating one book and building another |
| Switches per year | ~6–15 with hysteresis; 30+ without | Hysteresis (>70%, 2-period confirm) is the primary cost control |
| Whipsaw drag | The dominant hidden cost | Two switches that reverse within days pay cost for nothing |
| Lag cost | Give-back at each turn | The classifier confirms after the fast move |
| **Breakeven (frontmatter)** | **~40 bps** | The drawdown-reduction benefit must exceed switching + whipsaw cost |

The overlay only earns its keep when the persistent-phase benefit exceeds the transition-zone cost — which is why the confirmation threshold and switch frequency are the parameters that matter most.

## Capacity limits

High — this is an allocation layer, not a direct-flow strategy, so it does not consume order-book depth itself; its capacity is the **minimum** capacity of the sub-strategies it switches between. Frontmatter assumes **$100M** as a nominal ceiling, but in practice a regime overlay feeding a [[mean-reversion]] or [[pairs-trading]] sleeve is capped by *those* strategies' capacity (see their pages), while an overlay feeding a large [[trend-following]] book scales much further. Crowding risk is **low**: the overlay is a private risk decision, and even if many funds detect the same regime, that mostly reinforces the persistence the strategy relies on.

## What kills this strategy

- **Lag at the turns.** Regime detection is inherently lagging — by the time the model confirms a new regime, the fast transition is over. In crypto the transition can be a 60-second cascade (2025-10-10); the overlay cannot react in time and instead manages the *aftermath*. This is the dominant limitation.
- **Whipsaw.** Rapid regime flips in transition zones produce frequent switches, and the turnover cost can erase the benefit. Insufficient hysteresis is the usual cause.
- **Overfitting.** HMMs with too many states or features fit noise and fail out-of-sample (Source: [[book-the-man-who-solved-the-market]]). Choosing N is unavoidably judgmental (BIC/AIC help, but do not settle it).
- **Model disagreement.** Different models/horizons disagree on the current regime; acting on an unstable label is worse than not switching.
- **Novel regimes.** The assumption that future regimes resemble historical ones fails on genuinely new events (a first-of-its-kind depeg, a new market structure). The model has no state for what it has never seen.

## Kill criteria

- The overlay's realized Sharpe < the equal-weight static blend of its sub-strategies over the trailing 12 months (it is subtracting value).
- Regime-switch turnover cost exceeds the drawdown reduction it buys (net negative).
- Drawdown > 25% — the overlay failed to detect the crisis regime in time.
- Regime-label disagreement across models/horizons > 50% for a sustained period (unstable classification) → widen hysteresis or stand the overlay down.

See [[when-to-retire-a-strategy]].

## Advantages

- **Adaptive:** aligns strategy selection with the current crypto regime instead of forcing one approach across all states.
- Principled, probabilistic framework for the intuitive "different markets need different strategies."
- **Cuts drawdown** by detecting vol-shock regimes and de-risking / arming the fade rather than holding into the flush.
- HMMs capture regime persistence (the structural component) via transition probabilities.
- Combines naturally with [[risk-budgeting]] and [[volatility]] targeting for regime-conditional sizing.
- Academically grounded (Hamilton 1989; Ang & Bekaert 2002) and available as a live CDA data product.

## Disadvantages

- **Lagging** — confirms new regimes after the fast move, especially painful given crypto's second-scale cascades.
- **Overfitting risk** — too many states/features fit noise; N must be chosen a priori.
- **Whipsaw** — rapid switches raise turnover cost and can destroy the benefit.
- **Model-dependent** — different models disagree on the current regime.
- **Data- and compute-intensive** to train from scratch; non-trivial to implement well.
- Fails on **novel** market events with no historical analog.

## Sources

- [[book-the-man-who-solved-the-market]] — Renaissance's use of HMMs and signal processing for regime detection, from the team's speech-recognition and codebreaking backgrounds.
- [[book-probabilistic-ml-for-finance]] — Tatsat et al. (2023): detailed HMM implementations for regime detection in Python (Baum-Welch, Viterbi, Gaussian-mixture emissions) for financial time series.
- Hamilton, J. D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." *Econometrica* — the foundational regime-switching model.
- Ang, A. & Bekaert, G. (2002). "International Asset Allocation with Regime Shifts." *Review of Financial Studies*.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh) — the core signal
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100), the fast crisis flag
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday) for training
- `GET /api/v1/quant/history` — point-in-time probability records for leak-free backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/market"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this meta-strategy end-to-end — consuming the production 6-state HMM instead of training one:

- **Signal** — `GET /api/v1/quant/market` every 15-minute refresh for the label + posterior probabilities; map states to sub-strategy books per the STATE_TO_BOOK table and only switch after the >70% posterior holds for ≥2 consecutive refreshes (the hysteresis rule is the cost control)
- **Fast crisis flags** — `GET /api/v1/volatility/regime/score` and `GET /api/v1/liquidity/regime/score` corroborate a `vol_spike` read before the overlay de-risks real positions
- **Backtest** — `GET /api/v1/quant/regimes/history` — hourly 6-state HMM probabilities since 2020 (Parquet, Pro Plus) — is the core training/validation set; `GET /api/v1/quant/timeline` adds daily labels back to 2019, and `GET /api/v1/quant/history` supplies point-in-time records so switching backtests never see tomorrow's posterior
- **Model transparency** — `GET /api/v1/quant/model` (version, metrics, sha256) lets the agent detect model updates and re-validate its state-to-book mapping before trusting a new engine version
- **Tips** — measure the overlay against the equal-weight static blend of its sub-strategies (the null); if switch turnover cost exceeds the drawdown reduction over a rolling window, widen the hysteresis before killing the overlay
- **Prompt library** — the "Market Regime Detection" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) translates the six-state HMM probabilities into a risk posture; use it as the interpretation layer over /api/v1/quant/market

## Related

- [[trend-following]] — the strategy deployed in detected trending regimes
- [[mean-reversion]] — the strategy deployed in detected ranging regimes
- [[momentum]] — trend-regime directional book
- [[liquidation-cascade-fade]] — the vol-shock-regime snapback play
- [[funding-rate-arbitrage]] — a regime-agnostic sleeve to hold when directional books stand down
- [[volatility]] — the fast crisis flag and a core emission feature
- [[kalman-filter-trading]] — adaptive estimation that pairs with regime switching
- [[market-regime]] — the long-horizon state taxonomy
- [[risk-budgeting]] — regime-conditional risk allocation framework
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
