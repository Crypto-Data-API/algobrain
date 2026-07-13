---
title: "Radix"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, defi]
aliases: ["XRD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.radixdlt.com/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[staking]]", "[[consensus-mechanism]]", "[[ethereum]]", "[[casper-network]]", "[[icon]]"]
---

# Radix

**Radix** (XRD) is a [[layer-1]] platform built specifically for DeFi, designed around asset-oriented [[smart-contracts]] and a sharded, parallelized [[consensus-mechanism]] called **Cerberus**. Its differentiators are a developer environment purpose-built for finance — the **Radix Engine** and the **Scrypto** programming language, where tokens and other assets are native, first-class objects rather than balances tracked inside contract code. As of 2026-06-22 XRD trades at **$0.00106466**, ranked **#979** by market capitalization (mcap **$14,337,545**), down **3.98%** on the day and down **4.19%** over the trailing week within a broad crypto bear regime (BTC bear market; Fear & Greed Index 21 / Extreme Fear).

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XRD |
| **Market Cap Rank** | #979 |
| **Market Cap** | $14,337,545 |
| **Current Price** | $0.00106466 |
| **24h Change** | -3.98% |
| **7d Change** | -4.19% |
| **Categories** | Smart Contract Platform, Layer 1 (L1), DWF Labs Portfolio, Radix Ecosystem |
| **Website** | [https://www.radixdlt.com/](https://www.radixdlt.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Radix is a [[layer-1]] blockchain built from the ground up for DeFi, with the stated goal of being a secure, scalable home for financial [[smart-contracts]]. Rather than adopting a general-purpose EVM design, Radix made deliberate architectural choices aimed at the specific failure modes of DeFi — hacks, exploits, and composability bugs. Its three central pieces are the **Cerberus** [[consensus-mechanism]], the **Radix Engine** virtual machine, and the **Scrypto** asset-oriented programming language.

The native token **XRD** is used to pay transaction (gas) fees, to [[staking|stake]] for and delegate to validators that secure the network, and for network economics and governance. XRD has a defined maximum supply (24B), with circulating supply expanding via staking emissions.

---

## Architecture & Consensus

- **Cerberus consensus** — a [[proof-of-stake]] BFT [[consensus-mechanism]] designed to be **sharded** so that transactions touching different state can be processed in parallel, with cross-shard atomic composability ("braiding") intended to preserve DeFi's requirement that interdependent operations either all succeed or all fail. The aim is to scale throughput horizontally without sacrificing the atomic composability that DeFi depends on.
- **Radix Engine** — an asset-oriented virtual machine where tokens and other resources are native primitives the platform understands directly, rather than ad-hoc balances stored inside arbitrary contract logic (as with ERC-20 on [[ethereum]]). This is meant to make whole classes of token-handling bugs structurally impossible.
- **Scrypto** — a Rust-based smart-contract language built for the Radix Engine, designed so that handling assets is safe by default and developers work with finance-native abstractions (vaults, resources, blueprints).

Radix's pitch is therefore reliability and developer safety for financial applications, trading the network-effect advantages of EVM compatibility for an architecture it argues is fundamentally better suited to DeFi.

### The asset-oriented model in practice

The core conceptual difference from [[ethereum]] is *where tokens live*. On the EVM, an ERC-20 token is a balance number stored inside a contract's own storage; every transfer is bespoke contract code, which is why bugs like reentrancy, missing-return-value handling, and approval exploits recur. On Radix, a token is a **resource** the platform itself understands; tokens are held in **vaults** and moved through **buckets** with platform-enforced rules ("you cannot accidentally lose or duplicate a resource"). This is the source of Radix's claim that whole categories of token-handling bugs are made structurally impossible rather than merely discouraged by good coding practice. Scrypto developers compose **blueprints** (reusable component templates) and instantiate **components**, and the network's transaction model uses an explicit "transaction manifest" that lays out intended asset movements, improving how clearly a wallet can show users what a transaction will do.

### Roadmap: Babylon, Cerberus, Xi'an

Radix has shipped in phases. The **Babylon** upgrade brought the full Radix Engine v2, Scrypto, and the asset-oriented programming model to mainnet, enabling the current DeFi ecosystem. The fully **sharded Cerberus** consensus — the piece that delivers Radix's horizontal-scalability thesis with cross-shard atomic composability ("braiding") — has been the longer-horizon goal (associated with the project's "Xi'an" milestone). As with any ambitious scaling roadmap, delivery timelines and real-world throughput should be verified against official sources rather than assumed; the asset-oriented programming model is live today, while full unbounded sharding is the forward-looking promise.

---

## Comparison vs Peer Layer-1s

| Network | Consensus | Execution / VM | Language | EVM-compatible | Core thesis |
|---|---|---|---|---|---|
| **Radix** ([[radix]]) | Cerberus (sharded BFT PoS) | Radix Engine | Scrypto (asset-oriented) | No | DeFi-first; asset-native safety + horizontal sharding |
| [[ethereum]] | PoS (Gasper) | EVM | Solidity / Vyper | Yes (native) | General-purpose; deepest DeFi liquidity |
| [[casper-network]] | PoS → Zug (BFT) | WASM | Rust → WASM | No | Enterprise / RWA; upgradable contracts |
| [[icon]] | Delegated PoS (P-Reps) | Goloop / JVM | SCORE (Java/Python) | Partial | Cross-chain messaging |
| Solana | PoH + PoS | SVM | Rust | No | High throughput, parallel execution |
| Sui / Aptos | BFT PoS | Move VM | Move (resource-oriented) | No | Object/resource-oriented safety |

