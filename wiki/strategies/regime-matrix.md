---
title: "Strategy Regime Matrix"
type: index
created: 2026-04-10
updated: 2026-07-19
status: excellent
tags: [strategies, regime, regime-detection, portfolio-construction]
aliases: ["Regime Map", "Strategy-Regime Mapping"]
related: ["[[market-regime]]", "[[regime-detection]]", "[[regime-adaptive-strategy]]", "[[multi-strategy-portfolio]]", "[[strategy-correlation-matrix]]", "[[crypto-market-regime-taxonomy]]", "[[long-vol-vs-short-vol]]", "[[long-volatility-strategies]]", "[[short-volatility-strategies]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[cryptodataapi]]"]
---

# Strategy Regime Matrix

A master table mapping every strategy in this wiki to the market regime in which it works best (and worst). Used for portfolio construction: a robust multi-strategy book combines strategies whose strong regimes are *complementary*, so that some component is always carrying the load while others are in their natural drawdown.

> For the **crypto-specific, perps-native** regime states (the 14-basket framework: macro trend, BTC cycle, derivatives-native, liquidity/depth, basis, on-chain, institutional flow, etc.), see [[crypto-market-regime-taxonomy]]. This matrix's six generic dimensions are orthogonal to and composable with those baskets.

## How to Read the Matrix

Each strategy is rated on six regime dimensions. Ratings are qualitative — "this strategy was historically best in this regime" — not point estimates of expected Sharpe.

| Symbol | Meaning |
|---|---|
| ✅ | Strong positive regime — strategy historically thrives here |
| ➕ | Positive regime — strategy typically profits but not at peak |
| ⬜ | Neutral — strategy is roughly indifferent |
| ➖ | Negative regime — strategy typically struggles |
| ❌ | Strong negative regime — strategy historically loses heavily |

The six regimes:

1. **Trending Up** — sustained directional uptrend, e.g., 2017 crypto bull, 2020-2021 stocks
2. **Trending Down** — sustained downtrend, e.g., 2022 stocks, 2018 crypto
3. **Sideways / Chop** — range-bound, no directional bias, e.g., 2015 stocks, 2019-2020 EU
4. **High Volatility** — VIX > 25, large daily moves, e.g., March 2020, 2008 H2
5. **Low Volatility** — VIX < 15, calm markets, e.g., 2017 stocks, 2024 mid-year
6. **Risk-Off / Flight to Quality** — credit spreads widening, dollar bid, gold bid

> The six dimensions are **not mutually exclusive**: a real tape is a *vector* across them (e.g., "trending up + low vol" describes 2017; "trending down + high vol + risk-off" describes 2022 H1 and March 2020). Read the matrix by intersecting the columns that describe today's tape, not by picking a single regime.

### Mapping Regimes to Observable Signals

The matrix is only actionable if you can *classify* the current regime. The signals below are the practical inputs feeding [[regime-detection]] and any [[regime-adaptive-strategy|regime-adaptive overlay]]:

| Regime | Primary signal | Confirming signals | Caveat |
|---|---|---|---|
| **Trending up/down** | [[adx]] > 25; price above/below 200-day [[moving-average]] | [[macd]] sign, higher-highs/lower-lows structure, [[donchian-channel-breakout\|Donchian]] expansion | ADX is lagging; whipsaws at 20–25 |
| **Sideways / chop** | ADX < 20; flat 200-day slope | [[bollinger-band-width]] contraction, low realized vol | "Quiet before the storm" — chop precedes breakouts |
| **High volatility** | [[vix]] > 25 (equities); realized vol > implied baseline | [[atr]] expansion, widening [[bid-ask-spread]], rising correlations | Vol clusters — high begets high |
| **Low volatility** | VIX < 15; compressed ATR | Tight ranges, suppressed funding/skew | Suppressed vol masks building tail risk |
| **Risk-off / flight to quality** | Credit spreads (HY OAS) widening; dollar ([[dxy]]) bid; gold bid | Cross-asset correlations → 1; Treasuries rally; equity-bond correlation flips | Can arrive in a single gap with no warning |

