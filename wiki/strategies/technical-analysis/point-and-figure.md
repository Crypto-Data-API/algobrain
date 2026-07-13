---
title: "Point and Figure Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [point-and-figure, pnf, x-columns, o-columns, box-reversal, triple-top, vertical-count, noise-free, technical-analysis]
aliases: ["Point and Figure", "point-and-figure", "P&F Charting", "P&F Trading", "PnF"]
strategy_type: technical
timeframe: swing
markets: [stocks, commodities]
complexity: intermediate
backtest_status: untested
related: ["[[renko-trading]]", "[[support-and-resistance]]", "[[darvas-box]]", "[[gann-theory]]", "[[donchian-channel-breakout]]"]
---

# Point and Figure Trading

## Overview

Point and Figure (P&F) charting is one of the oldest methods in [[technical-analysis]], dating back to the late 1800s and predating standard bar and candlestick charts. Unlike time-based charts, P&F charts **ignore time entirely** and focus exclusively on **price movement**. Rising prices are recorded as columns of **X's**, and falling prices as columns of **O's**. A new X is added when price rises by a set amount (the **box size**), and a new column of O's begins only when price reverses by a specified multiple of the box size (typically **3 boxes** -- the "3-box reversal" method). This construction filters out minor fluctuations and noise, producing a clean visual representation of supply and demand. P&F charts generate clear, objective signals: **Double Top Breakout** (price exceeds the prior column of X's), **Triple Top Breakout** (price exceeds two prior X column highs), and their bearish equivalents. The **Vertical Count** and **Horizontal Count** methods provide specific price targets. P&F remains a favorite among classical technicians who want trend identification without the distraction of time-axis noise.

## How It Works

### Chart Construction
1. **Choose a box size:** Each box represents a fixed price increment (e.g., $2 for a $100 stock). The box size determines sensitivity.
2. **Choose the reversal amount:** The standard is **3-box reversal** -- price must move 3 boxes in the opposite direction to start a new column.
3. **Plot X's and O's:** If price rises by one box, add an X. Continue adding X's as price rises. When price drops by 3 boxes, move to the next column and plot O's downward. Continue until price reverses again by 3 boxes.

### Key Patterns
- **Double Top Breakout (bullish):** A column of X's rises above the top of the previous X column. Basic buy signal.
- **Double Bottom Breakdown (bearish):** A column of O's drops below the bottom of the previous O column. Basic sell signal.
- **Triple Top/Bottom:** Price exceeds two prior X column highs (buy) or breaks two prior O column lows (sell). Stronger signals because resistance/support was tested twice.
- **Bullish/Bearish Catapult:** A double top breakout that pulls back, forms a higher low, then breaks out again. Very strong continuation signal.

### Price Targets
- **Vertical Count:** X's in breakout column x box size x reversal amount + column low = upside target.
- **Horizontal Count:** Columns in congestion zone x box size x reversal amount + breakout level = target. This measures the "cause" and projects the "effect" -- similar to the [[wyckoff-method]] principle.

## Rules and Signals

### Entry
1. **Buy on a Double or Triple Top Breakout:** Current X column exceeds the highest X of prior X column(s).
2. **Sell on a Double or Triple Bottom Breakdown:** Current O column drops below the lowest O of prior O column(s).
3. **Trend filter:** Draw 45-degree Bullish Support Lines from significant lows and Bearish Resistance Lines from significant highs. Only take buy signals above the bullish support line.
4. **Stop-loss** at the 3-box reversal point from your entry. Risk 1-2% of account per trade.

## Example Trade

**Asset:** AAPL, $2 box size, 3-box reversal
1. AAPL forms three X columns with highs at $182, $182, and $182 -- a triple top resistance level.
2. A new X column rises to $184, breaking above the triple top at $182. **Triple Top Breakout** buy signal triggered.
3. Enter long at $184. The 3-box reversal stop is $178 (3 x $2 = $6 below the highest X). Risk: $6/share.
4. Vertical Count target: The breakout column has 8 X's. Target = low of column ($170) + (8 x $2 x 3) = $170 + $48 = $218.
5. AAPL trends higher, forming successive columns of X's and O's with rising highs and rising lows. The P&F chart shows a clean uptrend.
6. AAPL reaches $216 and triggers a Double Bottom Breakdown signal. Exit long at $210.
7. **Result:** Entry $184, exit $210. Profit: $26/share (+14.1%). Risk was $6/share. Risk-reward: 4.3:1.

## Advantages
- Eliminates time-based noise -- only significant price movements are plotted, producing cleaner signals than candlestick or bar charts
- Objective, rule-based signals: breakouts and breakdowns are unambiguous (price either exceeds the prior column's extreme or it does not)
- Built-in price targets via the Vertical and Horizontal Count methods
- The 3-box reversal naturally filters out minor whipsaws that plague time-based breakout strategies
- Trendlines on P&F charts are precisely defined (45-degree angles) with no subjectivity about where to draw them
- Excellent for identifying long-term [[support-and-resistance]] levels and major trend changes

## Disadvantages
- Ignoring time means you miss timing context -- a breakout that took 6 months to develop looks identical to one that took 6 days
- Box size selection significantly impacts signals -- too large filters out valid trades, too small creates noise
- P&F charts are not natively supported by all charting platforms, and constructing them manually is tedious
- Unfamiliar to most modern traders, making it difficult to discuss setups with a community or find educational resources
- Does not incorporate [[volume]], which is a significant limitation compared to methods like the [[wyckoff-method]]

## See Also
- [[renko-trading]] -- another time-independent charting method that uses fixed-size bricks instead of X's and O's
- [[support-and-resistance]] -- P&F charts excel at identifying horizontal support and resistance levels
- [[darvas-box]] -- another box-based breakout approach from the same classical era
- [[gann-theory]] -- Gann and P&F practitioners were contemporaries in the early 1900s charting community
- [[donchian-channel-breakout]] -- Donchian channels automate breakout detection similar to P&F double top signals
