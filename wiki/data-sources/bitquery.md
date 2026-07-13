---
title: "Bitquery"
type: source
created: 2026-05-04
updated: 2026-06-12
status: good
tags: [data-provider, on-chain-analytics, crypto, solana, defi, sniping]
source_type: data
source_url: "https://bitquery.io"
source_author: "Bitquery"
confidence: high
aliases: ["Bitquery.io"]
related: ["[[dune-analytics]]", "[[pump-fun]]", "[[solana]]", "[[memecoin-sniping]]", "[[token-migration-sniping]]", "[[pumpswap]]", "[[dex-screener]]"]
---

# Bitquery

**Bitquery** (bitquery.io) is a multi-chain blockchain data platform offering GraphQL APIs, streaming WebSocket subscriptions, and historical datasets across more than 40 chains, with particularly deep and well-maintained endpoints for [[solana]] -- including dedicated [[pump-fun]] APIs covering trades, OHLCV, bonding curve progress, top traders, and PumpSwap migrations. It is the primary programmatic data source many builders use to power custom Pump.fun sniping dashboards and on-chain alpha pipelines.

---

## Key Features

### GraphQL API
- **Single query language across chains:** GraphQL endpoint returns trades, transfers, balances, smart contract events, and decoded program data with one consistent schema
- **Decoded Solana programs:** Pump.fun's program (`6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`) is decoded so traders can query bonding curve state, buy/sell events, and graduation events by name rather than parsing raw instruction data
- **Cross-chain coverage:** EVM chains (Ethereum, BNB Chain, Polygon, Arbitrum, Base, others) plus Solana, Tron, and additional non-EVM chains

### Pump.fun-Specific Endpoints
- **Real-time trades:** Live feed of buys and sells for any Pump.fun token
- **OHLCV:** Candle data at multiple intervals for graphs, signal generation, and backtests
- **Bonding curve progress:** Query how close a token is to the ~$69k market cap graduation threshold
- **Top traders per token:** Wallets ranked by realized PnL on a specific Pump.fun token
- **Migration / PumpSwap events:** Detect the moment a token graduates to [[pumpswap]] or [[raydium]]
- **New launches stream:** Subscribe to all newly launched Pump.fun tokens for sniping pipelines

### Streaming Subscriptions
- **WebSocket / GraphQL subscriptions:** Push-based feeds for trades, new tokens, and large transfers -- lower latency than polling
- **Use case:** Sniper bots and alert systems consume these streams to act within the same block as relevant events

### Historical Data
- **Backfilled history:** Multi-year historical event data for backtesting and research
- **Aggregations:** Pre-computed daily/hourly aggregates for volume, unique traders, fee revenue

---

## Pricing & Access

- **Free tier:** Limited monthly query volume on the GraphQL API, suitable for prototyping and small dashboards
- **Paid plans:** Tiered subscriptions scale by query volume, concurrent subscriptions, and historical depth -- typical structure for production sniping or alerting pipelines
- **Enterprise:** Custom plans with dedicated support, SLAs, and higher throughput
- **Authentication:** API key required for most endpoints; passed in HTTP headers
- **Documentation:** Public docs at docs.bitquery.io including a dedicated Pump.fun section

Specific pricing tiers change; check bitquery.io for current plans.

---

## Use Cases for Traders

- **Custom Pump.fun sniping dashboards:** Pull live new-launch and bonding-progress data into a private dashboard tailored to a trader's filters (curve speed, holder count, dev wallet rules) -- a setup explicitly recommended for [[memecoin-sniping]]
- **Migration sniping pipelines:** Subscribe to graduation events to time buys on [[pumpswap]] or [[raydium]] within a small number of blocks (see [[token-migration-sniping]])
- **Holder and bundle detection:** Query token holder distributions to score rug risk pre-trade
- **Top-trader discovery:** Rank wallets by realized PnL on Pump.fun tokens to source copy-trade candidates
- **Backtesting strategies:** Historical OHLCV and trade data on Pump.fun tokens enables backtests of MC-level strategies, bonding-curve heuristics, and rug filters
- **Alerting:** Wire GraphQL subscriptions into Telegram, Discord, or webhook handlers for live whale-move and graduation alerts
- **Cross-venue analytics:** Compare PumpSwap vs. [[raydium]] liquidity and volume for the same token to spot venue-arbitrage opportunities
- **Research and reporting:** Aggregate ecosystem-wide stats (graduation rate, average time-to-bond, dev-wallet behavior) for thesis work

---

## Limitations

- **Cost at scale:** Production-grade sniping pipelines typically require paid plans; sustained subscription streams and high query volume can drive monthly costs into the thousands
- **GraphQL learning curve:** Requires familiarity with GraphQL and the specific schema; less point-and-click than [[dex-screener]] or [[birdeye]]
- **Rate limits:** Free tier rate and complexity limits make it unsuitable for live trading workloads
- **Latency vs. direct RPC:** For absolute lowest-latency sniping, running a direct Solana RPC node or Geyser stream can be faster than going through any third-party API; Bitquery is the convenience-vs-latency tradeoff
- **Coverage drift:** As Pump.fun and [[pumpswap]] evolve, decoded schemas need updating; occasionally lags during major program upgrades
- **Single-vendor risk:** A single data provider becomes a critical dependency for any pipeline built on it

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]])
- Bitquery Pump.fun API documentation (https://docs.bitquery.io/docs/blockchain/Solana/Pumpfun/Pump-Fun-API/)

---

## Related

- [[dune-analytics]] -- SQL-based on-chain analytics; Bitquery's main alternative for custom queries (Bitquery is more streaming/programmatic, Dune is more dashboard/SQL)
- [[pump-fun]] -- the protocol Bitquery has dedicated APIs for
- [[pumpswap]] -- Pump.fun's native DEX, also covered by Bitquery endpoints
- [[solana]] -- the chain with Bitquery's deepest coverage
- [[memecoin-sniping]] -- the trading strategy family Bitquery most directly supports
- [[token-migration-sniping]] -- specific strategy that depends on Bitquery's graduation event feeds
- [[dex-screener]] -- complementary UI-driven discovery tool
