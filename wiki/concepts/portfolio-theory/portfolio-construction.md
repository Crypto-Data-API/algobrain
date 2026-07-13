---
title: "Portfolio Construction"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, risk-management, quantitative]
aliases: ["Portfolio Construction"]
related: ["[[modern-portfolio-theory]]", "[[diversification]]", "[[risk-management]]", "[[sharpe-ratio]]", "[[correlation]]", "[[position-sizing]]", "[[risk-budgeting]]", "[[factor-investing]]", "[[rebalancing]]"]
domain: [portfolio-theory]
difficulty: intermediate
---

Portfolio construction is the process of selecting assets and determining their weights to build a portfolio that balances expected return against risk. It is the bridge between investment ideas (what to buy) and [[risk-management]] (how much to own). The field spans from simple heuristics like equal weighting to sophisticated quantitative methods like mean-variance optimization and hierarchical risk parity.

## Overview

At its core, portfolio construction answers two questions: which assets belong in the portfolio, and how much capital to allocate to each. The answers depend on the investor's objectives, constraints, risk tolerance, and beliefs about expected returns and [[correlation]] structure.

[[harry-markowitz]] formalized the problem in 1952 with [[modern-portfolio-theory]], showing that portfolios should be evaluated on risk-adjusted return, not individual asset returns. The key insight is that combining assets with low [[correlation]] produces a portfolio with less risk than any individual holding — the [[diversification]] free lunch.

However, theory and practice diverge significantly. Mean-variance optimization is notoriously sensitive to input estimates — small errors in expected returns produce wildly different optimal portfolios. This has led to a variety of practical alternatives that sacrifice theoretical elegance for robustness.

## How It Works

**Major approaches to portfolio construction**:

- **Equal weight**: Allocate the same dollar amount to each position. Simple, transparent, and surprisingly hard to beat. Implicitly assumes no forecasting ability and maximum [[diversification]].
- **Mean-variance optimization (MVO)**: Markowitz's original framework. Inputs: expected returns, volatilities, and correlations. Outputs: the efficient frontier of portfolios offering maximum return for each level of risk. In practice, often produces extreme concentrated positions and is highly sensitive to estimation error.
- **Risk parity**: Allocate so that each asset contributes equally to total portfolio risk. Does not require return forecasts — only risk estimates. Popularized by [[ray-dalio]]'s [[all-weather-portfolio]]. Tends to overweight bonds and underweight equities relative to traditional allocations.
- **Hierarchical Risk Parity (HRP)**: Developed by Marcos Lopez de Prado. Uses machine learning clustering to build a hierarchy of assets based on correlation structure, then allocates along the hierarchy. More stable than MVO because it does not require inverting the covariance matrix. Described in [[book-machine-learning-for-asset-managers|Machine Learning for Asset Managers]].
- **Factor-based**: Allocate across risk factors (value, momentum, quality, low-volatility) rather than individual securities. Targets diversified exposure to compensated risk premia.
- **Discretionary/conviction-weighted**: Size positions based on analyst conviction. Higher conviction = larger position. Used by most fundamental portfolio managers. The ITPM methodology falls here, emphasizing concentrated positions in high-conviction ideas with strict [[risk-management]] overlays.

**Constraints commonly applied**: maximum position size (e.g., 5% per stock), sector limits, liquidity requirements, turnover budgets, and tracking error limits relative to a benchmark.

**Choosing a method — a comparison:**

| Method | Inputs needed | Strength | Weakness |
|--------|---------------|----------|----------|
| Equal weight | None (just the universe) | Robust, transparent, hard to beat | Ignores risk and return differences |
| Mean-variance (MVO) | Expected returns, vols, correlations | Theoretically optimal Sharpe | Extremely sensitive to return estimates; concentrated, unstable |
| Risk parity | Risk estimates only | No return forecast; balanced risk | Overweights low-vol assets (bonds); needs leverage; vulnerable to a bond/equity crash |
| Hierarchical Risk Parity | Correlation matrix | Stable; no matrix inversion | Newer, less battle-tested; still estimate-dependent |
| [[factor-investing\|Factor-based]] | Factor exposures, premia | Diversified compensated risk | Factors can crowd and underperform for years |
| Conviction-weighted | Analyst views + risk overlay | Captures discretionary edge | Behavioural bias; concentration risk |

A practical compromise many allocators use is the **Black-Litterman** model, which starts from market-cap (equilibrium) weights and tilts them only where the investor has explicit views — taming MVO's instability by anchoring to the market unless you have a strong reason to deviate.

