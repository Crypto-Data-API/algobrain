---
title: Arbitrage
type: concept
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [arbitrage, strategies, microstructure, pricing]
aliases: [arb, no-arbitrage, law-of-one-price]
related:
  - "[[spread]]"
  - "[[liquidity]]"
  - "[[futures]]"
  - "[[price-discovery]]"
  - "[[etf-arbitrage]]"
  - "[[2020-03-bond-etf-dislocation]]"
  - "[[2017-2021-kimchi-premium]]"
  - "[[2022-05-terra-luna-depeg-arb]]"
---

# Arbitrage

Arbitrage is the practice of exploiting price differences for the same or equivalent asset across different markets or instruments to earn a risk-free (or low-risk) profit. More than just a trading strategy, the **no-arbitrage principle** is one of the foundational pillars of modern financial theory.

## Overview

In theory, arbitrage is riskless -- you simultaneously buy low in one market and sell high in another. In practice, execution risk, latency, fees, and capital requirements mean pure arbitrage is rare. Still, arb strategies play a vital role in keeping markets efficient through [[price-discovery]].

For a complete catalog of arbitrage strategies, see the [[arbitrage-overview|Arbitrage Strategy Index]].

## The Law of One Price

The **Law of One Price (LOOP)** states that identical assets must trade at the same price in all markets, after accounting for transaction costs. If a stock trades at $100 on the NYSE and $101 on the LSE, arbitrageurs will buy on NYSE and sell on LSE until prices converge.

LOOP is the empirical observation. The **no-arbitrage principle** is the theoretical implication: in an efficient market, no strategy should generate risk-free profit without capital at risk. These two ideas underpin nearly all of modern finance:

- **Derivatives pricing**: The [[black-scholes]] model, [[put-call-parity|put-call parity]], and all option pricing frameworks derive prices by constructing replicating portfolios and invoking no-arbitrage. If the option price deviates from the replicating portfolio cost, an arb exists.
- **Fixed income**: Bond pricing, yield curves, and [[interest-rate-parity]] are all built on no-arbitrage conditions. Forward rates are derived by assuming you cannot arb between spot and forward positions.
- **Crypto**: [[funding-rate-arbitrage]] and [[cash-and-carry]] exploit deviations from no-arbitrage in perpetual futures and spot markets.

Without the no-arbitrage principle, there would be no consistent way to price [[futures]], [[options]], or any derivative instrument.

## Types of Arbitrage

- **Spatial arbitrage**: Buying an asset on one exchange and selling it on another where the price is higher. Common in crypto due to fragmented markets. See [[cross-exchange-arbitrage]].
- **Cross-chain arbitrage**: Exploiting price differences for the same token across different blockchains, requiring [[cross-chain-bridges|bridges]] to move assets between chains. See [[cross-chain-arbitrage]].
- **Triangular arbitrage**: Exploiting pricing inconsistencies between three currency pairs (e.g., BTC/USD, ETH/BTC, ETH/USD) to extract profit from the loop. See [[triangular-arbitrage]].
- **Statistical arbitrage (stat arb)**: Using quantitative models to identify historically correlated assets that have temporarily diverged, betting on reversion. See [[statistical-arbitrage]], [[pairs-trading]].
- **Funding rate arbitrage**: In perpetual futures markets, going long spot and short perps (or vice versa) to collect the [[funding-rate|funding rate]] differential while remaining delta-neutral. See [[funding-rate-arbitrage]].
- **Cash-and-carry**: Buying the spot asset and selling the futures contract when futures trade at a premium ([[contango]]), locking in the basis as profit. See [[cash-and-carry]].
- **Volatility arbitrage**: Trading the difference between implied and realized [[volatility]]. See [[volatility-arbitrage]].
- **Merger arbitrage**: Buying the target and shorting the acquirer to capture the deal spread. See [[merger-arbitrage]].
- **Convertible arbitrage**: Long convertible bonds, short the underlying equity. See [[convertible-arbitrage]].

## Limits to Arbitrage

In a seminal 1997 paper, Andrei Shleifer and Robert Vishny demonstrated that **arbitrage opportunities can persist** even when they are visible to all market participants. Their "Limits to Arbitrage" framework explains why markets are not always efficient in practice.

