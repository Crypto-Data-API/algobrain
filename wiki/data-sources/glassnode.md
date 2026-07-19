---
title: "Glassnode"
type: source
created: 2026-05-14
updated: 2026-06-12
status: good
tags: [data-provider, on-chain-analytics, bitcoin, ethereum, crypto]
aliases: ["Glassnode.com"]
source_type: data
source_url: "https://glassnode.com"
source_author: "Glassnode"
confidence: high
related: ["[[on-chain-analytics]]", "[[cryptoquant]]", "[[nansen]]", "[[dune-analytics]]", "[[bitcoin]]", "[[ethereum]]", "[[polymarket-as-crypto-leading-indicator]]", "[[santiment]]", "[[laevitas]]", "[[point-in-time-data]]", "[[lookahead-bias]]", "[[crypto-perp-backtesting-pitfalls]]", "[[market-regime-detection-ml]]"]
---

Glassnode is a Swiss-based [[on-chain-analytics]] provider founded in 2017, specializing in aggregated, statistically-derived indicators on [[bitcoin]], [[ethereum]], and major Layer-1 networks. It differentiates from [[nansen]] (wallet labels), [[dune-analytics]] (custom SQL), and [[cryptoquant]] (exchange-flow granularity) by focusing on derived macro metrics such as SOPR, MVRV, and Realized Cap — the kind of curated, paper-grade indicators that became the lingua franca of institutional on-chain research.

## Overview

Where most on-chain platforms surface raw block-data slices, Glassnode's edge is **derivation and curation**: turning the public ledger into a small set of named, well-documented indicators that traders, analysts, and macro funds can cite without rebuilding the math. The platform's flagship indicators (MVRV, NUPL, SOPR, HODL Waves) are now standard vocabulary in crypto research notes from sell-side desks to independent newsletters.

## Core indicator families

### Profit / loss metrics
- **SOPR** (Spent Output Profit Ratio) — ratio of realized value to value at acquisition for every spent output; >1 = aggregate profit-taking, <1 = aggregate loss-taking
- **aSOPR** — adjusted SOPR excluding outputs younger than 1 hour, filtering noise from intra-exchange movement
- **NUPL** (Net Unrealized Profit/Loss) — paper P&L of the entire supply; segmented into euphoria / greed / optimism / hope / fear / capitulation bands
- **Realized Profit/Loss** — USD value of profits/losses crystallized on-chain in a given window

### Valuation metrics
- **MVRV** — market cap divided by realized cap; long-running overvalued/undervalued gauge
- **MVRV Z-score** — MVRV normalized by historical standard deviation; widely used to mark cycle tops and bottoms
- **Realized Cap** — sum of every UTXO's value at last move; treats coin supply as a cost-basis ledger
- **Thermo Cap** — cumulative USD value of all miner rewards; floor-valuation reference

### HODLer behavior
- **Coin Days Destroyed** — weighted measure of dormant supply moving
- **HODL Waves** — supply stratified by age bands (e.g., 1y+ coins as % of supply)
- **Long-Term Holder Supply / Short-Term Holder Supply** — split at the 155-day threshold
- **LTH / STH ratios** — cohort behavior comparisons used to identify accumulation vs distribution phases

### Network activity
- **Active Addresses** — daily unique addresses transacting
- **Transaction Volume** — on-chain USD throughput
- **NVT ratio** — Network Value to Transactions; on-chain PE analogue

### Mining metrics
- **Hash Ribbons** — short/long hash-rate moving average crossovers
- **Difficulty Ribbon** — smoothed difficulty MAs marking miner-stress regimes
- **Miner Position Index** — miner outflows vs 1-year average; positive readings flag distribution

### Exchange flows
- **Exchange Inflows / Outflows** — coins moving onto / off exchanges
- **Exchange Balance** — aggregate exchange-held supply over time

## API and data access

- **REST API** — JSON or CSV responses; one endpoint per metric
- **WebSocket** — real-time streaming on the upper tiers
- **Subscription tiers** (as of 2026, verify before committing):
  - Free — heavily delayed, limited metric set
  - Advanced — roughly $30-40/mo, daily resolution on most retail metrics
  - Professional — roughly $800-900/mo, hourly/10-min resolution and the full institutional metric library
  - Enterprise — custom pricing, SLA, and direct support
- **Client libraries** — official docs target curl/Postman; community Python and R wrappers exist but are unofficial

## Relevance to "Polymarket as crypto leading indicator"

Glassnode is the natural counterparty data source when testing whether [[polymarket-as-crypto-leading-indicator]] holds:

