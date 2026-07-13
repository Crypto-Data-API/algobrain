---
title: "Commodity Data Sources"
type: concept
created: 2026-04-14
updated: 2026-06-12
status: good
tags: [commodities, data-provider, futures]
aliases: ["Commodity Data Sources", "Commodity Data Providers"]
related: ["[[commodities]]", "[[macro-data-sources]]", "[[free-data-sources]]", "[[paid-data-providers]]", "[[eia-data]]", "[[usda-data]]", "[[cot-data]]", "[[commodity-free-tools]]", "[[commodity-seasonality-patterns]]"]
domain: [data-provider]
difficulty: beginner
---

A comprehensive guide to data sources for commodity research and trading, organized by access level and asset class. Commodity analysis requires supply/demand fundamentals, positioning data, price history, and real-time market data from multiple specialized providers.

## Government & Official Sources (Free)

These are the highest-quality, most widely followed commodity data sources -- all free and publicly available.

| Source | Coverage | Key Data | Frequency |
|--------|----------|----------|-----------|
| **[[eia|EIA]]** | Energy (oil, gas, coal, renewables) | Weekly petroleum stocks, natural gas storage, refinery inputs, crude production | Weekly/monthly |
| **[[usda|USDA]] ERS/FAS** | All agricultural commodities | WASDE reports, production, supply, distribution, export data; PSD database; API access | Monthly/weekly |
| **[[cftc|CFTC]]** | All US-traded futures | [[cot-report-analysis|COT reports]] -- weekly positioning data back to 1986 | Weekly (Friday) |
| **USGS** | Metals and minerals | Global supply, demand, and flow of minerals | Annual/quarterly |
| **World Bank** | All commodities | Worldwide prices ("Pink Sheet") and quarterly forecasts | Monthly |
| **FAO (FAOSTAT)** | Agriculture (global) | Statistical compilations on agricultural production and trade | Annual |
| **Eurostat** | European commodities | Detailed trade data for EU member states | Monthly |

## Exchange Data Sources

| Source | Coverage | Key Data |
|--------|----------|----------|
| **[[cme-group|CME Group]]** | Energy, metals, agriculture, livestock | Real-time and historical futures pricing, options data, COT data |
| **CBOT** | Agricultural commodities | Spot prices, futures, and forward prices (part of [[cme-group]]) |
| **[[london-metal-exchange|LME]]** | Base metals (copper, aluminium, nickel, zinc) | Global benchmark pricing and warehouse stock levels |
| **ICE** | Energy, softs (coffee, cocoa, cotton) | Brent crude, natural gas, soft commodity futures |

## Professional & Premium Platforms

| Platform | Specialization | Notes |
|----------|---------------|-------|
| **Bloomberg Terminal** | All asset classes | Industry standard; BCOM commodity index analytics |
| **Refinitiv Eikon (LSEG)** | All commodities | Comprehensive real-time data, news, and analytics |
| **S&P Global Platts** | Energy, metals, petrochemicals | Price benchmarks used in physical commodity contracts |
| **Wood Mackenzie** | Energy, metals, mining | Long-range supply/demand models, project-level analysis |
| **IEA** | Energy | Monthly Oil Market Report; medium-term outlook |
| **OPEC MOMR** | Crude oil | Production levels, demand forecasts, OECD inventory data |
| **Baker Hughes** | Oil & gas | Weekly US and international drilling rig count |

## Free/Accessible Tools for Independent Researchers

| Platform | Key Features | Cost |
|----------|-------------|------|
| **TradingView** | Charts, technical analysis, futures data | Free tier available |
| **Barchart.com** | Futures quotes, COT visualization, seasonal charts | Free + paid tiers |
| **Macrotrends.net** | Long-run historical commodity price charts (50+ years) | Free |
| **Quandl / NASDAQ Data Link** | Structured commodity data via API | Free (some datasets) |
| **Commodity Fundamentals API** | CFTC + EIA + USDA in one JSON endpoint | Paid; developer-friendly |
| **Vesper** | Agri-commodity pricing benchmarks (VPI) | Paid; strong for agriculture |
| **World Bank Pink Sheet** | Monthly price data across all commodity classes | Free |

## Data by Commodity Class

### Energy
- Primary: [[eia|EIA]] weekly reports (petroleum, natural gas, electricity)
- Secondary: OPEC MOMR, Baker Hughes rig count, IEA Oil Market Report
- See [[eia-data]] for detailed guide

### Agricultural
- Primary: [[usda|USDA]] WASDE, Crop Progress, Prospective Plantings
- Secondary: FAO, USDA FAS (international trade flows)
- See [[usda-data]] for detailed guide

### Metals
- Primary: [[london-metal-exchange|LME]] warehouse stocks, COMEX inventories
- Secondary: USGS mineral data, World Gold Council (for [[gold]])
- Shanghai Futures Exchange (SHFE) for Chinese metals pricing

### Positioning
- Primary: [[cftc|CFTC]] COT reports (legacy + disaggregated)
- See [[cot-data]] for detailed guide

## Building a Commodity Data Pipeline

For systematic traders, the key challenge is integrating data from multiple sources. The Commodity Fundamentals API aggregates CFTC, EIA, and USDA data through a single REST endpoint. For custom pipelines, most government sources offer free API access:

- EIA API: `api.eia.gov` (requires free key)
- USDA FAS: `apps.fas.usda.gov/OpenData` (free)
- CFTC COT: bulk CSV download from `cftc.gov`

## Related

- [[macro-data-sources]]
- [[free-data-sources]]
- [[paid-data-providers]]
- [[commodities]]

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
