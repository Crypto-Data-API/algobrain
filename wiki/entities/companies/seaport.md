---
title: "Seaport"
type: entity
entity_type: protocol
created: 2026-04-22
updated: 2026-04-22
status: good
tags: [crypto, nft, ethereum, defi, market-microstructure]
aliases: ["Seaport Protocol", "OpenSea Seaport"]
related: ["[[opensea]]", "[[nft]]", "[[nft-trading]]", "[[ethereum]]", "[[looksrare]]", "[[blur]]", "[[sudoswap]]"]
---

Seaport is an open-source Ethereum marketplace protocol published by [[opensea]] on 20 May 2022 as the replacement for the older Wyvern protocol. It is a low-level smart contract layer for listing, matching, and settling NFT trades, not a marketplace front end in itself. Because of its permissive license (MIT) and gas efficiency, Seaport has been adopted as the base infrastructure for numerous NFT marketplaces beyond OpenSea, with canonical deployments across Ethereum, Polygon, Arbitrum, Optimism, Avalanche, Base, and other EVM chains. The current version is Seaport 1.6, released 20 March 2024.

## How it works

Seaport models every trade as an interaction between two structured messages:

- **Offer items** — the assets the signer is willing to give up (NFTs, ERC-20 tokens, ETH).
- **Consideration items** — the assets the signer requires to be delivered, possibly to multiple recipients (seller proceeds, platform fees, creator royalties).

Because offer and consideration are both arrays of arbitrary items with recipients, a single Seaport order can express:

- A standard one-NFT-for-ETH sale.
- **Bundled trades** — multiple NFTs in one direction swapped for multiple NFTs / tokens in the other.
- **Criteria-based offers** — a bid for "any token from collection X" or "any token matching Merkle root Y" (e.g., any BAYC, or any NFT with a specific trait), without specifying a token ID upfront.
- **Conditional / partial fills** — orders that can be filled by more than one counterparty.
- **Explicit royalty routing** — royalties are just additional consideration recipients; whether and how to enforce them is a front-end decision.

Orders are signed off-chain (EIP-712) and broadcast through off-chain orderbooks, then settled on-chain when a counterparty calls Seaport's fulfillment functions. Settlement supports **fulfillBasicOrder** (gas-optimized single-item trades) and **matchOrders / fulfillAdvancedOrder** (arbitrary multi-item atomic swaps).

## Gas and fees

- Seaport itself charges no protocol fee. Fees and royalties are whatever the marketplace inserts as consideration items when constructing orders.
- The protocol is substantially more gas-efficient than Wyvern, particularly for bulk fills, because it allows multiple orders to be matched in a single transaction with shared setup.
- Because fees are optional at the protocol level, marketplaces (OpenSea, and later imitators) and communities have fought repeatedly over whether to include creator royalty recipients in consideration arrays by default.

## What traders use it for

- **OpenSea listings** — all OpenSea activity since mid-2022 settles through Seaport.
- **Aggregator execution** — NFT aggregators (Gem, Genie, Blur's aggregator) route through Seaport for any listing originally posted on OpenSea or any Seaport-compatible marketplace.
- **Bundle swaps** — traders swap entire sub-collections (e.g., 5 Azuki for 1 BAYC + some ETH) atomically.
- **Collection offers and trait offers** — buyers can post criteria-based offers that any matching NFT from a collection can hit, enabling resting bids at the collection or trait level.
- **Infrastructure for non-OpenSea marketplaces** — many NFT marketplaces have reused Seaport contracts directly rather than rewriting a settlement engine.

## Risks and limitations

- **Front-end fragmentation** — the same Seaport order can be surfaced and routed through multiple marketplaces, complicating royalty enforcement and rev-share.
- **Signature risk** — Seaport signatures can be broad (criteria-based, long-expiry). Phishing attacks that trick users into signing malicious Seaport orders have drained wallets; always verify the offer/consideration structure before signing.
- **Not a complete marketplace** — Seaport handles matching and settlement only. Orderbook hosting, order discovery, and royalty policy sit at the marketplace layer.
- **Composability limits royalty enforcement** — because any contract can settle a valid Seaport order, marketplaces cannot unilaterally force royalties through the protocol; they rely on allowlist/blocklist mechanisms (see NFT royalty enforcement discussion under [[blur]]).

## Related

- [[opensea]] — the protocol's creator and largest user
- [[blur]] — competing Ethereum NFT marketplace; uses its own settlement layer but aggregates Seaport orders
- [[looksrare]] — Ethereum marketplace that has integrated Seaport
- [[sudoswap]] — AMM-based alternative to orderbook protocols like Seaport
- [[nft-trading]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
