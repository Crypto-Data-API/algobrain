---
title: "NFT Royalty Enforcement"
type: concept
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, nft, market-microstructure]
aliases: ["Creator Royalties", "NFT Royalties", "Operator Filter Registry"]
related: ["[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]", "[[opensea]]", "[[blur]]", "[[sudoswap]]", "[[looksrare]]", "[[magic-eden]]", "[[rarible]]"]
domain: [market-microstructure]
prerequisites: ["[[nft]]", "[[nft-trading]]"]
difficulty: intermediate
---

NFT creator royalties are the per-sale percentage paid to the original creator on every secondary sale, typically 5-10%. The royalty is not enforced at the ERC-721 token standard level — it is a voluntary marketplace convention. The 2022-2023 "royalty wars" turned that voluntariness into an open economic fight between marketplaces, creators, and traders. By mid-2023, enforced royalties on Ethereum were effectively dead, which re-priced the entire round-trip cost structure of NFT trading and made strategies like [[nft-arbitrage]] dramatically more profitable.

## Mechanism

An NFT contract records a suggested royalty via the EIP-2981 standard, which exposes a `royaltyInfo(_tokenId, _salePrice)` function returning the `receiver` address and `royaltyAmount`. The EIP itself states explicitly that "the royalty payment must be voluntary, as transfer mechanisms such as `transferFrom()` include NFT transfers between wallets, and executing them does not always imply a sale occurred." Nothing in the ERC-721 or ERC-1155 standards forces a transfer to pay the royalty. Enforcement therefore lives one level up, at the marketplace smart contract or front-end:

- The marketplace fetches `royaltyInfo` on listing or sale.
- It splits the paid ETH into three flows: creator royalty, marketplace fee, and seller proceeds.
- Whether the royalty is actually paid depends entirely on whether that marketplace chose to respect it.

Because a marketplace is a smart contract, "the marketplace paid royalties" is really "the smart contract logic of that marketplace included the royalty transfer." Any competing contract can choose not to.

## The 2022-2023 Royalty Wars

Through 2021 and early 2022, [[opensea]] dominated Ethereum NFT volume and enforced a creator-configurable 5-10% royalty by marketplace policy. Most creators' business models depended on this secondary revenue, and NFT roadmaps were often funded by projected royalty income.

A series of events compressed royalties to zero:

1. **[[sudoswap]] launch (July 2022)** — Sudoswap introduced an AMM-based NFT trading model with no royalties at all. Because listings could be placed into bonding-curve pools with no marketplace-level royalty hook, creators had no way to collect. Trading on Sudoswap exploded for collections where traders would tolerate a non-royalty venue.
2. **X2Y2 optional royalties (August 2022)** — [[looksrare]]'s rival X2Y2 made royalties opt-in for buyers. Buyers who chose to pay got a cosmetic "supports creator" badge; most didn't.
3. **[[blur]] launch (October 2022)** — Blur launched as a pro-trader aggregator with royalties "enforced" only at a 0.5% floor minimum, far below the 5-10% creators expected. In early 2023 it moved to explicit zero-royalty defaults.
4. **Creator response** — Yuga Labs, Doodles, and other creators began excluding Blur and Sudoswap from their collections' smart contract permissions, attempting to block sales on those venues.
5. **Race to the bottom** — Because aggregators (see [[nft-aggregators]]) route to the cheapest venue, any single zero-royalty marketplace drained liquidity from royalty-enforcing ones, forcing each marketplace in turn to cut royalties or lose market share.

By August 2023, enforcement on Ethereum had collapsed.

## Operator Filter Registry

OpenSea's primary defensive mechanism was the **Operator Filter Registry**, launched November 2022. It was a smart contract allowlist / blocklist that creator contracts could integrate to restrict which marketplaces could transfer their NFTs.

How it worked:

