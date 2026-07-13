---
title: "DEX Screener"
type: entity
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [data-provider, crypto, defi, free]
entity_type: company
website: https://dexscreener.com
related:
  - "[[cryptodataapi]]"
  - "[[defilama]]"
  - "[[etherscan]]"
  - "[[coingecko]]"
  - "[[ai-agent-tokens]]"
  - "[[defai]]"
---

# DEX Screener

## Overview

DEX Screener is a free real-time analytics platform for decentralized exchanges. It tracks token prices, liquidity, and trading activity across all major DEXs and chains -- Ethereum, Solana, BSC, Arbitrum, Base, and dozens more. Its core strength is speed: new trading pairs appear on DEX Screener within minutes of their creation, making it the go-to tool for on-chain traders looking to find new tokens early. The clean interface, fast search, and multi-chain coverage have made it essential for anyone doing [[defi]] trading.

## Free Tier

Everything is free. No API key required for the web interface.

- **Real-time prices**: live token prices from on-chain DEX trades
- **Multi-chain**: Ethereum, Solana, BSC, Arbitrum, Base, Polygon, Avalanche, and 70+ chains
- **New pairs**: alerts for newly created trading pairs
- **Token search**: search any token by name, symbol, or contract address
- **Charts**: candlestick charts with volume, powered by on-chain trade data
- **Liquidity data**: pool liquidity, liquidity changes, holder distribution
- **Pair analytics**: buy/sell ratio, unique traders, transaction counts
- **API**: free API with reasonable rate limits

## Paid Tiers

DEX Screener is free for all core features. They offer **paid token promotion** for projects wanting visibility (boosted listings, banner ads), but the data and analytics tools are free for traders. No paywall on any trading-relevant feature.

## Alpha Edge

- Find new tokens within minutes of liquidity being added -- before CEX listings
- Track liquidity additions and removals as early signals of rug pulls or project growth
- Identify momentum tokens via volume surges across chains
- Monitor smart money by watching which new pairs attract large initial trades
- Cross-chain token discovery -- find tokens launching on newer L2s before they get attention
- Pair-level analytics reveal buy/sell pressure and unique trader counts

## API Details

- **Authentication**: none required for public endpoints
- **Base URL**: `https://api.dexscreener.com/latest/dex/`
- **Format**: JSON
- **Key endpoints**: `/search`, `/tokens/{address}`, `/pairs/{chainId}/{pairAddress}`
- **Rate limits**: reasonable but undocumented; avoid aggressive polling

```python
import requests
# Search for a token
results = requests.get("https://api.dexscreener.com/latest/dex/search?q=PEPE").json()
# Get pair data by chain and address
pair = requests.get(
    "https://api.dexscreener.com/latest/dex/pairs/ethereum/0x...pairAddress"
).json()
# Get all pairs for a token address
token = requests.get(
    "https://api.dexscreener.com/latest/dex/tokens/0x...tokenAddress"
).json()
```

## Use Cases

- Early token discovery for [[on-chain-trading]] and memecoin strategies
- Rug pull detection by monitoring liquidity removal events
- Cross-chain [[arbitrage]] identification when tokens trade on multiple DEXs
- Volume-based momentum screening across all DEX-traded tokens
- New pair monitoring for automated [[sniping]] strategies
- Combining with [[etherscan]] contract verification for token due diligence

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].
