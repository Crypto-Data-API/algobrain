---
title: "Fear & Greed Index"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, sentiment, free]
entity_type: company
website: https://money.cnn.com/data/fear-and-greed
related:
  - "[[coinglass]]"
  - "[[tradingview-platform]]"
---

# Fear & Greed Index

## Overview

The Fear & Greed Index refers to two widely followed free sentiment gauges: the **CNN Fear & Greed Index** for traditional markets and the **Alternative.me Crypto Fear & Greed Index** for crypto. Both produce a single number from 0 (extreme fear) to 100 (extreme greed), providing a quick read on market sentiment. Despite their simplicity, these indices are popular among both retail and institutional traders as contrarian timing tools. When everyone is fearful, contrarians buy; when everyone is greedy, contrarians sell.

## Free Tier

**CNN Fear & Greed Index (Stocks)**:
- Components: market momentum (S&P vs 125-day MA), stock price strength, stock price breadth, put/call ratio, market volatility ([[vix]]), junk bond demand, safe haven demand
- Updated daily, free on CNN website
- No official API

**Alternative.me Crypto Fear & Greed Index**:
- Components: volatility (25%), market momentum/volume (25%), social media (15%), surveys (15%), Bitcoin dominance (10%), Google Trends (10%)
- Updated daily, free API available
- Historical data accessible via API

## Paid Tiers

Both indices are completely free. No paid tiers exist. CNN publishes the stock version as editorial content. Alternative.me provides the crypto version as a free community tool with open API access.

## Alpha Edge

- **Contrarian timing**: buy when index reads extreme fear (<20), reduce exposure at extreme greed (>80)
- Historically, extreme fear readings in BTC have preceded significant rallies
- Combine with [[coinglass]] liquidation data for high-conviction fear-based entries
- Use as a regime filter: only take long setups when index is below 40, only short above 70
- Track divergences: price making new highs while greed is declining = warning
- Simple overlay on any strategy to filter entries by sentiment regime

## API Details

**CNN Fear & Greed** -- no official API. Common workarounds:
- Web scrape the CNN page
- Third-party APIs that track it (various open source projects)

**Alternative.me Crypto Fear & Greed** -- free, documented API:
- **Base URL**: `https://api.alternative.me/fng/`
- **Authentication**: none required
- **Format**: JSON

```python
import requests

# Crypto Fear & Greed Index
response = requests.get("https://api.alternative.me/fng/?limit=30").json()
for entry in response["data"]:
    print(f"Date: {entry['timestamp']}, Value: {entry['value']}, "
          f"Classification: {entry['value_classification']}")

# Returns: value (0-100), value_classification (Extreme Fear, Fear, Neutral, Greed, Extreme Greed)
```

## Use Cases

- Contrarian entry timing for [[swing-trading]] and [[position-trading]]
- Sentiment regime filter layered on top of [[technical-analysis]] strategies
- [[risk-management]] overlay: reduce position sizes during extreme greed
- Daily market briefing -- one-glance sentiment read alongside finviz heatmaps
- Backtesting sentiment-based strategies using historical fear/greed data
- Combining crypto fear/greed with [[coinglass]] funding rates for multi-signal confirmation
- Educational tool for understanding crowd psychology in markets
