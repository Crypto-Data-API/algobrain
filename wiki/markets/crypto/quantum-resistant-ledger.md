---
title: "Quantum Resistant Ledger"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, infrastructure]
aliases: ["QRL"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://www.theqrl.org"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[post-quantum-cryptography]]"]
---

# Quantum Resistant Ledger

**Quantum Resistant Ledger** (ticker **QRL**) is a **Layer-1 cryptocurrency engineered for post-quantum security**. Founded by Peter Waterland, it uses the hash-based **XMSS** signature scheme to protect transactions against attacks from future quantum computers — a threat to which the ECDSA signatures used by [[bitcoin|Bitcoin]] and [[ethereum|Ethereum]] are theoretically vulnerable (via Shor's algorithm). It runs its own [[proof-of-work]] blockchain and ranks **#320** by market capitalization.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | QRL |
| **Chain / Ecosystem** | Own Layer-1 blockchain (PoW) |
| **Current Price** | $0.989354 |
| **Market Cap** | $77,558,368 |
| **Market Cap Rank** | #320 |
| **24h Volume** | $18,929 |
| **24h Change** | -1.03% |
| **7d Change** | +3.88% |
| **Circulating Supply** | 78.39M QRL |
| **Max Supply** | 105.00M QRL |
| **FDV (at max supply)** | ~$103.9M |
| **Market Cap / FDV** | ~0.75 |
| **All-Time High** | $3.87 (2018-01-09) |
| **vs ATH** | -74.4% |
| **All-Time Low** | $0.04116971 (2023-12-01) |
| **vs ATL** | +2,303% |

**Macro backdrop (2026-06-21):** the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (extreme fear)** within an **"Established Bear Market"** regime. QRL's 24h volume is **extraordinarily thin (~$19K)** — among the most illiquid names of this size, so quoted prices are fragile and a single order can move the market. The "post-quantum" narrative is **event-driven** and tends to spike on quantum-computing headlines; the **+3.9% week** likely reflects narrative interest rather than flow.

---

## Technology & Protocol

QRL is a **standalone post-quantum Layer-1**, not a token on another chain:

- **XMSS signatures** — QRL's core design choice is the **eXtended Merkle Signature Scheme (XMSS)**, a *stateful* hash-based signature considered resistant to quantum attacks (notably Shor's algorithm, which threatens elliptic-curve signatures like ECDSA). Hash-based schemes rely only on the security of the underlying hash function, which Grover's algorithm weakens only quadratically.
- **Stateful trade-off** — XMSS signatures must **never be reused** (each key has a finite number of one-time signatures), which adds wallet/UX complexity versus stateless schemes; QRL manages this in-protocol.
- **Proof-of-Work chain** — QRL runs its own PoW Layer-1 (RandomX-family hashing), issuing new supply to miners; transfers settle natively rather than via smart contracts on another chain.
- **Roadmap** — the project has worked toward smart-contract / EVM-compatible capability ("QRL Zond") while preserving post-quantum signatures.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 78.39M QRL |
| **Total Supply** | 78.39M QRL |
| **Max Supply** | 105.00M QRL |
| **Circulating / Max** | ~74.7% |
| **Market Cap / FDV (at max supply)** | ~0.75 |

Circulating supply (78.39M) currently equals total supply, but **max supply is 105M** — roughly **26.6M tokens (~34% over current circulating)** remain to be emitted as **block rewards over the chain's mining schedule**, representing gradual long-run inflation. As a PoW chain, new supply goes to **miners** rather than via investor unlocks — a cleaner emission profile than a VC-unlock cliff, but still a dilution wedge (MC/FDV ~0.75 at max supply).

---

## Market Structure & Derivatives

| Venue type | Detail |
|---|---|
| **Spot (CEX/DEX)** | Very limited — the snapshot reports no major exchange listings and only ~$19K of 24h volume; historically a handful of smaller CEXs |
| **Derivatives / Perps** | None meaningful — negligible speculative-leverage demand, so [[perpetual-futures\|perps]], [[funding-rate\|funding]], and open-interest are not applicable |
| **Native chain** | Own Layer-1 PoW blockchain; on-chain transfers settle natively |

Deep, reliable order books are **absent**, making QRL an illiquid, hard-to-exit asset — the dominant market-structure fact for this name.

---

## Narrative & Category

QRL's thesis is **post-quantum security** ([[post-quantum-cryptography|post-quantum cryptography]]). It positions itself as a **"future-proof" chain** for value transfer and decentralized messaging that survives the day large-scale quantum computers can break classical cryptography. The narrative is fundamentally **event-driven**: interest and price react to **quantum-computing milestones** (e.g., advances from Google, IBM, or other labs) rather than DeFi/usage metrics. Category tags: Smart Contract Platform, Proof of Work (PoW), Quantum-Resistant.

---

## Valuation Framing

QRL is a **narrative-and-option token** rather than a cash-flow or usage-valued asset:

- **Optionality on a real but unscheduled threat:** the "quantum threat" to ECDSA is real, but its timeline is uncertain (potentially years to decades). QRL is best framed as a **call option on quantum-computing fears materializing before competitors adopt post-quantum signatures**.
- **No usage anchor:** despite long development, QRL has limited DeFi/usage traction; there is little fee revenue or active-user base to value, so price rests on narrative and event timing.
- **Erosion risk:** if [[bitcoin|Bitcoin]], [[ethereum|Ethereum]], or NIST-standardized PQC schemes (e.g., SPHINCS+, Dilithium) are adopted by incumbents, QRL's differentiation — its entire thesis — erodes.
- **Net:** speculative, low-liquidity, event-driven optionality; not reflexive like a [[meme-coins|meme]] (it has genuine tech), but its value is contingent on a narrative that can stay un-validated indefinitely.

---

## Peer Comparison

| Token | Category | Price | Mkt Cap | Rank | MC/FDV | Differentiator |
|---|---|---|---|---|---|---|
| **QRL** | Post-quantum L1 | $0.99 | $78M | #320 | ~0.75 | XMSS hash-based signatures |
| [[bitcoin\|BTC]] | PoW store-of-value | (mega-cap) | — | — | — | ECDSA (quantum-exposed long-run) |
| [[ethereum\|ETH]] | Smart-contract L1 | (mega-cap) | — | — | — | ECDSA; PQC on roadmap |

QRL's pitch is precisely the **inverse** of the incumbents' quantum exposure — it trades the incumbents' liquidity, security budget, and adoption for native post-quantum signatures, betting that quantum risk is mispriced.

---

## Notable History

- **June 2018:** mainnet launched (genesis 2018-06-26), one of the first chains explicitly built for quantum resistance using XMSS.
- **January 9, 2018:** all-time high of **$3.87** during the 2017–18 cycle (pre-mainnet, on early exchanges).
- **December 1, 2023:** all-time low of $0.0412.
- **2024–2026:** recovered sharply on quantum-computing narrative interest; trades near $0.99 on 2026-06-21, ~74% below ATH but well above its 2023 low (~23x).
- **Active development:** GitHub shows sustained work (461 stars, 1,394 merged PRs, 32 contributors) — unusual longevity for a small-cap from this era.

---

## Risks

- **Severe illiquidity:** ~$19K/24h volume and no major exchange listings make QRL extremely hard to enter/exit at scale; price quotes are fragile.
- **Narrative timing risk:** the "quantum threat" is real but its timeline is uncertain; the thesis can stay un-validated indefinitely, and competing chains may also adopt post-quantum signatures, eroding QRL's differentiation.
- **Adoption gap:** despite long development, QRL has limited DeFi/usage traction; value rests largely on narrative.
- **Future inflation:** ~34% additional supply remains to be mined into circulation.
- **Technical risk:** XMSS is stateful (signatures must not be reused), adding wallet/UX complexity versus standard schemes.
- **Regime sensitivity:** down ~74% from ATH; a thin small-cap in an extreme-fear / bear regime (Fear & Greed = 23 on 2026-06-21).

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 461 |
| **GitHub Forks** | 117 |
| **Pull Requests Merged** | 1,394 |
| **Contributors** | 32 |

---

## Related

- [[post-quantum-cryptography]] — the cryptographic threat/defense QRL addresses
- [[bitcoin]] / [[ethereum]] — chains whose ECDSA signatures QRL aims to improve on
- [[proof-of-work]]
- [[crypto-markets]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 via cryptodataapi.com / CoinGecko.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | QRL |
| **Market Cap Rank** | #305 |
| **Market Cap** | $77.36M |
| **Current Price** | $0.9865 |
| **Genesis Date** | 2018-06-26 |
| **Hashing Algorithm** | RandomX |
| **Categories** | Smart Contract Platform, Proof of Work (PoW), Quantum-Resistant |
| **Website** | [https://www.theqrl.org](https://www.theqrl.org) |

---

## Overview

Quantum Resistant Ledger is a cryptocurrency based on the Python programming language, aimed at combating future attacks by quantum computers. This cryptocurrency is the brainchild of Peter Waterland who realised that Bitcoin, Ethereum, and other such cryptocurrencies have no protection against future technology. It claims to be a “future-proof” cryptocurrency which enables transactions and decentralized communication while providing protection against classical as well as quantum computer attacks.

The Quantum Resistant Ledger company was founded by Peter Waterland, who found that Bitcoin, as well as Ethereum signatures are susceptible to attacks by powerful quantum computers. His research on quantum computers and signature programs let to the development of this new cryptocurrency, designed to be resistant to the present classical attacks as well as any future quantum computer attacks. Their team is made up of a diverse range of members spread out across the world, including developers (core, blockchain, mobile developers, etc.), analysts, advisors, marketing managers, designers and more.

Quantum Resistant Ledger is the first ever cryptocurrency and the only one in existence as of August 2018, to consider the threat that the future technology of quantum computing poses to cryptocurrencies and their working. It uses a technology specifically designed for post-quantum security, called XMSS, which makes it secure against powerful quantum computers even while using a Proof-of-Stake consensus mechanism. Security against cyber-attacks is a very serious concern in this digital age, especially when you have digital assets whose loss is likely to lead you to bankruptcy.

QRL is the first blockchain technology that provides durability and stability through resistance to quantum computer attacks. The encryption methods used by modern blockchains can become vulnerable to quantum computers over the next ten years. QRL tries to create a blockchain with long-term stability. By ...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 78.39M QRL |
| **Total Supply** | 78.39M QRL |
| **Max Supply** | 105.00M QRL |
| **Fully Diluted Valuation** | $77.36M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.87 (2018-01-09) |
| **Current vs ATH** | -74.43% |
| **All-Time Low** | $0.0412 (2023-12-01) |
| **Current vs ATL** | +2301.17% |
| **24h Change** | +9.98% |
| **7d Change** | +31.44% |
| **30d Change** | -3.26% |
| **1y Change** | +19.47% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.theqrl.org](https://www.theqrl.org) |
| **Reddit** | [https://www.reddit.com/r/qrl](https://www.reddit.com/r/qrl) |
| **Telegram** | [QRLedgerOfficial](https://t.me/QRLedgerOfficial) (2,228 members) |
| **Discord** | [https://www.theqrl.org/discord](https://www.theqrl.org/discord) |
| **GitHub** | [https://github.com/theQRL/QRL](https://github.com/theQRL/QRL) |
| **Whitepaper** | [https://github.com/theQRL/Whitepaper/blob/master/QRL_whitepaper.pdf](https://github.com/theQRL/Whitepaper/blob/master/QRL_whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $56,691.00 |
| **Market Cap Rank** | #305 |
| **24h Range** | $0.8792 — $0.9976 |
| **CoinGecko Sentiment** | 83% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
