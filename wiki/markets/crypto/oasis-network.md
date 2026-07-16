---
title: "Oasis"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["Oasis Network", "ROSE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://oasisprotocol.org/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[mina-protocol]]", "[[privacy-coins]]", "[[proof-of-stake]]", "[[zero-knowledge-proofs]]"]
---

# Oasis

**Oasis** (ticker **ROSE**, formerly "Oasis Network") is a [[proof-of-stake]] [[layer-1]] purpose-built for **confidential computing** — privacy-preserving smart contracts at scale, placing it in the [[privacy-coins|privacy-blockchain]] category. Its flagship runtime, **Sapphire**, is marketed as the first confidential EVM, where contract state and inputs can be kept encrypted even from validators via trusted-execution-environment (TEE)–backed compute. Oasis separates **consensus** (a settlement layer secured by [[proof-of-stake]]) from **ParaTimes** (parallel runtime environments for computation), and offers cross-chain privacy tooling (the Oasis Privacy Layer) so EVM dApps on other chains can tap confidential execution.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ROSE |
| **Market Cap Rank** | #439 |
| **Market Cap** | $51.96M |
| **Current Price** | $0.0066718 |
| **24h Change** | +2.46% |
| **7d Change** | +4.12% |
| **24h Volume** | $2.60M |
| **Circulating Supply** | ~7.79B ROSE |
| **Fully Diluted Valuation** | ~$66.72M |
| **All-Time High** | $0.597 (2022-01-15) — now -98.9% |
| **All-Time Low** | $0.00600 (2026-06-10) — now +11.2% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. ROSE trades roughly 11% above its all-time low (~$0.0060, set just days earlier on 2026-06-10) and about 99% below its January-2022 all-time high of $0.597. Its +4.12% 7-day and +2.46% 24h moves are among the few positive prints in this peer group, though on light ~$2.6M volume.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~7.79B ROSE |
| **Total Supply** | 10.00B ROSE |
| **Max Supply** | 10.00B ROSE |
| **Fully Diluted Valuation (FDV)** | ~$66.72M |
| **Market Cap / FDV** | ~0.78 |

ROSE is the network's gas, staking, and governance token, with a hard cap of 10B. Circulating supply is ~78% of max, so remaining dilution from staking rewards and unlocked allocations is moderate but not negligible — at full dilution the market cap would rise ~28% from current levels purely from supply growth, a mild structural headwind versus fully-circulating peers like [[dusk-network|DUSK]]. Validators and delegators **stake ROSE** on the consensus layer to secure the chain and earn staking rewards; rewards are funded from a fixed reward schedule rather than open-ended inflation, given the capped supply.

---

## How & Where It Trades

**Spot venues.** ROSE is listed on [[binance]] (ROSE/USDT), Bitget, and KuCoin, among others. The asset carries a BNB Smart Chain contract (`0xf006...bd4a`) and is tagged in the [[bnb]] Chain ecosystem.

**Derivatives.** ROSE perpetuals are available on major centralized derivatives venues. The wiki's prior snapshot did **not** record a ROSE perp on [[hyperliquid]], so do not assume one exists — verify the live venue list before trading derivatives. With a ~$51M market cap and only ~$2.3M daily volume (the thinnest in this peer group), liquidity is shallow and slippage/funding swings can be severe.

---

## Technology & Consensus

Oasis uses a **two-layer architecture**:

- **Consensus layer** — a [[proof-of-stake]] (Tendermint/Cosmos-SDK–based) settlement layer that orders blocks and secures the network.
- **ParaTime layer** — parallel runtimes that execute computation off the consensus critical path. The key runtimes are **Sapphire** (confidential EVM) and **Emerald** (standard EVM), with **Cipher** for confidential WASM contracts.

Confidentiality is delivered through **trusted execution environments (TEEs)**: contract execution happens inside hardware enclaves so that even node operators cannot see the plaintext state or inputs. This TEE-based model contrasts with [[zero-knowledge-proofs|zk]]-based privacy chains — it is faster and EVM-compatible but introduces a hardware-trust assumption. The Oasis Privacy Layer extends this confidentiality cross-chain to EVM dApps elsewhere, and Runtime Offchain Logic (ROFL) brings verifiable off-chain compute on-chain.

---

## Use Case, Narrative & Category

Oasis sits in the **privacy / confidential-computing L1** category ([[privacy-coins]]) alongside Secret Network, [[mina-protocol]] (zk-privacy), and others. Its narrative leans on confidential DeFi, on-chain data privacy, and — increasingly — **confidential AI / verifiable compute** (running models or agents over private user data). Tagged categories include Smart Contract Platform, Layer 1 (L1), Proof of Stake (PoS), Privacy Blockchain, Privacy Infrastructure, BNB Chain Ecosystem, Coinbase 50 Index, plus VC-portfolio tags (a16z, Pantera, Polychain, Blockchain Capital, Binance Labs/YZi).

---

## Valuation Framing (qualitative)

- **MC/FDV ~0.78:** ~22% of supply is still to enter circulation, a moderate but real dilution overhang. At today's price, fully diluted value is ~$67M versus a ~$52M live cap.
- **Near the floor:** ROSE printed its all-time low ($0.0060) on 2026-06-10, only ~11% below the current price. A name trading this close to its cycle low with a multi-year operating history and tier-1 VC backing (a16z, Pantera, Polychain) is the kind of "deep value, deep skepticism" setup that re-rates only on a clear adoption catalyst.
- **No earnings anchor:** like all infra L1s, ROSE has no cash-flow valuation; the bull case rests on confidential-compute / confidential-AI demand actually arriving. The bear case is that TEE-based privacy demand never materializes at scale, leaving a well-funded chain with thin usage.
- **Catalyst dependence:** a credible "confidential AI" flagship application (private inference over sensitive data) is the most plausible re-rating trigger; absent that, ROSE trades as bear-market beta on a privacy narrative.

