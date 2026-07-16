---
title: "CoW Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["COW"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://cow.fi"
related: ["[[ai-mev]]", "[[ai-solvers]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[intent-based-trading]]", "[[mev-strategies]]"]
---

# CoW Protocol

**CoW Protocol** (ticker **COW**) is an [[ethereum|Ethereum]]-based **intent-driven trading and [[mev|MEV]]-protection layer** — a meta-[[dex|DEX]] / [[dex|DEX aggregator]] whose flagship front-end CoW Swap lets users sign trade *intents* (desired outcomes) rather than transactions, which competing solvers then execute via **batch auctions**. The name comes from **Coincidence of Wants (CoW)**: when two opposite orders can be matched directly peer-to-peer without touching an on-chain liquidity pool, eliminating slippage and MEV for that portion. COW is the governance token of CowDAO and grants trading-fee discounts on CoW Swap.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | COW |
| **Chain** | [[ethereum\|Ethereum]] (+ Gnosis, Arbitrum, Base, Polygon, BNB) |
| **Market Cap Rank** | #284 |
| **Market Cap** | $90.96M |
| **Current Price** | $0.157317 |
| **24h Change** | +1.03% |
| **7d Change** | +6.90% |
| **24h Volume** | $5.34M |
| **Circulating Supply** | ~578.04M COW |
| **Total / Max Supply** | 1.00B COW |
| **All-Time High** | $2.22 (2022-03-28) |
| **All-Time Low** | $0.03987 (2022-11-09) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: against an **Established Bear Market** regime with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)** as of 2026-06-21, COW outperformed over the trailing week (+6.9% 7d) while also up ~+1% on the day — notable relative strength for a small-cap [[defi|DeFi]] token. At $0.157 it trades ~93% below its 2022 ATH ($2.22) but roughly 4x off its 2022 cycle low ($0.0399).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~578.04M COW |
| **Total Supply** | 1.00B COW |
| **Max Supply** | 1.00B COW |
| **Market Cap / FDV** | ~0.58 |
| **Fully Diluted Valuation** | ~$157M |

About **58% of max supply circulates**, leaving moderate dilution headroom — FDV is roughly **1.7x** the current market cap, so unvested team/DAO/ecosystem allocations remain a structural supply overhang to watch. COW's utility centers on **governance via CowDAO** and **fee discounts** for traders who hold it. Protocol fees accrue to CowDAO, which can direct treasury and incentive policy. The token is **not** a direct cash-flow claim: value capture is governance + discount utility rather than fee distribution, a recurring weakness across [[defi|DeFi]] governance tokens.

---

## Technology & Protocol

CoW Swap does **not** route the user's trade through a single [[automated-market-maker|AMM]]. Instead:

1. Users sign an **intent** ("swap X for at least Y of Z"), gas-free and off-chain.
2. A network of competing **solvers** ([[ai-solvers|see solvers]]) bid in a **batch auction** to find the best execution — they may match opposite intents directly (a **Coincidence of Wants**), tap multiple on-chain liquidity sources, or combine both.
3. The winning solver settles the whole batch on-chain at a single clearing price, with **uniform clearing prices** within a batch that neutralize sandwich / front-running [[mev|MEV]] attacks and pass solver surplus back to users.

This makes CoW a **[[dex|DEX]] aggregator + [[mev|MEV]]-protection layer** rather than a liquidity venue itself. It is a leading example of [[intent-based-trading|intent-based trading]] and [[ai-mev|MEV-aware execution]]. CoW also offers programmatic order types (TWAP, milkman/oracle orders) and **CoW Hooks** for composable pre/post-trade actions, plus **CoW AMM** — an MEV-capturing AMM design that protects liquidity providers from loss-versus-rebalancing (LVR).

## Market Structure & Derivatives

**Spot venues (CEX):** COW trades on Binance, Kraken, Upbit (KRW), Bitget, KuCoin, and Crypto.com Exchange.

**On-chain spot:** Liquid on [[uniswap]] V3 (Ethereum, vs WETH) and Balancer V2; deployed across Gnosis Chain, Arbitrum, Base, Polygon, and BNB Chain.

**Liquidity & depth:** ~$5.3M daily volume against a ~$91M cap (turnover ~6%) is moderate for a small-cap — adequate for retail size but thin for large blocks, where slippage and venue fragmentation across five-plus chains matter.

**Derivatives:** COW is not prominently listed as a perpetual on major perp DEXs (no [[hyperliquid|Hyperliquid]] perp in the venue data), so its trading is dominated by spot CEX/DEX flow rather than leveraged derivatives — a structurally lower-beta profile than perp-heavy narrative tokens.

---

## Peer Comparison

| Token | Category | Mcap Rank | Market Cap | MC/FDV | Differentiator |
|---|---|---|---|---|---|
| **CoW Protocol (COW)** | Intent / batch-auction DEX, MEV protection | #284 | ~$91M | ~0.58 | Batch auctions + solver competition + CoW AMM |
| [[uniswap\|Uniswap (UNI)]] | AMM DEX (UniswapX intents) | — | larger | — | Dominant on-chain liquidity venue |
| 1inch (1INCH) | DEX aggregator + Fusion intents | — | comparable | — | Aggregation + Fusion RFQ/intent mode |
| [[pendle\|—]] / 0x | RFQ / liquidity routing | — | — | — | Professional market-maker RFQ |

