---
title: "Purged K-Fold Cross-Validation"
type: concept
created: 2026-04-10
updated: 2026-06-14
status: excellent
tags: [backtesting, validation, machine-learning, cross-validation]
aliases: ["Purged CV", "CPCV", "Combinatorial Purged Cross-Validation", "Purged K-Fold"]
domain: [backtesting, machine-learning]
difficulty: advanced
related: ["[[backtesting-overview]]", "[[walk-forward-analysis]]", "[[overfitting-detection]]", "[[deflated-sharpe-ratio]]", "[[in-sample-vs-out-of-sample]]", "[[lookahead-bias]]", "[[probabilistic-sharpe-ratio]]", "[[cross-validation]]", "[[book-advances-in-financial-machine-learning]]"]
---

# Purged K-Fold Cross-Validation

Purged k-fold cross-validation is a time-series-aware validation technique developed in 2017 by Marcos López de Prado (then at Guggenheim Partners and Cornell University) to prevent look-ahead bias in financial backtesting. Standard k-fold cross-validation, the workhorse of machine learning, is broken on financial data because observations violate the independence assumption: overlapping label windows and serial correlation in features let test-set information leak into training. Purged k-fold fixes the leakage by *purging* training observations whose labels overlap the test set and adding an *embargo* buffer; Combinatorial Purged Cross-Validation (CPCV) generalizes this to produce a *distribution* of out-of-sample paths instead of a single point estimate (Source: [[book-advances-in-financial-machine-learning]]; Wikipedia, *Purged cross-validation*).

## Why Standard K-Fold Fails on Financial Data

A standard k-fold CV randomly partitions observations into k folds. For each fold, you train on the other k-1 folds and test on the held-out fold. This assumes independence between observations. Financial data violates independence in two ways (Source: Bhakta, *The Pitfalls of Standard Cross-Validation in Financial Machine Learning*).

### 1. Label Leakage From Overlapping Returns

Suppose you label observation `t` with the next-5-day return: `y_t = (P_{t+5} - P_t) / P_t`. The label at `t` is formed from days `t, t+1, t+2, t+3, t+4`; the label at `t+1` is formed from days `t+1, t+2, t+3, t+4, t+5`. They share days `t+1` through `t+4` — four out of five days, an **80% overlap** of return information — even if `P_t` itself is independent across days.

If observation `t` is in the training fold and `t+1` is in the test fold, the model has effectively seen 80% of the test label during training. Performance is dramatically inflated. The model looks great in CV and breaks in production. This is a concrete instance of [[lookahead-bias]].

This same phenomenon, viewed across the whole sample, is called **label concurrency**: multiple labels depend on overlapping returns, so they are not independent draws. The classic example is the triple-barrier labeling method, where labels at times `t` and `t+1` may resolve over a shared window and therefore share common returns (Source: Hudson & Thames, *Bagging in Financial Machine Learning: Sequential Bootstrapping*; MQL5, *Machine Learning Blueprint Part 4: Label Concurrency*).

### 2. Information Leakage From Features

Features that span multiple time steps (moving averages, momentum, volatility estimates) at time `t` depend on past prices at times `t-1, t-2, ...`. If those past prices are in the test fold, the test feature has been computed from training-fold data. For example, a **63-day rolling volatility** feature computed at the start of a test fold still reflects ~63 days of prices that may sit in an adjacent training fold; the autocorrelation in such features is the mechanism the embargo is designed to break.

The reverse can also happen: a "future" observation in the training set may have been computed using a feature that leaked from the past test fold.

## The Purged K-Fold Solution

Purged k-fold fixes label leakage by removing training-set observations whose label *overlaps* with test-set observations (Source: Bhakta, *The Pitfalls of Standard Cross-Validation in Financial Machine Learning*).

Procedure:
1. Split observations into k contiguous folds (not random)
2. For each test fold, identify training observations whose label formation period overlaps the test window
3. **Purge** those training observations — drop them from training
4. Optionally, **embargo** an additional buffer of training observations *after* the test fold to prevent forward-looking information from leaking back into training

The result: each train/test split is genuinely out-of-sample, with no label or feature leakage at the boundaries. López de Prado treats this in Chapter 7, "Cross-Validation in Finance," of *Advances in Financial Machine Learning* (Source: [[book-advances-in-financial-machine-learning]]).

