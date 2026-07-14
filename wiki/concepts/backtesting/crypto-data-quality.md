---
title: "Crypto Data Quality"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [backtesting, crypto, data-provider, methodology, market-microstructure, point-in-time]
aliases: ["Crypto GIGO Checklist", "Crypto Backtest Data Quality", "Crypto Data Cleaning"]
domain: [backtesting]
prerequisites: ["[[point-in-time-data]]", "[[lookahead-bias]]"]
difficulty: intermediate
related: ["[[crypto-perp-backtesting-pitfalls]]", "[[wash-trading]]", "[[point-in-time-data]]", "[[lookahead-bias]]", "[[survivorship-bias]]", "[[selection-bias-research]]", "[[hypothesis-to-backtest-workflow]]", "[[depeg-risk]]", "[[hyperliquid-backtesting]]", "[[cryptodataapi-backtesting]]", "[[regime-conditional-validation]]", "[[crypto-short-history-statistical-power]]"]
---

# Crypto Data Quality

Garbage in, garbage out. A crypto backtest is only as trustworthy as the price, volume, funding, and on-chain series feeding it, and crypto data is *dirtier by default* than equity data: no consolidated tape, no regulator forcing print accuracy, exchanges that fabricate volume, venues that vanish, and an interpretation layer (on-chain labels) that is silently rewritten. This page is a single **GIGO checklist** — seven corruption modes, each with *how it corrupts a backtest* and *how to detect and filter it* — meant to be run before any result from [[hypothesis-to-backtest-workflow]] is believed. It is the data-hygiene companion to [[crypto-perp-backtesting-pitfalls]], which covers the perp-mechanics side.

## The Checklist at a Glance

| # | Corruption mode | What it fakes | Primary defense |
|---|-----------------|---------------|-----------------|
| 1 | Wash-traded volume | Volume, VWAP, liquidity, momentum | Distrust venue; use adjusted volume; depth cross-check |
| 2 | Outages / API gaps / missing bars | Continuity, fills, gap returns | Gap audit; forward-fill flags; multi-source |
| 3 | Timestamp & clock-skew misalignment | Cross-venue causality, look-ahead | Normalise to UTC ms; align to event time |
| 4 | Low-float listing distortions | Early-life returns, volatility | Exclude launch window; float-aware universe |
| 5 | Stablecoin-depeg artifacts | USD-denominated PnL, collateral value | Use real quote unit; flag depeg windows |
| 6 | Revised on-chain data | Point-in-time feature values | Vintage stamps; as-of joins |
| 7 | Dead-token survivorship | Universe returns, win rate | Include delisted set; point-in-time universe |

## 1. Wash-Traded Volume

**How it corrupts a backtest.** [[wash-trading|Wash trading]] — self-matched buy/sell with no change in beneficial ownership — inflates reported volume without real liquidity. A 2019 Bitwise report to the SEC estimated **~95% of reported Bitcoin volume on unregulated exchanges was fake**; the Blockchain Transparency Institute put 80%+ of top-100 exchange volume as wash-traded. Any signal built on volume inherits the lie: **VWAP** anchors to prices that never absorbed size, **volume-breakout** and **on-balance-volume** signals fire on manufactured activity, **liquidity/ADV** estimates overstate the size you can trade, and **momentum** ranks light up for coins whose "interest" is a bot trading itself. A strategy fitted on wash-traded pairs looks liquid and tradeable in-sample and evaporates on live fills.

