---
title: "Options Pricing"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [options, derivatives, volatility]
aliases: ["Options Pricing", "Option Valuation", "Option Premium", "Options Pricing Models", "options-pricing-models", "options-pricing"]
domain: [options, quantitative]
prerequisites: ["[[options-overview]]"]
difficulty: intermediate
related: ["[[black-scholes]]", "[[options]]", "[[greeks]]", "[[the-greeks]]", "[[implied-volatility]]", "[[theta-decay]]", "[[put-call-parity]]", "[[binomial-model]]", "[[volatility-smile]]"]
---

Options pricing is the process of determining the fair value (premium) of an [[options|option]] contract. An option's price consists of two components: intrinsic value (the amount by which the option is in-the-money) and extrinsic value (time value plus volatility premium). Understanding how these components interact is fundamental to all options trading, from basic [[covered-calls]] to complex multi-leg institutional strategies.

## The Five Inputs

Every major options pricing model requires the same five inputs:

| Input | Symbol | Observable? | Effect on a CALL premium | Effect on a PUT premium |
|---|---|---|---|---|
| Underlying price | S | Yes | ↑ S → ↑ | ↑ S → ↓ |
| Strike price | K | Yes (contract spec) | ↑ K → ↓ | ↑ K → ↑ |
| Time to expiry (yrs) | T | Yes | ↑ T → ↑ (usually) | ↑ T → ↑ (usually) |
| Risk-free rate | r | Yes ([[us-treasury-bonds\|Treasury]] curve) | ↑ r → ↑ | ↑ r → ↓ |
| Volatility | σ | **No — estimated / [[implied-volatility\|implied]]** | ↑ σ → ↑ | ↑ σ → ↑ |

