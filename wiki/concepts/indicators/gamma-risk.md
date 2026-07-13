---
title: "Gamma Risk"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, risk-management, indicators]
aliases: ["Gamma Risk", "Gamma Trap", "Gamma Exposure Risk"]
domain: [risk-management, derivatives]
prerequisites: ["[[gamma]]", "[[delta]]", "[[theta]]", "[[options-greeks]]"]
difficulty: advanced
related: ["[[gamma]]", "[[delta]]", "[[theta]]", "[[options-greeks]]", "[[gamma-scalping]]", "[[trade-repair-and-rolling]]", "[[iron-condors]]", "[[credit-spread]]", "[[wheel-strategy]]", "[[hedging]]", "[[position-sizing]]"]
---

Gamma risk is the danger that a position's [[delta]] (directional exposure) shifts rapidly and adversely as the underlying moves or as expiration approaches. It is the primary risk facing short-premium options sellers — [[credit-spread|credit spreads]], [[iron-condors]], [[covered-calls]], and [[cash-secured-puts]] all carry negative [[gamma]], meaning that directional exposure accelerates *against* the position when the underlying moves toward a short strike.

## Overview

[[Gamma]] itself is neutral — it simply measures the rate of change of delta. Gamma *risk* arises when a trader is short gamma (short options) and the underlying moves enough to cause large, adverse delta shifts that compound losses. The core dynamic:

- **Long gamma** (long options): delta moves in your favor — gains accelerate, losses decelerate. Gamma is your friend.
- **Short gamma** (short options): delta moves against you — losses accelerate, gains decelerate. Gamma is your enemy.

Every premium-selling strategy involves short gamma. The premium collected (via [[theta]] decay) is the *compensation* for bearing gamma risk. This is the [[gamma]]-[[theta]] tradeoff: the time decay earned each day is the market's price for the gamma risk borne overnight and intraday.

## The Gamma Acceleration Curve

Gamma is not constant — it varies dramatically with moneyness and time to expiration:

### By Moneyness

| Position | Gamma Level | Implication |
|----------|-------------|-------------|
| Deep OTM | Low | Delta near 0, barely moves — low risk |
| ATM | **Highest** | Delta is most sensitive — maximum risk zone |
| Deep ITM | Low | Delta near 1.0, barely moves — low risk |

Short-premium sellers are safest when the underlying stays far from their short strikes (deep OTM). Risk escalates as the underlying approaches the short strike, where gamma is highest and delta shifts are fastest.

### By Time to Expiration

This is the critical dimension for understanding gamma risk:

| Time to Expiry | ATM Gamma | Behavior |
|---------------|-----------|----------|
| 60+ DTE | Low | Delta changes slowly; moves are manageable |
| 30-45 DTE | Moderate | Standard selling window; gamma is present but controllable |
| 21 DTE | **Inflection point** | Gamma begins accelerating sharply for ATM options |
| 7-10 DTE | High | Small underlying moves cause large delta swings |
| 0-3 DTE | **Extreme** | ATM options can swing from delta 0.1 to 0.9 on a 1% move |

As expiration approaches, gamma concentrates around the ATM strike like a spike. This concentration is what creates pin risk — the uncertainty about whether an option will expire ITM or OTM when the underlying is near the strike.

## The Gamma Trap

The "gamma trap" is the zone — roughly **21 DTE and closer** — where short-premium positions become increasingly dangerous despite accelerating [[theta]] decay. The trap works as follows:

1. **Theta accelerates** near expiration, tempting sellers to hold positions longer to capture faster daily decay
2. **But gamma accelerates faster**, meaning that any adverse underlying move causes outsized delta shifts and rapid P&L deterioration
3. A position that was comfortably OTM at 30 DTE can be tested and lose more than all the theta collected in a single adverse session at 10 DTE
4. The closer to expiration, the less time remains to recover — rolling options become expensive and may not be possible for a credit

This is why many professional premium sellers — particularly those running [[iron-condors]], the [[wheel-strategy|wheel]], or [[credit-spread|credit spreads]] — mechanically close or roll positions at approximately **21 DTE**, even if the position is profitable. The marginal theta earned in the final three weeks is not worth the gamma risk exposure. (Source: [[recovering-losing-options-positions]])

### Worked Example: The Gamma Trap in Action

A trader sells a $100 put at 45 DTE when the stock is at $108 (8% OTM). At entry:
- Delta: -0.15 (low directional exposure)
- Gamma: 0.02 (delta changes slowly)
- A $2 stock move shifts delta by only 0.04

