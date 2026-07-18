---
title: "Crypto Fear & Greed Index"
type: concept
created: 2026-07-17
updated: 2026-07-19
status: draft
tags: [crypto, market-regime, sentiment, behavioral-finance, indicators]
aliases: ["Crypto F&G Index", "Fear and Greed Index", "Alternative.me Fear & Greed"]
domain: [behavioral-finance, market-microstructure]
difficulty: beginner
prerequisites: ["[[behavioral-finance-overview]]", "[[market-regime]]"]
---

# Crypto Fear & Greed Index

The **Crypto Fear & Greed Index** is a daily composite sentiment indicator published by Alternative.me that aggregates multiple market signals into a single 0–100 score: 0 = "Extreme Fear," 100 = "Extreme Greed." It was first published in 2018 and tracks the emotional state of the crypto market, functioning as a contrarian regime gauge — extreme fear historically precedes reversals, extreme greed precedes corrections. It is one of the most widely cited crypto-specific sentiment tools and the primary crypto input in the [[contrarian-extremes]] strategy's composite score.

## How It Works

The index is a weighted composite of six input signals, re-weighted over time (current approximate weights as of 2024–25):

| Component | Weight | What it measures |
|-----------|--------|-----------------|
| **Volatility** | 25% | Current BTC volatility vs. 30-day and 90-day averages. Higher-than-average vol → fear. |
| **Market momentum/volume** | 25% | Current BTC volume vs. 30/90-day averages. Falling volume with rising price → greed; high volume on down days → fear. |
| **Social media** | 15% | Twitter/X post volume and engagement on crypto hashtags. Abnormally high engagement → greed. |
| **Surveys** | 15% | Periodic sentiment surveys (this component is occasionally paused). |
| **Bitcoin dominance** | 10% | Rising BTC dominance signals fear (rotation out of alts into BTC); falling dominance signals speculative appetite (altcoin greed). |
| **Google Trends** | 10% | Search volume for terms like "Bitcoin price manipulation" → fear; "how to buy Bitcoin" spikes → greed. |

The composite is recalculated daily and published at approximately UTC midnight.

**Score interpretation:**

| Score range | Label | Historical significance |
|------------|-------|------------------------|
| 0–24 | Extreme Fear | Has coincided with major bottoms (March 2020: 8; Jan 2023: 6) |
| 25–49 | Fear | Below-average sentiment; often a value accumulation zone |
| 50–74 | Greed | Above-average; markets trending up; mild caution |
| 75–100 | Extreme Greed | Has coincided with major tops (Nov 2021: 84 at BTC $69k peak; Jan 2018: 95) |

## Concrete Examples

- **March 2020 (COVID crash):** Index hit **8** on March 17, the lowest recorded reading. BTC was ~$4,800. The index stayed in Extreme Fear for three weeks before the recovery began. Buyers at the extreme Fear reading saw BTC at $69,000 eighteen months later.
- **January 2023 (post-FTX):** Index printed **6** for three consecutive days with BTC at $16,000–17,000 range. This was the bottom of the FTX collapse hangover; buyers at or below F&G = 10 saw BTC reach $73,000 by early 2024 — a gain of over 300%.
- **November 2021 (top):** Index reached 84 with BTC at $69,000. The market entered a year-long bear market following this Extreme Greed reading, with BTC falling 76% to $15,500 by November 2022.
- **January 2018 (top):** Index near 95 as BTC hit ~$17,000 in mid-January. The subsequent correction was −66% over three months.

These examples illustrate the contrarian principle but are not a systematic backtest — cherry-picked extremes do not constitute statistical evidence. A proper test would require measuring conditional vs. unconditional forward returns across all readings (see [[contrarian-extremes#Null Hypothesis]]).

## Trading Relevance

The Crypto Fear & Greed Index is used across several AlgoBrain strategies:

- **[[contrarian-extremes]]:** The index (weighted at 15% of the composite score) is a direct entry trigger. A composite score below 20 — which requires the F&G Index to be very low — triggers tranched buy entries into BTC or ETH. Conversely, F&G above 90 contributes to sell signals.
- **[[multi-strategy-crypto-portfolio]]:** The meme-regime score (from CryptoDataAPI) is partially informed by sentiment data including the Fear & Greed index. Extremely low readings flag bear/capitulation regime; extremely high readings flag speculative-euphoria.
- **[[funding-rate-arbitrage]]:** Deep fear readings tend to coincide with negative funding rates (the crowd goes short), which creates the best funding harvest opportunities for delta-neutral long-spot/short-perp positions. The F&G index confirms when the funding environment is most favourable.
- **[[prediction-market-strategies]]:** Sentiment extremes can misprice prediction-market outcomes — a "No" bias fade (selling overpriced "Yes" shares) is more likely to be profitable when the broader market is in Extreme Fear and retail is emotionally reactive.

**Limitations:** The index is a lagging/coincident indicator, not a leading one. Markets can remain in Extreme Fear for weeks as a trend continues (2022 bear market had multiple sub-20 readings during an ongoing downtrend). It is most reliable as a *confirmation* tool for other signals (technical levels, funding rates, on-chain data) rather than as a standalone trigger.

## Related

- [[contrarian-extremes]] — the primary AlgoBrain strategy that uses this index as a core input
- [[behavioral-finance-overview]] — the theoretical framework behind sentiment extremes
- [[fear-and-greed-index]] — the CNN/equity version of the same concept
- [[market-regime]] — broader regime classification that the index informs
- [[sentiment-trading]] — category of strategies that use sentiment as input
- [[funding-rate]] — funding rates and the F&G index tend to co-move at extremes
- [[multi-strategy-crypto-portfolio]] — uses regime scores that incorporate sentiment signals
- [[vix]] — the equity-market volatility analogue

## Sources

- Alternative.me Crypto Fear & Greed Index (alternative.me/crypto/fear-and-greed-index/)
- General crypto knowledge; no specific wiki source ingested yet.
