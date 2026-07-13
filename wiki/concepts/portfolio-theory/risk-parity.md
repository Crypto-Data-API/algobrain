---
title: Risk Parity
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - portfolio-theory
  - risk-management
  - quantitative
aliases:
  - Risk Parity
  - risk-parity
  - Equal Risk Contribution
domain: [portfolio-theory, risk-management]
prerequisites: ["[[volatility]]", "[[diversification]]", "[[modern-portfolio-theory]]"]
difficulty: advanced
related: ["[[ray-dalio]]", "[[bridgewater-associates]]", "[[all-weather-portfolio]]", "[[diversification]]", "[[risk-budgeting]]", "[[leverage]]", "[[volatility]]", "[[correlation]]"]
---

# Risk Parity

**Risk parity** is a portfolio allocation strategy that balances *risk contributions* across asset classes rather than allocating by capital weight. Each asset class is sized so that it contributes the same amount to overall portfolio [[volatility]] — an "equal risk contribution" (ERC) portfolio.

Popularized by [[ray-dalio]] at [[bridgewater-associates]], risk parity is the foundation of the [[all-weather-portfolio]]. It typically uses [[leverage]] to equalize returns across low-volatility assets like [[bonds]].

## The Math: Risk Contribution

The total variance of a portfolio with weight vector **w** and covariance matrix **Σ** is σ²ₚ = **wᵀΣw**. The *marginal* contribution to risk of asset *i* is the partial derivative ∂σₚ/∂wᵢ = (Σw)ᵢ / σₚ. The asset's *total risk contribution* is:

```
RCᵢ = wᵢ · (Σw)ᵢ / σₚ        and   Σᵢ RCᵢ = σₚ
```

A risk-parity portfolio solves for weights such that **RCᵢ = σₚ / N** for all *N* assets — every position carries an equal slice of total portfolio risk. With no off-diagonal correlations, this collapses to the simple "inverse-volatility" weighting wᵢ ∝ 1/σᵢ. With correlations present, the solution is found numerically (convex optimization or cyclical coordinate descent), because lowering one asset's weight changes every other asset's marginal contribution.

## How It Differs from Equal Weight

A naive equal-weight portfolio (e.g., 25% stocks, 25% bonds, 25% commodities, 25% gold) is not risk-balanced because stocks are far more volatile than bonds. In a 60/40 stock/bond portfolio, stocks typically contribute 85-90% of total portfolio risk. Risk parity solves this by asking: how much capital should each asset class receive so that each contributes the same amount of risk?

For example, if stocks are 3x more volatile than bonds, a risk parity approach would allocate roughly 3x more capital to bonds than to stocks, equalizing their risk contributions.

## The Role of Leverage

Because low-volatility assets like bonds have lower expected returns, a risk-parity portfolio allocated purely by risk would have a lower total return than a stock-heavy portfolio. To address this, risk parity strategies use [[leverage]] -- borrowing to scale up the overall portfolio so that its expected return matches or exceeds traditional allocations while maintaining superior diversification. This makes the strategy sensitive to borrowing costs and interest rate environments.

## Bridgewater's All Weather

[[bridgewater-associates]]'s All Weather fund, launched in 1996, is the most famous institutional risk parity strategy. The simplified retail version, the [[all-weather-portfolio]], applies the same principles without explicit leverage. Bridgewater's insight was that diversifying across economic regimes (growth, recession, inflation, deflation) through risk-balanced asset classes produces more consistent returns than traditional portfolios.

## Criticisms

Risk parity faced significant scrutiny in 2022 when both stocks and bonds declined simultaneously (a positive stock-bond [[correlation]] regime), breaking the negative-correlation assumption that underpins the approach. Critics also note that leverage amplifies losses during correlated drawdowns, that the strategy's reliance on historical volatility estimates is fragile during regime changes, and that systematic risk-parity selling during volatility spikes can be a procyclical amplifier of market stress (a concern raised after the February 2018 "Volmageddon" episode). See [[risk-budgeting]] for related portfolio construction techniques.

## Trading and Portfolio Relevance

- **Diversification of risk, not capital** — the core insight is that capital weights badly misrepresent where portfolio risk actually sits. A 60/40 portfolio is, in risk terms, ~90% an equity bet.
- **Regime dependence** — risk parity implicitly bets that bonds hedge equities. When the stock-bond [[correlation]] flips positive (typically in inflation-driven sell-offs), the diversification benefit collapses and leverage hurts.
- **Volatility targeting** — most live implementations layer a portfolio-level volatility target (e.g. 10% annualized) on top of ERC weights, scaling gross exposure up in calm markets and down in turbulent ones.
- **Capacity and cost** — leverage is obtained cheaply via futures (bond, equity-index) rather than borrowing cash, making funding cost and roll yield material to net returns.

## Related

- [[ray-dalio]]
- [[bridgewater-associates]]
- [[all-weather-portfolio]]
- [[diversification]]
- [[risk-budgeting]]
- [[leverage]]
- [[correlation]]
- [[volatility]]

## Sources

- Maillard, S., Roncalli, T., Teïletche, J. (2010). *"The Properties of Equally Weighted Risk Contribution Portfolios."* *Journal of Portfolio Management* 36 (4): 60–70.
- Qian, E. (2005). *"Risk Parity Portfolios: Efficient Portfolios Through True Diversification."* PanAgora Asset Management.
- Asness, C., Frazzini, A., Pedersen, L. H. (2012). *"Leverage Aversion and Risk Parity."* *Financial Analysts Journal* 68 (1): 47–59.
- Roncalli, T. (2013). *Introduction to Risk Parity and Budgeting.* Chapman & Hall/CRC.
- Bridgewater Associates. *"The All Weather Story"* (firm white paper).
