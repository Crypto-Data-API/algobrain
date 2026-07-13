---
title: "Kyber Network Crystal"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["KNC", "Kyber Network", "KyberSwap"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://kyber.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-exchange]]", "[[automated-market-maker]]", "[[liquidity]]"]
---

# Kyber Network Crystal

**Kyber Network Crystal** (KNC) is the governance and utility token of **Kyber Network**, a multi-chain liquidity hub whose flagship product is **KyberSwap** — a [[decentralized-exchange|DEX]] aggregator combined with a proprietary dynamic [[automated-market-maker|AMM]]. KyberSwap routes trades across many liquidity sources to find the best rate, and runs its own concentrated and dynamic-fee pools. As of 2026-06-22 KNC trades at **$0.11768**, ranking **#831** by market capitalization with a market cap of roughly **$20.0M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | KNC |
| **Market Cap Rank** | #831 |
| **Market Cap** | ~$20.01M |
| **Current Price** | $0.11768 |
| **24h Change** | -3.97% |
| **7d Change** | -4.41% |
| **Flagship product** | KyberSwap (DEX aggregator + dynamic AMM) |
| **Backers** | Pantera Capital, YZi Labs (formerly Binance Labs) |
| **Categories** | DEX, Exchange-based Tokens, DeFi, AMM, Governance, multi-chain (Ethereum, BNB Chain, Arbitrum, Polygon, Avalanche, Optimism, Base, and others) |
| **Website** | [https://kyber.network/](https://kyber.network/) |

> In the 2026-06-22 [[crypto-market-regime|risk-off regime]] (BTC ~$64,508; Crypto [[fear-and-greed-index|Fear & Greed Index]] at 21, "Extreme Fear"), KNC fell -3.97% on the day and -4.41% on the week, underperforming a soft tape.

---

## Overview

Kyber Network is one of the oldest DeFi liquidity protocols, with roots going back to 2017–2018. Its goal is to aggregate liquidity from many sources so that DApps, exchanges, and end users can access the best available rates for on-chain token swaps. All trades settle on-chain and are verifiable via block explorers.

The protocol has evolved through several generations:

- **Kyber's original reserve-based liquidity network** (a hub-and-spoke model connecting liquidity reserves).
- **Kyber DMM (Dynamic Market Maker)**, launched in 2021 — an [[automated-market-maker|AMM]] with **dynamic fees** that adjust with volatility and **amplified pools** for capital efficiency in correlated assets.
- **KyberSwap Elastic and KyberSwap Classic** — the current product line. **KyberSwap Aggregator** routes orders across hundreds of DEXs and pools across multiple chains to optimize execution, while Kyber's own pools provide native liquidity.

The **KNC token** is the protocol's governance and incentive asset. Holders can **stake KNC in the KyberDAO** to vote on proposals and parameters, and stakers historically earned a share of protocol trading fees (distributed in assets such as ETH). KNC thus functions as a [[governance-token|governance]] + fee-sharing token rather than a pure utility token.

### How the Aggregator Routes a Trade

KyberSwap's aggregator is a **smart order router**: for a given swap it scans hundreds of liquidity sources (its own pools plus external DEXs like [[uniswap|Uniswap]], [[curve-finance|Curve]], Balancer, and chain-native venues) and **splits a single order across multiple pools and even multiple hops** to minimise price impact and maximise output. A large ETH→USDC sell might be routed, say, 40% through one Uniswap V3 pool, 35% through a Curve pool, and 25% through Kyber's own pool, all atomically in one transaction. This "best-execution" routing is the product's primary value-add and the reason it remains widely integrated even after liquidity left its native pools.

### Value Accrual

KNC's value capture runs through the **KyberDAO**: staking KNC grants governance rights and a share of protocol fees (historically paid in ETH and other assets). The dependency chain is therefore *swap volume → protocol fees → staking rewards → KNC demand*. The weak link is that **aggregation is a thin-margin, low-moat business** — routers compete on basis points of execution quality, take rates are small, and post-2023 the native-AMM fee base shrank after liquidity flight. As a result KNC's value accrual is structurally constrained relative to AMMs that capture full LP fee flow.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~170.15M KNC |
| **Total Supply** | ~240.95M KNC |
| **Max Supply** | ~252.30M KNC |
| **Fully Diluted Valuation** | ~$30M (scales with price) |
| **Market Cap / FDV Ratio** | ~0.7 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $5.70 (2022-04-29) |
| **Current vs ATH** | ~-98% |
| **24h Change** | -3.97% |
| **7d Change** | -4.41% |

KNC trades roughly 98% below its 2022 peak. The token's underperformance reflects both the broad DeFi de-rating and the lasting reputational and liquidity damage from the November 2023 KyberSwap exploit (see below).

---

## Notable History: The November 2023 KyberSwap Exploit

In **November 2023, KyberSwap Elastic was exploited for approximately $48 million** across multiple chains. The attacker used a sophisticated **"infinite money glitch"** that abused a tick-boundary / rounding edge case in the concentrated-liquidity math of KyberSwap Elastic pools, manipulating the price within a tightly bounded liquidity range to repeatedly drain funds. It was one of the more technically advanced DeFi exploits of that cycle.

Aftermath:
- KyberSwap Elastic liquidity was drained and the protocol urged LPs to withdraw remaining funds.
- The attacker engaged in on-chain negotiation, at one point posting unusual demands (including governance control) before partial movements of funds.
- The incident triggered a restructuring at Kyber Network, including layoffs, and forced a strategic refocus, with the aggregator (which itself was not the source of the bug) remaining the core ongoing product.

**Lessons / why it matters for token holders:** the bug was in **bespoke concentrated-liquidity math**, not in a simple AMM — a reminder that the very capital-efficiency features that make CL pools attractive also widen the attack surface (tick boundaries, rounding, and price-range edge cases are subtle and hard to audit exhaustively). The damage was as much **reputational and liquidity-driven** as financial: even though the aggregator (the core surviving product) was never the source of the bug, TVL and trust in Kyber's native pools fell sharply and have not fully recovered.

This event is the single most important risk fact about the protocol and is recorded here honestly rather than omitted.

---

## Worked Example: Best-Execution Routing

A trader wants to swap 500 ETH for USDC on Ethereum. Sending it through a single Uniswap pool would move the price materially (high slippage). KyberSwap's aggregator instead:

1. **Scans** all reachable pools across many DEXs for ETH/USDC depth.
2. **Optimises a split** — e.g., 30% via Uniswap V3, 30% via Curve's tri-pool path, 20% via Balancer, 20% via Kyber's own pool — and may add a multi-hop leg (ETH→WBTC→USDC) if that yields more.
3. **Executes atomically** in one transaction, so the trader gets a single, better blended price than any one venue could offer, with the routing computed to minimise total price impact and gas-adjusted cost.

This is exactly the kind of execution-quality edge that matters for larger [[trading]] flows and is why aggregators (Kyber, [[1inch|1inch]], CowSwap) sit between users and the underlying liquidity.

---

## Competitive Position

KyberSwap competes primarily as a **DEX aggregator** (against [[1inch|1inch]], [[uniswap|Uniswap]]'s routing, ParaSwap, CowSwap, and chain-native aggregators) and secondarily as an AMM. Its multi-chain reach and dynamic-fee/amplified-pool innovations were historically differentiators. Post-2023 exploit, its standing diminished relative to its mid-cycle prominence, though the aggregator remains widely integrated.

### Aggregator / DEX Comparison

| Protocol | Primary model | Distinctive feature | Token / value accrual |
|---|---|---|---|
| **KyberSwap (KNC)** | Aggregator + native dynamic/CL AMM | Multi-chain reach; dynamic fees; amplified pools | KNC staking in KyberDAO shares fees |
| **[[1inch\|1inch]] (1INCH)** | Aggregator (Pathfinder) + Fusion (intent/RFQ) | Pioneer aggregator; gasless intent-based "Fusion" swaps | 1INCH governance + staking |
| **CowSwap (COW)** | Intent-based, batch auctions w/ solvers | MEV-protection via batch settlement and coincidence-of-wants | COW governance |
| **ParaSwap (PSP)** | Aggregator | Multi-path routing, partner fee tooling | PSP governance/staking |
| **[[uniswap\|Uniswap]] (UNI)** | AMM with built-in routing (UniswapX) | Deepest first-party liquidity; intent-based UniswapX layer | UNI governance |

The strategic reality: routing is a **commoditising** layer. Differentiation increasingly comes from MEV protection and intent/RFQ execution (CowSwap, 1inch Fusion, UniswapX), where Kyber must keep pace to retain integration share.

---

## Risks

- **Exploit precedent:** The ~$48M November 2023 Elastic hack demonstrates real smart-contract risk in Kyber's concentrated-liquidity math; trust must be rebuilt.
- **Liquidity / TVL flight:** Post-hack LP withdrawals reduced native liquidity, weakening the AMM side of the business.
- **Aggregator commoditization:** Routing is a competitive, low-moat business with thin take rates.
- **Governance/value accrual:** KNC value depends on protocol fees and staking demand, both pressured by lower volumes.
- **Org risk:** Restructuring and reduced headcount can slow development and incident response.
- **Liquidity / small-cap risk:** at ~$20M market cap (rank ~#831), KNC is small and volatile; on 2026-06-22 it fell -3.97% (24h) and -4.41% (7d) into an "Extreme Fear" tape.
- **General crypto risk:** broad regulatory uncertainty and multi-chain bridge/operational exposure given KyberSwap's wide chain footprint.

---

## Governance

KNC is governed through the **KyberDAO**. Holders **stake KNC** to receive voting power and to claim a pro-rata share of protocol fees (historically distributed in ETH and other tokens). The DAO votes on fee parameters, reward distribution, treasury usage, and protocol direction. Staking-for-fees aligns long-term holders with protocol volume, but because rewards scale with trading fees, the **post-2023 decline in volume and native liquidity directly compressed staking yield**, weakening the incentive loop that underpins KNC demand. The KNC token has itself been redenominated in Kyber's history (the migration to the current KNC contract), so holders should always confirm they hold the canonical token contract.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdefa4e8a7bcba345f687a2f1456f5edd9ce97202` |
| Polygon Zkevm | `0x6a80a465409ce8d36c513129c0feea61bed579ba` |
| Fantom | `0x1e1085efaa63edfe74aad7c05a28eae4ef917c3f` |
| Linea | `0x3b2f62d42db19b30588648bf1c184865d4c3b1d6` |
| Polygon Pos | `0x1c954e8fe737f99f68fa1ccda3e51ebdb291948c` |
| Binance Smart Chain | `0xfe56d5892bdffc7bf58f2e84be1b2c32d21c308b` |
| Arbitrum One | `0xe4dddfe67e7164b0fe14e218d80dc4c08edc01cb` |
| Zksync | `0x6ee46cb7cd2f15ee1ec9534cf29a5b51c83283e6` |
| Optimistic Ethereum | `0xa00e3a3511aac35ca78530c85007afcd31753819` |
| Avalanche | `0x39fc9e94caeacb435842fadedecb783589f50f5f` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | KNC/USDT | N/A |
| Kraken | KNC/USD | N/A |
| Upbit | KNC/KRW | N/A |
| Bitget | KNC/USDT | N/A |
| KuCoin | KNC/USDT | N/A |
| Crypto.com Exchange | KNC/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://kyber.network/](https://kyber.network/) |
| **Twitter** | [@kybernetwork](https://twitter.com/kybernetwork) |
| **Reddit** | [https://www.reddit.com/r/kybernetwork/](https://www.reddit.com/r/kybernetwork/) |
| **Telegram** | [kybernetwork ](https://t.me/kybernetwork ) (8,133 members) |
| **Discord** | [https://discord.gg/kyberswap](https://discord.gg/kyberswap) |
| **GitHub** | [https://github.com/kybernetwork/KyberWallet](https://github.com/kybernetwork/KyberWallet) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 440 |
| **GitHub Forks** | 186 |
| **Pull Requests Merged** | 1,354 |
| **Contributors** | 16 |

---

## Trading Characteristics

> *The figures below are a historical April 2026 snapshot, retained for context. Current price/rank/market-cap are in the Key Facts and Market data lines above (2026-06-22).*

| Characteristic | Detail (historical, 2026-04-09) |
|---|---|
| **24h Volume** | $4.84M |
| **Market Cap Rank** | #800 |
| **24h Range** | $0.1323 — $0.1384 |
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
- [[ethereum]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[concentrated-liquidity]]
- [[1inch]]
- [[uniswap]]
- [[curve-finance]]
- [[liquidity]]
- [[governance-token]]
- [[fear-and-greed-index]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
