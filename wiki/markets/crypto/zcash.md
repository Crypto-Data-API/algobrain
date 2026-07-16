---
title: "Zcash (ZEC)"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: excellent
tags: [crypto, privacy, zcash, zk-snarks]
entity_type: protocol
founded: 2016
website: "https://z.cash"
aliases: ["ZEC", "zcash-protocol"]
related: ["[[2026-06-05-zcash-orchard-counterfeiting-bug]]", "[[ai-vulnerability-discovery]]", "[[bitcoin]]", "[[blockchain]]", "[[crypto-markets]]", "[[dash]]", "[[hyperliquid]]", "[[monero]]", "[[mythos-release-window-exploit-short]]", "[[privacy-coins]]", "[[proof-of-work]]", "[[zero-knowledge-proofs]]"]
headquarters: "Decentralized"
---

# Zcash (ZEC)

**Zcash (ZEC)** is a privacy-focused Layer 1 cryptocurrency launched in 2016 that uses **[[zero-knowledge-proofs|zk-SNARKs]]** (zero-knowledge succinct non-interactive arguments of knowledge) to enable fully shielded transactions where the sender, recipient, and amount are encrypted on the [[blockchain]] while still being verified by the network. Zcash was the first major blockchain to implement zero-knowledge proofs for privacy, and the underlying cryptographic research has since influenced the broader crypto ecosystem, including [[ethereum]] L2 scaling. It is one of the two anchors of the [[privacy-coins]] sector, the other being [[monero|Monero]].

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #15 |
| **Market Cap** | $7.90B |
| **Current Price** | $470.81 |
| **24h Volume** | $394.77M |
| **24h Change** | +4.56% |
| **7d Change** | +13.56% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: despite a market-wide **extreme fear** reading ([[fear-and-greed-index|Fear & Greed]] = 22) and an **Established [[bear-market|Bear Market]]** regime as of 2026-06-20, ZEC is *up* ~4.6% on the day and ~13.6% on the week — and sits at rank #15, having recovered meaningfully from the ~38% single-day crash triggered by the June 5, 2026 Orchard counterfeiting disclosure (see below). This strong relative strength — and the divergence from privacy-peer [[monero|Monero]] (red over the same window) — is consistent with ZEC's tendency to trade on the privacy-coin narrative independently of broad [[crypto-markets]] beta. Price remains ~85.3% below the October 2016 ATH of $3,191.93.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZEC |
| **Market Cap Rank** | #15 (2026-06-20) |
| **Market Cap** | $7.90B (2026-06-20) |
| **Current Price** | $470.81 (2026-06-20) |
| **Genesis Date** | 2016-10-28 |
| **Consensus** | [[proof-of-work|Proof of Work]] (Equihash); PoS "Crosslink" planned |
| **Privacy** | Optional shielded (z-addr) or transparent (t-addr) via Unified Addresses |
| **Hashing Algorithm** | Equihash |
| **Supply** | 21M ZEC hard cap (same as [[bitcoin]]); halving schedule |
| **Categories** | Smart Contract Platform, Privacy Coins, Layer 1 (L1), Near Protocol Ecosystem, Zero Knowledge (ZK), Proof of Work (PoW), Pantera Capital Portfolio, Made in USA, Coinbase 50 Index, Quantum-Resistant, Privacy |
| **Founded By** | Zooko Wilcox and the Electric Coin Company |
| **Website** | [https://z.cash/](https://z.cash/) |

---

## Overview

Zcash is a privacy-focused cryptocurrency that uses trustless zero-knowledge proofs to enable fully encrypted transactions while maintaining blockchain transparency and security. It was the first cryptocurrency to implement zero-knowledge encryption for private peer-to-peer payments, addressing the fundamental privacy gap in traditional cryptocurrencies that expose transaction details publicly.

With a fixed supply of 21 million ZEC and a halving schedule similar to [[bitcoin|Bitcoin]], Zcash allows users to prove transactions are valid without revealing sensitive information like wallet balances, transaction amounts, or participant identities, making it suitable for everyday payments, long-term savings, and cross-border money transfers where financial confidentiality matters.

The protocol operates on its own blockchain currently using [[proof-of-work|Proof-of-Work]] consensus, though it's evolving toward Proof-of-Stake through the planned "Crosslink" upgrade to enhance security, scalability, and energy efficiency. Zcash employs trustless zero-knowledge proofs (Halo) within its Orchard shielded pool to verify transactions without revealing sender, receiver, or amount information.

Users can choose between transparent public transactions and shielded private transactions through Unified Addresses, which work with both types. The network is faster and cheaper than Bitcoin, with new blocks mined every 75 seconds and transaction fees typically just a fraction of a cent. Privacy adoption has surged in 2025, with over 30% of total ZEC supply now held in fully shielded pools.

Zcash was created by a group of scientists in 2013 who initially proposed Zerocoin as a privacy extension to Bitcoin before building a standalone protocol. The ecosystem operates with a self-funded development model where block rewards support independent teams through the Zcash Community Grants Committee and a new Coinholder-Controlled Fund.

---

## Technology & Privacy (zk-SNARKs)

Zcash's defining technology is the use of **[[zero-knowledge-proofs|zk-SNARKs]]** to prove a transaction is valid (inputs equal outputs, no double-spend, signatures correct) **without revealing any of the underlying data**. This is a fundamentally different privacy approach from [[monero|Monero]]'s decoy/ring-signature model.

| Component | Detail |
|---|---|
| **Privacy cryptography** | zk-SNARKs — succinct non-interactive zero-knowledge proofs |
| **Proving system evolution** | Original Sprout (2016) → Sapling (2018, faster/lighter, trusted setup) → **Halo 2 (no trusted setup, used by Orchard)** |
| **Shielded pools** | Sprout (legacy), Sapling, and **Orchard** (current, Halo 2-based, activated May 2022) |
| **Unified Addresses** | A single address format that can receive to transparent or shielded pools, smoothing UX |
| **Consensus** | [[proof-of-work|PoW]] (Equihash); ~75-second block time; **"Crosslink" PoS migration planned** |
| **Supply** | 21M hard cap with Bitcoin-style halvings |

**Transparent vs shielded (the optional-privacy model).** Zcash offers two transaction types:
- **Transparent (t-addresses)** — fully visible on the [[blockchain]], like [[bitcoin]].
- **Shielded (z-addresses)** — encrypted using zk-SNARKs; sender, receiver, and amount are hidden.

In practice, the majority of ZEC transactions historically used **transparent** addresses, which has weakened the effective anonymity set versus [[monero|Monero]]'s **mandatory** privacy — though shielded adoption has grown to >30% of supply by 2025. This *optionality* is the central design contrast between the two privacy leaders.

**Halo / Orchard and the trusted-setup problem.** Early zk-SNARK systems required a **trusted setup ceremony** (the "toxic waste" problem — if the setup secret leaked, undetectable counterfeiting was possible). **Halo 2** eliminated the trusted setup, and the **Orchard** pool is built on it. Ironically, it was a flaw in the Orchard implementation — not the trusted setup — that produced the June 2026 counterfeiting bug (below): a reminder that novel zk cryptography carries deep, hard-to-audit implementation risk.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | ~16,777,490 ZEC |
| **Total Supply** | ~16,777,551 ZEC |
| **Max Supply** | 21,000,000 ZEC |
| **Market Cap / FDV Ratio** | ~0.80 |

- **21M hard cap + halvings.** Unlike [[monero|Monero]]'s uncapped tail emission, Zcash mirrors [[bitcoin|Bitcoin]]'s **fixed 21M supply** with a **halving schedule** that periodically cuts the block reward. ~16.78M of 21M is circulating, so remaining issuance is a known, decreasing drip.
- **Self-funding / dev rewards.** Historically a portion of block rewards funded development (the "Founders' Reward," later the "Dev Fund"); the model has evolved toward the **Zcash Community Grants Committee** and a **Coinholder-Controlled Fund** — a governance contrast with Monero's fair-launch, no-funding model.
- **ZSAs (Zcash Shielded Assets).** A planned upgrade enabling **user-issued assets (tokens) that inherit Orchard's shielded privacy** — extending Zcash from a single private coin toward a private multi-asset platform. ZSAs are a key forward catalyst for the ecosystem narrative.
- **Crosslink (PoS).** The planned migration from PoW (Equihash) toward a hybrid/PoS security model — a roadmap item with both upside (efficiency, security) and migration risk.

---

## Ecosystem & Use Cases

- **Private payments & savings** — confidential peer-to-peer transfers and long-term holdings where balances should not be public.
- **Cross-border transfers** — privacy-preserving remittances and treasury movements.
- **zk technology influence** — Zcash's zk-SNARK research is foundational to [[ethereum|Ethereum]] zk-rollups (zkSync, Starknet, Polygon zkEVM); ZEC is the "original zk" reference point in the [[zero-knowledge-proofs|ZK]] narrative.
- **ZSAs (planned)** — user-issued shielded assets, turning Zcash into a private asset platform.
- **Coinbase 50 / index inclusion** — unlike [[monero|Monero]], ZEC retains listings on major regulated venues (incl. Coinbase 50 Index membership), giving it a broader liquidity base than default-privacy peers.

---

## Market Structure & Derivatives

Zcash, as an **optional-privacy** coin still listed on major regulated exchanges, has **deeper and less fragmented liquidity than [[monero|Monero]]** — but it still carries privacy-coin delisting risk and must be flagged honestly:

- **Spot venues**: [[binance|Binance]] (ZEC/USDT), [[kraken|Kraken]] (ZEC/USD), Bitget, KuCoin, and Coinbase (ZEC is in the Coinbase 50 Index). ~$394.8M reported 24h volume (2026-06-20) — robust for a privacy coin, reflecting the post-Orchard-crash recovery flows.
- **Perps / funding / OI**: **ZEC-PERP on [[hyperliquid|Hyperliquid]]** is the liquid venue for trading disclosure-driven downside (it was the natural short instrument during the June 2026 Orchard crash); perps also on major CEXs. OI and funding spike around privacy-regulation and disclosure events.
- **Delisting exposure (honest note)**: privacy coins face elevated compliance pressure; several exchanges have historically delisted ZEC, which can trigger sharp liquidity events. ZEC's *optional* privacy makes it more defensible to exchanges than Monero's default privacy, but it is not immune.
- **Liquidity sensitivity**: a relatively small market cap versus historical highs means ZEC can move sharply on modest capital flows — both up (privacy rallies) and down (disclosure shocks).

---

## Trading Playbook

- **Privacy-narrative proxy**: ZEC trades as a proxy for the [[privacy-coins|privacy-coin narrative]] and regulatory sentiment around financial privacy; price action can be **uncorrelated with broad [[crypto-markets]]** during privacy-specific news (e.g. strong on 2026-06-20 against an extreme-fear tape).
- **XMR/ZEC pairs trade**: the canonical privacy-basket relative-value trade is [[monero|Monero]] vs Zcash. The 2026-06-20 divergence (ZEC green, XMR red) shows rotation *within* the basket — watch the ratio.
- **Disclosure-risk short (event-driven)**: as a novel zk protocol, ZEC sits in the highest-risk bucket for AI-assisted vulnerability discovery (see [[ai-vulnerability-discovery]]). The June 2026 Orchard bug (found by Claude Opus 4.8) is the canonical example; ZEC-PERP on [[hyperliquid|Hyperliquid]] is the liquid venue for trading disclosure-driven downside. See [[mythos-release-window-exploit-short]] and [[2026-exploit-target-watchlist]].
- **Catalysts**: privacy-regulation headlines, exchange delisting/relisting, ZSAs and Crosslink roadmap progress, shielded-pool adoption growth, index flows (Coinbase 50).
- **Low-float sensitivity**: small flows move price hard — useful for momentum, dangerous for size.
- **Regime note (2026-06-20)**: ZEC's outperformance into extreme fear is a privacy-narrative signal, not broad-beta strength; recovery from the Orchard crash is constructive but the unprovable-exploitation overhang remains.

---

## History

- **2013–2016** — Scientists propose Zerocoin/Zerocash; the **Electric Coin Company** (Zooko Wilcox) builds the standalone protocol.
- **28 Oct 2016** — Mainnet launch; explosive debut to an **ATH of $3,191.93 (2016-10-29)** on near-zero initial supply, then a multi-year decline.
- **2018** — **Sapling** upgrade: dramatically faster/cheaper shielded transactions.
- **2022** — **Orchard** shielded pool activates (May 2022), built on **Halo 2** (no trusted setup).
- **2024** — Sets a cycle **ATL of $16.08 (2024-07-05)** before recovering.
- **2025** — Privacy-coin rally; shielded adoption surpasses 30% of supply; ZEC re-rates sharply (+800%+ YoY into 2026).
- **29 May – 5 Jun 2026** — **Orchard counterfeiting vulnerability** discovered (29 May) and disclosed (5 Jun); ZEC crashes ~38% in 24h (see below).
- **2026-06-20** — Recovered to rank #15 (~$470.81), up on the day and week against an extreme-fear tape.

---

## Competitive Positioning — Zcash vs Monero

| Dimension | **Zcash (ZEC)** | **[[monero|Monero]] (XMR)** |
|---|---|---|
| Privacy model | **Optional** (transparent or shielded) | **Mandatory / default** (all tx shielded) |
| Cryptography | **[[zero-knowledge-proofs|zk-SNARKs]]** (Halo 2 / Orchard) | Ring signatures + stealth addresses + RingCT |
| Supply | **21M hard cap**, halvings | Uncapped, perpetual tail emission |
| Consensus | [[proof-of-work|PoW]] (Equihash); PoS "Crosslink" planned | [[proof-of-work|PoW]] (RandomX, CPU/ASIC-resistant) |
| Anonymity set | Limited by shielded-pool *usage* (>30% of supply) | Maximal — entire chain is shielded |
| Effective fungibility | Lower (much history transparent) | Very high |
| Exchange access | Broader (Binance, Coinbase 50, Kraken) | Fragmented (delisted from Binance, OKX, EEA) |
| Dev funding | Dev Fund / Community Grants / Coinholder Fund | Fair launch, no premine/funding |
| Key 2026 tail risk | **AI-discovered Orchard counterfeiting bug** | Hashrate-concentration (Qubic) + delistings |
| Forward catalyst | ZSAs (shielded assets), Crosslink PoS | Tail-emission stability, atomic swaps |

**Bottom line**: Zcash offers stronger *cryptographic* privacy (zk-SNARKs) and better exchange access, but weaker *effective* privacy due to optional shielding; Monero offers maximal default privacy and fungibility but fragmented liquidity. They are the two poles of the [[privacy-coins]] sector and the primary pairs trade within it. See also [[dash|DASH]] (lower-tier optional privacy).

---

## Major News & Events

### June 2026 — Orchard counterfeiting vulnerability (ZEC −38%)

On **June 5, 2026**, Shielded Labs disclosed a **critical counterfeiting ("forgery") vulnerability in the Orchard shielded pool** that had been live and undetected since Orchard's May 2022 activation (~4 years). The flaw allowed minting of **unlimited, undetectable counterfeit ZEC** inside the shielded pool with no valid on-chain signature. It was found on **May 29, 2026** by security engineer **Taylor Hornby** (engaged by Shielded Labs in April 2026) working with **Anthropic's Claude Opus 4.8**; an emergency fix shipped **June 1–2, 2026**. ZEC fell **~38% in 24 hours** (to a low of $442.60; peak-to-trough drawdown reported up to ~50%). Because of Orchard's privacy design, it is **cryptographically impossible to prove whether the bug was exploited before the patch**. Founder Zooko Wilcox assessed the likelihood of actual exploitation as low (the short patching window after AI-assisted discovery), but the inherent un-provability is why the market sold off hard. Full write-up: [[2026-06-05-zcash-orchard-counterfeiting-bug]]. (Source: [[2026-06-05-zcash-orchard-counterfeiting-bug]])

This is the **first market-moving case of a frontier AI model finding a critical bug in a major crypto protocol** — and the live precedent behind the [[mythos-release-window-exploit-short]] strategy and a re-rank trigger for [[2026-exploit-target-watchlist]].

---

## Regulatory

- **Privacy-coin regulatory risk** — privacy coins face elevated AML/CFT compliance pressure; several exchanges have historically delisted ZEC, which can trigger sharp liquidity events. ZEC's **optional** privacy (vs. [[monero|Monero]]'s mandatory model) makes it more defensible to regulated venues, which is why it retains broad listings (Binance, Coinbase 50, Kraken) — but it is **not immune** to the EU AMLR / US surveillance-regulation cycle that drives the whole [[privacy-coins]] sector.
- **Quantum-resistance positioning** — ZEC is tagged "Quantum-Resistant" in some category schemes, part of the long-horizon zk/security narrative.
- **CLARITY Act / market-structure** — sector-wide US legislation could clarify ZEC's status, an indirect tailwind.

