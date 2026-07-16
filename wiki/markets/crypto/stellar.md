---
title: "Stellar"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi]
aliases: ["Stellar Lumens", "XLM"]
entity_type: protocol
founded: 2014
headquarters: "Decentralized (Stellar Development Foundation, San Francisco)"
website: "https://www.stellar.org/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[hyperliquid]]", "[[narrative-trading]]", "[[ripple]]", "[[stablecoins]]", "[[treasuries]]"]
---

# Stellar

**Stellar** (XLM) is an open-source payments-and-tokenization Layer 1 co-founded in 2014 by Jed McCaleb (also a [[ripple|Ripple]] co-founder) and Joyce Kim, optimized for fast, sub-cent transfers and fiat on/off-ramps via "Anchors." For traders it sits in the payments + real-world-asset basket: PayPal's PYUSD expansion to Stellar and Franklin Templeton's tokenized [[treasuries|Treasury]] fund made it one of the most institutionally-validated mid-cap L1s of 2025–2026.

---

## Market Data

| Metric | Value |
|---|---|
| **Price** | $0.215803 |
| **Market Cap** | $7,296,951,174 (~$7.30B) |
| **Market Cap Rank** | #16 |
| **24h Volume** | $289,352,374 (~$289.4M) |
| **24h Change** | −1.80% |
| **7d Change** | **+13.53%** (relative strength vs market) |
| **Circulating Supply** | 33,805,971,668 XLM (~33.81B) |
| **Total Supply** | 50,001,786,840 XLM (~50.00B) |
| **Max Supply** | None — issuance disabled (effectively capped ~50B) |
| **Market Cap / FDV** | ~0.68 (33.81B circ / 50.00B total) |
| **All-Time High** | $0.875563 (2018-01-03) — **−75.35%** from ATH |
| **All-Time Low** | $0.00047612 (2015-03-05) — **+45,228%** from ATL |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** Crypto Fear & Greed Index = **22 (extreme fear)**; the market is in an **Established Bear Market**. Notably, XLM is **+13.5% on the week** while most majors bled — a payments/RWA-narrative relative-strength tell worth flagging (see [[narrative-trading]]).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XLM |
| **Market Cap Rank** | **#16** (2026-06-20, ~$7.30B); was ~#22 at the April 2026 snapshot (~$5.2B) |
| **Price** | **$0.215803** (2026-06-20); $0.157 at April 2026 snapshot; 2025 high ~$0.47+ |
| **Chain / Sector** | Own Layer 1 ([[proof-of-work\|non-PoW]] — Stellar Consensus Protocol / Federated Byzantine Agreement); payments, [[stablecoins]], RWA tokenization |
| **Smart Contracts** | Soroban (Rust-based), live since 2024; Protocol 23 added parallel execution (late 2025) |
| **Supply Mechanics** | 50B total / ~33B circulating; no inflation (community disabled issuance 2019); rest held by SDF |
| **Founded** | 2014 (Jed McCaleb, Joyce Kim; early funding from Stripe) |
| **Website** | [https://www.stellar.org/](https://www.stellar.org/) |

---

## Overview

Stellar is an open-source, decentralized network co-founded in 2014 by Jed McCaleb and Joyce Kim to facilitate the fast and low-cost transfer of value across different currencies and assets globally. Managed by the non-profit Stellar Development Foundation, the project serves as a global infrastructure that connects banks, payment systems, and individuals to expand financial access to underserved populations. Its main value proposition lies in providing a bridge between traditional money and digital networks through the use of Anchors, which are trusted entities that hold deposits and issue credits on the ledger.

The network operates using the Stellar Consensus Protocol and a Federated Byzantine Agreement, where nodes choose trusted sets of other nodes to agree on the state of the ledger. This system ensures high throughput and fast finality, where transactions are considered permanent and irreversible within seconds. Key features include a built-in distributed exchange for trading assets without intermediaries and the Soroban platform for developing smart contracts. Users can also utilize the network for tokenizing real-world assets or accessing decentralized finance services like peer-to-peer lending.

Stellar's native token, XLM, is essential for maintaining network integrity by acting as an intermediary to find efficient exchange paths and preventing spam through small transaction fees and minimum account balance requirements. Unlike many other digital assets, the network has no inflation because the community voted to disable the automatic creation of new tokens. While the project received early funding from the payments company Stripe, it is now sustained by a global community of validators and developers rather than traditional venture capital.

---

## Technology & Consensus

Stellar does **not** use [[proof-of-work]] or classical proof-of-stake. It runs the **Stellar Consensus Protocol (SCP)**, an instantiation of **Federated Byzantine Agreement (FBA)**. The key idea is *quorum slices*: each node independently chooses which other nodes it trusts, and global consensus emerges from the overlap of these individually-chosen trust sets. This contrasts sharply with PoW (energy-secured, miner-driven) and with the closed validator set of [[ripple|XRP Ledger]] — there is no mining, no staking yield, and no fixed validator list.

| Property | Stellar (SCP / FBA) |
|---|---|
| **Consensus** | Stellar Consensus Protocol — Federated Byzantine Agreement (quorum slices) |
| **Security model** | Trust-based: nodes pick trusted quorum sets; safety preferred over liveness |
| **Block / ledger close time** | ~5 seconds, deterministic finality (no probabilistic confirmations) |
| **Throughput** | Thousands of ops/sec; Protocol 23 added **parallel execution** for Soroban |
| **Energy** | Negligible (no mining) |
| **Smart contracts** | **Soroban** (Rust/WASM), live since 2024 |
| **Native fee** | ~0.00001 XLM base fee per operation (anti-spam, not a yield source) |

Three pillars define the network's design:

- **Anchors** — trusted entities (banks, fintechs, money-service businesses) that hold fiat deposits and issue 1:1 redeemable credits (tokens) on-ledger, providing the fiat on/off-ramps that make Stellar a payments rail. The anchor network spans **170+ countries**.
- **Built-in DEX** — a native on-ledger order book and path-payment engine that automatically routes a payment through the cheapest sequence of asset conversions (e.g., USD → XLM → EUR) without external smart contracts.
- **Soroban** — the Rust-based smart-contract platform (live 2024). **Protocol 23** (late 2025) added parallel transaction processing, materially lifting throughput for tokenization and DeFi workloads.

---

## 2025–2026 Developments

- **PayPal PYUSD on Stellar (announced June 2025)** — PayPal announced PYUSD issuance on Stellar (pending NYDFS approval), targeting payments distribution across 170+ countries via Stellar's anchor network. The announcement helped drive XLM's ~100% surge in July 2025 to above $0.47.
- **Protocol 23 (activated late 2025)** — major upgrade adding parallel transaction processing for Soroban smart contracts, lifting throughput for tokenization workloads.
- **RWA tokenization traction** — Franklin Templeton's on-chain money fund (BENJI) holds **~$445M of tokenized US Treasuries on Stellar**; total tokenized RWAs on-chain ~$515M+ (2025). Société Générale-FORGE's EURCV stablecoin and Circle's USDC are live on the network. Mercado Bitcoin (LatAm's largest digital-asset platform) announced plans for **$200M** of tokenized fixed-income/equity instruments on Stellar.
- XLM subsequently retraced with the broader alt market — April 2026 snapshot $0.157, -82% from its 2018 ATH of $0.876.

