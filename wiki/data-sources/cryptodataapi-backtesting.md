---
title: "CryptoDataAPI — Backtesting Archive"
type: source
created: 2026-07-13
updated: 2026-07-14
status: good
tags: [data-provider, crypto, api, backtesting, historical-data, point-in-time, parquet, klines, funding, liquidations]
aliases: ["CryptoDataAPI Backtesting", "CDA Backtesting", "CryptoDataAPI Historical Archive", "CryptoDataAPI Archives"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-data]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-hyperliquid]]", "[[backtesting]]", "[[backtesting-overview]]", "[[point-in-time-data]]", "[[lookahead-bias]]", "[[crypto-perp-backtesting-pitfalls]]", "[[hyperliquid-backtesting]]", "[[crypto-data-quality]]", "[[purged-kfold-cv]]", "[[deflated-sharpe-ratio]]", "[[probability-of-backtest-overfitting]]", "[[survivorship-bias]]"]
---

CryptoDataAPI's Backtesting section is the historical arm of the API: a full archive of OHLCV klines, funding rates, and liquidation records, plus dated point-in-time daily snapshots and downloadable Parquet archives reaching back to 2020. It exists so that research uses the data as it stood on each historical date — the [[point-in-time-data]] discipline that keeps [[lookahead-bias]] out of strategy results.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/backtesting/klines | OHLCV candles, full archive | — | — |
| GET | /api/v1/backtesting/funding | Funding rates, historical | — | — |
| GET | /api/v1/backtesting/liquidations | Liquidation records, historical | — | — |
| GET | /api/v1/backtesting/snapshots | Snapshot types list | — | — |
| GET | /api/v1/backtesting/snapshots/{type} | Snapshot by type, historical | type | — |
| GET | /api/v1/backtesting/symbols | Backtest-available symbols | — | — |
| GET | /api/v1/backtesting/status | Collector status | — | — |
| GET | /api/v1/backtesting/export | Export data, custom range | — | — |
| GET | /api/v1/backtesting/archives-index | Index of archives | — | — |
| GET | /api/v1/backtesting/archives | List archived datasets | — | — |
| GET | /api/v1/backtesting/archives/download | Download archive (pre-signed URL) | — | — |
| GET | /api/v1/backtesting/daily-snapshots | Daily snapshot list | — | — |
| GET | /api/v1/backtesting/daily-snapshots/{date} | Snapshot by date, point-in-time | date | — |

Historical depth: Parquet archive from 2020.

## Live Data

Only `/backtesting/status` is about the present — it reports collector health so you know whether the archive is up to date. `/backtesting/symbols`, `/backtesting/snapshots`, and `/backtesting/archives-index` are discovery endpoints listing what is currently available to query or download.

## Historical Data

Everything else is history. `/backtesting/klines`, `/backtesting/funding`, and `/backtesting/liquidations` query the full archive directly; `/backtesting/export` pulls a custom range; `/backtesting/archives` + `/backtesting/archives/download` hand out pre-signed URLs for bulk Parquet datasets going back to 2020. The point-in-time core is `/backtesting/daily-snapshots/{date}`: the API's state frozen as of that day, so a backtest on 2023-03-15 sees exactly what a live system saw on 2023-03-15. Regime-probability history lives separately under the Pro Plus quant endpoints on [[cryptodataapi-regimes]].

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
- [[backtesting-overview]], [[point-in-time-data]], [[lookahead-bias]], [[crypto-perp-backtesting-pitfalls]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
