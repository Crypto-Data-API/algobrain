---
title: "EtherRock"
type: entity
created: 2026-04-07
updated: 2026-06-24
status: excellent
tags: [nft, crypto, ethereum, digital-art, history, meme]
aliases: ["EtherRocks", "EtherRock", "Ether Rock", "Ether Rocks"]
entity_type: protocol
founded: 2017
headquarters: ""
website: "https://etherrock.com"
related: ["[[nft]]", "[[ethereum]]", "[[nft-trading]]", "[[cryptopunks]]", "[[mooncats]]", "[[curio-cards]]", "[[autoglyphs]]"]
---

EtherRock is a collection of 100 clipart-rock images on the [[ethereum]] blockchain, created in December 2017 by an anonymous developer. Each of the 100 rocks uses the same Pet-Rock-style clipart image, differentiated only by color — there are no traits, no breeding, and no utility. Created as a simple experiment in digital scarcity during the earliest days of Ethereum NFTs, EtherRock was almost completely forgotten until August 2021, when "NFT archaeologists" rediscovered the contract during the NFT boom and floor prices briefly exceeded **$1 million per rock**. The spectacle of million-dollar rock JPEGs became an international media story and remains one of the most-cited examples of NFT speculation, meme culture, and the power of extreme scarcity (a 100-unit hard cap) combined with verifiable on-chain provenance.

> **Disclaimer**: This page is a historical and structural reference. No live floor prices are quoted for the current market. NFT collectibles are highly illiquid, sentiment-driven, and speculative; values can fall to near-zero. Nothing here is financial advice. As of **2026-06-24** the broad crypto tape is in an **Established Bear Market** (Fear & Greed = 22, "Extreme Fear"; BTC ≈ $62.6k, ETH ≈ $1.66k) — a backdrop in which thin, sentiment-driven collectible markets like EtherRock typically see depressed bids and very wide spreads.

## How EtherRock Works

EtherRock predates the [[erc-721|ERC-721]] standard (proposed late 2017, finalized January 2018). It is a single, bespoke smart contract that maintains an internal ledger of which address owns each of the 100 numbered rocks, plus a built-in sale mechanism.

- **Sale mechanism**: The contract itself acts as a primitive marketplace. An owner can list a rock for a price denominated in ETH, and a buyer can call the contract to purchase it. This on-contract listing/settlement logic was unusual and is part of the historical interest — the "marketplace" is the contract, not a third-party platform.
- **Art storage (off-chain)**: Unlike fully on-chain projects such as [[autoglyphs|Autoglyphs]], EtherRock does **not** store its images on-chain. The rock images are hosted off-chain and referenced by the project; the chain stores ownership and the sale state, not the pixels. This is a meaningful provenance distinction: the canonical asset is the on-chain ownership record, while the image is an off-chain artifact tied to it by convention.
- **Pre-721 marketplace incompatibility**: Because the original contract is not ERC-721, it is not natively readable by modern marketplaces. Trading on [[opensea|OpenSea]]/[[blur|Blur]] generally happens via **wrapper contracts** that mint a standards-compliant token representing custody of an underlying rock (similar in spirit to how [[curio-cards|Curio Cards]] and [[rare-pepes|Rare Pepes]] became marketplace-tradeable). Wrapping adds a layer of smart-contract trust.
- **No royalties / no utility**: There is no creator-royalty mechanism enforced by the original contract, no roadmap, no governance, no airdrops. The value proposition is intentionally pure: ownership of one of 100 rocks from a December 2017 contract.

### The Art (or Lack Thereof)

EtherRock's "art" is a single clipart image of a smooth, oval gray stone, recolored 100 times. There is no generative algorithm, no shape variation, and no creative intent beyond "here is a rock in a different color." This is the point: EtherRock's value has nothing to do with aesthetics and everything to do with scarcity, provenance, and meme culture. It is the archetype of the "provenance over pixels" thesis.

## Collection Economics

- **Hard cap**: 100 rocks, all now minted. There can never be a Rock #101.
- **Original distribution**: Rocks were sold sequentially from the contract at a price that stepped up with each sale; early rocks cost fractions of an ETH. Roughly 20 of 100 were claimed in 2017–2020; the remaining ~80 were minted in the August 2021 frenzy.
- **Royalties**: None enforced on-chain. Secondary trades on wrapper-enabled marketplaces may carry that marketplace's fee schedule, not a creator royalty.
- **Notable sales** (documented, dated): Rock #21 reportedly sold for ~400 ETH in August 2021 (~$1.3M at the time); the August 2021 floor briefly exceeded ~305 ETH (~$1M+). See the Notable Sales table below. No current floor is asserted here.

## Comparison vs Peer Early-NFT Collections

