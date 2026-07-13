---
title: "Waves"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins]
aliases: ["WAVES", "Waves Platform"]
entity_type: protocol
founded: 2016
headquarters: "Decentralized"
website: "https://waves.tech/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[proof-of-stake]]", "[[staking]]", "[[smart-contracts]]", "[[consensus-mechanism]]", "[[stablecoin]]", "[[depeg]]", "[[harmony]]"]
---

# Waves

**Waves** (WAVES) is an open [[layer-1|layer-1]] blockchain protocol and development toolset for Web3 applications, launched in 2016 by Sasha Ivanov. It uses a Leased [[proof-of-stake]] (LPoS) [[consensus-mechanism]] and was historically known for making token issuance and decentralized exchange simple. The WAVES token pays transaction fees, secures the network through [[staking]]/leasing, and is used in governance. It ranks **#649** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* WAVES trades at **$0.29416**, market cap **$29,410,601** (rank **#649**), up **+0.93%** over 24h and **+8.21%** over 7 days — a relatively firm 7-day move that outpaces the broad bear-market regime (BTC bear market; Fear & Greed Index 21 / Extreme Fear), where most small-caps are flat to negative.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | WAVES |
| **Market Cap Rank** | #649 |
| **Market Cap** | $29,410,601 |
| **Current Price** | $0.29416 |
| **24h Change** | +0.93% |
| **7d Change** | +8.21% |
| **Genesis Date** | 2016-06-12 |
| **Consensus** | Leased Proof of Stake (LPoS) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Proof of Stake (PoS) |
| **Website** | [https://waves.tech/](https://waves.tech/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Waves is an open blockchain protocol and development toolset for Web3 applications, aiming to raise the security, reliability, and speed of decentralized systems. Launched in 2016, it became known early for low-friction token issuance and a built-in decentralized exchange, and later for its Ride smart-contract language and the Waves DeFi ecosystem.

---

## Architecture & Consensus

- **Layer-1 chain:** Waves runs its own [[layer-1]] blockchain (not an Ethereum token, though a bridged ERC-20 representation of WAVES exists for trading and DeFi on [[ethereum]]).
- **Leased Proof of Stake (LPoS):** holders can lease (delegate) their WAVES to full nodes that produce blocks, sharing rewards without transferring custody — a [[proof-of-stake]] variant designed to broaden participation in securing the chain. Because leasing is non-custodial, delegators retain control of their coins while still contributing weight to a node's block-production probability, which is roughly proportional to the WAVES leased plus owned by that node.
- **Ride smart contracts:** Waves uses Ride, a purpose-built **non-Turing-complete** language for [[smart-contracts]]. By deliberately omitting loops and certain unbounded operations, Ride makes execution cost predictable and aims to remove whole classes of vulnerabilities (e.g., gas-exhaustion and reentrancy patterns common on the EVM). The trade-off is reduced expressiveness compared with Solidity.
- **Account scripts and dApps:** Ride supports both account-level scripts (attaching logic to an address, e.g. for multisig) and dApp scripts (callable functions resembling contracts), giving developers a model distinct from the [[ethereum]] contract paradigm.
- **Native DEX and token tooling:** issuing custom assets and trading them was a core early differentiator. The built-in **Waves Exchange / Matcher** provided an order-book DEX where the matcher orders trades off-chain and settles them on-chain, lowering friction relative to early AMMs.

### Throughput and design philosophy

Waves marketed high transaction throughput and low fees as core selling points; concrete TPS figures vary by source and are not asserted as audited here. The broader philosophy — a self-contained chain with native asset issuance, a native DEX, and a safety-oriented contract language — positioned Waves as an "all-in-one" Web3 toolkit rather than a pure smart-contract substrate, contrasting with general-purpose chains that rely on third-party tooling.

---

## Comparison vs Peer Layer-1s

| Network | Consensus | Smart-contract language | EVM-compatible | Distinctive feature |
|---|---|---|---|---|
| **Waves** ([[waves]]) | Leased PoS (LPoS) | Ride (non-Turing-complete) | No | Native DEX + easy token issuance; algo-stablecoin legacy (USDN) |
| [[ethereum]] | PoS (Gasper) | Solidity / Vyper | Yes (native) | Deepest liquidity & tooling |
| [[harmony]] | Effective PoS (sharded) | Solidity | Yes | Sharded low-fee EVM (Horizon bridge hack) |
| [[radix]] | Cerberus (sharded BFT PoS) | Scrypto (asset-oriented) | No | DeFi-first asset safety |
| [[icon]] | Delegated PoS (P-Reps) | SCORE (Java/Python) | Partial | Cross-chain messaging |

Like [[radix]] and [[icon]], Waves chose a non-EVM execution model, gaining a safety-oriented language at the cost of the EVM's developer and liquidity network effects. Unlike those peers, Waves's history is defined less by its consensus and more by the reputational fallout of its ecosystem [[stablecoin]] (see Notable History).

---

## Governance

Waves governance has historically combined **on-chain block-reward and parameter voting** by block-generating nodes with substantial influence from the founder, Sasha Ivanov, and the core team. Block producers vote on parameters such as block rewards over rolling voting periods. The ecosystem also experimented with DAO-style governance for its DeFi protocols (e.g., Neutrino/USDN governance via the NSBT token). The 2022 USDN crisis exposed the limits of this model: critics argued that founder influence and concentrated decision-making produced opaque, contested crisis responses rather than transparent, rules-based governance — a recurring criticism of the project (see Risks).

---

## What the WAVES Token Does

- **Gas / fees:** transaction fees on the Waves chain are paid in WAVES.
- **Staking / leasing:** WAVES is leased to block-producing nodes under LPoS to earn rewards.
- **Governance and collateral:** WAVES has been used in governance and, controversially, as collateral backing the ecosystem's algorithmic stablecoin (see history).

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 100.00M WAVES |
| **Total Supply** | 100.00M WAVES |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $40.85M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $61.30 (2022-03-31) |
| **Current vs ATH** | -99.33% |
| **All-Time Low** | $0.1309 (2016-08-02) |
| **Current vs ATL** | +212.84% |
| **24h Change** | -1.47% |
| **7d Change** | -1.40% |
| **30d Change** | -10.05% |
| **1y Change** | -55.52% |

---

## Platform & Chain Information

**Native Chain:** Waves (own [[layer-1]]). The address below is the **bridged ERC-20 representation** of WAVES on [[ethereum]], used for cross-chain trading and DeFi — not the native chain.

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum (bridged ERC-20) | `0x1cf4592ebffd730c7dc92c1bdffdfc3b9efcf29a` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Upbit | WAVES/KRW | N/A |
| Bitget | WAVES/USDT | N/A |
| KuCoin | WAVES/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://waves.tech/](https://waves.tech/) |
| **Twitter** | [@wavesprotocol](https://twitter.com/wavesprotocol) |
| **Reddit** | [https://www.reddit.com/r/Wavesplatform/](https://www.reddit.com/r/Wavesplatform/) |
| **Telegram** | [wavesnews](https://t.me/wavesnews) (1.52M members) |
| **GitHub** | [https://github.com/wavesplatform/](https://github.com/wavesplatform/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,175 |
| **GitHub Forks** | 447 |
| **Pull Requests Merged** | 3,231 |
| **Contributors** | 58 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.66M (2026-04-09 snapshot) |
| **Market Cap Rank** | #649 |
| **Price (2026-06-22)** | $0.29416 |
| **24h Change (2026-06-22)** | +0.93% |
| **7d Change (2026-06-22)** | +8.21% |
| **24h Range (2026-04-09 snapshot)** | $0.4084 — $0.4212 |
| **Last Updated** | 2026-06-22 |

---

## Ecosystem & Adoption

Waves built one of the earlier self-contained DeFi ecosystems, anchored by the native Waves Exchange (matcher-based DEX), the Neutrino protocol (USDN and related assets), and lending/AMM applications written in Ride. At its 2021–2022 peak the ecosystem carried meaningful TVL and an enthusiastic, heavily Russian-/CIS-linked community (the project and founder Sasha Ivanov have strong roots in that region, with a Telegram presence reported in the millions). The USDN crisis and the broad bear market sharply reduced activity, TVL, and developer mindshare thereafter. Current ecosystem metrics should be verified on-chain rather than assumed from historical highs. Waves has at times explored pivots (enterprise tooling, Web3 infrastructure, gaming/metaverse framing), but none has restored its former prominence among [[layer-1]] platforms.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **2022 — Neutrino USD (USDN) depeg:** Waves' ecosystem [[stablecoin]], **Neutrino USD (USDN)**, was an algorithmic stablecoin collateralized largely by the WAVES token (with NSBT as a secondary backing/governance asset). The mechanism let users mint USDN by locking WAVES, so the [[stablecoin]]'s solvency depended on WAVES's price — a **reflexive loop**: if WAVES fell, USDN's backing thinned, which could pressure the peg, which could trigger forced WAVES selling, which could push WAVES lower still. In early–mid 2022 USDN repeatedly **[[depeg|de-pegged]]** from $1, at one point trading well below peg (into the $0.70s–$0.80s region during the worst stretches). Critics — including prominent on-chain analysts — alleged the design was being gamed through leveraged loops and that the team's responses (parameter changes, intervention) were opaque; the Waves team publicly disputed the causes and accused others of a coordinated attack. The episode landed in the same window as the **May 2022 collapse of Terra/UST**, the much larger algorithmic [[stablecoin]] whose ~$40B implosion seared the fragility of token-backed stablecoins into the market's memory. USDN never durably reclaimed its peg and was later restructured/rebranded (toward an "XTN" index-token framing) rather than continuing as a $1 stablecoin. The affair inflicted lasting reputational and price damage on the Waves ecosystem. It is documented here transparently rather than omitted. (See [[depeg]] and [[stablecoin]] for the general mechanism.)
- **2022 all-time high:** WAVES peaked at **$61.30** on 2022-03-31, shortly before the USDN troubles and the broader market downturn; it has since fallen more than 99% from that peak. The proximity of the ATH to the USDN crisis is itself notable — the run-up was partly fueled by USDN/Neutrino activity that subsequently unwound.
- **June 2026 rally:** WAVES is up **+8.2% over 7 days** (and +0.9% on the day) as of 2026-06-22, a firmer-than-tape move in an otherwise weak small-cap, extreme-fear environment — likely driven by token-specific flows rather than a market-wide trend; treat such moves cautiously given the asset's thin liquidity and history.

> *Notable events will continue to be added through the wiki's source ingestion workflow.*

---

## Risks

- **Algorithmic-stablecoin legacy:** the USDN [[depeg]] is a cautionary case study in reflexive, token-backed collateral design (the same family of failure that destroyed Terra/UST); any revival of similar mechanisms warrants close scrutiny, and the episode permanently weighs on the project's credibility.
- **Governance / centralization concerns:** the project has faced repeated criticism over founder influence (Sasha Ivanov) and opaque, contested crisis-response decisions during the USDN events.
- **Non-EVM adoption hurdle:** Ride and the Waves stack are not EVM-compatible, limiting the developer pool and composability with the dominant [[ethereum]]/EVM DeFi world.
- **Ecosystem attrition:** TVL, active dApps, and developer activity contracted sharply after 2022; recovery depends on renewed, durable demand that has not materialized.
- **Geographic / regulatory concentration:** strong CIS/Russia linkage exposes the project to region-specific regulatory, sanctions, and reputational risk.
- **Small-cap volatility:** at ~$29M market cap (rank #649) with thin liquidity, sharp rallies (like the current +8% week) can reverse quickly.
- **Bear-regime drawdown:** down >99% from its 2022 ATH amid an Extreme Fear market; long-term recovery depends on renewed ecosystem demand.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[proof-of-stake]]
- [[consensus-mechanism]]
- [[smart-contracts]]
- [[staking]]
- [[stablecoin]]
- [[depeg]]
- [[harmony]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko; BTC bear regime, Fear & Greed Index 21 / Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
