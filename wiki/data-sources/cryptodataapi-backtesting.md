---
title: "CryptoDataAPI — Backtesting Archive"
type: source
created: 2026-07-13
updated: 2026-10-17
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
| GET | /api/v1/backtesting/klines | OHLCV candles from the local 1m archive; `interval` aggregates them (honoured since 2026-10-10) | symbol*, exchange, interval (1m/5m/15m/30m/1h/4h/1d), start*, end, bounds, limit, cursor, format | — |
| GET | /api/v1/backtesting/liquidation-density | Hyperliquid liquidation density near the mark (±0.5/1/2/3/5% bands) as a time series, with `by_trader_type` / `by_leverage` splits (new 2026-10-08) | coin* (≤25 comma list), start*, end, interval (5m/1h), splits, bounds, limit, cursor, format | Pro Plus |
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

### `/backtesting/klines` now honours `interval` (breaking fix, 2026-10-10)

**Until 2026-10-10 `/backtesting/klines` never read `interval`.** Every call returned 1-minute bars, including `interval=4h` and `interval=1d`. Any backtest that requested coarser bars from this route before that date actually ran on 1m rows. It now takes `interval` = `1m` (default, as stored), `5m`, `15m`, `30m`, `1h`, `4h` or `1d`, and aggregates the stored 1m bars on the UTC grid:

- `t` is the bar open, and `start` is floored to the interval.
- Each aggregated row gains **`n`**, the number of 1m bars inside it. A full 4h bar has `n: 240` and a full 1d bar `n: 1440`. A smaller `n` means a gap in the archive or a bar still forming at `end`. `n` is null on 1m rows.
- `grain.cadence` is the requested interval, and `grain.note` restates the `n` rule.
- **One aggregated page scans at most ~278 days of 1m rows**, so a long `1d` request returns early with `has_more: true`. Keep paging with `next_cursor`.
- Any query parameter the route does not read is now a `400 unknown_parameter`. The body lists the `accepted` set: `bounds`, `cursor`, `end`, `exchange`, `format`, `interval`, `limit`, `start`, `symbol`.

Live check on 2026-10-17: `?symbol=BTCUSDT&interval=4h&start=2026-10-14&limit=3` returned three 4h rows with `n: 240` and `grain.cadence: "4h"`.

> [!warning] Which klines source covers which depth
> The aggregated bars can only reach back as far as the local 1m rows behind them. On 2026-10-17 `coverage.local_first` for BTCUSDT was 2026-05-09. A `1d` request starting at 2025-01-01 returned **0 rows with `has_more: false`** and an `archive_hint`, not an error. Deeper history lives in the Parquet archives on `/backtesting/archives` (listed by `/backtesting/archives/index`):
> - **`klines`**: daily 1m Parquet files from 2026-03-30.
> - **`klines_deep`**: monthly files at **1h, 4h and 1d**. Binance runs from 2017-08 (BTCUSDT 2017-08 to 2026-07). Hyperliquid BTC 1d runs from 2023-01 and 4h from 2024-03.
>
> Many strategy pages say "`/backtesting/klines` serves 1h/4h/1d back to 2017-08". That depth exists only in the `klines_deep` archive, not on the REST route.

### Liquidation density near the mark (new 2026-10-08)

**`GET /backtesting/liquidation-density` (Pro Plus)** is a time series of Hyperliquid liquidation density around the mark. Previously you had to read whole `liquidation_map` / `liquidation_levels` snapshots (~1 MB each) to get this; a point here is ~2 KB. Each point is one coin at one 5-minute snapshot:

- `time` (bucket start), `snapshot_time` and `mark`.
- **`long_below`**: USD of long positions that liquidate below the mark. **`short_above`**: USD of shorts that liquidate above it. Both are keyed by **cumulative** band, `0.5`, `1`, `2`, `3` and `5` (% of mark), so the `5` band includes the `2` band.
- The same split **`by_trader_type`** (`vault`, `market_maker`, `whale`, `smart_money`, `high_leverage`, `other`) and **`by_leverage`** (`3`, `5`, `10`, `20`, `25`, `40`, `50`, `100`x).
- Every key is always present, and `0` means nothing in that band.

