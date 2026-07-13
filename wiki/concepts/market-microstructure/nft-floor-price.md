---
title: "NFT Floor Price"
type: concept
created: 2026-04-22
updated: 2026-07-13
status: good
tags: [crypto, nft, market-microstructure, liquidity]
aliases: ["Floor", "Floor Price", "Collection Floor"]
related: ["[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]", "[[nft-aggregators]]", "[[opensea]]", "[[blur]]", "[[benddao]]", "[[blend]]", "[[wash-trading]]", "[[liquidity]]", "[[cryptodataapi]]"]
domain: [market-microstructure, liquidity]
prerequisites: ["[[nft]]", "[[liquidity]]"]
difficulty: beginner
---

The NFT floor price is the lowest listed ask in a collection across the venues a trader or aggregator observes. Because NFTs are non-fungible, there is no single order book and no mid price the way an ERC-20 token has; the floor is the most widely used scalar proxy for collection valuation. Unlike an average or a median, the floor is set entirely by the most motivated seller, which makes it cheap to manipulate, highly reflexive, and dangerous when used as an oracle.

## Mechanism

For a collection of N tokens, let L be the set of currently listed tokens with ask prices p_1, p_2, ..., p_k. The floor price is:

```
floor = min( p_i ) for all listed tokens i
```

Key properties that follow from the definition:

- The floor moves if a single token is listed or delisted. There is no averaging or depth weighting.
- Historical sales do not affect the live floor. A 100 ETH sale yesterday does not lift the floor if someone is listing at 5 ETH today.
- The floor is venue-dependent. The floor on [[opensea]] can differ from [[blur]] or [[magic-eden]] at any given moment until aggregators arbitrage the gap.
- Trait-rare tokens are usually listed well above the collection floor, so the floor is effectively the floor for the cheapest acceptable-grade tokens.

## Not an Average, Not a Median

The single most common trader mistake is treating the floor as a central-tendency estimate of a collection's value. It is not.

- **Mean sale price** reflects the full distribution of sales including rares and grails; it systematically overstates the price of a generic token.
- **Median sale price** is closer to what a random token actually transacts at, but requires enough sales volume to estimate.
- **Floor price** is the best bid-side approximation of "cost of entry right now" but it represents the single most desperate seller, not the market.

During thin liquidity the floor can diverge wildly from the median sale price. A collection doing zero volume can see its floor drop 40% overnight because one holder panics; the "real" market price — what multiple buyers and sellers would clear at — may be far higher.

## Floor Manipulation

Because the floor is set by a single listing, it is trivially cheap to move in the short term. Traders routinely observe and exploit the following patterns:

- **Floor sweeping** — Buying up the N cheapest listings in a single transaction via an aggregator. This raises the quoted floor immediately and is sometimes done by holders defensively or by whales signaling confidence. Floor sweeps are visible on chain and tracked by [[nansen]] and [[dune-analytics]].
- **Floor delisting / relisting** — Delisting the cheapest token and relisting at a higher price to move the quoted floor. Costs nothing but the gas to cancel and relist. A coordinated holder community can push the quoted floor up meaningfully without any real buy pressure.
- **Fake floor in alternate currency** — Listing an NFT at "0.001 BTC" in a marketplace that quotes in ETH. Some aggregators have historically misread the currency and reported the listing as the new floor, tricking automated buyers. [[blur]] and [[opensea]] now filter alternate-currency listings from the primary floor display.
- **Trait floor manipulation** — Placing a low listing on a token that has a specific rare trait and counting it as "the floor for that trait" to bait trait-focused snipers.
- **Wash trading to lift the floor implicitly** — Selling an NFT to a controlled wallet at an inflated price to create the appearance of a higher-clearing market; the floor itself doesn't move, but perceived valuation does. See [[wash-trading]].

## Clean Floor vs Quoted Floor

Professional traders distinguish the naive quoted floor from the "clean floor" — the lowest listing that is not manipulated, sketchy, or an outlier.

Filters a clean-floor calculation typically applies:
- Exclude listings from wallets that minted at zero cost hours ago.
- Exclude listings in non-native currencies.
- Exclude listings with suspicious metadata (wrong chain, suspicious creator).
- Exclude self-listings (same wallet family buying and listing).
- Exclude listings priced absurdly below recent trades, which suggest a hacked wallet or a fat-finger.

Marketplaces including [[blur]] compute and expose an internal "clean floor" that differs from the naive minimum ask, and most serious NFT analytics platforms use a cleaned version rather than the raw min.

## Floor × Supply Is a Misleading Market Cap

A collection's "market cap" is almost always reported as `floor × total_supply`. This is mechanically wrong for two reasons:

1. Only a small fraction of the supply is listed at the floor. Selling all N tokens at the floor is impossible; the second token sold would clear at a lower price because the floor is rebuilt by the next cheapest listing.
2. Most of the supply is held by illiquid collectors, so the floor does not represent a realizable exit price for the collection aggregate.

A more honest metric is cumulative bid depth — the sum of active collection bids — which represents actual dollars willing to buy now. On [[blur]], bid depth became a first-class metric and is typically 2-10% of quoted market cap.

