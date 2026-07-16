---
title: "Theta Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, crypto, depin, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["THETA"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://www.thetatoken.org/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[depin]]", "[[ethereum]]", "[[layer-1]]", "[[proof-of-stake]]", "[[theta-fuel]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[crypto-beta-rotation]]", "[[liquidation-cascade-fade]]"]
---

# Theta Network

**Theta Network** (ticker **THETA**) is a [[layer-1|Layer-1]] blockchain and decentralized physical infrastructure network ([[depin]]) for video, media and AI compute. It pairs the **Theta Blockchain** (an [[ethereum|EVM]]-compatible [[proof-of-stake|PoS]] chain that handles payments, rewards and smart contracts) with the **Theta Edge Network** (a peer-to-peer mesh of GPU/bandwidth-sharing nodes that powers Theta EdgeCloud, a hybrid cloud-edge AI compute platform). THETA is the staking and governance asset; a second token, **[[theta-fuel|TFUEL]]**, is the operational gas/utility token used to pay for streaming and compute.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | THETA |
| **Current Price** | $0.15476 |
| **Market Cap** | $154,760,006 |
| **Market Cap Rank** | #206 |
| **24h Volume** | $6,695,099 |
| **24h Change** | +1.75% |
| **7d Change** | -3.34% |
| **Fully Diluted Valuation** | $154,760,006 |
| **Circulating Supply** | 1.00B THETA |
| **All-Time High** | $15.72 (2021-04-16) — now -99.0% |
| **All-Time Low** | $0.0404 (2020-03-13) — now +283.1% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market backdrop on 2026-06-21 is risk-off — the [[fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (extreme fear)** within what is being characterized as an **"Established Bear Market."** THETA managed a small +1.75% 24h bounce but is still -3.3% on the week, and thin ~$6.7M daily volume signals low liquidity typical of a deep drawdown. The token sits ~99% below its 2021 all-time high.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B THETA |
| **Total Supply** | 1.00B THETA |
| **Max Supply** | 1.00B THETA |
| **Market Cap / FDV Ratio** | 1.00 (fully circulating) |

- **Fixed cap, no inflation on THETA:** the entire 1B supply is in circulation (MC = FDV, ratio 1.00), so there is no future dilution/unlock overhang on the governance token. This is unusual among Layer-1s and removes one common source of structural sell pressure.
- **Dual-token model:** THETA is staked by Validator and Guardian nodes to secure the chain and is required for governance. **[[theta-fuel|TFUEL]]** is the *inflationary* gas token that pays for bandwidth/video delivery and EdgeCloud compute jobs; demand for network services accrues to TFUEL rather than THETA. The split deliberately localizes inflation/dilution risk to TFUEL while keeping THETA hard-capped — see [[theta-fuel]] for the operational-token side of the economy.
- **Genesis:** mainnet launched 2019; original token sale era 2017–2018.

---

## How & Where It Trades

THETA is a liquid, widely-listed altcoin available on most major centralized venues:

- **Spot (CEX):** Binance (THETA/USDT), Upbit (THETA/KRW — Korea is historically a strong THETA market), KuCoin (THETA/USDT), Crypto.com. Korean Won pairs are notable because retail Korean flow has periodically driven THETA premia.
- **Derivatives:** THETA perpetual futures are offered on major derivatives venues (e.g., Binance Futures). It is not among the deepest perp markets, so funding and open interest are modest relative to large-cap [[bitcoin]]/[[ethereum]] contracts; traders should expect wider spreads and thinner books during the current low-volume regime.
- **Liquidity note:** with ~$5.6M of 24h volume against a ~$152M cap, THETA trades thinly enough that large orders move price. This is standard for a coin ~95%+ below its all-time high in a bear market.

---

## Use Case, Narrative & Category

Theta sits at the intersection of three narratives that have driven its categorization on data aggregators: **DePIN** ([[depin]]), **AI compute**, and **video/media streaming**.

- **Edge Network / EdgeCloud:** the original thesis was decentralized video delivery (offloading CDN costs to a mesh of viewer nodes that relay streams and earn TFUEL). The network has since been repositioned around **EdgeCloud**, a hybrid platform marketing distributed GPU compute for AI inference, video transcoding and 3D rendering.
- **AI pivot:** Theta markets its edge-node GPU pool as supply for generative-AI workloads (text-to-video, rendering), aligning it with the DePIN-meets-AI thesis that drew capital into the sector in 2024–2025.
- **EVM compatibility:** the chain supports Solidity smart contracts, NFTs and DeFi primitives, positioning it as a general-purpose L1 in addition to its media/compute specialization.

---

## Valuation Framing (qualitative)

Valuing a DePIN/compute L1 like Theta is inherently speculative — there is no earnings stream, and the governance token (THETA) does not directly capture network fees (those accrue to [[theta-fuel|TFUEL]]). Useful qualitative anchors:

- **MC = FDV ($155M):** because supply is fully circulating, there is no hidden dilution; the entire valuation is "live." This compares favorably to low-float L1s where headline market cap understates eventual fully-diluted value.
- **Value accrual is indirect:** THETA upside depends on *staking demand* (security/governance) and the reflexive belief that a thriving EdgeCloud → more TFUEL burn/usage → more reason to stake THETA. Bears argue this linkage is weak; bulls treat THETA as a leveraged claim on the network narrative.
- **Compute-utilization is the key fundamental:** the metric that would justify re-rating is *paid* EdgeCloud GPU utilization and TFUEL burn, not marketing FLOPS. As of this snapshot these remain hard to verify from price alone.
- **Drawdown context:** ~99% below the 2021 ATH is typical for a 2021-cycle narrative coin; recovery to prior highs would require a ~64x move, so the realistic bull case is a partial re-rating on a credible AI-compute revenue story, not a return to the peak.

---

## Peer Comparison

THETA against other narrative-driven small/mid-cap L1s and infrastructure tokens in this cohort (data as of 2026-06-21):

| Token | Ticker | Price | Market Cap | Rank | 7d % | MC/FDV | Category |
|---|---|---|---|---|---|---|---|
| **Theta Network** | THETA | $0.15476 | $154.8M | #206 | -3.34% | 1.00 | DePIN / AI compute / video |
| [[vaulta]] | A | $0.065723 | $108.4M | #255 | -9.38% | 0.79 | Web3-banking L1 (ex-EOS) |
| [[aelf]] | ELF | $0.064383 | $52.9M | #432 | -0.72% | 0.82 | AI-focused L1 |
| [[oasis-network]] | ROSE | $0.0066718 | $52.0M | #439 | +4.12% | 0.78 | Confidential-compute L1 |
| [[nervos-network]] | CKB | $0.00104816 | $51.3M | #443 | -8.58% | 0.98 | PoW store-of-value L1 |
| [[dusk-network]] | DUSK | $0.085452 | $50.4M | #449 | -5.68% | 1.00 | Regulated-RWA L1 |

THETA is the largest-cap and most liquid name in this comparison group, reflecting its established brand and the durable pull of the DePIN + AI-compute narratives.

---

## Notable History

- **2017–2018:** Founded by Mitch Liu and Jieyi Long; backed by investors including Node Capital and (later) prominent figures from Silicon Valley and the streaming/esports world.
- **2019:** Theta mainnet launch; transition off Ethereum to its own Layer-1.
- **2021 bull market:** THETA reached its all-time high of **$15.72 (2021-04-16)**, riding the streaming/NFT/metaverse narrative. The current price is roughly **99% below** that peak.
- **2024:** Launch of **Theta EdgeCloud**, repositioning the edge network toward AI/GPU compute.
- **2020 low:** all-time low of **$0.0404 (2020-03-13)** during the COVID liquidity crash.

---

## Risks

- **Bear-market beta:** in an extreme-fear, "established bear market" regime, a high-beta, narrative-driven altcoin like THETA tends to fall harder than majors and recover later. Low volume amplifies drawdowns.
- **Narrative dependence:** the AI/DePIN compute thesis must convert into real, paying EdgeCloud demand. Decentralized GPU networks face stiff competition from centralized cloud (AWS/GCP) and from other DePIN compute projects; utilization and revenue, not marketing FLOPS figures, are what matter.
- **Value-accrual to THETA:** because network usage is paid in TFUEL, the link between protocol adoption and THETA price is indirect. Investors must believe staking demand and governance value will capture upside.
- **Liquidity/concentration:** thin spot/derivatives liquidity and reliance on a few exchanges (notably Korean venues) create slippage and venue-risk.
- **Competition:** crowded L1 and DePIN landscapes; differentiation on video/AI compute is not guaranteed.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[bitcoin]]
- [[depin]]
- [[theta-fuel]]
- [[layer-1]]
- [[proof-of-stake]]
- [[fear-and-greed-index]]
- [[oasis-network]]
- [[aelf]]
- [[vaulta]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko markets data, `raw/data/crypto-loop/coingecko-markets.json`.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | THETA |
| **Market Cap Rank** | #203 |
| **Market Cap** | $148.37M |
| **Current Price** | $0.1484 |
| **Genesis Date** | 2017-12-14 |
| **Categories** | Artificial Intelligence (AI), Smart Contract Platform, Layer 1 (L1), DePIN, Made in USA |
| **Website** | [https://www.thetatoken.org/](https://www.thetatoken.org/) |

---

## Overview

Theta Network is the leading blockchain-powered decentralized cloud for AI, media and entertainment. It can be viewed as a "dual network" consisting of two complementary subsystems, the Theta Edge Network and the Theta Blockchain. The edge network provides vast amounts of GPU compute power for AI, video, rendering and other tasks, while the Theta blockchain provides payment, reward, and smart contract capabilities. Below we provide more details for the two components.

Theta's Edge Network is a decentralized network consisting of over 10,000 active global nodes with 80 PetaFLOPS of always available distributed GPU compute power, equivalent to 250 Nvidia A100s. Theta Edge Network powers the Theta EdgeCloud, a leading hybrid cloud-edge AI computing platform launched on May 1, 2024. Leveraging Theta's recently approved patent on ‘Edge Computing Platform supported by Smart Contract Enabled Blockchain Network’ and the upcoming release of Elite+ Booster edge nodes, all Theta community members will be able to participate and share in the rewards from EdgeCloud AI, video, 3D rendering and gaming compute jobs. While chatbots like ChatGPT and others utilize GPUs, new generative AI models such as text-to-video, text-to-3D and sketch-to-3D will require 10-100x the amount of computational power. The combined GPU compute power of Theta's decentralized edge network and its preferred cloud partners is 20-30x more than other comparable networks in the industry today, holding the keys to global GPU compute, arguably the most valuable and most disruptive asset in history.

Theta blockchain is an EVM compatible multi-blockchain network which supports Turing complete smart contracts. This EVM support enables a wide range of interesting Web3 applications to be built on the Theta Network. Examples include non-fungible tokens (NFT), decentralized exchanges (DEX/DeFi), and decentralized autonomous organizations (DAO), which could become indispensable building blocks of the next generation A...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B THETA |
| **Total Supply** | 1.00B THETA |
| **Max Supply** | 1.00B THETA |
| **Fully Diluted Valuation** | $148.37M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $15.72 (2021-04-16) |
| **Current vs ATH** | -99.06% |
| **All-Time Low** | $0.0404 (2020-03-13) |
| **Current vs ATL** | +267.20% |
| **24h Change** | +1.55% |
| **7d Change** | +8.25% |
| **30d Change** | -9.13% |
| **1y Change** | -82.15% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | THETA/USDT | N/A |
| Upbit | THETA/KRW | N/A |
| KuCoin | THETA/USDT | N/A |
| Crypto.com Exchange | THETA/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.thetatoken.org/](https://www.thetatoken.org/) |
| **Twitter** | [@Theta_Network](https://twitter.com/Theta_Network) |
| **Reddit** | [https://www.reddit.com/r/theta_network/](https://www.reddit.com/r/theta_network/) |
| **Discord** | [https://discord.com/invite/nC8mCkgEmV](https://discord.com/invite/nC8mCkgEmV) |
| **GitHub** | [https://github.com/thetatoken/theta-protocol-ledger](https://github.com/thetatoken/theta-protocol-ledger) |
| **Whitepaper** | [https://s3.us-east-2.amazonaws.com/assets.thetatoken.org/Theta-white-paper-latest.pdf](https://s3.us-east-2.amazonaws.com/assets.thetatoken.org/Theta-white-paper-latest.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 362 |
| **GitHub Forks** | 85 |
| **Commits (4 weeks)** | 2 |
| **Pull Requests Merged** | 126 |
| **Contributors** | 10 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.85M |
| **Market Cap Rank** | #203 |
| **24h Range** | $0.1452 — $0.1490 |
| **CoinGecko Sentiment** | 67% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

THETA is tradable on [[binance]] — both **spot** (THETA/USDT) and a **USD-margined [[perpetual-futures|perpetual]]** contract, which exposes [[funding-rate|funding]], [[open-interest]] and [[liquidations]] data for leveraged flow. THETA is **NOT** listed on [[hyperliquid]]; **Binance is the primary leveraged venue**, so perp-derived signals (funding, OI, liquidation prints) should be read from Binance USD-M rather than a DEX-perp book. As a rank ~203 mid/small-cap with modest daily volume, the perp book is thinner and funding more jerky than large-caps: available leverage is lower, order books are shallower, and large clips move price. Practical implication — size positions to Binance depth, favor limit/VWAP execution over market orders, keep leverage conservative, and treat wide spreads plus concentration on a few CEXs (including Korean spot flow) as a real execution constraint.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on THETA's Binance USD-M contract when the rate is persistently one-sided, a common feature in thin narrative altcoin books.
- [[crowded-long-funding-fade]] — narrative-driven DePIN/AI hype can push THETA longs to extreme positive funding; fade the crowded side once funding and OI stretch together.
- [[liquidation-cascade-fade]] — thin liquidity means forced-liquidation flushes overshoot; fade the wick after a Binance long-liquidation cascade for a mean-reversion bounce.
- [[oi-confirmed-trend]] — use rising Binance open interest alongside price to confirm that a THETA breakout is backed by real positioning rather than a low-volume drift.
- [[crypto-beta-rotation]] — THETA is a high-beta DePIN/AI proxy; rotate into it when the risk-on regime favors small-cap beta over BTC/ETH, and out when beta compresses.
- [[breakout-and-retest]] — narrative catalysts (EdgeCloud/AI news) produce sharp range breaks; enter on the retest to avoid chasing thin, gappy moves.

### Volatility & regime character

Mid/small-cap altcoin with **high beta to BTC/ETH** — it typically falls harder than majors in risk-off and rebounds late. As a DePIN + AI-compute **infrastructure/narrative token**, its volatility is reflexive to sector sentiment (AI/DePIN capital rotation) rather than to protocol earnings. Directionally correlated with the broad altcoin complex, amplified by thin liquidity; expect elevated realized volatility, gap risk around news, and regime-dependent funding.

### Risk flags

- **Liquidity / venue concentration:** thin spot and perp depth concentrated on a few CEXs (Binance plus Korean venues like Upbit) — slippage and venue risk on size.
- **Narrative dependence:** valuation hinges on the AI/DePIN EdgeCloud thesis converting to paying GPU demand; sentiment reversals hit price disproportionately.
- **Indirect value accrual:** network usage is paid in [[theta-fuel|TFUEL]], so THETA's link to adoption is indirect and depends on staking/governance demand.
- **Supply note:** THETA is fully circulating (MC = FDV), so there is no unlock/emission overhang on the governance token — a structural positive relative to low-float peers.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=THETAUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=THETAUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=THETA` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=THETA` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=THETAUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=THETAUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=THETA"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---
