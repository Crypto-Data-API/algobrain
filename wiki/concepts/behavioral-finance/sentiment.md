---
title: Market Sentiment
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [behavioral-finance, volatility, indicators]
aliases: [sentiment, market-mood, market sentiment, investor sentiment]
domain: [behavioral-finance, market-microstructure]
prerequisites: ["[[behavioral-finance]]", "[[volatility]]"]
difficulty: beginner
related:
  - "[[volatility]]"
  - "[[volume]]"
  - "[[momentum]]"
  - "[[vix]]"
  - "[[funding-rate]]"
  - "[[mean-reversion]]"
  - "[[behavioral-finance]]"
  - "[[signal-vs-noise]]"
---

# Market Sentiment

Market sentiment is the overall attitude or mood of investors and traders toward an asset or market, reflecting collective psychology rather than fundamental value.

## Overview

Sentiment drives markets in the short to medium term, often causing prices to overshoot or undershoot fundamental value. Extreme greed fuels bubbles; extreme fear creates capitulation bottoms. Understanding sentiment helps traders identify when the crowd is likely wrong and position accordingly, or ride the momentum when sentiment aligns with the trend.

## Key Sentiment Indicators

- **Fear & Greed Index**: Aggregates multiple signals (volatility, momentum, market breadth, safe-haven demand) into a 0-100 scale. Extreme fear (< 20) often marks buying opportunities; extreme greed (> 80) warns of complacency.
- **VIX**: The [[volatility]] index for S&P 500 options. Spikes in VIX reflect fear; low VIX reflects complacency.
- **Put/Call ratio**: High ratio (more puts than calls) indicates bearish sentiment; low ratio indicates bullish sentiment.
- **Social media sentiment**: Analyzing Twitter/X, Reddit, and Telegram for crowd mood using NLP. Useful but noisy.
- **Funding rates**: In crypto perpetual futures, high positive funding rates indicate crowded longs (bullish sentiment); negative funding indicates crowded shorts.

## How It Works

### Contrarian Signals

Extreme sentiment readings often mark turning points. When everyone is bullish, there are few buyers left to push prices higher. When everyone is bearish, most selling has already occurred. Contrarian traders fade extreme sentiment readings.

### Sentiment Confirmation

In trending markets, sentiment aligned with the trend confirms its continuation. Bearish sentiment during a downtrend suggests lower prices ahead; bullish sentiment during an uptrend suggests more upside.

## Academic Evidence

Sentiment is not merely folk wisdom — it has a measurable, predictive footprint. Baker & Wurgler (2006) constructed a composite **investor-sentiment index** (from IPO volume, first-day IPO returns, the closed-end fund discount, NYSE turnover, the equity share in new issues, and the dividend premium) and showed that when sentiment is *high*, the subsequent returns of speculative, hard-to-value, hard-to-arbitrage stocks (small, young, unprofitable, high-volatility, distressed) are *low* — and vice versa. Sentiment matters most precisely where arbitrage is most limited, consistent with the [[behavioral-finance]] view that mispricing persists when smart money cannot cheaply correct it. The AAII Investor Sentiment Survey (bull-bear spread) and the University of Michigan Consumer Sentiment index are widely tracked weekly/monthly gauges with documented contrarian properties at extremes.

## Trading Relevance

Sentiment is most useful at extremes. In the middle range, it provides little edge — most sentiment readings are [[signal-vs-noise|noise]]. Combine sentiment indicators with [[support-and-resistance]], [[volume]], and [[momentum]] for higher-conviction trades. Never use sentiment alone -- it tells you the crowd's position, but the crowd can remain irrational longer than you can remain solvent.

Two practical framings:

- **Contrarian at extremes**: extreme readings (Fear & Greed < 20 or > 80, AAII bull-bear at multi-year tails, crypto funding deeply negative) flag exhaustion and elevated [[mean-reversion]] odds. These are *conditions*, not triggers — wait for price confirmation before fading.
- **Trend confirmation in the body**: in the middle range, sentiment aligned with the prevailing trend supports continuation. Divergence (price up, sentiment souring) can foreshadow a turn but is unreliable as a standalone signal.

A recurring failure mode is treating a sentiment indicator as a precise timing tool. Sentiment identifies *vulnerability*, not the moment of reversal; position sizing and stops must assume the extreme can persist or intensify.

## Related

- [[volatility]] / [[vix]] -- the VIX is a key fear/complacency gauge
- [[momentum]] -- sentiment drives and confirms momentum
- [[funding-rate]] -- the dominant crypto-perp sentiment proxy
- [[mean-reversion]] -- the edge that extreme sentiment readings flag
- [[signal-vs-noise]] -- why mid-range sentiment carries little information
- [[behavioral-finance]] -- the framework explaining why sentiment moves prices

## Sources

- Malcolm Baker & Jeffrey Wurgler, "Investor Sentiment and the Cross-Section of Stock Returns" (*Journal of Finance*, 2006) — the canonical investor-sentiment index and its predictive cross-sectional effects.
- Malcolm Baker & Jeffrey Wurgler, "Investor Sentiment in the Stock Market" (*Journal of Economic Perspectives*, 2007).
- CNN Business — *Fear & Greed Index* methodology. https://www.cnn.com/markets/fear-and-greed
- American Association of Individual Investors — *AAII Investor Sentiment Survey* (weekly bull-bear spread).
- Cboe — *VIX Index* white paper and methodology. https://www.cboe.com/tradable_products/vix/
