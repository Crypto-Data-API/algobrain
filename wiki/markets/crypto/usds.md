---
title: "USDS"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["Sky Dollar", "Sky USDS", "USDS"]
entity_type: protocol
founded: 2024
headquarters: "Decentralized"
website: "https://sky.money/"
related: ["[[crypto-markets]]", "[[dai]]", "[[ethereum]]", "[[makerdao]]", "[[stablecoins]]", "[[tether]]"]
---

# USDS

**USDS** (ticker **USDS**, native to [[ethereum|Ethereum]]) is the dollar [[stablecoin]] of the **[[sky|Sky]]** ecosystem — the protocol formerly known as [[makerdao|MakerDAO]] — and the successor to [[dai|DAI]], making it the **largest decentralized (crypto-collateralized) stablecoin**. For traders it matters less as a position and more as infrastructure: its **Sky Savings Rate (SSR)** is a key DeFi rates benchmark, and its supply is a gauge of on-chain dollar demand. It ranks in the **top 15 by market capitalization**.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #12 |
| **Market Cap** | ~$10.26B |
| **Current Price** | $0.99970 |
| **24h Volume** | ~$52.42M |
| **24h Change** | +0.00% |
| **7d Change** | +0.00% |
| **Circulating Supply** | ~10.26B USDS |
| **Max Supply** | Unlimited (mint/redeem against collateral) |
| **All-Time High** | $1.15 (2026-04-02) — **-13.23%** (data artifact, not a sustained depeg) |
| **All-Time Low** | $0.94827 (2024-10-03) — **+5.43%** |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

USDS holds its **soft peg** tightly at ~$0.9997. Supply stands at **~$10.26B**, down modestly from the **$11.82B all-time-high supply on 2026-04-05** — a contraction consistent with the deleveraging **"Established Bear Market"** regime ([[crypto-fear-and-greed-index|Fear & Greed]] = 23) where on-chain dollar demand softens. The "$1.15 ATH" remains a CoinGecko thin-market print, not a real depeg. See [[market-regime]].

---

## Technology / Protocol

USDS is the stablecoin of the decentralized **Sky** ecosystem (rebranded from MakerDAO in 2024), designed to hold a **soft peg** to the U.S. dollar. It is the upgraded, 1:1-convertible successor to [[dai|DAI]].

- **Minting** — USDS is created when users deposit approved collateral (crypto + tokenized real-world assets) into Sky's vaults/allocators, the same overcollateralized model Maker pioneered with DAI.
- **sUSDS / Sky Savings Rate (SSR)** — users convert USDS to **sUSDS** to earn the SSR, a protocol-revenue-funded yield that functions as a "DeFi Fed funds rate." Roughly **half of USDS supply** sits in sUSDS.
- **SKY governance** — locking USDS or holding SKY confers governance; the **MKR token was retired** and migrated to SKY in the 2025 Endgame transition.
- **Sky Stars** — semi-autonomous subDAOs (e.g., **Spark**) that extend USDS into specialized lending, liquidity, and institutional-credit verticals.

---

## Peg Mechanism, Collateral & De-Peg Risk

- **Peg type** — soft peg, defended by overcollateralization, the SSR (raising sUSDS yield pulls demand in when USDS is weak), and arbitrage against the 1:1 DAI↔USDS converter and on-chain pools.
- **Collateral / backing** — **overcollateralized + RWA/treasury-backed** via Sky allocators: a mix of crypto collateral and tokenized US Treasuries / real-world credit. Backing is on-chain transparent through Sky's allocator system.
- **De-peg / redemption risk** — the historical ATL of **$0.9483 (Oct 2024)** shows the peg can wobble in stress. Key risks: RWA/treasury **collateral concentration**, smart-contract risk in new modules (srUSDS, Generator System), governance missteps on the SSR, and a broad crypto-collateral drawdown. There is no centralized issuer redemption window — the peg is mechanism-driven, like [[gho|GHO]] and [[dai|DAI]]. See [[stablecoin-depegs]].

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~10.26B USDS |
| **Total Supply** | ~10.26B USDS |
| **Max Supply** | Unlimited (demand-elastic mint/redeem) |
| **Fully Diluted Valuation** | ~$10.26B |
| **Market Cap / FDV Ratio** | 1.00 |

Supply is **demand-elastic** — minted against collateral, burned on repayment — so there is **no dilution** in the equity sense (MC = FDV). The gauge that matters is **supply trend**: from $9–11B through Q1 2026 to a $11.82B peak on 2026-04-05, now retracing to ~$10.26B as leverage unwinds. About **half** of supply is staked into sUSDS earning the SSR.

---

## Market Structure & Trading Relevance

