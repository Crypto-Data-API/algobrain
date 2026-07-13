---
title: "Curve Fitting"
type: concept
created: 2026-04-13
updated: 2026-06-20
status: good
tags: [strategy-development, backtesting, overfitting, methodology]
aliases: ["Curve-Fitting", "Curve Fit", "Data Mining"]
domain: [strategy-development]
difficulty: intermediate
prerequisites: ["[[overfitting-detection]]"]
related: ["[[overfitting-detection]]", "[[data-snooping-and-p-hacking]]", "[[walk-forward-analysis]]", "[[hypothesis-to-backtest-workflow]]", "[[edge-taxonomy]]"]
---

# Curve Fitting

Curve fitting is the process of adjusting a strategy's parameters, rules, or filters until it produces good performance on a specific historical dataset. It is the *act* that produces [[overfitting-detection|overfitting]]. Every strategy that has been backtested has been curve-fit to some degree — the question is whether the fit captures *signal* (genuine market regularity) or *noise* (random features of the specific sample).

## The Mechanism

A simple moving average crossover has 2 parameters (fast period, slow period). Testing all combinations from 5-200 on 10 years of SPY data means evaluating ~19,000 parameter pairs. The best pair will have a great backtest — but how much of that greatness is real?

The answer depends on:

1. **How many combinations you tested** — more trials = more opportunities to fit noise. See [[data-snooping-and-p-hacking]]
2. **How many degrees of freedom your model has** — more parameters = more ways to fit the specific sample
3. **Whether the strategy has a theoretical reason to work** — see [[edge-taxonomy]]. A strategy grounded in a real mechanism (behavioral bias, structural flow) is more likely to be capturing signal than one found by pure data mining

## Curve Fitting vs. Legitimate Optimization

Not all parameter tuning is curve fitting. The distinction:

| | Curve Fitting (Bad) | Legitimate Optimization (OK) |
|---|---|---|
| **Motivation** | "Find the parameters that maximize backtest Sharpe" | "Test whether this economically-motivated strategy is robust across reasonable parameter ranges" |
| **Number of tests** | Hundreds or thousands | A handful of pre-specified values |
| **Parameter sensitivity** | Performance collapses with small changes | Performance is stable across a plateau of values |
| **Theory** | Parameters chosen for fit, then rationalized | Parameters derived from theory, then tested |
| **OOS performance** | Much worse than IS | Similar to IS |
| **Example** | "21-day lookback works best on this dataset" | "20-day lookback because that's roughly one trading month, and monthly rebalancing flows are the theoretical mechanism" |

## Common Forms

### Rule Stacking
Adding filters until the backtest looks clean: "buy when RSI < 30 AND MACD crosses AND volume > 2x average AND it's not a Friday AND VIX < 25." Each rule eliminates a few bad trades from the sample — and also eliminates the generalizability.

### Indicator Shopping
Testing 50 indicators until one "works" — moving averages, Bollinger Bands, Ichimoku, Keltner channels, etc. With enough indicators, you will always find one that aligns with your sample. This is [[data-snooping-and-p-hacking|data snooping]].

### Exit Optimization
Fitting take-profit and stop-loss levels to the specific price paths in the sample. A 2.7% stop-loss "works" because it avoids the three big drawdowns in the test period — drawdowns that will be at different levels in the future.

### Regime-Specific Tuning
Fitting different parameters for different market regimes (bull, bear, high-vol, low-vol). Each sub-model now has fewer data points and more degrees of freedom. The regime boundaries themselves become a source of overfitting.

## Illustrative Example (Hypothetical)

The following numbers are illustrative only — they describe the *shape* of curve fitting, not any real backtest.

Suppose a researcher builds a daily mean-reversion strategy on an index ETF. The first version — buy on a 2-day decline, sell after 5 days — produces a modest in-sample Sharpe of about 0.7. Dissatisfied, the researcher begins adding refinements:

1. Add an RSI filter (only buy when RSI < 35). In-sample Sharpe rises to ~1.1.
2. Add a volatility regime filter (only trade when realised vol is below its 60-day median). Sharpe ~1.5.
3. Tune the holding period from 5 days to "whatever maximised the backtest," landing on 7 days. Sharpe ~1.8.
4. Exclude three specific months where the strategy lost (rationalised post hoc as "macro events"). Sharpe ~2.4.

