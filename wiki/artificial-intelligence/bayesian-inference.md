---
title: "Bayesian Inference"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, quantitative, risk-management, volatility]
aliases: ["Bayesian Inference", "Bayesian Statistics", "Bayesian Updating", "bayesian-inference"]
domain: [ai-trading, risk-management]
difficulty: intermediate
prerequisites: ["[[probability]]"]
related: ["[[probability]]", "[[base-rate]]", "[[machine-learning-overview]]", "[[market-regime-detection-ml]]", "[[hidden-markov-model]]", "[[bayesian-optimisation]]", "[[risk-management-overview]]", "[[kelly-criterion]]"]
---

Bayesian inference is a method of statistical reasoning in which beliefs about an unknown quantity are expressed as a probability distribution and updated as new evidence arrives, via **Bayes' theorem**. Rather than producing a single point estimate, it produces a full *posterior distribution* over possible values -- a natural fit for trading, where every parameter (an asset's expected return, a strategy's true Sharpe, the probability a regime has shifted) is uncertain and that uncertainty itself is decision-relevant.

## How It Works

Bayes' theorem combines what you believed before seeing data (the **prior**) with how likely the data is under each hypothesis (the **likelihood**) to produce an updated belief (the **posterior**):

```
posterior ∝ likelihood × prior
P(θ | data) ∝ P(data | θ) × P(θ)
```

- **Prior** P(θ) -- your belief about parameter θ before observing new data (e.g., a weakly-informative prior on a strategy's edge).
- **Likelihood** P(data | θ) -- how probable the observed data is for each value of θ.
- **Posterior** P(θ | data) -- the revised belief, which becomes the prior for the next update.

This sequential updating is what makes Bayesian methods attractive for streaming financial data: each new bar, fill, or earnings print updates the posterior without re-fitting from scratch. Where exact posteriors are intractable, they are approximated with **Markov Chain Monte Carlo (MCMC)** or **variational inference**.

## Trading and Finance Relevance

- **Honest uncertainty about edge** -- a Bayesian estimate of a strategy's Sharpe is a distribution, not a number. The posterior credible interval tells you how much of the apparent edge could be noise -- directly attacking the [[overfitting-in-trading|overfitting]] and small-sample problems that plague naive backtests.
- **The [[base-rate|base-rate]] problem** -- Bayes' theorem is the formal cure for ignoring base rates. A signal with 90% accuracy on a rare event (a 1%-base-rate crash) still produces mostly false positives; Bayesian reasoning makes this explicit.
- **Regime detection** -- Bayesian state-space models and [[hidden-markov-model|hidden Markov models]] estimate the posterior probability that the market is in a given [[market-regime|regime]] (see [[market-regime-detection-ml]]), updating in real time as volatility and correlation shift.
- **Position sizing** -- a posterior over expected return feeds risk-adjusted sizing; combining it with the [[kelly-criterion|Kelly criterion]] (Bayesian Kelly) shrinks bets toward zero when the edge is uncertain, avoiding the over-betting that point-estimate Kelly causes.
- **Bayesian optimisation** -- [[bayesian-optimisation|Bayesian optimisation]] uses a probabilistic surrogate to tune expensive functions (hyperparameters, strategy parameters) with few evaluations, valuable when each backtest is costly.
- **Volatility and parameter shrinkage** -- Bayesian shrinkage pulls noisy estimates (covariance matrices, factor loadings) toward sensible priors, improving out-of-sample portfolio construction over raw sample estimates.

## Bayesian vs Frequentist (for traders)

The frequentist asks "how surprising is this data if there were no edge?" (a p-value). The Bayesian asks "given this data, what is the probability the edge is real, and how big?" The Bayesian framing maps more directly onto trading decisions, naturally incorporates prior knowledge (e.g., that most apparent edges are spurious), and degrades gracefully with small samples -- but it requires choosing a prior, which introduces subjectivity that must be justified and stress-tested.

## Related

- [[probability]] -- the foundation
- [[base-rate]] -- the canonical Bayesian pitfall in signal evaluation
- [[hidden-markov-model]] · [[market-regime-detection-ml]] -- Bayesian regime inference
- [[bayesian-optimisation]] -- Bayesian search over strategy/model parameters
- [[kelly-criterion]] -- position sizing under uncertain edge
- [[machine-learning-overview]] · [[risk-management-overview]]

## Sources

- Gelman et al., *Bayesian Data Analysis* (3rd ed.) -- the standard reference
- López de Prado, *Advances in Financial Machine Learning* (2018) -- on uncertainty quantification and overfitting in financial ML
- E.T. Jaynes, *Probability Theory: The Logic of Science* -- foundational treatment of Bayesian reasoning
