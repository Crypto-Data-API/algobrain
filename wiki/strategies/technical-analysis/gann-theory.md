---
title: "Gann Theory"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [gann, gann-angles, square-of-nine, time-cycles, geometric-trading, natural-law, price-time, technical-analysis]
aliases: ["Gann Trading", "W.D. Gann Method", "Gann Angles", "Gann Square", "Square of Nine"]
strategy_type: technical
timeframe: swing
markets: [stocks, commodities]
complexity: advanced
backtest_status: untested
related: ["[[fibonacci-trading]]", "[[elliott-wave]]", "[[harmonic-patterns]]", "[[support-and-resistance]]", "[[point-and-figure]]"]
---

# Gann Theory

## Overview

Gann Theory encompasses the trading methods of **William Delbert Gann** (1878-1955), one of the most legendary and controversial figures in market history. Gann claimed to have discovered **natural laws governing market behavior** based on the geometric relationship between **price and time**. His methods include **Gann angles** (lines drawn at specific degrees representing the rate of price change over time), the **Square of Nine** (a spiral numerical calculator used to forecast support, resistance, and turning points), and **time cycles** (the idea that markets repeat at predictable intervals based on astronomical and mathematical cycles). Gann reportedly turned $130 into $12,000 in 30 days in a verified 1909 demonstration and claimed a 92% win rate in his trading. His techniques are **esoteric and difficult to master** -- blending mathematics, geometry, astrology, and Biblical numerology -- but they have a devoted following, particularly among [[commodities]] and [[stocks]] traders who believe markets follow geometric and cyclical laws.

## How It Works

### Gann Angles
Gann angles are trendlines drawn from significant highs or lows at specific angles. The most important is the **1x1 angle (45 degrees)** -- one unit of price per one unit of time -- Gann's equilibrium line. Above the 1x1, the market is bullish; below it, bearish. Other key angles: **2x1 (63.75 degrees)** for steep uptrends, **1x2 (26.25 degrees)** for shallow uptrends, and **4x1, 8x1, 1x4, 1x8** for extreme moves.

A fan of Gann angles drawn from a major low creates dynamic [[support-and-resistance]] lines. Price tends to move from one angle to the next.

### Square of Nine
The Square of Nine is a spiral arrangement of numbers starting from 1 at the center and spiraling outward. Numbers on the same **cardinal cross** (0, 90, 180, 270 degrees) and **ordinal cross** (45, 135, 225, 315 degrees) share geometric relationships. To find support/resistance: locate a significant price on the Square, and the numbers at 90, 180, and 360-degree rotations are predicted turning points.

### Time Cycles
Gann believed markets repeat at regular intervals: 30, 60, 90, 120, 144, 180, 270, and 360 calendar days from a significant high or low. The **90-day and 180-day cycles** are the most watched.

## Rules and Signals

### Entry
1. **Gann angle support/resistance:** Enter long when price bounces off a rising Gann angle (especially the 1x1 or 2x1). Enter short when price rejects a declining angle.
2. **Square of Nine levels:** Calculate the next 90-degree and 180-degree rotations from the current price. Enter when price tests these levels with reversal signals.
3. **Time cycle confluence:** When a time cycle date coincides with a Gann angle or Square of Nine level, reversal probability increases significantly.
4. **Price-time squaring:** When price in points equals time elapsed in bars/days from a turning point, a trend change is imminent (e.g., $90 rally over 90 days).

### Stop-Loss and Targets
- Stop below the Gann angle that triggered the entry. If price breaks through a 1x1 angle, the next support is the 1x2 angle.
- Targets are the next Gann angle above (for longs) or the Square of Nine level at the next 180 or 360-degree rotation.
- Time-based exits: if the trade has not reached the target by the next significant time cycle date, reassess.

## Example Trade

**Asset:** Corn futures (monthly chart)
1. Corn makes a major low of $3.20/bushel. Draw a Gann fan: the 1x1 angle rises at 45 degrees from this low.
2. Over the next 6 months, corn rallies to $4.50, running above the 2x1 angle (steep bullish trend).
3. Corn breaks below the 2x1 angle and pulls back to the 1x1 angle at $3.85. The pullback occurs exactly **90 calendar days** from the major low -- a time cycle confluence.
4. A bullish reversal candle forms at the 1x1 angle. Enter long at $3.88. Stop at $3.60 (below the 1x1 angle). Risk: $0.28/bushel.
5. Square of Nine calculation: 360-degree rotation from $3.20 = $4.68 (approximate). Set this as the target.
6. Corn bounces off the 1x1 angle and rallies to $4.72 over the next 3 months.
7. **Result:** Profit of $0.84/bushel from a $3.88 entry. Risk-reward: 3:1. The 1x1 angle held as support, and the Square of Nine target was reached within a time cycle window.

## Advantages
- Integrates both price and time into a unified framework -- most strategies focus only on price levels
- Gann angles provide dynamic support/resistance that moves with time, adapting as the chart evolves
- The Square of Nine offers specific, calculated price targets rather than subjective levels
- Time cycle analysis can pinpoint when a move might occur, not just where -- a powerful edge when it works
- Works well in [[commodities]] markets that exhibit strong cyclical and seasonal tendencies
- A century of devoted practitioners have refined and documented the techniques extensively

## Disadvantages
- **Extremely difficult to learn and apply correctly.** Gann himself never published his complete methods, leading to conflicting interpretations
- The esoteric elements (astrology, Biblical numerology, "natural law") alienate most modern quantitative traders and lack empirical validation
- Gann angle calculations require proper **scaling** of the price-time axis -- different chart scaling produces different angles, introducing subjectivity
- The Square of Nine produces so many potential levels that some will always be "close" to price, creating the illusion of accuracy through hindsight fitting
- Very few successful modern traders publicly credit Gann methods as their primary approach

## See Also
- [[fibonacci-trading]] -- another ratio-based framework for identifying price levels, often used alongside Gann
- [[elliott-wave]] -- Gann and Elliott were contemporaries; their methods complement each other for long-term forecasting
- [[harmonic-patterns]] -- geometric price patterns with precise mathematical ratios, sharing Gann's spirit
- [[point-and-figure]] -- another classical charting method from Gann's era that ignores time
- [[support-and-resistance]] -- Gann angles and Square of Nine levels are specialized forms of support and resistance
