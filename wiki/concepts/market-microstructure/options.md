---
title: "Options"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [options, derivatives, volatility, risk-management]
aliases: ["options-contracts", "Options Trading", "options-trading", "Stock Options"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[derivatives]]", "[[volatility]]"]
difficulty: intermediate
related: ["[[derivatives]]", "[[futures]]", "[[volatility]]", "[[leverage]]", "[[implied-volatility]]", "[[vix]]", "[[volatility-risk-premium]]", "[[black-scholes]]", "[[options-chain]]"]
---

# Options

An option is a financial contract that gives the holder the right — but not the obligation — to buy or sell an underlying asset at a specified price before or on a given date. Options are the primary tool for trading [[volatility]] directly, constructing asymmetric payoffs, and building complex multi-leg strategies. The options market is one of the largest and most sophisticated derivatives markets in the world.

## The Basics

Options come in two forms: **calls** (right to buy) and **puts** (right to sell). The buyer pays a **premium** to the seller (writer) for this right. Options provide built-in [[leverage]] — a small premium controls a large notional position.

### Key Terms

| Term | Definition |
|------|-----------|
| **Strike price** | The price at which the holder can buy (call) or sell (put) the underlying |
| **Expiration** | The date after which the option expires worthless if not exercised |
| **Premium** | The price paid for the option = intrinsic value + extrinsic (time) value |
| **Intrinsic value** | How much the option is in-the-money (ITM). A $100 call when stock is at $105 has $5 intrinsic |
| **Extrinsic value** | Time value + volatility premium. Decays to zero at expiration |
| **Moneyness** | ITM (has intrinsic value), ATM (strike ≈ current price), OTM (no intrinsic value) |
| **American-style** | Can be exercised any time before expiry (most equity options) |
| **European-style** | Can only be exercised at expiry (SPX options, index options) |
| **Contract multiplier** | Standard equity options control 100 shares per contract |

## The Greeks

The Greeks measure how an option's price changes in response to different variables. Understanding them is essential for risk management.

| Greek | Measures | Practical Meaning |
|-------|---------|-------------------|
| **Delta (Δ)** | Price sensitivity to underlying | A 0.50 delta call gains ~$0.50 for each $1 move in the stock. Also approximates ITM probability |
| **Gamma (Γ)** | Rate of change of delta | High gamma near ATM at expiration — small price moves cause large delta swings. This is why 0DTE options are so volatile |
| **Theta (Θ)** | Time decay per day | Options lose value every day. ATM options decay fastest. Theta is the cost of holding a long option position |
| **Vega (ν)** | Sensitivity to implied volatility | A 1-point rise in IV increases the option price by the vega amount. Long options benefit from rising IV |
| **Rho (ρ)** | Sensitivity to interest rates | Usually minor, but matters for LEAPS and in high-rate environments |

### Greek Interactions

- **Long calls**: positive delta, positive gamma, negative theta, positive vega
- **Short puts**: positive delta, negative gamma, positive theta, negative vega
- **Straddles**: near-zero delta, positive gamma, negative theta, positive vega
- **Iron condors**: near-zero delta, negative gamma, positive theta, negative vega

The fundamental tradeoff: **gamma and theta are opponents**. If you want to benefit from large moves (long gamma), you pay time decay (negative theta). If you want to collect time decay (positive theta/short gamma), you are exposed to large moves.

## Put-Call Parity

The fundamental pricing relationship between calls and puts:

```
Call - Put = Stock - PV(Strike)
```

If this equation is violated, a risk-free arbitrage exists. Put-call parity ensures that a synthetic stock position (long call + short put at the same strike) behaves identically to holding the stock. Deviations from parity are exploited by market makers and are typically very small and short-lived.

## Volatility Smile and Skew

In practice, options at different strikes trade at different implied volatilities — violating the constant-volatility assumption of [[black-scholes|Black-Scholes]]:

- **Skew (equities)**: OTM puts have higher IV than ATM or OTM calls. This reflects demand for downside protection (portfolio hedging) and the empirical fact that stocks crash more often than they spike. The skew steepened dramatically after the 1987 crash.
- **Smile (FX, commodities)**: both OTM puts and OTM calls have higher IV than ATM options, forming a U-shape. Reflects tail risk in both directions.

The vol surface (IV across strikes and expirations) is a rich source of market information. See [[implied-volatility]], [[volatility-risk-premium]].

## Common Option Strategies

### Directional (Bullish/Bearish)

