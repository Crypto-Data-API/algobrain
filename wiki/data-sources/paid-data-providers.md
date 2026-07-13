---
title: "Paid Data Providers"
type: reference
created: 2026-04-10
updated: 2026-06-20
status: excellent
tags: [data, data-providers, paid]
aliases: ["Commercial Market Data", "Quant Data Vendors"]
related: ["[[data-sources-overview]]", "[[free-data-sources]]", "[[fundamental-data-sources]]", "[[options-data-sources]]", "[[crypto-data-sources]]", "[[historical-spread-data]]", "[[market-chameleon]]", "[[exchange-api-reference]]"]
---

# Paid Data Providers

Commercial vendors that supply data of sufficient quality for serious quantitative research. Each entry includes approximate price, what's covered, and known limitations. Pricing changes frequently — treat numbers as ballpark, not authoritative. This page is the paid-tier companion to [[free-data-sources]] and a sibling of [[fundamental-data-sources]], [[options-data-sources]], [[crypto-data-sources]], and [[historical-spread-data]]; see [[data-sources-overview]] for the full catalog.

> **Pricing disclaimer:** Every dollar figure on this page is a ballpark drawn from vendor pages and community reports circa 2024-2026. Vendors change plans, tiers, and per-product pricing frequently. Treat all numbers as order-of-magnitude only and confirm on the vendor's own site before committing budget. Nothing here is a quote.

## Quick-Reference Summary

The fastest way to read this page is the matrix below. It compresses every vendor into asset class, the price band, the single thing it is best at, and its sharpest limitation. Detailed entries follow.

| Provider | Primary asset class | Price band (approx/mo unless noted) | Best for | Sharpest limitation |
|---|---|---|---|---|
| **Polygon.io** | Equities, options, FX, crypto | ~$30-$2000+ | Default retail-quant API across asset classes | Some history starts ~2003-2004; universe caps on low tiers |
| **Norgate Data** | US/AU equities (EOD) | ~$30-$70 | Survivorship-free daily backtests | Daily-only; proprietary client; no REST API |
| **Databento** | US equities/options/futures (tick) | ~$50-$500 per product | Microstructure / depth-of-book history | Pay-per-product; US-focused |
| **CRSP** | US equities (1925+) | Free academic; ~$2K-$10K/yr | Decades-deep factor research | Daily/monthly only; redistribution-restricted |
| **Refinitiv** | Cross-asset + news + fundamentals | $5K-$50K+/seat | Institutional research desk | Expensive; institutional contracts only |
| **FactSet** | Fundamentals, ownership, M&A | Institutional | Point-in-time fundamentals + ownership | Expensive; institutional only |
| **Bloomberg Terminal** | Everything | ~$25K/yr/seat | Industry-standard terminal + BLP API | Most expensive; terminal lock-in |
| **CSI Data** | Futures (continuous) | ~$50-$200 | Properly-rolled continuous futures | Daily-only; proprietary client |
| **Tardis.dev** | Crypto (historical) | ~$59-$399 | L2/L3 orderbook + funding history | Historical only; no live feeds |
| **Kaiko** | Crypto (cross-venue) | $1K-$10K+ | Institutional multi-venue normalization | Expensive for individuals |
| **Glassnode** | On-chain (BTC/ETH/alts) | ~$30-$800 | Pre-computed on-chain metrics | Best metrics gated to high tiers |
| **OptionMetrics IvyDB** | Options (historical) | ~$10K-$50K+/yr | Academic-standard IV surfaces | Daily-only; no usable UI |
| **ORATS** | Options (IV surfaces) | ~$199-$999 | Retail-accessible fitted vol surfaces | US equities focus |
| **Sharadar** | Fundamentals (PIT) | ~$150 | Affordable point-in-time fundamentals | Narrower than Compustat |

See [[historical-spread-data]] for the spread/basis/funding-rate–specific breakdown of several of these same vendors, and [[market-chameleon]] for a retail-priced options-analytics layer that sits on top of OPRA data.

## Equities

### Polygon.io
Range: ~$30-$2000+/month depending on plan. Provides US and global stocks, options, forex, crypto, indices, news. WebSocket and REST APIs.

**Pros:** Modern API, full tick data on top tiers, OPRA options data, reasonable pricing for what you get, good documentation.

**Cons:** Some plans have universe restrictions; full historical depth requires higher tiers; not the absolute deepest history (some data starts only in 2003-2004).

**Best for:** Retail quant building intraday or daily strategies who needs real intraday fidelity without enterprise pricing. The default recommendation for most serious retail quant work as of 2024-2026.