| Collection | Chain | Year | Supply | Art storage | Defining trait |
|---|---|---|---|---|---|
| **EtherRock** | [[ethereum]] | Dec 2017 | 100 | Off-chain image | Ultra-low supply meme/provenance play |
| [[cryptopunks\|CryptoPunks]] | Ethereum | Jun 2017 | 10,000 | On-chain (hashes / later fully) | Canonical PFP, deep liquidity |
| [[autoglyphs\|Autoglyphs]] | Ethereum | Apr 2019 | 512 | Fully on-chain generative | "Grandfather of on-chain generative art" |
| [[curio-cards\|Curio Cards]] | Ethereum | May 2017 | ~30 designs (~30k+ tokens) | Off-chain (wrapped to ERC-1155) | Earliest art-NFT, edition-based |
| [[mooncats\|MoonCats]] | Ethereum | Aug 2017 | 25,600 | On-chain generative | Rediscovered "NFT archaeology" case |

EtherRock's distinguishing feature versus all of these is its **100-unit supply** — an order of magnitude scarcer than CryptoPunks or MoonCats, and scarcer even than Autoglyphs (512). That scarcity is the entire trading thesis, but it is also why no "floor sweep" or basket strategy exists.

## How & Where It Trades

- **Native contract**: Buying/selling can still be done directly through the original EtherRock contract logic (and the minimalist etherrock.com interface), which reflects the project's bare-bones ethos.
- **Modern marketplaces**: Via wrapper contracts, rocks appear on [[opensea|OpenSea]] and [[blur|Blur]]. Liquidity is concentrated in occasional one-off listings rather than a deep order book.
- **Liquidity profile**: Among the most illiquid collections in all of NFTs — only 100 units exist and most are held by long-term collectors. Trades can be weeks or months apart; the bid-ask spread is effectively a negotiation, not a quote. There is no reliable "tap the floor" exit.

## Narrative, Category & Catalysts

EtherRock sits in the **"OG / provenance NFT"** category alongside CryptoPunks, Curio Cards, MoonCats, and Autoglyphs, but with a strong overlay of **meme culture**. Its price is reflexive: media attention drives buyers, buyers drive price, price drives more media. Catalysts that historically moved it include (1) renewed NFT-cycle risk appetite, (2) viral media moments about "million-dollar rocks," and (3) broad ETH/crypto bull regimes. In a bear tape like mid-2026, all three catalysts are dormant.

## History / Timeline

**Key dated events:**

- **December 2017**: EtherRock smart contract deployed to Ethereum mainnet; rocks purchasable directly from the contract at a price that stepped up per sale. Bare-bones etherrock.com website.
- **December 2017 – July 2021**: Only ~20 of 100 rocks minted/sold. The project was virtually unknown — no community, no social presence, ~80 rocks unclaimed.
- **August 1–7, 2021**: NFT community rediscovers EtherRock during the "NFT archaeology" trend; word spreads on crypto Twitter about the 2017-era rocks with only ~20 minted.
- **August 7–15, 2021**: Minting and buying frenzy. The remaining ~80 rocks are minted rapidly; secondary prices skyrocket on the ultra-scarce supply.
- **August 22–24, 2021**: Floor surpasses **$1 million** (~305+ ETH at the time). CNBC, Bloomberg, BBC, and the Washington Post cover the "million-dollar rock JPEG" story.
- **August 2021**: Rock #21 reportedly sold for ~400 ETH (~$1.3M). Rock #55 was reportedly listed for ~2,000 ETH (~$6.6M), though it is unclear whether that sale completed.
- **September 2021 onward**: Prices decline from the August peak but remain elevated through early 2022, then fall with the broader NFT market in 2022–2023.
- **2024–2026**: Trading continues at sharply reduced volumes and prices. EtherRock remains a recognizable brand and a standard case study in NFT market dynamics.

## Notable Sales

| Rock # | Sale Price | Date | Notes |
|--------|-----------|------|-------|
| #21 | ~400 ETH (~$1.3M) | Aug 2021 | One of the highest confirmed sales |
| #72 | ~69 ETH (~$230K) | Aug 2021 | Early in the frenzy |
| Various | 305+ ETH | Aug 2021 | Floor briefly above ~305 ETH |

## Risks

- **Extreme illiquidity**: 100 units, mostly held long-term. Exiting at a quoted price is rarely possible; realized exit prices can be far below any "last sale."
- **Sentiment reflexivity**: Value is driven by attention and the NFT cycle. In Extreme-Fear regimes (e.g., 2026-06-24) bids thin out and the reflexive loop runs in reverse.
- **Off-chain art dependency**: The image is hosted off-chain; long-term, the canonical asset is the on-chain ownership record, but the visual depends on continued hosting/convention.
- **Wrapper / custody risk**: Trading on modern marketplaces requires wrapper contracts that introduce additional smart-contract trust and potential counterfeit-wrapper risk.
- **Wash-trading / price-signal risk**: In thin NFT markets, a handful of trades (or self-dealing) can set a misleading "floor." Treat headline last-sale figures skeptically.
- **Contract age**: The original contract predates modern auditing practices; it has functioned without incident since 2017 but carries pre-721 technical risk.

