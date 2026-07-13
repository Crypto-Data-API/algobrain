---
title: "Casey Rodarmor"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [person, crypto, bitcoin, nft, history]
aliases: ["Casey Rodarmor", "@rodarmor"]
entity_type: person
website: "https://rodarmor.com"
related: ["[[ordinals]]", "[[runes]]", "[[bitcoin]]", "[[nft]]", "[[ethereum]]", "[[nft-trading]]", "[[cryptopunks]]"]
---

# Casey Rodarmor

Casey Rodarmor is a software developer who created the [[ordinals|Bitcoin Ordinals]] protocol (launched January 2023) and the [[runes|Runes]] fungible-token protocol (launched at the April 2024 halving). Ordinals enable NFT-like inscriptions directly on the [[bitcoin|Bitcoin]] blockchain without requiring a sidechain or separate token standard, representing a fundamental shift in how Bitcoin's block space can be used. The protocols sparked intense debate within the Bitcoin community about the network's purpose, caused significant network congestion and fee spikes, and created entirely new fee-revenue and trading markets on Bitcoin's base layer.

## Background

Before creating Ordinals, Rodarmor worked as a contributor to [[bitcoin|Bitcoin Core]], the reference implementation of the Bitcoin protocol. This background gave him deep familiarity with Bitcoin's technical architecture, particularly the Taproot upgrade (activated November 2021) that made Ordinals technically feasible. His proximity to Bitcoin's core development community lent credibility to the project while also making the resulting controversy more pointed.

## The Ordinals Protocol

### How It Works

The Ordinals protocol assigns a unique serial number to each individual satoshi (the smallest unit of Bitcoin, 1/100,000,000 of a BTC). By tracking these serialized satoshis, the protocol enables users to "inscribe" arbitrary data -- images, text, audio, video, even entire applications -- directly into Bitcoin transactions. The inscribed data is stored on-chain in the witness data section of Bitcoin transactions.

Key technical details:

- **No sidechain required**: Unlike previous Bitcoin NFT attempts (e.g., Counterparty, Stacks), Ordinals operate natively on Bitcoin's base layer
- **Taproot dependency**: The protocol leverages the Taproot upgrade's expanded witness data capacity to store inscription content
- **Immutability**: Inscriptions are permanent and cannot be altered or deleted once written to the blockchain
- **No smart contracts**: Ordinals do not use smart contracts in the [[ethereum]] sense -- they rely purely on Bitcoin's existing transaction structure

### Launch and Adoption

Rodarmor launched the Ordinals protocol in January 2023. Adoption was rapid:

