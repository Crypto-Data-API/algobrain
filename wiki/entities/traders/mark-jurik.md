---
title: "Mark Jurik"
type: entity
created: 2026-07-20
updated: 2026-07-20
status: stub
tags: [person, indicators, technical-analysis, quantitative, machine-learning]
entity_type: person
aliases: ["Jurik", "Mark Jurik (Jurik Research)"]
website: "http://jurikres.com"
related: ["[[stretch-revert]]", "[[moving-averages]]", "[[adaptive-moving-averages]]", "[[jurik-moving-average]]", "[[laguerre-filter]]", "[[supersmoother-filter]]", "[[exponential-moving-average]]", "[[simple-moving-average]]", "[[frama]]", "[[kama]]", "[[vidya]]", "[[overfitting]]", "[[backtesting]]", "[[execution-model-differences]]", "[[paper-to-live-promotion]]", "[[when-to-retire-a-strategy]]", "[[tushar-chande]]", "[[john-bollinger]]", "[[john-ehlers]]", "[[perry-kaufman]]", "[[alan-hull]]", "[[patrick-mulloy]]", "[[arnaud-legoux]]", "[[technical-analysis]]"]
---

# Mark Jurik

Mark Jurik is the founder of **Jurik Research**, a signal-processing and forecasting software firm, and the creator of the **[[jurik-moving-average|Jurik Moving Average (JMA)]]** — a commercial adaptive smoother marketed on the claim that it delivers low lag, high smoothness, and minimal overshoot simultaneously. **The JMA algorithm is proprietary and has never been publicly disclosed.** It is the baseline behind `jma_stretch_revert` in the [[stretch-revert]] family, and the only one of the fourteen that cannot be independently verified.

> **Two thin records, for different reasons.** Jurik's biography is sparse in public sources: the material below comes from Jurik Research's own company page and from secondary summaries, not from independent reporting. And the *technical* record is closed by design — the JMA formula is a trade secret, licensed as a compiled library. Status is `stub` and should stay there.

## Key Facts

