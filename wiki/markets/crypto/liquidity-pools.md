---
title: "Liquidity Pools"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi, liquidity]
aliases: ["Liquidity Pools", "LP Pools", "AMM Pools"]
domain: [market-microstructure, defi]
difficulty: intermediate
related: ["[[uniswap]]", "[[impermanent-loss]]", "[[defi]]", "[[decentralized-exchanges]]", "[[yield-farming]]"]
---

Liquidity pools are smart-contract-based reserves of token pairs that enable decentralized token swaps without a traditional order book or [[market-making|market maker]]. They are the foundational mechanism behind [[automated-market-maker|Automated Market Makers (AMMs)]], which power the majority of trading volume on [[defi|decentralized finance]] platforms such as [[uniswap|Uniswap]], SushiSwap, Curve, and Balancer. Instead of matching buyers and sellers, traders swap against the pooled liquidity, and liquidity providers (LPs) earn a share of trading fees proportional to their contribution. Pools are the reserves that [[on-chain-trading|on-chain trades]] execute against and the source of capital for [[flash-loans|flash loans]].

## The AMM Mechanism

Traditional exchanges use order books where buyers and sellers post limit orders at specific prices. AMMs replace this with a mathematical pricing function applied to a pool of tokens. The most common formula is the constant product model, popularized by Uniswap: **x · y = k**, where x and y are the reserves of two tokens and k is a constant. When a trader swaps token A for token B, they add A to the pool and remove B, which changes the ratio of reserves and thus the price. The larger the trade relative to pool size, the more the price moves (slippage). This simple mechanism enables permissionless, 24/7 trading for any token pair without requiring a centralized intermediary or professional market makers.

The instantaneous (marginal) price of token X in terms of token Y is simply the ratio of reserves, **P = y / x**. Because k is held constant through every swap, removing X tokens forces the X reserve down and the Y reserve up, which raises the price of the remaining X — this is the AMM's automatic price discovery.

## Worked Example: x · y = k Price Impact

Consider an ETH/USDC pool seeded with **10 ETH and 20,000 USDC**, so the starting price is 2,000 USDC per ETH.

- k = x · y = 10 × 20,000 = **200,000**
- Spot price before trade = 20,000 / 10 = **$2,000 / ETH**

A trader wants to **buy 1 ETH** from the pool (ignore fees for clarity). After the trade the ETH reserve falls to 9 ETH. To keep k constant, the USDC reserve must rise to:

- New USDC reserve = k / new ETH reserve = 200,000 / 9 ≈ **22,222.2 USDC**
- USDC the trader must deposit = 22,222.2 − 20,000 = **2,222.2 USDC**

So buying 1 ETH costs **2,222.2 USDC**, an **effective price of ~$2,222 per ETH** — about **11% above** the $2,000 spot price. That gap is the **price impact / slippage**, and it grows non-linearly with trade size:

| ETH bought | USDC paid | Effective price | Slippage vs $2,000 | New pool price |
|-----------:|----------:|----------------:|-------------------:|---------------:|
| 0.1 | 202.0 | $2,020 | +1.0% | $2,040 |
| 1.0 | 2,222.2 | $2,222 | +11.1% | $2,469 |
| 2.0 | 5,000.0 | $2,500 | +25.0% | $3,125 |
| 5.0 | 20,000.0 | $4,000 | +100.0% | $8,000 |

The lesson: in a small pool, a 5 ETH order (half the reserves) doubles the average execution price. Deep pools have the same curve but much larger k, so the same dollar trade barely nudges the price. This is why liquidity depth, not just listing, determines tradability. Arbitrageurs then trade the pool back toward the external market price, and the fees they pay accrue to LPs.

## Liquidity Provision and Fees

Anyone can become a liquidity provider by depositing an equal *value* of both tokens into a pool. In return, the LP receives pool ("LP") tokens representing their proportional share of the reserves. When traders swap against the pool, they pay a fee (typically 0.30% on Uniswap v2), which is added to the pool reserves and accrues to LP token holders. LPs can withdraw their share at any time by burning their pool tokens. The fee income compensates LPs for the capital they commit and the risks they bear — chiefly [[impermanent-loss|impermanent loss]].

### LP Economics: When Is Providing Liquidity Profitable?

An LP is, in effect, a short-volatility position: they collect fees but lose to price divergence. The position is profitable when:

**fee income + incentive emissions > impermanent loss + gas/management costs**

This means LPs prefer **high-volume, low-volatility pairs** (e.g. stablecoin pairs on Curve, where IL is near zero but volume is high) and are punished by **low-volume, high-volatility pairs** (a thin pool of two trending tokens, where IL dwarfs fees). The rise of [[yield-farming|liquidity-mining]] incentives historically masked this trade-off — emissions paid LPs to absorb IL — but those rewards are mercenary and evaporate when emissions stop, a dynamic linked to the [[liquidity-trap|liquidity trap]].

## Concentrated Liquidity

