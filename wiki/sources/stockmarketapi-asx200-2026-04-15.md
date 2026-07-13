---
title: "StockMarketAPI ASX 200 Company Data"
type: source
created: 2026-04-15
updated: 2026-04-15
status: good
tags: [stocks, asx200, australia, data-provider, meta]
source_type: data
source_url: "https://stockmarketapi.ai"
source_author: "StockMarketAPI"
source_date: 2026-04-15
confidence: high
claims_count: 193
---

Batch import of ASX 200 constituent company data from the StockMarketAPI, including company profiles, narrative descriptions, 5-year financial statements, valuation metrics, and ASX filing links.

## Data Points Extracted

- Company metadata: name, ticker, exchange, sector, industry, headquarters, employees
- Narrative profiles: business description, history, recent developments, leadership
- 5-year financials: revenue, gross profit, operating income, net income, total assets, equity, cash flows, EPS
- Valuation metrics: P/E, P/B, P/S, margins, ROE, ROA, debt/equity, current ratio
- ASX filings: annual and half-year reports with R2-stored PDF and markdown links

## Import Statistics

| Metric | Count |
|---|---|
| **Total companies processed** | 193 |
| **Pages created (new)** | 162 |
| **Pages merged (existing)** | 31 |
| **Pages skipped** | 0 |
| **Data source** | StockMarketAPI |
| **Confidence** | HIGH — official ASX market data |
| **Import date** | 2026-04-15 |

## Limitations

- Financial data is a point-in-time snapshot, not live
- ASX 200 composition changes quarterly — this reflects the index as of 2026-04-15
- Some companies report in USD (BHP, RIO, CSL, RMD) — check reporting_currency field
- ASX fiscal years typically end 30 June; FY2025 = year ended June 2025
- Profile narratives are sourced from public data and may lag recent events
