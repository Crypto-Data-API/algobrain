---
title: "Risk Budgeting"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [risk-budgeting, risk-parity, hrp, hierarchical-risk-parity, portfolio-construction, risk-management, quantitative]
aliases: ["Risk Budget Strategy", "Risk Parity Extended", "Hierarchical Risk Parity", "HRP"]
strategy_type: quantitative
timeframe: position
markets: [stocks, bonds]
complexity: advanced
backtest_status: untested
related: ["[[black-litterman]]", "[[portable-alpha]]", "[[cppi]]", "[[garch-volatility]]", "[[regime-detection]]"]
---

# Risk Budgeting

## Overview

Risk budgeting is a portfolio construction methodology that allocates **risk** rather than capital. Instead of deciding "put 60% in stocks and 40% in bonds," risk budgeting asks "how much of my portfolio's total risk should come from equities vs bonds vs alternatives?" and sizes positions accordingly. This is a more principled approach because a 60/40 portfolio is not balanced in risk terms -- equities contribute roughly 90% of portfolio volatility despite being only 60% of capital.

The foundational concept is **risk parity**, popularized by Ray Dalio's All Weather Fund at Bridgewater (launched 1996). Risk parity equalizes the risk contribution of each asset class, typically resulting in a levered bond allocation (since bonds are less volatile, you need more of them to contribute equal risk). The extension to **risk budgeting** allows non-equal risk allocations: you might budget 40% of risk to equities, 30% to bonds, 20% to commodities, and 10% to alternatives, based on your views and return expectations.

**Hierarchical Risk Parity (HRP)**, introduced by Marcos Lopez de Prado in 2016, is a modern variant that uses machine learning (hierarchical clustering) to group correlated assets and allocate risk within and across clusters. HRP avoids the covariance matrix inversion required by traditional optimization, making it more robust to estimation error and suitable for large, ill-conditioned universes. HRP has become increasingly popular among quantitative allocators as a replacement for mean-variance and traditional risk parity.

## How It Works

