---
title: "Crypto Data Sources"
type: reference
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [data, crypto, on-chain]
aliases: ["Crypto Market Data", "Blockchain Data Sources"]
related: ["[[data-sources-overview]]", "[[free-data-sources]]", "[[paid-data-providers]]", "[[alternative-data-providers]]"]
---

# Crypto Data Sources

Where to get crypto market data, on-chain data, and DeFi-specific data. Crypto is unusual in that the highest-quality market data is often *free* — exchange APIs are public — and the value-add of paid vendors is mostly normalization and storage rather than new information. The expensive part of crypto data is the on-chain analytics layer and the cross-venue execution data.

This page is the crypto-specific companion to [[free-data-sources]] (free providers across all asset classes), [[paid-data-providers]] (institutional vendors), and the [[data-sources-overview]] hub. For the strategies that consume this data — [[funding-rate-arbitrage]], [[stablecoin-pair-arbitrage]], [[liquidation-cascade-arbitrage]], and [[mev-execution-guide]] — see the per-strategy "Indicators / Data Used" sections.

## Data Layers at a Glance

Crypto data divides into five distinct layers, each with a different cost/value profile. The rule of thumb: the closer the data is to a public chain or a public exchange feed, the cheaper it is; the value-add (and the price) climbs as you move toward labeled, normalized, and pre-computed analytics.

| Layer | What it is | Cost profile | Primary value-add of paid vendors |
|---|---|---|---|
| **Market data (spot/derivs)** | OHLCV, trades, L2 depth, funding, OI | Mostly free (exchange APIs) | Cross-venue normalization, historical L2 storage |
| **On-chain raw** | Blocks, transactions, logs, balances | Free (explorers, your own node) | Indexing, decoding, query convenience |
| **On-chain analytics** | MVRV, SOPR, flows, wallet labels | Free tiers thin; premium paid | Pre-computed metrics, smart-money labels |
| **DeFi/protocol** | TVL, yields, protocol revenue | Mostly free (DefiLlama, subgraphs) | Standardized financials, granularity |
| **Execution/MEV** | Mempool, bundle inclusion, MEV history | Free tools + paid low-latency RPC | Latency, private orderflow, decoded MEV |

## Provider Quick-Reference

A consolidated index of every provider mentioned on this page, with its layer, cost tier, and best use. Detailed write-ups follow in the sections below. (Cost descriptors are tier *shapes* — free vs. paid — not quoted prices; the inline ranges in the detail sections are the figures as documented historically and may drift.)

| Provider | Layer | Cost tier | Coverage strength | Best for |
|---|---|---|---|---|
| Exchange APIs (Binance, Coinbase, Kraken, OKX, Bybit, Bitfinex, Deribit) | Market | Free | Single-venue full depth + derivs | ~80% of all research |
| Tardis.dev | Market (historical) | Paid (low) | Normalized L2 history, multi-venue | Microstructure + arb backtests |
| Kaiko | Market | Paid (institutional) | 100+ venues normalized | Fund single-source-of-truth |
| Amberdata | Market + on-chain | Paid (institutional) | Combined market + chain | Funds wanting one vendor |
| CoinGecko / CoinMarketCap | Market (aggregated) | Free + paid | Broad coin universe | Universe construction, market cap |
| CryptoCompare / Cryptowatch | Market (aggregated) | Free + paid | Mid-tier cross-venue | Broad price reference |
| Glassnode | On-chain analytics | Free + paid | BTC/ETH + select alts | Cycle analysis, supply, flows |
| Nansen | On-chain analytics | Paid | ETH + EVM L2 wallet labels | [[smart-money-orderflow-combo\|Smart money]] tracking |
| Arkham Intelligence | On-chain analytics | Free + paid | Entity labeling | Wallet/entity tracking, alerts |
| Dune Analytics | On-chain (SQL) | Free + paid | Major chains, community dashboards | Custom analytics, backtest features |
| Flipside Crypto | On-chain (SQL) | Free + paid | Broad chain coverage | SQL analytics, broader than Dune |
| Chainalysis | On-chain (compliance) | Institutional | Forensics + intelligence | Compliance, AML, market intel |
| Block explorers (Etherscan, Solscan, etc.) | On-chain raw | Free | Per-chain | Basic queries, tx verification |
| The Graph | On-chain (indexing) | Free + paid | DeFi subgraphs | Protocol-specific GraphQL queries |
| Coinglass | Derivatives | Free + paid | Funding, OI, liquidations | Funding/liquidation strategies |
| Laevitas | Derivatives (options) | Free + paid | Options surfaces, basis | Vol surface, basis research |
| GVOL (Genesis Volatility) | Derivatives (options) | Paid | Crypto options RV/IV | Options vol analytics |
| DefiLlama | DeFi | Free | Broad protocol TVL/yield | TVL, yield, stablecoin flows |
| Token Terminal | DeFi (financials) | Free + paid | Protocol revenue/P-S | Protocol fundamental metrics |
| OpenSea / Reservoir / NFTScan | NFT | Free + paid | NFT marketplaces | Floor prices, sales, listings |
| Flashbots / MEV-Inspect / EigenPhi | MEV | Free | Ethereum MEV history | MEV analysis (see [[mev-execution-guide]]) |

