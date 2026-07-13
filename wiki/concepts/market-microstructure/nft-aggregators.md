---
title: "NFT Aggregators"
type: concept
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, nft, market-microstructure, liquidity]
aliases: ["NFT Aggregator", "Marketplace Aggregator", "Sweep Aggregator"]
related: ["[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]", "[[nft-floor-price]]", "[[opensea]]", "[[blur]]", "[[magic-eden]]", "[[looksrare]]", "[[rarible]]", "[[tensor]]"]
domain: [market-microstructure, liquidity]
prerequisites: ["[[nft]]", "[[nft-floor-price]]"]
difficulty: intermediate
---

NFT aggregators are protocols and front-ends that pull listings from multiple NFT marketplaces — OpenSea, Blur, LooksRare, X2Y2, Magic Eden, and others — and route buys through a single transaction. They turned a fragmented, per-marketplace shopping experience into a unified "view the whole market, sweep N cheapest" workflow. Aggregators are the reason cross-marketplace spreads, which were 5-20% in 2021, compressed to near-zero in 2023 and beyond.

## Mechanism

Every NFT listing on a marketplace is an on-chain or signed off-chain order that can be filled by anyone with the taker-side permissions and enough funds. Historically, buying required visiting each marketplace separately, connecting a wallet, approving the marketplace contract, and paying gas for each individual fill.

An aggregator:

1. **Indexes listings** by reading order books from each marketplace API (or on-chain order storage such as Seaport's).
2. **Normalizes orders** across different marketplace formats — Seaport (OpenSea / OpenSea-compatible), LooksRare, X2Y2, Blur, etc. — so a single UI can display them.
3. **Routes fills** through a single smart contract that accepts the user's total ETH and, in one transaction, executes each underlying order on its native marketplace.
4. **Batches gas costs** so buying 10 NFTs from 3 marketplaces costs meaningfully less than 10 individual transactions.
5. **Cleans order quality** by filtering spam listings, wrong-chain scams, mis-priced bait, and (sometimes) wash-traded collections.

The core value proposition: one click, one signature, one gas bill, N marketplaces.

## Sweep the Floor

The canonical aggregator operation is the floor sweep. From a single UI:

1. The user selects a collection.
2. The aggregator shows the N cheapest listings across all indexed marketplaces, sorted by price.
3. The user picks a quantity or a spend limit ("buy me 20 BAYC under 30 ETH each").
4. The aggregator constructs a batched transaction that fills each listing atomically in one block.

Because the aggregator contract fills each underlying order on its native marketplace, royalties and marketplace fees are still paid per-order — the aggregator adds no on-chain pricing intermediation, only UX and batching.

## Gas Savings

Batching 10 NFT buys through an aggregator versus 10 separate marketplace transactions typically saves 30-50% in gas on mainnet Ethereum. The savings come from:

- A single transaction overhead (21,000 gas base cost amortized over all buys).
- Reuse of warm storage slots within the aggregator's proxy contract.
- Elimination of redundant approval transactions (the aggregator router requests one approval covering many downstream contracts).
- In some implementations, partial fill handling — if one listing has been canceled since indexing, the rest still succeed without the entire transaction reverting.

On L2s (Base, Polygon, Arbitrum) where gas is already cheap, the batching advantage is smaller but UX still matters because the user signs once.

## Impact on Market Efficiency

Before aggregators, identical NFTs routinely listed 5-20% cheaper on LooksRare than on OpenSea because LooksRare had smaller volume and fewer buyers. An aggregator buyer sees both simultaneously and will always hit the cheapest first. Within months of aggregator adoption (late 2021 through 2022):

- Cross-marketplace floor spreads collapsed to near zero for major collections.
- Arbitrage bots running between marketplaces became unprofitable at the pure spatial level — the spread is closed by the aggregator's own routing.
- Listings migrated toward the marketplaces with the lowest fees, because aggregators make fees the only differentiator.
- Smaller marketplaces (X2Y2, LooksRare) lost pricing power; they could no longer quietly maintain higher-volume exclusive listings.
- Fees dropped industry-wide as marketplaces competed in a race to the bottom — culminating in [[blur]]'s zero-fee model and [[opensea]] subsequently reducing fees to zero for most collections.

## Major Aggregators

- **Genie** — The first production NFT aggregator, launched November 2021. Acquired by Uniswap Labs in June 2022 for integration into Uniswap's broader DEX infrastructure. Genie pioneered the sweep-the-floor UX and batched-fill smart contracts that competitors copied.
- **Gem** — Launched around the same time as Genie with a focus on portfolio-management and pro-trader features (trait filters, saved sweep templates). Acquired by [[opensea]] in April 2022 and subsequently integrated as OpenSea Pro.
- **OpenSea Pro** (formerly Gem) — OpenSea's official power-user front end, aggregating listings across 170+ marketplaces. Zero marketplace fees; royalties optional. Acts as both aggregator and primary venue.
- **[[blur]]** — Launched as an aggregator first (October 2022), then pivoted to become both an aggregator and the dominant pro-trader marketplace. Combines aggregation with its own bid-pool marketplace and [[blend]] lending. By 2024 Blur was processing the majority of Ethereum NFT volume (frequently cited above 70-75%). That dominance eroded through 2025: after OpenSea relaunched as **OS2** (May 2025) and announced a **$SEA** token airdrop, OpenSea reclaimed the top spot in overall Ethereum NFT volume. As of mid-2026 Blur remains a major venue and the leading pro-trader marketplace, but is no longer the unambiguous overall ETH volume leader.
- **Reservoir** — Was a neutral infrastructure layer rather than a consumer-facing aggregator, providing a unified API and router contract that any front-end could use to build its own aggregator. Many third-party NFT apps and wallets (including Coinbase and MetaMask) routed through Reservoir rather than integrating each marketplace individually. **Reservoir sunset its NFT API and associated services on 15 October 2025** — just months after a $14M raise — and pivoted its team to Relay Protocol (a general token swap/bridge layer). It open-sourced its codebase and partnered with Alchemy and Sequence to migrate customers off the platform. The router pattern Reservoir pioneered lives on in those successors.
- **[[tensor]]** — The dominant Solana NFT aggregator / marketplace hybrid, serving the Solana ecosystem where [[magic-eden]] is the main counterparty.
- **[[magic-eden]]** — Originally a Solana-native marketplace, has expanded into multi-chain aggregation across Solana, Ethereum, Bitcoin (Ordinals), and Base.

## Role in the Arbitrage Workflow

Aggregators are both the tool that kills simple cross-venue arbitrage and the platform on which more sophisticated arbitrage runs. Common trader uses:

- **Floor sweep arbitrage**: Buy 10-50 floor tokens on an aggregator, immediately list on [[blur]] one or two percent above floor to capture bid depth from a pending collection bid.
- **Bid / ask sandwich**: Place a collection bid on Blur at price X, then use an aggregator to sweep a listing at price X + small, flipping the position instantly.
- **Trait filtering at scale**: Filter thousands of listings across all venues for a specific rare trait, then buy below the trait-floor price. See [[nft-rarity-scoring]].
- **Portfolio liquidation**: Sell 50 tokens by routing accept-bid transactions through an aggregator, taking the highest bid per token across venues in one signed transaction.
- **Cross-chain watchlists**: Aggregators with Bitcoin Ordinals plus Ethereum plus Solana support let traders monitor related collections across chains simultaneously.

## Examples / Incidents

- **Uniswap acquisition of Genie (June 2022)**: Validated aggregation as infrastructure rather than a standalone consumer product, and set the expectation that NFT trading would become part of DEX/swap infrastructure.
- **OpenSea acquisition of Gem (April 2022)**: Defensive move by OpenSea to prevent an aggregator from becoming a disintermediating front-end.
- **Blur airdrop (February 2023)**: Blur's aggressive point-and-airdrop program shifted a massive share of Ethereum NFT volume to its aggregator in weeks, forcing OpenSea to match on fees and launch OpenSea Pro.
- **Royalty bypass through aggregators**: Aggregators that routed to zero-royalty venues (Sudoswap, Blur) in preference to royalty-enforcing venues accelerated the industry shift to optional royalties. See [[nft-royalty-enforcement]].

## 2025-2026 Update

The aggregator landscape consolidated significantly:

- **Reservoir wound down** its NFT API on 15 October 2025 (see above), removing a major neutral infrastructure layer; front-ends migrated to Alchemy, Sequence, or in-housed the open-sourced code.
- **OpenSea's OS2 relaunch (May 2025)** plus the $SEA token airdrop reasserted OpenSea as the overall Ethereum volume leader, partly reversing Blur's 2023-2024 dominance.
- The overall NFT market remained well below its 2021-2022 peak through 2025-2026, so aggregator volumes are correspondingly thinner, but the core "view the whole market, sweep N cheapest" workflow and near-zero cross-venue spreads persist.
- Phygital marketplaces such as [[phygital-nfts|Courtyard]] became some of the highest-volume venues by transaction count in 2026, though they are vertically integrated (vault + mint + marketplace) rather than cross-venue aggregators.

## Limitations and Risks

- **Stale listings**: Aggregator indexes can lag the underlying marketplaces by seconds. In hot markets, traders submit sweeps that partially fail because the cheapest listings were already filled.
- **Gas cost on reverts**: A partial revert — where some listings have been canceled between index and fill — can leave the buyer paying gas for the full batch while receiving only some of the NFTs.
- **Aggregator contract risk**: The aggregator's router contract holds temporary custody during the fill. A bug in the router is a systemic risk for everyone sweeping through it. Reservoir and Seaport Conduit both require user approvals that, if malicious, could drain wallets.
- **Front-running and MEV**: Public sweep transactions are observable in the mempool. Bots can race to buy the same listings at the same gas price, causing either the user or the bot to partially fail. Private mempools (Flashbots Protect, aggregator-level MEV protection) mitigate but do not eliminate.
- **Filtered listings surprise**: Aggregators quietly exclude listings they deem bait or scam. Sellers can't rely on their listing being visible to all buyers. Buyers can't rely on seeing every listing.
- **Listing fee asymmetry**: The buyer pays marketplace fees per underlying order even when using a zero-fee aggregator, so the apparent savings can be overstated.

## Related

- [[nft]]
- [[nft-trading]]
- [[nft-arbitrage]]
- [[nft-floor-price]]
- [[nft-rarity-scoring]]
- [[nft-royalty-enforcement]]
- [[opensea]]
- [[blur]]
- [[magic-eden]]
- [[looksrare]]
- [[rarible]]
- [[tensor]]
- [[sudoswap]]
- [[market-microstructure]]
- [[nansen]]
- [[dune-analytics]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
- Reservoir NFT/API sunset (15 Oct 2025), pivot to Relay Protocol: https://crypto.news/reservoir-infra-provider-for-coinbase-and-metamask-shuts-down-nft-services/
- OpenSea OS2 relaunch and $SEA token, marketplace status: https://opensea.io
- Verified via Perplexity (sonar), 2026-06-11; Reservoir sunset and OS2/Blur volume shift confirmed via WebSearch, 2026-06-11.
