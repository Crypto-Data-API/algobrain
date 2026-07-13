---
title: "Stable"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, altcoins]
aliases: ["STABLE", "StableChain", "Stable Chain"]
entity_type: protocol
founded: 2025
headquarters: "Decentralized (Stable Foundation; Bitfinex/Tether-backed)"
website: "https://www.stable.xyz/"
related: ["[[crypto-markets]]", "[[tether]]", "[[stablecoins]]", "[[hyperliquid]]"]
---

# Stable

**Stable** (STABLE) is a Bitfinex-backed, EVM-compatible Layer 1 ("StableChain") purpose-built for stablecoin payments, using [[tether|Tether]]'s USDT as the native gas token; its mainnet and STABLE governance token launched on **2025-12-08**. For traders, STABLE is the flagship listed expression of the **stablecoin-infrastructure narrative** — effectively a quasi-Tether-ecosystem equity proxy — and one of the few late-2025 launches that immediately received broad CEX listings plus a [[hyperliquid|Hyperliquid]] perp.

> **Important distinction:** STABLE is *not itself a stablecoin*. It is the **governance and staking token of a stablecoin-optimized blockchain**. The dollar that moves on StableChain is [[tether|USDT]], which also pays gas. STABLE captures network-governance value, not a dollar peg — so it trades as a volatile altcoin (boom/retrace history below), not a ~$1 asset. Do not confuse it with the various "USD"-suffixed tokens in this peer set.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | STABLE |
| **Market Cap Rank** | Top-100 (≈#95 tier), ~$0.5–0.6B market cap — as of June 2026 (approximate) |
| **Chain** | Own Layer 1 (EVM-compatible); **gas paid in USDT**, not in STABLE |
| **Token role** | Governance and network security (staking); USDT handles the payments function |
| **Supply mechanics** | 100B fixed max supply; only ~22% circulating (MC/FDV ≈ 0.22) — 25% team and 25% investors on 1-yr cliff + 4-yr vest; 40% grants/partnerships; 10% genesis distribution |
| **Backing** | $28M seed led by Bitfinex with Hack VC; Tether CEO Paolo Ardoino as adviser; >$2B pre-deposit campaign across 24,000+ wallets |
| **Website** | [https://www.stable.xyz/](https://www.stable.xyz/) |

---

## Overview

Stable is the first Layer 1 blockchain purpose-built for the USDT ecosystem, leveraging USDT as the native gas token to remove friction from volatile gas fees. Optimized for speed, scalability, and compliance, Stable enables seamless integration for payment processors, DeFi, RWA, fintechs, and enterprises. With instant settlement, low-cost cross-border transfers, and enterprise-ready infrastructure, it delivers a user-friendly environment that enhances capital efficiency and drives global adoption.

---

## Architecture — how StableChain works

StableChain is a **stablecoin-native settlement layer** rather than a general-purpose smart-contract platform retrofitted for payments. The design choices all serve one goal: make moving a dollar (USDT) feel like sending an email.

- **USDT as native gas.** On most EVM chains, a user holding only a stablecoin still needs the chain's volatile native coin (ETH, BNB, etc.) to pay gas. StableChain removes that friction by making **[[tether|USDT]] the gas token itself** — fees are quoted and paid in dollars, so balances are predictable and a user never has to acquire a separate "gas coin." For simple USDT-to-USDT transfers the chain targets **gasless / near-zero-fee** transactions, subsidized at the protocol/foundation level.
- **STABLE's role is governance and security, not gas.** The STABLE token secures the network via **staking/validation** and confers governance over protocol parameters. This is the crux of the value-capture question (see Risks): the token does **not** directly collect the transaction-fee stream, because that stream is denominated in USDT and largely minimized by design.
- **EVM compatibility.** StableChain is EVM-compatible, so existing Solidity contracts, wallets, and tooling port over with minimal changes — important for bootstrapping DeFi, RWA, and payment-processor integrations quickly.
- **Compliance-oriented rails.** Positioning emphasizes enterprise/fintech use (payment processors, neobanks, custody), implying screening/compliance hooks aimed at institutional settlement rather than purely permissionless DeFi.
- **Ecosystem alignment.** Stable sits inside the **Bitfinex/Tether orbit** (seed led by Bitfinex; Paolo Ardoino as adviser). Because Tether itself is a private company, StableChain is the closest **publicly tradeable proxy** to that ecosystem's growth.

### Comparison vs other stablecoin-payment L1s

STABLE is best understood against the small cohort of **purpose-built stablecoin/payment chains** that emerged in 2025, not against stablecoins. The peer trade is a *basket* (long/short the strongest narrative member).

| Chain (token) | Backer / orbit | Gas model | Niche | Differentiator |
|---|---|---|---|---|
| **Stable (STABLE)** | Bitfinex / [[tether|Tether]] | **USDT as gas** | USDT-native payments & settlement | Closest listed proxy to Tether ecosystem |
| **Plasma (XPL)** | Tether-aligned / Bitfinex orbit | USDT-fee-abstracted | High-throughput stablecoin payments | Earlier-mover stablecoin-chain narrative |
| **Tempo** | Stripe / Paradigm-linked | Stablecoin-fee-abstracted | Enterprise/fintech stablecoin settlement | TradFi/payments distribution |
| **[[tron]] (TRX)** | Justin Sun ecosystem | TRX as gas | Dominant incumbent for USDT transfers | Largest live USDT settlement volume today |

The incumbent to beat is **[[tron|Tron]]**, which already settles an enormous share of real-world USDT transfers. StableChain's bet is that *native* USDT gas and enterprise compliance tooling win share from Tron and from generic L1s/L2s.

---

## 2025–2026 Developments

- **Mainnet + TGE (2025-12-08)** — StableChain mainnet went live and the STABLE token launched, alongside the formation of the Stable Foundation. Launch was supported by 150+ partners across DeFi, payments, custody, neobank and infrastructure sectors (The Block, Morningstar/PR Newswire).
- **Pre-deposit campaign** — drew **over $2B in deposits from 24,000+ wallets** across two phases before launch; some coverage cited ~$1.1B locked at mainnet.
- **Funding** — $28M seed backed by Bitfinex and Hack VC, with Paolo Ardoino (Tether CEO) as adviser.
- **Price action** — listed near launch with ATL ~$0.0092 (2025-12-24), rallied to ATH $0.0389 (2026-02-27), then settled around the mid-$0.02s by spring 2026 — a typical new-listing boom/retrace profile.

---

## Trading Relevance

- **Narrative basket**: stablecoin-infrastructure / payments-chain basket (with Plasma/XPL and Tempo as direct competitors). STABLE is the closest tradeable proxy to the Tether/Bitfinex ecosystem, since Tether itself is private.
- **Venues**: spot on Kraken, Bitget, KuCoin, Crypto.com; **STABLE-PERP on [[hyperliquid|Hyperliquid]]** — the perp is the main instrument for shorting the unlock schedule.
- **Structural setup**: MC/FDV ≈ 0.22 with team/investor cliffs ending **December 2026** — a classic low-float/high-FDV unlock-overhang trade; expect supply pressure into and after the cliff (see [[token-unlock-trading]] if present).
- **Catalysts**: USDT supply growth, payment-processor integrations, exchange/perp listings, competitor launches (Plasma, Tempo), Tether regulatory news.
- **Risks**: token accrues governance, not gas fees (USDT is gas) — value-capture model is unproven; heavy insider allocation (50% team+investors).

### Trading playbook

- **Low-float / high-FDV unlock trade.** With only ~22% circulating and the **December 2026** team/investor cliff approaching, the dominant structural pressure is forward supply. The cleanest expression is the **[[hyperliquid|Hyperliquid]] STABLE-PERP**: fade rallies into the cliff and watch funding for crowded-short signals near the unlock date.
- **Narrative-momentum, not value.** STABLE has no live cash-flow claim, so it trades on narrative. Size it as a high-beta altcoin, not a stablecoin — the 4x boom from ATL ($0.0092) to ATH ($0.0389) inside ~9 weeks and the subsequent retrace to the mid-$0.02s show how violent the swings are.
- **Macro context (2026-06-23).** Broad crypto sits in **Extreme Fear** (Fear & Greed 21; market-health 29/100, bearish; long-horizon regime = bottoming/accumulation, with BTC ≈ $64,568). Speculative low-float L1 tokens like STABLE are high-beta to this risk backdrop — they bleed hardest in fear and rip hardest on relief. Position sizing should respect that beta.
- **Catalyst calendar to watch**: payment-processor / neobank integration announcements, USDT supply prints, competitor (Plasma/Tempo) milestones, and the unlock schedule itself.

---

## Tokenomics (April 2026 snapshot)

| Metric | Value |
|---|---|
| **Circulating Supply** | 21.62B STABLE |
| **Total Supply** | 100.00B STABLE |
| **Max Supply** | 100.00B STABLE |
| **Fully Diluted Valuation** | $2.57B |
| **Market Cap / FDV Ratio** | 0.22 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0389 (2026-02-27) |
| **Current vs ATH** | -33.88% |
| **All-Time Low** | $0.00922140 (2025-12-24) |
| **Current vs ATL** | +178.81% |
| **24h Change** | -4.11% |
| **7d Change** | -7.88% |
| **30d Change** | -7.52% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Stable

### Contract Addresses

| Chain | Address |
|---|---|
| Stable | `0x0000000000000000000000000000000000001003` |
| Binance Smart Chain | `0x011ebe7d75e2c9d1e0bd0be0bef5c36f0a90075f` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | STABLE/USD | N/A |
| Bitget | STABLE/USDT | N/A |
| KuCoin | STABLE/USDT | N/A |
| Crypto.com Exchange | STABLE/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | STABLE-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.stable.xyz/](https://www.stable.xyz/) |
| **Twitter** | [@stable](https://twitter.com/stable) |
| **Discord** | [https://discord.com/invite/stablexyz](https://discord.com/invite/stablexyz) |
| **GitHub** | [https://github.com/stablelabs/stable/](https://github.com/stablelabs/stable/) |
| **Whitepaper** | [https://www.stable.xyz/whitepaper.pdf](https://www.stable.xyz/whitepaper.pdf) |

---

## Trading Characteristics (April 2026 snapshot)

| Characteristic | Detail |
|---|---|
| **24h Volume** | $14.04M |
| **Market Cap Rank** | #96 |
| **24h Range** | $0.0257 — $0.0271 |
| **CoinGecko Sentiment** | 100% positive |
| **Snapshot Date** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## History / Timeline

| Date | Event |
|---|---|
| **2025 (pre-launch)** | $28M seed round led by **Bitfinex** with **Hack VC**; **Paolo Ardoino** (Tether CEO) joins as adviser. |
| **2025 (pre-launch)** | Two-phase **pre-deposit campaign** draws **>$2B from 24,000+ wallets**; some coverage cited ~$1.1B locked at mainnet. |
| **2025-12-08** | **StableChain mainnet** goes live; **STABLE token (TGE)** launches; **Stable Foundation** formed; 150+ launch partners across DeFi, payments, custody, neobank, infrastructure. |
| **2025-12-24** | All-time **low ~$0.0092** — typical new-listing post-TGE flush. |
| **2026-02-27** | All-time **high $0.0389** — ~4x off the ATL on peak narrative. |
| **Spring 2026** | Price settles around the **mid-$0.02s** — standard new-listing boom/retrace. |
| **December 2026 (scheduled)** | **Team/investor cliff ends** (25% team + 25% investors on 1-yr cliff + 4-yr vest) — the key forward supply event. |

---

## Risks

- **Value-capture risk (structural).** STABLE accrues **governance/staking value, not the fee stream** — gas is paid in USDT and largely minimized by design. Whether network growth translates into token value is **unproven**; this is the single biggest fundamental question for the asset.
- **Unlock / dilution risk.** ~50% of supply is allocated to **team + investors**, with the cliff ending **December 2026**. Low float today (MC/FDV ≈ 0.22) means meaningful forward dilution and a classic unlock overhang.
- **Competitive risk.** The stablecoin-chain niche is crowded — **Plasma (XPL)**, **Tempo (Stripe/Paradigm-linked)**, and incumbent **[[tron|Tron]]** (which already settles the bulk of real-world USDT) all contest the same flows.
- **Tether-dependency / counterparty risk.** STABLE's thesis is tied to [[tether|Tether]]/USDT growth and reputation; adverse USDT regulatory or reserve news would hit STABLE directly.
- **Liquidity / volatility risk.** Thin 24h volume (~$14M at snapshot) and high beta to a fearful macro tape (Fear & Greed 21) make it prone to sharp drawdowns.
- **Regulatory risk.** Stablecoin-payment infrastructure is squarely in the path of evolving stablecoin and money-transmission regulation globally.

---

## Related

- [[crypto-markets]]
- [[tether]] — issuer of USDT, the chain's gas token
- [[stablecoins]], [[stablecoin-supply]]
- [[hyperliquid]] — STABLE-PERP venue
- [[gho|GHO]], [[usual-usd|Usual USD]] — other stablecoin-ecosystem assets

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- The Block: "Stable, a Bitfinex-backed Layer 1 using Tether's USDT for gas, launches mainnet and native token" — https://www.theblock.co/post/381688/stable-launches-mainnet-native-token-foundation
- Morningstar / PR Newswire (2025-12-08): "Stable Launches StableChain Mainnet and Unveils Both the Stable Foundation and Native Token STABLE" — https://www.morningstar.com/news/pr-newswire/20251208ny41404/stable-launches-stablechain-mainnet-and-unveils-both-the-stable-foundation-and-native-token-stable
- Messari: "Stable: Mainnet and Token Generation Event" — https://messari.io/report/stable-mainnet-and-token-generation-event
- Verified via Perplexity (sonar) + web search, 2026-06-10
