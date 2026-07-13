---
title: Crypto Yield Stacking Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, meta-strategy, crypto, defi, yield-farming, staking, restaking, liquidity-provision]
strategy_type: hybrid
markets: [crypto]
complexity: advanced
backtest_status: untested
related: [multi-strategy-portfolio, dca-technical-hybrid, volatility-targeting]
---

# Crypto Yield Stacking Strategy

## Overview

Yield stacking layers multiple [[defi]] yield sources on top of the same base capital to maximize risk-adjusted returns. Instead of earning a single yield (like 3-5% from [[eth-staking]] alone), each layer adds incremental return: [[liquid-staking]] keeps you liquid, [[restaking]] adds protocol security rewards, [[liquidity-provision]] earns trading fees, and [[points-farming]] captures potential [[airdrop]] value. A fully stacked position can generate 15-30%+ effective APY on ETH-denominated capital. But risk compounds with each layer -- [[smart-contract-risk]], [[slashing]], and [[depeg-risk]] all stack too.

## The Synergy

Each layer alone offers modest yields in mature DeFi. ETH staking: 3-5%. LP fees on stable pairs: 2-8%. Points farming: speculative. The magic is that these yields are **additive on the same capital**. You do not need separate capital for each -- the same ETH generates staking yield, restaking yield, LP fees, and points simultaneously.

The synergy also creates a natural risk ladder. Layer 1 (direct staking) is the safest. Each subsequent layer adds complexity and risk but also incremental yield. You can choose how many layers to climb based on your risk tolerance. Conservative DeFi users stop at Layer 2 (liquid staking). Aggressive yield farmers climb all five layers.

## Component Strategies

| Layer | Strategy | Yield | Risk |
|-------|----------|-------|------|
| 1 | [[eth-staking]] direct | 3-5% APY | Slashing (rare), ETH price |
| 2 | [[liquid-staking]] via [[lido]]/[[rocket-pool]] | +0.5-1% | LST depeg risk |
| 3 | [[restaking]] via [[eigenlayer]] | +2-5% | Additional slashing, smart contract |
| 4 | [[liquidity-provision]] on [[curve-finance]]/[[balancer]] | +3-10% | Impermanent loss (minimal for stETH/ETH) |
| 5 | [[points-farming]] for upcoming [[airdrop]]s | Speculative +5-20% | Token may not launch or value may disappoint |

## Implementation

**Step 1: Acquire ETH**

Start with your base ETH position. Use [[dca-technical-hybrid]] to accumulate at favorable prices. Minimum recommended: 5-10 ETH to justify gas costs across multiple protocols.

**Step 2: Liquid Stake via Lido**

Deposit ETH into [[lido]] and receive stETH. Verify Lido's TVL, audit status, and that stETH/ETH trades within 0.1% of par. Alternative: [[rocket-pool]] rETH for more decentralization. stETH earns ~3.5% staking APY via rebasing.

**Step 3: Restake on EigenLayer**

Deposit stETH into [[eigenlayer]]. Select AVSs (Actively Validated Services) to delegate to -- conservative operators offer lower but safer rewards. Monitor slashing events. Incremental yield: 2-5% APY.

**Step 4: LP Remaining Liquid Tokens**

If your restaking position issues a liquid restaking token (like eETH from [[etherfi]]), deposit into the [[curve]] stETH/ETH pool. Earn swap fees (2-6% APY) and stake the LP token in Convex for boosted [[crv]] + [[cvx]] rewards.

**Step 5: Maximize Points Exposure**

Deposit into protocols with upcoming token launches. Track via [[defillama]] and [[dune-analytics]]. Treat points value as speculative -- do not rely on it for yield calculations.

**Step 6: Monitor the Stack Weekly**

Check: stETH/ETH peg (flag if > 0.5% deviation), EigenLayer slashing events, LP impermanent loss, total effective APY, and protocol TVL changes (decreasing TVL = risk signal).

## Example Setup

**10 ETH yield stack:**

| Layer | Protocol | Position | Est. APY | Annual Yield (ETH) |
|-------|----------|----------|----------|-------------------|
| 1+2 | Lido (stETH) | 10 ETH staked | 3.5% | 0.35 ETH |
| 3 | EigenLayer | 6 stETH restaked | 3.0% | 0.18 ETH |
| 4 | Curve stETH/ETH pool | 4 stETH LP'd | 5.0% | 0.20 ETH |
| 5 | Points (EtherFi, etc.) | Interactions | ~8.0%* | 0.80 ETH* |
| | **Total** | | **~15.3%+** | **1.53 ETH** |

*Points yield is estimated and speculative based on historical airdrop values.

Without stacking: 3.5% from staking alone = 0.35 ETH/year.
With stacking: ~15%+ = 4x the yield on the same capital.

## When It Excels / When It Fails

**Excels when:**
- ETH price is stable or rising (all yields compound on an appreciating asset)
- DeFi protocols are healthy with high TVL and no exploits
- New protocols launch with generous points/incentive programs
- Gas costs are low, making multi-protocol interactions economical
- Used by technically proficient users who monitor positions actively

**Fails when:**
- Smart contract exploit hits any layer -- cascading losses are possible
- stETH depegs significantly (as in June 2022, briefly trading at 0.93)
- EigenLayer slashing event destroys restaked capital
- ETH price crashes -- high APY on a -50% asset is still a major loss
- Gas costs spike, eroding yields for smaller positions
- Regulatory action forces protocol shutdowns or restricts staking

## Real-World Usage

[[yearn-finance]] vaults pioneered automated yield stacking, routing deposits through optimal DeFi strategies. [[etherfi]], [[renzo]], and [[puffer-finance]] have built liquid restaking tokens that simplify layers 1-3 into a single deposit. Institutional DeFi funds like [[arca]] and [[pantera]] run managed yield stacking strategies with dedicated risk monitoring.

The key principle: **yield stacking is risk stacking**. Each layer adds return and adds a failure point. The conservative approach takes layers 1-2 (liquid staking, ~4% APY) and stops. The moderate approach adds layer 3 (restaking, ~7-9% APY). Only experienced DeFi operators should climb to layers 4-5 where [[smart-contract-risk]] multiplies and active monitoring becomes essential. Always ask: is the incremental 2-3% yield worth the additional protocol risk?
