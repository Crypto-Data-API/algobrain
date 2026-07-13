---
title: Rate of Change (ROC) Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - momentum
  - roc
  - oscillator
  - rate-of-change
  - zero-line-crossover
strategy_type: momentum
timeframe: swing
markets:
  - stocks
  - crypto
complexity: beginner
backtest_status: untested
related:
  - "[[macd-crossover]]"
  - "[[rsi-divergence]]"
  - "[[momentum-rotation]]"
  - "[[moving-average-crossover]]"
---

# Rate of Change (ROC) Strategy

## Overview

The Rate of Change (ROC) indicator measures the **percentage change** in price over a specified number of periods, providing a pure [[momentum]] reading. A positive ROC indicates upward momentum (price is higher than N periods ago), while a negative ROC indicates downward momentum. The strategy uses **zero-line crossovers** as primary signals: crossing above zero signals a shift to bullish momentum, and crossing below zero signals bearish momentum. ROC can also be applied as a bounded [[oscillator]] to identify overbought/oversold conditions and [[divergence]] setups similar to [[rsi-divergence]].

## Rules

### Entry Rules
1. **Bullish Zero-Line Cross:** Enter long when ROC crosses **above zero** from negative territory. This confirms that current price has surpassed the price from N periods ago, indicating fresh upward momentum.
2. **Bearish Zero-Line Cross:** Enter short when ROC crosses **below zero** from positive territory.
3. **Trend Filter:** Only take long signals when price is above the 50-period [[moving-average]]; only take short signals when price is below the 50 MA. This filters out counter-trend noise.
4. **Momentum Threshold:** For stronger signals, require ROC to cross above +2% (long) or below -2% (short) rather than exactly zero, filtering out weak or choppy crossovers.
5. **Divergence Entry:** Like [[rsi-divergence]], look for price/ROC divergence at extremes for reversal trades.

### Exit Rules
1. **Opposite Crossover:** Exit longs when ROC crosses back below zero; exit shorts when ROC crosses back above zero.
2. **Momentum Fade:** If ROC is positive but declining (momentum weakening), tighten stops or take partial profits.
3. **Stop Loss:** Use a fixed ATR-based stop (e.g., 2x [[atr]] below entry for longs).
4. **Time Stop:** If the trade has not reached 1R profit within 10 bars, re-evaluate and consider closing.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[rate-of-change]] | 12-period (default) | Primary momentum signal |
| [[moving-average]] | 50-period SMA or EMA | Trend direction filter |
| [[atr]] | 14-period | Stop loss calculation |
| [[volume]] | N/A | Confirm momentum shifts |

## Example Trade

**Setup:** AAPL daily chart. Price is trading above the 50 EMA (uptrend). ROC(12) has been negative for 8 days during a pullback, currently reading -1.5%.

**Entry:** ROC(12) crosses above zero, reading +0.3%. Price is $185.20. Enter long on the close.

**Management:** ATR(14) = $3.10. Stop loss placed at $185.20 - (2 x $3.10) = $179.00. Risk = $6.20. Target at $197.60 (2:1 R/R).

**Exit:** ROC continues rising to +4.8% as price reaches $194.50. ROC then starts declining. When ROC crosses back below zero at $191.00, exit the position for a $5.80 profit per share.

## Performance Characteristics

- **Win Rate:** 40-50% on raw zero-line crossovers; improves to 50-60% with trend filter
- **Best Conditions:** Trending markets with sustained directional moves
- **Worst Conditions:** Range-bound, choppy markets where price oscillates around the lookback price
- **Average Holding Period:** 5-15 days on daily charts
- **Simplicity:** One of the most straightforward momentum indicators to compute and interpret

## Advantages

- Extremely simple to calculate and understand -- pure percentage price change
- No smoothing lag like [[macd-crossover]]; directly reflects price momentum
- Versatile: works as both a zero-line crossover system and an oscillator for overbought/oversold readings
- Can be applied to any timeframe and any liquid market
- Useful as a ranking tool in [[momentum-rotation]] and [[quantitative-strategies]]
- Easy to combine with other indicators for [[confluence]]

## Disadvantages

- Raw ROC is **noisy** and produces frequent whipsaws around the zero line in choppy conditions
- No built-in overbought/oversold levels (unlike [[relative-strength-index]]); levels vary by asset and timeframe
- Lookback period selection (N) significantly impacts results and requires optimization per instrument
- Does not account for [[volatility]] -- a 5% ROC in a low-vol stock is more significant than in a high-vol crypto asset
- Should be combined with a trend filter or additional confirmation; unreliable as a standalone signal
