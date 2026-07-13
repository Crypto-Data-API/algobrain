---
title: "Hyperliquid API and SDK"
type: source
created: 2026-06-20
updated: 2026-07-13
status: draft
tags: [data-provider, crypto, hyperliquid, market-microstructure, algorithmic, api-trading]
aliases: ["Hyperliquid API", "Hyperliquid WebSocket API", "Hyperliquid Python SDK", "hyperliquid-python-sdk"]
source_type: data
source_url: "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket"
source_author: "Hyperliquid (official docs) + hyperliquid-dex (GitHub)"
source_date: 2026-04-22
source_file: "raw/articles/2026-04-22-gap-finder-hyperliquid-order-books.md"
confidence: high
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hyperevm]]", "[[hip-3-builder-deployed-perps]]", "[[hyperliquid-order-book-microstructure]]", "[[level-4-order-book-data]]", "[[exchange-api-reference]]", "[[ccxt]]", "[[hypurrscan]]", "[[clob]]", "[[market-microstructure]]", "[[cryptodataapi]]"]
---

**Hyperliquid API and SDK** refers to the native programmatic interfaces for the [[hyperliquid|Hyperliquid]] on-chain [[clob|central limit order book]] — a REST "info"/"exchange" HTTP API, a WebSocket feed for real-time data and order submission, and the official `hyperliquid-python-sdk` that wraps signing, authentication, and serialization. Because every order, cancel, trade, and liquidation on Hyperliquid executes fully on-chain through [[hypercore|HyperCore]], these interfaces are the canonical way to read the live order book state and to trade against it programmatically. This page is the on-chain-CLOB-specific companion to the generic [[exchange-api-reference|exchange API reference]] and to the multi-venue abstraction layer [[ccxt|CCXT]].

> This page documents only what the grounding research and official docs state. It deliberately avoids inventing specific endpoint paths, message field names, or rate limits beyond what is already documented on the [[exchange-api-reference]] page and in the Hyperliquid GitBook. Always verify endpoints, schemas, and limits against the primary docs in **Sources** before deploying capital.

## Why a venue-specific API page

The general [[exchange-api-reference]] page already lists Hyperliquid's `https://api.hyperliquid.xyz/info` POST endpoint, the `wss://api.hyperliquid.xyz/ws` WebSocket base URL, and the core subscription types (`l2Book`, `allMids`, `trades`, `orderUpdates`, `candle`). This page goes one level deeper into the *workflow* of consuming and trading against an on-chain CLOB: how to stay in sync with the book, how the Python SDK handles auth/signing, and how [[hip-3-builder-deployed-perps|HIP-3]] markets reuse the same schema. It is intentionally cross-linked from [[exchange-api-reference]] and [[ccxt]] as the concrete worked example of an on-chain-CLOB connector.

## Interface surface

| Interface | Purpose | Best for |
|---|---|---|
| **REST (info)** | Snapshot reads: L2 book, mids, funding/OI/mark context, user fills, clearinghouse state | Initial state, polling-tolerant reads, backfill, reconciliation |
| **REST (exchange)** | Signed actions: place/cancel orders, manage positions | Order submission where WebSocket order entry isn't used |
| **WebSocket** | Real-time data streaming **and** an alternative to HTTP for sending orders | Maintaining a live book, low-latency execution |
| **Python SDK** | Wraps signing, auth, request serialization over REST + WS | Quants/algo traders who want venue-specific features without hand-rolling auth |

Hyperliquid exposes **separate URLs for mainnet and testnet** (Source: hyperliquid-docs WebSocket API). The exact paths are documented on [[exchange-api-reference]] and the GitBook; do not assume undocumented variants.

## WebSocket feeds

