---
title: "Expected Return"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [portfolio-theory, valuation, risk-management, quantitative]
aliases: ["Expected Return", "Expected Returns", "Expected Value of Return"]
related: ["[[capm]]", "[[sharpe-ratio]]", "[[geometric-mean]]", "[[kelly-criterion]]", "[[mean-variance-optimization]]", "[[risk-premium]]", "[[ergodicity-economics]]", "[[equity-risk-premium]]"]
domain: [portfolio-theory]
prerequisites: ["[[probability]]", "[[volatility]]"]
difficulty: intermediate
---

**Expected return** is the probability-weighted average of all possible returns from an asset or strategy — the mean of the return distribution. It is the central input to almost every allocation, pricing, and position-sizing decision in finance, and the quantity that risk is traded off against. Crucially, expected return is an *ex ante* (forward-looking) estimate, not a realized outcome; the gap between the two — and the fact that the *arithmetic* expected return is not what a single investor actually compounds — is where most allocation mistakes are made.

## Definition and formula

For a discrete set of outcomes, the expected return is:

```
E[R] = Σ p_i · R_i
```

where `p_i` is the probability of scenario `i` and `R_i` is the return in that scenario. For a continuous distribution it is the integral `E[R] = ∫ R · f(R) dR`, where `f(R)` is the probability density.

For a **portfolio**, expected return is the weighted average of constituent expected returns (this is exactly linear — unlike portfolio variance):

```
E[R_p] = Σ w_i · E[R_i]
```

with weights `w_i` summing to 1.

## Three ways to estimate it

1. **Historical average.** Use the sample mean of past returns as the estimate. Simple but unstable — sample means have enormous estimation error, and a 10-year mean can be dominated by one or two regimes. Estimation error in means is the single largest source of error in [[mean-variance-optimization|mean-variance optimization]].
2. **Equilibrium / factor models.** [[capm|CAPM]] gives `E[R_i] = R_f + β_i · (E[R_m] − R_f)`: expected return equals the risk-free rate plus beta times the [[equity-risk-premium|market risk premium]]. Multifactor models (Fama-French, Carhart) add value, size, momentum, and quality premia. These tie expected return to compensated [[risk-premium|risk premia]] rather than to noisy historical means.
3. **Building-block / yield-based.** Decompose expected return into observable components: for equities, `dividend yield + expected earnings growth + valuation change`; for bonds, `yield to maturity ± expected default/roll`. This is Antti Ilmanen's approach in *Expected Returns* (see [[book-expected-returns-antti-ilmanen]]) and tends to be more stable than raw historical means.

## Arithmetic vs geometric: the trap

The expected (arithmetic mean) return is **not** the rate at which a single investor's wealth compounds. For multiplicative (compounding) returns, wealth grows at the **time-average / [[geometric-mean|geometric mean]]** rate, which is lower than the arithmetic mean by the *variance drag*:

```
g ≈ E[R] − 0.5 · σ²
```

A strategy with +10% arithmetic expected return and 40% volatility compounds at roughly `0.10 − 0.5·0.16 = 0.02`, just 2% — and a high enough volatility makes the geometric return negative even with a positive expected return. This is the core lesson of [[ergodicity-economics]]: maximize the *time-average* growth rate, not the ensemble-average return. It is also why [[kelly-criterion|Kelly sizing]] caps leverage despite positive expected return.

## Trading relevance

- **Position sizing.** [[kelly-criterion|Kelly]] and fractional-Kelly sizing are functions of expected return relative to variance. Overestimating `E[R]` leads directly to over-betting and ruin.
- **Risk-adjusted comparison.** The [[sharpe-ratio|Sharpe ratio]] is `(E[R] − R_f) / σ` — expected *excess* return per unit of risk — the standard way strategies are ranked.
- **Optimization.** [[mean-variance-optimization|Mean-variance optimization]] takes the vector of expected returns as its primary input; because these are so error-prone, robust methods (Black-Litterman, shrinkage, equal-weight, risk parity) deliberately down-weight the expected-return estimate.
- **Backtesting honesty.** A naive backtest's mean return overstates live expected return after [[slippage]], fees, [[overfitting]], and survivorship. Net, deflated expected return is what matters — see [[deflated-sharpe-ratio]].
- **Skew matters.** Two strategies with identical expected return are not equivalent: a positive-skew payoff and a negative-skew carry payoff compound very differently because of the variance/skew drag. Expected return alone is an incomplete description of an opportunity.

## Common pitfalls

- Treating a realized backtest mean as the forward expected return.
- Confusing arithmetic expected return with what actually compounds.
- Ignoring estimation error — expected-return estimates have wide confidence intervals.
- Reporting gross rather than net (after-cost) expected return.

## Related

- [[capm]]
- [[sharpe-ratio]]
- [[geometric-mean]]
- [[kelly-criterion]]
- [[mean-variance-optimization]]
- [[risk-premium]]
- [[equity-risk-premium]]
- [[ergodicity-economics]]
- [[deflated-sharpe-ratio]]

## Sources

- Antti Ilmanen, *Expected Returns: An Investor's Guide to Harvesting Market Rewards* (Wiley, 2011) — the building-block decomposition (see [[book-expected-returns-antti-ilmanen]])
- Harry Markowitz, "Portfolio Selection," *Journal of Finance* (1952) — expected return as the objective in mean-variance theory
- William Sharpe, "Capital Asset Prices," *Journal of Finance* (1964) — equilibrium expected return (CAPM)
- Eugene Fama & Kenneth French, "Common Risk Factors in the Returns on Stocks and Bonds," *Journal of Financial Economics* (1993)
- Ole Peters, "The ergodicity problem in economics," *Nature Physics* (2019) — arithmetic vs time-average return
