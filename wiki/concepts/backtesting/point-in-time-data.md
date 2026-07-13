---
title: "Point-in-Time Data"
type: concept
created: 2026-05-05
updated: 2026-07-13
status: good
tags: [backtesting, data-provider, methodology, crypto, risk-management]
aliases: ["PiT Data", "Point in Time Data", "Vintage Data", "As-Of Data"]
domain: [backtesting]
difficulty: intermediate
related: ["[[lookahead-bias]]", "[[selection-bias-research]]", "[[glassnode]]", "[[coinapi]]", "[[kaiko]]", "[[crypto-perp-backtesting-pitfalls]]", "[[backtesting-pitfalls]]", "[[execution-model-differences]]", "[[cryptodataapi]]"]
---

# Point-in-Time Data

Point-in-time (PiT) data is data captured *as it was known at the time*, not as it appears in the database today. The distinction is structural rather than cosmetic: data is constantly revised, relabeled, restated, and reclassified after the fact, and a backtest that joins to "the latest version of the truth" silently consumes information that did not exist at the decision moment. This is especially severe for on-chain crypto metrics, where wallet labels and exchange tags are continuously updated as analytics vendors discover new clusters.

## Why PiT Matters

A backtest is a simulation of a decision-maker who knew only what was knowable at time `t`. If your features at time `t` were computed from a dataset that has since been corrected, expanded, relabeled, or backfilled, you are simulating an oracle, not a trader. The result is a structural form of [[lookahead-bias]] — not a coding bug, not an off-by-one error, but a vendor-side rewrite of history that happens *underneath* an otherwise clean pipeline.

PiT discipline is the answer. Every feature in a backtest needs a vintage stamp: "this is the value of metric X at time `t` *as it was knowable on date `t`*, not as it appears in today's snapshot." Without that, claims about historical edge are claims about a counterfactual where the trader had access to the future.

The Glassnode research framing is direct: backtests run on revised on-chain data systematically overperform their honest equivalents because the revisions are correlated with future price moves (Source: insights.glassnode.com/why-use-point-in-time-data).

## Examples of Revised Data in Crypto

On-chain data is among the worst offenders because the underlying blockchain is immutable but the *interpretation layer* is constantly changing.

- **Glassnode entity labels backfilled.** When Glassnode identifies a new exchange cluster (e.g., a previously unlabeled set of wallets later confirmed as Binance hot wallets), historical "exchange balance" series are retroactively updated to include those wallets. The series for January 2023 looks different in 2024 than it did in 2023.
- **Exchange wallet reclassifications.** A wallet labeled "OKX cold storage" in 2024 may be reclassified as "OKX user-held" or "Bybit hot wallet" once a deposit/withdrawal pattern is more fully clustered. Any feature using `exchange_balance` or `net_exchange_flow` inherits this revision.
- **Token reclassifications post-rebrand.** When MATIC migrated to POL, every series indexed by ticker had to be reconciled. Backtests joining current symbol → historical price often inherit lookahead because the *current* symbol implicitly encodes the survival/rebrand.
- **DeFi protocol contract upgrades.** TVL, deposit, and borrow series for protocols like Aave and Compound get adjusted when new contract versions deploy and historical data is migrated; the "Aave TVL on 2024-01-01" you read today is a stitched series.
- **Stablecoin issuer labels.** Tether's bank/custody labeling has been revised multiple times; series like "stablecoin issuer net mint" are essentially version-dependent.
- **Liquidation tagging.** Exchange liquidation feeds (Binance, Bybit) are sometimes corrected days later as failed-trade and self-trade entries are filtered out.

## Examples in TradFi

The same problem exists in equities, just better-known:

- **Restated earnings.** A Q4 2013 earnings number reported March 2014 might be restated in 2017. The version in Yahoo Finance today is the restated version.
- **Index constituent revisions.** S&P 500 membership lists at historical dates differ from current lists; bankrupt or acquired names are dropped from the "today's S&P 500" view.
- **Macro revisions.** GDP, CPI, and nonfarm payrolls all get revised. ALFRED (Archival FRED) provides the vintage; FRED itself does not.
- **Analyst estimates.** IBES timestamps are often the database-insertion date, not the broker-publication date.

See [[lookahead-bias]] for the full taxonomy of leakage sources; this page focuses on the *data-vintage* axis specifically.

## How Vendors Handle PiT

Not all data sources are PiT-compliant. The relevant question for any vendor is whether you can ask "what did this metric show on date `t`, as known on date `t`?" and get a deterministic answer.