> A robust classifier blends several signals; any single indicator (ADX alone, VIX alone) produces frequent false regime calls. See [[regime-detection]] for the methodology and [[market-regime]] for the conceptual frame.

### The Long-Vol / Short-Vol Master Axis

The deepest organizing principle of this matrix is that *almost every strategy is implicitly long or short volatility* (see [[long-vol-vs-short-vol]]):

- **Long-vol-like** strategies (trend following, breakout, contrarian-extremes, long straddles, [[tail-risk-hedging]]) make money during regime *shifts* — which are usually high-vol — and bleed in calm chop. They have **positive skew**: many small losses, occasional large wins.
- **Short-vol-like** strategies (mean reversion, carry, premium selling, grid, most DeFi yield) collect a steady premium in calm regimes and pay catastrophically when vol spikes. They have **negative skew**: many small wins, occasional ruinous losses.

Reading the matrix through this lens: the cleanest portfolio diversification combines a [[short-volatility-strategies\|short-vol core]] (carry, MR, premium selling) with a [[long-volatility-strategies\|long-vol overlay]] (trend, tail hedge), because their regime profiles are near mirror images. This is the single most important structural insight the matrix encodes — see [[trend-plus-tail-hedge]] and [[long-vol-vs-short-vol#The Synthesis: Short-Vol Core + Long-Vol Overlay]].

## The Matrix

### Trend Following

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[moving-average-crossover]] | ✅ | ✅ | ❌ | ➕ | ⬜ | ➕ |
| [[turtle-trading]] | ✅ | ✅ | ❌ | ✅ | ➖ | ✅ |
| [[trend-following-cta]] | ✅ | ✅ | ❌ | ✅ | ➖ | ✅ |
| [[supertrend]] | ✅ | ✅ | ❌ | ➕ | ⬜ | ➕ |
| [[ichimoku-cloud]] | ✅ | ➕ | ➖ | ⬜ | ⬜ | ⬜ |
| [[parabolic-sar]] | ✅ | ➕ | ❌ | ➖ | ➕ | ⬜ |
| [[donchian-channel-breakout]] | ✅ | ➕ | ❌ | ✅ | ⬜ | ➕ |
| [[macd-crossover]] | ➕ | ➕ | ❌ | ⬜ | ⬜ | ⬜ |

**Pattern:** trend strategies need *direction*. They lose in chop regardless of whether vol is high or low. They have the unusual property of being approximately *long volatility* — they make money during regime shifts (which are usually high-vol).

### Mean Reversion

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[mean-reversion]] | ⬜ | ⬜ | ✅ | ➖ | ✅ | ➖ |
| [[bollinger-band-reversion]] | ⬜ | ⬜ | ✅ | ⬜ | ✅ | ➖ |
| [[rsi-mean-reversion]] | ➕ | ➕ | ✅ | ➖ | ✅ | ❌ |
| [[pairs-trading]] | ⬜ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[statistical-arbitrage]] | ⬜ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[ornstein-uhlenbeck]] | ⬜ | ⬜ | ✅ | ➖ | ✅ | ➖ |
| [[contrarian-extremes]] | ➕ | ➕ | ⬜ | ✅ | ⬜ | ✅ |
| [[grid-trading]] | ➖ | ➖ | ✅ | ❌ | ✅ | ❌ |
| [[liquidation-cascade-fade]] | ➕ | ⬜ | ⬜ | ✅ | ➖ | ✅ |

**Pattern:** mean-reversion strategies are *short volatility*. They thrive in calm, range-bound markets and break when correlations spike (e.g., quant meltdown 2007). The exception is contrarian-extremes, which is explicitly designed to fade panic and benefits from high vol.

### Momentum / Breakout

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[breakout-strategies]] | ✅ | ✅ | ❌ | ✅ | ➖ | ➕ |
| [[opening-range-breakout]] | ✅ | ✅ | ❌ | ✅ | ➖ | ➕ |
| [[london-breakout]] | ✅ | ✅ | ❌ | ➕ | ➖ | ➕ |
| [[channel-breakout]] | ✅ | ➕ | ❌ | ➕ | ⬜ | ⬜ |
| [[volatility-breakout]] | ✅ | ✅ | ❌ | ✅ | ❌ | ➕ |
| [[momentum-rotation]] | ✅ | ➖ | ➖ | ⬜ | ➕ | ➖ |
| earnings-momentum | ✅ | ⬜ | ⬜ | ⬜ | ➕ | ➖ |
| sector-momentum-screen | ✅ | ➖ | ➖ | ⬜ | ✅ | ❌ |

