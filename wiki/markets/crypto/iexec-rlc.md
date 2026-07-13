---
title: "iExec RLC"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ai-trading]
aliases: ["RLC", "iExec"]
entity_type: protocol
founded: 2017
headquarters: "Lyon, France / Decentralized"
website: "http://iex.ec/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[depin]]", "[[decentralized-compute]]", "[[trusted-execution-environment]]", "[[artificial-intelligence]]"]
---

# iExec RLC

**iExec RLC** (RLC) is the native token of [[iexec-rlc|iExec]], a decentralized marketplace for confidential off-chain computing. iExec lets developers build privacy-first applications that combine [[decentralized-compute|decentralized compute]] resources, protected datasets, and confidential processing using [[trusted-execution-environment|Trusted Execution Environments (TEEs)]], giving users control over how their data is accessed and monetized. The protocol is increasingly positioned toward decentralized AI (DeAI), where confidential compute is used to run models and agents over private data. It is part of the broader [[depin|DePIN]] (Decentralized Physical Infrastructure) sector and ranks **#738** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* RLC trades around **$0.3345**, market cap **~$24.1M** (rank #738), **+2.69% over 24h** and **-5.12% over 7d**. The broader market sat in Extreme Fear (Fear & Greed 22, BTC ~$64,180) at the time of capture.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RLC |
| **Market Cap Rank** | #738 |
| **Market Cap** | $24,105,947 |
| **Current Price** | $0.334454 |
| **Genesis Date** | 2017-04-19 |
| **Categories** | Artificial Intelligence (AI), Oracle, Arbitrum Ecosystem, Ethereum Ecosystem, DePIN, AI Agents, Energi Ecosystem, Sora Ecosystem, GMCI DePIN Index, GMCI Index, Privacy Infrastructure, Privacy |
| **Website** | [http://iex.ec/](http://iex.ec/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

iExec is a decentralized cloud-computing marketplace launched in 2017 after one of the era's larger ICOs (~$12M raised in roughly three hours). It matches buyers of compute (developers, AI applications) with providers of off-chain resources — CPU/GPU power, datasets, and applications — coordinated and settled on-chain. The defining feature is **confidential computing**: workloads run inside [[trusted-execution-environment|Trusted Execution Environments]] (such as Intel SGX/TDX enclaves), so code and data remain encrypted even from the machine operator. This lets sensitive datasets be processed, rented, and monetized without ever being exposed in plaintext.

The platform exposes several primitives: **DataProtector** (encrypt and grant access to data), **Confidential Computing / iApps** (run privacy-preserving applications), and **Web3 Mail / messaging** (contact users without exposing their addresses). Since 2023–2024 iExec has reoriented around **DeAI (decentralized AI)** — running AI models and [[artificial-intelligence|AI]] agents over protected data inside TEEs so that neither the model owner nor the data owner has to trust the other. This positions iExec at the intersection of [[depin|DePIN]], confidential compute, and AI infrastructure.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 72.38M RLC |
| **Total Supply** | 87.00M RLC |
| **Max Supply** | 87.00M RLC |
| **Fully Diluted Valuation** | $35.92M |
| **Market Cap / FDV Ratio** | 0.83 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $15.51 (2021-05-10) |
| **Current vs ATH** | -97.34% |
| **All-Time Low** | $0.1538 (2018-12-15) |
| **Current vs ATL** | +167.97% |
| **24h Change** | +2.69% |
| **7d Change** | -5.12% |
| **1y Change** | -58.50% |

> RLC is far below its 2021 cycle peak of $15.51 (-97%+), reflecting both the broad altcoin drawdown and the gap between DePIN narratives and realized on-chain compute demand.

---

## Architecture & Token Role

The **RLC token** ("Run on Lots of Computers") is the unit of account and settlement for the iExec marketplace. Its roles:

- **Payment / work token** — buyers pay RLC to rent compute, datasets, and applications; providers ("workers") earn RLC for completing verifiable tasks. This is the core [[depin|DePIN]] demand loop: usage of confidential compute should drive RLC throughput.
- **Staking** — workers stake RLC as collateral in the **Proof-of-Contribution (PoCo)** consensus, which validates that off-chain results are correct before payment is released; bad actors can be slashed.
- **Governance** — RLC is used in iExec governance over protocol parameters and grants.

RLC is a fixed-supply ERC-20 (max 87M, with the bulk circulating) deployed primarily on [[ethereum|Ethereum]], with bridged representations on Arbitrum, Energi, and Sora. The fixed cap means there is no ongoing token emission diluting holders — unlike many DePIN tokens, the demand-vs-emissions dynamic for iExec is driven almost entirely by **marketplace usage** rather than inflationary worker rewards.

## Competitive Position

iExec competes in two overlapping arenas: general [[decentralized-compute|decentralized compute]] (against networks like Akash, [[render|Render]], and [[nosana|Nosana]] for GPU/AI compute) and **confidential computing** (against [[phala-network|Phala]], Oasis, [[nillion|Nillion]], and centralized TEE clouds). Its differentiator is the combination of TEE-based confidentiality with a built-in data-monetization layer (DataProtector + iApps), which most general GPU-marketplace peers do not offer.

| Network | Primary niche | Confidentiality approach | Settlement | Token | Key contrast vs iExec |
|---|---|---|---|---|---|
| **iExec (RLC)** | Confidential off-chain compute + data monetization | Intel SGX/TDX TEEs (PoCo validation) | Ethereum / Arbitrum | RLC (fixed 87M) | Pairs TEE compute with a data-access/monetization marketplace |
| **[[phala-network|Phala]]** | Confidential compute (TEE workers, AI agents) | TEE worker network | Phala / Polkadot | PHA | Broad TEE compute; iExec adds a richer data layer |
| **[[nillion|Nillion]]** | Blind computation / privacy | [[multi-party-computation|MPC]] + TEEs (cryptographic, no single trusted enclave) | Nillion chain | NIL (1B, emissive) | MPC removes hardware-vendor trust iExec inherits |
| **[[render|Render]]** | GPU rendering / AI compute | None (not confidential) | Solana | RENDER | Raw GPU throughput, no privacy primitive |
| **Akash** | Decentralized cloud (containers) | None (not confidential) | Cosmos | AKT | General cloud, no confidentiality or data-monetization layer |

iExec's narrowest, most defensible angle is **confidential compute over private data** — the same DeAI thesis as [[nillion|Nillion]] and [[phala-network|Phala]], but reached through hardware enclaves plus a fixed-supply token rather than cryptographic MPC or heavy emissions.

## How & Where It Trades

RLC has comparatively deep small-cap liquidity for a ~$24M-cap DePIN name, listed on major tier-1 centralized venues (**Binance** RLC/USDT, **Kraken** RLC/USD, **Upbit** RLC/BTC, plus Bitget, KuCoin, Crypto.com) and on-chain via **Uniswap V2/V3** and **Sushiswap** WETH pairs on [[ethereum|Ethereum]]. The Korean **Upbit** RLC/BTC listing is notable: Korean spot flow can drive episodic volatility detached from global order books. There is no widely-distributed RLC perpetual market, so funding-rate squeezes are less of a factor than for larger AI tokens — most volatility comes from spot rotation. The fixed 87M supply and MC/FDV of 0.83 mean limited structural emission overhang relative to emissive DePIN peers like [[naoris|Naoris]] or [[nillion|Nillion]].

## Narrative & Catalysts

RLC sits in the **DeAI / confidential-compute** intersection of the broader AI-coin basket (alongside [[bittensor|TAO]], [[render|RENDER]], [[fetch-ai|FET]], WLD). In the current tape (2026-06-22, Fear & Greed 21 / Extreme Fear, established bear-market regime) the AI/DePIN basket is high-beta and trending hard in both directions. RLC-specific catalysts that historically move the token:
- **Confidential-AI / DeAI product launches** — new iApps, TEE-backed model-serving, or DataProtector integrations that demonstrate real paid compute throughput.
- **Enterprise / data-monetization partnerships** — the demand side that the fixed-supply thesis depends on.
- **AI-basket beta** — RLC tends to amplify moves in the AI narrative leaders; rallies and drawdowns in [[bittensor|TAO]]/[[render|RENDER]] spill into RLC.
- **TEE-security headlines** — a high-profile SGX/TDX side-channel disclosure is a sector-wide negative catalyst for all TEE-reliant tokens.

## History & Timeline

- **2017-04** — iExec ICO raises ~$12M in roughly three hours; RLC ERC-20 launches (genesis 2017-04-19).
- **2018-2020** — V1-V4 marketplace and Proof-of-Contribution (PoCo) consensus roll out; SGX-based confidential computing introduced.
- **2021-05-10** — RLC all-time high of **$15.51** during the cycle peak.
- **2023-2024** — Strategic reorientation toward **DeAI**: confidential AI compute, DataProtector, Web3 messaging primitives.
- **2018-12-15** — All-time low of **$0.1538** (prior cycle bottom).

> Dated events above reflect publicly known project milestones; intra-period product specifics are kept qualitative where not independently verified.

## Risks

- **Demand realization** — like most DePIN/compute tokens, the central question is whether real, recurring paid compute demand materializes versus speculative token flow. Fixed supply helps holders only if usage grows.
- **TEE trust assumptions** — confidential computing inherits hardware-vendor trust (e.g., Intel SGX/TDX) and has a history of side-channel vulnerabilities; a TEE break would undermine the privacy guarantee.
- **Liquidity / size** — at a ~$24M cap and modest daily volume, RLC is a small-cap with elevated volatility and slippage risk.
- **Narrative dependence** — valuation is sensitive to the AI/DeAI and DePIN narrative cycles; in an Extreme-Fear bear tape, high-beta AI names tend to underperform on drawdowns.
- **Competitive crowding** — confidential-compute is increasingly contested by [[nillion|Nillion]] (MPC), [[phala-network|Phala]] (TEE), and well-funded centralized confidential-cloud offerings.

## Trading Playbook

> Educational framing only — not financial advice. RLC is a high-beta small-cap.

- **Regime awareness** — at Fear & Greed 21 (Extreme Fear) in an established bear market, AI/DePIN small-caps like RLC carry elevated downside beta; size positions far smaller than for majors and expect 2-3x the volatility of [[bitcoin|BTC]].
- **Basket correlation** — RLC trades as part of the AI basket; gauge entries against [[bittensor|TAO]]/[[render|RENDER]] momentum rather than in isolation. Broad-basket capitulation often marks better risk/reward than chasing isolated RLC spikes.
- **Liquidity / slippage** — use limit orders on Binance/Kraken; the ~$2M daily volume means market orders of size will move price. Watch the Upbit RLC/BTC book for Korea-driven gaps.
- **Catalyst vs noise** — distinguish DeAI product-usage signals (recurring compute throughput) from announcement-driven pumps; the former supports the fixed-supply thesis, the latter mean-reverts.
- **Invalidation** — a confirmed TEE side-channel break or stalled marketplace usage undermines the core thesis; treat such headlines as structural, not dip-buying opportunities.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x607f4c5bb672230e8672085532f7e901544a7375` |
| Energi | `0xb4ff17b5e93c40ff09326b0d538118022f02dc2b` |
| Sora | `0x008294f7b08f568a661de2b248c34fc574e7e0012a12ef7959eb1a5c6b349e09` |
| Arbitrum One | `0xe649e6a1f2afc63ca268c2363691cecaf75cf47c` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RLC/USDT | N/A |
| Kraken | RLC/USD | N/A |
| Upbit | RLC/BTC | N/A |
| Bitget | RLC/USDT | N/A |
| KuCoin | RLC/USDT | N/A |
| Crypto.com Exchange | RLC/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Sushiswap | 0X607F4C5BB672230E8672085532F7E901544A7375/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X607F4C5BB672230E8672085532F7E901544A7375/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X607F4C5BB672230E8672085532F7E901544A7375/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://iex.ec/](http://iex.ec/) |
| **Twitter** | [@iEx_ec](https://twitter.com/iEx_ec) |
| **Reddit** | [https://www.reddit.com/r/iexec](https://www.reddit.com/r/iexec) |
| **Telegram** | [iexec_rlc_official](https://t.me/iexec_rlc_official) (3,232 members) |
| **GitHub** | [https://github.com/iExecBlockchainComputing/iexec-sdk](https://github.com/iExecBlockchainComputing/iexec-sdk) |
| **Whitepaper** | [https://www.iex.ec/developers](https://www.iex.ec/developers) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 422 |
| **GitHub Forks** | 47 |
| **Commits (4 weeks)** | 2 |
| **Pull Requests Merged** | 321 |
| **Contributors** | 17 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.23M (Apr-2026 snapshot) |
| **Market Cap Rank** | #738 |
| **Current Price** | $0.334454 |
| **Last Updated** | 2026-06-21 |

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
- [[depin]]
- [[decentralized-compute]]
- [[trusted-execution-environment]]
- [[nosana]]
- [[render]]
- [[phala-network]]
- [[nillion]]
- [[bittensor]]
- [[artificial-intelligence]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.