### Risk Contribution Decomposition
For a portfolio with weights **w** and covariance matrix **Sigma**, the total portfolio volatility is sigma_p = sqrt(w' Sigma w). Each asset's **marginal risk contribution (MRC)** is:

**MRC_i = w_i x (Sigma x w)_i / sigma_p**

The sum of all MRCs equals total portfolio volatility. The **percentage risk contribution** of asset i is MRC_i / sigma_p.

### Risk Parity (Equal Risk Contribution)
Set each asset's percentage risk contribution to 1/N (where N = number of assets). This requires solving:

**w_i x (Sigma x w)_i = w_j x (Sigma x w)_j for all i, j**

This is a non-linear optimization problem solved numerically. The result: low-volatility assets (bonds) get higher weights, high-volatility assets (equities, commodities) get lower weights.

### Risk Budgeting (Custom Budgets)
Instead of equal risk, assign budgets: **b_i** for asset i (where sum of b_i = 1). The objective becomes:

**w_i x (Sigma x w)_i / sigma_p = b_i for all i**

This allows tilting risk toward assets with higher expected risk-adjusted returns.

### Hierarchical Risk Parity (HRP)
1. **Cluster assets** using hierarchical clustering on the correlation matrix (single-linkage or Ward's method).
2. **Quasi-diagonalize** the covariance matrix by reordering assets according to the clustering dendrogram.
3. **Allocate recursively:** Split the portfolio into two sub-clusters, allocate risk between them inversely proportional to their variance, then recurse into each sub-cluster.

HRP requires **no covariance matrix inversion**, making it robust to singularity and estimation noise.

## Rules / Application

### Implementation Steps
1. **Define asset universe:** e.g., US equity, international equity, EM equity, US Treasuries, TIPS, investment-grade bonds, high-yield bonds, commodities, gold, REITs.
2. **Estimate covariance matrix:** Use 3-5 years of daily or weekly returns. Apply Ledoit-Wolf shrinkage or exponentially-weighted moving average for stability. Optionally use [[garch-volatility]] for forward-looking estimates.
3. **Set risk budgets:** Equal budgets for risk parity, or custom based on views. Example: 30% equity risk, 30% bond risk, 20% commodity risk, 20% alternatives.
4. **Solve for weights:** Use numerical optimization (scipy.optimize in Python) or the HRP algorithm.
5. **Apply leverage** (optional): If the risk-parity solution has total portfolio vol below your target (e.g., 5% vol vs 10% target), lever the portfolio 2x using futures. This is the key innovation of risk parity -- leverage to achieve target return while maintaining balanced risk.
6. **Rebalance monthly** or when risk contributions drift by more than 5% from budgets.

### Regime-Conditional Risk Budgets
Combine with [[regime-detection]] to adjust budgets dynamically:
- **Trending/bull regime:** Higher equity risk budget (40%), lower bond budget (20%).
- **Mean-reverting/range regime:** Equal budgets across asset classes.
- **Crisis regime:** Higher bond/gold budget (50%), minimal equity (10%).

### HRP Implementation
1. Compute the correlation matrix from returns.
2. Apply hierarchical clustering (e.g., `scipy.cluster.hierarchy.linkage`).
3. Extract the dendrogram ordering.
4. Implement the recursive bisection allocation: at each split, allocate inversely proportional to cluster variance.
5. HRP naturally handles new assets and changing universes without full re-optimization.

## Example

**Setup:** Risk parity portfolio across 4 asset classes.

| Asset | Weight (60/40) | Risk Contribution (60/40) | Risk Parity Weight | Risk Contribution (RP) |
|-------|----------------|---------------------------|--------------------|-----------------------|
| US Equity (vol 16%) | 60% | 88% | 18% | 25% |
| US Bonds (vol 5%) | 40% | 12% | 55% | 25% |
| Commodities (vol 20%) | 0% | 0% | 14% | 25% |
| Gold (vol 15%) | 0% | 0% | 13% | 25% |

1. The 60/40 portfolio has 88% of its risk from equities. It is an equity portfolio with a small bond buffer.
2. Risk parity equalizes risk contributions at 25% each. Bonds dominate the weights (55%) because they are least volatile.
3. Unlevered risk parity vol: ~5%. To match the 60/40 portfolio's ~10% vol, apply 2x leverage.
4. **Levered risk parity return:** In a backtest from 2000-2025, the levered risk parity portfolio returned ~8% annualized with a max drawdown of 15%, vs the 60/40 portfolio's ~7% return and 35% max drawdown.
5. The improvement comes from diversification: balanced risk contributions mean no single asset class can dominate drawdowns.

## Advantages

- **True diversification:** Allocating risk equally means no single asset class dominates portfolio volatility, reducing drawdowns
- More principled than capital-weight allocation: 60/40 is an equity-risk portfolio masquerading as balanced
- HRP variant avoids covariance matrix inversion, making it robust to estimation error and suitable for large universes
- Combines naturally with [[garch-volatility]] for forward-looking risk estimates and [[regime-detection]] for dynamic budgets
- Strong backtest performance: risk parity has outperformed 60/40 on a risk-adjusted basis over most long-term periods
- **Modular:** Risk budgets can be customized to any investor's views and constraints without abandoning the framework
- Academically supported and institutionally adopted (Bridgewater, AQR, Invesco, PanAgora)

## Disadvantages

- **Requires leverage** to achieve competitive absolute returns -- levered bond positions can produce unexpected losses in rising rate environments (2022)
- Assumes **correlation stability:** if correlations spike in a crisis (stocks and bonds fall together), the "diversification" evaporates
- HRP is relatively new (2016) with limited live performance track records vs traditional methods
- The covariance matrix (even with shrinkage) is still an estimate -- garbage in, garbage out remains a risk
- Risk parity **does not incorporate expected returns** -- it may over-allocate to low-return assets simply because they are low-volatility
- Leverage introduces **financing costs** and margin requirements that erode returns in high-rate environments
- Rebalancing costs are higher than buy-and-hold because risk contributions constantly drift as volatilities and correlations change

## See Also

- [[black-litterman]] -- complementary framework that incorporates return views into portfolio construction
- [[garch-volatility]] -- volatility forecasting that enhances risk budget estimation
- [[portable-alpha]] -- uses risk budgeting to manage the combined leverage of alpha and beta
- [[cppi]] -- alternative dynamic allocation approach focused on floor protection
- [[regime-detection]] -- enables regime-conditional risk budgets for adaptive allocation