Each step *felt* like an improvement grounded in reasoning, but each one consumed degrees of freedom and quietly fitted the sample. When the same rules are run forward on truly unseen data, the realised Sharpe collapses back toward — or below — the original 0.7, because steps 2-4 captured sample-specific noise rather than a durable mechanism. The lesson: in-sample improvement that arrives by *accretion of conditions* is the signature of fitting, not of discovery.

## How to Detect It

See [[overfitting-detection]] for a comprehensive treatment, including:

- [[walk-forward-analysis|Walk-forward analysis]] — the most practical test; performance is measured only on data the optimiser never saw
- [[purged-kfold-cv|Combinatorial purged cross-validation]] — multiple OOS paths, with purging/embargo to prevent leakage
- [[deflated-sharpe-ratio|Deflated Sharpe ratio]] — corrects the observed Sharpe for the number of trials run
- Parameter sensitivity heatmaps — a robust strategy sits on a broad *plateau*; a curve-fit one sits on an isolated *peak*
- Probability of backtest overfitting (PBO) — estimates how often the in-sample best is below-median out-of-sample

### Quick self-audit checklist

Before trusting a backtest, answer honestly:

- [ ] Can I name the [[edge-taxonomy|edge source]] in one sentence, with who is on the other side?
- [ ] Were the rules and parameters written down *before* I saw the data?
- [ ] How many distinct configurations did I evaluate, total (including the ones I discarded)?
- [ ] Does performance survive small parameter perturbations (±10-20%)?
- [ ] Is out-of-sample performance within a reasonable band of in-sample?
- [ ] Did I add any rule whose only justification is that it improved the backtest?

A "no" to the first two, or a large trial count with no correction, should make the result presumptively suspect.

## The Fundamental Defense

The best defense against curve fitting is not statistical — it's intellectual:

1. **Start with a hypothesis, not a backtest** — see [[hypothesis-to-backtest-workflow]]
2. **Name the edge source** — see [[edge-taxonomy]]. If you can't identify which of the six edge categories your strategy exploits, you are probably fitting noise
3. **Pre-specify** — write down the strategy rules and parameters *before* looking at the data
4. **Use few parameters** — 1-3 is ideal; more than 5 is a red flag
5. **Accept lower in-sample performance** — a robust strategy with Sharpe 1.0 is worth far more than a curve-fit strategy with Sharpe 3.0

> "If you torture the data long enough, it will confess to anything." — attributed to Ronald Coase

## How This Connects to the Rest of the Wiki

Curve fitting is the *act*; [[overfitting-detection|overfitting]] is the *result*; [[data-snooping-and-p-hacking|data snooping]] is the *statistical engine* that makes both inevitable when trial counts are unmanaged. The cure is procedural rather than statistical: the [[hypothesis-to-backtest-workflow|hypothesis-to-backtest workflow]] forces an a-priori mechanism before any optimisation, and the [[research-checklist|research checklist]] gates a strategy before code is written. Once a strategy is live, the same disease reappears as silent decay, which is why [[when-to-retire-a-strategy]] and the broader [[failure-modes|failure-modes taxonomy]] treat "the edge was never real, it was fit" as a first-class cause of death. Disciplined edge identification via [[edge-taxonomy]] is the single best prophylactic — a strategy with a named, structural mechanism can be tuned without being fit.

## Sources

- [[book-advances-in-financial-machine-learning]] — López de Prado on the overfitting pipeline in quantitative research
- [[book-evidence-based-technical-analysis]] — Aronson on rigorous testing of technical analysis claims

## Related

- [[overfitting-detection]] — comprehensive detection methods
- [[data-snooping-and-p-hacking]] — the statistical underpinning
- [[walk-forward-analysis]] — primary validation method
- [[hypothesis-to-backtest-workflow]] — the correct research workflow
- [[research-checklist]] — questions before writing any code
- [[edge-taxonomy]] — naming the mechanism is the best defence against fitting noise
- [[failure-modes]] — "edge was never real" as a strategy-death cause
- [[when-to-retire-a-strategy]] — when post-launch decay confirms the edge was fit