## Why Traders Watch the Floor

- **Liquidity proxy**: A tighter spread between the floor and the top collection bid implies cheaper round-trip exits. When bid-ask spreads exceed 10-20% the collection is effectively illiquid.
- **Momentum signal**: A rapidly rising floor pulls in attention traders; a falling floor through key psychological round numbers (5 ETH, 10 ETH) can trigger cascading delistings and further declines.
- **Liquidation threshold**: [[benddao]], [[blend]] (see [[nft-lending]]), and other NFT lending protocols use the floor as the oracle for loan-to-value calculations. A 20% floor drop can push entire cohorts of loans below liquidation threshold simultaneously.
- **Arbitrage anchor**: In [[nft-arbitrage]] and for [[nft-aggregators]], the floor across venues is the first price a sweeper sees. Cross-venue floor gaps collapsed after aggregators but still open briefly during fast markets.

## The Blur Bidding Model

[[blur]] reshaped how the floor interacts with the real market. Instead of relying on fragile floor listings, Blur introduced pooled collection bids, where any bidder can place a bid at a chosen price level and be matched against any seller willing to hit that bid. Blur plots the full bid distribution as a depth chart.

The consequences for the floor:

- The true "bid-side floor" — the highest collection-level bid — became visible and trustworthy, often at or within a few percent of the ask-side floor.
- Sellers could "accept bid" rather than relist, tightening the spread and making the floor less manipulable.
- Attempts to prop up the floor via relisting are quickly undercut by anyone willing to hit the existing Blur bid.
- The Blur bid curve became the de facto liquidity oracle for NFT lending, replacing the raw floor for protocols like [[blend]].

## 2025-2026 Update

The mechanics above remain accurate, but the venue landscape shifted:

- **OpenSea reclaimed overall Ethereum NFT volume leadership** in 2025 after its **OS2** relaunch (May 2025) and **$SEA** token airdrop. Blur's pooled-bid depth chart is still a key liquidity reference, but it is no longer the single dominant venue it was in 2023-2024, so a robust floor read now aggregates across OpenSea, Blur, and [[magic-eden]] rather than treating Blur's curve as the sole oracle.
- **[[nft-aggregators|Reservoir]]** — a widely used neutral floor/listing data source — sunset its NFT API on 15 October 2025, so analytics stacks that depended on it migrated to Alchemy, Sequence, or marketplace-native feeds. This matters for anyone computing a cross-venue "clean floor" programmatically.
- Overall NFT trading volume stayed far below the 2021-2022 peak through 2025-2026, meaning thin-liquidity floor distortions (single-listing sensitivity, easy spoofing) are if anything more pronounced for all but a handful of blue-chip and high-throughput phygital collections.

## Examples / Incidents

- **BendDAO August 2022 crisis**: A cascading drop in the BAYC floor triggered mass [[benddao]] liquidations. Auctions opened at the current floor as the starting bid, but in thin, fast-falling markets there were literally zero bidders at those prices. The floor became a broken oracle, bad debt accumulated, and the protocol was forced to change auction parameters. Detailed in [[nft-lending]].
- **Moonbirds reveal collapse**: After the post-reveal rarity re-rate, the quoted floor dropped 30%+ within an hour because rarity-ranked sellers delisted and relisted in a rush, bouncing the min price repeatedly.
- **BAYC floor defense sweeps**: Large holders have periodically coordinated visible floor sweeps (buying dozens of listings simultaneously) to move the quoted floor and restart momentum.

## Limitations

- Single-listing sensitivity makes short-term floor data noisy and easily spoofed.
- Venue fragmentation means any single-venue floor is incomplete; aggregated floors are better but require trusted aggregation.
- Floor is a worst case, not a valuation. Using it as market cap or collateral value systematically overstates collection value.
- No floor exists for collections with zero active listings, which happens to illiquid collections; traders must fall back on last sale or top bid.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/nfts/overview` — NFT market overview
- `GET /api/v1/nfts/collections` — collection list
- `GET /api/v1/nfts/volume` — volume data
- `GET /api/v1/nfts/correlations` — collection correlations

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/nfts/overview"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-nft]].

## Related

- [[nft]]
- [[nft-trading]]
- [[nft-arbitrage]]
- [[nft-aggregators]]
- [[nft-lending]]
- [[nft-rarity-scoring]]
- [[opensea]]
- [[blur]]
- [[magic-eden]]
- [[benddao]]
- [[blend]]
- [[wash-trading]]
- [[liquidity]]
- [[market-microstructure]]
- [[nansen]]
- [[dune-analytics]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
- OpenSea OS2 relaunch / marketplace status: https://opensea.io
- Reservoir NFT/API sunset (15 Oct 2025): https://crypto.news/reservoir-infra-provider-for-coinbase-and-metamask-shuts-down-nft-services/
- Verified via Perplexity (sonar), 2026-06-11; OS2/Blur volume shift and Reservoir sunset confirmed via WebSearch, 2026-06-11.
