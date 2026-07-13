---
title: "Data Snooping and P-Hacking"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [strategy-development, statistics, backtesting, methodology]
aliases: ["Multiple Testing Problem", "Backtest Bias", "Selection Bias in Research", "Data Mining", "Data Snooping"]
domain: [strategy-development]
difficulty: advanced
related: ["[[strategy-development-overview]]", "[[deflated-sharpe-ratio]]", "[[probabilistic-sharpe-ratio]]", "[[overfitting]]", "[[overfitting-detection]]", "[[hypothesis-to-backtest-workflow]]", "[[sharpe-ratio-pitfalls]]", "[[walk-forward-analysis]]", "[[purged-kfold-cv]]", "[[selection-bias-research]]", "[[research-checklist]]", "[[live-journal]]"]
---

# Data Snooping and P-Hacking

The single largest source of false positives in trading research. If you have ever generated 100 backtests, picked the best one, and called it a strategy — you have data-snooped. The best one will look amazing. It will not work in production. This page explains why and what to do about it.

## The Core Problem

A backtest's Sharpe ratio is a *random variable*. Even on pure noise, a backtest can produce a high Sharpe by chance. The probability of doing so once is small. The probability of doing so *across many tries* is high.

If you run 1 random strategy, the probability of getting a Sharpe > 2 by chance over a 5-year backtest is roughly 5%. If you run 100 random strategies and pick the best, the *expected* maximum Sharpe is around 2.3 — purely from luck. If you run 1000, it climbs above 3.

This is the multiple comparisons problem applied to finance, and it is the most common reason backtested strategies fail in live trading. The problem is not that researchers are dishonest. The problem is that the math of selection-on-the-best biases the survivor upward, and most researchers never correct for it.

## The Three Ways It Happens

### 1. Explicit Multiple Testing

You write a script that loops over 500 parameter combinations and prints the best one. This is the most obvious form, and the most defensible to correct for, because you know N exactly.

### 2. Sequential Testing

You backtest strategy 1, it doesn't work, you tweak it into strategy 2, that doesn't work, you tweak it into strategy 3, ... eventually you find one that does. You only ran "one" strategy, but the dependent chain of tweaks is statistically equivalent to having run all of them.

This is much harder to correct for because you usually can't reconstruct N. The honest count includes every variant you considered and discarded — including the ones you rejected before running them because "they wouldn't work."

### 3. Community Data Snooping

Someone else tries 1000 strategies on the same data, publishes the best one, and you read the paper. You have not multiple-tested — but the *population of researchers* has. This is why "validated by academic literature" is much weaker than it sounds, especially in finance where the same datasets (CRSP, Compustat) have been mined for decades. See [Harvey, Liu & Zhu (2016) "...and the cross-section of expected returns"][harvey-liu-zhu] for the canonical analysis.

[harvey-liu-zhu]: # "...and the Cross-Section of Expected Returns — Harvey, Liu, Zhu, Review of Financial Studies 2016"

## How Bad Is It?

Bailey and López de Prado (2014) showed that with 5 years of daily data and only 7 trial backtests, the *expected* maximum in-sample Sharpe is approximately 1.0 *under the null hypothesis of no edge*. With 100 trials, the expected max in-sample Sharpe is around 1.9.

In other words: any strategy you find by trying 100 things and picking the best one needs an in-sample Sharpe of approximately 2 just to be statistically *indistinguishable from luck*. To have a real edge, it needs to be substantially higher than that.

This is why the in-sample / out-of-sample gap for selected strategies is usually catastrophic. The in-sample Sharpe is mostly the bias; the out-of-sample Sharpe is what's left after the bias is removed.

The expected best-of-N Sharpe under the null (no edge) is the number every researcher should keep on a sticky note:

| Trials (N) | Expected max in-sample Sharpe (null) | Interpretation of a 2.0 backtest |
|---|---|---|
| 1 | ~0.0 | a real signal |
| 7 | ~1.0 | suggestive at best |
| 100 | ~1.9 | indistinguishable from luck |
| 1000 | ~3.0+ | almost certainly luck |

This is the same multiple-testing arithmetic that appears as Pitfall 4 in [[sharpe-ratio-pitfalls]]; the [[deflated-sharpe-ratio]] is the formal correction that folds N, trial variance, skew, kurtosis, and sample length into a single significance number.

## The Deflated Sharpe Ratio

The deflated Sharpe ratio (DSR), introduced by Bailey and López de Prado, corrects the observed Sharpe for:

1. The number of trials performed (N)
2. The variance of those trials
3. The skewness and kurtosis of the strategy's returns
4. The length of the backtest

The DSR computes the probability that the *observed* Sharpe came from a non-zero true Sharpe given the number of trials. A DSR p-value < 0.05 means: even after accounting for the fact that you tried N things and picked the best, this Sharpe is unlikely to be luck.

See [[deflated-sharpe-ratio]] for the formula and worked example.

The headline finding from Bailey-López de Prado: most published "anomalies" with raw Sharpe ratios in the 0.5-1.0 range fail to clear the DSR significance threshold once trial counts are honestly accounted for.

## Defenses

### 1. Pre-registration

Write down the strategy specification *before* running any backtest. Lock in:
- Universe definition
- Entry rule
- Exit rule
- Position sizing rule
- Parameter values (or the exact range to be tested)
- Sample period
- Statistical test
- Decision rule (what passes, what fails)

Then run the backtest exactly once. Whatever you get is the result. No tweaking.

This is the standard in clinical trials and is the gold standard in finance research. It is also extremely uncomfortable, because most pre-registered ideas don't work — which is exactly the point.

