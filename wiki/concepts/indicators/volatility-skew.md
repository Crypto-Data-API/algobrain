---
title: "Volatility Skew"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, volatility, indicators]
aliases: ["Volatility Skew", "Vol Skew", "Skew", "Put Skew", "Risk Reversal Skew"]
related: ["[[volatility-smile]]", "[[implied-volatility]]", "[[protective-puts]]", "[[options-pricing]]", "[[black-scholes]]", "[[volatility-surface]]", "[[tail-risk]]", "[[variance-risk-premium]]", "[[options-greeks]]"]
domain: [indicators, derivatives]
prerequisites: ["[[implied-volatility]]", "[[volatility-smile]]"]
difficulty: advanced
---

Volatility skew refers to the pattern in which [[implied-volatility]] (IV) is not uniform across strikes for options of the same expiration, but instead systematically varies -- typically with out-of-the-money (OTM) puts carrying higher IV than at-the-money (ATM) options and OTM calls carrying lower IV. This is the most common shape of the IV curve for equity index options and is sometimes called "put skew" or "negative skew" because the IV curve slopes downward from left (low strikes / puts) to right (high strikes / calls). Skew is closely related to the [[volatility-smile]] but describes the asymmetric version of the pattern that dominates equity markets.

## Why Skew Exists

### Crash Risk Pricing

The primary driver of equity put skew is the market's demand for protection against large downside moves. After the 1987 crash, when the S&P 500 fell 20.5% in a single day, options market makers permanently increased the IV they charge for downside strikes. This was not a temporary reaction -- skew has persisted for nearly four decades because the structural demand for crash protection (from pension funds, insurance companies, and institutional portfolio managers) never goes away. An S&P 500 put at 90% of the current index level might carry IV of 22-28%, while the ATM option shows 16-18%.

### Leverage Effect

When stock prices fall, company leverage (debt-to-equity ratio) mechanically increases, which makes the equity riskier and increases realised volatility. This creates a negative correlation between returns and volatility that is consistent with higher IV at lower strikes. This effect, sometimes called the "leverage effect" or "asymmetric volatility" phenomenon, provides a fundamental economic justification for put skew beyond pure supply and demand.

### Supply and Demand Dynamics

Institutional investors are structurally long equities and structurally long [[protective-puts]] for risk management. This persistent buy-side demand for OTM puts inflates their prices (and therefore their IV). On the call side, covered call writing by yield-seeking funds creates selling pressure that suppresses OTM call IV. The net effect is a steep negative skew.

## Measuring Skew

Skew is commonly quantified in several ways:

- **25-delta skew**: The difference in IV between the 25-delta put and the 25-delta call (same expiration). For the S&P 500, this typically ranges from 4 to 10 volatility points, expanding during market stress.
- **Skew index (SKEW)**: The CBOE publishes a SKEW index derived from S&P 500 option prices. A reading of 100 means the market prices no tail risk; readings above 130 indicate elevated crash-risk pricing. The SKEW index typically ranges from 110 to 150.
- **90-100% skew**: The difference in IV between the 90% moneyness put and the ATM option. A steeper slope indicates more aggressive crash protection pricing.

## Term Structure of Skew

Skew is not constant across expirations. Short-dated skew is typically steeper than long-dated skew because near-term crash risk commands a higher premium per unit of time. A 1-month 25-delta put might show 8 vol points of skew, while the same delta at 12 months might show only 4 vol points. This term structure flattening reflects the market's view that while crashes can happen suddenly, their probability on a per-day basis is relatively small and gets diversified over longer horizons.

During market stress, the entire skew surface can shift dramatically. In the March 2020 COVID crash, S&P 500 1-month 25-delta skew exceeded 20 vol points, roughly triple its normal level.

## Trading Skew

### Skew as a Signal

Elevated skew often precedes or accompanies market declines, as institutional demand for protection surges. However, extremely high skew can also indicate that downside protection is already expensive and the market is already well-hedged, which paradoxically can limit the magnitude of further selloffs. Monitoring changes in skew (rather than its absolute level) is often more informative.

### Skew Trading Strategies

- **Selling put skew** (risk reversals): Sell the expensive OTM put and buy the cheaper OTM call. This profits if skew flattens or the underlying rallies, but carries significant downside risk if a crash occurs.
- **Put spread skew trades**: Buy a closer-to-ATM put (lower IV) and sell a more OTM put (higher IV), structuring the trade so that the higher IV on the short leg subsidises the cost of protection.
- **Skew arbitrage**: Trade mispricings between skew at different expirations or between related underlyings (e.g., single stocks vs. index) using calendar spreads or cross-asset trades.

## Related

- [[volatility-smile]] -- the broader pattern of which skew is the equity-specific manifestation
- [[implied-volatility]] -- the metric that skew describes the variation of
- [[protective-puts]] -- the primary source of demand that drives put skew
- [[options-pricing]] -- the framework in which skew must be accounted for
- [[black-scholes]] -- the model that assumes constant volatility and therefore cannot capture skew
- [[tail-risk]] -- the economic risk that skew prices into the market
- [[volatility-surface]] -- the full strike-and-expiration object that skew is a slice of
- [[variance-risk-premium]] -- the structural premium that downside-put demand feeds into

## Sources

- Rubinstein, M. (1994). *Implied Binomial Trees*. Journal of Finance 49(3). Documents the post-1987 emergence of equity-index skew and the "crashophobia" interpretation.
- Bates, D. (1991). *The Crash of '87: Was It Expected? The Evidence from Options Markets*. Journal of Finance 46(3). Foundational empirical work on crash-risk pricing in option skew.
- Bollen, N. and Whaley, R. (2004). *Does Net Buying Pressure Affect the Shape of Implied Volatility Functions?* Journal of Finance 59(2). Evidence that supply/demand order flow shapes skew.
- Natenberg, S. (1994). *Option Volatility and Pricing*. McGraw-Hill. Practitioner treatment of skew, risk reversals, and skew trading.
- CBOE. *SKEW Index White Paper*. Methodology for the CBOE SKEW index referenced above.
