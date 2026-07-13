---
title: "Sturdy (SN10)"
type: entity
created: 2026-04-19
updated: 2026-06-12
status: draft
tags: [crypto, bittensor, defi, yield]
aliases: ["SN10", "Sturdy Finance"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://sturdy.finance/"
related: ["[[bittensor]]", "[[bittensor-subnets]]", "[[dtao]]", "[[defi-yield-farming]]", "[[yield-aggregators]]", "[[stablecoin-yield]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Sturdy (SN10)

**Sturdy** (SN10) is a Bittensor subnet that pairs with Sturdy Finance's DeFi yield aggregator. Miners submit proposed capital allocations across lending markets (Aave, Compound, Morpho, Yearn-style vaults, etc.); validators score allocations on realized yield net of gas and risk. The best miner allocations are used to rebalance Sturdy Finance's on-chain vaults.

## How It Works

Sturdy Finance operates yield vaults on Ethereum (and rollups). SN10 effectively outsources the allocation-optimization problem to Bittensor miners. Each epoch:

1. Validators publish the current vault composition and available markets.
2. Miners submit proposed reallocations.
3. The selected allocation is executed on-chain.
4. Validators score miners retrospectively on the yield realized over the next epoch.

## Trading Relevance

**Directly useful for DeFi yield optimization.** Anyone running a stablecoin or ETH yield book can consume the SN10 signal (either by depositing into Sturdy vaults or by replicating the allocations off-chain). The subnet also has a clear off-chain revenue model: Sturdy Finance's vault management fees flow back to reinforce alpha-10 valuation.

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]] -- protocol context
- [[defi-yield-farming]], [[yield-aggregators]], [[stablecoin-yield]] -- strategy context
- [[sturdy-finance]] -- Sturdy's off-chain product

## Sources

- sturdy.finance
- taostats.io / dtao.gg
