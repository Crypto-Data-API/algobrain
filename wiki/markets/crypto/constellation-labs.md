---
title: "Constellation"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins]
aliases: ["DAG", "Constellation Network", "Constellation Labs"]
entity_type: protocol
headquarters: "United States"
website: "https://constellationnetwork.io/"
related: ["[[crypto-markets]]", "[[directed-acyclic-graph]]", "[[layer-1]]", "[[smart-contracts]]"]
---

# Constellation

**Constellation** (DAG), also known as **Constellation Network**, is a US-based **Directed Acyclic Graph (DAG)** distributed ledger — not a traditional blockchain — built around its **Hypergraph** network and the **Hypergraph Transfer Protocol (HGTP)**. Its design targets **feeless** transactions and **horizontal scaling** (throughput rising as more nodes join), with a stated focus on **validating and securing data feeds and big-data pipelines** rather than acting as a general DeFi chain. It ranks **#951** by market capitalization. See [[directed-acyclic-graph]] for the underlying data-structure concept.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* DAG trades at **$0.00398551**, with a market cap of **$15,477,640** (rank **#951**), down **-8.93%** over 24h and down a steep **-42.64%** over the past 7 days. This is a severe weekly drawdown — far worse than the broad market — during an already risk-off backdrop (Bitcoin ~$64,180; Fear & Greed 22 / Extreme Fear). The cause of the outsized move is not established here and should be investigated before drawing conclusions.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DAG |
| **Market Cap Rank** | #951 |
| **Market Cap** | $15,477,640 |
| **Current Price** | $0.00398551 |
| **24h Change** | -8.93% |
| **7d Change** | -42.64% |
| **Categories** | Layer 1 (L1), Layer 0 (L0), Directed Acyclic Graph (DAG), Made in USA, Smart Contract Platform |
| **Website** | [https://constellationnetwork.io/](https://constellationnetwork.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Constellation replaces the linear "chain of blocks" with a **Directed Acyclic Graph (DAG)** ledger (see [[directed-acyclic-graph]]). Instead of a single ordered chain that all transactions must compete to enter, validated transactions reference multiple prior ones, which lets the network's effective capacity grow as more nodes participate — a design Constellation describes as **horizontal scaling**. The intuitive framing the project uses: a conventional blockchain is like a party where the host supplies fixed resources that eventually run out, whereas Constellation is like a potluck where each new guest (node) brings more resources.

Distinguishing features:

- **Hypergraph & HGTP:** Constellation's core network (Hypergraph) and its Hypergraph Transfer Protocol coordinate validation across the DAG.
- **Feeless transactions:** Like several DAG ledgers (e.g., IOTA, Hedera Hashgraph), Constellation aims to avoid per-transaction gas fees.
- **State Channels / metagraphs:** Application-specific subnetworks ("metagraphs") can run their own logic and tokens while inheriting security from the main network — a way to onboard custom data pipelines and microservices.
- **Data-validation focus:** Constellation has emphasized **securing and validating data feeds** (including reported work with US federal/defense-adjacent partners on data interoperability), positioning DAG as a "data" chain rather than a DeFi-first chain. Such partnership claims are project-stated and not independently verified here.

DAG ledgers trade the simplicity and battle-testedness of linear blockchains for scalability; they also have a different (and historically less scrutinized) security model, which is a consideration when assessing the network.

### Architecture deep dive: Hypergraph, HGTP & metagraphs

- **Hypergraph (L0):** Constellation positions its core as a **Layer-0** coordination/validation fabric (hence the "L0/L1" category tags). The Hypergraph is the global DAG of validation that secures and orders data submitted by the network.
- **HGTP (Hypergraph Transfer Protocol):** the protocol that governs how nodes gossip, validate, and reach consensus over data in the DAG. Constellation's consensus has used a reputation-weighted, "proof-of-reputable-observation"–style design rather than classic PoW/PoS block production.
- **Metagraphs (formerly State Channels):** application-specific subnetworks that run their own logic, data validation, and even their own token, while **inheriting security from the Hypergraph**. Metagraphs are how Constellation onboards custom data pipelines, IoT feeds, and enterprise/defense data-validation workloads — the project's core differentiator versus DeFi-first chains.
- **Feeless at the user level:** like several DAG ledgers ([[iota|IOTA]], Nano), Constellation avoids per-transaction gas, instead securing the network through node staking and reputation. This means value accrues from **staking/security and metagraph activity** rather than gas burn.
- **Data-validation thesis:** Constellation has emphasized securing/validating data feeds and reported work with US federal/defense-adjacent partners (e.g., data interoperability programs). These partnership claims are **project-stated and not independently verified here** and should be confirmed against primary sources.

**Trade-off:** the reputation/DAG model targets throughput and data integrity, but it is **less battle-tested** than Nakamoto-style or large-validator BFT consensus, and its finality/security guarantees differ from [[bitcoin|Bitcoin]]/[[ethereum|Ethereum]]. That novelty is both the bull case (a purpose-built data chain) and a key risk.

---

## Comparison vs DAG / Data-Oriented Ledgers

| Dimension | **Constellation (DAG)** | [[iota\|IOTA (IOTA)]] | Hedera (HBAR) | [[chainlink\|Chainlink (LINK)]] (data, not DAG) |
|---|---|---|---|---|
| **Data structure** | DAG (Hypergraph, L0) | DAG (Tangle) | Hashgraph (aBFT DAG) | Oracle network on other chains |
| **Consensus** | Reputation-weighted HGTP | Coordinator → coordicide history | Asynchronous BFT, governing council | Decentralized oracle nodes |
| **Fees to user** | Feeless | Feeless | Low, fixed USD fees | Pay per oracle request (LINK) |
| **Core focus** | Securing/validating data feeds & pipelines (metagraphs) | IoT / machine data | Enterprise ledger, council-governed | Off-chain data delivery to smart contracts |
| **Governance/centralization** | Reputation set; smaller validator base | Historically coordinator-reliant | 39-member governing council | Node operators + Chainlink Labs |
| **Token role** | Staking/security, metagraph gas/access | Feeless transfer/staking | Gas, staking, governance | Oracle payment, staking |

Constellation's niche — **validating data feeds with security-inheriting metagraphs and US-government-adjacent positioning** — is genuinely differentiated, but it competes for the same "trusted data" mindshare as Chainlink (far larger and more adopted) and other DAG/enterprise ledgers (IOTA, Hedera) with stronger backing.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.84B DAG |
| **Total Supply** | 3.84B DAG |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $33.64M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4518 (2021-08-25) |
| **Current vs ATH** | -98.06% |
| **All-Time Low** | $0.00110189 (2019-03-09) |
| **Current vs ATL** | +694.47% |
| **24h Change** | -8.93% |
| **7d Change** | -42.64% |
| **1y Change** | -74.17% |

> **Severe recent drawdown:** DAG fell **~-42.6% over the past 7 days** (and **-8.93%** in 24h) as of 2026-06-21 — dramatically worse than the broad market over the same window. This kind of move usually reflects a token-specific catalyst (e.g., a large unlock, delisting/liquidity event, partnership reversal, or forced selling) layered on top of risk-off conditions. The specific driver is **not established in this wiki**; treat the price as highly distressed and confirm the cause before acting.

DAG trades roughly **-99%** below its 2021 all-time high.

---

## Token Utility

The DAG token is the native asset used to access and secure the network: it is staked by node operators to participate in validation/consensus and serves as the gas/access asset for the Hypergraph and its metagraphs. Constellation's model is feeless at the user level, so token value accrues more from staking/security and metagraph activity than from per-transaction fees. Verify current staking and metagraph economics against Constellation's documentation.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | DAG/EUR | N/A |
| KuCoin | DAG/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://constellationnetwork.io/](https://constellationnetwork.io/) |
| **Twitter** | [@conste11ation](https://twitter.com/conste11ation) |
| **Reddit** | [https://www.reddit.com/r/constellation/](https://www.reddit.com/r/constellation/) |
| **Telegram** | [constellationcommunity](https://t.me/constellationcommunity) (11,128 members) |
| **GitHub** | [https://github.com/Constellation-Labs/constellation](https://github.com/Constellation-Labs/constellation) |
| **Whitepaper** | [https://github.com/Constellation-Labs/Whitepaper/blob/master/constellation_whitepaper_v0.1.pdf](https://github.com/Constellation-Labs/Whitepaper/blob/master/constellation_whitepaper_v0.1.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 150 |
| **GitHub Forks** | 34 |
| **Pull Requests Merged** | 858 |
| **Contributors** | 15 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-21)** | $0.00398551 |
| **Market Cap (2026-06-21)** | $15,477,640 |
| **Market Cap Rank** | #951 |
| **24h Change** | -8.93% |
| **7d Change** | -42.64% (severe) |
| **Last Updated** | 2026-06-21 |

---

## How & Where DAG Trades

- **Spot venues:** DAG lists on **Kraken** (DAG/EUR), **KuCoin** (DAG/USDT), and historically other mid-tier CEXs. There is no broad Tier-1 spot footprint, which concentrates liquidity on a few venues.
- **Liquidity profile:** ~$15M cap (rank ~#951) with historically modest volume — **thin and easily moved**. The recorded ~-42.6% weekly drop is itself evidence of how violently a low-liquidity, single-venue-dependent token can gap. Slippage on size is severe.
- **Derivatives:** limited perp coverage; leverage on a token already in acute distress is extremely high-risk.
- **Implication:** price discovery is fragile and venue-dependent; a delisting, liquidity withdrawal, or large holder exit can move DAG far more than the broad market (as the 7d move shows).

---

## Narrative, Category & Catalysts

- **Category:** Layer-0/Layer-1 DAG ledger focused on **data validation / "Web3 data" infrastructure**, with a distinctive US-government / defense-adjacent partnership narrative.
- **Bull catalysts:** confirmed, revenue-bearing government or enterprise data-validation contracts; metagraph ecosystem growth; a "DePIN / data infrastructure" narrative revival; clarity that the 2026-06 drawdown was a one-off liquidity event rather than a fundamental break.
- **Bear/structural headwinds:** the **unexplained ~-42.6% 7-day collapse** (cause not established in this wiki — investigate before acting); non-standard, less-tested consensus security; reliance on unverified partnership claims; micro-cap illiquidity; competition from larger data/oracle and DAG networks.

---

## History / Timeline

- **2017–2018:** Constellation founded in the US; ICO-era project pitching a horizontally scalable DAG ledger.
- **2019-03-09:** all-time low around **$0.0011** recorded.
- **2021-08-25:** all-time high of **$0.4518** during the 2021 bull peak.
- **2021–2025:** development around the **Hypergraph**, **HGTP**, and **metagraphs (State Channels)**, with public emphasis on data-validation and US-government-adjacent partnership claims (project-stated, not verified here).
- **2026-06 (week of 2026-06-21):** **severe ~-42.6% 7-day drawdown** — far worse than the broad market; cause not established in this wiki. Treat as a flagged distress event.
- **2026-06-21/22:** DAG trades ~$0.00399, ~99% below ATH, in an Extreme-Fear regime.

> Dates reflect the page's recorded market data and widely documented project history; the **driver of the June 2026 collapse is not sourced here** — confirm independently before drawing conclusions.

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: F&G = 21 (Extreme Fear), established bear market, [[btc-bitcoin|BTC]] ~$64k. DAG is additionally in an acute, unexplained ~-42.6% weekly drawdown.

- **Bias:** elevated caution / avoid until the cause of the 7-day collapse is identified. A token-specific crash of this magnitude in a risk-off market is a red flag, not an automatic dip-buy.
- **Longs:** do **not** "catch the knife" blindly. If trading a potential capitulation bounce, demand confirmation (stabilization, volume normalization, and an *explained* catalyst) and size for total loss.
- **Avoid:** leverage entirely while distress is unresolved; thin single-venue liquidity makes liquidation cascades likely.
- **Risk controls:** treat as distressed; predefine invalidation (new lows on continued elevated volume = thesis broken); verify the cause of the drop before any decision.
- **Watch:** an official explanation of the 7d move, exchange-listing/liquidity status, and any confirmed metagraph/government-contract news as the key fundamental tells.

---

## Risks

- **Acute price distress (flagged):** A ~-42.6% 7-day collapse signals a token-specific stress event. Until the cause is identified, treat DAG as elevated-risk; sharp drops can precede further declines or reflect liquidity withdrawal.
- **Small-cap / liquidity risk:** Market cap is under ~$16M (rank ~#951), with historically modest volume — large slippage and volatility are likely.
- **Non-standard security model:** DAG consensus is less battle-tested than mature blockchain consensus; security and finality properties differ from chains like Bitcoin/Ethereum.
- **Adoption dependence:** The data-validation / government-partnership thesis is the core bull case; if those relationships or metagraph adoption do not materialize (or are overstated), the fundamental case weakens.
- **Cycle risk:** Down ~99% from ATH in an Extreme Fear market.

> Not investment advice. Figures are point-in-time; the unusual 7d drop in particular warrants independent verification before any decision.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[directed-acyclic-graph]]
- [[layer-1]]
- [[smart-contracts]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific dedicated Constellation source has been ingested into the wiki yet. The driver of the 2026-06 price drop is not sourced in this wiki.
