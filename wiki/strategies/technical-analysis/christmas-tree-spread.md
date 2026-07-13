---
title: "Christmas Tree Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, christmas-tree, ladder-spread, directional, low-cost, advanced, multi-leg]
aliases: ["Ladder Spread", "Christmas Tree", "Call Ladder", "Put Ladder"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[butterfly-spread]]", "[[broken-wing-butterfly]]", "[[ratio-spread]]", "[[backspread]]", "[[iron-condor]]", "[[implied-volatility]]", "[[delta]]"]
---

# Christmas Tree Spread

## Overview

The Christmas Tree Spread -- also called a **ladder spread** -- is a multi-leg options strategy that uses options at three (or more) different strikes in a ladder-like progression. The classic call christmas tree involves **buying 1 ATM call, selling 1 OTM call, and selling 1 further OTM call**, creating a low-cost directional bet that profits from a **moderate move** in the expected direction. The name comes from the visual appearance of the position on a risk graph: a peaked shape that narrows at the top, resembling a tree.

The strategy is a directional trade that combines elements of a [[ratio-spread]] and a [[broken-wing-butterfly]]. The first short option partially finances the long option, and the second short option further reduces the cost (sometimes to zero). The tradeoff is that the two short options create risk beyond the upper strike -- if the underlying moves too far, the position transitions from profitable to losing. The christmas tree profits from a moderate, controlled move to the first short strike zone. It is popular among traders who have a specific price target and want to express that view at minimal cost.

## Rules / Setup

### Entry
1. **Call christmas tree (bullish):** Buy 1 ATM call, sell 1 OTM call (e.g., $5-10 above ATM), sell 1 further OTM call (e.g., $10-20 above ATM). All same expiration.
2. **Put christmas tree (bearish):** Buy 1 ATM put, sell 1 OTM put, sell 1 further OTM put.
3. **Equal spacing is not required:** The strikes can be at any intervals, but equal spacing is most common for simplicity.
4. **Net cost:** The trade should be entered for a small net debit or zero cost. The two short options should largely finance the long option.
5. **Expiration:** 30-60 DTE. Enough time for the directional move to occur.
6. **IV environment:** Works best when [[implied-volatility]] is moderate to high, making the short options more valuable and reducing the entry cost.

### Exit
1. **Profit target:** Close at 50-75% of max profit when the underlying is near the first short strike.
2. **Stop-loss:** Close if the underlying blows through the second short strike with momentum. Beyond this point, losses begin accelerating.
3. **If the underlying does not move:** The position loses the small debit paid as all options expire worthless. Accept the loss.
4. **Rolling:** If the move is taking longer than expected, consider rolling the entire structure out in time.

### Position Sizing
Max risk on the downside = net debit paid (small). Max risk on the upside (beyond the outer strikes) = potentially significant, depending on how far beyond the position extends. Size conservatively: 1-3% of the account.

## Payoff Profile
- **Max profit:** Occurs when the underlying is at the **first short strike** at expiration. Equals (first short strike - long strike) minus net debit.
- **Max loss (downside):** The net debit paid. Occurs if the underlying does not move and all options expire worthless.
- **Max loss (upside/beyond):** Increases beyond the second short strike. The position has one uncovered short option past the outer strike, creating loss potential similar to a naked short option.
- **Break-even (lower):** Long strike + net debit paid.
- **Break-even (upper):** Depends on the structure; approximately the second short strike + max profit.

## Example Trade
**Asset:** AMZN trading at $190, 40 DTE. You expect a rally to approximately $200 but not beyond $210.
1. **Buy 1 AMZN $190 call** at $7.50.
2. **Sell 1 AMZN $200 call** at $3.50.
3. **Sell 1 AMZN $210 call** at $1.50.
4. **Net debit:** $7.50 - $3.50 - $1.50 = **$2.50** ($250 per christmas tree).
5. **Max profit at $200:** The $190 call is worth $10, the $200 call is worthless, the $210 call is worthless. Profit = $10.00 - $2.50 = **$7.50** ($750).
6. **At $210:** The $190 call is worth $20, the $200 call is worth $10 (loss), the $210 call is worthless. P&L = $20 - $10 - $2.50 = **$7.50** ($750). Still max profit range.
7. **At $220:** The $190 call is worth $30, the $200 call is worth $20 (loss), the $210 call is worth $10 (loss). P&L = $30 - $20 - $10 - $2.50 = **-$2.50** ($-250). Back to break-even.
8. **Above $220:** Losses increase $1 for $1 due to the uncovered short call.
9. **Below $190:** All expire worthless. Loss = **$2.50** ($250, the net debit).

## Advantages
- **Low cost entry:** The two short options substantially reduce or eliminate the cost of the long option
- **Defined downside risk:** If the underlying does not move, the loss is limited to the small net debit
- **Profits from moderate moves:** Ideal for traders with a specific price target zone rather than an open-ended directional view
- **Wide profit zone:** Between the first and second short strikes, the trade is at or near max profit
- **Flexible construction:** Strikes can be spaced to match specific chart levels, [[support-resistance-breakout|support/resistance]] zones, or expected move calculations

## Disadvantages
- **Unlimited risk beyond the outer strike:** The uncovered short option creates escalating losses if the underlying overshoots
- **Narrow optimal outcome:** Max profit requires the move to stop in a specific range
- **Complex execution:** Three legs with potentially wide bid-ask spreads make clean fills difficult
- **Requires active management:** The uncovered short leg demands monitoring; a runaway move must be closed quickly

## See Also
- [[butterfly-spread]] -- similar profit-at-a-target concept but with defined risk on both sides
- [[broken-wing-butterfly]] -- another asymmetric multi-leg structure with directional bias
- [[ratio-spread]] -- the christmas tree is essentially a ratio spread with an additional short leg
- [[backspread]] -- the opposite approach: profits from big moves, not moderate ones
