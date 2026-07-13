---
title: "Risk Reversal"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, risk-reversal, directional, synthetic, leverage, hedging, skew]
aliases: ["Combo", "Synthetic Forward", "Collar Without Stock"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks, forex]
complexity: intermediate
backtest_status: untested
related: ["[[covered-call]]", "[[jade-lizard]]", "[[straddle-strangle]]", "[[diagonal-spread]]", "[[implied-volatility]]", "[[delta]]", "[[vega]]"]
---

# Risk Reversal

## Overview

A Risk Reversal is a two-leg options strategy that combines a **long OTM call** with a **short OTM put** (bullish risk reversal), or a **long OTM put** with a **short OTM call** (bearish risk reversal). The premium collected from the short option partially or fully finances the long option, often resulting in a **zero-cost or very low-cost** entry. The resulting position behaves like a synthetic forward -- it has strong directional exposure with significant leverage but no upfront capital outlay.

Risk reversals are heavily used in **forex markets** for corporate hedging and by institutional traders to express [[volatility]] skew views. In equity markets, a bullish risk reversal is economically similar to owning the stock (or a [[covered-call]] without the stock) -- you participate in upside moves and are exposed to downside risk from the short put. The strategy is a pure directional bet with leveraged exposure. It is attractive when [[implied-volatility]] skew makes puts expensive relative to calls (or vice versa), as the trader sells the overpriced side and buys the underpriced side.

## Rules / Setup

### Entry
1. **Bullish risk reversal:** Sell 1 OTM put (e.g., 0.20-0.30 delta) and buy 1 OTM call (e.g., 0.20-0.30 delta). Same expiration.
2. **Bearish risk reversal:** Sell 1 OTM call and buy 1 OTM put. Same expiration.
3. **Strike selection:** Choose strikes equidistant from the current price, or skew them based on your directional conviction. Wider strikes = less premium but wider dead zone.
4. **Net cost:** Aim for zero or near-zero cost. If put skew is steep (puts more expensive), a bullish risk reversal may generate a small credit. In equity markets, puts typically carry higher IV than equidistant calls, which favors bullish risk reversals.
5. **Expiration:** 45-90 DTE for swing trades; 6-12 months for longer-term directional bets or hedges.

### Exit
1. **Profit target:** Close when the long option has doubled or tripled in value, or when the directional thesis is achieved.
2. **Stop-loss (downside for bullish):** If the underlying drops through the short put strike, manage the position: close for a loss, roll the put down and out, or accept assignment (if using the strategy as a cash-secured stock entry).
3. **Breakeven zone management:** Between the two strikes, both options are OTM and the position has little value. Avoid exiting in this dead zone unless the thesis has changed.
4. **IV management:** A drop in IV hurts the long option but helps the short option. The net effect depends on which leg has more vega exposure.

### Position Sizing
The short put creates substantial downside risk (strike x 100 minus credit). Size as you would a cash-secured put -- ensure you have the capital or willingness to take assignment. Never allocate more than 5-10% of the account to a single risk reversal.

## Payoff Profile
- **Max profit (bullish):** Unlimited to the upside. The long call appreciates dollar-for-dollar with the underlying above its strike.
- **Max loss (bullish):** Short put strike x 100 minus any net credit. The loss profile is identical to being long the stock below the put strike.
- **Break-even:** Depends on net credit/debit. For a zero-cost entry, approximately at the current stock price (between the two strikes).
- **Dead zone:** Between the two strikes, the position has near-zero P&L. Both options expire worthless and the trade is flat.

## Example Trade
**Asset:** GOOGL trading at $170, 60 DTE, put IV skew makes the put slightly more expensive than the call.
1. **Sell 1 GOOGL $160 put** (0.25 delta) for $4.20.
2. **Buy 1 GOOGL $180 call** (0.25 delta) for $3.80.
3. **Net credit:** $4.20 - $3.80 = **$0.40** ($40 per risk reversal).
4. **Bullish scenario:** GOOGL rallies to $195. The $180 call is worth ~$16, the $160 put is worthless. Profit: $16.00 + $0.40 = **$16.40** ($1,640 on near-zero capital).
5. **Bearish scenario:** GOOGL drops to $150. The $180 call is worthless, the $160 put is worth ~$10. Loss: $10.00 - $0.40 = **$9.60** ($960).
6. **Neutral scenario:** GOOGL stays at $170. Both options expire worthless. Profit: **$0.40** ($40 -- the initial credit).

## Advantages
- **Zero or low cost:** The short option finances the long option, requiring minimal upfront capital
- **Unlimited profit potential:** The long option provides theoretically unlimited gains in the directional leg
- **Exploits volatility skew:** Sells the overpriced side of the skew and buys the underpriced side
- **Leveraged directional exposure:** Participates in large moves without owning the underlying asset
- **Versatile hedging tool:** Widely used in [[forex]] for corporate currency hedging and in equities as a synthetic stock substitute

## Disadvantages
- **Substantial downside risk:** The short option creates a loss profile similar to stock ownership on the wrong side
- **Margin intensive:** The naked short option requires significant buying power
- **Dead zone between strikes:** If the price stays between the strikes, the trade expires flat despite capital being at risk
- **Directional dependency:** Requires a strong view on direction; range-bound markets produce no returns
- **Assignment risk:** The short option (especially a put approaching ITM) can be assigned early, requiring capital to take delivery

## See Also
- [[covered-call]] -- similar risk profile to a bullish risk reversal but requires stock ownership
- [[jade-lizard]] -- adds a call spread to a short put, capping upside risk
- [[straddle-strangle]] -- non-directional volatility strategies vs. the risk reversal's directional nature
- [[diagonal-spread]] -- another leveraged directional strategy using time spread mechanics
- [[seagull-option]] -- extends the risk reversal concept with a third leg to reduce cost further
