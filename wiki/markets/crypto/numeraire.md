---
title: "Numeraire"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi, machine-learning]
aliases: ["NMR"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://numer.ai/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[ai-trading]]", "[[machine-learning]]", "[[defi]]", "[[uniswap]]"]
---

# Numeraire

**Numeraire** (NMR) is the [[ethereum|Ethereum]]-based [[erc-20]] token that powers **Numerai**, a hedge fund and crowdsourced data-science tournament where thousands of anonymous quants build machine-learning models to predict global equity markets. Data scientists **stake NMR** on their predictions: accurate models are rewarded with NMR, while poor predictions are burned (slashed), aligning incentives between modelers and the fund. It sits at the intersection of [[ai-trading|AI/quant finance]] and [[defi|DeFi]], trading under the ticker NMR on the [[ethereum|Ethereum]] mainnet.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | NMR |
| **Native Chain** | [[ethereum|Ethereum]] ([[erc-20]]) |
| **Market Cap Rank** | #388 |
| **Market Cap** | $61.79M |
| **Fully Diluted Valuation** | $93.38M |
| **Current Price** | $8.78 |
| **24h Volume** | $9.30M |
| **24h Change** | -0.05% |
| **7d Change** | +4.34% |
| **All-Time High** | $93.15 (2021-05-16) |
| **All-Time Low** | $2.06 (2018-11-27) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

NMR is roughly flat on the day but a relative outperformer over the week (+4.3%), holding up better than much of the small-cap cohort even as the broader tape sits in **extreme fear** (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = 23) and a long-horizon **"Established Bear Market"** regime as of 2026-06-21. The AI/quant narrative has periodically given NMR idiosyncratic strength versus generic alts. Note the MC/FDV ratio of ~0.66 — about a third of the eventual capped supply is not yet circulating, a modest dilution overhang from staking emissions (offset by burns).

---

## Tokenomics & Supply

NMR has a hard-capped, deflationary supply with staking and burning baked into the protocol's mechanics.

| Metric | Value |
|---|---|
| **Circulating Supply** | ~7.04M NMR |
| **Total Supply** | ~10.63M NMR |
| **Max Supply** | 11.00M NMR |
| **Market Cap / FDV** | ~0.66 |
| **Contract (Ethereum)** | `0x1776e1f26f98b1a5df9cd347953a26dd3cb46671` |

- **Staking & slashing:** modelers lock NMR behind their tournament predictions. Wrong calls are burned, permanently reducing supply and tying token value to the tournament's signal quality.
- **Hard cap reduced over time:** Numerai's team has historically cut NMR's maximum supply (originally far larger) toward the current ~11M ceiling, a deflationary commitment.
- **Erasure protocol:** NMR also underpins Erasure, a staking framework for selling and staking on data/predictions more broadly.

---

## How & Where It Trades

NMR is primarily a **spot** asset. Liquidity is split between major centralized exchanges and Ethereum DEXes; it does not have a major, deeply liquid perpetual market, so funding/OI is not a dominant price driver.

| Venue | Type | Typical Pair |
|---|---|---|
| Binance | CEX (spot) | NMR/USDT |
| Kraken | CEX (spot) | NMR/USD |
| Upbit | CEX (spot) | NMR/BTC |
| Bitget / KuCoin | CEX (spot) | NMR/USDT |
| Uniswap V3 (Ethereum) | DEX (spot) | NMR/WETH |

- On-chain liquidity lives in [[uniswap|Uniswap]] V2/V3 NMR/WETH pools on Ethereum, so traders pay gas plus pool slippage on DEX routes.
- With ~$6.4M of 24h volume on a ~$68M cap, turnover is moderate; the relatively small free float (~7M tokens) means price can move quickly on concentrated buying.

---

## Use Case / Narrative / Category

Numeraire is the flagship **"crowdsourced AI hedge fund"** token, a distinct niche within [[defi|DeFi]] and [[ai-trading|AI-in-finance]].

- **Numerai tournament:** data scientists download obfuscated, encrypted financial data, train ML models, and submit predictions. Numerai aggregates the best models into a **meta-model** that trades a market-neutral equity portfolio.
- **Skin in the game:** staking NMR makes predictions costly to fake; the burn-on-failure design is an early, real-world example of crypto-economic incentive alignment for [[machine-learning|machine learning]].
- **Categories:** DeFi, Analytics/AI, [[ethereum|Ethereum Ecosystem]]. Backed historically by funds including Paradigm and Union Square Ventures, which lends it a "smart-money" association.

---

## Notable History

- **2017-06-20:** NMR launched; Numerai notably **airdropped** tokens to data scientists already competing in its tournament rather than running a public sale.
- **2019:** Erasure protocol and the broader staking framework introduced, extending NMR beyond the core tournament.
- **2021 bull market:** NMR reached its all-time high of **$93.15** (2021-05-16) on the AI/DeFi narrative.
- **All-time low $2.06** (2018-11-27) during the post-ICO bear market.
- **2026:** Trading around $8.78, well below ATH but materially above its all-time low, with the AI/quant theme giving it periodic relative strength versus generic small caps.

---

## Valuation Framing (qualitative)

NMR is best understood as a **utility-and-staking token tied to a single quant fund's data tournament**, not a fee-distributing equity. Its demand floor is the **stake required to participate** in the Numerai tournament plus Erasure use; its scarcity is reinforced by the **burn-on-failure** mechanism that permanently removes slashed NMR. The bull case is that a thriving modeler ecosystem and strong meta-model performance attract more staking (and burns tighten supply toward the 11M cap); the bear case is that participation is niche and the AI premium is sentiment-driven. Because organic demand is narrow, the token can carry a large **narrative premium** that compresses quickly when AI hype rotates — making it more a thematic AI/quant bet than a cashflow valuation.

---

## Peer Comparison

| Token | Category | MC Rank | Market Cap | Supply | Edge mechanism |
|---|---|---|---|---|---|
| **NMR** (this page) | Crowdsourced AI hedge fund | #388 | ~$62M | Capped 11M, ~66% circ | Stake/burn on ML predictions |
| [[fetch-ai\|Fetch.ai / ASI]] | AI agents / infra | larger-cap | mid/large | High supply | Autonomous agent economy |
| [[bittensor\|Bittensor (TAO)]] | Decentralized ML / subnets | large-cap | large-cap | Bitcoin-style emissions | Reward for ML contribution |
| [[the-graph\|The Graph (GRT)]] | Data indexing | mid-cap | mid-cap | Inflationary | Curate/index, not predict |

NMR is the **narrowest and oldest** of the AI/data tokens: a single fund's prediction tournament rather than a general-purpose AI marketplace. That gives it a clearer, real-world fundamental anchor (the fund actually trades the meta-model) but a much smaller addressable demand base than [[bittensor|TAO]]-style networks.

---

## Risks

- **Single-protocol dependency:** NMR's value is tightly coupled to the health, performance, and reputation of the Numerai hedge fund and tournament. Underperformance or a fund wind-down would directly impair the token.
- **Niche demand:** organic NMR demand comes mainly from tournament participants staking; absent a thriving modeler base, buy-side pressure is limited.
- **Small free float / volatility:** a ~7M circulating supply makes price sensitive to large orders and prone to sharp swings, amplified in an **extreme-fear, established-bear** regime (F&G 23).
- **Smart-contract & staking risk:** staking/slashing logic and the Ethereum contract carry the usual DeFi exposure to bugs and governance changes.
- **Speculative AI premium:** part of NMR's bid is narrative-driven (AI hype). That premium can compress fast when sentiment rotates.

> *Risk note: small-cap DeFi/AI token whose fundamentals hinge on a single hedge fund's tournament. Treat narrative-driven rallies with caution during a broad bear market.*

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[ai-trading]]
- [[machine-learning]]
- [[defi]]
- [[uniswap]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet.
