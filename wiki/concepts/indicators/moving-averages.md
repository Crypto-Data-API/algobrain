---
title: Moving Averages
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [moving-averages, technical-analysis, indicators]
aliases: [MA, moving-average, "50-day-ma", "50 day MA", "50 DMA"]
domain: [indicators]
difficulty: beginner
prerequisites: ["[[technical-analysis-overview]]"]
related:
  - "[[macd]]"
  - "[[bollinger-bands]]"
  - "[[support-and-resistance]]"
  - "[[momentum]]"
  - "[[john-murphy]]"
  - "[[technical-analysis-of-the-financial-markets]]"
  - "[[commodities]]"
  - "[[trend-following-cta]]"
  - "[[golden-cross]]"
  - "[[death-cross]]"
  - "[[intermarket-analysis]]"
---

# Moving Averages

A moving average is a smoothed representation of an asset's price over a specified number of periods, used to identify trend direction and dynamic [[support-and-resistance]].

## Overview

Moving averages filter out short-term noise to reveal the underlying trend. They are among the most widely used indicators in technical analysis, forming the basis of many other indicators including [[macd]] and [[bollinger-bands|Bollinger Bands]].

## Key Types

- **Simple Moving Average (SMA)**: Arithmetic mean of price over N periods. Each data point weighted equally. The 50-day and 200-day SMAs are the most watched.
- **Exponential Moving Average (EMA)**: Weights recent prices more heavily, making it more responsive to new data. The 12-day and 26-day EMAs are used in [[macd]].
- **Weighted Moving Average (WMA)**: Linearly weights prices, with the most recent having the highest weight.

## Key Signals

- **Golden cross**: Short-term MA (e.g., 50-day) crosses above long-term MA (e.g., 200-day). Considered a bullish signal.
- **Death cross**: Short-term MA crosses below long-term MA. Considered bearish.
- **Price vs MA**: Price above its MA suggests an uptrend; below suggests a downtrend.
- **MA as support/resistance**: In uptrends, pullbacks to the MA often find support. In downtrends, rallies to the MA often meet resistance.

## Trading Relevance

Moving averages are lagging indicators -- they confirm trends rather than predict them. Shorter periods (10, 20) react faster but produce more false signals; longer periods (100, 200) are smoother but slower. Many traders use multiple MAs together (e.g., 9/21 EMA for short-term, 50/200 SMA for long-term) to capture different timeframes. MAs work best in trending markets and produce whipsaws in range-bound conditions.

## Commodity Applications

Murphy's framework applies moving averages extensively to commodity futures, where they serve as the primary trend-identification tool for both discretionary and systematic traders (Source: [[book-technical-analysis-of-the-financial-markets]]).

- **The 200-day MA** is THE key support/resistance level for all [[commodities]]. When [[gold]], [[crude-oil]], or [[copper]] trade above their 200-day MA, it defines a bull market regime; below it defines a bear market. Many institutional commodity mandates use position relative to the 200-day MA as their primary allocation filter.
- **The 50/200 MA system** (the [[golden-cross]] and [[death-cross]]) is used by [[trend-following-cta|CTA funds]] across the commodity futures universe as a systematic entry/exit signal. Its simplicity is a feature, not a bug -- it captures the meat of major commodity trends while avoiding most whipsaws.
- **EMAs (shorter periods, 10/20)** tend to work better than SMAs in commodity markets due to higher volatility and more pronounced trend persistence. The 10/20 EMA crossover system is a staple of short-term commodity trading, particularly in energy markets where price moves are sharp and news-driven.
- **Multiple MA envelopes** -- plotting bands at fixed percentages above and below a long-term MA -- help commodity traders identify stretched conditions. When [[natural-gas]] trades 20%+ above its 200-day MA, mean-reversion setups become attractive.

## Adaptive and Advanced MAs

Modern variations of moving averages address the classic lag problem inherent in all MA calculations:

- **Hull Moving Average (HMA)**: Uses weighted moving averages and a square root of the period to dramatically reduce lag while maintaining smoothness. Popular among active commodity traders.
- **Double Exponential Moving Average (DEMA)** and **Triple Exponential Moving Average (TEMA)**: Patrick Mulloy's designs that reduce lag by applying EMA calculations recursively. TEMA is particularly responsive for fast-moving markets.
- **Kaufman Adaptive Moving Average (KAMA)**: Adjusts its smoothing based on market noise -- fast in trending markets, slow in choppy ones. This self-adjusting behavior makes it well-suited to commodities that alternate between strong trends and range-bound consolidation.

While these advanced MAs offer reduced lag, they also produce more false signals during choppy conditions. The classic SMA and EMA remain dominant in systematic commodity trading because their behavior is well-understood, easily backtested, and robust across different market regimes.

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy considers moving averages the most versatile and widely used indicator in technical analysis, covering SMA, EMA, WMA, crossover systems, and their application to all asset classes including commodities (Source: [[book-technical-analysis-of-the-financial-markets]])
- Mulloy, Patrick (1994), "Smoothing Data with Faster Moving Averages," *Technical Analysis of Stocks & Commodities* — original DEMA/TEMA designs
- Kaufman, Perry J. (1995), *Smarter Trading* — Kaufman Adaptive Moving Average (KAMA)
- Hull, Alan (2005) — Hull Moving Average (HMA)

## Related

- [[macd]] -- derived from exponential moving averages
- [[bollinger-bands]] -- built around a moving average
- [[support-and-resistance]] -- MAs act as dynamic S/R
- [[momentum]] -- MA crossovers signal momentum shifts
- [[commodities]] -- MAs are the primary trend tool for commodity futures
- [[trend-following-cta]] -- CTA funds rely on MA crossover systems
- [[golden-cross]] -- bullish 50/200 MA crossover
- [[death-cross]] -- bearish 50/200 MA crossover
- [[intermarket-analysis]] -- MAs applied across related markets
- [[john-murphy]] -- covers MAs as the foundational indicator in his framework
