---
title: Volatility Targeting Across Multiple Strategies
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, meta-strategy, volatility, risk-management, position-sizing, portfolio-construction]
strategy_type: hybrid
markets: [stocks, futures, crypto]
complexity: advanced
backtest_status: untested
related: [risk-on-risk-off-framework, multi-strategy-portfolio, mean-reversion]
---

# Volatility Targeting

## Overview

Volatility targeting normalizes risk across multiple strategies by scaling positions to maintain a **constant portfolio volatility**. If your target is 10% annualized volatility, you increase position sizes when realized vol is low and decrease them when vol is high. Applied across a multi-strategy book -- [[trend-following]], [[mean-reversion]], [[options-income]] -- each strategy receives a risk budget dynamically scaled by its current volatility. The result is a smoother equity curve and more predictable risk exposure.

## The Synergy

Without vol targeting, the strategy generating the most volatility dominates your portfolio risk. A [[crypto-momentum]] strategy running at 60% annual vol will swamp a [[pairs-trading]] strategy at 12% vol, even if they have equal capital allocations. Vol targeting fixes this by ensuring each strategy contributes **equal risk** rather than equal capital.

The deeper synergy: vol targeting **naturally de-risks during crises**. When volatility spikes (as in March 2020 or Q4 2018), positions automatically shrink. When volatility compresses (as in 2017 or early 2020), positions expand. This creates an implicit [[risk-on-risk-off-framework]] without requiring any macro signal interpretation.

## Component Strategies

Vol targeting is a meta-layer applied on top of any combination of base strategies:

- **[[trend-following]]** on futures -- typically 15-25% vol; scale to your target
- **[[equity-long-short]]** -- typically 10-18% vol; often already near target
- **[[options-income]]** (selling premium) -- typically 8-15% vol but with fat tails
- **[[mean-reversion]] / [[statistical-arbitrage]]** -- typically 5-12% vol; scale up
- **[[crypto-funding-rate-arbitrage]]** -- typically 10-30% vol depending on positioning

Each sub-strategy gets a **risk budget** (percentage of total portfolio vol) rather than a fixed capital allocation.

## Implementation

**Step 1: Calculate Realized Volatility**

For each strategy, compute 20-day realized volatility of daily returns:

```
RealizedVol = StdDev(daily_returns, 20 days) * sqrt(252)
```

For [[crypto]] strategies, use `sqrt(365)` since markets trade every day.

**Step 2: Compute Target Weight**

```
Target_Weight = (Risk_Budget * Portfolio_Target_Vol) / Strategy_Realized_Vol
```

Example: Portfolio target = 10% vol. Trend following has a 30% risk budget and current realized vol of 20%.

```
Target_Weight = (0.30 * 0.10) / 0.20 = 0.15 (15% of capital)
```

If trend following vol drops to 10%: Target_Weight = 0.30, doubling the allocation.

**Step 3: Apply Position Limits**

Cap maximum leverage at 1.5x for any single strategy and 2.0x for the total portfolio. When vol is extremely low, uncapped scaling would create dangerous leverage. Set floor weights too -- never less than 5% in any active strategy to maintain meaningful exposure.

**Step 4: Rebalance Weekly**

Every Monday, recalculate realized vol for each strategy and adjust weights. Use a **blended vol estimate**: 70% realized vol + 30% implied vol (from [[vix]] or strategy-specific options) to be forward-looking.

**Step 5: Correlations Matter**

True portfolio vol depends on inter-strategy [[correlation]]. If two strategies are 0.8 correlated, their combined risk is much higher than independent. Use a rolling 60-day correlation matrix to adjust. The formula becomes:

```
Portfolio_Vol = sqrt(W' * Cov_Matrix * W)
```

where W is the weight vector and Cov_Matrix includes cross-strategy covariances.

## Example Setup

A $500,000 multi-strategy portfolio targeting 10% annual vol:

| Strategy | Risk Budget | Current Vol | Target Weight | Capital |
|----------|------------|-------------|---------------|---------|
| [[trend-following]] (futures) | 30% | 18% | 16.7% | $83,500 |
| [[equity-long-short]] | 25% | 14% | 17.9% | $89,500 |
| [[options-income]] | 20% | 10% | 20.0% | $100,000 |
| [[mean-reversion]] (stat arb) | 15% | 8% | 18.8% | $94,000 |
| [[crypto-funding-rate-arb]] | 10% | 25% | 4.0% | $20,000 |
| **Cash buffer** | -- | -- | 22.6% | $113,000 |

Notice the cash buffer -- when strategies run hot, capital naturally moves to cash. This is the built-in de-risking mechanism.

## When It Excels / When It Fails

**Excels when:**
- Volatility regimes persist (high vol stays high, low vol stays low)
- Applied across genuinely uncorrelated strategies
- Drawdowns are preceded by rising vol (which triggers position reduction)
- Used by funds managing institutional capital that demands consistent risk

**Fails when:**
- Vol regime shifts abruptly -- a gap crash from low vol catches you fully sized
- Strategies have fat-tailed distributions where realized vol understates true risk
- Transaction costs erode returns from frequent rebalancing (especially in [[crypto]])
- Extremely low vol environments tempt excessive leverage

## Real-World Usage

[[aqr-capital]], [[man-group]], and virtually all professional [[cta]] firms use volatility targeting as a core portfolio construction technique. The typical target ranges from 8-15% annual vol depending on the fund's mandate. [[risk-parity]] funds like Bridgewater's All Weather explicitly vol-target each asset class to equalize risk contribution.

Academic research (Moreira and Muir, 2017) demonstrated that simple vol-targeting applied to a single equity index improves Sharpe ratios by 20-40%. Applied across multiple uncorrelated strategies, the improvement compounds further. The key lesson: **managing volatility is as important as generating returns**.