| Strategy | Construction | Max Profit | Max Loss | When to Use |
|----------|-------------|------------|----------|-------------|
| **Long call** | Buy call | Unlimited | Premium paid | Bullish, want leverage |
| **Long put** | Buy put | Strike - premium | Premium paid | Bearish, want defined risk |
| **Bull call spread** | Buy lower call, sell higher call | Width - debit | Debit paid | Moderately bullish, reduce cost |
| **Bear put spread** | Buy higher put, sell lower put | Width - debit | Debit paid | Moderately bearish |

### Income / Neutral

| Strategy | Construction | Max Profit | Max Loss | When to Use |
|----------|-------------|------------|----------|-------------|
| **Covered call** | Own stock + sell OTM call | Premium + (strike - cost) | Stock goes to zero | Willing to sell at strike, collect premium |
| **Cash-secured put** | Sell put + hold cash for assignment | Premium | Strike - premium | Willing to buy stock at strike |
| **Iron condor** | Sell OTM put spread + sell OTM call spread | Net credit | Width - credit | Range-bound, sell [[volatility]] |
| **Short strangle** | Sell OTM put + sell OTM call | Net credit | Unlimited | High IV, expect mean-reversion |

### Volatility

| Strategy | Construction | Max Profit | Max Loss | When to Use |
|----------|-------------|------------|----------|-------------|
| **Long straddle** | Buy ATM call + buy ATM put | Unlimited | Both premiums | Expect big move, unsure of direction |
| **Long strangle** | Buy OTM call + buy OTM put | Unlimited | Both premiums | Cheaper than straddle, needs bigger move |
| **Calendar spread** | Sell near-term, buy longer-term (same strike) | Variable | Net debit | Expect IV term structure to steepen |

### The ITPM Approach

The ITPM methodology (as demonstrated by [[anton-kreil]]) uses options exclusively for a long-short-equity portfolio:

- Every position is a long call, long put, short call, or short put on individual stocks
- Options provide natural leverage (3-4x) without margin debt
- Portfolio is constructed as a balanced long/short book
- Target statistics: 65/35 win-loss rate, 1.5+ R-score, 3+ Sharpe ratio
- Average holding period: 20-25 days

See [[itpm-meet-dieter-the-doubler]] for a documented case study achieving ~100% return in 6 months using this approach.

## The 0DTE Phenomenon

Zero-days-to-expiration (0DTE) options — contracts expiring the same day — have exploded since 2022:

- 0DTE options have grown to dominate SPX flow: ~59% of total SPX options volume in 2025, hitting record monthly highs of 62-63% in early-to-mid 2026 (up from roughly 5% in 2020). 0DTE was ~24% of all US-listed options volume in 2025 (Source: CBOE, verified via WebSearch, 2026-06-11)
- **Gamma risk**: 0DTE options have extreme gamma near ATM — small underlying moves produce enormous percentage changes in the option price
- **Market impact debate**: there is active debate about whether 0DTE flows amplify or dampen intraday market volatility. Market makers hedging 0DTE positions may create feedback loops
- **Retail appeal**: very low absolute premium ($0.50-$5 per contract) with lottery-ticket-like payoffs

## Options Data

Key data sources for options traders:

- **CBOE**: official volume and open interest data, VIX calculation methodology
- **Options chains**: available on most brokers and [[tradingview-platform|TradingView]], finviz, Yahoo Finance
- **Unusual options activity**: services like Unusual Whales, Cheddar Flow track large block trades that may signal institutional positioning
- **OPRA feed**: the official US options data feed — extremely high bandwidth, expensive
- **Put-call ratio**: total put volume / call volume. Extreme readings signal [[sentiment]] extremes. See [[contrarian-extremes]]

## Example Trade

A trader buys a BTC $60,000 call for $2,000 premium expiring in 30 days. If BTC rises to $65,000, the option is worth at least $5,000 — a 150% return on the premium paid. If BTC stays below $60,000, the option expires worthless and the trader loses only the $2,000 premium. The asymmetry — limited loss, potentially unlimited gain — is the defining feature of long options.

## Sources

- [[itpm-meet-dieter-the-doubler]] — ITPM case study demonstrating options-only portfolio management
- [[book-options-futures-other-derivatives]] — Hull's canonical options textbook
- [CBOE — The State of the Options Industry / SPX 0DTE share](https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august/) — 0DTE volume statistics. Verified via WebSearch, 2026-06-11

## Related

- [[derivatives]] — options are a core derivative type
- [[volatility]] — options are priced based on implied vol
- [[implied-volatility]] — the vol embedded in option prices
- [[vix]] — the "fear index" derived from SPX option prices
- [[volatility-risk-premium]] — the persistent gap between implied and realized vol
- [[futures]] — often used alongside options for hedging
- [[black-scholes]] — the foundational option pricing model
