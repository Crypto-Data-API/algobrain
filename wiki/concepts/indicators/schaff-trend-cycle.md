---
title: "Schaff Trend Cycle"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, momentum, trend-following, crypto]
aliases: ["STC", "Schaff Trend Cycle Indicator", "Schaff"]
related: ["[[macd]]", "[[stochastic-oscillator]]", "[[oscillators]]", "[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[vortex-indicator]]", "[[stonehill-forex-nnfx]]"]
domain: [technical-analysis]
prerequisites: ["[[macd]]", "[[stochastic-oscillator]]"]
difficulty: intermediate
---

The **Schaff Trend Cycle (STC)**, developed by Doug Schaff in the late 1990s, is a bounded 0–100 oscillator that runs a **MACD line through a double stochastic** calculation. The aim is MACD's trend sensitivity with less lag and a cleaner on/off output. In the [[nnfx-method|NNFX]] framework it is a commonly profiled **C1 confirmation** indicator on [[stonehill-forex|Stonehill Forex]] (Source: [[stonehill-forex-nnfx]]).

## Construction

1. **MACD line**: `M = EMA(close, fast) - EMA(close, slow)` (common defaults fast 23, slow 50).
2. **First stochastic of M** over a cycle length `L` (default 10): `%K1 = 100 x (M - min(M, L)) / (max(M, L) - min(M, L))`, then smooth: `PF = PF[-1] + f x (%K1 - PF[-1])`, with factor `f ≈ 0.5`.
3. **Second stochastic of PF** over `L`, smoothed the same way → **STC**.

Because each stochastic stage renormalises to its own recent range, the STC spends most of its time pinned near 0 or 100 and transitions quickly — a near-binary regime signal.

## How to read it

- **Classic levels**: bullish when STC rises through **25**, bearish when it falls through **75**.
- **Colour / slope flip**: many implementations colour the line by direction; NNFX testers often read the flip as the signal (see Stonehill's "Histogram/Color" reading method on its testing-settings page).
- Long flat stretches at 0/100 are normal and are *not* overbought/oversold readings.

## NNFX role

**C1 (primary trigger)** or **C2**. As C1 it provides the entry signal; when used as C2 alongside a different-construction C1 (e.g. [[vortex-indicator]]) it adds a momentum-of-trend check. Do not pair STC with another MACD-derived C2 — they share an input and add little.

## Crypto notes

- Double normalisation makes STC scale-free, so the same thresholds work across BTC and small caps, but it also means a tiny MACD wiggle in a dead market can produce a full 0→100 swing. Pair with a volatility filter ([[choppiness-index]], [[waddah-attar-explosion]]).
- Test cycle length 10 vs. slower settings on daily crypto; the 23/50 MACD defaults came from FX.

## Limitations

- Many platform versions differ in the smoothing factor and stage count; results are not portable without matching code.
- Near-binary output can flip several times in choppy tape — the NNFX one-candle and volume rules exist to absorb that.
- No independent crypto validation reviewed in this vault.

## Getting the Data (CryptoDataAPI)

**Live data:** `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=500` — closes for the MACD and stochastic stages; `GET /api/v1/indicators/technical/{symbol}` — the API's own SMA/BB/RSI structure state as a cross-check.
**Historical data:** `GET /api/v1/backtesting/klines` — archive for C1-in-isolation tests.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=500"
```

Catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-indicators]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Run the C1 isolation test** — trade every STC 25/75 cross (or colour flip) on daily `/api/v1/backtesting/klines` bars across a 5-asset basket with a fixed 2 x ATR stop; record expectancy net of fees.
- **Compare reading methods** — level-cross versus slope-flip change trade count by a factor of 2–3; report both before choosing.
- **Check redundancy** — correlate STC signals with `/api/v1/indicators/technical/{symbol}` RSI state; if they agree more than ~80% of the time, STC is not adding information as C2.

## Related

- [[nnfx-method]] · [[nnfx-crypto-daily-system]] — STC as C1
- [[macd]] · [[stochastic-oscillator]] · [[oscillators]] — its components
- [[vortex-indicator]] · [[aroon]] — different-construction confirmation partners

## Sources

- [[stonehill-forex-nnfx]] — Stonehill Forex, "Schaff Trend Cycle as a Confirmation Indicator" (2022) and indicator library, fetched 2026-09-28
