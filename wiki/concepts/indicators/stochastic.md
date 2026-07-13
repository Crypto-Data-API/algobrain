---
title: Stochastic Oscillator
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [stochastic, indicators, technical-analysis]
aliases: [stochastic-oscillator, stochastics]
domain: [indicators]
difficulty: beginner
related:
  - "[[rsi]]"
  - "[[momentum]]"
  - "[[moving-averages]]"
  - "[[support-and-resistance]]"
  - "[[john-murphy]]"
  - "[[george-lane]]"
  - "[[larry-williams]]"
  - "[[williams-percent-r]]"
  - "[[technical-analysis-of-the-financial-markets]]"
  - "[[commodities]]"
  - "[[commodity-seasonality-patterns]]"
  - "[[multiple-timeframe-analysis]]"
---

# Stochastic Oscillator

The Stochastic Oscillator is a momentum indicator that compares an asset's closing price to its price range over a specified period, producing a reading between 0 and 100.

## Overview

Developed by George Lane in the 1950s, the stochastic is based on the observation that in uptrends, prices tend to close near the high of the range, and in downtrends, near the low. When closing prices start deviating from this pattern, it signals weakening momentum.

## How It Works

- **%K line (fast)**: ((Current close - Lowest low over N periods) / (Highest high - Lowest low over N periods)) x 100. Default period is 14.
- **%D line (slow)**: 3-period SMA of %K. Acts as a signal line, similar to [[macd]]'s signal line.
- **Overbought (>80)**: Price is closing near the top of its recent range. May be extended.
- **Oversold (<20)**: Price is closing near the bottom of its recent range. May be due for a bounce.

## Key Signals

- **%K/%D crossover**: When %K crosses above %D in oversold territory, it generates a buy signal. When %K crosses below %D in overbought territory, it generates a sell signal.
- **Divergence**: Similar to [[rsi]], when price makes a new extreme but the stochastic does not, it warns of potential reversal.
- **Bull/bear setup**: George Lane emphasized the divergence between %D and price as the most reliable signal, calling it a "setup" that precedes a turn.

## Variants

- **Fast stochastic**: Uses raw %K and its SMA (%D). Very sensitive and generates many signals.
- **Slow stochastic**: Smooths the fast %K with a 3-period SMA before calculating %D. Fewer signals, less noise. Most traders use the slow version.

## Trading Relevance

The stochastic excels in range-bound markets for identifying turning points. Like [[rsi]], it can remain overbought or oversold for extended periods during strong trends, so it is most reliable when combined with trend identification tools like [[moving-averages]]. Many traders use stochastic on higher timeframes for trend bias and on lower timeframes for entry timing.

## Commodity Applications

Murphy notes that the stochastic oscillator is useful for identifying short-term reversals in agricultural and soft [[commodities]], where seasonal supply/demand cycles create predictable turning points (Source: [[book-technical-analysis-of-the-financial-markets]]).

In [[commodity-seasonality-patterns|seasonal commodity trading]], stochastic signals aligned with seasonal tendencies significantly increase win rate. When the seasonal pattern suggests a turning point is due (e.g., grain harvest lows, natural gas winter demand peaks) and the stochastic confirms with an overbought/oversold crossover, the combined signal is more robust than either alone.

Key commodity applications:

- **Soft commodities**: The slow stochastic on weekly charts of [[coffee]], [[sugar]], and [[cocoa]] can identify seasonal turning points. These markets have pronounced annual cycles driven by crop production, and the stochastic's range-positioning logic maps naturally onto seasonal price ranges.
- **[[multiple-timeframe-analysis|Multiple timeframe approach]]**: Weekly stochastic for trend direction in the commodity, daily stochastic for entry timing. When both are oversold and turning up simultaneously in a commodity with bullish seasonal tendencies, it creates a high-probability long entry.
- **Energy markets**: Stochastic readings in [[crude-oil]] and [[natural-gas]] combined with inventory data ([[eia|EIA]] weekly reports) provide a sentiment + fundamental confirmation framework.

Because commodity markets are more prone to genuine mean-reversion around production costs and seasonal norms than equities (which can trend indefinitely on earnings growth), the stochastic's overbought/oversold framework is arguably more appropriate for commodities than for stocks.

## Related Indicator: Williams %R

[[williams-percent-r|Williams %R]], created by [[larry-williams|Larry Williams]] in 1973, is essentially a mirror image of the Stochastic %K line. While the Stochastic %K measures where the close sits within the period range on a 0–100 scale (100 = at the high, 0 = at the low), Williams %R measures the distance of the close from the period high on a 0 to −100 scale (0 = at the high, −100 = at the low). The two indicators produce equivalent signals but with inverted scales (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study across US equities reported a 44.9% win rate for Stochastics. The moderate win rate reflects that the Stochastic, like most oscillators, works best in range-bound regimes where it identifies turning points. In trending markets, overbought/oversold signals produce whipsaws that lower the overall win rate (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy covers the stochastic oscillator in the oscillators chapter alongside [[rsi|RSI]], including George Lane's original framework, slow vs fast variants, and divergence analysis (Source: [[book-technical-analysis-of-the-financial-markets]])
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Williams %R connection, win-rate data, George Lane attribution
- Lane, George C. (1984), "Lane's Stochastics," *Technical Analysis of Stocks & Commodities*, Vol. 2 — Lane's own account of the oscillator and the %D/price divergence "setup"
- Williams, Larry (1973) — introduction of the %R oscillator (Williams %R)

## Related

- [[rsi]] -- similar overbought/oversold oscillator
- [[momentum]] -- stochastic measures momentum via range position
- [[moving-averages]] -- used to determine trend context for stochastic signals
- [[commodities]] -- stochastic excels at identifying commodity turning points
- [[commodity-seasonality-patterns]] -- stochastic aligned with seasonal patterns increases win rate
- [[multiple-timeframe-analysis]] -- weekly/daily stochastic framework for commodities
- [[john-murphy]] -- covers stochastic as a core oscillator in his technical analysis framework
