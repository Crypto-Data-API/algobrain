---
title: "Choppiness Index"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, volatility, market-regime, regime-detection, crypto]
aliases: ["CHOP", "Choppiness Index Indicator", "CI (Choppiness)"]
related: ["[[atr]]", "[[adx]]", "[[fractal-dimension]]", "[[waddah-attar-explosion]]", "[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[regime-detection]]", "[[stonehill-forex-nnfx]]"]
domain: [technical-analysis]
prerequisites: ["[[atr]]"]
difficulty: beginner
---

The **Choppiness Index (CHOP)**, created by Australian commodity trader E. W. (Bill) Dreiss, is a non-directional 0–100 measure of whether a market is **trending or ranging**. It compares the sum of each bar's [[atr|true range]] over `n` bars with the total high–low range of the window, on a log scale: high values mean price wandered a lot without getting anywhere (chop), low values mean it moved efficiently (trend). [[stonehill-forex|Stonehill Forex]] profiles it as a **volatility filter** for [[nnfx-method|NNFX]] (Source: [[stonehill-forex-nnfx]]).

## Construction

For period `n` (default 14):

```
CHOP = 100 * log10( sum(TR, n) / (max(High, n) - min(Low, n)) ) / log10(n)
```

The result is bounded 0–100. It is closely related to path-efficiency and [[fractal-dimension]] measures (and to the efficiency ratio inside [[kama]]).

## How to read it

- **Above ~61.8** — choppy / consolidating; trend signals are unreliable.
- **Below ~38.2** — strongly trending (in either direction), often late in a move.
- **Falling through a threshold** (commonly 50–55 in NNFX use) — trendiness emerging; the filter "passes". Stonehill describes the pass condition as the line being below a chosen level (Source: [[stonehill-forex-nnfx]]).

Direction must come from elsewhere; CHOP says only *whether*, not *which way*.

## NNFX role

**Volume / volatility filter.** Blocks C1 and baseline entries when the market is in chop, which is exactly when trend-following stacks bleed. It is an alternative to [[adx]] in the same slot and is cheaper to reason about.

## Crypto notes

- Crypto spends long periods in ranges between violent trends; a CHOP gate can cut trade count sharply. Measure whether the removed trades were net losers.
- Fibonacci-derived 38.2/61.8 thresholds have no special basis; tune on in-sample data and hold out.
- Weekend bars lower true range and can push CHOP up — keep them for continuity but be aware.

## Limitations

- Lagging by construction (window-based); it confirms a regime after it has started.
- Low CHOP near exhaustion can pass trades at the end of a move.
- No crypto-specific validation reviewed.

## Getting the Data (CryptoDataAPI)

**Live data:** `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — high/low/close for TR and the window range; `GET /api/v1/volatility/regime/{symbol}` and `GET /api/v1/quant/market` — independent regime classifiers to compare against CHOP.
**Historical data:** `GET /api/v1/backtesting/klines`; `GET /api/v1/quant/regimes/history` (Pro Plus) — labelled regimes for scoring CHOP's trend/range calls.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200"
```

Catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-regimes]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Score it against labelled regimes** — compute CHOP on `/api/v1/backtesting/klines` and compare its trend/range calls with `/api/v1/quant/regimes/history` labels; report agreement by regime.
- **Tune the gate out of sample** — sweep the pass threshold (45–60) on early years, freeze it, and test on the last 12 months.
- **Combine, don't duplicate** — if CHOP and the `/api/v1/volatility/regime/{symbol}` state agree most of the time, use the API regime as the live gate and CHOP as a backtestable proxy.

## Related

- [[nnfx-method]] · [[nnfx-crypto-daily-system]] — volatility slot
- [[adx]] · [[waddah-attar-explosion]] — alternative filters
- [[fractal-dimension]] · [[kama]] · [[regime-detection]] · [[atr]]

## Sources

- [[stonehill-forex-nnfx]] — Stonehill Forex, "Choppiness Index as a Volatility Indicator" (2023), fetched 2026-09-28