### 2. Hold-Out Sets

Set aside data you do not look at until the end. The honest version is:
- 60% in-sample (research, parameter selection, debugging)
- 20% validation (model selection across competing approaches)
- 20% test (one-shot final evaluation, never re-used)

Critically: once you "use" the test set, you cannot use it again. It is gone. You need fresh data for the next round of research.

Most researchers cheat on this by using the test set, getting a bad number, and then "fixing" the model and re-testing. This converts the test set into another in-sample set and destroys its value. The discipline of *not looking again* is the entire point.

### 3. Walk-Forward Validation

See [[walk-forward-analysis]]. A more efficient use of data than a simple hold-out, because you get out-of-sample evaluation across many periods rather than just one.

### 4. Cross-Validation Done Right

K-fold cross-validation as used in machine learning *doesn't work directly* on financial time series, because of:
- Serial correlation (today's return is correlated with yesterday's)
- Information leakage between adjacent folds
- Non-stationarity (the future doesn't look like the past)

López de Prado's *combinatorial purged k-fold cross-validation* (CPCV) addresses these. See [[purged-kfold-cv]].

### 5. Bonferroni and FDR Corrections

If you tested N strategies and want to claim any of them are significant, multiply your p-values by N (Bonferroni) or use the Benjamini-Hochberg false discovery rate procedure. Crude but defensible.

### 6. Counting Honest N

The hardest part of correction is knowing N. Some heuristics:
- Count every parameter combination you ran
- Count every "minor variation" you tried — they're all trials
- Count strategies you considered but rejected without backtesting (they share the same data)
- Multiply by 2-3 to account for things you've forgotten

When in doubt, overcount. The bias is always toward optimism.

### Defenses compared

| Defense | What it controls | Data cost | Catches sequential p-hacking? | Notes |
|---|---|---|---|---|
| Pre-registration | all forms | none | yes (the only one that does) | uncomfortable; gold standard |
| Hold-out test set | explicit + sequential | high (one-shot) | partly | destroyed once re-used |
| [[walk-forward-analysis]] | non-stationarity, selection | moderate | partly | many OOS windows, efficient |
| [[purged-kfold-cv|CPCV]] | leakage in time series | moderate | partly | k-fold done right for finance |
| Bonferroni / FDR | explicit multiple testing | none | no | crude but defensible; needs known N |
| [[deflated-sharpe-ratio]] | explicit + moments + length | none | no | most accurate single number |
| Honest-N research log | sequential + community | none | enables the count | feeds DSR / Bonferroni |

No single defense is complete. The robust practice is pre-registration *plus* a one-shot hold-out *plus* a deflated-Sharpe check against an honestly-counted N — belt, braces, and a second pair of braces. See [[overfitting]] and [[overfitting-detection]] for the modelling-side companions.

## The File-Drawer Problem

Negative results don't get published — they go in the file drawer. This means the published literature on any topic is biased toward false positives. In trading, your "literature" is the set of strategies you remember trying. The ones that didn't work get forgotten; the ones that almost worked stay in your head and influence future research.

The defense is to *write everything down*. A research log that records every strategy you tried (including the failures) is the only honest way to count N. See [[live-journal]] for a related practice on the production side.

## P-Hacking Specifically

P-hacking is the family of small choices that nudge a marginal result over a significance threshold:

- "Let me try a slightly different lookback window" (and stop when one works)
- "Let me drop this one outlier" (and not the others)
- "Let me restrict to only the years that worked" (regime selection)
- "Let me add a small filter" (overfitting via complexity)
- "Let me change the universe slightly" (selection on the dependent variable)

Each individual choice feels innocuous. Done dozens of times across a research session, they collectively turn noise into "significance." Pre-registration is the only real defense, because it removes the freedom to make these choices retrospectively.

## A Worked Example

Suppose you backtest a single moving-average crossover with parameters (10, 50) on SPY from 2010-2020 and get:
- Sharpe = 0.8
- t-statistic ≈ 2.5
- p-value ≈ 0.012

Looks significant. But you actually tested 50 parameter combinations and chose this one. The Bonferroni-corrected p-value is 0.012 × 50 = 0.6 — *not* significant. The deflated Sharpe ratio (which is more accurate than Bonferroni) gives a similar conclusion: the observed Sharpe is consistent with the null after accounting for trial count.

The honest interpretation: you have not found an edge. You have found the best of 50 random walks.

## The Bottom Line

Three rules:

1. **Count every test you run.** Including the ones you "almost" ran.
2. **Correct for the count.** Use deflated Sharpe, walk-forward, or fresh data.
3. **Pre-register when you can.** It is the only defense against sequential p-hacking.

A strategy that survives honest correction is rare. It is also vastly more likely to be real. The discipline is brutal but the alternative is pretending you have edges you don't have, which is a much more expensive way to learn.

## Sources

- [[book-advances-in-financial-machine-learning]] — López de Prado, especially Chapter 11 on backtest overfitting
- [[book-evidence-based-technical-analysis]] — Aronson on multiple testing in TA research
- Bailey, Borwein, López de Prado, Zhu (2014) "Pseudo-Mathematics and Financial Charlatanism" — *Notices of the AMS*
- Harvey, Liu, Zhu (2016) "...and the Cross-Section of Expected Returns" — *Review of Financial Studies*

## Related

- [[deflated-sharpe-ratio]]
- [[overfitting-detection]]
- [[walk-forward-analysis]]
- [[purged-kfold-cv]]
- [[hypothesis-to-backtest-workflow]]
- [[research-checklist]]
