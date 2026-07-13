---
title: "Custom Python Trading Bots"
type: concept
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [ai-trading, trading-bots, python, development]
related:
  - "[[bot-architecture]]"
  - "[[freqtrade]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[backtesting-pitfalls]]"
  - "[[backtrader-framework]]"
  - "[[book-python-for-algorithmic-trading]]"
---

# Custom Python Trading Bots

Building a trading bot from scratch in Python gives maximum flexibility but requires significant engineering effort. This is the approach used by serious independent traders and small quant teams who need capabilities beyond what [[freqtrade]] or [[three-commas|3Commas]] offer.

---

## Overview

Build custom when you need: unusual data sources, complex multi-asset strategies, specific execution logic, proprietary model integration, or non-standard venues (Source: [[book-python-for-algorithmic-trading]]). Total control in exchange for total responsibility, including [[bot-risks-and-pitfalls|every failure mode]].

---

## Architecture

The standard [[bot-architecture]] pipeline: **Data Feed** (REST/WebSocket) -> **Signal Generation** (indicators, models) -> **Risk Management** (sizing, limits) -> **Execution** (orders, fills, retries) -> **Logging** (audit trail). Choose event-driven (realistic) or vectorized (fast for [[backtesting-pitfalls|backtesting]]).

---

## Essential Libraries

| Library | Purpose |
|---|---|
| **CCXT** | Unified API for 100+ crypto exchanges |
| **pandas** / **numpy** | Data manipulation and numerical ops |
| **TA-Lib** / **pandas-ta** | Technical indicators |
| **websockets** / **aiohttp** | Real-time data streaming |
| **SQLAlchemy** | Trade history and state persistence |

---

## Critical Considerations

- **Error handling**: Wrap every API call in try/except with retries and exponential backoff
- **Rate limits**: Track usage, throttle requests to stay within exchange limits
- **API key security**: Environment variables or secrets manager -- never hardcode
- **Position tracking**: Reconcile local state with exchange state regularly
- **Crash recovery**: Persist state to database; resume from last known state on restart
- **Idempotency**: Duplicate signals must not create duplicate orders

Deploy with **Docker + cloud** (AWS/GCP, $5-50/mo) or VPS for reliability (Source: [[book-python-for-algorithmic-trading]]). Add health checks and [[bot-architecture|Telegram/Discord alerting]].

---

## Example

Minimal bot skeleton using CCXT:

```python
import ccxt, time
exchange = ccxt.binance({'apiKey': '...', 'secret': '...'})
while True:
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', '5m', limit=50)
    close = [c[4] for c in ohlcv]
    if close[-1] > sum(close[-20:]) / 20:
        exchange.create_market_buy_order('BTC/USDT', 0.001)
    time.sleep(300)
```

Intentionally naive -- a production bot needs everything in Critical Considerations above.

---

## Sources

- [[book-python-for-algorithmic-trading]] — comprehensive guide to the Python stack for algorithmic trading, including broker API integration, deployment architecture, and production-grade bot development

## See Also

- [[bot-architecture]] -- Detailed component design for trading bots
- [[freqtrade]] -- Framework that handles the boilerplate for you
- [[bot-risks-and-pitfalls]] -- What goes wrong with trading bots
- [[backtrader-framework]] -- Backtesting framework for validating strategies
- [[vectorbt]] -- Fast backtesting before going live
