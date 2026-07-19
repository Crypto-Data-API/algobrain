---
title: VWAP (Volume Weighted Average Price)
type: concept
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags: [vwap, indicators, technical-analysis, volume, liquidity]
aliases: [VWAP, volume-weighted-average-price]
domain: [indicators]
difficulty: beginner
related:
  - "[[volume]]"
  - "[[moving-averages]]"
  - "[[support-and-resistance]]"
  - "[[liquidity]]"
  - "[[macd]]"
  - "[[anchored-vwap]]"
  - "[[twap]]"
  - "[[slippage]]"
  - "[[bollinger-bands]]"
---

# VWAP (Volume Weighted Average Price)

VWAP is the average price an asset has traded at throughout the day, weighted by [[volume]] at each price level. It is the single most important execution benchmark on institutional trading desks and a widely used intraday trend and [[support-and-resistance]] reference for discretionary traders.

## Overview

VWAP is the primary benchmark used by institutional traders to evaluate execution quality. If you bought below VWAP, you got a better-than-average price; above VWAP, you paid more than average. It resets at the start of each trading session, making it primarily an intraday indicator — unlike a simple [[moving-averages|moving average]], a fresh VWAP begins at every session open and accumulates through the close.

Because so many algorithms reference VWAP, the level becomes partly self-fulfilling: execution desks lean on it, and price reacts to it. This reflexivity is the main reason VWAP "works" as intraday [[support-and-resistance]].

## Formula

VWAP is the cumulative dollar-volume traded divided by the cumulative share-volume traded, measured from the session open:

```
                Σ (Typical Priceᵢ × Volumeᵢ)
VWAP  =  ───────────────────────────────────────
                      Σ Volumeᵢ

where  Typical Priceᵢ = (Highᵢ + Lowᵢ + Closeᵢ) / 3   for bar i
```

The sums run cumulatively over every bar (i = 1 … now) since the session reset. Each successive bar adds to both the numerator and the denominator, so VWAP "remembers" the entire session and grows progressively harder to move as volume accumulates through the day.

### Worked example

Three intraday 5-minute bars on a stock, using typical price (HLC/3):

| Bar | Typical Price | Volume | Price × Volume | Cumulative P×V | Cumulative Volume | VWAP |
|-----|--------------|--------|----------------|----------------|-------------------|------|
| 1   | 100.00       | 10,000 | 1,000,000      | 1,000,000      | 10,000            | 100.00 |
| 2   | 101.00       | 30,000 | 3,030,000      | 4,030,000      | 40,000            | 100.75 |
| 3   |  99.00       | 20,000 | 1,980,000      | 6,010,000      | 60,000            | 100.17 |

After bar 2, VWAP = 4,030,000 / 40,000 = **100.75**. Note that the heavy 30,000-share bar pulls VWAP toward 101 more than the light 10,000-share bar held it at 100 — that volume weighting is the entire point. After bar 3, despite price dropping to 99, VWAP only eases to **100.17**, because the earlier volume still dominates the cumulative sums. A trader filling a buy order at 100.10 at this point has beaten the session benchmark.

### VWAP bands

Standard-deviation bands around VWAP (conceptually similar to [[bollinger-bands]] but anchored to VWAP rather than an SMA) mark over-extended conditions. The volume-weighted standard deviation of price around VWAP is computed, and bands are drawn at ±1σ, ±2σ, ±3σ. Reversion trades fade the outer bands back toward VWAP in range-bound sessions; trend traders treat a sustained push beyond +1σ as confirmation of intraday strength.

### Anchored VWAP

[[anchored-vwap|Anchored VWAP]] is a variation where the trader manually selects the starting point — an earnings release, a swing high/low, a gap, an FOMC announcement, an IPO date — rather than using the session open. The cumulative sums begin at the chosen anchor instead of at 00:00 of the session, which lets the level persist across multiple days and express "the average price paid by everyone who traded since event X." This makes anchored VWAP useful on swing and even position timeframes, where session VWAP is not.

## VWAP vs Related Benchmarks

| Benchmark | Weighting | Resets daily? | Primary use |
|-----------|-----------|---------------|-------------|
| **VWAP** | by [[volume]] | Yes (session) | Execution benchmark; intraday fair-value / S-R |
| **[[anchored-vwap]]** | by volume from a chosen anchor | No (runs from anchor) | Multi-day fair value relative to an event |
| **[[twap]]** (Time-Weighted Average Price) | equal per time slice | Yes (window) | Execution when minimizing footprint / signaling matters more than tracking volume |
| **[[moving-averages]] (SMA/EMA)** | by time (and recency for EMA) | No (rolling) | Trend over many sessions |

## Key Details

- **Above VWAP**: Price trading above VWAP suggests bullish intraday sentiment -- buyers are willing to pay above-average prices.
- **Below VWAP**: Price trading below VWAP suggests bearish intraday sentiment.
- **VWAP as magnet**: Price tends to revert to VWAP, especially during range-bound sessions.
- **VWAP as S/R**: Acts as dynamic intraday [[support-and-resistance]]. Institutional algorithms often use VWAP as a reference for execution, creating self-reinforcing behavior around the level.

## How Traders Use It

Day traders use VWAP to identify the intraday trend and plan entries. A common approach is to buy pullbacks to VWAP in an uptrend and sell rallies to VWAP in a downtrend. VWAP is also used to size into positions gradually — institutional algorithms like [[twap|TWAP]] (time-weighted) and VWAP algorithms execute large orders by tracking this benchmark to minimize [[slippage]].

