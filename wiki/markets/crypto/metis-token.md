---
title: "Metis"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ethereum]
aliases: ["METIS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.metis.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[optimistic-rollup]]", "[[sequencer]]", "[[data-availability]]", "[[smart-contracts]]", "[[staking]]", "[[airdrop]]"]
---

# Metis

**Metis** (METIS) is an [[ethereum]] [[layer-2]] scaling network built as an **[[optimistic-rollup]]**. Its distinguishing feature is a **decentralized [[sequencer]]** model — where many rollups rely on a single operator to order transactions, Metis pursues a multi-operator (DSEQ) sequencer set — and an evolving dual-network design (Andromeda + Hyperion). As of 2026-06-22 METIS trades at **$3.19**, ranked **#745** by market capitalization (mcap **$23,921,786**), down **0.82%** on the day but up **8.14%** over the trailing week, an outperformer within an otherwise broad crypto bear regime (Crypto Fear & Greed Index at 21 — "Extreme Fear").

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Crypto Fear & Greed Index: 21 (Extreme Fear).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | METIS |
| **Market Cap Rank** | #745 |
| **Market Cap** | $23,921,786 |
| **Current Price** | $3.19 |
| **24h Change** | -0.82% |
| **7d Change** | +8.14% |
| **Architecture** | Ethereum L2 — optimistic rollup (decentralized sequencer / DSEQ) |
| **Categories** | Smart Contract Platform, Layer 2 (L2), Rollup |
| **Website** | [https://www.metis.io/](https://www.metis.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Metis is an [[ethereum]] [[layer-2]] network that scales Ethereum using an **[[optimistic-rollup]]** design: transactions are executed off-chain on Metis and their data is committed back to Ethereum, which provides settlement security via fraud proofs. Metis has positioned itself as more than a single rollup, describing a multi-network architecture with two complementary chains:

- **Andromeda** — the foundational, general-purpose [[optimistic-rollup]] network, optimized for DeFi, gaming, and broad dApp deployment, emphasizing decentralization (via its DSEQ sequencer nodes) and proven security over peak performance.
- **Hyperion** — a higher-performance, AI-oriented network intended for parallel execution and AI/DePIN/gaming workloads, while keeping Ethereum-anchored security and **METIS as the gas token**.

The **METIS** token is the network's [[smart-contracts|gas]] / fee token across these chains, is used to collateralize and reward sequencer operators, and participates in governance. Metis notably has a small fixed supply (max 10M METIS), which gives it a much higher unit price than most long-tail tokens.

---

## Architecture: decentralized sequencer

The headline technical differentiator for Metis is its **decentralized sequencer (DSEQ)**. In a typical [[optimistic-rollup]], a single sequencer controlled by the rollup operator orders and batches transactions, which is a centralization and censorship risk and a single point of failure. Metis instead runs a set of sequencer operators that take turns ordering transactions and must stake/lock collateral, with the [[staking]] and rotation logic enforced on-chain. This is intended to reduce reliance on any single party and to bring rollup security properties closer to the decentralized ideal that optimistic rollups target.

Like other optimistic rollups, Metis depends on a challenge/fraud-proof window for security: state transitions are assumed valid unless challenged, so withdrawals back to [[ethereum]] L1 incur the standard rollup delay, and the security model assumes at least one honest party will submit a fraud proof when needed. Metis has published a roadmap toward standard rollup "stage" milestones (e.g., on-chain data availability and fraud-proof refinements).

### Rollup stack: settlement, data availability, execution

| Layer | Metis approach |
|---|---|
| **Settlement** | [[ethereum]] L1 — fraud-proof / dispute resolution and final state commitment posted to Ethereum smart contracts |
| **Data availability** | Historically used off-chain DA (MEMO / committee-style) for cost reduction; roadmap moves toward Ethereum-anchored / [[eip-4844\|EIP-4844 blob]]-style on-chain DA for stronger rollup guarantees. Off-chain DA weakens the trust model versus a "true" rollup until on-chain DA is adopted. |
| **Execution** | EVM-compatible off-chain execution on Andromeda (general purpose) and Hyperion (high-performance / parallelized, AI-oriented) |
| **Sequencing** | **Decentralized sequencer (DSEQ)** — a rotating, staked, multi-operator sequencer set rather than a single project-controlled operator |
| **Gas token** | **METIS** (unusual — most Ethereum L2s, including Base, Arbitrum, and Optimism, denominate gas in ETH) |

A notable design choice is that Metis uses **METIS itself as the gas token**, unlike the ETH-gas convention of [[optimism]], [[arbitrum]], and [[base]]. This creates organic, usage-driven sink demand for METIS but adds UX friction (users must hold METIS to transact) and ties fee revenue to the token rather than to ETH.

### Decentralized sequencer vs peers

The DSEQ model is Metis's principal claim to differentiation. The Ethereum L2 landscape in 2024-2026 was overwhelmingly served by **single, project-operated sequencers** ([[optimism]], [[arbitrum]], [[base]], [[blast]], [[zksync]] all launched with centralized sequencing), which concentrates censorship power, MEV capture, and a liveness single-point-of-failure in one operator. Metis's rotating staked sequencer set is intended to be one of the earlier production attempts at sequencer decentralization, though the real-world distribution of operators and stake should be verified rather than assumed.

---

## Comparison vs peer Layer-2 networks

| Network | Proof system | Sequencing | Gas token | Distinctive feature |
|---|---|---|---|---|
| **Metis** | [[optimistic-rollup\|Optimistic]] (fraud proofs) | **Decentralized (DSEQ)** | **METIS** | Decentralized sequencer; dual-chain (Andromeda + Hyperion AI) |
| [[optimism\|Optimism]] | Optimistic | Centralized (Superchain) | ETH | OP Stack, Superchain ecosystem |
| [[arbitrum\|Arbitrum]] | Optimistic (interactive fraud proofs) | Centralized | ETH | Largest L2 TVL; Nitro / Stylus |
| [[base\|Base]] | Optimistic (OP Stack) | Centralized | ETH | Coinbase distribution; no native token |
| [[blast\|Blast]] | Optimistic | Centralized | ETH | Native yield on bridged ETH/stables |
| [[taiko\|Taiko]] | [[zk-rollup\|ZK]] (Type-1 [[zkevm]]) | Based (L1 proposers) | ETH | Ethereum-equivalent based rollup |

Metis's optimistic design shares the long (~7-day) withdrawal challenge window common to fraud-proof rollups, in contrast to ZK rollups like [[taiko]] that achieve faster cryptographic finality via validity proofs.

---

## Governance

METIS is a governance token: holders and sequencer operators participate in protocol decisions, parameter changes, and ecosystem fund allocation. Metis has historically used a community-treasury / DAC ("Decentralized Autonomous Company") framework and on-chain mechanisms to direct ecosystem incentives. Sequencer operators must [[staking|stake]] METIS to participate, aligning the validator set's economic interest with network security, and a portion of sequencer rewards is distributed to stakers.

---

## Ecosystem & Adoption

Metis hosts a DeFi-centric ecosystem (DEXes, lending, yield) alongside gaming and, more recently, AI/DePIN-themed projects targeting the Hyperion network. Its decentralized-sequencer story and fixed, low token supply have been recurring talking points. The 18.42% weekly gain into 2026-06-21, against a falling broad market, suggests token-specific catalysts or speculative rotation rather than a market-wide move. METIS remains far below its 2022 all-time high (~$323), reflecting the broad de-rating of L2 governance/gas tokens.

---

## Risks

- **Optimistic-rollup security assumptions** — long withdrawal/challenge windows and dependence on honest fraud-proof submitters are inherent to the design; rollup "stage" maturity is still in progress.
- **Intense L2 competition** — Metis competes with much larger Ethereum L2s (Arbitrum, Optimism, Base, zkSync, etc.) for users, liquidity, and developers; mindshare and TVL are comparatively small.
- **Sequencer decentralization in practice** — DSEQ reduces but does not eliminate operator/governance concentration; the degree of real-world decentralization should be verified, not assumed.
- **Low liquidity & volatility** — a sub-$25M market cap and rank in the #700s mean thin order books; the large single-week swing illustrates elevated volatility.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 7.33M METIS |
| **Total Supply** | 10.00M METIS |
| **Max Supply** | 10.00M METIS |
| **Fully Diluted Valuation** | $29.06M |
| **Market Cap / FDV Ratio** | 0.73 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $323.54 (2022-01-16) |
| **Current vs ATH** | -99.10% |
| **All-Time Low** | $2.73 (2026-04-05) |
| **Current vs ATL** | +6.59% |
| **24h Change** | -4.34% |
| **7d Change** | -0.01% |
| **30d Change** | -7.39% |
| **1y Change** | -76.97% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x9e32b13ce7f2e80a01932b42553652e053d6ed8e` |
| Metis Andromeda | `0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | METIS/USDT | N/A |
| Kraken | METIS/USD | N/A |
| Bitget | METIS/USDT | N/A |
| KuCoin | METIS/USDT | N/A |
| Crypto.com Exchange | METIS/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X9E32B13CE7F2E80A01932B42553652E053D6ED8E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Sushiswap | 0X9E32B13CE7F2E80A01932B42553652E053D6ED8E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.metis.io/](https://www.metis.io/) |
| **Twitter** | [@MetisL2](https://twitter.com/MetisL2) |
| **Telegram** | [MetisL2](https://t.me/MetisL2) (17,944 members) |
| **GitHub** | [https://github.com/MetisProtoco](https://github.com/MetisProtoco) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.20M (2026-04-09 snapshot) |
| **Market Cap Rank** | #745 |
| **Price (2026-06-22)** | $3.19 |
| **24h Change (2026-06-22)** | -0.82% |
| **7d Change (2026-06-22)** | +8.14% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Notable Events

- **2021** — Metis launched its Andromeda mainnet as one of the earlier optimistic-rollup L2s, evolving from a "Decentralized Autonomous Company" (DAC) framework.
- **2022-01** — METIS reached its all-time high of ~$323.54 during the late-2021/early-2022 crypto peak, before the broad L2-token de-rating.
- **2023-2024** — Rolled out the decentralized sequencer (DSEQ) program, moving from a single operator toward a rotating, staked multi-operator set — an early production attempt at sequencer decentralization.
- **2024-2025** — Announced and developed **Hyperion**, an AI/DePIN-oriented high-performance network intended for parallel execution while keeping Ethereum-anchored security and METIS gas.
- **2026** — METIS set an all-time low of $2.73 (2026-04-05) amid the broad bear regime, then recovered modestly; trading $3.19 as of 2026-06-22.

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[optimistic-rollup]]
- [[sequencer]]
- [[data-availability]]
- [[smart-contracts]]
- [[staking]]
- [[airdrop]]
- [[arbitrum]]
- [[optimism]]
- [[base]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market data snapshot
- General market knowledge; no other specific wiki source ingested yet. Market figures dated 2026-06-22 are from cryptodataapi.com / CoinGecko (Crypto Fear & Greed Index: 21, Extreme Fear).
