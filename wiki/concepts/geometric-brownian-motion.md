---
title: "Geometric Brownian Motion (GBM)"
type: concept
created: 2026-07-03
updated: 2026-07-03
status: good
tags: [quantitative, volatility, derivatives]
aliases: ["Geometric Brownian Motion", "geometric-brownian-motion", "GBM", "Brownian Motion"]
domain: [quantitative, derivatives, volatility]
difficulty: advanced
related: ["[[black-scholes]]", "[[options-pricing-models]]", "[[monte-carlo-simulation]]", "[[random-walk-theory]]", "[[volatility]]", "[[volatility-smile]]", "[[black-swan]]", "[[efficient-market-hypothesis]]", "[[volatility-clustering]]", "[[kurtosis]]", "[[heston-model]]"]
---

# Geometric Brownian Motion (GBM)

Geometric Brownian Motion (GBM) is the standard continuous-time stochastic model for the price of a financial asset. It describes prices as evolving by a combination of a steady average growth (drift) and a random shock whose size scales with the current price level. GBM is the mathematical foundation of the [[black-scholes]] option-pricing formula, the default price process in [[monte-carlo-simulation]] of asset paths, and the workhorse assumption behind most textbook derivations in quantitative finance.

Formally, a price `S` following GBM obeys the stochastic differential equation (SDE):

```
dS = μ S dt + σ S dW
```

where `μ` is the **drift** (the expected instantaneous rate of return), `σ` is the **volatility** (the standard deviation of returns per unit time), and `dW` is the increment of a **Wiener process** — the mathematical name for standard Brownian motion, a continuous random path whose increments are independent, normally distributed, and have variance equal to the elapsed time. The two terms split the price change into a deterministic part (`μ S dt`) and a random part (`σ S dW`).

## Why "Geometric"

The defining feature is that both the drift and the shock are **proportional to the price level `S`**, not fixed in dollar terms. A stock trading at 500 is modelled as making moves ten times larger in absolute size than the same stock at 50, but the same size in *percentage* terms. GBM therefore models **proportional (percentage) returns** rather than additive dollar changes.

This is contrasted with **arithmetic Brownian motion** (`dS = μ dt + σ dW`), where the drift and shock are constant regardless of price. Arithmetic Brownian motion has two properties that make it unsuitable for equity and most asset prices: the price can go **negative** (a random downward shock can push it below zero), and a fixed-dollar volatility is unrealistic because a 1-dollar move means something very different for a 5-dollar stock than for a 5,000-dollar one. GBM fixes both: because the shock scales with `S`, the price can approach zero but never crosses it, so **prices stay strictly positive**, and volatility is naturally expressed as a percentage — matching how traders actually think about risk. See [[arithmetic-brownian-motion]] for the additive counterpart.

## Key Properties

- **Lognormal prices.** Because returns compound multiplicatively, the future price under GBM is **lognormally distributed** — its logarithm is normal. This guarantees positivity and produces the right-skewed price distribution seen in practice (a price can multiply many-fold on the upside but can only fall to zero on the downside).

- **Normally distributed log-returns.** The continuously compounded return over any interval, `ln(S_t / S_0)`, is normally distributed. This is why GBM is often summarised as "log-returns are normal, prices are lognormal."

- **The drift correction (−½σ² term).** Applying **Itô's lemma** — the chain rule of stochastic calculus — to `ln S` gives the log-price its own SDE:

  ```
  d(ln S) = (μ − ½σ²) dt + σ dW
  ```

  The extra `−½σ²` term is the **Itô (or convexity) correction**. It appears because volatility drags down the compounded growth of the price: the *median* log-return grows at `μ − ½σ²` even though the *expected* price still grows at `μ`. This is not a modelling choice but a mathematical consequence of the non-linearity of the logarithm, and it is a frequent source of confusion when people expect the average log-return to equal the drift. From this the closed-form solution follows:

  ```
  S_t = S_0 · exp[(μ − ½σ²) t + σ W_t]
  ```

- **Markov / memoryless.** GBM is a **Markov process**: the distribution of future prices depends only on the current price, not on the path taken to get there. Increments are independent — past moves carry no information about future moves. This is the continuous-time expression of a [[random-walk-theory]] and aligns with the **weak form** of the [[efficient-market-hypothesis]], under which past prices cannot be used to predict future returns.