## Collector / Trading Playbook

- **Treat as a blue-chip collectible, not a tradable asset.** With 100 units and infrequent trades, position sizing should assume you may not be able to exit for months and that realized prices are negotiation-driven.
- **Provenance verification first**: Confirm the rock derives from the original EtherRock contract and that any wrapper is the legitimate one before transacting.
- **Bear-tape dynamics**: In the current Extreme-Fear regime, illiquid OG collectibles often see the widest spreads of the cycle — patient, low-ball OTC bids tend to be the only real liquidity. Avoid chasing "last sale" prices.
- **Catalyst-aware**: The asset is reflexive; meaningful repricing historically requires a renewed risk-on NFT cycle plus a media catalyst, neither present in mid-2026.

## Historical Price Trajectory (2017–2023, documented)

The table below is a **historical** record of the August-2021 mania and its aftermath, not a current quote. No live floor is asserted.

| Date | Floor Price (ETH) | Floor Price (USD approx.) | Context |
|------|-------------------|---------------------------|---------|
| December 2017 | <0.1 ETH | <$50 | Launch — negligible interest |
| 2018-July 2021 | N/A | N/A | No market activity; ~80 rocks unminted |
| August 1-7, 2021 | 5-20 ETH | $15,000-$65,000 | Rediscovery begins |
| August 8-15, 2021 | 50-100 ETH | $160,000-$330,000 | Rapid acceleration |
| August 22-24, 2021 | 305-400 ETH | $1,000,000-$1,300,000 | Peak — million-dollar rocks |
| September 2021 | 100-200 ETH | $350,000-$700,000 | Initial decline from peak |
| January 2022 | 70-100 ETH | $200,000-$300,000 | Still elevated |
| June 2022 | 20-40 ETH | $25,000-$50,000 | Post-crash |
| 2023 | 10-25 ETH | $15,000-$45,000 | Bear market stabilization |
| 2024-2026 | Variable | Variable | Reduced market, niche trading |

## Cultural Significance

**The ultimate meme NFT**: EtherRock is the single most-cited example of NFT absurdity. A collection of 100 identical rock clipart images selling for over $1 million each was both a genuine market phenomenon and a cultural punchline. Media coverage typically used EtherRock as shorthand for the perceived insanity of the NFT market. Whether you view it as brilliant market dynamics or market madness depends on your perspective — but no one can ignore it.

**Scarcity as value**: EtherRock is the purest demonstration that scarcity alone — combined with historical provenance and cultural attention — can create enormous value regardless of artistic merit. The art is objectively worthless. The supply is 100. The contract is from 2017. The combination was worth millions.

**Provenance premium in action**: EtherRock's value derived almost entirely from its December 2017 creation date. If someone deployed an identical contract in 2021 with identical rock images, it would have been worthless. The on-chain timestamp — verifiable by anyone — was the fundamental source of value. This principle applies across the NFT market but nowhere more purely than EtherRock.

**NFT archaeology validation**: Along with [[mooncats|MoonCats]] and [[curio-cards|Curio Cards]], EtherRock's rediscovery validated the concept of "NFT archaeology" as a viable market activity. The idea that forgotten smart contracts could contain immense latent value motivated a wave of blockchain research and exploration.

**Media and reflexivity**: EtherRock demonstrated the reflexive relationship between media coverage and NFT prices. The story of million-dollar rocks generated massive media attention, which drew more buyers, which drove prices higher, which generated more media coverage. This reflexive loop — a concept described by [[george-soros|George Soros]] in financial markets — operated at an accelerated pace in the NFT market.

**The "it's just a JPEG" argument**: EtherRock became the standard reference in debates about NFT value. Critics used million-dollar rocks to argue that NFTs were pure speculation with no intrinsic value. Proponents argued that the value was in the provenance, scarcity, and cultural significance — not the JPEG. The debate remains unresolved but EtherRock is always Exhibit A.

## Holder Base

EtherRock holders skew toward wealthy crypto natives, NFT historians, and meme-culture enthusiasts. Many acquired rocks during the August 2021 frenzy and have held through the subsequent decline; turnover is very low. This long-term-holder dominance is part of why the collection trades so infrequently — there is little "weak-hand" float to set a continuous price.

## Sources

General market knowledge; no specific wiki source ingested yet. Dated figures (August 2021 sales, media coverage) reflect widely-reported public events. Macro framing as of 2026-06-24 per cryptodataapi.com / CoinGecko snapshot (Fear & Greed = 22, Established Bear Market).

## Related

- [[nft]] — NFT market overview and history
- [[ethereum]] — Underlying blockchain
- [[cryptopunks]] — The most iconic early Ethereum NFT (June 2017)
- [[mooncats]] — Another rediscovered early Ethereum NFT (August 2017)
- [[curio-cards]] — Another early Ethereum NFT project (May 2017)
- [[rare-pepes]] — Even earlier NFTs on Bitcoin (2016)
- [[nft-trading]] — NFT trading strategies
