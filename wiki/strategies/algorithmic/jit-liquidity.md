---
title: "JIT Liquidity"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, defi, liquidity, uniswap, mev, concentrated-liquidity, amm, just-in-time, ethereum]
aliases: ["Just-In-Time Liquidity", "JIT LP", "JIT Liquidity Provision"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[concentrated-liquidity]]", "[[mev-strategies]]", "[[defi-yield-farming]]", "[[uniswap]]", "[[impermanent-loss]]"]
---

# JIT Liquidity

## Overview

Just-In-Time (JIT) liquidity is an [[mev-strategies|MEV-adjacent]] strategy where a liquidity provider adds a tightly concentrated liquidity position on [[uniswap]] V3 (or similar AMMs) in the same block as a large pending swap, captures the trading fees from that swap, and removes the liquidity immediately after. By concentrating capital into an extremely narrow price range around the swap price, the JIT provider earns a disproportionate share of fees relative to passive LPs -- often capturing 80-95% of the fee on that single trade. The strategy requires monitoring the [[mempool]] for large pending swaps and submitting atomic transaction bundles via [[flashbots]] or similar block builder infrastructure.

## How It Works

1. **Detect large pending swap:** Monitor the mempool for significant swap transactions on Uniswap V3/V4 pools (e.g., a $500K ETH/USDC swap).
2. **Calculate optimal range:** Determine the tightest possible tick range around the execution price that will capture the swap. Narrower ranges earn more fees per unit of capital.
3. **Bundle three transactions atomically:** (a) Mint a concentrated LP position at the target tick range, (b) the victim's swap executes against your liquidity, (c) burn and withdraw the LP position.
4. **Submit via block builder:** Send the bundle through [[flashbots]] or a block builder to ensure atomic execution within a single block. If any transaction fails, the entire bundle reverts.
5. **Collect profit:** The fee earned from the large swap minus gas costs and any minor [[impermanent-loss]] from the price movement within the tick range.

## Example

A trader submits a $200,000 USDC-to-ETH swap on Uniswap V3 (0.30% fee tier). The JIT provider detects this in the mempool, mints a $1M concentrated position spanning just 2 ticks around the execution price, and the swap routes primarily through this liquidity. Fee earned: $200,000 x 0.30% = $600. The JIT provider's share (due to concentration): ~$500. After gas and builder tip (~$50), net profit is approximately **$450 in a single block**. The entire operation takes 12 seconds and the capital is exposed to [[impermanent-loss]] for only that one transaction.

## Advantages

- **Extremely capital efficient** -- concentrated ranges mean high fee capture relative to capital deployed
- **Minimal impermanent loss** -- liquidity is only active for a single block, so price exposure is negligible
- **Atomic execution** -- bundles revert entirely on failure, eliminating partial-fill risk
- **No directional exposure** -- the strategy is market-neutral, profiting purely from fees

## Disadvantages

- **Highly competitive** -- a small number of sophisticated teams dominate JIT provision, compressing margins
- **Harms passive LPs** -- JIT providers siphon fees that would otherwise go to long-term liquidity providers, creating controversy
- **Requires specialized infrastructure** -- mempool monitoring, bundle construction, and block builder relationships are non-trivial
- **Ethereum-centric** -- most viable on Ethereum mainnet; less applicable on chains with different mempool dynamics
- **Regulatory ambiguity** -- as an MEV-adjacent strategy, the legal classification remains unclear

## See Also

- [[concentrated-liquidity]] -- the underlying LP mechanism that enables JIT strategies
- [[mev-strategies]] -- the broader category of block-level value extraction
- [[flashbots]] -- the relay infrastructure used to submit JIT bundles
- [[defi-yield-farming]] -- passive yield strategies that JIT liquidity competes against
- [[uniswap]] -- the primary venue for JIT liquidity provision
