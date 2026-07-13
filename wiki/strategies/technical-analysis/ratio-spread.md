---
title: "Ratio Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [options, ratio-spread, directional, volatility, advanced, unlimited-risk, credit]
aliases: ["Call Ratio Spread", "Put Ratio Spread", "Ratio Vertical"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[backspread]]", "[[butterfly-spread]]", "[[calendar-spread]]", "[[iron-condor]]", "[[implied-volatility]]", "[[delta]]", "[[gamma]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]"]
---

# Ratio Spread

## Overview

A Ratio Spread involves buying N options at one strike and selling M options at a different strike, where **M is greater than N** (typically 1:2 or 1:3). The most common form is the **call ratio spread**: buy 1 ATM call and sell 2 OTM calls. The extra short option partially or fully finances the long option, often resulting in a **zero-cost or net credit** entry. The trade profits from a moderate directional move to the short strike but faces **unlimited risk** beyond the short strikes if the move continues.

Ratio spreads are the **inverse of [[backspread]]s** -- where backspreads want big moves, ratio spreads want moderate, controlled moves. The extra short option means the trader is net short [[vega]] and benefits from declining [[implied-volatility]]. This makes ratio spreads a favorite of experienced traders who have a directional view combined with an expectation of falling IV. The exposed (naked) short leg creates the key danger: if the underlying blows through the short strikes, losses accelerate with no cap.

## Rules / Setup

### Entry
1. **Call ratio spread (bullish):** Buy 1 ATM or slightly ITM call. Sell 2 OTM calls at a higher strike. Example: buy 1 $100 call, sell 2 $110 calls.
2. **Put ratio spread (bearish):** Buy 1 ATM or slightly ITM put. Sell 2 OTM puts at a lower strike.
3. **Net cost:** Structure the strikes so the trade is entered for zero cost or a small net credit. If paying a debit, it should be minimal.
4. **Ratio:** 1:2 is standard. 1:3 increases the credit but amplifies the risk and narrows the profit zone.
5. **Expiration:** 30-60 DTE. Enough time for the directional thesis to play out but not so long that [[theta]] is negligible.
6. **IV environment:** Best entered when [[implied-volatility]] is elevated and expected to decline.

### Exit and Adjustments
1. **Profit target:** Close at 50-75% of max profit. Do not hold to expiration hoping for a perfect pin at the short strike.
2. **Stop-loss on the naked leg:** Close the entire position if the underlying breaches the short strike with momentum. The naked short leg has unlimited risk (calls) or substantial risk (puts).
3. **Hedge the risk:** If the short strike is threatened, buy the next further OTM option to cap the risk (converting to a [[broken-wing-butterfly]] or [[butterfly-spread]]). This is the most common adjustment — it eliminates the unlimited risk while preserving the existing P&L.
4. **Roll the position:** If the thesis is intact but timing is off, roll the entire ratio spread to a later expiration. See [[trade-repair-and-rolling]] for the general rolling framework. For ratio spreads specifically, rolling the naked leg is the priority — the exposed short option carries [[gamma-risk]] that intensifies near expiration.
5. **IV management:** If IV spikes instead of declining, the extra short options increase in value faster than the long option. Consider closing early.
6. **The 21-DTE rule:** Ratio spreads with a naked short leg should be managed at ~21 DTE. The [[gamma-risk|gamma trap]] near expiration is especially dangerous for ratio spreads because the naked leg's delta accelerates against the position with no offsetting protection. (Source: [[recovering-losing-options-positions]])

### Position Sizing
The naked short option creates undefined risk. Size conservatively -- treat the risk as equivalent to a naked option position. Never allocate more than 2-3% of the account to a single ratio spread.

## Payoff Profile
- **Max profit:** Occurs when the underlying is at the short strike at expiration. Equal to (short strike - long strike) + net credit, or (short strike - long strike) - net debit.
- **Max loss:** Unlimited on the upside (call ratio) or down to zero on the downside (put ratio). The loss beyond the short strike increases dollar-for-dollar with each extra short contract.
- **Break-even (upside):** Short strike + max profit amount (for a call ratio).
- **Break-even (downside):** Long strike + debit paid (if debit entry); or no downside risk if entered for a credit.

## Example Trade
**Asset:** META trading at $500, 40 DTE, elevated IV after a pullback. You expect a bounce to $530 but not beyond $560.
1. **Buy 1 META $500 call** at $18.00.
2. **Sell 2 META $530 calls** at $9.00 each ($18.00 total credit).
3. **Net cost:** $18.00 - $18.00 = **$0.00** (zero cost entry).
4. **Max profit at $530:** $530 - $500 = $30.00 ($3,000 per spread).
5. **Upper break-even:** $530 + $30 = $560. Above $560, losses begin and are unlimited.
6. **Below $500:** All options expire worthless. Loss = $0 (zero cost entry means no downside risk).
7. META rallies to $528 in 30 days. Close the spread for approximately $22.00. **Profit: $2,200** on zero capital at risk (below $500).

## Advantages
- **Zero or low cost entry:** The extra short option(s) finance the long option, often eliminating the debit entirely
- **High max profit potential:** If the underlying moves exactly to the short strike, the return on capital is exceptional
- **Benefits from IV decline:** Net short [[vega]] means a drop in [[implied-volatility]] helps the position
- **No downside risk (if credit entry):** On a call ratio entered for zero cost, there is no loss if the underlying falls
- **Flexible ratios:** Can adjust the 1:2 ratio to 1:3, 2:3, etc. to fine-tune the credit and risk profile

## Disadvantages
- **Unlimited risk on one side:** The naked short option creates theoretically unlimited loss potential above the break-even
- **Requires active risk management:** Cannot be treated as a set-and-forget trade; the naked leg demands monitoring
- **Margin intensive:** Brokers require significant margin for the naked short option(s)
- **Narrow optimal outcome:** Max profit only occurs at one specific price -- partial profits are common
- **Dangerous in trending markets:** A runaway move through the short strikes produces accelerating losses

## See Also
- [[trade-repair-and-rolling]] — complete rolling and adjustment framework
- [[gamma-risk]] — the risk driving the 21-DTE rule, especially dangerous for the naked leg
- [[backspread]] — the opposite structure: buy more options than you sell for unlimited profit potential
- [[butterfly-spread]] — a ratio spread with the risk capped by an additional long wing
- [[broken-wing-butterfly]] — similar payoff achieved by adding a protective wing to a ratio spread
- [[iron-condor]] — a defined-risk alternative for range-bound markets
- [[implied-volatility]] — ratio spreads work best when IV is elevated and expected to decline
