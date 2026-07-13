---
title: "NFT Rarity Scoring"
type: concept
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, nft, market-microstructure]
aliases: ["Rarity Score", "NFT Rarity Ranking", "Trait Rarity"]
related: ["[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]", "[[nft-floor-price]]", "[[cryptopunks]]", "[[bored-ape-yacht-club]]", "[[art-blocks]]"]
domain: [market-microstructure, valuation]
prerequisites: ["[[nft]]", "[[nft-trading]]"]
difficulty: intermediate
---

NFT rarity scoring is a family of algorithms that assign each token in a generative collection a numerical rank based on the frequency of its visual or on-chain traits relative to the rest of the supply. Rarity scores give traders a standardized way to compare pieces inside a collection, spot undervalued tokens whose rank exceeds their listing price, and build statistical arbitrage strategies across an otherwise opaque asset class.

## Mechanism

A PFP or generative collection (10k-style) is assembled from a fixed trait dictionary — background, body, eyes, mouth, hat, accessory, and so on. For each trait value, the collection has a known frequency: for example, a Laser Eyes trait on 0.5% of supply has frequency 0.005. Rarity scoring algorithms aggregate those trait frequencies across all traits in a given token into a single number.

Three methods dominate:

### 1. Rarity Score (rarity.tools method)
Introduced by rarity.tools in April 2021, this is the most widely cited formula:

```
rarity_score(token) = sum over traits of ( 1 / trait_frequency )
```

A trait that appears in 1% of the collection contributes a score of 100; a trait that appears in 50% contributes 2. The sum over all traits is the token's score, and tokens are ranked from highest score (rarest) to lowest.

The method balances two failure modes that plagued earlier approaches: a simple product of frequencies collapses toward zero and is dominated by the single rarest trait, while averaging washes out rarity entirely. Summing reciprocals keeps both overall trait distribution and individual rare traits visible in the score.

### 2. Statistical Rarity
The product of trait frequencies:

```
statistical_rarity(token) = product over traits of ( trait_frequency )
```

This answers the literal question "what is the probability a random token has this exact trait combination?" It is mathematically clean but suffers because it is dominated entirely by the single rarest trait — a token with one 0.1% trait and six 50% traits scores nearly identically to a token with one 0.1% trait and six 20% traits, even though the second is more broadly rare.

