---
title: "Curio Cards"
type: entity
created: 2026-04-07
updated: 2026-06-24
status: excellent
tags: [nft, crypto, ethereum, digital-art, history]
aliases: ["CurioCards", "Curio Card", "CurioCard"]
entity_type: protocol
founded: 2017
headquarters: ""
website: "https://curio.cards"
related: ["[[nft]]", "[[ethereum]]", "[[nft-trading]]", "[[cryptopunks]]", "[[rare-pepes]]", "[[etherrock]]", "[[autoglyphs]]", "[[mooncats]]"]
---

Curio Cards is one of the earliest art-NFT projects on [[ethereum]], launched in May 2017 — weeks before [[cryptopunks|CryptoPunks]]. The collection consists of 30 unique digital card designs created by 7 artists, with varying edition sizes (typically around 2,000 per card, plus a few low-edition rarities). Curio Cards used a bespoke smart contract that predates the [[erc-721|ERC-721]] standard, making it one of the most historically significant projects in the evolution of NFTs. Largely forgotten for years after its creation, the project was rediscovered during the 2021 NFT boom and made marketplace-tradeable via a community ERC-1155 wrapper, with floor prices spiking from near-zero to multiple ETH per card.

> **Disclaimer**: This page is a historical and structural reference. No live floor prices are quoted for the current market. NFT collectibles are highly illiquid, sentiment-driven, and speculative; values can fall sharply. Nothing here is financial advice. As of **2026-06-24** the broad crypto tape is in an **Established Bear Market** (Fear & Greed = 22, "Extreme Fear"; BTC ≈ $62.6k, ETH ≈ $1.66k), a backdrop in which thin OG-NFT markets typically show wide spreads and low volume.

## How Curio Cards Work

Curio Cards predates the [[erc-721|ERC-721]] standard (proposed late 2017, finalized January 2018), so each of the 30 card designs was issued by its own **bespoke, pre-721 smart contract** deployed in May 2017. This architecture has several consequences a collector should understand:

- **Edition-based, not 1-of-1**: Unlike PFP collections, Curio Cards are *editions* — each design has a fixed number of identical copies (roughly ~2,000 for common designs, fewer for rarities). Collectors often pursue a **complete set** of all 30 designs, which creates set-completion demand distinct from single-trait pricing.
- **Off-chain art**: The card images are stored off-chain; the contracts track ownership of editions. The canonical asset is the on-chain edition ownership, with the image tied by convention (similar to [[etherrock|EtherRock]], and unlike fully on-chain [[autoglyphs|Autoglyphs]]).
- **ERC-1155 wrapper for tradeability**: Because the original pre-721 contracts are not natively readable by modern marketplaces, a **community-built wrapper contract** (deployed May 2021) lets holders wrap originals into standards-compliant ERC-1155 tokens that trade on [[opensea|OpenSea]] and elsewhere. Unwrapping returns the original. This wrapper is what unlocked liquidity in 2021 — but it adds a layer of smart-contract trust and a verification step.
- **The Misprint (Card 17b)**: An accidental misprint of Card 17 exists as a recognized rarity — a quirk of the original deployment that the collector community values precisely because it is an authentic 2017 artifact.
- **Royalties / utility**: No on-chain creator royalty in the original contracts; no utility, governance, or roadmap. Value is provenance- and set-driven.

## History

Curio Cards was conceived by Thomas Hunt (also known as "Mad Bitcoins") and a small group of collaborators in early 2017. The project was inspired by the concept of collectible trading cards and the emerging possibility of creating unique digital assets on Ethereum. Seven artists were recruited to create 30 original card designs, each with its own visual style and theme.

The smart contracts were deployed to the [[ethereum]] mainnet in May 2017. At the time, there was no standard for non-fungible tokens on Ethereum — the ERC-721 standard would not be proposed until late 2017 and finalized in January 2018. Curio Cards used a bespoke contract that managed ownership and transfer of individual card editions.

**Key dates:**
- **May 2017**: Smart contracts deployed and cards made available on Ethereum. CryptoPunks would not launch until June 2017.
- **2017-2020**: Minimal trading activity. The project was largely unknown outside a tiny community of early Ethereum adopters. Most cards could be purchased for fractions of an ETH or were effectively worthless in dollar terms.
- **March-April 2021**: The NFT boom brought renewed attention to historical projects. Collectors and researchers identified Curio Cards as one of the oldest art NFT projects on Ethereum, potentially predating CryptoPunks.
- **May 2021**: A community-led "wrapper" contract was deployed, allowing Curio Cards to be wrapped into ERC-1155 tokens compatible with modern marketplaces like OpenSea. This dramatically increased accessibility and liquidity.
- **Summer 2021**: Floor prices peaked at approximately 5-13 ETH per card depending on rarity and artist. The "historical NFT" narrative drove significant collector interest.
- **2022-2023**: Prices declined alongside the broader NFT market but the project retained a dedicated collector base.