> **Worked example — risk contribution vs dollar weight.** A simple two-asset book holds 60% equities (16% volatility) and 40% bonds (5% volatility), with low correlation. Even though bonds are 40% of the *dollars*, they contribute far less of the *risk*: equities' larger weight and triple the volatility mean stocks drive roughly 90%+ of total portfolio variance. A 60/40 portfolio is, in risk terms, almost an all-equity portfolio. [[risk-budgeting|Risk budgeting]] / risk parity reweights — often by adding leverage to the bonds — so each sleeve contributes equal risk, which is why true risk-parity funds hold far more than 40% in bonds. This gap between dollar weight and risk weight is the single most important idea in modern portfolio construction.

## Trading Applications

- **Rebalancing**: Portfolios drift from target weights as prices move. Periodic rebalancing (monthly, quarterly) or threshold-based rebalancing (when a position drifts more than 5% from target) maintains the intended risk profile. Rebalancing inherently sells winners and buys losers — a contrarian tendency that works in range-bound markets but can hurt in strong trends.
- **Risk budgeting**: Allocate a total risk budget (e.g., 15% annual volatility) across positions. This ensures the portfolio's risk is intentional and controlled, rather than an accidental byproduct of position sizing.
- **Correlation monitoring**: Portfolio construction is only as good as the correlation estimates feeding it. In crisis periods, correlations spike toward 1.0 — the diversification benefit disappears precisely when it is most needed. Stress-testing portfolios under high-correlation scenarios is essential.
- **Transaction cost awareness**: Frequent rebalancing incurs [[transaction-costs]] and tax events. Practical portfolio construction balances theoretical optimality against implementation costs.
- **Factor exposure control**: Beyond picking names, a constructor manages aggregate exposure to [[factor-investing|factors]] (value, momentum, quality, size, low-vol) and to sectors and macro variables (rates, the dollar), so the portfolio's bets are the *intended* ones rather than accidental tilts that show up only in a drawdown.

## How Practitioners Use It

- **Top-down vs bottom-up.** Top-down construction sets asset-class and factor budgets first, then fills them; bottom-up sizes each idea on conviction and then checks the aggregate risk. Most real books blend the two.
- **The conviction-to-weight map.** Discretionary managers (including the ITPM style) translate research conviction into [[position-sizing|position sizes]] but cap any single name and apply stop/risk overlays so that one bad call cannot sink the book.
- **Sleeves and overlays.** Large allocators split capital into sleeves (core beta, satellite alpha, hedges) and use derivative overlays (futures, options) to adjust net exposure cheaply without trading the underlying holdings.
- **Tax and cost overlay.** In taxable accounts, harvesting losses and avoiding short-term gains is itself a construction decision; turnover budgets and threshold rebalancing keep implementation drag low.

## Common Pitfalls

- **Estimation error masquerading as optimisation.** MVO will happily allocate 80% to whichever asset has the highest (noisy) expected-return estimate. Tiny input errors produce wildly different "optimal" weights — the classic "error-maximisation" critique.
- **Correlation regime shift.** Construction assumes a [[correlation]] structure that breaks exactly when it matters: in crises correlations converge toward 1.0 and [[diversification]] evaporates. Stress-test under high-correlation scenarios.
- **Hidden leverage and concentration.** Risk parity and carry strategies use leverage to lift low-vol assets; the leverage is invisible in dollar weights but lethal when both legs fall together (as in 2022).
- **Over-rebalancing.** Rebalancing too often bleeds returns to [[transaction-costs]] and taxes and fights strong trends; too rarely lets risk drift. The right cadence depends on cost and volatility.
- **Ignoring liquidity.** A book that is "optimal" on paper can be impossible to exit at scale; capacity and liquidity constraints must be built in, not bolted on.
- **Backtest overfitting.** Weights tuned to past data ([[overfitting]]) rarely survive out of sample; prefer robust, low-parameter schemes.

## Related

- [[modern-portfolio-theory]] — Theoretical foundation for portfolio construction
- [[diversification]] — Risk reduction through asset combination
- [[risk-management]] — Broader framework for managing portfolio risk
- [[sharpe-ratio]] — Key metric for evaluating portfolio risk-adjusted return
- [[correlation]] — Statistical relationship driving diversification benefits
- [[position-sizing]] — Determining individual position weights
- [[risk-budgeting]] — Allocating a total risk budget across positions
- [[factor-investing]] — Building exposure across compensated risk factors
- [[rebalancing]] — Restoring target weights as prices drift

## Sources

- (Source: [[book-inside-the-black-box]]) — Narang's description of systematic portfolio construction in quantitative trading
- (Source: [[book-machine-learning-for-asset-managers]]) — Lopez de Prado's HRP and modern portfolio construction techniques
