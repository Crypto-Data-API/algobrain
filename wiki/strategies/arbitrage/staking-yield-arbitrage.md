---
title: "Staking Yield Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [arbitrage, staking, yield, defi, lending, funding-rate, delta-neutral, restaking, eigenlayer, liquid-staking]
aliases: ["Staking Arb", "Yield Spread Arbitrage", "DeFi Yield Arb"]
strategy_type: quantitative
timeframe: swing|position
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[restaking-strategies]]", "[[funding-rate-arbitrage]]", "[[delta-neutral-yield-farming]]", "[[defi]]", "[[aave]]", "[[liquid-staking]]"]
---

# Staking Yield Arbitrage

## Overview

Staking yield arbitrage exploits yield differentials across DeFi staking, lending, and derivatives markets. In crypto, the same capital can earn vastly different returns depending on where it is deployed: native staking (e.g., ETH staking at ~3-5%), lending protocols like [[aave]] (variable rates from 1-10%+), [[funding-rate-arbitrage|perpetual swap funding rates]] (annualized 5-30%+ in bull markets), and [[restaking-strategies|restaking protocols]] like EigenLayer (additional yield on top of base staking). When these yields diverge, capital flows from lower-yield to higher-yield opportunities, and sophisticated traders capture the spread.

A particularly popular variant is the liquid staking token (LST) basis trade. When [[liquid-staking]] tokens like stETH (Lido) or rETH (Rocket Pool) trade at a discount to their underlying ETH value, buying the discounted LST and waiting for convergence to the peg provides a near risk-free return on top of the base staking yield. This trade was especially lucrative during the stETH depeg in June 2022, when stETH traded at a 5-7% discount following the Terra/Luna collapse and Three Arrows Capital liquidation.

## How It Works

The arbitrageur continuously monitors yields across the DeFi ecosystem and allocates capital to the highest risk-adjusted return:

- **Direct comparison:** If ETH staking yields 3.5% but [[aave]] ETH lending yields 6%, deposit ETH into Aave for the higher return. When Aave rates drop below staking yield, move back.
- **LST basis trade:** When stETH trades at 0.97 ETH (3% discount), buy stETH. Once the discount narrows to 0% (which it must once withdrawals are enabled), the 3% gain plus ongoing ~3.5% staking yield provides a ~6.5%+ annualized return.
- **Restaking yield stacking:** Deposit ETH into Lido (earn ~3.5% base), then stake the stETH into EigenLayer (earn additional 2-5% restaking yield), creating a total yield of 5.5-8.5%. Compare this to the lending rate; if the stacked yield exceeds lending by enough to compensate for the added smart contract risk, the arb is positive.
- **Delta-neutral yield capture:** Stake ETH to earn the staking yield, then short ETH perpetual futures to hedge all price exposure. Net return = staking yield minus funding rate cost (or plus, if funding is negative). This isolates the yield component with zero directional exposure.

## Entry/Exit Rules

### Entry
1. **Monitor yield sources:** Track staking rates (Lido, Rocket Pool, Coinbase), lending rates ([[aave]], Compound, Morpho), funding rates (Binance, Bybit, dYdX), and restaking yields (EigenLayer, Symbiotic).
2. **Calculate risk-adjusted spread:** Compare yields after accounting for smart contract risk, [[liquidity]] risk, and gas costs. A 1% yield differential may not justify the added risk of a new protocol.
3. **Enter when spread exceeds threshold:** If the spread between two comparable-risk yield sources exceeds 2-3% annualized, reallocate capital.
4. **For LST basis trades:** Enter when the LST discount exceeds 1-2%. Monitor the withdrawal queue and redemption timeline.
5. **For delta-neutral:** Stake the asset and simultaneously open a short perpetual position of equal notional value. Ensure the funding rate does not exceed the staking yield.

### Exit
1. **Yield convergence:** When the spread between yield sources narrows below the threshold, close the arb and reassess.
2. **LST peg recovery:** For LST basis trades, sell when the discount narrows to < 0.1% or the LST trades at a premium.
3. **Funding rate reversal:** For delta-neutral positions, exit if perpetual funding rates flip and the short position becomes costly (eating into staking yield).
4. **Protocol risk escalation:** Exit if the protocol experiences an exploit, governance attack, or significant withdrawal of TVL (total value locked).

## Example Trade

**Setup:** ETH staking via Lido yields 3.5% APY. stETH is trading at 0.965 ETH on Curve (3.5% discount). [[aave]] ETH lending rate is 2.0%. ETH perpetual funding rate on Binance is +0.01% per 8 hours (~13% annualized, paid by longs to shorts).

