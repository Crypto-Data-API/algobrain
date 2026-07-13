---
title: "Data Management (Trading Systems)"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [technology, backtesting, data-provider, quantitative]
aliases: ["Data Management", "Market Data Management", "Tick Store"]
domain: [market-microstructure]
related:
  - "[[databento]]"
  - "[[data-sources-overview]]"
  - "[[backtesting]]"
  - "[[survivorship-bias]]"
  - "[[look-ahead-bias]]"
  - "[[quantitative]]"
  - "[[deployment]]"
---

Data management is the engineering discipline of acquiring, cleaning, storing, and serving market and reference data so that research and live trading consume the *same*, *correct*, *point-in-time* data. In quant trading, data quality and data plumbing are a more common cause of failed strategies than bad models — a backtest is only as trustworthy as the data behind it.

## The Core Problems

- **Point-in-time correctness** — the data must reflect what was *knowable at the time*. Fundamentals get restated, index membership changes, and tickers get reused; a database that overwrites history silently injects [[look-ahead-bias|look-ahead bias]].
- **[[survivorship-bias|Survivorship bias]]** — delisted and bankrupt names must remain in the universe, or backtests overstate returns by excluding the losers.
- **Corporate actions** — splits, dividends, mergers, and ticker changes must be applied consistently to build accurate adjusted price series.
- **Time alignment & timezones** — bars, quotes, and events from multiple venues must share a coherent clock (UTC, exchange session boundaries).
- **Gaps and bad ticks** — missing data, fat-finger prints, and crossed quotes need detection and cleaning rules that are themselves point-in-time.
- **Research/production parity** — the feature pipeline used in backtests must match the one used live, or the strategy behaves differently in production.

## Storage Patterns

| Need | Typical tooling |
|---|---|
| Tick / order-book data | kdb+, ClickHouse, Arctic/MongoDB, Parquet on object storage |
| Bars / daily OHLCV | Parquet, DuckDB, TimescaleDB, SQLite for small projects |
| Fundamentals / reference | Postgres with point-in-time (bitemporal) tables |
| Feature store | Parquet/feature-store libs; versioned to match model training |
| Real-time cache | Redis / in-memory ring buffers for live signals |

Columnar formats (Parquet, ClickHouse, kdb+) dominate because trading queries are overwhelmingly column-oriented scans over time ranges.

## Pipeline Stages

1. **Ingest** — pull from vendors ([[databento]], EDGAR via [[edgar]], exchange feeds; see [[data-sources-overview]]) with idempotent, resumable jobs.
2. **Validate** — schema checks, gap detection, outlier flags, cross-vendor reconciliation.
3. **Normalize** — unified symbology (map across vendor IDs, CUSIP/FIGI), apply corporate actions, build adjusted series.
4. **Store** — write immutable, versioned, point-in-time datasets.
5. **Serve** — a single data-access layer that research and live trading share, so [[backtesting]] and [[deployment]] read identical data.

## Trading Relevance

Most "alpha decay" surprises trace to data: a backtest used split-adjusted prices that weren't knowable, or used a current index constituent list, or had future fundamentals leak in. Disciplined data management — point-in-time everything, delisted names retained, one shared access layer — is what separates a backtest you can trust from a number-generating toy. It is the unglamorous foundation under every [[quantitative]] strategy.

## Related

- [[databento]] — a normalized market-data source
- [[edgar]] — fundamentals/filings source
- [[data-sources-overview]] — provider catalog
- [[backtesting]] — the primary consumer of clean historical data
- [[survivorship-bias]] / [[look-ahead-bias]] — the failure modes data management prevents
- [[deployment]] — research/production data parity in live systems

## Sources

- General knowledge of quant data engineering; tooling references (kdb+, ClickHouse, Arctic, Parquet). No raw sources ingested yet.
