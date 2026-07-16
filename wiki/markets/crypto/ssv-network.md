---
title: "SSV Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, restaking]
aliases: ["SSV", "ssv.network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://ssv.network/"
related: ["[[crypto-markets]]", "[[eigenlayer]]", "[[ethereum]]", "[[lido]]", "[[liquid-staking]]", "[[restaking]]"]
---

# SSV Network

**SSV Network** (ticker **SSV**) is the governance token of ssv.network, the leading **Distributed Validator Technology (DVT)** protocol on [[ethereum|Ethereum]]. SSV — Secret Shared Validators — splits a single Ethereum validator's key into shares operated by multiple independent node operators, so that no one operator controls the key and the validator stays online even if some operators fail. It is core **ETH staking infrastructure** that improves the decentralization, fault-tolerance, and security of staking pools, liquid-staking protocols, and restaking systems.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | SSV |
| **Current Price** | $2.39 |
| **Market Cap** | $35.17M |
| **Market Cap Rank** | #580 |
| **24h Volume** | $5.67M |
| **24h Change** | +3.97% |
| **7d Change** | +2.55% |
| **Fully Diluted Valuation** | $35.17M |
| **All-Time High** | $65.82 (2024-03-25) |
| **All-Time Low** | $1.85 (2026-06-06) |
| **Chain** | [[ethereum\|Ethereum]] |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

SSV is up ~+4% on the day and ~+2.6% on the week — relative strength against a market where the **Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] sits at 23 (extreme fear)** in an **established bear market**. At ~$2.39 the token is roughly -96% below its March 2024 ATH of $65.82 and just above its recent all-time low of $1.85 (2026-06-06). With market cap and FDV equal (MC/FDV = 1.00), there is no unlock overhang — every dollar of demand acts on fully circulating supply.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~14.70M SSV |
| **Total Supply** | ~14.70M SSV |
| **Max Supply** | Uncapped (governance-controlled) |
| **Fully Diluted Valuation** | $35.17M |
| **Market Cap / FDV** | 1.00 |
| **All-Time High** | $65.82 (2024-03-25) |
| **All-Time Low** | $1.85 (2026-06-06) |

SSV's supply is essentially fully circulating (MC/FDV = 1.00), so there is no significant unlock overhang. The token has two core utilities:

- **Network fees** — Stakers/validators that use the DVT network pay operators in SSV; a network fee accrues to the SSV DAO treasury.
- **Governance** — SSV holders govern protocol parameters, operator/validator economics, and treasury use (including the large **SSV 2.0** initiative to add restaking-based "based applications").

---

## Technology — Distributed Validator Technology (DVT)

SSV's function is to make running an [[ethereum|Ethereum]] validator **fault-tolerant and decentralized** via secret-shared keys:

- A validator's signing key is split via **secret sharing** (Shamir-style) into KeyShares distributed to (typically) 4+ independent operators.
- The operators run a Byzantine-fault-tolerant **consensus protocol (IBFT)** so that a **threshold** of them (e.g., 3-of-4) must cooperate to sign attestations and blocks — the **full key is never reconstructed in one place**, removing the single point of compromise.
- If one or two operators go offline or misbehave, the remaining threshold keeps the validator performing its duties, **avoiding downtime penalties** and reducing slashing exposure from any single operator.

This is the backbone for **decentralizing large staking pools and [[liquid-staking|liquid-staking]] protocols** — [[lido|Lido]] (via its DVT / Simple DVT modules), EtherFi, and others use DVT (SSV and the competing Obol) to reduce single-operator risk. SSV is also positioned in the **[[restaking]]** narrative: **SSV 2.0** aims to let DVT-secured infrastructure underpin "based applications" and restaking-style services, tying SSV to the [[eigenlayer|EigenLayer]] ecosystem.

---

## Market Structure & Derivatives

**Spot venues.** SSV lists on Binance (SSV/USDT), Kraken (SSV/USD), Bitget, and KuCoin. On-chain liquidity is on [[uniswap]] V3 against WETH.

**Derivatives.** There is no prominent SSV perp on [[hyperliquid]]; spot is the main venue (verify derivatives availability live before assuming access). Some CEX futures desks list SSV but with modest, intermittent open interest.

**Liquidity profile.** ~$5.7M daily volume on a $35.17M cap (~16% velocity) is healthy for the cohort. Crucially, with **MC/FDV = 1.00** the float is fully circulating, so price discovery is not distorted by an impending unlock cliff — a structural advantage over high-FDV peers like [[redstone-oracles|RED]] or [[cysic|CYS]].

---

## Use Case, Narrative & Category

SSV sits in the **ETH staking infrastructure / DeFi infrastructure** category and is tagged restaking and liquid staking. Its narrative is that **DVT is a structural requirement for credible decentralization of Ethereum staking** — as more ETH is staked through pools, regulators and the community pressure those pools to avoid single-operator concentration, and DVT is the technology that delivers it. SSV's adoption by major liquid-staking providers (notably Lido's Simple DVT) is the central bull case, with SSV 2.0 / restaking extensions as the growth optionality. Its main competitor is **Obol Network**.

### Peer comparison — staking / validator infrastructure

| Protocol | Token | Category | Role | Mkt cap rank |
|---|---|---|---|---|
| **SSV Network** | **SSV** | **DVT (validator infra)** | **Secret-shared validator keys** | **#580** |
| Obol Network | OBOL | DVT (validator infra) | Distributed validator clusters | — |
| [[lido]] | LDO | [[liquid-staking]] | Largest ETH staking pool (DVT consumer) | Top-150 |
| Rocket Pool | RPL | Liquid staking | Permissionless node operators | — |
| [[eigenlayer]] | EIGEN | [[restaking]] | Restaked-ETH security marketplace | — |

