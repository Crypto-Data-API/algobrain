---
title: "Deflated Sharpe Ratio"
type: concept
created: 2026-04-10
updated: 2026-06-14
status: excellent
tags: [backtesting, metrics, statistics, validation, performance]
aliases: ["DSR", "Bailey-López de Prado Deflated Sharpe", "Deflated Sharpe"]
domain: [backtesting, statistics]
difficulty: advanced
related: ["[[backtesting-overview]]", "[[sharpe-sortino-calmar]]", "[[probabilistic-sharpe-ratio]]", "[[minimum-track-record-length]]", "[[data-snooping-and-p-hacking]]", "[[selection-bias-research]]", "[[overfitting-detection]]", "[[purged-kfold-cv]]", "[[sharpe-ratio-pitfalls]]"]
---

# Deflated Sharpe Ratio

A correction to the Sharpe ratio that accounts for the number of trial backtests performed, the length of the sample, and the higher moments (skewness and kurtosis) of the return distribution. Introduced by David H. Bailey and Marcos López de Prado in 2014, the deflated Sharpe ratio (DSR) outputs a *probability* (0–1) that an *observed* Sharpe came from a *non-zero true Sharpe* given how many strategy variations were tested. It is the most rigorous single defense against the multiple-testing problem in backtest research.

## Why the Standard Sharpe Is Misleading

A standard Sharpe ratio assumes you ran *one* backtest and want to know whether the result is statistically distinguishable from zero. In practice, researchers run dozens to thousands of backtests and pick the best. The "best of N" Sharpe is biased upward — by construction it has a higher expected value than any individual strategy's true Sharpe. This is the same statistical pathology as p-hacking and selection bias under multiple testing (see [[data-snooping-and-p-hacking]] and [[selection-bias-research]]), and it is the mechanism behind most false discoveries in quantitative finance — a strategy that survives selection on a backtest but fails out of sample (see [[in-sample-vs-out-of-sample]], [[curve-fitting]], [[overfitting]]).

Suppose you run 100 random strategies on the same data. Even if every one has true Sharpe = 0, the *best* one will likely show a high Sharpe purely by chance. Reporting that number as if it came from a single trial is misleading. The DSR formalizes the question: "how much should I deflate the observed Sharpe to undo the selection bias, the sample-length uncertainty, and the non-normality?"

The DSR explicitly corrects for four distinct distortions: **selection bias** (best-of-N), **backtest overfitting**, **sample length** (short track records are noisy), and **non-normality** of returns. (Source: [[deflated-sharpe-ratio|Bailey & López de Prado 2014]])

## Foundation: the Probabilistic Sharpe Ratio

The DSR is not a standalone object — it is the **Probabilistic Sharpe Ratio (PSR)** applied to the multiple-testing case. The PSR, introduced by Bailey and López de Prado in their 2012 paper "The Sharpe Ratio Efficient Frontier" (*Journal of Risk*, Vol. 15, No. 2, Winter 2012/13; SSRN 1821643), answers: given an observed Sharpe over a finite, non-normal sample, what is the probability that the *true* Sharpe exceeds a benchmark `SR*`?

The PSR is:

```
PSR(SR*) = Φ((SR_observed − SR*) × √(n − 1) / σ̂)
```

where the standard error of the Sharpe estimate is

```
σ̂ = √(1 − γ₃ × SR_observed + ((γ₄ − 1)/4) × SR_observed²)
```

Here `n` is the number of returns, `γ₃` is skewness, and `γ₄` is kurtosis (raw, so a Gaussian has γ₄ = 3). A key fact this captures: **skewness and kurtosis do not change the point estimate of the Sharpe ratio, but they substantially change its standard error and therefore its confidence interval.** (Source: [[probabilistic-sharpe-ratio|QuantPy: Probabilistic Sharpe Ratio]])

The **DSR is simply the PSR where the benchmark `SR*` is set to `SR₀(N)`** — the *expected maximum* Sharpe under the null of no skill after `N` independent trials — rather than a fixed threshold like `SR* = 0`. That single substitution is what converts the PSR (a single-trial significance test) into a multiple-testing correction. (Source: [[probabilistic-sharpe-ratio|Wikipedia: Deflated Sharpe ratio]])

## The Formula

The DSR is:

```
DSR = Φ((SR_observed − SR₀(N)) × √(T − 1) / √(1 − γ₃ × SR₀ + ((γ₄ − 1)/4) × SR₀²))
```

Where:
- `Φ` = CDF of the standard normal distribution
- `SR_observed` = the Sharpe ratio you actually computed
- `SR₀(N)` = the *expected maximum* Sharpe under the null of no edge after `N` independent trials (the deflated benchmark)
- `T` = number of return observations
- `γ₃` = skewness of returns
- `γ₄` = kurtosis of returns (raw)
- `N` = number of independent trial backtests

