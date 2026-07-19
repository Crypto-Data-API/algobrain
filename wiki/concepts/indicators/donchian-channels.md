---
title: "Donchian Channels"
type: concept
created: 2026-04-20
updated: 2026-07-19
status: excellent
tags: [indicators, technical-analysis, volatility, breakout, trend-following]
aliases: ["Donchian Channel", "Donchian", "Donchian Channels"]
prerequisites: ["[[indicators-ta-primer]]"]
domain: [indicators]
difficulty: beginner
related: ["[[richard-donchian]]", "[[donchian-channel-breakout]]", "[[turtle-trading]]", "[[turtle-traders]]", "[[atr]]", "[[average-true-range]]", "[[keltner-channels]]", "[[bollinger-bands]]", "[[breakout]]", "[[consolidation]]", "[[support]]", "[[resistance]]", "[[trend-following]]", "[[trailing-stop]]"]
---

Donchian Channels plot the highest high and lowest low over the last N periods, creating a price envelope that identifies breakout levels. Created by [[richard-donchian|Richard Donchian]] in the 1950s–1960s, often called the "father of trend following" (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## How It Works

The channel is computed entirely from raw price extremes over a lookback of N periods:

```
Upper band  = highest high of the last N periods   (rolling resistance)
Lower band  = lowest  low  of the last N periods   (rolling support)
Middle band = (Upper band + Lower band) / 2        (mean / equilibrium)
```

- **Upper band** acts as a moving [[resistance]] line and the long-breakout trigger.
- **Lower band** acts as a moving [[support]] line and the short-breakout (or long-exit) trigger.
- **Middle band** is sometimes used as a trend filter or a [[trailing-stop|trailing exit]] reference.

Default period is 20 for short-term or 55 for long-term breakouts. A breakout above the upper band signals a potential long entry; a break below the lower band signals a potential short (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

> Important quirk: by construction, on the bar that price makes a new N-period high, *price equals the upper band* — so a literal "close above the upper band" only happens versus the band's value as of the **prior** bar. Most implementations test against the highest high of the previous N bars (excluding today) to generate a clean signal.

### Worked Example

Take a 20-day channel. Over the last 20 sessions a stock's highest high was **$52.00** and its lowest low was **$44.00**.

- Upper band = **$52.00**, Lower band = **$44.00**, Middle = **$48.00**.
- Channel height = $52 − $44 = **$8** — a usable proxy for recent [[volatility]] and a [[consolidation]] range.
- Price closes at **$52.40**, a new 20-day high → **long-breakout** signal. A [[turtle-traders|Turtle-style]] trader sizes the position so that 1× [[average-true-range|ATR (N)]] of adverse move equals a fixed fraction of equity, and trails the exit at the opposite (e.g. 10-day) lower band.
- If price had instead broken **below $44**, that would be a short signal (or, for a long held from an earlier entry, the stop-and-reverse exit).

## Parameter Choice

| Lookback (N) | Character | Typical use |
|--------------|-----------|-------------|
| 10 | Fast, noisy | Short-term exits (Turtle System exit used the opposite 10-day band) |
| 20 | Balanced | Turtle **System 1** entry; classic short-term breakout |
| 55 | Slow, fewer trades | Turtle **System 2** entry; major-trend capture |
| 100+ | Very slow | Position/long-term trend, high-conviction breaks |

Shorter N reacts faster but generates more [[false breakout|false breakouts]]; longer N filters noise but enters later and risks giving back more on reversals — the universal speed-vs-lag trade-off shared with [[moving-averages|moving averages]].

## The Turtle Trading Connection

The most famous application of Donchian Channels is the [[turtle-trading|Turtle Trading]] system. In the early 1980s, [[richard-dennis|Richard Dennis]] and [[bill-eckhardt|Bill Eckhardt]] trained 23 novice "Turtles" using:

- **System 1**: 20-day Donchian breakout (skipping after previous wins)
- **System 2**: 55-day Donchian breakout
- Position sizing normalised by [[atr|ATR]] (Wilder's "N" unit)

The Turtles reportedly produced ~$150–175M in profits over four to five years (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study reported a 74.1% win rate for Donchian Channel signals — among the highest of all indicators tested. However, win-rate alone is misleading; the high rate likely reflects the mean-reversion component of channel trades rather than pure trend-following entries (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Comparison with Other Channels

- **vs [[bollinger-bands]]**: Bollinger uses standard deviation; Donchian uses raw high/low — simpler but less adaptive to volatility
- **vs [[keltner-channels]]**: Keltner uses ATR for width; Donchian uses fixed lookback extremes

| Channel | Centre line | Band width driver | Bands hug price? |
|---------|-------------|-------------------|------------------|
| **Donchian** | Midpoint of high/low | N-period high & low (price extremes) | No — they step in discrete jumps |
| **[[bollinger-bands\|Bollinger]]** | SMA (e.g. 20) | ± k × standard deviation | Yes — expand/contract smoothly |
| **[[keltner-channels\|Keltner]]** | EMA (e.g. 20) | ± k × [[average-true-range\|ATR]] | Yes — smooth, volatility-scaled |

Donchian is the bluntest of the three: it asks only "is price at a new N-period extreme?" — which is exactly why it underpins the most famous mechanical breakout systems.

Note: For trading strategies using Donchian Channels, see [[donchian-channel-breakout]].

## How Traders Use It

- **Breakout entry.** Go long when price makes a new N-period high (closes above the upper band); go short on a new N-period low. This is pure [[trend-following]] — the core of the [[turtle-trading|Turtle]] approach.
- **Exit / [[trailing-stop|trailing stop]].** Exit a long when price prints a new *shorter* low (e.g. the 10-day lower band while entering on the 20-day upper) — a Donchian channel itself functions as a volatility-aware trailing exit.
- **Range identification.** A flat, narrow channel marks a [[consolidation]]; a sudden expansion of the channel signals a regime change to trending.
- **Support/resistance map.** The bands are objective, lookback-defined [[support]] and [[resistance]] lines that need no subjective trendline drawing.
- **Confluence.** Pairing a Donchian break with rising [[volume]] and a higher-timeframe trend adds [[confluence]] and filters the many breaks that fail.

## Common Pitfalls

- **Whipsaw in ranges.** In a [[consolidation]], price repeatedly pokes above/below the bands without follow-through, producing a string of [[false breakout|false breakouts]] and small losses — the price of admission for trend systems.
- **Buying the literal extreme.** Entering exactly at the band means buying the highest price in N days; expect immediate adverse excursion. Position sizing (Turtle "N" units via [[average-true-range|ATR]]) and a hard stop are essential.
- **No volatility scaling on its own.** Raw Donchian bands don't size your risk; you must overlay ATR-based sizing and stops, or the same fixed share count is wildly riskier on volatile names.
- **Lookback over-optimisation.** Tuning N to a backtest's sweet spot is a classic [[overfitting]] trap; the original systems deliberately used round, robust values (10/20/55).
- **Low win rate is expected.** A trend-following Donchian system can be right under 50% of the time and still profit from fat-tailed winners — judging it on win rate alone misreads the edge.

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=55` — recent bars for the 20/55-period bands
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=200` — perp-side OHLCV

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV for channel backfill
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=55"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — the bands are just rolling max/min of highs/lows over `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=55`; test breakouts against the *prior* bar's band, per the construction quirk above
- **Size** — pair the breakout with ATR from the same klines for Turtle-style N-unit position sizing
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) covers several full crypto cycles of 20/55-day breakouts — including the range years where whipsaw losses dominate
- **Tip** — stick to the round, robust lookbacks (10/20/55) rather than tuning N per asset; the overfitting warning above bites hardest on crypto's short, regime-heavy history

## Related

- [[richard-donchian]] — creator; "father of trend following"
- [[donchian-channel-breakout]] — the tradeable strategy built on the channel
- [[turtle-trading]] / [[turtle-traders]] — the most famous application
- [[breakout]] — the signal Donchian channels formalise
- [[trend-following]] — the strategy family this serves
- [[trailing-stop]] — the opposite band as a volatility-aware exit
- [[consolidation]] — flat channels mark ranges
- [[support]] / [[resistance]] — what the lower/upper bands represent
- [[atr]] / [[average-true-range]] — pairs with Donchian for sizing and stops
- [[keltner-channels]] — ATR-based channel alternative
- [[bollinger-bands]] — standard-deviation channel alternative