| | |
|---|---|
| **Name** | Mark Jurik |
| **Firm** | Jurik Research — founder and owner |
| **Founded** | 1988, Silicon Valley (per the company's own site) |
| **Known for** | [[jurik-moving-average\|JMA]] and the Jurik-smoothed indicator suite |
| **Original domain** | Algorithms for identifying and classifying complex data, including military signal-processing applications; later commercial, industrial and financial |
| **Other work** | Neural-network instruction and the *NeuroTapes* video course; articles in *Futures* magazine and the *Journal of Computational Intelligence in Finance* |
| **Books (reported)** | *Neural Networks and Financial Forecasting* (author); *Computerized Trading* (editor); contributing author, *Virtual Trading* |
| **[[stretch-revert]] baseline** | [[jurik-moving-average\|JMA]] — `jma_stretch_revert` |
| **Algorithm status** | **Proprietary. Never disclosed. Licensed as a compiled library.** |

## Background

Jurik Research was founded in 1988 in Silicon Valley to build algorithms that identify and classify complex data. The company's own account describes signal-processing techniques originally developed for military projects being redirected, after the Cold War, into commercial, industrial and financial applications — forecasting work spanning aluminium futures, natural-gas pumping costs, consumer food demand, and sports results before the focus narrowed mainly to financial markets.

Jurik's own background is described as data modelling and time-series forecasting. They lectured and taught on **neural network technology** for over a decade, produced the *NeuroTapes* video course, and wrote for *Futures* magazine and the *Journal of Computational Intelligence in Finance*. Reported book credits are authorship of *Neural Networks and Financial Forecasting*, editorship of *Computerized Trading*, and a contributing chapter in *Virtual Trading*.

That places Jurik in the same broad generation as [[john-ehlers]] and [[perry-kaufman]] — technical specialists applying engineering and machine-learning methods to price series — but with one decisive difference in how the work was released.

> **Verification note:** jurikres.com serves an invalid TLS certificate (the hostname does not match the certificate's alternative names), so the company and FAQ pages could not be fetched directly. The details above are drawn from the indexed text of jurikres.com/about/company.htm and from secondary summaries. No education, birth year, degrees, or military-contract specifics are asserted, as none could be confirmed.

## Contributions

### The Jurik Moving Average

JMA is marketed as resolving the trade-off every other smoother is forced to accept. Conventional filter design says lag, smoothness, and overshoot are coupled: buy less of one, pay in another. Jurik Research's claim is that JMA delivers low lag, high smoothness, *and* minimal overshoot at the same time, tuned by a small number of exposed parameters (typically period, a "phase" control, and a power/smoothing control).

**No formula has ever been published.** JMA ships as a compiled add-in for charting platforms and is sold under licence. Everything in circulation describing "how JMA works" falls into two categories:

1. **Behavioural claims and exposed parameters** — what Jurik Research states the filter does, and which knobs a user can turn.
2. **Reverse-engineered approximations** — the "JMA" implementations found in TradingView Pine scripts, MQL4/MQL5 code, Python packages, and forum PDFs. These are *not* the algorithm. They are guesses fitted to observed output, **and they do not agree with one another.**

Reported development dates vary in secondary sources — an early adaptive average (JAMA) around 1994, with JMA appearing around 1999 — and none of these dates could be confirmed. See [[jurik-moving-average]], which presents no formula, because presenting one would be fabrication.

## Relevance to this wiki

`jma_stretch_revert` is a production-tier member of the [[stretch-revert]] family, chosen for noise rejection. It is also **the family's single reproducibility hole**, and that is the point of this page.

**A strategy built on a closed-source baseline cannot be independently audited.** Concretely, for `jma_stretch_revert`:

- **The backtest cannot be trusted to match live.** The family's validation plan is to replay all fourteen estimators over identical historical bars. If the backtest engine and the live bot use different JMA implementations — and given that every public implementation is a different approximation, they very likely do — then the historical residuals and the live residuals are computed from *different filters*. That is [[execution-model-differences|backtest-to-live divergence]] introduced at the signal layer, before execution costs are even considered, and it silently invalidates any [[paper-to-live-promotion|paper-to-live promotion]] decision for this member.
- **A result cannot be attributed.** If `jma_stretch_revert` outperforms, there is no way to determine whether the edge came from JMA's actual filter properties or from an artifact of whichever approximation was used. The finding is not reproducible by anyone else, including this vault's future self.
- **A failure cannot be diagnosed.** When a published baseline misbehaves, the formula can be inspected and the cause derived — this is exactly how the overshoot pathology in [[hull-moving-average|HMA]] and [[triple-exponential-moving-average|TEMA]] is understood without needing any experiment. With JMA, a bad run yields no explanation, only an observation.
- **[[when-to-retire-a-strategy|Retirement criteria]] lose their meaning.** Kill rules assume that when a strategy stops working you can ask *why* and decide whether the edge decayed or the implementation drifted. JMA permits neither question.

This is the direct contrast with [[john-ehlers]], whose four contributions to the same family — [[frama|FRAMA]], [[laguerre-filter|Laguerre]], [[supersmoother-filter|SuperSmoother]], [[zero-lag-exponential-moving-average|ZLEMA]] — are fully specified in books and free papers, and can be checked line by line against any implementation. In a vault whose central methodological concern is [[overfitting]] and unverifiable results, **auditability is a property of the baseline itself**, not a nice-to-have.

None of this is an accusation that JMA is bad. It may well be an excellent filter; the behavioural claims are plausible and Jurik Research has sold it for decades. The point is narrower and unavoidable: **a claim that cannot be checked cannot be relied on**, and a member of a strategy family whose stated purpose is *defence in depth against estimator-specific artifacts* is a poor fit when its estimator is the one artifact nobody can inspect.

## Related

- [[stretch-revert]] — the family whose `jma_stretch_revert` member depends on their work
- [[jurik-moving-average]] — the indicator, and the full reproducibility argument
- [[laguerre-filter]] · [[supersmoother-filter]] — the published DSP alternatives in the same group
- [[frama]] · [[kama]] · [[vidya]] — the published adaptive alternatives
- [[moving-averages]] · [[adaptive-moving-averages]] — the estimator landscape
- [[exponential-moving-average]] · [[simple-moving-average]] — the conventional baselines
- [[overfitting]] · [[backtesting]] · [[execution-model-differences]] · [[paper-to-live-promotion]] · [[when-to-retire-a-strategy]] — the validation machinery a closed baseline defeats
- [[john-ehlers]] — the reproducibility counterexample; four published baselines in the same family
- [[perry-kaufman]] · [[alan-hull]] · [[patrick-mulloy]] · [[arnaud-legoux]] — the other baseline authors
- [[tushar-chande]] · [[john-bollinger]] — indicator designers covered elsewhere in this vault
- [[technical-analysis]]

## Sources

- Jurik Research, "Contact & About" — http://jurikres.com/about/company.htm (founded 1988, Silicon Valley; military-to-commercial signal processing; Jurik's forecasting background; NeuroTapes; *Futures* magazine and *Journal of Computational Intelligence in Finance* articles; book credits)
- Jurik Research, "FAQs on Jurik's JMA" — http://jurikres.com/faq1/faq_ama.htm
- Jurik Research product catalogue, JMA — http://jurikres.com/catalog1/ms_ama.htm

*Verification note: jurikres.com returns a TLS hostname/certificate mismatch and could not be fetched directly; the details above come from the site's indexed text and secondary summaries. Mark Jurik's education, birth year, and any specific military contracts are unverified and are not asserted. The JAMA (~1994) and JMA (~1999) dates are reported inconsistently in secondary sources and are not treated as established. No source-summary page exists for this material, and no independent empirical evaluation of a JMA baseline on crypto perpetuals has been reviewed here — nor, given the closed algorithm, could one be replicated if it existed.*