## The Embargo

Even after purging overlapping labels, there's a subtler problem: serial correlation in features. If your features at time `t` are autocorrelated with features at `t+10`, and `t` is in the test fold while `t+10` is in the next training fold, the model can implicitly memorize the test set.

The embargo is a temporal buffer of observations *after* each test fold that are dropped from the training set. It is typically sized at **1–5% of the dataset** or set to **match the label formation horizon** (Source: QuantInsti, *Cross Validation in Finance*; Wikipedia, *Purged cross-validation*).

- **Concrete sizing example:** with a 5% embargo over 1,000 observations, the **50** data points immediately following each test fold are excluded from training (5% × 1,000 = 50) (Source: Wikipedia, *Purged cross-validation*).
- **Match the label horizon:** for a model predicting price movements "in the next 5 business days," the embargo should be at least **5 business days** to match the label formation horizon (Source: QuantInsti, *Cross Validation in Finance*).
- **Rule of thumb:** the embargo length should be at least as long as the autocorrelation length of your features. Long-lookback features need long embargoes.

## Combinatorial Purged Cross-Validation (CPCV)

A standard k-fold CV produces *one* out-of-sample equity curve. CPCV generalizes this to produce *many*, and is the subject of Chapter 12, "Backtesting through Cross-Validation" (CPCV), in *Advances in Financial Machine Learning* (Source: [[book-advances-in-financial-machine-learning]]).

Procedure:
1. Split data into N contiguous groups
2. Choose k groups to act as the test set in each split
3. Form every possible such choice; the training set in each is the remaining groups, purged and embargoed
4. Run the strategy on each split and record the trades

The number of unique train/test splits is the binomial coefficient:

```
C(N, k) = N! / (k! × (N − k)!)
```

The number of distinct **backtest paths** assembled from those splits is:

```
φ[N, k] = (k / N) × C(N, k)
```

(Source: Towards AI, *The Combinatorial Purged Cross-Validation Method*; Wikipedia, *Purged cross-validation*.)

Across all C(N, k) splits, each observation appears in some training set and in some test set. By stitching test-period predictions together across splits, CPCV produces a *distribution* of out-of-sample equity curves rather than a single point estimate — enormously more informative than walk-forward, which yields only one path.

### Worked path count

For **N = 6 groups** with **k = 2 test groups**:

```
C(6, 2) = 6! / (2! × 4!) = 15 unique train/test combinations
φ[6, 2] = (2 / 6) × 15 = (1/3) × 15 = 5 distinct backtest paths
```

So 15 split runs are reassembled into 5 full-length out-of-sample paths (Source: Wikipedia, *Purged cross-validation*).

## Why Multiple Paths Matter

A single walk-forward curve gives you one Sharpe number. You don't know whether that Sharpe is robust or whether you got lucky on the particular path the data took. CPCV gives you many Sharpes — one per path — and you can compute their empirical distribution. From that distribution you get:

- **Mean OOS Sharpe** — expected performance
- **Standard deviation of OOS Sharpe** — uncertainty about performance
- **Minimum OOS Sharpe** — worst-case path
- **Probability of OOS Sharpe < 0** — failure rate
- **Probability of Backtest Overfitting (PBO)** — see below and [[overfitting-detection]]

These are vastly more useful for sizing a strategy than a single number, and they feed directly into [[probabilistic-sharpe-ratio]] and [[deflated-sharpe-ratio]] inference.

## CPCV, PBO, and the Deflated Sharpe Ratio

CPCV is the practical engine behind two related overfitting diagnostics.

**Probability of Backtest Overfitting (PBO).** Bailey, Borwein, López de Prado, and Zhu introduced PBO in "The Probability of Backtest Overfitting," published in the *Journal of Computational Finance*, Vol. 20(4), pp. 39–69 (2017). The paper proposes **Combinatorially Symmetric Cross-Validation (CSCV)** — a non-parametric procedure that splits performance series into combinatorial in-sample/out-of-sample partitions — as the theoretical foundation for estimating PBO. CPCV operationalizes the same combinatorial idea for full strategy backtests: from its multiple paths you build an empirical distribution of in-sample-selected configurations and measure how often the in-sample best underperforms out-of-sample (Source: Bailey, Borwein, López de Prado & Zhu, 2017, SSRN 2326253).