**Pattern:** breakouts need direction *and* sufficient vol to push through resistance. Cross-sectional momentum (momentum rotation) is asymmetric — it works in up markets but fails in down markets because the "best" stocks become correlated with the broad decline.

### Carry / Yield

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[carry-trade]] | ✅ | ➖ | ✅ | ❌ | ✅ | ❌ |
| [[funding-rate-arbitrage]] | ✅ | ➕ | ✅ | ❌ | ✅ | ➖ |
| [[basis-trading]] | ✅ | ⬜ | ✅ | ❌ | ✅ | ➖ |
| [[stock-perp-oracle-basis]] | ⬜ | ⬜ | ✅ | ➖ | ✅ | ➖ |
| dividend-capture | ➕ | ⬜ | ✅ | ➖ | ✅ | ⬜ |
| [[covered-call]] | ➕ | ❌ | ✅ | ❌ | ✅ | ➖ |
| [[cash-secured-put]] | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |
| [[wheel-strategy]] | ➕ | ➖ | ✅ | ❌ | ✅ | ❌ |

**Pattern:** carry strategies are *short tail risk* — they collect small premiums in normal times and pay catastrophic losses in crises. Always combine with a tail hedge (see [[trend-plus-tail-hedge]]).

### Arbitrage

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| index-arbitrage | ⬜ | ⬜ | ⬜ | ✅ | ➕ | ⬜ |
| [[etf-arbitrage]] | ⬜ | ⬜ | ⬜ | ✅ | ⬜ | ⬜ |
| merger-arbitrage | ✅ | ➖ | ✅ | ❌ | ✅ | ❌ |
| convertible-arbitrage | ✅ | ➖ | ✅ | ➖ | ✅ | ❌ |
| [[triangular-arbitrage]] | ⬜ | ⬜ | ⬜ | ✅ | ➖ | ⬜ |
| [[cross-exchange-arbitrage]] | ⬜ | ⬜ | ⬜ | ✅ | ➖ | ⬜ |
| [[latency-arbitrage]] | ⬜ | ⬜ | ⬜ | ✅ | ➖ | ➕ |
| [[flash-loan-arbitrage]] | ⬜ | ⬜ | ⬜ | ✅ | ➖ | ⬜ |
| [[funding-rate-arbitrage]] | ✅ | ➕ | ✅ | ❌ | ✅ | ➖ |

**Pattern:** structural arbitrage is mostly regime-neutral but benefits from high volatility (more dislocations to capture). Risk arbitrage (merger arb, convert arb) breaks in risk-off regimes when deals collapse.

### Volatility / Options

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[short-strangle]] | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| [[short-straddle]] | ⬜ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[iron-condor]] | ⬜ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[iron-butterfly]] | ⬜ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[long-straddle]] | ⬜ | ⬜ | ❌ | ✅ | ❌ | ✅ |
| [[straddle-strangle]] | ⬜ | ⬜ | ❌ | ✅ | ❌ | ✅ |
| [[gamma-scalping]] | ⬜ | ⬜ | ➕ | ✅ | ❌ | ✅ |
| [[volatility-arbitrage]] | ⬜ | ⬜ | ⬜ | ➕ | ➕ | ➖ |
| [[volatility-targeting]] | ✅ | ⬜ | ⬜ | ⬜ | ✅ | ⬜ |
| [[tail-risk-hedging]] | ➖ | ➖ | ❌ | ✅ | ❌ | ✅ |
| [[vix-trading]] | ⬜ | ⬜ | ⬜ | ✅ | ⬜ | ✅ |

**Pattern:** the entire vol space splits cleanly into vol sellers (love calm chop, die in spikes) and vol buyers (love spikes and sustained high-vol regimes, bleed in calm). Combining the two via [[trend-plus-tail-hedge]] or [[regime-adaptive-strategy]] is one of the strongest portfolio constructions.

