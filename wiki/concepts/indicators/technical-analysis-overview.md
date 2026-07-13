---
title: "Technical Analysis"
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
confidence: medium
tags: [technical-analysis, strategies, concepts]
aliases: ["TA", "Charting", "Chart Analysis", "technical-analysis"]
domain: [technical-analysis]
prerequisites: []
difficulty: beginner
related: ["[[fundamental-analysis]]", "[[indicators]]", "[[support-and-resistance]]", "[[moving-averages]]"]
---

# Technical Analysis

**Technical analysis (TA)** is the study of past price and [[volume]] data to identify patterns, trends, and signals that may forecast future price movements. Unlike [[fundamental-analysis]], which evaluates intrinsic value from financial data or utility, TA assumes all relevant information is already reflected in the price.

## The Three Pillars

Originally articulated in Dow Theory (late 1800s):

1. **Price Discounts Everything**: All known information -- fundamentals, news, [[sentiment]], expectations -- is incorporated into the current price. The analyst's job is to read the price.
2. **Price Moves in Trends**: Markets trend upward, downward, or sideways. A trend is more likely to continue than reverse until it shows clear exhaustion.
3. **History Tends to Repeat**: Recurring psychological patterns (fear, greed, FOMO, panic) create recognizable chart formations across markets and timeframes. See [[behavioral-finance]].

## Major Tools and Techniques

### Support and Resistance

[[support-and-resistance]] are price levels where buying or selling pressure concentrates. **Support** acts as a floor; **resistance** as a ceiling. Broken support often becomes resistance and vice versa -- one of TA's most reliable patterns. These levels arise from market memory and clusters of [[order-flow]].

### Chart Patterns

**Reversal patterns**: [[head-and-shoulders]], double/triple tops and bottoms, rounding formations. **Continuation patterns**: [[flags-and-pennants|flags and pennants]], triangles, rectangles. **Breakout patterns**: cup and handle, wedges. Reliability improves when confirmed by [[volume]].

### Candlestick Patterns

[[candlestick-patterns]] originated in 18th-century Japanese rice trading. Single candle (doji, hammer, shooting star), two-candle (engulfing, piercing line), and three-candle (morning/evening star, three soldiers/crows) patterns remain among the most popular TA tools.

## Categories of Indicators

### Trend-Following

Best in trending markets; generate false signals in ranges.

| Indicator | Shows | Key Levels |
|-----------|-------|------------|
| [[moving-averages]] (SMA, EMA) | Smoothed average price | 20, 50, 200-period |
| [[macd]] | Moving average convergence/divergence | Signal line crossovers |
| [[adx]] | Trend strength (not direction) | >25 trending, <20 ranging |

The 200-day SMA is widely considered the bull/bear dividing line by institutional traders.

### Oscillators

Best in range-bound markets; can stay extreme during strong trends.

| Indicator | Shows | Key Levels |
|-----------|-------|------------|
| [[rsi]] | Overbought/oversold momentum | >70 overbought, <30 oversold |
| [[stochastic]] | Price position in recent range | >80 overbought, <20 oversold |
| [[cci]] | Deviation from mean | >100 / <-100 |

**[[divergence]]** is key: when price makes a new high but [[rsi]] does not, it signals weakening [[momentum]].

### Volume Indicators

| Indicator | Shows |
|-----------|-------|
| [[obv]] | Cumulative volume flow |
| [[vwap]] | Volume-weighted average price |
| Volume Profile | Volume distribution at each price level |

Core principle: **volume confirms price**. Breakouts on high volume are credible; low-volume moves are suspect.

### Volatility Indicators

| Indicator | Shows |
|-----------|-------|
| [[bollinger-bands]] | Standard deviation price envelopes |
| [[atr]] | Average price range over N periods |

[[bollinger-bands]] squeeze (narrowing bands) often precedes significant breakouts. [[atr]] is essential for [[volatility]]-adjusted [[stop-loss]] placement and [[position-sizing]].

## Timeframes

| Style | Charts | Holding Period |
|-------|--------|---------------|
| Scalping | 1m, 5m, 15m | Seconds to minutes |
| Day Trading | 5m, 15m, 1h | Minutes to hours |
| Swing Trading | 1h, 4h, Daily | Days to weeks |
| Position Trading | Daily, Weekly | Weeks to months |

**Multiple timeframe analysis** is best practice: identify trend on a higher timeframe, find entries on a lower one.

## TA in Crypto vs. Stocks

Crypto-specific factors: 24/7 markets (no gaps), higher [[volatility]] requiring adjusted settings, [[perpetual-futures]] data ([[open-interest]], [[funding-rate]], [[liquidation]] levels) as crucial context, [[on-chain-analysis]] as a complement, and thinner [[order-books]] on altcoins making manipulation easier. Stock-specific: session gaps, earnings cycles, sector rotation, and more mature [[market-microstructure]].

## Criticisms and Defenses

- **[[efficient-market-hypothesis]]**: Prices reflect all information, so TA cannot outperform. *Counter*: Markets are imperfectly efficient, especially crypto. [[behavioral-finance]] documents exploitable biases.
- **Random Walk Theory**: Past prices contain no useful information. *Counter*: [[momentum]] strategies have been shown to work across markets in academic studies.
- **Self-fulfilling prophecy**: TA works only because people believe in it. *Counter*: Even if true, that makes it useful by definition.
- **Data fitting**: Patterns found in hindsight often fail forward. *Counter*: Valid for some patterns. Focus on well-documented, high-probability setups with proper [[risk-management]].

## Common Misconceptions

1. **"TA predicts the future"** -- It identifies probabilities, not certainties. Combine with [[risk-management]].
2. **"More indicators = better"** -- Overload causes conflicting signals. Two or three well-understood indicators suffice.
3. **"TA works the same everywhere"** -- Application must adapt to each market's [[volatility]], [[liquidity]], and participant base.
4. **"If the indicator says buy, you should buy"** -- Context matters. [[rsi]] above 70 in a strong uptrend may indicate [[momentum]], not a sell signal.
5. **"TA is just drawing lines"** -- At its best, TA quantifies market psychology, [[order-flow]], and probability.

## Further Reading

- [[indicators]] -- Comprehensive guide to technical indicators
- [[support-and-resistance]] -- Key price levels in TA
- [[moving-averages]] -- The foundational trend-following indicator
- [[rsi]] -- The most popular momentum oscillator
- [[fundamental-analysis]] -- The complementary valuation approach
- [[risk-management]] -- Essential companion to any TA-based strategy
- [[behavioral-finance]] -- The psychology that underpins TA
