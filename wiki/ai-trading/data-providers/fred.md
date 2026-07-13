---
title: "FRED (Federal Reserve Economic Data)"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, macroeconomics, free]
entity_type: company
website: https://fred.stlouisfed.org
related:
  - "[[alpha-vantage]]"
  - "[[fear-and-greed-index]]"
  - "[[finviz]]"
---

# FRED (Federal Reserve Economic Data)

## Overview

FRED is the gold standard for economic data, maintained by the Federal Reserve Bank of St. Louis. It provides free access to over 800,000 time series covering US and international economic indicators: GDP, CPI, unemployment, interest rates, money supply, yield curves, housing data, trade balances, and much more. For any trader or investor doing [[macro-analysis]], FRED is the authoritative, free, and reliable source. The data is clean, well-documented, and updated on official release schedules.

## Free Tier

Everything is free. FRED is a public service of the US Federal Reserve.

- **Coverage**: 800,000+ economic time series
- **Key series**: GDP, CPI, PCE, unemployment rate, federal funds rate, 10Y/2Y yields, M2 money supply, housing starts, ISM manufacturing
- **History**: decades of data, some series back to the 1940s+
- **API rate limit**: 120 requests/minute with free API key
- **Formats**: JSON, XML, CSV via API; Excel/CSV download via web
- **Updates**: data updated on official government release schedules

## Paid Tiers

There are no paid tiers. FRED is entirely free and publicly funded. This makes it one of the most valuable resources in the entire trading data ecosystem. No upsell, no freemium tricks -- just clean government data.

## Alpha Edge

- [[regime-detection]]: identify economic cycles (expansion, contraction) for asset allocation
- Yield curve analysis: 10Y-2Y spread as recession predictor
- Interest rate forecasting using Fed Funds futures vs. actual rate data
- Inflation nowcasting by combining CPI, PCE, and breakeven inflation rates
- Money supply (M2) trends for liquidity-driven market analysis
- Labor market analysis for consumer spending and earnings predictions
- Cross-country economic comparison for [[forex]] trading signals

## API Details

- **Authentication**: free API key (register at FRED website)
- **Base URL**: `https://api.stlouisfed.org/fred/`
- **Format**: JSON, XML
- **Python library**: `fredapi` -- `pip install fredapi`
- **Key endpoints**: `/series/observations`, `/series/search`, `/releases`

```python
from fredapi import Fred
fred = Fred(api_key="YOUR_API_KEY")
gdp = fred.get_series("GDP")
cpi = fred.get_series("CPIAUCSL")
yield_10y = fred.get_series("DGS10")
unemployment = fred.get_series("UNRATE")
```

## Use Cases

- Building [[macro-trading]] models that incorporate economic indicators
- Recession probability models using yield curve and labor data
- Inflation-adjusted asset performance analysis
- Interest rate sensitivity analysis for bond and equity portfolios
- Combining with [[alpha-vantage]] stock data for macro-informed equity strategies
- Economic calendar automation for [[event-driven-trading]]
- Academic research and quantitative finance coursework
