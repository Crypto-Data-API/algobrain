---
title: "Bullish Engulfing"
type: concept
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [technical-analysis, indicators]
aliases: ["Bullish Engulfing", "Bullish Engulfing Pattern", "bullish-engulfing-candle"]
domain: [technical-analysis]
prerequisites: ["[[candlestick-patterns]]"]
difficulty: beginner
related: ["[[candlestick-patterns]]", "[[technical-analysis]]", "[[bearish-engulfing]]", "[[support-and-resistance]]", "[[volume-analysis]]"]
---

A bullish engulfing is a two-candle reversal pattern in [[candlestick-patterns|candlestick charting]] where a large green (bullish) candle completely engulfs the body of the preceding red (bearish) candle. The pattern signals a shift in momentum from sellers to buyers: the first candle shows continued selling pressure, but the second candle opens below the prior close and rallies to close above the prior open, indicating that buyers have decisively overwhelmed sellers. The larger the second candle relative to the first, the stronger the signal.

The bullish engulfing pattern is most reliable when it appears at established [[support-and-resistance|support levels]], at the end of a defined downtrend, or after a series of declining candles. Context matters significantly -- a bullish engulfing occurring in the middle of a trading range carries far less predictive weight than one forming at a key support zone where buyers are expected to step in. Volume confirmation strengthens the signal: a bullish engulfing accompanied by above-average [[volume-analysis|volume]] on the second candle suggests genuine institutional participation rather than a thin-market anomaly. Without volume confirmation, many engulfing patterns fail to follow through.

Traders typically use the bullish engulfing as a trigger for long entries, placing a stop-loss below the low of the engulfing candle (the lowest point of the two-candle pattern). Targets are often set at the next resistance level or based on a risk-reward ratio of at least 2:1. The pattern appears on all timeframes, but daily and weekly engulfing patterns tend to produce more reliable signals than intraday ones, where noise is higher. The inverse pattern -- [[bearish-engulfing]] -- signals potential downside when a large red candle engulfs a prior green candle, typically at resistance levels. Both patterns are among the most widely studied candlestick formations in [[technical-analysis]], though they should always be used in conjunction with other indicators rather than in isolation.

## Trading Relevance

A bullish engulfing is a confirmation signal, not a forecast. Its practical value is that it marks a point where the order flow has visibly flipped: the second candle's open below the prior close, followed by a close above the prior open, means buyers absorbed all of the prior session's selling and then some. That gives a trader a defined invalidation level (the pattern low) and therefore a clean risk-reward setup. The edge, to the extent one exists, is behavioral -- short sellers covering and sidelined buyers stepping in simultaneously at a level where downside momentum has stalled. Empirical studies (e.g. Bulkowski) find the raw pattern has only a slight directional edge in isolation; the reliability comes almost entirely from location ([[support-and-resistance|support]], trend exhaustion) and [[volume-analysis|volume]] confirmation. Systematic traders rarely trade it alone, but use it as one input in a multi-factor entry filter.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=2` — the two most recent candles for a live pattern check
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio for confirmation

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV bars for pattern scans
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=2"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this pattern directly:

- **Compute** — two-bar logic over `GET /api/v1/market-data/klines`: prior candle closes red, current candle closes green with its body spanning the prior body (close ≥ prior open, open ≤ prior close)
- **Confirm** — check the engulfing bar's volume against the average from `GET /api/v1/market-data/volume-history` — the page's volume-confirmation rule, automated
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) supports hit-rate and expectancy studies with location filters (support proximity, trend context)
- **Tip** — crypto trades 24/7, so the "opens below prior close" gap element rarely occurs on continuous bars; most crypto implementations relax the condition to pure body-engulfment

## Sources

- Nison, Steve. *Japanese Candlestick Charting Techniques* (2nd ed., 2001) -- the canonical Western reference defining the engulfing pattern (tsutsumi) and its reversal context
- Bulkowski, Thomas N. *Encyclopedia of Candlestick Charts* (2008) -- statistical reliability and frequency data for the bullish engulfing across thousands of historical instances
- [[book-technical-analysis-of-the-financial-markets]] -- Murphy's treatment of candlestick reversal patterns within broader technical analysis
