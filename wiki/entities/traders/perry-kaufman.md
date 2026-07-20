---
title: "Perry Kaufman"
type: entity
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [person, indicators, technical-analysis, quantitative]
entity_type: person
aliases: ["Perry J. Kaufman", "Kaufman"]
website: "https://kaufmansignals.com"
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[kama]]", "[[vidya]]", "[[frama]]", "[[exponential-moving-average]]", "[[simple-moving-average]]", "[[trading-system-design]]", "[[backtesting]]", "[[overfitting]]", "[[regime-detection]]", "[[hurst-exponent]]", "[[tushar-chande]]", "[[john-bollinger]]", "[[john-ehlers]]", "[[alan-hull]]", "[[patrick-mulloy]]", "[[arnaud-legoux]]", "[[mark-jurik]]", "[[technical-analysis]]"]
---

# Perry Kaufman

Perry J. Kaufman (born 1943) is a financial engineer and systematic-trading author who came to markets from aerospace navigation work. They created **Kaufman's Adaptive Moving Average ([[kama|KAMA]])** and its underlying **Efficiency Ratio** in *Smarter Trading* (1995), and wrote *Trading Systems and Methods* — a reference now in its sixth edition and one of the few genuinely comprehensive surveys of systematic trading methods. In the [[stretch-revert]] family, KAMA is the baseline behind `fast_kama_stretch_revert`.

## Key Facts

