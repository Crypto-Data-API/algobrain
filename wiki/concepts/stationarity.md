---
title: "Stationarity"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [quantitative, mean-reversion, backtesting, algorithmic]
aliases: ["Stationarity", "Stationary Time Series", "Weak Stationarity"]
domain: [market-microstructure, backtesting]
prerequisites: ["[[mean-reversion]]", "[[standard-deviation]]"]
difficulty: advanced
related: ["[[cointegration]]", "[[mean-reversion]]", "[[statistical-arbitrage]]", "[[pairs-trading]]", "[[random-walk]]", "[[autocorrelation]]", "[[overfitting-detection]]"]
---

Stationarity is the statistical property of a time series whose distribution does not change over time — its mean, variance, and autocorrelation structure stay constant. Stationarity is foundational to quantitative trading because most statistical models (regression, ARIMA, mean-reversion signals) assume it, and because a tradeable [[mean-reversion]] edge exists only when the quantity being traded is stationary. Raw asset *prices* are almost never stationary; *returns* and well-constructed *spreads* often are.

## Strict vs Weak Stationarity

- **Strict stationarity**: the full joint distribution of the series is invariant to time shifts. This is a strong condition rarely met or testable in practice.
- **Weak (covariance) stationarity**: only the first two moments are time-invariant — constant mean, constant variance, and an autocovariance that depends only on the lag, not on absolute time. This is the working definition used in finance.

A weakly stationary series fluctuates around a fixed level with stable dispersion. A non-stationary series wanders without an anchor (a [[random-walk]]) or has a deterministic trend or changing variance.

## Why Prices Are Non-Stationary but Spreads Can Be

A stock price typically behaves like a [[random-walk]] with drift: its mean rises over time and its variance grows without bound, so it is non-stationary (it has a "unit root"). You cannot mean-revert against a price level, because there is no fixed mean to revert to. This is why [[trend-following|trend-following]] strategies trade prices directly.

[[mean-reversion]] and [[statistical-arbitrage]] strategies instead trade a *constructed* series engineered to be stationary — most often a [[cointegration|cointegrated]] spread between two assets ($S = P_A - \beta P_B$). Two individually non-stationary prices can have a linear combination that *is* stationary; that combination is the only thing that genuinely mean-reverts and is therefore tradeable. The z-score entries used in [[pairs-trading]] are only meaningful if the spread is stationary, because z-score assumes a fixed mean and standard deviation.

## Testing for Stationarity

Standard unit-root and stationarity tests:

- **Augmented Dickey-Fuller (ADF)** — null hypothesis: a unit root (non-stationary). Rejecting the null (low p-value) is evidence of stationarity.
- **KPSS** — null hypothesis: stationarity. Useful as a complement to ADF because the nulls are reversed; agreement between the two is stronger evidence.
- **Phillips-Perron** — a non-parametric variant of ADF robust to some forms of heteroskedasticity and autocorrelation.
- **Hurst exponent** — H < 0.5 indicates mean-reverting (anti-persistent) behavior, H = 0.5 a random walk, H > 0.5 a trending series.
- **Ornstein-Uhlenbeck fit / half-life** — once stationarity is established, the [[ornstein-uhlenbeck|OU]] mean-reversion speed gives a half-life, which tells you whether reversion is fast enough to trade after costs.

## Making a Series Stationary

- **Differencing**: first differences of log prices (i.e., log returns) are usually stationary even when prices are not. ARIMA's "I" (integrated) term captures this.
- **Detrending**: removing a deterministic trend.
- **Constructing a cointegrated combination**: the basis of pairs/stat-arb spreads.
- **Variance stabilization**: log transforms or GARCH modeling for changing variance ([[volatility-clustering]]).

## Trading Relevance

Stationarity is the gating assumption behind whether a relationship is tradeable and whether a [[backtesting|backtest]] is trustworthy:

- A spread that tests as stationary in-sample but fails out-of-sample is the classic [[overfitting-detection|overfitting]] trap — testing thousands of pairs guarantees spurious "stationary" spreads by chance (multiple-comparisons bias).
- **Structural breaks** (mergers, regime shifts, index changes) destroy stationarity permanently; a spread that was mean-reverting can re-anchor at a new level and never come back — the single largest source of stat-arb losses.
- Regression of one non-stationary price on another without cointegration produces **spurious regression**: high R² and significant t-stats that are entirely fake. Stationarity testing is the guard against this.
- Most risk and signal models assume stationary inputs; feeding raw prices into a model that expects returns is a common silent error.

## Related

- [[cointegration]] — the mechanism that makes a spread of non-stationary prices stationary
- [[mean-reversion]] — only works on a stationary series
- [[statistical-arbitrage]] — built entirely on stationary spreads
- [[pairs-trading]] — the simplest stationary-spread strategy
- [[random-walk]] — the canonical non-stationary process
- [[autocorrelation]] — part of the stationarity definition
- [[overfitting-detection]] — spurious stationarity from data mining

## Sources

- Hamilton, J. D. *Time Series Analysis* (Princeton, 1994) — definitions of stationarity, unit roots, and the ADF test.
- Engle, R. F. & Granger, C. W. J. (1987). "Co-integration and Error Correction." *Econometrica* — cointegration of non-stationary series (Nobel-winning work).
- Chan, E. P. *Algorithmic Trading: Winning Strategies and Their Rationale* (Wiley, 2013) — practical ADF/Hurst/half-life testing for tradeable mean reversion.
- Granger, C. W. J. & Newbold, P. (1974). "Spurious Regressions in Econometrics." *Journal of Econometrics* — why non-stationary regressions mislead.
