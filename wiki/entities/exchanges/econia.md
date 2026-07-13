---
title: "Econia"
type: entity
entity_type: protocol
created: 2026-06-20
updated: 2026-06-20
status: draft
tags: [crypto, market-microstructure, liquidity, exchange]
aliases: ["Econia", "Econia Protocol", "Econia order book"]
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hyperbft]]", "[[clob]]", "[[hip-3-builder-deployed-perps]]", "[[injective-protocol]]", "[[sei-network]]", "[[orderly-network]]", "[[market-microstructure]]", "[[decentralized-exchanges]]"]
---

Econia is a fully on-chain central limit order book ([[clob|CLOB]]) deployed on the Aptos blockchain that powers partner interfaces such as Pontem's Gator trading UI. It is a useful comparison point to [[hyperliquid|Hyperliquid]]: both treat the CLOB as a protocol-level primitive, but Econia explores doing so on a general-purpose smart-contract L1 (Aptos) rather than on a purpose-built, app-specific chain. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Overview

Econia provides an on-chain order book on Aptos, serving as the matching layer behind front-ends like Pontem's Gator UI. Conceptually it is important because it represents a different architecture within the on-chain CLOB design space: rather than building a bespoke L1 around the order book (as Hyperliquid does with [[hypercore|HyperCore]] and [[hyperbft|HyperBFT]]), Econia implements the CLOB as a primitive on a non-app-specific smart-contract platform. Although its ecosystem is smaller than Hyperliquid's, it explores how to achieve high throughput and low fees for order matching on a general-purpose chain. (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Where Econia sits in the on-chain CLOB landscape

On-chain CLOBs differ in how deeply the order book is integrated into the base protocol versus running in smart contracts or separate modules. Econia and its peers each occupy a different point on that continuum:

| Protocol | Chain / base | CLOB integration style |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | Purpose-built L1 ([[hypercore|HyperCore]] + [[hyperbft|HyperBFT]]) | Order book in protocol state / consensus |
| Econia | Aptos (general-purpose L1) | CLOB as a smart-contract / protocol primitive on a general-purpose chain |
| [[injective-protocol|Injective]] | Cosmos-SDK L1 | Native exchange module |
| [[sei-network|Sei]] | Cosmos-based L1 | DeFi L1 with native CLOB |
| [[orderly-network|Orderly]] | Shared liquidity layer | CLOB liquidity layer shared across front-ends |

This places Hyperliquid at one end of a continuum (an exchange with an L1 built around it) and Econia as a contrasting implementation (a CLOB built atop a general-purpose chain). (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Why it matters for traders and researchers

- **Design comparison** — Econia illustrates the trade-offs of running a CLOB on a general-purpose L1 versus a vertically integrated, app-specific chain, which informs where strategies are best deployed.
- **Microstructure study** — As a fully on-chain order book, Econia is another venue whose order/cancel/trade behaviour is transparent on-chain, making it a candidate data source for microstructure research.
- **Ecosystem context** — Its role behind Pontem's Gator UI shows how a single on-chain CLOB primitive can serve multiple front-ends, a pattern also seen with shared-liquidity layers like [[orderly-network|Orderly]].

## Related

- [[hyperliquid]], [[hypercore]], [[hyperbft]], [[hip-3-builder-deployed-perps]] — the Hyperliquid on-chain CLOB stack Econia is compared against
- [[injective-protocol]], [[sei-network]], [[orderly-network]] — other on-chain CLOB design points
- [[clob]], [[market-microstructure]], [[decentralized-exchanges]]

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])
- Pontem — On-chain order books 101 (Econia & more): https://pontem.network/posts/on-chain-order-books-101-econia-more
