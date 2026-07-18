---
title: "Market Cap"
type: redirect
created: 2026-07-01
updated: 2026-07-13
status: good
tags: [valuation]
aliases: ["Market Cap", "market-cap", "Mkt Cap"]
related: ["[[market-capitalization]]", "[[cryptodataapi]]"]
---

See [[market-capitalization]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC history + 200D MA
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].
