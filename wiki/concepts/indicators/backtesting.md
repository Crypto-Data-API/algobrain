---
title: "Backtesting"
type: redirect
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [backtesting, quantitative]
aliases: ["Backtesting", "backtest"]
related: ["[[backtesting-overview]]", "[[cryptodataapi]]"]
---

See [[backtesting-overview]].

## Getting the Data (CryptoDataAPI)

**Historical archive:**
- `GET /api/v1/backtesting/klines` — OHLCV candle archive
- `GET /api/v1/backtesting/funding` — funding-rate archive
- `GET /api/v1/backtesting/liquidations` — liquidation records archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshot
- `GET /api/v1/backtesting/archives` — Parquet dataset archive (since 2020)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/symbols"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-backtesting]].
