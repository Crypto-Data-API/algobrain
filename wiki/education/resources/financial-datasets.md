---
title: Financial Datasets for ML Trading Models
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [education, data, machine-learning, tools]
related:
  - "[[python-quant-stack]]"
  - "[[kaggle-finance]]"
  - "[[backtesting-checklist]]"
---

# Financial Datasets — Where to Get Data for ML Trading Models

Data is the foundation of every AI trading system. The quality, granularity, and cleanliness of your data directly determines the ceiling of your model's performance. This page covers free, paid, and academic data sources along with critical pitfalls.

## Free Data Sources

**Yahoo Finance (via yfinance)** — Daily and intraday OHLCV for stocks, ETFs, indices, crypto, and forex. Fundamentals and options chains included. Good for learning and prototyping. Limitations: occasional data gaps, unreliable for production, rate-limited.

**Alpha Vantage** — Free API for stocks, forex, crypto, and economic indicators. 5 calls/minute on the free tier. Cleaner than Yahoo for intraday data. Good intermediate option.

**FRED (Federal Reserve Economic Data)** — Macroeconomic data: interest rates, GDP, unemployment, inflation, money supply. Essential for macro-based strategies and regime detection features. Completely free and highly reliable.

**CoinGecko / Binance API** — Crypto price data. CoinGecko covers 10,000+ tokens with historical daily data. Binance API provides tick-level data for listed pairs. Both free with rate limits.

**Kaggle Datasets** — Pre-packaged financial datasets ready for ML. Stock prices, options data, news sentiment, alternative data. No API setup required — download and start modeling. See [[kaggle-finance]].

## Paid Data Sources

**Polygon.io** — Real-time and historical US stock, options, forex, and crypto data. Tick-level granularity. Free tier available with delayed data. Paid plans from $29/month for real-time. The best balance of quality and cost.

**Quandl / Nasdaq Data Link** — Premium financial and alternative data. Includes proprietary datasets (satellite imagery, credit card transactions, sentiment). Some free datasets available. Industry standard for alternative data.

**Tiingo** — Stock and crypto data with a generous free tier. IEX real-time data, historical EOD, news feed. Good quality at a reasonable price ($10-30/month).

**EOD Historical Data** — Global stock coverage (70+ exchanges), fundamentals, and economic data. Affordable ($20/month) with good international coverage.

## Academic Data

**CRSP (Center for Research in Security Prices)** — The gold standard for US equity research data. Survivorship-bias-free. Available through WRDS (Wharton Research Data Services) at most universities.

**Compustat** — Fundamental financial data (income statements, balance sheets). Also via WRDS. Combined with CRSP, this powers most academic finance research.

## Crypto On-Chain Data

**Dune Analytics** — Query blockchain data with SQL. DEX volumes, wallet activity, protocol metrics. Free tier available. Essential for DeFi-related strategies.

**Flipside Crypto** — Curated on-chain datasets with bounties for analysis. Free access to cleaned blockchain data.

## Critical Data Pitfalls

- **Survivorship bias** — Datasets missing delisted stocks inflate backtest returns. Use [[backtesting-checklist]]
- **Split and dividend adjustments** — Unadjusted data creates phantom signals. Always use adjusted close prices
- **Timezone issues** — Mixing UTC and local timestamps causes look-ahead bias
- **Data snooping** — Testing many datasets until you find one that works is a form of overfitting