**How to detect and filter.**
- **Distrust the venue, not just the print.** Prefer verifiable venues (Binance, Coinbase, Kraken, and on-chain-transparent Hyperliquid) over low-cap CEXs and self-trading DEX pools. See [[wash-trading#Backtesting data-quality impact]].
- **Volume-vs-depth ratio.** Genuine volume correlates with order-book depth and realised price impact; wash-traded pairs show high volume against a thin book. Flag pairs where `volume / top-of-book depth` is an extreme outlier.
- **Use adjusted/real-volume feeds** (Messari, The Block, Kaiko) rather than raw exchange self-reports.
- **Statistical fingerprints.** Suspiciously uniform trade sizes, round-number clustering, and buy/sell size symmetry are wash-trade tells.

## 2. Exchange Outages, API Gaps, and Missing Bars

**How it corrupts a backtest.** Crypto venues go down (maintenance, overload during crashes, DDoS) and APIs drop bars. Two failure shapes result: a **silent gap** (missing rows the backtester skips over, so a strategy "holds" through a period it could not have traded) and a **forward-filled artifact** (a data vendor repeats the last price, creating a flat line that suppresses volatility and hides a real gap). Both are worst *exactly when it matters* — venues stall during the highest-volatility windows, so the backtest smooths over the March 2020, May 2022, and October 2025 stress moments where fills were impossible or catastrophic. Gap-return calculations (`close[t]/close[t-1]`) also explode across a gap boundary, injecting fake outsized returns.

**How to detect and filter.**
- **Bar-count audit.** For a fixed interval, assert the expected number of bars per day (e.g. 24 hourly, 1440 minute bars). Any shortfall is a gap — log it, don't interpolate silently.
- **Flag, don't fill.** If you forward-fill, carry an explicit `is_synthetic` flag and forbid trading on synthetic bars.
- **Detect frozen prices.** A run of identical OHLC values across many bars usually means a vendor forward-fill or a halted venue, not calm — treat as missing.
- **Cross-source reconciliation.** Compare two independent feeds; divergence or one-sided gaps localise the outage. During known outage windows, mark the strategy flat or unfillable rather than assuming continuous execution.

## 3. Cross-Venue Timestamp and Clock-Skew Alignment

**How it corrupts a backtest.** Every venue stamps trades on its own clock, in its own timezone convention and resolution (seconds vs milliseconds), with its own ingestion latency. Joining Binance spot to a Hyperliquid perp to an on-chain event without normalising means events appear to happen in the wrong order — and *out-of-order events are look-ahead bias in disguise*: if venue A's clock runs 500 ms ahead, a cross-venue arb signal can "see" A's move before B and print an edge that is pure timestamp artefact. On low-timeframe strategies (sub-minute), a few hundred milliseconds of skew is the entire signal.

**How to detect and filter.**
- **Normalise everything to UTC milliseconds** at ingestion; store the raw exchange timestamp *and* the receipt timestamp separately.
- **Align to a common event clock**, not to wall-clock bar boundaries, when comparing venues.
- **Measure skew empirically** against a shared reference (e.g. a widely-traded pair) and correct or embargo the offset before any cross-venue join.
- **Respect availability lag.** A bar or on-chain feature is only usable once it was actually *received*, not once it was *timestamped*. See [[lookahead-bias]] and [[point-in-time-data]].

## 4. Low-Float Listing Distortions

**How it corrupts a backtest.** New listings — especially low-float, high-FDV tokens — trade abnormally in their first hours to days: extreme volatility, thin depth, price discovery dominated by a handful of orders, and frequent reflexive squeezes. A backtest that treats launch-window bars as normal will (a) overstate momentum/volatility edges that are really just launch chaos, (b) assume fills that the thin book could never provide, and (c) let a few explosive early prints dominate the whole return series. The distortion is structural: circulating float is a small fraction of FDV, so ordinary flow moves the mark disproportionately.

**How to detect and filter.**
- **Exclude a launch embargo** — drop the first N days (or until liquidity/float crosses a threshold) from research and trading.
- **Float-aware universe rules.** Filter by circulating supply and realistic depth, not just market cap or FDV, and reconstruct that membership point-in-time (§7).
- **Winsorise or flag early prints** so a single launch candle cannot carry a strategy's Sharpe.
- **Separate listing behaviour** into its own regime rather than pooling it with mature-market data (see [[regime-conditional-validation]]).

## 5. Stablecoin-Depeg Data Artifacts

**How it corrupts a backtest.** Most crypto pairs are quoted in USDT/USDC/DAI, and backtests silently assume `1 stablecoin = $1`. During a depeg that assumption is false and corrupts data two ways. First, **PnL denomination**: a strategy quoted in USDT during a Tether wobble mis-measures USD returns. Second, **collateral value**: **USDC fell to ~$0.877 on 11 March 2023** after the SVB disclosure, and **UST bottomed near $0.06 in May 2022** — a position collateralised in the depegging asset loses on the trade *and* the collateral simultaneously. A further artefact: quote-currency depegs can make an asset's stablecoin price spike or crater purely because the *denominator* moved, faking a signal that never happened in USD terms. See [[depeg-risk]].

**How to detect and filter.**
- **Track the stablecoin's own USD price**, not just the pair. When the quote asset deviates from $1 beyond a tolerance, flag the window.
- **Reprice into a stable reference** (or an index of stablecoins) during depeg windows so returns reflect USD, not the denominator's move.
- **Model collateral haircuts** in depeg windows rather than valuing USDC/USDT at par.
- **Keep the depeg episodes as explicit stress windows** in the validation playbook (see [[crypto-perp-backtesting-pitfalls]]).

## 6. Revised On-Chain Data (Point-in-Time)

**How it corrupts a backtest.** The blockchain is immutable, but the *interpretation layer* is not. Entity labels, exchange-address clusters, contract tags, and MVRV/dormancy classifications are revised continuously as analytics providers relabel addresses. A feature like `exchange_net_inflow` for January 2024 reads differently in 2026 than it did in real time, because addresses were reclassified after the fact. Training on *today's* labels applied to *past* dates is a textbook [[lookahead-bias|look-ahead]] leak — the model learns from knowledge that did not exist at decision time, and the edge vanishes live.

**How to detect and filter.**
- **Vintage every feature.** Each on-chain value carries the as-of date on which that value was computed; joins use **as-of semantics**, never latest-labels. See [[point-in-time-data]].
- **Prefer dated snapshots** over recomputed history — query the archive as it stood on each date rather than a single current pull.
- **Sanity-check against price causality.** If an on-chain "leading" signal only leads *after* a relabel, suspect leakage.
- **Freeze the label set** used in a study and document its vintage in the strategy page.

## 7. Dead-Token Survivorship

**How it corrupts a backtest.** Delisted tokens, dead exchanges, and bankrupt venues drop out of most "historical" datasets, so a universe reconstructed today contains only survivors. This inflates returns dramatically: survivorship bias can overstate backtested crypto returns by roughly **200–400%**, and a worked "buy the top-20 alts" example showed **+2,800% with the bias vs +680% corrected**. Academic work on 3,904 cryptos (2014–2021) put the survivorship-and-delisting bias at ~0.93% annualised value-weighted, ballooning to **62.19% equal-weighted**. FTX (Nov 2022) took a complete contract history with it; Mango Markets (shut Jan 2025) and other dead DEXs simply vanish from snapshot pulls. Win rates and momentum edges look far better than reality because the losers were deleted. See [[survivorship-bias]] and [[selection-bias-research]].

**How to detect and filter.**
- **Build the universe point-in-time.** "Top-N as of each historical date," reconstructed from dated snapshots, not "top-N today" back-applied.
- **Include the dead set explicitly** — delisted tokens, rugged low-caps, and shuttered-venue contracts, marked to their true delisting/zero.
- **Cross-check roster size over time.** A universe whose historical membership exactly matches today's tickers is survivorship-biased by construction.
- **Model delisting as a return event** (often a large negative), not a silent disappearance.

## The Data-Trust Order of Operations

Run these gates before trusting *any* crypto series, in order:

1. **Source** — is the venue credible, and is the volume real (§1)?
2. **Completeness** — are there gaps, outages, or frozen bars (§2)?
3. **Alignment** — are timestamps UTC-normalised and skew-corrected (§3)?
4. **Universe** — is it point-in-time and survivorship-free (§4, §7)?
5. **Denomination** — is the quote/collateral unit actually worth $1 (§5)?
6. **Vintage** — are on-chain features as-of, not relabelled (§6)?

A series that clears all six is *clean enough* to feed the statistical machinery — and even then, crypto's short history limits how much any clean sample can prove (see [[crypto-short-history-statistical-power]]).

## Getting the Data (CryptoDataAPI)

CryptoDataAPI's backtesting archive is built for the point-in-time discipline these checks require:

- **Point-in-time universe & snapshots** — `GET /api/v1/backtesting/daily-snapshots/{date}` (state frozen as of that day), `GET /api/v1/backtesting/symbols` (what was tradeable) for survivorship-free rosters
- **Volume sanity** — `GET /api/v1/market-data/volume-history?days=90` (daily volume + buy ratio) and `GET /api/v1/liquidity/depth` to cross-check volume against real book depth
- **Clean archives** — `GET /api/v1/backtesting/klines`, `GET /api/v1/backtesting/funding`, `GET /api/v1/backtesting/liquidations`, plus Parquet via `GET /api/v1/backtesting/archives` (since 2020)
- **Stablecoin denomination** — `GET /api/v1/sentiment/stablecoins/history` to detect depeg windows in the quote unit
- **Collector status** — `GET /api/v1/backtesting/status` reveals gaps/outages in the archive itself

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/daily-snapshots/2023-03-11"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-backtesting]].

## Related

- [[crypto-perp-backtesting-pitfalls]] — the perp-mechanics companion to this data-hygiene page
- [[wash-trading]] — venues to distrust and how fake volume corrupts signals
- [[point-in-time-data]], [[lookahead-bias]] — the discipline behind §3 and §6
- [[survivorship-bias]], [[selection-bias-research]] — the §7 failure mode
- [[depeg-risk]] — the §5 collateral and denomination risk
- [[regime-conditional-validation]] — why launch and depeg windows are separate regimes
- [[crypto-short-history-statistical-power]] — why even clean data can't prove much
- [[hyperliquid-backtesting]] — venue-specific data sourcing (L2 archives, funding)
- [[hypothesis-to-backtest-workflow]] — where the cleaned data is consumed
- [[cryptodataapi-backtesting]] — the point-in-time archive endpoints
