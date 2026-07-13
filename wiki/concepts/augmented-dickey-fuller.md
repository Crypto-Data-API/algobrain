---
title: "Augmented Dickey-Fuller Test"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [quantitative, mean-reversion, pairs-trading, backtesting, statistical-arbitrage]
aliases: ["Augmented Dickey Fuller", "ADF Test", "ADF", "Dickey-Fuller Test", "Unit Root Test"]
domain: [quantitative]
prerequisites: ["[[stationarity]]", "[[mean-reversion]]"]
difficulty: advanced
related: ["[[stationarity]]", "[[cointegration]]", "[[mean-reversion]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[hurst-exponent]]", "[[half-life-of-mean-reversion]]", "[[ornstein-uhlenbeck]]", "[[random-walk-theory]]", "[[engle-granger]]", "[[backtesting]]"]
---

The **Augmented Dickey-Fuller (ADF) test** is a statistical hypothesis test for the presence of a *unit root* in a time series — equivalently, a test of whether the series is non-[[stationarity|stationary]] (trending / [[random-walk-theory|random-walk]]-like) versus mean-reverting. It is the workhorse stationarity test in [[pairs-trading]] and [[statistical-arbitrage]], used to decide whether a price series or a spread between two assets reverts to a mean and is therefore tradable. It extends the original 1979 Dickey-Fuller test by adding lagged difference terms so the test remains valid when the series has higher-order [[autocorrelation]].

## The Hypothesis

A simple autoregressive model is `y_t = ρ·y_{t-1} + ε_t`. If ρ = 1 the series has a unit root (a [[random-walk-theory|random walk]] — shocks are permanent and the series is non-stationary); if |ρ| < 1 the series is mean-reverting. The ADF test reparameterizes this and adds *p* lagged differences to absorb autocorrelation (the "augmented" part):

```
Δy_t = α + β·t + γ·y_{t-1} + Σ δ_i·Δy_{t-i} + ε_t
```

Here `γ = ρ − 1`, so testing `γ = 0` is equivalent to testing `ρ = 1`.

- **Null hypothesis (H0):** γ = 0 (ρ = 1) → a unit root is present → series is **non-stationary**.
- **Alternative (H1):** γ < 0 (ρ < 1) → **no** unit root → series is **stationary / mean-reverting**.

The test statistic is the t-ratio on γ. Because under the null this statistic does not follow a standard t-distribution, it is compared against **Dickey-Fuller critical values** (more negative than ordinary t critical values). A test statistic *more negative* than the critical value (or a p-value below 0.05) rejects H0 — evidence of stationarity. The lag order *p* is chosen to whiten residuals, typically via [[aic-bic|AIC/BIC]] minimisation or a rule like ⌊12·(T/100)^{1/4}⌋.

### Deterministic-term variants

The α and β·t terms are optional, and the choice materially affects the critical values and the conclusion. Choose the specification to match the economic prior about the series:

| Variant | Model includes | Use when | Critical values |
|---|---|---|---|
| **No constant, no trend** | only `γ·y_{t-1}` | series fluctuates around zero (e.g. a demeaned spread) | most negative thresholds |
| **Constant (drift)** | `α + γ·y_{t-1}` | series reverts to a non-zero mean | intermediate (the common default) |
| **Constant + trend** | `α + β·t + γ·y_{t-1}` | series may revert around a deterministic trend | least negative thresholds |

Misspecifying the deterministic terms (e.g. omitting a trend that exists) biases the test toward failing to reject — a common source of false "non-stationary" verdicts.

## Worked Interpretation

In Python (`statsmodels.tsa.stattools.adfuller`), a result might return a statistic of **−3.8** with 1%/5%/10% critical values of **−3.43 / −2.86 / −2.57**. Since −3.8 < −3.43, the null is rejected at the 1% level → the series is **stationary** (mean-reverting). A statistic of **−1.2** would fail to reject → treat the series as a random walk and do *not* trade it as mean-reverting.

| Test statistic | vs critical values (1%/5%/10%) | Decision | Interpretation |
|---|---|---|---|
| −3.8 | below −3.43 | reject H0 at 1% | strongly stationary — tradable spread |
| −2.9 | below −2.86, above −3.43 | reject H0 at 5% | stationary at 5% — proceed with caution |
| −2.0 | above −2.57 | fail to reject | random-walk-like — do **not** trade as reversion |
| −1.2 | well above −2.57 | fail to reject | clearly non-stationary |

Remember the direction: **more negative = more stationary = more tradable.** The statistic being negative is not enough — it must be *more negative than the critical value*. A p-value is the convenient summary: p < 0.05 rejects the unit-root null. Cross-check against the [[hurst-exponent]] (H < 0.5) and a short [[half-life-of-mean-reversion|half-life]] for a consistent verdict.

## Relationship to Cointegration

