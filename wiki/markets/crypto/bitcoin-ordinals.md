---
title: "Bitcoin Ordinals"
type: market
created: 2026-04-22
updated: 2026-06-21
status: excellent
tags: [crypto, bitcoin, nft, digital-assets]
aliases: ["Ordinals", "Bitcoin NFTs", "Inscriptions"]
related: ["[[bitcoin]]", "[[nft]]", "[[nft-trading]]", "[[brc-20]]", "[[ordi]]", "[[magic-eden]]", "[[gamma-nft]]", "[[ethereum]]"]
---

Bitcoin Ordinals are a protocol created by developer **Casey Rodarmor** (with ongoing maintenance by Raph Japh) that launched on Bitcoin mainnet in January 2023, enabling NFT-like inscriptions directly on the Bitcoin blockchain. Unlike [[ethereum|Ethereum]] NFTs that reference external metadata via token IDs, Ordinals embed arbitrary data — images, text, video, audio — into the witness data of individual satoshis, making them Bitcoin-native digital artifacts rather than pointers. The protocol introduced a numbering scheme ("ordinal theory") that gives each satoshi a unique identity, and has generated a distinct NFT asset class with its own marketplaces, collector community, and trading dynamics.

## How Ordinals Work

### Ordinal Theory
The core innovation is a consensus-free numbering system for satoshis. Each of the ~2.1 quadrillion satoshis ever to exist can be ordered by the block they were mined in and their position within that block. The ordinal rarity hierarchy (per the official Ordinals handbook) is:

- **Common**: Any sat that isn't the first sat of its block.
- **Uncommon**: The first sat of each block.
- **Rare**: The first sat of each difficulty adjustment period.
- **Epic**: The first sat of each halving epoch.
- **Legendary**: The first sat of each cycle (every 6 halvings).
- **Mythic**: The first sat of the genesis block (a single sat).

### Inscriptions
Data is embedded in a segregated witness (**SegWit**) transaction's witness field, taking advantage of the 2017 SegWit upgrade and the 2021 **Taproot** upgrade which increased the amount of data that can be cheaply placed in witness data. An inscription is permanently attached to a specific satoshi and transfers with that satoshi.

### No Token Standard Required
Ordinals require no changes to Bitcoin consensus — they exploit existing transaction fields. This is both a feature (permissionless, no forks) and a point of controversy (Bitcoin maximalists view them as "spam" bloating the blockchain).

## The BRC-20 Wrinkle

In March 2023, a pseudonymous developer called **domo** launched the **[[brc-20]]** token standard, which uses Ordinals inscriptions to create fungible tokens on Bitcoin. BRC-20 tokens work by inscribing JSON text with deploy/mint/transfer operations — entirely off-protocol indexing conventions, not a formal Bitcoin standard.

**[[ordi|ORDI]]** (March 8, 2023) was the first BRC-20 token, distributed through a "fair mint" where anyone could inscribe a transfer for the cost of a transaction. BRC-20 briefly dominated Bitcoin transaction activity in May 2023, pushing transaction fees above **$30** and generating weeks of mempool congestion.

### How a BRC-20 Transfer Works (qualitative)

Because there is no on-chain BRC-20 contract, the "token" is purely a social/indexer convention layered on inscriptions:

1. **Deploy** — someone inscribes a JSON object declaring a ticker, total supply, and per-mint limit.
2. **Mint** — users inscribe `mint` operations until the supply cap is reached; indexers credit balances on a first-come basis (a "fair mint").
3. **Transfer** — moving tokens is a *two-step* process: inscribe a `transfer` inscription, then send that inscription to the recipient. Indexers (Unisat, OKX, etc.) read the ordered inscriptions and agree on balances off-chain.

This indexer-dependent design is BRC-20's core fragility: there is no consensus enforcement, so the "ledger" is whatever the dominant indexers agree it is. Newer standards address this:

| Standard | Year | Fungibility model | Key trait |
|----------|------|-------------------|-----------|
| **[[brc-20\|BRC-20]]** | 2023 | Inscription + off-chain indexer | First mover; indexer-dependent, inefficient |
| **Runes** | 2024 | UTXO-based, protocol-native | Casey Rodarmor's design; far more block-space efficient |
| **SRC-20 / Stamps** | 2023 | Data in transaction outputs | Stores data more permanently (cannot be pruned) |
| **Rune-style fungibles** | 2024+ | OP_RETURN + UTXO | Designed to replace BRC-20 spam load |

## Market Timeline

