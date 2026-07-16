---
title: "Golem"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, crypto, depin]
aliases: ["GLM", "Golem Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://golem.network/"
related: ["[[crypto-markets]]", "[[decentralized-ai]]", "[[depin]]", "[[ethereum]]", "[[livepeer]]"]
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

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GLM |
| **Market Cap Rank** | #260 |
| **Market Cap** | $100.66M |
| **Current Price** | $0.1006 |
| **Categories** | Artificial Intelligence (AI), DePIN |
| **Website** | [https://golem.network/](https://golem.network/) |

---

## Overview

What Is Golem Network?

Golem Network is an open-source, decentralized computing platform that is building an ecosystem to provide computing power to the AI industry. A peer-to-peer marketplace for distributed computing resources. Users engage directly on the Golem platform, exchanging GLM tokens for the utilization of their idle computing resources.

Golem allows to break down tasks into smaller subtasks and distribute them across multiple providers, enabling parallel processing. This approach boosts efficiency and speeds up the completion of complex computations.

What is GLM?

GLM or Golem Network Token is needed to pay for computations on the network and is the currency that drives the marketplace. As a Requestor, you set a bid for an amount of GLM you are willing to pay to have your task completed. As a Provider, you earn GLM by computing tasks for Requestors.

How can I get involved?

If you want to stay up to date with the latest developments and updates, join the Golem Network Discord community here: https://chat.golem.network/

On Discord you can also find support to become a Provider or a Requestor in the Golem platform.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B GLM |
| **Total Supply** | 1.00B GLM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $100.66M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.32 (2018-04-13) |
| **Current vs ATH** | -92.40% |
| **All-Time Low** | $0.00913753 (2016-12-12) |
| **Current vs ATL** | +1001.00% |
| **24h Change** | +0.65% |
| **7d Change** | +2.93% |
| **30d Change** | -12.05% |
| **1y Change** | -61.80% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x7dd9c5cba05e151c895fde1cf355c9a1d5da6429` |
| Energi | `0xf3ff3bf1d1afcbebd98a304482c4099dc953e9a8` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | GLM/USDT | N/A |
| Upbit | GLM/KRW | N/A |
| Bitget | GLM/USDT | N/A |
| KuCoin | GLM/USDT | N/A |
| Crypto.com Exchange | GLM/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X7DD9C5CBA05E151C895FDE1CF355C9A1D5DA6429/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X7DD9C5CBA05E151C895FDE1CF355C9A1D5DA6429/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://golem.network/](https://golem.network/) |
| **Twitter** | [@golemproject](https://twitter.com/golemproject) |
| **Reddit** | [https://www.reddit.com/r/GolemProject](https://www.reddit.com/r/GolemProject) |
| **Telegram** | [golemnetworkproject](https://t.me/golemnetworkproject) (467 members) |
| **Discord** | [https://discord.com/invite/golem](https://discord.com/invite/golem) |
| **GitHub** | [https://github.com/golemfactory/golem](https://github.com/golemfactory/golem) |
| **Whitepaper** | [https://golem.network/doc/Golemwhitepaper.pdf](https://golem.network/doc/Golemwhitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 20 |
| **GitHub Forks** | 3 |
| **Pull Requests Merged** | 2,595 |
| **Contributors** | 49 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.65M |
| **Market Cap Rank** | #260 |
| **24h Range** | $0.0996 — $0.1020 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
