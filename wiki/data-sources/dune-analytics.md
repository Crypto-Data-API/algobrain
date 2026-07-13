---
title: "Dune Analytics"
type: source
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [data-provider, on-chain-analytics, defi]
source_type: data
source_url: "https://dune.com"
source_author: "Dune Analytics"
confidence: high
aliases: ["Dune", "Dune.com"]
related: ["[[defi]]", "[[crypto-data-sources]]", "[[token-terminal]]", "[[zapper]]", "[[on-chain-analytics]]"]
---

Dune Analytics is a community-powered blockchain analytics platform that allows users to query on-chain data using SQL and build shareable dashboards. Unlike pre-packaged analytics platforms, Dune gives users direct access to decoded blockchain data, enabling custom analysis of any on-chain activity -- from LP fee tracking and [[impermanent-loss]] calculation to [[mev-strategies|MEV]] monitoring, whale tracking, and protocol-specific metrics.

## Key Features

### SQL-Based Querying
- **DuneSQL:** A custom SQL engine optimized for blockchain data. Users write queries against decoded smart contract event logs, transaction data, and token transfer tables
- **Decoded contracts:** Dune automatically decodes smart contract ABIs, making it possible to query protocol-specific events (e.g., Uniswap swaps, Aave liquidations) by human-readable column names
- **Cross-chain:** Supports Ethereum, Polygon, Arbitrum, Optimism, BNB Chain, Solana, Base, and other major chains

### Community Dashboards
- **30,000+ public dashboards** created by analysts, protocols, and researchers
- **Popular dashboards:** DEX volume trackers, stablecoin supply monitors, NFT marketplace comparisons, wallet profiling, [[liquidity-pool]] analytics
- **Forkable queries:** Any public query can be forked and modified, enabling rapid iteration on analysis

### Data Tables
- **Raw tables:** Blocks, transactions, logs, traces for each chain
- **Decoded tables:** Protocol-specific event tables (e.g., `uniswap_v3_ethereum.Pair_evt_Swap`)
- **Spell tables:** Community-maintained abstraction layers (e.g., `dex.trades` aggregates all DEX trades across protocols and chains)
- **Prices:** Token price feeds for calculating USD-denominated metrics

## Trading Relevance

- **Backtesting DeFi strategies:** Query historical LP returns, fee accumulation, and [[impermanent-loss]] for specific pools before deploying capital
- **Whale tracking:** Monitor large wallet movements, accumulation patterns, and protocol interactions. Dashboards tracking "smart money" wallets are among Dune's most popular
- **MEV analysis:** Query flashbots data, sandwich attack frequency, and arbitrage profits on specific pools to assess [[mev-strategies|MEV]] risk before providing liquidity
- **Protocol health monitoring:** Track real-time TVL changes, user counts, transaction volumes, and fee generation for protocols you are farming or investing in
- **Custom alerts:** Combine Dune queries with external notification services to create alerts for on-chain events (large withdrawals, liquidation cascades, depeg events)
- **Alpha generation:** Custom queries can surface patterns not visible in pre-packaged analytics -- e.g., identifying pools with rising fee revenue but declining TVL (higher yield per LP dollar)

## Pricing

Dune restructured its tiers in 2024-2025 to a credit-based model. As of June 2026 (verify on [dune.com/pricing](https://dune.com/pricing) — these change):

- **Free ($0):** ~2,500 query-execution credits/month, public queries and dashboards, browse/fork the community library, and basic API access. Materially more generous than the old free tier
- **Analyst (~$75/mo, ~$65/mo annual):** more credits, private queries and dashboards, CSV export
- **Plus (~$399/mo, ~$349/mo annual):** higher credit allotment, faster execution priority, larger result sets, fuller API quota
- **Enterprise (custom):** dedicated compute, private datasets, SLA guarantees

The old "Premium" tier has been retired and folded into the Analyst/Plus/Enterprise structure. Credits are consumed by query executions (datapoints scanned), so cost scales with how heavy your queries are rather than a flat seat fee.

## Limitations

- **SQL knowledge required:** Not accessible to non-technical users without learning SQL
- **Query execution time:** Complex queries on large datasets can take minutes to hours; free tier has execution limits
- **Data freshness:** Most tables update within minutes, but some decoded tables may lag during high-congestion periods
- **No real-time streaming:** Dune is for analytical queries, not real-time trading signals

## Related

- [[token-terminal]] -- pre-packaged protocol financial metrics (complementary to Dune's custom queries)
- [[zapper]] -- portfolio-level DeFi tracking and management
- [[defi]] -- the ecosystem Dune primarily analyzes
- [[crypto-data-sources]] -- broader catalog of crypto data providers
- [[mev-strategies]] -- MEV analysis is a key Dune use case
- [[impermanent-loss]] -- frequently analyzed using Dune queries

## Sources

- Dune pricing and credit-system documentation — https://dune.com/pricing, https://docs.dune.com/learning/how-tos/pricing-faqs (current tiers verified June 2026)
- Dune product documentation — platform features and data architecture (DuneSQL, spell tables, decoded contracts)
