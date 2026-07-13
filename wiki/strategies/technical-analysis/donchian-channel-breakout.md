---
title: "Donchian Channel Breakout"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [trend-following, breakout, channels, donchian, richard-donchian]
aliases: ["Donchian Breakout", "Channel Breakout", "Donchian Channel Strategy"]
strategy_type: technical
timeframe: swing|position
markets: [futures, commodities, stocks]
complexity: beginner
backtest_status: untested
related: ["[[turtle-trading]]", "[[bollinger-band-reversion]]", "[[atr]]", "[[keltner-channels]]", "[[book-technical-analysis-of-the-financial-markets]]", "[[book-market-wizards]]", "[[richard-donchian]]", "[[donchian-channels]]"]
---

# Donchian Channel Breakout

## Overview

The Donchian Channel was developed by Richard Donchian, widely regarded as the "father of trend following" (Source: [[book-technical-analysis-of-the-financial-markets]]). The channel plots the highest high and lowest low over a specified N-period lookback, creating a visual envelope around price. A breakout above the upper channel signals bullish momentum; a break below the lower channel signals bearish momentum. The midline (average of upper and lower) can serve as an exit or a trend filter.

This indicator is historically significant because it became the foundation for the [[turtle-trading]] system taught by Richard Dennis to his Turtle Traders in the 1980s (Source: [[book-market-wizards]]). Despite its simplicity, the Donchian Channel captures a core truth of markets: new highs tend to lead to higher highs, and new lows tend to lead to lower lows.

## Rules

### Entry
1. **Long Entry:** Price closes above the N-period highest high (upper Donchian band). The standard lookback is 20 periods (matching the Turtle System 1).
2. **Short Entry:** Price closes below the N-period lowest low (lower Donchian band).
3. **Confirmation Filter (optional):** Require the close to be above/below the band, not just an intraday wick. Alternatively, wait for a second close beyond the channel.

### Exit
1. **Channel Exit:** Exit longs when price touches the lower Donchian band of a shorter lookback (e.g., 10-period). Exit shorts when price touches the upper 10-period band.
2. **Midline Exit:** Exit when price crosses back through the Donchian midline (halfway between upper and lower channels).
3. **Stop-Loss:** Place a fixed stop at 1-2x [[atr]] below entry (longs) or above entry (shorts).

### Position Sizing
Risk 1-2% of equity per trade. The [[atr]] can be used to normalize position sizes across instruments, as the [[turtle-trading|Turtles]] did.

## Indicators Used
- **Donchian Channel** (upper = N-period highest high, lower = N-period lowest low, midline = average)
- [[atr]] for stop-loss and position sizing
- [[volume]] for breakout confirmation (higher volume on breakout is preferable)

## Common Configurations
| Setting | Lookback | Exit Lookback | Use Case |
|---------|----------|---------------|----------|
| Short-term | 20 periods | 10 periods | Swing trading (Turtle System 1) |
| Long-term | 55 periods | 20 periods | Position trading (Turtle System 2) |
| Scalping | 10 periods | 5 periods | Intraday on lower timeframes |

## Example Trade
**Asset:** Gold Futures (GC), daily chart
1. Gold has been consolidating between $1,920 and $1,980 for 25 days. The 20-day Donchian upper band sits at $1,980.
2. On day 26, gold closes at $1,988, above the upper Donchian band. Enter long at $1,988.
3. Set stop-loss 2x ATR below entry. ATR(14) = $18, so stop = $1,988 - $36 = $1,952.
4. Gold trends upward over 3 weeks, reaching $2,065. The Donchian upper band keeps rising, confirming the uptrend.
5. Gold pulls back. The 10-day lowest low is $2,040. When price hits $2,040, exit.
6. **Result:** Entry $1,988, exit $2,040 = +$52/oz, risking $36/oz. Reward-to-risk ratio: 1.44:1.

## Performance Characteristics
- **Win Rate:** 30-45%. Like most breakout systems, many signals fail, but winners can be significantly larger than losers.
- **Profit Factor:** 1.5-2.5 in trending markets. The asymmetric payoff profile is the edge.
- **Best Market Conditions:** Markets that transition from consolidation to strong directional trends. Commodities and forex pairs with macro-driven trends.
- **Worst Market Conditions:** Prolonged sideways, choppy markets where price repeatedly pokes above/below the channel only to reverse.

## Advantages
- Extremely simple to calculate and implement -- no complex math required
- Objectively defines breakout levels with zero ambiguity
- Automatically adapts to market volatility (wider channels in volatile markets, narrower in quiet ones)
- Historical foundation -- proven concept that spawned the [[turtle-trading]] system
- Works on any market and timeframe

## Disadvantages
- **False breakouts** are the primary enemy -- price often pierces the channel and immediately reverses
- **Lagging by design:** you only enter after the move has started, missing the initial leg
- Performs poorly in range-bound or mean-reverting markets
- The simplicity is also a limitation -- no momentum or volume filters built in
- Requires a diversified portfolio of instruments to smooth returns over time

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy covers Donchian Channels as a core channel breakout tool, including construction, lookback period selection, and integration with trend-following systems
- [[book-market-wizards]] -- Schwager's interviews with Richard Dennis and other trend followers document the real-world application of Donchian Channel breakouts in the Turtle Trading experiment
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — [[richard-donchian|Donchian]] as the "father of trend following," win-rate data (74.1%), Turtle system connection

## See Also
- [[turtle-trading]] -- the most famous system built on Donchian Channels
- [[bollinger-band-reversion]] -- another channel-based strategy, but mean-reverting rather than breakout
- [[keltner-channels]] -- ATR-based channels that serve a similar visual function
- [[breakout-trading]] -- the general concept of trading breakouts from defined levels
