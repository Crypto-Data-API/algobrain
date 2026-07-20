---
title: "Adaptive Moving Averages"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, quantitative, crypto, mean-reversion, trend-following]
aliases: ["Adaptive Moving Average", "Advanced Moving Averages", "AMA", "Low-Lag Moving Averages", "Moving Average Taxonomy", "Smoothers"]
related: ["[[moving-averages]]", "[[stretch-revert]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[weighted-moving-average]]", "[[alma]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[jurik-moving-average]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[kalman-filter-trading]]", "[[bollinger-bands]]", "[[keltner-channels]]", "[[z-score]]", "[[standard-deviation]]", "[[hurst-exponent]]", "[[mean-reversion]]", "[[overfitting]]", "[[false-signals]]", "[[john-ehlers]]", "[[perry-kaufman]]", "[[tushar-chande]]", "[[median-absolute-deviation]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, quantitative, indicators]
prerequisites: ["[[moving-averages]]", "[[simple-moving-average]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

# Adaptive Moving Averages

Every moving average faces the same trade-off: smoothing requires averaging over history, and averaging over history introduces **lag**. An [[simple-moving-average|SMA]] of period *n* sits, on a linear trend, roughly `(n−1)/2` bars behind price. "Adaptive" and "advanced" moving averages are the several dozen published attempts to beat that trade-off — by rearranging the weights, by varying the smoothing constant with a measured market property, by designing an explicit filter response, or by fitting a model instead of averaging.

This page is the taxonomy hub for the estimator cluster in this vault. It groups the variants by **mechanism** rather than by author or popularity, because the mechanism is what determines how each one behaves at a pivot — and that behaviour is the whole design space of [[stretch-revert]], a strategy family whose fourteen members differ *only* in which of these estimators defines the baseline.

## Why the taxonomy is by mechanism

Grouping by mechanism makes the failure modes predictable. Each of the four groups fails in a characteristic way:

1. **Weighted / lag-cancelling** — fixed weights arranged so the lag terms cancel. They achieve near-zero lag under a constant slope and pay for it with **overshoot** at pivots and amplified high-frequency noise.
2. **Adaptive** — the smoothing constant varies with a measured market property (efficiency, volatility, fractal dimension). They handle regime change gracefully and pay for it with **added parameters** and a lag that is no longer a fixed, knowable quantity.
3. **Signal-processing filters** — designed from an explicit frequency response rather than as averages. They reject microstructure jitter well and pay for it with **opacity** — the parameters are not interpretable as "bars".
4. **Regression baselines** — fit a model to the window instead of averaging it. The deviation becomes a genuine residual with a defined scale, at the cost of **endpoint instability** (they read the fit at the extrapolated edge).

Nothing escapes the trade-off. Every design moves along the same lag-versus-noise frontier; none of them shifts the frontier itself. What varies is *where* on the curve each one sits and *what shape* its errors take.

## Group 1 — Weighted / lag-cancelling

Fixed weights arranged to cancel lag. No parameter varies with market state.

- **[[weighted-moving-average|WMA]]** — linear weights `w_i = i`. Effective lag `(n−1)/3` versus `(n−1)/2` for the SMA. Not adaptive itself, but the **building block** for HMA and the conceptual ancestor of the group.
- **[[alma|ALMA]]** — Gaussian weights whose peak is shifted toward the newest bar by an explicit `offset` parameter. The lag-versus-smoothness trade-off exposed as a knob rather than baked in.
- **[[hull-moving-average|HMA]]** — a WMA of WMAs with a √n final smoothing. Very low lag, stays visually smooth, **overshoots at pivots** — it extrapolates the recent slope.
- **[[triple-exponential-moving-average|TEMA]]** — Mulloy's recursive EMA-of-EMA lag cancellation. Algebraically zero-lag under constant slope, at roughly **7× noise amplification**.
- **[[zero-lag-exponential-moving-average|ZLEMA]]** — de-lags the *input* before smoothing (`2p_t − p_{t−lag}`). The correction assumes a linear trend, so it errs *in the trend direction* during acceleration.

**Shared failure mode:** these estimators assume the recent slope continues. When it does not — at exactly a pivot — they overshoot past price and then correct back. For a reversion strategy that is a signal-generating artifact, not information.

## Group 2 — Adaptive

The smoothing constant changes with a measured market property, so the same code is fast in trends and slow in chop.

- **[[frama|FRAMA]]** — Ehlers' fractal adaptive MA. Estimates the fractal dimension of recent price and maps it to an EMA alpha. Related to, but distinct from, the [[hurst-exponent]].
- **[[vidya|VIDYA]]** — [[tushar-chande|Chande]]'s volatility-indexed dynamic average. Smoothing accelerates with measured volatility or momentum.
- **[[kama|KAMA]]** — [[perry-kaufman|Kaufman]]'s efficiency-ratio adaptive MA. Ratio of net directional movement to total path length: near 1 in a clean trend (fast), near 0 in chop (slow). The most interpretable of the three.

**Shared failure mode:** the adaptation is itself an estimate on a window, so it lags the regime change it exists to detect. The estimator speeds up *after* the trend establishes and slows down *after* the chop begins. It also means the effective lag is a function of market state, so "how far behind is this baseline?" has no fixed answer — which complicates every downstream calculation that assumed one.

## Group 3 — Signal-processing filters

Designed from a stated frequency response. Mostly [[john-ehlers|Ehlers]]' work, importing DSP practice into technical analysis.

- **[[laguerre-filter|Laguerre Filter]]** — a short-kernel cascade giving EMA-like smoothing with less lag, controlled by a single damping factor γ.
- **[[supersmoother-filter|SuperSmoother]]** — a two-pole Butterworth-derived low-pass filter. Ehlers' argument for it is specifically that ordinary MAs **do not actually remove** the high-frequency content they claim to; SuperSmoother is designed with an explicit stopband.
- **[[jurik-moving-average|JMA]]** — commercial and **proprietary**. The algorithm has never been disclosed, so it cannot be independently verified, reproduced, or audited. Its presence in a backtest is an unfalsifiable dependency.

**Shared failure mode:** the parameters are not interpretable in the units traders reason in. A damping factor of 0.7 does not correspond to a bar count, so intuitions about "how much history is this seeing" fail. JMA's opacity is a separate and more serious issue — a strategy that depends on an undisclosed algorithm cannot be fully validated.

## Group 4 — Regression baselines

Fit a model to the window rather than averaging it. This changes what the deviation *is*: a residual with a defined scale rather than a distance from an arbitrary number.

- **[[least-squares-moving-average|LSMA]]** — OLS line read at the endpoint. Residual standard error, R², and slope t-statistics all available. Zero breakdown point.
- **[[theil-sen-regression|Theil-Sen]]** — median of all pairwise slopes. ~29.3% breakdown point versus 0% for OLS, at O(n²) cost. Must be paired with a robust scale ([[median-absolute-deviation|MAD]] × 1.4826) or the robustness is only half-implemented.
- **[[quadratic-regression]]** — second-order fit, so the baseline can curve with momentum. Most flexible, and the least stable at the endpoint.
- **[[kalman-filter-trading|Kalman filter]]** — state-space estimation rather than window fitting. Recursive, with an explicit noise model and a principled deviation from the filtered state. The most theoretically grounded and the most parameter-sensitive.

**Shared advantage:** the [[z-score]] built on a regression residual has a denominator that means something in the model's own terms, instead of a rolling [[standard-deviation]] of an undefined quantity.

**Shared failure mode:** all four read the fit at the most recent bar — the extrapolated edge, the point of maximum uncertainty. And a well-scaled residual of a mis-specified model is confidently wrong: a linear fit to a curving market produces clean-looking residuals that are systematically biased.

## Comparison table

Lag and noise gain are given relative to an SMA of the same period, on a constant-slope input. These are qualitative characterisations, not measured constants — actual values depend on period and on the input series.

| Estimator | Mechanism | Lag | Noise gain | Overshoot? | Group |
|---|---|---|---|---|---|
| [[simple-moving-average\|SMA]] | Equal weights | `(n−1)/2` — highest | 1× (baseline) | No | reference |
| [[exponential-moving-average\|EMA]] | Geometric decay | ~`(n−1)/2` | ~1× | No | reference |
| [[weighted-moving-average\|WMA]] | Linear weights | `(n−1)/3` | slightly > 1× | No | weighted |
| [[alma\|ALMA]] | Offset Gaussian weights | Tunable via `offset` | Low–moderate | Mild at high offset | weighted |
| [[hull-moving-average\|HMA]] | WMA of WMAs, √n smooth | Very low | Moderate | **Yes — pronounced** | weighted |
| [[triple-exponential-moving-average\|TEMA]] | Recursive EMA lag cancel | ~Zero (constant slope) | **~7×** | **Yes** | weighted |
| [[zero-lag-exponential-moving-average\|ZLEMA]] | De-lagged input | ~Zero (linear trend) | Moderate–high | Yes, in trend direction | weighted |
| [[frama\|FRAMA]] | Fractal dimension → alpha | Varies with regime | Varies | Mild | adaptive |
| [[vidya\|VIDYA]] | Volatility-indexed alpha | Varies with vol | Varies | Mild | adaptive |
| [[kama\|KAMA]] | Efficiency ratio → alpha | Fast in trend, slow in chop | Low in chop | No | adaptive |
| [[laguerre-filter\|Laguerre]] | Short-kernel cascade | Low | Low | Mild | filter |
| [[supersmoother-filter\|SuperSmoother]] | Two-pole low-pass | Moderate | **Lowest** | No | filter |
| [[jurik-moving-average\|JMA]] | Undisclosed | Claimed low | Claimed low | Unknown | filter |
| [[least-squares-moving-average\|LSMA]] | OLS endpoint | ~Zero on linear path | Moderate | Yes at reversals | regression |
| [[theil-sen-regression\|Theil-Sen]] | Median pairwise slope | ~Zero on linear path | Low | No — **slow to turn** | regression |
| [[quadratic-regression]] | 2nd-order endpoint | ~Zero, tracks curvature | High at endpoint | **Yes — strongly** | regression |
| [[kalman-filter-trading\|Kalman]] | State-space recursion | Tunable via noise ratio | Tunable | Depends on model | regression |

Read the table as a frontier, not a leaderboard. The estimators with "~Zero" lag all pay in the noise-gain or overshoot columns. There is no row that wins everywhere, and the existence of such a row would be a strong hint of an error.

## The honest bottom line

Three things are true simultaneously and are usually stated one at a time:

**1. Adaptive variants add parameters, and parameters are [[overfitting]] surface.** An SMA has one parameter. [[jurik-moving-average|JMA]] has period, phase, and power; [[frama|FRAMA]] has period plus fractal-window plus alpha bounds; [[alma|ALMA]] has period, offset, and sigma. Each additional knob multiplies the search space, and the best cell of any grid will look good on any history. A fourteen-estimator family — as in [[stretch-revert]] — is a fourteen-fold multiple-comparisons problem before a single estimator's own parameters are counted.

**2. [[moving-averages]] already gives the right advice: test the simple filter first.** That page's conclusion is that in crypto the 200D MA regime filter (price above or below) has historically mattered more than the exact MA type, and that the SMA and EMA remain dominant in systematic trading because their behaviour is well-understood and robust across regimes. Reaching for an adaptive variant before establishing that the simple filter fails is the wrong order of operations. The burden of proof is on the complicated estimator.

**3. Default parameters for most of these are convention, not derived optima.** The 12/26 EMA in MACD, the 20-period Bollinger basis, HMA's √n, ALMA's offset 0.85 and sigma 6, KAMA's 2/30 fast-slow bounds — these are the author's original published choices, propagated by platform defaults for decades. They were not optimised, and they are certainly not optimal for 15m crypto perps, an instrument that did not exist when most of them were published. This cuts both ways: the defaults are not sacred, but a parameter you *did* optimise is one you fitted, and the untuned default at least has the virtue of not having been fitted to your sample.

The genuinely defensible use of a multi-estimator family is **robustness testing**: if an effect is real it should survive a change of smoother. If profit appears under exactly one lag profile, that is a signature of curve-fitting rather than edge. That argument only works when several estimators have independent samples — running fourteen and reporting the best one is the opposite of the intended logic.

## Choosing an estimator for a reversion baseline

For [[mean-reversion]] work specifically, the selection criteria differ from trend-following:

- **Overshoot is disqualifying-ish.** An estimator that extrapolates past price at a pivot manufactures apparent "stretch" that is an artifact of the smoother. HMA, TEMA, and [[quadratic-regression]] all do this. It does not rule them out but it does mean their [[false-signals]] concentrate at exactly the bars a fade strategy trades.
- **Too fast is as bad as too slow.** [[zero-lag-exponential-moving-average|ZLEMA]] and [[triple-exponential-moving-average|TEMA]] hug price so closely they rarely register a stretch at all — high precision, near-zero recall.
- **A defined residual scale is worth real weight.** Only the regression group gives the [[z-score]] a principled denominator. See [[z-score#Why the regression baselines are different]].
- **Robustness must be end-to-end.** [[theil-sen-regression|Theil-Sen]] protects the numerator; unless the denominator is also robust, a single wick still corrupts the signal.
- **None of this is a regime gate.** No estimator tells you whether reverting is the right model at all — that is [[hurst-exponent]]'s job, and in [[stretch-revert]] it is mandatory rather than advisory.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes every estimator on this page is computed from; pull at least 2–3× the longest period as warm-up, since the recursive filters (EMA, TEMA, Laguerre, Kalman) need burn-in before their output is meaningful
- `GET /api/v1/hyperliquid/l2-book?coin=X` — the noise-gain column is not academic on thin books; a high-gain estimator on a wide-spread alt is amplifying the spread
- `GET /api/v1/volatility/regime/{symbol}` — the adaptive group's behaviour is regime-dependent by construction, so its output is only interpretable alongside the regime it was produced in

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for replaying every estimator over an identical bar set, which is the only way the comparison means anything
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels since 2020, for checking whether an estimator's advantage is regime-specific rather than general

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can use this taxonomy as a test harness rather than a menu:

- **One data pull, all estimators.** Fetch `GET /api/v1/hyperliquid/candles` once and compute every baseline over the identical bar set. Comparing estimators run on different pulls, warm-ups, or timestamps is comparing artifacts.
- **Measure the pairwise disagreement first.** Report the spread between estimator endpoints in basis points. Where several agree to within a few bps, the choice does not matter and the cheapest estimator wins — this is the decision variable, and it is usually the case in liquid majors.
- **Always include the SMA and EMA as controls.** Per [[moving-averages]], the simple filter is the baseline any adaptive variant must beat. An agent that reports only the exotic estimators has removed the null hypothesis from its own experiment.
- **Flag the noise-gain column against measured spread.** Cross `GET /api/v1/hyperliquid/l2-book?coin=X` with the estimator's noise gain — a ~7× amplifier such as TEMA on a wide alt book is producing signal from the spread.
- **Deflate before recommending.** Testing seventeen estimators and reporting the best is a multiple-comparisons problem. Validate against `GET /api/v1/backtesting/klines` with regime stratification from `GET /api/v1/quant/regimes/history`, and state how many variants were tried.

## Related

- [[moving-averages]] — the parent page; the classic SMA/EMA/WMA treatment and the "test the simple filter first" caution
- [[stretch-revert]] — the strategy family whose fourteen members differ only in which estimator here is the baseline
- [[simple-moving-average]] · [[exponential-moving-average]] · [[weighted-moving-average]] — the reference estimators
- [[alma]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] — group 1, weighted / lag-cancelling
- [[frama]] · [[vidya]] · [[kama]] — group 2, adaptive
- [[laguerre-filter]] · [[supersmoother-filter]] · [[jurik-moving-average]] — group 3, signal-processing filters
- [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] · [[kalman-filter-trading]] — group 4, regression baselines
- [[z-score]] — what the deviation from any of these baselines is converted into
- [[standard-deviation]] · [[median-absolute-deviation]] — the two scale choices for that conversion
- [[bollinger-bands]] · [[keltner-channels]] — bands built around a baseline
- [[hurst-exponent]] — the regime gate no estimator substitutes for
- [[mean-reversion]] — the trade the reversion-baseline selection serves
- [[overfitting]] · [[false-signals]] — the cost of every added parameter
- [[john-ehlers]] · [[perry-kaufman]] · [[tushar-chande]] — the primary authors in groups 2 and 3

## Sources

- Mulloy, Patrick (1994). "Smoothing Data with Faster Moving Averages," *Technical Analysis of Stocks & Commodities* — the original DEMA/TEMA lag-cancellation construction.
- Kaufman, Perry J. (1995). *Smarter Trading* — the efficiency ratio and KAMA.
- Chande, Tushar S. and Kroll, Stanley (1994). *The New Technical Trader* — VIDYA, the volatility-indexed dynamic average.
- Hull, Alan (2005) — the Hull Moving Average.
- Ehlers, John F. *Rocket Science for Traders* (2001), *Cybernetic Analysis for Stocks and Futures* (2004), and *Cycle Analytics for Traders* (2013) — the Laguerre filter, SuperSmoother, FRAMA, and the general case for applying DSP filter design to price series.
- Arnaud Legoux and Dimitrios Kouzis-Loukas (2009) — the Arnaud Legoux Moving Average (ALMA).
- Jurik Research — JMA is commercial and its algorithm is undisclosed; no primary description exists to cite.
- Theil, H. (1950) and Sen, P. K. (1968) — the median-of-pairwise-slopes estimator underlying the Theil-Sen baseline.
- The "test the simple filter first" conclusion and the observation that default parameters are convention are drawn from the vault's [[moving-averages]] page. The four-group taxonomy and the estimator roster follow the design of [[stretch-revert]] (2026-07-20).
- No vault source-summary page covers this taxonomy; lag and noise-gain characterisations are qualitative, derived from each estimator's construction rather than from a measured study.