> **Note on the denominator.** The standard-error term in the denominator is evaluated at the benchmark `SR₀`, not at `SR_observed`. This follows from how Bailey and López de Prado specialize the PSR: the variance of the Sharpe estimator is taken under the null whose Sharpe is `SR₀`. Some informal write-ups (including an earlier version of this page) wrote `SR_observed` inside the denominator; that is incorrect. The numerical effect is usually modest, but for negatively-skewed, fat-tailed strategies the choice can matter, so use `SR₀`.

`SR₀(N)`, the expected max Sharpe under the null, is derived from **extreme value theory**: the expected maximum of `N` independent draws from a standard normal grows like `√(2 ln N)`, and the Euler-Mascheroni constant enters the lower-order correction term. Its closed form is:

```
SR₀(N) ≈ √(2 × ln(N)) − ((1 − γ_E) × √(2 × ln(N)) − 1) / √(2 × ln(N))
```

where `γ_E ≈ 0.5772156649` is the Euler-Mascheroni constant. The constant appears precisely *because* `SR₀` models the expected maximum of normally-distributed random variables across multiple independent trials — a classic extreme-value result, not an arbitrary fudge factor. For practical purposes the expression is well approximated by:

```
SR₀(N) ≈ √(2 × ln(N)) − γ_E / √(2 × ln(N))
```

As a rough guide, `SR₀` rises slowly with `N` — order ~2 for hundreds of trials and ~3 for tens of thousands (because the leading term is `√(2 ln N)`, the penalty grows roughly with the square root of the log of the trial count). Treat any specific point value as an approximation to be computed for your own `N`, `T`, and frequency convention rather than a published constant.

The DSR is then the probability that the observed Sharpe exceeds the null expected max — i.e., the probability that the observed Sharpe represents real skill given the number of trials performed.

## Interpretation

- **DSR > 0.95** — strong evidence of real edge after correcting for multiple testing (the 95% confidence level, α = 0.05, one-sided)
- **DSR ≈ 0.5** — no evidence; the observed Sharpe is consistent with the null expected max
- **DSR < 0.05** — the observed Sharpe is *worse* than expected from random trials

A common pass criterion is **DSR > 0.95** (equivalent to a one-sided p-value of 0.05). The choice of confidence level is the analyst's: 0.95 is the conventional default, but allocators who want a higher bar before committing capital sometimes require 0.99, and exploratory screens may tolerate 0.90.

Some illustrative readings of the DSR against the raw Sharpe (Source: [[deflated-sharpe-ratio|Balaena Quant Insights, Issue 24]]):

- **DSR ≈ 0.30 with SR = 2.0** — a high raw Sharpe that nonetheless fails to survive deflation; suggests overfitting or too few data points
- **DSR ≈ 0.85 with SR = 1.0** — a modest raw Sharpe that holds up reasonably; indicates a real but unspectacular edge
- **DSR ≈ 0.97 with SR = 1.5** — a strong, statistically resilient strategy

The pattern is the lesson: a *lower* DSR on a *higher* raw Sharpe is the signature of overfitting, whereas a respectable DSR on a moderate Sharpe is the signature of a genuine edge.

## A Worked Example

You backtest 50 different parameter combinations of a momentum strategy on SPY daily returns over 10 years (T = 2520 trading days). The best performer has:

- Sharpe = 1.5
- Skewness = −0.4
- Excess kurtosis = 2.0 (so raw kurtosis γ₄ = 5.0)

Compute `SR₀` (approximation, computed here for illustration):

```
SR₀(50) ≈ √(2 × ln(50)) − 0.5772 / √(2 × ln(50))
       ≈ √(7.82) − 0.5772 / √(7.82)
       ≈ 2.80 − 0.21
       ≈ 2.59
```

The expected max Sharpe under the null after 50 trials is ≈ 2.59. Your observed Sharpe of 1.5 is *below* the expected max under the null, so the numerator `(SR_observed − SR₀) = (1.5 − 2.59)` is negative, the z-score is negative, and `Φ(z)` is well below 0.5. The DSR is therefore small — there is no evidence of real skill.

Conclusion: even though Sharpe 1.5 looks decent, after accounting for the fact that you tried 50 things, the result is consistent with luck. The strategy should be killed (see [[overfitting-detection]]).

To produce a DSR > 0.95 from 50 trials, the observed Sharpe would need to be substantially higher than 2.59, and the higher-moment correction (the denominator, evaluated at `SR₀`) would penalize the negative skew further. The exact probability is the output of `Φ(z)` from the implementation below; plug in your own numbers to get the precise value.

## What N Should Be

