---
title: "HyperCore: Hyperliquid's On-Chain Matching Engine"
type: concept
created: 2026-06-20
updated: 2026-06-20
status: draft
tags: [crypto, market-microstructure, liquidity, derivatives]
aliases: ["HyperCore", "Hyperliquid Core", "Hyperliquid matching engine"]
related: ["[[hyperliquid]]", "[[clob]]", "[[hyperbft]]", "[[hip-3-builder-deployed-perps]]", "[[econia]]", "[[hyperliquid-oracle-mechanics]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[market-microstructure]]", "[[perpetual-futures]]", "[[decentralized-exchanges]]"]
---

HyperCore is the protocol-level execution engine of the [[hyperliquid|Hyperliquid]] layer-one (L1) that houses its fully on-chain perpetual-futures and spot [[clob|central limit order books]], together with margining and liquidations. It is not a smart contract running on top of a general-purpose chain; it is the part of the L1 whose state-transition logic *is* the order book and matching engine, run as part of consensus. A separate Ethereum-like smart-contract layer, the HyperEVM, composes with HyperCore's liquidity. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Overview

Hyperliquid splits state execution into two components: HyperCore — which includes the on-chain perp and spot order books, margining, and liquidations — and HyperEVM, a general-purpose, Ethereum-modelled smart-contract environment that can access HyperCore's liquidity. Because the order book lives in protocol state rather than in an application contract, every order, cancel, trade, and liquidation in the perp and spot markets is executed fully on-chain, with matching embedded directly into HyperCore's state transition. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Matching rules

HyperCore replicates the central-limit-order-book behaviour familiar from centralized exchanges, but with transparent on-chain state:

| Property | HyperCore behaviour |
|---|---|
| Priority | Price-time priority — best price first, then earliest order at a level |
| Price granularity | Tick size enforced by the protocol |
| Size granularity | Lot size enforced by the protocol |
| Book contents | Resting bids (buy interest) and asks (sell interest); matching when an incoming order crosses the spread |
| Settlement | Order, cancel, trade, and liquidation all committed on-chain |
| Throughput (reported) | Cited "on the order of 200,000 orders/second," with ongoing optimization |

The ~200,000 orders/second figure is reported by Hyperliquid documentation and third-party coverage and is cited here as reported, not independently verified. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Margining and liquidations in state

Beyond matching, HyperCore manages margining and liquidations as protocol-level primitives. A [[hyperliquid-liquidation-engine|liquidation]] triggers when account equity falls below maintenance margin (defined as half the initial margin at max leverage), and the protocol closes positions via market orders into the existing book depth — so realized liquidation prices and slippage are a direct function of order-book liquidity at the moment of the event. [[hyperliquid-funding-rate-microstructure|Funding]] for perps and the premium index are likewise computed from order-book impact prices versus the [[hyperliquid-oracle-mechanics|oracle]] price. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## How it differs from smart-contract order books

| Dimension | HyperCore (protocol-level CLOB) | Smart-contract CLOB on general-purpose L1 |
|---|---|---|
| Where the book lives | Native L1 state, in consensus | Application contract on top of the chain |
| Order/cancel cost model | Protocol-optimized for high order churn | Subject to general gas accounting and VM limits |
| Throughput | Reported ~200k orders/s | Bounded by general-purpose VM and block design |
| Comparable design point | — | [[econia|Econia]] (on Aptos), [[injective-protocol|Injective]] exchange module, [[sei-network|Sei]] |

This architecture means protocol-level changes to HyperCore can alter how order books behave in ways that would be opaque on a centralized venue. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## MEV and ordering implications

Because order placement and matching are part of consensus (driven by [[hyperbft|HyperBFT]]) rather than handled by a private, off-chain matching engine, transaction ordering and finality directly shape MEV and front-running risk. Every order submission and cancellation passes through the consensus layer and is observable on-chain, which changes the playing field for latency-sensitive strategies relative to a CEX matching engine. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Trading relevance

- Latency and throughput characteristics determine which algorithmic strategies (fast quoting, cross-venue arbitrage) are viable.
- Tick/lot enforcement and price-time priority make execution semantics predictable and CEX-like.
- Liquidations consume book depth via market orders, so depth profiles and "liquidity walls" govern how severe liquidation cascades become.
- HyperCore's matching engine is shared by [[hip-3-builder-deployed-perps|HIP-3 builder-deployed perps]], so heterogeneous markets inherit the same execution core while differing in oracle, leverage, and fee settings.

## Related

- [[hyperliquid]] — the venue HyperCore powers
- [[hyperbft]] — the consensus that orders HyperCore's state
- [[hip-3-builder-deployed-perps]] — markets sharing HyperCore's engine
- [[clob]] — the order-book primitive HyperCore implements on-chain
- [[econia]] — comparable on-chain CLOB design point (Aptos)
- [[hyperliquid-oracle-mechanics]], [[hyperliquid-liquidation-engine]], [[hyperliquid-funding-rate-microstructure]] — HyperCore subsystems
- [[market-microstructure]], [[decentralized-exchanges]], [[perpetual-futures]]

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])
- Hyperliquid Docs — Order Book: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/order-book
- Hyperliquid Docs (overview): https://hyperliquid.gitbook.io/hyperliquid-docs
- Hyperliquid Docs — Funding: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding
- Hyperliquid Docs — Liquidations: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations
