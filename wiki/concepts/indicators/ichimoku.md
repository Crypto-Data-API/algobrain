---
title: "Ichimoku Kinko Hyo"
type: concept
created: 2026-04-20
updated: 2026-07-19
status: good
tags: [indicators, technical-analysis, trend-following]
aliases: ["Ichimoku", "Ichimoku Cloud", "Ichimoku Kinko Hyo", "Kumo"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]", "[[moving-averages]]", "[[support-and-resistance]]"]
difficulty: advanced
related: ["[[goichi-hosoda]]", "[[ichimoku-cloud]]", "[[trend-following]]", "[[support-and-resistance]]", "[[momentum]]"]
---

Ichimoku Kinko Hyo ("one-glance equilibrium chart") is an all-in-one technical indicator that combines trend identification, momentum measurement, support/resistance levels, and time projection in a single visual framework. Developed by Japanese journalist [[goichi-hosoda|Goichi Hosoda]] (pen name "Ichimoku Sanjin") starting in the late 1930s and published in a 7-volume series beginning 1969 (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Components

Five components:

1. **Tenkan-sen** (Conversion Line) — 9-period midpoint (highest high + lowest low) / 2
2. **Kijun-sen** (Base Line) — 26-period midpoint
3. **Chikou Span** (Lagging Span) — current close plotted 26 periods back
4. **Senkou Span A** (Leading Span A) — midpoint of Tenkan + Kijun, plotted 26 periods ahead
5. **Senkou Span B** (Leading Span B) — 52-period midpoint, plotted 26 periods ahead

Senkou Span A and B form the **Kumo** (cloud), which acts as dynamic support/resistance (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Trading Relevance

Ichimoku's appeal is that it reads as a single picture: a trader can glance at the chart and assess trend, momentum, and [[support-and-resistance]] at once.

- **Trend** — price above the cloud is bullish, below is bearish, inside is neutral/indecisive. Cloud thickness signals trend conviction.
- **Momentum / signals** — the Tenkan/Kijun ("TK") cross is the primary trigger; it is higher quality when it occurs on the correct side of the cloud.
- **Forward S/R** — because Senkou A and B are plotted 26 periods ahead, the cloud projects future support/resistance zones, unique among common indicators.
- **Confirmation** — the Chikou (lagging) span checks that current price has cleared price from 26 periods ago.

As a [[trend-following]] tool it is designed to capture large directional moves rather than to win often; its edge is in risk/reward, not hit rate. For the full rule set, entries/exits, and an example trade, see the strategy page [[ichimoku-cloud]].

## Extended Theory

Hosoda paired Ichimoku with three additional theories:

- **Time Theory** — key cycle numbers (9, 17, 26) for timing turns
- **Wave Theory** — market moves classified by wave structure
- **Price (Target) Theory** — price projection calculations

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## Markets

Long dominant in Japanese equities and FX; spread globally only in the 1990s due to translation lag. Now widely used across forex, crypto (where 24/7 markets suit the indicator's multi-timeframe nature), and equities. Ichimoku is entrenched among Japanese FX desks (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study reported a 42.3% win rate for Ichimoku signals. While the win rate appears low, Ichimoku is a trend-following system designed to capture large moves — its value lies in favourable risk/reward ratios rather than high win rates (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

Note: For trading strategies using Ichimoku, see [[ichimoku-cloud]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — OHLCV highs/lows from which all five lines are computed
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=200` — the same construction on Hyperliquid perp listings

**Historical data:**
- `GET /api/v1/backtesting/klines` — full kline archive (Binance spot 1h/4h/1d back to 2017-08) for TK-cross and cloud-breakout backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — all five lines are midpoint functions of highs/lows from `GET /api/v1/market-data/klines`; fetch at least ~130 bars so Senkou Span B (52-period midpoint displaced 26 ahead) and the Chikou span are fully populated
- **Signal** — grade TK crosses by cloud position (above the Kumo = strong bull signal, inside = weak/neutral) exactly as described above; the cloud projects 26 bars forward from data already in hand, so no future bars are needed
- **Backtest** — replay over `GET /api/v1/backtesting/klines` (1h/4h/1d Binance spot back to 2017-08); expect trend-following economics — a sub-50% hit rate carried by large winners, so judge by expectancy, not win rate
- **Tip** — the Chikou span compares the current close to price 26 bars ago; in a backtest evaluate it only with data available at signal time — charting displacement conventions are a common source of accidental lookahead

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)

## Related

- [[goichi-hosoda]]
- [[ichimoku-cloud]]
- [[trend-following]]
- [[support-and-resistance]]
- [[momentum]]
