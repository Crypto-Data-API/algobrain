---
title: MACD Crossover Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - momentum
  - macd
  - trend-following
  - crossover
  - gerald-appel
strategy_type: momentum
timeframe: swing
markets:
  - stocks
  - crypto
  - forex
complexity: beginner
backtest_status: untested
related:
  - "[[rsi-divergence]]"
  - "[[rate-of-change]]"
  - "[[moving-average-crossover]]"
  - "[[trend-following]]"
---

# MACD Crossover Strategy

## Overview

The MACD (Moving Average Convergence Divergence) crossover strategy trades signals generated when the MACD line crosses the signal line. Developed by **Gerald Appel** in the late 1970s, the MACD remains one of the most widely used [[momentum]] indicators in [[technical-analysis]]. The strategy exploits shifts in short-term momentum relative to longer-term momentum, capturing trend transitions early. The [[macd-histogram]] confirms momentum strength and direction, providing additional conviction for entries.

## Rules

### Entry Rules
1. **Bullish Entry:** Go long when the MACD line crosses **above** the signal line while both lines are **below the zero line**. This signals momentum shifting from bearish to bullish early in a potential uptrend.
2. **Bearish Entry:** Go short when the MACD line crosses **below** the signal line while both lines are **above the zero line**. This captures the transition from bullish to bearish momentum.
3. **Confirmation:** The [[macd-histogram]] should be expanding (bars growing) in the direction of the trade to confirm momentum is building, not fading.
4. **Trend Filter:** Use a [[moving-average]] (e.g., 200 EMA) on the higher timeframe to ensure trades align with the dominant trend direction. Only take bullish crossovers in uptrends and bearish crossovers in downtrends.

### Exit Rules
1. **Signal Exit:** Close the position when the MACD line crosses back in the opposite direction of the trade.
2. **Zero-Line Exit:** If the MACD line crosses the zero line against your position, exit immediately as the trend has shifted.
3. **Stop Loss:** Place stops below the most recent [[swing-low]] for longs or above the recent [[swing-high]] for shorts.
4. **Profit Target:** Use a 2:1 reward-to-risk ratio, or trail the stop using the signal line as a dynamic exit.

## Indicators Used

| Indicator | Default Settings | Purpose |
|-----------|-----------------|---------|
| [[macd]] | 12, 26, 9 (EMA) | Primary signal generation |
| [[macd-histogram]] | Derived from MACD | Momentum strength confirmation |
| [[moving-average]] (200 EMA) | 200-period | Trend direction filter |
| [[volume]] | N/A | Confirm conviction on crossover |

## Example Trade

**Setup:** BTC/USD daily chart. Price is trading above the 200 EMA (uptrend confirmed). The MACD line is at -150 and the signal line is at -120, both below zero. The MACD histogram bars are shrinking (becoming less negative).

**Entry:** MACD line crosses above the signal line at price $42,500. Histogram turns positive. Enter long.

**Management:** Stop loss placed below the recent swing low at $40,800. Risk = $1,700 per unit. Target set at $45,900 (2:1 R/R).

**Exit:** Price reaches target at $45,900. Alternative exit: MACD line crosses back below signal line at $44,600, closing the trade for a partial profit.

## Performance Characteristics

- **Win Rate:** Typically 40-55% depending on market conditions and filters applied
- **Best Conditions:** Trending markets with clear directional moves
- **Worst Conditions:** Choppy, range-bound markets produce frequent whipsaws
- **Average Holding Period:** 5-20 days on daily charts (swing timeframe)
- **Frequency:** 2-4 signals per month per instrument on daily charts

## Advantages

- Simple to learn and execute, ideal for beginners entering [[technical-analysis]]
- Works across all liquid markets (stocks, [[crypto]], [[forex]])
- Combines trend and momentum in a single indicator
- The histogram provides early warning of crossover signals
- Widely supported by every charting platform

## Disadvantages

- **Lagging indicator** -- crossovers occur after the move has already begun
- Generates many [[false-signals]] in sideways or choppy markets
- Default settings (12, 26, 9) may not suit all instruments or timeframes
- Can miss fast-moving breakouts due to signal delay
- Should not be used in isolation; always combine with [[support-resistance]] or [[volume-analysis]]