Parameters: `coin` (one, or a comma list of up to 25; HL names such as `kPEPE`), `start` / `end` (≤ 93 days per call, `end` exclusive), `interval` (`1h` default = the first snapshot of each hour, or `5m` = every snapshot), `splits` (`trader_type,leverage` default, or `none` for the all-account bands only, ~10x smaller), `bounds`, `limit`, `cursor` and `format=csv` (all-account bands only). The spec gives it `x-timeout-seconds: 30`. **History starts 2026-06-26**, when the full-universe liquidation feed began. The earlier `liquidation_levels` snapshots are a ~25-whale sample and are not included.

Live check on 2026-10-17 (BTC, 2026-10-16 00:00 to 02:00 UTC, 1h): mark 82,225.5; `long_below` was $0 inside ±1%, $149.9M inside 2% and $200.3M inside 5%. Whales held $149.8M of the 2% long band. That is the shape a cascade or magnet strategy reads: how much forced flow sits within a given move of the mark, and whose it is.

### Snapshot types added by the 2026-10 releases

- **`exchange_flow_spikes` (new 2026-10-08).** Every row of `/on-chain/exchange-flows/spike-alerts` is archived. Each 5-minute snapshot holds only the rows first seen in that tick, so a range lists each transfer once. History starts **2026-10-08 00:25 UTC**. The live endpoint keeps only the last 500 rows (about 10 hours), so this archive is the only way to backtest spike alerts. Rows carry the new `source` field (`transfer` or `balance_delta`). Each row's `ts` is unix **seconds**, while the snapshot `time` is milliseconds (verified 2026-10-17). See [[cryptodataapi-on-chain]].
- **`whale_activity` universe widened (2026-10-14).** From 2026-10-14 the snapshot carries the 100 coins in `/quant/whales` `top_coins`. Snapshots before 2026-10-14 hold **at most 60**. A coin missing from a pre-10-14 snapshot may simply have ranked 61-100, so do not read its absence as "no whale positioning". A coin new to the list reports `long_pct_pctile_30d: null` until it has 48 hourly samples. See [[cryptodataapi-regimes]].

### Archive listing cache (2026-10-09)

`/backtesting/archives` and `/archives/download` now read the archive listing from a cache. New uploads appear within 15 minutes under steady use, and within an hour at most. Response shapes and defaults are unchanged. **The unfiltered default `/archives` call is still a ~9 MB listing of every klines file.** Pass `data_type=daily`, `symbol` or a date range to get a small one. The OpenAPI spec now carries `data_type=daily` as the example for both routes.

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

The live `/market-intelligence/liquidations` route has carried the same `grain` block since 2026-09-23 (`kind: rolling_window`, `sum_ok: false`), plus `row_count_meaning: "liquidation_events_24h"`. Its rows are trailing-window levels, so do not sum successive polls of it. Use `/backtesting/hl-liquidation-bars` for flow. See [[cryptodataapi-market-intelligence]].

### ETF flow snapshots before 2026-09-25 are partial figures

> [!warning] Do not backtest on archived ETF flow snapshots from before 2026-09-25
> Until 2026-09-25, `/market-intelligence/etf/{asset}/flows` read Farside's newest row while issuers were still reporting (IBIT and FBTC last), so on most weekdays it served a **partial sum** stamped with the fetch time. For example, it served +$32.4M for the 2026-09-23 BTC trade date, against a settled Total of +$346.9M. The `coinglass_etf_flows` data type on `/backtesting/snapshots`, and the ETF values inside `/backtesting/daily-snapshots/{date}`, are point-in-time copies of what was served. Most weekday rows before 2026-09-25 therefore hold the partial figure, and **they are not being rewritten**. This is the rare case where the point-in-time copy is the wrong input for a flow backtest, because the live system itself was reading a wrong number. For settled history, use `GET /market-intelligence/etf/{asset}/flows?days=N` (up to 1000 settled trade days: BTC from 2024-01-11, ETH from 2024-07-23, SOL from 2025-10-28), keyed by `trade_date`. Snapshots from 2026-09-25 onward carry `trade_date`, `status` and `source`, so each row states which trade date it covers and whether it was settled. See [[cryptodataapi-market-intelligence]] for the rebuilt response.

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

# 4h bars aggregated from the 1m archive (honoured since 2026-10-10; check each row's n)
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=BTCUSDT&interval=4h&start=2026-10-01"

