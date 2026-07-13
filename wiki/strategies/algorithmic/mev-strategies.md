---
title: "MEV Strategies"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, mev, defi, front-running, sandwich-attack, flashbots, mempool, blockchain, ethereum, arbitrage]
aliases: ["Maximal Extractable Value", "Miner Extractable Value", "MEV Extraction", "Searcher Strategies"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[cross-exchange-arbitrage]]", "[[defi-yield-farming]]", "[[triangular-arbitrage]]", "[[ethereum]]", "[[uniswap]]", "[[flashbots]]", "[[ai-mev]]", "[[ai-trading-agents]]", "[[reinforcement-learning-trading]]", "[[ai-solvers]]", "[[intent-based-trading]]"]
---

# MEV Strategies

## Overview

Maximal Extractable Value (MEV) refers to the profit that can be extracted by reordering, inserting, or censoring transactions within a blockchain block. Originally called "Miner Extractable Value" (when miners controlled block production on proof-of-work [[ethereum]]), the concept was renamed after [[the-merge]] to reflect that validators now have this power. In practice, specialized actors called **searchers** identify profitable transaction orderings and submit them through relays like [[flashbots]] to block builders, who assemble the most profitable blocks.

MEV strategies include **front-running** (placing a transaction before a large trade to profit from the price impact), **back-running** (transacting immediately after a large trade to capture the price reversion), **sandwich attacks** (surrounding a victim transaction with a buy-before and sell-after to extract value), and **DEX arbitrage** (correcting price discrepancies across [[uniswap]], [[sushiswap]], [[curve]], and other AMMs). MEV is controversial -- it effectively taxes DeFi users -- but it is a multi-billion dollar industry that plays a structural role in blockchain economics.

The searcher layer is increasingly an arena for machine-learning — mempool classification, bid shading in priority auctions, and [[reinforcement-learning-trading|reinforcement-learning]] strategy selection all have a natural fit here. See [[ai-mev]] for the ML-specific angle on top of the strategy taxonomy below, and [[ai-trading-agents]] for the broader autonomous-agent context.

## Rules

### Entry (DEX Arbitrage -- Most Common MEV)
1. **Monitor AMM prices:** Track token prices across multiple DEX pools ([[uniswap]] V2/V3, [[sushiswap]], [[curve]], [[balancer]]). When Pool A prices diverge from Pool B, an arb exists.
2. **Calculate optimal trade size:** Use the constant-product formula (x * y = k) or concentrated liquidity math to determine the exact trade size that maximizes profit.
3. **Submit via [[flashbots]]:** Use Flashbots Protect or MEV-Share to submit the transaction bundle. This avoids the public [[mempool]] and prevents other searchers from front-running your arb.
4. **Atomic execution:** Use smart contract bundles that execute all legs in a single transaction. If any leg fails, the entire transaction reverts -- no partial fills, no leg risk.

### Entry (Sandwich Attack -- Controversial)
1. **Monitor the [[mempool]]** for large pending DEX swaps (e.g., a $100K USDC -> ETH swap on Uniswap).
2. **Front-run:** Submit a buy transaction for the same token with higher gas, executed before the victim's swap.
3. **Victim transaction executes:** The large swap pushes the price up further.
4. **Back-run:** Immediately sell the token after the victim's swap at the now-higher price.
5. **Profit:** The difference between your buy and sell prices, minus gas costs.

### Exit
1. **Atomic:** All MEV strategies are executed atomically within a single block. There is no "exit" -- the trade either completes profitably or reverts entirely.
2. **Gas optimization:** Failed transactions still cost gas on some chains. Optimize to minimize wasted gas on failed attempts.
3. **Profit extraction:** Profits are typically held in ETH or stablecoins in the searcher's contract, then periodically withdrawn.

### Position Sizing
Capital requirements vary. DEX arbs can be executed with [[flash-loans]] (borrow, arb, repay in a single transaction -- zero capital required). Sandwich attacks require upfront capital for the front-run purchase. Typical searchers deploy $50K-$500K in working capital.

