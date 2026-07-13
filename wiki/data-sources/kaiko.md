---
title: "Kaiko"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, crypto, derivatives, market-microstructure]
source_type: data
source_url: "https://www.kaiko.com"
aliases: ["Kaiko Data", "Kaiko Markets"]
related: ["[[crypto-data-sources]]", "[[coinapi]]", "[[ccxt]]", "[[slippage-modeling]]", "[[market-impact-models]]", "[[execution-model-differences]]", "[[crypto-perp-backtesting-pitfalls]]", "[[point-in-time-data]]"]
---

Kaiko is an institutional-grade crypto market-data provider offering tick-level trade data, full order-book snapshots and reconstructions, derivatives data, and execution benchmarks across 100+ centralized and decentralized venues. The firm targets banks, asset managers, exchanges, and quant funds that need audit-quality data for trade-cost analysis (TCA), backtesting, and reference pricing. Kaiko is frequently cited in microstructure research and was used in the post-incident liquidity reconstruction of the February 2025 Bybit hack.

## Overview

Kaiko was founded in 2014 in Paris and has positioned itself as the "Bloomberg of crypto" — a single, normalized data feed designed for institutional consumption rather than retail dashboards. Coverage spans spot, perpetual futures, dated futures, options, and on-chain DEX trades. The firm publishes the [[kaiko-indices|Kaiko Indices]] (a benchmark family) and supports compliance reporting under MiFID II / MiCA.

## What Kaiko Provides

### Tick-Level Trade Data

- Every trade print (price, size, side, timestamp, venue) for 100+ exchanges
- Sub-millisecond timestamps (venue + Kaiko receipt) — useful for latency-sensitive backtests
- Backfilled to the earliest history each venue makes available (BTC/USD on Bitstamp goes back to 2011)

### Order-Book Snapshots and Reconstructions

- **Snapshots** at configurable intervals (typically 100ms / 1s / 10s)
- **Full L2 reconstructions** from tick-by-tick deltas — required for realistic [[slippage-modeling|slippage modeling]] and [[market-impact-models|market-impact estimation]]
- **L3** (per-order) data on a subset of venues
- Used by quants to model real fill prices instead of assuming mid-price execution

### Derivatives Data

- Perpetual and dated futures: trades, OB snapshots, funding rates, mark prices, open interest
- Options chains (Deribit, OKX) with implied vols and Greeks
- Liquidations feeds for major perp venues

### Reference Rates and Indices

- BTC/USD and ETH/USD reference rates (volume-weighted, manipulation-resistant)
- Used as settlement benchmarks for OTC derivatives and ETFs
- Compliant with IOSCO Principles for Financial Benchmarks

### OHLCV and Aggregates

- 1-minute, 1-hour, 1-day OHLCV across all covered pairs
- VWAP / TWAP aggregates over arbitrary windows

### On-Chain / DEX Data

- Uniswap, Curve, and other major DEX trades reconstructed into tick form
- Useful for cross-venue arbitrage research between CEX and DEX liquidity

## Coverage

| Category | Detail |
|---|---|
| **Centralized exchanges** | 100+ including Binance, Coinbase, Kraken, OKX, Bybit, Bitfinex, Bitstamp, Gemini |
| **Decentralized venues** | Uniswap (v2/v3/v4), Curve, Balancer, dYdX, [[hyperliquid|Hyperliquid]] |
| **Derivatives venues** | [[bitmex|BitMEX]], Deribit, Binance Futures, OKX, Bybit, CME, [[hyperliquid|Hyperliquid]] |
| **Asset pairs** | 100,000+ trading pairs |
| **History** | Up to 2011 for the longest-running pairs |
| **NDF rates** | Non-deliverable forwards on emerging-market crypto pairs |

## Use Cases for Backtesting

### Depth-Aware Slippage Modeling

A backtest that assumes mid-price execution systematically overestimates returns. With Kaiko's full order book, a strategy can be replayed against the actual liquidity that existed at each timestamp — sweeping through the book to measure realistic fill prices for the intended order size. See [[slippage-modeling]] and [[market-impact-models]].

