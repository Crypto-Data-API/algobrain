---
title: "Pocket Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["POKT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.pokt.network/"
related: ["[[crypto-markets]]", "[[dao]]", "[[depin]]", "[[ethereum]]", "[[smart-contract-risk]]", "[[staking]]"]
---

# Pocket Network

**Pocket Network** (POKT) is a decentralized [[depin|DePIN]] network for blockchain **RPC** (Remote Procedure Call) data access — essentially a peer-to-peer alternative to centralized node providers like Infura or Alchemy. Independent operators run full nodes for many chains and earn POKT for serving data requests from applications, while developers gain censorship-resistant, redundant access to on-chain data. POKT is used to [[staking|stake]] nodes, pay/route relays, and govern the protocol.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* In a broad crypto bear regime (BTC ~$64,390; Fear & Greed Index 21 — "Extreme Fear"), POKT traded around **$0.00790723**, ranked **#928** by market cap (~**$15,907,508**), down **-2.31%** on the day and **down -6.96%** over 7 days.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | POKT |
| **Market Cap Rank** | #928 |
| **Market Cap** | $15,907,508 |
| **Current Price** | $0.00790723 |
| **24h Change** | -2.31% |
| **7d Change** | -6.96% |
| **Categories** | BNB Chain Ecosystem, Solana Ecosystem, Polygon Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Optimism Ecosystem, DePIN, Base Ecosystem, Binance Alpha Spotlight, Base Native |
| **Website** | [https://www.pokt.network/](https://www.pokt.network/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Pocket Network is a blockchain data platform that coordinates a decentralized network of node operators to serve **RPC requests** — the read/write data calls that every dApp, wallet, and indexer makes to a blockchain. Most applications today route this traffic through a handful of centralized RPC providers (Infura, Alchemy, QuickNode), creating a single point of failure and censorship for an otherwise decentralized stack. Pocket replaces that with a permissionless marketplace: many operators run nodes for many chains, requests are load-balanced across them, and operators are paid in POKT for verifiably serving valid responses.

This makes Pocket a flagship **[[depin|DePIN]]** (Decentralized Physical Infrastructure Network) project — it incentivizes a real-world fleet of node hardware/bandwidth with token rewards. Pocket supports a wide range of chains ([[ethereum|Ethereum]], Solana, Polygon, BNB Chain, Arbitrum, Optimism, Base, and more) and has historically processed large volumes of daily relays.

### Architecture & mechanism

- **Nodes (servicers)** stake POKT and run full nodes for one or more chains; the higher the stake, the more relays they can be assigned.
- **Apps / gateways** stake POKT (or pay via a gateway) to get an allowance of relays; the protocol routes their requests to staked nodes.
- **Proof-of-relay** — nodes must cryptographically prove they served valid responses to earn rewards, deterring free-riding and bad data.
- The protocol has evolved toward a **gateway/marketplace** model (often referred to as Pocket's "Shannon"/morse upgrades and Grove gateway) to improve quality-of-service and usability for developers who want a managed endpoint backed by the decentralized supply.

### Token role

The **POKT** token underpins the network:

- **Staking** — node operators stake POKT to provide service; apps stake to consume relays.
- **Work/payment** — POKT is the unit in which relay work is rewarded and (via the marketplace/gateway model) demand is settled.
- **Governance** — POKT holders (and the DAO) govern protocol parameters such as emissions and relay economics.

---

## Architecture Deep Dive

Pocket is a textbook **[[depin|DePIN]]** marketplace: it coordinates real-world hardware (full nodes serving many chains) with a token-incentive layer, and routes paying demand to that supply.

- **Supply side — servicers.** Independent operators run full archival/RPC nodes for one or more supported chains and [[staking|stake]] POKT to register as servicers. A higher stake entitles a node to be assigned a larger share of relays. Operators provide the bandwidth, storage, and uptime; the protocol provides demand and payment.
- **Demand side — apps & gateways.** Applications historically staked POKT to receive a metered allowance of relays; under the gateway/marketplace model they instead consume a managed endpoint (e.g., **Grove**, the gateway spun out of Pocket) that buys capacity from the decentralized supply and abstracts the staking mechanics away from developers.
- **Proof-of-relay (the core cryptoeconomic primitive).** To earn rewards, a node must cryptographically prove it served a *valid* response to a *real* request. A challenge/commit-reveal style proof and probabilistic sampling deter free-riding (claiming work never done) and serving bad data. This is what makes a permissionless RPC marketplace trustworthy without a central referee.
- **Multi-chain QoS routing.** Requests are load-balanced across many independent nodes per chain, giving redundancy and censorship-resistance that a single centralized provider cannot. The hard part — matching centralized latency/uptime — is addressed at the gateway layer.
- **Morse → Shannon migration.** Pocket's original chain ("Morse") is being succeeded by **Shannon**, a Cosmos-SDK rebuild designed to make demand settlement, relay accounting, and tokenomics more flexible and to better tie emissions to *paid* usage rather than raw relay counts. This re-architecture is the central forward-looking event for the protocol.

---

## Comparison vs RPC / DePIN Peers

| Dimension | **Pocket Network** | Infura | Alchemy | QuickNode | The Graph (indexing) |
|---|---|---|---|---|---|
| Model | **Decentralized [[depin\|DePIN]] marketplace** | Centralized (ConsenSys) | Centralized | Centralized | Decentralized indexing |
| What it serves | RPC relays (many chains) | RPC + APIs | RPC + enhanced APIs | RPC + add-ons | GraphQL queries (indexed data) |
| Censorship-resistance | **High (many operators)** | Low (single provider) | Low | Low | High |
| Single point of failure | No (redundant nodes) | Yes | Yes | Yes | No |
| Token | POKT (stake + pay relays) | None | None | None | GRT |
| Trust model | Proof-of-relay + staking | Trust the provider | Trust the provider | Trust the provider | Indexer staking + curation |
| Main weakness | Matching centralized latency/QoS | Centralization risk | Centralization risk | Centralization risk | Different layer (data, not RPC) |

Pocket's competitive pitch is **resilience and neutrality for a critical, otherwise-centralized layer**: most "decentralized" apps still funnel their RPC traffic through one or two companies, which is a real single-point-of-failure and censorship vector. Its challenge is that production teams demand centralized-grade latency and uptime, which the gateway model exists to deliver.

---

## Governance & Value Accrual

- **POKT DAO.** Protocol parameters — emission rates, relay reward economics, supported chains, treasury — are set by POKT governance, historically via the PNF (Pocket Network Foundation) and on-chain/community processes.
- **Value-accrual challenge.** POKT is fundamentally a *work token*: its value should reflect the demand to perform (and pay for) relay work. The structural tension — shared by most DePIN tokens — is the **emissions-vs-demand balance**: early on, inflationary POKT emissions bootstrap node supply faster than paid demand materialises, creating sell pressure. The Shannon migration and successive tokenomics reforms explicitly aim to dampen inflation and route real demand revenue to suppliers, tightening the link between usage and token value.
- **Unlimited max supply.** POKT has no hard cap; the *net* inflation rate (emissions minus any burn/demand sinks) is the key metric, not a supply ceiling.

---

## Notable History

- **2021 peak.** POKT reached its all-time high of ~$3.11 in January 2022 during the height of the infrastructure/DePIN narrative, then declined ~99% in the subsequent bear market — typical of bootstrap-emission infrastructure tokens.
- **Grove gateway spinout.** The team behind Pocket's managed-gateway product (Grove) became a major demand-aggregation front-end, packaging the decentralized supply into a developer-friendly endpoint.
- **Shannon upgrade.** The Cosmos-SDK rebuild ("Shannon") represents Pocket's most significant re-architecture, modernising relay accounting and demand settlement to make the marketplace genuinely demand-driven rather than emission-driven.

---

## Competitive Position & Risks

Pocket competes directly with centralized RPC giants on price, reliability, and breadth of chain support, and within DePIN against other infrastructure-incentive networks. Its pitch is resilience and decentralization for a critical, otherwise-centralized layer of the stack.

Key risks:

- **DePIN demand-vs-emissions balance** — like most DePIN tokens, POKT historically relied on **inflationary emissions** to bootstrap node supply. The hard problem is converting that supply into genuine, paid relay demand; if emissions outpace real usage revenue, the token faces persistent sell pressure. Tokenomics changes have aimed to reduce inflation and tie rewards more tightly to demand.
- **Centralized-incumbent competition** — Infura/Alchemy/QuickNode are well-funded, fast, and deeply integrated into developer tooling; switching costs and reliability expectations are high.
- **Infrastructure-narrative dependence** — POKT's fortunes track interest in decentralized infrastructure/[[depin|DePIN]], which is cyclical.
- **Quality-of-service** — decentralized RPC must match centralized latency/uptime to win serious production traffic; the gateway model is a response to this.
- **Low liquidity** — at a ~$16.2M market cap, POKT is a small-cap token prone to sharp moves on thin volume; it trades roughly 99% below its 2022 all-time high.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.01B POKT |
| **Total Supply** | 2.35B POKT |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $30.74M |
| **Market Cap / FDV Ratio** | 0.86 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.11 (2022-01-16) |
| **Current vs ATH** | -99.58% |
| **All-Time Low** | $0.00883573 (2025-04-17) |
| **Current vs ATL** | +47.63% |
| **24h Change** | -1.87% |
| **7d Change** | +3.47% |
| **30d Change** | -16.80% |
| **1y Change** | +31.78% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x764a726d9ced0433a8d7643335919deb03a9a935` |
| Base | `0x764a726d9ced0433a8d7643335919deb03a9a935` |
| Solana | `6CAsXfiCXZfP8APCG6Vma2DFMindopxiqYQN4LSQfhoC` |
| Polygon Pos | `0x764a726d9ced0433a8d7643335919deb03a9a935` |
| Binance Smart Chain | `0x764a726d9ced0433a8d7643335919deb03a9a935` |
| Optimistic Ethereum | `0x764a726d9ced0433a8d7643335919deb03a9a935` |
| Arbitrum One | `0x764a726d9ced0433a8d7643335919deb03a9a935` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Upbit | POKT/KRW | N/A |
| KuCoin | POKT/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | 6CASXFICXZFP8APCG6VMA2DFMINDOPXIQYQN4LSQFHOC/SO11111111111111111111111111111111111111112 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.pokt.network/](https://www.pokt.network/) |
| **Twitter** | [@POKTnetwork](https://twitter.com/POKTnetwork) |
| **Telegram** | [POKTnetwork](https://t.me/POKTnetwork) (3,535 members) |
| **Discord** | [https://discord.gg/pocket-network](https://discord.gg/pocket-network) |
| **GitHub** | [https://github.com/pokt-network](https://github.com/pokt-network) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.13M |
| **Market Cap Rank** | #894 |
| **24h Range** | $0.0130 — $0.0135 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[depin]]
- [[ethereum]]
- [[staking]]
- [[dao]]
- [[smart-contract-risk]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
