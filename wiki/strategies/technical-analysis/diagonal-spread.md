---
title: "Diagonal Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [options, diagonal-spread, directional, time-spread, poor-mans-covered-call, theta, income]
aliases: ["Poor Man's Covered Call", "PMCC", "Diagonal Calendar"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[calendar-spread]]", "[[covered-call]]", "[[butterfly-spread]]", "[[risk-reversal]]", "[[implied-volatility]]", "[[theta]]", "[[delta]]", "[[option-volatility-and-pricing]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]"]
---

# Diagonal Spread

## Overview

The Diagonal Spread combines elements of a [[calendar-spread]] and a vertical spread by buying a longer-dated option at one strike and selling a shorter-dated option at a **different strike**. The most popular variant is the **"Poor Man's Covered Call" (PMCC):** buy a deep ITM [[call-option]] with 6-12 months to expiration and sell a near-term OTM call against it, mimicking a [[covered-call]] at a fraction of the capital. The long option acts as a stock substitute, while the short option generates recurring income through [[theta]] decay.

Diagonals blend **directional bias** with **time decay harvesting**. By buying a deeper ITM option (high [[delta]], 0.70-0.85), the long leg moves nearly dollar-for-dollar with the underlying (Source: [[book-option-volatility-and-pricing]]). The short OTM leg decays faster due to its shorter expiration and lower intrinsic value. The trader profits from the time decay differential and from moderate directional moves. The strategy is capital-efficient: a deep ITM LEAPS call might cost $30-40 per share versus $200+ to own the stock outright, freeing up capital for other positions.

## Rules / Setup

### Entry
1. **Buy the back-month option:** Purchase a deep ITM call (0.70-0.85 delta) with 6-12 months (or LEAPS) to expiration. The high delta ensures the option behaves like the underlying.
2. **Sell the front-month option:** Sell an OTM call (0.20-0.35 delta) with 30-45 DTE at a strike above the current price.
3. **Ensure the long option's extrinsic value is minimal:** The less extrinsic value in the long option, the less time decay works against you. Deep ITM options have mostly intrinsic value.
4. **Verify the debit is less than the width between strikes:** This ensures a positive max profit potential.
5. **Expiration gap:** The long option should have at least 3-4x more DTE than the short option. Example: short at 30 DTE, long at 120+ DTE.

### Exit and Rolling

The diagonal spread is inherently a rolling strategy — the short leg is rolled repeatedly as the income engine. See [[trade-repair-and-rolling]] for the complete rolling framework.

1. **Roll the short option:** As each front-month cycle expires or reaches 75% profit, sell a new short call in the next 30-45 DTE cycle. This repeatable process is the income engine.
2. **Close the entire position:** If the underlying drops significantly and the directional thesis is broken, close both legs.
3. **Short option threatened:** If the underlying rallies above the short call strike, either roll the short call up and out for a credit, or close the spread and capture the net profit. Aim to roll for a net credit or small net debit — never add significant debit to chase a rallying stock.
4. **Profit target for the spread:** If the underlying has rallied substantially and both options are deep ITM, close the entire diagonal to lock in gains.
5. **The 21-DTE consideration:** The short leg carries [[gamma-risk]] near expiration. Rolling or closing the short call at ~21 DTE avoids the zone where small price moves cause outsized delta shifts. Since the long leg has months of remaining life, its gamma is low and stable — the risk is concentrated in the short leg.

### Position Sizing
The total risk is the net debit paid for the diagonal. Size so this amount represents no more than 5-10% of the account. The PMCC is more capital-efficient than a covered call (which requires full stock purchase), so it naturally allows broader diversification.

## Payoff Profile
- **Max profit:** Reached when the underlying is at the short call strike at front-month expiration. The short call expires worthless while the long call has maximum combined intrinsic + remaining extrinsic value.
- **Max loss:** The net debit paid for the spread. Occurs if the underlying drops significantly and both options lose value.
- **Break-even:** Approximately the long option's strike + net debit paid (adjusted for remaining extrinsic value).
- **Ongoing income:** Each time the short call is rolled, additional credit is collected, reducing the effective cost basis.

## Example Trade
**Asset:** AAPL trading at $200. You are bullish over the next 6 months.
1. **Buy 1 AAPL $175 call** (0.80 delta, 180 DTE) at $32.00.
2. **Sell 1 AAPL $210 call** (0.25 delta, 35 DTE) at $3.50.
3. **Net debit:** $32.00 - $3.50 = **$28.50** ($2,850 per diagonal) vs. $20,000 to buy 100 shares.
4. AAPL drifts to $205 in 30 days. The short $210 call is worth $1.00 (decayed from $3.50). Buy it back for $1.00, locking in $2.50 profit on the short leg.
5. Sell a **new $215 call** (35 DTE) for $3.00. The cost basis is now $28.50 - $2.50 - $3.00 = **$23.00**.
6. After 4-5 rolling cycles collecting $2-3 each, the effective cost basis drops significantly, and any further appreciation in the long call is pure profit.
7. **Capital efficiency:** $2,850 controls $20,000 worth of directional exposure with recurring income.

## Advantages
- **Capital efficient:** The deep ITM long option costs a fraction of owning the stock, freeing up capital for diversification
- **Recurring income:** Each short-option cycle generates premium that reduces the cost basis over time
- **Directional with income:** Combines bullish (or bearish) exposure with [[theta]] decay harvesting
- **Flexible rolling:** The short leg can be adjusted in strike and expiration each cycle to adapt to market conditions
- **Lower break-even than stock:** The accumulated short-call credits lower the effective purchase price

## Disadvantages
- **Long option loses time value:** Although deep ITM, the long option still has some extrinsic value that decays -- especially if held for many months
- **Risk of being "called away":** If the underlying rallies sharply above the short strike, the short call may be assigned, requiring early closure or rolling
- **Requires active management:** Each 30-45 day cycle requires rolling the short option -- this is not a passive strategy
- **Downside risk is the full debit:** If the underlying crashes, the long option can lose most of its value despite being deep ITM
- **IV sensitivity:** A drop in [[implied-volatility]] hurts the long option's remaining extrinsic value, though it helps the short leg (Source: [[book-option-volatility-and-pricing]])

## See Also
- [[trade-repair-and-rolling]] — the complete rolling and adjustment framework
- [[gamma-risk]] — risk on the short leg near expiration (21-DTE rule)
- [[calendar-spread]] — same-strike version of the diagonal; purely a time-decay play without directional bias
- [[covered-call]] — the strategy the PMCC replicates, but requires stock ownership
- [[risk-reversal]] — another capital-efficient directional strategy using options
- [[butterfly-spread]] — a non-directional alternative for range-bound expectations
- [[theta]] — the primary income mechanism when rolling short calls repeatedly
- [[double-diagonal]] — a variation combining two diagonal spreads for broader range coverage

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg explains the interplay of delta, theta, and vega across different expirations that makes diagonal spreads work, including the IV sensitivity dynamics of the long vs. short legs