### Why Arb Opportunities Persist

The Shleifer & Vishny framework identifies several frictions that prevent arbs from closing:

- **Capital constraints**: Arbitrageurs have finite capital. If a trade moves against them before converging, they may face margin calls and forced liquidation -- exactly when the arb opportunity is largest. This is sometimes called the "performance-based arbitrage" problem.
- **Transaction costs**: Fees, slippage, bid-ask [[spread]]s, and funding costs can eat into or eliminate the apparent profit.
- **Margin and collateral requirements**: Even "risk-free" arbs require capital posted as margin, which limits position sizing and creates path-dependency risk.
- **Counterparty risk**: In OTC markets, the other side may default before settlement. This was a major concern during [[2008-global-financial-crisis]].
- **Execution risk**: Legs of a multi-leg arb may not execute simultaneously. One leg fills, the other doesn't -- now you have directional exposure, not an arb.
- **Regulatory barriers**: Capital controls, KYC/AML requirements, and jurisdictional restrictions can physically block arb execution. The [[2017-2021-kimchi-premium|Kimchi Premium]] persisted for years because Korean capital controls made the arb mechanically difficult despite a 40% price gap.
- **Model risk**: In [[statistical-arbitrage]], the "arb" depends on a model of fair value. If the model is wrong, the trade is not an arb at all.

### The Fundamental Paradox

If arbitrageurs are the mechanism that makes markets efficient, but arb requires capital and carries risk, then markets can only be **approximately** efficient. The degree of efficiency depends on the amount of arb capital willing to bear these frictions. This is why mispricings tend to be largest during crises -- exactly when arb capital is most constrained.

## Real-World Arbitrage Failures

History provides stark examples of arb mechanisms breaking down:

| Event | Year | What Failed | Outcome |
|-------|------|-------------|---------|
| [[2020-03-bond-etf-dislocation]] | 2020 | Bond ETF creation/redemption arb | LQD traded 5.7% below NAV; Fed intervened |
| [[2022-05-terra-luna-depeg-arb]] | 2022 | UST/LUNA mint/burn stabilization arb | Reflexive death spiral destroyed $40B+ |
| [[2017-2021-kimchi-premium]] | 2017-21 | Cross-exchange crypto arb | 40% premium persisted for months due to capital controls |
| LTCM collapse | 1998 | Convergence arbs in bonds and swaps | $4.6B loss; near-systemic failure; Fed-orchestrated bailout |
| Volkswagen short squeeze | 2008 | Short arb on VW overvaluation | VW briefly became world's most valuable company; shorts lost billions |
| [[2020-2024-bridge-exploits|Bridge exploits]] | 2020-24 | Cross-chain arb infrastructure (bridges) | $2.5B+ lost to bridge hacks; systemic risk for cross-chain arbitrageurs |

These failures share a common pattern: the arb was theoretically correct, but real-world frictions (liquidity, capital, regulation, reflexivity) prevented it from working as expected.

## Trading Relevance

Pure arbitrage opportunities are typically captured by high-frequency firms with speed and infrastructure advantages. Retail traders more commonly engage in statistical or [[funding-rate-arbitrage|funding rate arbitrage]], which carry some directional or execution risk. Arb activity narrows [[spread]]s and improves market [[liquidity]] for all participants.

Understanding where and why arbs fail is arguably more important than identifying arb opportunities. The edge in arb trading comes not from spotting the price gap (which is often visible to everyone), but from having the **infrastructure, capital, and risk management** to execute and hold the trade through adverse conditions.

## Related

- [[spread]] -- arb compresses price differentials
- [[futures]] -- basis trades exploit spot-futures spread
- [[liquidity]] -- arb provides liquidity across venues
- [[price-discovery]] -- arb is a key mechanism
- [[etf-arbitrage]] -- creation/redemption mechanism that keeps ETF prices aligned with NAV
- [[arbitrage-overview]] -- comprehensive index of all arbitrage strategies
- [[2020-03-bond-etf-dislocation]] -- bond ETF arb failure during COVID crash
- [[2022-05-terra-luna-depeg-arb]] -- algorithmic stablecoin arb death spiral
- [[2017-2021-kimchi-premium]] -- persistent crypto arb anomaly from capital controls
