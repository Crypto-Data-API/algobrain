---
title: "Sentiment Analysis"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [behavioral-finance, machine-learning, trading-psychology]
aliases: ["Market Sentiment"]
domain: [behavioral-finance, quantitative]
prerequisites: ["[[behavioral-finance]]", "[[technical-analysis]]"]
difficulty: intermediate
related: ["[[behavioral-finance]]", "[[nlp-sentiment-analysis]]", "[[vix]]", "[[trading-psychology]]"]
---

Sentiment analysis in trading is the practice of measuring the collective mood, positioning, and expectations of market participants. It serves as both a confirming indicator (trending sentiment aligns with price) and a powerful contrarian signal (extreme sentiment often marks turning points).

## Sentiment Indicators

### Fear & Greed Index
CNN's Fear & Greed Index aggregates seven factors into a single 0-100 score:
- Market momentum (S&P 500 vs. 125-day MA)
- Stock price strength (52-week highs vs. lows)
- Stock price breadth (advancing vs. declining volume)
- Put/call ratio
- [[vix|VIX]] level
- Junk bond demand (spread over Treasuries)
- Market volatility

**Readings**: 0-25 = Extreme Fear (contrarian buy signal), 75-100 = Extreme Greed (contrarian sell signal)

### VIX (Volatility Index)
The [[vix|VIX]] measures implied [[volatility]] from [[options-overview|S&P 500 options]] prices:
- **VIX < 15**: Complacency / low fear
- **VIX 15-25**: Normal range
- **VIX 25-40**: Elevated fear
- **VIX > 40**: Panic -- historically marks major bottoms

### Put/Call Ratio
The ratio of [[options-overview|put]] volume to call volume:
- **High put/call** (>1.0): Excessive hedging/bearishness -- contrarian bullish
- **Low put/call** (<0.7): Excessive bullishness/complacency -- contrarian bearish
- CBOE equity put/call and index put/call ratios are the most commonly used

### Commitments of Traders (COT) Report
Weekly CFTC report showing positioning of commercial hedgers, large speculators, and small speculators in [[futures]] markets:
- **Commercials** (hedgers): Tend to be right at extremes -- follow their positioning
- **Large speculators** (trend followers): Tend to be wrong at extremes
- **Small speculators**: Most consistently wrong at extremes -- strong contrarian signal

### Fund Flow Data
Net inflows and outflows from mutual funds, ETFs, and investment products:
- Large inflows after extended rallies suggest late-stage buying (bearish)
- Large outflows after extended declines suggest capitulation (bullish)

### Social Media and NLP Sentiment
[[machine-learning|Machine learning]] and [[nlp-sentiment-analysis|NLP]] techniques applied to:
- Twitter/X posts, Reddit (r/wallstreetbets), StockTwits
- Financial news headlines
- Earnings call transcripts
- Google Trends search volume

Quantitative approaches assign sentiment scores to text data and aggregate across sources for a composite social sentiment reading.

## Crypto-Specific Sentiment

- **Crypto Fear & Greed Index**: Alternative.me's index using volatility, volume, social media, dominance, and trends
- **[[funding-rates]]**: Positive/negative perpetual funding reflects leveraged long/short sentiment
- **Exchange flows**: Large inflows to exchanges suggest selling intent; outflows to cold storage suggest accumulation
- **Stablecoin supply**: Growing [[stablecoins|stablecoin]] supply on exchanges indicates potential "dry powder" for buying

## Using Sentiment as a Trading Signal

### Contrarian Approach
The most robust use of sentiment is as a **contrarian** indicator:
- "Be fearful when others are greedy, and greedy when others are fearful" -- Warren Buffett
- Extreme sentiment readings have a strong historical track record of marking inflection points
- Best used in conjunction with [[technical-analysis|technical]] and fundamental analysis, not in isolation

### Trend Confirmation
Sentiment can also confirm existing trends:
- Gradually improving sentiment during an uptrend confirms underlying demand
- Deteriorating sentiment during a downtrend confirms supply pressure

### Limitations
- Sentiment can remain extreme for extended periods during strong trends
- Social media sentiment is easily manipulated (bots, coordinated campaigns)
- Different indicators can give conflicting signals
- Timing is imprecise -- extreme sentiment tells you "what" but not "when"

## Related

- [[behavioral-finance]] -- Theoretical foundation for why sentiment matters
- [[trading-psychology]] -- Individual cognitive biases that aggregate into market sentiment
- [[vix]] -- The primary institutional fear gauge

## Sources

- Sentiment analysis techniques are documented across [[behavioral-finance]] literature and quantitative trading research