**Deflated Sharpe Ratio (DSR).** Developed in 2014 by David H. Bailey (Lawrence Berkeley National Laboratory) and Marcos López de Prado (Guggenheim Partners / Cornell University), the DSR corrects an observed Sharpe ratio for the number of trials, non-normality, and sample length, to test whether an apparent edge survives multiple-testing inflation. Its standard form is:

```
DSR = Φ( (SR* − SR₀) · √(T − 1)
          / √(1 − γ̂₃·SR₀ + ((γ̂₄ − 1)/4)·SR₀²) )
```

where `SR*` is the observed (annualized-consistent) Sharpe, `SR₀` is the benchmark/expected-max Sharpe under the null given the number of trials, `T` is the number of returns, `γ̂₃`/`γ̂₄` are skewness/kurtosis, and `Φ` is the standard normal CDF. The CPCV path distribution supplies the inputs needed to set `SR₀` honestly (Source: Bailey & López de Prado, 2014, SSRN 2460551; Wikipedia, *Deflated Sharpe ratio*). See [[deflated-sharpe-ratio]] and [[probabilistic-sharpe-ratio]].

## A Worked Example

Strategy: a mean-reversion model with a 5-day forward return label, on 6 years of daily data.

Setup:
```
N = 6 (one fold per year)
k = 2 (each test set is 2 years out of 6)
Splits  = C(6, 2) = 15
Paths   = φ[6, 2] = (2/6) × 15 = 5
Embargo = 5 days (matching the label length)
```

For each of the 15 splits:
1. Identify 2 of 6 years as the test set
2. Training set = the other 4 years, with observations purged where their 5-day-forward label overlaps any test year
3. Embargo: drop the first 5 days after each test year from training
4. Train the model on the purged/embargoed training set
5. Predict on the test years
6. Record trades and P&L

After all 15 splits:
- Stitch the test predictions from each split into 5 full-length out-of-sample paths
- Compute Sharpe per path → distribution of OOS Sharpes
- Use the distribution (and PBO/DSR derived from it) as your honest estimate

A robust strategy will show a tight, positive Sharpe distribution. An overfit strategy will show a wide distribution with many negative paths even if the mean looks OK.

## CPCV vs. Walk-Forward

| Property | Walk-Forward | CPCV |
|---|---|---|
| Respects time order | Yes | Partially (purging/embargo restore it) |
| Number of OOS paths | 1 | Many (φ[N,k]) |
| Realistic deployment simulation | Yes (refit per window) | No (refit per fold) |
| Good for distributional inference | No | Yes |
| Computationally cheap | Yes | Expensive (many model fits) |
| Honest about parameter drift | Yes | No |
| Overfitting metrics (PBO, DSR) | Weak (one path) | Strong (distribution) |

In practice, **use both**. Walk-forward provides one realistic out-of-sample path suitable for deployment simulation; CPCV provides many paths for distributional inference about robustness. They complement each other and answer different questions. A controlled study, "Backtest Overfitting in the Machine Learning Era: A Comparison of Out-of-Sample Testing Methods in a Synthetic Controlled Environment," found CPCV markedly superior to both K-Fold and Walk-Forward at mitigating overfitting risk, exhibiting **lower PBO and superior Deflated Sharpe Ratio statistics** (Source: SSRN 4686376). See [[walk-forward-analysis]] and [[in-sample-vs-out-of-sample]].

## Sequential Bootstrapping (Advanced Debiasing)

Purging and embargo remove leakage at fold boundaries, but the *interior* of the training set still contains concurrent, redundant labels. López de Prado's complementary fix is **sequential bootstrapping**: rather than sampling training observations uniformly, draw them with probabilities weighted by a **uniqueness score**, so highly redundant (concurrent) observations are sampled less often.

```
Uniqueness = mean( 1 / concurrency ) over the label's timespan
```

where `concurrency` at a given time is the number of labels whose formation windows overlap that time. This produces training samples that behave more like independent draws, improving bagged ensembles (Source: MQL5, *Machine Learning Blueprint Part 4*; Hudson & Thames, *Sequential Bootstrapping*).

## Implementation and Tooling

