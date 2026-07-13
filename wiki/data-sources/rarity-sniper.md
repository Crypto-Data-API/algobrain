---
title: "Rarity Sniper"
type: source
source_type: data
source_url: "https://raritysniper.com"
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [nft, crypto, ethereum, data-provider]
aliases: ["RaritySniper", "rarity-sniper", "raritysniper.com"]
related: ["[[rarity-tools]]", "[[trait-sniper]]", "[[openrarity]]", "[[nft]]", "[[nft-trading]]", "[[opensea]]", "[[ethereum]]"]
---

Rarity Sniper is an [[nft]] rarity-ranking service that operates a public website, a widely-used Discord bot, and associated alert channels. It sits in the same tool category as [[rarity-tools]] and [[trait-sniper]]: traders use it to look up the rarity rank of a specific NFT within its collection, browse top-ranked pieces, and receive notifications around mint and reveal events. It is frequently cited alongside rarity.tools and TraitSniper as one of the three commonly-used rarity platforms for [[ethereum]] NFT collectors (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]).

## How it works

Rarity Sniper provides three primary surfaces:

- **Web app at raritysniper.com** — per-collection rarity rankings and search, with detailed breakdowns of how each trait contributes to an NFT's overall rarity score
- **Discord bot** — the most distinctive surface; users can query an NFT's rarity directly inside Discord servers where the bot is installed, which has driven adoption inside individual project communities
- **Alert channels** — mint-reveal and collection-update notifications for users tracking specific launches

The rarity scoring methodology is in the same family as the inverse-trait-frequency formula popularized by [[rarity-tools]]: rarer traits contribute disproportionately to a higher overall score. Exact formula details and any weighting adjustments are maintained by the operator and should be verified against the live site before anchoring trading decisions in specific rank numbers.

Collection coverage spans a broad set of Ethereum PFP and generative-art collections, with newer launches typically added during or shortly after reveal. As with other rarity platforms, coverage of non-Ethereum collections (Solana, Bitcoin Ordinals, Layer 2s) is more limited and varies by collection.

## Trading use cases

- **Mint-reveal sniping** — when a new collection reveals, traders use Rarity Sniper's rankings (often via the Discord bot for speed) to identify high-rank pieces that are listed on [[opensea]] at or near floor before the broader market reprices them
- **Trait-floor arbitrage** — browse the cheapest listing within a given trait to find rares that are mispriced relative to the typical trait premium
- **Portfolio monitoring** — check the rarity of held NFTs to inform listing prices and decide which pieces to hold versus sell
- **Community integration** — because the Discord bot is embedded in many project communities, rarity lookups happen inside the social venue where collectors are already active, reducing friction versus visiting a separate site

## Limitations and pitfalls

Rarity Sniper shares the same category-level risks as [[trait-sniper]] and [[rarity-tools]]:

- **Algorithm dependence** — different rarity tools can produce different ranks for the same NFT; a strategy anchored to "buy any top-100 at floor" is implicitly anchored to a specific algorithm. A piece that is rank-50 on Rarity Sniper may be rank-120 on [[openrarity]] or [[trait-sniper]]
- **Rarity is not value** — rarity is a statistical property of traits; market value depends on which traits the community considers desirable, not just their frequency. A rare trait in an unloved category can trade below floor
- **Crowded edge** — mint-reveal sniping is a well-known playbook, and dedicated bots compete with human users. The edge from being a few seconds faster than retail has compressed substantially
- **Gas wars on reveal** — when multiple snipers chase the same top-ranked piece, gas fees spike and the profitable-trade threshold narrows
- **Reveal mechanics risk** — delayed, staggered, or obfuscated metadata can produce temporarily wrong rankings, trapping snipers who act on the first numbers they see
- **Coverage latency** — smaller or newer collections may not be indexed immediately; absence from Rarity Sniper does not mean a collection is not tradeable elsewhere

## Related

- [[rarity-tools]] — the foundational rarity-scoring site and methodology reference
- [[trait-sniper]] — the closest direct competitor, with a browser-extension focus
- [[openrarity]] — open-source rarity standard that some tools publish alongside their native scores
- [[nft-trading]] — broader trading context for how rarity tools fit into an NFT workflow
- [[nft]] — primary asset class

## Sources

- NFT rarity tooling overview; Rarity Sniper cited alongside rarity.tools and TraitSniper as a commonly-used rarity platform (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]])
- Rarity Sniper (raritysniper.com) confirmed still operating as of mid-2026; exact current paid-tier pricing is not publicly published, so verify tier features and prices directly before relying on them. Discord bot commands and any chain coverage beyond Ethereum should likewise be checked against the live site.
