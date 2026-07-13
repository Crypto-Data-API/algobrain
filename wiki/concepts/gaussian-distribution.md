---
title: "Gaussian Distribution"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [quantitative, risk-management, portfolio-theory, volatility]
aliases: ["Gaussian Distribution", "Normal Distribution", "Bell Curve", "Normal Curve"]
domain: [portfolio-theory, statistics]
prerequisites: ["[[standard-deviation]]"]
difficulty: beginner
related: ["[[gaussian-assumption]]", "[[standard-deviation]]", "[[fat-tails]]", "[[negative-skew]]", "[[value-at-risk]]", "[[volatility]]", "[[black-scholes]]", "[[sharpe-ratio]]", "[[central-limit-theorem]]"]
---

The **Gaussian distribution** (or **normal distribution**, the "bell curve") is the symmetric, two-parameter probability distribution defined entirely by its mean (μ) and standard deviation (σ). It is the most important distribution in classical statistics because of the [[central-limit-theorem|central limit theorem]] — sums of many independent random effects tend toward it — and it is the workhorse assumption underneath most of quantitative finance. Its convenience is also its danger: real asset returns are *not* Gaussian, and treating them as if they were is the deepest source of risk-model failure in markets. This page covers the distribution itself; for the finance-specific critique of assuming it, see [[gaussian-assumption]].

## Definition

The probability density function is:

```
f(x) = (1 / (σ * sqrt(2π))) * exp( -(x - μ)^2 / (2σ^2) )
```

Key properties:

- **Symmetric** about the mean μ (zero skewness).
- **Mesokurtic** — kurtosis exactly 3 (excess kurtosis 0); the tails fall off as `exp(-x^2)`, very fast.
- **Fully described by μ and σ** — no information lives in higher moments.
- **Closed under linear combinations** — a weighted sum of jointly-normal variables is itself normal. This is what makes [[mean-variance-optimization|mean-variance]] portfolio math tractable.

## The Empirical Rule (68–95–99.7)

Under a Gaussian, probability mass concentrates tightly around the mean:

| Range | Probability inside |
|---|---|
| μ ± 1σ | ~68.3% |
| μ ± 2σ | ~95.4% |
| μ ± 3σ | ~99.7% |
| μ ± 4σ | ~99.994% (1 in ~16,000) |
| μ ± 5σ | ~1 in 3.5 million |
| μ ± 6σ | ~1 in 500 million |

This table is the source of every "N-sigma event" headline. A "6-sigma move" should, under the Gaussian, occur about once every ~1.4 million years of daily data. In markets they happen every few years — the clearest possible signal that returns are not Gaussian.

## Why It Dominates Finance

The Gaussian is embedded, often invisibly, in the core toolkit:

- **[[volatility]] as the risk measure** — σ *is* the risk only if returns are Gaussian.
- **[[sharpe-ratio|Sharpe ratio]]** — uses mean and σ alone; complete only under normality.
- **Parametric [[value-at-risk|Value-at-Risk]]** — `VaR = μ − z·σ`, with z from the normal CDF (z = 2.33 for 99%).
- **[[black-scholes|Black-Scholes]]** — assumes log-returns are Brownian, i.e. normally distributed at every horizon.
- **[[bollinger-bands|Bollinger Bands]]** — ±2σ bands implicitly invoke the 95% rule.

## Where the Gaussian Holds — and Where It Breaks

The Gaussian is genuinely correct for many things: measurement errors, aggregates of many small independent effects (via the central limit theorem), and quantities like human height. Taleb's distinction is **Mediocristan** (Gaussian-governed, no single observation dominates the total) vs **Extremistan** (one observation can dwarf the rest).

Financial returns live in **Extremistan**. The documented departures:

- **[[fat-tails|Fat tails]]** — daily equity-index returns show kurtosis of 8–30+, not 3. Extreme moves are orders of magnitude more frequent than the bell curve allows. October 19, 1987 (−20.5% on the S&P 500) was a ~20-sigma event under the Gaussian — effectively impossible — yet it happened.
- **[[negative-skew|Negative skew]]** — equities, credit, and short-vol strategies crash down faster than they rally up; the Gaussian's zero skew misses this entirely.
- **Volatility clustering** — large moves follow large moves; the Gaussian assumes i.i.d. returns with no such memory.
- **Non-stationarity** — μ and σ themselves drift with regime.

## Trading Relevance

Mistaking the Gaussian for reality understates tail risk by factors of 2–10× and is the formal mechanism behind most blow-ups (LTCM, Volmageddon, the GFC Gaussian-copula failure). The practical posture:

- Use σ and the bell curve as a *first-order* descriptor, never the whole story.
- Always report **skew and kurtosis** alongside mean and σ.
- Prefer **historical or stressed VaR** over parametric Gaussian VaR, and use heavy-tailed (Student-t, empirical bootstrap) innovations in stress tests.
- Size positions assuming the realised tail is fatter than the model — the rationale for half-Kelly and tail hedges.

For the full treatment of why the assumption fails and what to do instead, see [[gaussian-assumption]] and [[fat-tails]].

## Related

- [[gaussian-assumption]] — the finance-specific critique of assuming normality
- [[standard-deviation]] — the σ parameter that defines the distribution
- [[fat-tails]] — the kurtosis departure from Gaussian
- [[negative-skew]] — the skewness departure
- [[value-at-risk]] — the most direct casualty of the Gaussian assumption
- [[volatility]] — σ, treated as "risk" under normality
- [[black-scholes]] — the option-pricing instance
- [[central-limit-theorem]] — why the Gaussian arises so often

## Sources

- Sheldon Ross, *A First Course in Probability* — standard reference for the normal distribution and CLT.
- Mandelbrot, Benoit (1963) "The Variation of Certain Speculative Prices," *Journal of Business* — foundational documentation of fat tails versus the Gaussian in financial data.
- Cont, Rama (2001) "Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues," *Quantitative Finance* — survey of documented departures from normality.
- Taleb, Nassim, *The Black Swan* (2007) — Mediocristan vs Extremistan; the epistemic critique of the bell curve in finance.
