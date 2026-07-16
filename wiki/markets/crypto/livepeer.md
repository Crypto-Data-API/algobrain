---
title: "Livepeer"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, crypto, depin, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["LPT"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://livepeer.org/"
related: ["[[arbitrum]]", "[[crypto-markets]]", "[[decentralized-ai]]", "[[depin]]", "[[ethereum]]", "[[golem]]", "[[proof-of-stake]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[narrative-trading]]"]
---

# Livepeer

**Livepeer** (ticker **LPT**) is a decentralized video infrastructure network — one of the flagship **[[depin]]** (Decentralized Physical Infrastructure) projects. It coordinates a global marketplace of GPU operators ("orchestrators") who perform video transcoding and, increasingly, AI inference jobs, in exchange for fees. Built on **[[ethereum]]** and scaled on **[[arbitrum]]**, Livepeer aims to be the open, low-cost media and compute layer for Web3, undercutting centralized cloud-video providers.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | LPT |
| **Price** | $1.77 |
| **Market Cap** | $88.00M |
| **Market Cap Rank** | #292 |
| **24h Volume** | $7.14M |
| **24h Change** | +0.95% |
| **7d Change** | -3.07% |
| **Fully Diluted Valuation** | $88.00M |
| **Circulating Supply** | ~49.69M LPT |
| **All-Time High** | $99.03 (2021-11-09) — ~98% below |
| **All-Time Low** | $0.354051 (2019-10-26) — ~5x above |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

LPT is roughly flat on the day (+0.95%) and modestly down on the week (-3.07%) against an **extreme-fear (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = 23)** "Established Bear Market" backdrop on 2026-06-21. It sits ~98% below its 2021 ATH but remains roughly 5x above its 2019 ATL. Note that market cap equals FDV — circulating and total supply are effectively the same (~49.69M LPT), so there is no locked-supply overhang.

Turnover is ~8% of market cap (~$7.1M on ~$88M), typical of a quiet mid-cap [[depin]] token in a fearful tape. As a work/staking token rather than a medium of exchange, LPT's long-run value tracks real transcoding and AI-inference demand routed through the network rather than transaction throughput alone.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~49.69M LPT |
| **Total Supply** | ~49.69M LPT |
| **Max Supply** | Uncapped (inflationary) |
| **Market Cap / FDV** | 1.00 (fully circulating) |

LPT is a **work/staking token**, not the network's medium of exchange — fees for transcoding are paid in ETH (and stablecoins), while LPT is staked ("bonded") by orchestrators and delegators to earn the right to perform work and a share of fees plus inflationary rewards. The protocol uses a delegated-proof-of-stake design where staked LPT routes work proportionally and backs honest behavior via slashing. Inflation is algorithmic and adjusts based on the share of supply staked, targeting high participation. Because LPT is fully circulating (MC = FDV), there is no large locked-supply overhang — a structural positive versus newer tokens.

---

## How & Where It Trades

**Spot venues:** Binance, Kraken, Upbit (KRW), Bitget, KuCoin, and Crypto.com list LPT. On-chain, LPT trades on Uniswap V2/V3 on Ethereum (`0x58b6a8a3302369daec383334672404ee733ab239`).

**Multi-chain:** Canonical deployments exist on Ethereum, Arbitrum One (`0x289ba1701c2f088cf0faf8b3705246331cb8a839` — where most staking/work now occurs to cut gas costs), and Harmony.

**Derivatives:** LPT has perp listings on major venues; liquidity is thinner than large-caps, so position carefully. With ~$7.1M 24h volume on an ~$88M cap (~8% turnover), LPT is comparatively quiet — typical of a mid-cap DePIN token in a fearful tape. There is no liquid [[hyperliquid|Hyperliquid]]-style perp dominating price discovery; the spot CEX books (Binance, Upbit KRW) carry most flow, with Arbitrum DEX liquidity as the on-chain venue.

---

## Use Case & Narrative

Livepeer's original product is **decentralized video transcoding** — converting a raw video stream into the multiple formats/bitrates needed for streaming, at a fraction of centralized cloud cost. Its more recent narrative is the **AI compute / [[decentralized-ai]]** pivot: the same network of GPU orchestrators can run AI inference jobs (image, video, and increasingly LLM workloads), positioning Livepeer in the broader "[[depin]] + AI" trade alongside peers like **[[golem]]**, Render, and Akash. CoinGecko tags it across DePIN, AI, and the Ethereum/Arbitrum ecosystems, and it is included in DePIN-themed indices (GMCI DePIN) and the Coinbase 50 Index.

---

## Valuation Framing

LPT is not a cash-flow asset in the equity sense; it is a **work-access and staking right**. Qualitatively, the bull case requires transcoding plus AI-inference fee revenue (paid in ETH/stablecoins) to grow faster than algorithmic LPT inflation, so that staking yields are funded by real demand rather than dilution. The fact that LPT is fully circulating (MC = FDV) removes the unlock overhang that weighs on tokens like [[deep|DeepBook]] (~25% circulating) or [[keeta|Keeta]] (~56%), but it does not remove inflation — uncapped issuance still dilutes non-stakers. At ~$88M cap the market is pricing Livepeer as a speculative DePIN-plus-AI option rather than a network monetizing meaningful inference volume today; re-rating depends on the AI-compute thesis converting to recurring fees. Compared with compute peers Render and Akash, Livepeer's edge is its installed orchestrator base and video-specific tooling; its risk is that general-purpose GPU clouds (centralized and decentralized) absorb the inference workloads it is targeting.

---

## Peer Comparison

| Token | Category | Mkt-cap rank | MC / FDV | Supply model | Edge / niche |
|---|---|---|---|---|---|
| **Livepeer (LPT)** | DePIN compute (video + AI) | #292 | 1.00 | Uncapped, inflationary | Video transcoding + GPU inference |
| **[[golem]] (GLM)** | DePIN compute | mid-cap | ~1.00 | Fixed-ish | General CPU/GPU compute marketplace |
| Render (RNDR) | DePIN GPU render/AI | large-cap | high | Capped migration | GPU rendering, AI inference at scale |
| Akash (AKT) | DePIN cloud compute | mid-cap | partial | Inflationary | Decentralized container/cloud compute |
| **[[siacoin|Siacoin]] (SC)** | DePIN storage | #566 | ~1.00 | Uncapped PoW | Decentralized storage (adjacent DePIN) |

*Ranks/ratios reflect the 2026-06-21 snapshot for tokens in it; Render/Akash/Golem shown qualitatively.*

---

## Notable History

- **2017-2018** — Founded by Doug Petkanics and Eric Tang; mainnet launches 2018; genesis 2018-10-01.
- **2021-11-09** — **ATH $99.03** during the Web3/NFT bull market.
- **2022-2023** — Migration of staking and transcoding work to Arbitrum to reduce fees.
- **2024-2025** — "AI compute" subnet / GPU-inference initiatives launch, broadening the network beyond video.
- **2026-06-21** — Trades ~$1.77 (rank #292), holding mid-range relative to its all-time band amid an Established Bear Market.

---

## Risks

- **Demand dependency** — token value ultimately tracks real transcoding + AI-inference demand; if usage stays low, inflationary rewards dilute holders without offsetting fee growth.
- **Inflation** — uncapped, algorithmic LPT issuance dilutes non-stakers.
- **Competition** — centralized cloud video (AWS, Cloudflare) and other DePIN/AI-compute networks (Render, Akash, [[golem]]) compete for the same workloads.
- **Drawdown depth** — ~98% below ATH; the AI-compute narrative is still unproven at scale.
- **Liquidity** — thinner order books than large-caps amplify volatility in stressed markets.

---

## Related

- [[depin]] — Livepeer is a flagship DePIN network
- [[ethereum]], [[arbitrum]] — its host chains
- [[decentralized-ai]] — the AI-inference pivot
- [[golem]] — peer decentralized-compute network
- [[proof-of-stake]] — staking/bonding model
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LPT |
| **Market Cap Rank** | #318 |
| **Market Cap** | $75.34M |
| **Current Price** | $1.52 |
| **Genesis Date** | 2018-10-01 |
| **Hashing Algorithm** | Ethash |
| **Categories** | Artificial Intelligence (AI), DePIN |
| **Website** | [https://livepeer.org/](https://livepeer.org/) |

---

## Overview

The Livepeer project aims to deliver a live video streaming network protocol that is fully decentralized, highly scalable, crypto token incentivized, and results in a solution which can serve as the live media layer in the decentralized development (web3) stack. In addition, Livepeer is meant to provide an economically efficient alternative to centralized broadcasting solutions for any existing broadcaster. In this document we describe the Livepeer Protocol - a delegated stake based protocol for incentivizing participants in a live video broadcast network in a game-theoretically secure way. We present solutions for the scalable verification of decentralized work, as well as the prevention of useless work in an attempt to game the token allocations in an inflationary system.

The Livepeer Token (LPT) is the protocol token of the Livepeer network. But it is not the medium of exchange token. Broadcasters use Ethereum's Ether (ETH) to broadcast video on the network. Nodes who contribute processing and bandwidth earn ETH in the form of fees from broadcasters. LPT is a staking token that participants who want to perform work on the network stake in order to coordinate how work gets distributed on the network, and to provide security that the work will get done honestly and correctly. LPT has the following purposes:

It serves as a bonding mechanism in a delegated proof of stake system, in which stake is delegated towards transcoders (or validators) who participate in the protocol to transcode video and validate work. The token, and potential slashing that occurs due to protocol violation, is necessary in order to secure the network against a number of attacks. More below.
It routes work through the network in proportion to the amount of staked and delegated token, essentially serving as a coordination mechanism.

It is a unit of account that is specific to the Livepeer ecosystem, which forms the basis of a SectorCoin concept, applicable to additional functionality to be i...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 49.69M LPT |
| **Total Supply** | 49.69M LPT |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $75.34M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $99.03 (2021-11-09) |
| **Current vs ATH** | -98.47% |
| **All-Time Low** | $0.3541 (2019-10-26) |
| **Current vs ATL** | +328.34% |
| **24h Change** | -1.22% |
| **7d Change** | -2.36% |
| **30d Change** | -17.15% |
| **1y Change** | -77.77% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x58b6a8a3302369daec383334672404ee733ab239` |
| Harmony Shard 0 | `0xbd3e698b51d340cc53b0cc549b598c13e0172b7c` |
| Arbitrum One | `0x289ba1701c2f088cf0faf8b3705246331cb8a839` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LPT/USDT | N/A |
| Kraken | LPT/USD | N/A |
| Upbit | LPT/KRW | N/A |
| Bitget | LPT/USDT | N/A |
| KuCoin | LPT/USDT | N/A |
| Crypto.com Exchange | LPT/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X58B6A8A3302369DAEC383334672404EE733AB239/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X58B6A8A3302369DAEC383334672404EE733AB239/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://livepeer.org/](https://livepeer.org/) |
| **Twitter** | [@Livepeer](https://twitter.com/Livepeer) |
| **Reddit** | [https://www.reddit.com/r/livepeer](https://www.reddit.com/r/livepeer) |
| **Telegram** | [livepeerorg](https://t.me/livepeerorg) (3,524 members) |
| **Discord** | [https://discord.gg/RR4kFAh](https://discord.gg/RR4kFAh) |
| **GitHub** | [https://github.com/livepeer/livepeerjs](https://github.com/livepeer/livepeerjs) |
| **Whitepaper** | [https://github.com/livepeer/wiki/blob/master/WHITEPAPER.md](https://github.com/livepeer/wiki/blob/master/WHITEPAPER.md) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 72 |
| **GitHub Forks** | 34 |
| **Pull Requests Merged** | 578 |
| **Contributors** | 40 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.08M |
| **Market Cap Rank** | #318 |
| **24h Range** | $1.51 — $1.56 |
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

LPT is tradable on **[[binance]]** — both spot (LPT/USDT) and a **USD-margined [[perpetual-futures|perpetual]]** contract carrying [[funding-rate|funding]], [[open-interest]], and [[liquidations]] data. It is **NOT** listed on [[hyperliquid|Hyperliquid]], so Binance is the primary leveraged venue and the anchor for perp-based price discovery. With a small (~$75-88M) cap and thin order books versus large-caps, leverage should be used conservatively: available perp leverage does not overcome the reality that book depth is shallow, so large market orders will move price and stops can slip in stressed tapes. Venue concentration on a single dominant perp (Binance) means funding, OI, and liquidation signals are concentrated there; size positions to the thinner book, prefer limit execution, and expect wider effective spreads than headline quotes suggest. The lack of a Hyperliquid perp removes a common cross-venue funding/basis arbitrage leg for LPT.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding on LPT when it runs persistently positive/negative, sizing to the thin book and single-venue funding regime.
- [[cash-and-carry]] — pair Binance spot LPT against the USD-M perp to lock basis when the perp trades at a premium to spot.
- [[liquidation-cascade-fade]] — small-cap thin liquidity makes LPT prone to over-extended liquidation wicks; fade the flush back toward the mean once cascades exhaust.
- [[oi-confirmed-trend]] — use Binance open-interest build alongside price to confirm genuine DePIN/AI narrative trends rather than low-conviction moves.
- [[narrative-trading]] — LPT is a DePIN + AI-compute narrative token; position around AI-inference and DePIN theme rotations that drive its beta.
- [[breakout-and-retest]] — trade confirmed breakouts of range boundaries with a retest entry to manage the higher slippage risk of a thin small-cap.

### Volatility & regime character

LPT is a **small/mid-cap [[depin]] compute token** (video transcoding + AI inference) that behaves as a high-beta altcoin: it tends to amplify BTC/ETH direction and rallies hardest during DePIN and AI-narrative rotations, then bleeds during risk-off tapes (it sits ~98% below its 2021 ATH). It is not a memecoin, so reflexivity is narrative-driven (AI-compute thesis) rather than pure meme momentum. Correlation to ETH is structurally relevant given its Ethereum/Arbitrum host chains. Thin liquidity magnifies both up-moves and drawdowns relative to large-caps.

### Risk flags

- **Liquidity / venue concentration** — thin order books and a single dominant leveraged venue (Binance; no Hyperliquid) concentrate funding/OI/liquidation flow and amplify slippage.
- **Inflation / emissions** — uncapped, algorithmic LPT issuance dilutes non-stakers even though supply is fully circulating (MC = FDV, no discrete unlock cliffs).
- **Narrative dependence** — price leans heavily on the DePIN + AI-compute thesis converting to real fee demand; narrative fade removes a key catalyst.
- **Competition** — centralized cloud video and rival DePIN/AI-compute networks (Render, Akash, [[golem]]) compete for the same workloads, a persistent overhang on the thesis.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=LPTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=LPTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=LPT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=LPT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=LPTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=LPTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=LPT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
