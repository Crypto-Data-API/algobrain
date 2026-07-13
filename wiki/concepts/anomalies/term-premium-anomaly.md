---
title: "Term Premium Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, bonds, treasuries, quantitative]
aliases: ["Term Premium Anomaly", "Bond Term Premium", "Expectations Hypothesis Puzzle", "Fama-Bliss Anomaly"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[yield-curve]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[carry-anomaly]]", "[[time-series-momentum]]", "[[yield-curve]]"]
---

# Term Premium Anomaly

Long-dated bonds systematically earn higher returns than short-dated bonds — and the excess return exceeds what would be justified if the pure expectations hypothesis of the yield curve held. Equivalently: forward rates are biased predictors of future spot rates, and the bias is large enough to constitute a persistent trading opportunity. Fama & Bliss (1987) documented the pattern cleanly and it has been the foundation of fixed-income carry and roll-down strategies ever since.

## What

Under the pure expectations hypothesis, the forward rate at horizon n should equal the expected future spot rate at horizon n. Fama & Bliss showed that this hypothesis fails: the forward-spot spread (the "forward premium") predicts realized excess bond returns with positive coefficients significantly larger than zero. The historical excess return of rolling 5-year Treasuries over 1-year Treasuries has been roughly 1-2% annualized, with most of the premium earned in the 2-5 year segment of the curve (see Cochrane & Piazzesi 2005 for the refined factor).

## Original Paper

- Fama, E. & Bliss, R. (1987) "The Information in Long-Maturity Forward Rates" — *American Economic Review*
- Cochrane, J. & Piazzesi, M. (2005) "Bond Risk Premia" — *American Economic Review*

## Mechanism

- **Duration risk premium** — long bonds are riskier than short bonds (larger drawdowns, especially in rising-rate regimes) so investors demand a premium for holding them
- **Preferred-habitat / segmented-markets theory** (Modigliani-Sutch, Vayanos-Vila) — different investors have different maturity preferences, and when supply/demand at specific maturities becomes imbalanced, yields must clear with term premia that deviate from expectations
- **Inflation risk premium** — compensation for uncertainty about future real returns

Cochrane-Piazzesi's "tent-shaped" forward-rate factor unified these into a single risk factor that captures most of the time-variation in excess bond returns.

## Edge Category

**Structural** (duration risk premium) + **analytical** (the tent factor is a computable signal).

## Replication Status

Extensively replicated across markets and time samples. One of the more robust anomalies in fixed income. It has a clean theoretical justification (it is essentially a risk premium) and survives most tests.

## Decay History

Persistent but volatile. The term premium shrank dramatically in the 2010s as central banks held rates near zero and flattened curves aggressively. Post-2022 normalization, term premia have partially rebuilt, though they remain below historical averages.

## Current Viability

Tradeable, but sensitive to the rates cycle. Strategies include:

- **Static duration exposure** — long intermediate Treasuries as a carry and roll-down capture
- **Cochrane-Piazzesi timing** — scale duration exposure by the CP factor
- **Curve steepener/flattener** — tactical bets on term premium regimes

Sophisticated macro hedge funds time the term premium rather than holding it statically.

## Related Strategies

- [[carry-anomaly]] — term premium is the fixed-income expression of carry
- [[time-series-momentum]] — often combined with duration positioning
- Bond rolling strategies
- Barbell and laddered bond portfolios

## Sources

- Fama & Bliss (1987) — foundational
- Cochrane & Piazzesi (2005) — modern refinement
- Campbell & Shiller (1991) — expectations hypothesis test
- Ilmanen (2011) "Expected Returns" textbook treatment

## Related

- [[anomalies-overview]]
- [[carry-anomaly]]
- [[time-series-momentum]]
