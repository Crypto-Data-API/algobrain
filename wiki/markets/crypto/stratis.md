---
title: "Stratis"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["STRAX", "Stratis Platform"]
entity_type: protocol
founded: 2016
headquarters: "United Kingdom"
website: "https://www.stratisplatform.com/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[layer-1]]", "[[proof-of-stake]]", "[[proof-of-work]]", "[[smart-contracts]]"]
---

# Stratis

**Stratis** (STRAX) is an enterprise-focused [[layer-1|Layer-1]] blockchain development platform built on the Microsoft **.NET / C#** stack, targeting businesses — particularly in financial services — that want to develop, test, and deploy blockchain applications and private sidechains without standing up their own infrastructure. Stratis positions itself as a "blockchain-as-a-service" (BaaS) platform and uses a [[proof-of-stake|Proof-of-Stake]] consensus model. The STRAX token is the native asset used for staking, fees, and as the base currency of the Stratis ecosystem. As of 2026-06-22 STRAX trades at **$0.01089312**, ranked **#742** with a market cap of **$23,772,621**; it is **+15.20%** over 24h and **+18.54%** over 7 days — a sharp idiosyncratic rally that stands out strongly against the broad Extreme-Fear backdrop (see [Price History](#price-history)).

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | STRAX |
| **Market Cap Rank** | #742 |
| **Market Cap** | $23,772,621 |
| **Current Price** | $0.01089312 |
| **24h Change** | +15.20% |
| **7d Change** | +18.54% |
| **Genesis Date** | 2016-08-09 |
| **Consensus** | [[proof-of-stake|Proof-of-Stake]] |
| **Tech Stack** | C# / .NET |
| **Categories** | [[layer-1|Layer 1 (L1)]], Enterprise / BaaS, [[smart-contracts|Smart Contracts]] |
| **Website** | [https://www.stratisplatform.com/](https://www.stratisplatform.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

> *Subject-integrity note: this page previously carried a corrupted title ("Xertra") and website; the canonical project is **Stratis** (STRAX), restored here.*

---

## Overview

Stratis is a [[layer-1|Layer-1]] blockchain development platform aimed at enterprises and financial-services organizations that want to build, test, and deploy blockchain applications. Its distinguishing bet is the **Microsoft .NET / C#** developer ecosystem: most blockchain platforms target Solidity, Rust, or JavaScript, whereas Stratis lets the large pool of corporate .NET developers write [[smart-contracts|smart contracts]] and chain logic in C#. The platform offers private/permissioned **sidechains**, full-node libraries, and developer SDKs so businesses can deploy customized chains without running their own base-layer infrastructure — a "blockchain-as-a-service" model.

Technically, the original Stratis chain was derived from [[bitcoin|Bitcoin's]] core codebase, re-implemented in C# (the **NBitcoin / Stratis Full Node** stack) and switched to a [[proof-of-stake|Proof-of-Stake]] consensus rather than Bitcoin's energy-intensive [[proof-of-work|proof-of-work]] mining. The project ran an ICO in June 2016 that raised roughly 915 BTC.

The team is based in the **United Kingdom** with a distributed structure; founder and CEO **Chris Trew** has an enterprise-IT background. Stratis's historical competitive set included other BaaS / enterprise-chain projects such as Lisk; Stratis differentiated on its C#/.NET focus and support for private sidechains, which can appeal to corporations wanting to keep code proprietary. The token migrated from the original STRAT to **STRAX** in a later platform upgrade.

### Architecture and consensus in detail

Stratis preserves a **Bitcoin-style UTXO ledger** but replaces mining with a **[[proof-of-stake|Proof-of-Stake]]** variant (historically a UTXO-based PoS where coin-age / staked balance earns the right to forge the next block). Because the full node, wallet, and contract tooling are written in **C# on .NET**, the entire stack runs natively on the Microsoft ecosystem (Windows Server, Azure, Visual Studio), which is the project's core go-to-market wedge: it lets the very large pool of enterprise .NET developers build chain logic without learning Solidity, Rust, or the EVM toolchain.

Key components have included:

- **Stratis Full Node** — a C# re-implementation of a Bitcoin-like node with PoS consensus.
- **Smart Contracts in C#** — Stratis shipped a [[smart-contracts|smart-contract]] system letting contracts be authored in a constrained subset of C# rather than Solidity, lowering the barrier for .NET teams.
- **Sidechains / federated chains** — private or consortium chains that peg to the mainchain, aimed at businesses that want a permissioned ledger while still anchoring to a public chain.
- **InterFlux / cross-chain** — interoperability work to bridge STRAX with EVM ecosystems, reflecting the broader industry shift toward EVM compatibility.

### Value accrual and the .NET enterprise thesis

STRAX accrues value to the extent that **real enterprise deployments** use the mainchain and sidechains for fees, staking, and bridging. The bet is structural rather than speculative: the supply of corporate .NET developers vastly exceeds the supply of Solidity developers, so a credibly maintained C#/.NET chain could in principle onboard enterprise builders other L1s cannot reach. The persistent risk is that **enterprise blockchain demand has broadly underdelivered industry-wide**, so the addressable developer pool has not converted into sustained on-chain economic activity.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.15B STRAX |
| **Total Supply** | 2.15B STRAX |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $28.28M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $22.77 (2018-01-08) |
| **Current vs ATH** | ~-99.95% |
| **All-Time Low** | $0.0114 (2016-08-12) |
| **24h Change** | +15.20% |
| **7d Change** | +18.54% |

> STRAX trades roughly 99.95% below its January-2018 peak — one of the steeper drawdowns among surviving 2016/2017-era platform tokens — and is among the weaker performers by long-term price retention. **Idiosyncratic move flag:** as of 2026-06-22 STRAX is up **+15.20% in 24h and +18.54% over 7 days**, a sharp rally that runs *against* the broad **Extreme Fear** regime (Fear & Greed 21). Moves of this magnitude in a thin micro-cap during a risk-off market are usually idiosyncratic — driven by a single catalyst, a listing/relisting, a low-float squeeze, or concentrated flow — rather than a broad sector re-rating, and they tend to mean-revert; treat the spike with caution and verify the cause before extrapolating.

> *Historical snapshot (2026-04-09): 24h range $0.0131–$0.0136; rank #781.* (Superseded by the 2026-06-22 figures above; retained for continuity.)

---

## Platform & Chain Information

**Native Chain:** Own [[layer-1|Layer-1]] blockchain (C#/.NET, [[proof-of-stake|Proof-of-Stake]])

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | STRAX/USDT | N/A |
| Upbit | STRAX/KRW | N/A |
| Bitget | STRAX/USDT | N/A |
| KuCoin | STRAX/USDT | N/A |
| Crypto.com Exchange | STRAX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | STRAX-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.stratisplatform.com/](https://www.stratisplatform.com/) |
| **Twitter** | [@stratisplatform](https://twitter.com/stratisplatform) |
| **Reddit** | [https://www.reddit.com/r/stratisplatform/](https://www.reddit.com/r/stratisplatform/) |
| **Discord** | [https://discord.gg/9tDyfZs](https://discord.gg/9tDyfZs) |
| **GitHub** | [https://github.com/stratisproject/StratisCore](https://github.com/stratisproject/StratisCore) |
| **Whitepaper** | [https://cdn.prod.website-files.com/6756aa200744d4108ed2b169/681487a3d4b6dfb200d06722_Litepaper%202025.pdf](https://cdn.prod.website-files.com/6756aa200744d4108ed2b169/681487a3d4b6dfb200d06722_Litepaper%202025.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 43 |
| **GitHub Forks** | 49 |
| **Pull Requests Merged** | 343 |
| **Contributors** | 18 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.01089312 |
| **Market Cap (2026-06-22)** | $23,772,621 |
| **Market Cap Rank** | #742 |
| **24h Change** | +15.20% (idiosyncratic spike — see Price History) |
| **7d Change** | +18.54% |
| **Last Updated** | 2026-06-22 |
| **Historical (2026-04-09)** | 24h volume $714,237; rank #781; 24h range $0.0131–$0.0136 |

---

## Distinguishing Features

- **C# / .NET native** — uniquely targets the Microsoft enterprise developer ecosystem rather than Solidity/Rust/JS, lowering the on-ramp for corporate dev teams.
- **Enterprise BaaS focus** — private/permissioned sidechains and SDKs aimed at financial-services and business deployments.
- **Bitcoin-derived, PoS-secured** — re-implements a Bitcoin-style UTXO core in C# but uses [[proof-of-stake|Proof-of-Stake]] consensus.
- **Long operating history** — live since 2016, with a token migration from STRAT to STRAX.

---

## History

- **June 2016** — ICO raises ~915 BTC to fund development; founder/CEO **Chris Trew** leads a UK-based, distributed team.
- **August 2016** — mainnet genesis (2016-08-09); the Bitcoin-derived, C#-reimplemented [[proof-of-stake|PoS]] chain goes live.
- **2017–2018** — peak hype cycle: STRAX (then STRAT) reaches its ATH of ~$22.77 in January 2018 amid the broad enterprise-blockchain and ICO boom, marketed alongside peers like Lisk on the "build chains in a mainstream language" thesis.
- **2018–2020** — protracted bear market and the industry-wide cooling of the enterprise-blockchain narrative; price retraces >99% from ATH.
- **Platform upgrade era** — token migration from **STRAT → STRAX** as part of a re-architecture and rebrand, with subsequent work on C# smart contracts, federated sidechains, and EVM-interoperability (InterFlux).
- **Subject-integrity history (wiki-internal):** this page once carried a corrupted title/website ("Xertra"); that was identified and corrected — the canonical subject is **Stratis (STRAX)**, confirmed here.

---

## Stratis vs. Peer Enterprise / Platform Chains

| Dimension | Stratis (STRAX) | Lisk (LSK) | [[ethereum|Ethereum]] (ETH) | [[ardor]] (ARDR) |
|---|---|---|---|---|
| **Developer language** | C# / .NET | JavaScript / SDK | Solidity (EVM) | Java (Jelurida) |
| **Target** | Enterprise / financial-services BaaS | App-chain SDK | General smart contracts | Parent-child BaaS |
| **Consensus** | [[proof-of-stake|PoS]] (UTXO) | [[delegated-proof-of-stake|DPoS]] | PoS (post-Merge) | Forging [[proof-of-stake|PoS]] |
| **Base model** | [[bitcoin|Bitcoin]]-derived UTXO in C# | Account-based | Account-based | Nxt-derived |
| **Smart contracts** | C# (constrained subset) | JS modules | Full EVM | Lightweight scripting + child chains |
| **Origin** | 2016, UK | 2016 | 2015 | 2018 (Nxt 2013) |
| **Differentiator** | Microsoft .NET dev pool + private sidechains | Mainstream-language app chains | Liquidity + tooling network effect | Pruned parent-child architecture |

Stratis's defining wedge is the **Microsoft .NET developer ecosystem** — a positioning none of its smart-contract peers share. The trade-off is that it forgoes the EVM network effect (liquidity, tooling, composability) that has concentrated developer mind-share on Ethereum-compatible chains.

## Risks

- **Weak long-term price retention** — down ~99.95% from ATH, reflecting limited commercial traction relative to early ambitions.
- **Enterprise-adoption uncertainty** — enterprise blockchain demand has broadly underdelivered industry-wide; STRAX value depends on real platform usage.
- **Competitive niche** — competes against general-purpose smart-contract chains and dedicated enterprise consortium frameworks (e.g., Hyperledger), and forgoes the EVM network effect.
- **Liquidity / small-cap risk** — ~$24M market cap (rank #742) implies thin liquidity and high volatility, amplified in the current Extreme-Fear regime.
- **Spike-reversion risk** — the +15.20%/24h and +18.54%/7d move (2026-06-22) is a sharp, idiosyncratic rally against a risk-off tape; such micro-cap spikes frequently mean-revert and should not be read as a trend without a verified catalyst.

> *This page is informational, not investment advice. Small-cap crypto assets are highly volatile and can lose most of their value rapidly.*

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

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no additional specific wiki source ingested yet.
