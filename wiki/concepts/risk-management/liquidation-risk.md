---
title: "Liquidation Risk"
type: redirect
created: 2026-04-15
updated: 2026-07-13
status: good
tags: [risk-management]
aliases: ["Liquidation Risk", "liquidation-risk"]
related: ["[[liquidation]]", "[[cryptodataapi]]"]
---

See [[liquidation]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (top coins)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, max pain
- `GET /api/v1/market-intelligence/etf/btc/aum` — BTC ETF total AUM
- `GET /api/v1/market-intelligence/exchange-balance` — exchange BTC balance + flow
- `GET /api/v1/market-intelligence/taker-buy-sell` — taker buy/sell ratio by exchange (4h window)

**Historical data:**
- `GET /api/v1/market-intelligence/etf/{asset}/flows` — BTC/ETH/SOL/XRP ETF flow history
- `GET /api/v1/market-intelligence/coinbase-premium` — Coinbase premium index history
- `GET /api/v1/market-intelligence/btc/cycle-indicators` — all 8 BTC cycle indicators, historical
- `GET /api/v1/backtesting/liquidations` — liquidation records archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]].