---

## Risks

- **Novel-cryptography / AI-discovery risk** — as a frontier zk privacy protocol, Zcash sits in the highest-risk bucket for AI-assisted vulnerability discovery. The June 2026 Orchard counterfeiting bug (found with Claude Opus 4.8) is the canonical example; further latent flaws cannot be ruled out. See [[ai-vulnerability-discovery]].
- **Unprovable-exploitation risk** — Orchard's privacy design means it is cryptographically impossible to prove whether the counterfeiting bug was exploited before the patch, an inherent overhang for shielded-supply integrity.
- **Regulatory / delisting risk** — privacy coins face elevated compliance pressure; several exchanges have historically delisted ZEC, which can trigger sharp liquidity events.
- **Optional-privacy weakness** — because most transactions are transparent, the effective anonymity set is smaller than [[monero|Monero]]'s, weakening the privacy thesis.
- **Liquidity / volatility** — a relatively small market cap versus historical highs means ZEC can move violently on modest flows; ZEC-PERP on [[hyperliquid|Hyperliquid]] is the liquid venue for disclosure-driven downside.
- **Consensus / [[proof-of-work]] risk** — mining concentration and the pending Proof-of-Stake "Crosslink" transition introduce migration and security-model uncertainty.
- **Macro/regime** — high-beta privacy alt in an Established Bear Market with extreme fear; ~85% off ATH.

