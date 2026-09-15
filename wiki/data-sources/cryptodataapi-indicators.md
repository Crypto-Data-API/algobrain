---
title: "CryptoDataAPI — Indicators"
type: source
created: 2026-07-13
updated: 2026-09-15
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

**BREAKING — SIGNUM RGG now colours from completed UTC daily bars only (2026-09-09):** `color`, `days_in_color`, `adx`, `plus_di`, `minus_di`, `flipped_at`, `pct_change_since_flip`, `price`, `range`, and the detail endpoint's `history` are computed from the last **completed** UTC daily bar. Previously these included the still-forming (open) day, so a marginal flip at 00:30 UTC could un-flip by the close and `days_in_color` could count a day that had not finished — contradicting the documented rule and the causal daily archive. Every row now carries `is_final: true` and `computed_from` (the date of that last completed bar); expect `days_in_color` to read one lower than before the deploy and a handful of marginal colours to differ. The forming-bar read moved to new `color_live`, `adx_live`, and `days_in_color_live` fields (equal to the completed fields once the series already ends yesterday). The feed still recomputes hourly.

**Additive fields and params (2026-09-09):** each row now carries a `pegged` boolean (stablecoin / $1-pinned asset, default `false`) — pegged rows stay in the list but are documented as excluded from breadth and top-list aggregates elsewhere in the API. `flip_alert` (the last 4 closed 1h bars all disagree with the daily colour) is joined by `intraday_disagrees` (the same predicate), `recent_flip` (`days_in_color <= 3`), and `flip_alert_reason` (`"intraday_disagrees"` or `null`). The list endpoint gained an `offset` param (rows to skip after sorting) and its `limit` cap was raised from 500 to 1000 (default 250, response echoes `offset`). On `/indicators/signum-rgg/{symbol}`, the 60-day `intraday_history` is now **opt-in** via `?intraday=true` (one live candle pull per symbol per 30 min; omitted by default) instead of always included — it was fetching roughly 1,500 hourly bars per request and queuing sequential callers into the edge timeout. The symbol resolver also now tries the exact Hyperliquid name first, so `/indicators/signum-rgg/kPEPE` correctly returns the HL perp row (`PEPE` still resolves to Binance spot).

## Historical Data

Each per-symbol endpoint (`/indicators/signum-rgg/{symbol}`, `/indicators/technical/{symbol}`) carries a rolling 60-day history alongside the current detail, and Signum RGG is backfillable from daily klines. For longer lookbacks, reconstruct the indicators from OHLCV via [[cryptodataapi-market-data]] klines or the [[cryptodataapi-backtesting]] archive. The archived full-universe SIGNUM RGG colour map for a single day — a `summary` (breadth counts, top lists) plus the full `by_symbol` map, stored since 2026-03-02 — is also directly queryable via `GET /api/v1/backtesting/signum-rgg?date=YYYY-MM-DD`, under the same auth gate as `/backtesting/daily-snapshots/{date}`; see [[cryptodataapi-backtesting]] for the full endpoint row.

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
- https://cryptodataapi.com/api (raw OpenAPI JSON; `SignumRggResponse`, `SignumRggDetailResponse`, `SignumRggItem` fields — `color`/`color_live`, `days_in_color`/`days_in_color_live`, `adx`/`adx_live`, `is_final`, `computed_from`, `pegged`, `flip_alert`/`flip_alert_reason`, `intraday_disagrees`, `recent_flip` — and the `offset`/`limit` (max 1000) and `intraday` query params confirmed live, fetched 2026-09-15)