- The collection's NFT contract used OpenSea's `DefaultOperatorFilterer` abstract contract.
- Every transfer called `_checkFilterOperator(msg.sender)`.
- If the caller was an address on OpenSea's blocklist — which included Blur's marketplace proxy, Sudoswap, and other royalty-bypassing venues — the transfer reverted.
- Result: the NFT literally could not be sold on Blur, Sudoswap, or similar venues, only on OpenSea and royalty-respecting marketplaces.

Benefits claimed:
- Creators could enforce royalties at the contract level without trusting marketplaces.
- A single centrally-maintained list kept collections up to date.

Problems in practice:
- Centralized: OpenSea controlled the blocklist. Creators were effectively outsourcing their marketplace permissions to their largest competitor.
- Composability broken: DeFi integrations, wallet batch transfers, and other legitimate operators risked being swept up as collateral damage if blocklisted.
- Trading UX punishing: Buyers on Blur who tried to buy a filtered collection saw the transaction revert with no clear error.
- Creators felt squeezed: They were forced to pick a side in a proxy fight between OpenSea and Blur.

## Sunset of the Operator Filter (August 2023)

In August 2023 OpenSea announced it would sunset the Operator Filter Registry and move to an "optional royalty" model for all collections, with a "suggested" royalty displayed to buyers but not enforced. Concretely: the filter stopped blocking marketplaces on **31 August 2023**, with a grace period during which creator-preferred royalties continued to be enforced for collections already using the filter (and on non-Ethereum chains) until **29 February 2024**.

Reasons OpenSea cited publicly:
- Enforcement had become impossible because most liquid collections had already abandoned the filter.
- The filter was splitting the NFT community rather than protecting creators.
- Zero-fee competitors were winning market share regardless of what OpenSea did.

Reasons unsaid but widely understood:
- OpenSea needed to stop losing volume to Blur.
- Maintaining the blocklist was a product liability and legal risk.
- Creator royalty revenue had already collapsed by 60-80% industry wide, so the filter wasn't protecting much.

After the sunset, royalty enforcement on Ethereum became creator-by-creator rather than marketplace-by-marketplace, with most high-volume collections receiving less than 1% effective royalty.

## Alternative Enforcement Mechanisms

Creators explored other approaches with mixed success:

- **Transfer allowlists**: Whitelist only specific marketplaces that pay royalties. Highly restrictive; breaks composability with future venues and DeFi integrations. Used on a few premium drops but mostly rejected.
- **DN-404 and hybrid fungible/NFT standards**: Experimental token standards that mint fungible ERC-20 shadow tokens which "crystallize" into NFTs on transfer, making pure NFT trading harder to route around. Adoption limited to a few 2024 collections.
- **Right of reclaim**: Creator retains an on-chain right to buy back the NFT at the last sale price if the buyer doesn't pay royalty. Mostly theoretical; gas costs and coordination problems prevent adoption.
- **Off-chain rewards tied to royalty payment**: Projects give token airdrops, gated-access rights, or staking yield only to holders who purchased on royalty-paying marketplaces. Weak enforcement but it preserves some incentive. This is the model most surviving creator-economy projects now use.
- **Chain-level enforcement (Solana, Flow)**: Some non-Ethereum chains experimented with royalty-enforcement at the token-program level. [[magic-eden]] on Solana has gone back and forth on enforcement; as of 2024, most Solana NFT royalties are also optional.

## Why This Matters for Traders

The collapse of royalty enforcement changed the economics of NFT trading dramatically:

- **Round-trip cost**: In 2021 the cost of buying and selling an NFT on OpenSea was roughly 2.5% marketplace fee + 5-10% royalty on the sell side + gas. Total round-trip friction was commonly 8-13% of the trade value.
- **2024 and beyond**: On Blur, round-trip friction can be under 1% (zero marketplace fee, zero royalty, bid-accepted gas only). Royalty elimination alone compressed round-trip costs by 70-90% for non-enforcing collections.
- **Arbitrage viability**: [[nft-arbitrage]] strategies requiring 1-3% net edge were entirely infeasible under 10% round-trip costs. Under sub-1% costs, floor-sweep-and-flip strategies that capture 0.5-2% per round trip became consistently profitable.
- **Capacity of strategies**: Lower friction lets the same edge be captured at more turns per month, multiplying capacity.
- **Liquidity bifurcation**: Collections that still enforce royalties via transfer allowlists trade with wider spreads and lower volumes. Most high-liquidity collections now effectively treat royalties as a voluntary tip.
- **Creator capture**: The value captured by creators on secondary markets dropped from hundreds of millions annually (2021-2022) to a fraction of that. Projects whose roadmaps depended on secondary royalties (3D, metaverse, gaming collections) had business models break.

