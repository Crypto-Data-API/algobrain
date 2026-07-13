---
title: "Cboe SKEW Index"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [volatility, indicators, options, risk-management]
aliases: ["SKEW", "Cboe SKEW Index", "Black Swan Index", "cboe-skew", "SKEW Index"]
related: ["[[vix]]", "[[volatility-skew]]", "[[volatility-surface]]", "[[tail-risk]]", "[[universa-investments]]", "[[convex-tail-hedge-arbitrage]]"]
domain: [volatility, risk-management]
prerequisites: ["[[implied-volatility]]", "[[volatility-skew]]"]
difficulty: intermediate
---

The **Cboe SKEW Index** (ticker: SKEW) measures the perceived [[tail-risk]] in [[sp500|S&P 500]] returns over the next 30 days, derived from the prices of out-of-the-money [[sp500|SPX]] options. Often called the "Black Swan Index," it quantifies how much the implied probability distribution of S&P 500 returns deviates from a normal distribution -- specifically, how heavily the market is pricing the left tail.

## Overview

The SKEW Index was introduced by the Chicago Board Options Exchange (Cboe) in February 2011, alongside the existing [[vix|VIX]] index. While the VIX captures the magnitude of expected volatility, SKEW captures the *asymmetry* of that expectation -- the degree to which traders are paying up for downside protection relative to upside exposure.

SKEW is computed from the same SPX option chain used for the VIX, but focuses specifically on the [[volatility-skew|implied-volatility skew]] across out-of-the-money strikes. Higher SKEW readings mean the market is paying disproportionately more for OTM puts than for OTM calls or at-the-money straddles.

## How It's Calculated

SKEW is derived from the third moment (skewness) of the risk-neutral probability distribution implied by SPX option prices, normalized so that:

- **SKEW = 100** corresponds to a perfectly symmetric, normal (Gaussian) return distribution
- **SKEW > 100** indicates a left-skewed distribution -- the market is pricing in a higher probability of a 2- or 3-standard-deviation downside move than a normal distribution would predict
- **SKEW < 100** would indicate a right-skewed distribution (very rare for SPX)

The exact formula uses a portfolio of OTM SPX puts and calls weighted to extract the cubed-deviation moment. In practical terms, SKEW rises when:

- OTM puts become more expensive relative to ATM straddles
- The [[volatility-surface]] steepens on the downside (left wing)
- Institutions bid up tail-hedges

The index is published in real time during market hours.

## Interpretation Range

| SKEW Range | Interpretation |
|------------|----------------|
| ~100 | Returns priced as roughly normal; little tail-risk premium |
| 100-130 | Typical range; modest left-tail premium |
| 130-145 | Elevated tail-risk pricing; institutional hedging active |
| 145+ | Extreme tail-risk pricing; rare regime, often associated with calm-but-anxious markets |

The index has historically traded mostly in the 110-140 band, with multi-year averages near 120-125.

## Historical Context

Notable SKEW peaks include:

- **2017** -- SKEW reached record highs above 150 multiple times during a year of historically low realized volatility, reflecting heavy tail-hedge demand even as VIX traded near all-time lows
- **2018** -- Elevated SKEW preceded the February 2018 "[[volmageddon]]" volatility shock, though SKEW itself did not spike *during* the event (it spiked beforehand and collapsed during the move)
- **2020** -- SKEW behavior during the COVID crash was paradoxical: it actually fell during the crash as OTM puts realized rather than predicted the move; the pre-crash February reading was elevated but not extreme

A persistent finding in academic research is that SKEW is a poor short-horizon predictor of realized crashes despite its "Black Swan Index" nickname.

## SKEW vs VIX

SKEW and VIX measure different aspects of the SPX option surface:

- **VIX** measures the *level* of implied volatility (overall option premium)
- **SKEW** measures the *asymmetry* of implied volatility (relative cost of OTM puts vs. ATM)

The two indices are largely orthogonal -- they can move together or independently. Common regime combinations:

| VIX | SKEW | Interpretation |
|-----|------|----------------|
| Low | Low | Complacent, no hedging |
| Low | High | "Complacent but hedged" -- calm markets where institutions are quietly bidding tail protection |
| High | Low | Acute realized stress; OTM puts becoming less expensive relative to ATM as everything rises in vol |
| High | High | Crisis with continued tail-hedging demand |

The "low VIX, high SKEW" regime is often watched as a warning signal -- it suggests sophisticated players are paying up for crash insurance even as broad volatility measures look benign.

## ITPM Use Cases

For traders running an ITPM-style options portfolio, SKEW is useful for:

- **Timing tail-hedge purchases** -- buying OTM puts when SKEW is depressed (puts are relatively cheap) and trimming when SKEW is extended
- **Identifying skew arbitrage opportunities** -- comparing SKEW levels against historical ranges to size [[risk-reversal]] positions or [[convex-tail-hedge-arbitrage]] trades
- **Detecting institutional fear** -- divergence between SKEW and VIX flags hedging activity invisible in headline volatility
- **Calibrating [[options-premium-selling]] programs** -- selling far-OTM puts is more attractive when SKEW is elevated and the put wing is rich
- **Cross-checking [[volatility-surface]] models** -- a sudden SKEW jump without a VIX move highlights a localized surface deformation

## Limitations

- **Methodology critique** -- the SKEW formula gives heavy weight to far-OTM option prices, which are illiquid and can be distorted by quoting conventions
- **Not a crash predictor** -- despite the "Black Swan" label, empirical work (e.g., research by Bakshi, Kapadia, Madan and follow-ups) shows SKEW has weak predictive power for actual large drawdowns over short horizons
- **Mechanical hedging effects** -- structured product flows and CTA/[[risk-parity]] hedging can push SKEW higher without reflecting genuine tail-risk views
- **Single-asset scope** -- SKEW only covers SPX; comparable skew measures must be computed bespoke for other indices, single names, or commodities
- **Sensitivity to [[volatility-of-volatility]]** -- in low-VIX regimes, small absolute price changes in OTM puts produce large SKEW moves, exaggerating the signal

## Related

- [[vix]] -- the level of expected SPX volatility, computed from the same option chain
- [[volatility-skew]] -- the underlying surface phenomenon SKEW measures
- [[volatility-surface]] -- the broader 2D structure of implied vol across strikes and tenors
- [[tail-risk]] -- the asymmetric downside risk SKEW attempts to quantify
- [[universa-investments]] -- Mark Spitznagel's tail-hedge fund whose approach is closely related to SKEW dynamics
- [[convex-tail-hedge-arbitrage]] -- strategies that exploit mispricing in the SKEW-implied left tail
- [[implied-volatility]]
- [[risk-reversal]]

## Sources

- Cboe SKEW Index methodology white paper (Chicago Board Options Exchange, 2011)
- Bakshi, Kapadia, and Madan, "Stock Return Characteristics, Skew Laws, and the Differential Pricing of Individual Equity Options," *Review of Financial Studies* (2003)
