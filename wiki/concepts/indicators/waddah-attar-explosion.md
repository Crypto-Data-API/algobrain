---
title: "Waddah Attar Explosion"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, volatility, momentum, crypto]
aliases: ["WAE", "Waddah Attar Explosion Indicator"]
related: ["[[macd]]", "[[bollinger-bands]]", "[[choppiness-index]]", "[[adx]]", "[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[stonehill-forex-nnfx]]"]
domain: [technical-analysis]
prerequisites: ["[[macd]]", "[[bollinger-bands]]"]
difficulty: intermediate
---

The **Waddah Attar Explosion (WAE)**, released in 2007 by trader Ahmad Waddah Attar for MetaTrader, is a momentum-plus-volatility histogram: a scaled **change in MACD** (the "trend" bars, green up / red down) plotted against an **"explosion line"** derived from [[bollinger-bands|Bollinger Band]] width, with a **dead-zone** floor. Despite the name it uses no volume. In [[nnfx-method|NNFX]] it is a commonly used **volume/volatility filter** (Source: [[stonehill-forex-nnfx]]).

## Construction

Typical defaults: sensitivity 150, fast EMA 20, slow EMA 40, BB length 20, BB multiplier 2.0, dead zone in price units.

```
macd[t]      = EMA(close, fast) - EMA(close, slow)
trend[t]     = (macd[t] - macd[t-1]) * sensitivity    # >0 green bar, <0 red bar (absolute value plotted)
explosion[t] = BB_upper(close, 20, 2) - BB_lower(close, 20, 2)
dead_zone    = constant (FX: pips; often an ATR multiple in ports)
```

## How to read it

- **Long filter passes**: green bar **above** the explosion line and above the dead zone.
- **Short filter passes**: red bar above the explosion line and dead zone.
- **Rising explosion line** with bars above it = volatility expanding in the trade's direction ("explosion"); bars below the line = insufficient fuel.

Stonehill's profile emphasises the angle of the explosion line and warns never to trade on a volume indicator alone (Source: [[stonehill-forex-nnfx]]).

## NNFX role

**Volume / volatility filter** — the last check before entry. It answers "is momentum expanding faster than the recent volatility envelope?" rather than giving direction on its own.

## Crypto notes

- The fixed dead zone is in price units and **must be replaced** with a volatility-scaled value (e.g. a fraction of [[atr]]) for crypto; a fixed number is meaningless across BTC at 60k and a token at 0.50.
- The sensitivity multiplier likewise only scales the display; the bar-versus-line comparison depends on it, so normalise both by price or ATR when porting.
- Because it uses no volume, pair it with actual exchange volume if a literal volume check is wanted.

## Limitations

- Stonehill's WAE profile states comprehensive test results were still pending — there is no published Stonehill result to lean on.
- Parameter-heavy (five inputs plus dead zone); easy to overfit.
- Many code variants exist (V2, V3, "Uber"), with different scaling.

## Getting the Data (CryptoDataAPI)

**Live data:** `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — closes for the MACD and Bollinger components; `GET /api/v1/market-data/volume-history` — real daily volume to complement a volume-free WAE.
**Historical data:** `GET /api/v1/backtesting/klines` — archive for filter-effectiveness tests.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Normalise first** — compute trend bars and explosion line as fractions of price (or ATR) so one dead-zone value works across the basket.
- **Measure filter value** — on `/api/v1/backtesting/klines`, compare a fixed C1's trades with and without the WAE gate; accept only if average R per trade rises, not merely trade count falls.
- **Cross-check with real volume** — flag WAE passes where `/api/v1/market-data/volume-history` shows below-median volume; test whether those trades underperform.

## Related

- [[nnfx-method]] · [[nnfx-crypto-daily-system]] — volume/volatility slot
- [[choppiness-index]] · [[adx]] — alternative filters
- [[macd]] · [[bollinger-bands]] — components

## Sources

- [[stonehill-forex-nnfx]] — Stonehill Forex, "Waddah Attar Explosion as a Volume Indicator" (2022), fetched 2026-09-28
