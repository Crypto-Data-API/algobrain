---
title: "Median Absolute Deviation (MAD)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [quantitative, statistics, volatility, risk-management, crypto, indicators]
aliases: ["MAD", "Median Absolute Deviation", "Robust Scale", "Robust Z-Score", "MAD-Z"]
related: ["[[standard-deviation]]", "[[z-score]]", "[[theil-sen-regression]]", "[[linear-regression]]", "[[least-squares-moving-average]]", "[[quadratic-regression]]", "[[stretch-revert]]", "[[outliers]]", "[[mean-reversion]]", "[[volatility]]", "[[bollinger-bands]]", "[[keltner-channels]]", "[[atr]]", "[[hurst-exponent]]", "[[overfitting]]", "[[stationarity]]", "[[microstructure-noise-low-timeframe]]", "[[bid-ask-spread]]", "[[liquidation-cascade]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[alma]]", "[[hull-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[kalman-filter-trading]]", "[[failure-modes]]", "[[volatility-regime-classification]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [quantitative, risk-management]
prerequisites: ["[[standard-deviation]]", "[[z-score]]"]
difficulty: intermediate
---

# Median Absolute Deviation (MAD)

The median absolute deviation is a **robust measure of spread**: take the median of the data, take each point's absolute distance from that median, then take the median of those distances.

```
MAD = median( | x_i − median(x) | )
```

It answers the same question a [[standard-deviation]] answers — how spread out is this sample — while being almost completely indifferent to how extreme the extreme values are. That indifference is the entire point, and on crypto price data, where a single wick is a routine event rather than an anomaly, it is worth a great deal.

## The 1.4826 consistency constant

Raw MAD is not on the same scale as σ. For normally distributed data, MAD converges to the 0.75 quantile of the standard normal, `Φ⁻¹(0.75) ≈ 0.6745`, times σ. So MAD systematically reads about two-thirds of the standard deviation of the same normal sample.

Multiplying by the reciprocal fixes it:

```
1 / 0.6745 ≈ 1.4826

σ̂ = 1.4826 × MAD
```

Under normality `1.4826 × MAD` is a **consistent estimator of σ** — the two agree in expectation as the sample grows. That is what makes the constant worth carrying: it means a MAD-based scale can be dropped into any formula that expected a standard deviation, with thresholds unchanged. A "2σ band" and a "2 × 1.4826 × MAD band" mean the same thing on clean normal data and diverge only when the data is contaminated, which is exactly the behaviour you want.

The constant is **specific to the normal distribution.** It is not a universal conversion factor. On genuinely fat-tailed data, `1.4826 × MAD` and the sample σ are estimating different things and will not agree — but this is a feature: the disagreement between them is a direct, cheap measurement of how contaminated the sample is.

```python
def mad(x, scaled=True):
    """Median absolute deviation. scaled=True returns a sigma-comparable value."""
    m = median(x)
    d = median(abs(xi - m) for xi in x)
    return 1.4826 * d if scaled else d

def robust_z(x_t, window):
    """Robust z-score: median location, MAD scale."""
    m = median(window)
    s = mad(window, scaled=True)
    return (x_t - m) / s if s > 0 else 0.0
```

## Breakdown point: 50% versus 0%

The breakdown point is the fraction of a sample that can be replaced with arbitrary values before the estimate can be driven anywhere at all.

| Statistic | Breakdown point | What one bad point does |
|---|---|---|
| Mean | **0%** | Drags the estimate without limit |
| [[standard-deviation]] | **0%** | Inflates without limit — worse than the mean, because the deviation is squared |
| Median | **50%** | Nothing, until half the sample is corrupted |
| **MAD** | **50%** | Nothing, until half the sample is corrupted |

50% is the theoretical maximum. Beyond half, "the data" and "the contamination" are no longer distinguishable, so no estimator can do better.

The contrast with σ deserves a concrete illustration, because the asymmetry is larger than intuition suggests. Take 100 residuals drawn from a distribution with true σ = 1. Now replace one of them with 50 — a single 50-sigma print, which on a thin alt perp is a Tuesday.

- **σ** jumps from ≈ 1.0 to ≈ 5.0. The squared term means the one bad point contributes 2500 to a sum that was previously about 100.
- **1.4826 × MAD** stays at ≈ 1.0. One point out of a hundred cannot move a median.

Standard deviation is *more* fragile than the mean, not less, because squaring amplifies exactly the observations that should count least. This is the property that makes the next section matter.

## The robust z-score

The conventional [[z-score]] is `(x − mean)/σ`. Both components have a 0% breakdown point, so the whole statistic does. The robust replacement swaps both:

```
z_robust = (x − median) / (1.4826 × MAD)
```

Interpretation is unchanged when the data is clean — both read "how many typical deviations from typical" — and they diverge precisely when there is something to diverge about. A common convention flags `|z_robust| > 3.5` as an outlier (Iglewicz and Hoaglin, 1993), which is deliberately more conservative than a nominal 3σ rule because a robust scale does not get inflated by the very points it is trying to detect.

**Half-measures do not work.** A robust numerator with a fragile denominator, or vice versa, is not partially robust — it is just broken in a less obvious way. [[theil-sen-regression]] makes exactly this point: pairing a median-of-slopes fit with a standard-deviation residual scale reintroduces outlier sensitivity through the back door, and the error is invisible in the output because the number still looks like a z-score.

## Efficiency: what robustness costs

Robustness is not free, and this page would be dishonest without the price tag.

Under **genuinely normal data with no contamination**, the sample standard deviation is the efficient estimator of σ, and `1.4826 × MAD` has an asymptotic relative efficiency of about **37%**. In practical terms: MAD needs roughly 2.7× as many observations to estimate σ as precisely as the sample standard deviation does from clean normal data. It is a noisier estimate.

That trade is real and should be evaluated, not assumed:

- **On clean, well-behaved data, use σ.** You are paying a factor of 2.7 in sample efficiency for protection against contamination that is not there.
- **On data with even light contamination, MAD wins quickly.** The efficiency comparison assumes exact normality. Under a contaminated-normal model — say 99% N(0,1) and 1% N(0,10) — the sample σ's *bias* swamps MAD's *variance* almost immediately. A single-percent contamination rate is enough to flip the comparison.
- **Crypto residuals on 15m perp bars are firmly in the second case.** Fat tails, jumps, exchange glitches, and [[liquidation-cascade|cascade]] wicks are not rare events in this data; they are a recurring structural feature.

There are middle grounds — Rousseeuw and Croux (1993) proposed the `S_n` and `Q_n` estimators, which retain a 50% breakdown point at roughly 58% and 82% efficiency respectively. They are more expensive to compute and much less widely implemented. MAD's advantage is that it is `O(n)` with a selection algorithm, trivially explainable, and available everywhere.

## Why this page matters to stretch-revert

This is the reason the page exists, and it is a **design observation about the family, not a performance claim.**

Every member of [[stretch-revert]] computes its signal the same way: a baseline estimator gives a fair value, the residual `price − baseline` is the stretch, and the stretch is normalised into a [[z-score]] against a **rolling ordinary standard deviation**. The family's own pseudocode makes this explicit:

```python
sigma = rolling_std(b.close - baseline, window=cfg.z_window)
z     = resid / sigma
```

That denominator has a 0% breakdown point, and the consequence is a specific, mechanical pathology:

> **A large dislocation inflates the very scale it is measured against, and therefore shrinks its own measured z-score.**

Walk through it. A liquidation flush produces a residual several times larger than anything in the recent window. That residual enters the rolling σ window on the next bar. Being squared, it dominates the sum. σ jumps. Every subsequent residual — including the continuing dislocation the strategy is trying to trade — is divided by an inflated denominator and reads *smaller* in z terms than it should. The bigger the dislocation, the more it suppresses its own signal.

This runs in the same direction as the adaptive-baseline suppression problem documented on [[frama]] and [[vidya]], and compounds with it. On the FRAMA member, a fast move raises `alpha`, so the baseline chases price and the **numerator** shrinks; simultaneously the fresh large residuals inflate σ, so the **denominator** grows. Both effects reduce the measured z-score during the largest real dislocations. [[vidya]] documents the same double-squeeze for its stdev formulation, and notes that raw residual and z-score can move in opposite directions through a widening dislocation.

**Where MAD is the missing half.** The family already has one robust component. [[theil-sen-regression|Theil-Sen]] gives a **robust location** — a fitted baseline with a ~29.3% breakdown point that a wick cannot tilt. That fixes the numerator of the z-score for one member. But **nothing in the family makes the scale robust.** All fourteen members, Theil-Sen included, divide by an ordinary rolling standard deviation. The `theilsen_stretch_revert` member is therefore a robust numerator over a fragile denominator, which is precisely the half-measure the section above warns against.

MAD is the other half. `resid / (1.4826 × MAD)` is the coherent completion: robust location, robust scale, a threshold that keeps its meaning across regimes and does not get quietly recalibrated by the events it is supposed to detect.

**What this is not.** This is an observation about the internal consistency of the design. It is emphatically **not** a claim that swapping σ for MAD would have improved the family's live results, and nothing here should be read that way:

- The live sample is 53 trades across four members that have actually traded. That is far too small to attribute any outcome to the scale estimator, and [[stretch-revert]] says so about its own numbers.
- The suppression effect described above is a *measurement* argument. It says the z-score understates large dislocations. Whether trading a correctly-measured larger z-score would have made money is an entirely separate question, and one the data cannot answer.
- Robustness fixes measurement failures, not position failures. That distinction is the central lesson of the [[theil-sen-regression]] page — an 80% win rate with negative P/L — and it applies here identically. A robust scale would not have prevented a single unreverting move.
- Swapping the scale estimator is itself a parameter change on an already-large surface, and a change validated only on the sample that motivated it is [[overfitting]] with extra steps.

The correct next step is not to swap it live. It is to compute both scales in parallel over `GET /api/v1/backtesting/klines` history, measure how often and how far they diverge per asset, and find out whether the effect is large enough to matter before touching anything.

## Practical notes

| Consideration | Guidance |
|---|---|
| Window length | 50–100 bars for a residual scale. Shorter windows make MAD's efficiency cost bite; longer ones span volatility regimes and break [[stationarity]] |
| Zero MAD | If more than half the window is identical (a stalled, illiquid book), MAD is exactly 0 and the z-score divides by zero. Always guard it; σ degrades more gracefully here |
| Compute cost | `O(n)` with a selection algorithm, `O(n log n)` with a naive sort. Two passes rather than one. Cheap next to [[theil-sen-regression\|Theil-Sen]]'s `O(n²)` |
| Rolling implementation | Less incrementally updatable than a rolling σ, which has an exact online form. Usually irrelevant at 15m bars, potentially material on a 1m fast loop |
| Reporting | Always state whether a quoted z-score used σ or MAD. The two are not interchangeable and the number looks identical either way |
| Related robust scales | Interquartile range (breakdown 25%), `S_n` / `Q_n` (breakdown 50%, higher efficiency), trimmed and winsorised σ |

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the residuals and both scale estimates are computed from; pull well past the scale window so the rolling estimate is stable
- `GET /api/v1/volatility/regime/{symbol}` — volatility state; a MAD calibrated in one regime silently changes meaning in another
- `GET /api/v1/hyperliquid/l2-book?coin=X` — depth check; on thin books much of the residual dispersion both estimators see is [[bid-ask-spread|spread]], not price
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expansion alongside a large robust z argues the displacement is real flow rather than a print

**Historical data:**
- `GET /api/v1/backtesting/klines` — the archive for the comparison that actually matters: σ versus `1.4826 × MAD` on identical residuals across full cycles
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels since 2020, for stratifying the divergence between the two scales by regime

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can quantify the argument on this page rather than assert it:

- **Compute both scales on identical residuals and report the ratio.** From one `GET /api/v1/hyperliquid/candles` pull, emit `resid/σ` and `resid/(1.4826 × MAD)` side by side. The ratio `σ / (1.4826 × MAD)` is a direct contamination gauge: near 1.0 means clean data and σ is fine; persistently above ~1.3 means σ is being driven by tail events on that asset.
- **Measure the self-suppression effect directly.** For each large residual, record σ on the bar before it entered the rolling window and on the bar after. The jump is the amount by which the dislocation deflated its own z-score. Do this per asset — the effect scales with how thin the book is.
- **Always label the scale in the output.** A z-score reported without its denominator's provenance is not reproducible, and the σ and MAD versions of the same bar can differ by a factor of two during a cascade.
- **Guard the zero-MAD case.** Stalled or illiquid books produce `MAD = 0` and an undefined z. Fall back explicitly and log it; a silent divide-by-zero fallback to σ reintroduces exactly the fragility being avoided.
- **Validate on history, not on the live sample.** Use `GET /api/v1/backtesting/klines` with regime stratification from `GET /api/v1/quant/regimes/history` before changing any live scale estimator. Fifty-three trades cannot distinguish a scale effect from noise, per [[overfitting]].

## Related

- [[standard-deviation]] — the fragile alternative with a 0% breakdown point; the denominator every [[stretch-revert]] member currently uses
- [[z-score]] — the normalisation; the robust form swaps both its components
- [[theil-sen-regression]] — the robust *location* the family already has; MAD is the robust scale it lacks
- [[stretch-revert]] — the strategy family this observation applies to
- [[linear-regression]] · [[least-squares-moving-average]] · [[quadratic-regression]] — the regression group, whose residuals need a scale
- [[outliers]] — what a 50% breakdown point defends against
- [[frama]] · [[vidya]] — where adaptive-baseline suppression compounds with scale inflation
- [[volatility]] · [[volatility-regime-classification]] · [[atr]] — other spread measures, with different robustness profiles
- [[bollinger-bands]] · [[keltner-channels]] — band constructions built on σ and on ATR respectively
- [[stationarity]] — the assumption underneath any rolling scale estimate
- [[liquidation-cascade]] · [[microstructure-noise-low-timeframe]] · [[bid-ask-spread]] — the sources of contamination in crypto residuals
- [[hurst-exponent]] — the regime gate; a robust scale does not substitute for it
- [[overfitting]] · [[failure-modes]] — why a scale swap must be validated on history, not on the sample that motivated it
- [[alma]] · [[kama]] · [[hull-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — sibling baselines, all normalised by σ

## Sources

- Hampel, F. R. (1974). The influence curve and its role in robust estimation. *Journal of the American Statistical Association* 69(346). Popularised MAD as a robust scale estimator and introduced the influence-function framework.
- Rousseeuw, P. J. & Croux, C. (1993). Alternatives to the median absolute deviation. *Journal of the American Statistical Association* 88(424). Source of the ~37% asymptotic efficiency figure for MAD under normality, and of the `S_n` / `Q_n` alternatives with higher efficiency at the same 50% breakdown point.
- Iglewicz, B. & Hoaglin, D. C. (1993). *How to Detect and Handle Outliers*. Origin of the `|z_robust| > 3.5` flagging convention.
- Huber, P. J. (1981). *Robust Statistics*. General framework, including the breakdown-point concept used throughout this page.
- The `1.4826 = 1/Φ⁻¹(0.75)` consistency constant is a standard result and is derived directly from the normal quantile function.

The [[stretch-revert]] design observation is derived from that page's published pseudocode and from the [[theil-sen-regression]] and [[frama]] pages in this vault. No backtest comparing σ and MAD scales on this family has been run, and no vault source-summary page covers MAD.