---

## Ecosystem & Use Cases

Stellar's thesis is "blockchain rails for regulated money movement." Its traction is concentrated in three use cases:

| Use case | Detail |
|---|---|
| **Cross-border payments / remittances** | Sub-cent fees, ~5s finality, path-payment routing; anchor network across **170+ countries** for fiat in/out. |
| **Stablecoins** | A primary distribution rail — see [[stablecoins]]: **Circle USDC**, **Société Générale-FORGE EURCV**, and **PayPal PYUSD** (announced for Stellar June 2025, pending NYDFS) issued on-ledger. |
| **RWA tokenization** | **Franklin Templeton's** on-chain money fund **BENJI** holds **~$445M of tokenized US [[treasuries]] on Stellar**; total tokenized RWAs on Stellar ~$515M+ (2025). **Mercado Bitcoin** (LatAm's largest digital-asset platform) announced **$200M** of tokenized fixed-income/equity instruments on Stellar. |

The economic catch for traders: this institutional usage validates the *network*, but XLM's by-design negligible fees mean usage does **not** mechanically accrue value to the token (see Risks).

---

## Market Structure & Derivatives

| Channel | Detail |
|---|---|
| **Spot venues** | Deep books on [[binance\|Binance]], [[kraken\|Kraken]], Bitget, KuCoin, Crypto.com; plus the native on-ledger DEX. |
| **Perps** | **XLM-PERP on [[hyperliquid]]** and all major derivatives venues — funding/open-interest are the cleanest real-time positioning signal (no CME XLM future). |
| **Index inclusion** | GMCI 30 and **Coinbase 50** indices; part of the "Made in USA" basket — relevant for US-regulatory-tailwind rotation trades. |
| **Structural supply** | The **SDF non-circulating holding (~16B XLM)** is the dominant overhang; disbursement cadence is the supply variable to monitor. |

The April 2026 snapshot 24h volume was ~$102M; the 2026-06-20 snapshot shows **~$289.4M**, a meaningful liquidity pickup consistent with the +13.5% weekly relative strength.

---

## Trading Playbook

