---
title: "DeFi Yield Farming"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, defi, yield-farming, liquidity-mining, staking, lending, impermanent-loss, aave, curve, convex]
aliases: ["Yield Farming", "Liquidity Mining", "DeFi Yield Strategies"]
strategy_type: hybrid
timeframe: position|long-term
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[mev-strategies]]", "[[funding-rate-arbitrage]]", "[[impermanent-loss]]", "[[liquidity-pool]]", "[[automated-market-maker]]", "[[staking]]"]
---

# DeFi Yield Farming

## Overview

DeFi yield farming is the practice of deploying crypto assets into decentralized finance protocols to earn yield. At its simplest, this means providing [[liquidity]] to a [[decentralized-exchange]] (DEX) pool and earning a share of trading fees. At its most complex, it involves stacking multiple yield sources -- LP fees, protocol token rewards, lending interest, and governance incentives -- across composable DeFi protocols to maximize returns.

The strategy exploded during "DeFi Summer" (2020) when protocols like [[compound]] and [[sushiswap]] introduced [[liquidity-mining]] programs that distributed governance tokens to users. Yield farmers chase the highest APY across protocols, moving capital quickly from opportunity to opportunity. Core venues include [[aave]] and [[compound]] (lending/borrowing), [[uniswap]] and [[curve]] (DEX liquidity), [[convex]] and [[yearn]] (yield aggregation), and [[lido]] (liquid staking). While yields can be extraordinary (sometimes 100%+ APY during incentive periods), they come with significant risks: [[impermanent-loss]], [[smart-contract-risk]], token price depreciation, and protocol exploits.

## Rules

### Entry
1. **Select a protocol and pool:** Choose based on yield (APY), total value locked (TVL), protocol reputation, audit history, and asset pair risk. Higher yield = higher risk.
2. **Provide liquidity:** Deposit assets into the protocol. For DEX LPs, deposit both tokens in the required ratio (e.g., 50/50 ETH/USDC on [[uniswap]], or single-sided on [[curve]] stableswap pools).
3. **Stake LP tokens:** Many protocols offer additional rewards for staking your LP tokens in a gauge or farm contract. [[curve]] gauges distribute CRV rewards; [[convex]] boosts these further.
4. **Compound yields:** Regularly harvest reward tokens and reinvest (compound) into the same or higher-yielding pools. Yield aggregators like [[yearn]] and [[beefy]] automate this process.
5. **Layer yields:** Advanced farmers stack multiple sources: earn LP fees + CRV rewards + CVX boost + bribe income. The "Curve Wars" ecosystem epitomizes this layering.

### Exit
1. **Yield degradation:** When the APY drops below your required return (due to more capital entering the pool or token reward emissions declining), move capital to a higher-yielding opportunity.
2. **[[impermanent-loss]] threshold:** Monitor IL on volatile pairs. If IL exceeds earned fees, consider exiting before the loss deepens.
3. **Risk events:** Exit immediately if the protocol suffers an exploit, a governance attack, or a stablecoin depeg (e.g., UST collapse). Do not wait for recovery.
4. **Reward token management:** Regularly sell or hedge reward tokens (CRV, CVX, etc.) rather than accumulating. Many farming tokens decline 80-90% from their peaks.
5. **Gas cost awareness:** On [[ethereum]] mainnet, gas costs can eat heavily into small positions. Exit or consolidate when gas is low, or use L2s like [[arbitrum]] or [[optimism]].

### Position Sizing
Diversify across 3-5 protocols and multiple chains. Never allocate more than 25% of crypto portfolio to a single pool. Weight more heavily toward battle-tested protocols ([[aave]], [[curve]], [[uniswap]]) and less toward new, unaudited farms.

## Indicators Used
- **APY / APR** -- the headline yield metric. APR = simple rate; APY = compounded. Verify whether the displayed APY is sustainable or inflated by temporary incentives.
- **Total Value Locked (TVL)** -- the total capital in a protocol. Higher TVL generally means lower yield but higher safety. Rapidly declining TVL is a red flag.
- [[impermanent-loss]] calculator -- for volatile pairs, estimate IL at various price scenarios before entering.
- **Protocol revenue vs. emissions** -- sustainable yield comes from real revenue (trading fees, lending interest). If yield is 90% token emissions, it is not sustainable.
- **Audit status** -- check whether the protocol's smart contracts have been audited by reputable firms (Trail of Bits, OpenZeppelin, Spearbit).
- **Token emission schedule** -- understand when reward token emissions decrease, as this directly impacts APY.