At 10 DTE, stock is at $101 (put is near ATM):
- Delta: -0.48 (significant directional exposure)
- Gamma: 0.12 (6x higher than at entry)
- A $2 stock move now shifts delta by 0.24 — the position's risk profile changes violently with every tick

The trader went from a comfortable 0.15 delta position to a near-coin-flip 0.48 delta position, and the gamma means it's getting worse with every tick down. This is the trap: the theta being earned is real but small, while the gamma risk is enormous.

## Gamma Risk by Strategy

| Strategy | Gamma Exposure | Risk Profile |
|----------|---------------|-------------|
| [[credit-spread]] | Negative (short leg dominates) | Risk spikes as underlying approaches short strike near expiry |
| [[iron-condors]] | Negative on both sides | Whichever side is tested experiences gamma acceleration |
| [[covered-calls]] | Mildly negative | Stock delta (1.0) dwarfs gamma effect on the call; gamma risk is modest |
| [[cash-secured-puts]] | Negative | Full gamma risk as stock drops toward strike; no offsetting long delta |
| Long [[vertical-spread]] (debit) | Positive (long leg dominates) | Gamma works in your favor near the long strike |
| [[gamma-scalping]] | Positive (deliberately) | Buys gamma and hedges delta to profit from realized moves |

## Managing Gamma Risk

### The 21-DTE Roll Rule

The most widely adopted gamma risk management technique is to close or roll short-premium positions at approximately 21 DTE. This captures roughly 60-70% of the total theta decay available (since theta accelerates in the final weeks) while avoiding the zone where gamma risk dominates. See [[trade-repair-and-rolling]] for rolling mechanics.

### Position Sizing

Gamma risk compounds with position size. The [[position-sizing|2% rule]] (risk no more than 1-2% of portfolio equity per trade) is particularly important for short-premium strategies where gamma can cause rapid loss acceleration. Defined-risk structures ([[iron-condors]], [[credit-spread|credit spreads]]) cap the maximum damage, but the speed of loss near expiration can still catch oversized positions. (Source: [[recovering-losing-options-positions]])

### Portfolio-Level Greeks Monitoring

Professional traders aggregate gamma across all open positions to monitor net portfolio gamma exposure. A portfolio with large negative gamma is vulnerable to any sharp move in the underlying. When net gamma becomes too negative, the trader can:
- Close the most at-risk (nearest ATM, nearest expiry) positions
- Add long gamma positions (buy straddles, strangles, or outright options)
- Reduce position count to lower aggregate gamma exposure

### Profit Targets and Loss Limits

Pre-defined exit rules — close at 50% of max profit, close at 2× credit received for a loss — prevent holding into the gamma trap zone. These mechanical rules override the temptation to "squeeze out" the last 20% of profit. (Source: [[recovering-losing-options-positions]])

## Gamma Risk vs. Vega Risk

Both gamma and [[vega]] create risk for short-premium sellers, but they operate differently:

| Dimension | Gamma Risk | Vega Risk |
|-----------|-----------|-----------|
| **Trigger** | Underlying price movement | Implied volatility change |
| **When worst** | Near expiration (high gamma) | Far from expiration (high vega) |
| **Speed** | Fast — delta shifts happen tick by tick | Moderate — IV changes over hours/days |
| **Hedge** | Close/roll near 21 DTE | Manage vega exposure across expirations |

A short-premium portfolio is typically most exposed to vega risk early in the trade (when IV spikes cause mark-to-market losses) and most exposed to gamma risk late in the trade (when underlying moves cause rapid delta shifts).

## Related

- [[gamma]] — the underlying Greek (second-order price sensitivity)
- [[delta]] — the directional exposure that gamma shifts
- [[theta]] — the decay earned as compensation for gamma risk (gamma-theta tradeoff)
- [[trade-repair-and-rolling]] — the 21-DTE rule and rolling mechanics to escape the gamma trap
- [[iron-condors]] — high gamma risk strategy requiring active management
- [[credit-spread]] — defined-risk short-premium structure with gamma risk
- [[gamma-scalping]] — a strategy that deliberately goes long gamma
- [[options-greeks]] — overview of all Greek risk measures
- [[position-sizing]] — sizing to survive gamma-driven loss acceleration

## Sources

- (Source: [[recovering-losing-options-positions]])
- Cross-referenced from [[gamma]], [[trade-repair-and-rolling]], [[iron-condors]]
