---
title: "Phala Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["PHA", "PHALA", "Phala"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://phala.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[polkadot]]", "[[smart-contracts]]", "[[trusted-execution-environment]]"]
---

# Phala Network

**Phala Network** (PHA) is a decentralized off-chain **confidential compute cloud** built on [[trusted-execution-environment|trusted execution environments]] (TEEs). It originated in the [[polkadot|Polkadot]] ecosystem (as a parachain) and provides a network of TEE-equipped worker nodes that run programs with hardware-enforced confidentiality and verifiable execution — effectively a decentralized, privacy-preserving alternative to centralized cloud compute. More recently Phala has positioned its TEE compute as an execution layer for **Web3 AI agents**. PHA is the network's staking, payment, and governance token. It ranks **#607** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* PHA trades at **$0.03917094**, market cap **$32,918,026** (rank **#607**), up **+4.53%** over 24h and **+7.04%** over 7 days, in a broad risk-off regime (BTC ~$64,166; Fear & Greed Index 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PHA |
| **Market Cap Rank** | #607 |
| **Market Cap** | $32,918,026 |
| **Current Price** | $0.03917094 |
| **24h Change** | +4.53% |
| **7d Change** | +7.04% |
| **Categories** | Confidential Compute (TEE), Infrastructure, DePIN, Polkadot Ecosystem, AI Agents, Artificial Intelligence (AI), Smart Contract Platform |
| **Website** | [https://phala.network/](https://phala.network/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Phala Network is a decentralized confidential-compute network: a distributed cloud of worker nodes equipped with [[trusted-execution-environment|TEE]] hardware (e.g., Intel SGX/TDX) that execute code with hardware-enforced confidentiality and attestable correctness. The core idea is to let developers run programs — smart-contract logic, oracles, off-chain workers, and more recently AI agents — where the operator cannot see or tamper with the data and where execution can be cryptographically attested.

The project began as a Polkadot parachain ([[polkadot]] ecosystem) and has expanded toward an "execution layer for Web3 AI," marketing TEE compute as a way to host tamper-proof AI agents that interact with [[smart-contracts]] across chains. (The AI-agent framing is the project's own positioning; the underlying primitive remains decentralized TEE compute.)

The maximum supply is 1 billion PHA, with the majority circulating. PHA trades on major centralized exchanges including Binance and Kraken, and on decentralized exchanges as a bridged ERC-20 on [[ethereum]].

---

## Architecture & Consensus

- **TEE worker network:** independent operators run TEE-enabled hardware; workloads execute inside enclaves so that inputs, code, and intermediate state are shielded from the host machine.
- **Remote attestation:** workers prove (via hardware attestation) that they are running the expected code inside a genuine enclave, giving users verifiable confidentiality and integrity.
- **Polkadot heritage:** Phala's consensus and security historically derived from being a Polkadot parachain (shared security from the relay chain), with a separate worker/compute layer (Phat Contracts / off-chain workers) on top.
- **Confidential compute, not a privacy coin:** unlike [[privacy-coins]] focused on hiding transactions, Phala's value proposition is private, verifiable *computation* — closer in spirit to [[secret|Secret Network]] (also TEE-based) but oriented toward general off-chain compute and DePIN.

### Phat Contracts and the compute model

Phala's developer-facing product evolved from on-chain "ink!"/WASM contracts to **Phat Contracts** — off-chain programs that run on the TEE worker fleet and can perform HTTP requests, heavy computation, and cross-chain calls that are impractical inside a normal [[smart-contracts|smart contract]] gas environment. A Phat Contract can act as a verifiable oracle, a serverless backend for a dApp, or an autonomous worker that signs and submits transactions to other chains. Because execution happens inside an enclave with [[trusted-execution-environment|remote attestation]], consumers get a cryptographic guarantee about *which code ran* on *which data* without the worker operator being able to read or alter it.

### Phala 2.0 / AI-agent pivot

From 2024 onward Phala rebranded much of its stack around **confidential AI**: hosting AI agents and model inference inside GPU-equipped TEEs (e.g., Intel TDX paired with confidential-GPU technology such as NVIDIA's H100 confidential computing). The thesis is that AI agents holding keys, secrets, or proprietary prompts need an execution environment that is *both* verifiable and private — something a normal cloud GPU cannot prove and a public blockchain cannot keep secret. Phala markets this as "verifiable AI" / "trustless agents," and integrates with agent frameworks rather than building a single end-user product. This is the project's own positioning; the underlying primitive remains decentralized, attestable TEE compute.

### Comparison with peer confidential-compute / privacy networks

| Project | Privacy primitive | Layer / base | Native focus | Token role |
|---|---|---|---|---|
| **Phala (PHA)** | TEE (Intel SGX/TDX, confidential GPU) | [[polkadot\|Polkadot]] heritage; ERC-20 on [[ethereum\|Ethereum]] | Decentralized confidential **compute** / AI agents (DePIN) | Staking, worker collateral, payment, governance |
| [[secret\|Secret Network (SCRT)]] | TEE (Intel SGX) | [[cosmos\|Cosmos]] [[layer-1\|L1]] | Privacy-preserving **smart contracts** (secret contracts) | Gas, staking, governance |
| [[coti\|COTI (COTI)]] | Garbled Circuits / MPC | Confidentiality layer secured by [[ethereum\|Ethereum]] | Confidential transactions & on-chain compute | Fees, staking, governance |
| Oasis (ROSE) | TEE (SGX) + ParaTimes | Standalone L1 | Confidential EVM (Sapphire) | Gas, staking, governance |
| Aleph Zero / Aztec | ZK + MPC / ZK rollup | L1 / [[layer-2\|L2]] | Cryptographic privacy (no hardware trust) | Gas, governance |

Phala's differentiator within this set is the **DePIN compute angle** — selling raw, attestable off-chain compute (now GPU/AI) rather than primarily privacy for transactions, and its trade-off is shared with [[secret|Secret]] and Oasis: it depends on TEE hardware-vendor trust (see [[#Risks]]) rather than pure cryptography.

---

## What the PHA Token Does

- **Staking / worker collateral:** node operators stake PHA to provide compute and earn rewards; staking aligns honest behavior.
- **Payment:** PHA is used to pay for confidential-compute resources on the network.
- **Governance:** PHA holders participate in protocol governance.

### Staking and value accrual

Historically Phala used a **delegated, worker-bound staking model**: each TEE worker (a "Gatekeeper"-secured StakePool / vault) required PHA collateral, and PHA holders could delegate to pools to share worker rewards while the staked PHA acted as slashable bond against worker misbehavior or downtime. Emissions were paid from a mining-reward budget that decays over time toward the 1B max supply. The intended value-accrual loop is: demand for confidential compute (and AI inference) → fees paid in / for PHA → larger reward pool and more workers staking PHA collateral → tighter circulating float. The key caveat is that this loop only tightens if **real paid compute demand** materializes; absent it, emissions are mostly recycled among stakers rather than backed by external revenue (see [[#Risks]]). Verify the current staking parameters and emission schedule against Phala's live documentation, as the AI-compute rearchitecture has changed worker economics.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 834.94M PHA |
| **Total Supply** | 1.00B PHA |
| **Max Supply** | 1.00B PHA |
| **Fully Diluted Valuation** | $35.62M |
| **Market Cap / FDV Ratio** | 0.83 |

A high MC/FDV (~0.83) means most of the fixed 1B supply is already circulating, so PHA carries **less future-unlock dilution overhang** than tokens like [[venom|VENOM]] or [[lisk|LSK]] in this peer set. Remaining issuance comes mainly from the decaying mining-reward budget rather than locked investor/team cliffs.

---

## Governance

PHA holders govern the protocol. With Phala's Polkadot/Substrate heritage, governance has used on-chain mechanisms (referenda, council/treasury, and OpenGov-style proposals on the Substrate side) to control protocol parameters, the treasury, worker-reward configuration, and major upgrades such as the move toward confidential GPU/AI compute. As the project bridges activity to [[ethereum|Ethereum]] and an AI-compute focus, governance increasingly concerns budget allocation for compute subsidies and ecosystem grants. As with most small-cap protocols, on-chain voter turnout is typically low and influence concentrates among large stakers and the core team/foundation.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.39 (2021-05-15) |
| **Current vs ATH** | -97.44% |
| **All-Time Low** | $0.0212 (2026-03-01) |
| **Current vs ATL** | +67.94% |
| **24h Change** | -4.90% |
| **7d Change** | -10.01% |
| **30d Change** | -0.30% |
| **1y Change** | -56.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6c5ba91642f10282b576d91922ae6448c9d52f4e` |
| Sora | `0x0033271716eec64234a5324506c4558de27b7c23c42f3e3b74801f98bdfeebf7` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PHA/USDT | N/A |
| Kraken | PHA/USD | N/A |
| Bitget | PHA/USDT | N/A |
| KuCoin | PHA/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X6C5BA91642F10282B576D91922AE6448C9D52F4E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X6C5BA91642F10282B576D91922AE6448C9D52F4E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://phala.network/](https://phala.network/) |
| **Twitter** | [@PhalaNetwork](https://twitter.com/PhalaNetwork) |
| **Discord** | [https://discord.com/invite/phala-network](https://discord.com/invite/phala-network) |
| **Whitepaper** | [https://files.phala.network/phala-paper.pdf](https://files.phala.network/phala-paper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.09M |
| **Market Cap Rank** | #671 |
| **24h Range** | $0.0355 — $0.0386 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **Origins (2018–2020):** Phala was founded around 2018 and ran a token-generation event in 2020, positioning itself as a confidential-compute project in the [[polkadot|Polkadot]] ecosystem.
- **Parachain era:** Phala (and its canary network Khala on Kusama) secured Polkadot/Kusama parachain slots via crowdloans, inheriting relay-chain shared security for its on-chain layer while running the TEE worker fleet off-chain.
- **2021 all-time high:** PHA reached **$1.39** on 2021-05-15 amid enthusiasm for Polkadot parachains and privacy/compute infrastructure; it has since fallen ~97% from that peak.
- **Phat Contracts launch:** Phala shipped Phat Contracts, generalizing the network from a privacy-compute niche into a serverless off-chain compute platform with HTTP/cross-chain access from inside TEEs.
- **AI-agent / confidential-GPU pivot (2024–2025):** since the 2023–2024 AI wave, Phala repositioned its TEE compute toward hosting decentralized/confidential AI agents and inference (confidential GPU computing, agent frameworks, and "verifiable AI"). This narrative has periodically supported renewed market interest.
- **2026 small-cap drawdown and recovery:** PHA printed an all-time low of **$0.0212** on 2026-03-01 during the small-cap washout, then recovered; as of 2026-06-22 it is up **+7.04% over 7 days** and **+4.53% on the day** versus a weak Extreme-Fear tape (BTC ~$64,166).

> *Notable events will continue to be added through the wiki's source ingestion workflow.*

---

## Risks

- **Hardware-trust dependency:** confidentiality and integrity rely on TEE hardware (Intel SGX/TDX, confidential GPUs). Disclosed enclave side-channel vulnerabilities (an industry-wide pattern) could weaken guarantees until mitigated — the same structural risk faced by [[secret|Secret Network]] and Oasis. This is a *trust-the-vendor* model, unlike pure-cryptography approaches such as ZK/MPC.
- **Demand / revenue risk:** the staking-and-emissions loop only accrues value if external paying compute demand exists. If AI/DePIN compute usage does not materialize, rewards are largely recycled inflation rather than fee-backed.
- **Narrative dependence:** PHA's valuation is sensitive to the AI-agent / DePIN narrative; price can move sharply with sentiment cycles independent of fundamentals.
- **Polkadot-ecosystem exposure:** the on-chain layer historically depends on relay-chain security and the health of the broader Polkadot/Kusama ecosystem; a bridged ERC-20 on [[ethereum|Ethereum]] adds bridge surface for cross-chain holders.
- **Competition:** confidential compute is contested by [[secret|Secret]], Oasis, [[coti|COTI]], and ZK-based privacy chains; Phala must win on price/performance of *verifiable* compute.
- **Small-cap volatility & drawdown:** at ~$33M market cap (rank #607) and down ~97% from ATH, PHA is volatile and thinly traded; large orders can move price materially.

> Not investment advice. Figures are point-in-time; verify project, on-chain, and TEE-security claims independently.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[trusted-execution-environment]]
- [[polkadot]]
- [[secret]]
- [[coti]]
- [[privacy-coins]]
- [[smart-contracts]]
- [[ai-trading]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); BTC ~$64,166, Fear & Greed 21 / Extreme Fear.
- General market knowledge; no additional specific wiki source ingested yet.