## Example Trade
**Protocol:** Curve Finance + Convex Finance. **Pool:** 3pool (DAI/USDC/USDT).
1. **Deposit $50,000** in equal parts DAI, USDC, USDT into Curve's 3pool. Receive 3CRV LP tokens.
2. **Stake 3CRV on Convex:** Convex auto-stakes in Curve's gauge with boosted CRV rewards plus CVX rewards.
3. **Yield breakdown:**
   - Trading fees: 2% APY (real yield from swaps)
   - CRV rewards: 4% APY (boosted by Convex's veCRV holdings)
   - CVX rewards: 3% APY (Convex's governance token)
   - **Total: ~9% APY** on a stablecoin position with minimal [[impermanent-loss]] (all three assets are pegged to $1).
4. **Monthly income:** $50,000 x 9% / 12 = **~$375/month** in combined fees and reward tokens.
5. **After 6 months:** Earned ~$2,250. CRV and CVX tokens are harvested weekly and partially sold, partially reinvested.
6. **Risk event:** If one stablecoin depegs (e.g., USDC drops to $0.97), the pool rebalances heavily toward the depegged asset, causing losses beyond normal IL. Exit promptly in such scenarios.

## Performance Characteristics
- **Win Rate:** 70-85% of farming positions generate positive returns over their holding period, assuming no exploits or depegs.
- **Profit Factor:** 1.5-3.0 for established protocols. Can be higher during incentive programs but often inflated by depreciating reward tokens.
- **Best Market Conditions:** Bull markets with high DeFi activity (more trading fees), generous token emission programs, and rising TVL. Stablecoin farming performs consistently in any market.
- **Worst Market Conditions:** Bear markets (reward tokens crash 80-90%, TVL exits, fees dry up), protocol exploits, stablecoin depegs, and regulatory crackdowns on DeFi.

## Advantages
- **High yields:** DeFi farming offers yields far exceeding traditional finance, especially during incentive periods
- **Permissionless access:** Anyone with a wallet can participate -- no KYC, no minimum investment, no geographic restrictions
- **Composability:** Yields can be layered across protocols -- the "money legos" of DeFi enable creative strategies
- **Transparency:** All yields, TVL, and protocol mechanics are on-chain and verifiable
- **Stablecoin options:** Farming with stablecoins on pools like Curve 3pool provides yield with minimal directional risk

## Disadvantages
- **[[impermanent-loss|Impermanent loss]]:** Providing liquidity to volatile pairs can result in losses that exceed the fees earned. A 2x price divergence causes ~5.7% IL.
- **[[smart-contract-risk]]:** Bugs, exploits, and hacks have cost DeFi users billions. Even audited protocols can be compromised.
- **Reward token depreciation:** Most farming reward tokens (governance tokens) lose 80-95% of value over time, making "real" APY much lower than displayed
- **Gas costs:** On Ethereum mainnet, claiming rewards and compounding can cost $20-$100+ per transaction, eroding returns on small positions
- **Complexity:** Stacking multiple protocols increases smart contract exposure multiplicatively
- **Regulatory risk:** DeFi protocols face increasing regulatory scrutiny; token rewards may be reclassified as securities
- **Rug pulls:** New, unaudited farms can be outright scams where the deployer drains user funds

## See Also
- [[impermanent-loss]] -- the key risk specific to LP positions on DEXs
- [[automated-market-maker]] -- the mechanism underlying DEX liquidity provision
- [[mev-strategies]] -- another DeFi-native strategy that interacts with yield farming economics
- [[staking]] -- a simpler yield-generation method via proof-of-stake validation
- [[aave]] -- the leading DeFi lending protocol for farming lending yields
- [[curve]] -- the dominant DEX for stablecoin farming and CRV rewards
- [[convex]] -- the yield booster built on top of Curve
