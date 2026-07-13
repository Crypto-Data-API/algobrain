---
title: "Quiver Quantitative"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, alternative-data, stocks]
entity_type: company
website: https://www.quiverquant.com
related:
  - "[[unusual-whales]]"
  - "[[koyfin]]"
  - "[[yahoo-finance]]"
---

# Quiver Quantitative

## Overview

Alternative data platform aggregating non-traditional datasets that give traders an edge beyond standard price and fundamental data. Quiver Quant's flagship product is Congressional trading data (STOCK Act disclosures), but the platform covers a wide range of alternative signals: government contracts, lobbying expenditures, corporate insider trading (Form 4 filings), Reddit/WallStreetBets sentiment, patent filings, Wikipedia page traffic, and more. The thesis is simple -- follow the money and information flows that most traders ignore.

## Pricing

- **Free tier**: basic access to several datasets with limited history and delayed updates
- **Pro**: ~$50/mo -- full API access, real-time updates, complete historical data
- **Premium**: ~$200/mo -- advanced analytics, custom alerts, bulk data downloads, priority API
- API-first design makes it easy to integrate into quantitative workflows

## What You Get (vs Free)

- Full historical datasets going back years (free tier shows recent data only)
- Real-time updates when new STOCK Act filings, insider trades, or contract awards are published
- API access for programmatic data pulls into Python-based trading systems
- Custom alerts when specific lawmakers, insiders, or companies trigger activity
- Bulk data exports for large-scale [[backtesting]] and cross-referencing with price data
- Advanced filtering and screening across all alternative datasets

## Alpha Edge

- **Congressional trading**: US lawmakers' stock trades have historically outperformed the S&P 500 by meaningful margins. Whether through policy foresight, committee knowledge, or coincidence, tracking their trades has been a documented source of alpha. Quiver makes these STOCK Act filings immediately searchable and actionable
- **Insider buying signals**: corporate insiders (CEOs, CFOs, directors) buying their own stock is one of the most studied and validated signals in finance. Cluster buying -- multiple insiders buying simultaneously -- is even stronger
- **Government contracts**: companies winning large government contracts often see stock appreciation. Tracking contract awards in real time provides a lead over earnings reports
- **Lobbying as signal**: companies that increase lobbying spending in specific policy areas may be positioning for favorable regulation
- **Reddit/WSB sentiment**: meme stock momentum and retail sentiment tracking for short-term tactical trades

## Key Features

- **Congressional Dashboard**: searchable database of every stock trade by US senators and representatives
- **Insider Trading Tracker**: Form 4 filings with filtering by transaction type, insider role, and cluster activity
- **Government Contracts**: federal contract awards searchable by company, agency, and value
- **Lobbying Data**: corporate lobbying expenditures by company and policy area
- **Reddit/WSB Sentiment**: real-time tracking of ticker mentions and sentiment on WallStreetBets
- **API**: RESTful endpoints for all datasets, returning JSON for easy Python integration

## Who Uses It

- Retail traders building [[alternative-data]] strategies beyond traditional fundamentals
- Quantitative researchers testing insider and Congressional trading signals
- Political traders and policy-focused investors
- Journalists and researchers investigating conflicts of interest in Congress
- Algo traders incorporating non-price signals into systematic models
- Anyone who believes the most valuable data is the data most people are not looking at

Pairs well with [[unusual-whales]] (which also tracks Congress) for cross-referencing Congressional options activity with stock trades.
