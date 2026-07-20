---
title: "Z-Score"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [statistics, quantitative, mean-reversion, indicators, volatility, crypto]
aliases: ["Z Score", "Standard Score", "Standardised Score", "Sigma Move", "Number of Standard Deviations", "Standardisation"]
related: ["[[stretch-revert]]", "[[standard-deviation]]", "[[mean-reversion]]", "[[bollinger-bands]]", "[[keltner-channels]]", "[[median-absolute-deviation]]", "[[hurst-exponent]]", "[[half-life-of-mean-reversion]]", "[[stationarity]]", "[[gaussian-distribution]]", "[[fat-tails]]", "[[kurtosis]]", "[[skewness]]", "[[volatility-clustering]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[outliers]]", "[[overfitting]]", "[[mvrv-z-score]]", "[[time-stop]]", "[[false-signals]]", "[[microstructure-noise-low-timeframe]]", "[[crypto-short-history-statistical-power]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [quantitative, technical-analysis, risk-management]
prerequisites: ["[[standard-deviation]]", "[[gaussian-distribution]]"]
difficulty: intermediate
---

# Z-Score

A z-score restates an observation as the number of standard deviations it sits from a reference mean: **z = (x − μ) / σ**. It is the single most-used standardisation in quantitative trading, because it converts an asset-specific, unit-bearing quantity (dollars of spread, percent above a moving average) into a dimensionless number that can be compared across assets, timeframes, and volatility regimes.

In [[stretch-revert]] the z-score is not an input to the strategy — it **is** the strategy. Every one of the family's fourteen members computes a baseline, takes the residual of price against it, divides by a scale estimate, and fades the result. The estimator choice determines the numerator; the scale choice determines the denominator; the threshold determines when to trade. Everything else is risk plumbing.

> **Not to be confused with [[mvrv-z-score]].** That page covers an on-chain valuation metric — market cap versus realised cap, standardised over Bitcoin's full history. It shares the arithmetic and nothing else: different input, different window, different timescale, different trade. Do not read conclusions from one onto the other.

## Definition

$$z = \frac{x - \mu}{\sigma}$$

- **x** — the observation. In [[stretch-revert]] this is price; in [[pairs-trading]] it is the spread; in a volatility filter it is a realised-vol reading.
- **μ** — the reference location. A rolling mean, a fitted baseline, a long-run average, or a theoretical zero.
- **σ** — the scale. Usually a rolling [[standard-deviation]], but see [The σ-estimation problem](#the-σ-estimation-problem) — this is where most implementations go wrong.

A z of +2 means "two scale units above the reference". Positive means rich, negative means cheap, and zero means at the reference. Distance from zero is the *magnitude of the anomaly*; the sign is its direction.

**Residual form.** When μ comes from a fitted model rather than a plain average, the numerator is a regression residual and the z-score is a **standardised residual**:

$$z_t = \frac{p_t - \hat{p}_t}{\hat{\sigma}_{resid}}$$

This distinction matters and is the subject of [Why the regression baselines are different](#why-the-regression-baselines-are-different).

## Rolling versus expanding windows

Neither μ nor σ is known in advance, so both must be estimated from data. The two standard choices:

| Window | μ, σ computed over | Behaviour | Failure mode |
|---|---|---|---|
| **Rolling** (e.g. last 100 bars) | A fixed-length trailing window | Adapts to the current regime; z stays roughly comparable across eras | The reference moves *with* the anomaly; a sustained trend gets absorbed into μ and stops looking extreme |
| **Expanding** (all history to date) | Everything from series start | Stable reference; a genuinely unprecedented move reads as unprecedented | Non-stationary series drift out of range and z ratchets to permanent extremes; the estimate is dominated by ancient data |

For intraday crypto reversion, rolling is effectively mandatory — a BTC price z-scored against its expanding-window mean since 2017 would have read "+4σ rich" for years at a stretch, which is a statement about a bull market, not a trade signal.

But rolling windows carry their own defect, and it is the one that bites reversion strategies: **the window absorbs the move you are trying to detect.** A trend that persists for longer than the window length gradually pulls μ along with it and inflates σ, so the z-score decays toward zero while price keeps going. The signal quietly turns itself off during exactly the regime that would hurt most — which sounds protective but is not, because the position was opened at the start of that trend, when z was still extreme.

**Window length is a real parameter with real [[overfitting]] surface.** Two windows are typically in play at once — the baseline period and the scale window — and they need not be equal. Backtests are sensitive to both, and the pair forms a 2-D grid whose best cell will look good on any history.

## The σ-estimation problem

This is the most important section on the page.

The z-score exists to detect outliers. The ordinary [[standard-deviation]] is computed by squaring deviations from the mean — which means **the outlier you are hunting for is, at the moment it appears, the single largest contributor to the very scale you are measuring it against.** A 5σ move, once it enters the window, inflates σ enough that it no longer reads as 5σ. The estimator eats its own signal.

Concretely, with a 100-bar window and one bar that deviates by 10 units where the other 99 deviate by ~1:

- Sum of squared deviations ≈ 99 × 1 + 100 = 199, so σ ≈ √(199/99) ≈ 1.42
- Without the outlier, σ ≈ 1.0
- The outlier's own z-score: 10 / 1.42 ≈ **7.0**, not 10 — a 30% understatement, caused entirely by its own presence

With a shorter window or a larger outlier, the masking is worse. In a 25-bar window a single wick can halve the apparent extremity of every subsequent reading for the next 25 bars.

### Robust scale: MAD

The standard fix is a robust scale estimator. The **median absolute deviation** ([[median-absolute-deviation|MAD]]) is:

$$\text{MAD} = \text{median}\big(\,|x_i - \text{median}(x)|\,\big)$$

MAD has a 50% breakdown point — half the data can be arbitrary before it moves — versus 0% for the standard deviation. To make it comparable to σ, multiply by the consistency constant:

$$\hat{\sigma}_{robust} = 1.4826 \times \text{MAD}$$

The 1.4826 is `1 / Φ⁻¹(0.75)` — it rescales MAD so that for *normally distributed* data it converges to the same value as σ. Note the conditional: the constant makes MAD a consistent estimator of σ **under normality**. On fat-tailed data the two do not agree, and that disagreement is the point, not an error. MAD reports the scale of the bulk of the distribution; σ reports the scale of the bulk *plus* the tail.

The robust z-score is then:

$$z_{robust} = \frac{x - \text{median}(x)}{1.4826 \times \text{MAD}}$$

**When to prefer it:** whenever the data contains bad prints, wicks, or exchange glitches — which on thin alt perps is always. See [[outliers]].

**When not to:** MAD is less efficient than σ on genuinely clean, near-normal data (roughly 37% efficiency at the normal model), so it is noisier when there is nothing to be robust against. It also cannot distinguish an outlier from the first bar of a real regime break — the same trade-off documented at length on [[theil-sen-regression]].

### The half-solved problem in stretch-revert

The family's `theilsen_stretch_revert` member illustrates an asymmetry worth naming explicitly:

> [[theil-sen-regression|Theil-Sen]] gives a **robust location** — the numerator is protected. But if σ in the denominator is still an ordinary rolling standard deviation, the **scale is not protected**, and the outlier corrupts the z-score through the back door.

A single wick that Theil-Sen correctly ignores when fitting the line still lands in the residual series, still gets squared, and still inflates the denominator for the length of the scale window. The result is a strategy that believes it is outlier-resistant and is only half so. The coherent construction pairs a robust numerator with a robust denominator:

```python
def robust_z(price, baseline, scale_window=100):
    """Theil-Sen (or any robust baseline) MUST be paired with a robust scale."""
    resid = price - baseline                      # robust numerator
    r = resid[-scale_window:]
    mad = median(abs(r - median(r)))
    if mad == 0:
        return None                               # degenerate window; do not trade
    return resid[-1] / (1.4826 * mad)             # robust denominator
```

The error is invisible in the output — both versions return a plausible-looking number — which is why it survives into production. It is the most common implementation bug in this class of strategy.

## Why crypto breaks the normal-distribution intuition

The z-score's reputation comes from the 68-95-99.7 rule: under a [[gaussian-distribution|normal distribution]], |z| > 3 has probability ~0.27%, roughly a 1-in-370 observation. That intuition is the reason "3σ" *feels* like it means something.

**In crypto it does not mean that.** Two properties break it:

1. **[[fat-tails|Fat tails]].** Crypto returns have excess [[kurtosis]] far above the Gaussian. Moves that the normal model prices at 1-in-370 arrive several times a year; 5σ moves that "should" occur once every 14,000 years appear multiple times a decade (see the frequency table on [[standard-deviation]]). A |z| = 3 reading is therefore a *common* event, not a rare one.
2. **[[volatility-clustering]].** σ is not constant. Large moves cluster, so the estimate that produced today's z was calibrated on a different volatility regime than the one currently in force. During a regime transition the denominator is systematically stale — too small entering a vol expansion (z overstated), too large leaving one (z understated). Every threshold silently changes meaning.

Add [[skewness]] and the picture is worse: crypto downside tails are typically fatter than upside tails, so a −3σ and a +3σ are not symmetric events even though the arithmetic treats them identically. A symmetric entry threshold is an implicitly asymmetric bet.

**The practical conclusion:**

> A z-threshold in crypto is **not a probability statement. It is a ranking device.**

`|z| > 2.5` should be read as "this is among the more extended readings in the recent window" — a way to sort candidates and impose a consistent trigger across assets. It should never be read as "this has a 1.2% chance of occurring". Strategies that size positions off implied Gaussian tail probabilities are mis-sized by an order of magnitude in exactly the conditions that matter.

This also means **z-thresholds do not transfer between assets or timeframes without recalibration.** A 2.5σ stretch on BTC 15m and a 2.5σ stretch on a mid-cap alt 15m are different animals: the alt's σ is inflated by [[microstructure-noise-low-timeframe|bid-ask bounce]], so its z-score is partly measuring the spread. The empirical fix is to calibrate thresholds per-asset against the realised distribution of z, not against normal-theory quantiles.

## Non-stationarity of μ and σ

The z-score assumes there *is* a mean to revert to. That assumption is [[stationarity]], and it is the load-bearing one:

- **If μ drifts**, the z-score measures deviation from a stale reference. A trending asset produces persistently one-signed z-scores, and a reversion strategy fades every bar of the trend.
- **If σ drifts**, the threshold changes meaning without changing value. A fixed entry at |z| > 2.5 fires much more often in a calm regime (small σ makes ordinary moves look extreme) than in a violent one.

Neither μ nor σ is stationary in crypto over any horizon that matters. The mitigations, in rough order of usefulness:

- **Regime-gate the signal.** [[hurst-exponent]] below ~0.5 as a precondition — the [[stretch-revert]] family treats this as mandatory rather than advisory precisely because a z-score computed on a trending series is a well-measured number about the wrong model.
- **Bound the holding period.** The z may never return to zero. A [[time-stop]] sized from the [[half-life-of-mean-reversion]] caps the exposure.
- **Use a fitted baseline** so the numerator adapts to local drift rather than assuming a flat mean.
- **Detrend or difference** before z-scoring where the application allows it.
- **Recalibrate thresholds per regime**, not globally.

Short samples make all of this harder to verify: the confidence interval around a rolling σ estimated on a few dozen bars is wide, and crypto's history is short in the ways that matter for statistical power ([[crypto-short-history-statistical-power]]).

## Why the regression baselines are different

All fourteen [[stretch-revert]] members compute a z-score. Only three compute one with a principled scale.

The eleven **averaging** baselines ([[simple-moving-average|SMA]], [[exponential-moving-average|EMA]], [[alma|ALMA]], [[frama|FRAMA]], [[vidya|VIDYA]], [[kama|KAMA]], [[hull-moving-average|HMA]], [[triple-exponential-moving-average|TEMA]], [[zero-lag-exponential-moving-average|ZLEMA]], [[jurik-moving-average|JMA]], [[laguerre-filter|Laguerre]], [[supersmoother-filter|SuperSmoother]]) produce a number, and price's distance from it mixes two unrelated things: genuine displacement, and the mechanical lag of the smoother. There is no model, so there is no theory of what the deviation *should* look like — the σ used to standardise it is a rolling standard deviation of a quantity with no defined null distribution. The band multiple is convention. This is also true of [[bollinger-bands]], which is exactly a ±2σ z-score band on an SMA.

The three **regression** baselines are different in kind:

| Baseline | Fit | Scale available | Note |
|---|---|---|---|
| [[least-squares-moving-average\|LSMA]] | OLS line, read at endpoint | Residual standard error, with R² and slope t-stats | The textbook case; scale is not robust |
| [[theil-sen-regression\|Theil-Sen]] | Median of pairwise slopes | Should use MAD × 1.4826 | Robust numerator; denominator must be made robust too |
| [[quadratic-regression]] | 2nd-order fit, read at endpoint | Residual standard error | Endpoint extrapolation is least stable of the three |

A regression explicitly decomposes the window into "what the model explains" and "what it does not". The leftover is a residual with a **defined scale** — the residual standard error — rather than a rolling standard deviation of an undefined quantity. That gives the z-score an actual denominator instead of a plausible one, and makes the threshold interpretable in the model's own terms.

**This is a real advantage and a limited one.** The residual standard error is principled *conditional on the model being right*. A linear fit to a curving market produces well-scaled residuals of a mis-specified model, and the z-score will be confidently wrong. Endpoint evaluation compounds it: the endpoint is the extrapolated edge of the fit, the point of maximum uncertainty, and it is where the indicator reads its value.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes both μ and σ are estimated from; pull well beyond the scale window so the denominator has a stable rolling sample rather than being re-seeded each run
- `GET /api/v1/hyperliquid/l2-book?coin=X` — on thin books a large part of measured σ *is* the spread, so a z-score computed without a depth check is partly standardising [[microstructure-noise-low-timeframe|noise]] against itself
- `GET /api/v1/volatility/regime/{symbol}` — the volatility regime the σ estimate was calibrated in; a threshold set in one regime does not mean the same thing in another
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into a large z argues the displacement is real flow rather than a print

**Historical data:**
- `GET /api/v1/backtesting/klines` — for measuring the *empirical* distribution of z per asset, which is the only defensible way to set a threshold
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for checking whether z-thresholds hold their meaning across labelled states

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute and, more usefully, *audit* a z-score:

- **Report the empirical tail, not the Gaussian one.** From `GET /api/v1/backtesting/klines`, compute the realised frequency of |z| > 2, 2.5, 3 per coin. If |z| > 3 occurs on 2% of bars rather than 0.27%, the threshold is a ranking cut-off and should be described as one. Publishing the normal-theory probability alongside crypto data is a category error.
- **Always emit both scales.** Return `resid/σ` and `resid/(1.4826 × MAD)` side by side. A large gap between them is a direct measurement that the window contains an outlier — which is more actionable than either number alone.
- **Check the denominator for self-contamination.** Recompute σ with the current bar excluded. If z changes materially, the observation is inflating its own scale and the reading understates the anomaly.
- **Calibrate per asset.** Pull `GET /api/v1/hyperliquid/l2-book?coin=X` and compare the median spread to the σ estimate. When the stretch is within a couple of spreads, the z-score is measuring the book, not a dislocation.
- **Stratify by regime before trusting a threshold.** Join z-scores against `GET /api/v1/quant/regimes/history` and check the threshold's hit rate separately in range- and trend-labelled states. A single global threshold hides the fact that the same z means opposite things in the two regimes.

## Related

- [[stretch-revert]] — the strategy family; the "stretch" is a z-score of price against an adaptive baseline
- [[standard-deviation]] — the conventional denominator, and why it understates tails
- [[median-absolute-deviation]] — the robust alternative, with the 1.4826 consistency constant
- [[outliers]] — what the robust variants defend against
- [[mvrv-z-score]] — a *distinct* on-chain valuation metric sharing only the arithmetic
- [[bollinger-bands]] · [[keltner-channels]] — the band formulation of the same idea
- [[least-squares-moving-average]] · [[theil-sen-regression]] · [[quadratic-regression]] — the regression group, whose residuals have a defined scale
- [[simple-moving-average]] · [[exponential-moving-average]] · [[moving-averages]] · [[adaptive-moving-averages]] — the averaging baselines, whose deviations do not
- [[gaussian-distribution]] · [[fat-tails]] · [[kurtosis]] · [[skewness]] — why the probability reading fails in crypto
- [[volatility-clustering]] — why σ is stale exactly when it matters
- [[stationarity]] — the assumption underneath any z-score
- [[hurst-exponent]] — the regime gate that decides whether reverting toward μ is even the right model
- [[half-life-of-mean-reversion]] · [[time-stop]] — what to do when z does not return to zero
- [[mean-reversion]] — the trade
- [[overfitting]] — window lengths and thresholds are parameters, and they form a grid
- [[false-signals]] · [[microstructure-noise-low-timeframe]] — when the measured stretch is the spread

## Sources

- The 1.4826 consistency constant for MAD is `1/Φ⁻¹(0.75)`, a standard result in robust statistics; see Rousseeuw and Croux (1993), "Alternatives to the Median Absolute Deviation," *Journal of the American Statistical Association*, for the derivation and for more efficient robust scale alternatives.
- Hampel, F. R. (1974). "The Influence Curve and Its Role in Robust Estimation," *Journal of the American Statistical Association* — the breakdown-point framework underlying the σ-versus-MAD comparison.
- Mandelbrot, B. (1963). "The Variation of Certain Speculative Prices," *Journal of Business* — the original documentation that financial returns are not normally distributed, which is why the 68-95-99.7 reading of a z-score fails on market data.
- The sigma-frequency comparison table and the fat-tail critique are drawn from the vault's [[standard-deviation]] page.
- The `theilsen_stretch_revert` robust-numerator/fragile-denominator problem is documented on [[theil-sen-regression]] and derives from the family design recorded on [[stretch-revert]] (dashboard snapshot, 2026-07-20). No source-summary page exists for that snapshot.
- No vault source-summary page covers z-scores specifically; the analysis here is derived from the method and from existing vault pages ([[standard-deviation]], [[fat-tails]], [[stationarity]], [[overfitting]]).
