---
title: "MoonCats"
type: entity
created: 2026-04-07
updated: 2026-06-23
status: excellent
tags: [nft, crypto, ethereum, digital-art, history]
aliases: ["MoonCat", "MoonCats", "MoonCat Rescue", "MoonCatRescue"]
entity_type: protocol
founded: 2017
headquarters: ""
website: "https://mooncat.community"
related: ["[[nft]]", "[[ethereum]]", "[[nft-trading]]", "[[cryptopunks]]", "[[etherrock]]", "[[curio-cards]]", "[[ponderware]]", "[[nft-archaeology]]", "[[erc-721]]", "[[erc-998]]"]
---

MoonCats (originally MoonCatRescue) is a collection of 25,600 unique procedurally generated pixel cats on the [[ethereum]] blockchain, created in August 2017. The project is one of the earliest NFT experiments on Ethereum, but its most remarkable story is not its creation — it is its abandonment and rediscovery. After launching in 2017, the original creators stopped maintaining the project, and it was largely forgotten for nearly four years. In March 2021, during the NFT boom, the community rediscovered the dormant smart contract, and all remaining unrescued MoonCats were claimed within hours. MoonCats became the defining case study in "NFT archaeology" — the practice of finding and revaluing old, forgotten blockchain contracts.

> **Note on "ticker" / market data:** MoonCats is an **NFT collection, not a fungible ERC-20 token** — there is no ticker, market cap, or per-token price feed. The relevant "price" is the OpenSea/Blur **floor** (and tiered sub-floor markets for Genesis, OG-rescued, and low-ID cats), denominated in ETH. Floor figures cited below are point-in-time and qualitative; verify current floors on-chain / on marketplaces before any decision. No live price block is maintained here.

## History

MoonCats was created by Ponderware, a small development team, as an experiment in on-chain generative art and collectibles. The concept was simple: users could "rescue" (mint) unique procedurally generated pixel cats directly from a smart contract on Ethereum. Each cat was generated algorithmically with different colors, patterns, and poses.

**Key dates:**

- **August 9, 2017**: MoonCatRescue smart contract deployed to Ethereum mainnet. The contract allowed users to search for and "rescue" cats by calling a function on the contract. Each rescue generated a unique cat based on a seed value.
- **August-September 2017**: Approximately 3,000-4,000 MoonCats were rescued by early Ethereum users. The project received modest attention within the small Ethereum community of the time.
- **Late 2017-2020**: The original Ponderware team stopped actively maintaining or promoting the project. No website updates, no community engagement. The smart contract remained on Ethereum — immutable and functional — but effectively abandoned. The ~21,000+ unrescued cats sat in the contract, waiting.
- **March 12, 2021**: An anonymous user or small group rediscovered the MoonCatRescue contract while exploring old Ethereum projects during the NFT boom. Word spread rapidly through crypto Twitter and Discord.
- **March 12-13, 2021**: A rescue frenzy ensued. All remaining ~21,000+ unrescued MoonCats were claimed within hours as users rushed to mint from the rediscovered contract. Gas prices spiked as rescue transactions competed for block space.
- **March 2021**: The community rallied around the rediscovered project. A new wrapper contract (**MoonCatAcclimator**) was created to make MoonCats compatible with modern NFT marketplaces (the original 2017 contract predated standards like ERC-721). This wrapper made MoonCats tradable on OpenSea and other platforms.
- **April-August 2021**: Floor prices peaked at 1-2 ETH (~$3,000-$7,000) as the historical NFT narrative drove demand. Trading volume was substantial for a collection that had been forgotten days earlier.
- **Late 2021**: Ponderware, the original creators, re-engaged with the community. They launched MoonCatRescue "Acclimated" — an official wrapper with additional features — and created supplementary projects and accessories for MoonCat holders.
- **2022-2023**: Prices declined with the broader NFT market. The community remained active but smaller, with many holders being long-term collectors attracted by the historical narrative.
- **2024-2026**: Trading continues at reduced volumes. MoonCats occupy a niche position as a historical NFT collection with a compelling rediscovery story.

## Collection Details

- **Blockchain**: [[ethereum]]
- **Token standard**: Custom pre-ERC-721 contract (wrappable via MoonCatAcclimator to ERC-721)
- **Total supply**: 25,600 unique cats
- **Mint price**: Free (gas only) — both in the original 2017 rescue and the 2021 rediscovery rescue
- **Generation**: Procedurally generated from a seed value — each cat has unique colors, patterns, and poses
- **Creator**: Ponderware

