---
title: "Gut Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, guts, gut-spread, ITM, volatility, straddle-variant, advanced]
aliases: ["Long Guts", "Short Guts"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[straddle-strangle]]", "[[strip-strap]]", "[[reverse-iron-condor]]", "[[implied-volatility]]", "[[gamma-scalping]]"]
---

# Gut Spread

## Overview

A Gut Spread (also called "Guts") is a straddle-like strategy constructed with **in-the-money** options instead of at-the-money options. A **Long Guts** position buys an ITM call and an ITM put, while a **Short Guts** position sells both. The payoff profile is functionally equivalent to a [[straddle-strangle]], but the use of ITM options changes the premium dynamics and practical considerations.

Long Guts costs more than a straddle because both legs carry intrinsic-value, but the break-even points are often **lower** since the extrinsic premium component may be smaller. Short Guts collects more premium upfront but faces higher [[assignment]] risk because both options are already ITM.

## Setup

### Long Guts
1. **Buy 1 ITM call** (strike 5-10% below current price) + **1 ITM put** (strike 5-10% above current price).
2. Same expiration for both legs, typically 30-60 DTE.
3. Total cost = call premium + put premium. Both will have large intrinsic-value components.

### Short Guts
1. **Sell 1 ITM call** and **sell 1 ITM put** at the same strikes as above.
2. Collects substantial premium but requires significant margin.
3. Maximum profit = total premium collected minus the intrinsic value overlap.

## Payoff Profile

| Scenario | Long Guts | Short Guts |
|---|---|---|
| Large move in either direction | Profits (one leg gains more than the other loses) | Large loss |
| Price stays between strikes | Max loss = total extrinsic premium paid | Max profit |
| Price at either strike | Partial loss/gain depending on premium | Partial profit |

**Long Guts max loss** = net extrinsic value paid (total premium minus total intrinsic value). **Short Guts max loss** = unlimited in both directions.

## When to Use

- **Long Guts:** You expect a large move and prefer ITM options for their tighter bid-ask spreads and higher [[liquidity]] on some underlyings. Also useful when ATM strikes have unfavorable pricing.
- **Short Guts:** You expect the stock to remain range-bound and want to collect maximum premium. Only for experienced traders comfortable with substantial margin requirements and [[assignment]] risk.

## Advantages
- ITM options often have tighter bid-ask spreads and better [[liquidity]] than OTM alternatives
- Long Guts break-even points can be more favorable than an equivalent straddle
- Short Guts collects more premium upfront than a [[short-straddle]]
- Functionally equivalent payoff to straddle/strangle -- choose based on which options have better pricing

## Disadvantages
- **Higher capital requirement** -- ITM options are more expensive than ATM or OTM
- **Assignment risk** is elevated for Short Guts since both legs are already ITM
- More complex to analyze due to the large intrinsic-value component in each leg
- Short Guts carries **unlimited risk** in both directions with heavy margin demands

## See Also
- [[straddle-strangle]] -- the ATM/OTM equivalent of the guts strategy
- [[strip-strap]] -- directional straddle variants using extra legs
- [[short-straddle]] -- the more common ATM premium-selling alternative