### Microstructure Research

Order-book imbalance, queue position, spread dynamics, and cancel-replace behavior require L2/L3 data that retail aggregators do not provide. Kaiko's reconstructions are a standard input for these studies.

### Transaction Cost Analysis (TCA)

Buy-side firms compare their actual execution prices against Kaiko-derived benchmarks (arrival price, VWAP, implementation shortfall) to attribute trading costs and evaluate brokers / smart-order routers.

### Cross-Venue Arbitrage Research

Synchronized timestamped data across venues is essential to study latency arbitrage, funding-rate arbitrage, and basis trades. See [[crypto-perp-backtesting-pitfalls]].

### Avoiding Look-Ahead Bias

Kaiko provides immutable, [[point-in-time-data|point-in-time]] data — trades and OB states are never retroactively edited. This contrasts with some retail aggregators that fill in late-arriving data after the fact.

## Pricing Tiers (Approximate)

| Tier | Audience | Price |
|---|---|---|
| **Researcher / academic** | Universities, individuals | Free or discounted access for non-commercial research |
| **Professional** | Small funds, prop traders | Low five figures USD/year for selected venues / data types |
| **Enterprise** | Banks, large funds, exchanges | Custom contracts; six- to seven-figure USD/year for full tick + OB |

Pricing is venue- and data-type-segmented (e.g., spot vs. derivatives, snapshots vs. full reconstructions). Historical bulk downloads are priced separately from real-time streaming. Kaiko does not publish a public price sheet.

## How Kaiko Compares to Alternatives

| Provider | Strength | Weakness vs. Kaiko |
|---|---|---|
| **[[coinapi|CoinAPI]]** | Wider exchange count, simpler REST API, lower price | Less depth on order books; weaker microstructure focus |
| **CryptoCompare** | Free tier, friendly for retail | Aggregated/normalized data; not tick-true at venue level |
| **Tardis** | Strong on derivatives tick + OB, competitive pricing | Smaller venue set than Kaiko; less institutional brand |
| **Amberdata** | Combines on-chain + market data | Order-book depth is shallower than Kaiko |
| **[[ccxt|CCXT]]** | Free, open-source, live data | Not a historical archive; rate-limited; not PIT-clean |

In practice institutional desks often pair Kaiko (historical / reference / OB) with [[ccxt|CCXT]] (live multi-venue execution) and on-chain providers like [[glassnode|Glassnode]] or [[dune-analytics|Dune]] for the on-chain leg.

## Data Caveats

1. **PIT semantics**: trade data is immutable, but Kaiko occasionally backfills late or corrected venue data — query timestamps versus receipt timestamps to detect this.
2. **Rate limits**: REST API has per-second and per-day limits on the lower tiers; bulk historical downloads require S3 / streaming endpoints.
3. **Venue coverage gaps**: some smaller perp venues (e.g., very new launches) may take weeks to be added.
4. **DEX data**: reconstruction depends on subgraph health; outages or reorgs can introduce transient gaps.
5. **Cost vs. benefit**: for retail-scale strategies that don't need OB depth, the price step from CoinAPI/Tardis to Kaiko is hard to justify.

## Sources

1. Kaiko official site — https://www.kaiko.com
2. Kaiko documentation — https://docs.kaiko.com
3. Kaiko research blog (microstructure case studies) — https://research.kaiko.com

## Related

- [[crypto-data-sources]] — Full catalog of crypto data providers
- [[coinapi|CoinAPI]] — Multi-exchange aggregator alternative
- [[ccxt|CCXT]] — Open-source library for live multi-venue access
- [[slippage-modeling]] — Modeling realistic execution costs
- [[market-impact-models]] — Estimating price impact of large orders
- [[execution-model-differences]] — Why backtest fills diverge from live fills
- [[crypto-perp-backtesting-pitfalls]] — Crypto-specific backtest hazards
- [[point-in-time-data]] — Avoiding look-ahead bias in historical data
- [[hyperliquid|Hyperliquid]] — On-chain perp venue covered by Kaiko
- [[bitmex|BitMEX]] — Historical perp data covered by Kaiko
