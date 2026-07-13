---
title: "Genie"
type: entity
entity_type: company
website: "https://www.genie.xyz"
created: 2026-04-22
updated: 2026-04-22
status: good
tags: [nft, crypto, ethereum, defi]
aliases: ["Genie XYZ", "Genie by Uniswap"]
related: ["[[gem-nft]]", "[[opensea]]", "[[looksrare]]", "[[blur]]", "[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]", "[[ethereum]]"]
---

Genie was the first NFT marketplace aggregator of note, launched in November 2021, designed to let traders browse and purchase NFTs across multiple marketplaces in a single interface and, critically, in a single batched transaction. On 21 June 2022 it was acquired by Uniswap Labs (terms undisclosed), which integrated Genie's aggregation engine into the Uniswap app's NFT section. Genie was one of two aggregators (alongside [[gem-nft]]) that defined the "sweep the floor" user experience that later became table stakes across the NFT marketplace ecosystem.

## How it works

The core Genie product is a cross-marketplace order router. Rather than browsing [[opensea]], [[looksrare]], [[blur]], X2Y2, and other marketplaces individually, a trader sees a unified order book per collection. Purchasing multiple items triggers a single on-chain transaction that interacts with each source marketplace's protocol atomically.

Key capabilities:

- **Unified listings view** — aggregated floor, rarity rank, trait filters across all supported marketplaces
- **Batch purchase ("sweep")** — buy N items in one transaction; if any item fails (already sold, reverted), the transaction can be configured to continue with the rest
- **Gas savings** — a single batched call is dramatically cheaper than N separate purchase transactions. Effective gas savings depend on collection and network conditions, but the structural saving is real
- **Bulk listing tools** — list multiple NFTs at once with customizable strategies (e.g. price each at floor, or ladder)
- **Collection analytics** — floor, volume, and recent sales overlaid onto the browsing experience

After the Uniswap acquisition, Genie functionality was merged into the Uniswap web app's NFT tab. The standalone genie.xyz interface was phased out in favor of NFT trading integrated alongside Uniswap's token-swap UX.

## Trading use cases

- **Floor sweeping** — the canonical use case: buy N cheapest items in a collection in one transaction, often to accumulate ahead of expected demand or to farm marketplace rewards
- **Cross-venue arbitrage** — identify price gaps between marketplaces; Genie's unified view made this easier than manually comparing listings
- **Gas-efficient acquisition at scale** — for funds or whales acquiring a large position, batched purchases substantially reduce gas and execution risk
- **Pre-Uniswap-integration legacy** — Genie was historically the "pro" aggregator, heavily used by [[nft]] power users before [[gem-nft]] and later [[blur]] took significant market share

## Limitations and pitfalls

- **Absorbed into Uniswap** — the standalone product no longer operates independently; today the Genie experience lives as the Uniswap app's NFT section and continues to evolve under Uniswap's product direction
- **Aggregator competition** — [[gem-nft]] (acquired by [[opensea]]) and pro-trader marketplaces like [[blur]] all offer aggregator-style UX, eroding what was once a unique edge
- **Source liquidity dependence** — an aggregator is only as good as the marketplaces it routes to; if a key marketplace (e.g. [[blur]]) is not supported, the aggregator understates true best price
- **Listing staleness** — across multiple marketplaces, listings can be cancelled or modified between display and execution; transactions may partially fail, costing gas on reverts
- **Royalty policy variance** — different marketplaces enforce different royalty rules; sweeping across venues can inadvertently include royalty-honoring and royalty-avoiding listings in the same purchase, with ethical and community implications

## Related

- [[gem-nft]] — the other first-generation aggregator; acquired by [[opensea]]
- [[opensea]] — primary source marketplace for aggregated listings
- [[looksrare]] — early aggregated marketplace with LOOKS token incentives
- [[blur]] — later pro-trader marketplace that combined marketplace + aggregator features
- [[nft-arbitrage]]
- [[nft-trading]]

## Sources

- Uniswap Labs acquisition announcement, 21 June 2022 (blog.uniswap.org/genie)
- Coverage of NFT aggregator evolution (Source: [[2026-04-22-gap-finder-nft-trading]])
