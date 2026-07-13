---
title: "Data Sources"
type: overview
created: 2026-04-10
updated: 2026-04-20
status: good
tags: [data, data-providers, infrastructure]
aliases: ["Market Data", "Data Providers", "Data Feeds", "data-providers"]
related: ["[[free-data-sources]]", "[[paid-data-providers]]", "[[alternative-data-providers]]", "[[crypto-data-sources]]", "[[transaction-cost-modeling]]", "[[backtesting-overview]]", "[[fundamental-analysis-overview]]"]
---

# Data Sources

A catalog of where to get the data needed to research and run trading strategies. Data quality is the single largest determinant of whether a backtest is honest. Most "great" backtests are built on data that has subtle survivorship, lookahead, or selection bias — and replacing the data source often kills the strategy.

This section lists the main providers by category, their strengths and weaknesses, approximate cost, and which kinds of strategies they enable. Cross-referenced from individual strategy pages via the `data_required` frontmatter field.

## Quick Decision Tree

**I'm doing personal-account research with no budget:**
- Equities: Yahoo Finance (with caveats), Alpha Vantage, IEX Cloud free tier
- Crypto: exchange public APIs (Binance, Coinbase, Kraken)
- Macro: FRED (with revision caveats — see [[lookahead-bias]])
- Fundamentals: SEC EDGAR direct (free, painful)

**I'm building a serious quant strategy on equities:**
- Polygon.io ($199-$499/month) for daily and minute data
- Norgate Data for survivorship-free historical
- CRSP/Compustat (academic licensing) or QuantConnect's bundled data
- Refinitiv or FactSet for fundamentals point-in-time

