---
title: "Automated Market Maker"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [defi, market-microstructure, crypto]
aliases: ["AMM", "Automated Market Makers"]
related: ["[[uniswap]]", "[[impermanent-loss]]", "[[defi]]", "[[market-making-strategy]]"]
domain: [defi, market-microstructure]
difficulty: intermediate
---

An automated market maker (AMM) is a decentralized exchange (DEX) mechanism that uses [[smart-contracts|smart contracts]] and mathematical pricing formulas to facilitate token swaps, replacing the traditional [[order-book|order book]] model with liquidity pools funded by depositors. [[uniswap|Uniswap]] pioneered the dominant AMM design, and AMMs now handle the majority of on-chain trading volume in [[defi|DeFi]].

## Overview

In traditional finance and centralized crypto exchanges, trading relies on order books: buyers and sellers post limit orders, and a matching engine pairs them. This model requires active market makers who continuously quote bid/ask prices. AMMs eliminate this requirement by using a deterministic pricing function that automatically sets prices based on the ratio of assets in a liquidity pool.

Anyone can become a liquidity provider (LP) by depositing paired tokens into a pool and earning a share of trading fees proportional to their contribution. This permissionless, automated approach democratized market making but introduced new risks, most notably [[impermanent-loss]].

## How AMMs Work

### Constant Product Formula (x * y = k)

The most common AMM model, used by Uniswap V2 and SushiSwap:

- A pool contains two tokens: Token A (quantity `x`) and Token B (quantity `y`)
- The invariant **x * y = k** must hold before and after every trade
- When a trader buys Token A, they add Token B to the pool and remove Token A. The formula automatically adjusts the price

**Example**: A pool holds 10 ETH and 10,000 USDC (k = 100,000). A trader wants to buy 1 ETH.
- After the trade: 9 ETH remain, so USDC needed = 100,000 / 9 = 11,111 USDC
- Trader pays 1,111 USDC for 1 ETH (effective price: $1,111 vs. the initial $1,000 spot)
- This price impact is called **slippage** and increases with trade size relative to pool depth

### Other AMM Formulas

| Model | Formula | Used By | Best For |
|-------|---------|---------|----------|
| **Constant Product** | x * y = k | Uniswap V2, SushiSwap | General-purpose token pairs |
| **StableSwap** | Hybrid constant product + constant sum | Curve Finance | Stablecoin-stablecoin pairs (low slippage near peg) |
| **Concentrated Liquidity** | Position-based ranges | Uniswap V3 | Capital-efficient LP positions in defined price ranges |
| **Weighted** | x^w1 * y^w2 = k | Balancer | Unequal-weight pools (e.g., 80/20) |
| **Virtual AMM** | Synthetic constant product | Perpetual Protocol | Perpetual futures without physical liquidity |

## Key Concepts

### Liquidity Pools

A liquidity pool is a smart contract holding reserves of two (or more) tokens. LPs deposit tokens in the correct ratio and receive LP tokens representing their share of the pool. When they withdraw, they receive their proportional share of the pool's current balances (which may differ from their deposit due to [[impermanent-loss|impermanent loss]] and accumulated fees).

### Trading Fees

AMMs charge fees on each swap, typically:
- **Uniswap V2**: 0.30% flat
- **Uniswap V3**: 0.01%, 0.05%, 0.30%, or 1.00% (selected per pool)
- **Curve**: 0.04% (optimized for stablecoin efficiency)
- **PancakeSwap**: 0.25%

Fees are distributed pro-rata to LPs. In high-volume pools, fee income can significantly offset [[impermanent-loss]].

### Price Oracle Function

AMMs inherently produce price data because the token ratio defines the price. Uniswap V2 introduced time-weighted average price (TWAP) oracles that other DeFi protocols use for on-chain price feeds, though dedicated oracle networks like [[chainlink|Chainlink]] are preferred for security-critical applications.

### Arbitrage and Price Discovery

AMM prices are kept in line with the broader market through arbitrage. When the AMM price diverges from centralized exchanges, arbitrageurs trade against the pool to capture the difference, pushing the price back toward the market rate. This process:

- Ensures AMM prices track global market prices
- Generates trading volume (and fee income for LPs)
- Is also the mechanism that causes [[impermanent-loss]]

## AMMs vs. Order Books

| Feature | AMM | Order Book |
|---------|-----|------------|
| Liquidity source | Passive LPs depositing into pools | Active market makers quoting bid/ask |
| Price determination | Mathematical formula | Supply/demand of limit orders |
| Capital efficiency | Lower (liquidity spread across all prices, except V3) | Higher (concentrated at current price) |
| Permissionless | Yes -- anyone can LP | Usually requires market maker agreements |
| Slippage | Predictable, formula-based | Variable, depends on book depth |
| Best for | Long-tail tokens, DeFi composability | High-volume, tight-spread markets |
| MEV vulnerability | High (sandwich attacks, front-running) | Lower on centralized platforms |

## Major AMM Protocols

- **[[uniswap|Uniswap]]**: Largest DEX by volume. V3 introduced concentrated liquidity (2021). Deployed on Ethereum, Polygon, Arbitrum, Optimism, Base, and others.
- **Curve Finance**: Optimized for stablecoin and like-kind asset swaps with extremely low slippage. Also uses the CRV governance token and "gauge" system for directing liquidity incentives.
- **Balancer**: Supports multi-token pools with custom weightings (e.g., 80% ETH / 20% DAI).
- **SushiSwap**: Uniswap V2 fork with additional features (lending, launchpad).
- **PancakeSwap**: Largest AMM on BNB Chain.

## Risks

- **[[impermanent-loss]]**: The primary cost of providing liquidity, caused by price divergence
- **Smart contract risk**: Bugs or exploits in the AMM contract can drain pools
- **MEV (Maximal Extractable Value)**: Sandwich attacks and front-running by bots that extract value from LP pools
- **Rug pulls**: Malicious token creators can drain liquidity from pools of worthless tokens
- **Oracle manipulation**: Using AMM price feeds as oracles can enable flash loan attacks

## Related

- [[uniswap]]
- [[impermanent-loss]]
- [[defi]]
- [[market-making-strategy]]
- [[liquidity-pools]]
- [[order-book]]
- [[stablecoins]]

## Sources

- General DeFi knowledge; no specific wiki source ingested yet.