### Cat Characteristics

MoonCats are generated with the following variable traits:
- **Pose**: Standing, sitting, sleeping, or pouncing
- **Color**: Determined by RGB values in the seed — virtually unlimited color combinations
- **Pattern**: Solid, striped, or spotted variations
- **Expression**: Eyes and mouth vary
- **Genesis cats**: The first 256 MoonCats (IDs 0x0000 through 0x00ff) are considered "Genesis" cats and carry a rarity premium

### Rarity Tiers

| Category | Count | Notes |
|----------|-------|-------|
| Genesis cats | 256 | First 256 IDs, separate asset class — see below |
| Named cats | Varies | Owners can name their cats on-chain |
| "OG rescued" 2017 | ~3,000-4,000 | Cats rescued in 2017, before the project was forgotten; trade at ~3x+ floor premium |
| "Early 2018 rescued" | ~2,300 (#3365-#5683) | Cats rescued in 2018; trade at ~2x+ floor premium |
| Ultra-rare mint dates | ~74 (#5684-#5757) | Only 71 cats minted in 2019, 3 in 2020 — extreme scarcity periods |
| "Rediscovered" 2021 | ~21,000+ | Cats rescued during the March 2021 frenzy — the floor population |

Cats rescued in the original 2017 period carry a provenance premium over those rescued during the 2021 rediscovery, as they demonstrate early adoption. This premium is verifiable on-chain via transaction timestamps and rescue-order numbers.

### Genesis MoonCats

The 256 Genesis cats (IDs 0x0000-0x00ff) are a separate asset class from the main 25,344 "rescued" cats, with distinct economics that matter for traders:

- **Origin mechanics**: Genesis cats could not be rescued like the standard collection — they were sold directly in rounds. Initial adoption price was 0.3 ETH each, with each subsequent round costing an additional 0.3 ETH. All Ether collected was burned, removing it from circulation — a deflationary sink unusual among NFT launch mechanisms.
- **Trait restrictions**: Genesis cats use a restricted visual palette (various shades of grey only). Black Genesis cats appear only in Standing and Pouncing poses; White Genesis cats appear only as Sleeping and Stalking — making pose/color combinations within Genesis a secondary rarity axis.
- **Pricing**: As of 2026, Genesis cats trade at ~100 ETH floor with high-end listings exceeding 420 ETH, representing a ~1,000x premium over the general MoonCats floor of ~0.1 ETH. The Genesis market is effectively a different collection in trading terms.

### Rescue-order premium and MoonCat #0

Beyond Genesis, rescue-order itself is a primary pricing axis:

- **MoonCat #0** — the very first minted MoonCat — is widely considered the most valuable non-Genesis cat
- **Sub-#100 cats** regularly sell for more than 100x floor
- **#0-#3364** (2017 rescues) command ~3x+ floor as the "OG" cohort
- **#3365-#5683** (2018 rescues) command ~2x+ floor
- **#5684-#5754** (2019, 71 total) and **#5755-#5757** (2020, 3 total) occupy a niche scarcity tier traded among historical collectors

This temporal-scarcity structure differs fundamentally from [[cryptopunks|CryptoPunks]], where rarity depends primarily on trait composition. In MoonCats, when you rescued the cat matters as much or more than what the cat looks like.

### Character cats

A separate collector segment targets MoonCats that visually resemble pop-culture characters. The most popular are **"Garfields"** — orange tabby patterns — which consistently sell above floor. Other character-cat premiums appear when specific color/pattern combinations match recognizable cartoon or meme references. This is a subjective aesthetic layer that sits on top of the rarity and rescue-order axes.

## Technical Infrastructure

MoonCats predate the [[erc-721]] standard, which creates trading friction that every holder eventually encounters. The original MoonCatRescue contract uses a custom pre-standard interface that is not directly compatible with [[opensea|OpenSea]], [[blur|Blur]], or any modern NFT marketplace. To trade a MoonCat on current infrastructure, the cat must first be "acclimated" — wrapped — via a second contract.

### The MoonCatAcclimator wrapper

- **Contract address**: `0xc3f733ca98E0daD0386979Eb96fb1722A1A05E69`
- **Standard**: ERC-721 compatible, implementing the [[erc-998]] Composable Non-Fungible Token Standard
- **Deployed**: March 2021, shortly after the community rediscovery
- **Function**: The user transfers their original MoonCat into the Acclimator contract, which mints a wrapped ERC-721 representation that can be listed on standard marketplaces. The wrapped version is reversible — holders can unwrap at any time to return the cat to the original contract.

Because the Acclimator implements ERC-998, wrapped MoonCats can themselves own other NFTs and ERC-20 tokens, creating hierarchical ownership structures. In practice, this composability is used for MoonCat Accessories (see [[ponderware|Ponderware]] projects) and is more often a narrative than a live trading mechanic.

### Original MoonCatRescue contract

- **Contract address**: `0x60cd862c9c687a9de49aecdc3a99b74a4fc54ab6`
- **Standard**: Pre-[[erc-721]] custom interface
- **State**: Immutable and still functional — the original rescue logic can technically still be called, though the full supply is now claimed

### Trading implications

- **Wrapper adds gas cost and a trust dependency**: Each acclimation requires an Ethereum transaction; holders must trust the Acclimator contract to honour unwrap requests
- **Two-layer ownership verification**: When evaluating a MoonCat listing, traders should verify both the Acclimator token ID and the underlying original MoonCat ID; the mapping is one-to-one but requires explicit checking
- **Marketplace filtering**: Only acclimated MoonCats appear on [[opensea|OpenSea]] and [[blur|Blur]] listings. Unwrapped cats sitting in the original contract are effectively invisible to floor-price scans and may represent hidden supply
- **ERC-998 underutilisation**: Despite the technical capability, most wrapped MoonCats do not own any sub-assets, so the composability feature is latent rather than a live valuation driver

## Price History

- **August 2017 (launch)**: Free to rescue (gas only). Gas costs at the time were negligible — fractions of a cent.
- **2017-2020**: No meaningful secondary market. The project was abandoned and forgotten. Any trading was among a handful of early adopters at negligible prices.
- **March 12-13, 2021 (rediscovery)**: Free to rescue (gas only, though gas prices had risen significantly since 2017). Within hours of rediscovery, secondary market prices appeared on improvised trading channels.
- **March-April 2021**: Once the wrapper contract enabled OpenSea trading, floor prices quickly established at 0.1-0.5 ETH.
- **May-August 2021**: Peak prices. Floor reached 1-2 ETH (~$3,000-$7,000). Genesis cats traded for 5-10+ ETH. Total collection market cap briefly exceeded $50 million.
- **2022**: Floors declined to 0.2-0.5 ETH as the NFT market contracted.
- **2023-2026**: Floors have settled below 0.1 ETH for common cats. Genesis cats retain a ~100 ETH floor with listings exceeding 420 ETH — a ~1,000x separation from the general floor. OG-rescued and early-rescue-order cats retain 2-100x premiums over floor depending on rescue number. Trading volume is low but consistent; the market has become dominated by long-term historical collectors rather than speculators.

## Cultural Significance

**NFT archaeology pioneer**: MoonCats is the defining example of "NFT archaeology" — the practice of discovering forgotten smart contracts on Ethereum and revaluing them based on historical significance. The MoonCats rediscovery in March 2021 inspired a wave of blockchain archaeology that unearthed [[etherrock|EtherRock]], [[curio-cards|Curio Cards]], and numerous other forgotten projects. The concept that old, abandoned contracts could become valuable purely because of their age and on-chain provenance was a novel insight that shaped the 2021 NFT market.

**Immutability demonstrated**: MoonCats perfectly illustrates blockchain immutability. The smart contract sat on Ethereum for nearly four years, untouched and unmaintained, yet remained fully functional. When users returned in 2021, they could interact with the contract exactly as they could in 2017. No server was needed, no company had to stay in business, no database had to be maintained. The cats were just... there, on-chain, waiting.

**Community-driven revival**: The MoonCats revival was entirely community-driven. The original creators had walked away. Community members wrote the wrapper contract, built the new website, organized the Discord, and created the social infrastructure around the rediscovered project. This demonstrated that NFT communities could form and thrive without any central team — a powerful example of decentralized coordination.

**Abandonment as provenance**: Paradoxically, the fact that MoonCats was abandoned enhanced its perceived authenticity. In a 2021 market flooded with cynical cash-grab NFT projects, MoonCats' backstory — created as a genuine experiment, abandoned, then organically rediscovered — felt more authentic than projects launched specifically to capitalize on NFT hype. The abandonment became part of the provenance.

## Current Development (2024-2026)

Unlike most rediscovered 2017 NFT projects that remain community-run, [[ponderware|Ponderware]] — the original creators — re-engaged with MoonCats in late 2021 and have remained active through 2026. Their roadmap is published at ponderware.com/projects and mooncatrescue.com/roadmap and directly affects MoonCats valuations, since utility catalysts can meaningfully shift the holder base and demand curve.

Active and planned projects:

- **MoonCatAcclimator (2021, live)** — the wrapping contract that made modern trading possible (see Technical Infrastructure above)
- **MoonCat Accessories (live)** — community-created NFTs that accessorise individual MoonCats using the ERC-998 composability layer
- **CondoMini (live)** — a 5-in-1 customisable NFT that enables owners to create neighbourhoods within a broader "MiniVille" ecosystem; functions as a companion product to MoonCats
- **Idle game (planned / in development)** — an idle-genre game where MoonCats owners enter their cats into competitive gameplay with limited direct control. As of 2026 this is a roadmap item rather than live software; its eventual release is a known catalyst traders track

Trading-relevant observations:

- Ponderware announcements typically cause short-term floor movement on the base MoonCats collection, particularly for cats that would qualify as game entrants or accessory targets
- The planned idle game positions MoonCats within the broader 2024-2026 industry shift toward utility-based NFTs, potentially giving the collection a second-act narrative beyond pure archaeology provenance
- Companion projects (CondoMini, Accessories) create optional secondary exposure for MoonCats holders but are separately tradeable markets; holders evaluating the ecosystem should track each independently

## Comparison vs other historical / pixel-art NFT collections

MoonCats sits in the "early-Ethereum historical collectible" niche. Its closest comparables differ on supply, rarity logic, and how heavily provenance (rather than aesthetics) drives price:

| Collection | Launched | Supply | Primary rarity axis | Liquidity / depth | Distinguishing factor |
|---|---|---|---|---|---|
| **MoonCats** | Aug 2017 | 25,600 | Rescue-order + Genesis tier | Thin; collector-held | "NFT archaeology" rediscovery story; temporal-scarcity pricing |
| **[[cryptopunks\|CryptoPunks]]** | Jun 2017 | 10,000 | Trait composition (attributes) | Deepest of the cohort (blue-chip) | The reference early-Ethereum NFT; trait-driven, not order-driven |
| **[[etherrock\|EtherRock]]** | Dec 2017 | 100 | Pure scarcity (ID only) | Extremely thin, very high floor | Ultra-low-supply meme-status collectible |
| **[[curio-cards\|Curio Cards]]** | May 2017 | 30 designs (multi-edition) | Edition / card rarity | Thin, museum-grade collector base | Predates ERC-721; "first NFT art series" claim |
| **Chromie Squiggle (Art Blocks)** | 2020 | ~10,000 | Generative trait / color | Moderate | Generative-art-platform flagship, not an archaeology play |

The key trading distinction: in **CryptoPunks** rarity is *what the asset looks like*; in **MoonCats** rarity is heavily *when it was rescued* (2017 OG > 2018 > the 2021 rediscovery floor) plus the separate Genesis tier. That makes MoonCats a multi-market collection where the headline floor understates the value distribution.

## Narrative, category & catalysts

- **Category:** historical / "NFT archaeology" blue-chip-adjacent collectible — a provenance trade, not a utility or yield trade.
- **Demand drivers:** nostalgia and on-chain provenance, [[ponderware|Ponderware]] roadmap catalysts (Accessories, CondoMini, the planned idle game), and broad NFT-cycle risk appetite.
- **Catalysts to watch:** any Ponderware utility release (idle game launch in particular), renewed interest in 2017-era NFTs during NFT-cycle upturns, and notable Genesis/low-ID sales that reset reference prices.
- **Regime context (2026-06-23):** the crypto tape is in **Extreme Fear** (Fear & Greed 21; market-health 29/100, bearish), with the long-horizon regime read as **Bottoming / Accumulation** ([[bitcoin|BTC]] ~$64,568, [[ethereum|ETH]] ~$1,737). The **NFT/collectibles basket is highly sentiment-driven and has been weak in this tape** — thin historical collections see widened bid-ask, vanishing floor liquidity, and outsized sensitivity to a handful of sellers. (Macro snapshot 2026-06-22 20:03 UTC, regime context only.)

## Trading Considerations

**Liquidity**: Low. MoonCats trade on OpenSea and Blur via the wrapper contract, but daily volume is minimal. The 25,600 supply is large relative to demand, which limits price appreciation.

**Wrapper requirement**: Original MoonCats must be "acclimated" (wrapped) via the MoonCatAcclimator contract to be traded on standard NFT marketplaces. This adds a gas cost and a trust dependency on the wrapper contract.

**OG vs. rediscovery provenance**: Cats rescued in 2017 (before abandonment) are verifiably distinguishable from those rescued in March 2021. The 2017 cats carry a premium among collectors who value original-era provenance. On-chain transaction timestamps make this verification straightforward.

**Genesis premium**: The first 256 MoonCats (Genesis cats) trade at significant premiums over the general population. Collectors seeking the "best" MoonCats focus on Genesis IDs.

**Holder demographics**: Primarily historical NFT collectors and participants in the March 2021 rediscovery event. The community has a nostalgic, collector-oriented culture rather than a speculative trading culture.

**Key risk**: The large supply (25,600) in a thin market means price is highly sensitive to sell pressure. Even a small number of holders liquidating can push floors down significantly. The project's cultural significance may not be sufficient to sustain long-term value in a market with many competing historical NFT narratives.

### Structured risks

- **Sentiment reflexivity** — as a pure provenance/collectible play with no cash flow, value is reflexive on NFT-cycle sentiment; it rises in NFT bull phases and bleeds in risk-off tape like the current Extreme Fear regime.
- **Thin-liquidity / sell-pressure sensitivity** — 25,600 supply against minimal daily volume means a few liquidating holders can reset the floor; exits during weak tape are costly.
- **NFT-cycle dependence** — there is no utility floor; demand depends almost entirely on the health of the broader NFT/collectibles market, which is weak in this regime.
- **Tiered-market fragmentation** — the headline floor, Genesis (~100 ETH+), OG-rescued, and low-ID markets are effectively separate, thin order books; "floor" can be misleading when evaluating a specific cat.
- **Wrapper / contract dependency** — trading requires the MoonCatAcclimator wrapper; gas cost plus a trust dependency on the wrapper contract, and unwrapped cats are invisible to floor scans (latent supply).
- **Narrative competition** — many rediscovered 2017 projects compete for the same archaeology-collector capital, capping durable demand.

### Trading playbook (current bear tape)

- **Provenance trade, not a momentum trade.** Edge here is buying historically significant, verifiable cohorts (low-ID, 2017 OG, Genesis) at distressed floors *during* fear, not chasing floor pumps in euphoria.
- **Buy the tier, not the floor.** The asymmetric value is in sub-#100 / Genesis / OG cats whose premiums compress in bear tape; the generic ~floor population offers little upside and poor liquidity.
- **Size for illiquidity.** Assume you cannot exit quickly without slippage; position only what you can hold through a full NFT-cycle drawdown.
- **Track Ponderware catalysts.** Utility releases (especially the idle game) are the main idiosyncratic upside; floors typically twitch on announcements — but in Extreme Fear, fade fast moves rather than chase them.
- **Verify before buying.** Confirm Acclimator ID ↔ underlying MoonCat ID, rescue-order/year, and Genesis status on-chain — mispriced listings appear because tier structure is opaque.

## Sources

- Existing ingested sources on MoonCats history (see `wiki/log.md` entries from 2026-04-07)
- Gap-finder deep research 2026-04-22 (Source: [[2026-04-22-gap-finder-the-provided-wiki-pages]]) — Genesis cats pricing and burn mechanics, rescue-order premiums, character-cat segment, MoonCatAcclimator contract address, Ponderware roadmap including CondoMini, Accessories, and planned idle game

## Related

- [[nft]] — NFT market overview and history
- [[ethereum]] — Underlying blockchain
- [[cryptopunks]] — The most iconic early Ethereum NFT (June 2017)
- [[curio-cards]] — Another early Ethereum NFT project (May 2017)
- [[etherrock]] — Another rediscovered early Ethereum NFT (December 2017)
- [[nft-trading]] — NFT trading strategies
- [[nft-archaeology]] — the trading concept pioneered by the March 2021 MoonCats rediscovery
- [[ponderware]] — the creator team's ongoing development
- [[erc-721]] — the NFT standard MoonCats predate and wrap into
- [[erc-998]] — the composable NFT standard the MoonCatAcclimator implements
