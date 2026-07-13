---
title: "Call Option"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [options, derivatives]
aliases: ["Call", "Long Call", "Call Contract", "Call Options", "call-options", "calls"]
domain: [derivatives]
prerequisites: ["[[options]]"]
difficulty: beginner
related: ["[[put-option]]", "[[options]]", "[[strike-price]]", "[[premium]]", "[[delta]]", "[[covered-call]]", "[[bull-call-spread]]"]
---

# Call Option

A call option is a contract that gives the holder the **right, but not the obligation**, to buy an underlying asset at a specified price (the [[strike-price]]) on or before a specified expiration date. The buyer pays a [[premium]] to the seller (writer) for this right. Calls are the most fundamental bullish options instrument and the building block of most options strategies.

## How It Works

- **Buyer (long call):** pays the premium upfront. Profits if the underlying rises above the strike price by more than the premium paid. Maximum loss is limited to the premium. Maximum profit is theoretically unlimited.
- **Seller (short call / writer):** receives the premium. Profits if the underlying stays below the strike price through expiration. Maximum profit is the premium received. Maximum loss is theoretically unlimited (the underlying can rise without bound).

### Payoff at Expiration

```
Long call payoff = max(0, underlying_price − strike_price) − premium_paid
Short call payoff = premium_received − max(0, underlying_price − strike_price)
```

### Breakeven

```
breakeven = strike_price + premium_paid
```

## Key Greeks

| Greek | Meaning for Long Call |
|-------|----------------------|
| **[[delta]]** | Positive (0 to +1.0); ATM calls have ~0.50 delta |
| **Gamma** | Positive; highest near ATM and expiration |
| **Theta** | Negative; time decay works against the buyer |
| **Vega** | Positive; higher IV benefits the buyer |

## Common Uses

- **Directional speculation** — leveraged bullish bet with defined risk
- **Hedging short positions** — long calls protect against a short stock position running higher
- **Income generation** — selling covered calls ([[covered-call]]) against long stock to earn premium
- **Spread components** — calls are legs of [[bull-call-spread]], [[bear-call-spread]], [[straddle-strangle|straddles]], and [[iron-condor|iron condors]]

## Call vs Stock

| Dimension | Long Call | Long Stock |
|-----------|----------|------------|
| **Capital required** | Premium only | Full share price |
| **Max loss** | Premium | Full share price (to zero) |
| **Max profit** | Unlimited | Unlimited |
| **Time decay** | Yes (theta) | No |
| **Dividends** | Not received | Received |
| **Leverage** | Yes (built-in) | Only with margin |

## Related

- [[put-option]] — the bearish counterpart
- [[options]] — options overview
- [[covered-call]] — selling calls against stock
- [[bull-call-spread]] — defined-risk bullish spread using calls
- [[strike-price]] — the exercise price
- [[premium]] — the price paid for the option
- [[delta]] — the primary Greek for directional exposure

## Sources

- Hull, John C. *Options, Futures, and Other Derivatives* (10th ed.) — standard textbook treatment of call payoffs, parity, and the Greeks
- McMillan, Lawrence G. *Options as a Strategic Investment* — practitioner reference on call strategies, covered calls, and spreads
- Cboe (Chicago Board Options Exchange) — *Options Contract Specifications* and educational documentation on listed equity and index call options
