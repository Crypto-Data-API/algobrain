---
title: "Horizen"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, privacy]
aliases: ["Horizen", "ZEN", "ZenCash"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.horizen.io"
related: ["[[base]]", "[[crypto-markets]]", "[[ethereum]]", "[[privacy-coins]]", "[[zcash]]"]
---

# Horizen

**Horizen** (ticker **ZEN**, originally launched as **ZenCash** in 2017) is a privacy-oriented blockchain platform. It began as a Zcash-derived ([[zcash]]) Equihash Proof-of-Work coin with optional shielded transactions, and is now undergoing a major transition — **Horizen 2.0** — repositioning the project as an Ethereum-aligned **Layer-3 appchain deployed on [[base|Base]]** (Coinbase's Ethereum L2). The 2.0 vision is a modular privacy stack offering zero-knowledge proofs, TEEs, and other privacy-enhancing technologies as accessible building blocks for web apps.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ZEN |
| **Current Price** | $4.66 |
| **Market Cap** | $84,326,738 |
| **Market Cap Rank** | #299 |
| **24h Volume** | $11,167,691 |
| **24h Change** | +6.88% |
| **7d Change** | +6.33% |
| **24h Range** | $4.35 — $4.74 |
| **Fully Diluted Valuation** | $97,830,448 |
| **All-Time High** | $165.92 (2021-05-08), -97.19% |
| **All-Time Low** | $3.26 (2019-10-17), +42.8% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the backdrop on 2026-06-21 is risk-off — the [[fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (extreme fear)** in an **"Established Bear Market."** ZEN is bucking the trend with ~+6.9% on the day and ~+6.3% on the week, on a respectable ~$11.2M of daily volume — outperformance that may reflect Horizen 2.0 migration newsflow rather than broad market strength. At ~$4.66 the token trades ~97% below its 2021 peak and only ~43% above its 2019 all-time low.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~18.10M ZEN |
| **Total Supply** | 21.00M ZEN |
| **Max Supply** | 21.00M ZEN |
| **Market Cap / FDV Ratio** | ~0.86 |

- **Bitcoin-style hard cap:** ZEN has a fixed **21,000,000** maximum supply (mirroring [[bitcoin|Bitcoin]]), with ~18.1M currently circulating — roughly 14% still to be emitted/unlocked.
- **Consensus evolution:** ZEN historically secured an Equihash PoW chain with a node/secure-node incentive system; Horizen 2.0 moves away from the prior hybrid PoW/PoS model toward application-level security inherited from Base/Ethereum.
- **Migration mechanics:** holders should track the official Horizen 2.0 token-migration path (ERC-20 ZEN on Base alongside the legacy chain), as bridging/migration introduces operational considerations.

---

## Market Structure & Derivatives

ZEN has historically been more broadly listed than pure privacy coins, but its privacy heritage still creates listing sensitivity:

- **Spot (CEX):** Binance (ZEN/USDT), Bitget (ZEN/USDT), KuCoin (ZEN/USDT). ZEN's optional (rather than mandatory) privacy and ongoing pivot away from being a pure privacy coin have helped it retain more major-exchange access than mandatory-privacy peers like [[pirate-chain|Pirate Chain]].
- **Derivatives:** ZEN-PERP perpetual futures trade on [[hyperliquid|Hyperliquid]] (on-chain perps DEX), giving ZEN a decentralized derivatives venue with visible [[open-interest]] and [[funding-rate|funding]]. Funding/OI depth is modest but tradable; in the current bear-market regime expect funding to track broad altcoin sentiment. This makes ZEN unusual among privacy coins — its peer [[pirate-chain|Pirate Chain]] (ARRR) has no liquid perp market at all.
- **On-chain (Base):** as Horizen 2.0 rolls out on [[base|Base]], ZEN gains DEX liquidity within the Base/Ethereum DeFi ecosystem (contract `0xf43eb8de897fbc7f2502483b2bef7bb9ea179229` on Base).
- **Liquidity:** ~$11.2M daily volume against an ~$84M cap is healthy turnover (~13%/day) for a small-cap — meaningfully deeper than the thin books of mandatory-privacy peers.
- **Privacy-coin caveat:** despite broader access than mandatory-privacy coins, ZEN's legacy as a shielded/Zcash-derived asset means it can still be caught by exchange privacy-coin delisting waves; the 2.0 pivot is partly a strategic response to that risk.

### Privacy-Coin Peer Comparison

| Coin | Ticker | Privacy model | MC rank | Approx. market cap | Derivatives |
|---|---|---|---|---|---|
| [[monero|Monero]] | XMR | Mandatory (ring signatures) | Privacy leader | Multi-billion | Broad CEX + perps |
| [[zcash|Zcash]] | ZEC | Optional (zk-SNARK) | Mid-cap privacy | Hundreds of $M | Broad CEX + perps |
| **Horizen** | **ZEN** | **Optional → privacy infra (2.0 on Base)** | **#299** | **~$84M** | **ZEN-PERP on [[hyperliquid|Hyperliquid]]** |
| [[pirate-chain|Pirate Chain]] | ARRR | Mandatory (100% shielded) | #389 | ~$62M | None (spot-only) |

Horizen is mid-cap among privacy coins and uniquely is pivoting *out* of the pure-privacy-coin category toward selling privacy infrastructure, which differentiates its risk/reward from Monero, Zcash and Pirate Chain.

---

## Use Case, Narrative & Category

Horizen's narrative is mid-transition from **privacy coin** to **modular privacy infrastructure** ([[privacy-coins]]):

- **Legacy (ZenCash/Horizen 1.0):** a Zcash-fork Equihash coin with shielded transactions, a "Sidechain" SDK (Zendoo) for app-specific chains, and a secure-node network.
- **Horizen 2.0:** repositioning as a **Layer-3 on Base**, inheriting Ethereum security and Base scalability while offering a decentralized privacy stack (ZKPs, TEEs, ABE, MPC, FHE) as composable primitives for any app — "the first privacy appchain on Base."
- **Privacy-as-a-service thesis:** rather than selling private money, Horizen 2.0 aims to sell programmable privacy infrastructure to developers across the Ethereum ecosystem.

---

## Valuation Framing

[[privacy-coins|Privacy coins]] have no cash flows and are valued on adoption and the credibility of their privacy guarantees. Horizen straddles two valuation regimes:

- **Legacy privacy-coin lens:** as a Zcash-derived, hard-capped (21M) PoW coin, ZEN historically traded as a mid-tier privacy asset, valued on usage and listing access. On this lens it competes directly with [[zcash|Zcash]] and [[monero|Monero]] for the same mindshare and liquidity.
- **Privacy-infrastructure / appchain lens:** Horizen 2.0 reframes ZEN as the token of a Base-aligned L3 selling composable privacy primitives (ZKPs, TEEs, MPC, FHE). On this lens the relevant comparison set shifts toward Ethereum L2/L3 and ZK-infrastructure tokens, and value would accrue from developer adoption and fees on the new stack rather than from private-money usage.
- **Migration-as-catalyst:** the recent outperformance into Extreme Fear is best read as a *re-rating bet* on a successful 2.0 transition rather than broad market strength. The thesis is binary on execution — strong developer traction re-rates ZEN as infra; a stalled migration leaves it a shrinking legacy privacy coin near its 2019 lows.
- **Hard-cap anchor:** the fixed 21M supply (Bitcoin-style scarcity) underpins a long-run scarcity narrative regardless of which lens dominates.

---

## Notable History

- **2017:** Launched as **ZenCash**, a fork of the Zcash codebase using Equihash PoW.
- **2018:** Rebranded to **Horizen**; suffered a **51% attack** in mid-2018, after which the project introduced a delayed-block-submission penalty to harden against reorg attacks — a frequently-cited case study in PoW security.
- **2021 bull market:** ZEN reached its all-time high of **$165.92 (2021-05-08)**; the current price is roughly **97% below** that peak.
- **2019 low:** all-time low of **$3.26 (2019-10-17)** — notably, the current price is only modestly above that historic low.
- **2024–2026:** announcement and rollout of **Horizen 2.0** as an L3 appchain on Base, marking the strategic pivot from a standalone privacy chain to an Ethereum-aligned privacy platform.

---

## Risks

- **Migration/execution risk:** the Horizen 2.0 transition is a fundamental re-architecture (abandoning the prior PoW/PoS chain for an L3 on Base). Migration friction, technical delays, or weak developer adoption of the new privacy stack are the central risks.
- **Privacy-coin regulatory/delisting risk:** as a Zcash-derived shielded asset, ZEN remains exposed to exchange privacy-coin delistings and AML/travel-rule pressure, even as the 2.0 pivot tries to reduce that exposure.
- **PoW security history:** the 2018 51% attack is a reminder that smaller-cap chains are vulnerable; the new model shifts security reliance onto Base/Ethereum, which is itself a dependency.
- **Bear-market beta:** recent outperformance is news-driven; a sustained risk-off move can still pull ZEN down with the sector.
- **Competition:** crowded zero-knowledge / privacy-infrastructure space competing for the same developer mindshare on Ethereum L2s/L3s.

---

## Related

- [[crypto-markets]]
- [[base]]
- [[privacy-coins]]
- [[zcash]]
- [[monero]]
- [[pirate-chain]]
- [[bitcoin]]
- [[hyperliquid]]
- [[perpetual-futures]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko markets data.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZEN |
| **Market Cap Rank** | #306 |
| **Market Cap** | $77.29M |
| **Current Price** | $4.25 |
| **Hashing Algorithm** | Equihash |
| **Categories** | Zero Knowledge (ZK), Made in USA, Privacy Infrastructure, Base Native, Privacy |
| **Website** | [https://www.horizen.io](https://www.horizen.io) |

---

## Overview

What is the project about?&nbsp;

Horizen is a modular privacy-first platform designed to make privacy technology, such as zero-knowledge proofs and TEEs accessible and usable across the web. Originally launched in 2017 as a fair launch, non-ICO project, Horizen is now undergoing a major evolution with the launch of Horizen 2.0, a next-generation Layer 3 (L3) appchain deployed on Base, the Ethereum Layer 2 developed by Coinbase.

Horizen 2.0 is built as an Ethereum-aligned Layer 3 appchain on Base, inheriting Ethereum's security while implementing its own application-level integrity guarantees.

Key components of Horizen’s security model include:

Ethereum-Aligned Security:&nbsp;As an appchain deployed on Base, Horizen 2.0 benefits from Base’s rollup security and settlement on Ethereum, ensuring robust finality and composability with other L2 and L3 applications.

Simplified and Secure Architecture:&nbsp;Unlike Horizen’s previous iterations (which used a hybrid PoW/PoS model), Horizen 2.0 focuses on application-level security, decentralization of its privacy layers, and composability with existing infrastructure — reducing complexity and increasing user safety.

Decentralized Privacy Stack:&nbsp;Horizen’s focus on decentralizing privacy infrastructure (e.g., decentralized proof generation) allows for modular, secure applications that uphold data confidentiality without compromising performance.

What makes your project unique?

Privacy-first Approach:&nbsp;Horizen integrates a diverse stack of privacy-enhancing technologies (PETs) — including zero-knowledge proofs (ZKPs), trusted execution environments (TEEs), attribute-based encryption (ABE), multi-party computation (MPC), and fully homomorphic encryption (FHE) — to deliver scalable, flexible, and future-ready privacy solutions across its platform.

First Privacy Appchain on Base:&nbsp;As an L3 on Base, Horizen benefits from Ethereum’s security and Base’s scalability, while enabling a privacy layer for any app on t...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 18.18M ZEN |
| **Total Supply** | 21.00M ZEN |
| **Max Supply** | 21.00M ZEN |
| **Fully Diluted Valuation** | $89.29M |
| **Market Cap / FDV Ratio** | 0.87 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $165.92 (2021-05-08) |
| **Current vs ATH** | -97.43% |
| **All-Time Low** | $3.26 (2019-10-17) |
| **Current vs ATL** | +30.40% |
| **24h Change** | -0.14% |
| **7d Change** | +2.84% |
| **30d Change** | -10.38% |
| **1y Change** | -49.77% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0xf43eb8de897fbc7f2502483b2bef7bb9ea179229` |
| Horizen | `0x57da2d504bf8b83ef304759d9f2648522d7a9280` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZEN/USDT | N/A |
| Bitget | ZEN/USDT | N/A |
| KuCoin | ZEN/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.horizen.io](https://www.horizen.io) |
| **Twitter** | [@horizenglobal](https://twitter.com/horizenglobal) |
| **Reddit** | [https://www.reddit.com/r/Horizen](https://www.reddit.com/r/Horizen) |
| **Telegram** | [horizencommunity](https://t.me/horizencommunity) (5,704 members) |
| **GitHub** | [https://github.com/HorizenOfficial](https://github.com/HorizenOfficial) |
| **Whitepaper** | [https://downloads.horizen.io/file/web-assets/Horizen+Whitepaper+v1.0.0.pdf](https://downloads.horizen.io/file/web-assets/Horizen+Whitepaper+v1.0.0.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 99 |
| **GitHub Forks** | 59 |
| **Commits (4 weeks)** | 3 |
| **Pull Requests Merged** | 243 |
| **Contributors** | 28 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $12.24M |
| **Market Cap Rank** | #306 |
| **24h Range** | $4.24 — $4.48 |
| **CoinGecko Sentiment** | 50% positive |
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
- [[base]]

---