Most price series are individually non-stationary (integrated of order one, **I(1)**) — their levels wander but their first differences are stationary. The value for traders is testing the **spread** between two related assets: under the [[engle-granger|Engle-Granger two-step]] method, you regress one asset on the other (OLS) and run the ADF test on the *residuals*. If the residual spread is stationary, the two assets are [[cointegration|cointegrated]] — a long-run equilibrium relationship — and the spread is a candidate for [[pairs-trading]]. This is the standard gate before deploying a mean-reversion pair.

A subtlety: when ADF is applied to *estimated* residuals (rather than a pre-specified spread), the appropriate critical values are the **Engle-Granger / MacKinnon cointegration critical values**, which are more negative than the standard ADF thresholds because the regression "used up" data to fit the hedge ratio. For more than two assets, the **Johansen test** generalises cointegration testing and estimates the number of cointegrating relationships directly.

## Worked Cointegration Example

Consider two refiners whose prices co-move. Step 1: regress stock A on stock B to get a hedge ratio β = 1.3, forming the spread `S_t = A_t − 1.3·B_t`. Step 2: run ADF on `S_t` (constant, no trend). Suppose the statistic is **−3.5** against a 5% Engle-Granger critical value of about −3.34 → reject the unit-root null → the spread is stationary → the pair is **cointegrated**. You then fit an [[ornstein-uhlenbeck]] process, find a [[half-life-of-mean-reversion|half-life]] of ~12 days, set entry at ±2 standard deviations of the spread and exit at the mean, and re-test the relationship on rolling windows so a structural break does not silently kill the edge.

## How Traders and Quants Use It

ADF is the quantitative filter that separates genuinely mean-reverting spreads from spurious ones that merely *looked* range-bound in a backtest window. Use it to:

- **Screen pairs/baskets** for [[cointegration]] before building a [[statistical-arbitrage]] book.
- **Confirm mean-reversion** alongside complementary measures — the [[hurst-exponent]] (H < 0.5 implies mean-reversion) and the [[half-life-of-mean-reversion]] (from an [[ornstein-uhlenbeck]] fit) that sets holding period and stop horizon.
- **Monitor live spreads** — re-run ADF on a rolling window so you can de-risk or kill a pair when its spread stops being stationary (the cointegration has broken).
- **Avoid overfitting** — a relationship can pass ADF in-sample and break out-of-sample because cointegration is not stable; ADF must be re-run on rolling windows and confirmed walk-forward (see [[backtesting]]).

### Caveats and Pitfalls

- **Low power against near-unit-root processes** — ADF frequently fails to reject the null even when a series is weakly mean-reverting, especially in short samples; a "fail to reject" is *not* proof of a random walk.
- **Structural breaks** — a regime shift (merger, index reconstitution, policy change) can make a genuinely stationary series appear non-stationary, or vice versa; consider break-robust variants (e.g. Zivot-Andrews).
- **Lag-length sensitivity** — too few lags leaves autocorrelation in the residuals (size distortion); too many lags reduces power. Use an information criterion, not a guess.
- **Multiple-testing / data snooping** — screening thousands of pairs guarantees some pass ADF by chance; control the false-discovery rate and demand out-of-sample confirmation.
- **Confirmatory pairing** — practitioners pair ADF with the **KPSS test** (whose null is the *opposite* — stationarity). Agreement (ADF rejects, KPSS fails to reject) gives confidence; disagreement flags a borderline or break-affected series. Treat an ADF pass as **necessary but not sufficient**.

## Related

- [[stationarity]] — the property ADF tests for
- [[random-walk-theory]] — the unit-root null ADF tries to reject
- [[cointegration]] / [[engle-granger]] — the multi-series property built on stationary spreads
- [[pairs-trading]] / [[statistical-arbitrage]] — the strategies that depend on it
- [[hurst-exponent]] — complementary mean-reversion diagnostic
- [[ornstein-uhlenbeck]] — the continuous-time mean-reverting process behind the spread
- [[half-life-of-mean-reversion]] — sizing the holding period
- [[backtesting]] — guarding against in-sample-only cointegration

## Sources

- Dickey, D.A. & Fuller, W.A. (1979), "Distribution of the Estimators for Autoregressive Time Series with a Unit Root," *Journal of the American Statistical Association*.
- Said, S.E. & Dickey, D.A. (1984), "Testing for Unit Roots in Autoregressive-Moving Average Models of Unknown Order," *Biometrika* — the "augmented" extension.
- Engle, R.F. & Granger, C.W.J. (1987), "Co-integration and Error Correction," *Econometrica*.
- MacKinnon, J.G. (2010), "Critical Values for Cointegration Tests" — the response-surface critical values.
- Ernest Chan, *Algorithmic Trading: Winning Strategies and Their Rationale* (2013) — ADF, Hurst, half-life, and cointegration applied to mean-reversion trading.
- statsmodels documentation, `statsmodels.tsa.stattools.adfuller`.