## Indicators Used
- [[mempool]] monitoring -- watching pending transactions for profitable opportunities
- DEX pool reserves -- on-chain state of AMM pools determines current prices and available liquidity
- Gas price / priority fee -- determines the cost of inclusion and competitive bidding against other searchers
- [[flashbots]] bundle simulation -- pre-execution simulation to verify profitability before submitting
- Block builder APIs -- integration with block builders (Flashbots, BloXroute, Ultra Sound) for transaction inclusion
- Cross-DEX price feeds -- real-time price comparison across all relevant AMMs

## Example Trade
**Type:** DEX Arbitrage (the "clean" MEV strategy)
1. **Detection:** WETH/USDC price on Uniswap V3: $3,200. WETH/USDC price on SushiSwap: $3,188. Discrepancy: $12 (0.38%).
2. **Optimal size:** Calculate that buying 15 ETH on SushiSwap and selling on Uniswap maximizes profit given pool depths.
3. **Construct bundle:** Write a smart contract that: (a) takes a [[flash-loan]] for 15 ETH worth of USDC from Aave, (b) buys 15 ETH on SushiSwap at $3,188, (c) sells 15 ETH on Uniswap at $3,200, (d) repays the flash loan + fee.
4. **Submit via Flashbots:** Bundle is submitted with a priority fee bid. Block builder includes it if profitable.
5. **Result:** Gross profit: 15 x $12 = $180. Flash loan fee: ~$2. Gas + priority fee: ~$30. **Net profit: ~$148** in a single block (~12 seconds).
6. **Capital used:** $0 (flash loan funded). This is the appeal of on-chain MEV.

## Performance Characteristics
- **Win Rate:** Varies wildly. Top searchers achieve 60-80% inclusion rates. Failed bundles are common due to competition.
- **Profit Factor:** 5.0-50.0 on successful extractions (costs are low relative to profits on winning trades).
- **Best Market Conditions:** High [[volatility]], large DEX trading volume, new token launches, significant mempool activity.
- **Worst Market Conditions:** Low DeFi activity, highly competitive environments where profits are bid away to block builders.
- **Market Size:** MEV extraction on Ethereum alone totals hundreds of millions of dollars annually.

## Advantages
- **Zero-capital execution:** [[flash-loans]] enable arbitrage with no upfront capital for DEX arb strategies
- **Atomic risk management:** Transactions either succeed profitably or revert entirely -- no partial losses
- **Enormous profit potential:** Top MEV searchers earn millions annually
- **Structural edge:** Deep technical knowledge of blockchain mechanics creates a high barrier to entry
- **Market efficiency:** DEX arbitrage serves a legitimate function by keeping on-chain prices aligned with global markets

## Disadvantages
- **Ethically controversial:** Sandwich attacks extract value directly from regular DeFi users, effectively acting as a hidden tax
- **Extremely competitive:** The MEV landscape is dominated by sophisticated teams with custom infrastructure
- **Technical complexity:** Requires deep knowledge of Solidity, EVM internals, [[mempool]] dynamics, and block builder economics
- **Regulatory uncertainty:** Front-running is illegal in traditional markets; the legal status of MEV is unresolved
- **Arms race dynamics:** As more searchers enter, profits are competed away and flow increasingly to block builders and validators
- **Failed transaction costs:** On chains without bundle reversion guarantees, failed MEV attempts waste gas
- **Centralization concerns:** MEV infrastructure (Flashbots, relays, block builders) introduces centralization vectors into supposedly decentralized networks

## See Also
- [[flashbots]] -- the dominant MEV relay and infrastructure provider
- [[cross-exchange-arbitrage]] -- the off-chain equivalent of DEX arbitrage
- [[cross-chain-arbitrage]] -- multi-blockchain arb exploiting price fragmentation across chains
- [[cross-chain-bridges]] -- bridge infrastructure enabling cross-chain MEV
- [[triangular-arbitrage]] -- price inconsistency exploitation across three pairs
- [[flash-loans]] -- the zero-capital borrowing mechanism that enables capital-free MEV
- [[defi-yield-farming]] -- another DeFi-native strategy, focused on yield rather than extraction
- [[ethereum]] -- the primary blockchain where MEV extraction occurs
- [[uniswap]] -- the largest DEX and primary venue for MEV activity
