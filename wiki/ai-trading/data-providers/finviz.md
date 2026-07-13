---
title: "Finviz"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, stocks, free]
entity_type: company
website: https://finviz.com
related:
  - "[[yahoo-finance]]"
  - "[[tradingview-platform]]"
  - "[[alpha-vantage]]"
---

# Finviz

## Overview

Finviz (Financial Visualizations) is a powerful free stock screener and market visualization tool. Its signature feature is the sector heatmap -- a treemap showing every S&P 500 stock colored by daily performance -- which gives an instant visual read on market breadth and sector rotation. The screener supports extensive fundamental and technical filters, and the site also aggregates insider trading data, analyst ratings, futures, forex, and financial news. For stock traders who want fast, visual market intelligence without paying, Finviz is one of the best tools available.

## Free Tier

- **Stock screener**: filter by 60+ fundamental and technical criteria
- **Heatmaps**: S&P 500 sector/industry heatmaps (daily, weekly, monthly, YTD)
- **Stock pages**: charts, financials, analyst ratings, insider trading, news per ticker
- **Insider trading**: recent insider buys/sells across all stocks
- **Futures/forex**: major futures and forex pair quotes
- **News**: aggregated financial news headlines
- **Maps**: performance heatmaps by sector, industry, country
- **Limitations**: delayed data (15-20 min), limited screener results export, ads

## Paid Tiers

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Delayed data, basic screener, ads |
| Elite | $39.50/mo | Real-time data, premarket data, advanced screening, backtesting, email alerts, no ads |

Elite is a meaningful upgrade: real-time data, premarket quotes, advanced screener filters, and a backtesting tool make it a solid value for active stock traders.

## Alpha Edge

- Powerful free screening for [[value-investing]] (P/E, P/B, debt ratios, dividend yield)
- [[momentum-trading]] filters: RSI, moving average position, volume surge, gap up/down
- Sector heatmaps give instant market breadth reads -- see rotation in seconds
- Insider trading data as a signal for management confidence
- Analyst rating changes aggregated across tickers
- Futures overview for pre-market macro read (S&P, oil, gold, bonds)
- Combine Finviz screening with [[yahoo-finance]] deep-dives for a complete free workflow

## API Details

Finviz does not offer an official API. Data access options:

- **Web scraping**: commonly done with Python `finvizfinance` or `beautifulsoup4`
- **Python library**: `finvizfinance` -- `pip install finvizfinance`
- **Export**: Elite subscribers can export screener results to CSV
- **Note**: web scraping is against Finviz TOS; use at your own risk

```python
from finvizfinance.screener.overview import Overview
screener = Overview()
filters = {"Market Cap.": "Large ($10bln to $200bln)", "P/E": "Under 15"}
screener.set_filter(filters_dict=filters)
results = screener.screener_view()  # returns DataFrame
```

## Use Cases

- Daily market overview via sector heatmaps before the trading session
- Stock screening for [[value-investing]] and [[momentum-trading]] setups
- Insider trading analysis as a sentiment/conviction signal
- Quick fundamental lookup on individual tickers
- Pre-market preparation using futures and sector performance data
- Building stock universes for [[backtesting]] by exporting screener results
- Pairing with [[tradingview-platform]] for screening + charting workflow
