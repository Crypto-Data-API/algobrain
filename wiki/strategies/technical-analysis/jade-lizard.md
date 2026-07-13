---
title: "Jade Lizard"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, jade-lizard, premium-selling, neutral, slightly-bullish, defined-risk-upside, advanced]
aliases: ["Jade Lizard Spread"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[iron-condor]]", "[[straddle-strangle]]", "[[covered-call]]", "[[risk-reversal]]", "[[implied-volatility]]", "[[theta]]", "[[delta]]"]
---

# Jade Lizard

## Overview

The Jade Lizard is a **three-leg, premium-selling** options strategy that combines a **short put** with a **short call spread** (short OTM call + long further OTM call). When structured correctly, the total premium collected from all three legs exceeds the width of the call spread, which means there is **no risk to the upside**. The only risk is to the downside, similar to a short put, if the underlying drops below the short put strike minus the total credit received.

The Jade Lizard is **neutral to slightly bullish** in bias. It collects premium from both sides of the market -- the short put benefits from a stable or rising price, and the short call spread benefits from the price staying below the short call. The key structural advantage over a [[straddle-strangle|short strangle]] is the elimination of unlimited upside risk. The trade is popular among premium sellers who want broader exposure to [[theta]] decay while capping one side of their risk. The name "Jade Lizard" was popularized by the tastytrade community.

## Rules / Setup

### Entry
1. **Sell 1 OTM put:** Choose a strike at approximately 0.20-0.30 [[delta]] below the current price. This is the primary risk leg.
2. **Sell 1 OTM call:** Choose a strike at approximately 0.15-0.25 delta above the current price.
3. **Buy 1 further OTM call:** Buy a call 1-3 strikes above the short call to cap upside risk.
4. **Critical rule:** Ensure the **total credit received exceeds the width of the call spread**. Example: if the call spread is $5 wide, the combined credit from all three legs must be greater than $5.00. This eliminates upside risk entirely.
5. **Expiration:** 30-45 DTE for optimal [[theta]] decay characteristics.
6. **IV environment:** Enter when [[implied-volatility]] is elevated (IV rank > 30) to maximize the premium collected.

### Exit
1. **Profit target:** Close the entire position at 50% of max profit. This usually means buying back all three legs when the total cost is half the original credit.
2. **Downside management:** If the short put is breached, manage as you would any naked [[put-option]]: roll down and out for a credit, or close for a loss.
3. **Upside management:** If the price rallies above the short call, the call spread caps the loss. Since total credit > call spread width, there is no net loss on the upside.
4. **Time-based exit:** Close with 7-10 DTE remaining to avoid [[gamma]] acceleration risk.

### Position Sizing
The max risk is on the downside: short put strike x 100 minus total credit received. Size so this worst-case scenario represents no more than 3-5% of the account. In practice, the risk is comparable to selling a cash-secured put.

## Payoff Profile
- **Max profit:** Total credit received. Occurs when the underlying is between the short put and short call strikes at expiration.
- **Max loss (downside):** Short put strike x 100 minus total credit received. Occurs if the underlying goes to zero.
- **Max loss (upside):** Zero or net profit, if structured correctly (total credit > call spread width).
- **Break-even:** Short put strike minus total credit received.

## Example Trade
**Asset:** AMZN trading at $190, 35 DTE, IV rank at 42.
1. **Sell 1 AMZN $180 put** (0.25 delta) for $3.20.
2. **Sell 1 AMZN $200 call** (0.20 delta) for $2.60.
3. **Buy 1 AMZN $205 call** for $1.50.
4. **Total credit:** $3.20 + $2.60 - $1.50 = **$4.30** ($430 per Jade Lizard).
5. **Call spread width:** $5.00. Since total credit ($4.30) is **less than** $5.00, there is slight upside risk of $0.70. To eliminate upside risk entirely, widen the put or tighten the call spread until credit > $5.00.
6. **Revised example -- sell the $182 put** for $3.80: Total credit = $3.80 + $2.60 - $1.50 = **$4.90**. Still less than $5. Consider selling the $183 put for $4.10: credit = $5.20 > $5.00. **No upside risk.**
7. **Break-even (downside):** $183 - $5.20 = **$177.80**.
8. AMZN stays at $188 for 30 days. All options decay. Close for $1.50 total. **Profit: $3.70** ($370, 71% of max).

## Advantages
- **No upside risk (when structured correctly):** The total credit exceeds the call spread width, making a rally harmless
- **Collects premium from both sides:** More premium than a simple [[credit-spread]] or naked put alone
- **Benefits from [[theta]] decay:** Three short legs (net) means aggressive time decay in the trader's favor
- **Flexible:** Can adjust strikes and widths to fine-tune the directional bias and credit
- **Defined upside risk:** Even if not perfectly structured, the call spread caps the maximum upside exposure

## Disadvantages
- **Unlimited downside risk:** The short put has the same risk as a [[covered-call|cash-secured put]] -- substantial loss if the underlying collapses
- **Margin intensive:** The naked short put requires significant buying power
- **Requires precise structuring:** Must verify that total credit exceeds call spread width to achieve the "no upside risk" condition
- **Three legs increase execution complexity:** Wider bid-ask slippage across three options
- **Not ideal in strong downtrends:** A falling market attacks the most exposed leg (the short put)

## See Also
- [[iron-condor]] -- defined risk on both sides, but lower premium collected
- [[straddle-strangle]] -- selling strangles has unlimited risk on both sides; Jade Lizard caps one side
- [[risk-reversal]] -- similar three-leg structure with a different risk profile
- [[covered-call]] -- simpler premium-selling strategy for bullish stock owners
- [[theta]] -- the primary profit engine for Jade Lizard trades
