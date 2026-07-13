---
title: "Glassnode"
type: entity
created: 2026-04-06
updated: 2026-05-05
status: good
tags: [data-provider, crypto, on-chain, bitcoin]
entity_type: company
website: https://glassnode.com
related:
  - "[[nansen]]"
  - "[[santiment]]"
  - "[[laevitas]]"
  - "[[point-in-time-data]]"
  - "[[lookahead-bias]]"
  - "[[crypto-perp-backtesting-pitfalls]]"
  - "[[market-regime-detection-ml]]"
---

# Glassnode

## Overview

The premier on-chain analytics platform for Bitcoin and crypto fundamentals. Glassnode provides 200+ on-chain metrics that let you analyze blockchain activity the way fundamental analysts study company financials. Their core insight: Bitcoin's blockchain is a transparent ledger, so you can study holder behavior, supply dynamics, miner economics, and exchange flows to gauge where markets are in a cycle. If [[nansen]] is about WHO is transacting, Glassnode is about WHAT the aggregate market is doing on-chain.

## Pricing

- **Free**: limited metrics with 24-hour resolution, basic charts, no API
- **Advanced**: ~$500/mo -- full metric library, hourly resolution, API access, alerts
- **Professional**: ~$800+/mo -- tick-level data, priority API, institutional reports, custom dashboards
- Academic and startup programs available with discounted rates

## What You Get (vs Free)

- Full library of 200+ metrics (free tier shows ~30 at daily resolution only)
- Hourly and 10-minute resolution data (free is 24h only -- useless for trading)
- Full historical data going back to Bitcoin's genesis block
- API access for programmatic data pulls into trading systems and [[backtesting]] frameworks
- Workbench: custom metric builder for combining and transforming on-chain signals
- Alerts on metric thresholds (e.g., notify when exchange inflows spike above 2 standard deviations)
- Institutional research reports (The Week On-Chain)

## Alpha Edge

- **Cycle identification**: metrics like NUPL (Net Unrealized Profit/Loss), MVRV Z-Score, and Puell Multiple have historically identified Bitcoin macro tops and bottoms with high accuracy
- **Exchange flows**: net exchange inflows precede sell-offs; large outflows signal accumulation. This is one of the most reliable short-term signals in crypto
- **Supply analysis**: tracking coins held by long-term holders vs. short-term holders reveals when experienced investors are distributing to new buyers (late-cycle behavior)
- **SOPR (Spent Output Profit Ratio)**: shows whether coins being moved are in profit or loss -- resets to 1.0 act as support in bull markets
- **Miner behavior**: miner revenue, hash rate, and miner outflows to exchanges signal capitulation or accumulation phases

## Key Features

- **Glassnode Studio**: interactive charting with 200+ on-chain, derivatives, and market metrics
- **Workbench**: build custom metrics using formulas across any combination of existing metrics
- **Alerts**: threshold-based notifications on any metric via email or Telegram
- **API**: RESTful API returning JSON -- integrates with Python, R, and trading platforms
- **The Week On-Chain**: flagship weekly research report breaking down current market structure
- **Dashboards**: pre-built views for Bitcoin, Ethereum, stablecoins, DeFi, and mining

## Who Uses It

- Bitcoin-focused macro traders timing cycle entries and exits
- Crypto hedge funds integrating on-chain signals into quantitative models
- Long-term investors using on-chain fundamentals for accumulation/distribution decisions
- Researchers and analysts publishing on-chain market commentary
- Mining operations monitoring hash rate economics and miner profitability
- Anyone who believes understanding [[bitcoin]] supply dynamics gives an edge over pure price action

## Point-in-Time Data

Glassnode is one of the few crypto data providers that publishes its on-chain metrics as **versioned, immutable [[point-in-time-data|point-in-time (PiT)]] snapshots**. A PiT snapshot freezes every metric value as it was computed at the historical moment in question — no retroactive revisions are silently applied to past observations.

This matters because most on-chain metrics are *derived* from heuristics and labels that get updated continuously as analysts learn more about the network:

- **Entity tags**: a wallet that today is labeled "Binance cold wallet" may not have been labeled at all in 2022. If your backtest queries the *current* exchange-balance metric for a 2022 trade, you are using future knowledge.
- **Exchange wallet classifications**: clusters get re-classified, merged, or split as on-chain forensics improves. A spike in "exchange inflows" computed today may not have existed in the dataset traders had at the time.
- **Smart-contract labels (DeFi)**: protocol address sets get expanded as new versions deploy; TVL calculations on revised data systematically overstate adoption rates in early periods.
- **Coin-age based metrics (NUPL, MVRV, Realized Cap)**: depend on the exact UTXO graph snapshot at compute time; small revisions to the cost-basis model retroactively shift levels by 1-3% across history.

Backtests built on the *current-as-of-today* version of a metric inherit a subtle but devastating form of [[lookahead-bias]]. Glassnode's PiT API exposes the metric as it stood at any historical timestamp `t`, so a strategy can be simulated using only information that genuinely existed at `t`. This is the same discipline that equity quants apply with PiT fundamental data ([[survivorship-bias|survivorship-bias-free]] datasets from Compustat / S&P Capital IQ) — Glassnode brings it to crypto on-chain.

A naive backtest on revised data can show a 1.5x Sharpe inflation on entity-flow-based strategies, per Glassnode's own published research. See [[crypto-perp-backtesting-pitfalls]] for the broader catalogue of crypto-specific lookahead traps.

## Use Cases for Backtesting

- **On-chain feature engineering with PiT discipline**: build features (exchange-inflow z-score, long-term-holder supply changes, miner-position index) using the PiT API so signals reflect what was knowable at decision time. Pair with [[walk-forward-optimization]] for an honest validation pipeline.
- **Regime detection inputs**: NUPL, MVRV Z-Score, and Puell Multiple are common state variables for [[market-regime-detection-ml|ML-based regime detection]] models (HMMs, k-means on standardised metrics). PiT versioning is essential here — a regime classifier trained on revised metrics will mis-label historical regimes and overstate forward-looking accuracy.
- **Survivorship-bias correction**: Glassnode covers tokens that have since fallen out of the top-50, including pre-collapse history for failed projects (Terra/LUNA, FTT). Including these in cross-sectional backtests is necessary to avoid the upward-biased returns of a "BTC + ETH + whatever's in the top-10 today" universe. See [[survivorship-bias]].
- **Stress-testing on real flow shocks**: the October 10-11, 2025 cascade and the April 2026 Aave/KelpDAO incident are both reflected in Glassnode flow data; replaying those windows is more informative than synthetic Monte Carlo for tail-event sizing.
- **Cross-validating funding-rate strategies**: combining Glassnode exchange-balance flows with [[coinglass]] funding/OI data produces a more robust signal than either source alone — a [[funding-rate-arbitrage]] strategy that ignores spot-side flows missed the 2025 funding compression early.
