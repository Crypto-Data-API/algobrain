---
title: "ZEROBASE"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, altcoins, ethereum]
aliases: ["ZBT", "ZeroBase"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://zerobase.pro/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[zero-knowledge-proof]]", "[[verifiable-compute]]", "[[defi]]"]
---

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

# ZEROBASE

**ZEROBASE** (ZBT) is a **real-time [[zero-knowledge-proof|ZK-proof]] network** — proving infrastructure designed to generate zero-knowledge proofs with low latency so that applications can use verifiable computation interactively rather than waiting minutes for a proof. It positions itself as a decentralized cryptographic infrastructure layer that combines [[zero-knowledge-proof|ZKPs]] with trusted execution environments (TEEs) to enable [[verifiable-compute|verifiable off-chain computation]] without exposing sensitive data. As of 2026-06-22 ZBT trades at **$0.1203**, ranked **#646** by market capitalization with a market cap of roughly **$29.53M** (24h **+2.57%**, 7d **+4.29%**) — one of the stronger performers in its cohort despite the broad Extreme Fear backdrop (Fear & Greed 21; BTC ~$64,508).

---

## What ZeroBase Does

ZeroBase's core pitch is **real-time proving**: generating [[zero-knowledge-proof|ZK proofs]] fast enough to sit inside interactive workflows (login, staking, yield, settlement) rather than only in batch/rollup settings. By pairing ZK with TEEs, it aims to deliver privacy-preserving, cryptographically verifiable results that institutions can audit without revealing the underlying inputs.

The project markets a set of products built on this proving layer:

- **zkStaking** — staking with verifiable, privacy-aware accounting.
- **zkLogin** — privacy-preserving authentication.
- **ProofYield** — verifiable yield / real-world-asset strategy products aimed at institutional [[defi|DeFi]].

The unifying theme is compliance-aligned, privacy-preserving infrastructure where outputs are provably correct.

---

## Mechanism & Architecture

- **Real-time ZK proving network** — a decentralized set of provers generate proofs on demand with an emphasis on latency, so verifiable compute can be used interactively.
- **ZKP + TEE hybrid** — combines [[zero-knowledge-proof|zero-knowledge proofs]] with hardware trusted execution environments to balance performance, privacy, and verifiability.
- **Verifiable off-chain computation** — applications offload computation to the network and receive results plus proofs, consistent with the broader [[verifiable-compute]] paradigm.
- **Multi-chain deployment** — token contract `0xfab99fcf605fd8f4593edb70a43ba56542777777` is deployed on [[ethereum|Ethereum]], Base, and BNB Chain.

ZeroBase is associated with backing from YZi Labs (formerly Binance Labs) per its CoinGecko category tags.

### The proving / verification model, precisely

A [[zero-knowledge-proof|zero-knowledge proof]] lets a *prover* convince a *verifier* that a statement is true (e.g. "this computation, run on these private inputs, produced this output") while revealing nothing about the inputs themselves, and without the verifier re-running the work. Two properties make this useful: the proof is **succinct** (small and cheap to check, regardless of how heavy the original computation was) and **sound** (a cheating prover cannot fabricate a valid proof for a false statement). ZeroBase's contribution is on the *latency* axis of this pipeline — the slow step in practice is the prover's work of generating the proof, which for general computations can take seconds to minutes. By optimizing for **real-time proof generation** (and offloading parts of the trust/performance trade-off to TEEs), ZeroBase aims to make the prove → verify loop fast enough to sit inside an interactive user flow rather than a batch settlement job.

The **TEE hybrid** is the contentious design choice. A pure ZK proof rests on cryptographic hardness assumptions only; adding a trusted execution environment (a hardware enclave such as Intel SGX) lets the network run computation in an attested, isolated context and prove *about* that execution faster — but it imports a hardware trust assumption (and the history of TEE side-channel and microarchitectural attacks) that a purist ZK system avoids. The bet is that the latency win is worth the added trust surface for compliance-oriented institutional workloads.

---

## The ZBT Token

ZBT is the network token (circulating ≈ 245M of a 1B max supply; market-cap-to-FDV ratio ≈ 0.24, so roughly 75% of supply is not yet circulating — a notable unlock/emission overhang). It was distributed in part via a **Binance HODLer Airdrop** and surfaced through Binance Alpha / Binance Wallet IDO programs. In a proving network, the token typically serves to:

- **Pay for proving / compute** — fees for proof generation and verifiable-compute jobs.
- **Stake / secure** — collateral for provers and network operators.
- **Govern** — protocol parameters and treasury.

---

## Competitive Position

ZeroBase competes in the broader [[zero-knowledge-proof|ZK]] proving and [[verifiable-compute]] market, where the differentiator it claims is **proof latency** (real-time vs. batch). It overlaps with proving networks and coprocessors such as [[brevis|Brevis]], [[lagrange|Lagrange]], [[boundless|Boundless]], Succinct, and decentralized proving marketplaces, as well as privacy-focused infrastructure. The ZK-infrastructure space is well-funded and crowded; sustainable advantage depends on actually delivering low-latency proving at competitive cost and attracting real application demand rather than incentive-driven usage.

| Project | Primary primitive | Trust model | Differentiator vs. ZeroBase |
|---|---|---|---|
| **ZeroBase (ZBT)** | Real-time ZK proving network | ZK + TEE hybrid | Latency focus + TEE-assisted compliance products (zkStaking/zkLogin/ProofYield) |
| **[[lagrange\|Lagrange]] (LA)** | ZK coprocessor + prover network + zkML | Pure ZK, restaking-secured | Broader bundle (coprocessor, cross-chain state, zkML); operator-grade prover net |
| **[[boundless\|Boundless]] (ZKC)** | Universal proving marketplace (RISC Zero zkVM) | Pure ZK, PoVW staking | Chain-agnostic open marketplace; general zkVM lineage |
| **[[brevis\|Brevis]] (BREV)** | ZK coprocessor over historical data | Pure ZK + optimistic | History/cross-chain data queries for DeFi |
| **Succinct (SP1)** | General zkVM + prover network | Pure ZK | RISC-V zkVM, broad developer tooling |

The notable axis where ZeroBase diverges is its **TEE reliance** — a performance lever its pure-ZK rivals deliberately avoid.

---

## Narrative & Catalysts

ZeroBase rides the **ZK-infrastructure / verifiable-compute** narrative plus a **Binance-ecosystem** distribution angle (its category tags include Binance HODLer Airdrops, Binance Alpha Spotlight, and Binance Wallet IDO). Catalysts to watch: production traction for its real-time-proving claim (the differentiator stands or falls on shipped latency), adoption of zkStaking/ProofYield by real institutional [[defi|DeFi]] counterparties, and any further Binance-ecosystem listings/programs. Against it: the heavy emission overhang (only ~24% of supply circulating) means token-side catalysts can be swamped by unlock-driven selling.

---

## History & Timeline

- **2025-10-17** — ZBT all-time high of **$1.02** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-02-06** — All-time low of **$0.0583** during the bear market (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-22** — Trades ~$0.1203 (~90% below ATH), rank #646, market cap ~$29.5M; flagged in the daily on-chain snapshot as one of the top tokens in a **Bollinger-band volatility squeeze** (a compressed-volatility setup that often precedes an expansion move in either direction), and a relative outperformer (+2.57% 24h, +4.29% 7d) against the Extreme-Fear backdrop (cryptodataapi.com / CoinGecko; raw/data/crypto-loop/daily.json).

> Distribution via a Binance HODLer Airdrop and Binance Alpha / Wallet IDO programs is noted from category tags; no specific dated TGE source has been ingested, so an exact launch date is not asserted.

---

## Risks

- **Supply overhang** — only ~24% of tokens circulate; future unlocks can dilute.
- **Unproven real-time-proving claims** — low-latency ZK at scale is hard; marketing claims need verification against production usage.
- **TEE trust assumptions** — reliance on hardware enclaves introduces a trust/attack surface distinct from pure cryptography.
- **Smart-contract & cryptographic risk** — bugs in circuits, enclaves, or verifier contracts.
- **Microcap volatility** — rank #646, ~$29.5M cap; down ~90% from its 2025 ATH.
- **Crowded category** — many well-capitalized rivals.

*Not investment advice. ZK-infrastructure microcaps are highly speculative.*

---

## Trading Playbook (bear / Extreme-Fear regime)

> *Not investment advice. Context only, for the 2026-06-22 Established-Bear-Market regime (Fear & Greed 21).*

- **Regime read.** ZBT is a sub-$30M ZK-infra microcap; in a bear tape it is high-beta and prone to incentive-farming-driven volatility. Its relative outperformance (+4.29% 7d while the broad market is risk-off) is notable but typical of low-float names that move on thin volume.
- **Squeeze watch.** The 2026-06-22 daily snapshot flagged ZBT in a Bollinger-band volatility squeeze. Squeezes resolve into an expansion move but do not predict *direction* — in an Established Bear Market the base rate favors a downside break unless paired with a real catalyst.
- **Unlock discipline.** With only ~24% of supply circulating, the dominant medium-term overhang is emissions/unlocks; rallies into known unlock windows have historically faded across this cohort.
- **Sizing.** Thin liquidity means market orders move price; size down and use limits.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZBT |
| **Market Cap Rank** | #646 |
| **Market Cap** | $29,526,895 |
| **Current Price** | $0.1203 |
| **24h Change** | +2.57% |
| **7d Change** | +4.29% |
| **Categories** | Smart Contract Platform, Decentralized Finance (DeFi), BNB Chain Ecosystem, Ethereum Ecosystem, Zero Knowledge (ZK), Base Ecosystem, Proof of Stake (PoS), YZi Labs (Prev. Binance Labs) Portfolio, Binance HODLer Airdrops, Privacy Blockchain, Binance Alpha Spotlight, Binance Wallet IDO |
| **Website** | [https://zerobase.pro/](https://zerobase.pro/) |

---

## Overview

ZEROBASE is a decentralized cryptographic infrastructure network that enables verifiable off-chain computation using zero-knowledge proofs (ZKPs) and trusted execution environments (TEEs). 

It powers products like zkStaking, zkLogin, and ProofYield—bridging institutional DeFi, user privacy, and real-world asset strategies. 

ZEROBASE delivers programmable, compliance-aligned staking and transparent cryptographic assurance without exposing sensitive data.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 244.99M ZBT |
| **Total Supply** | 1.00B ZBT |
| **Max Supply** | 1.00B ZBT |
| **Fully Diluted Valuation** | $104.09M |
| **Market Cap / FDV Ratio** | 0.24 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.02 (2025-10-17) |
| **Current vs ATH** | -89.84% |
| **All-Time Low** | $0.0583 (2026-02-06) |
| **24h Change** (2026-06-22) | +2.57% |
| **7d Change** (2026-06-22) | +4.29% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xfab99fcf605fd8f4593edb70a43ba56542777777` |
| Base | `0xfab99fcf605fd8f4593edb70a43ba56542777777` |
| Binance Smart Chain | `0xfab99fcf605fd8f4593edb70a43ba56542777777` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZBT/USDT | N/A |
| Kraken | ZBT/USD | N/A |
| Upbit | ZBT/KRW | N/A |
| Bitget | ZBT/USDT | N/A |
| KuCoin | ZBT/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://zerobase.pro/](https://zerobase.pro/) |
| **Twitter** | [@zerobasezk](https://twitter.com/zerobasezk) |
| **Telegram** | [zerobasezk](https://t.me/zerobasezk) (22,363 members) |
| **Discord** | [https://discord.com/invite/zerobasezk](https://discord.com/invite/zerobasezk) |
| **GitHub** | [https://github.com/ZeroBase-Pro](https://github.com/ZeroBase-Pro) |
| **Whitepaper** | [https://zerobase.pro/docs/ZEROBASE_WhitePaper_EN.pdf](https://zerobase.pro/docs/ZEROBASE_WhitePaper_EN.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Market Cap Rank** | #646 |
| **Market Cap** | $29,526,895 |
| **Price** | $0.1203 |
| **24h Change** | +2.57% |
| **7d Change** | +4.29% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[zero-knowledge-proof]]
- [[verifiable-compute]]
- [[brevis]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific protocol source ingested yet.
