---
title: "Trading Volatility — Colin Bennett (2014)"
type: source
created: 2026-04-15
updated: 2026-04-28
status: good
tags: [book, education, volatility, options, derivatives, variance-swaps]
source_type: book
source_author: "Colin Bennett"
source_date: 2014
confidence: high
aliases: ["Trading Volatility", "Bennett Volatility"]
related:
  - "[[volatility-trading]]"
  - "[[implied-volatility]]"
  - "[[realized-volatility]]"
  - "[[variance-swap]]"
  - "[[volatility-swap]]"
  - "[[vix]]"
  - "[[volatility-skew]]"
  - "[[options-greeks]]"
---

## Overview

**Trading Volatility: Trading Volatility, Correlation, Term Structure and Skew** by Colin Bennett, published in 2014, is the most comprehensive practitioner reference on the institutional volatility trading business. Bennett — formerly head of European volatility research at Santander and Deutsche Bank — wrote the book initially as an internal handbook for his clients (institutional volatility traders) and later released it as a free PDF that became required reading on volatility desks globally.

Unlike [[option-volatility-and-pricing|Natenberg]], which focuses on directional options trading using vanilla calls and puts, Bennett focuses on the *industrial* volatility trading business: variance swaps, volatility swaps, dispersion trades, correlation trades, term structure plays, and the products institutional vol traders actually use to express pure volatility views. The book's distinguishing feature is that it covers exotic products (variance swaps, conditional variance swaps, gamma swaps, corridor variance swaps) that get one paragraph in most options books.

## Coverage

### Foundations
- Implied vs. realized volatility, vol risk premium, the variance risk premium
- Greeks for vol trading (vega, vanna, volga)
- Why options aren't pure vol exposure (delta, gamma, and the cost of dynamic hedging)

### Variance and Volatility Products
- **[[variance-swap|Variance swaps]]**: The cleanest pure-volatility instrument. Bennett's treatment of replication, fair strike calculation, and the vol/var convexity is canonical.
- **[[volatility-swap|Volatility swaps]]**: Linear in realized vol; harder to replicate but cleaner intuitively.
- **Gamma swaps, conditional variance swaps, corridor variance swaps**: Specialized products for hedging specific exposures.
- **VIX futures and options**: The standardized listed market for vol trading.

### Vol Surface Trading
- **Skew trading**: Selling expensive OTM puts, buying cheaper OTM calls
- **Term structure**: Calendar spreads, vol curve steepeners/flatteners
- **Smile dynamics**: How vol surfaces move when spot moves (sticky-strike vs. sticky-delta)

### Multi-Asset Vol
- **dispersion-trading**: Long single-stock variance, short index variance — earns the implied correlation premium
- **Correlation swaps**: Direct expression of correlation views
- **Cross-asset vol**: FX vs. equity vol, equity vs. credit vol

### Hedging and Tail Risk
- Tail-risk hedging cost analysis
- Optimal hedge construction (puts vs. variance swaps vs. VIX calls)
- Volatility as portfolio insurance

## Key Takeaways

- **Variance swaps are the institutional pure-vol product.** A variance swap pays the difference between realized and implied variance; it's the closest thing to a "vol forward" available. Most institutional vol books are built on variance swaps, not options.
- **The variance risk premium is large and persistent.** Implied variance has historically been 3-5 vol points above realized variance in equity indices. This is the structural source of returns for vol-selling strategies.
- **Dispersion is the institutional volatility flagship trade.** Long single-stock vol / short index vol harvests the implied correlation premium. The trade was crowded, paid handsomely from 2003-2007, blew up in 2008, and remains a core institutional vol strategy.
- **Vol-of-vol and skew dynamics matter.** When equity markets crash, ATM vol rises, OTM put vol rises faster (skew steepens), and vol-of-vol explodes. Strategies that are short any of these get hurt simultaneously.
- **VIX futures are not VIX.** The VIX is a 30-day forward variance; VIX futures are forward expectations of VIX. Term structure dynamics (contango vs. backwardation) drive most VIX-product P&L, not spot VIX moves.
- **Correlation is non-stationary in stress.** Pairwise correlations across stocks and across asset classes converge to 1 in stressed periods. Strategies that rely on stable correlations fail systematically in crashes.
- **Vol is bounded below at zero but unbounded above.** The asymmetric distribution of vol changes makes short-vol strategies look great until they don't. Bennett includes detailed case studies of vol blow-ups (LTCM, 2008, XIV in 2018).
- **Vol products are unwound asymmetrically.** When vol rises, dealers who are short vol need to buy back exposure. The market structure creates feedback loops where rising vol begets rising vol — see "vol-mageddon" (Feb 2018).

## Who Should Read This

Anyone serious about volatility trading. Vol traders at banks, hedge funds, or prop shops will find it the most useful single reference available. Allocators evaluating vol-arbitrage hedge funds will gain a clear picture of what their managers are doing. Quants building vol-based systematic strategies will appreciate the practical detail Bennett provides on product mechanics and replication.

## How It Applies to AI Trading

Bennett's framework is the conceptual scaffolding for systematic volatility trading. Most ML-vol strategies fall into one of the following buckets, all detailed in the book:
- **Variance risk premium harvesting**: Sell variance swaps or short straddles, hedge gamma; ML adds entry/exit timing
- **Vol surface arbitrage**: Detect mispriced points on the vol surface using cross-sectional or time-series features
- **Skew/term-structure plays**: Trade the shape of the surface, not the level
- **Dispersion variants**: ML-enhanced single-stock-vs-index vol baskets
- **Vol regime detection**: Classify regimes (calm, transition, stressed) and apply different strategies in each

For risk management, the book's detailed treatment of vol-of-vol and correlation breakdown is essential. Live vol strategies that don't model these regime dynamics blow up — and Bennett's case studies show exactly how.

## Availability

The original PDF (~470 pages) was distributed free by Santander Investment Bank and is still findable online; the published Wiley edition (2014) is a polished version of the same material.

## Rating

**10/10** — The single best book on institutional volatility trading. No other text covers variance swaps, dispersion, and exotic vol products at this depth and clarity. Pair with [[option-volatility-and-pricing|Natenberg]] for directional options foundations.

## Sources

- Bennett, Colin (2014). *Trading Volatility: Trading Volatility, Correlation, Term Structure and Skew*. Self-published / Wiley.

## Related

- [[volatility-trading]] — The discipline
- [[implied-volatility]] — The forward-looking measure
- [[realized-volatility]] — The backward-looking measure
- [[variance-swap]] — The flagship product
- [[volatility-swap]] — Linear-in-vol companion product
- [[vix]] — Standardized vol index
- [[volatility-skew]] — The shape of the implied vol surface
- [[options-greeks]] — The risk decomposition
- [[option-volatility-and-pricing|Natenberg]] — Directional options companion
