---
title: "Portfolio Theory Overview"
type: overview
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [portfolio-theory]
aliases: ["Portfolio Theory Overview"]
related: ["[[portfolio-theory]]", "[[diversification]]", "[[correlation]]", "[[sharpe-ratio]]", "[[rebalancing]]", "[[capital-asset-pricing-model]]"]
---

# Portfolio Theory

Modern portfolio theory, asset allocation, diversification, and portfolio construction.

Portfolio theory provides the mathematical framework for combining assets to maximize returns for a given level of risk. The key insight -- first formalized by Harry Markowitz in 1952 -- is that [[diversification]] across imperfectly [[correlation|correlated]] assets can reduce portfolio [[volatility]] without sacrificing expected return. This is sometimes called "the only free lunch in finance."

These concepts underpin everything from simple 60/40 stock-bond [[asset-allocation|allocations]] to sophisticated multi-strategy hedge fund portfolios. Understanding how [[interest-rates]] affect asset prices and cross-asset correlations is essential for any portfolio-level decision.

> This is the section overview for `wiki/concepts/portfolio-theory/`. For the formal Markowitz mean-variance framework, see the [[portfolio-theory|Modern Portfolio Theory]] concept page.

## The Core Idea in One Equation

For a two-asset portfolio with weights `w₁, w₂`, the expected return is just the weighted average:

```
E[Rp] = w₁·E[R₁] + w₂·E[R₂]
```

But the risk is *not* a weighted average -- it depends on the [[correlation]] `ρ` between the assets:

```
σp² = w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·ρ·σ₁·σ₂
```

The cross-term `2·w₁·w₂·ρ·σ₁·σ₂` is the engine of diversification. When `ρ < 1`, combined portfolio volatility is *less* than the weighted average of the individual volatilities. The lower (or more negative) the correlation, the bigger the risk reduction -- which is why mixing imperfectly correlated assets, not just owning many of them, is what matters.

## Building Blocks of the Discipline

| Concept | What it answers | Page |
|---------|-----------------|------|
| Diversification | Why combine assets at all? | [[diversification]] |
| Correlation | How much do assets move together? | [[correlation]] |
| Efficient frontier | What is the best risk/return trade-off? | [[efficient-frontier]] |
| Asset allocation | How much in each asset class? | [[asset-allocation]] |
| Rebalancing | How to hold the target over time? | [[rebalancing]] |
| Sharpe ratio | Is the return worth the risk? | [[sharpe-ratio]] |
| CAPM | What return should an asset earn? | [[capital-asset-pricing-model]] |
| Risk parity | Allocate by risk, not capital? | [[risk-parity]] |

## How It Fits Together

1. Start from individual asset **expected returns** and **volatilities** ([[volatility]]).
2. Layer in **[[correlation|correlations]]** to compute portfolio risk.
3. Solve for the set of optimal mixes -- the **[[efficient-frontier]]**.
4. Pick a point on the frontier matching your risk tolerance; this *is* your **[[asset-allocation]]**.
5. **[[capital-asset-pricing-model|CAPM]]** then prices the risk you cannot diversify away (systematic / market risk, measured by [[beta]]).
6. Maintain the chosen mix with disciplined **[[rebalancing]]**, judging results by **[[sharpe-ratio|risk-adjusted return]]**.

## Limitations and Criticisms

Portfolio theory is a model, and like all models it simplifies. Practitioners should know where it breaks:

- **Correlations are unstable.** They tend to rise toward 1 in crises (see [[correlation]]), exactly when diversification is most needed -- the failure mode that hit 60/40 portfolios in 2022.
- **Returns are not normally distributed.** Real markets have fat tails and crashes that variance/volatility understates (see [[volatility]], [[risk-management]]).
- **Inputs are noisy.** Mean-variance optimisation is extremely sensitive to estimated returns; small input errors produce wildly different "optimal" weights ("error maximisation").
- **Single-period, frictionless.** The classic framework ignores taxes, transaction costs, and the multi-period nature of real investing.

These caveats motivated later refinements: [[capital-asset-pricing-model|CAPM]], factor models, [[risk-parity]], and the [[all-weather-portfolio]] approach.

## Start Here

- [[portfolio-theory|Modern Portfolio Theory]] -- the Markowitz mean-variance framework and the efficient frontier
- [[diversification]] -- Why holding multiple uncorrelated assets reduces risk
- [[correlation]] -- Measuring how assets move together (and when correlations break down)
- [[asset-allocation]] -- Dividing capital across asset classes (the dominant return driver)
- [[efficient-frontier]] -- The set of portfolios with the best risk/return trade-off
- [[sharpe-ratio]] -- Risk-adjusted return, the objective most portfolios optimize
- [[rebalancing]] -- Realigning weights back to target allocation
- [[risk-management]] -- Controlling downside, the practical complement to MPT
- [[interest-rates]] -- The macro variable that reprices every asset class

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/concepts/portfolio-theory"
WHERE type != "index"
SORT updated DESC
```

## Key Topics to Cover

- Modern Portfolio Theory (MPT)
- Efficient frontier
- Capital Asset Pricing Model (CAPM)
- Asset allocation strategies
- Rebalancing
- Sharpe ratio and risk-adjusted returns
