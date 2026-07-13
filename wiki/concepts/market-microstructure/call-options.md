---
title: Call Options
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - options
  - derivatives
  - market-microstructure
aliases:
  - call-option
  - calls
  - call
domain: [market-microstructure]
prerequisites: ["[[options]]", "[[strike-price]]"]
difficulty: beginner
related:
  - "[[options]]"
  - "[[put-options]]"
  - "[[derivatives]]"
  - "[[strike-price]]"
  - "[[covered-call]]"
  - "[[options-greeks]]"
  - "[[put-call-parity]]"
  - "[[implied-volatility]]"
---

# Call Options

A **call option** gives the holder the right, but not the obligation, to buy an underlying asset at a specified [[strike-price]] before or on the expiration date. Buyers pay a [[premium]] for this right.

Call options profit when the underlying asset rises above the strike price. They are a core building block of [[options]] strategies.

## Payoff Structure

The payoff at expiration for a long call is: **max(0, underlying price - strike price) - premium paid**. The maximum loss is limited to the premium, while the potential profit is theoretically unlimited as the underlying price rises. This asymmetric payoff profile makes calls attractive for bullish speculation with defined risk.

## Intrinsic vs. Extrinsic Value

- **Intrinsic value** -- the amount by which the option is in-the-money (underlying price minus strike, if positive). An option with no intrinsic value is out-of-the-money.
- **Extrinsic value** (time value) -- the portion of the premium above intrinsic value, reflecting time remaining until expiration and implied [[volatility]]. Extrinsic value decays as expiration approaches (theta decay).

## When to Use Calls

- **Buying calls** -- a bullish directional bet with limited risk. Traders buy calls when they expect the underlying to rise significantly before expiration.
- **Selling (writing) calls** -- generates income from the premium collected. Naked short calls carry unlimited risk if the underlying rallies. The [[covered-call]] strategy -- selling calls against stock you own -- is a common income and hedging approach.

## Greeks

The [[options-greeks]] describe how a call's price responds to its inputs. For a long call: positive **delta** (0 to +1 — it gains value as the underlying rises; ATM ≈ +0.50, deep ITM approaches +1), positive **gamma** (delta accelerates as the underlying rises, peaking at-the-money near expiry), negative **theta** (it loses extrinsic value daily, accelerating in the final 30 days for buyers), positive **vega** (it gains value when [[implied-volatility]] rises), and positive **rho** (higher interest rates increase call value). A short (written) call carries the opposite signs — notably it is short gamma and short vega, so a sharp rally plus an IV spike hurts the seller twice.

## Worked Example

Stock = $102, $100-strike call, 30 days to expiry, IV = 30%. The call has $2 of intrinsic value (102 − 100) and might trade at ≈ $4.20 — the remaining ≈ $2.20 is extrinsic (time) value. If the stock rises $3 to $105 the next day with IV unchanged, a delta of ≈ +0.60 adds ≈ $1.80, gamma adds a bit more as delta rises, minus a few cents of theta — the call finishes near $6.00. The buyer paid $420 (×100 multiplier) for exposure that a 3% move turned into roughly $600. If instead the stock sat still, theta would bleed the position toward its $2 intrinsic value by expiry.

## When Calls Lose Value Fast

Like long [[put-options]], long calls can lose even when direction is right: **IV crush** after an event can erase vega gains, **theta** accelerates in the final weeks, and **OTM calls** decay to zero quickly if the rally stalls. Buying calls into earnings is a classic trap — elevated IV collapses after the report, frequently leaving the holder with a loss even on a favourable move.

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* — standard reference for call payoff, pricing, and Greeks
- CBOE / OCC options education materials — contract specifications, exercise/assignment, and multiplier conventions
- [[put-options]] — the bearish counterpart; see also [[put-call-parity]] linking the two

## Related

- [[options]]
- [[put-options]]
- [[derivatives]]
- [[strike-price]]
- [[covered-call]]
- [[options-greeks]]
- [[put-call-parity]]
- [[implied-volatility]]
