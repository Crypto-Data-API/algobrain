---
title: "Dune Analytics"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, crypto, on-chain, free]
entity_type: company
website: https://dune.com
related:
  - "[[etherscan]]"
  - "[[defilama]]"
  - "[[coingecko]]"
  - "[[ai-agent-tokens]]"
  - "[[ai-trading-agents]]"
  - "[[ai-mev]]"
---

# Dune Analytics

## Overview

Dune Analytics is a SQL-based blockchain analytics platform -- often called the "GitHub of on-chain data." Users write custom SQL queries against indexed on-chain data from Ethereum, Polygon, Solana, Bitcoin, and dozens of other chains. A massive community of analysts has built thousands of public dashboards covering everything from [[defi]] protocol metrics to NFT trading to whale wallet tracking. If you need custom on-chain analysis that goes beyond what [[etherscan]] or [[defilama]] can provide, Dune is where you build it.

## Free Tier

- **Query execution**: limited execution credits (10/month)
- **Public dashboards**: browse and fork thousands of community dashboards
- **Data access**: full indexed blockchain data (Ethereum, L2s, Solana, etc.)
- **Visualization**: charts, tables, counters from query results
- **Sharing**: all free-tier queries and dashboards are public
- **Limitations**: slow query execution queue, no private dashboards, limited API access

## Paid Tiers

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | 10 executions/mo, public only |
| Plus | $349/mo | 2,500 credits, private queries, CSV export |
| Premium | $1,399/mo | 25,000 credits, priority execution, full API |

API access for programmatic query execution is a paid feature. Higher tiers get faster execution and larger result sets.

## Alpha Edge

- Build custom whale tracking dashboards to monitor [[smart-money]] movements
- Analyze protocol revenue and fee trends before they hit mainstream metrics
- Track token flows between exchanges and wallets for supply/demand signals
- Monitor DEX volume and liquidity shifts across [[defi]] protocols
- Identify accumulation/distribution patterns via on-chain transfer analysis
- Create custom metrics that no one else is tracking -- true information edge

## API Details

- **Query language**: DuneSQL (Trino-based SQL dialect)
- **Chains indexed**: Ethereum, Polygon, Optimism, Arbitrum, Solana, Bitcoin, BNB, and more
- **API**: execute queries and fetch results programmatically (paid plans)
- **Python**: `dune-client` -- `pip install dune-client`

```python
from dune_client.client import DuneClient
dune = DuneClient(api_key="YOUR_API_KEY")
result = dune.get_latest_result(query_id=1234567)
# Or execute a fresh query
result = dune.run_query(query_id=1234567)
```

## Use Cases

- Custom [[on-chain-analysis]] dashboards for any blockchain protocol
- Whale wallet monitoring and [[smart-money]] tracking
- Protocol research: revenue, users, transaction volume, retention
- DEX and [[defi]] analytics beyond what aggregators provide
- NFT market analysis and collection-level metrics
- Building proprietary trading signals from raw blockchain data
