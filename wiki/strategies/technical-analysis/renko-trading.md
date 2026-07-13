---
title: "Renko Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [renko, renko-charts, brick-charts, trend-following, noise-filter, atr-renko, time-independent, technical-analysis]
aliases: ["Renko Charts", "Renko Brick Trading", "Renko Strategy"]
strategy_type: technical
timeframe: swing
markets: [stocks, crypto, forex]
complexity: beginner
backtest_status: untested
related: ["[[point-and-figure]]", "[[heikin-ashi]]", "[[supertrend]]", "[[moving-average-crossover]]", "[[parabolic-sar]]"]
---

# Renko Trading

## Overview

Renko charts originated in Japan (the name comes from "renga," meaning "brick") and construct price charts using **fixed-size bricks** that only plot when price moves a specified amount. Unlike traditional candlestick or bar charts that create a new candle every time period, Renko charts create a **new brick only when price moves the set brick size** in one direction. If the brick size is $5, a new green (bullish) brick appears only when price rises $5 from the prior brick's close, and a new red (bearish) brick appears only when price falls $5. **Time is completely ignored** -- a single brick might represent 5 minutes or 5 days of price action, depending on volatility. This construction eliminates minor fluctuations, whipsaws, and noise, producing extremely clean trend visualization. A **brick color change** (green to red or red to green) is the simplest trading signal: a trend reversal. Renko charts combine well with [[moving-average-crossover]] overlays and the [[supertrend]] indicator for confirmation. The method is popular across [[stocks]], [[crypto]], and [[forex]] for traders who want clean, simple trend identification without complex indicator stacks.

## How It Works

### Chart Construction
1. **Choose a brick size:** This is the most important decision. Common approaches:
   - **Fixed brick size:** A static value (e.g., $5 for stocks, 10 pips for [[forex]], $500 for BTC).
   - **ATR-based brick size:** Use the **Average True Range** over 14 periods to dynamically set the brick size. This adapts to current volatility -- wider bricks in volatile markets, tighter bricks in calm markets.
2. **Plotting rules:** Starting from a closing price, if price rises by one brick size, plot a green brick. If price continues rising by another brick size, plot another green brick above it. Bricks are only added when the full brick size is achieved. If price reverses by **two brick sizes** (the standard Renko reversal requirement), plot a red brick in the opposite direction.
3. **No wicks, no gaps:** Renko bricks are uniform blocks with no shadows or wicks. Each brick is the same height and connects directly to the adjacent brick. This produces the characteristic staircase appearance.

### Signal Generation
- **Trend identification:** A series of same-colored bricks indicates a trend. Five consecutive green bricks = strong uptrend. Five consecutive red bricks = strong downtrend.
- **Trend reversal signal:** A **brick color change** is the primary signal. When a red brick appears after a series of green bricks, the uptrend may be ending. When a green brick appears after red bricks, a new uptrend may be starting.
- **Support and resistance:** Horizontal levels where brick color changes cluster indicate strong [[support-and-resistance]] zones.

## Rules and Signals

### Entry
1. **Brick color change entry:** Go long when the first green brick appears after a series of red bricks. Go short when the first red brick appears after green bricks.
2. **Two-brick confirmation:** For more conservative entries, wait for **two consecutive bricks** in the new color before entering. This reduces false signals but delays the entry.
3. **Moving average filter:** Overlay a 10-period [[moving-average-crossover]] on the Renko chart. Only take long entries when bricks are above the MA; only short entries when below.
4. **[[supertrend]] confirmation:** Apply the [[supertrend]] indicator to the Renko chart. Enter only when the brick color change aligns with a Supertrend flip.

### Stop-Loss
- Place the stop at the **opposite end of the reversal brick** -- for a long entry, the stop is one brick below the green reversal brick. This equals exactly two brick sizes of risk.
- Alternatively, trail the stop by placing it one brick below the most recent green brick as the trend advances.

## Example Trade

**Asset:** ETH/USD, ATR-based Renko (14-period ATR = $80, so brick size = $80)
1. ETH has been declining: 7 consecutive red bricks from $3,200 to $2,640.
2. Price reverses by 2 bricks ($160) and a green brick forms at $2,800. First color change signal.
3. A second green brick forms at $2,880, confirming the trend change. The 10-period moving average on the Renko chart is at $2,850 -- price is now above it.
4. Enter long at $2,880. Stop at $2,720 (one brick below the reversal brick). Risk: $160/ETH.
5. ETH trends upward, printing green bricks: $2,960, $3,040, $3,120, $3,200, $3,280, $3,360.
6. Trail the stop one brick below the most recent green brick. Current stop: $3,280.
7. A red brick prints at $3,280, closing the position at $3,280.
8. **Result:** Entry $2,880, exit $3,280. Profit: $400/ETH (+13.9%). Risk was $160. Risk-reward: 2.5:1.

## Advantages
- Eliminates time-based noise, making trends exceptionally easy to identify visually
- Extremely simple signal generation -- brick color change is unambiguous and requires no interpretation
- Built-in whipsaw reduction: the two-brick-size reversal requirement filters out minor counter-trend moves
- ATR-based brick sizing automatically adapts to changing market volatility
- Works across all markets ([[stocks]], [[crypto]], [[forex]]) and can be combined with standard indicators
- Ideal for beginners -- no need to interpret candlestick patterns, divergences, or complex indicator readings

## Disadvantages
- **Lagging by design:** The two-brick reversal requirement means you always enter after the initial reversal has already occurred, sacrificing some profit
- Brick size selection dramatically impacts performance -- too small creates noise, too large misses trades
- Renko charts are not suitable for strategies that depend on precise timing, [[volume]] analysis, or candlestick patterns
- In choppy, range-bound markets, repeated brick color changes generate frequent false signals and whipsaws
- The smooth, clean appearance can create a false sense of certainty about trend direction

## See Also
- [[point-and-figure]] -- another time-independent charting method; P&F uses X's and O's instead of bricks
- [[heikin-ashi]] -- smoothed candlesticks that share Renko's goal of cleaner trend visualization but retain the time axis
- [[supertrend]] -- pairs well with Renko charts as a trend-confirmation overlay
- [[moving-average-crossover]] -- simple moving averages on Renko charts add an effective trend filter
- [[parabolic-sar]] -- another trailing-stop indicator that complements Renko trend signals
