---
title: "rarity.tools"
type: source
source_type: data
source_url: "https://rarity.tools"
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [nft, crypto, ethereum, data-provider]
aliases: ["Rarity Tools", "rarity-tools"]
related: ["[[openrarity]]", "[[trait-sniper]]", "[[nft]]", "[[nft-trading]]", "[[opensea]]", "[[cryptopunks]]", "[[bored-ape-yacht-club]]", "[[art-blocks]]", "[[ethereum]]"]
---

rarity.tools is the foundational NFT rarity-scoring website, launched in April 2021, that introduced the "Rarity Score" methodology now widely used across the [[nft]] ecosystem. Originally evolved from a browser tool built by developer emp_rickharrison (known as wFbrowser) for ranking Waifusion NFTs, rarity.tools became the first widely-adopted public tool for ranking individual NFTs by scarcity within a collection, and its scoring formula remains the de facto standard that most competing tools either reuse or benchmark against.

## How it works

Rarity.tools calculates a Rarity Score for each NFT in a supported collection using a simple, reproducible formula:

```
Rarity Score (trait) = 1 / (trait frequency / total supply)
Rarity Score (NFT)   = sum of Rarity Scores across all traits
```

Higher scores indicate rarer NFTs. The design intentionally rewards NFTs that possess multiple uncommon traits, while also giving a large single-trait outlier (a trait held by very few NFTs) substantial weight.

Key features of the site include:

- Per-collection rarity rankings, sortable by overall rank or by any individual trait
- Filtering by trait combinations (e.g. show all BAYC with gold fur and laser eyes)
- Direct links to marketplace listings, typically to [[opensea]]
- Price data overlaid on rarity rank so traders can see which rare items are underpriced
- Coverage spans hundreds of Ethereum NFT collections, including [[cryptopunks]], [[bored-ape-yacht-club]], [[azuki]], [[art-blocks]] and most of the major PFP and generative art projects

The methodology is transparent and has been replicated in open-source implementations, which is part of what drove adoption across the ecosystem.

## Trading use cases

For active NFT traders, rarity.tools is a core pricing reference tool:

- **Undervalued rare sniping** — cross-reference a collection's floor listings on [[opensea]] against rarity rank; items with high rank but near-floor pricing are arbitrage candidates
- **Trait-floor analysis** — identify the cheapest listing within a specific trait (e.g. cheapest gold-fur BAYC) to gauge whether a trait commands a premium vs the collection floor
- **Collection evaluation at mint** — once a reveal happens, rarity.tools rankings populate quickly, and early movers who identify top-1% items before the wider market repricing capture significant upside
- **Listing strategy** — sellers use rarity rank to price their NFT relative to the collection's distribution rather than simply matching floor

## Limitations and pitfalls

- **Rarity is not value** — rarity is a statistical property of traits; actual market value depends on meta-narratives (e.g. which traits the community considers culturally desirable), not just scarcity. A one-of-one trait in an unwanted color class may trade below floor
- **Algorithm dependence** — the Rarity Score formula equal-weights all traits, which overrates "filler" traits that collections may not consider meaningful. [[openrarity]] was created partly to address concerns about scoring methodology
- **Speed disadvantage at reveal** — professional traders using [[trait-sniper]] or private rarity APIs typically get rarity data seconds after reveal, well before rarity.tools finishes indexing a collection
- **Limited chain coverage** — rarity.tools historically focused on Ethereum; traders in Solana, Bitcoin Ordinals, or other ecosystems need alternative tools like [[magic-eden]]-native rankings or collection-specific rarity providers
- **Manual listing approval** — not every collection automatically appears; smaller collections may be absent for days or weeks after launch
- **Site appears unmaintained** — as of 2026-04, the rarity.tools root domain redirects to the project's X/Twitter account, suggesting the site is no longer actively operated. Treat historical coverage as the main value and use [[openrarity]] or [[trait-sniper]] for live rankings

## Related

- [[openrarity]] — open-source successor standard
- [[trait-sniper]] — rarity tool optimized for mint-reveal speed
- [[opensea]] — primary marketplace where rarity-ranked NFTs are listed
- [[nft-trading]] — broader trading context
- [[nft-arbitrage]] — strategies that exploit rarity-price mispricings

## Sources

- rarity.tools methodology documentation and collection listings
- Background on Rarity Score formula and adoption (Source: [[2026-04-22-gap-finder-nft-trading]])