---

## Platform & Chain Information

**Native Chain:** Zcash (Layer 1); also bridged representations elsewhere

### Contract Addresses

| Chain | Address |
|---|---|
| Near Protocol | `zec.omft.near` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZEC/USDT | N/A |
| Kraken | ZEC/USD | N/A |
| Bitget | ZEC/USDT | N/A |
| KuCoin | ZEC/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ZEC-PERP | Perpetual |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3,191.93 (2016-10-29) |
| **Current vs ATH** | -85.25% |
| **All-Time Low** | $16.08 (2024-07-05) |
| **Current vs ATL** | +2827.88% |
| **24h Change** | +4.56% |
| **7d Change** | +13.56% |

> *ATH/ATL and change figures per CoinGecko snapshot, 2026-06-20.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://z.cash/](https://z.cash/) |
| **Twitter** | [@zcash](https://twitter.com/zcash) |
| **Reddit** | [https://www.reddit.com/r/zec](https://www.reddit.com/r/zec) |
| **Telegram** | [Zcash_Community](https://t.me/Zcash_Community) (5,765 members) |
| **GitHub** | [https://github.com/zcash/zcash](https://github.com/zcash/zcash) |
| **Whitepaper** | [https://zips.z.cash/protocol/protocol.pdf](https://zips.z.cash/protocol/protocol.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 4,811 |
| **GitHub Forks** | 2,073 |
| **Commits (4 weeks)** | 34 |
| **Pull Requests Merged** | 1,812 |
| **Contributors** | 102 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. Note that shielded (z-address) balances are encrypted by design and not analyzable; only transparent (t-address) holdings are visible.*

---

## See Also / Related

- [[bitcoin]] — the transparent blockchain Zcash was designed to improve upon, and the supply-cap model ZEC mirrors
- [[monero]] — the other privacy-coin anchor (mandatory privacy vs ZEC's optional)
- [[dash]] — lower-tier optional-privacy peer
- [[privacy-coins]] — sector page
- [[zero-knowledge-proofs]] — the cryptography ZEC pioneered
- [[blockchain]] — the underlying technology
- [[proof-of-work]] — Zcash's current consensus mechanism
- [[crypto-markets]] — broader market context
- [[hyperliquid]] — ZEC-PERP venue
- [[ai-vulnerability-discovery]], [[mythos-release-window-exploit-short]], [[2026-exploit-target-watchlist]] — AI-discovery / disclosure-risk context
- [[2026-06-05-zcash-orchard-counterfeiting-bug]] — full Orchard bug write-up

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko markets snapshot, 2026-06-20 (current Market Data and Price History blocks)
- (Source: [[2026-06-05-zcash-orchard-counterfeiting-bug]]) — Orchard counterfeiting vulnerability write-up

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 16.79M ZEC |
| **Total Supply** | 16.79M ZEC |
| **Max Supply** | 21.00M ZEC |
| **Fully Diluted Valuation** | $9.17B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $549.50M |
| **Market Cap Rank** | #14 |
| **24h Range** | $544.80 — $584.38 |
| **CoinGecko Sentiment** | 64% positive |
| **Last Updated** | 2026-07-16 |

---

## See Also

- [[crypto-markets]]

---
