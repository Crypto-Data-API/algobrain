---
title: "Algorithmic Trading"
type: overview
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [algorithmic, quantitative, ai-trading, crypto, defi]
aliases: ["Algo Trading", "Systematic Trading"]
related: ["[[strategies-overview]]", "[[quantitative-overview]]", "[[arbitrage-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[backtesting-overview]]", "[[failure-modes]]"]
---

# Algorithmic Trading

Algorithmic trading is the family of strategies in which code — not discretionary human judgment — follows explicit rules for signal generation, position sizing, and execution. This ranges from simple moving-average crossovers running on a Raspberry Pi to institutional systems processing millions of messages per second on co-located FPGA hardware. What they share is a commitment to systematic, repeatable, testable decision-making.

## What Distinguishes This Family

- **Edge sources** (see [[edge-taxonomy]]): the broadest mix of any category — *analytical* (factor models, portfolio construction), *structural* (index rebalancing flows, execution benchmarks, on-chain mechanics like liquidations and liquidity incentives), *latency* (MEV, sniping), and *risk-bearing* (trend-following's crisis-alpha premium). The defining feature is not the edge itself but that the edge is harvested by machine.
- **Typical timeframes**: the full spectrum — microseconds (MEV, block-space races) through daily rebalances (factor portfolios) to monthly (CTA trend systems). The category is defined by automation, not holding period.
- **Capital and data requirements**: highly bimodal. Factor and CTA strategies need clean multi-decade datasets and benefit from scale; on-chain strategies need node/RPC access, mempool or indexer data, and often work *better* at small size where gas and impact stay negligible. All variants require engineering skill: backtest infrastructure, monitoring, and fail-safes.
- **Who it suits**: traders who can code, who prefer building and validating systems over watching screens, and who accept that the work shifts from trade selection to research process — hypothesis discipline ([[hypothesis-to-backtest-workflow]]), overfitting control ([[overfitting-detection]]), and knowing the [[failure-modes]] that kill automated systems unattended.

## Strategies in This Category

### Systematic & Institutional

- [[algorithmic-trading]] — Foundations of automated trading systems: architecture, signal pipelines, execution
- [[trend-following-cta]] — The managed-futures approach that has captured macro trends, uncorrelated with equities, for 40+ years
- [[factor-investing]] — Harvesting systematic risk premia (value, momentum, quality, size) distilled from decades of academic research
- [[long-short-equity]] — Market-neutral or net-biased equity books built from systematic stock ranking
- [[black-litterman]] — Bayesian portfolio construction blending market equilibrium with active views
- [[cppi]] — Constant proportion portfolio insurance: rule-based downside protection with upside participation
- [[risk-budgeting]] — Allocating capital by risk contribution rather than notional weight
- [[portable-alpha]] — Separating beta exposure (via derivatives) from an independent alpha engine
- [[dispersion-trading]] — Selling index volatility against single-name volatility to harvest the correlation premium
- [[basis-trading]] — Capturing spot-futures spreads, from bond basis to crypto cash-and-carry
- [[commodity-index-rebalancing]] — Front-running predictable commodity index roll and rebalance flows
- [[implementation-shortfall]] — Execution algorithms that minimize the gap between decision price and fill price
- [[dark-pool-trading]] — Executing in non-displayed venues to reduce market impact and information leakage

### DeFi Yield & Liquidity

- [[defi-yield-farming]] — Deploying capital across lending, LP, and incentive programs for on-chain yield
- [[leveraged-yield-farming]] — Borrowing against collateral to multiply farming yields (and liquidation risk)
- [[cross-chain-yield-farming]] — Rotating capital across chains to chase the highest incentive-adjusted yields
- [[concentrated-liquidity]] — Active range management on Uniswap v3-style AMMs to maximize fee capture
- [[jit-liquidity]] — Just-in-time liquidity provision: adding and removing LP depth around a single large swap
- [[restaking-strategies]] — Layering EigenLayer-style restaking yields on top of base staking returns
- [[airdrop-farming]] — Systematically qualifying wallets for prospective token airdrops
- [[points-farming]] — Accumulating protocol points programs ahead of expected token conversions

### MEV & Sniping

- [[mev-strategies]] — Maximal extractable value on blockchains: arbitrage, liquidations, sandwiching
- [[jito-bundle-sniping]] — Solana MEV via Jito bundle auctions for priority block inclusion
- [[zkml-predictive-mev]] — Frontier MEV using zero-knowledge machine learning to predict and prove profitable ordering
- [[liquidity-sniping]] — Buying within the first blocks of a new pool's liquidity going live
- [[memecoin-sniping]] — Automated entry into newly launched memecoins before discovery
- [[token-migration-sniping]] — Trading contract migrations and token swaps where mispricing windows open

### On-Chain Signals & Automation

- [[on-chain-flow-trading]] — Trading aggregate blockchain flows: exchange inflows/outflows, whale movements
- [[on-chain-smart-money-tracking]] — Following labeled high-performing wallets as a signal source
- [[intent-based-trading]] — Expressing trades as intents filled by solver networks rather than direct execution
- [[copy-trading]] — Automatically mirroring the trades of selected traders or wallets
- [[telegram-bot-trading]] — Retail automation layer: bot-driven execution for on-chain tokens
- [[synthetic-asset-trading]] — Trading synthetic representations of off-chain assets on-chain
- [[nft-trading]] — Systematic approaches to NFT floor sweeps, trait arbitrage, and liquidity
- [[ai-agent-strategies]] — LLM/agent-driven trading systems and the strategies built around agent tokens

## Start Here

- [[factor-investing]] — harvesting systematic risk premia across asset classes
- [[trend-following-cta]] — the managed-futures approach to capturing macro trends
- [[mev-strategies]] — maximal extractable value on blockchains (arbitrage, liquidations, sandwiching)

## All Pages in This Folder

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/algorithmic"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Key Topics to Cover

- Market making algorithms
- TWAP and VWAP execution
- High-frequency trading (HFT)
- Latency arbitrage
- Signal generation and execution
- Backtesting frameworks
- Risk management in algo trading

## Related

- [[strategies-overview]] — parent catalog of all strategy categories
- [[quantitative-overview]] — the research/statistics sibling: models and anomalies that algos often implement
- [[arbitrage-overview]] — price-discrepancy strategies, many of which only exist in automated form
- [[day-trading-overview]] — manual intraday trading; the discretionary counterpart to execution algos
- [[edge-taxonomy]] — classifying where an automated edge actually comes from
- [[regime-matrix]] — which systematic strategies work in which market regimes
- [[backtesting-overview|Backtesting]] — validation methodology every algo must pass
- [[failure-modes]] — how automated strategies die: decay, crowding, regime change, infrastructure