## Examples / Incidents

- **Yuga Labs and the Sewer Pass**: The BAYC parent company launched sub-collections with Operator Filter enforcement, attempting to carve out royalty-paying niches even as the broader market moved on. Royalty capture on Sewer Pass held up better than on BAYC itself but still declined.
- **Doodles opt-out**: Doodles temporarily blocked Blur through the Operator Filter, saw secondary volume collapse, and reversed course within weeks. Became a canonical case of creator capitulation.
- **Sudoswap pools on blue chips**: Bored Ape floor tokens began appearing in Sudoswap pools for the first time in late 2022 as traders routed around the Operator Filter using proxy contracts, signaling the filter's real-world weakness.
- **Blur vs OpenSea market share shift**: By early 2023, Blur had captured more than 70% of Ethereum NFT volume. The Operator Filter was clearly losing, which in retrospect made the August 2023 sunset inevitable.

## 2025-2026 Update

The royalty picture did not reverse:

- **OpenSea's OS2 relaunch (May 2025)** and **$SEA** token airdrop helped OpenSea reclaim overall Ethereum NFT volume leadership, but it did **not** broadly reintroduce enforced royalties — secondary creator fees on OpenSea remain optional/suggested rather than mandatory. Across [[blur]] and [[magic-eden]], royalties likewise remain opt-in or variable as of mid-2026.
- The low round-trip-cost environment (sub-1% on pro venues) that makes [[nft-arbitrage]] viable therefore persists.
- **DN-404** and related hybrid fungible/NFT standards stayed experimental and niche; no hybrid standard achieved durable mainstream adoption as a royalty-enforcement mechanism by 2026. The dominant surviving creator model is off-chain incentives (airdrops, gated access, staking yield tied to royalty-paying purchases) rather than on-chain enforcement.
- No major jurisdiction recharacterized royalties as obligatory licensing payments through mid-2026, so contract-level voluntary royalties remain the status quo.

## Limitations and Open Questions

- Royalty enforcement remains possible in principle at the contract level (transfer allowlists, hybrid standards) but requires sacrificing composability that most creators and buyers want.
- On L2s and newer chains, new enforcement experiments continue, but none have gained durable market share.
- Secondary-royalty business models are largely defunct; creators increasingly rely on primary mint revenue, token airdrops, and off-chain benefits. Trading-relevant royalty enforcement is now a niche feature of a few premium collections.
- Regulatory pressure could revive enforcement if royalties are recharacterized as obligatory licensing payments under copyright law, but as of 2026 this has not happened in any major jurisdiction.

## Related

- [[nft]]
- [[nft-trading]]
- [[nft-arbitrage]]
- [[nft-aggregators]]
- [[nft-floor-price]]
- [[opensea]]
- [[blur]]
- [[sudoswap]]
- [[looksrare]]
- [[magic-eden]]
- [[rarible]]
- [[market-microstructure]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
- EIP-2981 specification: https://eips.ethereum.org/EIPS/eip-2981 (function signature, voluntary nature confirmed)
- OpenSea Operator Filter sunset (31 Aug 2023 stop; grace period to 29 Feb 2024) and shift to optional creator fees: https://cointelegraph.com/news/opensea-disable-on-chain-royalty-enforcement-tool
- OpenSea OS2 relaunch / royalties still optional in 2025-2026: https://opensea.io
- Verified via Perplexity (sonar), 2026-06-11; Operator Filter sunset date and post-2024 optional-royalty status confirmed via WebSearch, 2026-06-11.
