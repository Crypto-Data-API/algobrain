---
title: "Monte Carlo Simulation"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [quantitative, backtesting, risk-management, derivatives, volatility, methodology]
aliases: ["Monte Carlo Simulation", "monte-carlo-simulation", "Monte Carlo", "MC Simulation"]
domain: [quantitative, risk-management, backtesting]
difficulty: intermediate
related: ["[[value-at-risk]]", "[[expected-shortfall]]", "[[backtesting]]", "[[monte-carlo-backtesting]]", "[[monte-carlo-permutation-test]]", "[[options-pricing-models]]", "[[black-scholes]]", "[[binomial-model]]", "[[risk-of-ruin]]", "[[position-sizing]]", "[[random-walk-theory]]", "[[black-swan]]"]
---

# Monte Carlo Simulation

Monte Carlo simulation is a computational method that estimates the range of possible outcomes of an uncertain process by running a large number of random trials and reading off the resulting distribution. Instead of solving a problem analytically, you build a model of the process, feed it randomly sampled inputs many thousands of times, and treat the collected outputs as an empirical approximation of the true answer. It is the workhorse technique for problems where a closed-form solution is intractable — path-dependent option payoffs, multi-asset portfolio risk, and long-horizon wealth projections all fall into this category.

The name comes from the Monte Carlo casino: the method was developed by Stanislaw Ulam, John von Neumann, and others on the Manhattan Project in the 1940s to model neutron diffusion, and named for the role of chance in its sampling. In finance it is used any time the quantity of interest is a *distribution* rather than a single deterministic number.

## How It Works

A Monte Carlo simulation has four steps, regardless of application:

1. **Specify the model and input distributions.** Write down how outputs depend on inputs (the pricing formula, the equity-curve update rule, the portfolio return equation) and assign a probability distribution to each uncertain input — for example, asset returns drawn from a normal, log-normal, or empirically bootstrapped distribution.
2. **Draw many random samples.** Use a random number generator to draw one value (or one entire path) per input, then evaluate the model to produce one outcome. Repeat this `N` times, where `N` is typically in the thousands to millions.
3. **Aggregate the outputs.** Collect the `N` results into an empirical distribution — a histogram of everything that could happen and how often.
4. **Read the answer off the distribution.** Extract whatever summary the problem calls for: the mean (expected value), a percentile (e.g. the 5th-percentile loss for [[value-at-risk]]), a tail average ([[expected-shortfall]]), or the probability of a threshold event (probability of ruin, probability of hitting a return target).

### Why it converges

Monte Carlo rests on the **law of large numbers**: as the number of trials `N` grows, the sample average converges to the true expected value. The **central limit theorem** tells you *how fast*: the standard error of a Monte Carlo estimate shrinks in proportion to `1/√N`. This has an important, often frustrating consequence — to halve the error you must **quadruple** the number of simulations. Getting one more decimal digit of accuracy costs roughly 100× the compute. This slow convergence is the method's defining practical limitation and the reason variance-reduction techniques exist.

### Random vs quasi-random sampling

Standard Monte Carlo uses **pseudo-random** numbers. A refinement, **quasi-Monte Carlo**, replaces them with *low-discrepancy sequences* (Sobol, Halton) that fill the sample space more evenly and can converge closer to `1/N` than `1/√N` for smooth, low-dimensional problems. It trades some of the clean statistical error bars of true randomness for faster convergence.

### Variance-reduction techniques

Because error falls only as `1/√N`, practitioners reduce the *variance* of the estimator rather than just throwing more paths at it:

- **Antithetic variates** — for each random draw `z`, also evaluate its mirror `-z`. The two negatively correlated paths average to a lower-variance estimate.
- **Control variates** — subtract off the error of a related quantity whose true value is known analytically (e.g. price a complex option and use a vanilla option with a [[black-scholes]] closed form as the control).
- **Importance sampling** — deliberately over-sample the rare region that dominates the answer (deep tail losses, far out-of-the-money payoffs), then re-weight. Essential for estimating rare-event probabilities efficiently.
- **Stratified / Latin hypercube sampling** — partition the input space and sample each stratum, avoiding accidental clumping.

## Applications in Finance and Trading

### Option and derivative pricing

The most established use. When a derivative's payoff is **path-dependent** — Asian options (average price), barrier and lookback options, many exotics and structured products — there is often no closed-form solution like [[black-scholes]]. Monte Carlo simulates thousands of underlying price paths (typically under [[geometric-brownian-motion]] or a stochastic-volatility model), computes the payoff along each path, and averages the discounted payoffs to get the price. See [[options-pricing-models]] and, for the lattice alternative, the [[binomial-model]].

### Value-at-Risk and tail risk

**Monte Carlo VaR** simulates thousands of possible portfolio outcomes over a horizon by drawing correlated moves across all positions, then reads the loss at a chosen percentile (e.g. the 1st or 5th). Unlike the parametric (variance-covariance) method, it can handle non-linear instruments like options and non-normal return assumptions. It complements [[value-at-risk]] and [[expected-shortfall]] and sits alongside historical and parametric approaches as one of the three canonical VaR methods.

### Portfolio and retirement projections

