---
title: "JOE (Trader Joe / LFJ)"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi]
aliases: ["JOE", "Trader Joe", "LFJ"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lfj.gg/avalanche"
related: ["[[crypto-markets]]", "[[avalanche]]", "[[decentralized-exchange]]", "[[automated-market-maker]]", "[[concentrated-liquidity]]", "[[impermanent-loss]]", "[[governance-token]]", "[[liquidity-pool]]"]
---

# JOE (Trader Joe / LFJ)

**JOE** is the governance and fee-sharing token of **Trader Joe** — now branded **LFJ** ("Let's Fucking Joe" / lfj.gg) — the leading [[decentralized-exchange|decentralized exchange]] on [[avalanche|Avalanche]], with deployments also on [[arbitrum|Arbitrum]] and BNB Chain. Trader Joe's swap engine is powered by its proprietary **Liquidity Book**, a discretized [[concentrated-liquidity|concentrated-liquidity]] [[automated-market-maker|AMM]]. As of 2026-06-22 JOE trades at **$0.0321257**, ranking **#962** by market capitalization with a market cap of roughly **$14.69M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Price $0.0321257 · rank #962 · market cap $14,685,812 · 24h +0.09% · 7d +1.26%. Market-wide sentiment: Fear & Greed Index 21 (Extreme Fear).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | JOE |
| **Market Cap Rank** | #962 |
| **Market Cap** | ~$14.69M |
| **Current Price** | $0.0321257 |
| **24h Change** | +0.09% |
| **7d Change** | +1.26% |
| **Brand** | Trader Joe → LFJ |
| **Home chain** | Avalanche (also Arbitrum, BNB Chain) |
| **AMM** | Liquidity Book (concentrated, "bin"-based) |
| **Categories** | DEX, Exchange-based Tokens, DeFi, Yield Farming, AMM, Launchpad, DEX Aggregator |
| **Website** | [https://lfj.gg/avalanche](https://lfj.gg/avalanche) |

> In the 2026-06-22 [[crypto-market-regime|Extreme-Fear regime]] (Fear & Greed Index 21), JOE held up better than most mid-cap DeFi tokens — essentially flat at +0.09% over 24h and +1.26% on the week — supported by its entrenched position as Avalanche's flagship DEX.

---

## Overview

Trader Joe launched in 2021 as Avalanche's flagship DeFi platform and quickly became the dominant DEX of the Avalanche ecosystem. The platform offers token **swaps**, **liquidity provision**, **yield farming**, lending (historically via "Banker Joe"), a launchpad ("Rocket Joe"/Launchpad), and an NFT marketplace ("Joepegs"). In 2024 the team rebranded the product to **LFJ** while keeping the JOE ticker.

The protocol's key technical contribution is the **Liquidity Book (LB)** AMM. Unlike Uniswap V3's continuous tick ranges, Liquidity Book uses discrete price **"bins."** Liquidity placed in a bin trades at a single fixed price with **zero slippage within that bin**, and LPs can shape their liquidity distribution across bins. LB also supports **variable/dynamic fees** that rise with volatility, helping compensate LPs for impermanent loss during turbulent markets. This makes it a distinctive flavor of [[concentrated-liquidity|concentrated liquidity]].

The **JOE token** is the native governance token and also **accrues a share of trading fees** collected by the protocol (historically via staking JOE into sJOE / veJOE / rJOE mechanisms, which routed protocol revenue or boosts to stakers). JOE thus combines [[governance-token|governance]] with a fee/value-accrual role.

---

## Mechanism & Architecture: the Liquidity Book

The Liquidity Book (LB) is best understood by contrast with the two dominant [[automated-market-maker|AMM]] designs:

- **[[uniswap]] V2 (constant product, `x*y=k`)** — liquidity is spread across the entire price range from 0 to ∞. Capital is heavily diluted; slippage is continuous and present on every trade.
- **Uniswap V3 (continuous concentrated liquidity)** — LPs choose a continuous price *range*; capital is concentrated, but price still moves continuously *within* the range, so every fill incurs some slippage and LP accounting uses non-fungible positions.
- **Liquidity Book (discrete bins)** — the price axis is chopped into discrete **bins**, each a fixed-width price step. All liquidity inside a bin trades at one constant price with **zero slippage until that bin is exhausted**; price moves only when a bin empties and trading rolls into the next. LP positions within a bin are **fungible**, simplifying composability.

Two consequences matter for traders and LPs:

1. **Zero-slippage-within-bin** approximates an [[order-book]] at the bin price, useful for stable or pegged pairs.
2. **Dynamic / variable fees** — LB layers a volatility-based surcharge on the base fee. When price oscillates rapidly across bins (a proxy for toxic, [[impermanent-loss|IL]]-inducing flow), the fee rises, compensating LPs for the adverse selection that classic AMMs absorb at a fixed fee. This is LB's most important economic innovation: it lets passive LPs charge more precisely when they are being picked off.

### Worked example (illustrative)

An LP concentrates AVAX/USDC liquidity in a few bins straddling the current price. While AVAX trades sideways, swaps clear at bin price with zero slippage and the LP earns the low base fee on high volume. When AVAX then whipsaws on a news spike, the dynamic-fee component spikes, so the same LP captures a larger fee on the volatile flow — partially offsetting the [[impermanent-loss]] from the price move. A static-fee Uniswap-V2 LP would have eaten the IL while still charging only the flat fee. Numbers are illustrative; the mechanism is the point.

---

## Comparison vs Competitors

| DEX | Home turf | AMM design | Distinctive edge | Main constraint |
|---|---|---|---|---|
| **Trader Joe / LFJ (JOE)** | [[avalanche\|Avalanche]] (+ Arbitrum, BNB) | Liquidity Book (discrete-bin concentrated) | Zero-slippage bins + volatility-scaled dynamic fees | Tied to Avalanche DeFi activity |
| [[uniswap\|Uniswap]] | Ethereum + many L2s | V2 constant product / V3–V4 continuous concentrated | Deepest liquidity, broadest reach, V4 hooks | Generic; commoditized fees |
| [[curve-finance\|Curve]] | Ethereum + multichain | StableSwap invariant | Best-in-class stable/pegged swaps | Narrow to correlated assets |
| [[dodo\|DODO]] | Multichain | Proactive Market Maker (oracle-anchored) | Single-token LP, CEX-like depth | Oracle dependence |
| [[pancakeswap\|PancakeSwap]] | BNB Chain (+ multichain) | V2/V3 forks + LB licensing | Scale on BNB, low fees | Crowded multichain push |

LB is a genuine technical differentiator versus the wave of Uniswap V2/V3 forks; PancakeSwap notably adopted a Liquidity-Book-style design under license, validating the model.

---

## Governance & Value Accrual

- **sJOE** — stake JOE to receive a share of protocol revenue paid in stablecoins ([[usdc]]); a direct fee-share, the cleanest value-accrual leg.
- **veJOE / rJOE (historical)** — vote-escrowed and "rocket" variants used to direct liquidity-mining boosts and launchpad ("Rocket Joe") allocations, in the [[curve-finance|Curve]]-style vote-escrow lineage.
- **Governance** — JOE holders steer protocol parameters, emissions and treasury via the LFJ governance process.

The accrual is revenue-reflexive: sJOE distributions rise and fall with trading volume, which in turn tracks Avalanche DeFi activity. With ~80% of the capped 500M supply already circulating (MC/FDV ≈ 0.81), emission-driven dilution is limited relative to uncapped peers — the swing factor is volume, not new supply.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~403.57M JOE |
| **Total Supply** | ~499.71M JOE |
| **Max Supply** | 500.00M JOE |
| **Fully Diluted Valuation** | ~$16M (scales with price) |
| **Market Cap / FDV Ratio** | ~0.81 |

JOE has a hard cap of 500 million tokens, with most already in circulation — limiting future emission-driven dilution relative to uncapped peers.

---

## History & Notable Events

- **2021** — Trader Joe launches as Avalanche's flagship DeFi platform; rapidly becomes the dominant DEX of the ecosystem during the Avalanche "rush" growth program. JOE hits its all-time high of **$5.09 on 2021-11-21**.
- **2022** — Ships the **Liquidity Book (LB)** AMM, its discrete-bin concentrated-liquidity design with dynamic fees — a clean break from being "another Uniswap fork." Expands beyond Avalanche to [[arbitrum|Arbitrum]] and BNB Chain.
- **2022–2023** — Broadens product surface: lending ("Banker Joe"), launchpad ("Rocket Joe"), DEX aggregator, and the **Joepegs** NFT marketplace.
- **2024** — **Rebrands the product to LFJ** ("Let's Fucking Joe", lfj.gg) while retaining the JOE ticker and contracts. Liquidity-Book-style designs are adopted by other DEXs (e.g., PancakeSwap under license), validating the model.
- **2025–2026** — Operates as Avalanche's leading DEX through the bear regime; JOE trades ~99% below its cycle high, with fortunes coupled to Avalanche DeFi activity.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $5.09 (2021-11-21) |
| **Current vs ATH** | ~-99% |
| **24h Change** | +0.09% |
| **7d Change** | +1.26% |

JOE trades roughly 99% below its November 2021 ATH, reflecting both the broad DeFi drawdown and the relative cooling of the Avalanche ecosystem versus its 2021 peak. Price action into 2026-06-22 was resilient given the Extreme-Fear backdrop — broadly flat on the day (+0.09%) and slightly up on the week (+1.26%).

---

## Competitive Position

Trader Joe/LFJ is the leading DEX on Avalanche by liquidity and volume, and a meaningful (though smaller) player on Arbitrum and BNB Chain. Its Liquidity Book AMM is a genuine technical differentiator versus generic Uniswap V2/V3 forks, particularly its zero-slippage bins and dynamic fees. Its main constraint is ecosystem-level: its fortunes are tightly coupled to Avalanche's relative DeFi activity, which faces strong competition from Solana, Base, Arbitrum, and others.

---

## Risks

- **Ecosystem concentration:** Heavy dependence on Avalanche's DeFi activity; if Avalanche volumes stay subdued, fees and JOE value accrual suffer.
- **Smart-contract risk:** The custom Liquidity Book code is sophisticated and carries audit/exploit risk inherent to novel AMM math.
- **Competition:** DEX fee compression and aggressive incentives from rival chains pressure margins.
- **Value-accrual dependence:** JOE benefits require sustained fee revenue and staking demand.
- **Liquidity / volatility:** A ~$15M-cap token can be volatile, as the recent double-digit daily swings show.

---

## Platform & Chain Information

**Native Chain:** Avalanche

### Contract Addresses

| Chain | Address |
|---|---|
| Avalanche | `0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd` |
| Mantle | `0x371c7ec6d8039ff7933a2aa28eb827ffe1f52f07` |
| Binance Smart Chain | `0x371c7ec6d8039ff7933a2aa28eb827ffe1f52f07` |
| Arbitrum One | `0x371c7ec6d8039ff7933a2aa28eb827ffe1f52f07` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | JOE/USDT | N/A |
| Kraken | JOE/USD | N/A |
| Bitget | JOE/USDT | N/A |
| Crypto.com Exchange | JOE/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lfj.gg/avalanche](https://lfj.gg/avalanche) |
| **Twitter** | [@LFJ_gg](https://twitter.com/LFJ_gg) |
| **Discord** | [https://discord.com/invite/lfj](https://discord.com/invite/lfj) |
| **GitHub** | [https://docs.lfj.gg](https://docs.lfj.gg) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $62.54M |
| **Market Cap Rank** | #813 |
| **24h Range** | $0.0508 — $0.0758 |
| **CoinGecko Sentiment** | 75% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[avalanche]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[concentrated-liquidity]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
