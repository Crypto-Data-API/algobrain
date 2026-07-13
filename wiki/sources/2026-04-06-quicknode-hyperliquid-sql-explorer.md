---
title: "QuickNode Hyperliquid SQL Explorer — Live Data Ingestion"
type: source
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, hyperliquid, data-provider, exchange]
source_type: data
source_url: "https://www.quicknode.com/docs/sql-explorer/hyperliquid-queries"
source_author: "QuickNode"
source_date: 2026-04-06
source_file: "r2://trader-wiki/data/2026-04-06-quicknode-hyperliquid-sql.md"
confidence: high
claims_count: 15
---

# QuickNode Hyperliquid SQL Explorer — Live Data Ingestion

## What This Source Is

[[quicknode|QuickNode]] SQL Explorer is a SQL query interface for on-chain [[hyperliquid|Hyperliquid]] data. Rather than a static report or article, this source represents **live data pulled directly from the Hyperliquid L1 blockchain** via QuickNode's structured SQL API. All claims are on-chain verified, giving them HIGH confidence by default.

The API allows arbitrary SQL queries against indexed Hyperliquid blockchain tables, covering everything from individual [[perpetual-futures|perpetual futures]] trades to aggregate market statistics, [[funding-rate|funding rates]], [[liquidation|liquidations]], and vault operations.

## API Details

- **Endpoint:** `POST https://api.quicknode.com/sql/rest/v1/query`
- **Cluster ID:** `hyperliquid-core-mainnet`
- **Auth:** QuickNode API key (header)
- **Response format:** JSON with row-based results

## Available Tables (29 total)

The SQL Explorer exposes 29 tables covering the full breadth of Hyperliquid on-chain activity:

| Category | Tables |
|---|---|
| **Trading** | trades, fills, orders, builder_fills |
| **Funding** | funding |
| **Blocks & Transactions** | blocks, transactions, builder_transactions |
| **Transfers & Ledger** | asset_transfers, ledger_updates, bridge |
| **Markets** | perpetual_markets, spot_markets, market_contexts |
| **Pricing** | oracle_prices |
| **Account State** | clearinghouse_states, vault_equities, sub_accounts |
| **Identity & Delegation** | agents, display_names, delegator_rewards |
| **Builder Ecosystem** | builder_transactions, builder_labels, builder_fills |
| **Analytics Rollups** | various rollup/aggregate tables |

## Key Claims Extracted

All claims below are **HIGH confidence** — they are derived from on-chain data, not estimates or projections.

### Market Structure

1. **[[hyperliquid|Hyperliquid]] has 229 [[perpetual-futures|perpetual]] markets** — this includes crypto assets and traditional finance instruments.
2. **Hyperliquid trades traditional assets** — the platform lists [[perpetual-futures|perps]] on SP500, Gold, Silver, Oil, TSLA, NVDA, and other non-crypto underlyings, blurring the line between [[decentralized-exchanges|DEX]] and traditional derivatives venue.
3. **Platform supports multiple clearinghouses** — perp, hyna, cash, xyz, km, flx, para, vntl — indicating a modular architecture with separate risk engines.

### Volume & Activity (24h as of 2026-04-06)

4. **[[bitcoin|BTC]] 24h volume: $1.87B** with 452,594 trades — BTC remains the dominant contract by a wide margin.
5. **[[ethereum|ETH]] 24h volume: $587.5M** — roughly 3x less than BTC, consistent with broader market cap ratios.
6. **Platform handles 3-10M daily fills** — significant throughput for an L1 [[decentralized-exchanges|decentralized exchange]].
7. **40K-2.5M daily active traders** — wide range suggests variance between quiet and volatile days.

### Open Interest & Positioning

8. **[[bitcoin|BTC]] [[open-interest|open interest]]: ~$2B notional** — substantial for a decentralized venue; comparable to mid-tier centralized exchanges.
9. **[[funding-rate|Funding rates]] mostly positive (longs pay shorts)** — indicates net-long positioning bias across most markets.
10. **FARTCOIN has elevated funding at 0.0074%** — a memecoin with outsized speculative interest relative to its market cap.

### Liquidations & Whale Activity

11. **[[liquidation|Liquidation]] events: 10,406 on Apr 5** — a moderately active liquidation day, useful for benchmarking volatility.
12. **Whale trades exceeding $2M in single transactions** — the platform attracts institutional-scale flow.
13. **Top single trader did $276M in 24h volume** — extreme concentration; a single participant accounting for significant platform share.

### Token & Ecosystem

14. **HYPE token trading at ~$36.90** — the native token of Hyperliquid, relevant for staking, fees, and governance.
15. **Active builder ecosystem with $114K daily builder fees** — builders (frontend operators / integrators) earn meaningful revenue, suggesting a healthy third-party ecosystem around the protocol.

## Confidence Assessment

| Aspect | Rating | Notes |
|---|---|---|
| **Data provenance** | HIGH | On-chain, verifiable via L1 state |
| **Completeness** | HIGH | 29 tables cover nearly all protocol activity |
| **Timeliness** | HIGH | Live queries, not cached snapshots |
| **Accuracy** | HIGH | SQL over indexed blockchain data; no estimation |
| **Bias risk** | LOW | Raw data, not editorialized |

The only caveat: volume/trade counts reflect on-chain activity only. Any off-chain or pre-settlement activity (if it exists) would not appear in these tables.

## Pages Created From This Source

- [[hyperliquid]] — entity page for the Hyperliquid protocol
- [[hyperliquid-market-snapshot-2026-04-06]] — point-in-time market snapshot with full data tables
- [[quicknode]] — data provider entity page

## Pages That Should Be Updated or Created

The following pages would benefit from data extracted in this ingestion:

- [[bitcoin]] — update with Hyperliquid-specific volume and OI data
- [[ethereum]] — update with Hyperliquid ETH perp volume
- [[solana]] — update if SOL perp data was captured
- [[funding-rate]] — add Hyperliquid funding rate examples and cross-platform comparison
- [[open-interest]] — add Hyperliquid OI as a DEX benchmark
- [[liquidation]] — add daily liquidation count data point
- [[perpetual-futures]] — reference Hyperliquid's 229-market breadth and traditional asset listings
- [[decentralized-exchanges]] — update with Hyperliquid volume/throughput as a leading DEX

## Raw Data Location

The raw query results and full SQL used for this ingestion are stored at:

```
raw/data/2026-04-06-quicknode-hyperliquid-sql.md
```

## See Also

- [[hyperliquid]]
- [[quicknode]]
- [[perpetual-futures]]
- [[decentralized-exchanges]]
- [[funding-rate]]
- [[open-interest]]