## Market Data

### Exchange APIs (Free, Direct)

The default and best starting point. Every major venue exposes free public REST and WebSocket APIs.

- **Binance** — largest by volume, broadest pair coverage, depth and trades freely available. Historical depth via REST endpoints.
- **Coinbase / Coinbase Pro** — US-regulated, full L2 depth via WebSocket, free historical via REST.
- **Kraken** — strong API, decent historical depth, supports many fiat pairs.
- **OKX / Bybit / Bitget** — major derivatives venues, free perpetual funding history.
- **Bitfinex** — early adopter, strong historical depth.
- **Deribit** — the dominant crypto options venue, free API access.
- **dYdX, GMX, Hyperliquid** — DEX perps; on-chain data plus indexer APIs.

**Pros:** Free, real-time, full venue depth, includes derivatives, funding rates, open interest.

**Cons:** Single-venue (you have to query each separately for cross-venue analysis), historical depth varies (some only 1-3 years), schema differences across venues, rate limits.

**Use for:** ~80% of all crypto research can be done entirely with free exchange APIs.

### Tardis.dev (Paid)

Range: $59-$399/month.

**Pros:** Historical data normalized across major venues including full L2 orderbook history, trades, derivatives funding, options chains. Modern API.

**Cons:** Historical only; for live data you still need direct exchange feeds.

**Best for:** Microstructure research, backtesting strategies that depend on orderbook depth, cross-venue arbitrage backtests. The single most cost-effective serious crypto data source.

### Kaiko (Paid, Institutional)

Range: $1K-$10K+/month.

**Pros:** Institutional-grade normalization across 100+ venues, includes derivatives, OHLCV and reference rates, designed for fund clients.

**Cons:** Expensive for individuals.

**Best for:** Funds running multi-venue strategies needing a single source of truth.

### Amberdata (Paid, Institutional)

Combines market data and on-chain. Comparable pricing to Kaiko.

### CoinGecko / CoinMarketCap (Free + Paid Tiers)

Aggregated price data. Free tiers are good for basic info; paid tiers ($129+/month) for higher rate limits.

**Use for:** Universe construction, market cap sorting, broad sentiment. Not for backtesting.

### Cryptowatch / CryptoCompare

Mid-tier aggregators. Cryptowatch was a popular Kraken-owned aggregator with a free chart UI; CryptoCompare offers REST APIs across venues.

## On-Chain Analytics

### Glassnode

Range: free + $30-$800/month tiers.

**Pros:** Pre-computed metrics for BTC, ETH, and select alts: UTXO age distribution, MVRV, SOPR, NUPL, exchange flows, miner balances, hash rate, etc. Saves significant engineering effort.

**Cons:** Most useful metrics are on higher tiers. Free tier is mostly demonstration.

**Use for:** Macro crypto cycle analysis, supply distribution, flow tracking.

### Nansen

Range: $150-$2000+/month.

**Pros:** Wallet labels (smart money tracking), real-time alerts, portfolio analytics. The leading wallet-intelligence platform.

**Cons:** Expensive. Coverage strongest on ETH and EVM L2s; weaker elsewhere.

**Use for:** [[smart-money-orderflow-combo|Smart-money]] tracking, NFT activity, DeFi position tracking.

