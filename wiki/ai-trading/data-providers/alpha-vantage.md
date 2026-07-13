---
title: "Alpha Vantage"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, stocks, crypto, forex, free]
entity_type: company
website: https://www.alphavantage.co
related:
  - "[[yahoo-finance]]"
  - "[[fred]]"
  - "[[tradingview-platform]]"
---

# Alpha Vantage

## Overview

Alpha Vantage is one of the best free starting points for quant traders who need clean, structured API access to stocks, forex, crypto, and macroeconomic data. Unlike [[yahoo-finance]] which relies on unofficial scraping, Alpha Vantage provides an actual documented API with consistent endpoints. It covers intraday and daily OHLCV, company fundamentals, earnings data, and over 50 technical indicators computed server-side. The free tier is restrictive on volume but the data quality and API design make it a strong foundation for building [[algorithmic-trading]] systems.

## Free Tier

- **Rate limit**: 25 requests/day (standard free key)
- **Coverage**: US stocks, forex pairs, crypto, economic indicators
- **Data types**: intraday (1/5/15/30/60 min), daily/weekly/monthly OHLCV
- **Fundamentals**: income statement, balance sheet, cash flow, earnings
- **Technical indicators**: SMA, EMA, RSI, MACD, Bollinger Bands, and 50+ more via API
- **Macro data**: GDP, CPI, inflation, federal funds rate, treasury yields

## Paid Tiers

| Plan | Price | Requests |
|------|-------|----------|
| Free | $0 | 25/day |
| Premium | $49/mo | 75 req/min |
| Premium+ | $99/mo | 150 req/min |
| Enterprise | $249/mo | 1,200 req/min |

Premium plans unlock higher rate limits and priority support. Data coverage is the same across all tiers -- you just get faster throughput.

## Alpha Edge

- Build complete [[algorithmic-trading]] strategies using a single clean API
- Server-side technical indicators eliminate local computation and potential errors
- Combine price data with fundamentals for multi-factor [[quantitative-trading]] models
- Cross-asset analysis: correlate stock moves with forex and crypto in one API
- Macro data overlay for [[regime-detection]] and interest rate sensitivity analysis

## API Details

- **Authentication**: free API key (register on website)
- **Format**: JSON and CSV responses
- **Python library**: `alpha_vantage` -- `pip install alpha-vantage`
- **Base URL**: `https://www.alphavantage.co/query`
- **Key parameters**: `function`, `symbol`, `interval`, `apikey`

```python
import requests
url = "https://www.alphavantage.co/query"
params = {"function": "TIME_SERIES_DAILY", "symbol": "AAPL", "apikey": "YOUR_KEY"}
data = requests.get(url, params=params).json()
```

## Use Cases

- Primary data source for learning [[quantitative-trading]] with a real API
- Building multi-asset strategy pipelines (stocks + forex + crypto)
- Technical indicator computation without local libraries
- Fundamental screening for [[value-investing]] signals
- Macro data ingestion for [[regime-detection]] models
- Feeding [[backtesting]] engines with clean historical OHLCV data
