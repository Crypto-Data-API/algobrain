---
title: "CryptoKitties"
type: entity
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [nft, crypto, ethereum, gaming, history]
aliases: ["CryptoKitties", "Crypto Kitties"]
entity_type: protocol
founded: 2017
headquarters: ""
website: "https://www.cryptokitties.co"
related: ["[[nft]]", "[[ethereum]]", "[[nft-trading]]", "[[cryptopunks]]", "[[layer-2]]"]
---

CryptoKitties is a blockchain-based virtual pet game on [[ethereum]] that allows players to breed, collect, and trade unique digital cats. Launched on November 28, 2017 by Dapper Labs (then Axiom Zen), it was the first NFT project to achieve genuine viral mainstream attention — so popular that it congested the Ethereum network, spiking gas prices by over 600% and slowing transactions across the entire blockchain. CryptoKitties proved that NFTs could generate real economic activity and mainstream media coverage, but also exposed Ethereum's fundamental scaling limitations, directly motivating the development of [[layer-2]] solutions and alternative blockchains. Dapper Labs, the company behind CryptoKitties, went on to build the Flow blockchain and NBA Top Shot.

## History

CryptoKitties was developed by a team at Axiom Zen, a Vancouver-based venture studio, led by Roham Gharegozlou, Dieter Shirley, and Mack Flavelle. Dieter Shirley, the project's technical lead, also authored the **ERC-721 standard** — the token standard that defines non-fungible tokens on Ethereum — which was directly inspired by his work building CryptoKitties.

**Key dates:**

- **November 28, 2017**: CryptoKitties launches on Ethereum mainnet. The game introduces the concept of "breeding" — combining two cat NFTs to produce a new cat with a mix of "cattributes" (genetic traits). Each cat is unique and represented by an ERC-721 token.
- **December 2-5, 2017**: The game goes viral. Daily active users spike to over 14,000. Ethereum network congestion reaches critical levels — pending transactions exceed 30,000, and gas prices increase over 600%. The CryptoKitties team accounts for approximately 12-15% of all Ethereum network traffic at peak.
- **December 2, 2017**: The Genesis kitty "Dragon" sells for 600 ETH (approximately $170,000 at the time), making international headlines.
- **December 2017**: CryptoKitties generates over $12 million in total transaction volume within its first two weeks. Media coverage spans BBC, CNN, the New York Times, and virtually every major tech outlet.
- **February 2018**: Dapper Labs spins out from Axiom Zen as a standalone company, raising $12 million from investors including a16z crypto, Union Square Ventures, and Naval Ravikant.
- **March 2018**: Dapper Labs raises an additional $15 million. Meanwhile, daily CryptoKitties activity has already declined over 90% from December peaks.
- **September 2018**: The ERC-721 standard is finalized (EIP-721), establishing the technical foundation for all future NFTs on Ethereum. Shirley's work on CryptoKitties directly informed the standard.
- **2019-2020**: CryptoKitties activity continues to decline. Dapper Labs shifts focus to building the Flow blockchain and NBA Top Shot, both of which would benefit from lessons learned from CryptoKitties' Ethereum scaling problems.
- **2020-2021**: NBA Top Shot launches on Flow (October 2020), generating over $230 million in sales by early 2021 — directly descended from CryptoKitties.
- **2021**: CryptoKitties experiences a modest revival during the NFT boom, with some rare cats trading for significant sums, but activity remains a fraction of 2017 levels.

## Collection Mechanics

- **Blockchain**: [[ethereum]] mainnet
- **Token standard**: [[erc-721|ERC-721]] — the standard was authored by CryptoKitties' lead developer Dieter Shirley and finalized (EIP-721) alongside the project; CryptoKitties is effectively the standard's birthplace
- **Total supply**: Over 2 million cats bred — **uncapped supply** (new cats are minted through breeding rather than a fixed mint)
- **Generation 0 cats**: 50,000 "Gen 0" cats released by Dapper Labs over time (one every 15 minutes initially), serving as the base genetic stock
- **Mint price**: Gen 0 cats sold via Dutch auction (high start price declining over time); secondary-market and breeding costs varied
- **IP rights**: Governed by Dapper Labs' "Nifty License," which grants holders limited commercial use up to a revenue cap ([[nft-ip-rights]]) — an early, formalized NFT IP framework

