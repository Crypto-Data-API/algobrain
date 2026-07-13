---
title: "Put Option"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [options, derivatives]
aliases: ["Put", "Long Put", "Put Contract"]
domain: [derivatives]
difficulty: beginner
related: ["[[call-option]]", "[[options]]", "[[strike-price]]", "[[premium]]", "[[delta]]", "[[married-put]]", "[[bear-put-spread]]"]
---

# Put Option

A put option is a contract that gives the holder the **right, but not the obligation**, to sell an underlying asset at a specified price (the [[strike-price]]) on or before a specified expiration date. The buyer pays a [[premium]] to the seller (writer) for this right. Puts are the most fundamental bearish options instrument and the primary tool for portfolio downside protection.

## How It Works

- **Buyer (long put):** pays the premium upfront. Profits if the underlying falls below the strike price by more than the premium paid. Maximum loss is limited to the premium. Maximum profit is the strike price minus premium (the underlying can only fall to zero).
- **Seller (short put / writer):** receives the premium. Profits if the underlying stays above the strike price through expiration. Maximum profit is the premium received. Maximum loss is the strike price minus premium (assigned shares at the strike while underlying goes to zero).

### Payoff at Expiration

```
Long put payoff = max(0, strike_price − underlying_price) − premium_paid
Short put payoff = premium_received − max(0, strike_price − underlying_price)
```

### Breakeven

```
breakeven = strike_price − premium_paid
```

## Key Greeks

| Greek | Meaning for Long Put |
|-------|---------------------|
| **[[delta]]** | Negative (0 to −1.0); ATM puts have ~−0.50 delta |
| **Gamma** | Positive; highest near ATM and expiration |
| **Theta** | Negative; time decay works against the buyer |
| **Vega** | Positive; higher IV benefits the buyer |

## Common Uses

- **Directional speculation** — leveraged bearish bet with defined risk
- **Portfolio insurance** — long puts protect a stock portfolio against declines ([[married-put]])
- **Income generation** — selling cash-secured puts to acquire stock at a lower price while earning premium
- **Spread components** — puts are legs of [[bear-put-spread]], [[bull-put-spread]], [[straddle-strangle|straddles]], and [[iron-condor|iron condors]]
- **Tail-risk hedging** — deep OTM puts as disaster insurance (see [[crash-fear-premium]])

## Put vs Short Stock

| Dimension | Long Put | Short Stock |
|-----------|----------|-------------|
| **Capital required** | Premium only | Margin + borrow costs |
| **Max loss** | Premium | Unlimited (stock can rise indefinitely) |
| **Max profit** | Strike − premium | Share price (stock goes to zero) |
| **Time decay** | Yes (theta) | No (but borrow costs) |
| **Dividends** | Not owed | Must pay dividends on borrowed shares |
| **Risk** | Defined | Undefined |

## Related

- [[call-option]] — the bullish counterpart
- [[options]] — options overview
- [[married-put]] — protective put strategy
- [[bear-put-spread]] — defined-risk bearish spread using puts
- [[crash-fear-premium]] — the premium for tail-risk put protection
- [[greeks]] — the full set of option sensitivities
- [[put-call-parity]] — the relationship linking puts, calls, and the underlying
- [[cboe-put-putwrite-index]] — benchmark for systematic put writing

## Sources

- Hull, J. C., *Options, Futures, and Other Derivatives* (10th ed.) — definitive textbook treatment of put payoffs, Greeks, and pricing
- Natenberg, S., *Option Volatility and Pricing* — practitioner reference on put behavior and volatility
- Options Clearing Corporation (OCC) / CBOE, *Characteristics and Risks of Standardized Options* — official disclosure document on contract mechanics and assignment
