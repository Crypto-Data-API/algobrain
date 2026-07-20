---
title: "Patrick Mulloy"
type: entity
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [person, indicators, technical-analysis, quantitative]
entity_type: person
aliases: ["Patrick G. Mulloy", "Mulloy"]
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[triple-exponential-moving-average]]", "[[dema]]", "[[exponential-moving-average]]", "[[simple-moving-average]]", "[[hull-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[macd]]", "[[tushar-chande]]", "[[john-bollinger]]", "[[john-ehlers]]", "[[perry-kaufman]]", "[[alan-hull]]", "[[arnaud-legoux]]", "[[mark-jurik]]", "[[technical-analysis]]"]
---

# Patrick Mulloy

Patrick G. Mulloy is the author of two 1994 *Technical Analysis of Stocks & Commodities* articles that introduced **DEMA** and **[[triple-exponential-moving-average|TEMA]]** — the double and triple exponential moving averages. Both are lag-cancelling linear combinations of nested [[exponential-moving-average|EMAs]] rather than repeatedly-smoothed averages, and despite the names they respond *faster* than a single EMA, not slower. TEMA is the baseline behind `tema_stretch_revert` in the [[stretch-revert]] family.

> **The biographical record is essentially empty.** Beyond authorship of the two articles and the initial "G.", no reliable information about Mulloy could be verified — no birth year, nationality, education, employer, institutional affiliation, or subsequent publications. This page documents the contribution, which is well-attested, and does not speculate about the person, which is not.

## Key Facts

| | |
|---|---|
| **Name** | Patrick G. Mulloy |
| **Known for** | DEMA (Double Exponential Moving Average) and [[triple-exponential-moving-average\|TEMA]] (Triple Exponential Moving Average) |
| **Primary publication** | "Smoothing Data With Faster Moving Averages," *Technical Analysis of Stocks & Commodities*, V.12:1, January 1994, pp. 11–19 |
| **Companion publication** | "Smoothing Data With Less Lag," *Technical Analysis of Stocks & Commodities*, V.12:2, February 1994, pp. 72–80 |
| **[[stretch-revert]] baseline** | [[triple-exponential-moving-average\|TEMA]] — `tema_stretch_revert` |
| **Biographical record** | Not established — see note above |

## Background

Nothing verifiable is on the public record. Mulloy appears in the *Stocks & Commodities* author archive as the byline on the two 1994 articles below, and their name survives in the indicator documentation of essentially every charting platform, but no biography, affiliation, or later body of work could be confirmed. Unlike [[john-ehlers]] or [[perry-kaufman]], who built companies and long publishing careers around their methods, Mulloy's footprint appears to be the two articles.

This is not unusual for the *Stocks & Commodities* era: the magazine published a large volume of one-off technical contributions from practitioners who never became public figures, and several indicators in daily use today have similarly thin provenance.

## Contributions

### DEMA and TEMA (1994)

The problem Mulloy addressed is the standard one — an [[exponential-moving-average|EMA]] lags by construction — and the solution is to *estimate the lag and subtract it*.

```
EMA1 = EMA(price, n)
EMA2 = EMA(EMA1,  n)
EMA3 = EMA(EMA2,  n)

DEMA = 2 × EMA1 − EMA2
TEMA = 3 × EMA1 − 3 × EMA2 + EMA3
```

The logic: `EMA2` is the EMA of an already-lagged series, so it lags roughly twice as much. The difference `EMA1 − EMA2` therefore approximates the lag error itself, and adding it back to `EMA1` cancels most of it. TEMA extends this to a second-order correction using three nestings, cancelling more lag at the cost of more noise amplification.

The names mislead: neither is a "double-smoothed" or "triple-smoothed" average. Both are **linear combinations with coefficients summing to 1 but with individual terms exceeding 1** (TEMA's are +3, −3, +1), which is precisely what makes them fast — and precisely what makes them overshoot at turning points, since amplified terms amplify curvature error too.

### The two articles

The exact division of labour between the January and February 1994 articles is reported inconsistently in secondary sources. Wikipedia's entries for both DEMA and TEMA credit the **January 1994** article ("Smoothing Data With Faster Moving Averages," V.12:1, pp. 11–19) with introducing both indicators. The **February 1994** follow-up ("Smoothing Data With Less Lag," V.12:2, pp. 72–80) also discusses TEMA and DEMA, applying them to [[macd|MACD]] and to Nasdaq analysis. Some sources instead credit the February article with TEMA specifically.

The safe statement, and the one this vault uses: **Mulloy introduced DEMA and TEMA in a pair of 1994 *Stocks & Commodities* articles**, with January 1994 the standard citation. Neither article has been read for this vault.

## Relevance to this wiki

`tema_stretch_revert` is a simulation-tier member of the [[stretch-revert]] family. Its designated role is that **only sharp extensions register as stretch**: because TEMA tracks price so closely, ordinary drift never produces a large residual, so the member fires rarely and only on violent moves.

That is high precision and near-zero recall — the opposite corner of the design space from [[supersmoother-filter|SuperSmoother]]. Whether it is *useful* depends on whether violent extensions revert more reliably than mild ones, which is an empirical question the family has not answered: the member has not traded.

The exit pathology is the acute case of the one described on [[alan-hull]]. TEMA overshoots more than [[hull-moving-average|HMA]] does, because HMA re-smooths its extrapolated term with a final √n pass and TEMA has no equivalent outer smoothing. So the "residual back through zero" exit is more likely to be triggered by the baseline swinging past price than by price returning to the baseline. Any evaluation of this member must separate the two before drawing conclusions.

Mulloy's TEMA, [[alan-hull]]'s [[hull-moving-average|HMA]], and Ehlers and Way's [[zero-lag-exponential-moving-average|ZLEMA]] form the **lag-cancellation cluster** among the fourteen baselines. All three subtract an estimate of the smoother's own error; all three assume local linearity; all three fail in the same way where curvature is high. Treating them as three independent robustness checks overstates the diversification they actually provide — a point that applies equally to the DSP cluster ([[john-ehlers]]) and the adaptive cluster ([[perry-kaufman]]).

## Related

- [[stretch-revert]] — the family whose `tema_stretch_revert` member depends on their work
- [[triple-exponential-moving-average]] — the indicator, with full mechanics
- [[dema]] — its two-EMA sibling from the same work
- [[exponential-moving-average]] — the building block both nest
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[hull-moving-average]] · [[zero-lag-exponential-moving-average]] — the other lag-cancellers
- [[macd]] — the indicator the February 1994 article applies DEMA/TEMA to
- [[john-ehlers]] · [[perry-kaufman]] · [[alan-hull]] · [[arnaud-legoux]] · [[mark-jurik]] — the other baseline authors in this family
- [[tushar-chande]] · [[john-bollinger]] — indicator designers covered elsewhere in this vault
- [[technical-analysis]]

## Sources

- Patrick G. Mulloy, "Smoothing Data With Faster Moving Averages," *Technical Analysis of Stocks & Commodities*, V.12:1 (January 1994), pp. 11–19 — https://store.traders.com/-v12-c01-smoothi-pdf.html
- Patrick G. Mulloy, "Smoothing Data With Less Lag," *Technical Analysis of Stocks & Commodities*, V.12:2 (February 1994), pp. 72–80 — https://store.traders.com/-v12-c02-smoothi-pdf.html (article title, volume, pages and abstract verified from the publisher's store listing)
- Wikipedia, "Double exponential moving average" — https://en.wikipedia.org/wiki/Double_exponential_moving_average (credits the January 1994 article with introducing both DEMA and TEMA)
- Wikipedia, "Triple exponential moving average" — https://en.wikipedia.org/wiki/Triple_exponential_moving_average
- *Technical Analysis of Stocks & Commodities* author archive, Patrick G Mulloy — https://technical.traders.com/archive/combo/display5.asp?author=Patrick+G+Mulloy

*Verification note: neither article has been read for this vault — only publisher listings and encyclopedia summaries. No biographical detail about Mulloy (birth year, nationality, education, employer, affiliation) could be verified and none is asserted. The January-versus-February attribution of TEMA specifically remains unresolved. No independent empirical evaluation of a TEMA baseline on crypto perpetuals has been reviewed here.*