Long-horizon wealth planning uses Monte Carlo to model the **sequence-of-returns risk** that deterministic average-return math hides: two portfolios with the same average return can end very differently depending on *when* the bad years land, especially once withdrawals begin. Simulating thousands of return sequences yields a probability of a plan surviving (e.g. "success rate" of a retirement withdrawal strategy) rather than a single misleadingly-precise number.

### Backtesting robustness

A single historical backtest is one draw from the distribution of possible histories, which invites overfitting. Monte Carlo methods stress-test a strategy by resampling:

- **Trade / return reshuffling** — randomly reorder the sequence of realized trade returns to build a distribution of equity curves and drawdowns, exposing how much the headline result depended on lucky ordering.
- **Synthetic price paths** — generate artificial price series with similar statistical properties and re-run the strategy to see whether the edge survives on data it was never fit to.

These sit within the broader [[backtesting]] toolkit; see [[monte-carlo-backtesting]] for the resampling approach and [[monte-carlo-permutation-test]] for the closely related significance test that asks whether a backtest result could have arisen by chance.

### Risk of ruin and position sizing

Given a strategy's win rate, payoff ratio, and bet size, Monte Carlo simulates thousands of trade sequences to estimate the probability of the account drawing down past a ruin threshold before recovering. This directly informs [[risk-of-ruin]] estimates and [[position-sizing]] decisions, capturing path effects that a simple expected-value calculation misses.

### Corporate valuation sensitivity

In discounted-cash-flow (DCF) analysis, Monte Carlo replaces single point estimates for revenue growth, margins, and discount rate with distributions, producing a distribution of intrinsic values instead of one figure — a far more honest picture of valuation uncertainty.

## Inputs and Assumptions

A Monte Carlo simulation is only as good as the distributions and correlations fed into it — **garbage in, garbage out**. The most common failure modes are not bugs in the sampling but errors in the assumptions:

- **Distributional assumptions.** Models built on the normal (or [[geometric-brownian-motion]] log-normal) distribution systematically **understate fat tails**: real financial returns exhibit far more extreme moves than a Gaussian predicts. A simulation calibrated to normal returns will report a comfortingly small tail risk that reality routinely violates — the [[black-swan]] problem.
- **Correlation and its breakdown.** Multi-asset simulations must model how inputs move together, usually by decomposing the covariance matrix (**Cholesky decomposition**) to generate correlated random draws. But correlations are not stable — in crises they converge toward 1 as everything sells off together, so a simulation using placid-market correlations dramatically understates joint losses.
- **Regime shifts.** Volatility clustering, structural breaks, and regime changes mean parameters estimated from one period may not hold in the next. Static-parameter simulations miss this.
- **Stationarity.** The method implicitly assumes the sampled distribution resembles the future. When the data-generating process itself changes, the simulation is confidently wrong.

## Strengths vs Limitations

**Strengths**

- **Flexibility** — handles arbitrary payoffs, path-dependence, and many interacting variables that defeat analytical methods.
- **Full distributions, not point estimates** — you get percentiles, tail measures, and probabilities of events, not just an average.
- **Transparency of assumptions** — every input distribution is explicit and can be stress-tested.
- **Scales to high dimensions** — its error rate is independent of the number of variables, which is why it beats grid methods for large portfolios.

**Limitations**

- **Compute-heavy** — the `1/√N` convergence makes high precision expensive.
- **Assumption-sensitive** — the output inherits every flaw in the input distributions and correlation structure.
- **False precision** — a smooth histogram over 100,000 paths looks authoritative regardless of whether the underlying model is right; the visual polish can mask garbage assumptions.
- **It does not predict.** This is the key conceptual point: Monte Carlo does not forecast the future. It **characterises the distribution implied by your model and assumptions**. If the model is a [[random-walk-theory]] with normal shocks, the output describes that random walk — nothing more. The simulation is a lens on your assumptions, not a crystal ball.

### Relationship to other methods

Monte Carlo is one of three broad approaches to estimating risk and value distributions, each with a different bias:

| Method | How it builds the distribution | Trade-off |
|---|---|---|
| Historical simulation | Replays actual past outcomes | No distributional assumption, but limited to what history contains |
| Parametric (analytical) | Assumes a distribution and computes in closed form | Fast, but rigid and usually normal-tailed |
| Monte Carlo | Samples from assumed distributions/models | Flexible and handles non-linearity, but slow and assumption-dependent |

In practice these are complementary: historical methods anchor to reality, parametric methods give speed and intuition, and Monte Carlo fills the gap for complex, non-linear, path-dependent problems.

## Related

- [[value-at-risk]]
- [[expected-shortfall]]
- [[backtesting]]
- [[monte-carlo-backtesting]]
- [[monte-carlo-permutation-test]]
- [[options-pricing-models]]
- [[black-scholes]]
- [[binomial-model]]
- [[risk-of-ruin]]
- [[position-sizing]]
- [[random-walk-theory]]
- [[black-swan]]
- [[volatility]]
- [[geometric-brownian-motion]]

## Sources

- Standard quantitative-finance references on numerical methods and derivative pricing (e.g. Hull, *Options, Futures, and Other Derivatives*; Glasserman, *Monte Carlo Methods in Financial Engineering*) — general-knowledge synthesis, no specific figures cited.
- General texts on financial risk management covering Monte Carlo VaR and its relationship to historical and parametric methods.
