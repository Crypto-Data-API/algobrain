---
title: "IoTeX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["IOTX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://iotex.io"
related: ["[[consensus-mechanism]]", "[[crypto-markets]]", "[[depin]]", "[[ethereum]]", "[[harmony]]", "[[layer-1]]", "[[layer-2]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[staking]]"]
---

# IoTeX

**IoTeX** (IOTX) is an EVM-compatible [[layer-1]] blockchain focused on **[[depin|DePIN]]** (Decentralized Physical Infrastructure Networks) — connecting real-world devices, sensors, and machines to on-chain applications. Live since 2017, IoTeX provides identity, data, and verification layers that let physical hardware feed trusted data into [[smart-contracts]], increasingly framed by the project as infrastructure for "real-world AI." As of 2026-06-22 IOTX trades at **$0.00316585**, ranked **#645** by market capitalization (mcap **$29,895,463**), down **0.50%** on the day and down **7.14%** over the trailing week within a broad crypto bear regime (BTC bear market; Fear & Greed Index 21 / Extreme Fear).

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | IOTX |
| **Market Cap Rank** | #645 |
| **Market Cap** | $29,895,463 |
| **Current Price** | $0.00316585 |
| **24h Change** | -0.50% |
| **7d Change** | -7.14% |
| **Categories** | Artificial Intelligence (AI), Internet of Things (IOT), Ethereum Ecosystem, DePIN, Base Ecosystem, Account Abstraction, AI Agents, GMCI DePIN Index, GMCI Index, Made in USA, Robotics, Base Native |
| **Website** | [https://iotex.io](https://iotex.io) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

IoTeX is an EVM-compatible [[layer-1]] focused on connecting the physical world to blockchains — the category now widely called **[[depin|DePIN]]** (Decentralized Physical Infrastructure Networks). Live since 2017, IoTeX provides the data, identity, and verification layers that let real-world devices and sensors deliver trusted, verifiable data to [[smart-contracts]] and, increasingly, to AI systems. The project markets adoption across mobility, robotics, energy, and health, and frames itself as infrastructure for "real-world AI" where physical machines act as trustworthy data sources.

A distinguishing piece of IoTeX's stack is its emphasis on **device identity and trusted hardware**: rather than treating IoT data as unverified inputs, IoTeX aims to anchor device identity and data provenance on-chain so that applications can rely on the data's authenticity. The native **IOTX** token is used to pay [[smart-contracts|gas]] fees, to [[staking|stake]] for and vote on delegates that secure the network, and for governance.

---

## Architecture & Consensus

IoTeX runs a **Roll-DPoS** ([[proof-of-stake]]) [[consensus-mechanism]] — a delegated, committee-rotating variant of delegated proof-of-stake. Token holders [[staking|stake]] and vote for delegates; a rotating subset of elected delegates produces blocks, which the project pairs with EVM compatibility so existing [[ethereum]] tooling and Solidity contracts can be reused. IoTeX has also expanded its presence onto other ecosystems (it is listed with a [[layer-2]]-adjacent Base deployment), broadening where IOTX-denominated applications can run.

On top of the base chain, IoTeX has built DePIN-specific middleware — modules for connecting devices, attesting to off-chain computation/data, and rewarding hardware operators — which is the layer most relevant to its target use cases (smart devices, sensor networks, and machine-generated data feeds).

### The DePIN technical stack

IoTeX's distinctive value proposition is not raw throughput but a set of [[depin|DePIN]]-oriented primitives that aim to make off-chain hardware *trustworthy* to on-chain [[smart-contracts]]:

- **W3bstream** — the project's flagship middleware framework, designed to ingest real-world data from devices, run verifiable off-chain computation, and generate proofs that [[smart-contracts]] can consume. It is the bridge between messy physical-world data and deterministic on-chain logic.
- **Decentralized Identity (DID) and device binding** — IoTeX anchors device identity on-chain so that a given data feed can be attributed to a specific, registered piece of hardware, raising the cost of spoofed or fabricated data.
- **ioPay / IoTeX wallet and SDKs** — developer and user tooling for building and interacting with DePIN apps.
- **IoTeX 2.0 ("MachineFi" → modular DePIN)** — the project's later roadmap reframed the stack around modular infrastructure for connecting machines, identity, and AI agents. Specific module names, throughput, and adoption figures should be treated as project-stated positioning, not audited benchmarks.

The core idea — that a blockchain can serve as a neutral settlement and verification layer for physical infrastructure (mapping, mobility, environmental sensing, energy, connectivity) — is the broader [[depin]] thesis; IoTeX is one of several networks competing to be its base layer.

---

## Comparison vs Peer DePIN / Layer-1s

| Network | Consensus | EVM-compatible | Niche | DePIN approach |
|---|---|---|---|---|
| **IoTeX** ([[iotex]]) | Roll-DPoS (committee-rotating) | Yes | DePIN / real-world AI | Full L1 + W3bstream middleware + device DID |
| Helium | PoS (migrated to Solana) | N/A (Solana SVM) | Wireless / IoT coverage | App-chain → Solana-based token & subDAOs |
| peaq | NPoS (Polkadot SDK) | Yes (EVM pallet) | DePIN / "Economy of Things" | Polkadot-ecosystem DePIN L1 |
| Render / DePIN apps on general L1s | host-chain | varies | GPU / compute, sensing | Apps deployed on Ethereum/Solana/Base |
| [[harmony]] | Effective PoS (sharded) | Yes | General low-fee EVM L1 | Not DePIN-specific |

IoTeX's edge versus rivals is owning an EVM-compatible [[layer-1]] *and* purpose-built device/data middleware; its disadvantage is that general-purpose chains (Solana, [[ethereum]] L2s like Base) can host DePIN apps with far deeper liquidity, and category leaders like Helium have larger real-world device footprints.

---

## Token Economics & Value Accrual

IOTX has a **capped maximum supply of 10 billion** tokens, distinguishing it from the uncapped, inflationary designs of peers like [[casper-network]] and [[harmony]]. With circulating supply already near the total supply, IoTeX's market cap and fully-diluted valuation are close (MC/FDV ≈ 1.00), meaning relatively little future dilution overhang from unlocks. Value accrual mechanisms include:

- **Gas fees** — paid in IOTX for transactions and contract execution.
- **Staking / delegation** — IOTX is staked to vote for delegates under Roll-DPoS; stakers earn rewards and, historically, "bucket"-based staking gave longer locks more voting weight.
- **DePIN demand** — registering devices, paying for W3bstream computation, and DePIN-app activity are the intended demand sinks that would tie token value to real-world usage rather than speculation alone. Whether that demand materializes at scale is the central open question for the thesis.

A capped supply with usage-driven sinks is structurally healthier than pure inflation, but only if on-chain DePIN demand grows; absent that, IOTX behaves like a thinly traded narrative token.

---

## Governance

IoTeX governance operates through its **delegate system**: IOTX holders stake and vote for delegates, who under Roll-DPoS produce blocks and carry influence over network decisions. The **IoTeX Foundation** and core team have historically driven protocol upgrades and the roadmap (MachineFi, W3bstream, IoTeX 2.0). As with all delegated-stake systems, effective control tracks the concentration of staked IOTX among top delegates, so decentralization claims should be weighed against actual delegate distribution rather than assumed.

---

## Ecosystem & Adoption

IoTeX's ecosystem is concentrated in DePIN and IoT-flavored applications (mobility, robotics, environmental and health sensing, and "real-world AI" data tooling), and the token is included in DePIN-themed market indices (e.g., GMCI DePIN Index). IoTeX has also deployed onto **Base**, Coinbase's [[ethereum]] [[layer-2]], broadening where IOTX-denominated apps can run and tapping that ecosystem's liquidity. Partnership and integration claims (with hardware makers and standards organizations) have featured prominently in the project's marketing; such claims should be treated as the project's own positioning rather than independently verified figures. Device counts, active DePIN deployments, and TVL should likewise be verified on-chain rather than assumed from marketing. IOTX trades roughly 98% below its 2021 peak of about $0.26, consistent with the broad decline in long-tail altcoins.

---

## Notable History

- **2017–2018 — Founding and launch.** IoTeX launched as an IoT-focused blockchain, raising funds in 2017 and going live with its own [[layer-1]], one of the earliest projects explicitly targeting the device-to-blockchain problem space that would later be branded [[depin|DePIN]].
- **November 2021 — All-time high.** IOTX peaked near **$0.2556** on 2021-11-13 during the bull market, partly on enthusiasm for the IoT/MachineFi narrative, before falling ~98%.
- **MachineFi → W3bstream → IoTeX 2.0.** The project iterated its branding and stack from "MachineFi" toward the W3bstream verifiable-compute middleware and a modular DePIN framing, repositioning around the DePIN and "real-world AI" narratives as those categories gained attention.
- **Base deployment.** IoTeX extended onto the Base [[layer-2]] (contract address recorded below), reflecting a multi-chain strategy rather than relying solely on its native L1.
- **March 2020 — All-time low.** IOTX printed an all-time low near **$0.00121576** on 2020-03-13 during the COVID market crash; current prices remain well above that level (+280%) even after the long bear.

---

## Risks

- **DePIN narrative dependence** — much of IOTX's valuation case rests on the still-early DePIN thesis; if real-world device adoption and paying demand lag, the token has limited independent support.
- **Competition** — the DePIN/IoT-on-chain space includes well-funded rivals (e.g., Helium, peaq, and other device networks), and general-purpose L1/L2s can host DePIN apps too.
- **Delegate concentration** — Roll-DPoS bounds block production to elected delegates, a centralization trade-off versus permissionless validation.
- **Data-trust assumptions** — the entire DePIN value proposition depends on device identity and W3bstream proofs being hard to spoof; if attackers can fabricate "verified" real-world data cheaply, the trust premium collapses.
- **Multi-chain fragmentation** — spreading across the native L1 and Base [[layer-2]] can fragment liquidity and complicate the value-accrual story.
- **Low liquidity & price decay** — a sub-$30M market cap, rank below #600, and a ~98% drawdown from all-time high imply thin liquidity and weak momentum.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 9.44B IOTX |
| **Total Supply** | 9.44B IOTX |
| **Max Supply** | 10.00B IOTX |
| **Fully Diluted Valuation** | $43.63M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2556 (2021-11-13) |
| **Current vs ATH** | -98.19% |
| **All-Time Low** | $0.00121576 (2020-03-13) |
| **Current vs ATL** | +280.20% |
| **24h Change** | -2.86% |
| **7d Change** | +1.86% |
| **30d Change** | -9.01% |
| **1y Change** | -75.08% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6fb3e0a217407efff7ca062d46c26e5d60a14d69` |
| Base | `0xbcbaf311cec8a4eac0430193a528d9ff27ae38c1` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | IOTX/USDT | N/A |
| Upbit | IOTX/BTC | N/A |
| Bitget | IOTX/USDT | N/A |
| KuCoin | IOTX/USDT | N/A |
| Crypto.com Exchange | IOTX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X6FB3E0A217407EFFF7CA062D46C26E5D60A14D69/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://iotex.io](https://iotex.io) |
| **Twitter** | [@iotex_io](https://twitter.com/iotex_io) |
| **Reddit** | [https://www.reddit.com/r/IoTeX](https://www.reddit.com/r/IoTeX) |
| **Telegram** | [IoTeXGroup](https://t.me/IoTeXGroup) (23,065 members) |
| **GitHub** | [https://github.com/iotexproject/iotex-core](https://github.com/iotexproject/iotex-core) |
| **Whitepaper** | [https://github.com/iotexproject/files/blob/main/publications/IoTeX_2_0_Whitepaper_1.1_EN.pdf](https://github.com/iotexproject/files/blob/main/publications/IoTeX_2_0_Whitepaper_1.1_EN.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.23M (2026-04-09 snapshot) |
| **Market Cap Rank** | #645 |
| **Price (2026-06-22)** | $0.00316585 |
| **24h Change (2026-06-22)** | -0.50% |
| **7d Change (2026-06-22)** | -7.14% |
| **CoinGecko Sentiment** | 100% positive |
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
- [[layer-1]]
- [[layer-2]]
- [[depin]]
- [[proof-of-stake]]
- [[consensus-mechanism]]
- [[smart-contracts]]
- [[staking]]
- [[harmony]]
- [[casper-network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market data snapshot
- General market knowledge; no other specific wiki source ingested yet. Market figures dated 2026-06-22 are from cryptodataapi.com / CoinGecko (BTC bear regime; Fear & Greed Index 21 / Extreme Fear).
