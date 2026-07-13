---
title: "Exchange API Reference for Arbitrage"
type: reference
created: 2026-04-20
updated: 2026-06-20
status: excellent
tags: [data, crypto, arbitrage, market-microstructure, algorithmic, execution]
aliases: ["Exchange APIs", "Crypto API Reference", "Arbitrage API Endpoints"]
related: ["[[crypto-data-sources]]", "[[data-sources-overview]]", "[[cross-exchange-arbitrage]]", "[[funding-rate-arbitrage]]", "[[triangular-arbitrage]]", "[[binance]]", "[[coinbase]]", "[[hyperliquid]]", "[[fees]]", "[[latency-arbitrage]]"]
---

# Exchange API Reference for Arbitrage

A normalized reference for the API endpoints, WebSocket feeds, rate limits, and data schemas an arbitrage agent needs across major crypto venues. Individual exchange pages document each venue broadly; this page focuses on the **specific endpoints required for real-time arbitrage monitoring and execution**.

The core insight: every exchange exposes the same *types* of data (prices, order books, funding rates, trades) but with different URLs, authentication requirements, message formats, and rate limits. An arbitrage system must normalize across all of them.

This page is the execution-plumbing companion to the strategy maps. The strategies themselves live in [[arbitrage-opportunity-map]], [[asterdex-perp-trading-map]], and [[hyperliquid-perp-trading-map]]; for on-chain (DEX/bridge/flash-loan) addresses see the sibling [[defi-contract-registry]].

## Venue Overview

A structural comparison of the six CEX/DEX venues detailed below, drawn from the per-venue sections on this page. Use it to pick venues before diving into endpoint detail. (Auth column = whether public market data requires authentication; funding interval matters because rates must be annualized before comparison.)

| Venue | Type | Perps? | Public-data auth | Funding interval | Notable for arb |
|---|---|---|---|---|---|
| [[binance]] | CEX | Yes (fapi) | No | 8h | Highest volume; primary price discovery |
| [[coinbase]] | CEX | No (US) | Yes | n/a | Regulatory clarity; fiat on/off-ramp |
| [[hyperliquid]] | On-chain CLOB | Yes | No | **1h** | No KYC; on-chain auditable fills |
| OKX | CEX | Yes | No | 8h | Unified account; maker rebates at top tier |
| Bybit | CEX | Yes | No | 8h | Competitive top-tier fees; unified account |
| Kraken | CEX | Futures (separate) | No | (futures) | Deep fiat liquidity; strong security record |

For AsterDEX-specific endpoint behavior (hidden orders, multi-chain deployments, Pyth-priced stock perps), see [[asterdex]] and the AsterDEX strategy notes in [[asterdex-perp-trading-map]] — AsterDEX is not yet endpoint-documented on this page.

## Quick Reference: What You Need by Strategy

| Strategy | Required Feeds | Latency Sensitivity | Auth Required |
|---|---|---|---|
| [[cross-exchange-arbitrage]] | Spot order books (L2), trade streams | Sub-second | Yes (trading) |
| [[funding-rate-arbitrage]] | Funding rates, spot prices, perp prices | Minutes | Yes (trading) |
| [[triangular-arbitrage]] | Multiple spot order books on same venue | Sub-100ms | Yes (trading) |
| [[cash-and-carry]] | Spot prices, futures prices, funding rates | Minutes-hours | Yes (trading) |
| [[cross-chain-arbitrage]] | DEX prices, bridge status, gas prices | Seconds | No (on-chain) |
| [[statistical-arbitrage]] | OHLCV candles, trade history | Seconds-minutes | Optional |
| [[etf-arbitrage]] | NAV feeds, ETF prices, creation/redemption | Seconds | Yes (AP status) |

## Binance

The highest-volume CEX globally. Primary price discovery venue for most crypto pairs.

### REST API