The WebSocket endpoint serves real-time data streams and can also be used as an alternative to HTTP for sending orders (Source: hyperliquid-docs WebSocket API). The feeds relevant to order-book work, as documented on [[exchange-api-reference#hyperliquid|the exchange API reference]]:

| Subscription | Data | Notes |
|---|---|---|
| `l2Book` | L2 order book (aggregated price levels) | The primary depth feed for maintaining a local book |
| `trades` | Individual fills for a coin | Execution monitoring, trade-print analysis |
| `allMids` | Mid prices across all assets | Lightweight cross-asset price scan |
| `orderUpdates` | Order-status changes for your address | Authenticated; reconciliation of your own orders |
| `candle` | OHLCV candle updates per interval | Trend/feature inputs |

A subscription is opened with a `subscribe` method message carrying a `subscription` object naming the `type` and (where relevant) the `coin` or `user`, e.g. `{"method": "subscribe", "subscription": {"type": "l2Book", "coin": "BTC"}}` (Source: [[exchange-api-reference]]).

### Snapshots vs diffs

Order-book WebSocket feeds in general arrive as either full snapshots or incremental diffs (and many venues mix the two — a snapshot followed by deltas). The grounding research describes the canonical pattern: **start from a full order book snapshot, then apply incremental updates** to maintain the live book (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). The shared [[exchange-api-reference#data-quality-caveats|data-quality caveats]] apply directly: an L2 book maintained from a diff stream drifts out of sync if a sequence gap is missed.

## REST endpoints

The REST "info" endpoint is a single POST URL whose behavior is selected by a `type` field in the JSON body. The request types documented on [[exchange-api-reference#hyperliquid|the exchange API reference]] include:

| Request type | Returns |
|---|---|
| `allMids` | Mid prices for all assets |
| `l2Book` (with `coin`) | Full L2 order book for one coin |
| `metaAndAssetCtxs` | Funding rates, open interest, mark prices for all assets |
| `fundingHistory` (coin + time range) | Historical funding rates |
| `userFills` (user address) | Trade history for an address |
| `clearinghouseState` (user address) | Positions, margin, PnL for an address |

Signed actions (placing/cancelling orders, managing positions) go through the "exchange" action path and require a request signature; the SDK handles this. Rate limits are described on [[exchange-api-reference]] as **generous but not officially documented** (approximately ~1,200 requests/minute observed) — treat that as an observation, not a guarantee, and budget headroom.

## Python SDK (`hyperliquid-python-sdk`)

The official Python SDK is hosted at **github.com/hyperliquid-dex/hyperliquid-python-sdk** and is designed to facilitate trading with Hyperliquid's API, handling key management, request signing, and serialization (Source: hyperliquid-docs / GitHub). It is the natural venue-specific complement to [[ccxt|CCXT]] for traders who want finer-grained access to Hyperliquid features (advanced order types, [[hip-3-builder-deployed-perps|HIP-3]] markets) than a unified multi-venue abstraction exposes.

### Authentication and signing

| Step | What the docs state |
|---|---|
| **Generate API key** | Generate and authorize a new API private key via the **Hyperliquid UI** (Source: hyperliquid-docs / GitHub) |
| **Configure secret** | Set the wallet's private key as the secret key in the SDK's configuration (Source: hyperliquid-docs / GitHub) |
| **Signing** | The SDK serializes and signs requests so the caller does not hand-roll the signature scheme |

The separation of an **authorized API key** (generated in the UI) from the **wallet private key** lets a bot sign actions without exposing the master wallet credentials more than necessary — a standard agent-execution hygiene point echoed in [[exchange-api-reference#how-trading-and-ai-systems-consume-these-apis|the exchange-API consumption model]] (the agent proposes, a risk gate disposes).

### Typical usage surface

The SDK exposes the same logical operations as the raw API: subscribe to order-book streams, place limit/market orders, manage positions with trigger (stop / take-profit) orders, and query funding, margin, and account state (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). It pairs naturally with pandas/NumPy for real-time analytics or backtesting against captured Hyperliquid data — see [[level-4-order-book-data]] for the research-grade capture path.

> The grounding research does not enumerate exact SDK method names or signatures. Read the repository README and examples directory for the current API surface, which changes between releases.

## Staying in sync with the book — best practices

These are the documented/canonical patterns for maintaining a correct local view of an on-chain CLOB (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]; shared caveats in [[exchange-api-reference]]):

| Practice | Why |
|---|---|
| **Snapshot then apply diffs** | Seed the local book from a full snapshot, then apply incremental updates so you never start from a partial state |
| **Detect and handle gaps** | If a sequence/update gap is detected, the book is suspect — do not act on it |
| **Resync on suspicion** | On a detected gap, re-fetch a fresh snapshot rather than guessing the missing deltas |
| **Resubscribe on disconnect** | On WebSocket drop, reconnect and re-seed from snapshot before resuming execution |
| **Validate against REST** | Periodically reconcile the WS-maintained book against a REST `l2Book` snapshot to catch silent drift |

Because Hyperliquid settles on-chain, the latency profile differs from a CEX matching engine: the [[exchange-api-reference#latency-considerations|latency table]] lists Hyperliquid REST at ~100–300 ms and WebSocket at ~50–200 ms, with finality gated by on-chain consensus ([[hypercore|HyperCore]] / HyperBFT) rather than a private engine. This matters for any latency-sensitive strategy and for how aggressively you can cancel/replace.

## HIP-3 markets share the same API schema

[[hip-3-builder-deployed-perps|HIP-3 builder-deployed perpetuals]] are permissionless perp markets that inherit [[hypercore|HyperCore's]] matching engine while letting an independent deployer set the oracle, contract specs, leverage limits, settlement, and fee shares. Critically for tooling, **HIP-3 markets share the same API schema as core assets**, so bots and strategies built against the core API can be adapted to HIP-3 markets with minimal code changes (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). This makes HIP-3 markets attractive for quant experimentation — the same `l2Book`/`trades` subscriptions and the same order-placement path apply, with the heterogeneity living in the deployer-set parameters rather than the connector code.

## Relationship to other tooling

| Tool | Role relative to the native API |
|---|---|
| [[ccxt]] | Unified multi-venue wrapper; supports Hyperliquid but smooths the common 80% of calls. Use the native SDK for venue-specific features (HIP-3, advanced order types) |
| [[hypurrscan]] | Read-only on-chain explorer/analytics; not an execution path — use for monitoring, not the trade decision |
| [[exchange-api-reference]] | Cross-venue endpoint/schema reference; this page is its on-chain-CLOB worked example |
| [[level-4-order-book-data]] | Research-grade L4 capture (via a non-validating node) — a different, deeper data path than the public API feeds |

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order book snapshot
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest
- `GET /api/v1/hyperliquid/summary?coin=BTC` — all-in-one perp data

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BTC&limit=100` — current + historical funding
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

- [[hyperliquid]] — the venue these interfaces serve
- [[hypercore]] — the on-chain engine that produces the book state
- [[hyperevm]] — the smart-contract layer that composes with HyperCore liquidity
- [[hip-3-builder-deployed-perps]] — markets sharing this API schema
- [[hyperliquid-order-book-microstructure]] — what the feeds let you measure
- [[level-4-order-book-data]] — research-grade capture path
- [[exchange-api-reference]] — generic cross-venue endpoint reference
- [[ccxt]] — multi-venue abstraction over this and other APIs
- [[hypurrscan]] — read-only explorer/analytics layer
- [[clob]] · [[market-microstructure]] — conceptual grounding

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])
- Hyperliquid Docs — WebSocket API: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket
- Hyperliquid Docs (overview): https://hyperliquid.gitbook.io/hyperliquid-docs
- Hyperliquid Python SDK: https://github.com/hyperliquid-dex/hyperliquid-python-sdk
- [[exchange-api-reference]] — documented Hyperliquid REST/WS endpoints and rate-limit observations
