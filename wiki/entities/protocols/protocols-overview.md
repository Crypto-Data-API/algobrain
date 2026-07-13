---
title: "Protocols"
type: index
created: 2026-04-06
updated: 2026-06-17
status: good
tags: [protocols, defi, entities, index]
---

# Protocols

The hub for DeFi protocols, blockchain projects, and decentralized infrastructure relevant to trading. These protocols rebuild financial primitives on-chain — trading, lending, borrowing, staking, and derivatives — without traditional intermediaries. Understanding them is essential for anyone trading on-chain or building DeFi-native strategies like arbitrage, liquidation, or MEV extraction.

The foundational set: [[uniswap]] pioneered the automated market maker (AMM); [[aave]] enables decentralized lending and flash loans; [[makerdao]] issues the DAI stablecoin as DeFi's central bank; and infrastructure like [[quicknode]] supplies the RPC nodes that connect trading bots to chains.

## DEXs & AMMs

- [[uniswap]] — The dominant DEX and AMM; concentrated liquidity (v3/v4)
- [[curve-finance]] — Stableswap AMM optimized for like-priced assets
- [[sushiswap]] — Multi-chain AMM and the original "vampire attack"

## Lending & Stablecoins

- [[aave]] — Decentralized lending, borrowing, and flash loans
- [[compound]] — Algorithmic money-market protocol
- [[makerdao]] — DAI issuer; over-collateralized lending; DeFi central bank

## Derivatives & Perps

- [[dydx]] — Order-book perpetual-futures DEX
- [[gmx]] — Oracle-priced perps with the GLP liquidity model
- [[synthetix]] — Synthetic-asset and derivatives liquidity layer

## Staking & Yield

- [[lido]] — Liquid staking; the largest stETH issuer
- [[yearn]] — Yield-aggregation vaults
- [[convex]] — Boosted Curve yield and governance aggregation

## Networks & Scaling

- [[polygon]] — EVM scaling network and ecosystem
- [[arbitrum]] — Optimistic-rollup L2

## Infrastructure & AI

- [[quicknode]] — High-performance blockchain RPC for trading applications
- [[bittensor]] — Decentralized machine-learning network
- [[virtuals-protocol]] — On-chain AI-agent launch and coordination layer

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/entities/protocols"
WHERE type != "index"
SORT updated DESC
```

## Sources

- General market knowledge; no specific wiki source ingested yet.
