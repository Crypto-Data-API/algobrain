---
title: "Hermez Network"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, ethereum, layer-2]
aliases: ["HEZ"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://hermez.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[polygon]]", "[[layer-2]]", "[[zk-rollup]]"]
---

# Hermez Network

**Hermez Network** (ticker **HEZ**) is the legacy token of **Hermez**, a decentralized **[[zk-rollup]]** built to scale payments and token transfers on top of [[ethereum]]. Hermez was acquired by [[polygon]] in 2021 and folded into **Polygon Hermez / Polygon zkEVM**, with the HEZ token slated for migration to MATIC/POL — so HEZ today is primarily a **legacy, low-liquidity** asset rather than a live, actively developed token. It ranks **#598** by market capitalization.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | HEZ |
| **Current Price** | $3.06 |
| **Market Cap** | ~$33.95M |
| **Market Cap Rank** | #598 |
| **24h Volume** | ~$9,883 |
| **24h Change** | -0.10% |
| **7d Change** | +0.28% |
| **Fully Diluted Valuation** | ~$33.95M |
| **All-Time High** | $10.30 (2021-12-26) — **-70.3%** |
| **All-Time Low** | $0.883591 — **+246%** |

Trading backdrop: the broad crypto market sits in **extreme fear** ([[fear-and-greed-index|Crypto Fear & Greed Index]] ≈ **23**) amid an **established bear market** as of 2026-06-21. HEZ is essentially **dormant**: 24h volume is only ~$9.9K and price is nearly flat (-0.1% on the day). As a legacy token slated for migration, its quoted market cap reflects residual holdings rather than an actively traded market.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~11.07M HEZ |
| **Total Supply** | ~11.07M HEZ |
| **Max Supply** | ~11.08M HEZ |
| **Market Cap** | ~$33.95M |
| **Fully Diluted Valuation** | ~$33.95M |
| **MC / FDV Ratio** | 1.00 |

Supply is small and effectively fully circulating: circulating ≈ total ≈ max (~11.07M HEZ), so **MC = FDV (ratio 1.00)** with no meaningful [[dilution|dilution]] remaining. The compact supply gives HEZ a higher per-token price (~$3) than the other tokens in this group despite a similar ~$34M cap — a denomination artifact, not a sign of strength. Note that the *real* future supply question for HEZ is not emission but **migration**: holders are expected to convert HEZ into POL on terms set by the Polygon ecosystem.

---

## How & Where It Trades

**Spot venues.** HEZ has **no meaningful centralized-exchange liquidity** today. CoinGecko reports trading essentially limited to a single on-chain pair — **HEZ/WETH on [[uniswap]] V2 (Ethereum)** — with ~$9.9K daily volume. There is no deep order book; any size trade would face severe slippage. This is consistent with a token whose project has moved on to its successor network.

### Market structure at a glance

| Dimension | Read |
|---|---|
| **Spot depth** | Effectively one on-chain pool (HEZ/WETH, Uniswap V2) |
| **Daily turnover** | ~$9.9K (~0.03% of cap) — dormant |
| **Derivatives** | None; no perps/funding/OI |
| **Float quality** | MC/FDV = 1.00 — fully diluted, no emission |
| **Key variable** | Migration terms to [[polygon]] POL, not trading flow |

**zk-rollup mechanics (legacy product).** Hermez was a **zero-knowledge rollup** for [[ethereum]]:

- It **batched many transfers off-chain** and posted succinct **zk-SNARK validity proofs** on-chain, drastically cutting per-transfer cost while inheriting Ethereum's security.
- It targeted **scalable payments and token transfers** (high-throughput, low-fee L2 transfers) rather than general smart contracts.
- HEZ was used for protocol fees and coordinator auctions in the original Hermez design.
- The technology lives on in **Polygon zkEVM**, the successor that generalized Hermez's zk-rollup approach to full EVM compatibility.

**Derivatives.** HEZ has no perpetual-futures / [[hyperliquid]] market and no funding/open-interest data — and given its near-zero spot liquidity, none would be expected.

---

## Use Case, Narrative & Category

HEZ sits in the **[[ethereum|Ethereum]] [[layer-2|Layer-2]] / [[zk-rollup]]** category (CoinGecko tags: Smart Contract Platform, Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK), Rollup). Its original narrative — cheap, scalable Ethereum payments via validity proofs — has been **superseded by its own successor**, [[polygon]] zkEVM. HEZ now functions mainly as a legacy claim on that migration rather than a token with forward-looking utility.

---

## Valuation Framing (qualitative)

HEZ is a **wind-down / migration asset**, and should be valued as such rather than as a live L2 token:

- **Value = migration optionality, not usage.** HEZ has no live fee accrual; its residual value is essentially a claim on whatever HEZ→POL conversion the Polygon ecosystem honours. The ~$34M cap is held up by holders waiting on (or unaware of) that path.
- **Fully diluted, no emission.** Unlike most names in this cohort, there is no dilution overhang (MC/FDV = 1.00) — the entire supply already exists.
- **Liquidity is the binding constraint.** At ~$9.9K daily volume on a single pool, the quoted cap is not realisable; an LP withdrawal could collapse tradable liquidity.
- **Successor captured the value.** The technological upside migrated to [[polygon]] zkEVM and the POL token; HEZ does not benefit from that ecosystem's growth except via conversion.

The honest read: HEZ is a **deprecated, dormant legacy token** whose price is a function of migration mechanics and thin-pool dynamics, not of an operating network.

---

## Peer Comparison

| Token | Status | Category | Price | Market Cap | Rank | MC/FDV |
|---|---|---|---|---|---|---|
| **Hermez (HEZ)** | Legacy / migrating | zk-rollup (→ Polygon zkEVM) | $3.06 | ~$34M | #598 | 1.00 |
| [[polygon\|Polygon (POL)]] | Live (successor) | L2 ecosystem | — | (large-cap) | — | — |
| zkSync (ZK) | Live | zk-rollup | — | (mid-cap) | — | — |
| Starknet (STRK) | Live | zk-rollup (STARK) | — | (mid-cap) | — | — |

*Hermez pioneered Ethereum zk-rollups but, uniquely in this group, exists today as a **wind-down token** rather than an active competitor — its technology lives on inside [[polygon]] zkEVM. See [[zk-rollup]] and [[layer-2]].*

---

## Notable History

- **Acquired by Polygon in August 2021** (a ~$250M token-swap deal); Hermez became **Polygon Hermez**, the foundation of what later launched as **Polygon zkEVM**. The official Twitter handle is **@PolygonHermez**, reflecting this lineage.
- As part of the acquisition, **HEZ was designated for migration to MATIC** (now POL) — making continued HEZ trading a wind-down rather than an active market.
- All-time high of **$10.30 on 2021-12-26**, near peak L2/ZK hype; now ~70% below that level with negligible volume.

---

## Risks

- **Legacy / deprecation risk** — the project lives on as Polygon zkEVM; HEZ is a wind-down token slated for migration to POL, with limited independent future.
- **Extreme illiquidity** — ~$4.7K daily volume on a single Uniswap V2 pair; effectively untradeable at size.
- **Migration / redemption uncertainty** — value depends on the terms and availability of any HEZ→MATIC/POL conversion.
- **Single-venue concentration** — one on-chain pool means any LP withdrawal can collapse tradable liquidity.
- **Bear-market backdrop** — extreme-fear, established-bear-market conditions further suppress an already-dormant asset.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[polygon]]
- [[layer-2]]
- [[zk-rollup]]
- [[uniswap]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific wiki source ingested yet.