Concrete playbooks:

- **VWAP reclaim / loss** — a stock that opens weak, sells off, then reclaims VWAP and holds above it on rising volume flips the intraday bias bullish. The mirror image (losing VWAP and failing to reclaim) is a short setup.
- **First test / mean-reversion** — in a balanced, range-bound session, the first pullback to VWAP after an opening drive is a common scalp entry, targeting the prior extreme with a stop on the other side of VWAP.
- **Trend-day fade avoidance** — on a strong trend day, price rides one side of VWAP (or the +1σ band) all session. Recognizing a trend day early stops traders from repeatedly fading the move back to VWAP, which is the classic way to get run over.
- **Execution / TWAP-VWAP slicing** — institutions slice a large parent order into child orders timed to the day's expected volume profile so the average fill tracks VWAP, holding [[market-impact]] and [[slippage]] down. The trader's fill is then judged in basis points relative to the day's VWAP ("I bought 4 bps through VWAP").

### Worked example (execution)

A desk must buy 600,000 shares of a name that trades ~6M shares/day. Dumping the order at once would move the price several percent (high [[market-impact]]). Instead a VWAP algo participates at ~10% of volume each interval, front-loading where the historical volume profile is heaviest (the open and the close). If the day's VWAP prints 50.20 and the algo's average fill is 50.18, the desk beat VWAP by ~4 bps — a measurably good execution under the [[transaction-costs|transaction-cost]] regime by which brokers are scored.

## Historical Origin

Volume-Weighted Average Price emerged from institutional trading desks in the 1980s–1990s as an execution benchmark. Brokers were judged on whether their fills beat VWAP — making it the primary measure of execution quality. Institutions slice large orders to track VWAP and minimise market impact. VWAP is now the dominant intraday benchmark in equities, futures, and increasingly crypto (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Best-Practice Combination

**VWAP + [[macd|MACD]]** is a popular intraday stack: VWAP provides institutional bias (price above VWAP = bullish context), while MACD confirms momentum direction and timing. This combination is particularly effective for day trading equities and crypto (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Common Pitfalls and Risks

- **It is a lagging average, not a forecast.** VWAP describes where trading has already happened. Late in the session it is extremely sticky (the denominator is huge), so it gives almost no fresh information into the close.
- **Garbage near the open.** With only a few bars accumulated, early-session VWAP whipsaws and can be dominated by a single large opening print. Many traders wait 15–30 minutes for it to stabilize.
- **Wrong session/anchor = wrong level.** Futures and crypto trade nearly 24h; choosing the wrong session reset (e.g. cash-equity hours vs full electronic session) produces a different VWAP. For multi-day context use [[anchored-vwap]] instead of session VWAP.
- **Self-fulfilling, until it isn't.** VWAP's S/R quality comes from algos referencing it; on news-driven trend days that reflexivity breaks and price ignores VWAP entirely. Do not mechanically fade it.
- **Benchmark gaming.** Because brokers are scored against VWAP, an execution can "beat VWAP" while still being poor in absolute terms — e.g. by trading passively while the price runs away. VWAP measures relative, not absolute, execution quality.
- **Not for low-liquidity names.** In thin instruments, a few prints distort the volume weighting and the level becomes unreliable; see [[liquidity]].

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Historical origin, institutional context, VWAP+MACD combination
- Berkowitz, Logue & Noser (1988), "The Total Cost of Transactions on the NYSE," *Journal of Finance* — early academic formalisation of VWAP as a transaction-cost benchmark
- Madhavan, A. (2002), "VWAP Strategies," *Transaction Performance: The Changing Face of Trading* (Institutional Investor) — institutional VWAP execution algorithms

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=24` — intraday OHLCV bars: typical price (H+L+C)/3 weighted by each bar's volume gives session VWAP
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — rolling 24h stats for the current session

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep kline archive for anchored-VWAP and multi-session studies
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — perp-side bars for Hyperliquid VWAP

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=24"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — cumulative Σ(typical price × volume) / Σ(volume) over bars from `GET /api/v1/market-data/klines` since the chosen anchor; crypto has no exchange session, so anchor to 00:00 UTC (the convention) or an event bar for [[anchored-vwap]]
- **Resolution** — 1h bars give a coarse but workable session VWAP; 1m klines in `GET /api/v1/backtesting/klines` (since 2026-03-30 only) sharpen the estimate for execution-grade comparisons
- **Backtest** — replay VWAP-reclaim and band-reversion rules against `GET /api/v1/backtesting/klines` (Binance spot 1h back to 2017-08), recomputing the cumulative sums from each day's anchor
- **Tip** — the early-session instability warning applies doubly at 1h resolution: skip signals until several bars have accumulated, and never fade VWAP on days the HMM state from `GET /api/v1/quant/market` reads `strong_trend_bull`/`strong_trend_bear`

## Related

- [[volume]] -- VWAP is weighted by volume
- [[anchored-vwap]] -- VWAP run from a chosen event instead of the session open
- [[twap]] -- time-weighted sibling benchmark used in execution algorithms
- [[moving-averages]] -- VWAP functions as a volume-weighted, session-resetting MA
- [[bollinger-bands]] -- analogous standard-deviation banding (around an SMA rather than VWAP)
- [[support-and-resistance]] -- VWAP acts as dynamic intraday S/R
- [[liquidity]] -- VWAP reliability degrades in thin instruments
- [[slippage]] -- VWAP algorithms exist to minimize it
- [[macd]] -- VWAP+MACD is a common intraday indicator stack
