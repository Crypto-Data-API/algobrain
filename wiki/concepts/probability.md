---
title: "Probability"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [quantitative, risk-management, behavioral-finance]
aliases: ["Probability Theory", "Probability"]
domain: [risk-management, portfolio-theory]
prerequisites: []
difficulty: beginner
related: ["[[expected-value]]", "[[kelly-criterion]]", "[[probability-calibration]]", "[[bayesian-inference]]", "[[power-laws]]", "[[fat-tails]]", "[[gamblers-ruin]]", "[[base-rate-neglect]]"]
---

Probability is the mathematical framework for quantifying uncertainty — assigning numbers between 0 and 1 to the likelihood of outcomes. For a trader, every position is implicitly a probabilistic bet: the question is never "will this go up?" but "what is the probability-weighted distribution of outcomes, and is the price offering me positive [[expected-value|expected value]] against it?" Mastery of probability is the difference between gambling and edge.

## Overview

The two dominant interpretations of probability both matter in markets:

- **Frequentist**: probability is the long-run relative frequency of an event over many repetitions. Useful for backtested strategies with large samples (e.g. "this setup wins 58% of the time over 4,000 trades").
- **Bayesian**: probability is a degree of belief that is updated as evidence arrives via [[bayesian-inference|Bayes' theorem]]. Essential for one-off, non-repeatable events (a Fed decision, an earnings surprise, an ETF approval) where there is no long run to average over. [[prediction-market-calibration|Prediction markets]] price events in this Bayesian, subjective-probability sense.

Most trading reality is Bayesian: you start with a prior, observe a price, news, or order-flow signal, and update.

## Core concepts and formulas

**Expected value** — the probability-weighted average outcome, the foundation of every trading decision:

```
E[X] = Σ p_i · x_i
```

A trade with a 40% chance of +$300 and 60% chance of −$100 has `E = 0.4×300 − 0.6×100 = +$60`. Positive expectancy with controlled variance is the only durable edge.

**Conditional probability and Bayes' theorem** — updating a belief given evidence:

```
P(A | B) = P(B | A) · P(A) / P(B)
```

This is how a trader should revise the probability of, say, a breakout succeeding given that volume confirmed it. Ignoring the prior `P(A)` is the [[base-rate-neglect|base-rate fallacy]] — a pervasive behavioral error (see [[behavioral-finance]]).

**Independence and the gambler's fallacy** — independent events carry no memory; a coin that landed heads five times is still 50/50. Believing otherwise is the [[gamblers-fallacy|gambler's fallacy]]; the opposite error (assuming a streak will continue) is the [[hot-hand-fallacy|hot-hand fallacy]]. Markets are *not* generally independent ([[volatility-clustering]], [[autocorrelation]]), which is precisely what creates exploitable structure.

**Distributions** — the shape of the outcome set matters more than the point estimate. The [[gaussian-assumption|normal distribution]] is mathematically convenient but underestimates extremes; real returns follow [[fat-tails|fat-tailed]] and [[power-laws|power-law]] distributions where rare events dominate P&L. A risk model is only as good as its assumed distribution.

**Variance and risk of ruin** — even a positive-EV strategy can bankrupt a trader if bet sizing ignores variance. The [[gamblers-ruin|gambler's ruin]] problem and the [[kelly-criterion|Kelly criterion]] formalize how to size bets so that compounding works for you rather than driving you to zero.

## Trading relevance

- **Edge = probability × payoff, net of costs.** A 55% win rate is worthless if losers are bigger than winners; a 35% win rate is excellent if winners are 4x losers. Always reason about the full distribution, not the hit rate.
- **Calibration over conviction.** A good trader is *calibrated*: when they say 70%, the event happens ~70% of the time. See [[prediction-market-calibration]] and [[probability-calibration]]. Overconfidence ([[overconfidence-bias]]) is the most expensive probabilistic error.
- **Position sizing is applied probability.** [[kelly-criterion|Kelly]] and fractional-Kelly translate edge and odds into a bet fraction that maximizes long-run geometric growth while bounding ruin.
- **Beware small samples.** A strategy with 30 trades tells you almost nothing; the [[law-of-large-numbers]] needs hundreds to thousands of independent observations before frequencies stabilize. Most "edges" discovered on small samples are noise (see [[backtesting-pitfalls]]).
- **Tail probabilities are systematically underpriced.** Because humans and Gaussian models both underweight extreme moves, options skew and [[tail-risk-hedging|tail hedges]] are often the locus of mispricing.

## Related

- [[expected-value]] — the probability-weighted decision metric
- [[kelly-criterion]] — optimal bet sizing under known edge
- [[bayesian-inference]] — updating probabilities with evidence
- [[probability-calibration]] — whether stated probabilities match reality
- [[power-laws]], [[fat-tails]] — the true shape of return distributions
- [[gamblers-ruin]] — how variance bankrupts positive-EV bettors
- [[base-rate-neglect]] — the most common probabilistic bias in trading

## Sources

- Kahneman, D. *Thinking, Fast and Slow* — base-rate neglect, conjunction fallacy, and human mishandling of probability.
- Thorp, E. *A Man for All Markets* — applied probability, edge, and Kelly sizing in gambling and markets.
- Hull, J. *Options, Futures, and Other Derivatives* — probability distributions in derivatives pricing.
- Bernstein, P. *Against the Gods: The Remarkable Story of Risk* — history of probability and risk measurement.
