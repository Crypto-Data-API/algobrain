---
title: "Data Providers"
type: index
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [data-provider, ai-trading, index]
aliases: ["Data Providers", "Data Provider Catalog"]
related: ["[[data-sources-overview]]", "[[alternative-data-alpha]]"]
---

# Data Providers

Market-data sources, APIs, and analytics vendors for trading systems. Good data is the single biggest determinant of model quality, so this section catalogs the major providers of price data, options analytics, on-chain data, alternative data, and institutional risk models — with their coverage, access tiers, and trading use-cases.

For a cost-tier walkthrough that maps the free-to-paid edge boundary by asset class and trading style, start with [[data-sources-overview]]. This page is the directory index for the individual provider write-ups.

## Start Here

- [[data-sources-overview]] — complete guide: which sources give alpha at each price tier, by asset class and trading style
- [[bloomberg-terminal]] — the institutional gold standard (~$2K/mo/seat); benchmark everything else against it
- [[fred]] — Federal Reserve Economic Data; 800K+ macro time series, free
- [[polygon-io]] — SIP-grade real-time stock + options API for quant/algo builds

## Providers by Category

### Equities, fundamentals & general market data
- [[yahoo-finance]] — free fundamentals, delayed quotes, options chains
- [[alpha-vantage]] — multi-asset REST API with a free tier
- [[finnhub]] — stocks/fundamentals/news API
- [[polygon-io]] — institutional-grade real-time + historical stock/options API
- [[eod-historical-data]] — broad historical EOD coverage at low cost
- [[barchart]] — futures/equities data and screeners
- [[algoseek]] — institutional tick/quote and order-book history
- [[tradingview-platform]] — best free multi-asset charting; Pine Script backtesting
- [[bloomberg-terminal]] — the full institutional stack

### Options analytics & volatility

### Institutional risk models (factor risk & optimization)

### Crypto, DeFi & on-chain
- [[coingecko]] — broad coin prices, market cap, volume
- [[coinglass]] — derivatives: funding, open interest, liquidations
- [[glassnode]] — Bitcoin/ETH on-chain metrics
- [[santiment]] — crypto sentiment + dev-activity signals
- [[laevitas]] — crypto options vol surface and basis analytics
- [[nansen]] — labelled wallets / smart-money tracking
- [[arkham-intelligence]] — cross-chain entity deanonymization
- [[dune-analytics]] — community SQL dashboards over on-chain data
- [[defilama]] / [[defillama]] — TVL, yields, stablecoin and bridge flows
- [[dex-screener]] — real-time DEX token prices and new pairs
- [[birdeye]] — Solana/multi-chain DEX analytics
- [[etherscan]] — Ethereum block explorer / raw chain data
- [[the-graph]] — indexed/queryable on-chain data via subgraphs

### Macro, sentiment & alternative data
- [[fred]] — macroeconomic time series (the macro gold standard)
- [[fear-and-greed-index]] — CNN (stocks) + Alternative.me (crypto) sentiment gauges

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/ai-trading/data-providers"
WHERE type != "index"
SORT updated DESC
```

## Related

- [[data-sources-overview]] — cost-tier guide and recommended stacks by trading style
- [[alternative-data-alpha]] — combining data sources for informational edge
