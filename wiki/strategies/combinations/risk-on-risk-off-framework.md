---
title: Risk-On / Risk-Off Framework
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [combinations, meta-strategy, macro, regime-switching, risk-management, asset-allocation]
strategy_type: hybrid
markets: [crypto, bonds, commodities]
complexity: intermediate
backtest_status: untested
related: [volatility-targeting, multi-strategy-portfolio, sector-momentum-screen]
---

# Risk-On / Risk-Off Framework

## Overview

Instead of running one strategy through all market conditions, the Risk-On/Risk-Off (RORO) framework **shifts your entire portfolio posture** based on macro and market signals. When conditions favor growth, you lean into [[momentum-trading]], [[leverage]], and high-beta assets. When conditions deteriorate, you rotate into [[bonds]], [[gold]], cash, and defensive-sectors. The framework turns regime identification into a systematic allocation decision.

## The Synergy

Most strategies perform well in one regime and poorly in another. [[trend-following]] thrives in trending risk-on markets but whipsaws during transitions. [[mean-reversion]] works in range-bound risk-off environments but gets crushed in momentum rallies. RORO solves this by **matching strategy to regime** rather than forcing one approach through all conditions.

During risk-on periods (2020-2021), you ride momentum in equities and crypto. During risk-off (2022), you are already in cash, bonds, and hedges before the damage hits. The framework does not predict the future -- it reads the present environment and positions accordingly.

## Component Strategies

**Risk-ON allocation:**
- Overweight equities, especially growth-stocks and small-cap-momentum
- [[crypto-exposure]] at full position size
- High-beta sectors: technology, consumer discretionary, financials
- Use [[leverage]] (1.2-1.5x) on conviction positions
- [[trend-following]] signals fully enabled

**Risk-OFF allocation:**
- Overweight [[treasury-bonds]] (long duration), [[gold]], and [[cash-equivalents]]
- Defensive sectors: utilities, healthcare, consumer staples
- Reduce or eliminate [[leverage]]
- Enable [[hedging-strategies]] -- put spreads, VIX calls
- [[mean-reversion]] and [[income-strategies]] preferred

## Implementation

**Step 1: Build a Composite Risk Indicator**

Combine four signals into a single score (0-100):

| Signal | Risk-ON Condition | Weight |
|--------|------------------|--------|
| [[vix]] level | Below 20 | 25% |
| [[yield-curve]] slope (10Y-2Y) | Positive and steepening | 25% |
| [[credit-spreads]] (HY-IG) | Narrowing or below 400bps | 25% |
| S&P 500 vs [[200-day-moving-average]] | Price above 200-day MA | 25% |

**Step 2: Define Regimes**

- Score 70-100: **Full Risk-ON** -- deploy aggressive allocation
- Score 40-69: **Neutral** -- balanced allocation, moderate sizing
- Score 0-39: **Full Risk-OFF** -- defensive allocation, hedges active

**Step 3: Rebalance Weekly**

Every Friday, recalculate the composite score. Shift allocation gradually -- move 25% of the delta per week to avoid whipsawing. If the score drops from 80 to 30, do not flip instantly. Transition over 2-3 weeks.

**Step 4: Overlay with [[momentum-breadth]]**

Add a confirmation layer: percentage of S&P 500 stocks above their 50-day MA. If breadth is above 60%, that confirms risk-on. Below 30% confirms risk-off. Breadth divergences (index rising but breadth falling) are early warning signals.

## Example Setup

A $100,000 portfolio with composite score at 75 (Risk-ON):

| Asset | Allocation | Vehicle |
|-------|-----------|---------|
| US equities (growth tilt) | 45% | QQQ, individual momentum-stocks |
| International equities | 15% | EFA, emerging markets |
| Crypto (BTC/ETH) | 15% | Direct or ETF |
| Commodities (energy, metals) | 10% | GSG, individual futures |
| Bonds (short duration) | 10% | SHY |
| Cash | 5% | Money market |

When the score drops to 25 (Risk-OFF), shift to:
- US equities (defensive) 20%, bonds (long duration TLT) 35%, gold (GLD) 20%, cash 25%.

## When It Excels / When It Fails

**Excels when:**
- Clear macro regime shifts occur (2020 recovery, 2022 tightening)
- Volatility clusters -- crisis periods sustain for weeks/months
- Multiple signals align (VIX spikes + yield curve inverts + credit widens)

**Fails when:**
- Regimes shift rapidly back and forth (whipsaw in 2023)
- Flash crashes that reverse within days -- too slow to capture
- Signals conflict (low VIX but inverted yield curve, as in late 2019)
- The framework lags at turning points by 1-3 weeks

## Real-World Usage

Macro hedge funds like [[bridgewater-associates]] run sophisticated versions of RORO with dozens of regime indicators. Family offices commonly use simplified versions for strategic allocation. [[ray-dalio]]'s "All Weather" portfolio is a static version; RORO is the dynamic version. Many [[risk-parity]] funds implement RORO implicitly through their [[volatility-targeting]] overlays.

The key insight: **you do not need to predict regimes, only recognize them promptly**. Being 2 weeks late to risk-off still saves you from 80% of a drawdown. Being 2 weeks late to risk-on still captures 80% of a rally. Timeliness matters less than accuracy of regime identification.
