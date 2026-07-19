---
title: "Backtesting"
type: redirect
created: 2026-04-06
updated: 2026-07-19
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

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run backtests over the archive directly:

- **Discover** — `GET /api/v1/backtesting/symbols` and `GET /api/v1/backtesting/archives-index` list what is available before designing a test
- **Fetch** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08; 1m only since 2026-03-30), `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30), `GET /api/v1/backtesting/liquidations` (Hyperliquid, since 2026-03-30)
- **Point-in-time** — replay `GET /api/v1/backtesting/daily-snapshots/{date}` (full `/daily` payload since 2026-03-02) so each simulated day sees only what a live system saw
- **Tip** — bulk research is faster over Parquet: `GET /api/v1/backtesting/archives/download` returns pre-signed URLs that load straight into pandas/DuckDB
