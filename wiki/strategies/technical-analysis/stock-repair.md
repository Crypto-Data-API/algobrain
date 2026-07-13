---
title: "Stock Repair Strategy"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [options, stock-repair, recovery, covered-ratio-spread, equity-options, cost-reduction]
strategy_type: quantitative
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[covered-call]]", "[[collar]]", "[[bull-call-spread]]", "[[ratio-spread]]", "[[vertical-spreads]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[wheel-strategy]]"]
---

# Stock Repair Strategy

## Overview

The Stock Repair Strategy is a covered ratio spread designed to **lower the break-even point** on an underwater stock position without committing additional capital. The trader holds 100 shares of a stock that has declined, then overlays a 1x2 call spread: buy 1 ATM call and sell 2 OTM calls at the original purchase price (or near it). The net cost is approximately zero because the premium from the two sold calls finances the purchased call. If the stock recovers to the short call strike, the position breaks even at a price well below the original entry. The trade-off is that upside above the short calls is completely capped.

## Setup

1. **Hold 100 shares** of the underlying that is currently trading below your purchase price.
2. **Buy 1 ATM call** at the strike nearest the current (reduced) stock price.
3. **Sell 2 OTM calls** at a strike near your original purchase price (the break-even target).
4. The premium from the 2 sold calls should roughly equal the cost of the 1 bought call, making the overlay **zero cost**.
5. All options share the **same expiration** -- 60-90 DTE to give the stock time to recover.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock recovers to short call strike | Position breaks even (or profits) at a lower price than the original entry |
| Stock rises above short call strike | Gains are capped; one naked short call offsets the long call, shares called away at strike |
| Stock stays flat or declines further | Options expire worthless; loss remains on the stock position only |

**New break-even** = approximately midway between the current price and the original entry. **Max profit** = capped at the short call strike. **Max additional loss from the overlay** = zero (net zero cost at entry).

## Position in the Recovery Toolkit

The stock repair strategy is one of several options for managing underwater stock positions. See [[trade-repair-and-rolling]] for the complete recovery framework. The decision between repair strategies depends on the trader's outlook:

| Situation | Best Approach |
|-----------|---------------|
| Expect partial recovery, willing to cap upside | **Stock repair** (this strategy) |
| Thesis intact, need more time | [[trade-repair-and-rolling|Rolling]] the position |
| Want downside protection, keep upside | [[protective-puts]] or [[collar]] |
| Want income while waiting for recovery | [[covered-call]] writing at cost basis |
| Thesis is broken | Close the position and accept the loss |

The stock repair strategy is particularly useful for [[wheel-strategy|wheel]] traders who have been assigned on a put and find themselves deep underwater — it offers a zero-cost path to a lower breakeven without the slow grind of selling far-OTM covered calls for small premiums.

## When to Use

- You hold a stock that has **dropped significantly** and you want to lower your break-even without adding capital.
- You believe the stock will **partially recover** but may not return to your original purchase price soon.
- You are willing to **cap any upside** above the short call strike in exchange for a faster path to break-even.
- You prefer a zero-cost adjustment over dollar-cost averaging or adding to a losing position.

## Advantages
- Zero or near-zero cost to implement -- no additional capital required
- Lowers the effective break-even price, making recovery achievable with a smaller rebound
- Simple concept once the ratio structure is understood
- Eliminates the psychological trap of waiting for a full recovery to the original price

## Disadvantages
- Upside is strictly capped at the short call strike -- if the stock rallies past it, you miss all further gains
- If the stock continues to decline, the overlay does nothing to reduce the loss on the shares
- The 2 sold calls create a 1:1 covered call plus 1 naked short call -- the naked leg requires margin
- Only works for partial recoveries; a stock that never rebounds renders the strategy moot
- Rolling or managing the position at expiration adds complexity

## See Also
- [[trade-repair-and-rolling]] — the complete recovery and adjustment framework
- [[gamma-risk]] — risk consideration for the short calls near expiration
- [[covered-call]] — the simpler one-call version of selling premium against shares
- [[collar]] — an alternative hedge that caps downside instead of lowering break-even
- [[wheel-strategy]] — common context where stock repair is needed (underwater assignment)
- [[ratio-spread]] — the general family of unequal-leg spread strategies
- [[bull-call-spread]] — the long call spread component embedded in the repair structure