### Breeding Mechanics

CryptoKitties introduced novel "genetic" mechanics:
- Each cat has a 256-bit genome encoding traits (cattributes)
- Breeding two cats produces an offspring with a mix of parental traits plus possible mutations
- Cats have a "cooldown" period between breeding sessions (faster-breeding cats are more valuable)
- Rare trait combinations ("fancy cats," "exclusive cats") emerge from specific breeding combinations
- Some traits are "mewtations" — rare genetic outcomes that can only occur through breeding

CryptoKitties pioneered NFT [[nft-rarity-scoring|rarity]] as an emergent, breeding-driven property rather than a fixed minted distribution: scarcity of a given cattribute depends on how often it surfaces in the gene pool. Generation number (lower Gen = more prestigious), cooldown speed, "fancy"/"special"/"exclusive" status, and mewtations are the main value axes — a fundamentally different rarity model from the fixed-trait PFP collections that followed ([[bored-ape-yacht-club|BAYC]], [[azuki|Azuki]]).

### Notable Cats

| Cat | Sale Price | Date | Notes |
|-----|-----------|------|-------|
| Dragon (Genesis) | 600 ETH (~$170K) | Dec 2017 | Most expensive sale at launch |
| Founder Cat #18 | 253 ETH (~$110K) | Sep 2018 | Founder cats had unique traits |
| Genesis Cat | 246.9 ETH (~$117K) | Dec 2017 | The very first CryptoKitty |

## Price History

- **November-December 2017 (launch)**: Gen 0 cats initially sold for 0.01-0.5 ETH via Dutch auction. Prices for rare cats quickly spiked as the game went viral. Top cats sold for 100-600 ETH. Average sale prices reached 0.5-5 ETH.
- **January-March 2018**: Average prices declined sharply as initial hype faded. Common cats dropped to 0.01-0.05 ETH. Rare and Gen 0 cats maintained some value.
- **2018-2020**: The market essentially collapsed. Common cats were effectively worthless (less than gas cost to transfer). Only the rarest cats retained any value, and trading volume was minimal.
- **2021**: The NFT boom brought modest renewed interest. Some rare CryptoKitties traded for 10-50 ETH as collectors sought historical NFTs. However, the massive supply (2M+ cats) and the project's declining cultural relevance limited price recovery.
- **2022-2026**: Activity remains minimal. The CryptoKitties marketplace still functions but trading volume is negligible compared to peak. The project's primary value is historical and educational.

> **Data disclaimer:** All prices above are historical, ETH-denominated figures from 2017-2021, not current quotes. CryptoKitties trade extremely thinly today; any current value should be **verified directly on the CryptoKitties marketplace or an [[nft-aggregators|aggregator]]/[[opensea|OpenSea]]**. Treat the trajectory as qualitative.

## Market Structure

| Venue | Role for CryptoKitties |
|---|---|
| CryptoKitties native marketplace | Primary venue for breeding, siring, and Gen 0 auctions; still operational |
| [[opensea|OpenSea]] | Lists secondary CryptoKitties; thin order book |
| [[nft-aggregators|Aggregators]] | Limited coverage given low volume |

- **Liquidity & volume:** Negligible versus the 2017 peak. The uncapped 2M+ supply means common cats are effectively unsellable — for many, [[ethereum|ETH]] gas to transfer exceeds the cat's value, stranding them permanently.
- **No fixed floor:** Because supply is uncapped and heterogeneous (Gen 0 vs. high-gen, fancy vs. common), there is no single meaningful [[nft-floor-price|floor price]]; value is entirely cat-specific.
- **Layer-2 note:** Dapper Labs migrated breeding/transaction flows toward cheaper infrastructure over time (and built the **Flow** blockchain), but the original ERC-721 cats remain on [[ethereum]] mainnet with its gas costs.

## Valuation Drivers

- **Historical provenance:** The dominant value driver today. Gen 0 cats, Founder cats, the Genesis cat, and cats minted in the first viral days carry a "historical NFT" premium.
- **Generation & rarity:** Low generation number, fast cooldown, fancy/exclusive/special status, and rare mewtations ([[nft-rarity-scoring]]).
- **Standard-defining status:** CryptoKitties' role as the [[erc-721|ERC-721]] birthplace gives the earliest cats museum-piece appeal to collectors of crypto history.

