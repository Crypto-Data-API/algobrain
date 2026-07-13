---
title: "Hurst Exponent"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [quantitative, mean-reversion, trend-following, indicators, backtesting]
aliases: ["Hurst Exponent", "Hurst", "H exponent"]
related: ["[[mean-reversion]]", "[[trend-following]]", "[[momentum]]", "[[random-walk]]", "[[random-walk-theory]]", "[[autocorrelation]]", "[[fractional-differentiation]]", "[[statistical-arbitrage]]", "[[pairs-trading]]", "[[cointegration]]", "[[stationarity]]", "[[augmented-dickey-fuller]]", "[[half-life-of-mean-reversion]]", "[[regime-detection]]"]
domain: [quantitative]
prerequisites: ["[[random-walk]]", "[[autocorrelation]]"]
difficulty: advanced
---

The **Hurst exponent** (*H*) is a statistic between 0 and 1 that measures the long-term memory (long-range dependence) of a time series -- whether it tends to trend, mean-revert, or follow a [[random-walk]]. Originally developed by hydrologist Harold Edwin Hurst (1951) to size the Aswan Dam reservoir against long-memory Nile flooding, it was later connected to fractional Brownian motion and fractal geometry by Benoit Mandelbrot. In quantitative finance it is widely used to classify a series' behaviour and to decide whether a [[trend-following]] or [[mean-reversion]] approach is appropriate -- it is a *regime diagnostic*, not a trade trigger.

## Interpretation

| Hurst value | Behaviour | Autocorrelation of increments | Trading implication |
|---|---|---|---|
| **H = 0.5** | [[random-walk]] / Brownian motion (no memory) | Zero | No edge from persistence; the [[random-walk-theory|random-walk]] null holds |
| **0.5 < H < 1.0** | Persistent / trending (fractional Brownian motion) | Positive (positive moves follow positive) | Past direction tends to continue -- favours [[momentum]] / [[trend-following]] |
| **0 < H < 0.5** | Anti-persistent / mean-reverting | Negative (moves tend to reverse) | Past moves tend to reverse -- favours [[mean-reversion]] / [[pairs-trading]] |

The closer H is to 1, the stronger the trend persistence; the closer to 0, the stronger the tendency to revert. Note the asymmetry of strength: most tradable financial series sit *close* to 0.5 (e.g. 0.45-0.55), so a Hurst meaningfully away from the random-walk null is the exception, not the rule.

## How It Is Estimated

Two common approaches:

1. **Rescaled range (R/S) analysis** -- the original method. For sub-series of increasing length *n*, compute the range *R* of the cumulative deviations from the mean, divide by the standard deviation *S*, and average across windows. R/S scales as *c·n^H*, so H is the slope of log(R/S) regressed on log(n):

   $$\mathbb{E}\left[\frac{R(n)}{S(n)}\right] = c \cdot n^{H} \quad\Longrightarrow\quad \log\!\left(\frac{R}{S}\right) = \log c + H\,\log n$$

2. **Variance of the lagged differences (variance-ratio / "var of lag")** -- the variance of the *τ*-lagged price difference scales with the lag as:

   $$\operatorname{Var}\!\big(y_t - y_{t-\tau}\big) \;\propto\; \tau^{\,2H}$$

   Regressing log-variance on log-lag and *halving* the slope gives H. This is the method popularised by Ernest Chan for testing mean reversion; for a pure random walk the variance grows linearly with τ (slope ≈ 1, H ≈ 0.5).

The two methods can disagree on short, noisy financial series, and R/S in particular is biased upward on small samples; practitioners use corrections (e.g. the Anis-Lloyd / Peters adjustment), de-trend the series first, and report confidence intervals or bootstrap the H estimate.

## Worked Interpretation

Suppose you take five years of daily log-prices of a candidate [[pairs-trading]] spread and run the variance-of-lag estimator over lags τ = 2…100 days. The log-variance vs log-lag regression has a slope of **0.78**. Halving gives **H ≈ 0.39**.

- H = 0.39 < 0.5 → the spread is **anti-persistent / mean-reverting**, consistent with a tradable reversion pair.
- The same data run through an [[augmented-dickey-fuller|ADF]] test returns a statistic of −3.6 (below the 5% critical value of −2.86) → **rejects the unit-root null**, confirming stationarity.
- Fitting an [[ornstein-uhlenbeck]] process to the spread yields a [[half-life-of-mean-reversion|half-life]] of ~8 days → sets a sensible holding horizon and stop.