CoW's edge versus aggregators is **MEV protection by construction** (batch auctions with uniform clearing prices) rather than as an add-on. Its main competitive pressure is UniswapX and 1inch Fusion, which bring intent/RFQ execution to far larger user bases.

---

## Valuation Framing

COW is best framed as a **call option on intent-based execution becoming the default**. Because the token captures governance and discounts rather than direct fees, fundamental valuation hinges on whether CowDAO eventually routes value to holders (fee switch, buybacks, or AMM revenue) and on settled volume growth. With FDV ~1.7x cap and limited cash-flow accrual today, COW screens as narrative/optionality exposure, not a yield asset. Qualitative only — not a price target.

---

## Use Case / Narrative / Category

CoW Protocol sits at the intersection of **DEX aggregation, MEV protection, and intent-based architecture** — increasingly central narratives as the industry moves from "send a transaction" to "express an intent and let solvers compete." The category bet is that intent + batch-auction settlement becomes the default safe way to trade on-chain, with CowDAO capturing fees from the order flow it routes. CoW also offers programmatic order types (TWAP, milkman/oracle orders) and "CoW Hooks" for composable pre/post-trade actions.

---

## Notable History

- Originated from the Gnosis ecosystem as Gnosis Protocol v2 / CowSwap, later spun out as **CoW Protocol** with the COW governance token and CowDAO.
- Pioneered **batch auctions with uniform clearing prices** and a competitive **solver** market as a structural defense against MEV.
- COW reached an all-time high of **$2.22 (2022-03-28)** and bottomed at **$0.0399 (2022-11-09)**; it has since traded well below the ATH through the bear market.
- Continued expansion across L2s/sidechains (Gnosis Chain, Arbitrum, Base, Polygon, BNB Chain).

---

## Risks

- **Solver centralization:** Execution quality depends on a healthy, competitive solver set; concentration among a few solvers is a risk vector.
- **Smart-contract / settlement risk:** Batch settlement contracts and solver logic are complex attack surfaces.
- **Token value capture:** COW is governance + fee-discount utility; direct revenue accrual to holders is limited, a common DeFi-token weakness.
- **Competition:** Other aggregators and intent/MEV-protection systems (1inch, UniswapX, etc.) compete for the same order flow.
- **Bear-market / liquidity risk:** Small-cap status (#284) and the extreme-fear (Fear & Greed 23), Established Bear Market backdrop amplify volatility and slippage.
- **Dilution overhang:** ~42% of supply not yet circulating (MC/FDV ~0.58); future unlocks can pressure price.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[dex]]
- [[decentralized-exchange]]
- [[mev]]
- [[intent-based-trading]]
- [[mev-strategies]]
- [[ai-solvers]]
- [[ai-mev]]
- [[uniswap]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-21 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | COW |
| **Market Cap Rank** | #290 |
| **Market Cap** | $85.20M |
| **Current Price** | $0.1474 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), MEV Protection, Intent |
| **Website** | [https://cow.fi](https://cow.fi) |

---

## Overview

COW token allows its holders the right to govern and curate the infrastructure of the CoW Protocol ecosystem through the CowDAO. Additionally, COW token holders receive fee discounts when trading on CowSwap &amp; some other perks.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 578.17M COW |
| **Total Supply** | 1.00B COW |
| **Max Supply** | 1.00B COW |
| **Fully Diluted Valuation** | $147.36M |
| **Market Cap / FDV Ratio** | 0.58 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.22 (2022-03-28) |
| **Current vs ATH** | -93.36% |
| **All-Time Low** | $0.0399 (2022-11-09) |
| **Current vs ATL** | +269.44% |
| **24h Change** | +1.71% |
| **7d Change** | +7.40% |
| **30d Change** | -8.60% |
| **1y Change** | -66.40% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdef1ca1fb7fbcdc777520aa7f396b4e015f497ab` |
| Binance Smart Chain | `0x5bfdaa3f7c28b9994b56135403bf1acea02595b0` |
| Base | `0xc694a91e6b071bf030a18bd3053a7fe09b6dae69` |
| Xdai | `0x177127622c4a00f3d409b75571e12cb3c8973d3c` |
| Arbitrum One | `0xcb8b5cd20bdcaea9a010ac1f8d835824f5c87a04` |
| Polygon Pos | `0x2f4efd3aa42e15a1ec6114547151b63ee5d39958` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | COW/USDT | N/A |
| Kraken | COW/EUR | N/A |
| Upbit | COW/KRW | N/A |
| Bitget | COW/USDT | N/A |
| KuCoin | COW/USDT | N/A |
| Crypto.com Exchange | COW/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Balancer V2 | 0X6810E776880C02933D47DB1B9FC05908E5386B96/0XDEF1CA1FB7FBCDC777520AA7F396B4E015F497AB | Spot |
| Uniswap V3 (Ethereum) | 0XDEF1CA1FB7FBCDC777520AA7F396B4E015F497AB/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://cow.fi](https://cow.fi) |
| **Twitter** | [@CoWSwap](https://twitter.com/CoWSwap) |
| **Discord** | [https://discord.gg/cowprotocol](https://discord.gg/cowprotocol) |
| **GitHub** | [https://github.com/gnosis/cow-token/](https://github.com/gnosis/cow-token/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 67 |
| **GitHub Forks** | 4 |
| **Pull Requests Merged** | 137 |
| **Contributors** | 5 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.84M |
| **Market Cap Rank** | #290 |
| **24h Range** | $0.1449 — $0.1500 |
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