## Cultural Significance

**First viral NFT**: CryptoKitties was the first NFT project to break through to mainstream media and public consciousness. The story — digital cats crashing an entire blockchain network — was irresistible to journalists and introduced millions of people to the concept of NFTs for the first time.

**Ethereum's stress test**: By congesting the Ethereum network to the point of near-unusability, CryptoKitties revealed a fundamental truth about blockchain scaling that shaped years of subsequent development. The experience directly motivated:
- [[layer-2]] scaling solutions (Optimism, Arbitrum, Polygon)
- Alternative blockchains designed for high-throughput applications (Flow, Solana, Avalanche)
- Ethereum's own shift toward a rollup-centric scaling roadmap

**ERC-721 birthplace**: The ERC-721 standard — the technical foundation for virtually all NFTs on Ethereum — was created by CryptoKitties' lead developer. Every CryptoPunk wrapper, every BAYC, every Art Blocks piece that uses ERC-721 is built on a standard that emerged from building CryptoKitties.

**Dapper Labs pipeline**: CryptoKitties incubated Dapper Labs, which went on to build Flow blockchain and NBA Top Shot. NBA Top Shot became one of the most successful NFT products ever, generating over $1 billion in total sales. The direct line from CryptoKitties to Top Shot shows how early experiments can seed major products.

**Game mechanics innovation**: The breeding mechanic — combining two NFTs to produce a new unique NFT — was novel and influenced subsequent NFT gaming projects including Axie Infinity (which became a $4B+ ecosystem in 2021). The concept of on-chain "genetics" with rarity tiers became a template for play-to-earn gaming.

**Cautionary tale**: CryptoKitties also demonstrated the speed at which NFT projects can lose momentum. From global headlines and $170K cat sales to near-zero activity in less than three months, the CryptoKitties trajectory foreshadowed the boom-bust pattern that would repeat across the NFT market in 2021-2022.

## Collector & Trading Risks

- **Illiquidity (extreme):** The CryptoKitties marketplace still operates but daily volume is minimal. Rare cats may take weeks or months to find a buyer; common cats may never sell.
- **Supply overhang:** Over 2 million cats exist and breeding can create more. This **uncapped supply** is fundamentally different from fixed-supply collections like [[cryptopunks|CryptoPunks]] (10,000) or [[etherrock|EtherRock]] (100), making price appreciation for common cats nearly impossible.
- **Gas-cost trap:** On [[ethereum]] mainnet, gas to transfer or breed a cat can exceed a common cat's value, permanently stranding low-value cats in wallets.
- **Historical-premium concentration:** Remaining value is overwhelmingly provenance-driven (Gen 0, Founder, Genesis, first-week cats). This market is thin and dependent on a small pool of crypto-history collectors.
- **Wash-trading / thin-tape distortion:** With near-zero genuine volume, isolated sales and any [[wash-trading]] can grossly misrepresent "market" prices.
- **Holder demographics:** A shrinking niche of nostalgic early adopters, historical-NFT collectors, and a small breeder community — declining audience risk.

### Macro Backdrop (mid-2026, qualitative)

The NFT market is deeply depressed this cycle, with the crypto [[fear-and-greed-index|Fear & Greed Index]] near 23 ("Established Bear Market"). CryptoKitties, already long past its 2017 relevance, sees only historical-collector interest. Qualitative context only — there is no fungible price feed for the collection; verify any live figure on a marketplace.

## Related

- [[nft]] — NFT market overview and history
- [[ethereum]] — Underlying blockchain
- [[cryptopunks]] — Older Ethereum NFT project (June 2017)
- [[layer-2]] — Scaling solutions motivated by CryptoKitties congestion
- [[nft-trading]] — NFT trading strategies
- [[bored-ape-yacht-club]] — Later PFP collection that inherited CryptoKitties' lessons
- [[erc-721]] — The token standard born from CryptoKitties
- [[nft-rarity-scoring]] — Breeding/generation-based rarity
- [[opensea]], [[nft-aggregators]] — Secondary venues
- [[wash-trading]] — Thin-tape distortion risk

## Sources

General market knowledge; no specific wiki source ingested yet.
