---
title: "Arnaud Legoux"
type: entity
created: 2026-07-20
updated: 2026-07-20
status: stub
tags: [person, indicators, technical-analysis, quantitative]
entity_type: person
aliases: ["Legoux"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[alma]]", "[[weighted-moving-average]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[hull-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[tushar-chande]]", "[[john-bollinger]]", "[[john-ehlers]]", "[[perry-kaufman]]", "[[alan-hull]]", "[[patrick-mulloy]]", "[[mark-jurik]]", "[[technical-analysis]]"]
---

# Arnaud Legoux

Arnaud Legoux is the co-creator, with Dimitrios Kouzis-Loukas, of the **[[alma|Arnaud Legoux Moving Average (ALMA)]]**, released in 2009. ALMA applies a Gaussian weighting kernel that is *shifted* toward recent bars by a tunable offset, decoupling the smoothness/responsiveness trade-off into two independent knobs rather than one period setting. It is the baseline behind `alma_stretch_revert` in the [[stretch-revert]] family.

> **The public record on Legoux is thin.** Beyond co-authorship of ALMA and a general description as working in quantitative finance, no biographical detail could be verified — no birth year, nationality, education, employer, firm, or other published work. This page is deliberately short rather than padded with speculation. Status is `stub` and should stay there until a primary source surfaces.

## Key Facts

| | |
|---|---|
| **Name** | Arnaud Legoux |
| **Known for** | [[alma\|ALMA]] (Arnaud Legoux Moving Average), 2009 |
| **Co-creator** | Dimitrios Kouzis-Loukas (name is also rendered "Dimitris Kouzis-Loukas" and "Dimitrios Douzis-Loukas" across sources — the correct spelling is unresolved) |
| **Stated inspiration** | The Gaussian filter |
| **[[stretch-revert]] baseline** | [[alma\|ALMA]] — `alma_stretch_revert` |
| **Biographical record** | Not established — see note above |

## Background

Not established. Secondary sources — TradingView's own indicator documentation among them — describe Legoux and Kouzis-Loukas as working in quantitative finance and trading, and state that they set out to build a moving average with better smoothness *and* better responsiveness than the alternatives available in 2009. No primary source, personal site, institutional page, or published paper could be located, and no further biographical claim is made here.

ALMA appears to have spread through practitioner channels rather than through a publication: it circulated on trading forums, was implemented in Pine Script and MQL, and is now a built-in overlay on TradingView and most major charting platforms. There is no journal article or book behind it that this vault has identified.

**Dimitrios Kouzis-Loukas** is credited as co-creator on every source consulted. No page exists for them in this vault — the record is too thin to support one, and even the spelling of the name is inconsistent across sources.

## Contributions

### ALMA (2009)

ALMA is a **windowed weighted average with a Gaussian kernel and a phase offset**. Over a window of *n* bars it assigns weights

```
w[i] = exp( −(i − m)² / (2 s²) )        for i = 0 … n−1
m    = offset × (n − 1)                  # where the Gaussian is centred
s    = n / sigma                         # how wide the bell is

ALMA = Σ w[i] × price[i]  /  Σ w[i]
```

with typical defaults of `offset = 0.85` and `sigma = 6`.

The two parameters do genuinely separate things, which is the design's actual contribution:

- **`sigma` controls smoothness.** A wide bell spreads weight across many bars (smooth, laggy); a narrow bell concentrates it (responsive, noisy).
- **`offset` controls lag directly.** At `offset = 0.5` the Gaussian is centred in the window — maximum smoothness, symmetric weighting, and the lag of a centred filter. Pushing it toward `1.0` slides the peak onto the most recent bars, cutting lag without changing the kernel's shape.

Most moving averages force smoothness and lag onto a single period parameter: lengthen the window and you get both more smoothing and more lag. ALMA lets them be tuned somewhat independently. Legoux is reported to have drawn the idea from the Gaussian filter and to have compared ALMA favourably against [[hull-moving-average|HMA]].

The honest caveat: those two extra degrees of freedom are also two extra opportunities for [[overfitting]]. A baseline with `period`, `sigma`, and `offset` has a much larger search space than one with `period` alone, and a backtest that tunes all three is fitting more than it looks like it is.

## Relevance to this wiki

`alma_stretch_revert` is a production-tier member of the [[stretch-revert]] family, and one of only four members with any live trades at the time of writing (7 trades, 71% win rate, +$2.19 — a sample far too small to mean anything).

Its role in the estimator lineup is **low lag while staying smooth** — the corner ALMA's two-parameter design is built to reach. That places it between the lag-cancellation cluster ([[hull-moving-average|HMA]], TEMA, ZLEMA), which achieves speed by subtracting extrapolated error and pays in overshoot, and the DSP cluster ([[laguerre-filter|Laguerre]], [[supersmoother-filter|SuperSmoother]]), which achieves cleanliness by explicit filter design and pays in lag. ALMA gets there by *weighting* instead — a purely feedforward kernel with no recursion, no error subtraction, and therefore no overshoot mechanism.

That makes ALMA structurally the most independent of the fast baselines, which is worth something to the family's diversification argument: unlike TEMA/HMA/ZLEMA, it will not fail at a reversal for the shared linear-extrapolation reason. Whether that independence shows up in the results is untestable at seven trades.

## Related

- [[stretch-revert]] — the family whose `alma_stretch_revert` member depends on their work
- [[alma]] — the indicator, with full mechanics
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[weighted-moving-average]] — the general class ALMA belongs to
- [[simple-moving-average]] · [[exponential-moving-average]] — the conventional alternatives
- [[hull-moving-average]] — the baseline ALMA is most often compared against
- [[laguerre-filter]] · [[supersmoother-filter]] — the DSP-designed alternatives
- [[john-ehlers]] · [[perry-kaufman]] · [[alan-hull]] · [[patrick-mulloy]] · [[mark-jurik]] — the other baseline authors in this family
- [[tushar-chande]] · [[john-bollinger]] — indicator designers covered elsewhere in this vault
- [[technical-analysis]]

## Sources

- TradingView, "Arnaud Legoux Moving Average" — https://www.tradingview.com/support/solutions/43000594683-arnaud-legoux-moving-average/ (co-creation with Kouzis-Loukas; Gaussian-filter inspiration; comparison to HMA)
- TrendSpider Learning Center, "What is the Arnaud Legoux Moving Average Indicator?" — https://trendspider.com/learning-center/what-is-the-arnaud-legoux-moving-average-indicator/ (2009 date; offset Gaussian design)

*Verification note: no primary source authored by Legoux has been located. The 2009 date, the co-creator attribution, and the Gaussian-filter inspiration come from platform documentation and educational secondary sources, not from an original publication. No biographical detail (birth year, nationality, education, employer, firm) could be verified and none is asserted. The co-creator's name is spelled three different ways across the sources consulted. No source-summary page exists for this material, and no independent empirical evaluation of an ALMA baseline on crypto perpetuals has been reviewed here.*