**Trade 1 -- LST basis trade:**
1. **Buy 100 stETH** on Curve for 96.5 ETH (saving 3.5 ETH vs. staking directly).
2. **Hold for 3 months.** Earn 3.5% annualized staking yield = ~0.875 stETH in rewards.
3. **stETH peg recovers** to 0.998 ETH. Sell 100.875 stETH for ~100.67 ETH.
4. **Profit:** 100.67 - 96.5 = **4.17 ETH** (~4.3% return in 3 months, ~17% annualized).

**Trade 2 -- Delta-neutral yield:**
1. **Stake 50 ETH** via Lido, receiving 50 stETH. Base yield: 3.5% APY.
2. **Short 50 ETH** worth of ETH-PERP on Binance. Funding rate: +13% annualized (received by shorts).
3. **Total yield:** 3.5% (staking) + 13% (funding) = **16.5% annualized**, with zero ETH price exposure.
4. **Hold for 1 month.** Earn ~1.375% = **0.69 ETH**.
5. **Risk:** If funding rate flips negative (shorts pay longs), the trade becomes unprofitable. Monitor daily and exit if funding averages negative over 3+ days.

## Risk Management

- **Smart contract risk:** Every DeFi protocol carries the risk of exploits, bugs, or governance attacks. Diversify across protocols and avoid allocating more than 20% of capital to any single protocol.
- **LST depeg risk:** Liquid staking tokens can depeg further before recovering. The stETH discount widened to 7% in June 2022 before recovering over several months. Size positions to withstand further depegging.
- **Funding rate volatility:** Perpetual funding rates can swing from +30% to -20% annualized within days. Delta-neutral yield strategies must be actively monitored and exited when funding flips.
- **[[liquidity]] risk:** Large staking/unstaking operations may face withdrawal queues (ETH staking queue can take days to weeks during high demand).
- **Restaking risk:** EigenLayer and similar restaking protocols add additional slashing conditions on top of base staking. The compounded risk of multiple slashing vectors is non-trivial.
- **Gas costs:** Moving capital between protocols on Ethereum L1 incurs gas fees ($5-50+ per transaction). Frequent rebalancing can erode yield on smaller positions.

## Advantages
- **Multiple yield sources** -- the DeFi ecosystem provides diverse, uncorrelated yield opportunities
- **Delta-neutral variant eliminates price risk** -- earn yield without exposure to crypto price swings
- **LST basis trades have structural convergence** -- stETH will converge to ETH value once withdrawals are enabled
- **Composable** -- yields can be stacked (stake + restake + lend the receipt token) for enhanced returns
- **Transparent and accessible** -- all rates are on-chain, publicly observable, and require no minimum capital or KYC

## Disadvantages
- **Smart contract risk** -- protocol exploits can result in total loss of capital
- **Yield compression** -- as more capital flows into high-yield opportunities, rates compress toward equilibrium
- **Complexity** -- managing positions across multiple protocols, chains, and yield sources requires sophisticated tracking
- **Gas costs** -- Ethereum L1 gas fees make frequent rebalancing uneconomical for smaller portfolios (< $10K)
- **Impermanent loss** -- providing LST [[liquidity]] on AMMs exposes capital to impermanent loss if the peg moves
- **Regulatory uncertainty** -- staking yields may be classified as securities income in some jurisdictions

## Real-World Examples
- **stETH depeg (June 2022):** Following the Terra/Luna collapse and Three Arrows Capital insolvency, stETH traded at a 5-7% discount to ETH. Traders who bought the discount earned 5-7% convergence profit plus ~4% staking yield over the following months as the peg recovered.
- **EigenLayer restaking boom (2024):** EigenLayer attracted $15B+ in restaked ETH, offering additional yield (via airdrops and AVS payments) on top of base Ethereum staking. The compounded yield attracted massive capital inflows.
- **Basis trade blow-ups:** In November 2022, the FTX collapse caused funding rates to spike negative as the market crashed. Delta-neutral stakers who were short perps suddenly faced large negative funding costs, turning profitable positions into losses.

## See Also
- [[funding-rate-arbitrage]] -- the perpetual swap funding rate component of delta-neutral strategies
- [[restaking-strategies]] -- yield enhancement through restaking protocols like EigenLayer
- [[delta-neutral-yield-farming]] -- the broader category of hedged yield strategies
- [[liquid-staking]] -- the LST infrastructure (Lido, Rocket Pool) that enables these trades
- [[defi]] -- the ecosystem in which staking yield arbitrage operates, including [[aave]] lending