| | |
|---|---|
| **Name** | Perry J. Kaufman |
| **Born** | 1943 |
| **Education** | BS in Mathematics, University of Wisconsin; MBA, New York Institute of Technology |
| **Pre-trading career** | Aerospace — navigation and control systems for Project Gemini and the Orbiting Astronomical Observatory (predecessor of the Hubble Space Telescope) |
| **Known for** | [[kama\|KAMA]] (Kaufman's Adaptive Moving Average); the Efficiency Ratio |
| **Key roles** | Head of Trading Systems, Transworld Oil Ltd (Bermuda), 1981–1991; principal, Man-Drapeau Research (Singapore), 1992–1998; portfolio manager and senior quantitative analyst, Graham Capital Management, 2003–2008 |
| **Academic** | A founder of the *Journal of Futures Markets*; served on the Director's Committee of Columbia University's Center for the Study of Futures Markets; taught systematic trading at Baruch College |
| **Key books** | *Commodity Trading Systems and Methods* (1978); *Smarter Trading* (1995); *Trading Systems and Methods* (6th ed., 2020); *Alpha Trading*; *A Short Course in Technical Trading* |
| **[[stretch-revert]] baseline** | [[kama\|KAMA]] — `fast_kama_stretch_revert` |
| **Signature theme** | Trading as engineering: measurable, testable, fully specified systems |

## Background

Kaufman began as what they have described as a "rocket scientist," working on navigation and control systems for **Project Gemini** and the **Orbiting Astronomical Observatory** — the predecessor of the Hubble Space Telescope — and programming at the Army Research Laboratory while completing a mathematics degree at the University of Wisconsin. They later did graduate work in astrophysics before moving into markets, and took an MBA from the New York Institute of Technology.

The trading career spanned commercial commodity futures, farm management, and then a series of quantitative roles: Head of Trading Systems at **Transworld Oil Ltd** in Bermuda (1981–1991), principal at **Man-Drapeau Research** in Singapore (1992–1998), and portfolio manager and senior quantitative analyst at **Graham Capital Management** (2003–2008). Alongside the practitioner work they were a founder of the *Journal of Futures Markets*, sat on the Director's Committee of Columbia University's Center for the Study of Futures Markets, and taught a graduate course in systematic trading at Baruch College.

That career shape — aerospace control systems first, markets second — is the same one that produced [[john-ehlers]] (defence electronics) and [[tushar-chande]] (industrial R&D), and it explains a shared instinct across all three: treat the market as a noisy signal, and the trading method as an engineered system whose behaviour must be specified and measured rather than argued about.

## Contributions

### The Efficiency Ratio

Kaufman's most portable idea is not an indicator but a *measurement*: how much of the market's movement is going somewhere.

```
ER = |Price(t) − Price(t−n)|  /  Σ |Price(i) − Price(i−1)|   over the last n bars
     ^ net directional change     ^ total path length travelled
```

The numerator is displacement; the denominator is distance. A perfectly straight trend travels no further than its net change, so ER → 1. Pure chop covers enormous distance and goes nowhere, so ER → 0. Kaufman framed this as the **fractal efficiency** of the price path, and it is conceptually adjacent to the [[hurst-exponent|Hurst exponent]] the [[stretch-revert]] family uses as its [[regime-detection|regime gate]] — both ask whether price movement is persistent or self-cancelling, from different mathematics.

### KAMA

[[kama|KAMA]] uses the Efficiency Ratio to drive an EMA's smoothing constant between a fast bound and a slow bound:

```
SC = [ ER × (fast_α − slow_α) + slow_α ] ²      # typically fast=2, slow=30 periods
KAMA(t) = KAMA(t−1) + SC × (Price(t) − KAMA(t−1))
```

When the market is trending efficiently, the smoothing constant approaches the fast bound and KAMA tracks price closely. When the market is churning, it collapses toward the slow bound and KAMA goes nearly flat — deliberately refusing to chase noise. This makes KAMA one of the canonical [[adaptive-moving-averages|adaptive moving averages]], sharing the era and the ambition with [[tushar-chande]]'s [[vidya|VIDYA]] (1992, volatility-indexed) and later [[john-ehlers]]' [[frama|FRAMA]] (2005, fractal-dimension-indexed).

### Trading Systems and Methods

*Trading Systems and Methods* (Wiley, six editions since the 1978 first edition as *Commodity Trading Systems and Methods*) is a survey rather than an advocacy book: it catalogues indicators, systems, and algorithms with their construction, their variants, and their known weaknesses. Its relevance here is less any single technique than its posture — that a method should be written down completely enough to be [[backtesting|tested]], and that the testing is where most methods die. That is the same posture [[strategy-development]] and [[overfitting]] take in this vault.

## Relevance to this wiki

**Direct dependency.** [[kama|KAMA]] is the baseline behind `fast_kama_stretch_revert`, the [[stretch-revert]] member running on the bot's 1–5 minute fast loop rather than the family's usual 15m bars. That pairing is deliberate and worth stating plainly: on very low timeframes the noise floor is dominated by [[microstructure-noise-low-timeframe|bid-ask bounce]], and an adaptive baseline that *stops moving* when efficiency collapses is exactly the right shape — it declines to define a mean out of pure spread oscillation. Whether that theory survives contact with live fills is untested; the member has not yet traded.

**Indirect dependency, and a warning.** The [[stretch-revert]] family's [[regime-detection|regime gate]] rests on a Hurst-exponent measurement of whether price is trending or mean-reverting. Kaufman's Efficiency Ratio measures a closely related property. This matters because it means an adaptive baseline like KAMA is already doing regime detection *internally*, using a statistic correlated with the gate that sits outside it. The gate and the estimator are not independent tests, and a family that reads as "regime-gated adaptive reversion" is in some measure applying the same idea twice and counting it once.

**Estimator clustering.** KAMA, [[vidya|VIDYA]] ([[tushar-chande]]), and [[frama|FRAMA]] ([[john-ehlers]]) form the *adaptive cluster* among the fourteen baselines: all three vary an EMA's smoothing constant by a measure of how orderly recent price action has been. They differ in what they measure — trend efficiency, volatility, fractal dimension — but they will agree far more often than they disagree. As with the DSP cluster noted on [[john-ehlers]], this cuts against the family's claim that fourteen estimators constitute fourteen independent robustness checks. Genuinely independent confirmation would need members from *different* clusters to be independently profitable, which the current 53-trade sample cannot demonstrate.

## Related

- [[stretch-revert]] — the family whose `fast_kama_stretch_revert` member depends on their work
- [[kama]] — Kaufman's Adaptive Moving Average and the Efficiency Ratio
- [[adaptive-moving-averages]] · [[moving-averages]] — the category KAMA helped define
- [[vidya]] · [[frama]] — the sibling adaptive baselines by [[tushar-chande]] and [[john-ehlers]]
- [[exponential-moving-average]] · [[simple-moving-average]] — the fixed-parameter baselines KAMA adapts
- [[hurst-exponent]] · [[regime-detection]] — the regime measurements the Efficiency Ratio parallels
- [[trading-system-design]] · [[backtesting]] · [[overfitting]] — the discipline *Trading Systems and Methods* teaches
- [[john-ehlers]] · [[tushar-chande]] — the other engineer-to-quant adaptive-indicator designers
- [[john-bollinger]] · [[alan-hull]] · [[patrick-mulloy]] · [[arnaud-legoux]] · [[mark-jurik]] — other estimator authors in this family
- [[technical-analysis]]

## Sources

- Perry J. Kaufman, *Smarter Trading: Improving Performance in Changing Markets* (McGraw-Hill, 1995) — the original KAMA and Efficiency Ratio specification
- Perry J. Kaufman, *Trading Systems and Methods*, 6th edition (Wiley, 2020, ISBN 978-1119605355)
- Perry J. Kaufman, *Commodity Trading Systems and Methods* (1978); *Technical Analysis in Commodities* (1980); *Handbook of Futures Markets* (1984); *Alpha Trading*; *A Short Course in Technical Trading*
- Wikipedia, "Perry J. Kaufman" — https://en.wikipedia.org/wiki/Perry_J._Kaufman (birth year 1943; education; Transworld Oil, Man-Drapeau Research, Graham Capital roles and dates; *Journal of Futures Markets*)
- StockCharts ChartSchool, "Kaufman's Adaptive Moving Average (KAMA)" — https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/kaufmans-adaptive-moving-average-kama (attribution; Efficiency Ratio as fractal efficiency)
- Kaufman Signals — https://kaufmansignals.com

*Verification note: the 1995 attribution of KAMA to* Smarter Trading *is the standard citation and is widely repeated, but* Smarter Trading *itself has not been read for this vault, and the StockCharts reference confirms the attribution without confirming the year. The Baruch College course and Columbia committee service come from secondary biographical summaries rather than a primary source. No source-summary page exists for the Kaufman material in this vault, and no independent backtest of a KAMA baseline has been reviewed here.*