SSV is **infrastructure beneath the staking pools**, not a staking pool itself — its customers are Lido, EtherFi and similar, which makes it a pick-and-shovel play on the decentralization of ETH staking rather than a direct staking-yield product. Its only true like-for-like competitor is Obol.

### Valuation framing (qualitative)

SSV trades at ~$35M with no dilution overhang (MC/FDV = 1.00), so the entire story is **demand**, not supply. The bull case is that DVT becomes mandatory infrastructure for credibly decentralized staking and that SSV's Lido/EtherFi anchoring plus SSV 2.0 restaking extensions drive network-fee revenue to the DAO treasury. The bear case is **demand concentration** in a handful of large pools, a two-horse DVT race with Obol, and the fact that the token is -96% from ATH because DVT fee revenue has yet to scale to anything that justifies historical valuations. A re-rating likely tracks measurable growth in DVT-secured ETH and on-chain network fees rather than market beta.

---

## Notable History

- **2021** — ssv.network emerges from the Blox / bloxapp team; backers include Coinbase Ventures and OKX Ventures.
- **2022-2023** — Testnets and the rollout of the DVT protocol; integration work with staking pools and liquid-staking providers begins.
- **2023-2024** — **Lido's Simple DVT module** adopts SSV (alongside Obol), a landmark validation of DVT for large-scale staking. SSV reached its all-time high of **$65.82 on 2024-03-25** during the restaking/staking-infra hype cycle.
- **2024-2025** — Announcement of **SSV 2.0**, expanding from pure validator DVT toward restaking-secured "based applications."
- **2026** — Token set a new all-time low of $1.85 (2026-06-06) in the broad bear market before stabilizing around $2.35.

---

## Risks

- **Slashing risk** — As validator infrastructure, SSV-secured validators are exposed to Ethereum **slashing**: a faulty DVT cluster, a consensus bug, or operator misbehavior could cause slashing of the underlying staked ETH, damaging trust in the network and the token. This is the defining risk for a DVT protocol.
- **Operator-set / liveness risk** — DVT relies on a healthy, decentralized operator set; if too many operators are correlated (same cloud, same jurisdiction) the fault-tolerance benefit erodes, and threshold failures could take validators offline.
- **Competitive risk** — Obol Network competes directly in DVT; if liquid-staking providers favor a rival, SSV's fee and adoption growth slows.
- **Dependency / concentration risk** — Much of SSV's relevance hinges on adoption by a few large players (e.g., [[lido|Lido]]); a shift in their DVT choices would materially affect demand.
- **Restaking-narrative risk** — SSV 2.0's restaking pivot ties part of the thesis to the broader [[restaking]] / [[eigenlayer]] ecosystem, which carries its own systemic and slashing-cascade risks.
- **Macro risk** — In an extreme-fear, established-bear regime ([[crypto-fear-and-greed-index|Fear & Greed]] 23), low-cap infra tokens are prone to liquidity drought despite SSV's recent weekly strength.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[restaking]]
- [[liquid-staking]]
- [[lido]]
- [[eigenlayer]]
- [[threshold-network-token]]
- [[uma]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SSV |
| **Market Cap Rank** | #645 |
| **Market Cap** | $29.94M |
| **Current Price** | $2.04 |
| **Categories** | Decentralized Finance (DeFi), Restaking, Liquid Staking |
| **Website** | [https://ssv.network/](https://ssv.network/) |

---

## Overview

SSV promotes decentralization, security, and liveness across the Ethereum consensus layer and forms the foundation of SSV.network – a fully decentralized and robust ETH staking network. Using the network will be open and simple for anyone who wants to run an Ethereum validator; from DIY users all the way to staking pools and big institutional staking services. This applies to using the network both as a user or a service provider; regardless of staking configuration, as long as duties are properly executed, anyone is eligible to provide service and reap rewards for doing so.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 14.70M SSV |
| **Total Supply** | 14.70M SSV |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $29.94M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $65.82 (2024-03-25) |
| **Current vs ATH** | -96.91% |
| **All-Time Low** | $1.85 (2026-06-06) |
| **Current vs ATL** | +10.24% |
| **24h Change** | +1.43% |
| **7d Change** | -1.51% |
| **30d Change** | -15.53% |
| **1y Change** | -79.66% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x9d65ff81a3c488d585bbfb0bfe3c7707c7917f54` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SSV/USDT | N/A |
| Kraken | SSV/USD | N/A |
| Bitget | SSV/USDT | N/A |
| KuCoin | SSV/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X9D65FF81A3C488D585BBFB0BFE3C7707C7917F54/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ssv.network/](https://ssv.network/) |
| **Twitter** | [@ssv_network](https://twitter.com/ssv_network) |
| **Discord** | [https://discord.com/invite/eDXSP9R](https://discord.com/invite/eDXSP9R) |
| **GitHub** | [https://github.com/bloxapp/ssv-web](https://github.com/bloxapp/ssv-web) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 19 |
| **GitHub Forks** | 25 |
| **Commits (4 weeks)** | 2 |
| **Pull Requests Merged** | 1,668 |
| **Contributors** | 21 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.20M |
| **Market Cap Rank** | #645 |
| **24h Range** | $2.00 — $2.06 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
