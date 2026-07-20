---
title: "Linear Regression"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [quantitative, statistics, indicators, technical-analysis, backtesting, crypto]
aliases: ["Linear Regression", "OLS", "Ordinary Least Squares", "Least Squares Regression", "Regression Line", "Linear Regression Channel"]
related: ["[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[quadratic-regression]]", "[[stretch-revert]]", "[[median-absolute-deviation]]", "[[standard-deviation]]", "[[z-score]]", "[[mean-reversion]]", "[[hurst-exponent]]", "[[overfitting]]", "[[stationarity]]", "[[autocorrelation]]", "[[volatility]]", "[[outliers]]", "[[moving-averages]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[adaptive-moving-averages]]", "[[alma]]", "[[frama]]", "[[vidya]]", "[[kama]]", "[[hull-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[kalman-filter-trading]]", "[[cointegration]]", "[[pairs-trading]]", "[[bollinger-bands]]", "[[correlation]]", "[[beta]]", "[[deflated-sharpe-ratio]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [quantitative, technical-analysis]
prerequisites: ["[[standard-deviation]]", "[[correlation]]"]
difficulty: intermediate
---

# Linear Regression

Linear regression fits a straight line through a set of points by minimising the **sum of squared vertical distances** from the points to the line. It is the foundation underneath the regression group of [[stretch-revert]] — [[least-squares-moving-average|LSMA]], [[theil-sen-regression|Theil-Sen]] and [[quadratic-regression]] — and, more broadly, underneath most of applied quantitative finance: betas, hedge ratios, factor models, and [[cointegration]] residuals are all regression output.

Its importance to a mean-reversion trader is narrower and sharper than its importance to a statistician. A regression decomposes a price window into *what the line explains* and *what it does not*, and that leftover — the residual — **is the tradable stretch**. Everything else on this page exists to say how much you can trust the size of that residual.

## The fit

For points `(x_1, y_1) … (x_n, y_n)`, ordinary least squares (OLS) chooses slope `b` and intercept `a` minimising `Σ(y_i − a − b·x_i)²`. In the trading case `x` is just the bar index `0, 1, … n−1` and `y` is the close.

```python
def ols(y):
    """Slope, intercept and residuals of an OLS fit against bar index."""
    n  = len(y)
    x  = list(range(n))
    mx = sum(x) / n
    my = sum(y) / n

    sxy = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    sxx = sum((x[i] - mx) ** 2 for i in range(n))

    b = sxy / sxx                 # slope
    a = my - b * mx               # intercept
    resid = [y[i] - (a + b * x[i]) for i in range(n)]
    return a, b, resid
```

- **Slope `b`** — the fitted rate of change per bar. Direction and pace of the trend inside the window.
- **Intercept `a`** — the fitted value at `x = 0`.
- **Residual `e_i = y_i − ŷ_i`** — the unexplained part. In a trading context, the distance price sits from its own fitted trend.
- **The line always passes through `(x̄, ȳ)`** — the centroid. This turns out to matter a great deal; see below.

## Residuals, R², and the standard error

Three derived quantities carry the interpretation.

**Coefficient of determination.** `R² = 1 − SS_res/SS_tot`, the fraction of the window's variance the line accounts for. On short price windows `R²` is routinely high for trivial reasons: any series with drift fits a line reasonably well over 20 bars. A high `R²` on a 25-bar close series is not evidence of a trend worth trading — it is evidence that 25 points and two parameters are not many constraints.

**Standard error of the estimate.** `SE = sqrt(SS_res / (n − 2))`, the typical residual size in price units. This is the natural scale for the stretch: `z = e_t / SE` converts "price is $340 above the fitted line" into "price is 2.4 typical residuals above the fitted line", which is comparable across assets and epochs.

**Prediction interval.** Wider than a confidence interval on the mean response, because it must also carry the irreducible error of a single new observation. Its width is not constant across the window — it is narrowest at the centroid `x̄` and widens toward both ends. That geometry is the single most under-appreciated fact in indicator design, and the next section is about it.

## The endpoint versus the midpoint

A regression line fitted to the last `n` bars can be read at any `x`. Two readings matter:

- **The midpoint** — the fitted value at the centre of the window. This is where the fit is best determined and the prediction interval narrowest. It is also, structurally, `(n−1)/2` bars in the past. A "linear regression curve" plotted at the midpoint is a smoother with exactly the centroid lag of an [[simple-moving-average|SMA]] of the same length — because the OLS line passes through `(x̄, ȳ)` and `ȳ` *is* the SMA.
- **The endpoint** — the fitted value at the most recent bar, `a + b·(n−1)`. This is the [[least-squares-moving-average|LSMA]]. Because the line extrapolates the window's slope all the way to the present, the endpoint tracks a linear ramp with essentially **zero lag**, where the SMA trails by `(n−1)/2` bars.

That is the whole trick behind the LSMA as a low-lag baseline, and it is not free. The endpoint sits at the edge of the fitted range, the point of **maximum leverage and widest prediction interval**. It is the least well determined value on the line, and it is the one the indicator reports. Two consequences follow directly:

1. **The endpoint overshoots at turns.** When a trend ends, the fitted slope is still the old slope, and extrapolating it one more bar carries the baseline past where price is going. The LSMA characteristically overshoots and then snaps back.
2. **A single outlier at the window edge is maximally damaging.** High-leverage points — those far from `x̄` — pull the fitted slope hardest. The most recent bar is a maximum-leverage point *and* the bar the endpoint is read at, so an outlier there corrupts both the slope and the reading it produces.

## How badly crypto violates the assumptions

OLS is unbiased and efficient — the Gauss-Markov result — under a specific set of conditions. Crypto breaks most of them, and the breakages are not marginal.

| Assumption | What it requires | Crypto reality |
|---|---|---|
| Linearity | The true relationship is a straight line | Price paths curve; momentum accelerates. The reason [[quadratic-regression]] exists |
| Homoscedasticity | Constant error variance | **Volatility clustering.** Residual variance is regime-dependent and autocorrelated in its own right |
| Independent errors | `e_t` uncorrelated with `e_{t−1}` | **Overlapping windows and autocorrelated returns.** Residuals from a rolling fit are strongly serially dependent by construction |
| Normal errors | Gaussian residuals (for exact inference) | Fat tails, jumps, and gaps. Kurtosis far above 3 |
| No influential outliers | No single point dominates | Wicks, bad prints, exchange glitches — routine on thin perp books |

**Volatility clustering breaks homoscedasticity.** Crypto volatility arrives in bursts: a quiet week followed by a liquidation cascade. A regression fitted across that boundary has residuals whose typical size changes by an order of magnitude within the window. The single `SE` it reports is an average of two incompatible regimes, so it overstates the scale in the quiet part and understates it in the violent part. A z-score built on it means different things at different points in the same window.

**Autocorrelation breaks independence.** OLS standard errors assume each observation contributes fresh information. When residuals are serially correlated — and rolling-window price residuals always are — the effective sample size is far smaller than `n`. The formula divides by the nominal `n`, so the standard errors come out **too small**.

**The consequence is systematically optimistic inference.** t-statistics on the slope are inflated, confidence intervals are too narrow, and "the trend is statistically significant at 1%" is a statement that has quietly assumed away the two things most wrong with the data. This is not a small correction: with strong positive autocorrelation, nominal standard errors can understate the true uncertainty by a factor of two or more. Newey-West / HAC standard errors are the standard repair and are essentially never applied inside a trading indicator.

The practical position for [[stretch-revert]]: **use the regression for its point estimate and its residual scale, and do not use its p-values for anything.** The line is a useful summary of the window. The inference machinery attached to it is not licensed by this data, and treating a significant slope t-stat as evidence of a real trend is one of the quieter ways [[overfitting]] enters a strategy.

## Sensitivity to outliers

The breakdown point of an estimator is the fraction of the data that can be replaced with arbitrary values before the estimate can be driven anywhere at all.

| Estimator | Breakdown point |
|---|---|
| OLS slope ([[least-squares-moving-average\|LSMA]]) | **0%** |
| Sample mean ([[simple-moving-average\|SMA]]) | **0%** |
| [[theil-sen-regression\|Theil-Sen]] slope | **~29.3%** |
| Median | 50% |

Zero means literally one point. Move a single close far enough and the OLS slope goes wherever you want, without limit, because squaring the error means the objective function is dominated by whichever point is furthest away. A 25-bar window containing one absurd wick does not produce a slightly wrong fit; it produces a fit determined by the wick.

The compounding failure is worse than the direct one. An outlier corrupts the **numerator** of a z-score (it tilts the line, moving the baseline and therefore the residual) *and* the **denominator** (its own squared residual inflates `SE`). The two errors do not reliably cancel, and their net effect is that a large genuine dislocation can arrive with a *smaller* measured z-score than a modest one. That specific pathology is the subject of [[median-absolute-deviation]], which is the robust denominator the family currently lacks.

[[theil-sen-regression|Theil-Sen]] fixes the numerator by replacing least squares with a median of pairwise slopes. It costs O(n²) and it is slow at genuine structural breaks — robustness and responsiveness are the same dial.

## Extension to polynomial fits

"Linear" refers to linearity **in the coefficients**, not in `x`. Fitting `y = a + b·x + c·x²` is still a linear model, solved by the same normal equations with an extra column in the design matrix. That is [[quadratic-regression]], the third member of the regression group: it lets the baseline curve, so an accelerating move is fitted rather than treated as a growing residual.

The trade-off is standard and unforgiving. Each added term:

- fits the in-sample window better (`R²` cannot decrease when you add a term — it is mechanically non-decreasing, which is why `R²` alone can never justify a higher order);
- makes the **endpoint extrapolation wilder**, because a quadratic's slope at the window edge can be far steeper than any straight line's;
- adds a degree of freedom to the [[overfitting]] surface.

Above second order this becomes untenable fast. A cubic or quartic fitted to 25 noisy closes and read at its endpoint produces a baseline that can be several percent away from price for purely numerical reasons. The regression group stops at order two for good reason.

## Role in stretch-revert

In [[stretch-revert]] the baseline defines fair value and the trade fades `price − baseline`. For the regression members that residual is not a heuristic distance — it is a defined statistical object with its own scale:

- **[[least-squares-moving-average|LSMA]]** — OLS read at the endpoint. Low-lag baseline; the residual is the stretch, `SE` is its natural scale.
- **[[theil-sen-regression|Theil-Sen]]** — the robust replacement for the same fit, at O(n²) cost. Runs at 1× leverage in the live family.
- **[[quadratic-regression]]** — the curved version, for windows where momentum is accelerating.

The eleven averaging-based members ([[alma|ALMA]], [[frama|FRAMA]], [[vidya|VIDYA]], [[kama|KAMA]], [[hull-moving-average|HMA]], [[triple-exponential-moving-average|TEMA]], [[zero-lag-exponential-moving-average|ZLEMA]], [[jurik-moving-average|JMA]], [[laguerre-filter]], [[supersmoother-filter]], [[kalman-filter-trading|Kalman]]) produce a number, and price's distance from it mixes genuine displacement with the smoother's mechanical lag. There is no model, so there is no principled answer to how big a deviation *should* be — the band multiple is convention. The regression group's advantage is that this question has an answer.

**The honest caveat.** Having a defined residual scale improves the *measurement*, not the *trade*. A well-measured stretch in a window that is genuinely trending is a well-measured trend, and fading it loses money at any level of statistical rigour. The regression machinery is why the family's [[hurst-exponent]] regime gate is mandatory rather than advisory.

## Parameters and tuning

| Parameter | Typical | Notes |
|---|---|---|
| Window `n` | 14–50 bars | Short windows fit anything; long windows blend regimes and break homoscedasticity worse |
| Read point | endpoint | Midpoint gives SMA-equivalent lag; endpoint gives the LSMA's low lag and widest interval |
| Order | 1 (2 for [[quadratic-regression]]) | `R²` cannot decrease with order, so it can never justify raising it |
| Residual scale | `SE`, or `1.4826 × MAD` | The robust option is the safer default on crypto — see [[median-absolute-deviation]] |
| Entry z | 2.0–3.0 | On whichever scale is chosen; the two are not interchangeable |

**Overfitting warning.** Regression looks parameter-light — a window and an order — and the surrounding choices are where the degrees of freedom hide: window, order, read point, scale estimator, scale window, entry threshold, exit threshold, stop multiple. That is a large grid, and its best cell will look excellent on any history. Because [[stretch-revert]] already runs fourteen estimators, a per-estimator sweep compounds a multiple-comparisons problem that needs [[deflated-sharpe-ratio]] treatment before any result means anything.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the fit runs over; pull well beyond the window length so the residual scale has a stable rolling sample
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread and depth check; a residual smaller than a couple of spreads is not a dislocation regardless of how significant the fit says it is
- `GET /api/v1/derivatives/funding-rates?coin=X` — carry cost on any held reversion
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding into a large residual argues the displacement is real flow rather than noise

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for refitting across cycles and measuring how residual dispersion actually varies by regime
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels since 2020, for scoring residuals only inside range-labelled states
- `GET /api/v1/volatility/regime/{symbol}` — volatility state; the direct read on the homoscedasticity assumption

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] should treat the fit as cheap and the inference as suspect:

