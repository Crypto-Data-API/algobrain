---
title: "Darvas Box Method"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [darvas-box, breakout, momentum, nicolas-darvas, box-theory, trend-following, technical-analysis]
aliases: ["Darvas Box", "Darvas Box Theory", "Nicolas Darvas Method", "Box Breakout"]
strategy_type: technical
timeframe: swing
markets: [stocks]
complexity: beginner
backtest_status: untested
related: ["[[support-resistance-breakout]]", "[[channel-breakout]]", "[[donchian-channel-breakout]]", "[[turtle-trading]]", "[[volume]]"]
---

# Darvas Box Method

## Overview

The Darvas Box Method was developed by **Nicolas Darvas**, a professional dancer who turned $36,000 into over **$2 million** in the stock market between 1957 and 1959 while touring the world -- receiving only daily stock quotes via telegram. He documented his system in the 1960 bestseller *How I Made $2,000,000 in the Stock Market*. The method is remarkably simple: when a stock makes a **new 52-week high**, Darvas drew a "box" around the consolidation range -- the **top of the box** is the new high, and the **bottom** is the lowest price during that consolidation. A **buy signal** occurs when price breaks above the box top on strong [[volume]]. The **stop-loss** is placed just below the box bottom. If the stock continues higher, a new box is drawn, and the stop ratchets up to the bottom of the new box. The method is essentially a **momentum breakout system** with a built-in trailing stop mechanism. Despite being over 60 years old, the core principles -- buying strength, cutting losers, and letting winners run -- remain timeless and are embedded in many modern stocks trading strategies.

## How It Works

Darvas combined **technical box construction** with a fundamental filter: he only traded stocks in **growth industries** that were making new highs (he called them "techno-fundamentally" sound). The box system is the mechanical component:

1. **New high identification:** A stock makes a new high (ideally a 52-week or all-time high). This signals unusual strength and institutional interest.
2. **Box construction:** After the new high, the stock consolidates. The top of the box is the new high price. Over the following days, as the stock retraces, the lowest point of the pullback becomes the bottom of the box. The box is "set" once the stock stops making new lows (typically 3 consecutive days without a new low).
3. **Breakout entry:** When price closes above the box top, buy. Darvas required this to happen on **above-average volume** -- confirming institutional participation.
4. **Stop-loss at box bottom:** Place the stop immediately below the bottom of the box. If price breaks below the box bottom at any point, sell -- no exceptions.
5. **Stacking boxes:** If the stock continues higher and forms a new consolidation, draw a new box. The stop-loss moves up to the bottom of the new box. This creates a **ratcheting trailing stop** that locks in profits while letting the trend run.

## Rules and Signals

### Entry
1. Screen for stocks making **new 52-week highs** -- Darvas only traded the strongest names in the market.
2. Wait for the stock to consolidate after the new high. Identify the box: high = new high price, low = the pullback low.
3. **Buy when price breaks above the box top.** Confirm with above-average [[volume]] on the breakout day.
4. If the breakout fails and price falls back into the box, exit immediately.

### Stop-Loss
- Place the stop just below the **bottom of the current box** (e.g., $0.10 or 0.5% below the box low).
- This stop is non-negotiable. If triggered, sell and move on. Darvas was ruthless about cutting losses.

### Trailing Stop (Box Stacking)
- As the stock advances and forms new boxes at higher levels, move the stop up to the bottom of each new box. Never move the stop down -- only up. Risk 1-2% of account per trade.

## Example Trade

**Asset:** NVDA (NVIDIA), daily chart
1. NVDA makes a new 52-week high of $145 on strong earnings and AI demand. Volume is 3x the 50-day average.
2. NVDA consolidates between $145 (box top) and $132 (box bottom) over the next 8 trading days. The box is set.
3. On day 9, NVDA breaks above $145 on heavy [[volume]], closing at $148. Enter long at $148. Stop at $131 (below box bottom). Risk: $17/share.
4. NVDA rallies to $172 and consolidates. New box: top = $172, bottom = $160. Move stop up to $159.
5. NVDA breaks above $172 and rallies to $195. New box: top = $195, bottom = $183. Move stop to $182.
6. NVDA eventually falls back below $183, triggering the stop.
7. **Result:** Entry at $148, exit at $182. Profit: $34/share (+23%). Initial risk was $17/share. Risk-reward: 2:1, captured over a multi-week trend.

## Advantages
- Extremely simple to understand and execute -- no complex indicators, ratios, or calculations required
- Forces traders to buy strength and avoid "bargain hunting" in declining stocks
- The box-bottom stop provides a clear, objective exit level with no ambiguity
- The box-stacking trailing stop naturally lets winners run while locking in profits
- Aligns with the momentum factor that is well-documented in academic finance literature
- Works well for part-time traders -- Darvas himself traded using only daily closing prices received via telegram

## Disadvantages
- Performs poorly in choppy, range-bound markets where breakouts frequently fail and reverse (whipsaws)
- The method relies on stocks making new highs -- it misses bottoming patterns and reversal trades entirely
- In modern markets with algorithmic trading, breakouts above obvious consolidation ranges are frequently trapped by institutional stop hunts
- The original method was designed for stocks and does not directly translate to [[forex]] or other non-equity markets
- No guidance on how to size boxes in volatile versus calm environments

## See Also
- [[support-resistance-breakout]] -- the same core concept of buying breakouts above consolidation
- [[channel-breakout]] -- channel systems share the breakout-and-trail philosophy
- [[donchian-channel-breakout]] -- Donchian channels automate the "new high" identification that Darvas did manually
- [[turtle-trading]] -- the Turtle system is a formalized evolution of breakout-and-trail strategies like Darvas
- [[volume]] -- the critical confirmation tool for Darvas box breakouts
