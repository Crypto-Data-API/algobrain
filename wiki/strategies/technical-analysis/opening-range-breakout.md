---
title: Opening Range Breakout Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - breakout
  - opening-range
  - intraday
  - toby-crabel
  - orb
strategy_type: breakout
timeframe: intraday
markets:
  - stocks
  - futures
complexity: intermediate
backtest_status: untested
related:
  - "[[volatility-breakout]]"
  - "[[support-resistance-breakout]]"
  - "[[vwap-trading]]"
  - "[[scalping]]"
---

# Opening Range Breakout Strategy

## Overview

The Opening Range Breakout (ORB) strategy marks the **high and low of the first 15-30 minutes** of the trading session, then trades the breakout of that range. Popularized by **Toby Crabel** in his 1990 book *Day Trading with Short-Term Price Patterns and Opening Range Breakout*, this method capitalizes on the fact that the opening range often sets the tone for the entire session. The first 15-30 minutes concentrate institutional order flow, earnings reactions, and overnight gap resolution. A decisive break of this range with [[volume]] typically leads to a sustained intraday move. The strategy uses [[atr]] for profit targets and works best on high-volume days with clear directional bias.

## Rules

### Entry Rules
1. **Define the Opening Range:** Mark the high and low of the first 15 minutes (aggressive) or 30 minutes (conservative) after the market open.
2. **Long Entry:** Buy when price breaks **above** the opening range high by a small buffer (e.g., 1-2 ticks). Confirm with above-average [[volume]] on the breakout candle.
3. **Short Entry:** Sell when price breaks **below** the opening range low by 1-2 ticks with volume confirmation.
4. **Gap Filter:** On large gap-up days (>1% above prior close), favor long-side ORB trades. On large gap-down days, favor short-side. Avoid trading ORB into the gap (fading gaps requires a different approach).
5. **One Trade Per Day:** After the first breakout triggers, do not re-enter if stopped out. The cleanest ORB signals happen once.

### Exit Rules
1. **ATR Target:** Set the profit target at 1.5-2x the opening range width, or use 1x [[atr]](14) of the daily chart.
2. **Time Stop:** Close all positions by 15:30 (30 minutes before market close) regardless of profit/loss. The ORB is a morning momentum play.
3. **Stop Loss:** Place the stop at the **opposite side of the opening range**. If long above the high, stop is at the opening range low (and vice versa).
4. **Trailing Stop:** Once price moves 1x the opening range width in your favor, trail the stop to breakeven, then to 50% of open profit.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| Opening Range (High/Low) | First 15 or 30 min | Define breakout levels |
| [[volume]] | Intraday bars | Confirm breakout conviction |
| [[atr]] | 14-period (daily) | Target calculation and position sizing |
| [[vwap]] | Session | Directional bias confirmation |
| [[moving-average]] (9 EMA) | 5-min chart | Intraday trend direction |

## Example Trade

**Setup:** SPY opens at $520.50 after a strong overnight futures session. The first 15 minutes print a high of $521.30 and a low of $520.10. Opening range width = $1.20. Volume in the first 15 minutes is 30% above the 20-day average.

**Entry:** At 9:50 AM, SPY breaks above $521.30 on heavy volume. Enter long at $521.35. The [[vwap]] is at $520.80, confirming bullish bias (price above VWAP).

**Management:** Stop loss at $520.10 (opening range low). Risk = $1.25. Target = $521.35 + (1.5 x $1.20) = $523.15. R/R = 1.44:1.

**Exit:** SPY rallies to $523.15 by 11:30 AM. Target hit, close position. Alternatively, trail stop to breakeven at $521.35 once price passes $522.55 (1x range width).

## Performance Characteristics

- **Win Rate:** 50-60% on high-volume days; drops to 35-45% on low-volume/choppy days
- **Best Conditions:** High-volume days, earnings catalysts, gap days, trending market environments
- **Worst Conditions:** Low-volume holiday sessions, FOMC announcement days (pre-announcement chop), narrow opening ranges
- **Average Holding Period:** 30 minutes to 4 hours
- **Key Filter:** Opening range width matters -- very narrow ranges (<0.3x daily ATR) produce more false breakouts

## Advantages

- Clear, objective rules with defined entry, stop, and target levels
- Captures the most liquid and volatile part of the trading day
- Works well on stocks and [[futures]] with regular session opens
- Can be combined with [[vwap-trading]] for additional confluence
- Simple enough for intermediate traders; no complex indicators required

## Disadvantages

- Limited to markets with a defined opening session (not ideal for 24/7 [[crypto]] markets)
- False breakouts (fakeouts) are common, especially on low-volume days
- Requires real-time monitoring and fast execution during the morning session
- Stop loss can be wide if the opening range is large, requiring smaller position sizes
- Only provides 1 trade per day -- not suitable for traders seeking high frequency
- Does not work well during major [[economic-events]] where the market chops before a scheduled release