All three agree: the spread mean-reverts, and ~8 days is the reversion timescale. By contrast, an outright equity index over the same window typically returns H ≈ 0.50-0.55 — *not* reliably tradable as either trend or reversion at that frequency. The Hurst value alone never authorises a trade; it screens which *family* of strategy the data can even support.

## Relationship to Mean Reversion and Stationarity

A series with H < 0.5 mean-reverts, which connects directly to the [[half-life-of-mean-reversion|half-life of mean reversion]] estimated from an [[ornstein-uhlenbeck]] / [[augmented-dickey-fuller|ADF]] framework: low H, a stationary ADF result, and a short OU half-life are three independent ways of saying the same thing — the series reverts. They are complementary because they fail differently: ADF has [[augmented-dickey-fuller#Caveats|low power]] in short samples, while Hurst is sensitive to estimator settings. In [[statistical-arbitrage]] and [[cointegration]] work, the Hurst exponent of a candidate spread is one screen (alongside ADF on the residual) for whether a pair is worth trading.

## Limitations and Pitfalls

- **Non-stationarity of H itself**: H drifts over time and across [[regime-detection|regimes]]; a single static estimate over a long window blends incompatible regimes (e.g. a calm range followed by a trending breakout averages to a misleading ~0.5).
- **Estimator sensitivity**: results depend heavily on method, window length, and lag range; the same series can look trending or reverting under different settings. Always report the method and window.
- **Small-sample bias**: R/S overestimates H on short series; financial windows of a few hundred points carry wide confidence intervals around the estimate.
- **Weak edge**: an H meaningfully away from 0.5 indicates *statistical* memory but does not guarantee a profitable, cost-covering strategy. After transaction costs and slippage a marginal H of 0.45 may be untradable.
- **Confounding with volatility clustering**: GARCH-type volatility persistence can masquerade as long memory in the level series; apply the test to returns/spreads, not raw prices, and be wary of conflating memory in volatility with memory in direction.

## How Traders and Quants Use It

The Hurst exponent is most useful as a **regime classifier and strategy selector** rather than a standalone signal. Common applications:

| Use case | How H is applied |
|---|---|
| **Strategy gating** | Only deploy a [[pairs-trading]] / [[mean-reversion]] book when the spread's *rolling* Hurst is comfortably below 0.5; only scale [[trend-following]] exposure up when H on the trade horizon rises above ~0.55. |
| **Regime detection** | Compute H on a rolling lookback (e.g. 250 days) to flag transitions between trending and ranging regimes (see [[regime-detection]]). |
| **Spread screening** | In [[statistical-arbitrage]], pre-filter a universe of candidate spreads, keeping only low-H, ADF-stationary pairs. |
| **Risk gating** | Reduce mean-reversion sizing when a previously low-H spread drifts toward 0.5 — a sign the edge is decaying or the regime is shifting. |
| **Feature for ML models** | Rolling H is a popular input feature for regime-classification and meta-labelling models. |

Computed on a rolling window, it helps avoid the classic error of running a mean-reversion book in a trending market (or vice-versa). Because the estimate is noisy, it is best combined with stationarity tests ([[augmented-dickey-fuller|ADF]], [[half-life-of-mean-reversion|half-life]]) and treated as a confirmation indicator, never trusted in isolation.

## Related

- [[mean-reversion]] -- low-H regime strategy
- [[trend-following]] -- high-H regime strategy
- [[momentum]] -- persistence the high-H regime captures
- [[random-walk]] / [[random-walk-theory]] -- the H = 0.5 null
- [[autocorrelation]] -- the underlying property H summarises
- [[stationarity]] -- the property low-H series tend to share
- [[augmented-dickey-fuller]] -- complementary unit-root / stationarity test
- [[half-life-of-mean-reversion]] -- sizing the reversion horizon for low-H spreads
- [[cointegration]] / [[pairs-trading]] / [[statistical-arbitrage]] -- uses Hurst to screen spreads
- [[regime-detection]] -- rolling Hurst as a regime indicator

## Sources

- H.E. Hurst, "Long-term storage capacity of reservoirs," *Transactions of the American Society of Civil Engineers* (1951).
- Ernest P. Chan, *Algorithmic Trading: Winning Strategies and Their Rationale* (2013) -- variance-ratio estimation of the Hurst exponent for mean-reversion testing.
- B.B. Mandelbrot & J.R. Wallis, work on R/S analysis and fractional Brownian motion.
- A.A. Anis & E.H. Lloyd, "The expected value of the adjusted rescaled Hurst range of independent normal summands," *Biometrika* (1976) -- small-sample bias correction for R/S.
- General market knowledge; no specific wiki source ingested yet beyond the above references.
