---
title: Order Flow Scalping Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - scalping
  - order-flow
  - footprint-charts
  - delta
  - cvd
  - tape-reading
  - institutional
strategy_type: scalping
timeframe: scalp
markets:
  - futures
  - crypto
complexity: advanced
backtest_status: untested
related:
  - "[[scalping]]"
  - "[[vwap-trading]]"
  - "[[market-making-strategy]]"
  - "[[support-resistance-breakout]]"
---

# Order Flow Scalping Strategy

## Overview

Order flow scalping reads **live market order data** to identify institutional buying and selling activity in real time, entering trades aligned with the dominant aggressive flow. Unlike traditional [[technical-analysis]] that relies on historical price patterns, order flow analysis examines **what is happening right now** in the order book: who is buying, who is selling, and at what size. The strategy uses **footprint charts** (volume at each price level split by buy/sell aggressor), **delta** (net aggressive buying minus selling), and **Cumulative Volume Delta (CVD)** to spot imbalances. This is the modern evolution of tape reading -- what floor traders did by watching the ticker tape, now done digitally with tools like **Bookmap**, **Sierra Chart**, **Jigsaw**, and **Exocharts**. It is among the most skill-intensive approaches in [[day-trading]].

## Rules

### Entry Rules
1. **Imbalance Detection:** On footprint charts, look for **diagonal imbalances** where the bid volume at one price level is 3x+ greater than the ask volume at the adjacent level (or vice versa). Stacked imbalances across 3+ price levels signal strong institutional participation.
2. **Delta Divergence:** When price makes a new low but delta is rising (more aggressive buyers than sellers despite price dropping), it signals absorption -- institutions are buying the dip. Enter long. The reverse applies for shorts.
3. **CVD Confirmation:** Cumulative Volume Delta trending in the direction of the intended trade confirms that net aggressive flow supports the setup. Divergence between CVD and price is a powerful reversal signal.
4. **Absorption Entry:** Watch for large resting limit orders (visible on the DOM or heatmap tools like bookmap) absorbing aggressive market orders without price moving. When the aggressive flow exhausts and the resting orders hold, enter in the direction of the resting order side.
5. **Breakout Flow:** When price approaches a key level and footprint shows a surge of aggressive buyers (market buy orders) stacking up, enter with the flow expecting a breakout of that level.

### Exit Rules
1. **Flow Reversal:** Exit immediately when the order flow shifts against your position -- delta turns negative (for longs) or aggressive selling appears on the footprint.
2. **Fixed Target:** Take profit at 4-10 ticks on [[futures]] or equivalent on [[crypto]] perpetuals. Scalping targets are small by design.
3. **Stop Loss:** Maximum stop of 4-8 ticks. Place stops behind the absorption zone or the imbalance cluster that triggered the entry.
4. **Time Exit:** If the expected move does not materialize within 1-3 minutes, exit at scratch. Order flow setups resolve quickly.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| Footprint Charts | Bid x Ask volume per price | Identify imbalances and absorption |
| Delta (per bar) | Real-time | Net aggressive buy vs. sell |
| CVD (Cumulative Volume Delta) | Session or rolling | Trend of net aggressive flow |
| DOM / Order Book | Real-time depth | Spot resting orders and absorption |
| Heatmap (Bookmap) | Real-time | Visualize limit order placement and pulls |
| [[vwap]] | Session | Fair value reference for directional bias |

## Example Trade

**Setup:** NQ (Nasdaq 100 futures) on a footprint chart, 1-minute bars. Price pulls back to the session [[vwap]] at 18,450. The footprint shows aggressive selling (red delta) driving price down, but resting buy orders at 18,445-18,450 are absorbing every sell wave without price breaking lower. CVD is flat despite the price decline -- sellers are not winning.

**Entry:** A stacked diagonal imbalance appears: buy imbalance of 4:1 at 18,448, 18,449, and 18,450. Delta flips positive on the current bar. Enter long at 18,451 as price lifts off the absorption zone.

**Management:** Stop loss at 18,443 (below the absorption zone, 8 ticks). Target at 18,461 (10 ticks). R/R = 1.25:1 with expected win rate of 60-65%.

**Exit:** Aggressive buying accelerates. Footprint shows stacked buy imbalances at every price as shorts cover. Price reaches 18,461 in 90 seconds. Close for a 10-tick profit ($40 per contract).

## Performance Characteristics

- **Win Rate:** 55-65% for experienced practitioners; below 50% during learning phase
- **Trades Per Day:** 10-40 high-conviction setups on active instruments
- **Average Holding Time:** 30 seconds to 5 minutes
- **Best Conditions:** High-volume sessions with institutional participation (market open, London/NY overlap, FOMC days)
- **Worst Conditions:** Low-volume overnight sessions, holidays, pre-announcement lulls where flow is thin and unreliable
- **Learning Curve:** 6-18 months of screen time to develop proficiency reading live order flow

## Advantages

- Provides the **most real-time edge** available to discretionary traders -- sees what is happening now, not what happened historically
- Identifies institutional activity that is invisible on standard candlestick charts
- Absorption and imbalance signals often precede price movement by seconds, offering early entries
- Works exceptionally well at key [[support-resistance]] levels where large participants defend or attack
- Combines powerfully with [[vwap-trading]] and [[scalping]] techniques
- Applicable to [[futures]] and [[crypto]] perpetuals where order flow data is transparent

## Disadvantages

- **Extremely steep learning curve** -- most traders need 6+ months of dedicated screen time before profitability
- Requires specialized (and often expensive) software: Bookmap, Sierra Chart, Jigsaw, Exocharts
- Data feeds with sufficient granularity (tick-level, market-by-order) can be costly
- Not applicable to [[forex]] spot (decentralized, no centralized order book) or most stocks (dark pools obscure true flow)
- Spoofing and layering by algorithms create false signals -- large displayed orders may be pulled before execution
- Mentally exhausting; requires intense concentration for extended periods
- Difficult to backtest systematically; order flow is inherently real-time and contextual