The hardest part of using DSR honestly is choosing N. Some heuristics:

- **Minimum:** every parameter combination you ran
- **Better:** every parameter combination *plus* every variation of the strategy logic you considered
- **Honest:** include strategies you considered but didn't backtest because "they wouldn't work" — the cognitive selection happens whether or not you ran the code
- **Conservative:** multiply your honest N by 2–3 to account for things you've forgotten

When in doubt, overcount. The penalty grows slowly with N (`√ln(N)`), so a 10× overcount of N only modestly increases the penalty. Honest N-counting is also the practical bridge to [[minimum-track-record-length]]: if your DSR fails, MTRL tells you how many more observations you would need before the same Sharpe could clear the bar.

## What If the Trials Aren't Independent?

The DSR formula assumes the N trials are *independent*. In practice they often aren't — variants of the same strategy are highly correlated, so the literal trial count overstates the true breadth of the search. The "effective N" is smaller than the literal N.

An approximate correction: use `N_eff = N × (1 − ρ)` where ρ is the average correlation between trial returns. For highly correlated trials (ρ ≈ 0.9), the effective N is much smaller than the raw count, and the deflation is less severe. This is only a heuristic, however.

López de Prado's **Combinatorial Purged Cross-Validation (CPCV)** framework (see [[purged-kfold-cv]], [[cross-validation]]) provides a more rigorous estimate of effective trials: rather than assuming a correlation, it generates many train/test splits, produces an empirical *distribution* of trial Sharpes, and computes the actual variance of that distribution — from which the effective number of independent trials can be backed out directly. (Source: [[purged-kfold-cv|towards AI: Combinatorial Purged Cross-Validation]])

CPCV builds on **purged k-fold cross-validation**, the technique López de Prado introduced in 2017 to remove overlapping observations and prevent look-ahead leakage in time-series data (see [[lookahead-bias]], [[purged-kfold-cv]]). (Source: [[purged-kfold-cv|Wikipedia: Purged cross-validation]])

## Higher Moments Matter

The denominator of the DSR formula (the Sharpe-estimator standard error, evaluated at `SR₀`) penalizes:

- **Negative skewness** (selling vol, picking up nickels in front of a steamroller): the term `−γ₃ × SR₀` *increases* the denominator when γ₃ < 0, *reducing* the DSR
- **High kurtosis** (fat tails): the term `+((γ₄ − 1)/4) × SR₀²` increases the denominator, reducing the DSR

This is not arbitrary: skewness and kurtosis leave the point estimate of the Sharpe unchanged but widen its confidence interval, which is exactly what a larger standard error encodes. A strategy with apparent Sharpe 2.0 but heavily negative skew and fat tails will have a much lower DSR than a strategy with the same Sharpe but Gaussian returns. The formula's message: "your apparent edge depends on tails that haven't fully shown up yet" (see [[sharpe-ratio-pitfalls]]).

Conversely, a positively-skewed strategy (trend following, long-vol) is penalized less for the same observed Sharpe, because the higher moments suggest the observed performance is more conservative than it looks.

## When to Use DSR

- **Always**, after picking a strategy from a research process that involved multiple trials (it belongs at the end of any [[hypothesis-to-backtest-workflow]])
- **Especially** when reporting a strategy's expected performance to someone making allocation decisions
- **Most especially** when the observed Sharpe is between 1 and 2 — the range where the bias is most likely to be misleading

