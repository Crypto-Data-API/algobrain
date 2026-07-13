---
title: "Concentrated Liquidity"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, defi, uniswap, liquidity, concentrated-liquidity, impermanent-loss, amm, lp-management, rebalancing]
aliases: ["Concentrated Liquidity Management", "Active LP Management", "Uniswap V3 LP Strategy"]
strategy_type: algorithmic
timeframe: swing|position
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[jit-liquidity]]", "[[defi-yield-farming]]", "[[impermanent-loss]]", "[[uniswap]]", "[[automated-market-maker]]"]
---

# Concentrated Liquidity

## Overview

Concentrated liquidity, introduced by [[uniswap]] V3 and expanded in V4, allows liquidity providers to allocate capital within a specific price range rather than across the entire price curve. This dramatically improves capital efficiency -- a position concentrated within a narrow range can earn the same fees as a full-range position with 100-4000x less capital. However, this efficiency comes with active management requirements: if the market price moves outside your chosen range, your position earns zero fees and suffers maximum [[impermanent-loss]]. Successful concentrated liquidity management is essentially a volatility and range prediction strategy.

## How It Works

1. **Select a pool and fee tier:** Choose a token pair and fee tier (e.g., ETH/USDC 0.30%). Higher fee tiers suit more volatile pairs; lower tiers suit stablecoin pairs.
2. **Set price range:** Define the lower and upper tick boundaries. Wider ranges earn fees more consistently but with lower capital efficiency. Narrower ranges earn higher fees per dollar deployed but go out of range more often.
3. **Deposit liquidity:** Provide both tokens in the ratio dictated by your range and the current price. If the current price is near one edge of your range, the deposit will be heavily weighted toward one token.
4. **Monitor and rebalance:** When the market price approaches or exits your range, rebalance by withdrawing, adjusting the range, and redepositing. Automated vaults (Arrakis, Gamma, Bunni) can handle this.
5. **Harvest fees:** Accrued trading fees are collected manually or auto-compounded by vault protocols.

## Example

An LP provides $100,000 to the ETH/USDC pool on Uniswap V3 with a range of $2,800-$3,400 (current price: $3,100). This is roughly a +/- 10% range. Capital efficiency is approximately 10x compared to a full-range position. Weekly fees earned: ~$300 (annualized ~15% APY). After 3 weeks, ETH rises to $3,350, approaching the upper bound. The LP rebalances: withdraws, sets a new range of $3,100-$3,700, and redeposits. The rebalance costs ~$20 in gas. If the LP had not rebalanced and price exceeded $3,400, the entire position would have converted to USDC, earning zero fees.

## Advantages

- **Superior capital efficiency** -- earn the same fees with a fraction of the capital required by full-range positions
- **Customizable risk/reward** -- choose ranges that match your volatility outlook and risk tolerance
- **Composable** -- LP tokens (NFT positions) can be used in other DeFi protocols as collateral or yield stacking
- **Automated vault options** -- protocols like Arrakis and Gamma reduce active management burden

## Disadvantages

- **Active management required** -- passive "set and forget" leads to out-of-range positions earning nothing
- **Amplified [[impermanent-loss]]** -- concentrated positions suffer IL faster and more severely when prices move out of range
- **Rebalancing costs** -- frequent range adjustments incur gas fees and realize losses from IL at each rebalance
- **Complexity** -- requires understanding of tick math, fee tiers, and range optimization; not beginner-friendly
- **MEV exposure** -- rebalance transactions can be sandwiched by [[mev-strategies|MEV searchers]], increasing costs

## See Also

- [[jit-liquidity]] -- an extreme form of concentrated liquidity used for single-block MEV extraction
- [[impermanent-loss]] -- the primary risk of LP positions, amplified by concentration
- [[defi-yield-farming]] -- broader DeFi yield strategies that include LP management
- [[uniswap]] -- the protocol that pioneered concentrated liquidity
- [[automated-market-maker]] -- the underlying mechanism for DEX liquidity provision