| Endpoint | Purpose | Rate Limit | Auth |
|---|---|---|---|
| `GET /api/v3/ticker/bookTicker` | Best bid/ask for one or all symbols | 40 req/s (all symbols), 2 req/s (single) | No |
| `GET /api/v3/depth` | Order book snapshot (5/10/20/50/100/500/1000/5000 levels) | 50 weight per call | No |
| `GET /api/v3/ticker/price` | Latest price for one or all symbols | 2 req/s (single), 40 req/s (all) | No |
| `GET /api/v3/trades` | Recent trades (up to 1000) | 10 weight | No |
| `GET /api/v3/klines` | OHLCV candles (1m to 1M intervals) | 2 weight | No |
| `GET /fapi/v1/fundingRate` | Historical funding rates | 1 weight | No |
| `GET /fapi/v1/premiumIndex` | Current funding rate + next funding time + mark price | 1 weight | No |
| `GET /fapi/v1/openInterest` | Current open interest | 1 weight | No |
| `POST /api/v3/order` | Place order | 1 weight | Yes (HMAC-SHA256) |
| `DELETE /api/v3/order` | Cancel order | 1 weight | Yes |

**Rate limits:** 1,200 weight/minute for REST. IP-based for public, API-key-based for signed. Exceeding triggers a 429 HTTP response and potential IP ban (repeated offenses).

### WebSocket Streams

Base URL: `wss://stream.binance.com:9443/ws/` or `wss://stream.binance.com:9443/stream?streams=`

| Stream | Format | Update Frequency | Use Case |
|---|---|---|---|
| `<symbol>@bookTicker` | `{s, b, B, a, A}` (symbol, bid price, bid qty, ask price, ask qty) | Real-time (every BBO change) | Cross-exchange arb trigger |
| `<symbol>@depth@100ms` | Diff depth update | Every 100ms | Order book maintenance |
| `<symbol>@depth5` / `@depth10` / `@depth20` | Partial book snapshot | 1000ms | Quick depth check |
| `<symbol>@trade` | Individual trade events | Real-time | Execution monitoring |
| `<symbol>@kline_1m` | 1-minute candle updates | Real-time | Trend detection |
| `<symbol>@markPrice` (futures) | Mark price + funding rate | Every 3 seconds | Funding rate monitoring |
| `!markPrice@arr` (futures) | All mark prices + funding rates | Every 3 seconds | Cross-asset funding scan |

**Connection limits:** 5 messages/second per connection. Max 1024 streams per connection. Max 300 connections per 5 minutes per IP.

**bookTicker message schema:**
```json
{
  "u": 400900217,
  "s": "BTCUSDT",
  "b": "67234.50",
  "B": "1.234",
  "a": "67234.60",
  "A": "0.567",
  "T": 1713600000000,
  "E": 1713600000001
}
```

**Funding rate (premiumIndex) schema:**
```json
{
  "symbol": "BTCUSDT",
  "markPrice": "67234.50000000",
  "indexPrice": "67230.12000000",
  "estimatedSettlePrice": "67232.00000000",
  "lastFundingRate": "0.00010000",
  "nextFundingTime": 1713628800000,
  "interestRate": "0.00010000",
  "time": 1713600000000
}
```
Annualized rate = `lastFundingRate × 3 × 365` (funding every 8 hours).

### Binance Key Details for Arb

- **Fee tiers:** VIP 0 = 0.10%/0.10% (maker/taker). VIP 9 = 0.01%/0.03%. See [[fees]] for full tier table
- **Withdrawal processing:** Typically 1-30 minutes depending on network congestion and internal review
- **Funding interval:** Every 8 hours (00:00, 08:00, 16:00 UTC)
- **Order types for arb:** LIMIT, MARKET, LIMIT_MAKER (rejected if would immediately fill — guarantees maker fee), IOC (immediate-or-cancel), FOK (fill-or-kill)

---

## Coinbase (Advanced Trade API)

US-regulated, primary spot venue for institutional USD pairs. Higher fees but regulatory clarity.

### REST API

