---
title: "Impermanent Loss"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [defi, liquidity, risk-management, crypto]
aliases: ["IL", "Divergence Loss"]
related: ["[[uniswap]]", "[[automated-market-maker]]", "[[defi]]", "[[liquidity-pools]]"]
domain: [defi, risk-management]
difficulty: intermediate
---

Impermanent loss (IL) is the reduction in value that occurs when providing liquidity to an [[automated-market-maker|automated market maker (AMM)]] compared to simply holding the tokens in a wallet. It is caused by price divergence between the two paired assets in a liquidity pool and is called "impermanent" because the loss reverses if prices return to their original ratio -- though in practice, this often does not happen.

## Overview

When a liquidity provider (LP) deposits two tokens into an AMM pool (e.g., ETH/USDC on [[uniswap|Uniswap]]), the AMM algorithm continuously rebalances the LP's position as prices change. This rebalancing means the LP ends up holding more of the depreciating token and less of the appreciating token relative to a simple buy-and-hold strategy. The difference between the LP position value and the hold value is impermanent loss.

IL is the fundamental cost of providing liquidity in [[defi|DeFi]]. LPs accept this cost in exchange for earning trading fees from swaps that occur in the pool. Profitability depends on whether accumulated fees exceed the impermanent loss.

## How It Works

### The Constant Product Formula

Most AMMs (Uniswap V2, SushiSwap) use the constant product formula:

**x * y = k**

Where:
- `x` = quantity of Token A in the pool
- `y` = quantity of Token B in the pool
- `k` = a constant that must be maintained

When the price of Token A increases relative to Token B, arbitrageurs buy the now-underpriced Token A from the pool and sell Token B into it. This restores the pool price to the market price but changes the LP's token ratio.

### Numerical Example

1. LP deposits 1 ETH ($1,000) + 1,000 USDC into an ETH/USDC pool. Total value: $2,000.
2. ETH price doubles to $2,000.
3. **If held (no LP)**: 1 ETH ($2,000) + 1,000 USDC = $3,000.
4. **As LP**: The pool rebalances. The LP now holds ~0.707 ETH ($1,414) + ~1,414 USDC = $2,828.
5. **Impermanent loss**: $3,000 - $2,828 = $172 (5.7% of the hold value).

### IL by Price Change

| Price Change | Impermanent Loss |
|-------------|-----------------|
| 1.25x (25% move) | 0.6% |
| 1.50x (50% move) | 2.0% |
| 2x (100% move) | 5.7% |
| 3x (200% move) | 13.4% |
| 5x (400% move) | 25.5% |
| 10x (900% move) | 42.5% |

Key insight: IL is symmetric -- a 2x increase and a 50% decrease both cause the same 5.7% IL. The loss depends on the magnitude of divergence, not the direction.

## When IL Becomes Permanent

"Impermanent" is somewhat misleading. The loss becomes permanent (realized) when:

- The LP withdraws liquidity at a different price ratio than when they deposited
- One token in the pair goes to zero (common with low-cap altcoins)
- The LP is forced to exit due to margin/collateral requirements

In volatile [[crypto|crypto]] markets, prices rarely return to their original ratio, making the loss effectively permanent in many cases.

## Mitigating Impermanent Loss

### Pool Selection

- **Stablecoin pairs** (USDC/USDT, DAI/USDC): Minimal IL because prices stay tightly correlated
- **Correlated pairs** (stETH/ETH, WBTC/BTC): Low IL because assets track each other
- **Volatile pairs** (SHIB/ETH, new token/ETH): High IL risk, requiring very high fee income to compensate

### Protocol Innovations

- **Concentrated liquidity** ([[uniswap]] V3): LPs choose a price range, earning more fees per dollar deployed but facing amplified IL if price moves outside the range
- **Curve Finance**: Optimized AMM formula (StableSwap) designed specifically for low-IL stablecoin trading
- **Balancer**: Weighted pools (e.g., 80/20 instead of 50/50) that reduce IL on the overweight asset
- **IL protection programs**: Some protocols (Bancor V3, previously) offered insurance against IL, though these have been largely discontinued due to unsustainability

## IL vs. Trading Fees

The decision to provide liquidity is fundamentally a bet that:

**Trading fees earned > Impermanent loss incurred**

Factors that increase fee income:
- High trading volume relative to pool depth
- Higher fee tiers (Uniswap V3 offers 0.01%, 0.05%, 0.30%, 1.00% tiers)
- Concentrated liquidity in an active price range

Factors that increase IL:
- High [[volatility|volatility]] of the paired assets
- Large price divergence from the entry ratio
- Long duration of the LP position during trending markets

## Related

- [[automated-market-maker]]
- [[uniswap]]
- [[defi]]
- [[liquidity-pools]]
- [[yield-farming]]
- [[staking]]

## Sources

- General DeFi knowledge; no specific wiki source ingested yet.