- **Report the residual, the scale, and the scale's provenance.** `z = 2.4` is meaningless without knowing whether the denominator was `SE` or `1.4826 × MAD`, and over what window. Log all three; the two scales diverge most in exactly the bars a fade would trade.
- **Never quote a slope p-value as evidence.** Rolling-window price residuals are autocorrelated and heteroscedastic, so nominal standard errors are optimistic and the t-stat is inflated. If significance is genuinely needed, compute HAC standard errors and say so — otherwise use the fit as a point estimate only.
- **Measure the heteroscedasticity rather than assuming it.** Bucket residuals from `GET /api/v1/backtesting/klines` by the volatility state from `GET /api/v1/volatility/regime/{symbol}`. If residual dispersion differs several-fold across buckets, a single `SE` is not a usable scale and the entry threshold means different things in different regimes.
- **Quantify the outlier exposure.** Refit each window with the single largest-residual bar removed and report how far the endpoint moved. A large gap says the 0% breakdown point is binding on that asset, and [[theil-sen-regression|Theil-Sen]] is buying something real there.
- **Check the endpoint against the midpoint.** The gap between the two readings is the extrapolation the LSMA is performing. When it is large, the low-lag advantage has become an overshoot risk, and entries taken against it deserve a higher bar.

## Related

- [[least-squares-moving-average]] — OLS read at the endpoint; the low-lag baseline this page explains
- [[theil-sen-regression]] — the robust alternative fit, ~29.3% breakdown point instead of 0%
- [[quadratic-regression]] — the second-order extension
- [[median-absolute-deviation]] — the robust residual scale that belongs with a robust fit
- [[standard-deviation]] · [[z-score]] — the conventional scale and its normalisation
- [[stretch-revert]] — the strategy family; the residual is the tradable stretch
- [[outliers]] — what a 0% breakdown point exposes you to
- [[stationarity]] · [[autocorrelation]] · [[volatility]] — the assumptions crypto breaks
- [[hurst-exponent]] — the regime gate that decides whether fading a residual is sane
- [[cointegration]] · [[pairs-trading]] · [[beta]] · [[correlation]] — other places regression carries the weight
- [[moving-averages]] · [[simple-moving-average]] · [[exponential-moving-average]] · [[adaptive-moving-averages]] — the averaging alternative, with no model and no residual
- [[alma]] · [[frama]] · [[vidya]] · [[kama]] · [[hull-moving-average]] · [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] · [[jurik-moving-average]] · [[laguerre-filter]] · [[supersmoother-filter]] · [[kalman-filter-trading]] — sibling baselines
- [[bollinger-bands]] — the band formulation of the same deviation idea
- [[overfitting]] · [[deflated-sharpe-ratio]] — the tuning and multiple-comparisons hazards

## Sources

- Gauss, C. F. (1809) and Legendre, A. M. (1805) — the origin of the method of least squares; priority is historically disputed between them.
- The Gauss-Markov theorem (OLS is the best linear unbiased estimator under linearity, homoscedasticity, and uncorrelated errors) is standard textbook material; see any econometrics text, e.g. Greene, *Econometric Analysis*.
- Newey, W. K. & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica* 55(3). The standard repair for the two assumption failures described above.
- Rousseeuw, P. J. & Leroy, A. M. (1987). *Robust Regression and Outlier Detection*. Framework for the breakdown-point comparisons in the outlier section.
- Volatility clustering as a stylised fact of financial returns dates to Mandelbrot (1963) and is formalised in the ARCH/GARCH literature (Engle 1982, Bollerslev 1986).

No vault source-summary page covers linear regression. The application-specific claims about [[stretch-revert]] on this page are derived from the family page and from the arithmetic of the fit, not from a measured backtest.
