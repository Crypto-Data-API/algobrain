---
title: "Restaking Strategies"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, defi, restaking, eigenlayer, staking, liquid-staking, avs, ethereum, yield, lrt]
aliases: ["Restaking", "EigenLayer Strategies", "Liquid Restaking", "LRT Strategies"]
strategy_type: hybrid
timeframe: position|long-term
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[defi-yield-farming]]", "[[points-farming]]", "[[staking]]", "[[ethereum]]", "[[lido]]"]
---

# Restaking Strategies

## Overview

Restaking is the practice of taking already-staked ETH (or liquid staking tokens like stETH, rETH) and re-pledging it to secure additional protocols, earning layered yields on the same capital. [[eigenlayer]] pioneered this concept on [[ethereum]], allowing stakers to opt-in to securing Actively Validated Services (AVSs) -- middleware, oracles, bridges, and data availability layers -- in exchange for additional rewards. The 2024-2026 restaking meta has created an ecosystem of Liquid Restaking Tokens (LRTs) like eETH (ether.fi), pufETH (Puffer), and rsETH (KelpDAO), which make restaked positions liquid and composable across DeFi.

## How It Works

1. **Stake ETH:** Deposit ETH into a liquid staking protocol like [[lido]] (receive stETH) or Rocket Pool (receive rETH). Earn the base Ethereum staking yield (~3-4% APY).
2. **Restake via EigenLayer:** Deposit stETH/rETH into [[eigenlayer]] directly, or use an LRT protocol (ether.fi, Puffer, KelpDAO) to receive a liquid restaking token.
3. **Delegate to AVS operators:** Choose which AVSs to secure through your restaked capital. Each AVS offers different reward rates and risk profiles. Diversify across multiple AVSs.
4. **Earn layered yields:** Accumulate base staking yield + AVS rewards + potential LRT protocol incentives + [[points-farming|points]] for future airdrops.
5. **Manage risk:** Monitor AVS slashing conditions, operator performance, and smart contract risk. Restaking multiplies exposure -- a slashing event on one AVS can affect your base staked ETH.

## Example

A restaker deploys 32 ETH ($100,000 at $3,125/ETH). Step 1: Stake via Lido, receive 32 stETH, earn 3.5% APY ($3,500/year). Step 2: Deposit stETH into ether.fi, receive 32 eETH (liquid restaking token). Step 3: eETH is delegated to 3 AVSs paying a combined 2% additional APY ($2,000/year). Step 4: Use eETH as collateral on [[aave]] to borrow USDC and deploy into stablecoin farming for an additional 5% ($5,000). Total layered yield: ~10.5% on the original ETH, plus ether.fi points for a potential airdrop. The tradeoff: smart contract risk is now stacked across Lido, EigenLayer, ether.fi, and Aave -- four protocols deep.

## Advantages

- **Capital efficiency** -- earn multiple yield layers on the same underlying ETH
- **Liquid positions** -- LRTs keep restaked capital liquid and usable across DeFi, unlike locked staking
- **Ecosystem growth** -- restaking secures new protocols, and early restakers often receive token airdrops
- **Flexible risk management** -- choose which AVSs to delegate to based on risk/reward appetite

## Disadvantages

- **Compounding smart contract risk** -- each protocol layer adds another vector for exploits or bugs
- **Slashing risk** -- AVS slashing conditions can result in loss of restaked ETH; multiple AVS delegations multiply this exposure
- **Complexity** -- managing LRT positions, AVS selection, and DeFi composability requires significant expertise
- **Nascent and evolving** -- the restaking ecosystem is young; AVS economics, reward sustainability, and slashing parameters are still being developed
- **Correlation risk** -- a major Ethereum or EigenLayer incident would cascade across all layers simultaneously

## See Also

- [[defi-yield-farming]] -- broader yield strategies that restaking extends and layers upon
- [[points-farming]] -- a complementary strategy often combined with restaking for airdrop eligibility
- [[staking]] -- the base layer of proof-of-stake yield that restaking builds on
- [[ethereum]] -- the blockchain underpinning the restaking ecosystem
- [[lido]] -- the leading liquid staking protocol providing stETH for restaking
