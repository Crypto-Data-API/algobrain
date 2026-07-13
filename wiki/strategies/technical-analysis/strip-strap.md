---
title: "Strip and Strap"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, strip, strap, volatility, straddle-variant, directional-vol, debit]
strategy_type: quantitative
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[straddle-strangle]]", "[[short-straddle]]", "[[reverse-iron-condor]]", "[[implied-volatility]]", "[[gamma-scalping]]"]
---

# Strip and Strap

## Overview

The Strip and Strap are directionally biased variants of the [[straddle-strangle]]. A **Strip** consists of buying 1 ATM call and 2 ATM puts at the same strike and expiration -- it profits from large moves in either direction but pays out more on the downside, reflecting a **bearish volatility bias**. A **Strap** reverses the ratio: 2 ATM calls and 1 ATM put, producing a **bullish volatility bias** that pays more if the stock rallies. Both strategies require a big move to overcome the combined premium cost, but unlike a standard straddle, they express a view on which direction the breakout is more likely.

## Setup

**Strip:** Buy 1 ATM call + 2 ATM puts at the same strike and expiration. Total cost = call premium + (2 x put premium).

**Strap:** Buy 2 ATM calls + 1 ATM put at the same strike and expiration. Total cost = (2 x call premium) + put premium.

Use 30-60 DTE to allow time for the expected move while managing [[theta]] decay.

## Payoff Profile

| Scenario | Strip Outcome | Strap Outcome |
|---|---|---|
| Large move down | 2 puts profit heavily; call expires worthless | 1 put profits; 2 calls expire worthless |
| Stock stays flat | Max loss = total premium paid | Max loss = total premium paid |
| Large move up | 1 call profits; 2 puts expire worthless | 2 calls profit heavily; put expires worthless |

**Max loss** = total premium paid for all legs. **Max profit** = unlimited in the favored direction. **Break-evens** shift based on the 2:1 ratio compared to a standard straddle.

## When to Use

- You expect a **large move** but have a directional lean -- bearish bias favors the strip; bullish bias favors the strap.
- A binary event (earnings, regulatory decision) is approaching and you believe the downside or upside is underpriced.
- [[implied-volatility]] is not yet elevated, keeping the combined premium affordable.
- You want more exposure than a standard straddle provides in your favored direction.

## Advantages
- Asymmetric payoff -- larger reward in the expected direction of the breakout
- Unlimited profit potential in both directions (but tilted toward the bias)
- Defined risk -- maximum loss is limited to total premium paid
- Flexible tool for event-driven trading with a directional view

## Disadvantages
- Higher total premium cost than a standard straddle due to the extra contract
- Requires a larger move to reach break-even compared to a straddle
- [[theta]] decay is accelerated because three contracts are decaying simultaneously
- If the stock moves in the wrong direction, the extra leg adds to the cost without proportional benefit

## See Also
- [[straddle-strangle]] -- the standard non-directional volatility play
- [[reverse-iron-condor]] -- a defined-risk breakout strategy
- [[short-straddle]] -- the opposite trade (selling volatility)
- [[gamma-scalping]] -- dynamically hedging long straddle positions