# Liquidation density within ±0.5-5% of mark, hourly, all-account bands only (Pro Plus)
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/liquidation-density?coin=BTC,ETH&start=2026-10-01&splits=none"
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

- CryptoDataAPI changelog releases 2026-10-08, 2026-10-09, 2026-10-10 and 2026-10-14 (via `GET /api/v1/changelog`, fetched 2026-10-17), the live OpenAPI spec (`/api/v1/backtesting/klines` `interval` param and description, `/api/v1/backtesting/liquidation-density` params and description; fetched 2026-10-17), and live calls on 2026-10-17: `/backtesting/klines?interval=4h` (`n`, `grain.cadence`), a 1d request before local retention (empty page plus `archive_hint`), the unknown-parameter 400, `/backtesting/liquidation-density?coin=BTC`, `/backtesting/snapshots/types` (`exchange_flow_spikes` earliest 2026-10-08 00:25 UTC) and `/backtesting/archives/index` (`klines` and `klines_deep` coverage)
- https://cryptodataapi.com/api (live OpenAPI JSON) and live curl tests of `/backtesting/hl-liquidations` and `/backtesting/archives/purchase` (fetched 2026-09-08)
- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
- https://cryptodataapi.com/api (raw OpenAPI JSON; `/api/v1/backtesting/signum-rgg` path, `date` param, and `SignumRggArchiveResponse` schema — `date`, `as_of`, `computed_from`, `summary`, `by_symbol` — confirmed live, fetched 2026-09-15)
- https://cryptodataapi.com/api (raw OpenAPI JSON; `/api/v1/backtesting/hl-trade-flow` path and `BacktestHLTradeFlowResponse`/`BacktestHLTradeFlowBucket` schemas, plus the `hl_trade_flow` `data_type` value on `/api/v1/backtesting/archives`, confirmed live, fetched 2026-09-17)
- https://cryptodataapi.com/api (raw OpenAPI JSON; `/api/v1/backtesting/hl-funding-bars` path, `BacktestHLFundingBar`/`BacktestHLFundingBarsResponse` schemas — `time`, `coin`, `funding_sum`, `n_settlements`, `funding_rate_mean`, `oi_open`/`oi_close`/`oi_change_pct`, `mark_close`, `n_snapshots` — its `coin`/`interval`/`start`/`end`/`bounds`/`limit`/`cursor`/`format` params, and the `grain=hourly` param on `/api/v1/backtesting/funding`, all confirmed live, fetched 2026-09-22)
- https://cryptodataapi.com/api (raw OpenAPI JSON, confirmed live, fetched 2026-09-23): the additive `GrainDescriptor` schema (`kind`, `cadence`, `is_cumulative`, `sum_ok`, `window`, `settlements_per_day`, `note`) and `CoverageInfo` schema (`local_first`, `local_last`, `archive_hint`), plus `next_cursor`/`has_more`, now on `BacktestKlinesResponse`, `BacktestFundingResponse`, `BacktestLiquidationsResponse`, `BacktestHLLiquidationsResponse`, and `BacktestHLTradeFlowResponse`; the `grain` query-param description on `/api/v1/backtesting/funding` (`snapshot_5m` default / `hourly`) and the `premium` field on `BacktestFundingEntry`; the new `/api/v1/backtesting/hl-liquidation-bars` path, its `coin`/`interval`/`start`/`end`/`bounds`/`limit`/`cursor`/`format` params, and `BacktestHLLiquidationBarsResponse`/`BacktestHLLiquidationBar` schemas (`time`, `coin`, `long_usd`, `short_usd`, `total_usd`, `n_long`, `n_short`, `max_fill_usd`, `audit`); the `cursor` param and comma-list `symbol`/`coin` param descriptions on `/liquidations`, `/hl-liquidations`, `/hl-trade-flow`, and `/hl-liquidation-bars`; and the additive `BacktestingLimits` schema (`edge_requests_per_second_per_key`, `edge_burst`, `heavy_read_concurrency`, `heavy_read_queue_seconds`, `max_rows_per_page`, `public_edge_timeout_seconds`) plus `bt_funding_hourly_rows`/`bt_hl_liquidation_events_rows` on `BacktestStatusResponse`
