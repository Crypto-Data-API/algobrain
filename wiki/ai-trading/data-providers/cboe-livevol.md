---
title: "Cboe LiveVol"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, volatility, derivatives, market-microstructure]
entity_type: company
founded: 2009
website: https://datashop.cboe.com
aliases: ["LiveVol", "LiveVol Pro", "Cboe DataShop"]
related:
  - "[[opra]]"
  - "[[optionmetrics]]"
  - "[[orats]]"
  - "[[databento]]"
  - "[[polygon-io]]"
  - "[[volatility-surface]]"
  - "[[volatility-skew]]"
---

# Cboe LiveVol

Cboe LiveVol is the options-data and analytics arm of [[cboe-global-markets|Cboe Global Markets]], the largest US options exchange operator. It provides historical and real-time options market data sourced directly from [[opra]] (the Options Price Reporting Authority consolidated tape), along with institutional-grade volatility analytics through the LiveVol Pro web platform. Distribution is now centralized through Cboe DataShop, and LiveVol products are widely used by hedge funds, proprietary trading desks, market makers, and academic researchers as the canonical reference for US options data.

## Overview

LiveVol was originally founded in 2009 as an independent options analytics firm and was acquired by Cboe in 2015. After the acquisition, the LiveVol product line was folded into Cboe's data business and is now sold under the Cboe LiveVol and Cboe DataShop brands. Because Cboe operates the four largest US options exchanges (Cboe Options, C2, BZX Options, EDGX Options), and because LiveVol receives the full [[opra]] feed, the data is considered authoritative for US-listed equity and index options.

LiveVol's positioning is institutional rather than retail: pricing, delivery formats, and tooling assume the user is a quant, a trading desk, or an academic with the infrastructure to handle large historical files and real-time tick streams. Solo traders typically work with derivative or value-added redistributors like [[orats]], [[optionmetrics]], or [[databento]] rather than going direct to LiveVol.

## Cboe DataShop Context

Cboe DataShop is the unified storefront for all Cboe-owned market data products, of which LiveVol is one segment alongside Cboe equities, futures (VIX, /VX), index, and FX data. From a buyer's perspective:

- LiveVol historical and analytical products are catalogued under DataShop's "Options" category
- Subscriptions and one-time purchases run through DataShop's commerce layer
- Real-time feeds are typically separate exchange-data subscriptions licensed under Cboe's market-data agreements rather than DataShop one-offs
- Academic licensing is available at reduced rates for research-only use

**Status as of June 2026:** LiveVol remains an active brand and platform within Cboe DataShop, listed alongside Cboe's other analytics platforms — Trade Alert (order-flow alerting, acquired 2020), Silexx (OEMS), and FT Options. Trending DataShop options products include the Cboe Open-Close Volume Summary, Enhanced US Options Trade-by-Trade Execution Detail, Option EOD Summary, Option Quotes, and Option Trades datasets, delivered via download, REST, and streaming APIs (datashop.cboe.com, verified 2026-06-10).

## Product Lines

### LiveVol Pro

Web-based options analytics platform aimed at active institutional traders.

- **Volatility surface visualizations**: full skew and term-structure across strikes and expiries, including historical playback to see how the surface has evolved
- **Order flow analytics**: large-print tracking, sweep detection, and customer-vs-firm breakdowns derived from the [[opra]] tape
- **Real-time Greeks and IV**: across all listed US equity, ETF, and index options
- **Strategy scanner**: filters for opportunities across spreads, calendars, and other multi-leg structures
- **Historical replay**: ability to step through past sessions for research or training

### Historical Options Data

The flagship dataset for backtesting and academic research.

- **Tick-level options trades and quotes**: from [[opra]], reaching back to roughly 2004 in deep history
- **End-of-day (EOD) options**: open, high, low, close, volume, open interest for every listed contract
- **Implied volatility and Greeks**: pre-computed using Cboe's model and the contemporaneous risk-free rate, dividend, and forward inputs
- **Open-Close volume data**: customer/firm/market-maker breakdowns of opening and closing transactions, useful for positioning analysis
- **Underlying reference data**: aligned equity and index pricing for clean backtests

Files are typically delivered as compressed CSVs via DataShop, with sizes that make a serious backtest a multi-terabyte exercise.

### EOD and Summary Products

