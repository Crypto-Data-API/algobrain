---
title: "Sentiment Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [sentiment, nlp, fear-greed, social-media, contrarian, momentum, funding-rate, quantitative, machine-learning]
aliases: ["Sentiment Analysis Trading", "Social Sentiment Strategy", "Fear and Greed Trading"]
strategy_type: quantitative
timeframe: swing|intraday
markets: [stocks, crypto]
complexity: intermediate
backtest_status: untested
related: ["[[news-trading]]", "[[regime-detection]]", "[[momentum-rotation]]", "[[vix-trading]]", "[[mean-reversion]]", "[[social-arbitrage]]", "[[alternative-data-alpha]]", "[[informational-edge]]"]
---

# Sentiment Trading

## Overview

Sentiment trading aggregates signals from news, social media, on-chain data, and market indicators into a **composite sentiment score**, then trades based on whether sentiment is extreme (contrarian) or trending (momentum). The strategy exploits the behavioral insight that markets are driven by human emotions -- **fear** and **greed** -- and that these emotions create predictable patterns: extreme fear produces oversold bottoms, and extreme greed produces overbought tops.

The approach has evolved dramatically with advances in **natural language processing (NLP)** and machine learning. Modern sentiment systems process thousands of news articles, millions of tweets, Reddit posts, Telegram messages, and on-chain signals in real-time, converting unstructured text and data into quantitative trading signals. What was once subjective ("the market feels fearful") is now measurable: the CNN Fear & Greed Index, crypto Fear & Greed Index, put/call ratios, funding rates, social media mention velocity, and NLP-derived sentiment scores all provide quantifiable inputs.