- **Cross-validation** — when a Polymarket Fed-cut or BTC-threshold market repositions, check whether Glassnode shows corresponding exchange flow shifts or LTH accumulation. Corroboration strengthens the PM signal; absence suggests PM is leading consensus rather than reflecting flows already in motion
- **Reverse-direction check** — when on-chain accumulation patterns emerge first (e.g., MVRV exiting oversold, LTH supply rising sharply), do Polymarket BTC-threshold contracts reprice afterward? If on-chain leads PM, then PM is not the leading indicator — it is the lagging one
- **Regime classification** — Glassnode macro metrics (MVRV Z-score, NUPL band) define the regime in which PM signal correlation should be tested; PM signal strength may be regime-conditional (e.g., works during euphoria, breaks down in capitulation)

## Comparison to alternatives

| Tool | Strength | Best use vs Glassnode |
|------|----------|------------------------|
| [[cryptoquant]] | Better exchange-specific flow granularity (Binance, Coinbase splits) | Use both — overlapping but complementary |
| [[nansen]] | Wallet-level labels, real-time alerts on smart-money cohorts | Different layer of the stack; tactical vs macro |
| [[dune-analytics]] | Custom queries, flexible joins, any-table access | Build what Glassnode does not surface |

## Use cases for a crypto trading app

- **Macro regime gate** — MVRV Z-score above/below historical bands switches a portfolio between risk-on and risk-off allocations
- **HODLer capitulation detection** — sharp LTH selling pressure historically clusters near cycle bottoms; combine with aSOPR < 1.0 confirmation
- **Halving cycle context** — Realized Cap evolution provides cycle position relative to prior halvings
- **Cross-asset signal** — ETH SOPR vs BTC SOPR divergence flags rotation between the two majors

## Limitations

- Most flagship metrics are **macro/aggregated** — limited utility for intraday or short-term tactical trading
- The **free tier is heavily delayed**; serious analytical work requires Professional or higher
- Many indicators derive from **public chain data** and can be reproduced via [[dune-analytics]] — Glassnode's value is curation, documentation, and consistency, not exclusive data access
- Some classic indicators (notably **NVT**) have decayed in signal quality as DeFi, Layer-2s, and off-chain settlement fragment the on-chain footprint of economic activity
- Indicator methodology occasionally changes; historical backtests should re-pull data rather than rely on cached series

## Point-in-Time Data

Glassnode is one of the few crypto data providers that publishes its on-chain metrics as **versioned, immutable [[point-in-time-data|point-in-time (PiT)]] snapshots**. A PiT snapshot freezes every metric value as it was computed at the historical moment in question — no retroactive revisions are silently applied to past observations.

This matters because most on-chain metrics are *derived* from heuristics and labels that get updated continuously:

- **Entity tags**: a wallet labeled "Binance cold wallet" today may not have been labeled at all in 2022. Backtesting with current data introduces future knowledge.
- **Exchange wallet classifications**: clusters get re-classified, merged, or split as on-chain forensics improves.
- **Coin-age based metrics (NUPL, MVRV, Realized Cap)**: depend on the exact UTXO graph snapshot at compute time; small revisions to the cost-basis model retroactively shift levels by 1-3% across history.

Backtests built on the *current-as-of-today* version of a metric inherit a subtle but devastating form of [[lookahead-bias]]. Glassnode's PiT API exposes the metric as it stood at any historical timestamp `t`. A naive backtest on revised data can show a 1.5x Sharpe inflation on entity-flow-based strategies. See [[crypto-perp-backtesting-pitfalls]] for the broader catalogue of crypto-specific lookahead traps.

## Backtesting Use Cases

- **On-chain feature engineering with PiT discipline**: build features (exchange-inflow z-score, long-term-holder supply changes, miner-position index) using the PiT API so signals reflect what was knowable at decision time. Pair with [[walk-forward-optimization]] for an honest validation pipeline.
- **Regime detection inputs**: NUPL, MVRV Z-Score, and Puell Multiple are common state variables for [[market-regime-detection-ml|ML-based regime detection]] models (HMMs, k-means on standardised metrics). PiT versioning is essential here.
- **Survivorship-bias correction**: Glassnode covers tokens that have since fallen out of the top-50, including pre-collapse history for failed projects. See [[survivorship-bias]].
- **Stress-testing on real flow shocks**: the October 10-11, 2025 cascade and April 2026 incidents are both reflected in Glassnode flow data.
- **Cross-validating funding-rate strategies**: combining Glassnode exchange-balance flows with [[coinglass]] funding/OI data produces a more robust signal than either source alone.

## Notable use in historical episodes

- LTH Supply distributions tracked the 2021 ATH distribution wave and the 2022 capitulation cohort transfer
- aSOPR breaks below 1.0 have historically clustered around late-cycle bear bottoms, marking the point where the average spent coin moves at a loss

## Related

- [[on-chain-analytics]]
- [[cryptoquant]]
- [[nansen]]
- [[dune-analytics]]
- [[bitcoin]]
- [[ethereum]]
- [[polymarket-as-crypto-leading-indicator]]

## Sources

- Glassnode Studio documentation (https://docs.glassnode.com)
- Glassnode Academy methodology pages for SOPR, MVRV, NUPL, HODL Waves
