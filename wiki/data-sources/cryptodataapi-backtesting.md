---
title: "CryptoDataAPI — Backtesting Archive"
type: source
created: 2026-07-13
updated: 2026-09-23
status: good
tags: [data-provider, crypto, api, backtesting, historical-data, point-in-time, parquet, klines, funding, liquidations]
aliases: ["CryptoDataAPI Backtesting", "CDA Backtesting", "CryptoDataAPI Historical Archive", "CryptoDataAPI Archives"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-data]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-news]]", "[[backtesting]]", "[[backtesting-overview]]", "[[point-in-time-data]]", "[[lookahead-bias]]", "[[crypto-perp-backtesting-pitfalls]]", "[[hyperliquid-backtesting]]", "[[crypto-data-quality]]", "[[purged-kfold-cv]]", "[[deflated-sharpe-ratio]]", "[[probability-of-backtest-overfitting]]", "[[survivorship-bias]]"]
---

CryptoDataAPI's Backtesting section is the historical arm of the API: a full archive of OHLCV klines, funding rates, and liquidation records, plus dated point-in-time daily snapshots and downloadable Parquet archives reaching back to 2020. It exists so that research uses the data as it stood on each historical date — the [[point-in-time-data]] discipline that keeps [[lookahead-bias]] out of strategy results.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/backtesting/klines | OHLCV candles, full archive | symbol*, exchange, start*, end, bounds, limit, cursor, format | — |
| GET | /api/v1/backtesting/funding | Funding rates, historical (`grain=snapshot_5m` default or `hourly`) | symbol*, exchange, start*, end, bounds, limit, grain, cursor, format | — |
| GET | /api/v1/backtesting/liquidations | Liquidation records, historical (venue-merged, rolling window) | symbol (≤25 comma list), start*, end, bounds, limit, cursor, format | — |
| GET | /api/v1/backtesting/hl-liquidations | Per-event Hyperliquid liquidation tape (exact fills: side, px, sz, USD notional, method, mark price) | coin (≤25 comma list), start*, end, bounds, limit, cursor, format | Pro |
| GET | /api/v1/backtesting/hl-liquidation-bars | Incremental Hyperliquid liquidation flow per closed 5m/15m/1h UTC bucket, summed from the exact fill tape, with an `audit` trail back to the fills | coin (≤25 comma list), interval (5m/15m/1h), start*, end, bounds, limit, cursor, format | Pro |
| GET | /api/v1/backtesting/hl-trade-flow | Archived 1-min HL taker buy/sell buckets per perp (same shape as live minus `cvd_usd`) | coin (≤25 comma list), start*, end, bounds, limit, cursor, format | Pro |
| GET | /api/v1/backtesting/hl-funding-bars | Hyperliquid funding + open interest on the candle clock (per-bar `funding_sum`, OI, mark) | coin (≤25), interval (1h/4h/1d), start*, end, bounds, limit, cursor, format | Pro Plus |
| GET | /api/v1/backtesting/news-events | Archived catalyst tape with measured market-response labels | start*, symbol, end, min_impact, bounds, limit | Pro Plus |
| GET | /api/v1/backtesting/snapshots | Historical JSON snapshots for one data type, streamed | data_type*, start*, end, bounds, limit, universe | — |
| GET | /api/v1/backtesting/snapshots/types | Available snapshot types with row counts and date ranges | — | — |
| GET | /api/v1/backtesting/symbols | Backtest-available symbols | — | — |
| GET | /api/v1/backtesting/status | Collector status | — | — |
| GET | /api/v1/backtesting/export | Export data, custom range | — | — |
| GET | /api/v1/backtesting/archives/index | Index of archives — data types, symbols, exchanges, date ranges | — | — |
| GET | /api/v1/backtesting/archives | List archived datasets | — | — |
| GET | /api/v1/backtesting/archives/download | Download archive (pre-signed URL) | — | — |
| GET | /api/v1/backtesting/archives/purchase | Buy one archived object over x402 (pay per resource); free for Pro Plus keys | data_type*, exchange, symbol, date, month, interval, bundle, snapshot_type | keyless (x402) / Pro Plus free |
| GET | /api/v1/backtesting/daily-snapshots | Daily snapshot list | — | — |
| GET | /api/v1/backtesting/daily-snapshots/{date} | Snapshot by date, point-in-time | date | — |
| GET | /api/v1/backtesting/signum-rgg | Archived full-universe SIGNUM RGG colour map for one date (`summary` + `by_symbol`) | date* | — |