- **Narrative baskets**: the payments/remittance basket (with [[ripple]] XRP — XLM and XRP are highly correlated, sharing a co-founder and use case; **XLM typically follows XRP moves with a lag and higher beta**) and the RWA/tokenization basket (Franklin Templeton, [[treasuries]]). See [[narrative-trading]].
- **Relative-strength tell**: XLM's +13.5% week into a Fear & Greed = 22 tape is the kind of payments/RWA-narrative leadership that flags rotation; pair-trade vs [[ripple]] XRP or vs [[bitcoin]] to isolate the idiosyncratic move.
- **Catalysts**: NYDFS approval/go-live of **PYUSD on Stellar**, new RWA issuers, Soroban DeFi TVL growth, and the **SDF disbursement schedule** (the ~16B XLM non-circulating SDF holding is the structural supply overhang).
- **Where it trades**: deep spot on [[binance|Binance]], [[kraken|Kraken]], Bitget, KuCoin, Crypto.com; **XLM-PERP on [[hyperliquid]]**; GMCI 30 / Coinbase 50 constituent.

---

## Tokenomics & Supply

> *Current figures 2026-06-20; structural notes are evergreen.*

| Metric | Value |
|---|---|
| **Circulating Supply** | ~33.81B XLM |
| **Total Supply** | ~50.00B XLM |
| **Max Supply** | None — inflation disabled by **2019 community vote**; effectively capped at ~50B |
| **Market Cap** | ~$7.30B |
| **Market Cap / FDV Ratio** | ~0.68 (33.81B circulating / 50.00B total) |

**Supply mechanics:**

- The network's original 1%/yr inflation was **switched off by community vote in 2019** — no new XLM is created.
- The **Stellar Development Foundation (SDF)** holds the bulk of the non-circulating ~16B XLM. Its disbursement cadence is the single most important supply factor and the reason MC/FDV sits below 1.0.
- Per-operation fees (~0.00001 XLM) and a **minimum account balance** exist purely as anti-spam mechanisms, not as a value-capture or yield mechanism.

---

## Price History

> *Current figures 2026-06-20; ATH/ATL anchors are evergreen.*

| Metric | Value |
|---|---|
| **All-Time High** | $0.875563 (2018-01-03) |
| **Current vs ATH** | **−75.35%** |
| **All-Time Low** | $0.00047612 (2015-03-05) |
| **Current vs ATL** | **+45,228%** |
| **24h Change** | −1.80% |
| **7d Change** | **+13.53%** |

