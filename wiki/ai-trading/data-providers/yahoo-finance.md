---
title: "Yahoo Finance"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, stocks, free]
entity_type: company
website: https://finance.yahoo.com
related:
  - "[[alpha-vantage]]"
  - "[[tradingview-platform]]"
---

# Yahoo Finance

## Overview

The OG free data source for retail traders and quant beginners. Yahoo Finance provides delayed stock prices, fundamentals (5-year financials), options chains, earnings calendars, and news aggregation. The unofficial `yfinance` Python library has made it the default starting point for anyone learning [[algorithmic-trading]] or building a first trading bot. Despite being unofficial and occasionally breaking, it remains the most widely used free market data source in the Python ecosystem.

## Free Tier

- **Stock data**: delayed quotes (~15 min), daily/weekly/monthly OHLCV going back decades
- **Fundamentals**: income statements, balance sheets, cash flow (5 years), key ratios
- **Options chains**: basic options data with strikes, expiry, bid/ask
- **Earnings**: calendar, EPS estimates, earnings history
- **News**: aggregated financial news per ticker
- **Limits**: ~2,000 requests/hour via `yfinance` (unofficial, no API key required)
- **Coverage**: US stocks, some international, ETFs, mutual funds, indices, crypto

## Paid Tiers

Yahoo Finance does not offer a traditional paid API. The **Yahoo Finance Plus** subscription (~$25/mo) provides enhanced web features like advanced charts, research reports, and portfolio tools -- but no official API access. For programmatic access, most traders rely entirely on the free unofficial endpoints via `yfinance`.

## Alpha Edge

- Screen for value-investing opportunities using free fundamental data (P/E, P/B, debt ratios)
- Track earnings surprises and estimate revisions for momentum signals
- Build basic fundamental-analysis pipelines without spending a dollar
- Monitor options unusual activity for sentiment signals
- Backtest simple strategies using decades of daily price history

## API Details

- **Library**: `yfinance` (Python) -- `pip install yfinance`
- **Authentication**: none required
- **Rate limits**: ~2,000 req/hr (unofficial, may change without notice)
- **Data format**: returns pandas DataFrames natively
- **Gotchas**: unofficial API breaks periodically when Yahoo changes endpoints; no guaranteed uptime or support; adjusted vs. unadjusted price discrepancies

```python
import yfinance as yf
ticker = yf.Ticker("AAPL")
hist = ticker.history(period="1y")
financials = ticker.financials
options = ticker.option_chain("2026-04-17")
```

## Use Cases

- First data source for learning [[python-trading]] and quantitative analysis
- Quick fundamental screening across large stock universes
- Earnings calendar monitoring for [[event-driven-trading]]
- Portfolio tracking and historical performance analysis
- Feeding daily OHLCV into [[backtesting]] frameworks like [[backtrader]] or [[zipline]]
- Options chain analysis for basic volatility research
