---
title: "Coinglass"
type: entity
created: 2026-04-06
updated: 2026-05-05
status: good
tags: [data-provider, crypto, derivatives, free]
entity_type: company
website: https://www.coinglass.com
related:
  - "[[coingecko]]"
  - "[[dex-screener]]"
  - "[[fear-and-greed-index]]"
  - "[[ai-agent-tokens]]"
  - "[[ai-trading-agents]]"
  - "[[liquidation-cascade-modeling]]"
  - "[[auto-deleveraging]]"
  - "[[2025-10-crypto-liquidation-cascade]]"
  - "[[crypto-perp-backtesting-pitfalls]]"
---

# Coinglass

## Overview

Coinglass is the go-to platform for crypto derivatives data. It aggregates funding rates, open interest, liquidation data, and long/short ratios across all major centralized exchanges (Binance, Bybit, OKX, etc.). The liquidation heatmaps -- showing price levels where leveraged positions will be forcibly closed -- are its signature feature. For anyone trading crypto perpetual futures or trying to understand market leverage, Coinglass provides essential data that is difficult to find elsewhere. Free web access covers most features; the API is a paid product.

## Free Tier

- **Funding rates**: real-time and historical across exchanges
- **Open interest**: aggregated and per-exchange, by coin
- **Liquidations**: real-time liquidation feed, 24h totals, historical
- **Long/short ratios**: trader sentiment across exchanges
- **Liquidation heatmaps**: visual maps of liquidation price clusters
- **Grayscale/ETF flows**: Bitcoin and Ethereum ETF flow data
- **Limits**: full web access is free; some advanced charts behind login

## Paid Tiers

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Full web access, basic features |
| Basic API | $59/mo | API access, historical data |
| Pro API | $199/mo | Higher limits, more endpoints |
| Enterprise | Custom | Full data access, dedicated support |

The free web version covers most trader needs. API plans are primarily for building automated systems that consume Coinglass data programmatically.

## Alpha Edge

- Predict [[liquidation]] cascades by identifying dense liquidation clusters on heatmaps
- [[funding-rate]] arbitrage: spot exchanges with extreme positive/negative funding
- Gauge market leverage via open interest relative to market cap
- Long/short ratio extremes as contrarian sentiment indicators
- Track exchange-level open interest divergences for flow analysis
- ETF flow data as a proxy for institutional sentiment on BTC/ETH

## API Details

- **Authentication**: API key (paid plans only)
- **Format**: JSON
- **Key endpoints**: `/api/futures/funding-rate`, `/api/futures/open-interest`, `/api/futures/liquidation`
- **Web scraping**: many traders scrape the free web version (against TOS but common)

```python
import requests
headers = {"coinglassSecret": "YOUR_API_KEY"}
# Get funding rates
funding = requests.get("https://open-api.coinglass.com/public/v2/funding",
                       headers=headers).json()
# Get open interest
oi = requests.get("https://open-api.coinglass.com/public/v2/open_interest",
                   headers=headers, params={"symbol": "BTC"}).json()
```

## Use Cases

- Monitoring leverage and liquidation risk for [[risk-management]] in crypto
- [[funding-rate]] arbitrage strategy development
- Liquidation cascade prediction for [[mean-reversion]] entries
- Derivatives sentiment overlay for spot trading decisions
- Combining with [[coingecko]] price data for comprehensive crypto analysis
- ETF flow tracking for macro crypto positioning

## Liquidation Cascade Data

Coinglass's most distinctive dataset is its **historical liquidation feed**, aggregated across the major centralized perp venues — Binance, Bybit, OKX, [[hyperliquid]], Bitget, dYdX — with per-trade granularity going back several years. For each forced close it captures: timestamp, exchange, symbol, side, size in USD, price, and (where exposed) the liquidation type (mark-price vs. ADL).

Sub-products built on this feed:

- **Liquidation heatmaps**: estimated cluster of stop and liquidation prices by leverage tier, derived from public OI distributions. Useful for identifying levels where a cascade is mechanically likely.
- **Funding-rate term-structure dashboards**: 8h, 1d, 7d, 30d annualised funding rates per exchange and per symbol, with cross-venue divergence views. The compression from a ~19% APY peak in 2024 to sub-4% by mid-2025 (post-[[2025-10-crypto-liquidation-cascade|October 2025 cascade]]) is fully visible in this dataset.
- **OI / funding heatmap composites**: overlay of open-interest concentration with funding extremes — flags the venues most exposed to a given crowding regime.
- **Long/Short ratio histories** per exchange and per account-class (top-trader, all-trader) — useful as a contrarian sentiment filter.
- **ETF flow reconciliation**: BTC/ETH ETF net-flow data alongside perp positioning, allowing cash-and-carry / basis backtests to use a single, time-aligned dataset.

For perp-strategy researchers this is the closest available public proxy for what a top-tier shop reconstructs from raw exchange feeds (Kaiko, Amberdata).

## Backtesting Use Cases

- **Stress-testing strategies against the Oct 10-11 2025 cascade**: replay the ~$20B liquidation event using the per-minute liquidation feed alongside mark-price data. Strategies whose [[crypto-perp-backtesting-pitfalls|backtests]] showed shallow drawdowns through this window almost certainly did not model the cascade correctly. See [[2025-10-crypto-liquidation-cascade]] and [[liquidation-cascade-modeling]].
- **Validating ADL exposure assumptions**: by cross-referencing the public liquidation feed with insurance-fund balance changes (also tracked by Coinglass on Binance/Bybit), a researcher can detect periods when [[auto-deleveraging|ADL]] events likely occurred — and then verify whether their backtest's "delta-neutral" basis trade survived. Most retail backtests assume liquidations only hit losing positions; ADL invalidates that assumption.
- **Modelling realistic liquidation triggers**: instead of using a fixed liquidation price computed from initial-margin formulas, calibrate to the empirical distribution of per-symbol liquidation prices — capturing the real interaction between mark-price methodology, funding flows, and dynamic margin tiers.
- **Funding-rate regime detection**: feed funding-rate term-structure series into [[market-regime-detection-ml|regime classifiers]]. The 2024-2025 compression episode is exactly the kind of regime shift that breaks naive [[funding-rate-arbitrage]] backtests.
- **Capacity calibration**: compare 24h liquidation totals and OI per venue to estimate the ceiling at which a strategy starts to *cause* the cascades it tries to exploit.
