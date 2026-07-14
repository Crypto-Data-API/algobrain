---
title: "Moneyness"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: good
tags: [options, derivatives, pricing]
aliases: ["ITM", "ATM", "OTM", "In-the-Money", "At-the-Money", "Out-of-the-Money", "In the Money", "At the Money", "Out of the Money"]
domain: [market-microstructure]
prerequisites: ["[[options]]", "[[strike-price]]"]
difficulty: beginner
related: ["[[options]]", "[[strike-price]]", "[[delta]]", "[[implied-volatility]]", "[[black-scholes]]"]
---

Moneyness describes the relationship between an option's [[strike-price]] and the current price of the underlying asset. It determines whether an option has intrinsic value and is the primary framework traders use for strike selection, probability assessment, and understanding how the [[options-greeks|Greeks]] behave across the options chain.

## The Three States

| State | Call Option | Put Option | Intrinsic Value |
|-------|-----------|-----------|----------------|
| **In-the-Money (ITM)** | Stock price > Strike | Stock price < Strike | Positive |
| **At-the-Money (ATM)** | Stock price ≈ Strike | Stock price ≈ Strike | Near zero |
| **Out-of-the-Money (OTM)** | Stock price < Strike | Stock price > Strike | Zero |

### Examples (stock at $100)

| Strike | Call Moneyness | Put Moneyness |
|--------|---------------|---------------|
| $90 | ITM ($10 intrinsic) | OTM (no intrinsic) |
| $100 | ATM | ATM |
| $110 | OTM (no intrinsic) | ITM ($10 intrinsic) |

## Intrinsic vs. Extrinsic Value

An option's price (premium) consists of two components:

```
Premium = Intrinsic Value + Extrinsic Value (Time Value)
```

- **Intrinsic value**: The amount an option is in-the-money. A $100 call when the stock is at $108 has $8 intrinsic value. OTM and ATM options have zero intrinsic value.
- **Extrinsic value**: Everything else — primarily [[theta|time value]] and [[implied-volatility|volatility premium]]. Extrinsic value is highest for ATM options and decays to zero at expiration.

| Moneyness | Intrinsic Value | Extrinsic Value | Total Premium |
|-----------|----------------|-----------------|---------------|
| Deep ITM | High | Low (mostly intrinsic) | High |
| ATM | ~Zero | Maximum | Moderate |
| OTM | Zero | Moderate (all extrinsic) | Low |
| Deep OTM | Zero | Minimal | Very low |

## How the Greeks Vary by Moneyness

Moneyness fundamentally shapes how each Greek behaves:

### [[delta]]
- **Deep ITM**: Delta approaches ±1.0 (moves dollar-for-dollar with stock)
- **ATM**: Delta ≈ ±0.50 (roughly 50% chance of expiring ITM)
- **Deep OTM**: Delta approaches 0 (barely moves with stock)
- Delta provides a rough probability estimate of expiring ITM

### [[gamma]]
- **ATM**: Gamma is highest — delta changes fastest near the strike
- **ITM/OTM**: Gamma is lower — delta is more stable
- Near expiration, ATM gamma spikes dramatically (the "gamma knife")

### [[theta]]
- **ATM**: Theta decay is fastest (most extrinsic value to lose)
- **Deep ITM/OTM**: Theta is smaller (less extrinsic value)
- ATM theta accelerates sharply in the final weeks before expiration

### [[vega]]
- **ATM**: Highest vega — most sensitive to [[implied-volatility]] changes
- **Deep ITM/OTM**: Lower vega — volatility changes have less impact
- Longer-dated ATM options have the highest vega of any option

## Standardized Moneyness

Professional traders often express moneyness in standardized terms rather than raw strike prices:

### Delta-Based Moneyness

The most common convention. Traders refer to options by their delta:
- **25-delta put** = OTM put with delta of -0.25 (~25% ITM probability)
- **50-delta** = ATM (by convention, the strike closest to 50 delta)
- **25-delta call** = OTM call with delta of +0.25

This is the standard quoting convention in FX options and increasingly used in equity options.

### Log-Moneyness

```
m = ln(S/K)
```

Positive for ITM calls (OTM puts), negative for OTM calls (ITM puts), zero for ATM. Used in academic literature and volatility surface modeling.

### Standardized by Volatility

```
d = ln(S/K) / (σ√T)
```

This normalizes moneyness by the option's total expected move (volatility × square root of time). An option that is 1 standard deviation OTM has d ≈ -1 regardless of the stock price, volatility, or expiration. This is the natural coordinate for the [[volatility-surface]].

## Strike Selection in Practice

### Delta-Based Selection Rules

Most professional options traders select strikes by delta rather than by price distance:

| Objective | Typical Delta | Rationale |
|-----------|--------------|-----------|
| Directional bet with leverage | 0.40–0.60 | Balanced risk/reward, highest gamma |
| Defined-risk directional | 0.25–0.35 | Lower cost, decent probability |
| Premium selling (short strikes) | 0.15–0.30 | High probability of profit, manageable gamma |
| Hedging / protective puts | 0.20–0.35 | Balance protection cost vs. coverage |
| Lottery tickets / tail bets | 0.05–0.15 | Very cheap, very low probability |

### Fundamental-Directional Approach

Discretionary fundamental traders typically use:
- ATM or slightly ITM options for core positions (delta 0.50–0.70)
- 20–60 day expirations to balance theta cost against time for thesis to play out
- Strike selection aligned with fundamental [[catalyst]] timing

## Deep ITM and Deep OTM Considerations

### Deep ITM Options
- Behave almost like stock (delta near ±1.0)
- Very low extrinsic value — minimal theta decay
- Useful as **stock replacement** (similar P&L with less capital)
- Wide bid-ask spreads and lower liquidity
- Early [[assignment-and-exercise|exercise]] risk for American-style options

### Deep OTM Options
- Very cheap in absolute terms
- Very low probability of profit
- High percentage gains if the underlying makes a large move
- Subject to rapid [[theta]] decay (all extrinsic value)
- The "lottery ticket" appeal — and the reason most retail options buyers lose money

## Related

- [[options]] — overview of options contracts
- [[strike-price]] — the fixed price in the option contract
- [[delta]] — the Greek most directly tied to moneyness
- [[gamma]] — rate of delta change, peaks at ATM
- [[theta]] — time decay, fastest for ATM options
- [[implied-volatility]] — IV varies by moneyness (the [[volatility-surface|vol surface]])
- [[options-greeks]] — how all Greeks relate to moneyness
- [[assignment-and-exercise]] — exercise decisions depend on moneyness

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg's treatment of moneyness, intrinsic/extrinsic value, and how the Greeks vary across strikes