**I'm trading ITPM-style discretionary options (ratio calendar spreads):**
- A broker platform (TradeStation, IBKR, ThinkOrSwim) provides everything needed for live trading — chains, IV, greeks, P&L modeling
- Free macro: FRED + ForexFactory. Free fundamentals: Yahoo Finance + Earnings Whispers + OpenInsider
- Add ORATS ($199/mo) only if you want historical IV surfaces for research
- See [[itpm-ratio-calendar-spread#Data Sources & Infrastructure]] for the complete stack

**I'm building arbitrage strategies across multiple venues:**
- [[exchange-api-reference]] for normalized API endpoints, WebSocket feeds, rate limits
- [[historical-spread-data]] for funding rate, basis, and cross-exchange spread time series
- Exchange APIs + Tardis.dev for synchronized multi-venue order book data

**I'm building HFT or microstructure strategies:**
- Databento (per-data-product pricing)
- Polygon's full tick data
- Direct exchange feeds (most expensive — $5K-$50K+/month per venue)

**I'm building alternative-data alpha:**
- Specific vendors per data type — see [[alternative-data-providers]]

**I'm trading crypto:**
- Exchange APIs are usually sufficient and free
- Kaiko, Amberdata, Tardis.dev for normalized historical
- See [[crypto-data-sources]]

## Sub-Pages

- [[free-data-sources]] — Yahoo, FRED, Alpha Vantage, exchange APIs
- [[paid-data-providers]] — Polygon, Databento, Norgate, Refinitiv, FactSet
- [[alternative-data-providers]] — satellite, credit card, web scraping
- [[crypto-data-sources]] — exchange APIs, Kaiko, on-chain analytics
- [[macro-data-sources]] — FRED, ALFRED, BEA, BLS, central banks
- [[news-and-sentiment-sources]] — RavenPack, Bloomberg event tags
- [[exchange-api-reference]] — Normalized API endpoints for arbitrage (Binance, Coinbase, Hyperliquid, OKX, Bybit, Kraken)
- [[historical-spread-data]] — Funding rates, basis, cross-exchange spreads, IV surfaces for arb backtesting

## Commodity Data

Commodity markets have their own data ecosystem, distinct from equities/crypto:

- [[commodity-data-sources]] — Comprehensive catalog of commodity-specific data providers (exchange data, government reports, commercial analytics, satellite/alt data)
- [[eia-data]] — US Energy Information Administration: weekly petroleum status, natural gas storage, Short-Term Energy Outlook, Drilling Productivity Report, API access
- [[usda-data]] — US Department of Agriculture: WASDE supply/demand estimates, Prospective Plantings, Crop Progress, Grain Stocks, export inspections, FAS global data
- [[cot-data]] — CFTC Commitments of Traders reports: commercial hedger and managed money positioning across all US futures markets (see also [[commercial-hedger-positioning]], [[speculative-positioning]])
- [[commodity-free-tools]] — Free tools for commodity analysis: TradingView commodity charts, Barchart seasonal tools, Macrotrends historical prices, NOAA weather data, FRED commodity series

## Quality Dimensions

When evaluating any data source, ask:

1. **Is it point-in-time?** Does each observation reflect what was *knowable* at that historical moment, or has it been updated since?
2. **Is it survivorship-free?** Are delisted, bankrupt, and merged instruments included?
3. **What's the latency?** How quickly is new data published after the underlying event?
4. **What's the granularity?** Daily, minute, second, tick?
5. **What's the depth?** How far back does the history go?
6. **What's the universe coverage?** How many instruments / countries / asset classes?
7. **Is there a quality SLA?** What happens when there are gaps, errors, or corrections?
8. **What's the licensing?** Can you redistribute, derive products, share with partners?
9. **What's the cost structure?** Flat, per-symbol, per-API-call, per-MB?

A "free" source that requires 80 hours of cleaning is more expensive than a $500/month source that's clean. A "cheap" source with hidden survivorship bias produces strategies that fail in production — also expensive.

## Cost Tiers (Equities Daily Data, US)

| Tier | Cost | Examples | What you get |
|---|---|---|---|
| Free | $0 | Yahoo, IEX free, Alpha Vantage free | Basic OHLCV, survivorship-biased universe, occasional gaps |
| Hobbyist | $20-$50/mo | Alpha Vantage paid, Tiingo, EOD Historical Data | Cleaner OHLCV, some fundamentals, limited intraday |
| Serious retail | $100-$500/mo | Polygon Starter, Norgate, IBKR data | Survivorship-free, point-in-time, intraday |
| Pro | $500-$5K/mo | Polygon higher tiers, FactSet light, Refinitiv Eikon | Full intraday, fundamentals point-in-time, alt data bundles |
| Institutional | $5K-$50K+/mo | Bloomberg Terminal, full FactSet, Refinitiv, direct exchange | Everything plus terminal, alt data, deep history |

## Data You Probably Don't Have That You Need

Even paid retail data sources usually lack:

1. **Point-in-time index constituents** — most sources give current S&P 500 membership only
2. **Point-in-time fundamentals** — most give the latest restated version
3. **Survivorship-free delisted history** — most filter to currently-listed instruments
4. **Historical splits and dividends adjustments applied correctly** — many providers introduce subtle errors
5. **Corporate action history** — mergers, spinoffs, ticker changes, stock dividends
6. **Borrow rates and short interest history**
7. **Options chain history with implied vol surfaces**
8. **Tick-level orderbook snapshots beyond 1-2 years**

If your strategy depends on any of these and your data source doesn't provide them, you cannot honestly backtest the strategy.

## Building Your Own Data Lake

For serious research, most quants end up building a local data lake:

1. **Storage:** Parquet or Arrow on S3/R2/local SSD
2. **Format:** point-in-time, partitioned by date and symbol
3. **Pipeline:** scripts to fetch from multiple providers, normalize, deduplicate, version
4. **Access layer:** DuckDB or pandas for ad-hoc, Spark for scale
5. **Vintage tracking:** keep snapshots of data as it was on each date you fetched it

This is 1-3 months of engineering work but pays back many times over in research velocity and data integrity.

## Sources

- [[book-quantitative-trading-ernest-chan]] — Chan on practical data sourcing for retail quants
- [[book-advances-in-financial-machine-learning]] — López de Prado on data integrity and point-in-time

## Related

- [[backtesting-overview]]
- [[lookahead-bias]]
- [[survivorship-bias]]
- [[transaction-cost-modeling]]
- [[strategy-development-overview]]
