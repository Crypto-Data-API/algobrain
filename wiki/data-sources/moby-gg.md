---
title: "Moby.gg"
type: source
source_type: data
source_url: "https://moby.gg"
created: 2026-04-22
updated: 2026-06-20
status: good
tags: [nft, crypto, data-provider, aggregator]
aliases: ["Moby", "moby-gg", "moby.gg"]
related: ["[[rarity-tools]]", "[[trait-sniper]]", "[[rarity-sniper]]", "[[nft-aggregators]]", "[[opensea]]", "[[blur]]", "[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]"]
---

Moby.gg is a versatile [[nft]] trading platform that combines rarity checking with marketplace aggregation features. It lets traders evaluate rarity scores for individual NFTs while simultaneously comparing listings across multiple marketplaces, positioning it as a hybrid between pure rarity tools like [[rarity-tools]] and marketplace aggregators in the [[nft-aggregators]] category (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).

## How it works

Moby.gg combines two features that are usually offered separately:

- **Rarity scoring** — like [[rarity-tools]], [[rarity-sniper]], and [[trait-sniper]], Moby.gg surfaces per-NFT rarity ranks and trait scarcity within a collection, allowing traders to evaluate how rare a given item is relative to the rest of the supply
- **Marketplace aggregation** — rather than restricting users to a single venue like [[opensea]], Moby.gg aggregates listings across multiple marketplaces so traders can compare prices for the same NFT or trait in one view (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]])

The research available to the wiki does not specify the exact list of marketplaces aggregated, the rarity-scoring formula used (inverse-frequency as popularized by [[rarity-tools]] vs an [[openrarity]]-style statistical score), refresh cadence, or whether the platform supports direct purchases, wallet-sweep, or only redirects to the originating marketplace.

## Trading use cases

- **Cross-marketplace arbitrage** — identify the same NFT or trait listed more cheaply on one venue than another; relevant when [[opensea]], [[blur]], and other marketplaces fragment liquidity and pricing
- **Rarity-adjusted pricing** — combine rarity rank with live floor/listing data to spot NFTs that are rare but underpriced relative to their trait scarcity; the standard workflow shared with [[rarity-tools]] and [[trait-sniper]]
- **Single-pane workflow** — avoid tab-switching between a rarity site and a marketplace by having rarity and cross-venue listing data in one interface
- **Collection evaluation** — quickly assess whether a collection's listings skew toward floor sweeping or reflect a meaningful rarity premium, informing entry decisions

## Limitations

- **Limited public documentation** — the research available to the wiki describes Moby.gg only in general terms; specifics around methodology, marketplace coverage, fee structure, and supported chains were not captured
- **Rarity methodology uncertainty** — different scoring algorithms (inverse-frequency, statistical, composite) can produce different rank orders; without published methodology, rank comparisons between Moby.gg and peers like [[rarity-tools]], [[trait-sniper]], and [[rarity-sniper]] should not be assumed equivalent
- **Aggregator trust and latency** — aggregator listings depend on how frequently the platform pulls from each marketplace's API or indexer; stale data creates false arbitrage signals, a common pitfall across [[nft-aggregators]]
- **Chain coverage unknown** — whether Moby.gg covers only Ethereum-based NFTs (as [[rarity-tools]] historically did) or extends to Solana, Bitcoin Ordinals, or L2s was not captured in the research
- **Feature set may have evolved** — many NFT tools launched during the 2021 bull market have shifted focus, added or removed features, or gone dormant; claims here reflect a general description, not live-tested behavior

## Related

- [[rarity-tools]] — foundational rarity-scoring website
- [[trait-sniper]] — rarity and mint-reveal sniping tool with browser extension
- [[rarity-sniper]] — rarity-assessment site with attribute-breakdown scoring
- [[nft-aggregators]] — broader category of marketplace-aggregation tools
- [[opensea]] — primary NFT marketplace likely among aggregated sources
- [[blur]] — pro-trader marketplace likely among aggregated sources
- [[nft-arbitrage]] — strategies that exploit cross-marketplace and rarity-vs-price mispricings
- [[nft-trading]] — broader trading context

## Sources

- Overview of NFT rarity-scoring platforms including Moby.gg (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]])

---

> **Data disclaimer — primary-source verification pending.** As of June 2026 the domain still appears to be online, but the platform's current product scope, marketplace coverage, rarity methodology, supported chains, and pricing could not be confirmed from available sources. Many NFT-bull-market tools from 2021-2022 have since pivoted, gone dormant, or rebranded, so the description above should be re-verified against the live site before relying on it. All claims on this page derive from a secondary research summary plus a connectivity check, not from first-hand feature inspection. The page is structurally complete, but the load-bearing specifics (exact marketplaces aggregated, scoring formula, chain coverage, fees) remain unverified — treat them as qualitative until confirmed against the live product.
