---
title: "Livepeer"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, depin, ai-trading]
aliases: ["LPT"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://livepeer.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[depin]]", "[[arbitrum]]", "[[proof-of-stake]]", "[[decentralized-ai]]", "[[golem]]"]
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
