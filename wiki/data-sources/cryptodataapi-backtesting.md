---
title: "CryptoDataAPI — Backtesting Archive"
type: source
created: 2026-07-13
updated: 2026-09-22
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
| GET | /api/v1/backtesting/klines | OHLCV candles, full archive | — | — |
| GET | /api/v1/backtesting/funding | Funding rates, historical | — | — |
| GET | /api/v1/backtesting/liquidations | Liquidation records, historical (venue-merged, rolling window) | symbol, start*, end, bounds, limit | — |
| GET | /api/v1/backtesting/hl-liquidations | Per-event Hyperliquid liquidation tape (exact fills: side, px, sz, USD notional, method, mark price) | coin, start*, end, bounds, limit | Pro |
| GET | /api/v1/backtesting/hl-trade-flow | Archived 1-min HL taker buy/sell buckets per perp (same shape as live minus `cvd_usd`) | coin, start*, end, bounds, limit | Pro |
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

`/backtesting/hl-trade-flow` (Pro, same tier pattern as `hl-liquidations`) archives the Hyperliquid per-coin trade tape documented live on [[cryptodataapi-hyperliquid]]: 1-minute taker buy/sell buckets per perp, forward-only from 2026-09-09. Each archived row is the live `/hyperliquid/trade-flow` bucket shape minus the served-only `cvd_usd` field (which resets per live request and is not meaningful stored). Minutes with no fills are not stored. It serves a local retention window; the full history is archived daily as the `hl_trade_flow` data type (one Parquet per day, all coins) alongside `hl_liquidations` via `/backtesting/archives` (the archive itself stays Pro Plus).

`/backtesting/hl-funding-bars` (Pro Plus, added 2026-09-19) returns Hyperliquid funding and open interest aligned to the candle clock — one row per closed bar per coin (`interval` 1h/4h/1d), with `time` equal to the matching `/hyperliquid/candles` `timestamp` so a funding/OI condition can be tested against the exact bar a price signal fires on. Per bar: `funding_sum` (carry actually settled in `(time, time + interval]`, summed across every settlement landing in the bar) with `n_settlements`; `funding_rate_mean` (mean live hourly rate over the bar's 5-min samples); `oi_open`/`oi_close`/`oi_change_pct` (base-coin units, first/last 5-min sample in the bar); `mark_close`; and `n_snapshots`. **`funding_sum: null` with `n_settlements: 0` means that day's settled prints are not yet archived — not zero carry** (settled prints are archived daily, for the previous UTC day; `funding_rate_mean` is available immediately since it doesn't depend on that archive step). Bars start **2026-03-30**: Hyperliquid publishes no historical open interest, so OI history is forward-only from CryptoDataAPI's own 5-minute capture and cannot be backfilled further back — older settled funding alone (no OI) is available further back via `/backtesting/funding?grain=hourly`. Coin list up to 25, window ≤ 93 days per call, cursor-paged, `format=csv` available.

**Backfill fix (2026-09-21):** both `/backtesting/hl-funding-bars` and `/backtesting/funding?grain=hourly` collected settled funding prints once a day for the previous day only, so a missed collector run left that day's `funding_sum: null` / `n_settlements: 0` permanently — **2026-09-12, 2026-09-13, and 2026-09-19** were affected this way. The daily job now back-fills any of the last 10 settled days it finds missing, so a single missed run self-heals within that window without manual reconciliation. No response-shape change.

## Live Data

Only `/backtesting/status` is about the present — it reports collector health so you know whether the archive is up to date. `/backtesting/symbols`, `/backtesting/snapshots/types`, and `/backtesting/archives/index` are discovery endpoints listing what is currently available to query or download.

## Historical Data

Everything else is history. `/backtesting/klines`, `/backtesting/funding`, `/backtesting/liquidations`, `/backtesting/hl-liquidations`, and `/backtesting/hl-trade-flow` query the full archive directly; `/backtesting/export` pulls a custom range; `/backtesting/archives` + `/backtesting/archives/download` hand out pre-signed URLs for bulk Parquet datasets going back to 2020; `/backtesting/archives/purchase` sells a single archived object over x402 for an agent that doesn't hold an API key at all (payment mechanics, the 404-before-quote guarantee, and the Pro-Plus-free exception are detailed on [[cryptodataapi-mcp]]'s x402 section). The point-in-time core is `/backtesting/daily-snapshots/{date}`: the API's state frozen as of that day, so a backtest on 2023-03-15 sees exactly what a live system saw on 2023-03-15. `/backtesting/signum-rgg?date=YYYY-MM-DD` is a thin wrapper over that same daily snapshot that returns just its `signum_rgg` block (universe breadth `summary` plus the full per-symbol `by_symbol` map), stored since 2026-03-02 under the same auth gate as `daily-snapshots`; `computed_from` (present on days archived from 2026-09-09 onward) marks the last completed daily bar the colours were read from — see [[cryptodataapi-indicators]] for the live SIGNUM RGG endpoints this mirrors, including the 2026-09-09 completed-bar breaking change. Regime-probability history lives separately under the Pro Plus quant endpoints on [[cryptodataapi-regimes]]. `/backtesting/news-events` (Pro Plus, detailed on [[cryptodataapi-news]]) is a shallower archive by construction: it only holds qualified catalysts, and its history starts 2026-08-18 — the day the news family shipped — and **cannot be backfilled**, because the underlying RSS sourcing only ever serves a recent window.

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
