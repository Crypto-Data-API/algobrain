---
title: "AlgoSeek"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, futures, quantitative, backtesting]
entity_type: company
website: https://www.algoseek.com
founded: 2015
headquarters: "New York, USA"
aliases: ["AlgoSeek LLC", "Algoseek"]
related:
  - "[[polygon-io]]"
  - "[[quantconnect-bootcamp]]"
  - "[[backtesting]]"
  - "[[options-greeks]]"
---

# AlgoSeek

Institutional-grade historical market data vendor specializing in tick-level and minute-frequency datasets across US equities, options, and futures. AlgoSeek is best known among quantitative retail traders as the historical options data provider integrated into [[quantconnect-bootcamp|QuantConnect]], where it supplies minute-bar options data covering 4,000+ underlying symbols since January 2012, sourced from OPRA. For QuantConnect users, this eliminates the need to license and process raw OPRA feeds independently -- one of the most expensive and operationally heavy steps in options research.

## Overview

AlgoSeek (operating as AlgoSeek LLC) is a New York-based market data company that captures, cleans, normalizes, and redistributes historical and intraday market data. Per the company's own history, its roots go back to around 2000, when a trader and two developers built a proprietary ticker plant for an internal trading fund; the data business was spun off from the fund and launched its first commercial dataset in 2015. As of 2026 the company positions itself as a "data infrastructure provider," and its founding team claims 140 years of collective data/algo-trading experience with over 60% of the R&D team holding PhDs (per algoseek.com and Tracxn, June 2026).

Its product lineup spans:

- **US options**: trades and quotes, minute-bar aggregates, end-of-day chains -- full OPRA universe
- **US equities**: tick-by-tick TAQ-style data and minute bars
- **US futures**: CME and ICE tick data and aggregates
- **Reference and corporate actions**: symbology, splits, dividends, expirations, exercise/assignment data
- **Alternative datasets**: company-specific feeds and curated research bundles
- **Real-time data (added by 2025-2026)**: professional and academic real-time market data services delivered via RESTful API and WebSocket — a shift from the company's historical-only origins
- **Infrastructure products**: ArdaDB, a cloud database built on open-source ClickHouse for hosting and querying large market datasets, plus ticker-plant and co-location services

The company's operational focus is on producing point-in-time, survivorship-bias-free, corporate-action-adjusted data suitable for backtesting and research. This contrasts with simpler price feeds where adjustments and delistings can silently bias historical results.

## Pricing

AlgoSeek does not publish full retail pricing on its public website -- most products are sold via enterprise quotes. Approximate ballpark figures discussed publicly:

- **Direct historical options data licenses**: typically thousands to tens of thousands of dollars per dataset, depending on scope and history depth
- **QuantConnect integration (indirect access)**: included in QuantConnect's paid tiers (starting around $20-50/mo for individual researchers); options data costs are bundled rather than billed per file
- **Tick-level equities/futures**: priced per-symbol-year or as full-universe licenses
- **Academic discounts** are available for some datasets

For most retail quants, the QuantConnect integration is the cheapest practical access to AlgoSeek options history, since direct licensing is structured for institutional buyers.

## What You Get / Key Features

- **Options minute bars**: OHLC, volume, and open interest per contract per minute, on every listed US options symbol since January 2012
- **Strike, expiry, and chain reconstruction**: full options chain at any point in history, including delisted contracts and expired strikes
- **OPRA-sourced**: covers all 17+ US options exchanges
- **Corporate action handling**: splits, special dividends, mergers, ticker changes applied consistently across the dataset
- **Tick-level options and equities**: every quote and trade, for users who need sub-minute resolution
- **Greeks and IV (where licensed)**: derived analytics computed from underlying and option prices
- **Point-in-time integrity**: data is timestamped and not silently revised, a critical property for [[backtesting|valid backtests]]

## Use Cases / Who Uses It

- Quantitative researchers backtesting options strategies (vol selling, delta-neutral, calendar spreads, [[0dte-trading|0DTE]] systems)
- [[quantconnect-bootcamp|QuantConnect]] users running options research on the Lean engine -- the most common retail entry point
- Academic finance researchers studying volatility surfaces, anomalies, and market microstructure
- Hedge funds and prop firms needing OPRA-quality history without building their own capture infrastructure
- Algo developers validating execution logic at the tick level on equities and futures
- Anyone who needs survivorship-bias-free historical chains -- a known weakness of cheaper data sources

## Strengths and Limitations

**Strengths**

- Direct OPRA capture with rigorous cleaning and corporate action handling
- Deep history (2012+ on options, longer on equities/futures)
- Tight integration with [[quantconnect-bootcamp|QuantConnect]] making it the de facto retail-quant options dataset
- Wide product range -- one vendor for equities, options, and futures
- Point-in-time discipline suited to honest backtesting

**Limitations**

- Direct licensing is expensive and oriented toward institutional buyers
- Real-time access is a newer offering (REST/WebSocket feeds now exist, including academic tiers) but is still less retail-established than [[polygon-io]] or broker APIs; many users continue to pair AlgoSeek history with a separate live feed
- Outside the QuantConnect platform, integration requires meaningful engineering work (large datasets, parquet/CSV ingestion)
- Minute resolution is coarse for some intraday options strategies -- tick data exists but at higher cost
- Documentation and support primarily target enterprise customers

## Related

- [[quantconnect-bootcamp]] -- primary retail integration path for AlgoSeek options data
- [[polygon-io]] -- alternative options data API, more retail-friendly real-time but shorter history depth
- [[backtesting]]
- [[options-greeks]]

## Sources

- AlgoSeek corporate site and company history — https://algoseek.com/company
- AlgoSeek data catalog (equities, futures, options) — https://algoseek.com/data-sets/list
- QuantConnect AlgoSeek US Equities dataset page — https://www.quantconnect.com/datasets/algoseek-us-equities
- Tracxn company profile, AlgoSeek (2026) — https://tracxn.com/d/companies/algoseek/
- Verified via Perplexity (sonar) and web search, 2026-06-10; no acquisition or ownership change found 2024-2026, company actively operating