Uniswap v3 (launched May 2021) introduced concentrated liquidity, allowing LPs to specify a price range within which their capital is active. Instead of spreading liquidity across the entire price curve from 0 to infinity, LPs can concentrate it around the current market price, dramatically improving capital efficiency — by a reported factor of up to ~4,000× in the tightest ranges. An LP providing liquidity in a narrow band earns fees as if they had deployed far more capital in a v2-style pool. However, if the price moves outside the chosen range, the position goes inactive (earns no fees) and ends up 100% in the weaker token. This converts the passive "set and forget" model of v2 into an active position-management problem closer to running a market-making book.

## Comparison of Major AMM Designs

Different protocols use different invariant functions tuned to different asset types:

| Protocol | Invariant / model | Typical fee tiers | Best suited for | Key trait |
|----------|-------------------|-------------------|-----------------|-----------|
| **Uniswap v2** | Constant product x·y=k | 0.30% | Any volatile pair | Simple, full-range, passive |
| **Uniswap v3** | Concentrated liquidity (x·y=k within a range) | 0.01% / 0.05% / 0.30% / 1.00% | Active LPs, all pairs | High capital efficiency, active management |
| **Curve** | StableSwap (hybrid constant-sum + constant-product) | ~0.01%–0.04% | Stablecoins & pegged assets (USDC/USDT, stETH/ETH) | Very low slippage near peg |
| **Balancer** | Weighted geometric mean (x^w·y^w…=k) | Customizable | Multi-asset & non-50/50 pools | Up to 8 tokens, custom weights (e.g. 80/20) |

- **Curve's StableSwap** flattens the price curve near the 1:1 peg, so large stablecoin swaps incur minimal slippage — at the cost of severe price impact if a peg breaks.
- **Balancer** generalizes the constant-product formula to a weighted product of many tokens, letting a pool behave like a self-rebalancing index fund (e.g. an 80/20 BAL/ETH pool).
- **Uniswap v3** is effectively a superset of v2 — a v3 position spanning (0, ∞) reproduces v2 behaviour.

## Risks

**[[impermanent-loss|Impermanent loss]]** is the primary risk for LPs. It occurs when the price ratio of the two tokens diverges from the ratio at deposit. The LP's position underperforms a simple buy-and-hold of the two tokens; the loss is "impermanent" only if prices revert, and becomes permanent on withdrawal otherwise. For volatile pairs, this can easily exceed fee income. **Smart contract risk** is ever-present — bugs or exploits in pool contracts have drained billions of dollars from DeFi since 2020. **Rug pulls** occur when a malicious token creator seeds a pool, attracts liquidity, then pulls all value via a supply mint or contract backdoor. **Toxic order flow / [[mev|MEV]]** also erodes LP returns: arbitrageurs and sandwich bots extract value from stale pool prices before honest LPs can react (sometimes called LVR — loss-versus-rebalancing).

### Impermanent Loss vs. Price Divergence

For a constant-product (x·y=k) pool, IL depends only on the price ratio change, not the direction:

| Price change of one token | Impermanent loss vs. HODL |
|--------------------------:|--------------------------:|
| 1.25× | ~0.6% |
| 1.5× | ~2.0% |
| 2× | ~5.7% |
| 4× | ~20.0% |
| 5× | ~25.5% |
| 10× | ~42.5% |

The curve is symmetric: a token falling to half its price produces the same IL as one doubling. This is why concentrated-liquidity LPs in [[uniswap|Uniswap]] v3 face *amplified* IL inside their range — the same divergence maps to a larger loss because the capital is more tightly deployed.

### Risk Summary

| Risk | Affected party | Mitigation |
|------|----------------|------------|
| [[impermanent-loss\|Impermanent loss]] | LPs | Stable/correlated pairs, fee-rich pools, hedging |
| Smart-contract exploit | LPs & traders | Audited, battle-tested protocols; [[defi-hacks-and-exploits]] |
| Rug pull / mint backdoor | Liquidity providers & buyers | Locked liquidity, verified contracts, token scanners |
| [[mev\|MEV]] / sandwiching | LPs & traders | Private order flow, batch auctions ([[on-chain-trading]]) |
| Thin-pool exit | Token holders | Check real depth before sizing (see [[liquidity-trap]]) |

## Related

- [[uniswap]] — the leading AMM protocol
- [[impermanent-loss]] — the key risk for liquidity providers
- [[defi]] — the broader decentralized finance ecosystem
- [[decentralized-exchanges]] — venues built on liquidity pools
- [[market-making]] — the traditional finance equivalent
- [[yield-farming]] — strategies for maximizing LP returns
- [[automated-market-maker]] — the pricing engine pools feed
- [[staking]] — an alternative on-chain yield source
- [[on-chain-trading]] — trades execute against pool reserves
- [[flash-loans]] — borrow from pools atomically; also the surface for oracle manipulation
- [[liquidity-trap]] — when pool depth is too thin to exit

## Sources

- General market knowledge; no specific wiki source ingested yet.
