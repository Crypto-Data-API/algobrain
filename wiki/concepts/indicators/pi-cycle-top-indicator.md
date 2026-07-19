---
title: "Pi Cycle Top Indicator"
type: concept
created: 2026-06-24
updated: 2026-07-19
status: draft
tags: [indicators, bitcoin, market-regime]
aliases: ["Pi Cycle Top", "pi-cycle", "Pi Cycle Top Indicator", "Pi Cycle"]
domain: [indicators]
prerequisites: ["[[200-day-moving-average]]", "[[bitcoin]]"]
difficulty: intermediate
related:
  - "[[on-chain-analysis]]"
  - "[[200-day-moving-average]]"
  - "[[bitcoin]]"
  - "[[mvrv]]"
  - "[[nupl]]"
  - "[[realized-price]]"
  - "[[glassnode]]"
---

# Pi Cycle Top Indicator

The **Pi Cycle Top Indicator** is a [[bitcoin]] cycle-timing tool that compares a short and a long moving average of price to flag potential market-cycle tops. It uses the **111-day simple moving average (111DMA)** and a **350-day simple moving average multiplied by 2 (2×350DMA)**, signalling a possible top when the faster 111DMA crosses *above* the slower 2×350DMA. Historically a handful of these crossovers have occurred near major Bitcoin cycle peaks, which is the source of the indicator's reputation — but the small number of observations makes it more of a heuristic than a precise tool.

## How It Works

The indicator is built from two moving averages of Bitcoin's daily closing price:

- **111-day moving average (111DMA)** — a medium-term trend line that tracks price reasonably closely.
- **2 × 350-day moving average (2×350DMA)** — the long-term 350-day average, then doubled. The 350DMA is a very slow trend line; multiplying it by two lifts it well above the long-run average.

The numbers 111 and 350 are chosen partly because 350 is roughly twice 111 (about a 1:π/π-style relationship that gives the indicator its "Pi" name; the ratio 350/111 ≈ π). In practice the construction is mechanical:

1. Compute the 111DMA each day.
2. Compute the 350DMA, multiply by 2.
3. Watch the gap between them. In normal conditions the 111DMA sits *below* the 2×350DMA.
4. A **top signal** fires when the rising 111DMA crosses **above** the 2×350DMA — i.e. price momentum has accelerated so far that the medium-term average overtakes twice the long-term average.

The logic is that a top crossover only happens after a steep, blow-off rally that drags the medium-term average sharply upward relative to the slow baseline — the kind of parabolic move that has historically preceded cycle exhaustion.

## How Traders Use It

- **Cycle-top warning** — a 111DMA / 2×350DMA crossover is treated as a heads-up to reduce exposure, tighten risk, or take profit, rather than a precise sell trigger.
- **Confluence with other tops signals** — practitioners rarely use it alone. They combine it with valuation-style on-chain metrics such as [[mvrv]], [[nupl]], and distance above [[realized-price]] (see [[on-chain-analysis]]) to build a weight-of-evidence picture of a frothy market.
- **Trend context** — because both inputs are moving averages, it doubles as a coarse read on how stretched price is versus its long-run trend, complementary to the [[200-day-moving-average]].

## Illustrative Example

Suppose Bitcoin enters a strong, accelerating uptrend. As price climbs steeply, the 111DMA rises quickly while the 2×350DMA — anchored to a much longer window — lags far behind. If the rally is parabolic enough, the 111DMA eventually catches up to and crosses above the 2×350DMA. A trader watching the indicator would read that crossover as a signal that the market is in a historically euphoric, over-extended state and might begin scaling out of risk. (Magnitudes and timing of any real-world crossover vary; this example is schematic, not a forecast.)

## Limitations and Pitfalls

- **Tiny sample size** — across Bitcoin's history there have been only a few crossovers, so the "track record" rests on a handful of data points. That is far too few to be statistically robust, and the relationship could break in future cycles.
- **Lagging by construction** — both inputs are moving averages of past prices, so the signal arrives only after a large move has already happened. It identifies *that* the market is stretched, not precisely *when* it will turn.
- **Top-only, not a bottom signal** — the Pi Cycle Top says nothing about cycle lows. It is asymmetric and should not be inverted to call bottoms.
- **Overfitting risk** — the specific 111 / 350×2 parameters were chosen with hindsight to fit past tops, a classic curve-fitting hazard. Out-of-sample reliability is unproven.
- **Bitcoin-specific** — it is calibrated to Bitcoin's historical cycle structure and does not transfer cleanly to other assets, especially in a market where cycle dynamics may be flattening over time.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — BTC daily closes; ~2.7 years per request comfortably covers the 350-day window plus warm-up
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC price history with the 200D MA precomputed, for trend context alongside the Pi Cycle lines

**Historical data:**
- `GET /api/v1/backtesting/klines` — Binance spot daily BTCUSDT back to 2017-08, enough to replay the April 2021 crossover (the 350-day warm-up makes signals evaluable from mid-2018 onward)
- `GET /api/v1/market-intelligence/btc/cycle-indicators` — the 8-indicator BTC cycle battery (historical) for cross-checking a Pi Cycle signal against other cycle metrics

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [BTC cycle](https://cryptodataapi.com/bitcoin-cycle-indicators)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — from daily closes: SMA(111) and 2 × SMA(350); the signal is the day SMA(111) closes above 2 × SMA(350) having been below it
- **Confluence** — never act on the cross alone (the page's sample-size caveat); pull `GET /api/v1/market-intelligence/btc/cycle-indicators` and `GET /api/v1/on-chain/dormancy/btc` (MVRV zone classification) for the weight-of-evidence read
- **Backtest** — `GET /api/v1/backtesting/klines` daily BTC covers roughly one clean, fully-warmed-up crossover (2021); treat any "hit rate" statistic on n≈2-3 events as anecdote, not evidence
- **Tip** — track the *gap ratio* (111DMA ÷ 2×350DMA) as a continuous stretch gauge instead of waiting for the binary cross — it degrades gracefully if future cycles flatten and never quite trigger

## Related

- [[on-chain-analysis]]
- [[200-day-moving-average]]
- [[bitcoin]]
- [[mvrv]]
- [[nupl]]
- [[realized-price]]
- [[glassnode]]

## Sources

General market knowledge; no specific wiki source ingested yet.