| Endpoint | Purpose | Rate Limit | Auth |
|---|---|---|---|
| `GET /api/v3/brokerage/best_bid_ask` | BBO for one or more products | 10 req/s | Yes (API key) |
| `GET /api/v3/brokerage/product_book` | Order book (aggregated levels) | 10 req/s | Yes |
| `GET /api/v3/brokerage/market/products/{id}/candles` | OHLCV | 10 req/s | Yes |
| `GET /api/v3/brokerage/market/products/{id}/ticker` | Latest ticker | 10 req/s | Yes |
| `POST /api/v3/brokerage/orders` | Place order | 15 req/s | Yes (OAuth2 or API key) |

**Rate limits:** 10,000 requests/hour for private endpoints. More restrictive than Binance.

### WebSocket Feed

Base URL: `wss://advanced-trade-ws.coinbase.com`

| Channel | Data | Update Frequency |
|---|---|---|
| `level2` | Full L2 order book updates | Real-time (every change) |
| `ticker` | Price, volume, BBO, 24h stats | Real-time |
| `ticker_batch` | Batched ticker for multiple products | Every 5 seconds |
| `market_trades` | Individual trades | Real-time |
| `heartbeats` | Connection health | Every second |

**Authentication required** for all WebSocket channels (JWT or API key signature).

### Coinbase Key Details for Arb

- **Fee tiers:** Advanced Trade pricing: 0.40%/0.60% (maker/taker) below $1K volume. Drops to 0.00%/0.05% above $400M monthly. Significantly higher than Binance at retail levels
- **Supported order types:** LIMIT, MARKET, STOP_LIMIT, BRACKET
- **Fiat settlement:** ACH (3-5 business days), wire (same day). Critical for fiat-crypto arb legs
- **No perpetual futures** (US regulatory constraint) — limits use in funding rate arb

---

## Hyperliquid

On-chain CLOB with CEX-level performance. 70-80% market share in on-chain perpetuals. No KYC.

### REST API (Info Endpoint)

Base URL: `https://api.hyperliquid.xyz/info` (POST with JSON body)

| Request Type | Body | Purpose |
|---|---|---|
| `{"type": "allMids"}` | None | Mid prices for all assets |
| `{"type": "l2Book", "coin": "BTC"}` | coin param | Full L2 order book |
| `{"type": "metaAndAssetCtxs"}` | None | All funding rates, open interest, mark prices |
| `{"type": "fundingHistory", "coin": "BTC", "startTime": ...}` | coin + time range | Historical funding rates |
| `{"type": "userFills", "user": "0x..."}` | user address | Trade history for an address |
| `{"type": "clearinghouseState", "user": "0x..."}` | user address | Positions, margin, PnL |

**Rate limits:** Generous but undocumented officially. Approximately 1,200 requests/minute observed.

### WebSocket

Base URL: `wss://api.hyperliquid.xyz/ws`

Subscribe message format:
```json
{"method": "subscribe", "subscription": {"type": "l2Book", "coin": "BTC"}}
{"method": "subscribe", "subscription": {"type": "allMids"}}
{"method": "subscribe", "subscription": {"type": "trades", "coin": "BTC"}}
{"method": "subscribe", "subscription": {"type": "orderUpdates", "user": "0x..."}}
```

| Channel | Data | Update Frequency |
|---|---|---|
| `l2Book` | Full L2 order book snapshots | Every change |
| `allMids` | All mid prices | Real-time |
| `trades` | Individual fills | Real-time |
| `orderUpdates` | Order status changes for your address | Real-time |
| `candle` | OHLCV candle updates | Per interval close |

### Hyperliquid Key Details for Arb

- **Fee tiers:** 0.01% maker / 0.035% taker (default). Referral codes reduce further. No VIP tiers — flat structure
- **Funding interval:** Every 1 hour (not 8 hours like most CEXs). Annualize: `rate × 24 × 365`
- **Max leverage:** 40x (BTC/ETH/HYPE), lower for smaller assets. Tiered down for large positions
- **Throughput:** 200,000 orders/sec, sub-200ms latency
- **No KYC:** Wallet-based authentication only. Critical for regulatory arbitrage considerations
- **On-chain settlement:** All positions, orders, and fills are on the HyperBVM L1 — fully auditable
- **Order types:** LIMIT, MARKET (simulated), TRIGGER (stop/take-profit), scaled orders

