---
title: "Moving Average"
type: redirect
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [indicators, technical-analysis]
aliases: ["moving-average", "Moving Average", "MA"]
related: ["[[moving-averages]]", "[[cryptodataapi]]"]
---

See [[moving-averages]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/indicators/technical` — price-structure state (SMA/BB/RSI) across assets
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN state

**Historical data:**
- `GET /api/v1/indicators/technical/{symbol}` — per-asset detail + 60d history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — raw OHLCV for computing your own

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/technical"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-indicators]].

**Live dashboards:** [technical structure](https://cryptodataapi.com/technical-structure) · [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — `GET /api/v1/indicators/technical` returns the SMA-based price-structure state for the whole universe in one call (Pro+); `GET /api/v1/market-data/btc-price-history` ships BTC's 200D MA precomputed
- **Compute** — any custom MA derives from `GET /api/v1/market-data/klines` closes (up to 1,000 bars per request)
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) for crossover and MA-filter studies
- **Tip** — see [[moving-averages]] for the full concept; this stub exists for the "MA" alias