1. **S** — Current price of the underlying asset
2. **K** — Strike price of the option
3. **T** — Time to expiration (in years)
4. **r** — Risk-free interest rate (typically the [[us-treasury-bonds|Treasury]] rate matching the option's tenor)
5. **σ (sigma)** — Volatility of the underlying, either historical or [[implied-volatility|implied]]

(Dividends, `q`, are a sixth input in the dividend-adjusted form.) Of these inputs, all but one are directly observable in the market. Volatility is the exception — it must be estimated or backed out from market prices ([[implied-volatility|implied volatility]]). This makes volatility the key variable that options traders debate, and it is the reason options are often described as "volatility instruments" rather than directional bets.

### The Black-Scholes Formula

For a European call (no dividends), the [[black-scholes|Black-Scholes]] closed form is:

```
C = S·N(d1) − K·e^(−rT)·N(d2)
P = K·e^(−rT)·N(−d2) − S·N(−d1)        (put, via put-call parity)

  d1 = [ ln(S/K) + (r + σ²/2)·T ] / (σ·√T)
  d2 = d1 − σ·√T

where N(·) is the standard normal cumulative distribution function (CDF).
```

`N(d2)` is (under the risk-neutral measure) the probability the call finishes in-the-money; `N(d1)` is the call's delta. The term `K·e^(−rT)` is the strike discounted to present value at the risk-free rate.

### Worked Example (Black-Scholes)

Price a 3-month ATM European call. Inputs (illustrative): S = 100, K = 100, T = 0.25, r = 4% (0.04), σ = 20% (0.20), no dividends.

- `σ·√T` = 0.20 × √0.25 = 0.20 × 0.5 = **0.10**
- `d1` = [ ln(100/100) + (0.04 + 0.20²/2)·0.25 ] / 0.10 = [ 0 + (0.04 + 0.02)·0.25 ] / 0.10 = 0.015 / 0.10 = **0.15**
- `d2` = 0.15 − 0.10 = **0.05**
- `N(0.15)` ≈ 0.5596, `N(0.05)` ≈ 0.5199
- `K·e^(−rT)` = 100 × e^(−0.04×0.25) = 100 × e^(−0.01) ≈ 99.005
- `C` = 100 × 0.5596 − 99.005 × 0.5199 ≈ 55.96 − 51.47 ≈ **$4.49**

So the fair value of the ATM call is about $4.49 per share. With zero intrinsic value (S = K), this entire premium is **extrinsic / time value**, driven by σ and T. The matching put, via parity below, is C − S + K·e^(−rT) = 4.49 − 100 + 99.005 ≈ **$3.50**. (Illustrative numbers; `N(·)` values rounded.)

## Pricing Models

| Model | Year | Best for | Key assumptions / mechanics |
|---|---|---|---|
| [[black-scholes\|Black-Scholes]] | 1973 | European, vanilla | Closed form; constant σ, log-normal price, continuous trading |
| [[binomial-model\|Binomial (Cox-Ross-Rubinstein)]] | 1979 | American, dividends, early exercise | Discrete up/down lattice; converges to Black-Scholes as steps → ∞ |
| Trinomial / finite-difference | — | American, complex payoffs | Numerical PDE solution on a grid |
| Monte Carlo | — | Exotic, path-dependent | Simulate thousands of price paths, average discounted payoffs |

The [[black-scholes|Black-Scholes model]] (1973) was the first widely adopted closed-form solution for European option pricing. It assumes constant volatility, log-normal price distribution, no dividends (in the basic form), and continuous trading. Despite these simplifying assumptions — which the [[volatility-smile|volatility smile]] visibly contradicts — Black-Scholes remains the industry-standard *language* for quoting options and calculating [[greeks]]. The [[binomial-model|binomial model]] (Cox-Ross-Rubinstein, 1979) uses a discrete lattice of up/down price moves over multiple time steps, converging to Black-Scholes as steps increase. It handles American-style early exercise, dividends, and variable volatility more naturally, because at each node you can compare the value of holding vs. exercising. Monte Carlo simulation prices options by running thousands of random price paths and averaging the discounted payoffs — it is the method of choice for exotic and path-dependent options (Asians, barriers, lookbacks) where no analytical solution exists.

### Binomial Intuition (One Step)

In a single-period [[binomial-model|binomial tree]], the underlying either rises to `S·u` or falls to `S·d`. The risk-neutral up-probability is `p = (e^(rT) − d) / (u − d)`, and the option value is `e^(−rT) · [ p·payoff_up + (1−p)·payoff_down ]`. Chaining many such steps and shrinking the time increment reproduces the Black-Scholes price — the two models agree in the limit.

## Intrinsic vs. Extrinsic Value

Intrinsic value is straightforward: for a call, it is max(S - K, 0); for a put, max(K - S, 0). Out-of-the-money options have zero intrinsic value. Extrinsic value is everything above intrinsic and reflects the market's assessment of the probability that the option could become (more) profitable before expiry. Extrinsic value is highest for at-the-money options and decays over time ([[theta-decay]]). It also increases with higher [[implied-volatility]] -- when the market expects larger price swings, the probability of the option finishing in-the-money increases, and so does the premium.

## Put-Call Parity

[[put-call-parity|Put-call parity]] is a fundamental arbitrage relationship that links the prices of European calls and puts with the same strike and expiration:

```
C − P = S − K·e^(−rT)        (no dividends)
C − P = S·e^(−qT) − K·e^(−rT)  (with continuous dividend yield q)
```

If this relationship is violated, a risk-free arbitrage profit can be earned — e.g. if the left side is too high, sell the call, buy the put, buy the stock, and finance at `r` to lock in a riskless gain (a *conversion*; the reverse is a *reversal*). Parity does not tell you the absolute price of an option, but it ensures internal consistency between calls and puts. It also explains why [[implied-volatility|implied volatility]] for a call and a put at the *same* strike must be equal for European options — a fact the [[volatility-smile|smile]] relies on. **Quick check using the worked example above:** C − P = 4.49 − 3.50 = 0.99, and S − K·e^(−rT) = 100 − 99.005 = 0.995 ✓ (small residual from rounding `N(·)`).

## The Greeks as Price Sensitivities

The [[greeks|Greeks]] (see also [[the-greeks]]) are partial derivatives of the option price with respect to each input. They are the working risk language of every options desk:

| Greek | Measures sensitivity to | Symbol | Note |
|---|---|---|---|
| Delta | Underlying price (S) | Δ = ∂C/∂S | ≈ probability ITM for calls; hedge ratio |
| Gamma | Rate of change of delta | Γ = ∂²C/∂S² | Highest ATM near expiry; convexity |
| Theta | Passage of time (T) | Θ = ∂C/∂T | [[theta-decay\|Time decay]]; usually negative for long options |
| Vega | Volatility (σ) | ν = ∂C/∂σ | Long options are long vega; the [[volatility-smile\|smile]]'s P&L driver |
| Rho | Interest rate (r) | ρ = ∂C/∂r | Most relevant for long-dated options |

Together, the [[greeks|Greeks]] provide a complete picture of an option's risk exposures and are the primary tools used for hedging and portfolio management. A market maker who sells an option will *delta-hedge* (trade the underlying to neutralize Δ) and then manage residual gamma, theta, and vega exposure.

## Trading Relevance

The practical takeaway for a trader is that buying or selling an option is rarely a pure directional bet — it is a joint bet on direction, time, and volatility. Because all but one of the five inputs are observable, the trade comes down to a view on **implied versus realised volatility**: an option is "cheap" if its [[implied-volatility|IV]] is below the volatility you expect to materialise, and "expensive" if above. This is why systematic options edges (e.g. the [[volatility-risk-premium|volatility risk premium]]) are framed around IV being persistently richer than subsequent realised vol, favouring net sellers who collect [[theta-decay|theta]]. Reading an [[options-chain|options chain]] is, in effect, reading the model's outputs (premium, IV, [[greeks|Greeks]]) across strikes and expiries to find structures where the priced-in volatility is mispriced relative to your forecast.

## Common Pitfalls

- **Trusting a single σ.** Black-Scholes assumes one volatility, but the market's [[volatility-smile|smile/skew]] shows IV varies by strike. Pricing OTM options at ATM vol mis-values the wings — feed the *strike-appropriate* IV.
- **Forgetting dividends and early exercise.** American calls/puts on dividend payers can be optimal to exercise early; the basic Black-Scholes form misses this — use the [[binomial-model|binomial]] or a dividend adjustment.
- **Confusing IV with a probability forecast.** IV is a risk-neutral, supply-and-demand-laden quantity, not a calibrated real-world probability; the persistent gap to realised vol is the [[volatility-risk-premium|volatility risk premium]].
- **Mismatched risk-free rate.** Use the discount/funding rate matching the option's tenor; rho effects are small but real for long-dated contracts.
- **Ignoring the Greeks' instability near expiry.** Gamma and theta blow up as T → 0 for ATM options; positions that look benign can become violently path-dependent in the final days.

## Sources

- Black, F. and Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities," *Journal of Political Economy* — the original closed-form model.
- Merton, R. (1973), "Theory of Rational Option Pricing," *Bell Journal of Economics* — dividend/extensions to Black-Scholes.
- Cox, J., Ross, S. and Rubinstein, M. (1979), "Option Pricing: A Simplified Approach," *Journal of Financial Economics* — the binomial lattice model.
- Hull, J. (2018), *Options, Futures, and Other Derivatives*, Pearson — standard reference on pricing models, put-call parity, and the Greeks.
- Natenberg, S. (1994), *Option Volatility and Pricing*, McGraw-Hill — intrinsic/extrinsic value and the trader's volatility framing.
- General market knowledge — the Black-Scholes worked example, binomial intuition, and parity check are standard derivations.

## Related

- [[black-scholes]] — the foundational pricing model
- [[binomial-model]] — lattice model for American options and early exercise
- [[options]] — overview of options contracts
- [[options-chain]] — where model outputs are read across strikes/expiries
- [[greeks]] — sensitivity measures derived from pricing models
- [[the-greeks]] — the Greeks as a risk-management toolkit
- [[implied-volatility]] — the market's forecast of future volatility
- [[volatility-smile]] — why a single σ is insufficient across strikes
- [[theta-decay]] — time decay component of extrinsic value
- [[put-call-parity]] — the call/put arbitrage relationship
- [[volatility-risk-premium]] — why IV tends to exceed realised volatility
