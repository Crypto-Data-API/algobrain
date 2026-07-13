---
title: Scalping Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - scalping
  - day-trading
  - high-frequency
  - tick-charts
  - level-2
  - tape-reading
strategy_type: scalping
timeframe: scalp
markets:
  - forex
  - futures
  - crypto
complexity: advanced
backtest_status: untested
related:
  - "[[order-flow-scalping]]"
  - "[[vwap-trading]]"
  - "[[market-making-strategy]]"
  - "[[opening-range-breakout]]"
---

# Scalping Strategy

## Overview

Scalping is a [[day-trading]] approach that extracts many **small profits (1-10 pips or ticks)** from brief price movements, holding positions for seconds to minutes. Scalpers exploit micro-level supply and demand imbalances, market microstructure inefficiencies, and short-term momentum bursts. The strategy demands **fast execution**, **tight spreads**, **high-volume markets**, and the ability to read **Level 2 order books** and tick charts. Scalping produces a high volume of trades (50-200+ per day), relying on a slight edge per trade compounded across many repetitions. It is one of the most demanding strategies in trading, requiring intense focus, discipline, and low-latency infrastructure.

## Rules

### Entry Rules
1. **Market Selection:** Trade only the most liquid instruments with the tightest bid-ask spreads. Ideal: EUR/USD ([[forex]]), ES/NQ ([[futures]]), BTC/USDT perps ([[crypto]]).
2. **Tick Chart Entries:** Use 100-tick, 200-tick, or 500-tick charts instead of time-based charts. Enter when a cluster of aggressive buying (upticks) or selling (downticks) creates a micro-momentum burst.
3. **Level 2 / DOM Entry:** Watch the [[order-book]] (Depth of Market). Enter when large resting orders are absorbed and price pushes through that level, indicating genuine demand overcoming supply.
4. **Spread Scalp:** In highly liquid markets, place limit orders at the bid and ask to capture the spread (similar to [[market-making-strategy]] but manual).
5. **Momentum Scalp:** Enter in the direction of a sudden volume surge on tick charts. Use a 9 EMA on the tick chart for micro-trend direction.

### Exit Rules
1. **Fixed Target:** Set a target of 2-5 ticks (futures) or 3-8 pips (forex). Do not hold for larger moves -- take the quick profit.
2. **Time Exit:** If the trade does not move in your favor within 30-60 seconds, exit at scratch (breakeven) or accept a tiny loss.
3. **Stop Loss:** Maximum stop of 3-5 ticks. The edge comes from high win rate and tiny losses, not large risk/reward ratios.
4. **Adverse Flow Exit:** If the order book suddenly loads up against your position (large orders appearing on the opposite side), exit immediately without waiting for the stop.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| Tick Charts | 100-500 tick | Price action at micro level |
| Level 2 / DOM | Real-time | Order flow and liquidity reading |
| [[vwap]] | Session | Intraday fair value reference |
| 9 EMA | On tick chart | Micro-trend direction |
| Cumulative Delta | Real-time | Net buying vs. selling pressure |
| Time & Sales (Tape) | Real-time | Identify large aggressive orders |

## Example Trade

**Setup:** ES (E-mini S&P 500) futures on a 200-tick chart. Price is above [[vwap]] (bullish bias). The DOM shows a large resting sell order at 5,285.00 (2,000 contracts). Time & Sales shows aggressive buying absorbing this order -- 1,800 contracts traded at 5,285.00 in 10 seconds without price dropping.

**Entry:** The 2,000-lot sell wall is absorbed. Enter long at 5,285.25 as price begins to move through the level. The 9 EMA on the tick chart is sloping up.

**Management:** Stop at 5,284.00 (5 ticks). Target at 5,286.50 (5 ticks). Risk/reward = 1:1, but the edge is in the win rate (~60-70% on high-quality setups).

**Exit:** Price reaches 5,286.50 in 45 seconds. Close for a 5-tick profit ($62.50 per contract). Move on to the next setup.

## Performance Characteristics

- **Win Rate:** 55-70% required to be profitable after commissions
- **Trades Per Day:** 50-200+ depending on market conditions and style
- **Average Holding Time:** 15 seconds to 5 minutes
- **Best Conditions:** High-volume, trending sessions with sustained directional flow
- **Worst Conditions:** Low-volume midday chop (11:30 AM - 1:30 PM ET), pre-holiday sessions, wide-spread environments
- **Critical Factor:** Net profitability after commissions and fees. A scalper grossing $500/day but paying $400 in commissions nets only $100.

## Advantages

- Many opportunities per day; does not require waiting for setups
- Very short exposure time reduces overnight and tail risk
- Small per-trade risk means individual losses are tiny
- Income is relatively consistent when the edge is maintained
- Develops elite tape reading and market microstructure skills
- No overnight position risk or gap risk

## Disadvantages

- **Commissions and fees** can consume a large percentage of gross profits; requires very low fee structures
- Extremely mentally demanding; requires sustained focus for hours
- Latency matters -- retail traders are at a disadvantage to colocated participants
- Slippage during volatile moments can turn winning trades into losers
- Not scalable: large position sizes move the market against you in liquid instruments
- Burnout rate is very high; most scalpers cannot sustain peak performance long-term
- Requires specialized tools: direct market access (DMA), fast data feeds, tick-chart capable platforms

## See Also

- [[scalping-vs-position-trading]] -- comparison of the fastest and slowest active trading styles