---

## Peer Comparison

ROSE against other privacy and small/mid-cap infrastructure L1s in this cohort (data as of 2026-06-21):

| Token | Ticker | Price | Market Cap | Rank | 7d % | MC/FDV | Privacy tech |
|---|---|---|---|---|---|---|---|
| **Oasis** | ROSE | $0.0066718 | $52.0M | #439 | +4.12% | 0.78 | TEE / confidential EVM |
| [[dusk-network]] | DUSK | $0.085452 | $50.4M | #449 | -5.68% | 1.00 | ZK compliance / confidential SC |
| [[nervos-network]] | CKB | $0.00104816 | $51.3M | #443 | -8.58% | 0.98 | PoW (privacy not core) |
| [[theta-token\|Theta]] | THETA | $0.15476 | $154.8M | #206 | -3.34% | 1.00 | n/a (DePIN/compute) |
| [[mina-protocol]] | MINA | — | — | — | — | — | ZK / succinct blockchain |

Among the sub-$60M privacy/infra names, ROSE is one of only two with a *positive* 7-day return in an extreme-fear tape, distinguishing its TEE-based confidential-compute approach from [[dusk-network|DUSK's]] ZK-compliance angle and [[zero-knowledge-proofs|zk]]-based [[mina-protocol]].

---

## Notable History

- The Oasis Network mainnet launched in 2020, backed by a16z, Binance Labs, Polychain, and others.
- ROSE printed its all-time high of **$0.597 on 2022-01-15** during the prior bull cycle.
- It has since fallen ~99%, reaching a fresh all-time low of **$0.00600 on 2026-06-10**.
- As of 2026-06-21 it trades at ~$0.0067, about 11% off the low, with a rare positive 7-day return (+4.12%) in an otherwise weak peer group.

---

## Risks

- **TEE / hardware-trust assumption.** Confidentiality relies on the integrity of hardware enclaves; side-channel or microarchitectural attacks against TEEs are an ongoing research concern and represent a distinct risk versus pure-cryptographic (zk) privacy.
- **Adoption gap.** Confidential-computing demand on-chain has been slow to materialize; the value case depends on usage that remains limited.
- **Privacy / regulatory scrutiny.** Privacy-focused chains face heightened regulatory attention.
- **Competition.** Crowded privacy-and-AI narrative with both zk-based and TEE-based rivals.
- **Liquidity / sentiment.** Low volume (~$2.6M/day), down ~99% from ATH, sitting only ~11% above a fresh all-time low under an extreme-fear macro regime.

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[layer-1]]
- [[proof-of-stake]]
- [[privacy-coins]]
- [[zero-knowledge-proofs]]
- [[mina-protocol]]
- [[dusk-network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ROSE |
| **Market Cap Rank** | #468 |
| **Market Cap** | $44.61M |
| **Current Price** | $0.00562786 |
| **Hashing Algorithm** | Proof of Stake |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Proof of Stake (PoS), Privacy Blockchain, Privacy Infrastructure, Privacy |
| **Website** | [https://oasisprotocol.org/](https://oasisprotocol.org/) |

---

## Overview

Oasis is a layer-one blockchain built to support confidential applications at scale. It’s home to Sapphire, the world’s first private EVM network, Oasis Privacy Layer, a cross-chain privacy solution for any EVM dApp, and Runtime Offchain Logic, a framework that brings trustworthy off-chain computing, onchain. Powered by its ROSE token, Oasis leverages a unique layered architecture and native rollup support, making it ideal for use cases in AI, DeFi, DAOs, gaming, and more.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 7.93B ROSE |
| **Total Supply** | 10.00B ROSE |
| **Max Supply** | 10.00B ROSE |
| **Fully Diluted Valuation** | $56.28M |
| **Market Cap / FDV Ratio** | 0.79 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5973 (2022-01-15) |
| **Current vs ATH** | -99.06% |
| **All-Time Low** | $0.00545645 (2026-07-13) |
| **Current vs ATL** | +3.20% |
| **24h Change** | -1.96% |
| **7d Change** | -3.25% |
| **30d Change** | -20.38% |
| **1y Change** | -80.48% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xf00600ebc7633462bc4f9c61ea2ce99f5aaebd4a` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ROSE/USDT | N/A |
| Bitget | ROSE/USDT | N/A |
| KuCoin | ROSE/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://oasisprotocol.org/](https://oasisprotocol.org/) |
| **Twitter** | [@oasisprotocol](https://twitter.com/oasisprotocol) |
| **Reddit** | [https://www.reddit.com/r/oasisnetwork](https://www.reddit.com/r/oasisnetwork) |
| **Telegram** | [oasisprotocolcommunity](https://t.me/oasisprotocolcommunity) (21,798 members) |
| **Discord** | [https://discord.com/invite/8tUba8eqSw](https://discord.com/invite/8tUba8eqSw) |
| **GitHub** | [https://github.com/oasisprotocol](https://github.com/oasisprotocol) |
| **Whitepaper** | [https://docsend.com/view/aq86q2pckrut2yvq](https://docsend.com/view/aq86q2pckrut2yvq) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.60M |
| **Market Cap Rank** | #468 |
| **24h Range** | $0.00560154 — $0.00587430 |
| **CoinGecko Sentiment** | 67% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
