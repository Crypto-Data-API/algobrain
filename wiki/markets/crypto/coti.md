---
title: "COTI"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins]
aliases: ["COTI", "Currency Of The Internet"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://coti.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[smart-contracts]]", "[[defi]]"]
---

# COTI

**COTI** (COTI) is a privacy- and payments-focused blockchain project that began life as an enterprise payment network ("Currency Of The Internet") and has since evolved into **COTI V2**, a confidentiality layer built around the cryptographic technique known as **Garbled Circuits**. In its current form COTI positions itself as a fast, lightweight confidentiality layer secured by [[ethereum]], aiming to bring privacy-preserving computation to public-blockchain use cases such as confidential transactions, on-chain AI, [[defi]], and decentralized identity. It ranks **#682** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* COTI trades at **$0.00950149**, with a market cap of **$27,474,021** (rank **#682**), down **-0.87%** over 24h and down **-7.94%** over the past 7 days. These prices sit during a period of broad market weakness (Bitcoin ~$64,166; Fear & Greed Index 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | COTI |
| **Market Cap Rank** | #682 |
| **Market Cap** | $27,474,021 |
| **Current Price** | $0.00950149 |
| **24h Change** | -0.87% |
| **7d Change** | -7.94% |
| **Categories** | Privacy Blockchain, Privacy Infrastructure, Ethereum Ecosystem, Smart Contract Platform, Layer 2 (L2), Zero Knowledge (ZK), Payments |
| **Website** | [https://coti.io/](https://coti.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

COTI's roadmap splits cleanly into two eras:

- **COTI V1 (payments / enterprise):** Originally launched around 2019, COTI marketed itself as an enterprise-grade payments infrastructure. Its earlier architecture leaned on a DAG-based ledger ("Trustchain") and a "Trust Score" consensus model, targeting low-fee, high-throughput payment rails, merchant tools, and stablecoin/CBDC infrastructure. This positioned COTI alongside other payment-focused chains rather than general-purpose [[smart-contracts]] platforms.
- **COTI V2 (privacy / confidentiality):** COTI re-architected around **privacy as the core product**, building a confidentiality layer that uses **Garbled Circuits** — a multi-party-computation (MPC) technique — to allow computation over encrypted data. The pitch is that smart contracts can operate on private inputs without exposing them on-chain, enabling confidential transactions, private [[defi]], decentralized identity, and privacy for on-chain AI workloads, while still anchoring security to [[ethereum]].

Garbled Circuits is a long-standing cryptographic primitive (distinct from zero-knowledge proofs and fully homomorphic encryption); COTI's distinguishing claim is engineering it into a practical, low-overhead confidentiality layer for Web3. As with all privacy-tech claims, real-world performance, security audits, and adoption should be verified independently before relying on them.

---

## Architecture & Consensus

### V1: Trustchain (DAG) and Trust Score

The original COTI ran on **Trustchain**, a directed-acyclic-graph (DAG) ledger rather than a linear block-chain. Instead of miners or a fixed validator set ordering blocks, each new transaction confirmed prior transactions, and a **Trust Score** algorithm rated participants by reliability, giving higher-trust transactions faster confirmation. This DAG + Trust Score design targeted the payments use case: low fees, high throughput, and merchant/PSP tooling (the "MultiDAG" / payment-network framing). It placed V1 alongside payment-rail chains rather than general-purpose [[smart-contracts|smart-contract]] platforms.

### V2: Garbled Circuits confidentiality layer

COTI V2 re-architected around **privacy as the product**. Its core primitive is **Garbled Circuits (GC)** — a multi-party-computation (MPC) technique in which a boolean circuit representing a computation is "garbled" (encrypted) so that parties can jointly evaluate it over their private inputs without revealing those inputs to each other. COTI's pitch is that GC is more lightweight and faster to set up than fully homomorphic encryption (FHE) and avoids the heavy proving costs of [[zero-knowledge-proof|zero-knowledge]] systems for certain confidential-compute patterns. Practically, V2 is positioned as a **confidentiality layer secured by [[ethereum|Ethereum]]** (an L2-style execution/privacy layer) where contracts can hold and operate on encrypted state — enabling confidential transactions, private [[defi]], decentralized identity, and privacy for on-chain AI.

### How it compares to other privacy primitives

| Approach | Used by | Hardware trust? | Trade-off |
|---|---|---|---|
| **Garbled Circuits / MPC** | **COTI V2** | No (cryptographic) | Practical for many confidential ops; circuit/comms overhead, newer in production |
| [[trusted-execution-environment\|TEE]] (SGX/TDX) | [[secret\|Secret]], [[pha\|Phala]], Oasis | Yes (vendor enclave) | Fast, general-purpose; side-channel & vendor-trust risk |
| Fully homomorphic encryption (FHE) | Fhenix, Zama-based | No (cryptographic) | Strongest privacy; historically very heavy compute |
| [[zero-knowledge-proof\|ZK proofs]] | Aztec, Aleo | No (cryptographic) | Great for validity/privacy; proving cost, app-specific |

COTI's bet is that MPC/Garbled Circuits hits a sweet spot of **no hardware trust assumption** (unlike its TEE-based peers [[secret|Secret]] and [[pha|Phala]]) while remaining cheaper than FHE for common confidential-compute patterns. The counter-risk is maturity: GC-based on-chain confidentiality is less battle-tested in production, and privacy/security claims must be independently audited.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.76B COTI |
| **Total Supply** | 2.76B COTI |
| **Max Supply** | 4.91B COTI |
| **Fully Diluted Valuation** | $37.18M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.6686 (2021-09-29) |
| **Current vs ATH** | -97.98% |
| **All-Time Low** | $0.00556342 (2019-11-07) |
| **Current vs ATL** | +70.78% |
| **24h Change** | -0.87% |
| **7d Change** | -7.94% |
| **1y Change** | -74.32% |

The token sits roughly **-98%** below its 2021 all-time high, a drawdown typical of altcoins that peaked in the last cycle and never recovered. Like most small-cap tokens, COTI's price is highly sensitive to overall market risk appetite, and the current reading (Bitcoin ~$64,166, Fear & Greed 21 / Extreme Fear) is a meaningful headwind.

---

## Token Utility

The COTI token serves as the native asset of the network. Across its history it has been used (or is intended to be used) for transaction fees / gas, staking and securing the network, governance participation, and as collateral/treasury within COTI's payment and confidentiality products. Token holders should confirm the exact current utility against COTI's latest documentation, since the V1-to-V2 transition changed the token's role and there has been a token-migration/conversion process associated with COTI V2.

### Staking and value accrual

COTI has historically run staking programs (e.g., "Treasury" staking) where holders lock COTI for variable lock periods to earn rewards, with longer locks earning higher multipliers. In the V1 payments model, staking also tied into node/validator roles and Trust Score. Under V2, COTI's intended value-accrual story is that COTI is the **gas and security asset of the confidentiality layer** — fees for confidential computation and demand from privacy-using applications flow back to the token, while staking secures the network and locks supply. The important caveats: (1) the V1→V2 transition involved a **token migration/conversion**, changing supply mechanics and the token's role, and (2) value accrual depends on real usage of the confidentiality layer, which should be verified against live metrics rather than assumed. Note the max supply (~4.91B) sits well above the circulating/total (~2.76B), so future issuance is possible — confirm the current emission/vesting schedule.

---

## Governance

COTI holders participate in protocol governance, which over the project's life has covered staking parameters, treasury/incentive allocation, ecosystem grants, and the strategic direction of the V1→V2 transition. As with most small-cap protocols, practical influence concentrates among the founding team/foundation and large holders, and on-chain turnout is typically low. The migration to a confidentiality-layer model means governance increasingly concerns the privacy stack, developer incentives, and integrations rather than the legacy payments business.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xddb3422497e61e13543bea06989c0789117555c5` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | COTI/USDT | N/A |
| Kraken | COTI/USD | N/A |
| Bitget | COTI/USDT | N/A |
| KuCoin | COTI/USDT | N/A |
| Crypto.com Exchange | COTI/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XDDB3422497E61E13543BEA06989C0789117555C5/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Sushiswap | 0XDDB3422497E61E13543BEA06989C0789117555C5/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0XDDB3422497E61E13543BEA06989C0789117555C5/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://coti.io/](https://coti.io/) |
| **Twitter** | [@COTInetwork](https://twitter.com/COTInetwork) |
| **Reddit** | [https://www.reddit.com/r/cotinetwork](https://www.reddit.com/r/cotinetwork) |
| **Telegram** | [COTInetwork](https://t.me/COTInetwork) (19,199 members) |
| **Discord** | [https://discord.me/coti](https://discord.me/coti) |
| **GitHub** | [https://github.com/coti-io/confidentiality-contracts](https://github.com/coti-io/confidentiality-contracts) |
| **Whitepaper** | [https://coti.io/files/coti_v2_whitepaper.pdf](https://coti.io/files/coti_v2_whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 23 |
| **GitHub Forks** | 4 |
| **Pull Requests Merged** | 14 |
| **Contributors** | 4 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.00950149 |
| **Market Cap (2026-06-22)** | $27,474,021 |
| **Market Cap Rank** | #682 |
| **24h Change** | -0.87% |
| **7d Change** | -7.94% |
| **Last Updated** | 2026-06-22 |

---

## Risks

- **Small-cap / liquidity risk:** With a market cap around ~$27M and a rank in the high-600s, COTI is a thin-liquidity asset prone to large percentage swings and slippage on size.
- **Technology / execution risk:** The V2 confidentiality stack relies on advanced cryptography (Garbled Circuits / MPC). Such systems are hard to audit, are less battle-tested in production than mature ZK or TEE stacks, and privacy claims should not be taken at face value without independent review.
- **Pivot risk:** COTI has materially repositioned (payments → privacy). Pivots can dilute brand, fragment the community, and create token-migration friction.
- **Competition risk:** confidential-compute is crowded — TEE-based [[secret|Secret]] and [[pha|Phala]], FHE projects, and [[zero-knowledge-proof|ZK]]-based privacy chains all compete for the same developers and use cases.
- **Regulatory risk:** Privacy-focused blockchains face heightened regulatory scrutiny in some jurisdictions; some category tags historically flagged COTI under "alleged securities" lists. Treat such classifications as unverified labels rather than legal conclusions.
- **Cycle risk:** Down ~98% from ATH and trading in an Extreme Fear market; small-caps tend to underperform in risk-off regimes.

> This page is not investment advice. Figures are point-in-time market data; verify on-chain and project claims independently.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **2019 launch (V1):** COTI ("Currency Of The Internet") launched as an enterprise payments network on the Trustchain DAG with the Trust Score consensus model. All-time low of **$0.00556342** printed on 2019-11-07.
- **2021 cycle peak:** COTI reached its all-time high of **$0.6686** on 2021-09-29 during the bull market and payments/CBDC narrative; it has since fallen ~98% from that peak.
- **COTI V2 pivot (2023–2024):** COTI announced and built **COTI V2**, re-architecting around privacy via Garbled Circuits and positioning as a confidentiality layer secured by [[ethereum|Ethereum]], with an associated token-migration/conversion process.
- **2026 small-cap drawdown:** amid the broad altcoin washout, COTI traded in the sub-$0.01 range; as of 2026-06-22 it is **-7.94% over 7 days** and **-0.87% on the day** in an Extreme-Fear market (BTC ~$64,166).

> *Notable events and news will continue to be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[layer-2]]
- [[smart-contracts]]
- [[defi]]
- [[privacy-coins]]
- [[secret]]
- [[pha]]
- [[zero-knowledge-proof]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko; BTC ~$64,166, Fear & Greed 21 / Extreme Fear.
- General market knowledge; no specific dedicated COTI source has been ingested into the wiki yet.
