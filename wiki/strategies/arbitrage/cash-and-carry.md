---
title: "Cash and Carry Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [arbitrage, basis-trade, futures, contango, market-neutral, crypto, commodities, risk-free]
aliases: ["Basis Trade", "Cash and Carry", "Spot-Futures Arbitrage"]
strategy_type: quantitative
timeframe: position|long-term
markets: [crypto, commodities]
complexity: intermediate
backtest_status: untested
related: ["[[funding-rate-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[contango]]", "[[backwardation]]", "[[futures]]", "[[basis]]"]
---

# Cash and Carry Arbitrage

## Overview

Cash and carry arbitrage is one of the oldest and most straightforward arbitrage strategies in finance. The trader buys an asset on the spot market and simultaneously sells a futures contract on the same asset at a higher price. The difference between the futures price and the spot price is the **[[basis]]**, and it represents the locked-in, near-risk-free profit that the trader captures as the futures contract converges to spot at expiry. This convergence is guaranteed by the mechanics of futures settlement.

The strategy works when futures trade in [[contango]] (futures price > spot price), which occurs when carry costs (storage, insurance, opportunity cost of capital) or speculative demand push futures above spot. In crypto markets, contango is common during bullish periods -- BTC quarterly futures on [[cme]], [[deribit]], or [[binance]] frequently trade 5-20% annualized above spot. In commodities, contango arises from storage costs and seasonal supply/demand dynamics. The cash and carry trade is the textbook "risk-free" arbitrage, though in practice, it carries execution, counterparty, and margin risks.

## Rules

### Entry
1. **Identify contango:** Futures price must be meaningfully above spot price. Calculate the annualized basis: ((Futures - Spot) / Spot) x (365 / DTE). Only enter if the annualized yield exceeds your required return (typically > 8-10%).
2. **Buy spot:** Purchase the underlying asset on the spot market. For crypto, buy BTC/ETH on a trusted exchange or hold in self-custody.
3. **Sell futures:** Simultaneously sell an equal notional amount of futures at the higher price. Choose the nearest liquid expiry (quarterly contracts are standard).
4. **Lock in the basis:** The difference between the futures sell price and spot buy price is your locked-in profit, realized at expiry.
5. **Ensure same settlement:** Both legs must reference the same asset and settle at the same price at expiry.

### Exit
1. **Hold to expiry:** The default strategy. At futures expiration, the futures price converges to spot. Close both legs or let the futures settle. Profit = initial basis.
2. **Early exit on basis compression:** If the basis narrows quickly (e.g., within a few days instead of weeks), you can close both legs early to capture most of the profit without waiting.
3. **Roll the position:** If a further-dated futures contract has an attractive basis, close the current position at expiry and open a new one.
4. **Emergency exit:** If counterparty risk emerges (exchange solvency concerns), unwind immediately regardless of basis.

### Position Sizing
Allocate based on the capital required for both legs. For crypto, the spot purchase + futures margin typically requires 1.5-2x the notional value. Limit exposure to any single exchange to 20-25% of portfolio.

## Indicators Used
- [[basis]] -- futures price minus spot price; the fundamental signal. Positive basis = contango = trade opportunity.
- Annualized basis yield -- (basis / spot) x (365 / DTE). Compares the opportunity to other yield sources.
- [[contango]] / [[backwardation]] -- the term structure of futures prices. Contango across multiple expiries confirms the setup.
- [[open-interest]] on futures -- high OI means deep liquidity for execution.
- Funding rate on [[perpetual-futures]] -- if perp funding is also high, confirms bullish carry environment.
- Days to expiry -- shorter DTE means faster convergence but potentially less total basis to capture.

## Example Trade
**Asset:** BTC spot at $68,000. CME BTC quarterly futures (62 DTE) at $70,040.
1. **Buy 1 BTC spot** at $68,000.
2. **Sell 1 BTC futures** (CME quarterly) at $70,040.
3. **Locked-in basis:** $70,040 - $68,000 = $2,040. **Annualized yield:** ($2,040 / $68,000) x (365 / 62) = **17.7% APY**.
4. **Hold for 62 days.** BTC moves to $75,000 at expiry.
5. **Spot position:** +$7,000 gain. **Futures position:** -$4,960 loss ($75,000 - $70,040). But the futures converged to spot, so the net is: $7,000 - $4,960 = $2,040. Or if BTC drops to $60,000: spot loses $8,000, futures gain $10,040, net = $2,040.
6. **Result:** Regardless of where BTC settles, the profit is $2,040 (minus fees). The trade is directionally neutral.

## Performance Characteristics
- **Win Rate:** ~99% when executed correctly. Losses only occur from counterparty failure, execution errors, or forced liquidation on the futures leg.
- **Profit Factor:** Very high in theory (near-infinite risk-adjusted returns on the locked basis). In practice, reduced by fees, margin costs, and counterparty risk.
- **Best Market Conditions:** Bull markets with speculative demand pushing futures into steep contango. Crypto bull runs. Commodity markets with high storage costs.
- **Worst Market Conditions:** Backwardation (futures below spot) -- the trade does not exist. Bear markets with collapsing basis.

## Advantages
- **Near risk-free:** When both legs are properly matched, the profit is locked in at entry regardless of price direction
- **Predictable returns:** The yield is known at entry -- no guesswork about future market conditions
- **Simple conceptually:** Buy low (spot), sell high (futures), wait for convergence
- **Works across asset classes:** Applicable to crypto, commodities, bonds, and equities
- **No directional bias needed:** Profits are independent of whether the asset goes up or down

## Disadvantages
- **Counterparty risk:** If the exchange holding your spot or futures fails (e.g., [[ftx]]), the "risk-free" profit vanishes along with your capital
- **Margin risk:** Large adverse moves in the underlying can trigger margin calls on the futures short, requiring additional capital or forced liquidation before convergence
- **Capital-intensive:** Requires funding both the spot purchase and futures margin simultaneously
- **Opportunity cost:** Capital is locked for the duration of the futures contract (weeks to months)
- **Basis can widen before narrowing:** Temporary mark-to-market losses are possible even though the final convergence is guaranteed
- **Execution risk:** Both legs must be executed near-simultaneously to lock in the basis; slippage on either leg erodes profit

## See Also
- [[funding-rate-arbitrage]] -- the perpetual futures equivalent, earning funding payments instead of basis convergence
- [[contango]] -- the futures term structure condition that enables the trade
- [[basis]] -- the spread between spot and futures that defines the profit
- [[futures]] -- the derivatives instrument used for the short leg
- [[cross-exchange-arbitrage]] -- another market-neutral crypto strategy