- **[[glassnode]] versioned snapshots.** Glassnode publishes PiT versions of their on-chain metrics with a `point_in_time=true` flag on the API; a separate "v1 immutable" archive preserves the values as originally computed at each timestamp.
- **[[coinapi]] immutable trade history.** CoinAPI's flat-file trade and order-book archives are append-only; published research from CoinAPI on survivorship-bias correction also includes guidance on vintage handling for delisted instruments.
- **[[kaiko]] tick-level archives.** Kaiko's institutional product preserves raw exchange messages, so reconstructions are deterministic from the raw feed; revisions to derived metrics can be re-computed without contaminating the raw layer.
- **Compustat / S&P Capital IQ Point-in-Time.** The TradFi reference for PiT fundamentals; provides "as-first-reported" and "as-restated" versions side-by-side.
- **ALFRED (Archival FRED).** Free vintage macro data — every release of every series at every date.

Free data sources (Yahoo, CoinGecko free tier, Glassnode free tier) almost never provide PiT versioning. If your data is free, it is almost certainly *not* PiT.

## How to Audit Your Data

Concrete checks before trusting any feature:

1. **Vintage timestamps.** For every label, every entity tag, every classification — when was it first applied? If the answer is "we don't track that," the feature is not safe for backtests.
2. **Re-pull diff.** Cache a snapshot of your data, wait 30-60 days, re-pull the same query, and diff. Any non-trivial difference in historical values means your vendor revises silently. Quantify the magnitude.
3. **Version pinning.** If the vendor exposes versioning (Glassnode `metric_version`, Compustat PIT version IDs), pin to the version that existed at the original computation date.
4. **Symbol / ticker stability.** Walk every ticker in your universe back through any reclassification (rebrands, splits, migrations). Identifier stability is a precondition for honest backtests.
5. **Asymmetric revisions.** Check whether revisions are mean-zero across the panel. If revisions correlate with subsequent returns (positive revisions follow up-days), your backtest will overstate edge mechanically.

## Implementing PiT in Backtests

The structural rule: **never join historical features to a "latest labels" table**. Concretely:

- **Snapshot-as-of queries.** Store every feature as `(entity_id, valid_from, valid_to, value)` and query with `WHERE t BETWEEN valid_from AND valid_to`. This is the bitemporal-database pattern; libraries like `pytables`, kdb+, and TimescaleDB support it natively.
- **Vintage-stamped feature stores.** Each feature row carries `(observation_time, knowable_time, value)`; the backtest filters on `knowable_time <= decision_time`.
- **Forward-only feature computation.** Compute features causally from raw data, one bar at a time, with no reference to future bars. Slower than vectorized computation, but mechanically PiT-safe.
- **Frozen archives.** For irreproducible features (e.g., third-party scores, analyst estimates), download once at the historical date and treat the archived file as ground truth. Never re-pull.

## Common Bugs

- **Using current ticker symbols on historical data.** A query that says "give me daily closes for SOL since 2020" silently filters to instruments that *currently* trade as SOL; delisted forks, rebrands, and merged tickers are excluded. This is [[selection-bias-research|survivorship-bias adjacent]] and equally damaging.
- **"Latest labels" joins.** Joining a historical price table to a current `entity_labels` table propagates today's clustering decisions into yesterday's features.
- **Forward-filled missing data.** Innocuous if the gap really was missing in real time, lookahead if the value was filled from a later vintage.
- **TTM / rolling-window fields.** Derived fields like trailing-twelve-month earnings or 30-day average funding rate may secretly include restated components.
- **"As-of-now" feature engineering.** Code that says `df['feature'] = df.groupby('asset').transform(...)` over the whole panel can leak future information unless the transform is strictly causal.
- **Re-pulled price data with adjustments.** Splits, dividends, and rebases get applied retroactively; today's pull of a 2022 close may not equal the 2022 pull.

A useful diagnostic from [[lookahead-bias]]: shift every input feature forward one bar and re-run. If Sharpe drops more than ~30%, you had a data-vintage leak somewhere.

## Sources

- [Glassnode — Why Use Point-in-Time Data](https://insights.glassnode.com/why-use-point-in-time-data/) — definitive explanation of PiT data for on-chain analytics and how revised entity labels create lookahead bias in crypto backtests
- [CoinAPI — How to Eliminate Survivorship Bias in Crypto Backtesting](https://www.coinapi.io/blog/how-to-eliminate-survivorship-bias-in-crypto-backtesting) — vintage handling for delisted instruments and immutable trade archives
- [Corporate Finance Institute — Look-Ahead Bias](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/look-ahead-bias/) — TradFi framing of PiT fundamentals and restated-data leakage

## Getting the Data (CryptoDataAPI)

**Historical archive:**
- `GET /api/v1/backtesting/klines` — OHLCV candle archive
- `GET /api/v1/backtesting/funding` — funding-rate archive
- `GET /api/v1/backtesting/liquidations` — liquidation records archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshot
- `GET /api/v1/backtesting/archives` — Parquet dataset archive (since 2020)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/symbols"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-backtesting]].

## Related

- [[lookahead-bias]]
- [[selection-bias-research]]
- [[glassnode]]
- [[coinapi]]
- [[kaiko]]
- [[crypto-perp-backtesting-pitfalls]]
- [[backtesting-pitfalls]]
- [[execution-model-differences]]
