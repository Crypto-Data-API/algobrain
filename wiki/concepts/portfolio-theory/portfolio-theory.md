---
title: "Modern Portfolio Theory"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [portfolio-theory, quantitative, risk-management]
aliases: ["MPT", "Portfolio Theory", "Markowitz", "Mean-Variance Optimization"]
domain: [portfolio-theory]
prerequisites: ["[[diversification]]", "[[correlation]]", "[[volatility]]"]
difficulty: intermediate
related: ["[[risk-management]]", "[[diversification]]", "[[correlation]]", "[[sharpe-ratio]]", "[[capital-asset-pricing-model]]", "[[volatility]]", "[[long-short-equity]]"]
---

Modern Portfolio Theory (MPT) is a mathematical framework, introduced by Harry Markowitz in 1952, for constructing portfolios that maximize expected return for a given level of risk (or minimize risk for a target return). Its central insight is that a portfolio's risk depends not only on the volatility of its individual holdings but on the [[correlation|correlations]] between them, so combining imperfectly correlated assets can lower total risk without sacrificing expected return.

## Overview

MPT treats risk as the standard deviation (or variance) of portfolio returns and seeks the portfolio that offers the best risk/return trade-off. It reframed investing from picking individual "good" assets to engineering a *combination* whose aggregate behaviour is superior to any of its parts. Markowitz won the 1990 Nobel Memorial Prize in Economic Sciences (shared with William Sharpe and Merton Miller) for this work.

## The Mathematics

For a portfolio of *n* assets with weights *w*, expected returns *μ*, and covariance matrix *Σ*:

```
Expected return:   E(Rp) = Σ wᵢ · μᵢ           (= wᵀμ)
Portfolio variance: σp²  = Σ Σ wᵢ wⱼ σᵢⱼ        (= wᵀΣw)
```

For the simple two-asset case the variance expands to:

```
σp² = wA²σA² + wB²σB² + 2 wA wB ρAB σA σB
```

The cross term `2 wA wB ρAB σA σB` is the engine of diversification: when the [[correlation]] ρAB is less than 1, portfolio volatility is *less* than the weighted average of the individual volatilities. With ρ = -1, risk can in principle be driven to zero with the right weights.

## The Efficient Frontier

Plotting every possible portfolio in risk (x-axis) vs. expected-return (y-axis) space produces a bullet-shaped region. The **efficient frontier** is the upper-left boundary: the set of portfolios that deliver the maximum expected return for each level of risk. Any portfolio below the frontier is dominated — you could earn more return at the same risk, or the same return at lower risk. Mean-variance optimization is the procedure of solving for the weights that place a portfolio on this frontier subject to constraints (e.g., weights sum to 1, no shorting).

## Capital Market Line and the Tangency Portfolio

Introducing a risk-free asset (e.g., T-bills) lets investors hold a blend of the risk-free asset and one specific risky portfolio — the **tangency portfolio**, where a line drawn from the risk-free rate is tangent to the efficient frontier. This line is the **Capital Market Line**, and its slope is the [[sharpe-ratio|Sharpe ratio]] of the tangency portfolio. The tangency portfolio maximizes:

```
Sharpe Ratio = (E(Rp) − Rf) / σp
```

This result — that all investors should hold the same risky portfolio and adjust risk only via the risk-free/leverage mix — is the bridge from MPT to the [[capital-asset-pricing-model|CAPM]].

## Limitations

MPT's assumptions are routinely violated in practice:

- **Returns are not normally distributed** — markets exhibit fat tails and skew; variance understates true tail risk.
- **Correlations are unstable** — in crises correlations spike toward 1.0, collapsing diversification exactly when it is needed most, as the [[2008-global-financial-crisis]] demonstrated.
- **Estimation error** — optimizers are extremely sensitive to the input estimates of expected returns; small errors produce wildly concentrated, unstable weights ("error maximization"). Practitioners respond with shrinkage estimators, [[risk-parity]], Black-Litterman, and Hierarchical Risk Parity (de Prado).
- **Single-period, static** — the canonical model ignores transaction costs, taxes, and multi-period dynamics.

## Trading and Portfolio Relevance

Even discretionary traders who never run an optimizer benefit from MPT's core discipline: the goal is return *per unit of risk*, not raw return, and uncorrelated bets beat correlated ones. Five long positions in highly correlated names are effectively one large bet. Practitioners extend the framework beyond long-only optimization: [[long-short-equity]] strips out market beta to isolate stock-selection alpha, while [[risk-parity]] allocates by risk contribution rather than capital. (Source: [[itpm-education-methodology-overview]])

## Sources

- Markowitz, H. (1952). "Portfolio Selection." *The Journal of Finance*, 7(1), 77–91.
- Sharpe, W.F. (1964). "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk." *The Journal of Finance*.
- Bodie, Kane & Marcus, *Investments* — standard textbook treatment of mean-variance optimization and the efficient frontier.
- [[itpm-education-methodology-overview]] — practitioner extensions (long/short, top-down allocation).

## Related

- [[diversification]] -- the practical lesson of MPT
- [[correlation]] -- drives the diversification benefit
- [[sharpe-ratio]] -- the risk-adjusted return measure MPT maximizes
- [[capital-asset-pricing-model]] -- the equilibrium model that extends MPT
- [[risk-management]] -- MPT as the foundation of institutional risk frameworks
- [[long-short-equity]] -- extension allowing short positions