*(April 2026 snapshot, historical: $0.157, rank ~#22, −82% from ATH.)*

---

## Platform & Chain Information

**Native Chain:** Stellar

### Contract Addresses

| Chain | Address |
|---|---|
| Stellar | `CAS3J7GYLGXMF6TDJBBYYSE3HQ6BBSMLNUQ34T6TZMYMW2EVH34XOWMA` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | XLM/USDT | N/A |
| Kraken | XLM/USD | N/A |
| Bitget | XLM/USDT | N/A |
| KuCoin | XLM/USDT | N/A |
| Crypto.com Exchange | XLM/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | XLM-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.stellar.org/](https://www.stellar.org/) |
| **Twitter** | [@stellarorg](https://twitter.com/stellarorg) |
| **Reddit** | [https://www.reddit.com/r/stellar](https://www.reddit.com/r/stellar) |
| **GitHub** | [https://github.com/stellar/stellar-core](https://github.com/stellar/stellar-core) |
| **Whitepaper** | [https://8130068.fs1.hubspotusercontent-na1.net/hubfs/8130068/stellar-consensus-protocol.pdf](https://8130068.fs1.hubspotusercontent-na1.net/hubfs/8130068/stellar-consensus-protocol.pdf) |

---

## Developer Activity

> *Snapshot 2026-04-09.*

| Metric | Value |
|---|---|
| **GitHub Stars** | 3,118 |
| **GitHub Forks** | 969 |
| **Commits (4 weeks)** | 86 |
| **Pull Requests Merged** | 1,777 |
| **Contributors** | 84 |

---

## Trading Characteristics

> *Current 2026-06-20; CoinGecko sentiment from the 2026-04-09 snapshot.*

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$289.4M |
| **Market Cap Rank** | #16 |
| **CoinGecko Sentiment** | 83% positive (2026-04-09 snapshot) |
| **Last Updated** | 2026-06-20 |

*(April 2026 snapshot, historical: 24h volume $102.10M, rank #22, 24h range $0.1565–$0.1649.)*

---

## Whale & Holder Information

> *Largest non-circulating holder is the Stellar Development Foundation (~17B XLM) — its disbursement cadence is the main structural supply factor to monitor.*

---

## History & Cycles

| Date | Event |
|---|---|
| **2014** | Stellar founded by **Jed McCaleb** (also a [[ripple\|Ripple]] co-founder) and **Joyce Kim**; early funding from **Stripe**. Stellar Development Foundation (SDF) stewards the protocol. |
| **2015** | All-time low $0.00047612 (2015-03-05). |
| **2018-01-03** | All-time high **$0.875563** during the 2017–18 bull mania. |
| **2019** | Community vote **disables inflation** — no new XLM created thereafter. SDF also burned ~half its holdings that year. |
| **2024** | **Soroban** (Rust smart contracts) goes live, opening DeFi/RWA workloads. |
| **2025-06** | PayPal announces **PYUSD on Stellar** (pending NYDFS approval). |
| **2025-07** | XLM surges ~100% to **>$0.47** on PYUSD + Protocol 23 momentum. |
| **2025 (late)** | **Protocol 23** activates: parallel smart-contract execution. |
| **2025** | Franklin Templeton **~$445M tokenized [[treasuries]]** (BENJI) on Stellar; Mercado Bitcoin announces $200M tokenization plan; SocGen-FORGE EURCV live. |
| **2026-04** | Snapshot $0.157, rank ~#22 — retraced with the broader alt market. |
| **2026-06-20** | $0.215803, rank **#16**, **+13.5% on the week** despite Fear & Greed = 22 (extreme fear). |

---

## Competitive Positioning

Stellar's closest comparable is [[ripple|XRP Ledger]] — same founder (Jed McCaleb), overlapping cross-border-payments use case, and high price correlation. The two diverge on consensus model, supply, and go-to-market:

| Dimension | **Stellar (XLM)** | **[[ripple\|XRP Ledger (XRP)]]** |
|---|---|---|
| **Consensus** | Stellar Consensus Protocol (FBA, open quorum slices) | XRP Ledger Consensus (closed/curated validator UNL) |
| **Primary use case** | Payments + stablecoin rails + RWA tokenization | Cross-border payments / on-demand liquidity (ODL) |
| **Supply** | ~50B total, inflation disabled; SDF holds ~16B | 100B fixed; large escrow released on schedule |
| **Institutional partners** | PayPal (PYUSD), Circle (USDC), Franklin Templeton, SocGen-FORGE | RippleNet banks, RLUSD stablecoin |
| **Niche / steward** | Non-profit SDF; financial-inclusion + RWA angle | For-profit Ripple Labs; bank-settlement angle |

Against the broader **payments-stablecoin L1** field, Stellar competes with faster general-purpose chains (Solana, Tron, Ethereum L2s) that increasingly host the same stablecoins; its edge is the regulated **anchor network** and deep institutional RWA relationships rather than raw throughput.

---

## Risks

- **Value-accrual gap**: institutional usage validates the network but does **not** mechanically accrue to XLM — fees are negligible by design, so XLM is closer to a "gas + reserve + speculative" asset than a fee-capturing token.
- **Payments-chain competition**: [[ripple|XRP Ledger]], plus stablecoins migrating to faster/cheaper L1s and L2s, can erode Stellar's rail advantage.
- **SDF supply overhang**: the ~16B non-circulating XLM controlled by the SDF is a structural sell-side variable; disbursement decisions can pressure price.
- **Narrative dependence**: in an Established Bear Market (Fear & Greed = 22), even relative-strength names can reverse hard on broad de-risking; XLM's beta to [[bitcoin]] and to [[ripple]] remains high.

---

## Related

- [[crypto-markets]]
- [[ripple]] — closest comparable (shared co-founder, payments use case, high correlation)
- [[bitcoin]]
- [[proof-of-work]] — contrast: Stellar uses SCP/FBA, not mining
- [[stablecoins]] — PYUSD, USDC, EURCV distribution rails
- [[treasuries]] — Franklin Templeton tokenized Treasury fund
- [[hyperliquid]] — XLM perp venue
- [[narrative-trading]] — payments and RWA baskets

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- AInvest — "Stellar (XLM) at a Pivotal Moment: Institutional Adoption and PYUSD Integration" (Sep 2025): https://www.ainvest.com/news/stellar-xlm-pivotal-moment-assessing-institutional-adoption-pyusd-integration-catalysts-price-breakout-2509/
- AInvest — "XLM's 100% Surge and PayPal's Stablecoin Move" (Jul 2025): https://www.ainvest.com/news/xlm-100-surge-paypal-stablecoin-move-era-stellar-2507/
- Blockchain.News — "Stellar (XLM) Surges Amid Protocol 23 Upgrade and Major Partnerships" (2025-07-18): https://blockchain.news/news/20250718-stellar-xlm-surges-amid-protocol-23-upgrade-and-major-partnerships-whats-next
- CCN — "Meet Stellar: How XLM Is Quietly Driving Global Payments": https://www.ccn.com/education/crypto/meet-stellar-xlm-global-payments/
- Verified via Perplexity sonar + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 34.19B XLM |
| **Total Supply** | 50.00B XLM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $9.44B |
| **Market Cap / FDV Ratio** | 0.68 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
