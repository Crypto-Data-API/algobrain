---
title: "Alan Hull"
type: entity
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [person, indicators, technical-analysis, education]
entity_type: person
aliases: ["Hull", "Alan Hull (trader)"]
website: "https://alanhull.com"
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[hull-moving-average]]", "[[weighted-moving-average]]", "[[simple-moving-average]]", "[[exponential-moving-average]]", "[[triple-exponential-moving-average]]", "[[zero-lag-exponential-moving-average]]", "[[alma]]", "[[false-signals]]", "[[tushar-chande]]", "[[john-bollinger]]", "[[john-ehlers]]", "[[perry-kaufman]]", "[[patrick-mulloy]]", "[[arnaud-legoux]]", "[[mark-jurik]]", "[[technical-analysis]]"]
---

# Alan Hull

Alan Hull is an Australian trader, author, and market educator based in Victoria, best known for creating the **[[hull-moving-average|Hull Moving Average (HMA)]]** in 2005. The HMA came out of a side-quest: while working on a different indicator they were sidetracked by the problem of lag in moving averages, and the solution — nesting weighted moving averages so that one's lag cancels another's, then re-smoothing over the square root of the period — has since been implemented in charting platforms worldwide. In the [[stretch-revert]] family it is the baseline behind `hma_stretch_revert`.

## Key Facts

| | |
|---|---|
| **Name** | Alan Hull |
| **Nationality** | Australian |
| **Based** | Victoria, Australia (contact address: Warrandyte, Victoria) |
| **Known for** | [[hull-moving-average\|Hull Moving Average]] (2005) |
| **Background** | Mathematics plus early IT experience; four decades trading and investing |
| **Books** | *Active Investing*; *Trade My Way*; *Invest My Way* |
| **Contributed to** | Martin Roth's *Top Stocks* series; Daryl Guppy's *Better Stock Trading*; Jim Berg's *Shares to Buy and When*; *The Wiley Trading Guide* |
| **Presents for** | Australian Securities Exchange (ASX); Australian Technical Analysts Association (ATAA); Australian Investors Association (AIA) |
| **Publications** | Newsletters including the ActVest range and a weekly blue-chip report |
| **[[stretch-revert]] baseline** | [[hull-moving-average\|HMA]] — `hma_stretch_revert` |
| **Website** | https://alanhull.com |

## Background

Hull's own account has them buying their first stock at age eight — bought for them by their father, also a trader and investor — with that early exposure turning into decades of market work. They describe combining a mathematical background with early IT experience and roughly four decades of trading and investing, and they are a well-established figure in the Australian retail investing scene, writing for and presenting to the ASX, the Australian Technical Analysts Association, and the Australian Investors Association.

Their published output is aimed squarely at self-directed Australian investors: three authored books (*Active Investing*, *Trade My Way*, *Invest My Way*), contributions to several other Australian trading volumes, and a subscription newsletter business. Note the scope boundary — most of that work concerns Australian equity investing, which is out of scope for this vault. What is in scope is the indicator.

> **Note:** Hull's work sits mostly in equity investing, which this vault's scope rules exclude. This page exists solely because the HMA is a [[stretch-revert]] baseline; the equity material is mentioned for biographical accuracy and is not developed here.

## Contributions

### The Hull Moving Average (2005)

The HMA attacks lag by arithmetic cancellation rather than by adaptation. Given period *n*:

```
HMA(n) = WMA( 2 × WMA(price, n/2) − WMA(price, n),  √n )
```

The inner term `2 × WMA(n/2) − WMA(n)` is a linear extrapolation: it takes a fast weighted average and pushes it further in the direction the slow one says the trend is going, cancelling most of the lag under a locally linear trend. Because that subtraction amplifies noise, the result is then re-smoothed by a short **√n**-period [[weighted-moving-average|WMA]] — long enough to restore visual smoothness, short enough not to reintroduce the lag just removed.

