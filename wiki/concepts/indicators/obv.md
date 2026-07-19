---
title: On-Balance Volume (OBV)
type: concept
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags: [obv, indicators, volume]
aliases: [OBV, on-balance-volume, "On Balance Volume"]
domain: [indicators]
prerequisites: ["[[volume]]"]
difficulty: beginner
related:
  - "[[volume]]"
  - "[[momentum]]"
  - "[[rsi]]"
  - "[[moving-averages]]"
  - "[[joseph-granville]]"
  - "[[bollinger-bands]]"
  - "[[divergence]]"
  - "[[accumulation-distribution]]"
  - "[[support-and-resistance]]"
---

# OBV (On-Balance Volume)

OBV is a cumulative [[volume]] indicator that adds volume on up-close days and subtracts volume on down-close days, designed to reveal whether volume is flowing into or out of an asset.

## Overview

Created by [[joseph-granville|Joe Granville]] in 1963 (popularized in his book *Granville's New Key to Stock Market Profits*), OBV was one of the first indicators to incorporate [[volume]] into technical analysis. The core premise is that **volume precedes price** — institutional accumulation or distribution shows up in OBV before it appears in the price chart. The absolute value of OBV is irrelevant (it depends on an arbitrary starting point); what matters is its *direction* and its *relationship to price*. OBV belongs to the same family as [[accumulation-distribution|Accumulation/Distribution]] and Chaikin Money Flow, but is the simplest: it uses only the sign of the daily close change, ignoring the *magnitude* of the move.

## How It Works

OBV is a running cumulative total. The formula for each period:

```
            ┌  OBV_prev + Volume_today    if Close_today > Close_yesterday
OBV_today = ┤  OBV_prev − Volume_today    if Close_today < Close_yesterday
            └  OBV_prev                   if Close_today = Close_yesterday
```

- **If today's close > yesterday's close**: OBV = previous OBV + today's volume
- **If today's close < yesterday's close**: OBV = previous OBV − today's volume
- **If today's close = yesterday's close**: OBV = previous OBV (unchanged)

The result is a running total that rises when up-day volume dominates and falls when down-day volume dominates. Note the binary nature: a +0.1% close and a +5% close on the same volume add *exactly the same* amount to OBV — OBV cares only about direction, not size.

### Worked Example

Start OBV at an arbitrary 0. Track six sessions:

| Session | Close | Direction vs. prior | Volume | OBV calculation | OBV |
|---|---|---|---|---|---|
| 1 | 50.00 | — (start) | 10,000 | 0 (baseline) | 0 |
| 2 | 50.40 | up | 12,000 | 0 + 12,000 | +12,000 |
| 3 | 50.10 | down | 9,000 | 12,000 − 9,000 | +3,000 |
| 4 | 50.10 | flat | 7,000 | unchanged | +3,000 |
| 5 | 51.20 | up | 20,000 | 3,000 + 20,000 | +23,000 |
| 6 | 50.90 | down | 6,000 | 23,000 − 6,000 | +17,000 |

OBV climbs from 0 to +17,000 over the window even though price ends only +1.8%. The big up-day (session 5) on heavy volume drove most of the rise, signalling that buyers showed up with conviction. If price had instead made a *new low* in session 6 while OBV held well above its session-3 trough, that would be a textbook **bullish divergence**. (Illustrative numbers only.)

### A Smoothing Variant

Because raw OBV is noisy, traders often overlay a [[moving-averages|moving average]] of OBV (e.g. a 20-day MA) and treat OBV crossing its own MA as a confirmation/trigger, analogous to a signal line.

## Key Signals

- **OBV confirming price**: Both price and OBV making new highs (or new lows) together confirms the trend is healthy.
- **Bullish divergence**: Price makes a lower low but OBV makes a higher low. Suggests accumulation is occurring despite falling prices -- potential reversal signal.
- **Bearish divergence**: Price makes a higher high but OBV makes a lower high. Suggests distribution is occurring despite rising prices -- potential topping signal.
- **OBV breakout**: OBV breaking to new highs before price does can be an early signal that a price breakout is imminent.

## Trading Relevance

OBV is most valuable as a [[divergence]] and confirmation tool. It helps distinguish between genuine breakouts (supported by volume) and false breakouts (lacking volume conviction). Combine OBV with [[support-and-resistance]] levels and [[momentum]] indicators for higher-probability setups. OBV works across all timeframes and asset classes.

| Signal | What you see | Read as |
|---|---|---|
| Confirmation | Price and OBV make new highs together | Healthy, well-supported trend |
| Bullish divergence | Price lower low, OBV higher low | Accumulation under weakness — reversal up likely |
| Bearish divergence | Price higher high, OBV lower high | Distribution into strength — top warning |
| OBV breakout lead | OBV breaks to new high before price | Early signal a price breakout is imminent |
| OBV/MA cross | OBV crosses above its own moving average | Volume momentum turning positive |

## Common Pitfalls

- **Binary close-rule blindness.** Because OBV only uses the *sign* of the close change, a tiny up-close on huge volume and a tiny down-close on huge volume swing OBV violently — a single ambiguous session can distort the line. Magnitude-aware alternatives ([[accumulation-distribution|Accumulation/Distribution]], Chaikin Money Flow) address this.
- **Gappy / illiquid names.** OBV assumes meaningful, comparable daily volume; in thin or heavily gapping stocks the cumulative total is unreliable.
- **Crypto and 24/7 markets.** With no clean daily "close," the choice of session boundary materially changes OBV; use it cautiously on continuously-traded assets.
- **Absolute level has no meaning.** OBV's numeric value depends on the arbitrary start point — never compare OBV levels across assets or read into a specific number; only slope and divergence matter.
- **Divergences can persist.** Like most leading signals, an OBV divergence can run for weeks before price confirms; pair it with price [[trend]] structure rather than acting on it alone.

## Best-Practice Combination

OBV is a key component of the professional **Trend + Momentum + Volatility + Volume** stack: 50/200 EMA + [[rsi|RSI]] + [[bollinger-bands|Bollinger Bands]] + OBV. In this combination, the moving averages identify trend direction, RSI provides momentum timing, Bollinger Bands frame volatility, and OBV confirms volume conviction behind moves (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## About the Creator

[[joseph-granville|Joseph Granville]] created OBV in 1963, making it one of the earliest indicators to formally incorporate volume into technical analysis. His core insight — that volume precedes price — has been validated across decades of market data (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — close and volume per bar, the only two inputs OBV needs
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=500` — the same computation on Hyperliquid perps
- `GET /api/v1/market-data/volume-history?days=90` — daily volume with buy ratio as an independent read on flow direction

**Historical data:**
- `GET /api/v1/backtesting/klines` — full kline archive (Binance spot 1h/4h/1d back to 2017-08) for OBV divergence and confirmation backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — running sum over `GET /api/v1/market-data/klines` bars: add volume when close > prior close, subtract when lower; only OBV's *slope* and its divergence from price matter, never the absolute level
- **Signal** — flag price highs unconfirmed by OBV highs (distribution) and OBV breakouts that precede price breakouts — Granville's "volume precedes price" premise, testable directly
- **Backtest** — replay over `GET /api/v1/backtesting/klines` (1h/4h/1d back to 2017-08); because OBV is cumulative, always recompute from the start of the test window rather than splicing partial series with different origins
- **Tip** — OBV counts every printed unit of volume equally, so wash-traded pairs corrupt it silently; restrict it to major pairs and sanity-check against the buy ratio in `GET /api/v1/market-data/volume-history` — OBV rising while the buy ratio falls is a data-quality red flag, not a signal

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Granville attribution, best-practice indicator combination stack.
- Granville, J. (1963), *Granville's New Key to Stock Market Profits* — the book that introduced and popularized OBV.
- General market knowledge — formula, worked example, and divergence/confirmation interpretation are standard technical-analysis material.

## Related

- [[volume]] -- OBV is built on volume data
- [[momentum]] -- OBV divergences signal momentum shifts
- [[divergence]] -- the primary OBV signal (price vs. volume flow)
- [[accumulation-distribution]] -- magnitude-aware sibling of OBV
- [[support-and-resistance]] -- OBV confirms breakouts through these levels
- [[rsi]] -- divergence signals work similarly in both
- [[moving-averages]] -- OBV is often smoothed with an MA signal line
- [[joseph-granville]] -- OBV's creator
- [[bollinger-bands]] -- OBV is part of the EMA+RSI+Bollinger+OBV professional stack