- **mlfinlab** (Hudson & Thames) provides open-source implementations of `PurgedKFold` and CPCV with embargo support, plus sequential bootstrapping; its Numba-JIT optimization reportedly delivers a ~**30,000×** speedup on the sequential-bootstrap routine versus the naive Python loop (Source: mlfinlab documentation).
- López de Prado discusses these failure modes more broadly in "The 10 Reasons Most Machine Learning Funds Fail," *Journal of Portfolio Management*, Vol. 44, Issue 6 (2018) (Source: jpm.pm-research.com).

## Implementation Gotchas

- **Compute label end times correctly.** The end of label `y_t` is the time at which the label is fully observed (e.g., `t+5` for a 5-day forward return). Purging requires knowing this exact time.
- **Embargo should be ≥ feature autocorrelation length**, not just label length. Long-lookback features (e.g., 63-day volatility) need long embargoes.
- **Purging can dramatically shrink the training set** for small N — use larger N if your label window is long relative to your fold size.
- **Trade information also overlaps.** If the strategy holds positions for h days, trades initiated at time `t` affect P&L through time `t+h`. Purge with this in mind.
- **Watch concurrency in the training interior**, not just at boundaries — sequential bootstrapping addresses this.

## When Not to Use Purged CV

- **Pure cross-sectional strategies** with no label time-window: standard k-fold may suffice
- **Very small datasets** where dropping purged observations leaves nothing usable: walk-forward only
- **Strategies that re-fit constantly** (online learners): walk-forward better matches deployment

## Sources

- [[book-advances-in-financial-machine-learning]] — López de Prado, M. (2018). *Advances in Financial Machine Learning*. John Wiley & Sons, published 21 February 2018, ISBN 978-1-119-48208-6. Chapter 7 ("Cross-Validation in Finance") and Chapter 12 ("Backtesting through Cross-Validation" / CPCV). https://www.oreilly.com/library/view/advances-in-financial/9781119482086/c07.xhtml
- Bailey, D., Borwein, J., López de Prado, M., & Zhu, Q. (2017). "The Probability of Backtest Overfitting." *Journal of Computational Finance*, 20(4): 39–69. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
- Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio." https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
- López de Prado, M. (2018). "The 10 Reasons Most Machine Learning Funds Fail." *Journal of Portfolio Management*, 44(6): 120–133. https://jpm.pm-research.com/content/44/6/120.abstract
- Wikipedia, "Purged cross-validation." https://en.wikipedia.org/wiki/Purged_cross-validation
- Wikipedia, "Deflated Sharpe ratio." https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio
- "Backtest Overfitting in the Machine Learning Era: A Comparison of Out-of-Sample Testing Methods in a Synthetic Controlled Environment." SSRN 4686376. https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4686376_code4361537.pdf?abstractid=4686376&mirid=1
- mlfinlab documentation, "Combinatorial Purged Cross-Validation." https://www.mlfinlab.com/en/latest/cross_validation/cpcv.html
- QuantInsti, "Cross Validation in Finance: Purging, Embargoing, Combinatorial." https://blog.quantinsti.com/cross-validation-embargo-purging-combinatorial/
- Bhakta, "The Pitfalls of Standard Cross-Validation in Financial Machine Learning." https://bhakta-works.medium.com/the-pitfalls-of-standard-cross-validation-in-financial-machine-learning-aec03f672179
- Towards AI, "The Combinatorial Purged Cross-Validation Method." https://towardsai.net/p/l/the-combinatorial-purged-cross-validation-method
- Hudson & Thames, "Bagging in Financial Machine Learning: Sequential Bootstrapping." https://hudsonthames.org/bagging-in-financial-machine-learning-sequential-bootstrapping-python/
- MQL5, "Machine Learning Blueprint (Part 4): Label Concurrency." https://www.mql5.com/en/articles/19850

## Related

- [[backtesting-overview]]
- [[walk-forward-analysis]]
- [[in-sample-vs-out-of-sample]]
- [[overfitting-detection]]
- [[deflated-sharpe-ratio]]
- [[probabilistic-sharpe-ratio]]
- [[lookahead-bias]]
- [[cross-validation]]
- [[data-snooping-and-p-hacking]]
- [[curve-fitting]]
- [[minimum-track-record-length]]
- [[monte-carlo-permutation-test]]
- [[book-advances-in-financial-machine-learning]]
