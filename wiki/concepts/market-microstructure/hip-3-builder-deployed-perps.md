---
title: "HIP-3: Builder-Deployed Perpetuals"
type: concept
created: 2026-06-20
updated: 2026-06-20
status: draft
tags: [crypto, market-microstructure, derivatives, liquidity]
aliases: ["HIP-3", "Builder-deployed perps", "Builder-deployed perpetuals", "HIP-3 perps"]
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hyperbft]]", "[[clob]]", "[[econia]]", "[[hyperliquid-oracle-mechanics]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[market-microstructure]]", "[[decentralized-exchanges]]"]
---

HIP-3 (Hyperliquid Improvement Proposal 3) enables permissionless, builder-deployed perpetual-futures markets that share [[hypercore|HyperCore]]'s matching engine and margining stack but are configured by independent deployers who set their own oracle, contract specifications, leverage limits, settlement rules, and fee shares. It transforms [[hyperliquid|Hyperliquid]] from a tightly curated perp DEX into a platform where each HIP-3 DEX behaves as an independent perp venue layered on shared infrastructure. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Overview

HIP-3 allows builders to deploy their own perp markets without permission. Each market inherits HyperCore's high-performance [[clob|order books]] and margining, but the deployer is responsible for defining how the market actually works. The result is not merely more tickers on one venue — it is an entire layer of heterogeneous microstructures that can differ in risk, fee structure, oracle quality, and liquidity, all sharing the same matching core and [[hyperbft|HyperBFT]] consensus. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## What deployers control

| Parameter | Set by deployer | Notes |
|---|---|---|
| Oracle | Yes | Oracle source/quality varies per market |
| Contract specifications | Yes | Defines the instrument |
| Leverage limits | Yes | Can differ from core markets |
| Settlement rules | Yes | Deployer-defined |
| Fee shares | Yes | Configurable; in some configs can exceed 100%, causing protocol fees to rise in lockstep with deployer fees |
| Matching engine | No (shared) | Inherited from HyperCore |
| Consensus / finality | No (shared) | Inherited from HyperBFT |

A "growth mode" is noted for HIP-3 perps in which protocol fees, rebates, and volume contributions are substantially reduced. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Per-DEX backstop liquidation and "no-cross" margin

Each HIP-3 DEX has its own fully on-chain strategy contract that takes over liquidatable positions as part of a backstop mechanism — underlining the independence of each DEX even while it uses shared infrastructure. HIP-3 DEXs also support a **"no-cross" margin mode**: isolated margin with margin removal allowed, but without cross-margin across positions. The same account can therefore be subject to different margining rules depending on whether it is trading core markets or a HIP-3 market. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) See [[hyperliquid-liquidation-engine|liquidation engine]] for the core-market mechanics this builds on.

## Adoption and volume (as reported)

| Metric | Reported figure | Source |
|---|---|---|
| HIP-3 builder-deployed volume | $62 billion in a single month | The Defiant |
| Hyperliquid share of global perps volume | 6.63% (a record at the time) | The Defiant |

These figures are cited as reported by The Defiant and are not independently verified here. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Market-structure implications for traders

- **Heterogeneous risk** — A HIP-3 market with aggressive leverage, higher deployer fee shares, and a less robust oracle may offer richer volatility/funding opportunities but also higher liquidation and counterparty risk.
- **New arbitrage routes** — Independent deployer settings on a shared matching engine create new mispricing and funding-arbitrage opportunities across HIP-3 and core markets — and new failure modes.
- **Fragmented liquidity** — Some deployers attract deep books while others remain thin, so depth and slippage vary widely across HIP-3 markets.
- **Low integration cost** — HIP-3 markets share the same API schema as core assets, so bots and strategies can be adapted with minimal code changes, making them attractive for quant experimentation.
- **Funding heterogeneity** — Because each market sets its own oracle, [[hyperliquid-funding-rate-microstructure|funding]] and the premium index can differ market-to-market even on similar underlyings. See [[funding-rate]].

(Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Related

- [[hypercore]] — the shared matching engine HIP-3 markets inherit
- [[hyperbft]] — the shared consensus / finality
- [[hyperliquid]] — the host venue
- [[hyperliquid-oracle-mechanics]], [[hyperliquid-liquidation-engine]], [[hyperliquid-funding-rate-microstructure]] — core mechanics that HIP-3 markets vary
- [[econia]] — comparable on-chain CLOB design point
- [[perpetual-futures]], [[funding-rate]], [[clob]], [[market-microstructure]], [[decentralized-exchanges]]

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])
- Hyperliquid Docs — HIP-3 Builder-Deployed Perpetuals: https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals
- Hyperliquid Docs — Margining: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining
- Hyperliquid Docs — Fees: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees
- Hyperliquid Docs — Liquidations: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations
- The Defiant — Builder-deployed perp markets push Hyperliquid to record share of global perps volume: https://thedefiant.io/news/defi/builder-deployed-perp-markets-push-hyperliquid-to-record-share-of-global-perps-volume