The result is among the fastest-responding common moving averages, with near-zero lag under a straight trend. The price is **overshoot at turning points**: the extrapolation assumes linearity, so where curvature is high the HMA continues past the turn before correcting. That is not a flaw so much as the direct cost of the design, and it is the property that matters most for how the HMA behaves as a mean-reversion baseline.

Structurally, the HMA belongs to the **lag-cancellation cluster** of [[stretch-revert]] baselines, alongside [[patrick-mulloy]]'s [[triple-exponential-moving-average|TEMA]] and Ehlers and Way's [[zero-lag-exponential-moving-average|ZLEMA]]. All three subtract an estimate of the smoother's own error; all three overshoot at reversals for the same reason.

## Relevance to this wiki

`hma_stretch_revert` is one of the [[stretch-revert]] family's ten production-tier members. Its role in the estimator lineup is to **flag stretch early**: because the HMA hugs price closely, a given absolute deviation registers sooner than it would against a laggier baseline.

Two consequences follow, and the second is the one worth watching.

**Entry.** An early-flagging baseline generates more candidate stretches. Some of those are genuine dislocations caught sooner, which is the point; others are ordinary wobbles that a slower baseline would never have called extreme. This is a precision/recall trade, and where it lands depends entirely on the [[false-signals|false-signal]] rate in the traded book — thin alt perps punish it hardest.

**Exit, and this is the subtle failure.** The family's exit rule is "residual back through zero." With an overshooting baseline, that condition can be satisfied by *the baseline moving* rather than by *price reverting*. At a genuine turn the HMA extrapolates past the price, the residual crosses zero, and the trade is closed — potentially a bar or two before the reversion it was actually waiting for. The entry thesis can be correct and the exit rule cashes out anyway. Any read of `hma_stretch_revert`'s win rate needs to first audit whether exits were driven by price or by baseline; see [[hull-moving-average]] for the full treatment and [[triple-exponential-moving-average]] for the more acute version of the same pathology.

More broadly, Hull's HMA is the clearest illustration in the family of *why the estimator is the strategy*. It and [[supersmoother-filter|SuperSmoother]] sit at opposite corners of the design space — fast and overshooting versus late and clean — and will disagree about whether a given bar is stretched at all. That disagreement is the entire reason for running fourteen baselines, and also the reason the best-performing one cannot be taken at face value without deflation.

## Related

- [[stretch-revert]] — the family whose `hma_stretch_revert` member depends on their work
- [[hull-moving-average]] — the indicator
- [[weighted-moving-average]] — the building block the HMA nests
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[triple-exponential-moving-average]] · [[zero-lag-exponential-moving-average]] — the other lag-cancellers, same overshoot pathology
- [[simple-moving-average]] · [[exponential-moving-average]] — the conventional alternatives
- [[alma]] — the other weighting-scheme (rather than filter-theory) baseline
- [[false-signals]] — the risk an early-flagging baseline amplifies
- [[patrick-mulloy]] · [[john-ehlers]] · [[perry-kaufman]] · [[arnaud-legoux]] · [[mark-jurik]] — the other baseline authors in this family
- [[tushar-chande]] · [[john-bollinger]] — indicator designers covered elsewhere in this vault
- [[technical-analysis]]

## Sources

- Alan Hull, official site — https://alanhull.com and the "About Alan Hull" page (creator of the HMA; author of *Active Investing*, *Trade My Way*, *Invest My Way*; first stock at age eight; ASX/ATAA/AIA presenting; Warrandyte, Victoria contact address)
- Alan Hull, "The Hull Moving Average" — https://alanhull.com/the-hull-moving-average/ (2005 origin; the lag side-quest account)
- Traders Union biography of Alan Hull — https://tradersunion.com/persons/alan-hull/ (Melbourne base; four decades of experience; ActVest newsletter)

*Verification note: no birth year, formal qualifications, or company registration details are asserted here — none were confirmed. "Four decades of experience" and "mathematical background with early IT expertise" are Hull's own self-description from their About page, not independently verified. The HMA's 2005 origin is Hull's own account. No independent empirical evaluation of the HMA has been reviewed for this vault, and no source-summary page exists for this material.*