- **Not a directional asset** — USDS is a cash leg and yield instrument. Uses: parking dry powder in **sUSDS at the SSR** (3.75–4.5% in early 2026), collateral in DeFi money markets, and **basis/peg arbitrage** when USDS trades off $1.00 on [[uniswap]], Curve, or Orca (deployed on Ethereum, Base, Arbitrum, and Solana).
- **As a signal** — USDS supply growth = on-chain dollar/leverage demand; **SSR changes are a governance-set "DeFi Fed funds"** that ripple through lending rates on Spark, [[aave|Aave]], and Morpho.
- **Relative-value context** — competes with [[tether|USDT]] and USDC for float; the decentralized-issuer premium/discount is a recurring DeFi narrative.

### Exchange Listings

| Venue | Pair | Type |
|---|---|---|
| Kraken | USDS/USD | Spot (CEX) |
| Upbit | USDS/KRW | Spot (CEX) |
| Bitget | USDS/USDT | Spot (CEX) |
| Uniswap V3/V2 (Ethereum) | USDS/DAI, USDS/USDC | Spot (DEX) |
| Orca (Solana) | USDS/USDC | Spot (DEX) |
| Curve | USDS stable pools | Spot (DEX) |

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdc035d45d973e3ec169d2276ddab16f1e407384f` |
| Base | `0x820c137fa70c8691f0e44dc420a5e53c168921dc` |
| Arbitrum One | `0x6491c05a82219b8d1479057361ff1654749b876b` |
| Solana | `USDSwr9ApdHk5bvJKMjzff41FfuX8bSxdKcR81vTwcA` |

---

## Narrative & Category

USDS is the flagship **decentralized, crypto-+-RWA-backed stablecoin** — category peers are [[gho|GHO]] (Aave), [[dai|DAI]] (its own legacy form), and [[usual-usd|USD0]]; the contrast is fiat-backed [[tether|USDT]]/USDC and the political/fiat-backed [[usd1-wlfi|USD1]]. The Sky thesis is "self-sovereign dollar at scale," with the SSR as a transparent on-chain savings rate and Sky Stars extending utility into institutional credit. Its size (top-15) makes USDS a systemic DeFi building block.

---

## Valuation Framing (qualitative)

USDS itself is a peg asset and is not "valued"; the economics accrue to **SKY** (protocol revenue from the spread between collateral yield/RWA returns and the SSR paid to sUSDS holders). Frame USDS via: total supply and its trend, the **sUSDS share** of supply (engagement), the **SSR level vs Treasury yields and vs sGHO/sUSDe** (competitiveness), and peg tightness. Growing supply at a stable peg with a competitive SSR is a bullish read-through for SKY; the current supply retracement from the April peak is a mild headwind.

---

## Peer Comparison

| Stablecoin | Model | Backing | Mkt Cap (rank) | Yield wrapper |
|---|---|---|---|---|
| **USDS** | Decentralized + RWA | Crypto + treasuries (Sky) | ~$10.26B (#12) | sUSDS (SSR ~3.75–4.5%) |
| [[gho\|GHO]] | Decentralized, overcollateralized | Aave collateral | ~$598M (#91) | sGHO (~5–7%) |
| [[dai\|DAI]] | Decentralized (Sky legacy) | Crypto + RWA | large | DSR (legacy) |
| [[usual-usd\|USD0]] | RWA-backed | Tokenized T-bills | mid-cap | USD0++ |
| [[tether\|USDT]] / USDC | Fiat-backed (centralized) | Cash + T-bills | huge | none native |

> *Peer market caps point-in-time (2026-06-20 where shown); others are category context.*

---

## Risks

- **Peg deviations** — historical ATL $0.9483 (Oct 2024); soft peg can wobble in stress.
- **RWA / treasury concentration** — large tokenized-Treasury and real-world-credit exposure introduces counterparty and custody risk beyond pure crypto collateral.
- **Smart-contract risk** — new modules (srUSDS, Generator System, Spark) expand the attack surface.
- **Regulatory** — US stablecoin legislation's treatment of decentralized issuers is unsettled.
- **Governance / execution** — reliance on SKY governance and Rune Christensen's Endgame roadmap (SkyLink, srUSDS).
- **Supply contraction** — a shrinking float (as now) signals weakening on-chain dollar demand and pressures protocol revenue.

> *This page is informational, not investment advice. As a stablecoin, deviations from $1 are the signal to watch.*

---

## Major News & Events (2024–2026)

- **September 2024** — MakerDAO rebranded to **Sky**; USDS introduced as the upgraded successor to [[dai|DAI]] (1:1 convertible).
- **May 2025 — Endgame transition completed** — the protocol retired the MKR token and migrated to **SKY** as the governance asset.
- **Mid-2025** — the **Spark** subDAO grew its Liquidity Layer 175% YoY to **$3.6B** in allocated assets.
- **Q1 2026** — Sky Savings Rate held in a 3.75–4.5% APY band, tracking US Treasury yields; total USDS supply ran $9–11B with about half staked into sUSDS.
- **2026-04-05** — USDS supply hit an **all-time high of $11.82B** (peaked near $12B in April).
- **2026-04-07** — the final **DAI-to-USDS migration** phase went live, the largest stablecoin conversion to date.
- **2026 (Jun)** — supply retraces to **~$10.26B** as leverage unwinds in the bear regime; peg holds at ~$0.9997.
- **2026 roadmap** — Rune Christensen outlined SkyLink (cross-chain), srUSDS (leveraged liquidity), and a new Generator System; Sky's own 2026 outlook projects $20.6B USDS supply and ~$611.5M gross protocol revenue (projection, not fact).

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[stablecoins]]
- [[makerdao]], [[sky]]
- [[dai]]
- [[gho]] — Aave's decentralized stablecoin peer
- [[tether]] — fiat-backed contrast
- [[aave]], [[uniswap]]
- [[stablecoin-depegs]], [[stablecoin-yield]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- Market data 2026-06-20 from `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko); macro backdrop from `raw/data/crypto-loop/_digest.md`.
- Sky official site — https://sky.money/ and https://sky.money/susds
- BlockEden: "DAI-to-USDS Migration Goes Live April 7" (2026-04-03) — https://blockeden.xyz/blog/2026/04/03/dai-usds-migration-makerdao-sky-protocol-stablecoin-rebrand/
- Messari Sky Protocol profile — https://messari.io/project/sky-protocol
- Eco: "Sky Savings Rate Deep Dive 2026: SSR, sUSDS, USDS Mechanics" — https://eco.com/support/en/articles/15254003-sky-savings-rate-deep-dive-2026-ssr-susds-usds-mechanics
- Verified via Perplexity (sonar) + web search, 2026-06-10

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDS |
| **Market Cap Rank** | #12 |
| **Market Cap** | $9.97B |
| **Current Price** | $0.9998 |
| **Categories** | Stablecoins, USD Stablecoin, Fiat-backed Stablecoin, Base Native |
| **Website** | [https://sky.money/](https://sky.money/) |

---

## Overview

USDS is the stablecoin of the decentralized Sky ecosystem, designed to maintain a soft peg (a value intended to stay close) to the U.S. dollar. It functions as a versatile tool for&nbsp;decentralized finance (DeFi), allowing value to move through the system via peer-to-peer lending and saving without a middleman. The token is 'put to work' by being supplied to various protocol modules; for example, users can convert USDS into sUSDS to earn interest from protocol revenue or lock it to receive&nbsp;SKY governance tokens. As the ecosystem grows, this scales through "Sky Stars," which are semi-autonomous projects that expand the stablecoin’s utility into specialized areas like institutional credit and advanced lending.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 9.97B USDS |
| **Total Supply** | 9.97B USDS |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $9.97B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.15 (2026-04-02) |
| **Current vs ATH** | -13.22% |
| **All-Time Low** | $0.9483 (2024-10-03) |
| **Current vs ATL** | +5.43% |
| **24h Change** | +0.01% |
| **7d Change** | +0.02% |
| **30d Change** | +0.01% |
| **1y Change** | +0.01% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdc035d45d973e3ec169d2276ddab16f1e407384f` |
| Base | `0x820c137fa70c8691f0e44dc420a5e53c168921dc` |
| Arbitrum One | `0x6491c05a82219b8d1479057361ff1654749b876b` |
| Solana | `USDSwr9ApdHk5bvJKMjzff41FfuX8bSxdKcR81vTwcA` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | USDS/USDT | N/A |
| Kraken | USDS/USD | N/A |
| Upbit | USDS/KRW | N/A |
| Bitget | USDS/USDT | N/A |
| Crypto.com Exchange | USDS/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | USDSWR9APDHK5BVJKMJZFF41FFUX8BSXDKCR81VTWCA/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |
| Uniswap V2 (Ethereum) | 0XDC035D45D973E3EC169D2276DDAB16F1E407384F/0X56072C95FAA701256059AA122697B133ADED9279 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://sky.money/](https://sky.money/) |
| **Twitter** | [@SkyEcosystem](https://twitter.com/SkyEcosystem) |
| **Whitepaper** | [https://developers.sky.money/](https://developers.sky.money/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $108.69M |
| **Market Cap Rank** | #12 |
| **24h Range** | $0.9997 — $0.9999 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
