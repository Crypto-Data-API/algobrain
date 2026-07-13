---
title: "Technical Analysis of the Financial Markets — John Murphy (1999)"
type: concept
created: 2026-04-07
updated: 2026-04-14
status: good
tags: [education, book, technical-analysis, indicators, commodities]
related:
  - "[[technical-analysis-overview]]"
  - "[[rsi]]"
  - "[[macd]]"
  - "[[bollinger-bands]]"
  - "[[moving-average-crossover]]"
  - "[[support-resistance-breakout]]"
  - "[[candlestick-patterns]]"
  - "[[trend-following]]"
  - "[[chart-patterns]]"
  - "[[volume-analysis]]"
  - "[[fibonacci-retracement]]"
  - "[[intermarket-analysis]]"
  - "[[dow-theory]]"
  - "[[multiple-timeframe-analysis]]"
  - "[[sector-rotation]]"
  - "[[john-murphy]]"
  - "[[adx]]"
  - "[[stochastic]]"
  - "[[commodities]]"
---

## Overview

**Technical Analysis of the Financial Markets** by John J. Murphy, originally published as *Technical Analysis of the Futures Markets* in 1986 and substantially revised in 1999, is the single most comprehensive reference on technical analysis. Murphy systematically covers every major branch of TA — chart construction, trend analysis, reversal and continuation patterns, volume and open interest, moving averages, oscillators, point-and-figure charting, candlesticks, Elliott Wave, time cycles, and intermarket analysis. The book treats technical analysis as a self-contained discipline with its own internal logic, grounded in the premise that price discounts everything, prices move in trends, and history repeats itself.

What distinguishes Murphy's work from other TA books is its breadth and its emphasis on intermarket relationships. The final sections demonstrate how bonds, currencies, commodities, and equities are linked in a chain of cause and effect — a framework that remains highly relevant for macro-aware traders. The 1999 edition also integrates candlestick analysis and updates the treatment of oscillators to include modern indicators like [[rsi]], [[macd]], and [[bollinger-bands]]. It is routinely the first book assigned in CMT (Chartered Market Technician) exam preparation.

## Key Takeaways

- **Trend is the foundational concept.** All technical tools exist to identify whether a trend is in place, its direction, its maturity, and when it is likely to reverse. Trading with the trend dramatically improves odds of success.
- **Support and resistance are the most important price levels.** Every chart pattern is ultimately a manifestation of supply and demand clustering at specific prices. Broken support becomes resistance and vice versa.
- **Moving averages are the most versatile indicator.** They smooth price data, define trend direction, and generate signals through crossovers. The 50-day and 200-day MAs are the most widely followed.
- **Volume confirms price.** Volume should increase in the direction of the prevailing trend. Declining volume on rallies or selloffs warns of potential reversal.
- **Oscillators identify extremes.** [[rsi]] overbought (>70) and oversold (<30) levels, [[macd]] divergences, and stochastic crossovers help identify exhaustion points within trends.
- **Chart patterns have measurable reliability.** [[chart-patterns]] like head and shoulders, double tops/bottoms, triangles, and flags have statistically documented success rates and price-target measurement rules.
- **[[candlestick-patterns]] provide granular price action signals.** Engulfing patterns, doji, hammers, and shooting stars reveal short-term sentiment shifts visible on individual bars.
- **[[fibonacci-retracement]] levels identify probable support and resistance.** The 38.2%, 50%, and 61.8% retracement levels consistently attract price in corrective moves.
- **Multiple timeframe analysis is essential.** A signal on a daily chart means more when confirmed by the weekly chart. Murphy recommends analyzing at least three timeframes.
- **Intermarket analysis connects all asset classes.** Bonds lead stocks, the dollar inversely correlates with commodities, and commodity strength signals inflation — these relationships provide context no single-market analysis can.
- **[[bollinger-bands]] measure volatility dynamically.** Prices tend to revert to the middle band (20-period MA), and band width contractions precede explosive moves.
- **No single indicator is sufficient.** Murphy repeatedly emphasizes combining tools — trend indicators with oscillators, price with volume, patterns with support/resistance.

## Who Should Read This

Every trader or investor who uses charts, regardless of market or timeframe. It is especially essential for those studying for the CMT designation. Beginners will find it accessible (Murphy assumes no prior knowledge), while experienced traders benefit from the systematic integration of tools they may use in isolation. Quantitative traders who dismiss TA should still read it to understand the signals their counterparties are acting on.

## How It Applies to AI Trading

Murphy's framework translates almost directly into feature engineering for ML trading models. Moving averages, RSI, MACD, Bollinger Band width, volume ratios, and support/resistance levels are among the most common features in [[technical-analysis-overview]]-based algorithmic systems. The intermarket analysis chapters provide a theoretical basis for multi-asset feature sets — feeding bond yield changes, dollar index movements, and commodity prices into equity models. Chart pattern detection has become a computer vision application, with CNNs trained on candlestick chart images to identify patterns Murphy catalogs manually. The key insight for AI traders: Murphy's toolkit defines the "conventional wisdom" features that markets price around — even if your model discovers something better, it needs to understand what the majority of participants are watching.

## Rating

**9/10** — The most complete single-volume TA reference in existence. Some material on point-and-figure and time cycles feels dated, but the core 80% remains the industry standard. Every technical indicator page in this wiki ultimately traces back to concepts Murphy codified.

## Related

- [[technical-analysis-overview]] — The discipline this book defines
- [[rsi]] — Relative Strength Index, covered in depth in the oscillator chapters
- [[macd]] — Moving Average Convergence Divergence, Murphy's preferred momentum tool
- [[bollinger-bands]] — Volatility bands built on moving average and standard deviation
- [[moving-average-crossover]] — The most basic trend-following signal Murphy describes
- [[support-resistance-breakout]] — The foundational pattern analysis concept
- [[candlestick-patterns]] — Japanese charting techniques integrated in the 1999 revision
- [[trend-following]] — The strategy philosophy underlying all of Murphy's work
- [[chart-patterns]] — Head and shoulders, triangles, flags — all cataloged here
- [[volume-analysis]] — Volume as confirmation tool for price movements
- [[fibonacci-retracement]] — Fibonacci ratios applied to price corrections
