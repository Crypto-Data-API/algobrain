---
title: "Verus"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["VRSC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://verus.io"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[layer-1]]", "[[monero]]", "[[privacy-coins]]", "[[proof-of-stake]]", "[[proof-of-work]]", "[[verge]]"]
---

# Verus

**Verus** (ticker **VRSC**) is a fair-launched (no ICO, no premine) [[layer-1]] blockchain that combines [[proof-of-work]] and [[proof-of-stake]] in a hybrid "Proof of Power" consensus (≈50/50 PoW/PoS), and pairs it with native zero-knowledge [[privacy-coins|privacy]] (Sapling), a self-sovereign identity system (VerusID), and a decentralized currency/DeFi protocol. Verus markets itself as one of the most 51%-attack-resistant public chains and uses the CPU-friendly **VerusHash** algorithm to keep mining broadly decentralized.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | VRSC |
| **Market Cap Rank** | #582 |
| **Market Cap** | $35.07M |
| **Current Price** | $0.435832 |
| **24h Volume** | $160.71 |
| **24h Change** | -1.80% |
| **7d Change** | +4.48% |
| **Circulating Supply** | ~80.46M VRSC |
| **All-Time High** | $6.74 (2024-12-08), -93.5% |
| **All-Time Low** | $0.00177843 (2018-07-26) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: backdrop is an **Established Bear Market** with the Crypto Fear & Greed Index at **~23 (extreme fear)**. The most striking data point is the **~$161 of 24h reported volume** — effectively no liquidity on tracked CEX venues, so the 24h/7d prints reflect stale or sparse quotes more than active trading. (Real trading occurs partly on Verus's own on-chain decentralized currency markets, which CoinGecko does not fully capture.)

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~80.46M VRSC |
| **Total Supply** | ~80.46M VRSC |
| **Max Supply** | ~83.54M VRSC |
| **Fully Diluted Valuation (FDV)** | ~$35.07M |
| **Market Cap / FDV** | 1.00 |

The **MC/FDV ratio of 1.00** means there is essentially **no dilution overhang**: circulating supply already equals total supply, and circulating is ~96% of the max supply. VRSC was a **no-ICO, no-premine, 100% fair launch**, so there are no team/VC unlock schedules. New issuance comes from PoW+PoS block rewards (mild, capped inflation toward the ~83.5M ceiling).

---

## How & Where It Trades

**Spot venues:** liquidity is extremely thin. CoinGecko surfaced no major centralised-exchange pair as a primary market for VRSC; trading historically occurs on smaller exchanges and Verus's own on-chain decentralized currency markets. With ~$216 of daily volume, any meaningful order would dominate the book.

**Derivatives:** No perpetual or futures market exists for VRSC — there is **no perp**. This is a spot-only, very-low-liquidity asset.

**Liquidity read:** volume/market-cap turnover is essentially **0%** on tracked venues. Treat VRSC as illiquid; exit liquidity may not exist at the quoted price.

---

## Technology & Consensus

Verus runs **"Proof of Power"**, a hybrid consensus that blends ~50% [[proof-of-work]] and ~50% [[proof-of-stake]]. The design is intended to solve the PoS "nothing-at-stake" problem and to be provably resistant to 51% hash attacks (an attacker would need to dominate both mining and staking simultaneously). Mining uses **VerusHash**, a CPU-friendly (and ASIC-resistant, "mobile-mineable") hash function aimed at keeping participation broad. On top of consensus, Verus ships:

- **Zero-knowledge privacy** via Zcash-style Sapling shielded transactions.
- **VerusID** — a self-sovereign, on-chain identity and naming system.
- **Public Blockchains as a Service (PBaaS)** — automated provisioning of new chains, with use cases such as polls and elections.

---

## Use Case, Narrative & Category

The narrative is **privacy + identity + fair-launch decentralization** on a self-mineable L1 — closer in spirit to [[bitcoin]]/Zcash ethos than to a VC-backed smart-contract platform. CoinGecko categories: Smart Contract Platform, Layer 1 (L1), MEV Protection, Proof of Work (PoW), Privacy Blockchain, Mobile Mining. It appeals to a niche of [[privacy-coins|privacy]] advocates and CPU miners rather than to mainstream DeFi flows.

---

## Valuation Framing (qualitative)

VRSC is a **fair-launch privacy/identity L1 valued on community conviction**, with valuation almost entirely detached from tradeable liquidity. Lenses:

- **No dilution overhang** — MC/FDV = 1.00 and circulating ≈ 96% of max supply; no team/VC unlocks. New issuance is mild PoW+PoS block reward toward the ~83.5M ceiling. This is a structurally clean cap-table, the opposite of low-float launches like [[vana|VANA]].
- **Liquidity, not supply, is the binding constraint** — at ~$161/day reported CEX volume, the ~$35M market cap is essentially a notional-only figure; there is no realistic exit at quoted price for size. Price discovery is unreliable.
- **vs. privacy peers** — Verus offers optional Sapling zk-shielding (stronger than [[verge|Verge]]'s IP obfuscation, weaker assurance than Monero's always-on model) plus a differentiated identity layer (VerusID) and PBaaS. Its valuation reflects niche adoption rather than the broader privacy premium captured by [[monero|Monero]].

---

## Peer Comparison

| Token | Rank | Price | Market cap | 24h volume | Privacy / niche | Cap-table |
|---|---|---|---|---|---|---|
| **VRSC (Verus)** | #582 | $0.436 | ~$35M | ~$161 | zk-shielding + VerusID + PBaaS | Fair launch, MC/FDV 1.0 |
| [[verge\|XVG]] | #506 | $0.00255 | ~$42M | ~$2.8M | Tor/I2P obfuscation | Uncapped, fair launch |
| [[monero\|XMR]] | large-cap | — | — | deep | Always-on cryptographic | Tail emission |
| [[vana\|VANA]] | #572 | $1.15 | ~$36M | ~$2.1M | Data/AI L1 | Low-float, MC/FDV 0.26 |

Verus stands out for combining privacy with a self-sovereign identity system and chain-as-a-service (PBaaS), but its near-zero tradeable liquidity makes it the least investable of the cohort on tracked venues.

---

## Notable History

- All-time high around **$6.74 (2024-12-08)**; VRSC now trades roughly 93.5% below that peak.
- All-time low of **$0.00177843 (2018-07-26)**.
- 100% fair launch (no ICO/premine) — a defining feature of its community-project identity.
- Active but small open-source developer base (GitHub: VerusCoin/VerusCoin).

---

## Risks

- **Liquidity risk (extreme):** ~$216/day volume and no derivatives — realistic entry/exit at quoted prices is doubtful; price discovery is unreliable.
- **Niche adoption:** privacy/identity narrative has a small addressable market and faces regulatory headwinds against privacy coins.
- **Visibility:** rank #582 and minimal CEX presence mean low awareness and fragile demand.
- **Security model novelty:** "Proof of Power" is less battle-tested than pure PoW or large-cap PoS at scale.
- **Macro:** small-cap, low-liquidity asset into an Established Bear Market (F&G ~23).

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 89 |
| **GitHub Forks** | 70 |
| **Commits (4 weeks)** | 12 |
| **Pull Requests Merged** | 498 |
| **Contributors** | 16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[proof-of-work]]
- [[proof-of-stake]]
- [[privacy-coins]]
- [[verge]] — fellow fair-launch privacy coin
- [[monero]] — privacy-coin benchmark
- [[bitcoin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko; `raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | VRSC |
| **Market Cap Rank** | #444 |
| **Market Cap** | $48.39M |
| **Current Price** | $0.6006 |
| **Categories** | Smart Contract Platform, Layer 1 (L1), MEV Protection, Proof of Work (PoW), Privacy Blockchain, Mobile Mining |
| **Website** | [https://verus.io](https://verus.io) |

---

## Overview

Verus Coin aims to be the world's most advanced technology, zero knowledge privacy-enabling blockchain, Verus Coin brings Sapling performance and zero knowledge features to an intelligent system with a completely unique, combined proof of stake/proof of work consensus algorithm that solves the nothing at stake problem. With this and its approach towards CPU mining and ASICs, Verus Coin may also be the most naturally decentralizing and attack resistant blockchain to exist.
Over and above its leading privacy, interchain contracts, and security features, Verus Coin's next steps include automated provisioning of public blockchains as a service, using the same technology that Verus developers created and used to solve the ""nothing at stake"" problem. At that point, the first applications that will allow provisioning of chains on their behalf will be polls and elections.

Verus introduces a new consensus algorithm called Proof of Power, a 50% PoW / 50% PoS algorithm, which solves theoretical weaknesses in other PoS systems, and is provably immune to 51% hash attacks, making Verus one of, if not the most, double-spend resistant public blockchain(s) running. With its groundbreaking consensus protocol, Verus also uses a unique hash algorithm, VerusHash, a quantum secure hash algorithm that is near-equally mineable on both CPUs and GPUs.  The Verus Coin’s project vision includes automatically provisioned public blockchains as a service.  Verus was a no-ICO, no-premine, 100% fairly launched community project.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 80.57M VRSC |
| **Total Supply** | 80.57M VRSC |
| **Max Supply** | 83.54M VRSC |
| **Fully Diluted Valuation** | $48.39M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $6.74 (2024-12-05) |
| **Current vs ATH** | -91.10% |
| **All-Time Low** | $0.00177843 (2020-11-29) |
| **Current vs ATL** | +33647.39% |
| **24h Change** | +1.25% |
| **7d Change** | +47.65% |
| **30d Change** | +37.10% |
| **1y Change** | -71.89% |

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
| **Website** | [https://verus.io](https://verus.io) |
| **Twitter** | [@veruscoin](https://twitter.com/veruscoin) |
| **Reddit** | [https://www.reddit.com/r/VerusCoin/](https://www.reddit.com/r/VerusCoin/) |
| **Discord** | [https://verus.io/discord](https://verus.io/discord) |
| **GitHub** | [https://github.com/VerusCoin/VerusCoin](https://github.com/VerusCoin/VerusCoin) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $494.38 |
| **Market Cap Rank** | #444 |
| **24h Range** | $0.5906 — $0.6006 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
