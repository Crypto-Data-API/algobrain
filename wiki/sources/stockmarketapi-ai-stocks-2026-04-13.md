---
title: "StockMarketAPI — AI Stocks Import (2026-04-13)"
type: source
created: 2026-04-13
updated: 2026-04-13
status: good
tags: [source, data, ai-trading, machine-learning, meta]
source_type: data
source_url: "https://stockmarketapi.ai"
source_author: "StockMarketAPI + AI Stocks Excel"
source_date: 2026-04-13
source_file: "r2://trader-wiki/data/2026-04-13-ai-stocks-not-sp500.xlsx"
confidence: high
claims_count: 150
---

Batch import of 150 AI-related stocks not listed on the S&P 500 index.

## Import Details

| Field | Value |
|---|---|
| **Date** | 2026-04-13 |
| **Total Tickers** | 150 |
| **Pages Created** | 141 |
| **Pages Merged** | 9 |
| **Data Sources** | StockMarketAPI (company details + metrics), curated Excel spreadsheet (AI categorisation) |
| **Confidence** | HIGH (market data), MEDIUM (AI categorisation) |

## Sector Breakdown

| Sector | Count |
|---|---|
| AI Software & Cloud | 34 |
| Other AI | 30 |
| Semiconductors & Chip Equipment | 19 |
| Healthcare & BioTech AI | 19 |
| Robotics & Automation | 11 |
| Cybersecurity | 7 |
| Defense & Government | 7 |
| Data Centers & Infrastructure | 7 |
| Fintech & Insurance AI | 6 |
| Autonomous Vehicles & Mobility | 5 |
| Quantum Computing | 4 |
| AI Voice & NLP | 4 |

## Market Cap Distribution

| Tier | Count |
|---|---|
| Large Cap (>$10B) | 15 |
| Mid Cap ($2B-$10B) | 51 |
| Small Cap ($300M-$2B) | 59 |
| Micro Cap (<$300M) | 25 |

## Methodology

1. Tickers sourced from curated Excel spreadsheet (StockAnalysis.com, Barchart, GreenStockNews, Morningstar)
2. Company details fetched via StockMarketAPI bulk endpoint
3. Financial metrics fetched per-ticker from StockMarketAPI
4. AI involvement descriptions from Excel used for categorisation and inline wikilinks
5. Cross-linked to existing wiki nodes (AI concepts, S&P 500 companies, sector pages)

## Related

- [[artificial-intelligence]]
- [[ai-trading-overview]]
- [[ai-stocks-overview]]
- [[s-and-p-500]]
