---
title: "CryptoDataAPI — Hyperliquid"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, hyperliquid, perpetual-futures, order-book, funding-rates, open-interest]
aliases: ["CryptoDataAPI Hyperliquid", "CDA Hyperliquid", "Hyperliquid Perps Data API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[hyperliquid]]", "[[hyperliquid-order-book-microstructure]]", "[[level-4-order-book-data]]", "[[hyperliquid-api-and-sdk]]", "[[cryptodataapi-hyperliquid-traders]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-backtesting]]"]
---

The Hyperliquid category of [[cryptodataapi]] exposes [[hyperliquid]] perp-market data through one authenticated REST surface: exchange metadata, all mid prices, funding, open interest, OHLCV candles, and L2 order-book snapshots. It is the read-only intelligence layer for Hyperliquid; order placement and account management live in [[hyperliquid-api-and-sdk]].

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/hyperliquid/meta | Exchange metadata | — | — |
| GET | /api/v1/hyperliquid/prices | All mid prices | — | — |
| GET | /api/v1/hyperliquid/funding-rates | Current + historical funding | coin, limit 1-100 | — |
| GET | /api/v1/hyperliquid/open-interest | All-asset OI | — | — |
| GET | /api/v1/hyperliquid/candles | OHLCV candles | coin, interval, limit 1-1000 | — |
| GET | /api/v1/hyperliquid/l2-book | L2 order book snapshot | coin | — |
| GET | /api/v1/hyperliquid/summary | All-in-one perp data | coin | — |

Tier "—" = not marked with a plan gate in the API docs; standard plan rate limits apply.

## Live Data

`/hyperliquid/prices` (all mids in one call), `/hyperliquid/open-interest` (every listed asset), `/hyperliquid/l2-book` (order-book depth snapshot per coin), `/hyperliquid/meta` (contract specs), and `/hyperliquid/summary` (the single-call current-state bundle for one coin) all return live state.

## Historical Data

`/hyperliquid/funding-rates` returns current plus historical funding (up to `limit` 100 records per coin), and `/hyperliquid/candles` serves up to 1,000 OHLCV bars per request at a chosen interval. For point-in-time daily snapshots of the full ~230-perp universe, see `/api/v1/daily/hyperliquid` and the [[cryptodataapi-backtesting]] archive.

## Trading Applications

- Microstructure reads — L2 snapshots from `/hyperliquid/l2-book` support the spread/depth/imbalance analysis in [[hyperliquid-order-book-microstructure]]; for full order-by-order reconstruction see [[level-4-order-book-data]]
- Funding carry — per-coin funding history feeds [[funding-rate-arbitrage]] legs on Hyperliquid, cross-checked against Binance via [[cryptodataapi-derivatives]]
- OI screening — the all-asset `/hyperliquid/open-interest` call ranks where leverage is concentrating across the entire perp universe in one request
- Signal research — `/hyperliquid/candles` provides the OHLCV backbone for backtesting [[perpetual-futures]] strategies on Hyperliquid listings
- Execution context — pull `/hyperliquid/summary` before entries placed through [[hyperliquid-api-and-sdk]] to sanity-check funding, OI, and price in one call

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=200"
```

## Related

- [[cryptodataapi]] — hub page with auth, plans, and the full category map
- [[cryptodataapi-hyperliquid-traders]] — leaderboard, wallet signals, and copy-trading intelligence
- [[cryptodataapi-derivatives]] — Binance + cross-exchange funding and OI
- [[cryptodataapi-backtesting]] — historical archives for research
- [[hyperliquid]] — exchange profile
- [[hyperliquid-api-and-sdk]] — native trading API and SDK
- [[hyperliquid-order-book-microstructure]] — what to do with the L2 book

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
