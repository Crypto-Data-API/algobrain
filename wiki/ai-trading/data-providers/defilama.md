---
title: "DefiLlama"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, crypto, defi, free]
entity_type: company
website: https://defillama.com
related:
  - "[[coingecko]]"
  - "[[dune-analytics]]"
  - "[[dex-screener]]"
  - "[[defai]]"
  - "[[ai-trading-agents]]"
  - "[[decentralized-ai]]"
---

# DefiLlama

## Overview

DefiLlama is the best free DeFi analytics dashboard and data platform. It tracks Total Value Locked (TVL) across all major protocols and chains, aggregates yield/APY data, monitors stablecoin flows, and measures bridge volumes. The entire platform is open source with no API key required, making it the gold standard for DeFi-specific data. If you are trading or investing in [[defi]] protocols, DefiLlama is an essential and completely free resource.

## Free Tier

Everything is free. No API key needed. No rate limit published (but be reasonable).

- **TVL data**: protocol-level and chain-level TVL, historical TVL charts
- **Yields**: APY/APR aggregator across lending, LPing, staking, vaults
- **Stablecoins**: circulating supply, chain distribution, peg monitoring
- **Bridges**: cross-chain volume, bridge TVL
- **DEX volume**: aggregated DEX trading volume by chain and protocol
- **Fees/Revenue**: protocol fee and revenue tracking
- **Liquidations**: DeFi lending liquidation data
- **Unlocks**: token unlock schedules

## Paid Tiers

DefiLlama is completely free and open source. There are no paid tiers. The project is funded by donations and its own token-related activities. This is rare in the data provider space and makes it invaluable for independent researchers and small trading operations.

## Alpha Edge

- Track capital flows between protocols and chains to front-run rotation trends
- Identify [[yield-farming]] opportunities by comparing APYs across protocols
- Monitor stablecoin depegging risk by watching supply shifts and chain distribution
- Bridge volume as a leading indicator for chain-level activity
- Protocol revenue trends for fundamental valuation of DeFi tokens
- Liquidation data for predicting cascading sells in DeFi lending markets
- Compare TVL vs. token market cap to find undervalued/overvalued protocols

## API Details

- **Authentication**: none required
- **Base URL**: `https://api.llama.fi/`
- **Format**: JSON
- **Documentation**: https://defillama.com/docs/api
- **Open source**: full codebase on GitHub (DefiLlama)

```python
import requests
# Get TVL for all protocols
protocols = requests.get("https://api.llama.fi/protocols").json()
# Get historical TVL for a specific protocol
aave_tvl = requests.get("https://api.llama.fi/protocol/aave").json()
# Get yield pools
yields = requests.get("https://yields.llama.fi/pools").json()
```

## Use Cases

- DeFi protocol fundamental analysis (TVL, revenue, fees)
- [[yield-farming]] strategy optimization across protocols and chains
- Stablecoin risk monitoring for treasury management
- Chain rotation strategies based on TVL and volume trends
- Building DeFi dashboards combining DefiLlama with [[coingecko]] price data
- Research input for [[defi]] governance and investment decisions