## Collection Details

- **Blockchain**: [[ethereum]]
- **Token standard**: Custom pre-ERC-721 contract (wrappable to ERC-1155)
- **Total designs**: 30 unique card designs
- **Artists**: 7 artists contributed designs
- **Edition sizes**: Vary by card, typically ~2,000 editions per design (some cards have fewer)
- **Total supply**: Approximately 30,000-50,000 individual card tokens across all designs
- **Art style**: Diverse — ranges from abstract digital art to pop-culture references, pixel art, and psychedelic imagery

### Notable Cards

| Card # | Artist | Notes |
|--------|--------|-------|
| Card 1 | — | First card in the collection, highest collector demand |
| Card 17 ("Misprint") | — | A card with a known error, valued for its rarity and uniqueness |
| Card 29 | — | Considered one of the rarest due to lower edition count |

The collection's appeal lies less in individual card aesthetics and more in its historical significance as one of the first art NFT deployments on any major smart contract blockchain.

### Collection Economics

- **30 designs, editioned**: ~2,000 editions for common designs and far fewer for rarities; total supply on the order of tens of thousands of individual tokens. Scarcity is at the *design/edition* level, not 1-of-1.
- **Set-completion demand**: A meaningful share of collector activity is driven by the goal of assembling a complete 30-card set, which supports a persistent bid for even common cards and a premium for the hard-to-find ones (Card 1, Card 17b "Misprint", low-edition cards).
- **Royalties**: None enforced by the original 2017 contracts; secondary economics depend on the marketplace of execution and the wrapper layer.

## Comparison vs Peer Early-NFT Collections

| Collection | Chain | Year | Structure | Art storage | Defining trait |
|---|---|---|---|---|---|
| **Curio Cards** | [[ethereum]] | May 2017 | 30 editioned designs | Off-chain (wrapped to ERC-1155) | Earliest art-NFT, set-completion |
| [[cryptopunks\|CryptoPunks]] | Ethereum | Jun 2017 | 10,000 unique | On-chain (later) | Canonical PFP, deep liquidity |
| [[autoglyphs\|Autoglyphs]] | Ethereum | Apr 2019 | 512 unique | Fully on-chain generative | On-chain generative art |
| [[etherrock\|EtherRock]] | Ethereum | Dec 2017 | 100 unique | Off-chain clipart | Ultra-scarce meme/provenance |
| [[rare-pepes\|Rare Pepes]] | [[bitcoin]] (Counterparty) | 2016 | ~1,774 cards | Off-chain | Bitcoin-native "first NFTs" |

Curio Cards' distinguishing trait in this set is the **editioned-card / set-completion** model on an Ethereum contract that predates ERC-721 — a different demand structure from the 1-of-N PFP and 1-of-1 art peers.

## Price History

The figures below are **historical and dated** (2017–2023), not current quotes; no live floor is asserted here.

- **May 2017 (launch)**: Cards were available at negligible cost — fractions of an ETH, when ETH itself was trading around $80-90.
- **2017-2020**: Effectively zero market activity. Individual cards could be found for well under $1 in some cases. No meaningful secondary market existed.
- **March-April 2021**: Rediscovery. As researchers traced the history of Ethereum NFTs, Curio Cards were identified as predating CryptoPunks. Early buyers acquired cards for 0.01-0.1 ETH.
- **May 2021**: The ERC-1155 wrapper launch enabled OpenSea trading. Floors jumped to 0.5-2 ETH almost immediately.
- **July-August 2021**: Peak prices. Floor prices for common cards reached 5-7 ETH (~$15,000-$25,000). Rarer cards and Card 1 traded at 10-13 ETH ($30,000-$45,000).
- **2022**: Floors declined to 1-3 ETH as the NFT market contracted. Historical significance provided a floor but couldn't resist broader market gravity.
- **2023-2026**: Trading continues at reduced volumes. Floors have settled in the sub-1 ETH range for common cards, with historically significant cards (Card 1, low-edition cards) commanding premiums.

## Cultural Significance

**Pre-CryptoPunks provenance**: Curio Cards' May 2017 deployment date makes it one of the oldest verifiable art NFT projects on Ethereum. This matters in a market where historical provenance commands significant premiums. Whether Curio Cards or CryptoPunks was "first" depends on exact deployment dates and definitions, but Curio Cards has a legitimate claim to priority.