Historical depth: Parquet archive from 2020.

`/backtesting/liquidations` vs `/backtesting/hl-liquidations`: the former is the general, cross-exchange liquidation-records archive (venue-merged, summary-level) already covered under Trading Applications below; `hl-liquidations` is Hyperliquid-specific and per-event — every exact liquidation fill (market and backstop) across the full HL perp universe, with side, price, size, USD notional, liquidation method, and mark price. `hl-liquidations` serves a local retention window of roughly 30 days rather than the full history; the full history is archived daily as the `hl_liquidations` data type (one Parquet per day, all coins) via `/backtesting/archives`. Use `liquidations` for cross-exchange summary flow, `hl-liquidations` when a strategy needs the exact fill tape on Hyperliquid. `hl-liquidations` moved from Pro Plus to **Pro** tier on 2026-09-07 (the underlying daily-Parquet archive stays Pro Plus).

**`/backtesting/hl-liquidation-bars` (new, 2026-09-12; Pro, same tier as the tape)** is the closed-bucket counterpart to `hl-liquidations`: incremental liquidation flow per closed 5m/15m/1h UTC bucket, summed from the exact Hyperliquid fill tape rather than read off a live rolling window. Each bucket carries `time`, `coin` (`null` on the market-wide series), `long_usd`, `short_usd`, `total_usd`, `n_long`, `n_short`, and `max_fill_usd`; buckets with no fills are not returned, and `start`/`end` are floored to the bucket grid so the bucket containing "now" — still forming — is never served (its fills still live only on `hl-liquidations`). Omit `coin` for one market-wide row per bucket (window ≤ 31 days), or pass a coin or comma list for per-coin rows (window ≤ 93 days); beyond either limit the API returns `400 range_too_large`. Every bar also carries an `audit` block naming the exact `hl-liquidations` call whose fills sum to it, so a bar is independently reproducible, not just reported. This is a `bar`-kind [[#Grain — what a row actually is (2026-09-12)|grain]] series, safe to sum across time — unlike the `rolling_window` default `/backtesting/liquidations` (see below).

`/backtesting/hl-trade-flow` (Pro, same tier pattern as `hl-liquidations`) archives the Hyperliquid per-coin trade tape documented live on [[cryptodataapi-hyperliquid]]: 1-minute taker buy/sell buckets per perp, forward-only from 2026-09-09. Each archived row is the live `/hyperliquid/trade-flow` bucket shape minus the served-only `cvd_usd` field (which resets per live request and is not meaningful stored). Minutes with no fills are not stored. It serves a local retention window; the full history is archived daily as the `hl_trade_flow` data type (one Parquet per day, all coins) alongside `hl_liquidations` via `/backtesting/archives` (the archive itself stays Pro Plus).

`/backtesting/hl-funding-bars` (Pro Plus, added 2026-09-19) returns Hyperliquid funding and open interest aligned to the candle clock — one row per closed bar per coin (`interval` 1h/4h/1d), with `time` equal to the matching `/hyperliquid/candles` `timestamp` so a funding/OI condition can be tested against the exact bar a price signal fires on. Per bar: `funding_sum` (carry actually settled in `(time, time + interval]`, summed across every settlement landing in the bar) with `n_settlements`; `funding_rate_mean` (mean live hourly rate over the bar's 5-min samples); `oi_open`/`oi_close`/`oi_change_pct` (base-coin units, first/last 5-min sample in the bar); `mark_close`; and `n_snapshots`. **`funding_sum: null` with `n_settlements: 0` means that day's settled prints are not yet archived — not zero carry** (settled prints are archived daily, for the previous UTC day; `funding_rate_mean` is available immediately since it doesn't depend on that archive step). Bars start **2026-03-30**: Hyperliquid publishes no historical open interest, so OI history is forward-only from CryptoDataAPI's own 5-minute capture and cannot be backfilled further back — older settled funding alone (no OI) is available further back via `/backtesting/funding?grain=hourly` — see below for what that mode actually returns. Coin list up to 25, window ≤ 93 days per call, cursor-paged, `format=csv` available.

**Backfill fix (2026-09-21):** both `/backtesting/hl-funding-bars` and `/backtesting/funding?grain=hourly` collected settled funding prints once a day for the previous day only, so a missed collector run left that day's `funding_sum: null` / `n_settlements: 0` permanently — **2026-09-12, 2026-09-13, and 2026-09-19** were affected this way. The daily job now back-fills any of the last 10 settled days it finds missing, so a single missed run self-heals within that window without manual reconciliation. No response-shape change.

### Grain — what a row actually is (2026-09-12)

**Every `/backtesting/*` range reader now carries an additive `grain` block on its response, stating what ONE ROW of that series actually is** — so it can't be mis-summed by assumption. `grain.kind` is one of: `event` (one fill), `bar` (a closed bucket), `rate_snapshot` (the live rate sampled on a timer), `rolling_window` (a trailing total sampled on a timer), or `settled_payment` (one settlement print) — alongside `cadence`, `is_cumulative`, `sum_ok` (whether summing rows across time is meaningful), `window`, `settlements_per_day` (funding series only), and a one-sentence `note`. This is a genuinely different thing from the `grain` **query parameter** `/backtesting/funding` accepts (`snapshot_5m` / `hourly`, covered next): the query param picks which row *shape* you get back, and that shape's rows then each carry a matching `grain` block describing themselves — related, but not the same knob.

Across the six endpoints that carry it: `/backtesting/klines` rows are `bar`; `/backtesting/funding` rows are `rate_snapshot` in the default `grain=snapshot_5m` shape and `settled_payment` in the `grain=hourly` shape; `/backtesting/liquidations` rows are `rolling_window`; `/backtesting/hl-liquidations` rows are `event`; `/backtesting/hl-trade-flow` and the new `/backtesting/hl-liquidation-bars` rows are both `bar`.

> [!warning] Two default-shape traps `grain` exists to catch
> `/backtesting/funding` default rows (`grain=snapshot_5m`) are **`rate_snapshot`**, not payments — the live rate sampled roughly every 5 minutes, about 12 samples per Hyperliquid funding settlement. Summing those samples to estimate carry paid **overstates it roughly 12x**; for the carry actually paid, use `grain=hourly` (below). Separately, `/backtesting/liquidations` rows are **`rolling_window`** — a trailing 24h level sampled on a timer, not an incremental flow. Do not sum it (double-counts) and do not difference consecutive rows (the sliding window makes that arithmetic meaningless too). For incremental Hyperliquid liquidation flow that IS safe to sum, use the event tape `/backtesting/hl-liquidations` (`event`) or the new bucketed `/backtesting/hl-liquidation-bars` (`bar`) — both carry `sum_ok: true`.

**`/backtesting/funding?grain=hourly` — settled Hyperliquid funding payments, not sampled rates.** `grain=hourly` switches `/backtesting/funding` from the default live-rate shape to one row per real settlement, sourced from Hyperliquid's own `fundingHistory` (the carry actually paid), carrying the additive `premium` field; `open_interest` and `mark_price` are `null` on these rows because Hyperliquid has no historical source for either at settlement time. These rows' `grain.kind` is `settled_payment` with `sum_ok: true` — safe to sum, unlike the default `snapshot_5m` shape above. The hourly series is loaded daily for the previous UTC day, so it lags roughly a day behind (use [[cryptodataapi-hyperliquid|`/hyperliquid/funding-rates`]] for the live tail), and is seeded from the `funding_deep` cold archive back to 2024. It is Hyperliquid-only: passing `grain=hourly` with `exchange=binance` returns `400 grain_unavailable`. The default `grain=snapshot_5m` shape is byte-identical to before apart from the additive fields — `premium` is `null` on snapshot rows.

### Paging, coverage, and comma-list scoping (2026-09-12)

**Keyset paging on every range reader.** `/backtesting/klines`, `/funding`, `/liquidations`, `/hl-liquidations`, `/hl-trade-flow`, and `/hl-liquidation-bars` all accept a `cursor` query parameter and return additive `next_cursor` (string, `null` once the window is exhausted) and `has_more` (bool) fields. To page correctly: pass the previous response's `next_cursor` back as `cursor` on the next call, keep `start`/`end` unchanged, and stop once `has_more` is `false`. Rows are now ordered by each table's full primary key — `(time, tid)` on the HL event tape, `(time, symbol)` / `(time, coin)` on the multi-symbol readers — so rows sharing a timestamp may come back in a different relative order than before, though the set of rows for a window is unchanged. **The old `start = last.time + 1` trick is unsafe and should not be used**: one liquidation order sweeping N order-book levels lands as N rows at the exact same millisecond, and advancing `start` past that millisecond silently drops every sibling row still sitting at it — a real, silent data-loss bug on the per-event tapes, not merely an inefficiency.

**`coverage` on every range reader (additive).** Each response also carries `local_first` / `local_last` (ms, the requested scope's local retention edges) and `archive_hint` (a string, else `null`, populated when the window starts before local retention — those rows live in the daily Parquet archive via `/backtesting/archives` instead). An empty `data` array is no longer silent: check `coverage` to tell "genuinely no events" from "before local retention, check the archive." For `/backtesting/hl-liquidations` specifically: live capture began **2026-07-23**; the archive also holds a pilot backfill for **2026-04-24 → 2026-05-05**; nothing exists for **2026-05-06 → 2026-07-22** — a real gap, not a collector fault, worth knowing before researching historical HL liquidations in that window.

**Comma-list scoping and CSV.** `symbol` / `coin` accept up to 25 comma-separated values on `/liquidations`, `/hl-liquidations`, `/hl-liquidation-bars`, and `/hl-trade-flow` — each value rides its own index in the response (`422 too_many_values` above that). `format=csv` is now available on `/funding`, `/liquidations`, `/hl-liquidations`, `/hl-liquidation-bars`, and `/hl-trade-flow` (`/klines` already had it); in CSV mode the response has no JSON envelope, so paging state moves to the `X-Has-More` / `X-Next-Cursor` response headers instead of body fields.

## Live Data

Only `/backtesting/status` is about the present — it reports collector health so you know whether the archive is up to date. `/backtesting/status` also returns a `limits` block with the bulkhead's real operating numbers (2026-09-12): **2 requests/s per key sustained, burst 20** (then `429`); **2 concurrent heavy reads with a 25s queue** before `503 backtesting_busy`; **10,000 rows per page**; and a **60s public-edge deadline** — the same numbers published on the docs page — plus `bt_funding_hourly_rows` and `bt_hl_liquidation_events_rows` row counts. Sending `Accept-Encoding: gzip` compresses pages roughly 10x at the edge. `/backtesting/symbols`, `/backtesting/snapshots/types`, and `/backtesting/archives/index` are discovery endpoints listing what is currently available to query or download.

## Historical Data

Everything else is history. `/backtesting/klines`, `/backtesting/funding`, `/backtesting/liquidations`, `/backtesting/hl-liquidations`, `/backtesting/hl-liquidation-bars`, and `/backtesting/hl-trade-flow` query the full archive directly; `/backtesting/export` pulls a custom range; `/backtesting/archives` + `/backtesting/archives/download` hand out pre-signed URLs for bulk Parquet datasets going back to 2020; `/backtesting/archives/purchase` sells a single archived object over x402 for an agent that doesn't hold an API key at all (payment mechanics, the 404-before-quote guarantee, and the Pro-Plus-free exception are detailed on [[cryptodataapi-mcp]]'s x402 section). The point-in-time core is `/backtesting/daily-snapshots/{date}`: the API's state frozen as of that day, so a backtest on 2023-03-15 sees exactly what a live system saw on 2023-03-15. `/backtesting/signum-rgg?date=YYYY-MM-DD` is a thin wrapper over that same daily snapshot that returns just its `signum_rgg` block (universe breadth `summary` plus the full per-symbol `by_symbol` map), stored since 2026-03-02 under the same auth gate as `daily-snapshots`; `computed_from` (present on days archived from 2026-09-09 onward) marks the last completed daily bar the colours were read from — see [[cryptodataapi-indicators]] for the live SIGNUM RGG endpoints this mirrors, including the 2026-09-09 completed-bar breaking change. Regime-probability history lives separately under the Pro Plus quant endpoints on [[cryptodataapi-regimes]]. `/backtesting/news-events` (Pro Plus, detailed on [[cryptodataapi-news]]) is a shallower archive by construction: it only holds qualified catalysts, and its history starts 2026-08-18 — the day the news family shipped — and **cannot be backfilled**, because the underlying RSS sourcing only ever serves a recent window.

## Trading Applications

- **Bias-free research** — dated daily snapshots enforce [[point-in-time-data]] and eliminate [[lookahead-bias]], the foundation of any credible [[backtesting]] workflow (see [[backtesting-overview]])
- **Perp strategy backtests** — historical funding and liquidation records address the funding-payment and liquidation-cascade issues catalogued in [[crypto-perp-backtesting-pitfalls]]
- **Hyperliquid replay** — combine archived klines and funding with live schema from [[cryptodataapi-hyperliquid]] for [[hyperliquid-backtesting]] with matching production data shapes
- **Bulk quantitative research** — Parquet archives since 2020 load straight into pandas/DuckDB for vectorised multi-year studies without pagination
- **Survivorship checks** — `/backtesting/symbols` plus dated snapshots reveal what was actually tradeable on each date, keeping delisted assets in the test universe

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/daily-snapshots/2024-01-15"
```

## From Archive to Validated Strategy

The archive is the raw input; a credible strategy is what survives the validation machinery run on top of it. The path from these endpoints to a deployable edge:

1. **Clean the data first.** Run the archive through the [[crypto-data-quality]] GIGO checklist — wash-traded volume, missing bars, clock skew, depeg artifacts, revised on-chain labels — before trusting any series.
2. **Construct a survivorship-free universe.** Combine `/backtesting/symbols` with dated `/backtesting/daily-snapshots/{date}` snapshots to reconstruct *what was actually tradeable on each historical date*, keeping delisted tokens and dead-venue contracts in the test set. "Top-N as of each date" from the dated snapshots, never "top-N today" back-applied — this is the concrete defense against [[survivorship-bias]].
3. **Validate with leakage-safe cross-validation.** Feed the cleaned, point-in-time series into [[purged-kfold-cv|purged K-Fold / CPCV]] so overlapping labels are purged and embargoed across fold boundaries.
4. **Correct for multiple testing.** Report the [[probability-of-backtest-overfitting|Probability of Backtest Overfitting (PBO)]] on the configuration search and the [[deflated-sharpe-ratio|Deflated Sharpe Ratio]] on the winner — the archive makes both honest by supplying dated, survivorship-free inputs rather than a flattering survivor-only sample.

The dated daily snapshots are what make this rigorous: the same point-in-time frame that eliminates [[lookahead-bias]] also fixes the universe roster on each date, so survivorship construction and leakage-safe validation draw from one consistent source.

## Related

- [[cryptodataapi]] — provider hub (auth, tiers, category map)
- [[cryptodataapi-regimes]] — Pro Plus quant history and Parquet regime archive
- [[cryptodataapi-market-data]] — live Binance spot counterpart
- [[cryptodataapi-derivatives]], [[cryptodataapi-hyperliquid]] — live funding/OI counterparts
- [[cryptodataapi-news]] — the live catalyst tape `/backtesting/news-events` archives
- [[backtesting-overview]], [[point-in-time-data]], [[lookahead-bias]], [[crypto-perp-backtesting-pitfalls]]

## Sources

- https://cryptodataapi.com/api (live OpenAPI JSON) and live curl tests of `/backtesting/hl-liquidations` and `/backtesting/archives/purchase` (fetched 2026-09-08)
- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
- https://cryptodataapi.com/api (raw OpenAPI JSON; `/api/v1/backtesting/signum-rgg` path, `date` param, and `SignumRggArchiveResponse` schema — `date`, `as_of`, `computed_from`, `summary`, `by_symbol` — confirmed live, fetched 2026-09-15)
- https://cryptodataapi.com/api (raw OpenAPI JSON; `/api/v1/backtesting/hl-trade-flow` path and `BacktestHLTradeFlowResponse`/`BacktestHLTradeFlowBucket` schemas, plus the `hl_trade_flow` `data_type` value on `/api/v1/backtesting/archives`, confirmed live, fetched 2026-09-17)
- https://cryptodataapi.com/api (raw OpenAPI JSON; `/api/v1/backtesting/hl-funding-bars` path, `BacktestHLFundingBar`/`BacktestHLFundingBarsResponse` schemas — `time`, `coin`, `funding_sum`, `n_settlements`, `funding_rate_mean`, `oi_open`/`oi_close`/`oi_change_pct`, `mark_close`, `n_snapshots` — its `coin`/`interval`/`start`/`end`/`bounds`/`limit`/`cursor`/`format` params, and the `grain=hourly` param on `/api/v1/backtesting/funding`, all confirmed live, fetched 2026-09-22)
- https://cryptodataapi.com/api (raw OpenAPI JSON, confirmed live, fetched 2026-09-23): the additive `GrainDescriptor` schema (`kind`, `cadence`, `is_cumulative`, `sum_ok`, `window`, `settlements_per_day`, `note`) and `CoverageInfo` schema (`local_first`, `local_last`, `archive_hint`), plus `next_cursor`/`has_more`, now on `BacktestKlinesResponse`, `BacktestFundingResponse`, `BacktestLiquidationsResponse`, `BacktestHLLiquidationsResponse`, and `BacktestHLTradeFlowResponse`; the `grain` query-param description on `/api/v1/backtesting/funding` (`snapshot_5m` default / `hourly`) and the `premium` field on `BacktestFundingEntry`; the new `/api/v1/backtesting/hl-liquidation-bars` path, its `coin`/`interval`/`start`/`end`/`bounds`/`limit`/`cursor`/`format` params, and `BacktestHLLiquidationBarsResponse`/`BacktestHLLiquidationBar` schemas (`time`, `coin`, `long_usd`, `short_usd`, `total_usd`, `n_long`, `n_short`, `max_fill_usd`, `audit`); the `cursor` param and comma-list `symbol`/`coin` param descriptions on `/liquidations`, `/hl-liquidations`, `/hl-trade-flow`, and `/hl-liquidation-bars`; and the additive `BacktestingLimits` schema (`edge_requests_per_second_per_key`, `edge_burst`, `heavy_read_concurrency`, `heavy_read_queue_seconds`, `max_rows_per_page`, `public_edge_timeout_seconds`) plus `bt_funding_hourly_rows`/`bt_hl_liquidation_events_rows` on `BacktestStatusResponse`