The strategy can be implemented as **contrarian** (buy extreme fear, sell extreme greed -- a [[mean-reversion]] approach) or **momentum** (ride sentiment waves -- buy when sentiment is accelerating positive, sell when it turns). The contrarian approach has stronger theoretical and empirical support in equity markets (Buffett's "be fearful when others are greedy"), while momentum sentiment works better in crypto where herding behavior and narrative-driven pumps dominate shorter timeframes.

## How It Works

### Sentiment Data Sources

**Market-Based Indicators:**
- **VIX (Fear Gauge):** High [[vix-trading|VIX]] = fear. VIX > 30 = extreme fear (contrarian buy). VIX < 15 = complacency (contrarian caution).
- **Put/Call Ratio:** High ratio (>1.2) = bearish hedging (contrarian buy). Low ratio (<0.7) = bullish complacency (contrarian sell).
- **Funding Rates (Crypto):** High positive funding (>0.05%/8hr) = overcrowded longs (contrarian short or reduce). Negative funding = overcrowded shorts (contrarian long).
- **CNN Fear & Greed Index:** Composite of momentum, volatility, put/call, safe haven demand, breadth, and junk bond demand. Range 0 (extreme fear) to 100 (extreme greed).

**Text-Based Signals (NLP):**
- **News sentiment:** NLP models (FinBERT, GPT-based classifiers) score news articles as positive, negative, or neutral. Aggregate across hundreds of sources.
- **Social media:** Twitter/X mention volume, sentiment polarity, and velocity for specific tickers or crypto tokens. Tools: LunarCrush, Santiment, TheTIE.
- **Reddit/Forum activity:** WallStreetBets mention frequency, bullish/bearish post ratio, meme stock detection.
- **Earnings call transcripts:** NLP analysis of management tone, uncertainty language, and forward guidance sentiment.

**On-Chain Signals (Crypto):**
- **Exchange inflows/outflows:** Large inflows to exchanges = selling pressure (bearish). Outflows = accumulation (bullish).
- **Whale wallet activity:** Large wallets accumulating = bullish signal. Distributing = bearish.
- **Stablecoin supply on exchanges:** High stablecoin reserves on exchanges = "dry powder" ready to buy (bullish).

### Signal Aggregation
1. Normalize each sentiment indicator to a 0-100 scale (0 = extreme bearish, 100 = extreme bullish).
2. Weight the indicators based on historical predictive power (e.g., funding rates may get 25% weight in crypto, VIX 30% weight in stocks).
3. Compute the **composite sentiment score** as the weighted average.
4. Define regimes: 0-20 = extreme fear, 20-40 = fear, 40-60 = neutral, 60-80 = greed, 80-100 = extreme greed.

## Rules / Application

### Contrarian Approach (Mean-Reversion)
1. **Buy signal:** Composite sentiment < 20 (extreme fear). Historically, buying S&P 500 when Fear & Greed < 20 has produced average 3-month returns of +8-12%.
2. **Sell signal:** Composite sentiment > 80 (extreme greed). Reduce equity exposure, raise cash, or initiate short positions.
3. **Confirmation:** Wait for the sentiment score to turn (e.g., Fear & Greed bottoms and begins rising) before buying -- catching the turn rather than the falling knife.
4. **Position sizing:** Scale into positions as sentiment reaches more extreme levels. Buy 25% at score=25, 50% at score=15, 100% at score=5.

### Momentum Approach (Trend-Following)
1. **Buy signal:** Sentiment score crosses above 50 from below (sentiment inflection from bearish to bullish). Social media mention velocity accelerating.
2. **Sell signal:** Sentiment score crosses below 50 from above, or mention velocity peaks and declines.
3. **Crypto application:** In meme coin and altcoin markets, sentiment momentum (rapidly increasing Twitter mentions, Telegram activity) often precedes price pumps by hours to days.
4. **Combine with price:** Only take momentum sentiment signals when price confirms (sentiment improving + price above 20-day MA).

### Funding Rate Strategy (Crypto-Specific)
1. **Short bias when funding > 0.05%/8hr:** Overcrowded longs are paying shorts to hold. Mean reversion likely.
2. **Long bias when funding < -0.03%/8hr:** Overcrowded shorts are paying longs. Squeeze potential.
3. **Neutral when funding is 0.00-0.03%:** No edge from funding rate alone.

## Example

**Setup:** Contrarian sentiment strategy on Bitcoin using composite sentiment score.

1. **Inputs:** Crypto Fear & Greed Index (25% weight), BTC funding rate (25%), exchange net flows (20%), Twitter sentiment (15%), on-chain whale activity (15%).
2. **June 15:** BTC drops from $70K to $55K over 2 weeks. Fear & Greed Index: 12 (extreme fear). Funding rate: -0.04% (shorts overcrowded). Exchange outflows: +$800M in 48 hours (whales accumulating). Twitter sentiment: 18/100. Composite score: **14 (extreme fear).**
3. **June 17:** Composite score bottoms at 11 and begins rising (12, 14, 17 over 3 days). **Enter long:** Buy BTC at $56,500. Position size: 75% of target (waiting for potential lower retest).
4. **June 18:** BTC retests $55,000. Composite holds above 10. **Add remaining 25%** at $55,200.
5. **July 5:** BTC recovers to $64,000. Composite score: 55 (neutral). **Exit half** for +$8,500 profit on 0.5 BTC.
6. **July 20:** BTC reaches $68,000. Composite score: 72 (greed). **Exit remaining** for +$12,800 total profit on the position.
7. **Win rate context:** Over 10 similar extreme-fear signals in the past 3 years, 8 produced profitable trades within 30 days (80% win rate), with average returns of +15%.

## Advantages

- **Quantifies emotions:** Converts subjective market "feel" into measurable, tradable signals
- Contrarian sentiment signals have **strong empirical backing** -- extreme fear has historically been a reliable buy signal in both equities and crypto
- **Multiple data sources** provide redundancy: if one indicator is noisy, others can confirm or filter
- NLP and ML advances have dramatically improved the speed and accuracy of text-based sentiment extraction
- Funding rates in crypto provide a **direct measure of positioning** (longs vs shorts), which is unavailable in traditional markets
- The strategy is flexible: can be applied as contrarian (mean-reversion) or momentum depending on the market and timeframe
- Sentiment data is increasingly available via APIs (Santiment, LunarCrush, TheTIE, Alternative.me), reducing implementation barriers

## Disadvantages

- **Sentiment can stay extreme longer than you can stay solvent:** Extreme fear can persist for months during genuine bear markets (2008, 2022), and contrarian buyers get destroyed
- **NLP is imperfect:** Sarcasm, context, and nuance in social media text are difficult for models to interpret correctly. "This stock is a total rocket" could be bullish or sarcastic
- **Garbage data:** Social media is full of bots, paid promoters, and coordinated manipulation campaigns, especially in crypto. Fake sentiment can produce false signals
- **Lagging indicator:** By the time a composite sentiment score registers "extreme fear," the move has largely happened. The signal may indicate the bottom or just the beginning of a deeper decline
- **Overfitting risk:** With dozens of sentiment indicators and weighting schemes, it is easy to optimize a model that worked historically but fails forward
- Sentiment signals have **low frequency** in equity markets (extreme readings occur only a few times per year), limiting trading opportunities
- The strategy requires **continuous data feeds** and processing infrastructure -- more complex than purely price-based strategies

## See Also

- [[news-trading]] -- event-driven approach that overlaps with sentiment from news NLP
- [[vix-trading]] -- VIX as a key sentiment indicator and tradable instrument
- [[regime-detection]] -- combining sentiment with statistical regime models for enhanced signals
- [[momentum-rotation]] -- price momentum that often correlates with sentiment momentum
- [[mean-reversion]] -- the market behavior contrarian sentiment trading exploits
