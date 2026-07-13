---
title: "Polymarket API"
type: source
created: 2026-05-03
updated: 2026-06-12
status: good
tags: [data-provider, prediction-markets, crypto, api]
aliases: ["Polymarket API", "CLOB API", "Polymarket CLOB"]
source_type: data
source_url: "https://docs.polymarket.com"
source_author: "Polymarket"
confidence: high
related: ["[[polymarket]]", "[[prediction-market-strategies]]", "[[ai-prediction-markets]]", "[[crypto-data-sources]]"]
---

The [[polymarket]] API surface is the programmatic gateway to the largest crypto-native prediction market, settling on [[polygon]]. It exposes a Central Limit Order Book (CLOB) for placing and cancelling orders via EIP-712 signed messages, plus read-only APIs for market metadata, historical trades, and live order-book streams. The full documentation lives at [docs.polymarket.com](https://docs.polymarket.com).

## API Surface

| API | Purpose | Type |
|-----|---------|------|
| **CLOB API** | Place, cancel, and query orders. EIP-712 signed messages. Zero trading fees. | REST + signed |
| **Gamma API** | Market metadata: categories, tags, slugs, end-dates, resolution sources. Used for discovery and filtering. | REST (read) |
| **Data API** | Historical trades, prices, volume; OHLC candles for charting and backtesting. | REST (read) |
| **WebSocket** | Real-time order-book diffs and trade ticks. Subscribe by market or asset id. | WS (read) |
| **Subgraph** | Polymarket events indexed via [[the-graph]] for SQL-like (GraphQL) queries over historical state. | GraphQL |

### CLOB API
The [[clob-api|CLOB]] is the active trading endpoint. Orders are off-chain limit orders signed with EIP-712 typed structured data; matched orders are then settled on-chain on [[polygon]]. There is no taker or maker fee at the protocol level. Order cancellations are also signed messages and are free.

### Gamma API
The Gamma API serves the metadata backbone of Polymarket's UI: market questions, categories, tags, slug routing, end dates, and oracle/resolution metadata. Bots use it for market discovery, filtering by tag (e.g., "elections", "crypto", "sports"), and resolving slugs to the asset/condition ids needed by the CLOB.

### Data API
Historical OHLC, trade prints, and volume series. This is the endpoint to hit when backtesting [[prediction-market-strategies]] or building charts. Pagination is required for long lookbacks.

### WebSocket
Real-time order-book updates and trade ticks. Essential for [[market-making]] bots and any strategy reacting to micro-structure events (e.g., large order arrivals, book imbalance shifts).

### Subgraph
A [[the-graph]] subgraph indexes Polymarket on-chain events (orders filled, positions, redemptions). Useful when you need historical state queries that are awkward in the REST APIs, or when the official API is rate-limited.

## Authentication

- **Public reads** (Gamma, Data, WebSocket public channels) require no authentication
- **CLOB orders** are signed with the trader's wallet via **EIP-712** typed structured data; the wallet itself is the identity
- **API keys** can be derived for the CLOB to authenticate higher-rate-limit endpoints and authenticated WebSocket channels (e.g., your own order updates). Keys are tied to the wallet that created them
- No OAuth or username/password flow — wallet-based identity end to end

## Rate Limits

Polymarket enforces tiered rate limits on the CLOB and Data APIs that vary by endpoint and authentication state. Public endpoints are more aggressively throttled than authenticated ones. Refer to the [official docs](https://docs.polymarket.com) for current numerical limits — they change as infrastructure evolves and any number quoted here would go stale quickly.

## Official SDKs

- **Python:** [`py-clob-client`](https://github.com/Polymarket/py-clob-client) — order signing, REST helpers, WebSocket. The de-facto choice for Python bots
- **TypeScript / JavaScript:** [`@polymarket/clob-client`](https://github.com/Polymarket/clob-client) — same surface for Node and browser
- Both SDKs handle EIP-712 signing, nonce management, and API key derivation

## Trading Use Cases

- **Algorithmic [[market-making]]** — quote both sides of binary outcome pairs, capture the spread, hedge inventory by trimming on the WebSocket book signal
- **Cross-market [[arbitrage]]** — between [[polymarket]] and other prediction venues (e.g., [[kalshi]]), or between correlated questions on Polymarket itself (e.g., conditional vs unconditional outcomes)
- **Backtesting** — pull historical OHLC and trade prints from the Data API to evaluate [[prediction-market-strategies]] before deploying capital
- **Real-time signal generation** — react to order-book imbalance, large prints, or sudden bid/ask shifts using the WebSocket feed
- **Dashboards and analytics** — build internal tooling for portfolio tracking, P&L, exposure-by-category, or [[ai-prediction-markets|LLM-driven]] research overlays
- **Closing-price arbitrage** — detect when an open market diverges from a more-informed reference (e.g., a sportsbook line or another prediction market)

## On-Chain Alternative

Because all Polymarket orders settle on [[polygon]], the same trade and position data is reachable trust-minimisedly through:

- **Polygon RPC** — query the Polymarket conditional-token contracts directly (positions, redemptions, transfers)
- **Subgraph** — pre-indexed events queryable in GraphQL (faster than raw RPC)
- **Block explorers** (Polygonscan) — for ad-hoc lookups

This matters when (a) the official API is rate-limited, (b) you need data the REST API does not expose, or (c) you want a verifiable, tamper-evident audit trail.

## Comparison to Alternatives

| Use case | Best tool |
|----------|-----------|
| Live trading / order placement | **Polymarket CLOB API** (the only path) |
| Real-time market data | **Polymarket WebSocket** |
| Bulk historical analytics | **[[dune-analytics|Dune]]** or **Subgraph** (SQL/GraphQL beats paginated REST for big lookbacks) |
| Trust-minimised position auditing | **Polygon RPC** directly |
| Cross-protocol DeFi context | **[[dune-analytics|Dune]]** (joins Polymarket data with broader on-chain activity) |

## Limitations

- **Geo-restrictions (changed in 2026):** US-based users were historically blocked from trading on the legacy offshore CLOB. This changed in 2026: following Polymarket's acquisition of the CFTC-licensed exchange **QCX/QCEX** and a CFTC **Amended Order of Designation**, a regulated **Polymarket US** venue now allows intermediated US market access (onboarding through brokerages/customers). US traders should distinguish between the legacy offshore CLOB API and the regulated US platform — the available markets, contract set, and onboarding flow differ, and some state-level restrictions may still apply. Verify current jurisdictional rules before routing orders
- **Async support:** Historically `py-clob-client` lacked native async; bot builders often wrap calls in thread pools or use the TypeScript SDK for async-heavy systems
- **Pagination on history:** Long historical pulls from the Data API can be slow under default page sizes; the Subgraph is usually faster for backfills
- **Liquidity bias:** API can quote any market, but for many low-volume questions the order-book is thin, making nominal "API access" different from "executable strategy"
- **Resolution risk** is API-invisible: data feeds don't surface oracle disputes or ambiguity in the resolution source — that risk lives in the underlying market design

## Notable Bots and Tools

- **OpenClaw / Polyclaw** ([[chainstack]]) — open-source AI-driven trading framework built on the Polymarket CLOB; combines LLM research with automated order placement
- Polymarket's docs reference **170+ third-party tools** built on the API surface (analytics dashboards, alert bots, copy-trading systems, LLM agents)
- A growing ecosystem of [[ai-prediction-markets|LLM-prediction]] bots use the API as their execution layer

## Pricing

- **API access:** free
- **Trading fees:** zero at the protocol level (no maker/taker fee)
- Costs are limited to Polygon gas for on-chain settlement and the implicit cost of crossing the spread

## Related

- [[polymarket]] — the venue itself
- [[polygon]] — settlement chain
- [[prediction-market-strategies]] — strategy catalogue executed via this API
- [[ai-prediction-markets]] — LLM-driven prediction-market trading
- [[the-graph]] — indexer behind the Subgraph
- [[dune-analytics]] — alternative for historical SQL-style analytics
- [[crypto-data-sources]] — broader catalogue
- [[chainstack]] — built OpenClaw / Polyclaw on this API

## Sources

- Polymarket official documentation: <https://docs.polymarket.com>
- CFTC Amended Order of Designation enabling intermediated US market access (PRNewswire, 2026): <https://www.prnewswire.com/news-releases/polymarket-receives-cftc-approval-of-amended-order-of-designation-enabling-intermediated-us-market-access-302625833.html>
- `py-clob-client` repository: <https://github.com/Polymarket/py-clob-client>
- `@polymarket/clob-client` repository: <https://github.com/Polymarket/clob-client>