---

## OKX

Major derivatives venue with strong futures and options products.

### REST API

| Endpoint | Purpose | Rate Limit | Auth |
|---|---|---|---|
| `GET /api/v5/market/books` | Order book (1-400 levels) | 40 req/2s | No |
| `GET /api/v5/market/ticker` | Latest ticker | 20 req/2s | No |
| `GET /api/v5/market/trades` | Recent trades | 20 req/2s | No |
| `GET /api/v5/public/funding-rate` | Current funding rate | 20 req/2s | No |
| `GET /api/v5/public/funding-rate-history` | Historical funding rates | 10 req/2s | No |
| `GET /api/v5/public/open-interest` | Open interest | 20 req/2s | No |
| `POST /api/v5/trade/order` | Place order | 60 req/2s | Yes (HMAC-SHA256) |

### WebSocket

Base URLs: `wss://ws.okx.com:8443/ws/v5/public` (public) / `wss://ws.okx.com:8443/ws/v5/private` (private)

| Channel | Data | Notes |
|---|---|---|
| `books5` / `books` / `books50-l2-tbt` | Order book (5/400/50 levels, tick-by-tick) | `books50-l2-tbt` is best for arb |
| `tickers` | BBO + 24h stats | Real-time |
| `trades` | Individual trades | Real-time |
| `funding-rate` | Funding rate updates | Per settlement |
| `mark-price` | Mark price | Real-time |

### OKX Key Details for Arb

- **Fee tiers:** VIP 0 = 0.08%/0.10% (maker/taker). VIP 8 = -0.005%/0.015% (maker rebate)
- **Funding interval:** Every 8 hours (00:00, 08:00, 16:00 UTC). Same as Binance
- **Unified account:** Spot, futures, options, margin all in one account. Simplifies cross-instrument arb

---

## Bybit

Major derivatives exchange with competitive fee tiers.

### REST API

| Endpoint | Purpose | Rate Limit | Auth |
|---|---|---|---|
| `GET /v5/market/orderbook` | Order book (1-200 levels) | 50 req/s | No |
| `GET /v5/market/tickers` | Ticker data | 50 req/s | No |
| `GET /v5/market/funding/history` | Historical funding rates | 20 req/s | No |
| `GET /v5/market/open-interest` | Open interest | 20 req/s | No |
| `POST /v5/order/create` | Place order | 10 req/s | Yes (HMAC-SHA256) |

### WebSocket

Base URL: `wss://stream.bybit.com/v5/public/linear` (USDT perps) / `wss://stream.bybit.com/v5/public/spot`

| Channel | Data | Notes |
|---|---|---|
| `orderbook.1` / `orderbook.50` / `orderbook.200` | Order book (1/50/200 levels) | Snapshot + delta |
| `tickers` | BBO, funding rate, OI | Real-time |
| `publicTrade` | Individual trades | Real-time |

### Bybit Key Details for Arb

- **Fee tiers:** VIP 0 = 0.10%/0.10%. Pro 5 = 0.00%/0.02%
- **Funding interval:** Every 8 hours (00:00, 08:00, 16:00 UTC)
- **Unified Trading Account** available (similar to OKX)

---

## Kraken

Long-standing exchange with strong security track record and deep fiat liquidity.

### REST API

| Endpoint | Purpose | Rate Limit | Auth |
|---|---|---|---|
| `GET /0/public/Depth` | Order book (up to 500 levels) | 1 req/s per pair | No |
| `GET /0/public/Ticker` | Ticker (BBO, volume, VWAP) | 1 req/s | No |
| `GET /0/public/Trades` | Recent trades | 1 req/s | No |
| `POST /0/private/AddOrder` | Place order | 15 req/45s | Yes (HMAC-SHA512) |