When *not* to use DSR:
- **Genuine N=1 pre-registered strategies** (rare, but they don't need deflation; the PSR against `SR* = 0` suffices)
- **Live track records** — DSR is for backtests. It corrects backtest selection bias but is inherently **backward-looking** and cannot guarantee future performance. Live, out-of-sample returns remain the ultimate test (see [[in-sample-vs-out-of-sample]], [[walk-forward-analysis]]).

## Limitations

1. **Doesn't fix lookahead bias.** DSR corrects for trial count, sample length, and higher moments, but if your data has leakage, the deflated Sharpe is still wrong — just wrong by less. Combine with [[lookahead-bias]] and [[point-in-time-data]] hygiene.

2. **Doesn't fix survivorship or cost bias.** A backtest that ignores realistic [[transaction-cost-modeling]], [[slippage-modeling]], or — for crypto perps — funding and liquidation effects (see [[crypto-perp-backtesting-pitfalls]]) will still be inflated; DSR does not see those.

3. **Assumes you know N.** Most researchers don't have an honest count, and DSR is only as good as the N you feed it.

4. **Sensitive to higher-moment estimates.** Skewness and kurtosis are noisy in finite samples; a backtest with ~1000 observations has poorly-estimated higher moments.

5. **Asymptotic.** The formula uses asymptotic approximations that are less accurate for very small N or T.

6. **Breaks down for truly fat-tailed strategies.** For strategies whose return distributions are extremely fat-tailed (some long-vol or naked-short profiles), the Gaussian-anchored higher-moment correction can be unreliable. Strong serial correlation in returns and structural breaks in the data-generating process likewise violate the assumptions and can make the DSR misleading.

7. **Backward-looking by construction.** DSR is a statement about a historical sample. It is a necessary filter, not a sufficient guarantee.

Despite the limitations, DSR is the single most useful selection-bias correction available and should be the default reporting standard for any new strategy.

## Implementation

A reference Python implementation. Note the denominator standard-error term is evaluated at `SR₀`, consistent with the corrected formula above:

```python
import numpy as np
from scipy.stats import norm

def deflated_sharpe(sharpe, n_trials, n_observations, skewness=0.0, kurtosis=3.0):
    """
    Compute the deflated Sharpe ratio: P(true SR > expected-max-SR-under-null).

    sharpe:         observed Sharpe ratio (must match the frequency of n_observations)
    n_trials:       number of (effective) independent trial backtests performed
    n_observations: number of return observations (T)
    skewness:       returns skewness (gamma_3)
    kurtosis:       returns kurtosis, raw (gamma_4); Gaussian = 3.0
    """
    euler_gamma = 0.5772156649

    # Expected maximum Sharpe under the null of no skill after n_trials (extreme-value).
    sqrt_2lnN = np.sqrt(2.0 * np.log(n_trials))
    sr0 = sqrt_2lnN - ((1.0 - euler_gamma) * sqrt_2lnN - 1.0) / sqrt_2lnN

    # Sharpe-estimator standard-error term, evaluated at the benchmark SR0.
    denom = np.sqrt(1.0 - skewness * sr0 + ((kurtosis - 1.0) / 4.0) * sr0**2)

    z = ((sharpe - sr0) * np.sqrt(n_observations - 1.0)) / denom
    return norm.cdf(z)
```

## Sources

- Bailey, D. H. & López de Prado, M. (2014). "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality." *Journal of Portfolio Management*, 40(5), 94–107. SSRN 2460551. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551>
- Bailey, D. H. & López de Prado, M. (2012). "The Sharpe Ratio Efficient Frontier" (introduces the Probabilistic Sharpe Ratio and Minimum Track Record Length). *Journal of Risk*, 15(2), Winter 2012/13. SSRN 1821643. <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1821643>
- Wikipedia. "Deflated Sharpe ratio." <https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio>
- Wikipedia. "Purged cross-validation." <https://en.wikipedia.org/wiki/Purged_cross-validation>
- QuantPy. "Is Your Sharpe Ratio Lying to You? Meet the Probabilistic Sharpe Ratio." <https://medium.com/@TheQuantPy/is-your-sharpe-ratio-lying-to-you-meet-the-probabilistic-sharpe-ratio-d06077e423e8>
- towards AI. "The Combinatorial Purged Cross-Validation method." <https://towardsai.net/p/l/the-combinatorial-purged-cross-validation-method>
- Bailey, Borwein, López de Prado, Zhu. "How 'Backtest Overfitting' in Finance Leads to False Discoveries." *Significance* (Royal Statistical Society / Oxford Academic), 18(6), 22. <https://academic.oup.com/jrssig/article/18/6/22/7038278>
- Portfolio Optimizer. "The Probabilistic Sharpe Ratio: Hypothesis Testing and Minimum Track Record Length for the Difference of Sharpe Ratios." <https://portfoliooptimizer.io/blog/the-probabilistic-sharpe-ratio-hypothesis-testing-and-minimum-track-record-length-for-the-difference-of-sharpe-ratios/>
- Balaena Quant Insights, Issue 24. "Deflated Sharpe Ratio (DSR)." <https://medium.com/balaena-quant-insights/deflated-sharpe-ratio-dsr-33412c7dd464>
- [[book-advances-in-financial-machine-learning]] — Marcos López de Prado, Chapters 8 & 14

## Related

- [[backtesting-overview]]
- [[probabilistic-sharpe-ratio]]
- [[minimum-track-record-length]]
- [[sharpe-sortino-calmar]]
- [[sharpe-ratio-pitfalls]]
- [[purged-kfold-cv]]
- [[cross-validation]]
- [[walk-forward-analysis]]
- [[in-sample-vs-out-of-sample]]
- [[data-snooping-and-p-hacking]]
- [[selection-bias-research]]
- [[overfitting]]
- [[overfitting-detection]]
- [[curve-fitting]]
- [[lookahead-bias]]
- [[hypothesis-to-backtest-workflow]]
- [[crypto-perp-backtesting-pitfalls]]
- [[book-advances-in-financial-machine-learning]]
