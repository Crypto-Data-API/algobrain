---
title: "Options Implied Volatility Skew Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [options, volatility, quantitative, derivatives]
aliases: ["Options Implied Vol Skew", "IV Skew Anomaly", "Put-Call Skew Predictability", "Xing-Zhang-Zhao Skew"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[implied-volatility]]", "[[volatility-skew]]"]
difficulty: advanced
related: ["[[anomalies-overview]]", "[[volatility-risk-premium]]", "[[crash-fear-premium]]", "[[volatility-skew]]", "[[skew-trading]]"]
---

# Options Implied Volatility Skew Anomaly

The shape of the equity-option implied-volatility surface — specifically the relative richness of out-of-the-money puts versus at-the-money calls — contains predictive information about subsequent stock returns. Stocks whose OTM puts are unusually expensive relative to their calls subsequently underperform. Xing, Zhang, Zhao (2010) showed this cross-sectional skew signal predicts returns at the 1-month horizon with economically significant magnitudes.

## What

For each stock with listed options, compute a "skew" measure as the difference between the implied volatility of an OTM put (e.g., 10% out-of-the-money) and an ATM call, typically using 1-month expirations:

```
skew = IV(OTM put) − IV(ATM call)
```

Rank stocks by skew. Long low-skew (flat or slightly inverted), short high-skew (steep put-rich curve). The resulting portfolio earned ~1% per month in Xing-Zhang-Zhao's sample, suggesting informed traders are buying OTM puts on stocks they expect to decline.

## Original Paper

Xing, Y., Zhang, X., Zhao, R. (2010) "What Does the Individual Option Volatility Smirk Tell Us About Future Equity Returns?" — *Journal of Financial and Quantitative Analysis*.

Related: Bali & Hovakimian (2009) on the "call-put IV spread" as an alpha signal.

## Mechanism

- **Informed options trading** — traders with private information about upcoming bad news (earnings, M&A failure, FDA rejection) prefer to trade options because of leverage and embedded downside protection. Their demand for protective puts steepens the skew for affected stocks.
- **Hedge-driven demand for puts** — portfolio managers with concentrated exposures buy protective puts on their holdings; the demand is a legitimate hedging signal and provides alpha when the puts become expensive
- **Crash-risk aversion** — related to the [[crash-fear-premium]]: investors overpay for tail protection, but the *cross-sectional* variation in this overpayment is informative

## Edge Category

**Informational** (front-running smart options flow) + some **structural** (hedging pressure).

## Replication Status

Replicated at the individual-stock level and aggregated to market-wide skew indices. Options-based return predictors are one of the more robust areas in empirical finance, likely because the signal comes from a sophisticated trading venue.

## Decay History

Mild decay. The effect is smaller post-publication but still positive. Modern refinements use the full implied-vol surface rather than a single skew point.

## Current Viability

Tradeable by options-capable quant funds. Requires:

- Clean intraday options data (expensive)
- Short-dated (1-month) options chains with sufficient liquidity
- Ability to trade both the underlying and the options cross-section

Retail or small quant funds can approximate the signal using daily-close options data from OptionMetrics or CBOE, though latency and fill quality matter.

Related market-wide signals (CBOE SKEW index, VIX term-structure slopes) have weaker but still-detectable predictive power for broad market moves.

## Related Strategies

- [[volatility-risk-premium]] — selling options earns the average vol premium; skew exploitation is a cross-sectional refinement
- [[crash-fear-premium]] — the broader tail-risk insurance market
- Dispersion trading
- Put-selling overlays with skew-conditional filters

## Sources

- Xing, Zhang, Zhao (2010) — original cross-sectional skew paper
- Bali & Hovakimian (2009) "Volatility Spreads and Expected Stock Returns"
- Bollerslev, Tauchen, Zhou (2009) "Expected Stock Returns and Variance Risk Premia"
- Cremers & Weinbaum (2010) "Deviations from Put-Call Parity and Stock Return Predictability"

## Related

- [[anomalies-overview]]
- [[volatility-risk-premium]]
- [[crash-fear-premium]]