### Dune Analytics

Range: free + paid tiers ($349-$799+/month).

**Pros:** SQL queryable on-chain data across major chains, large library of community-built dashboards, flexible.

**Cons:** Requires SQL skills, query latency varies, you build your own metrics.

**Use for:** Custom on-chain analytics, backtesting on-chain features, DeFi protocol analytics.

### Arkham Intelligence

Range: free + paid.

**Pros:** Wallet labeling (with crowdsourced contributions), entity tracking, alerts.

**Cons:** Newer vendor, narrower coverage than Nansen on some chains.

### Chainalysis

Range: institutional. Mostly used for compliance and law enforcement, but also offers market intelligence products.

### Blockchain Explorers (Free)

- **Etherscan** (Ethereum), **BscScan** (BSC), **Polygonscan**, **Solscan**, **Snowtrace** (Avalanche), **Arbiscan** (Arbitrum)
- **Blockchair** — multi-chain, including BTC, BCH, LTC, BSV
- **Mempool.space** — BTC mempool monitoring

Free APIs available with rate limits. Sufficient for most basic on-chain queries.

### The Graph (Free + Paid)

Decentralized indexing protocol. Subgraphs index DeFi protocols and expose GraphQL APIs.

**Use for:** Querying specific DeFi protocols (Uniswap, Aave, etc.) at low cost.

## Derivatives-Specific Data

### Skew (acquired by Coinbase) — historical, partial replacement: Coinglass

- **Coinglass** (formerly Coinalyze) — funding rates, open interest, liquidations, options data across venues. Free and paid tiers.
- **Laevitas** — crypto derivatives analytics, options surfaces, futures basis.
- **Genesis Volatility (GVOL)** — crypto options volatility analytics, RV and IV.

**Use for:** Funding-rate strategies ([[funding-rate-arbitrage]]), basis trading, liquidation cascade analysis, options vol surface research.

## DeFi-Specific Data

### DefiLlama (Free)

The most comprehensive free DeFi TVL and yield aggregator.

**Pros:** Free, broad protocol coverage, includes TVL, yields, treasury data, stablecoin flows.

**Cons:** Aggregated; for granular data you still need on-chain queries.

**Use for:** TVL tracking, protocol selection, yield comparisons.

### Token Terminal

Range: free + paid.

**Pros:** Standardized financial metrics for crypto protocols (revenue, TVL, P/S ratios).

**Cons:** Subset of protocols.

### Flipside Crypto

Range: free + paid.

**Pros:** SQL-based on-chain analytics similar to Dune but with broader chain coverage.

## NFT Data

- **OpenSea API** (free) — listings, sales, floor prices for the largest NFT marketplace
- **Reservoir** — multi-marketplace aggregation API
- **NFTScan** / **NFT Price Floor** — NFT analytics aggregators

## MEV Data

- **MEV-Inspect / Flashbots** — Ethereum MEV transaction history
- **EigenPhi** — decoded MEV transaction analysis and profit attribution
- **Eden Network** / private mempool data

For the operational side — how to *act* on this data as a searcher (bundle construction, mempool monitoring, gas bidding) — see [[mev-execution-guide]] and the parent [[mev-strategies]] / [[mev]] pages. MEV data is also a key input to [[liquidation-cascade-arbitrage]] (pending oracle updates and at-risk positions).

## How Trading and AI Systems Consume This Data

The provider catalog above is only half the picture; the other half is *how* an automated system ingests it. Different consumers have radically different latency and completeness requirements.

| Consumer | Latency need | Data shape | Typical sources |
|---|---|---|---|
| **Live execution / MEV bots** | Sub-block (<1s) | Streaming WebSocket + mempool | Direct exchange WS, custom RPC node, Flashbots |
| **Systematic backtest** | None (offline) | Normalized historical L2 + trades | Tardis.dev, Kaiko, exchange REST archives |
| **On-chain feature pipelines** | Minutes–hours | Batch SQL extracts | Dune, Flipside, The Graph subgraphs |
| **LLM/AI research agents** | Seconds | REST JSON, summarized metrics | CoinGecko, DefiLlama, Glassnode API, Dune API |
| **Risk / monitoring dashboards** | Seconds–minutes | Aggregated snapshots | Coinglass, DefiLlama, exchange REST |