### Value / Fundamental

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| value-investing-strategy | ✅ | ➕ | ✅ | ➕ | ✅ | ➕ |
| growth-investing-strategy | ✅ | ❌ | ⬜ | ➖ | ✅ | ❌ |
| long-short-equity | ⬜ | ⬜ | ✅ | ⬜ | ✅ | ⬜ |
| [[event-driven-trading]] | ➕ | ➕ | ✅ | ⬜ | ⬜ | ➖ |
| [[news-trading]] | ⬜ | ⬜ | ⬜ | ✅ | ➖ | ➕ |
| earnings-momentum | ✅ | ⬜ | ⬜ | ⬜ | ➕ | ➖ |
| [[sector-rotation]] | ✅ | ➖ | ➕ | ⬜ | ✅ | ➖ |
| [[fundamental-technical-fusion]] | ✅ | ⬜ | ➕ | ⬜ | ✅ | ⬜ |

**Pattern:** value vs. growth is a regime story. Growth crushes in low-vol up trends (2017-2021 mega-cap tech). Value crushes in inflationary, rising-rate regimes (2022). Long-short equity is roughly neutral but benefits from dispersion.

### DeFi / Crypto-Native

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[defi-yield-farming]] | ✅ | ➖ | ✅ | ➖ | ✅ | ❌ |
| [[concentrated-liquidity]] | ⬜ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[delta-neutral-yield-farming]] | ⬜ | ⬜ | ✅ | ➖ | ✅ | ➖ |
| [[basis-trading]] | ✅ | ⬜ | ✅ | ❌ | ✅ | ❌ |
| [[airdrop-farming]] | ✅ | ➖ | ⬜ | ⬜ | ✅ | ❌ |
| [[restaking-strategies]] | ✅ | ➖ | ✅ | ❌ | ✅ | ❌ |
| [[memecoin-sniping]] | ✅ | ❌ | ➖ | ✅ | ❌ | ❌ |
| [[mev-strategies]] | ⬜ | ⬜ | ✅ | ✅ | ➖ | ⬜ |

**Pattern:** crypto strategies cluster heavily in the "long, low-vol, calm" regime. Almost the entire DeFi ecosystem dies in risk-off events. Diversifying within crypto requires combining DeFi yield with explicit short or long-vol positions.

### Macro / Cross-Asset

| Strategy | Up | Down | Chop | High Vol | Low Vol | Risk-Off |
|---|---|---|---|---|---|---|
| [[risk-on-risk-off-framework]] | ✅ | ✅ | ➖ | ✅ | ⬜ | ✅ |
| [[cross-asset-signals]] | ✅ | ✅ | ⬜ | ✅ | ⬜ | ✅ |
| [[regime-adaptive-strategy]] | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [[risk-budgeting]] | ⬜ | ⬜ | ➕ | ⬜ | ✅ | ⬜ |
| [[risk-parity]] | ➕ | ➖ | ✅ | ❌ | ✅ | ❌ |
| [[yield-curve-trading]] | ➕ | ➕ | ⬜ | ⬜ | ⬜ | ✅ |
| [[carry-trade]] | ✅ | ➖ | ✅ | ❌ | ✅ | ❌ |

**Pattern:** explicitly regime-adaptive strategies (regime-detection-driven) are designed to be robust across all six regimes by switching their exposure. They underperform pure single-regime strategies in *that* regime but are far less vulnerable to regime shifts.

## Diversification Implications

A well-constructed multi-strategy book should hold strategies whose regime profiles *complement* each other. Examples:

### Portfolio A: Trend + Carry + Tail Hedge
- [[trend-following-cta]] — wins in trending regimes (up or down)
- [[carry-trade]] — wins in calm range-bound regimes
- [[tail-risk-hedging]] — wins in high-vol risk-off regimes

The three together cover all six regimes. Each strategy in isolation has long stretches of underperformance; the combination has much shorter ones.

### Portfolio B: Mean Reversion + Trend + Macro
- [[pairs-trading]] — wins in calm chop
- [[turtle-trading]] — wins in trending high-vol
- [[risk-on-risk-off-framework]] — wins in regime transitions

