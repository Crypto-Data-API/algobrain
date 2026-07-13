---
title: "QuickNode"
type: entity
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [data-provider, crypto, company]
aliases: ["QN", "QuikNode"]
entity_type: company
founded: 2017
headquarters: "Miami, Florida, USA"
website: "https://www.quicknode.com"
related: ["[[hyperliquid]]", "[[data-providers]]", "[[ethereum]]", "[[polygon]]", "[[arbitrum]]"]
---

# QuickNode

QuickNode is a Web3 infrastructure provider offering blockchain node endpoints, APIs, and data services. Founded in 2017 and headquartered in Miami, Florida, the company serves as a backbone for developers and analysts who need reliable, low-latency access to on-chain data across multiple blockchains. It is one of the "big three" commercial RPC providers alongside Alchemy and Infura/MetaMask Developer.

## Company Facts

- **Funding**: ~$106M raised across 6 rounds from 27 investors; the largest was a **$60M Series B (2023-01-24) led by 10T Holdings at an $800M valuation** (other backers across rounds include Tiger Global, SoftBank, and Seven Seven Six).
- **Coverage**: QuickNode advertises support for **80+ chains and 140+ networks** (RPC/REST/WebSocket endpoints, full-node and archive-node options), up from ~25 chains a few years earlier.
- **Ecosystem programs**: QuickNode is rolling out a **$65M accelerator program for Layer 2 projects** in collaboration with Google, Coinbase Ventures, and Dragonfly (The Block).
- **Competitors**: Alchemy, Infura (Consensys), Chainstack, Ankr, dRPC, Dwellir.

## Core Products

- **Node Endpoints** — Managed RPC nodes across 80+ chains / 140+ networks, removing the need to run self-hosted infrastructure.
- **QuickNode APIs** — Higher-level APIs for token balances, NFT data, transaction history, and event streams.
- **Streams** — Real-time, exactly-once on-chain data delivery pipelines (alternative to home-rolled websocket ingestion for trading systems).
- **Functions** — Serverless edge code that reacts to on-chain events and transforms blockchain data without managing infrastructure.
- **QuickAlerts / Webhooks** — Notifications on smart-contract events (useful for liquidation, whale-transfer, and listing alerts).
- **Marketplace** — Third-party add-ons extending endpoint functionality.
- **SQL Explorer** — A SQL-based query interface that exposes indexed blockchain data as relational tables, enabling analysts and traders to run arbitrary queries against on-chain state.

## SQL Explorer and Hyperliquid

The SQL Explorer product is particularly relevant for trading research. It provides a REST endpoint for executing SQL queries against indexed blockchain data:

```
POST https://api.quicknode.com/sql/rest/v1/query
```

QuickNode supports **Hyperliquid** via the cluster `hyperliquid-core-mainnet`, with 29+ queryable tables covering:

| Category | Example Tables |
|---|---|
| Trading activity | trades, fills, orders |
| Market structure | markets, funding, open interest |
| Liquidations & clearing | clearinghouse states, liquidations |
| Blockchain primitives | blocks, transactions |
| Vault & builder data | vault equities, builder data |
| Aggregated metrics | analytics rollups |

Because the data is sourced directly from on-chain records, it carries **high confidence** — it reflects actual settled state rather than exchange-reported figures.

## Trading Relevance

QuickNode matters for active traders and quantitative researchers for several reasons:

- **Real-time on-chain data** — Query the latest blocks, trades, and funding rates without waiting for third-party aggregators to update.
- **SQL accessibility** — The SQL interface lowers the barrier for complex analytics. Traders who know SQL can build custom dashboards, alerts, and reports without writing chain-specific parsing code.
- **Whale and flow tracking** — Cross-referencing fills, orders, and clearinghouse states enables monitoring of large position changes, liquidation cascades, and funding rate shifts.
- **Builder ecosystem analytics** — Builder data tables allow analysis of Hyperliquid's builder activity and fee structures.
- **Historical data for backtesting** — Archived on-chain data supports strategy backtesting against verified trade and funding history rather than potentially unreliable exchange exports.

## Usage in This Wiki

This wiki uses QuickNode's SQL Explorer API as a primary data source for live Hyperliquid market intelligence, including market snapshots, funding analysis, and volume metrics.

## Related

- [[hyperliquid]] — exchange whose on-chain data QuickNode indexes (cluster `hyperliquid-core-mainnet`)
- [[data-providers]] — broader data-provider catalog
- [[ethereum]], [[polygon]], [[arbitrum]] — major networks served by QuickNode endpoints

## Sources

- QuickNode SQL Explorer API documentation and live usage in this wiki, 2026-04-06.
- QuickNode blog — "QuickNode Raises $60M Series B": https://blog.quicknode.com/quicknode-raises-60-million-in-series-b-funding/
- Tracxn — QuickNode funding rounds and investors: https://tracxn.com/d/companies/quicknode/__NiURmT91P-gDEki96ypsAvVtQV6tAhNCskRLF8rduW0/funding-and-investors
- The Block — "QuickNode rolling out $65 million accelerator program for Layer 2 projects with Google, Coinbase Ventures and Dragonfly": https://www.theblock.co/post/343493/quicknode-rollout-65-million-usd-accelerator-program-layer-2-projects-google-coinbase-ventures-dragonfly
- QuickNode — official site (chain/network coverage): https://www.quicknode.com/
- Web verification via Perplexity/WebSearch, 2026-06-10.
