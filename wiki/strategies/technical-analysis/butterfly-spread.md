---
title: "Butterfly Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [options, butterfly, defined-risk, neutral, low-volatility, low-cost, directional]
aliases: ["Long Butterfly", "Call Butterfly", "Put Butterfly"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, crypto]
complexity: intermediate
backtest_status: untested
related: ["[[iron-condor]]", "[[iron-butterfly]]", "[[broken-wing-butterfly]]", "[[calendar-spread]]", "[[implied-volatility]]", "[[theta]]", "[[option-volatility-and-pricing]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]"]
---

# Butterfly Spread

## Overview

The Butterfly Spread is a **defined-risk, low-cost** options strategy that profits when the underlying asset finishes near a specific price at expiration. The classic call butterfly is constructed by buying 1 lower-strike call, selling 2 middle-strike calls, and buying 1 upper-strike call -- all at the same expiration. The middle strike is typically at-the-money or at the expected target price. The result is a position that costs very little to enter yet offers a favorable risk-to-reward ratio if the price pins near the center strike.

Butterflies are fundamentally a bet on **low realized [[volatility]]** (Source: [[book-option-volatility-and-pricing]]). The maximum profit occurs when the underlying lands exactly at the middle strike at expiration, and the position loses value as the price moves away in either direction. This makes the butterfly the mirror image of a [[straddle-strangle]] -- instead of paying for a big move, you are paying a small amount for a precise, quiet outcome. Variants include the **put butterfly** (same structure using puts), the **[[broken-wing-butterfly]]** (asymmetric wings), and the [[iron-butterfly]] (combination of puts and calls).

## Rules / Setup

### Entry
1. **Select the center strike:** Choose the price where you expect the underlying to settle at expiration. This is typically ATM or at a key [[support-resistance-breakout|support/resistance]] level.
2. **Build the spread:** Buy 1 call at the lower strike (e.g., $95), sell 2 calls at the center strike (e.g., $100), buy 1 call at the upper strike (e.g., $105). All strikes are equally spaced.
3. **Expiration:** 14-45 DTE. Shorter expirations offer more leverage but require higher precision on the pin.
4. **Cost:** The net debit should be a small fraction of the wing width. On a $5-wide butterfly, a $0.75-$1.50 debit is typical.
5. **IV environment:** Enter when [[implied-volatility]] is moderate to high (the butterfly is cheaper in relative terms when you expect IV to decline).

### Exit
1. **Profit target:** Close at 50-75% of max profit. Waiting for the perfect pin is unrealistic.
2. **Stop-loss:** Close if the underlying moves decisively beyond either wing strike with significant time remaining.
3. **Time management:** If price is near the center strike in the final week, hold — [[theta]] decay works aggressively in your favor. If price is away from center, close to salvage remaining value.

### Adjustments and Rolling

Butterflies are defined-risk structures (max loss = debit paid), so adjustments are less urgent than for unlimited-risk positions. However, active management can improve outcomes when the underlying moves away from the center strike. See [[trade-repair-and-rolling]] for the general adjustment framework.

**Rolling the center strike:** If the underlying drifts away from the original center strike early in the trade (with significant time remaining), the trader can close the current butterfly and open a new one centered at the current price. This "recenters" the profit zone. The cost is the debit to close the losing butterfly (which will be less than the original debit if caught early) plus the debit to open the new one.

**Converting to an [[iron-butterfly]]:** If a long call butterfly is tested on one side, the trader can add a put butterfly at the same center strike to create an iron butterfly. This increases the credit collected and widens the effective profit zone, at the cost of adding more capital.

**Adding or adjusting wings:** If the underlying moves beyond one wing, the trader can:
- Close the losing butterfly for a partial loss and redeploy into a new structure
- Buy a further OTM option on the threatened side to create a [[broken-wing-butterfly]], shifting the risk profile

**[[Gamma-risk]] near expiration:** Butterflies have concentrated gamma at the center strike, especially in the final week. The two short center-strike options create negative [[gamma]] that accelerates if the underlying is pinned near the center. While this benefits the trader (theta works aggressively), any last-minute move through the center strike can rapidly shift the P&L. For butterflies held into the final week, be prepared for volatile mark-to-market swings.

### Position Sizing
Risk the entire debit paid. Size so that a total loss represents no more than 1-3% of the account. The low cost per butterfly allows multiple contracts.

## Payoff Profile
- **Max profit:** Wing width minus debit paid, multiplied by 100. Occurs when the underlying is exactly at the center strike at expiration.
- **Max loss:** The net debit paid. Occurs when the underlying is at or beyond either wing strike at expiration.
- **Break-even points:** Lower strike + debit paid (downside); upper strike - debit paid (upside).
- **Greeks at entry:** Near-zero [[delta]], negative [[vega]], positive [[theta]] (when price is near center) (Source: [[book-option-volatility-and-pricing]]).

## Example Trade
**Asset:** AAPL trading at $200, 30 DTE, you expect price to stay near $200.
1. **Buy 1 AAPL $195 call** at $8.00.
2. **Sell 2 AAPL $200 calls** at $5.50 each ($11.00 total credit).
3. **Buy 1 AAPL $205 call** at $3.75.
4. **Net debit:** $8.00 + $3.75 - $11.00 = **$0.75** ($75 per butterfly).
5. **Max profit:** $5.00 - $0.75 = $4.25 ($425) if AAPL closes at exactly $200.
6. **Break-evens:** $195.75 and $204.25.
7. At expiration, AAPL closes at $201. The butterfly is worth approximately $4.00. Profit: $4.00 - $0.75 = **$3.25** ($325 per butterfly, +433% return on risk).

## Advantages
- **Low cost, high reward ratio:** Risk $0.75 to make $4.25 is a 5.7:1 reward-to-risk ratio
- **Defined risk:** Maximum loss is the small debit paid -- no margin calls, no surprises
- **Versatile targeting:** Can be centered at any price to express a specific directional view
- **Benefits from [[theta]] decay:** Time erosion helps the position as long as price stays near center
- **Multiple variants:** Put butterflies, [[broken-wing-butterfly|broken wings]], and [[iron-butterfly|iron butterflies]] adapt the structure for different market views

## Disadvantages
- **Narrow profit zone:** Price must finish close to the center strike for meaningful profit
- **Low probability of max profit:** The exact pin is unlikely; most butterflies are closed for partial profit or loss
- **Sensitive to realized [[volatility]]:** Any large move in either direction moves the position toward max loss
- **Execution costs:** Three legs (four options) mean wider bid-ask slippage, especially on less liquid names
- **Early expiration risk:** American-style options with short legs can be assigned early, complicating the position

## See Also
- [[trade-repair-and-rolling]] — rolling and adjustment framework for tested butterflies
- [[gamma-risk]] — risk concentration at the center strike, especially near expiration
- [[iron-butterfly]] — same payoff profile constructed with puts and calls for a credit entry
- [[broken-wing-butterfly]] — asymmetric variant that eliminates risk on one side
- [[iron-condor]] — wider profit zone but lower max profit; similar low-vol thesis
- [[calendar-spread]] — another low-volatility strategy that profits from time decay
- [[implied-volatility]] — understanding IV helps determine when butterflies are attractively priced

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg provides comprehensive analysis of butterfly spread construction, Greek profiles at entry, and the relationship between butterfly pricing and volatility expectations
