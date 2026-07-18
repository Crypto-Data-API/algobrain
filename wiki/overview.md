---
title: "AlgoBrain — Overview"
type: overview
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [overview, meta]
---

# AlgoBrain — Overview

This page provides a high-level synthesis of the wiki's current state: mission, major themes, knowledge density, gaps, and emerging insights.

## Mission

A crypto-trading-strategy knowledge base for AI-assisted strategy research and generation. Scope: **crypto, blockchain, DeFi, trading, algorithms, and markets** — plus the macro context (FX, rates, commodities, market history) and AI/ML knowledge that feed crypto strategy development. Stock-picking and equity-fundamental content is deliberately out of scope.

## Current State

Forked from a broader trading wiki on 2026-07-13, pruned to crypto scope, and since expanded to **4,850+ pages** (top-2,500 coin coverage, Trading Profiles across the tradable set, and a growing combination-strategy program). The knowledge base spans:

- **Strategies** (~390 pages): funding-rate harvesting, basis/carry, liquidation-cascade plays, MEV, memecoin sniping, market making, grid/mean-reversion/momentum systems, the 27-basket Hyperliquid signal library, a 100+ page arbitrage encyclopedia from medieval bills of exchange to cross-L2 MEV, and the [[combination-matrix|combination-strategy matrix]]
- **Concepts** (~1,030 pages): market microstructure, indicators, portfolio theory, risk management, backtesting methodology, behavioral finance, anomalies, options mechanics, on-chain metrics (MVRV, SOPR, NUPL, HODL waves), macro
- **Markets** (~2,470 pages): 2,400+ crypto asset pages — every Binance- or Hyperliquid-tradable name carries a Trading Profile with venue, strategy, and live-data guidance — plus commodities, forex, and bonds for macro context
- **Entities** (~265 pages): crypto exchanges, DeFi protocols, quant/crypto funds, trading legends, miners and treasury companies, regulators
- **Crypto narratives** (backtester-ready catalog): 19 categories, 69 archetypes, 290 quantified historical instances
- **AI & AI-trading** (~300 pages): ML models, trading bots, backtesting frameworks, LLM finance applications, and the general AI knowledge base
- **History & news**: crypto market history (Mt. Gox → FTX → ETF era) plus macro/trading history (1987, LTCM, GFC, Volmageddon)

**Flagship clusters:** [[crypto-market-regime-taxonomy|14-Basket Crypto Regime Taxonomy]] (regime detection → strategy gating, see [[regime-strategy-playbook]]) · [[hyperliquid-baskets-overview|Hyperliquid Basket Library]] · [[regime-matrix|Strategy Regime Matrix]] · [[crypto-perp-backtesting-pitfalls|Crypto-Perp Backtesting]] · [[arbitrage-overview|Arbitrage Hub]] · [[crypto-narratives-overview|Narrative Impact Catalog]].

## Data Layer

**[[cryptodataapi|CryptoDataAPI]]** (https://cryptodataapi.com) is the canonical data source for this wiki: 190+ REST endpoints covering prices/klines, funding rates, open interest, liquidations, order-book depth, volatility/market/meme/event/security/policy regimes, HMM quant probabilities, on-chain flows, miner metrics, whale tracking, Hyperliquid trader intelligence, sentiment, ETF flows, and a Parquet backtesting archive back to 2020. Pages that map to an endpoint carry a **"Getting the Data (CryptoDataAPI)"** section with live + historical access patterns.

## Knowledge Gaps

Priority areas to fill next:
1. **Backtesting results**: empirical validation data for the strategy pages, using the CryptoDataAPI backtesting archive
2. **Regime-gated performance**: which strategies actually work in which of the 14 regimes
3. **Current market snapshots**: refresh market-state pages via CryptoDataAPI live endpoints
4. **On-chain strategy depth**: more strategies built on exchange-flow, dry-powder, and whale-score signals
5. **Cross-venue microstructure**: Hyperliquid vs CEX funding/basis divergence patterns

## Emerging Themes

1. **Regime-first strategy design**: every strategy gated to explicit market-regime conditions rather than run unconditionally
2. **AI-exploit risk as tradeable edge**: frontier-model vulnerability discovery compressing disclosure cycles (see the AI-exploit cluster)
3. **DEX-TradFi convergence**: Hyperliquid trading traditional assets on-chain; CME/ETF institutional rails maturing
4. **Whale/copy-trading intelligence**: wallet-level positioning data as a first-class signal
5. **Narrative quantification**: mapping world events → crypto price impact with backtestable priors

## Contradictions & Open Questions

- Efficient-market skepticism vs. documented anomaly persistence in crypto (funding, listing effects, session patterns) — both perspectives well-sourced
- Quantitative/systematic approaches (de Prado, Chan) vs. discretionary trading (Market Wizards) — the wiki covers both without favoring either