- **Constant μ and σ.** The classic model assumes drift and volatility are **constant** over time. This assumption is what makes GBM analytically tractable, and it is also its single biggest weakness (see Limitations).

## Where It Is Used

- **Option pricing.** GBM is the engine of the [[black-scholes]] model: assuming the underlying follows GBM with constant volatility, and constructing a continuously rebalanced hedge, yields the Black-Scholes-Merton partial differential equation and its closed-form option prices. It underpins most analytical [[options-pricing-models]].

- **Monte Carlo path simulation.** GBM is the **default price process** when [[monte-carlo-simulation]] generates synthetic asset paths — for pricing path-dependent and exotic options, projecting portfolio values, and stress-testing strategies. Each simulated step draws a normal random shock and applies the discretised GBM update. See the discussion of synthetic price paths in [[monte-carlo-simulation]].

- **Risk and projection.** GBM (or its lognormal endpoint distribution) is commonly used to model value-at-risk horizons, retirement and wealth projections, and any calculation that needs a tractable forward distribution of prices.

## Intuition and Example

Think of GBM as compound growth with noise. Over a short interval the price is expected to grow by roughly `μ · dt`, but on top of that it receives a random nudge whose size is `σ · S · √dt`. Because the nudge scales with `S`, a run of good luck raises the base on which future moves compound, producing the characteristic **exponential-with-jitter** appearance of a simulated stock chart. Two paths starting from the same price with the same `μ` and `σ` can diverge widely purely by chance, and the *spread* of possible prices fans out over time — the essence of why long-horizon forecasts are so uncertain even when the model is "correct." Averaged over enough simulated paths, the mean price rises along the smooth curve `S_0 · exp(μt)`, while any single realised path wanders around it.

## Limitations

GBM is a mathematically elegant approximation, and real markets violate nearly every one of its assumptions. Being honest about these gaps is essential:

- **Volatility is not constant.** GBM assumes a single fixed `σ`, but realised volatility varies dramatically over time and clusters — calm periods and turbulent periods bunch together ([[volatility-clustering]]). The market's own disagreement with the constant-volatility assumption is visible in the [[volatility-smile]]: options at different strikes imply different volatilities, which cannot happen if a single GBM `σ` were correct.

- **Returns are not normal.** Real return distributions have **fat tails** (excess [[kurtosis]]) and **skew**. Extreme moves that a normal distribution says should almost never happen occur with uncomfortable regularity, so GBM systematically **understates tail risk** — the [[black-swan]] problem.

- **Prices jump.** GBM has continuous paths, but real prices **gap** — overnight, on earnings, on news, in crashes. Continuous hedging arguments break down precisely when they are needed most.

- **Parameters shift with regime.** `μ` and `σ` are not stable constants; they drift with the macro and market regime. A model calibrated in a placid period is confidently wrong in the next crisis.

### Extensions that relax GBM

- **Stochastic volatility** — let `σ` itself be random and mean-reverting, as in the [[heston-model]]. This reproduces the volatility smile and clustering that GBM cannot.
- **Jump-diffusion** — add a discontinuous jump component to the continuous GBM path (the Merton jump-diffusion model), capturing gaps and fat tails. See [[jump-diffusion]] / [[merton-model]].
- **Local volatility** — make `σ` a deterministic function of price and time (the Dupire local-vol model), fitting the observed smile exactly.

These models add realism at the cost of tractability and extra parameters; GBM remains the baseline against which they are all defined.

## Related

- [[black-scholes]]
- [[options-pricing-models]]
- [[monte-carlo-simulation]]
- [[random-walk-theory]]
- [[efficient-market-hypothesis]]
- [[volatility]]
- [[volatility-smile]]
- [[volatility-clustering]]
- [[kurtosis]]
- [[black-swan]]
- [[heston-model]]
- [[arithmetic-brownian-motion]]

## Sources

- Standard quantitative-finance and derivatives references covering the lognormal price model and the Black-Scholes framework (e.g. Hull, *Options, Futures, and Other Derivatives*) — general-knowledge synthesis, no specific figures cited.
- Standard stochastic-calculus texts on Itô's lemma, Wiener processes, and the geometric Brownian motion SDE and its closed-form solution.
