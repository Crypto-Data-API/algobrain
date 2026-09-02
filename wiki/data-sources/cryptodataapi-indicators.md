---
title: "CryptoDataAPI — Indicators"
type: source
created: 2026-07-13
updated: 2026-09-02
status: good
tags: [data-provider, crypto, api, indicators, adx, rsi, bollinger-bands, moving-average, technical-analysis]
aliases: ["CryptoDataAPI Indicators", "CDA Indicators", "Signum RGG", "CryptoDataAPI Technical State"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-data]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-market-health]]", "[[adx]]", "[[rsi]]", "[[bollinger-bands]]", "[[moving-average]]", "[[indicators-overview]]", "[[support-and-resistance]]"]
---

CryptoDataAPI's Indicators section serves two pre-computed technical families so you never have to rebuild them from raw klines: **Signum RGG**, an ADX(14)+DMI trend classifier that buckets each asset into RED/GREY/GREEN, and **Technical**, a price-structure state built from SMA, Bollinger Bands, and RSI. Both are computed server-side across the asset universe, are backfillable from daily klines, and expose per-asset detail with a rolling 60-day history.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/indicators/signum-rgg | ADX(14)+DMI RED/GREY/GREEN | backfillable daily klines | Pro+ |
| GET | /api/v1/indicators/signum-rgg/{symbol} | Per-asset detail + 60d history | symbol | Pro+ |
| POST | /api/v1/indicators/signum-rgg/refresh | Force recompute | — | Pro |
| GET | /api/v1/indicators/technical | Price-structure state (SMA/BB/RSI) | — | Pro+ |
| GET | /api/v1/indicators/technical/{symbol} | Per-asset detail + 60d history | symbol | Pro+ |
| POST | /api/v1/indicators/technical/refresh | Force recompute | — | Pro |

## Live Data

The two base endpoints — `/indicators/signum-rgg` and `/indicators/technical` — return the current classification for the whole universe in one call: the live RGG colour per asset and the live SMA/BB/RSI structure state. The POST `/refresh` endpoints force an immediate recompute when you need the state updated ahead of the scheduled cycle.

**`sr` support/resistance field (added 2026-08-25):** the technical-structure block on `/indicators/technical` and `/indicators/technical/{symbol}` now carries an `sr` object — `sr.support` and `sr.resistance`, each up to 3 levels, nearest-to-price first. Every level is `{price, strength, dist_pct}`: `strength` is how many swing pivots clustered into that level, and `dist_pct` is the signed % distance from mark (negative for support, positive for resistance). Levels are derived from swing-pivot detection on the same 250-day daily series already backing the rest of the technical block (no new data source), clustered within 1.5% of each other, and dropped once more than 30% away from mark. An empty `[]` on either side is a genuine "no clean level" read, not missing data — `sr` defaults to `{support: [], resistance: []}` when nothing clusters.

## Historical Data

Each per-symbol endpoint (`/indicators/signum-rgg/{symbol}`, `/indicators/technical/{symbol}`) carries a rolling 60-day history alongside the current detail, and Signum RGG is backfillable from daily klines. For longer lookbacks, reconstruct the indicators from OHLCV via [[cryptodataapi-market-data]] klines or the [[cryptodataapi-backtesting]] archive.

## Trading Applications

- **Trend filtering** — Signum RGG wraps [[adx]]/DMI into a three-colour gate: only take longs in GREEN, fade or stand aside in RED, and treat GREY as chop per [[indicators-overview]]
- **Mean-reversion setups** — the technical state combines [[bollinger-bands]] and [[rsi]] so you can screen the whole universe for stretched-and-oversold candidates in one request
- **Support/resistance confluence** — pair the `sr` field's clustered [[support-and-resistance]] levels with an oversold RSI/BB read: a mean-reversion long that lands within a level's `dist_pct` of a high-`strength` support cluster has more confirmation than the RSI signal alone, and a level's absence (`sr.support: []`) is itself information that price has no nearby structure to lean on
- **Trend-structure confirmation** — [[moving-average]] position within the technical state confirms or vetoes signals from the regime engine on [[cryptodataapi-regimes]]
- **Universe screening** — one call classifies every covered asset, replacing per-symbol indicator computation in scanners and dashboards
- **Signal research** — the 60d per-asset histories let you check how long RGG colours or RSI states persist before committing them to a live rule

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/signum-rgg/BTC"
```

## Related

- [[cryptodataapi]] — provider hub (auth, tiers, category map)
- [[cryptodataapi-regimes]] — regime families that complement these indicator states
- [[cryptodataapi-market-data]] — raw klines if you want to compute indicators yourself
- [[cryptodataapi-backtesting]] — historical archive for indicator backtests
- [[cryptodataapi-market-health]] — composite market scores
- [[adx]], [[rsi]], [[bollinger-bands]], [[moving-average]], [[indicators-overview]], [[support-and-resistance]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
