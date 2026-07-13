---
title: "Horizen"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, privacy]
aliases: ["ZEN", "ZenCash", "Horizen"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.horizen.io"
related: ["[[crypto-markets]]", "[[base]]", "[[privacy-coins]]", "[[zcash]]", "[[ethereum]]"]
---

# Horizen

**Horizen** (ticker **ZEN**, originally launched as **ZenCash** in 2017) is a privacy-oriented blockchain platform. It began as a Zcash-derived ([[zcash]]) Equihash Proof-of-Work coin with optional shielded transactions, and is now undergoing a major transition — **Horizen 2.0** — repositioning the project as an Ethereum-aligned **Layer-3 appchain deployed on [[base|Base]]** (Coinbase's Ethereum L2). The 2.0 vision is a modular privacy stack offering zero-knowledge proofs, TEEs, and other privacy-enhancing technologies as accessible building blocks for web apps.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ZEN |
| **Current Price** | $4.66 |
| **Market Cap** | $84,326,738 |
| **Market Cap Rank** | #299 |
| **24h Volume** | $11,167,691 |
| **24h Change** | +6.88% |
| **7d Change** | +6.33% |
| **24h Range** | $4.35 — $4.74 |
| **Fully Diluted Valuation** | $97,830,448 |
| **All-Time High** | $165.92 (2021-05-08), -97.19% |
| **All-Time Low** | $3.26 (2019-10-17), +42.8% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the backdrop on 2026-06-21 is risk-off — the [[fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (extreme fear)** in an **"Established Bear Market."** ZEN is bucking the trend with ~+6.9% on the day and ~+6.3% on the week, on a respectable ~$11.2M of daily volume — outperformance that may reflect Horizen 2.0 migration newsflow rather than broad market strength. At ~$4.66 the token trades ~97% below its 2021 peak and only ~43% above its 2019 all-time low.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~18.10M ZEN |
| **Total Supply** | 21.00M ZEN |
| **Max Supply** | 21.00M ZEN |
| **Market Cap / FDV Ratio** | ~0.86 |

- **Bitcoin-style hard cap:** ZEN has a fixed **21,000,000** maximum supply (mirroring [[bitcoin|Bitcoin]]), with ~18.1M currently circulating — roughly 14% still to be emitted/unlocked.
- **Consensus evolution:** ZEN historically secured an Equihash PoW chain with a node/secure-node incentive system; Horizen 2.0 moves away from the prior hybrid PoW/PoS model toward application-level security inherited from Base/Ethereum.
- **Migration mechanics:** holders should track the official Horizen 2.0 token-migration path (ERC-20 ZEN on Base alongside the legacy chain), as bridging/migration introduces operational considerations.

---

## Market Structure & Derivatives

ZEN has historically been more broadly listed than pure privacy coins, but its privacy heritage still creates listing sensitivity:

- **Spot (CEX):** Binance (ZEN/USDT), Bitget (ZEN/USDT), KuCoin (ZEN/USDT). ZEN's optional (rather than mandatory) privacy and ongoing pivot away from being a pure privacy coin have helped it retain more major-exchange access than mandatory-privacy peers like [[pirate-chain|Pirate Chain]].
- **Derivatives:** ZEN-PERP perpetual futures trade on [[hyperliquid|Hyperliquid]] (on-chain perps DEX), giving ZEN a decentralized derivatives venue with visible [[open-interest]] and [[funding-rate|funding]]. Funding/OI depth is modest but tradable; in the current bear-market regime expect funding to track broad altcoin sentiment. This makes ZEN unusual among privacy coins — its peer [[pirate-chain|Pirate Chain]] (ARRR) has no liquid perp market at all.
- **On-chain (Base):** as Horizen 2.0 rolls out on [[base|Base]], ZEN gains DEX liquidity within the Base/Ethereum DeFi ecosystem (contract `0xf43eb8de897fbc7f2502483b2bef7bb9ea179229` on Base).
- **Liquidity:** ~$11.2M daily volume against an ~$84M cap is healthy turnover (~13%/day) for a small-cap — meaningfully deeper than the thin books of mandatory-privacy peers.
- **Privacy-coin caveat:** despite broader access than mandatory-privacy coins, ZEN's legacy as a shielded/Zcash-derived asset means it can still be caught by exchange privacy-coin delisting waves; the 2.0 pivot is partly a strategic response to that risk.

### Privacy-Coin Peer Comparison

| Coin | Ticker | Privacy model | MC rank | Approx. market cap | Derivatives |
|---|---|---|---|---|---|
| [[monero|Monero]] | XMR | Mandatory (ring signatures) | Privacy leader | Multi-billion | Broad CEX + perps |
| [[zcash|Zcash]] | ZEC | Optional (zk-SNARK) | Mid-cap privacy | Hundreds of $M | Broad CEX + perps |
| **Horizen** | **ZEN** | **Optional → privacy infra (2.0 on Base)** | **#299** | **~$84M** | **ZEN-PERP on [[hyperliquid|Hyperliquid]]** |
| [[pirate-chain|Pirate Chain]] | ARRR | Mandatory (100% shielded) | #389 | ~$62M | None (spot-only) |

Horizen is mid-cap among privacy coins and uniquely is pivoting *out* of the pure-privacy-coin category toward selling privacy infrastructure, which differentiates its risk/reward from Monero, Zcash and Pirate Chain.

---

## Use Case, Narrative & Category

Horizen's narrative is mid-transition from **privacy coin** to **modular privacy infrastructure** ([[privacy-coins]]):

- **Legacy (ZenCash/Horizen 1.0):** a Zcash-fork Equihash coin with shielded transactions, a "Sidechain" SDK (Zendoo) for app-specific chains, and a secure-node network.
- **Horizen 2.0:** repositioning as a **Layer-3 on Base**, inheriting Ethereum security and Base scalability while offering a decentralized privacy stack (ZKPs, TEEs, ABE, MPC, FHE) as composable primitives for any app — "the first privacy appchain on Base."
- **Privacy-as-a-service thesis:** rather than selling private money, Horizen 2.0 aims to sell programmable privacy infrastructure to developers across the Ethereum ecosystem.

---

## Valuation Framing

[[privacy-coins|Privacy coins]] have no cash flows and are valued on adoption and the credibility of their privacy guarantees. Horizen straddles two valuation regimes:

- **Legacy privacy-coin lens:** as a Zcash-derived, hard-capped (21M) PoW coin, ZEN historically traded as a mid-tier privacy asset, valued on usage and listing access. On this lens it competes directly with [[zcash|Zcash]] and [[monero|Monero]] for the same mindshare and liquidity.
- **Privacy-infrastructure / appchain lens:** Horizen 2.0 reframes ZEN as the token of a Base-aligned L3 selling composable privacy primitives (ZKPs, TEEs, MPC, FHE). On this lens the relevant comparison set shifts toward Ethereum L2/L3 and ZK-infrastructure tokens, and value would accrue from developer adoption and fees on the new stack rather than from private-money usage.
- **Migration-as-catalyst:** the recent outperformance into Extreme Fear is best read as a *re-rating bet* on a successful 2.0 transition rather than broad market strength. The thesis is binary on execution — strong developer traction re-rates ZEN as infra; a stalled migration leaves it a shrinking legacy privacy coin near its 2019 lows.
- **Hard-cap anchor:** the fixed 21M supply (Bitcoin-style scarcity) underpins a long-run scarcity narrative regardless of which lens dominates.

---

## Notable History

- **2017:** Launched as **ZenCash**, a fork of the Zcash codebase using Equihash PoW.
- **2018:** Rebranded to **Horizen**; suffered a **51% attack** in mid-2018, after which the project introduced a delayed-block-submission penalty to harden against reorg attacks — a frequently-cited case study in PoW security.
- **2021 bull market:** ZEN reached its all-time high of **$165.92 (2021-05-08)**; the current price is roughly **97% below** that peak.
- **2019 low:** all-time low of **$3.26 (2019-10-17)** — notably, the current price is only modestly above that historic low.
- **2024–2026:** announcement and rollout of **Horizen 2.0** as an L3 appchain on Base, marking the strategic pivot from a standalone privacy chain to an Ethereum-aligned privacy platform.

---

## Risks

- **Migration/execution risk:** the Horizen 2.0 transition is a fundamental re-architecture (abandoning the prior PoW/PoS chain for an L3 on Base). Migration friction, technical delays, or weak developer adoption of the new privacy stack are the central risks.
- **Privacy-coin regulatory/delisting risk:** as a Zcash-derived shielded asset, ZEN remains exposed to exchange privacy-coin delistings and AML/travel-rule pressure, even as the 2.0 pivot tries to reduce that exposure.
- **PoW security history:** the 2018 51% attack is a reminder that smaller-cap chains are vulnerable; the new model shifts security reliance onto Base/Ethereum, which is itself a dependency.
- **Bear-market beta:** recent outperformance is news-driven; a sustained risk-off move can still pull ZEN down with the sector.
- **Competition:** crowded zero-knowledge / privacy-infrastructure space competing for the same developer mindshare on Ethereum L2s/L3s.

---

## Related

- [[crypto-markets]]
- [[base]]
- [[privacy-coins]]
- [[zcash]]
- [[monero]]
- [[pirate-chain]]
- [[bitcoin]]
- [[hyperliquid]]
- [[perpetual-futures]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko markets data.
