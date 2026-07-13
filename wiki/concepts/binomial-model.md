---
title: "Binomial Option Pricing Model"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, quantitative, volatility]
aliases: ["Binomial Model", "binomial-model", "binomial tree", "binomial lattice", "Cox-Ross-Rubinstein", "CRR model"]
related: ["[[options-pricing]]", "[[black-scholes]]", "[[options]]", "[[greeks]]", "[[implied-volatility]]", "[[monte-carlo-simulation]]", "[[put-call-parity]]"]
domain: [options, quantitative]
prerequisites: ["[[options-pricing]]", "[[options]]"]
difficulty: intermediate
---

The **binomial option pricing model** is a discrete-time method for valuing options by modelling the underlying asset's price as a recombining tree (lattice) of up and down moves over many small time steps. Introduced by Cox, Ross, and Rubinstein (CRR) in 1979, it prices an option by working backward from expiration through the tree, and it converges to the continuous-time [[black-scholes]] price as the number of steps increases. Its key practical advantage over Black-Scholes is that it handles **American-style early exercise**, discrete dividends, and changing parameters naturally.

## How the Tree Is Built

Over each small time step `Δt`, the underlying price `S` is assumed to move to either `S·u` (up) or `S·d` (down). In the standard CRR parameterisation, the step sizes are tied to volatility `σ`:

- **Up factor:** `u = e^(σ·√Δt)`
- **Down factor:** `d = 1/u = e^(−σ·√Δt)`

Because `d = 1/u`, an up-then-down move returns to the starting price, so the tree *recombines* — the number of distinct nodes grows linearly (n+1 terminal nodes for n steps) rather than exponentially, which is what makes the lattice computationally cheap.

### Risk-neutral probability

Pricing uses the **risk-neutral probability** of an up move, not the real-world probability:

`p = (e^(r·Δt) − d) / (u − d)`

where `r` is the risk-free rate (for a dividend-paying asset, replace `e^(r·Δt)` with `e^((r−q)·Δt)`, `q` = dividend yield). Under this measure the expected discounted payoff equals the no-arbitrage price.

## Backward Induction (the valuation engine)

1. **Build the price tree** forward to expiration using `u` and `d`.
2. **Compute terminal payoffs** at each final node: `max(S_T − K, 0)` for a call, `max(K − S_T, 0)` for a put.
3. **Roll back** node by node. The value at each earlier node is the discounted risk-neutral expectation of its two child nodes:

   `V = e^(−r·Δt) · [ p·V_up + (1−p)·V_down ]`

4. **For American options**, at each node take the *greater* of the rolled-back continuation value and the immediate exercise value: `V = max(continuation, intrinsic)`. This early-exercise comparison is exactly what closed-form Black-Scholes cannot do, and it is the binomial model's signature capability.

The value at the root node (time 0) is the option's fair price.

## Relationship to Black-Scholes and Monte Carlo

- As steps `n → ∞`, the binomial price converges to the [[black-scholes]] price for European options — the two models are consistent in the limit (this is the central CRR result).
- **Binomial vs. Black-Scholes:** use the lattice when early exercise, discrete dividends, or path-dependent decisions matter (American options, employee stock options, callable/convertible features); use Black-Scholes for fast European valuation and as the lingua franca for quoting [[implied-volatility]].
- **Binomial vs. [[monte-carlo-simulation|Monte Carlo]]:** the lattice is efficient and naturally handles early exercise for low-dimensional problems; Monte Carlo is preferred for exotic, multi-asset, or strongly path-dependent payoffs where the tree becomes unwieldy.

## Trading Relevance

- **American option valuation.** Most single-stock equity options are American-style. A trader pricing or hedging them — or judging whether early exercise of a deep-in-the-money option or one with a pending dividend is rational — needs a lattice (or equivalent) rather than vanilla Black-Scholes.
- **Greeks by finite difference.** The tree yields the [[greeks]] (delta, gamma, theta) directly by perturbing inputs and re-pricing, which is convenient for desks that already run a binomial engine.
- **Intuition and teaching.** The two-state-per-step structure makes the **no-arbitrage and risk-neutral pricing** logic transparent: the option can be replicated by a dynamically rebalanced position in the underlying and the risk-free asset, which is the same hedging argument that underlies [[delta-hedging]] and [[black-scholes]].
- **Dividends and corporate actions.** Discrete dividends and other deterministic adjustments are inserted at the relevant tree dates, giving more faithful pricing of dividend-sensitive American options than the continuous-yield Black-Scholes approximation.

The main limitation is that accuracy requires many steps (and the price can oscillate slightly as steps increase), and like all single-volatility models it assumes a constant `σ` unless extended (e.g. implied trees) to fit a [[volatility-skew|volatility surface]].

## Related

- [[options-pricing]] — overview of the five inputs and competing pricing models
- [[black-scholes]] — the continuous-time limit of the binomial model
- [[monte-carlo-simulation]] — the simulation alternative for exotic/path-dependent options
- [[greeks]] — sensitivities the lattice computes by finite difference
- [[put-call-parity]] — the arbitrage relationship the model respects
- [[implied-volatility]] — the volatility input backed out of market prices
- [[delta-hedging]] — the replication argument underlying lattice pricing
- [[options]] — the contracts being valued

## Sources

- Cox, J., Ross, S. and Rubinstein, M. (1979), "Option Pricing: A Simplified Approach," *Journal of Financial Economics* 7(3) — the original binomial (CRR) model.
- Hull, J. (2018), *Options, Futures, and Other Derivatives*, Pearson — binomial trees, backward induction, risk-neutral valuation, and American-option early exercise.
- Black, F. and Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities," *Journal of Political Economy* — the continuous-time model to which the binomial converges.
