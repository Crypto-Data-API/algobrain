---
title: "RedStone"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, oracle]
aliases: ["RED", "RedStone Oracles"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.redstone.finance/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[oracle-manipulation]]", "[[pyth-network]]"]
---

# RedStone

**RedStone** (ticker **RED**) is the governance token of RedStone Oracles, a **modular oracle** protocol that specialises in price feeds for **yield-bearing collateral** — liquid staking tokens (LSTs), liquid restaking tokens (LRTs), and Bitcoin LSTs — used by lending and money markets. RedStone deploys on [[ethereum|Ethereum]] and [[base]] and markets itself as the fastest-growing oracle, with blue-chip DeFi clients including Spark, Morpho, Compound, Pendle, Venus, [[lido|Lido]], EtherFi, Ethena, Puffer, Balancer, Lombard, Enzyme, Frax and 80+ others.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | RED |
| **Current Price** | $0.111554 |
| **Market Cap** | $47.25M |
| **Market Cap Rank** | #476 |
| **24h Volume** | $8.22M |
| **24h Change** | +8.73% |
| **7d Change** | +18.51% |
| **Fully Diluted Valuation** | $111.70M |
| **All-Time High** | $0.9325 (2025-03-06) |
| **All-Time Low** | $0.0894 (2026-06-06) |
| **Chain** | [[ethereum\|Ethereum]] / [[base\|Base]] |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

RED is one of the standout movers in the cohort: **+8.7% on the day and +18.5% on the week**, sharp relative strength against a tape where the **Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] is 23 (extreme fear)** amid an **established bear market**. The token has bounced to ~$0.112 from a recent all-time low of $0.0894 set on 2026-06-06, but remains roughly -88% below its March 2025 ATH of $0.9325. The weekly volume surge (~$8.2M/day, up sharply from prior weeks) suggests renewed speculative interest. The recovery is from a deeply depressed base, and a high-FDV unlock overhang still caps the structural picture (see Tokenomics).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~423.0M RED |
| **Total Supply** | 1.00B RED |
| **Max Supply** | 1.00B RED |
| **Fully Diluted Valuation** | $111.70M |
| **Market Cap / FDV** | ~0.42 |
| **All-Time High** | $0.9325 (2025-03-06) |
| **All-Time Low** | $0.0894 (2026-06-06) |

RED has a **hard cap of 1 billion tokens**, with roughly 42% in circulation today. The low MC/FDV ratio (~0.42) signals substantial supply still to unlock via team, investor, ecosystem, and emission allocations — a meaningful future dilution overhang to watch. The token is used for governance, securing feeds (staking/restaking-backed economic security via [[eigenlayer|EigenLayer]] AVS integration), and aligning node operators and data providers.

---

## Technology — modular pull oracle

RedStone's architecture is **modular and pull-based**, distinguishing it from the always-on push feeds of [[chainlink|Chainlink]]:

- **Off-chain signed data** — Oracle nodes sign data packages off-chain; dApps inject the latest signed data into transactions on demand ("pull" model), paying gas only when the feed is actually consumed. This makes it cheap to support many assets and many chains, since RedStone does not pay gas to push thousands of feeds that may never be read.
- **Three delivery modes** — RedStone offers **Core** (on-demand pull, data attached to the user's transaction), **Classic** (traditional on-chain push feeds for protocols that prefer them), and **X** (a low-latency, fast-update mode for perps/derivatives venues). This lets integrators trade off gas cost vs. latency per use case.
- **Yield-bearing-collateral specialism** — Its edge is fast, accurate pricing of LSTs (stETH, weETH), LRTs, and BTC LSTs, including the exchange-rate / fundamental components that lending markets need to value rebasing and yield-accruing collateral safely. This is harder than pricing a plain spot asset because the fair value depends on the staking exchange rate and accrued yield.
- **Restaking-secured** — RedStone leverages [[restaking]] / [[eigenlayer|EigenLayer]] (as an AVS) to add crypto-economic security to its feeds, with [[zero-knowledge-proofs|ZK]]-based data integrity proofs on the roadmap.

These products make RedStone a direct competitor to [[chainlink]], [[pyth-network]], and [[api3]] in the DeFi oracle market, focused on the fast-growing LST/LRT collateral niche.

---

## Market Structure & Derivatives

**Spot venues.** RED launched via **Binance Launchpool** and lists on Binance (RED/USDT), Kraken (RED/USD), Upbit (RED/KRW), Bitget, KuCoin, and Crypto.com. Liquidity spans [[ethereum|Ethereum]] and the [[base|Base]] L2.

**Derivatives.** RED perpetuals are available on major CEX futures desks and on [[hyperliquid]]; with the recent +18.5% weekly move and elevated ~$8.2M daily volume, funding can swing as leveraged positioning chases momentum. Confirm OI and funding live before sizing.

**Liquidity profile.** The week's turnover spike (~$8.2M/day, ~17% of the $47.25M cap) is high for the cohort and points to a momentum-driven re-rating off the June low rather than steady organic flow. RED is more liquid than peers like [[ssv-network|SSV]] or [[uma|UMA]] at this snapshot, but still a low-cap where depth thins beyond modest size.

---

## Use Case, Narrative & Category

RedStone is an **oracle / DeFi-infrastructure** play whose narrative is tightly coupled to the growth of **liquid staking and restaking**. As LSTs and LRTs become the dominant form of collateral in lending markets, demand for specialised, gas-efficient feeds for these assets grows — and RedStone has positioned itself as the default for that segment, citing $10bn+ secured and 80+ clients. The pull-based modular design is pitched as cheaper and more chain-agnostic than legacy push oracles, while the [[eigenlayer]] integration ties RedStone to the broader [[restaking]] thesis.

### Peer comparison — oracle protocols

| Protocol | Token | Model | Specialism | MC/FDV | Mkt cap rank |
|---|---|---|---|---|---|
| [[chainlink]] | LINK | Decentralized push + CCIP | Blue-chip general standard | high | Top-20 |
| [[pyth-network]] | PYTH | Pull (first-party publishers) | High-frequency price feeds | low | Top-100 |
| **RedStone** | **RED** | **Modular pull (signed data)** | **LST/LRT/BTC-LST collateral** | **~0.42** | **#476** |
| [[api3]] | API3 | First-party dAPIs + OEV | First-party data + OEV | — | — |
| [[tellor]] | TRB | Stake + dispute | Censorship-resistant fallback | ~0.97 | #543 |
| [[uma]] | UMA | Optimistic / dispute-based | Arbitrary assertions | ~0.70 | #549 |

RedStone's distinctive lane is the **yield-bearing-collateral** segment — pricing the LSTs and LRTs that increasingly dominate DeFi lending collateral — where its pull model and exchange-rate feeds are a genuine product differentiator versus the generalist Chainlink and the price-feed-focused Pyth.

### Valuation framing (qualitative)

RED trades at ~$47M cap but a ~$112M FDV (MC/FDV ~0.42): only ~42% of the 1B cap circulates, so the headline risk is **future unlocks**. The bull case rests on RedStone's real traction — $10bn+ secured, 80+ blue-chip integrations (Morpho, Pendle, Venus, Ethena, EtherFi, [[lido|Lido]]) — and a structurally growing LST/LRT collateral market that plays to its specialism. The bear case is the **dilution overhang** (substantial team/investor/ecosystem supply still to vest) and competition from the much larger [[chainlink]]. The recent +18.5% week is a bounce off a deeply depressed ATL base, not a return to fundamentals-driven re-rating; the sustainability of value accrual to the token (vs. the protocol) remains the open question.

---

## Notable History

- **2020-2021** — RedStone Finance founded; built its off-chain signed-data oracle architecture optimised for gas efficiency and many-asset support.
- **2023-2024** — Rapid client growth among lending and yield protocols (Morpho, Pendle, Venus, Ethena, EtherFi, etc.) on the back of LST/LRT collateral demand; positioned as a leading restaking-era oracle.
- **2025-03** — RED token generation event via **Binance Launchpool**; token reached its ATH of $0.9325 shortly after launch (2025-03-06).
- **2025-2026** — Steady decline from launch highs alongside the broader market; set a new all-time low of $0.0894 on 2026-06-06.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — Specialising in yield-bearing collateral means pricing complex assets (LSTs/LRTs) whose fair value depends on exchange rates and underlying yield; mispricing can trigger faulty liquidations or enable exploits. See [[oracle-manipulation]].
- **Pull-model liveness risk** — In a pull design, a stale or unavailable signed-data feed at the moment of need (e.g., during a volatile liquidation cascade) can leave protocols pricing on outdated data.
- **Dilution / unlock risk** — With only ~42% of the 1B cap circulating (MC/FDV ~0.42), future unlocks represent significant sell-pressure potential.
- **Concentration risk** — Revenue and relevance are concentrated in the LST/LRT/restaking vertical; a contraction in [[restaking]] or LST demand would hit RedStone disproportionately.
- **Competitive & macro risk** — Faces the much larger [[chainlink]] and high-frequency [[pyth-network]]; in an extreme-fear, established-bear regime ([[crypto-fear-and-greed-index|Fear & Greed]] 23) low-cap infra tokens with high FDV overhangs are especially vulnerable, and momentum-driven bounces like the recent week can reverse quickly.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[base]]
- [[chainlink]]
- [[pyth-network]]
- [[api3]]
- [[uma]]
- [[tellor]]
- [[restaking]]
- [[eigenlayer]]
- [[lido]]
- [[oracle-manipulation]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RED |
| **Market Cap Rank** | #449 |
| **Market Cap** | $47.45M |
| **Current Price** | $0.1054 |
| **Categories** | Infrastructure, Oracle, Binance Launchpool, Real World Assets (RWA), Base Native |
| **Website** | [https://www.redstone.finance/](https://www.redstone.finance/) |

---

## Overview

RedStone Is The Fastest Growing oracle, specialising in yield-bearing collateral for lending markets and securing $10bn+ . Blue chip DeFi protocols are our clients including Spark, Morpho, Compound, Pendle, Venus, Lido, EtherFi, Ethena, Puffer, Balancer, Lombard, Enzyme, Frax, Agora, M^0 and 80+ other Clients. RedStone provides a wide variety of in-demand assets such as LSTs, LRTs, Bitcoin LSTs and many others.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 449.98M RED |
| **Total Supply** | 1.00B RED |
| **Max Supply** | 1.00B RED |
| **Fully Diluted Valuation** | $105.44M |
| **Market Cap / FDV Ratio** | 0.45 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.9325 (2025-03-06) |
| **Current vs ATH** | -88.70% |
| **All-Time Low** | $0.0869 (2026-06-25) |
| **Current vs ATL** | +21.25% |
| **24h Change** | -2.88% |
| **7d Change** | +3.16% |
| **30d Change** | +9.81% |
| **1y Change** | -69.72% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc43c6bfeda065fe2c4c11765bf838789bd0bb5de` |
| Base | `0x4eb92702ba4cfbf80561bad64d89c706ac824960` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RED/USDT | N/A |
| Kraken | RED/USD | N/A |
| Upbit | RED/KRW | N/A |
| Bitget | RED/USDT | N/A |
| KuCoin | REDSTONE/USDT | N/A |
| Crypto.com Exchange | RED/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.redstone.finance/](https://www.redstone.finance/) |
| **Twitter** | [@redstone_defi](https://twitter.com/redstone_defi) |
| **Telegram** | [redstonefinance](https://t.me/redstonefinance) (4,157 members) |
| **Discord** | [https://discord.gg/redstonedefi](https://discord.gg/redstonedefi) |
| **GitHub** | [https://github.com/redstone-finance](https://github.com/redstone-finance) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.44M |
| **Market Cap Rank** | #449 |
| **24h Range** | $0.1050 — $0.1103 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