| Date | Event |
|------|-------|
| 2023-01-20 | Ordinals mainnet launch by Casey Rodarmor |
| 2023-02 | Inscription count crosses 100,000 |
| 2023-03-08 | First BRC-20 token (ORDI) launched |
| 2023-05 | BRC-20 mania pushes BTC fees above $30; daily inscription count peaks near 500,000 |
| 2023-12 | 60+ million total inscriptions |
| 2023-Q4 | Bitcoin Ordinals trading volume briefly rivals Ethereum NFT volume |
| 2024-2025 | Market matures; major collections (NodeMonkes, Bitcoin Puppets, Runestone) established |
| 2024 | **Runes** protocol launched by Rodarmor (alternative fungible token standard, more efficient than BRC-20) |

## Notable Collections

- **NodeMonkes** — 10,000 pixel monkeys; considered the "CryptoPunks of Bitcoin"
- **Bitcoin Puppets** — community-driven meme collection that gained significant cultural traction
- **Runestone** — free claim airdrop tied to the Runes protocol launch
- **Taproot Wizards** — hand-drawn wizard art inscriptions; early Ordinals culture piece
- **Bitcoin Frogs** — one of the earliest viral Bitcoin PFP collections

## Key Marketplaces

| Marketplace | Notes |
|-------------|-------|
| **[[magic-eden|Magic Eden]]** | Largest Ordinals marketplace after expanding from Solana |
| **[[gamma-nft\|Gamma]]** | Ordinals-native platform for minting and trading inscriptions |
| **OKX NFT** | Major Asian marketplace with strong Ordinals liquidity |
| **Unisat** | Browser wallet + marketplace, popular for BRC-20 trading |

## Trading Characteristics

**Higher transaction friction:** Bitcoin's 10-minute block time and higher fees (compared to Solana or even Ethereum rollups) make Ordinals less suited to high-frequency trading. Trades settle slower, increasing execution risk on volatile collections.

**Custody complexity:** Ordinals require Taproot-compatible wallets that preserve satoshi-level UTXOs. Sending Ordinals-bearing sats from a regular Bitcoin wallet can inadvertently spend them as fees. This has caused numerous high-value losses.

**Correlation with BTC:** Ordinals floor prices correlate more strongly with BTC price than Ethereum NFTs did with ETH. A BTC rally drives capital into Ordinals; a BTC correction drains it out sharply.

**Rare sats market:** Independent of inscriptions, there is a secondary market for rare satoshis themselves (uncommon, rare, epic, legendary, mythic) sorted by ordinal theory properties. These trade at premiums to face value on venues like **Magisat** and **Ordinalsbot**.

### Ordinals vs. Ethereum NFTs

| Dimension | Bitcoin Ordinals | [[ethereum\|Ethereum]] NFTs |
|-----------|------------------|------------------------------|
| Data location | Inscribed *on-chain* in witness data (the artifact lives on Bitcoin) | Usually a token pointing to off-chain metadata (IPFS/HTTP) |
| Standard | Indexer convention (no consensus standard) | Formal token standards (ERC-721, ERC-1155) |
| Programmability | Minimal — Bitcoin has no rich smart contracts | Full smart-contract logic (royalties, mechanics) |
| Settlement | ~10-min blocks, higher fees | Faster on [[layer-2\|L2s]], cheaper |
| Permanence | Fully self-contained, immutable | Depends on metadata host staying online |
| Royalties | Hard to enforce on-chain | Enforceable (though market-optional in practice) |

The "data fully on-chain" property is Ordinals' main differentiator and a key part of the collector thesis: an inscription cannot break by losing its metadata host, unlike many early Ethereum NFTs. The trade-off is the lack of programmability and the controversy over block-space consumption.

## Controversy

Bitcoin Ordinals remain contentious within the Bitcoin community:

- **Critics** (including developer Luke Dashjr) argue inscriptions are spam that bloat the blockchain, raise fees for monetary users, and deviate from Bitcoin's "sound money" mission. Dashjr has published patches to filter inscriptions as non-standard transactions.
- **Supporters** argue the protocol is permissionless, fees paid are fees paid, and miner revenue from inscription demand helps secure the network post-halving as block subsidies decline.

This tension occasionally surfaces as proposals to soft-fork out inscription support, though no such proposal has gained meaningful mining/node support.

## Related

- [[bitcoin]] — Underlying blockchain; Ordinals floor prices track BTC closely
- [[nft]] — Broader NFT market context
- [[brc-20]] — Fungible tokens via inscriptions
- [[ordi]] — First BRC-20 token
- [[magic-eden]] — Leading Ordinals marketplace
- [[gamma-nft]] — Ordinals-native marketplace
- [[nft-trading]] — General NFT trading strategies
- [[ethereum]] — comparison point for the dominant NFT chain

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
- Official Ordinals handbook: https://docs.ordinals.com/ (rare sat categories, ordinal theory)