Three relatively uncorrelated strategies that depend on different market features.

### Portfolio C: Crypto-Specific
- [[funding-rate-arbitrage]] — wins in calm bull
- [[basis-trading]] — wins in calm bull
- [[straddle-strangle]] (long vol on BTC) — wins in spikes

Limited diversification because most crypto strategies cluster in the same regime. Adding equity-side hedges or moving outside crypto entirely is usually necessary for true diversification.

### Portfolio D: Live Bot Six-Strategy Stack (the deployed production system)

The six strategies in the production live bot are deliberately spread across regime profiles to allow regime-aware on/off toggling rather than continuous deployment of all six:

| Regime | Strategies that thrive |
|---|---|
| **Trending up** | [[moving-average-crossover]] (long), [[funding-rate-arbitrage]], [[stock-perp-oracle-basis]] |
| **Trending down** | [[moving-average-crossover]] (short), [[liquidation-cascade-fade]] (after capitulation) |
| **Sideways / chop** | [[grid-trading]], [[funding-rate-arbitrage]], [[rsi-mean-reversion]], [[stock-perp-oracle-basis]] |
| **High vol / risk-off** | [[liquidation-cascade-fade]] |
| **Low vol** | [[grid-trading]], [[funding-rate-arbitrage]], [[rsi-mean-reversion]], [[stock-perp-oracle-basis]] |

The cleanest regime-inverse pair in the stack is `[[grid-trading]]` (ADX < 20 required) vs. `[[moving-average-crossover]]` (needs ADX > 25 or sustained trend) — they should never be ON simultaneously across the same universe. The bot can use `[[adx]]` as a single-signal toggle: `ADX < 20 → grid ON, trend OFF`; `ADX > 25 → trend ON, grid OFF`; `20 ≤ ADX ≤ 25 → both OFF, rely on carry/MR strategies`.

`[[liquidation-cascade-fade]]` is the one strategy that *wants* the high-vol risk-off regime that bleeds the other five — making it a structural diversifier when paired with the carry-heavy core. Its low base rate (rare events) means it sits idle most of the time but provides convex returns when crisis hits.

## Regime Transitions Are Where Money Is Made and Lost

A static regime map understates the real risk: **the danger is not being in the wrong regime, it is being caught on the wrong side of a regime *transition*.** Most catastrophic strategy losses occur in the days around a regime shift, not deep inside a stable regime.

| Transition | What happens | Who gets hurt | Who benefits |
|---|---|---|---|
| **Low vol → high vol** (vol spike) | Realized vol gaps; correlations → 1 | Short-vol sellers, carry, MR, grid | [[tail-risk-hedging]], long straddles, [[trend-following-cta]] |
| **Chop → trend** (breakout) | Range resolves directionally | [[mean-reversion]], [[grid-trading]], range-faders | [[breakout-strategies]], [[donchian-channel-breakout]], trend |
| **Trend → chop** (exhaustion) | Direction stalls, whipsaws begin | Trend followers, momentum | [[mean-reversion]], [[pairs-trading]], premium sellers |
| **Risk-on → risk-off** (flight to quality) | Credit widens, dollar/gold bid, leverage unwinds | Carry, growth, DeFi yield, risk parity | [[risk-on-risk-off-framework]], tail hedges, gold/Treasuries |
| **High vol → low vol** (vol crush) | IV collapses post-shock | Long-vol holders (overlay bleeds again) | Short-vol re-entry, [[gamma-scalping]] sellers |

**Implication for construction:** strategies that *thrive* on transitions ([[trend-following-cta]], [[tail-risk-hedging]], [[liquidation-cascade-fade]], [[contrarian-extremes]]) are the natural insurance against strategies that *die* on transitions (carry, MR, grid, premium selling). A book that holds only one class is fragile to exactly one transition type. See [[failure-modes]] for the mechanics of transition-driven blowups.

## Decision Framework: Using the Matrix in Practice

