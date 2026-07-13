---
title: "Unusual Whales"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, options, stocks]
entity_type: company
website: https://unusualwhales.com
related:
  - "[[spotgamma]]"
  - "[[quiver-quant]]"
  - "[[options-trading]]"
---

# Unusual Whales

## Overview

Options flow scanner that tracks unusual options activity across the US equity market. The core premise: when someone buys $5 million in short-dated call options on a stock before a major catalyst, they might know something you do not. Unusual Whales surfaces these large, anomalous trades -- block orders, sweeps, dark pool prints -- and presents them in a real-time feed. Also famous for its Congressional trading tracker (the "Pelosi tracker"), which monitors stock trades disclosed by US lawmakers under the STOCK Act. Popularized heavily by options Twitter/FinTwit and retail traders during the 2020-2021 meme stock era.

## Pricing

- **Basic**: ~$50/mo -- options flow feed, basic filtering, delayed dark pool data
- **Premium**: ~$120/mo -- real-time flow, advanced filters, Congress tracker, sector flow, alerts
- **Platinum**: ~$200/mo -- full historical data, API access, institutional-grade analytics
- Free tier shows limited delayed data and basic features

## What You Get (vs Free)

- Real-time options flow feed with filtering by size, type (sweep, block, split), sentiment (bullish/bearish), sector, and expiry
- Dark pool prints: large block trades executed off-exchange that indicate institutional activity
- Congressional trading tracker: every stock trade reported by US senators and representatives
- Sector and ETF flow analysis showing where institutional money is rotating
- Alerts engine for custom criteria (e.g., notify when >$1M in calls hit on any pharma stock)
- Historical flow data for pattern analysis and [[backtesting]]

## Alpha Edge

- **Unusual activity precedes moves**: large, concentrated options bets -- especially sweeps that aggressively lift the ask -- often precede stock moves by 1-5 days. Not always insider trading, but informed money leaving footprints
- **Sweep vs. block distinction**: sweeps indicate urgency (hitting multiple exchanges simultaneously), which is more meaningful than passive block trades
- **Congressional alpha**: studies show that US lawmakers' stock trades have historically outperformed the S&P 500. Whether through policy insight or coincidence, tracking their trades has been a profitable strategy
- **Dark pool signals**: large dark pool prints at unusual sizes or frequencies can reveal institutional accumulation before public filings
- **Earnings season edge**: unusual call buying before earnings often signals informed expectations about beats

## Key Features

- **Flow Feed**: real-time stream of unusual options activity across all US equities
- **Congress Tracker**: searchable database of every trade by US lawmakers with historical performance
- **Dark Pool Dashboard**: off-exchange transaction monitoring with volume analysis
- **Sector Flow**: aggregate options flow by sector to identify rotation and sentiment shifts
- **Alerts**: custom notifications based on trade size, ticker, sector, or flow type
- **Mobile App**: monitor flow on the go with push notifications

## Who Uses It

- Retail options traders looking for trade ideas based on unusual activity
- Swing traders using options flow as a directional signal
- Political traders following Congressional stock picks
- FinTwit / options Twitter community (Unusual Whales has strong social media presence)
- Traders who want a second opinion -- if smart money is betting big in the same direction as your thesis, it adds conviction
- Anyone interested in [[alternative-data]] signals from options markets

Works best when combined with your own analysis. Flow data confirms or challenges a thesis -- it should not be your only signal. See [[spotgamma]] for understanding the structural impact of options positioning.
