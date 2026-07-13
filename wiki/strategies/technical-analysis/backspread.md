---
title: "Backspread"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, backspread, long-volatility, unlimited-profit, directional, asymmetric, advanced]
aliases: ["Call Backspread", "Put Backspread", "Reverse Ratio Spread"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, crypto]
complexity: advanced
backtest_status: untested
related: ["[[ratio-spread]]", "[[straddle-strangle]]", "[[butterfly-spread]]", "[[risk-reversal]]", "[[implied-volatility]]", "[[gamma]]", "[[vega]]"]
---

# Backspread

## Overview

A Backspread (also called a reverse ratio spread) is the **mirror image of a [[ratio-spread]]**. It involves selling fewer near-the-money options and buying more far-OTM options, creating a position with **unlimited profit potential** on the long side and **limited risk**. The classic call backspread sells 1 ATM call and buys 2 OTM calls; the put backspread sells 1 ATM put and buys 2 OTM puts. The premium from the short option partially finances the long options, often resulting in a small net debit or even a credit.

Backspreads are **long-[[volatility]]** strategies that profit from **big moves** in the directional leg. They are structurally the opposite of ratio spreads: where ratio spreads want calm, moderate moves, backspreads want explosive price action. The trade is net long [[vega]] and net long [[gamma]], meaning it benefits from rising [[implied-volatility]] and accelerating price movement. The worst outcome is a moderate move to the short strike at expiration, where the maximum loss occurs. Backspreads are popular in crypto markets and ahead of binary events where tail moves are underpriced.

## Rules / Setup

### Entry
1. **Call backspread (bullish):** Sell 1 ATM or slightly ITM call. Buy 2 (or more) OTM calls at a higher strike. Example: sell 1 $100 call, buy 2 $110 calls.
2. **Put backspread (bearish):** Sell 1 ATM or slightly ITM put. Buy 2 (or more) OTM puts at a lower strike.
3. **Ratio:** 1:2 is standard. 1:3 provides more upside leverage but costs more.
4. **Net cost:** Aim for zero cost or a small debit. If entered for a credit, the trade also profits if the underlying moves sharply against the directional leg (both sides profitable in extreme moves).
5. **Expiration:** 30-60 DTE minimum. The long options need time to be profitable; shorter expirations are hurt by [[theta]] decay on the extra long legs.
6. **IV environment:** Enter when [[implied-volatility]] is low and expected to rise. The net long vega position profits from IV expansion.

### Exit
1. **Big move in the right direction:** Let the position run if the underlying is moving strongly past the long strikes. The 2:1 ratio means profits accelerate as the price moves further.
2. **Moderate move to short strike (worst case):** Close the position if the underlying approaches the short strike with expiration near. This is the maximum loss zone.
3. **IV spike:** A sharp increase in IV can make the position profitable even before the underlying has moved much. Consider taking profit on the IV expansion.
4. **Time management:** If the move has not materialized with less than 14 DTE, consider closing. Theta decay on the extra long options accelerates in the final weeks.

### Position Sizing
Max loss occurs at the long strike at expiration = (short strike - long strike) x contract multiplier + net debit. Size so this worst case represents 2-4% of the account. The unlimited profit potential provides excellent asymmetry.

## Payoff Profile
- **Max profit (call backspread):** Unlimited to the upside. Above the upper break-even, profit increases dollar-for-dollar for each additional long contract.
- **Max loss:** Occurs when the underlying is exactly at the long option strike at expiration. Loss = (difference between strikes) minus net credit (or plus net debit).
- **Break-even (upper, call backspread):** Long strike + (max loss / number of extra long contracts).
- **Break-even (lower, if credit entry):** Short strike minus net credit. Below this, the position profits from the credit received.
- **Greeks:** Net long [[gamma]], net long [[vega]], net negative [[theta]]. The position accelerates in profit as the underlying moves and benefits from IV increases.

## Example Trade
**Asset:** TSLA trading at $250, 45 DTE. You expect a major move higher but want limited downside.
1. **Sell 1 TSLA $250 call** at $14.00.
2. **Buy 2 TSLA $270 calls** at $7.00 each ($14.00 total).
3. **Net cost:** $14.00 - $14.00 = **$0.00** (zero cost entry).
4. **Max loss:** At $270 at expiration. The short $250 call is worth $20, the two $270 calls are worthless. Loss = **$20.00** ($2,000).
5. **Upper break-even:** $270 + $20 = **$290**.
6. **Scenario A -- big move up:** TSLA rallies to $320. Short $250 call worth $70 (loss: $56). Two $270 calls worth $50 each = $100 (gain: $86). **Net profit: $30.00** ($3,000).
7. **Scenario B -- stays flat:** TSLA stays at $250. All options expire worthless. **P&L: $0** (zero cost entry).
8. **Scenario C -- drops:** TSLA falls to $220. All options expire worthless. **P&L: $0** (zero cost entry).
9. The backspread only loses money in the narrow range between $250-$290, with max loss at $270.

## Advantages
- **Unlimited profit potential:** The extra long options provide uncapped gains on big directional moves
- **Limited and defined risk:** Max loss is known at entry and occurs only at one specific price at expiration
- **Low or zero cost:** The short option finances the long options, often eliminating upfront cost
- **Benefits from volatility expansion:** Net long [[vega]] means rising IV increases the position's value
- **Asymmetric payoff:** Risk is limited but reward is theoretically unlimited -- excellent risk/reward structure

## Disadvantages
- **The "valley of death":** Maximum loss occurs at the long strike at expiration -- a moderate move hits hardest
- **Theta decay on extra long options:** Two long options decay faster than the one short, bleeding value daily
- **Requires a large move:** The underlying must move significantly past the long strikes to profit
- **Low probability of max profit:** Big moves are rare; many backspreads expire near the loss zone

## See Also
- [[ratio-spread]] -- the opposite structure: sell more options than you buy (profits from small moves)
- [[straddle-strangle]] -- another long-volatility strategy, but non-directional
- [[butterfly-spread]] -- a defined-risk structure that also profits from specific price targets
- [[gamma-scalping]] -- another approach to profiting from large moves using long gamma
