---
title: Multi-Strategy Portfolio Construction
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, meta-strategy, portfolio-construction, diversification, sharpe-ratio, hedge-fund, alpha]
strategy_type: hybrid
markets: [futures, crypto, bonds]
complexity: advanced
backtest_status: untested
related: [volatility-targeting, risk-on-risk-off-framework, crypto-yield-stack]
---

# Multi-Strategy Portfolio Construction

## Overview

A multi-strategy portfolio allocates capital across multiple **uncorrelated** strategies to produce a portfolio with a higher [[sharpe-ratio]] than any individual strategy. The core insight: strategies that are individually mediocre (Sharpe 0.5-1.0) combine into a portfolio with Sharpe 1.5-2.0+ if they are genuinely uncorrelated. This is not diversification across assets -- it is **diversification across alpha sources**. Each strategy exploits a different market inefficiency, ensuring that when one strategy draws down, others are flat or profitable.

## The Synergy

The math is elegant. If you have N uncorrelated strategies each with Sharpe ratio S, the portfolio Sharpe is approximately:

```
Portfolio_Sharpe = S * sqrt(N)
```

Five uncorrelated strategies each with Sharpe 0.7 produce a portfolio Sharpe of 0.7 * sqrt(5) = 1.57. This is the fundamental reason multi-strategy hedge funds dominate institutional allocations -- they manufacture consistency from individually inconsistent components.

The synergy goes deeper than diversification. Strategies that are anti-correlated (one profits when another loses) create **natural hedges** that reduce drawdowns without explicit hedging costs. [[trend-following]] and [[mean-reversion]] are classic examples: trend following profits in sustained moves while mean reversion profits in reversals. Together, they cover both regimes.

## Component Strategies

A robust multi-strategy portfolio includes 4-6 strategies spanning different asset classes, timeframes, and edge types:

| Strategy | Edge Type | Typical Sharpe | Correlation to Equities |
|----------|----------|---------------|------------------------|
| [[trend-following]] (managed futures) | Momentum across markets | 0.5-0.8 | -0.1 to 0.1 |
| equity-long-short | Stock selection alpha | 0.6-1.0 | 0.3-0.5 |
| [[options-income]] (selling premium) | Volatility risk premium | 0.7-1.2 | -0.2 to 0.3 |
| [[mean-reversion]] / [[stat-arb]] | Short-term price inefficiency | 0.8-1.5 | 0.0-0.2 |
| [[crypto-funding-rate-arbitrage]] | Basis/funding rate capture | 0.5-1.0 | 0.1-0.3 |
| [[macro-relative-value]] | Cross-asset mispricing | 0.4-0.8 | -0.1 to 0.2 |

## Implementation

**Step 1: Strategy Selection and Qualification**

Each strategy must meet minimum criteria before inclusion:
- Minimum 2 years of live or paper-traded track record
- Sharpe ratio above 0.4 (standalone)
- Maximum drawdown below 25%
- Clear, articulable edge that is not capacity-constrained at your capital level
- Rolling 60-day [[correlation]] to other portfolio strategies below 0.3

**Step 2: Risk Budget Allocation**

Allocate risk budgets (not capital) based on conviction, capacity, and diversification value:

| Strategy | Risk Budget | Rationale |
|----------|------------|-----------|
| Trend following (futures) | 25% | Low correlation, crisis alpha |
| Equity long-short | 25% | Highest capacity, moderate Sharpe |
| Options income | 20% | Steady returns, short vol tail risk |
| Mean reversion / stat arb | 15% | High Sharpe but limited capacity |
| Crypto funding rate arb | 15% | Unique return source, crypto exposure |

**Step 3: Apply [[volatility-targeting]]**

Convert risk budgets into capital allocations using the vol-targeting framework. Each strategy's allocation = Risk_Budget * Portfolio_Target_Vol / Strategy_Current_Vol. This ensures no single strategy dominates risk, even if its volatility spikes.

**Step 4: Correlation Monitoring**

Track the rolling 60-day correlation matrix between all strategies. If any pair exceeds 0.5 correlation for 3 consecutive months, investigate. Possible responses:
- Reduce allocation to the higher-vol strategy in the correlated pair
- Add a negatively correlated strategy to offset
- Drop one strategy if the correlation is structural (same underlying edge)

**Step 5: Quarterly Rebalance and Review**

Every quarter: recalculate vol targets, review strategy performance attribution, and assess whether each strategy is still generating alpha. Kill strategies that have drawn down more than 2x their historical max drawdown or whose edge has demonstrably decayed.

## Example Setup

A $1,000,000 portfolio targeting 10% annual volatility:

| Strategy | Risk Budget | Current Vol | Capital Allocated |
|----------|------------|-------------|------------------|
| CTA trend following | 25% | 16% | $156,250 |
| US equity L/S (quant) | 25% | 12% | $208,333 |
| SPX options premium | 20% | 9% | $222,222 |
| Equity pairs/stat arb | 15% | 7% | $214,286 |
| Crypto perp funding arb | 15% | 22% | $68,182 |
| **Cash/collateral** | -- | -- | $130,727 |

The cash buffer provides collateral for futures/options margin and acts as a reserve for [[rebalancing]] and drawdown management.

## When It Excels / When It Fails

**Excels when:**
- Strategies maintain low cross-correlation over time
- Individual strategy drawdowns are offset by gains elsewhere
- Volatility regimes shift -- some strategies gain while others retreat
- Applied with sufficient capital to run each strategy at meaningful scale ($500K+ total)

**Fails when:**
- Correlation spikes during crises (2008, March 2020) -- "all correlations go to 1"
- Too many strategies share the same underlying factor exposure (disguised concentration)
- Operational complexity leads to execution errors across multiple systems
- Strategy decay is not identified quickly, and dead strategies drag the portfolio

## Real-World Usage

The multi-strategy model is the dominant institutional hedge fund structure. [[citadel]], [[millennium-management]], [[balyasny]], and [[point72]] operate as "pod shops" -- each portfolio manager runs an independent strategy, and the platform aggregates across 50-200+ pods. The platform captures the sqrt(N) diversification benefit at massive scale.

For individual traders, a simplified version with 3-5 strategies is achievable. The critical requirement is genuine strategy independence -- not just different tickers, but different **edge types** exploiting different **market inefficiencies**. Running three momentum strategies in different asset classes is less diversifying than running one momentum + one mean reversion + one volatility premium strategy. Focus on **edge diversification**, not asset diversification.
