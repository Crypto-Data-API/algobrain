---
title: "Flash Loan Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [arbitrage, defi, flash-loan, aave, dex, mev, atomic, zero-capital, ethereum]
aliases: ["Flash Loan Arb", "Atomic Arbitrage", "DeFi Flash Arb"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[mev-strategies]]", "[[decentralized-exchanges]]", "[[aave]]", "[[cross-exchange-arbitrage]]", "[[triangular-arbitrage]]"]
---

# Flash Loan Arbitrage

## Overview

Flash loan arbitrage is a DeFi-native strategy that uses uncollateralized loans to exploit price discrepancies across [[decentralized-exchanges]]. The key innovation is that the borrow, arbitrage, and repayment all occur within a single atomic transaction on the blockchain. If the transaction is not profitable (i.e., the loan cannot be repaid), the entire transaction reverts as if it never happened. This means the trader risks zero capital -- only the gas fee for a failed transaction.

Flash loans are available through protocols like [[aave]] (0.09% fee), dYdX (historically zero fee), and Balancer (variable fee). Over $1 million in arbitrage profit is extracted daily across DeFi ecosystems, making this one of the most active arb markets in crypto. The strategy is deeply intertwined with [[mev-strategies]] (Maximal Extractable Value), as sophisticated searchers compete to identify and execute profitable flash loan routes, often bribing block validators for priority transaction ordering.

## How It Works

A flash loan arbitrage transaction is a single smart contract call that performs multiple steps atomically:

1. **Borrow** a large amount of capital from a flash loan provider (e.g., 1,000 ETH from [[aave]]).
2. **Swap** the borrowed asset on DEX A where it is relatively cheaper (e.g., [[uniswap]]).
3. **Swap** the received asset on DEX B where it is relatively more expensive (e.g., SushiSwap).
4. **Repay** the flash loan plus the fee (0.09% for Aave).
5. **Keep** the remaining profit.

Multi-hop routing enables complex paths: borrow USDC, swap to WETH on Uniswap V3, swap to DAI on Curve, swap back to USDC on Balancer, repay loan. Each hop exploits a small inefficiency, and the cumulative profit exceeds the loan fee and gas costs. All of this executes in a single block (~12 seconds on Ethereum).

## Entry/Exit Rules

### Entry
1. **Monitor DEX prices:** Continuously scan price feeds from [[uniswap]], SushiSwap, Curve, Balancer, and other DEXs for the same token pairs.
2. **Calculate profitability:** Identify paths where buying on one DEX and selling on another yields more than the flash loan fee + gas cost.
3. **Simulate the transaction:** Use tools like Tenderly or local EVM forks to simulate the full transaction and confirm net profitability before submitting.
4. **Submit with optimal gas:** Use Flashbots or MEV-Share to submit the transaction privately, avoiding front-running by other bots.

### Exit
1. **Atomic completion:** There is no exit management. The trade either completes profitably in a single transaction or reverts entirely.
2. **No holding period:** Capital is borrowed and returned within the same block. No positions are held.

## Example Trade

**Opportunity:** ETH is priced at $3,400 on SushiSwap but $3,412 on Uniswap V3 (0.35% spread).

1. **Borrow 1,000 ETH** from [[aave]] flash loan.
2. **Buy 1,000 ETH** on SushiSwap at $3,400 each = $3,400,000 cost.
3. **Sell 1,000 ETH** on Uniswap V3 at $3,412 each = $3,412,000 proceeds.
4. **Gross profit:** $12,000.
5. **Flash loan fee (0.09%):** 0.9 ETH = ~$3,060.
6. **Gas cost:** ~$150 (complex multi-call transaction).
7. **Net profit:** $12,000 - $3,060 - $150 = **$8,790** in a single transaction, with zero capital at risk.
8. **Duration:** One block (~12 seconds).

## Risk Management

- **Zero capital risk:** If the arb is not profitable after fees, the transaction reverts. The only loss is the gas fee for the failed transaction (~$5-50).
- **Gas price spikes:** During network congestion, gas costs can exceed the arb profit. Always simulate with current gas prices.
- **Sandwich attacks:** Other [[mev-strategies|MEV bots]] may front-run your transaction, moving the price before your swap executes. Use private mempools (Flashbots).
- **Smart contract risk:** Bugs in the arbitrage contract can lead to fund loss. Thoroughly audit all custom contract code.
- **[[slippage]] on large trades:** The simulated profit assumes specific pool reserves. If another trade hits the pool before yours, the prices change.
- **Protocol risk:** Flash loan providers could be exploited or paused, blocking execution.

## Advantages
- **Zero capital required** -- borrow any amount, from 1 ETH to 100,000 ETH, without collateral
- **Zero directional risk** -- the trade either profits or does not execute at all
- **Atomic execution** -- no leg risk, no partial fills, no holding period
- **Permissionless** -- anyone can write and deploy a flash loan arbitrage contract
- **Composable** -- can chain multiple DeFi protocols in a single transaction for complex multi-hop routes

## Disadvantages
- **Extreme competition** -- thousands of bots scan for the same opportunities; only the fastest or best-connected wins
- **MEV extraction** -- validators and block builders can steal profitable transactions by reordering or copying them
- **Requires Solidity expertise** -- must write and deploy custom smart contracts
- **Gas costs for failures** -- failed transactions still cost gas; high failure rates erode returns
- **Shrinking margins** -- as more searchers enter, profitable opportunities become rarer and smaller
- **Chain-specific** -- each blockchain (Ethereum, Arbitrum, BSC) requires separate infrastructure and contracts

## Real-World Examples
- **bZx attack (2020):** A flash loan was used to manipulate oracle prices across multiple DeFi protocols, extracting ~$350K in a single transaction. While exploitative, it demonstrated the power of atomic composability.
- **Daily MEV extraction:** Flashbots data shows consistent flash loan arbitrage profits across [[uniswap]], SushiSwap, and Curve pools, totaling millions per week.
- **Multi-hop routes:** Sophisticated bots route through 5-7 pools in a single transaction, finding profit paths that are invisible to simple two-pool scanners.

## See Also
- [[mev-strategies]] -- the broader category of on-chain value extraction that includes flash loan arb
- [[cross-chain-arbitrage]] -- cross-blockchain arb; flash loans can fund the single-chain leg of a cross-chain strategy
- [[decentralized-exchanges]] -- the venues where flash loan arb occurs
- [[aave]] -- the most popular flash loan provider
- [[triangular-arbitrage]] -- a related multi-hop arbitrage approach
- [[cross-exchange-arbitrage]] -- the centralized exchange equivalent
