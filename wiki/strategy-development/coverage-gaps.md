---
title: "Coverage Gaps — Strategy-Creation Fill Plan"
type: index
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [meta, strategy-development, roadmap]
---

# Coverage Gaps — Strategy-Creation Fill Plan

Tracking doc for filling the gaps found in the 2026-07-14 gap analysis of the crypto strategy-creation workflow. Scope is deliberately the *value-bearing* gaps: genuinely missing pages plus crypto-native essays that need buildable depth — **not** blind reformatting of chart-pattern/options-spread reference pages (Elliott wave, Fibonacci, iron condor, etc.), which stay as reference essays.

## Wave 1 — new pages + named high-value rewrites (39 pages)

**Signal & feature engineering (front of funnel):** [[feature-engineering-crypto]], [[crypto-signal-library]], [[information-coefficient]], [[signal-orthogonalization]], [[feature-selection-trading]], [[meta-labeling]], [[triple-barrier-labeling]], [[fractional-differentiation]], [[composite-alpha-blending]], [[ml-crypto-price-prediction]].

**Idea generation & validation:** [[crypto-idea-generation]], [[crypto-data-quality]], [[regime-conditional-validation]], [[crypto-short-history-statistical-power]], [[crypto-forward-testing]], [[probability-of-backtest-overfitting]].

**Missing archetypes:** [[hyperliquid-market-making]], [[loss-versus-rebalancing]] (concept) + LVR-aware LP in the [[concentrated-liquidity]] rewrite, [[crypto-options-volatility-selling]], [[crypto-options-dispersion]], [[etf-flow-directional]], [[bitcoin-halving-cycle-timing]], [[crypto-beta-rotation]].

**Execution, sizing, portfolio:** [[cross-venue-execution-crypto]], [[thin-market-execution]], [[funding-aware-position-sizing]], [[liquidation-price-aware-sizing]], [[crypto-portfolio-heat]], [[multi-strategy-crypto-portfolio]].

**Live ops runbooks:** [[paper-to-live-promotion]], [[bot-kill-switch-design]], [[position-reconciliation]], [[exchange-api-key-security]], [[proof-of-reserves]] (data-source).

**Essay → buildable rewrites (crypto-native, highest value):** [[concentrated-liquidity]], [[jit-liquidity]], [[market-making-strategy]], [[mev-strategies]], [[defi-yield-farming]].

**Thin-page crypto instantiations (edits to existing equity-framed pages):** feature-engineering-finance, alpha-model, ml-trading-pipeline, wash-trading (data-quality angle), cryptodataapi-backtesting (validation bridge), smart-order-routing (crypto venues).

## Wave 2 — depth-parity uplift (~24 crypto-native essays)

Rewrite these existing essays to the buildable strategy schema (`funding-rate-arbitrage` template): basis-trading, restaking-strategies, points-farming, airdrop-farming, liquidity-sniping, synthetic-asset-trading, intent-based-trading, nft-trading, delta-neutral-yield-farming, crypto-yield-stack, smart-money-orderflow-combo, sentiment-trading, momentum-rotation, skew-trading, garch-volatility, order-flow-scalping, scalping, vwap-trading, cross-exchange-arbitrage, flash-loan-arbitrage, latency-arbitrage, staking-yield-arbitrage, calendar-spread-arbitrage, cash-and-carry.

## Out of scope (stay as reference essays)
The 49 technical-analysis chart-pattern/options-spread pages, tiny redirect stubs, and large operational/index pages (arbitrage-monitoring-setup, arbitrage-parameter-cheatsheet, arbitrage-worked-examples, live-journal, regime-matrix) — already good or a poor fit for the single-strategy schema.

## Conventions for all new/rewritten pages
Frontmatter per root `CLAUDE.md`; strategy pages carry the full buildable schema + 16-section structure with a realistic cost overlay; every page mapping to data gets a `## Getting the Data (CryptoDataAPI)` section using only verified endpoints; link generously; crypto scope only.
