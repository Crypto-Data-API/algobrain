---
title: "Impermanent Loss"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [defi, crypto, liquidity, risk-management]
aliases: ["Impermanent Loss", "IL", "Divergence Loss"]
related: ["[[liquidity-pools]]", "[[uniswap]]", "[[defi]]", "[[automated-market-maker]]", "[[yield-farming]]", "[[hodl]]", "[[staking]]"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[automated-market-maker]]", "[[liquidity-pools]]"]
difficulty: intermediate
---

Impermanent loss (also called divergence loss) is the reduction in value that [[liquidity-pools|liquidity providers]] (LPs) experience when the price ratio of the assets in an [[automated-market-maker]] (AMM) pool changes relative to when they deposited. It is called "impermanent" because the loss only crystallises if the LP withdraws at the changed price ratio -- if prices return to the original ratio, the loss disappears. In practice, however, prices rarely revert exactly, making impermanent loss a persistent cost of providing liquidity on platforms like [[uniswap|Uniswap]], SushiSwap, and Curve.


## How It Occurs

In a standard constant-product AMM (the x * y = k model used by Uniswap V2), the pool must always maintain the invariant that the product of the two token reserves equals a constant. When the external market price of one token rises, arbitrageurs buy the appreciating token from the pool (where it is momentarily cheap) and sell the depreciating token into the pool, rebalancing the reserves until the pool price matches the market price. This process systematically removes the appreciating asset from the pool and adds the depreciating asset.

As a result, the LP ends up holding more of the token that dropped in relative value and less of the token that increased. Compared to simply holding the original token amounts in a wallet (the "[[hodl|HODL]]" benchmark), the LP's portfolio is worse off by the impermanent loss amount.

## The Formula

For a 50/50 constant-product pool, impermanent loss depends solely on the price ratio change. If the price of one asset changes by a factor of *r* relative to the other:

**IL = 2 * sqrt(r) / (1 + r) - 1**

Some concrete examples:

| Price Change (r) | Impermanent Loss |
|---|---|
| 1.25x (25% increase) | -0.6% |
| 1.50x (50% increase) | -2.0% |
| 2.00x (100% increase) | -5.7% |
| 3.00x (200% increase) | -13.4% |
| 5.00x (400% increase) | -25.5% |
| 0.50x (50% decrease) | -5.7% |

The loss is symmetric: a 2x increase and a 0.5x decrease both produce a 5.7% impermanent loss. Note that these percentages represent the shortfall versus holding, not an absolute loss -- the LP position may still be profitable in dollar terms if both assets appreciated.

## When It Becomes Permanent

Impermanent loss becomes a realised, permanent loss in several scenarios:

- **The LP withdraws** at a price ratio different from their entry. This is the most common case.
- **One token goes to zero** (a rug pull or project failure). The LP is left holding nearly 100% of the worthless token due to the AMM rebalancing mechanism.
- **Permanent regime change**: If ETH was $2,000 when the LP entered an ETH/USDC pool and is now $4,000 with no expectation of reverting, the ~5.7% impermanent loss is effectively permanent.

LPs are compensated for impermanent loss through trading fees earned by the pool. The key question for any LP is whether the fee income exceeds the impermanent loss. In high-volume pools (e.g., ETH/USDC on Uniswap with daily volume exceeding $100M), fees often compensate for IL. In low-volume or exotic token pools, they frequently do not.

## Mitigation Strategies

- **Stablecoin pools**: Pools of correlated assets (e.g., USDC/USDT, stETH/ETH) have minimal price divergence and therefore minimal impermanent loss. Curve Finance specialised in these pools for this reason.
- **Concentrated liquidity**: Uniswap V3 introduced concentrated liquidity, allowing LPs to provide liquidity within a specific price range. This increases fee income per dollar of capital but amplifies impermanent loss if price moves outside the range, requiring active management.
- **Single-sided liquidity**: Some protocols (Bancor V3, Thorchain) offered single-sided LP deposits with impermanent loss protection, funded by protocol-level insurance or token inflation. Results have been mixed -- Bancor paused its IL protection program in 2022 due to unsustainability.
- **Hedging**: Sophisticated LPs use [[options]] or [[perpetual-futures]] to delta-hedge their AMM position, reducing directional exposure. This converts the LP position into something closer to a pure fee-collection strategy, though hedging costs eat into returns.

## Trading Relevance

Impermanent loss reframes liquidity provision as a short-volatility, short-gamma position: an LP is effectively selling a strip of options to the pool, collecting fees as premium and paying out via IL when prices move. This makes LP yield directly comparable to an option-writing strategy, and it means LPs should demand higher fee APRs precisely when realised volatility is high. Quantitatively-minded LPs estimate breakeven by comparing the pool's annualised fee yield against expected IL given the pair's [[volatility]]; if implied/realised vol on the pair exceeds the level at which fees cover divergence loss, the position has negative expected value versus simply holding. Delta-hedging the LP exposure with [[perpetual-futures]] is the DeFi analogue of a market maker delta-hedging an option book.

## Related

- [[liquidity-pools]] -- the mechanism in which impermanent loss occurs
- [[uniswap]] -- the largest AMM and where most IL discussion originates
- [[defi]] -- the broader ecosystem context
- [[automated-market-maker]] -- the mathematical model underlying IL
- [[yield-farming]] -- the practice of providing LP capital for yield, where IL is the primary risk
- [[hodl]] -- the buy-and-hold benchmark IL is measured against

## Sources

- Pintail, "Uniswap: A Good Deal for Liquidity Providers?" (2019) -- the original derivation of the constant-product IL formula.
- Uniswap V2 and V3 whitepapers (Adams et al., 2020-2021).
- Bancor, "Impermanent Loss Protection" documentation and 2022 program-pause announcement.
- General DeFi / AMM literature.