### WebSocket (v2)

Base URL: `wss://ws.kraken.com/v2`

| Channel | Data | Notes |
|---|---|---|
| `book` | Order book (10/25/100/500/1000 levels) | Snapshot + delta |
| `ticker` | BBO + stats | Real-time |
| `trade` | Trades | Real-time |
| `ohlc` | Candles | Per interval |

### Kraken Key Details for Arb

- **Fee tiers:** 0.16%/0.26% (maker/taker) below $50K. 0.00%/0.10% above $10M monthly
- **Strong fiat on-ramps:** USD, EUR, GBP, CAD, AUD, JPY. Useful for fiat-crypto arb legs
- **Kraken Futures** (separate platform): has perpetuals with funding rates, different API

---

## Cross-Exchange Normalization Challenges

An arbitrage system must handle these differences:

### Funding Rate Sign Convention
| Exchange | Positive Funding Means | Funding Interval |
|---|---|---|
| Binance | Longs pay shorts | 8 hours |
| OKX | Longs pay shorts | 8 hours |
| Bybit | Longs pay shorts | 8 hours |
| Hyperliquid | Longs pay shorts | **1 hour** |
| dYdX | Longs pay shorts | 1 hour |

The sign convention is consistent across major CEXs, but **Hyperliquid and dYdX use 1-hour funding** vs. 8-hour on CEXs. When comparing rates, always annualize first.

### Timestamp Formats
| Exchange | Format | Timezone |
|---|---|---|
| Binance | Unix milliseconds | UTC |
| Coinbase | ISO 8601 string | UTC |
| Hyperliquid | Unix milliseconds | UTC |
| OKX | Unix milliseconds (string) | UTC |
| Bybit | Unix milliseconds (string) | UTC |
| Kraken | Unix seconds (float) | UTC |

### Symbol/Pair Naming
| Exchange | BTC/USDT Spot | BTC/USDT Perp |
|---|---|---|
| Binance | `BTCUSDT` | `BTCUSDT` (fapi) |
| Coinbase | `BTC-USDT` | N/A |
| Hyperliquid | N/A (perps only) | `BTC` |
| OKX | `BTC-USDT` | `BTC-USDT-SWAP` |
| Bybit | `BTCUSDT` | `BTCUSDT` (linear) |
| Kraken | `XXBTZUSD` / `BTCUSD` | `PF_XBTUSD` (futures) |

### Recommended Normalization Libraries
- **CCXT** (Python/JS/PHP) — unified API across 100+ exchanges. Best starting point for multi-venue arb. Handles auth, rate limiting, and schema normalization
- **Tardis.dev SDK** — for historical data normalization (backtesting)
- **Custom wrappers** — for latency-sensitive production systems where CCXT overhead (5-20ms) matters

## Latency Considerations

| Exchange | Typical REST Latency | WebSocket Latency | Co-location Available |
|---|---|---|---|
| Binance | 50-200ms | 10-50ms | No (AWS Tokyo/Virginia) |
| Coinbase | 50-150ms | 10-30ms | No |
| Hyperliquid | 100-300ms | 50-200ms | No (on-chain finality) |
| OKX | 50-200ms | 10-50ms | No |
| Bybit | 50-200ms | 10-50ms | No |
| Kraken | 100-300ms | 20-100ms | No |

For [[latency-arbitrage]], every millisecond matters. For [[funding-rate-arbitrage]] or [[cash-and-carry]], latency is largely irrelevant — you have hours to position.

## How Trading and AI Systems Consume These APIs

The endpoints above are raw inputs. A production arbitrage or agentic-trading system layers the following pipeline on top of them:

| Layer | What it does | Feeds from |
|---|---|---|
| **Ingestion** | Maintain persistent WebSocket connections per venue; reconnect on drop; resync L2 books from REST snapshot + diff stream | `bookTicker`/`l2Book`/`books` streams; `depth` REST snapshots |
| **Normalization** | Map venue-specific symbols, timestamps, and funding-sign conventions onto one internal schema | The three normalization tables above; CCXT |
| **Signal** | Compute cross-venue spreads, annualized funding differentials, triangular loops | Normalized BBO + funding feeds |
| **Risk gate** | Check inventory limits, counterparty caps (max 20-30% per venue per [[arbitrage-opportunity-map]]), and fee-adjusted edge | [[fees]]; account state endpoints |
| **Execution** | Place signed orders (HMAC/JWT) using maker-preserving order types; cancel/replace on staleness | `POST` order endpoints; `LIMIT_MAKER`/IOC/FOK |
| **Reconciliation** | Confirm fills, update positions, recompute net delta | `userFills`/`clearinghouseState`; order-update streams |

For an **AI agent** specifically, the read path (public market-data endpoints, mostly unauthenticated) is safe to expose broadly, while the write path (signed order placement) should sit behind a deterministic risk gate — the agent proposes, the gate disposes. The normalization layer is what lets a single agent reason across venues without venue-specific prompting: every venue's funding rate arrives already annualized and sign-aligned, every order book already in one format. The decision framework for *which* strategy an agent should run on a given venue lives in [[arbitrage-opportunity-map#part-7-from-map-to-position--a-decision-framework|the arbitrage map's decision framework]].

## Data-Quality Caveats

Reference endpoints describe what data is *available*, not whether it is *correct* in the moment you act on it. Known pitfalls:

- **Annualize before comparing.** [[hyperliquid]] and dYdX fund hourly; CEXs fund every 8 hours. A raw rate comparison is meaningless across these — always annualize first (the per-venue "Key Details" sections give the multiplier). This is the single most common cross-venue funding error.
- **Order-book staleness.** L2 books maintained from diff streams drift out of sync if a sequence gap is missed. Periodically resync from a REST snapshot and validate the sequence/update IDs.
- **Rate-limit bans, not just throttles.** Exceeding REST weight on [[binance]] triggers a 429 and, on repeat offenses, an IP ban — losing a venue mid-trade leaves a leg unhedged. Budget headroom below the documented limits.
- **CCXT overhead.** The normalization convenience of CCXT adds ~5-20ms (per the normalization-libraries note); fine for funding/basis arb (hours of latitude), too slow for [[latency-arbitrage]] where custom wrappers are required.
- **Withdrawal/settlement latency is an arb risk, not a data field.** Binance withdrawals take minutes; Coinbase fiat settles in days (ACH 3-5 business days). A "profitable" cross-venue spread can evaporate before capital physically arrives at the other leg.
- **On-chain finality vs. CEX latency.** [[hyperliquid]] settles on-chain (auditable but higher latency); CEXs are faster but you trust their matching engine. Different risk, not strictly better/worse.
- **Endpoints and limits change.** Treat every endpoint, rate limit, and fee tier on this page as accurate as of the documented date (April 2026) and re-verify against the primary docs in Sources before deploying capital.

## Related

- [[arbitrage-opportunity-map]] — the strategies these feeds serve
- [[asterdex-perp-trading-map]] · [[hyperliquid-perp-trading-map]] — venue-specific perp playbooks
- [[defi-contract-registry]] — on-chain (DEX/bridge/flash-loan) execution addresses
- [[crypto-data-sources]] · [[data-sources-overview]] — broader data catalog
- [[cross-exchange-arbitrage]] · [[funding-rate-arbitrage]] · [[triangular-arbitrage]] · [[cash-and-carry]] · [[latency-arbitrage]]
- [[fees]] — fee-tier tables referenced throughout
- [[binance]] · [[coinbase]] · [[hyperliquid]]

## Sources

- Binance API documentation (api.binance.com)
- Coinbase Advanced Trade API documentation
- Hyperliquid API documentation (hyperliquid.gitbook.io)
- OKX API V5 documentation
- Bybit V5 API documentation
- Kraken REST API documentation
- [[crypto-data-sources]]
- [[fees]]
