---
title: "ORE"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi]
aliases: ["ORE", "ORE Supply"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://ore.supply/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[proof-of-work]]", "[[solana]]"]
---

# ORE

**ORE** (ORE) is a [[proof-of-work]] digital commodity issued on the [[solana]] blockchain, marketed as fair-launch "digital gold." Unlike most Solana tokens, ORE is *mined* rather than pre-allocated: anyone can run the open-source miner and compete to earn newly issued ORE, with no team or VC pre-mine. The current iteration is **ORE v2** (built by Regolith Labs), which reworked the original mining mechanism to control issuance and reduce spam load on Solana. It ranks **#552** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* ORE trades at **$78.93**, market cap **$37,196,791**, **+5.16% (24h)** and **-1.88% (7d)** — outperforming a fearful tape (BTC $64,508; Fear & Greed 21 / Extreme Fear).

---

## What ORE Is

ORE applies [[bitcoin]]-style proof-of-work economics on top of Solana's high-throughput settlement layer. Where Bitcoin awards a block reward to a single winning miner, ORE's design lets *every* valid miner earn a proportional share of issuance, lowering the variance that pushes individual hobbyist miners out of Bitcoin. The pitch is a programmable, fairly-distributed scarce commodity — "digital gold" that anyone can produce with a CPU rather than specialized ASICs.

- **Fair launch** — no pre-mine, no insider allocation; all supply enters circulation through mining.
- **Mineable on commodity hardware** — proof-of-work is CPU-friendly, lowering the barrier versus ASIC-dominated chains.
- **Solana-native** — settlement, fees, and program logic run on Solana, so mining throughput is bounded by Solana block space and fees rather than a dedicated chain.

## Mechanism (ORE v2)

ORE v1 launched in 2024 but its uncapped, per-account reward design generated so many transactions it congested Solana, forcing a pause. **ORE v2** reintroduced the token with a controlled emission schedule and a redesigned mining/claiming flow that throttles issuance and mitigates the spam problem. Hard supply is capped (max supply 3,000,000 ORE; circulating/total ≈ 448,184 at the snapshot above), giving ORE a fixed-scarcity profile comparable to capped proof-of-work assets. Mining and contract code are open source under Regolith Labs (`regolith-labs/ore`).

### Deep dive — proof-of-work without a dedicated chain

ORE's novelty is running [[proof-of-work]] *as a program on an L1* ([[solana]]) rather than as the consensus of its own chain:

- **Hashing off-chain, settlement on-chain** — miners compute proof-of-work (a hash puzzle) off-chain on commodity CPUs, then submit a valid solution to the ORE program on Solana, which verifies it and mints the reward. Solana provides settlement and ordering; it is *not* securing ORE via PoW (Solana itself uses proof-of-stake).
- **Shared, proportional rewards** — where [[bitcoin]] pays the entire block reward to one winning miner (high variance, pushing out hobbyists), ORE's design distributes issuance proportionally across valid miners, smoothing per-miner rewards and lowering the barrier to participation.
- **Controlled emission** — v2 throttles issuance against a fixed max supply (3,000,000 ORE), so the inflation rate declines toward zero as supply approaches the cap — a capped-PoW scarcity profile.
- **Spam/congestion lesson** — v1's uncapped per-account rewards incentivized transaction spam that congested Solana; v2's throttled flow is the direct fix. ORE's throughput and cost remain bounded by Solana block space and fees.

## Token Role & value accrual

ORE is the asset itself — a mined commodity token, not a governance or fee token for a separate platform. Its value proposition rests entirely on (a) the credibility of its fair-launch, no-pre-mine distribution, (b) capped, declining-issuance scarcity, and (c) any speculative "digital gold" narrative premium. There is **no staking yield, fee-share, or cash flow** baked into the base token — value accrual is purely monetary/Schelling-point, exactly as with [[bitcoin]] or [[gold]]. The MC/FDV ratio of ~1.00 (circulating ≈ total) is a genuine strength versus the unlock-heavy peers in this cohort: there is no team/VC unlock cliff, only ongoing mining issuance up to the 3M cap. Governance, to the extent it exists, is informal/social via Regolith Labs and the community rather than an on-chain token vote.

## Competitive Position

ORE sits in the small niche of *mineable* tokens on smart-contract chains — adjacent to other fair-launch / proof-of-work-on-an-L1 experiments:

| Asset | Chain / model | Issuance | Vs. ORE |
|---|---|---|---|
| **ORE** | PoW program on [[solana]] | Mined, capped 3M, proportional rewards | Solana speed/low fees + Bitcoin-style fair launch; CPU-mineable |
| **[[bitcoin]] (BTC)** | Own PoW chain | Mined, capped 21M, single-winner | The reference "digital gold"; ASIC mining, vastly deeper liquidity/security |
| **Kaspa (KAS)** | Own PoW (BlockDAG) | Mined, capped | Dedicated high-throughput PoW chain vs. ORE's on-L1 program |
| **Memecoin/fair-launch tokens** | Various L1s | Often LP/airdrop, not mined | ORE's mining + hard cap differentiates from typical fair-launch memes |

Its differentiator is the combination of Solana's speed/low fees with a Bitcoin-like issuance ethos and a true no-pre-mine launch. Liquidity is thin and concentrated on Solana DEXs (notably Orca), typical for a sub-$50M-cap commodity token.

---

## Risks

- **Speculative narrative asset** — value depends heavily on the "digital gold" story; there is no cash-flow or yield underpinning the price.
- **Severe drawdown history** — ORE is down ~97% from its 2024 all-time high (~$1,452), reflecting how violently sentiment-driven these tokens reprice.
- **Low liquidity** — sub-$1M daily volume and DEX-only depth mean large orders move price sharply and exits can be costly.
- **Chain-dependency / congestion risk** — ORE's mining load famously congested Solana under v1; its economics remain coupled to Solana fees and block space.
- **Small-cap / concentration risk** — a ~$37M market cap with a small contributor base is vulnerable to concentrated holdings and abandonment.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ORE |
| **Market Cap Rank** | #552 |
| **Market Cap** | $37,196,791 |
| **Current Price** | $78.93 |
| **24h / 7d Change** | +5.16% / -1.88% |
| **Categories** | Decentralized Finance (DeFi), Solana Ecosystem, Proof-of-Work, Mobile Mining |
| **Website** | [https://ore.supply/](https://ore.supply/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 448,184 ORE |
| **Total Supply** | 448,184 ORE |
| **Max Supply** | 3.00M ORE |
| **Fully Diluted Valuation** | $17.39M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1,451.62 (2024-07-30) |
| **Current vs ATH** | -97.35% |
| **All-Time Low** | $6.27 (2025-09-25) |
| **Current vs ATL** | +513.18% |
| **24h Change** | +2.72% |
| **7d Change** | +2.40% |
| **30d Change** | -33.77% |
| **1y Change** | +82.19% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `oreoU2P8bN6jkk3jbaiVxYnG1dCXcYxwhwyK9jSybcp` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | OREOU2P8BN6JKK3JBAIVXYNG1DCXCYXWHWYK9JSYBCP/SO11111111111111111111111111111111111111112 | Spot |

### How & where it trades

- **Spot** — ORE trades primarily on-chain on [[solana]] DEXs (notably Orca, ORE/SOL). CEX presence is limited; this is a DEX-native commodity token, so price discovery happens on Solana liquidity pools.
- **Derivatives** — no broadly-documented major ORE perp at the snapshot; exposure is spot-only, meaning no easy leverage or hedging.
- **Liquidity & float** — the standout structural fact is the **high per-unit price** (~$78.93) on a tiny **~448k-unit** supply: a ~$37M cap on sub-$1M daily volume. Books are very thin, so large orders move price sharply and exits can be costly. Unlike the rest of this cohort, ORE has **no unlock overhang** (MC/FDV ≈ 1.00) — the dilution comes only from ongoing mining issuance toward the 3M cap. Treat as a low-liquidity, high-volatility commodity token. See [[liquidity]] and [[slippage]].

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ore.supply/](https://ore.supply/) |
| **Twitter** | [@OREsupply](https://twitter.com/OREsupply) |
| **Discord** | [https://discord.gg/bSKU7TdtcY](https://discord.gg/bSKU7TdtcY) |
| **GitHub** | [https://github.com/regolith-labs/ore](https://github.com/regolith-labs/ore) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 813 |
| **GitHub Forks** | 293 |
| **Commits (4 weeks)** | 11 |
| **Pull Requests Merged** | 66 |
| **Contributors** | 8 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $530,423.00 |
| **Market Cap Rank** | #596 |
| **24h Range** | $37.51 — $44.14 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Narrative, Category & Catalysts

ORE's narrative is **"digital gold on Solana" / fair-launch proof-of-work** — a scarce, mineable, no-pre-mine commodity that anyone can produce on commodity hardware. It is a hybrid of the [[bitcoin]] sound-money ethos and Solana's throughput. Catalysts to watch:

- Renewed "sound money" / PoW-revival sentiment cycles and Solana-ecosystem strength.
- Growth in active miners and genuine holder distribution (network effect for a Schelling-point asset).
- New venues / deeper liquidity (CEX listings) reducing the thin-book penalty.
- Stability of the v2 emission mechanism under load (avoiding a v1-style congestion episode).

Headwinds: no cash flow to anchor value, severe historical drawdown (-97% from the 2024 ATH), thin liquidity, and Solana fee/congestion coupling.

---

## Major News & Events

> *Real, dated timeline. Undated mechanism items (v1 launch/pause, v2 relaunch) are described qualitatively above; only verified dated figures are tabulated here.*

| Date | Event |
|---|---|
| 2024 | ORE v1 launched on [[solana]]; uncapped per-account rewards drove transaction spam that congested Solana, forcing a pause (qualitative; see Mechanism). |
| 2024-07-30 | ORE all-time high of **$1,451.62** (CoinGecko price history). |
| 2025-09-25 | ORE all-time low of **$6.27** (CoinGecko price history). |
| 2026-06-22 | Snapshot: ORE ~$78.93, ~$37.2M cap (rank #552), -97% from ATH but +513% from ATL; +5.16% on the day vs. Extreme Fear tape. |

> *ORE v2 (Regolith Labs) reworked emission and the mining/claiming flow; precise relaunch dates will be added as sources are ingested.*

---

## Trading Playbook (bear / Extreme-Fear + bottoming regime)

> *Educational framing of behavior in the current regime — not advice.*

- **Regime context (2026-06-23):** market-health 29/100 (bearish), Fear & Greed 21 (Extreme Fear), long-horizon regime shifting to *Bottoming / Accumulation* with neutral on-chain health (48.5). Narrative commodity microcaps reprice violently with sentiment.
- **Beta & correlation:** ORE is a high-beta proxy for Solana-ecosystem and "sound money / PoW" sentiment; it can decouple from BTC on narrative flows (its +5.16% green print against a red tape illustrates this). The +82% 1y vs. -34% 30d shows how regime-dependent the path is.
- **Liquidity discipline:** sub-$1M daily volume on DEX-only depth means severe [[slippage]] on size — use limit orders, scale in, and assume exits are costly. The high unit price ($78.93) does not imply depth.
- **Risk events:** unlike its peers there is no unlock cliff (MC/FDV ≈ 1.00); the key idiosyncratic risks are Solana congestion/fee spikes, contributor abandonment, and a sentiment unwind of the "digital gold" premium.
- **Bottoming-regime stance:** as a non-cash-flow Schelling-point asset, accumulation theses rest entirely on the narrative holding and distribution widening. Treat ORE as a speculative commodity bet; size small and apply [[risk-management]] / [[position-sizing]].

---

## See Also

- [[crypto-markets]]
- [[solana]]
- [[proof-of-work]]
- [[bitcoin]]
- [[gold]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.

## Overview

ORE is future-proof electronic cash. ORE exists to advance the original vision for crypto, identified by Satoshi Nakamoto: creating digital money that cannot be debased or controlled by centralized authorities. 

Bitcoin solved the double-spend problem. Solana solved scalability at the Layer 1 level. Modern wallets improved self-custody user experience. ORE solved the Proof-of-Work value leak.

Built on Solana, ORE inherits the network's scalability, composability, and future upgrades, including privacy enhancements, without requiring the tradeoffs traditionally associated with securing blockchain consensus. For these reasons, we describe ORE (after Bitcoin: "Peer-to-peer electronic cash") as:
- ORE, the asset, is a future-proof electronic cash system.
- ORE, the protocol, is a future-proof electronic cash system on Solana.

ORE is named after Nicholas Oresme, the 14th-century philosopher and economist who argued that money should belong to the people who use it rather than rulers who debase it. That philosophy serves as the foundation for the protocol: in many ways, ORE is the continuation of a centuries-old idea — that monetary systems are strongest when they are governed by rules rather than rulers.

---