1. **Classify the current regime vector** using the [[#Mapping Regimes to Observable Signals|signals table]] — produce a reading across all six dimensions, not a single label.
2. **Read down the matrix columns** that describe today's tape; favor strategies marked ✅/➕ in those columns, throttle or disable strategies marked ➖/❌.
3. **Check the transition risk** — if a [[regime-detection|regime-detection]] signal is near a threshold (e.g., ADX 20–25, VIX 18–22), treat the regime as *transitional* and reduce gross on regime-sensitive strategies; transitional zones are where both trend and MR books underperform simultaneously.
4. **Never run a regime-inverse pair simultaneously on the same universe** — e.g., [[grid-trading]] (needs chop) and [[moving-average-crossover]] (needs trend) should be toggled by a single [[adx]] gate, not both ON.
5. **Confirm complementarity** of the active book against the [[strategy-correlation-matrix]] — regime-complementary strategies should also be return-uncorrelated; if they are correlated in practice, the diversification is illusory.
6. **Size for the transition, not the regime** — position sizing should assume the regime can flip; a [[volatility-targeting]] or [[risk-budgeting]] overlay shrinks exposure as vol rises, dampening transition damage automatically.

## How This Was Constructed

These ratings come from a mix of:

1. **Theoretical regime structure** — what *should* happen given the strategy's economic mechanism
2. **Historical backtests** in this wiki (where available)
3. **Academic literature** on each strategy class
4. **Practitioner experience** as documented in the wiki's source library

They are *not* precise. Two researchers would produce slightly different matrices. Treat them as a *starting point* for portfolio construction, not a literal allocation rule.

## Common Misuses of the Matrix

| Misuse | Why it's wrong | Better practice |
|---|---|---|
| Treating ratings as expected-Sharpe point estimates | Ratings are ordinal and qualitative; the gap between ✅ and ➕ is not calibrated | Use ratings to *rank* and *toggle*, not to size |
| Picking a single regime label for the tape | Real markets are a vector across dimensions; a "trending up" tape can also be high-vol | Intersect all six columns |
| Assuming regime persistence | The biggest losses come in transitions, not stable regimes (see [[#Regime Transitions Are Where Money Is Made and Lost\|transitions]]) | Size for the flip; throttle near thresholds |
| Confusing regime-complementarity with return-uncorrelation | Two strategies can favor different regimes yet still draw down together | Cross-check the [[strategy-correlation-matrix]] |
| Over-switching (regime-chasing) | Frequent on/off toggling racks up costs and lags regime detection | Use hysteresis bands (e.g., ADX 20/25) not single thresholds |

## Updating This Matrix

When new strategies are added to the wiki, append a row to the relevant category. When a strategy's regime behavior changes (e.g., due to alpha decay or structural change), update the row and note the change date.

## Sources

- [[book-the-quants]] — Patterson on the regime-collapse of stat arb in 2007
- [[book-when-genius-failed]] — Lowenstein on LTCM's regime sensitivity
- [[book-trend-following]] — Covel on trend-following's regime profile
- Asness, Moskowitz, Pedersen (2013) "Value and Momentum Everywhere" — *Journal of Finance*

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].
**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [long-term regimes](https://cryptodataapi.com/regimes)


## Related

- [[market-regime]] — the conceptual frame underlying the six dimensions
- [[regime-detection]] — how to classify the current regime from observable signals
- [[regime-adaptive-strategy]] — strategies that switch exposure as the regime changes
- [[multi-strategy-portfolio]] — combining regime-complementary strategies
- [[strategy-correlation-matrix]] — return correlations (complement to this regime view)
- [[crypto-market-regime-taxonomy]] — the perps-native 14-basket framework
- [[risk-on-risk-off-framework]] — the macro regime overlay
- [[long-vol-vs-short-vol]] — the master long-vol / short-vol axis organizing the matrix
- [[long-volatility-strategies]] — the convex, transition-loving cluster
- [[short-volatility-strategies]] — the carry-like, calm-loving cluster
- [[trend-plus-tail-hedge]] — the canonical regime-complementary construction
- [[volatility-targeting]] / [[risk-budgeting]] — overlays that size for regime transitions
- [[failure-modes]] — transition-driven blowups
- [[edge-taxonomy]] — where each strategy's edge originates
