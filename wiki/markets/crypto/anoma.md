---
title: "Anoma"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, ethereum]
aliases: ["Anoma Network", "XAN"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://anoma.net/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[interoperability]]", "[[layer-1]]", "[[smart-contracts]]"]
---

# Anoma

**Anoma** (XAN) is an **intent-centric** [[layer-1]] architecture and decentralized operating system for Web3 applications. Its core idea is to let users express *what* outcome they want (an "intent") rather than *how* to execute it; a network of solvers and counterparties then matches and settles those intents. Anoma aims to let a developer write one app that works across any chain, abstracting away the underlying [[interoperability]] plumbing. It currently ranks **#753** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 XAN trades at **$0.00929593** with a market cap of **$23,209,834** (rank **#753**), up **+3.28%** over 24h and up **+6.35%** over the prior 7 days — one of the few gainers in this batch despite an Extreme Fear market (Fear & Greed 22; BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XAN |
| **Market Cap Rank** | #753 |
| **Market Cap** | $23,209,834 |
| **Current Price** | $0.00929593 |
| **24h Change** | +3.28% |
| **7d Change** | +6.35% |
| **Type** | Intent-centric [[layer-1]] / application architecture |
| **Categories** | Infrastructure, Intent, Zero Knowledge (ZK), Privacy Infrastructure, Ethereum & BNB Chain Ecosystems |
| **Backers** | Polychain Capital, Delphi Ventures (per category tags) |
| **Website** | [https://anoma.net/](https://anoma.net/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Anoma describes itself as a decentralized OS powering a unified app layer for Web3. Instead of deploying [[smart-contracts]] that imperatively specify execution, developers build apps whose users submit **intents** — signed declarations of desired end-states (e.g., "swap X for at least Y," "join this auction," "lend under these terms"). Solvers compete to find a set of counterparties and a transaction batch that satisfies everyone's intents, which is then settled on-chain.

This **intent-centric architecture** is Anoma's central differentiator. By matching intents off-path and settling outcomes, Anoma targets richer multi-party coordination (counterparty discovery, barter, auctions) that is awkward to express in a per-contract, account-based model, and it bakes in [[interoperability]] so that an application is not tied to one chain.

---

## Architecture & Edge

Anoma reframes the unit of blockchain interaction from the **transaction** (an imperative "do exactly this") to the **intent** (a declarative "achieve this outcome"). Today's chains force users — or the wallets/aggregators acting for them — to pre-compute the exact execution path; Anoma instead lets users sign a constraint ("I'll give up to X for at least Y of Z, before time T") and delegates the work of finding a satisfying execution to a competitive market of **solvers**. The bet is that this is a more natural primitive for multi-party coordination and a cleaner way to abstract cross-chain complexity. As with all infrastructure, value scales with the **volume and value of intents** routed and settled through the network.

- **Intents over transactions**: users state goals; solvers/provers handle execution. This shifts complexity away from app developers and end users, and is the same primitive now appearing in [[defi]] via [[cow-protocol|CoW]], UniswapX, 1inch Fusion and others — Anoma generalizes it to a full architecture.
- **Counterparty discovery & matching**: Anoma natively supports finding the *other side* of a desired trade or interaction, enabling **multi-party settlement (n-party barter, auctions, ring-trades)** rather than just pairwise swaps — coordination that is awkward to express in a per-contract, account-based model.
- **Distributed solver market**: solvers compete to construct the transaction batch that best satisfies a set of intents; ordering fairness, MEV capture/redistribution, and solver decentralization are the open economic questions of the model.
- **Chain-agnostic / interoperable**: intents can be settled across heterogeneous chains, so "write once, run anywhere" is a design goal rather than a bolt-on bridge; [[interoperability]] is built into the architecture.
- **Privacy lineage**: Anoma's team (Heliax) also built **Namada** (a related privacy/asset-agnostic [[proof-of-stake]] chain); the architecture emphasizes programmable privacy and zero-knowledge techniques.

---

## Comparison vs Intent / Coordination Layers

Intent-centric design is a fast-growing category. Anoma is the most *architecturally* ambitious — a full intent-native OS rather than an app-layer feature:

| Dimension | **Anoma (XAN)** | **CoW Protocol (COW)** | **Across / UniswapX** | **dYdX / [[orbs]] dLIMIT** |
|---|---|---|---|---|
| **Scope** | Full intent-centric architecture / OS | Intent-based DEX (batch auctions) | Intent-based bridging/swaps | Order-type execution add-ons |
| **What's abstracted** | Execution + counterparty + chain | Trade execution + MEV protection | Cross-chain fill | Advanced order types |
| **Solvers** | Open solver market | Solver competition | Relayers/fillers | Keepers/validators |
| **Cross-chain** | Native design goal | Limited | Core feature | Per-integration |
| **Maturity** | Early / pre-broad-adoption | Live, real volume | Live, real volume | Live |
| **Privacy** | Programmable (ZK, Namada lineage) | Minimal | Minimal | Minimal |

Anoma's edge is **breadth** — it targets general multi-party, cross-chain, privacy-aware coordination, not just swaps. The flip side is that focused competitors ([[cow-protocol]], UniswapX) already ship real volume on the narrow problem, while Anoma's broader vision is still proving product-market fit. See [[intent]] and [[interoperability]].

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.50B XAN |
| **Total Supply** | 10.00B XAN |
| **Max Supply** | 10.00B XAN |
| **Fully Diluted Valuation** | $74.80M |
| **Market Cap / FDV Ratio** | 0.25 |

A ~0.25 cap/FDV ratio means only about a quarter of the 10B max supply circulates; the remaining ~75% is subject to **team, investor and ecosystem unlock schedules** (Anoma is venture-backed — Polychain, Delphi per CoinGecko tags). This is a meaningful **future-supply overhang** and a key bear-case input — far more dilutive than fair-launch [[ergo|ERG]] or high-float [[cartesi|CTSI]].

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2728 (2025-09-29) |
| **Current vs ATH** | -97.26% |
| **All-Time Low** | $0.00597404 (2026-03-08) |
| **Current vs ATL** | +55.6% |
| **24h Change (2026-06-21)** | +3.28% |
| **7d Change (2026-06-21)** | +6.35% |

> *Earlier 30d/1y figures from the 2026-06-12 snapshot are superseded by the 2026-06-21 figures above.*

---

## XAN Token

XAN is the native token of the Anoma ecosystem (total/max supply 10B; ~2.5B circulating, so a low market-cap-to-FDV ratio implies sizable future unlocks). Intended utilities include:

- **Fees / settlement** for intent matching and execution across the network;
- **Staking and security** for solvers/validators;
- **Governance** of the protocol.

XAN is a relatively new listing (associated with a Binance Alpha spotlight) and was venture-backed (Polychain, Delphi per CoinGecko category tags).

---

## How & Where It Trades

- **Spot venues:** XAN trades on **Kraken** (XAN/USD), **KuCoin** (XAN/USDT) and **Crypto.com** (XAN/USD), and on-chain as an ERC-20 on [[ethereum]] (with a BNB Chain deployment). As a recent listing it benefits from CEX distribution but lacks the deep, long-tenured liquidity of older tokens.
- **Liquidity profile:** ~$6.1M reported 24h volume against a ~$23M cap — relatively high turnover, characteristic of a young, narrative-driven token where speculation dominates over organic usage. Expect sharp moves in both directions.
- **Derivatives:** no deep, liquid perp market is established for XAN at this size; it is primarily spot-driven, so position sizing is the main risk control.
- **New-listing dynamics:** as a 2025-vintage Binance-Alpha-spotlight token with a low float, XAN's price is highly sensitive to **unlock events, listing news, and narrative rotations** rather than fundamentals.

---

## Narrative, Category & Catalysts

Anoma rides the **intent-centric** narrative — arguably one of the more credible "next primitive" theses in crypto, validated in miniature by the success of intent-based DEXs ([[cow-protocol|CoW]], UniswapX, 1inch Fusion). Anoma's pitch is to generalize that primitive into a full architecture, with a **privacy/ZK** flavor inherited from the Namada lineage.

**Potential catalysts:**
- Mainnet maturation and the first real intent-based applications shipping with live solver markets and genuine cross-chain settlement.
- Broad **intent-centric** narrative strength (the category is gaining mindshare across [[defi]]).
- Namada / privacy ecosystem momentum reflecting back onto Anoma.

**Headwinds / what would hurt:**
- The **75% non-circulating supply** unlocking into a weak market (the dominant near-term bear input).
- Focused intent competitors capturing the practical use cases before Anoma's broader architecture finds product-market fit.
- Continued risk-off in the Established Bear Market punishing speculative, pre-revenue infrastructure tokens hardest.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xcedbea37c8872c4171259cdfd5255cb8923cf8e7` |
| Binance Smart Chain | `0x7427bd9542e64d1ac207a540cfce194b7390a07f` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | XAN/USD | N/A |
| KuCoin | XAN/USDT | N/A |
| Crypto.com Exchange | XAN/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://anoma.net/](https://anoma.net/) |
| **Twitter** | [@anoma](https://twitter.com/anoma) |
| **Discord** | [https://discord.com/invite/anoma](https://discord.com/invite/anoma) |
| **GitHub** | [https://github.com/anoma/anoma](https://github.com/anoma/anoma) |
| **Whitepaper** | [https://github.com/anoma/whitepaper/blob/main/whitepaper.pdf](https://github.com/anoma/whitepaper/blob/main/whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 33,938 |
| **GitHub Forks** | 4,114 |
| **Pull Requests Merged** | 891 |
| **Contributors** | 37 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.09M |
| **Market Cap Rank** | #788 |
| **24h Range** | $0.00715536 — $0.00795972 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Timeline

| Date | Event |
|---|---|
| **2025-09-29** | All-time high of **$0.2728** around the token's debut / listing period. |
| **2025** | XAN listing associated with a **Binance Alpha spotlight**; venture backing from Polychain and Delphi (per CoinGecko category tags). |
| **2026-03-08** | All-time low of **$0.00597404** during the deepening bear. |
| **Ongoing** | Continued protocol development (large GitHub footprint — ~34k stars across the org), with the architecture and Namada-lineage privacy work advancing toward production intent applications. |

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

> *Not investment advice. Crypto assets are highly volatile and can go to zero.*

**Technical / protocol**
- **Early/unproven architecture**: intent-centric systems are a young paradigm; **solver markets, MEV/ordering fairness, and counterparty-discovery economics** are still being validated in production. Decentralizing the solver set without recreating centralization or extraction is unsolved.

**Adoption / economic**
- **Unlock overhang**: only ~25% of supply circulates, so team/investor/ecosystem unlocks are a **meaningful future supply headwind** — the dominant near-term bear input.
- **Adoption risk**: value depends on developers actually building intent-based apps *on Anoma specifically* and on solver liquidity materializing, while focused competitors already capture the narrow use cases.

**Market / liquidity**
- **Micro-cap, new-listing volatility**: at ~$23M and rank #753, XAN is thinly traded, narrative-driven and prone to sharp moves; recent strength can reverse quickly.

---

## Trading Playbook

> *Educational framing, not advice.*

- **Regime read (2026-06-22):** Established Bear Market, Extreme Fear (F&G 21). XAN is a low-float, narrative-driven new listing — high beta, high reflexivity. It showed relative strength in the prior batch, but pre-revenue infra tokens are fragile in risk-off.
- **What to watch (bullish):** the intent-centric narrative gaining momentum across [[defi]], the first real Anoma intent apps shipping with live solver markets, and Namada/privacy tailwinds.
- **What to watch (bearish):** **upcoming token unlocks** (track the vesting schedule closely — ~75% of supply is still locked), narrative rotation away from intents, and BTC breaking to new lows.
- **Mechanics:** thin book, no liquid hedge — size small, use limit orders, and treat unlock dates as scheduled volatility events. Relative-value note: XAN is far more dilution-exposed than fair-launch [[ergo]] or high-float [[cartesi]] peers.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[interoperability]]
- [[smart-contracts]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
