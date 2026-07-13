---
title: "Bollinger Bands"
type: redirect
created: 2026-04-15
updated: 2026-07-13
status: good
tags: [indicators, technical-analysis, volatility]
aliases: ["Bollinger Bands", "BB"]
related: ["[[bollinger-bands]]", "[[cryptodataapi]]"]
---

See [[bollinger-bands]] (canonical page in `concepts/indicators/`).

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
