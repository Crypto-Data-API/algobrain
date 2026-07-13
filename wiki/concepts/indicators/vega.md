---
title: "Vega"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [options, derivatives, volatility]
aliases: ["Option Vega", "Volatility Sensitivity", "Kappa"]
related: ["[[options-greeks]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[implied-volatility]]", "[[volatility]]", "[[black-scholes]]", "[[options]]", "[[volatility-smile]]", "[[volatility-skew]]"]
domain: [derivatives, risk-management]
difficulty: intermediate
---

**Vega** measures how much an option's price changes for a 1-percentage-point change in [[implied-volatility]]. It quantifies the sensitivity of an option's value to the market's expectation of future volatility. Vega is critical for any trader whose strategy depends on volatility direction rather than (or in addition to) the direction of the underlying asset.

## Overview

Vega is technically not a Greek letter (it is sometimes called kappa in academic literature), but it is universally included in the standard set of [[options-greeks]] due to its practical importance. Implied volatility is one of the primary drivers of option prices, and vega tells you exactly how much a change in IV will affect your position.

All long options -- both calls and puts -- have positive vega. When implied volatility rises, option prices increase; when it falls, option prices decrease. Conversely, all short options have negative vega. This means:

- **Long vega**: The position profits when implied volatility rises and loses when it falls. Strategies: long straddles, long strangles, long options, backratios.
- **Short vega**: The position profits when implied volatility falls and loses when it rises. Strategies: [[iron-condor]], [[short-strangle]], [[short-straddle]], [[credit-spread]], [[covered-call]].

## How It Works

### Vega by Moneyness and Time

- **At-the-money (ATM)** options have the highest vega. They are most sensitive to changes in implied volatility because their price is composed almost entirely of extrinsic (time) value, which is directly influenced by IV.
- **In-the-money (ITM)** and **out-of-the-money (OTM)** options have lower vega. Deep ITM options are dominated by intrinsic value (insensitive to IV); far OTM options have little value regardless.
- **Longer-dated options** have higher vega than shorter-dated options. A LEAPS option might have a vega of 0.40, meaning a 1-point IV increase adds $0.40 to the price. A weekly option might have a vega of only 0.05.

### Vega and Implied Volatility Regimes

The practical impact of vega depends heavily on the current volatility environment:

- **Low IV environment (e.g., VIX at 12-15)**: Options are cheap. Long vega positions are inexpensive but may suffer from ongoing theta decay if volatility stays low. A volatility spike delivers outsized returns.
- **High IV environment (e.g., VIX at 30+)**: Options are expensive. Short vega positions earn larger premiums but face the risk of further IV expansion. Mean reversion of volatility tends to favor short vega when IV is elevated.
- **IV crush**: After binary events (earnings, FDA decisions, elections), implied volatility often drops sharply. Traders who are short vega into these events profit from the IV collapse. This is the basis of many earnings strategies.

### Vega vs. Realized Volatility

It is important to distinguish between vega (sensitivity to implied volatility) and the actual profitability of a volatility trade. An option's P&L depends on both the implied volatility at which it was purchased and the [[realized-volatility]] that actually occurs. A long vega position can lose money even if realized volatility is high, if implied volatility was already pricing in that level of movement. The edge in volatility trading comes from correctly predicting the difference between implied and realized volatility.

## Trading Applications

### Volatility Trading

Many professional options strategies are primarily vega trades rather than directional trades:

- **Long vega (buying volatility)**: Purchase straddles or strangles when you believe implied volatility is too low relative to expected future realized volatility. Profits from IV expansion or large realized moves.
- **Short vega (selling volatility)**: Sell premium when you believe implied volatility is too high. Profits from IV contraction (mean reversion) and the underlying staying within expected ranges.
- **[[calendar-spread|Calendar spread]]**: Buy longer-dated options (high vega) and sell shorter-dated options (low vega), creating a net long vega position that profits from IV increases in the back month.

### Earnings and Event Trading

Earnings announcements create a known binary event. Implied volatility typically rises into earnings and collapses after the announcement (regardless of the stock's direction). Traders exploit this pattern:

- **Pre-earnings**: Sell straddles or iron condors to capture the expected IV crush (short vega)
- **Pre-earnings contrarian**: Buy straddles or strangles if you believe the expected move is underpriced (long vega)
- **Post-earnings**: With IV crushed, vega risk is minimal and trades become primarily directional

### Portfolio Vega Management

Professional traders monitor aggregate portfolio vega to understand exposure to a broad volatility shift. A portfolio with -$2,000 vega loses $2,000 for every 1-point increase in IV across all positions. During market stress (when IV can spike 10+ points in a day), unmanaged short vega exposure can produce catastrophic losses.

## Related

- [[options-greeks]]
- [[implied-volatility]]
- [[volatility]]
- [[volatility-smile]]
- [[volatility-skew]]
- [[delta]]
- [[gamma]]
- [[theta]]
- [[black-scholes]]
- [[options]]

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg's chapters on volatility and vega provide the essential framework for understanding volatility-based options trading