Lower-cost daily summary feeds for users who do not need tick data: closing prices, IV, Greeks, open interest, and aggregated volume per contract per day.

## Strengths

- **Canonical data source**: as a Cboe-owned product receiving the full [[opra]] feed, LiveVol is the reference implementation against which other vendors are usually benchmarked
- **Deep history**: tick-level options data back to the mid-2000s covers multiple full volatility regimes including 2008, 2010 flash crash, 2015-2016, 2018 vol-mageddon, 2020 COVID, 2022 rates shock
- **Exchange-owned and audited**: data integrity processes meet exchange-grade standards, which matters for academic publication and regulatory work
- **Pre-computed analytics**: IV and Greeks are calculated and stored, saving users a non-trivial amount of pricing-engine work
- **Wide adoption**: results are easier to compare to existing literature and industry research because so many published studies use LiveVol or [[optionmetrics]] data

## Weaknesses

- **Cost**: institutional pricing runs from a few hundred to several thousand US dollars per month per product line; full historical tick coverage with real-time access is firmly in the five-to-six-figure annual range
- **Complexity for solo traders**: data volume, schema, and licensing make it impractical for a one-person shop without dedicated data engineering
- **Licensing constraints**: redistribution and derived-product creation are tightly controlled; the data cannot be embedded in commercial products without separate negotiation
- **Workflow tooling**: unlike [[orats]] or [[market-chameleon]], LiveVol does not optimize for a packaged "screener-to-trade-idea" workflow; users build their own pipelines
- **Less attractive for global coverage**: focus is US-listed options; international options data is patchier
- **Procurement friction**: enterprise sales cycle typical of exchange-owned data vendors, with paperwork and audit requirements that small firms find painful

## ITPM-Style Use Cases

For an [[itpm-playbook|ITPM-style]] options portfolio operating at institutional scale, LiveVol is one of the natural data backbones:

- **Volatility surface research**: build and validate proprietary volatility models using a clean, deep [[opra]]-sourced surface; identify systematic mispricings in [[volatility-skew|skew]] and term structure
- **Backtesting overlay strategies**: rigorous historical testing of covered-call, [[options-premium-selling|premium-selling]], collar, and risk-reversal programs against actual contemporaneous chains rather than synthetic Black-Scholes pricing
- **Skew analysis**: study the dynamics of the [[volatility-skew]] across regimes -- including periods of extreme skew (March 2020, January 2018) -- to inform tail-hedge sizing
- **Open-Close positioning**: use customer-vs-firm volume breakdowns to identify when retail or institutional positioning is extreme and likely to reverse
- **Earnings-cycle research**: measure how implied vs realized volatility evolves through historical earnings cycles to calibrate event-trading edges
- **Academic-grade citations**: when investor-relations or LP documents reference research, having LiveVol/[[opra]] as the data source raises the credibility of any backtest claim

For solo traders or small teams where the budget does not stretch to LiveVol direct, the practical alternative is a tiered stack: [[orats]] or [[optionmetrics]] for analytical depth, [[databento]] or [[polygon-io]] for cheaper [[opra]]-derived pricing, and Cboe DataShop only for the specific historical slices that require canonical data.

## Related

- [[opra]] -- the consolidated US options tape that LiveVol redistributes
- [[cboe-global-markets]] -- the parent exchange operator
- [[optionmetrics]] -- direct competitor on academic and institutional historical options data
- [[orats]] -- value-added analytics layer on similar underlying data
- [[databento]], [[polygon-io]] -- lower-cost OPRA redistributors targeting quant developers
- [[volatility-surface]], [[volatility-skew]] -- the primary research subjects LiveVol is used for
- [[options-premium-selling]] -- a strategy family that benefits heavily from LiveVol-quality historical chains for backtesting

## Sources

- Cboe DataShop product catalogue — https://datashop.cboe.com/
- LiveVol Pro platform page — https://datashop.cboe.com/livevol-pro
- Cboe press release, CBOE Holdings agreement to acquire LiveVol's market data and analytics business (August 2015) — ir.cboe.com archives
- Public academic papers using LiveVol historical data (replication studies, volatility research)
- Verified via web search, 2026-06-10 — LiveVol brand and DataShop distribution confirmed active; 2015 acquisition price was not disclosed in verifiable public sources
