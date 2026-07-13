---
title: "Broken Wing Butterfly"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, broken-wing-butterfly, directional, credit, defined-risk, asymmetric, advanced]
aliases: ["BWB", "Skip-Strike Butterfly", "Unbalanced Butterfly"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[butterfly-spread]]", "[[iron-butterfly]]", "[[ratio-spread]]", "[[iron-condor]]", "[[implied-volatility]]", "[[theta]]", "[[delta]]"]
---

# Broken Wing Butterfly

## Overview

The Broken Wing Butterfly (BWB) is an **asymmetric variation** of the standard [[butterfly-spread]] in which one wing is wider than the other. By skipping a strike on one side, the trader creates a directional butterfly that can be entered for a **net credit** or at zero cost, eliminating risk on the wider side entirely. The trade retains the butterfly's narrow profit zone but shifts it directionally and removes the risk of loss if the underlying moves against the wider wing.

The BWB is a popular variant among advanced options traders because it combines the best features of a [[butterfly-spread]] (defined risk, favorable reward-to-risk) with a directional lean and premium collection. A **put BWB** is commonly used as a bullish-to-neutral trade: the wider wing is below the current price, where there is no risk, and max profit occurs at the center strike. A **call BWB** is bearish-to-neutral. The strategy can be thought of as a [[ratio-spread]] with a protective long option added on the exposed side -- converting undefined risk into defined risk while often preserving the credit entry.

## Rules / Setup

### Entry
1. **Put BWB (bullish/neutral):** Buy 1 higher-strike put, sell 2 middle-strike puts, buy 1 lower-strike put -- but make the lower wing **wider** than the upper wing. Example: buy $105 put, sell 2x $100 puts, buy $90 put (upper wing = $5, lower wing = $10).
2. **Call BWB (bearish/neutral):** Buy 1 lower-strike call, sell 2 middle-strike calls, buy 1 higher-strike call with a wider upper wing.
3. **Credit entry:** The wider wing is cheaper to buy than a standard butterfly's equidistant wing, so the overall position can be entered for a net credit or zero cost.
4. **No risk on the wide side:** If total credit received >= width of the narrow wing minus width to the wider wing difference, there is zero loss if the price goes through the wider wing.
5. **Expiration:** 30-45 DTE for optimal theta characteristics.
6. **IV environment:** Elevated [[implied-volatility]] helps generate a larger credit.

### Exit
1. **Profit target:** Close at 50-75% of max profit if the underlying is near the center strike.
2. **Narrow wing risk:** If the underlying moves toward the narrow wing, the position behaves like a standard butterfly wing -- losses are capped at (narrow wing width - credit received).
3. **Wide wing (safe) side:** If the price moves toward the wide wing, the position reaches zero loss or locks in the credit. No action needed.
4. **Time management:** The profit zone expands as expiration approaches (theta works for you near the center strike). Hold if price is near center; close early if price is at the narrow wing.

### Position Sizing
Max loss = narrow wing width - net credit received. This is the only side at risk. Size so this max loss represents 2-4% of the account.

## Payoff Profile
- **Max profit:** Occurs at the center (short) strike at expiration. Equals the narrow wing width minus debit (or plus credit) on that side.
- **Max loss (narrow wing):** Narrow wing width minus credit received. This is the only at-risk side.
- **Max loss (wide wing):** Zero (or a small profit equal to the credit received). The wider wing eliminates risk on that side.
- **Break-even:** Center strike minus max profit (for a put BWB), adjusted for credit/debit.

## Example Trade
**Asset:** SPY trading at $510. You are neutral to slightly bullish and expect SPY to stay above $500.
1. **Buy 1 SPY $510 put** at $8.00.
2. **Sell 2 SPY $500 puts** at $4.50 each ($9.00 total credit).
3. **Buy 1 SPY $480 put** at $1.50.
4. **Net credit:** $9.00 - $8.00 - $1.50 = **-$0.50** (small debit). Let's adjust: use $485 put at $2.00. Net = $9.00 - $8.00 - $2.00 = **-$1.00** debit. Or sell the $502 puts: credit = $9.50. Net credit = $9.50 - $8.00 - $1.50 = **$0.00** (zero cost).
5. **Simplified example at zero cost:** Upper wing ($510-$500) = $10 wide. Lower wing ($500-$480) = $20 wide.
6. **Max profit at $500:** The $510 put is worth $10, the two $500 puts are worthless, the $480 put is worthless. Profit = $10.00 ($1,000).
7. **If SPY drops to $480 or below:** The structure collapses to the value of the wide wing difference: $510 put - 2x$500 puts + $480 put = $10 - $0 + $0 = net loss is limited. With the wider lower wing, the max loss below $480 is = ($10 - $20) + credit = -$10 + $0 = $10 loss. Max loss on the wide side = $1,000.
8. **If SPY stays above $510:** All puts expire worthless. P&L = net credit ($0 in this case).
9. **The key tradeoff:** Risk on the downside (wide wing) in exchange for higher potential profit at the center.

## Advantages
- **Directional lean with defined risk:** The asymmetric wings create a built-in directional bias
- **Credit or zero-cost entry:** The wider wing is cheap, allowing favorable entry pricing
- **Eliminates one side of risk:** No loss on the wider wing side makes the trade simpler to manage
- **Higher probability than standard butterfly:** The directional shift means the profitable zone is skewed toward the expected price range
- **Flexible structure:** Wing widths, strikes, and ratios can all be customized for specific market views

## Disadvantages
- **Risk on the narrow wing:** While one side is protected, the other side carries meaningful risk if the underlying moves against the position
- **Lower max profit than a standard butterfly:** The asymmetric structure and credit entry reduce the max potential compared to an equidistant butterfly
- **Complex execution:** Three legs at non-standard strike intervals make the trade harder to execute with tight fills
- **Difficult to model:** The payoff diagram is asymmetric and can be confusing; careful strike selection is required
- **Pin risk near expiration:** The two short options at the center strike create assignment risk with American-style options

## See Also
- [[butterfly-spread]] -- the standard equidistant version of the butterfly
- [[iron-butterfly]] -- credit butterfly with puts and calls at the ATM strike
- [[ratio-spread]] -- similar concept without the protective wing (undefined risk)
- [[christmas-tree-spread]] -- another asymmetric multi-leg structure with directional bias
