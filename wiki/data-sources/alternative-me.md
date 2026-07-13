---
title: "Alternative.me — Crypto Fear & Greed Index"
type: source
created: 2026-04-22
updated: 2026-07-13
status: good
tags: [data-provider, sentiment, behavioral-finance, crypto]
source_type: data
source_url: "https://alternative.me/crypto/fear-and-greed-index/"
source_author: "Alternative.me"
aliases: ["Crypto Fear & Greed Index", "Alternative.me", "Fear and Greed Index"]
related: ["[[crypto-data-sources]]", "[[news-and-sentiment-sources]]", "[[behavioral-finance]]", "[[bitcoin]]", "[[mean-reversion]]", "[[contrarian-indicators]]", "[[cryptodataapi]]"]
---

Alternative.me provides the **Crypto Fear & Greed Index**, the most widely referenced sentiment gauge in [[crypto-markets|cryptocurrency markets]]. The index produces a daily score from 0 (Extreme Fear) to 100 (Extreme Greed) by aggregating multiple data sources into a single sentiment reading. It is free to access via both the website and a public API.

## Index Methodology

The Crypto Fear & Greed Index is a composite of six weighted data sources:

| Component | Weight | Data Source |
|-----------|--------|-------------|
| **Volatility** | 25% | Current [[bitcoin|BTC]] [[volatility]] vs. 30-day and 90-day averages; unusually high volatility signals fear |
| **Market Momentum / Volume** | 25% | Current volume and momentum vs. 30/90-day averages; high buying volume in a rising market signals greed |
| **Social Media** | 15% | Twitter/X post volume and engagement rates for crypto hashtags; rapid increases signal greed |
| **Surveys** | 15% | Weekly crypto polling (currently paused in some periods) |
| **BTC Dominance** | 10% | Rising BTC dominance suggests fear (flight to safety within crypto); falling dominance suggests greed (risk-on altcoin speculation) |
| **Google Trends** | 10% | Search volume for crypto-related queries; spikes in "bitcoin crash" signal fear; spikes in "buy bitcoin" signal greed |

### Index Ranges

| Score | Classification | Historical Interpretation |
|-------|---------------|--------------------------|
| 0–24 | **Extreme Fear** | Historically signals buying opportunities — market oversold, capitulation likely near |
| 25–49 | **Fear** | Cautious sentiment, potential accumulation zone |
| 50–55 | **Neutral** | Balanced sentiment |
| 56–74 | **Greed** | Bullish sentiment, momentum trades may work |
| 75–100 | **Extreme Greed** | Historically signals caution — euphoric conditions precede corrections |

## API Access

The Fear & Greed Index offers a free, public JSON API with no authentication required:

| Endpoint | Description |
|----------|-------------|
| `https://api.alternative.me/fng/` | Current index value |
| `https://api.alternative.me/fng/?limit=30` | Last 30 days of readings |
| `https://api.alternative.me/fng/?limit=0` | Full history since February 2018 |
| `https://api.alternative.me/fng/?date_format=us` | US date format |

Response format:
```json
{
  "data": [
    {
      "value": "25",
      "value_classification": "Extreme Fear",
      "timestamp": "1713744000",
      "time_until_update": "43200"
    }
  ]
}
```

## Trading Relevance

### As a Contrarian Indicator

The Fear & Greed Index is most valuable as a **contrarian** signal at extremes:

- **Extreme Fear (<20)**: Historically, buying [[bitcoin]] when the index drops below 20 has produced positive returns over 30/60/90-day horizons in the majority of instances. Extreme fear often coincides with [[capitulation]] selling, exchange liquidation cascades, and peak negative sentiment — conditions associated with [[mean-reversion]] opportunities.
- **Extreme Greed (>80)**: Sustained readings above 80 have frequently preceded 10-30% corrections. The index reached 90+ during the November 2021 peak, the March 2024 BTC all-time high run, and other local tops.

### Limitations

1. **Lagging at inflection points**: The index uses trailing averages, so it may remain in "fear" after the bottom has already been made
2. **BTC-centric**: Heavily weighted toward [[bitcoin]] metrics; may not reflect [[altcoins|altcoin]]-specific sentiment
3. **Not a timing tool**: Extreme readings can persist for weeks — the index signals zones, not precise entry/exit points
4. **Self-referential risk**: As the index becomes widely followed, its signals may become crowded and less effective
5. **No volume weighting by exchange**: Social media signals can be manipulated by bots

### Integration with Other Signals

The Fear & Greed Index works best when combined with:

- [[funding-rate|Funding rates]] on [[perpetual-futures]] (negative funding + extreme fear = stronger buy signal)
- [[bitcoin|BTC]] exchange reserves declining during fear (on-chain confirmation via [[cryptoquant|CryptoQuant]])
- [[rsi|RSI]] oversold readings on daily/weekly charts
- [[options]] market data: elevated put/call ratios on [[deribit]] during fear periods
- [[liquidation]] cascade data — large long liquidation events often coincide with peak fear

## Historical Accuracy

Selected extreme readings and subsequent 90-day [[bitcoin|BTC]] performance:

| Date | Index Reading | BTC Price | 90-Day Return |
|------|--------------|-----------|---------------|
| March 2020 (COVID crash) | 8 (Extreme Fear) | ~$5,000 | +140% |
| June 2022 (LUNA/3AC collapse) | 6 (Extreme Fear) | ~$20,000 | -5% (further decline before recovery) |
| November 2022 (FTX collapse) | 20 (Extreme Fear) | ~$16,000 | +45% |
| November 2021 (peak) | 84 (Extreme Greed) | ~$69,000 | -40% |

Note: Past performance does not guarantee future results. The index failed to predict the extended 2022 bear market bottom with precision.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — Fear & Greed index
- `GET /api/v1/sentiment/stablecoins` — stablecoin market cap + 14d/90d flows
- `GET /api/v1/sentiment/macro` — EUR/USD, gold, yields

**Historical data:**
- `GET /api/v1/market-intelligence/fear-greed-history` — Fear & Greed timeseries
- `GET /api/v1/sentiment/stablecoins/remote-history?days=365` — daily stablecoin history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/fear-greed"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]].

## Related

- [[crypto-data-sources]] — Comprehensive crypto data provider catalog
- [[news-and-sentiment-sources]] — Sentiment data providers
- [[behavioral-finance]] — Psychological biases driving fear/greed cycles
- [[bitcoin]] — Primary asset the index tracks
- [[mean-reversion]] — Strategy framework for trading extreme sentiment
- [[cryptoquant]] — On-chain analytics to confirm sentiment signals
- [[deribit]] — Options data for cross-referencing sentiment

## Sources

_Content based on Alternative.me public documentation, API specification, and historical index data. No raw sources ingested._
