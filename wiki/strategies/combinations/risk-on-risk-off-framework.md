---
title: Risk-On / Risk-Off Framework
type: reference
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [combinations, meta-strategy, macro, regime-switching, risk-management, portfolio-construction]
strategy_type: hybrid
markets: [crypto, bonds, commodities]
complexity: intermediate
backtest_status: untested
related: [volatility-targeting, multi-strategy-portfolio, sector-momentum-screen]
gates:
  - id: vix_below_20
    role: filter
    rule: "Composite leg 1 (25%): VIX below 20 scores risk-on"
    runnable: false
    note: "No VIX is served. /volatility/implied has crypto DVOL, but the page does not offer it as a stand-in. Needs a CBOE VIX feed."
  - id: yield_curve_steepening
    role: filter
    rule: "Composite leg 2 (25%): 10Y-2Y Treasury slope positive and steepening scores risk-on"
    runnable: false
    note: "/sentiment/macro serves a single Treasury yield (treasury_yield), not the 10Y and 2Y points a slope needs. Needs FRED (DGS10, DGS2) or similar."
  - id: credit_spreads_narrow
    role: filter
    rule: "Composite leg 3 (25%): HY-IG credit spread narrowing or below 400 bps scores risk-on"
    runnable: false
    note: "No credit-spread series is served. Needs ICE BofA OAS indices via FRED or a bond-data vendor."
  - id: spx_above_200dma
    role: filter
    rule: "Composite leg 4 (25%): S&P 500 above its 200-day moving average scores risk-on"
    runnable: false
    note: "No equity index prices are served. A crypto analogue (BTC above its 200-day MA, /indicators/technical) exists but the page does not offer it."
  - id: composite_regime
    role: filter
    rule: "Composite 0-100 from the four equal-weighted legs: 70-100 full risk-on, 40-69 neutral, 0-39 full risk-off"
    runnable: false
    input: derived
    inputs: [vix_below_20, yield_curve_steepening, credit_spreads_narrow, spx_above_200dma]
    note: "Every leg is TradFi data we do not serve."
  - id: breadth_confirmation
    role: filter
    rule: "Confirm with breadth: more than 60% of S&P 500 stocks above their 50-day MA confirms risk-on, below 30% confirms risk-off"
    runnable: false
    note: "No equity breadth is served. /market-health/altcoin-breadth?ma_period=50 is the crypto analogue, which the page does not name."
  - id: regime_allocation
    role: sizing
    rule: "Risk-on: growth equities, crypto at full size (15% BTC/ETH in the example), leverage 1.2-1.5x on conviction; risk-off: long Treasuries, gold, cash, defensive sectors, hedges on"
    runnable: false
    input: derived
    inputs: [composite_regime]
    note: "Only as runnable as composite_regime."
  - id: gradual_rebalance
    role: sizing
    rule: "Recompute every Friday and move 25% of the allocation gap per week, so a full flip takes 2-3 weeks"
    runnable: true
    input: position
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
