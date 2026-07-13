---
title: "Liquidity Provision"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [crypto, defi, amm, yield, market-making]
aliases: ["liquidity providing", "providing liquidity", "AMM liquidity provision", "DeFi LP"]
domain: [crypto, defi]
difficulty: intermediate
related: ["[[decentralized-exchanges]]", "[[uniswap]]", "[[curve-dao-token|Curve]]", "[[market-maker]]", "[[liquidity-provider]]", "[[concentrated-liquidity]]", "[[impermanent-loss]]", "[[automated-market-maker]]"]
---

Liquidity provision is the practice of depositing token pairs (or single-sided assets) into an automated market maker (AMM) pool so that other users can trade against the pool. In return, liquidity providers (LPs) earn a pro-rata share of the pool's trading fees — plus, often, additional incentive token emissions. LPs are the decentralized equivalent of a [[market-maker]], except the pricing is handled algorithmically by the AMM curve rather than by an order book.

> **Scope note:** this page covers liquidity provision in the **DeFi / AMM** sense. For the traditional-markets concept — registered market makers and HFT firms posting two-sided quotes on a limit order book — see [[liquidity-provider]].

## AMM Pool Mechanics

Different AMM designs suit different assets:

- **Constant product** (`x*y=k`, Uniswap v2) — works for any pair but is capital-inefficient, spreading liquidity across all prices from zero to infinity
- **Stable swap** (Curve) — a flatter curve optimized for assets that should trade near 1:1 (USDC/USDT, stETH/ETH), concentrating liquidity near parity
- **Concentrated liquidity** (Uniswap v3) — LPs choose a custom price range, magnifying fee earnings but also magnifying [[impermanent-loss]] risk when price exits the range
- **Weighted pools** (Balancer) — customizable weights (e.g., 80/20) that blend LP'ing with portfolio rebalancing

## LP Tokens and Fee Accrual

When a user deposits into a pool they receive an LP token representing their share. Trading fees — typically 0.01% (stable pairs) to 1% (exotic pairs) — accrue inside the pool, so burning the LP token redeems a proportionally larger amount of the underlying assets over time. Many pools also route additional incentives (CRV, BAL, ARB, OP) to LPs who stake their LP tokens in a gauge.

## Impermanent Loss

The core risk: if one asset in the pair appreciates relative to the other, an LP ends up holding less of the winning asset and more of the losing one than a simple buy-and-hold. This is called [[impermanent-loss]] — impermanent only if prices return to the entry ratio. Volatile pairs (ETH/USDC) carry high IL risk; correlated pairs (stETH/ETH, USDC/USDT) carry very low IL risk, which is why stable pools are the bedrock of conservative DeFi yield strategies.

## Major Venues

[[uniswap|Uniswap]] dominates volatile-pair volume across Ethereum and L2s. [[curve-dao-token|Curve]] dominates stablecoin and LST liquidity. Balancer supports weighted and boosted pools. Trader Joe (Avalanche) and Aerodrome (Base) are significant ecosystem-specific venues.

## Trading Relevance

For a trader, AMM liquidity provision is a **yield strategy with an embedded short-gamma payoff**. The fee income behaves like collecting option premium, while [[impermanent-loss]] behaves like being short a straddle: the LP loses, relative to holding, precisely when one asset moves sharply. The practical decision is whether expected fees plus incentive emissions exceed expected IL plus gas and smart-contract risk. Key levers a trader controls:

- **Pair selection.** Correlated/stable pairs (USDC/USDT, stETH/ETH) minimize IL and suit low-risk yield; volatile pairs maximize fees but require a directional or vol view to be net-positive.
- **Range selection in concentrated liquidity.** A tight range multiplies fee capture but converts the position into an active management problem — once price exits the range the LP holds 100% of the worse asset and earns nothing until rebalanced. This is effectively running a [[market-maker]] book that must be re-quoted.
- **Incentive durability.** Emission-driven APYs ("liquidity mining") often collapse once token rewards taper; a trader must distinguish sustainable fee yield from temporary subsidy.

Crucially, AMM LPs face **uninformed-vs-informed flow** the same way an order-book [[liquidity-provider]] does: arbitrageurs are the *informed* flow that rebalances the pool to the true price, and the value they extract (loss-versus-rebalancing, LVR) is the on-chain analog of [[adverse-selection]].

## Related

- [[decentralized-exchanges]]
- [[liquidity-provider]] — the traditional-markets (order-book) counterpart
- [[impermanent-loss]]
- [[concentrated-liquidity]]
- [[automated-market-maker]]
- [[market-maker]]

## Sources

- Adams, Hayden, et al. *Uniswap v2 Core* (2020) and *Uniswap v3 Core* (2021) whitepapers — constant-product and concentrated-liquidity AMM designs.
- Egorov, Michael. *StableSwap — Efficient Mechanism for Stablecoin Liquidity* (Curve Finance, 2019) — the stable-swap invariant.
- Milionis, Jason, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang. "Automated Market Making and Loss-Versus-Rebalancing" (2022) — formalizes the LVR cost that arbitrageurs extract from LPs.
- Balancer. *Balancer Whitepaper* (2019) — weighted-pool mechanics.