### Norgate Data
Range: ~$30-$70/month for US/Australian markets. Specialty: survivorship-free EOD equity data with point-in-time index constituents going back decades.

**Pros:** **Survivorship-free out of the box**, point-in-time index membership, includes delisted securities, stock-level metadata, splits and dividends correctly handled. Extremely good data quality for the price.

**Cons:** Daily-only, US and Australia only, no real-time, requires their proprietary client (no REST API), Windows-friendly.

**Best for:** Anyone backtesting daily long/short equity strategies on the US who is currently using Yahoo. The single biggest data-quality upgrade you can make as a retail quant for under $100/month.

### Databento
Range: per-product, often $50-$500/month per data product. Specialty: nanosecond-precision tick data for US equities, options, futures, normalized across venues.

**Pros:** Direct exchange feeds, full depth-of-book history, normalized schema across venues, modern API.

**Cons:** Pay per product (can add up), focused on US market microstructure use cases.

**Best for:** Microstructure research, HFT prototyping, anything requiring tick-level depth.

### CRSP (Center for Research in Security Prices)
Range: free for academics, ~$2K-$10K/year for non-academic. The gold-standard US equity dataset since 1925.

**Pros:** Survivorship-free, point-in-time, deep history (1925+), very clean, the academic standard.

**Cons:** Daily and monthly only (not intraday), licensing is restrictive (no redistribution), institutional access required.

**Best for:** Academic-style factor research where you need decades of history. Often paired with Compustat for fundamentals.

### Refinitiv (formerly Thomson Reuters)
Range: institutional pricing, $5K-$50K+/month per seat. Full equity, fundamentals, news, FX, fixed income, alternative data.

**Pros:** Comprehensive, includes Refinitiv Eikon terminal, IBES analyst estimates, Lipper fund data, Reuters news.

**Cons:** Expensive, institutional contracts only, complex licensing.

**Best for:** Institutional research desks. Overkill for individuals.

### FactSet
Range: institutional, similar to Refinitiv. Strong on fundamentals, ownership data, M&A, ESG.

**Pros:** Excellent fundamentals point-in-time, deep ownership and analyst data, strong workflow integration.

**Cons:** Expensive, institutional only.

### Bloomberg Terminal
Range: ~$25K/year per seat. Everything: markets, news, analytics, messaging.

**Pros:** Industry-standard, comprehensive, real-time everything, the BLP API for programmatic access.

**Cons:** Most expensive option, locked to a physical terminal (or B-Unit), proprietary API.

**Best for:** Institutional desks where the terminal is the cost of doing business.

## Futures

### CSI Data
Range: ~$50-$200/month. Specialty: clean futures continuous contracts with multiple roll methods, historical depth.

**Pros:** Properly handled rolls (which most free sources get wrong), deep history.

**Cons:** Daily-only, requires proprietary client.

### Pinnacle Data
Range: ~$50-$200/month. Similar to CSI, futures specialty.

### CQG / Trading Technologies / Rithmic
Real-time and historical futures via direct exchange feeds. Used by intraday and HFT futures traders.

## Forex

### Dukascopy (Free Historical)
Free historical tick FX data going back to 2003 for many pairs. Quality is variable.

### TrueFX
Free tick-level historical FX from a consortium of liquidity providers. High quality.

### EBS / Refinitiv FXall
Institutional FX market data — interbank prices and trades. Expensive, professional only.

## Options