### 3. Information Content / OpenRarity
OpenRarity is an open-source rarity protocol originated jointly by OpenSea, Curio, icy.tools, and PROOF (partners confirmed on the [ProjectOpenSea/open-rarity GitHub](https://github.com/ProjectOpenSea/open-rarity)). It models rarity using Shannon entropy from information theory:

```
information_content(trait_value) = -log2( trait_frequency )
rarity(token) = sum over traits of information_content(trait_value)
```

The log transformation solves the "dominated by rarest trait" problem of statistical rarity while remaining grounded in probability theory. It also makes scores additive across independent traits, which is theoretically cleaner than the reciprocal-sum heuristic. Several marketplaces adopted it as a neutral alternative to rarity.tools when collections or platforms disputed proprietary rankings.

## The Rarity-Premium Curve

Empirically, the sale price of an NFT within a collection rises non-linearly with rarity rank. For most 10k PFP collections the relationship looks like:

- Floor tier (ranks ~500 through 9999): prices cluster tightly around the collection floor. Additional rarity above floor adds single-digit percentage premium.
- Mid-tier (ranks ~50 to ~500): premium grows roughly logarithmically — a rank-100 token typically trades at 1.5-3x floor.
- Top tier (ranks 1-50): premium explodes. The rarest pieces — "grails" — can trade at 10x, 50x, or 100x floor for famous collections. The CryptoPunks alien and ape variants are extreme examples, trading for hundreds to thousands of ETH versus a sub-40 ETH floor.

The curve is not smooth. Collections develop "trait obsessions" where a particular trait (Gold Fur, Solid Gold, Laser Eyes) commands a premium far exceeding its statistical rarity because of cultural or meme value.

## How Traders Use It

- **Statistical arbitrage within a collection**: Traders scan listings, compare listing price to rarity rank, and buy tokens whose price is low for their rank. This is the core strategy of [[nft-arbitrage]] inside a single collection, distinct from cross-venue arbitrage.
- **Sniping on mint**: For new drops, rarity scores are not visible until reveal. Tools like TraitSniper and Rarity Sniper race to publish rarity rankings within seconds of reveal, enabling snipers to buy under-listed rares before the market reprices.
- **Trait floor pricing**: Rather than using a single collection floor, serious traders track a "trait floor" — the lowest listing with a given rare trait. The spread between the overall floor and the rare-trait floor reveals where the market places premium.
- **Portfolio valuation**: Lending protocols and portfolio trackers use rarity-adjusted valuation rather than plain floor × count.
- **Bid placement**: On [[blur]], traders place bids at specific rarity-rank thresholds rather than at floor, allowing them to scoop mid-rares at floor-equivalent prices from sellers who are rank-illiterate.

## Examples

- **CryptoPunks**: The nine Alien Punks (0.09% of supply) became the canonical rarity benchmark. Punk 5822 sold for 8000 ETH in February 2022. Statistical rarity alone cannot explain this premium; it is driven by the combination of rarity and collection history.
- **Bored Ape Yacht Club**: Solid Gold Fur (0.46% of supply) commands a systematic multi-hundred-ETH premium over the floor, regardless of other traits. The trait-fur dimension dominates the rarity calculation in practice.
- **Art Blocks Curated**: Generative art collections complicate rarity because many traits are continuous (color ranges, algorithmic parameters) rather than discrete. Rarity scoring here is often replaced by curator and artist-based taste rankings.
- **Pudgy Penguins**: After the 2023 brand resurgence, mid-rarity penguins (ranks 1000-3000) re-rated sharply upward as collectors discovered the collection lacked the extreme rarity spread of CryptoPunks, making "normal" penguins the usable trading unit.

## 2025-2026 Note

The methods above are mathematical and historically stable — the rarity.tools reciprocal-sum formula (2021), statistical rarity, and OpenRarity information-content scoring remain the canonical approaches and have not been superseded. What changed by 2026 is mostly context: with overall NFT volume far below the 2021-2022 peak, rarity-based statistical arbitrage within a collection is a thinner, more episodic edge concentrated in a few liquid blue-chips, and rarity-snipe-on-reveal opportunities are rarer simply because there are far fewer hyped 10k generative mints. OpenSea integrated rarity ranking natively, reducing reliance on standalone calculators, though independent tools (TraitSniper, Rarity Sniper) still serve fast-reveal sniping.

## Limitations

- **Subjective traits override math**: Traits like "bored" versus "tired" mouths in BAYC have near-identical rarity but wildly different market prices based on community memes. Pure rarity math misses this entirely.
- **Trait-level market preferences**: The market can assign a premium to a specific value (e.g., Gold Fur) that swamps the aggregate rarity score. A rank-3000 token with Gold Fur can out-sell a rank-100 token without it.
- **Rarity drift across calculators**: rarity.tools, OpenRarity, and CoinStats can produce meaningfully different ranks on the same token. Disputes over canonical rankings are common and can move markets when a marketplace switches methods.
- **Trait correlation**: All three standard methods assume trait independence. In practice traits are correlated (certain hats only appear with certain bodies), which biases the raw scores.
- **Thin sample for grails**: The top 10-20 tokens in a collection often have unique trait combinations appearing only once. "Rarity" collapses into "uniqueness" and the scoring system stops discriminating meaningfully.
- **Metadata manipulation**: For off-chain metadata (IPFS, centralized servers) a malicious creator can in principle alter the trait distribution. On-chain metadata (Art Blocks, CryptoPunks) avoids this but is a minority of the market.

## Related

- [[nft]]
- [[nft-trading]]
- [[nft-arbitrage]]
- [[nft-floor-price]]
- [[nft-aggregators]]
- [[cryptopunks]]
- [[bored-ape-yacht-club]]
- [[art-blocks]]
- [[pudgy-penguins]]
- [[market-microstructure]]
- [[nansen]]
- [[dune-analytics]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
- OpenRarity GitHub repository: https://github.com/ProjectOpenSea/open-rarity (partners, methodology)
- rarity.tools rarity-score methodology (reciprocal-sum formula, 2021): https://rarity.tools
- Verified via Perplexity (sonar), 2026-06-11. Note: live consumer status of standalone calculators (rarity.tools, TraitSniper) was not independently confirmable; page claims are methodological/historical and remain accurate.