Radix's closest philosophical cousins are the **Move-based chains (Sui, Aptos)**, which also treat assets as first-class, ownership-tracked resources rather than contract-internal balances. Radix and Move chains share the bet that a finance-native object model is safer than the EVM; they differ in language and consensus design. Against EVM incumbents and Solana, Radix's handicap is liquidity and developer network effects — the same non-EVM adoption hurdle faced by [[casper-network]].

---

## Governance & Token Economics

Network economics center on **XRD staking**. Validators run nodes and are selected/weighted by stake; XRD holders delegate to validators and share in **staking emissions**, which expand circulating supply toward the 24B max. Network transaction fees are paid in XRD and a portion is burned, creating a usage-linked fee sink that partly offsets emissions (so heavier on-chain activity is mildly deflationary at the margin). Governance has historically been steered by **RDX Works** (the development company) and the **Radix Foundation**, with the long-term aim of progressively decentralizing protocol decision-making to validators and the community. The validator set's size and stake distribution are the practical determinants of how decentralized the network really is, and — as with all delegated-stake L1s — should be checked against on-chain data rather than assumed.

---

## Notable History

- **DLT research origins.** Radix grew out of years of distributed-ledger research (the project, founded by Dan Hughes, predates many of its peers in conceptual work) aimed specifically at solving scalability without sacrificing atomic composability for DeFi.
- **2021 token migration and ATH.** The eToken/XRD ecosystem moved to the current XRD design, and XRD reached an all-time high near **$0.6513** on 2021-11-14 at the bull-market peak before a >99.8% decline.
- **2023 — Babylon mainnet upgrade.** Babylon delivered the full asset-oriented programming model (Radix Engine v2, Scrypto, transaction manifests, the Radix Wallet with smart-account features), turning Radix from a token-ledger into a programmable DeFi [[layer-1]] and seeding the current ecosystem of DEXes and lending markets.
- **DWF Labs involvement.** XRD is tagged as part of the DWF Labs portfolio, reflecting market-maker/investor involvement (a relationship that, as with any market-maker tie, can affect liquidity and price dynamics).
- **January 2026 — All-time low.** XRD printed an all-time low around **$0.00101084** on 2026-01-10 during the deep small-cap [[crypto-markets]] drawdown; it trades only modestly above that level amid the current Extreme Fear regime.

---

## Ecosystem & Adoption

Radix has a self-contained ecosystem of DEXes, lending markets, and other DeFi primitives built in Scrypto, plus tooling such as the Radix Wallet. The deliberate decision **not** to be EVM-compatible is double-edged: it enables the asset-oriented model but also means Radix cannot trivially attract the large pool of existing Solidity developers, liquidity, and tooling. XRD trades roughly 99.8% below its 2021 all-time high (~$0.65) and sits near rank #959 with a sub-$15M market cap, reflecting both the broad altcoin downturn and the challenge of bootstrapping an ecosystem outside the dominant EVM standard.

---

## Risks

- **Non-EVM adoption hurdle** — a bespoke language (Scrypto) and VM mean a smaller developer pool and weaker composability with the wider [[ethereum]]/EVM DeFi world; ecosystem growth is the key uncertainty.
- **Competition** — Radix competes against entrenched EVM L1/L2 DeFi hubs and other "DeFi-first" or parallelized chains (e.g., Solana, Sui, Aptos) for liquidity and builders.
- **Liquidity is very thin** — XRD has a low market cap, a low rank, and historically light trading volume across few venues, so entering or exiting size can move the price significantly.
- **Execution / roadmap risk** — full sharded Cerberus and scaling targets are ambitious; delivery and real-world throughput should be verified rather than assumed.
- **Severe price decay** — a ~99.8% drawdown from all-time high underscores weak long-term momentum.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 13.41B XRD |
| **Total Supply** | 13.41B XRD |
| **Max Supply** | 24.00B XRD |
| **Fully Diluted Valuation** | $16.77M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.6513 (2021-11-14) |
| **Current vs ATH** | -99.81% |
| **All-Time Low** | $0.00101084 (2026-01-10) |
| **Current vs ATL** | +23.76% |
| **24h Change** | -1.56% |
| **7d Change** | +6.85% |
| **30d Change** | -33.13% |
| **1y Change** | -84.47% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | XRD/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.radixdlt.com/](https://www.radixdlt.com/) |
| **Twitter** | [@radixdlt](https://twitter.com/radixdlt) |
| **Reddit** | [https://www.reddit.com/r/Radix/](https://www.reddit.com/r/Radix/) |
| **Telegram** | [radix_dlt](https://t.me/radix_dlt) (19,258 members) |
| **Discord** | [https://discord.com/invite/WkB2USt](https://discord.com/invite/WkB2USt) |
| **GitHub** | [https://github.com/radixdlt](https://github.com/radixdlt) |
| **Whitepaper** | [https://www.radixdlt.com/whitepapers](https://www.radixdlt.com/whitepapers) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $125,916.00 (2026-04-09 snapshot) |
| **Market Cap Rank** | #979 |
| **Price (2026-06-22)** | $0.00106466 |
| **24h Change (2026-06-22)** | -3.98% |
| **7d Change (2026-06-22)** | -4.19% |
| **CoinGecko Sentiment** | 50% positive |
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
- [[layer-1]]
- [[proof-of-stake]]
- [[smart-contracts]]
- [[staking]]
- [[consensus-mechanism]]
- [[ethereum]]
- [[casper-network]]
- [[icon]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market data snapshot
- General market knowledge; no other specific wiki source ingested yet. Market figures dated 2026-06-22 are from cryptodataapi.com / CoinGecko (BTC bear regime; Fear & Greed Index 21 / Extreme Fear).