Practical ingestion notes:

- **Streaming vs. polling.** Latency-sensitive consumers (arb, MEV, liquidations) must use WebSocket streams and a private/low-latency RPC; polling REST loses races. Research and AI consumers can poll REST on a schedule.
- **Normalization is the recurring cost.** Every venue uses different symbols (`BTCUSDT` vs. `BTC-USD` vs. `XBT/USD`), funding conventions, and timestamp units. A canonical internal schema is mandatory before data from multiple venues is combined.
- **AI/LLM agents prefer pre-computed metrics.** Feeding an LLM raw L2 books is wasteful; feeding it Glassnode/DefiLlama/Coinglass *summaries* (MVRV, TVL, funding, OI) is dense and decision-relevant. Production pipelines lean on aggregated REST endpoints for this reason.
- **Rate limits drive architecture.** Free tiers throttle hard. A caching layer between the provider and the strategy (or a paid tier) is required for anything beyond prototyping.

## A Recommended Crypto Stack

### Free
Exchange APIs (Binance, Coinbase, Deribit) + Etherscan + DefiLlama + Glassnode free + Dune free. Covers most personal research.

### Starter Paid (~$200-$500/month)
Tardis.dev historical + Glassnode mid-tier + Coinglass paid. Adds normalized historical depth, premium on-chain metrics, derivatives analytics.

### Serious Retail (~$1K-$3K/month)
Add Nansen for wallet intelligence, Dune Plus tier for analytics, Laevitas or GVOL for options.

### Institutional
Kaiko or Amberdata + Nansen Enterprise + Chainalysis + custom node infrastructure for specific chains.

## Common Crypto Data Pitfalls

1. **Wash trading inflates reported volume.** Many smaller venues report fake volume. Cross-check with chain analytics or use institutional sources that filter.

2. **Survivorship in coin universes.** Coins that delisted or went to zero are often missing from historical datasets. Major bias for any historical altcoin study.

3. **Missing exchange data during outages.** Exchanges go down. Historical data may have gaps that aren't flagged.

4. **Funding rate sign conventions.** Different venues use different sign conventions for funding. Read the docs carefully.

5. **Time zone and timestamp formats.** Some APIs return UTC, some local, some Unix epochs in seconds, some in milliseconds. Normalize.

6. **Cross-venue price differences.** "BTC price" depends on which venue. For backtests that match real execution, use the venue you'd actually trade on.

7. **DEX TVL gaming.** Recursive deposits, double-counting across protocols, and token-price denomination effects can all inflate apparent TVL.

### Pitfall Summary

| Pitfall | Who it hits hardest | Mitigation |
|---|---|---|
| Wash trading | Volume-ranked universe selection | Filter via institutional data or chain analytics |
| Survivorship in coin universes | Historical altcoin studies | Include delisted/dead tokens explicitly |
| Outage data gaps | Backtests assuming continuous feeds | Cross-check timestamps for gaps; flag them |
| Funding sign conventions | Funding-rate strategies | Read each venue's docs; normalize sign |
| Timestamp format drift | Any multi-venue merge | Normalize to UTC ms before joining |
| Cross-venue price differences | Execution-realistic backtests | Use the venue you will actually trade |
| DEX TVL gaming | Protocol selection by TVL | Cross-check with on-chain queries |

These caveats are the crypto counterpart to the survivorship/lookahead biases documented for traditional assets in [[free-data-sources]] — re-validate any deployable strategy against a clean dataset (see also [[survivorship-bias]] and [[lookahead-bias]]).

## Sources

- Crypto exchange API documentation (varies by venue)
- [[alternative-data-providers]] — for the broader alt-data ecosystem
- Flashbots and EigenPhi public documentation (for the MEV-data layer)
- General market knowledge; no specific wiki source ingested yet.

## Related

- [[data-sources-overview]]
- [[free-data-sources]]
- [[paid-data-providers]]
- [[alternative-data-providers]]
- [[funding-rate-arbitrage]]
- [[stablecoin-pair-arbitrage]]
- [[liquidation-cascade-arbitrage]]
- [[mev-execution-guide]]
- [[mev-strategies]]
- [[smart-money-orderflow-combo]]
- [[survivorship-bias]], [[lookahead-bias]]