See [[options-data-sources]] for the full breakdown, [[market-chameleon]] for a retail-priced analytics layer over OPRA data, and [[historical-spread-data#Options Implied Volatility Surfaces]] for what a [[volatility-arbitrage]] backtest actually needs. Headlines:

- **OPRA via Polygon / Databento** — full US listed options tape
- **OptionMetrics IvyDB** — academic standard for historical options data with calculated greeks and IVs
- **ORATS** — daily and intraday IV surfaces, theoretical greeks
- **CBOE LiveVol** — direct from exchange

## Crypto

### Kaiko
Range: $1K-$10K+/month. Institutional crypto data — normalized trades, OHLCV, orderbook snapshots across 100+ venues.

**Pros:** Comprehensive cross-venue normalization, institutional-grade quality, includes derivatives.

**Cons:** Expensive for individuals; free exchange APIs are usually sufficient for personal research.

**Best for:** Funds running multi-venue crypto strategies who need a single source of truth.

### Tardis.dev
Range: ~$59-$399/month. Historical crypto market data including full orderbook, trades, derivatives funding, options chains across major venues. The default backtesting source for crypto spread, basis, and [[funding-rate-arbitrage|funding-rate]] research — see [[historical-spread-data]] for how its synchronized feeds avoid phantom-arb signals.

**Pros:** Affordable, deep historical depth, full L2/L3 orderbook history (extremely valuable), modern API.

**Cons:** Historical only — no live data feeds.

**Best for:** Microstructure research and backtest validation on crypto. The most cost-effective serious crypto data source as of 2024-2026.

### Amberdata
Range: institutional. Crypto market data plus on-chain analytics.

**Pros:** Combines market and on-chain data in one product.

**Cons:** Expensive.

### CryptoCompare / CoinAPI (Paid Tiers)
Range: $50-$1000/month. Aggregated crypto market data.

**Pros:** Easy to use, broad coverage.

**Cons:** Lower granularity than venue-direct sources.

## On-Chain Analytics

### Glassnode
Range: $30-$800/month. On-chain analytics for BTC, ETH, and many alts.

**Pros:** Pre-computed metrics (UTXO age, MVRV, SOPR, exchange flows), good charts, decent API.

**Cons:** Most useful metrics are on higher tiers.

### Nansen
Range: $150-$2000+/month. Wallet-level analytics and labels for ETH and L2s.

**Pros:** Wallet labels (smart money tracking), portfolio analytics, alerts.

**Cons:** Expensive for individuals.

### Dune Analytics
Range: free + paid tiers. SQL-based queryable blockchain data.

**Pros:** Extremely flexible (SQL on chain data), large community of pre-built dashboards.

**Cons:** Requires SQL skills, latency varies.

### Arkham Intelligence
Range: free + paid. Wallet labeling and entity tracking.

## Fundamentals (See Also [[fundamental-data-sources]])

- **Compustat (S&P)** — gold standard, point-in-time, institutional pricing
- **S&P Capital IQ** — broader than Compustat, includes private companies
- **Sharadar** ($150/mo) — affordable point-in-time fundamentals via Quandl/Nasdaq Data Link
- **Wisesheets / Stockanalysis.com / Simply Wall St** — retail-friendly aggregators

## News and Events

### RavenPack
Range: institutional. Real-time news entity tagging and sentiment scoring.

### Bloomberg Event Tags
Built into the terminal. Pre-tagged event types for systematic event-driven strategies.

### News API Aggregators (e.g., NewsCatcher)
Range: $50-$500/month. Aggregated news from many sources via REST.

## Buying Decision Framework

When choosing a paid provider, ask:

1. **What's the smallest dataset that solves my actual problem?** Don't pay for Bloomberg if Polygon's $99 plan is enough.
2. **Is the data point-in-time?** This is non-negotiable for serious research.
3. **What's the licensing?** Can you derive products from it? Share with collaborators? Build a paid SaaS on top?
4. **What's the support quality?** When data is wrong (it will be), can you actually reach a human?
5. **What's the lock-in?** Proprietary clients and APIs are friction; standard formats (CSV, Parquet, JSON over REST) are portable.
6. **What's the upgrade path?** Can you start cheap and grow without re-architecting?

A reasonable progression for a retail quant getting serious:

```
Year 1: Yahoo + FRED + free crypto APIs + SEC EDGAR (cost: $0)
Year 2: + Norgate or Polygon Starter ($30-$200/month)
Year 3: + Tardis for crypto, Sharadar for fundamentals ($500/month)
Year 4: + OptionMetrics or ORATS if doing options ($1K-$3K/month)
Year 5: institutional tier if running real money
```

## Access Mechanism by Provider

How you actually pull the data matters as much as what it covers. A REST/WebSocket or flat-file vendor drops into an automated pipeline; a proprietary-client or terminal-only vendor forces manual export or screen-scraping and resists [[ai-trading|automation]].

| Provider | Access method | Automation-friendly? | Portable formats |
|---|---|---|---|
| Polygon.io | REST + WebSocket | Yes | JSON, flat files |
| Databento | REST + streaming + flat files | Yes | DBN, CSV, Parquet |
| Tardis.dev | REST + flat-file download | Yes | CSV, JSON |
| Kaiko | REST + streaming + S3 | Yes | CSV, Parquet |
| Glassnode | REST API | Yes | JSON, CSV |
| Dune Analytics | SQL + API | Yes (SQL skills) | CSV, JSON |
| Sharadar | API (Nasdaq Data Link) | Yes | CSV, JSON |
| ORATS | REST API + flat files | Yes | CSV, JSON |
| OptionMetrics IvyDB | WRDS / flat-file delivery | Partial (batch) | CSV |
| Norgate Data | Proprietary client | No (client-bound) | Exports via client |
| CSI / Pinnacle | Proprietary client | No | Exports via client |
| Refinitiv | Eikon + API (entitlement-gated) | Partial | Proprietary + CSV |
| Bloomberg | Terminal + BLP API (B-Unit) | Partial (seat-bound) | Proprietary |

Portable, REST-or-flat-file vendors (Polygon, Databento, Tardis, Kaiko, Sharadar, ORATS) are the natural fit for systematic pipelines. Terminal- and client-bound vendors are perfectly good for human research but introduce friction and lock-in for automated workflows.

## How Trading and AI Systems Consume Paid Data

A serious quant or [[ai-trading|AI-driven]] system consumes paid data along a predictable pipeline, and the choice of vendor is mostly a function of where it sits in that pipeline:

1. **Backtest / research layer** — needs deep, *point-in-time*, survivorship-free history. This is where Norgate, CRSP, Compustat, Sharadar, OptionMetrics, and Tardis earn their keep. Getting this layer wrong (restated fundamentals, survivorship bias, mid-price fills) silently inflates every downstream result; see [[lookahead-bias]], [[survivorship-bias]], and [[backtesting]].
2. **Signal / feature layer** — pre-computed analytics that save reimplementation: Glassnode's on-chain metrics, ORATS' fitted surfaces, [[market-chameleon|Market Chameleon's]] earnings-vol statistics, RavenPack's news sentiment. AI/LLM feature stores increasingly ingest these directly.
3. **Live / execution layer** — needs low-latency, normalized real-time feeds: Polygon WebSockets, Databento streaming, Kaiko live, or direct exchange feeds (CQG/Rithmic for futures, [[exchange-api-reference|exchange APIs]] for crypto). Latency-sensitive strategies pay for venue-direct data; daily strategies do not.
4. **Cost / TCA layer** — realistic [[transaction-cost-modeling|transaction-cost modeling]] requires bid/ask depth, not mid. Databento depth-of-book and Tardis L2/L3 orderbooks feed slippage models; backtests on mid prices overstate fills by roughly half the spread.

For **LLM-based and agentic systems** specifically, the dominant consideration is *machine-readability and licensing*: REST/JSON and flat-file (CSV/Parquet) vendors drop straight into a retrieval or feature pipeline, whereas terminal- and proprietary-client vendors require human-in-the-loop export. Redistribution and derived-product clauses also matter more for AI products that surface data to end users — see the licensing question in the framework above.

## Data-Quality Caveats

Paid does not mean clean. Recurring failure modes to guard against, regardless of vendor:

- **Survivorship bias** — does the universe include delisted/failed securities? Norgate and CRSP are survivorship-free by design; many cheaper feeds are not. See [[survivorship-bias]].
- **Point-in-time vs restated** — fundamentals and index constituents must be as-of the backtest date, not the latest restatement. Compustat, FactSet, and Sharadar offer PIT; naive feeds bake in [[lookahead-bias]].
- **Roll handling for futures** — raw contract prices have roll gaps that create phantom signals. Use properly back-adjusted continuous contracts (CSI, Norgate). Detailed in [[historical-spread-data#Spread Construction from Futures]].
- **Mid vs bid/ask** — analytics and snapshot feeds often serve mid; backtesting fills on mid overstates profitability by ~half the spread. Pair with depth data for [[transaction-cost-modeling|realistic cost modeling]].
- **Predicted vs settled values** — crypto funding feeds may return the *predicted* next rate rather than the *settled* rate; use settled for backtesting (see [[historical-spread-data#Key Pitfalls]]).
- **Timestamp synchronization** — multi-leg / cross-venue work needs both legs timestamped to the same resolution; 1-second mismatches manufacture phantom arbs.
- **Corporate-action handling** — splits, dividends, and merger strike changes must be applied correctly, especially for options history.
- **Coverage gaps and start dates** — several "deep history" feeds actually start in the early 2000s; verify the true start date for your universe.
- **Vendor revisions** — historical data is sometimes silently revised. Snapshot and version your pulls if reproducibility matters.

## Sources

- [[book-quantitative-trading-ernest-chan]] — Chan on data vendors
- Vendor websites and pricing pages (subject to frequent change)
- General market knowledge and community reports (r/algotrading, quant forums) on vendor quality and pricing, circa 2024-2026

## Related

- [[data-sources-overview]]
- [[free-data-sources]]
- [[fundamental-data-sources]]
- [[options-data-sources]]
- [[crypto-data-sources]]
- [[historical-spread-data]]
- [[market-chameleon]]
- [[exchange-api-reference]]
- [[transaction-cost-modeling]]
- [[survivorship-bias]]
- [[lookahead-bias]]
- [[backtesting]]
- [[ai-trading]]