**Pre-standard innovation**: Like [[cryptopunks|CryptoPunks]], Curio Cards demonstrates that NFT projects existed before the ERC-721 standard that would define the space. The custom contract approach shows the organic evolution of the NFT concept — developers building what they needed before standards existed.

**Rediscovery narrative**: Curio Cards is the archetypal "forgotten NFT" story. A project created in 2017, ignored for four years, then rediscovered and revalued by a new generation of collectors. This pattern — which also played out with [[mooncats|MoonCats]] and [[etherrock|EtherRock]] — became a defining feature of the 2021 NFT market as collectors engaged in "blockchain archaeology."

**Community-led revival**: The wrapper contract that made Curio Cards compatible with modern marketplaces was created by the community, not the original team. This demonstrated how decentralized communities could revive and modernize old projects — a model later applied to other historical NFTs.

## How & Where It Trades

- **Primary venue**: [[opensea|OpenSea]], trading the **wrapped (ERC-1155)** versions. High-value cards (Card 1, Misprint, low-edition designs) also change hands via OTC deals.
- **Wrap/unwrap step**: Original pre-721 cards are not natively marketplace-compatible. Collectors wrap them via the community ERC-1155 wrapper to list, and can unwrap to return the original. This is the single most important operational detail for trading Curio Cards.
- **Liquidity profile**: Low but more consistent than ultra-scarce peers — because there are thousands of editioned tokens, common cards have a thinner-but-continuous market, while rarities behave like illiquid 1-of-1s. Volume is far below major PFP collections.

## Narrative, Category & Catalysts

Curio Cards sit in the **"OG art-NFT / blockchain archaeology"** category alongside [[mooncats|MoonCats]], [[etherrock|EtherRock]], and [[autoglyphs|Autoglyphs]]. The core narrative is **"earliest art NFT on Ethereum, pre-CryptoPunks"** plus set-completion collecting. Historical catalysts: (1) renewed interest in NFT history during cycle upswings, (2) museum/exhibition or media coverage of early NFTs, (3) CryptoPunks/blue-chip strength dragging up adjacent OG provenance assets. In the mid-2026 Extreme-Fear tape, these catalysts are dormant and collector demand is muted.

## Risks

- **Wrapper / smart-contract risk**: Trading requires the community ERC-1155 wrapper. While widely used, it adds smart-contract trust and a counterfeit-wrapper risk — always verify the wrapper address against the official curio.cards site.
- **Authentication risk**: Verify cards originate from the correct original Curio Cards contract addresses; lookalikes and re-deploys exist. Provenance is the entire value, so authentication is non-negotiable.
- **Illiquidity (especially rarities)**: Common cards trade thinly; rarities can go weeks/months between sales with negotiation-driven pricing.
- **Sentiment reflexivity**: Value tracks the NFT/crypto cycle; Extreme-Fear regimes (2026-06-24) thin bids and widen spreads.
- **Thin-market price signal / wash-trading**: Few trades mean a handful of transactions can set a misleading floor; treat last-sale prints skeptically.
- **Pre-721 contract age**: Original 2017 contracts predate modern auditing; they have functioned without incident but carry legacy technical risk.

## Collector / Trading Playbook

- **Decide set vs single**: Set-completers and single-rarity buyers face different liquidity; a complete-set strategy demands patience and OTC for the rare cards.
- **Verify before you buy**: Confirm the original contract and the legitimate wrapper address; this is the most common avoidable error.
- **Bear-tape behavior**: In the current regime, common cards may offer occasional liquidity while rarities require patient OTC bids; avoid chasing thin "last sale" prints.
- **Holder base**: Primarily historical-NFT collectors and OG Ethereum users — a small, knowledgeable community focused on historical significance over flipping, which keeps turnover low.

## Sources

General market knowledge; no specific wiki source ingested yet. Dated figures (May 2017 deployment, May 2021 wrapper launch, 2021 peak prices) reflect widely-reported public events. Macro framing as of 2026-06-24 per cryptodataapi.com / CoinGecko snapshot (Fear & Greed = 22, Established Bear Market).

## Related

- [[nft]] — NFT market overview and history
- [[ethereum]] — Underlying blockchain
- [[cryptopunks]] — The other major early Ethereum NFT project (June 2017)
- [[rare-pepes]] — Earlier NFTs on Bitcoin via Counterparty (2016)
- [[mooncats]] — Another early Ethereum NFT project (August 2017)
- [[nft-trading]] — NFT trading strategies