- Within weeks, thousands of inscriptions were created, ranging from pixel art to full images to text documents
- The BRC-20 token standard (inspired by [[ethereum|Ethereum's]] ERC-20) emerged as a derivative innovation, enabling fungible tokens on Bitcoin via Ordinals
- By mid-2023, millions of inscriptions had been created, with some trading for significant sums on dedicated marketplaces

## Impact on Bitcoin

### Network Congestion and Fees

Ordinals caused substantial network effects on Bitcoin:

- **Block space demand**: Inscription data consumed significant block space, competing with regular financial transactions
- **Fee spikes**: Transaction fees rose dramatically during periods of high inscription activity, pricing out smaller users
- **Mempool congestion**: The Bitcoin mempool (queue of unconfirmed transactions) grew to unprecedented sizes

### The Purpose Debate

Ordinals reignited a fundamental debate within the Bitcoin community:

- **Pro-Ordinals camp**: Argued that Bitcoin's block space is a free market and any valid transaction should be permitted. Ordinals bring new users, new use cases, and increased miner revenue, strengthening Bitcoin's long-term security budget
- **Anti-Ordinals camp**: Argued that Bitcoin's block space should be reserved for financial transactions. Inscriptions are "spam" that degrades the network's primary function as a monetary system. Some Bitcoin developers proposed filtering inscription transactions
- **Miner incentives**: Miners generally welcomed Ordinals because inscription activity significantly increased fee revenue, providing an important supplement to the declining block subsidy

### Comparison to Ethereum NFTs

Ordinals differ from [[ethereum]]-based [[nft|NFTs]] in several important ways:

- **On-chain storage**: Ordinals store data directly on Bitcoin's blockchain, while most Ethereum NFTs store only a pointer to off-chain data (IPFS or centralized servers)
- **No royalties**: Ordinals have no built-in royalty mechanism, unlike ERC-721 and ERC-2981 standards on Ethereum
- **No smart contract programmability**: Ordinals cannot implement complex logic like Ethereum NFTs can
- **Cultural context**: Bitcoin Ordinals emerged in a community historically skeptical of NFTs, creating unique cultural dynamics

## The Runes Protocol (2024)

In September 2023 Rodarmor published the "Runes" blog post proposing a deliberately simple fungible-token protocol for Bitcoin — partly to displace the inefficient BRC-20 standard that had emerged on top of his Ordinals work. Key design choices: balances live in UTXOs (fitting Bitcoin's native model), transfers and etchings are encoded in a single OP_RETURN output, no off-chain data is required, and there is no native token.

**Runes launched at block 840,000 — the fourth Bitcoin halving, April 20, 2024.** The launch drove a frenzy of "etchings" and mints that pushed Bitcoin transaction fees to record levels on halving day, briefly making fees a dominant share of miner revenue at the exact moment the block subsidy halved to 3.125 BTC. Runes trading volume initially dwarfed BRC-20 and Ordinals activity on marketplaces such as [[magic-eden|Magic Eden]] and OKX.

## Status 2025-2026

- Ordinals/Runes activity has been highly cyclical since the 2024 peak: inscription counts passed the tens of millions in 2024, but fee share and marketplace volumes fell sharply through 2025 as speculative interest rotated elsewhere.
- The "spam filter" debate continued into 2025-2026 among Bitcoin Core / Knots node operators over relaying inscription transactions — keeping Rodarmor's protocols at the center of Bitcoin's block-space politics.
- Rodarmor stepped back from day-to-day maintenance of the `ord` reference client (handing the lead maintainer role to "raphjaph" in early 2023) but remains publicly active in Bitcoin protocol experimentation and open-source work (e.g., newer projects discussed on his blog and podcasts), with no major role change reported in 2025-2026 (Perplexity check, 2026-06-10).

## Trading Relevance

For traders, Rodarmor's protocols created measurable, tradeable market structure on Bitcoin: (1) **fee-market signals** — inscription/Runes waves drive mempool congestion and fee spikes that matter for timing on-chain settlement and for miner-revenue analysis; (2) **new asset classes** — inscriptions (e.g., NodeMonkes, Bitcoin Puppets) and Runes tokens trade on Magic Eden, OKX, and Binance-listed wrappers, with deeply cyclical liquidity; (3) **miner economics** — fee revenue from his protocols is a recurring variable in post-halving miner-profitability models and thus in hashrate and [[bitcoin]] cycle analysis.

## Legacy

Rodarmor's creation of Ordinals represents one of the most significant developments in Bitcoin's history since the Taproot upgrade itself. Whether viewed as innovation or distraction, Ordinals permanently expanded the conception of what Bitcoin can be used for and created an entirely new ecosystem of Bitcoin-native digital artifacts. The protocol demonstrated that even a "finished" protocol like Bitcoin can be reimagined through creative technical work.

## Related

- [[ordinals]]
- [[runes]]
- [[bitcoin]]
- [[nft]]
- [[nft-trading]]
- [[ethereum]]
- [[cryptopunks]]
- [[opensea]]
- [[magic-eden]]

## Sources

- Casey Rodarmor, "Runes" (blog post, September 25, 2023): https://rodarmor.com/blog/runes/
- Runes protocol documentation announcement (March 2024): https://x.com/rodarmor/status/1773152223406547415
- Protos, "Ordinals founder Casey Rodarmor to launch Runes at Bitcoin halving" (2024): https://protos.com/ordinals-founder-casey-rodarmor-to-launch-runes-at-bitcoin-halving/
- CoinDesk/Yahoo Finance, "Runes, Casey Rodarmor's Protocol for 'Sh!tcoins' on Bitcoin, Set to Go Live at Halving" (April 2024): https://finance.yahoo.com/news/runes-casey-rodarmors-protocol-sh-060000422.html
- Ordinals handbook and `ord` repository: https://github.com/ordinals/ord
- Perplexity verification of current status, 2026-06-10.
