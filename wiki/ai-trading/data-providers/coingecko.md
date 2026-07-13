---
title: "CoinGecko"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, crypto, free]
entity_type: company
website: https://www.coingecko.com
related:
  - "[[coinglass]]"
  - "[[defilama]]"
  - "[[dex-screener]]"
  - "[[ai-agent-tokens]]"
  - "[[defai]]"
  - "[[ai-trading-agents]]"
---

# CoinGecko

## Overview

CoinGecko is the most comprehensive free crypto data aggregator, tracking 10,000+ coins and tokens across hundreds of exchanges. It provides prices, market cap, trading volume, exchange data, [[defi]] TVL, and NFT floor prices -- all accessible via a generous free API. For anyone building crypto trading tools or research pipelines, CoinGecko is typically the first data source integrated. Its breadth of coverage and no-API-key public endpoints make it the default choice for crypto market data.

## Free Tier

- **Coverage**: 10,000+ coins/tokens, 600+ exchanges
- **Price data**: current prices, historical daily prices, OHLC (1/7/14/30/90/180/365 days)
- **Market data**: market cap, 24h volume, circulating/total supply, ATH/ATL
- **Exchange data**: exchange volumes, trading pairs, trust scores
- **DeFi**: TVL by protocol, DeFi market cap
- **NFTs**: floor prices, volume, market cap by collection
- **Limits**: public endpoints require no API key; rate-limited to ~10-30 calls/min
- **Demo API key**: 30 calls/min, 10,000 calls/mo

## Paid Tiers

| Plan | Price | Rate Limit |
|------|-------|------------|
| Demo | Free | 30 calls/min |
| Analyst | $129/mo | 500 calls/min |
| Lite | $499/mo | 500 calls/min |
| Pro | $999/mo | 1,000 calls/min |

Paid tiers add on-chain DEX data, historical snapshots, and dedicated support.

## Alpha Edge

- Track [[market-dominance]] shifts between BTC, ETH, and altcoins for rotation strategies
- Monitor altcoin momentum via volume surges and market cap rankings
- Identify exchange flow anomalies (volume spikes on specific exchanges)
- DeFi TVL tracking for protocol-level fundamental-analysis
- NFT market sentiment via floor price trends and volume changes
- Cross-reference CoinGecko data with [[coinglass]] derivatives data for confirmation

## API Details

- **Authentication**: optional API key (free demo key available)
- **Base URL**: `https://api.coingecko.com/api/v3/`
- **Format**: JSON
- **Python library**: `pycoingecko` -- `pip install pycoingecko`

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
btc = cg.get_price(ids="bitcoin", vs_currencies="usd", include_24hr_change="true")
market = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc", per_page=100)
```

## Use Cases

- Building crypto portfolio trackers and dashboards
- Altcoin screening and momentum detection for [[swing-trading]]
- Exchange volume analysis for [[arbitrage]] opportunity identification
- DeFi protocol research and TVL-based valuation models
- Historical price data for crypto [[backtesting]]
- Market cap weighted index construction for crypto baskets
