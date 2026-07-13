---
title: "Straddle & Strangle"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [options, volatility, straddle, strangle, earnings-play, event-driven, long-volatility]
aliases: ["Long Straddle", "Long Strangle", "Buying Volatility"]
strategy_type: technical
timeframe: day|swing
markets: [stocks, crypto]
complexity: intermediate
backtest_status: untested
related: ["[[iron-condor]]", "[[gamma-scalping]]", "[[volatility-arbitrage]]", "[[implied-volatility]]", "[[vega]]", "[[gamma]]", "[[option-volatility-and-pricing]]"]
---

# Straddle & Strangle

## Overview

Straddles and strangles are **long-volatility** strategies that profit from large price moves in either direction. A **straddle** involves buying a [[call-option]] and a [[put-option]] at the same [[strike-price]] and expiration. A **strangle** uses different strikes -- typically an OTM call and an OTM put -- making it cheaper but requiring a larger move to profit. Both strategies are directionally agnostic: the trader does not care which way the price moves, only that it moves *enough* to overcome the combined premium paid.

These strategies are most commonly deployed before known [[catalyst]]s -- [[earnings]] announcements, [[fomc]] decisions, FDA rulings, or major crypto protocol upgrades. The core bet is that the actual realized move will exceed what [[implied-volatility]] has priced in (Source: [[book-option-volatility-and-pricing]]). The danger is well-known: [[implied-volatility]] tends to be elevated before events, and the post-event [[iv-crush]] can destroy the position's value even if the underlying moves moderately.

## Rules

### Entry
1. **Straddle:** Buy 1 ATM call + 1 ATM put at the same strike and expiration. Choose the strike closest to the current price.
2. **Strangle:** Buy 1 OTM call (e.g., +5% above spot) + 1 OTM put (e.g., -5% below spot). Same expiration.
3. **Timing:** Enter 1-5 days before the expected catalyst. Entering too early bleeds [[theta]]; entering the day-of means IV is at its peak.
4. **IV assessment:** Compare current [[implied-volatility]] to the stock's average earnings move (available on options analytics platforms). Only enter if the expected move exceeds the straddle cost.
5. **Expiration:** Use the nearest expiration that captures the event. Weekly options are preferred for earnings plays to minimize extrinsic value.

### Exit
1. **Quick exit after event:** Close the position within 1-2 hours of the catalyst (e.g., morning after earnings). This avoids ongoing [[theta]] decay on the losing leg.
2. **Profit target:** Exit when the position reaches 50-100% profit. Do not get greedy waiting for a larger move.
3. **Stop-loss:** If the event produces a muted move and both legs lose value, close immediately. Do not hold hoping for a delayed reaction.
4. **Leg out cautiously:** If the move is strong in one direction, consider closing the profitable leg and holding the losing leg as a lottery ticket only if it has negligible remaining value.

### Position Sizing
Risk the entire premium paid. Size positions so that a total loss (both legs expire worthless) represents no more than 1-3% of the account.

## Indicators Used
- [[implied-volatility]] -- determines how expensive the straddle/strangle is; compare IV to historical realized vol
- [[vega]] -- measures sensitivity to IV changes; the position loses value if IV drops (IV crush)
- [[gamma]] -- high gamma near ATM means the position accelerates in profit as the underlying moves
- [[theta]] -- the daily cost of holding the position; the enemy of long options
- [[atr]] / historical move analysis -- compare the straddle price to the stock's average move on the catalyst day
- [[earnings-calendar]] / [[economic-calendar]] -- timing the catalyst

## Example Trade
**Asset:** NVDA trading at $800, reporting earnings after the close. Weekly options expire in 3 days.
1. **Buy 1 NVDA $800 call** at $28.00 and **Buy 1 NVDA $800 put** at $26.00. Total straddle cost: $54.00 ($5,400).
2. **Break-even points:** $800 + $54 = $854 on the upside; $800 - $54 = $746 on the downside. NVDA needs to move ~6.75% to break even.
3. **Scenario A -- big move:** NVDA reports blowout earnings and opens at $870. The $800 call is worth ~$72, the put is worth ~$0.50. Position value: $72.50. Profit: $72.50 - $54.00 = $18.50 ($1,850 per straddle, +34%).
4. **Scenario B -- muted move:** NVDA opens at $810. The call is worth ~$18, the put ~$3. Position value: $21. Loss: $54 - $21 = $33 ($3,300 per straddle, -61%). IV crush destroyed both legs.
5. **Result:** The strategy only works when the realized move exceeds the implied move.

## Performance Characteristics
- **Win Rate:** 30-45%. Most events produce moves smaller than implied, so the majority of straddles lose money.
- **Profit Factor:** Can exceed 2.0 if the trader is selective, entering only when historical analysis shows the straddle is cheap relative to typical moves.
- **Best Market Conditions:** High-impact events with uncertain outcomes. Stocks with a history of large earnings surprises. Crypto before major fork/upgrade events.
- **Worst Market Conditions:** Events where the outcome is widely anticipated. Low-volatility environments where premiums are thin but moves are still small.

## Advantages
- **Directionally agnostic:** Profits regardless of whether the move is up or down
- **Unlimited profit potential:** Gains are theoretically unlimited on the call side, substantial on the put side
- **High [[gamma]]:** The position accelerates in profit as the underlying moves further from the strike (Source: [[book-option-volatility-and-pricing]])
- **Simple thesis:** You only need to answer one question -- will the move be big enough?

## Disadvantages
- **Expensive:** Buying two options means paying double the premium and double the [[theta]] decay
- **[[iv-crush|IV crush]] risk:** [[implied-volatility]] collapses after events, destroying extrinsic value on both legs simultaneously
- **Low win rate:** Most straddles/strangles lose money because implied vol tends to overstate realized moves
- **Time decay is relentless:** Every day held without a move erodes the position's value
- **Difficult timing:** Entering too early bleeds theta; entering on the day-of means IV is at its peak and the straddle is maximally expensive

## Straddles and Strangles in Long/Short Portfolios

In the [[itpm]] [[long-short-equity]] methodology, long straddles and strangles serve as volatility expansion bets within a broader portfolio:

- Used when a fundamental catalyst is expected but direction is uncertain (e.g., binary earnings events, regulatory decisions)
- The POTM (Professional Options Trading Masterclass) teaches strap straddles and strip straddles for directionally biased volatility plays
- [[raj-malhotra]] focuses on VIX-based volatility trading as a complement to directional equity options
- Straddles/strangles can serve as portfolio hedges when positioned on index products

## See Also
- [[iron-condor]] -- the opposite trade: selling volatility by betting the price stays in a range
- [[gamma-scalping]] -- a dynamic hedging approach to monetize long gamma positions
- [[volatility-arbitrage]] -- systematically trading the spread between implied and realized volatility
- [[implied-volatility]] -- the critical variable that determines whether a straddle is cheap or expensive
- [[earnings]] -- the most common catalyst for straddle/strangle trades
- [[long-short-equity]] -- portfolio context for volatility plays
- [[straddle-vs-strangle]] -- detailed comparison of the two variants
- [[gut-spread]] -- an ITM variation of the strangle

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg's definitive treatment of straddle/strangle mechanics, the relationship between implied and realized volatility, and gamma's role in long-volatility positions
