---
title: "Liquid Staking"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [crypto, defi, staking, ethereum, yield]
aliases: ["liquid staking", "LST", "liquid staking token", "liquid staking derivative"]
domain: [crypto, defi]
difficulty: intermediate
related: ["[[staking]]", "[[restaking]]", "[[lido-dao]]", "[[rocket-pool]]", "[[ethereum]]", "[[proof-of-stake]]", "[[depeg-risk]]"]
---

Liquid staking is a DeFi primitive that lets users stake cryptocurrency — most commonly [[ethereum|ETH]] — while receiving a transferable, tradeable token that represents their staked position plus accrued rewards. Traditional [[staking]] locks capital and disables its use elsewhere; liquid staking preserves the yield of [[proof-of-stake]] validation while keeping the underlying capital productive across the rest of DeFi.

## How It Works

A user deposits ETH into a liquid staking protocol. The protocol pools deposits, runs (or delegates to) validators on the [[ethereum|Ethereum]] beacon chain, and mints the depositor a liquid staking token (LST) that is redeemable for the underlying stake plus its share of rewards. The LST can be freely transferred, sold, used as collateral, deposited into [[liquidity-provision|liquidity pools]], or restaked — all while the underlying ETH continues earning staking rewards.

## Major LSTs

- **stETH** (Lido) — the dominant LST by market share, a rebasing token whose balance grows daily to reflect staking rewards
- **rETH** (Rocket Pool) — a reward-bearing token whose price (not balance) appreciates versus ETH over time
- **cbETH** (Coinbase) — a centralized, custodial reward-bearing LST
- **swETH** (Swell) — a newer reward-bearing LST emphasizing decentralization

## Rebasing vs Reward-Bearing

Rebasing tokens (stETH) adjust wallet balances daily, which keeps price close to 1:1 with ETH but breaks compatibility with many DeFi protocols. Reward-bearing tokens (rETH, cbETH) hold balance constant while the exchange rate with ETH grows, making them cleanly composable but causing the token to trade above 1 ETH.

## Peg and Depeg Risk

LSTs are expected to trade near their underlying ETH value. The peg is maintained by arbitrage — anyone can redeem the LST for ETH via the protocol's queue, and the ability to redeem (plus secondary market liquidity) typically holds the price tight. Peg stress appears during liquidity crises: in June 2022, stETH briefly traded at roughly 0.93 ETH when Three Arrows Capital and Celsius were forced sellers and redemptions were not yet enabled on withdrawal-less beacon chain. See [[depeg-risk]].

## Role in DeFi

LSTs are the foundational building block for higher-order yield: they are deposited into [[liquidity-provision|AMM pools]], used as loan collateral, wrapped, and — most importantly — restaked. See [[restaking]] for how LSTs extend into securing additional services via EigenLayer.

## Related

- [[staking]]
- [[restaking]]
- [[proof-of-stake]]
- [[depeg-risk]]
- [[smart-contract-risk]]

## Sources

- Lido. *Lido Documentation* (docs.lido.fi) — stETH mechanics, rebasing, and withdrawal architecture.
- Rocket Pool. *Rocket Pool Documentation* (docs.rocketpool.net) — rETH reward-bearing model and node-operator design.
- Ethereum Foundation. *Staking* and *The Merge / Shanghai (Shapella)* documentation (ethereum.org) — proof-of-stake validation and staking withdrawals enabled April 2023.
- Coinbase. *cbETH Whitepaper* (2022) — custodial reward-bearing LST design.
- On-chain and market data on the June 2022 stETH discount during the Three Arrows Capital / Celsius forced-selling episode (Dune Analytics, Curve stETH/ETH pool data).
