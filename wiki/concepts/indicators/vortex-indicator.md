---
title: "Vortex Indicator"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, trend-following, momentum, crypto]
aliases: ["VI", "Vortex", "VI+ VI-"]
related: ["[[adx]]", "[[atr]]", "[[aroon]]", "[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[schaff-trend-cycle]]", "[[stonehill-forex-nnfx]]"]
domain: [technical-analysis]
prerequisites: ["[[atr]]"]
difficulty: beginner
---

The **Vortex Indicator (VI)**, published by Etienne Botes and Douglas Siepman in *Technical Analysis of Stocks & Commodities* (January 2010), measures trend direction with two lines, **VI+** and **VI−**, built from how far each bar's range reaches beyond the prior bar's opposite extreme, normalised by true range. A VI+/VI− crossover is the signal. It is a standard **confirmation** indicator in the [[nnfx-method|NNFX]] library at [[stonehill-forex|Stonehill Forex]] (Source: [[stonehill-forex-nnfx]]).

## Construction

For period `n` (default 14):

```
VM+[t] = |High[t] - Low[t-1]|        # upward "vortex movement"
VM-[t] = |Low[t]  - High[t-1]|       # downward vortex movement
TR[t]  = true range
VI+    = sum(VM+, n) / sum(TR, n)
VI-    = sum(VM-, n) / sum(TR, n)
```

It is conceptually close to the directional-movement lines of [[adx]] (+DI/−DI) but uses cross-bar high-to-low reach rather than high-to-high and low-to-low changes.

## How to read it

- **VI+ crosses above VI−** = bullish; **VI− above VI+** = bearish ("Two Lines Cross" reading in Stonehill's testing table).
- **Spread** between the lines = trend strength; lines tangled near 1.0 = no trend.

## NNFX role

**C1 or C2.** Its construction (range-based) differs from oscillator families like [[schaff-trend-cycle]] or RSI, which makes it a good C2 partner for them. Stonehill's 2022 profile found performance mixed and window-dependent — including no parameter set with positive ROI on 4-hour XAU/USD over its 3-month test (Source: [[stonehill-forex-nnfx]], LOW confidence as evidence).

## Crypto notes

- Crypto's large wicks inflate both VM+ and VM−; crossings on thin weekend bars are noisier. Consider requiring the spread `VI+ − VI−` to exceed a small threshold (e.g. 0.05) before counting a cross.
- Period 14 on daily bars; test 21 for fewer, later signals.

## Limitations

- Crossovers whipsaw in ranges like any two-line system; needs a volatility filter.
- Short published test windows; no crypto-specific validation reviewed.

## Getting the Data (CryptoDataAPI)

**Live data:** `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=500` — high/low/close for VM and TR.
**Historical data:** `GET /api/v1/backtesting/klines` — multi-year daily bars for crossover testing.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=500"
```

Catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Test as C2 behind a fixed C1** — hold C1 constant and measure whether requiring VI agreement raises expectancy per trade on `/api/v1/backtesting/klines`, not just win rate.
- **Tune the spread threshold** — sweep a minimum `VI+ − VI−` gap of 0–0.1 on in-sample years only; confirm on a held-out year.
- **Compare with +DI/−DI** — compute [[adx]] directional lines from the same bars; if signals overlap heavily, keep only one.

## Related

- [[nnfx-method]] · [[nnfx-crypto-daily-system]] — VI as C2
- [[adx]] · [[aroon]] · [[schaff-trend-cycle]] — related trend/confirmation tools
- [[atr]] — true range denominator

## Sources

- [[stonehill-forex-nnfx]] — Stonehill Forex, "Vortex Indicator as a Confirmation Indicator" (2022), fetched 2026-09-28
- Botes, E. and Siepman, D. (2010), "The Vortex Indicator", *Technical Analysis of Stocks & Commodities* — original publication (not reviewed directly)
