---
title: "London Breakout Strategy"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [london-breakout, session-trading, asian-range, gbp, forex-strategy, intraday, volatility-breakout, london-open, technical-analysis]
aliases: ["London Breakout", "London Open Strategy", "London Session Breakout", "Asian Range Breakout"]
strategy_type: technical
timeframe: intraday
markets: [forex]
complexity: beginner
backtest_status: untested
related: ["[[opening-range-breakout]]", "[[volatility-breakout]]", "[[support-resistance-breakout]]", "[[channel-breakout]]", "[[supply-demand-zones]]"]
---

# London Breakout Strategy

## Overview

The London Breakout Strategy exploits the **volatility surge** that occurs when the London [[forex]] session opens at **8:00 AM GMT (3:00 AM EST)**. London is the world's largest forex trading center, handling approximately 38% of global daily volume. When London opens, the flood of institutional order flow from European banks, hedge funds, and corporations creates a decisive directional move that often sets the tone for the rest of the day. The strategy is simple: identify the **Asian session range** (the high and low established during the quieter Tokyo session from midnight to 8 AM GMT), then trade the breakout in whichever direction London pushes price. Buy stops are placed above the Asian high and sell stops below the Asian low. The trade targets a **1:2 or 1:3 risk-reward ratio** and is typically closed before the New York session overlap or end of the London session. The strategy works best on **GBP pairs** (GBP/USD, GBP/JPY, EUR/GBP) because the British pound is most active during London hours, but it also applies to EUR/USD, EUR/JPY, and other major pairs.

## How It Works

The strategy leverages a fundamental structural feature of the 24-hour forex market: **session transitions create volatility.** The Asian session (Tokyo) tends to be the quietest period for European and GBP-denominated pairs, establishing a narrow consolidation range. When London opens, the massive influx of new participants breaks this range, and price often trends strongly in one direction for the first 2-4 hours of the London session.

### Session Times (GMT)
- **Asian session (range formation):** 00:00 - 08:00 GMT. Mark the highest high and lowest low during this window.
- **London open (breakout trigger):** 08:00 GMT. Orders are triggered.
- **Trade window:** 08:00 - 12:00 GMT (first 4 hours of London). Most of the directional move occurs here.
- **Close deadline:** Before 17:00 GMT (London close) at the latest. Many traders close by 12:00-14:00 GMT.

## Rules and Signals

### Entry
1. At 08:00 GMT, mark the **Asian session high and low** on the 15-minute or 1-hour chart. Add a **buffer of 10 pips** above/below to prevent false breakouts from spread widening.
2. **Place buy stop** at Asian high + 10 pips. **Place sell stop** at Asian low - 10 pips. When one triggers, cancel the other (OCO).
3. **Filter: Asian range size.** Ideal range is **30-60 pips** for GBP pairs. Skip if the range exceeds 80 pips (diminished breakout potential) or is under 20 pips (false break prone).
4. **Avoid high-impact news days:** If Bank of England, ECB, or NFP announcements are scheduled during London hours, skip the trade.

### Stop-Loss
- Place the stop on the **opposite side of the Asian range**. If the buy stop triggers, the stop goes at the Asian low - 10 pips (or the midpoint of the range for a tighter stop).
- Alternatively, use a **fixed stop of 30-40 pips** for GBP pairs, adjusting based on recent average daily range.

### Profit Targets
- **Target 1:2 risk-reward** as the standard approach. If your stop is 40 pips, target 80 pips.
- **Partial profit strategy:** Take 50% at 1:1 R:R, move stop to breakeven, and let the remainder run to 1:2 or 1:3.
- **Time-based exit:** If the trade has not hit the target by 12:00-14:00 GMT, close the position regardless of profit or loss. The London session's directional momentum fades in the afternoon.

## Example Trade

**Asset:** GBP/USD, 15-minute chart
1. Asian session (00:00-08:00 GMT): GBP/USD ranges between 1.2720 (high) and 1.2680 (low). Asian range = 40 pips. Within the ideal 30-60 pip window.
2. At 08:00 GMT, place buy stop at 1.2730 (high + 10 pips) and sell stop at 1.2670 (low - 10 pips).
3. At 08:15 GMT, London opens with strong bullish order flow. GBP/USD breaks above the Asian high, triggering the buy stop at 1.2730. Cancel the sell stop.
4. Stop-loss at 1.2670 (Asian low - 10 pips). Risk: 60 pips.
5. Target at 1:2 R:R = 1.2730 + 120 pips = 1.2850.
6. Take 50% profit at 1.2790 (1:1 R:R, +60 pips). Move stop to breakeven (1.2730).
7. GBP/USD continues to rally during the London morning, reaching 1.2840 by 11:30 GMT. Close the remaining 50% at 1.2840.
8. **Result:** First half: +60 pips. Second half: +110 pips. Average: +85 pips on 60 pips of risk. Effective R:R: 1.4:1 on the blended position.

## Advantages
- Extremely simple system with clear, mechanical rules -- no subjective interpretation required
- Exploits a well-documented structural feature of the forex market (London session volatility surge)
- Fixed daily routine: mark the range, place orders, manage the trade, done by midday -- ideal for part-time traders
- Works consistently on GBP pairs (GBP/USD, GBP/JPY) and EUR pairs (EUR/USD, EUR/GBP) because London session dynamics are structurally persistent
- No indicators required -- pure price action and session structure

## Disadvantages
- **Only works in [[forex]]** -- entirely dependent on forex session timing with no application to [[stocks]] or [[crypto]]
- **False breakouts are common:** Price may spike above the Asian range, trigger the buy stop, then reverse and stop out
- The strategy has become widely known, and some institutional algorithms may exploit the predictable placement of retail stop orders
- Performance varies significantly by pair and by market regime -- backtesting across different periods shows inconsistent results
- Spread widening at the London open can trigger false entries if the buffer is too small

## See Also
- [[opening-range-breakout]] -- the same session-based breakout concept applied to the first 15-30 minutes of market opens
- [[volatility-breakout]] -- London Breakout is a specific application of the general volatility breakout framework
- [[support-resistance-breakout]] -- the Asian range high and low function as intraday support and resistance levels
- [[channel-breakout]] -- channel systems share the breakout-and-trend philosophy on longer timeframes
- [[supply-demand-zones]] -- institutional zones formed during the Asian session may reinforce or invalidate the London breakout direction
