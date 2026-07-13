---
title: "Orbs"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ethereum, defi]
aliases: ["ORBS", "Orbs Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.orbs.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[smart-contracts]]"]
---

# Orbs

**Orbs** (ORBS) is a decentralized execution layer that positions itself as a **"Layer-3" (L3)** — a programmable backend that runs alongside [[ethereum]] and other [[layer-1]]/[[layer-2]] chains rather than competing with them. Its decentralized network of [[proof-of-stake|proof-of-stake]] validators ("Guardians") executes logic that base-layer [[smart-contracts]] cannot perform efficiently, such as scheduled and conditional on-chain orders. Orbs is best known in [[defi]] for its execution-layer products **dTWAP** and **dLIMIT** (decentralized time-weighted-average-price and limit orders) and its **Liquidity Hub** aggregation layer. It currently ranks **#646** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 ORBS trades at **$0.00598756** with a market cap of **$29,724,484** (rank **#646**), up **+1.04%** over 24h and down **-1.67%** over the prior 7 days — broadly flat amid an Extreme Fear market (Fear & Greed 22; BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ORBS |
| **Market Cap Rank** | #646 |
| **Market Cap** | $29,724,484 |
| **Current Price** | $0.00598756 |
| **24h Change** | +1.04% |
| **7d Change** | -1.67% |
| **Consensus** | [[proof-of-stake]] (delegated; "Guardians" / Helix consensus) |
| **Categories** | Infrastructure, Smart Contract Platform, Decentralized Finance ([[defi]]), Layer 3 (L3) |
| **Website** | [https://www.orbs.com/](https://www.orbs.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Orbs originally launched (mainnet 2019) as a public [[proof-of-stake]] blockchain aimed at giving enterprises the auditability of a public chain with performance closer to a private one. Over time the project re-positioned itself as an **execution layer** — a network of independent validator nodes that perform computation *between* and *on behalf of* EVM smart contracts on existing chains. Orbs describes this role as a "Layer-3," sitting above [[layer-1]] settlement and [[layer-2]] scaling: instead of holding state itself, it triggers and orchestrates actions on the underlying chains.

The Orbs network is secured by **Guardians** (validators) who run nodes and are elected/backed by ORBS stakers through a delegation model. The protocol uses a randomized leaderless consensus design (historically branded "Helix") and a Proof-of-Stake universe in which delegators share in network rewards for backing reputable Guardians.

---

## Architecture & Edge / What Makes Orbs Distinct

Orbs' core insight is that a base-layer [[smart-contracts|smart contract]] is reactive — it only runs when someone sends it a transaction — and cannot, on its own, *schedule* future actions or react to time/price conditions. Orbs supplies a decentralized network of validators ("Guardians") that monitor conditions off-chain and trigger the necessary on-chain transactions, effectively giving DEXs the "always-on backend" that centralized exchanges have natively. Value scales with the **volume of execution work** routed through the network: the more orders, TWAPs and aggregated swaps protocols push through Orbs, the more validator activity (and the staking demand that secures it) the system requires.

- **Helix consensus / Guardians**: Orbs runs a randomized, leaderless [[proof-of-stake]] consensus (historically branded **Helix**) across independent validator nodes ("Guardians"), elected and backed by ORBS delegators. This is what lets the execution services be *decentralized* rather than a single keeper bot.
- **Decentralized execution services**: Orbs validators can run logic that a single EVM transaction cannot — notably splitting a large order into many smaller timed executions. This is the basis of **dTWAP** (decentralized time-weighted-average-price) and **dLIMIT** (decentralized limit/stop orders), which let decentralized exchanges offer order types normally associated with centralized venues. These are integrated by DEXs such as QuickSwap, SpookySwap, PancakeSwap and others.
- **Liquidity Hub**: an aggregation/optimization layer that sources liquidity for DEX swaps to reduce [[slippage]], routing trades to the best available execution across integrated liquidity sources.
- **Chain-agnostic**: deployed across [[ethereum]], BNB Chain, Polygon, [[arbitrum]], Avalanche, Fantom and others (see contract addresses below), so its execution layer is not tied to one ecosystem. This breadth is the moat — and the maintenance burden.

---

## Comparison vs Competing Execution / Order-Infra Layers

Orbs occupies an unusual niche: decentralized off-chain execution infrastructure for on-chain order types. Its competitors are a mix of keeper networks, intent layers, and native DEX order tooling:

| Dimension | **Orbs (ORBS)** | **Gelato Network** | **Chainlink Automation** | **CoW Protocol** |
|---|---|---|---|---|
| **Primary role** | Decentralized TWAP/limit execution + Liquidity Hub | Web3 functions / automation + RaaS | Decentralized keepers / automation | Intent-based batch-auction DEX |
| **Security model** | PoS Guardians (Helix) | Executor network | Decentralized oracle network | Solver competition |
| **Best-known for** | dTWAP / dLIMIT for DEXs | Automated smart-contract tasks | Reliable on-chain triggers | MEV-protected swaps, CoWs |
| **Token** | ORBS (stake/delegate) | GEL | LINK | COW |
| **Positioning** | "Layer-3" execution backend | Automation middleware | Oracle/automation standard | Trade-intent settlement |

Orbs' differentiation is its **specialization in advanced DEX order types** (TWAP/limit) delivered as a turnkey integration; [[chainlink]] Automation and Gelato are more general-purpose automation, while CoW Protocol solves a related but distinct problem (intent batching / MEV protection). The "Layer-3 execution backend" framing overlaps with the broader [[intent]]-centric trend that [[anoma]] also targets.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.93B ORBS |
| **Total Supply** | 10.00B ORBS |
| **Max Supply** | 10.00B ORBS |
| **Fully Diluted Valuation** | $89.95M |
| **Market Cap / FDV Ratio** | 0.49 |

A ~0.49 cap/FDV ratio means roughly half the 10B max supply is already circulating; the remainder is staking rewards/inflation rather than locked VC cliffs, so dilution is gradual rather than concentrated in unlock events. This is a middle ground between high-float legacy tokens like [[cartesi|CTSI]] (~0.91) and low-float new launches like [[caldera|ERA]] (~0.17).

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3604 (2021-03-16) |
| **Current vs ATH** | -97.50% |
| **All-Time Low** | $0.00469039 (2019-12-20) |
| **Current vs ATL** | +91.78% |
| **24h Change (2026-06-21)** | +1.04% |
| **7d Change (2026-06-21)** | -1.67% |

> *Earlier 30d/1y figures from the 2026-06-12 snapshot are superseded by the 2026-06-21 figures above.*

---

## ORBS Token

The ORBS token has a fixed total/max supply of 10 billion (~4.93B circulating). It is used to:

- **Stake and delegate** to Guardians, securing the [[proof-of-stake]] network and earning a share of rewards;
- **Pay/settle** for execution-layer services on the network;
- Provide the economic alignment ("skin in the game") that backs honest validator behavior.

ORBS is an ERC-20-style token deployed natively on [[ethereum]] and bridged across multiple chains, rather than the gas coin of a standalone L1.

---

## How & Where It Trades

- **Spot venues:** ORBS trades on **Upbit** (ORBS/KRW — a notable Korean-market presence), **Bitget** and **KuCoin** (ORBS/USDT), plus on-chain on **Uniswap V2** and **SushiSwap** (ORBS/WETH) on [[ethereum]].
- **Derivatives / perps:** ORBS has live perpetual-futures markets — an **ORBS-PERP** on [[hyperliquid]] and stablecoin-margined perps listed on **KuCoin, Binance, OKX, Bybit and MEXC** (per CoinGlass funding feed, snapshot 2026-06-22). On that date the KuCoin ORBS perp showed a **negative funding rate (~−0.28%)**, meaning **longs were paying shorts / positioning skewed short**, consistent with the broad Extreme-Fear, bearish small-cap tape.
- **Liquidity profile:** ~$4.8M reported 24h spot volume against a ~$30M cap; turnover is moderate but the book is thin in absolute terms. Korean (Upbit) flow can drive outsized, news-independent moves.
- **Korea premium / venue concentration:** the prominent Upbit KRW pair means ORBS price can decouple from global pairs during Korean retail surges — a known source of volatility for this token.

---

## Narrative, Category & Catalysts

Orbs' narrative is **decentralized execution infrastructure / "Layer-3"** for [[defi]]. Its fortunes are tied less to a single chain and more to the breadth of DEX integrations using dTWAP, dLIMIT and the Liquidity Hub — a "picks-and-shovels" thesis for on-chain order flow.

**Potential catalysts:**
- New, high-volume DEX integrations of dTWAP / dLIMIT / Liquidity Hub (more order flow → more execution work → more staking demand).
- Growth in on-chain perp/spot DEX volume generally (Orbs is a beneficiary of the broader "DEXs eat CEX order types" trend).
- Expansion of the [[intent]]-centric execution narrative, which Orbs predates and overlaps with.

**Headwinds:** native L2 sequencers and DEXs increasingly build order-type tooling in-house, eroding the need for an external execution layer; and the "Layer-3" framing is contested and may not translate into durable token demand.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xff56cc6b1e6ded347aa0b7676c85ab0b3d08b0fa` |
| Fantom | `0x43a8cab15d06d3a5fe5854d714c37e7e9246f170` |
| Harmony Shard 0 | `0xaad96d04f00b718b9ed43e39db8e73de61cef8b7` |
| Binance Smart Chain | `0x43a8cab15d06d3a5fe5854d714c37e7e9246f170` |
| Polygon Pos | `0x614389eaae0a6821dc49062d56bda3d9d45fa2ff` |
| Arbitrum One | `0xf3c091ed43de9c270593445163a41a876a0bb3dd` |
| Avalanche | `0x3ab1c9adb065f3fca0059652cd7a52b05c98f9a9` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Upbit | ORBS/KRW | N/A |
| Bitget | ORBS/USDT | N/A |
| KuCoin | ORBS/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ORBS-PERP | Perpetual |
| Uniswap V2 (Ethereum) | 0XFF56CC6B1E6DED347AA0B7676C85AB0B3D08B0FA/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Sushiswap | 0XFF56CC6B1E6DED347AA0B7676C85AB0B3D08B0FA/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.orbs.com/](https://www.orbs.com/) |
| **Twitter** | [@orbs_network](https://twitter.com/orbs_network) |
| **Reddit** | [https://www.reddit.com/r/ORBS_Network/](https://www.reddit.com/r/ORBS_Network/) |
| **Telegram** | [OrbsNetwork](https://t.me/OrbsNetwork) (48,799 members) |
| **GitHub** | [https://github.com/orbs-network/orbs-spec](https://github.com/orbs-network/orbs-spec) |
| **Whitepaper** | [https://www.orbs.com/orbs-position-paper](https://www.orbs.com/orbs-position-paper) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 324 |
| **GitHub Forks** | 6 |
| **Pull Requests Merged** | 82 |
| **Contributors** | 11 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.78M |
| **Market Cap Rank** | #640 |
| **24h Range** | $0.00885092 — $0.00917823 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Timeline

| Date | Event |
|---|---|
| **2019** | Orbs public [[proof-of-stake]] mainnet launches, originally pitched as an enterprise-grade public chain. |
| **2019-12-20** | All-time low of **$0.00469039**. |
| **2021-03-16** | All-time high of **$0.3604** during the bull market. |
| **2021–2024** | Strategic pivot from "public blockchain" to **decentralized execution layer / "Layer-3,"** shipping dTWAP, dLIMIT and the Liquidity Hub and integrating with multiple DEXs. |
| **Ongoing** | Multi-chain expansion (Ethereum, BNB Chain, Polygon, Arbitrum, Avalanche, Fantom) and perp listings across major venues. |

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

> *Not investment advice. Crypto assets are highly volatile and can go to zero.*

**Technical / protocol**
- **Execution-layer / smart-contract risk**: dTWAP, dLIMIT and Liquidity Hub depend on validator (Guardian) honesty and contract correctness across many chains, widening the attack surface relative to a single-chain protocol.
- **Cross-chain fragility**: maintaining execution services across seven-plus chains multiplies the surface for bridge/contract bugs.

**Adoption / economic**
- **Adoption dependency**: value accrual leans on third-party DEXs and protocols continuing to integrate Orbs execution services; competition from **native L2 order-flow tooling built in-house** is rising.
- **Narrative risk**: the "Layer-3" framing is contested industry-wide and may not translate into durable demand for the token.

**Market / liquidity**
- **Micro-cap liquidity**: at ~$30M market cap and rank #646, ORBS is thinly traded; price can gap on modest flow.
- **Korea-premium volatility**: the prominent Upbit KRW pair can drive sharp, news-independent moves and decoupling from global pairs.

---

## Trading Playbook

> *Educational framing, not advice.*

- **Regime read (2026-06-22):** Established Bear Market, Extreme Fear (F&G 21). ORBS perp funding skewed negative (longs paying shorts) on KuCoin — positioning leans bearish, typical of small caps in this tape.
- **What to watch (bullish):** new high-volume DEX integrations of dTWAP/dLIMIT/Liquidity Hub (the real demand driver), rising on-chain DEX/perp volume broadly, and a market rotation back toward [[defi]] infrastructure.
- **What to watch (bearish):** native L2/DEX order tooling displacing Orbs, fading Upbit/Korean interest, or BTC breaking lower and dragging small caps.
- **Mechanics:** moderate but thin liquidity — limit orders, watch the Upbit KRW pair for Korea-driven spikes, and note that a *liquid perp exists* (Hyperliquid / KuCoin / Binance) so ORBS is one of the few tokens in this batch where a hedge or short is practical. Funding can be used as a positioning/sentiment gauge.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[smart-contracts]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Perp funding/derivatives data from CoinGlass funding feed (crypto-loop daily snapshot, 2026-06-22).
- General market knowledge; no specific wiki source ingested yet.
