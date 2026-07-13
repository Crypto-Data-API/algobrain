---
title: "Etherscan"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, crypto, on-chain, free]
entity_type: company
website: https://etherscan.io
related:
  - "[[dune-analytics]]"
  - "[[dex-screener]]"
  - "[[defilama]]"
  - "[[defai]]"
  - "[[ai-trading-agents]]"
---

# Etherscan

## Overview

Etherscan is the most widely used Ethereum blockchain explorer and a critical free tool for on-chain research. It provides transaction lookup, wallet tracking, smart contract verification, gas tracking, and token approval management. The same team operates BscScan, PolygonScan, Arbiscan, and BaseScan for other EVM chains. For any trader interacting with [[defi]] protocols or tracking on-chain activity, Etherscan is the foundational tool.

## Free Tier

- **Transaction lookup**: full transaction details, internal transactions, event logs
- **Wallet tracking**: balance, transaction history, token holdings, NFTs
- **Smart contracts**: source code verification, read/write contract interaction
- **Gas tracker**: current gas prices, historical gas charts
- **Token data**: token transfers, holders, supply, top holders
- **API**: 5 calls/second with free API key
- **Labels**: identified addresses (exchanges, bridges, known entities)

## Paid Tiers

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | 5 calls/sec, standard access |
| Standard | $199/mo | 10 calls/sec, advanced APIs |
| Pro | $399/mo | 20 calls/sec, priority support |

Most individual traders operate entirely on the free tier. Paid tiers are for heavy API use.

## Alpha Edge

- Track whale wallets to detect accumulation and distribution of specific tokens
- Monitor smart contract interactions to see what [[defi]] protocols large players are using
- Verify smart contract security before interacting (check verified source code, proxy patterns)
- Gas tracker for optimal transaction timing and cost management
- Token holder analysis: watch for concentration risk or whale dumping
- Internal transaction tracing reveals complex [[defi]] interactions and MEV activity

## API Details

- **Authentication**: free API key (register on Etherscan)
- **Base URL**: `https://api.etherscan.io/api`
- **Format**: JSON
- **Rate limit**: 5 calls/sec (free), higher on paid plans
```python
import requests
API_KEY = "YOUR_API_KEY"
base = "https://api.etherscan.io/api"
# Get ETH balance for an address
balance = requests.get(base, params={
    "module": "account", "action": "balance",
    "address": "0x...", "apikey": API_KEY
}).json()
# Get token transfers for an address
transfers = requests.get(base, params={
    "module": "account", "action": "tokentx",
    "address": "0x...", "apikey": API_KEY
}).json()
```

## Use Cases

- Whale wallet monitoring for [[smart-money]] tracking strategies
- Smart contract verification before DeFi interactions ([[risk-management]])
- Gas optimization for on-chain trading execution
- Token holder distribution analysis for investment research
- Building on-chain data pipelines with the API for [[algorithmic-trading]]
- Cross-referencing with [[dune-analytics]] for deeper on-chain investigation
