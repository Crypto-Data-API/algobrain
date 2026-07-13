---
title: "Golem"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, depin, ai-trading]
aliases: ["GLM", "Golem Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://golem.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[depin]]", "[[decentralized-ai]]", "[[livepeer]]"]
---

# Golem

**Golem** (ticker **GLM**, host chain **[[ethereum]]**) is one of the oldest [[decentralized-compute]] projects in crypto — a peer-to-peer marketplace where "providers" rent out idle CPU/GPU resources to "requestors" who need computing power, paid in GLM. Golem is a core **[[depin]]** (Decentralized Physical Infrastructure) network and has repositioned around supplying compute to the AI industry, competing in the same decentralized-compute trade as **[[livepeer]]**, Render, Akash, and io.net.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | GLM |
| **Native chain** | [[ethereum]] (ERC-20; Energi deployment) |
| **Price** | $0.107297 |
| **Market Cap** | $107.35M |
| **Market Cap Rank** | #259 |
| **24h Volume** | $6.06M |
| **24h Change** | +0.46% |
| **7d Change** | -2.84% |
| **Circulating Supply** | 1.00B GLM |
| **Total Supply** | 1.00B GLM |
| **Max Supply** | None recorded (effectively fixed ~1B) |
| **Fully Diluted Valuation** | $107.35M |
| **Market Cap / FDV** | ~1.00 (fully circulating) |
| **All-Time High** | $1.32 (2018-04-13) — now ~-92% |
| **All-Time Low** | $0.00913753 (2016-12-12) — now ~+11.7x |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

GLM is roughly flat (+0.46% 24h, -2.84% 7d) against an **established bear market** with the Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)** on 2026-06-21. It trades ~92% below its 2018 ATH but remains an order of magnitude above its 2016 ATL. Market cap equals FDV — GLM is fully circulating, so there is no future-unlock dilution to model.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B GLM |
| **Total Supply** | 1.00B GLM |
| **Max Supply** | 1.00B GLM (effectively fixed) |
| **Market Cap / FDV** | 1.00 (fully circulating) |

GLM is a pure **utility / medium-of-exchange token**: requestors pay GLM to have tasks computed, and providers earn GLM for supplying compute. Supply is fully circulating (~1B, MC = FDV), so there is **no unlock overhang** — a structural advantage in a market wary of vesting cliffs. GLM is the ERC-20 successor to the original GNT token (a 1:1 migration completed in 2020/2021). There is no native staking yield; token value is driven entirely by demand for compute on the network rather than emissions or lock-up mechanics.

---

## How & Where It Trades

**Spot venues:** Binance, Upbit (KRW), Bitget, KuCoin, and Crypto.com list GLM. On-chain, GLM trades on Uniswap V2/V3 and Sushiswap on Ethereum (`0x7dd9c5cba05e151c895fde1cf355c9a1d5da6429`), with a deployment on Energi.

**Derivatives:** GLM perp listings exist on some venues but liquidity is thin. With ~$6.06M of 24h volume on a ~$107M cap (~5.6% turnover), GLM is one of the quieter mid-caps — low turnover means wider effective spreads and higher slippage on size. Price discovery is dominated by spot.

**Native chain:** Ethereum (with an Energi deployment).

---

## Peer Comparison — Decentralized Compute / DePIN

| Project | Ticker | Focus | MC rank (2026-06-21) | Notes |
|---|---|---|---|---|
| **Golem** | GLM | General CPU/GPU compute | #259 | Oldest; fully circulating; demand-gap critique |
| Render | RNDR/RENDER | GPU rendering + AI inference | higher-cap | Strongest revenue narrative in cohort |
| Akash | AKT | Cloud/compute marketplace | mid-cap | Kubernetes-style decentralized cloud |
| io.net | IO | GPU aggregation for AI | mid-cap | Newer, AI-native, heavier unlocks |
| [[livepeer]] | LPT | Video transcoding + AI | mid-cap | GPU network with staking |

Golem's edge is tenure and a clean (no-unlock) cap table; its disadvantage is that rivals like Render/io.net have captured more of the AI-compute mindshare and, in some cases, more demonstrable paid usage.

---

## Valuation Framing (qualitative)

GLM is essentially a **demand-call option on decentralized compute**. With MC = FDV (~$107M) and no emissions, the cap table is clean, so the question is purely whether real paid compute throughput grows. Historically the network's *paid* utilization has lagged its ~$100M+ valuation, meaning the price embeds an option on the [[decentralized-ai]]/[[depin]] narrative converting to revenue rather than a multiple on current cash flows. A re-rate would require evidence of sustained, fee-paying AI/GPU workloads — not just listings or partnerships. In the current **extreme-fear** tape this option is being marked cheaply; the symmetric risk is that the demand gap persists and GLM continues to trade as "dead money" relative to faster-growing peers. This is qualitative framing, not a price target.

---

## Use Case & Narrative

Golem's vision is a **"global supercomputer"** — aggregating idle machines worldwide into a rentable compute marketplace. Originally targeted at CGI rendering and scientific workloads, its current narrative is **decentralized compute for AI**, supplying GPU cycles for training/inference as part of the broader **[[depin]] + [[decentralized-ai]]** thesis. The pitch versus centralized cloud (AWS, GCP) is permissionless access and lower cost; the challenge is that real, paying compute demand has historically lagged the narrative. Golem is included in DePIN-themed indices (GMCI DePIN) and tagged across AI, DePIN, and the Ethereum ecosystem.

---

## Notable History

- **2016** — Golem raises a then-landmark ICO (one of Ethereum's earliest); **ATL $0.009 on 2016-12-12** during the GNT era.
- **2018-04-13** — **ATH $1.32** during the first major alt-coin cycle.
- **2018-2019** — Brass Golem mainnet (CGI rendering) launches; adoption modest.
- **2020-2021** — Migration from GNT to the new GLM token; "New Golem" / Yagna platform launches, broadening to general compute.
- **2024-2025** — Repositioning toward supplying compute to the AI industry.
- **2026-06-21** — Trades ~$0.1073 (#259), roughly flat on the day in an extreme-fear market.

---

## Risks

- **Demand gap** — long-standing critique that actual paid compute usage is small relative to market cap; value rests on the AI-compute narrative converting to revenue.
- **Competition** — strong rivals in [[decentralized-compute]] (Render, Akash, io.net, [[livepeer]]) plus dominant centralized clouds (AWS, GCP, Azure).
- **No yield / no staking** — holders rely entirely on price appreciation from usage growth.
- **Liquidity** — low turnover (~4% of cap/day) means thin books and slippage.
- **Drawdown depth** — ~92% below ATH; one of the longest-running "build vs. adoption" stories in crypto.

---

## Related

- [[depin]] — Golem is a foundational DePIN compute network
- [[ethereum]] — its host chain
- [[decentralized-ai]] — the AI-compute pivot
- [[livepeer]] — peer decentralized-compute / GPU network
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
