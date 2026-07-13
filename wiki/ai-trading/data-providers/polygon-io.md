---
title: "Polygon.io"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, stocks, options, api]
entity_type: company
website: https://polygon.io
related:
  - "[[alpha-vantage]]"
  - "[[yahoo-finance]]"
  - "[[bloomberg-terminal]]"
---

# Polygon.io

## Overview

Real-time and historical market data API built for developers and algo traders. Polygon.io provides institutional-quality data feeds -- SIP (consolidated tape) for equities and OPRA for options -- through clean, modern REST and WebSocket APIs. This is the data infrastructure layer: no charts, no dashboards, just raw data pipes designed to power trading systems, [[algorithmic-trading]] platforms, fintech apps, and quantitative research. Coverage spans US stocks, options, forex, and crypto with tick-level granularity.

## Pricing

- **Free**: 5 API calls/minute, delayed data, limited endpoints -- enough to prototype
- **Starter**: $99/mo -- real-time data, full REST API, basic WebSocket, aggregated bars
- **Developer**: $199/mo -- tick-level data, full options data, higher rate limits
- **Advanced**: $399/mo -- unlimited API calls, SIP/OPRA feeds, priority support
- **Enterprise**: custom pricing for co-location, dedicated feeds, and compliance-grade SLAs

## What You Get (vs Free)

- Real-time SIP data (consolidated from all US exchanges) instead of 15-minute delayed quotes
- Full OPRA options chain data: every strike, every expiry, greeks, IV, tick-by-tick
- Tick-level trade and quote data for granular market microstructure analysis
- WebSocket streaming for real-time feeds into live trading systems
- 20+ years of historical daily/minute/tick data for [[backtesting]]
- Reference data: ticker details, stock splits, dividends, market holidays, exchange metadata
- Snapshot endpoints for current state of entire market in a single call

## Alpha Edge

- **Institutional data at retail price**: SIP and OPRA feeds that would cost $10K+/mo from traditional vendors, available for $99-399/mo. This levels the playing field for independent algo traders
- **Tick-level options data**: full options chain with greeks and IV enables sophisticated volatility analysis, gamma exposure calculation, and options-based signals at a fraction of [[bloomberg-terminal]] cost
- **Speed**: WebSocket streaming with low-latency delivery -- not HFT-grade, but fast enough for most systematic strategies
- **Algo-friendly**: built API-first with consistent endpoints, good documentation, and client libraries in Python, JavaScript, Go, and Rust
- **Full market snapshots**: pull the entire US equity or options market state in one API call -- essential for screening and universe management

## Key Features

- **REST API**: clean endpoints for aggregates (bars), trades, quotes, snapshots, and reference data
- **WebSocket Streaming**: real-time trade and quote feeds for live trading systems
- **Options Data**: full OPRA chain with greeks, IV, and tick history -- rare at this price point
- **Flatfiles**: bulk historical data downloads for large-scale [[backtesting]] without API rate limits
- **Client Libraries**: official SDKs for Python, JavaScript, Go, Rust, Kotlin
- **Launchpad**: managed WebSocket infrastructure for fintech apps serving many end users

## Who Uses It

- Algo traders building systematic strategies who need reliable, fast data feeds
- Fintech startups (Robinhood historically used Polygon data) building consumer-facing apps
- Quantitative researchers needing tick-level historical data for academic or fund research
- Independent developers building trading bots, scanners, and analytics tools
- Options traders who need full chain data without a Bloomberg Terminal
- Anyone who has outgrown [[yahoo-finance]] and [[alpha-vantage]] but cannot justify Bloomberg pricing
