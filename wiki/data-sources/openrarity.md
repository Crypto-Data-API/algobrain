---
title: "OpenRarity"
type: source
source_type: data
source_url: "https://openrarity.gitbook.io"
created: 2026-04-22
updated: 2026-04-22
status: good
tags: [nft, crypto, ethereum, data-provider]
aliases: ["Open Rarity", "OpenRarity Protocol"]
related: ["[[rarity-tools]]", "[[trait-sniper]]", "[[opensea]]", "[[magic-eden]]", "[[nft]]", "[[nft-trading]]", "[[ethereum]]"]
---

OpenRarity is an open-source rarity protocol launched in 2022 as a collaboration between [[opensea]], Curio, Icy.tools, and PROOF, with the explicit goal of establishing a single, transparent, reproducible standard for calculating NFT rarity scores across the industry. Before OpenRarity, competing proprietary rarity algorithms produced conflicting ranks for the same NFT depending on which site you consulted, creating information asymmetry that favored whoever had the "right" algorithm. OpenRarity's approach is mathematically principled and public, so any marketplace, tool, or trader can compute the same number.

## How it works

OpenRarity calculates rarity using **information content** derived from [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)), not the simple inverse-frequency formula used by [[rarity-tools]]. The core idea:

```
Information content of a trait = -log2(P(trait))
Rarity score for an NFT        = sum of information content across all its traits
```

Where `P(trait)` is the probability of that trait appearing in the collection (i.e. trait count / collection size).

Design choices that differentiate it from the legacy Rarity Score:

- **Information-theoretic basis** — uses a well-defined mathematical concept rather than an ad-hoc formula
- **Treats trait categories equally** — avoids systematic biases when some categories have many possible values and others have few
- **Open source** — reference implementations available in Python and JavaScript, calculation is fully auditable
- **Collection-agnostic** — works for any ERC-721 or ERC-1155 collection with structured trait metadata
- **Non-opinionated** — does not weight traits by perceived desirability; produces a pure statistical score

Integration is broad across the ecosystem. [[opensea]] displays OpenRarity rank on NFT pages. [[magic-eden]], Curio, and a number of collection-specific sites have also adopted it.

## Trading use cases

- **Cross-venue rarity consistency** — since OpenRarity produces the same rank regardless of which platform you check, traders can compare listings across marketplaces without correcting for algorithm drift
- **Baseline for arbitrage against other algorithms** — divergences between OpenRarity rank and [[rarity-tools]] rank highlight NFTs mispriced relative to one algorithm's view of the market, which can be monetized
- **Defensible valuations** — when building quant models for NFT pricing, using an open reproducible score (rather than an opaque proprietary one) makes the model auditable and portable
- **Collection fairness auditing** — collectors can independently verify that advertised rarity ranks match the actual on-chain trait distribution

## Limitations and pitfalls

- **Not an opinionated value estimate** — OpenRarity scores traits by statistical rarity only; a rare-but-ugly trait scores the same as a rare-and-meta-defining trait, so score does not equal price
- **Metadata dependency** — the algorithm assumes clean, structured trait metadata; collections with inconsistent or gamed metadata (e.g. deliberately injected "ultra rare" tags on common NFTs) produce misleading scores
- **Does not capture combinatorial rarity** — trait combinations (e.g. two specific traits co-occurring) get no extra weight beyond the sum of individual information content
- **Adoption not universal** — some marketplaces and collections still favor their own algorithms; rarity rank can differ between OpenRarity and the collection creator's "official" rank
- **Not a substitute for market data** — traders should still consult [[nft-price-floor]] and trait-floor data; rarity is a prior, not a price

## Related

- [[rarity-tools]] — earlier, widely-adopted rarity standard that OpenRarity was partly created to supersede
- [[trait-sniper]] — rarity/sniping tool, reports OpenRarity alongside its own scoring
- [[opensea]] — displays OpenRarity rank natively
- [[magic-eden]] — adopted OpenRarity for supported collections
- [[nft-trading]]
- [[nft-arbitrage]]

## Sources

- OpenRarity developer documentation (openrarity.gitbook.io)
- Integration coverage across [[opensea]] and [[magic-eden]] (Source: [[2026-04-22-gap-finder-nft-trading]])
