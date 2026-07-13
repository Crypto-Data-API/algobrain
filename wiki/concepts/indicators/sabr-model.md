---
title: "SABR Volatility Model"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, volatility, derivatives, quantitative, options-pricing, indicators]
aliases: ["SABR", "Stochastic Alpha Beta Rho", "SABR Model"]
domain: [options-pricing, volatility-modeling, quantitative]
prerequisites: ["[[black-scholes]]", "[[implied-volatility]]", "[[volatility-smile]]", "[[volatility-skew]]", "[[volatility-surface]]"]
difficulty: advanced
related: ["[[black-scholes]]", "[[volatility-smile]]", "[[volatility-skew]]", "[[volatility-surface]]", "[[implied-volatility]]", "[[options-pricing-models]]", "[[local-volatility]]", "[[gamma-scalping]]", "[[delta-hedge]]"]
---

The SABR model — short for **Stochastic Alpha Beta Rho** — is a stochastic volatility model used to price [[options]] in the presence of a [[volatility-smile|volatility smile]]. Introduced by Patrick Hagan, Deep Kumar, Andrew Lesniewski and Diana Woodward in 2002, SABR became the de-facto industry standard for managing the smile in interest-rate options markets and is widely used in equity, FX and commodity options as well.

## Why SABR Exists

[[black-scholes|Black–Scholes]] assumes a single constant [[implied-volatility|implied volatility]] for all strikes and expiries, which is empirically false — real markets exhibit a [[volatility-smile|smile]] (or [[volatility-skew|skew]]) where out-of-the-money options trade at different implied vols than at-the-money options.

Practitioners need a model that:

1. **Fits the smile** observed in the market today
2. **Implies sensible dynamics** for how the smile moves when the underlying moves
3. **Hedges correctly** — i.e., produces a [[delta-hedge|delta]] that actually neutralises P&L when the spot moves
4. **Is fast** enough to recalibrate on every market update

[[local-volatility]] models (Dupire) fit the smile perfectly today but produce well-known wrong dynamics: in a Dupire model, the smile flattens as spot moves, contradicting market behaviour. SABR was designed specifically to fix this.

## The SABR SDE

SABR models the forward `F` and its volatility `α` as correlated stochastic processes:

```
dF = α · F^β · dW₁
dα = ν · α · dW₂
dW₁ · dW₂ = ρ · dt
```

The four parameters:

| Parameter | Name | Controls |
|-----------|------|----------|
| `α` (alpha) | initial volatility | overall level of implied vol |
| `β` (beta) | CEV exponent | backbone behaviour: 0 = normal, 1 = lognormal |
| `ρ` (rho) | spot–vol correlation | smile asymmetry (skew) |
| `ν` (nu, sometimes "vol-of-vol") | volatility of volatility | smile curvature (convexity / wings) |

In practice, traders typically **fix β** based on market convention (β = 1 for equity/FX, β = 0 or 0.5 for rates) and calibrate the remaining three parameters to market quotes.

## The Hagan Approximation

What made SABR genuinely usable on a trading desk is **Hagan's asymptotic expansion**: a closed-form formula that maps the four SABR parameters to a Black–Scholes-equivalent implied volatility for any strike `K` and expiry `T`. This means a trader can:

1. Calibrate SABR parameters to a few liquid strikes
2. Use the formula to interpolate / extrapolate to any other strike instantly
3. Hedge using BS Greeks computed at the SABR-implied vol

The Hagan formula is fast enough to run inside a market-making quote engine.

## Why SABR Hedges Better Than Local Vol

The key behavioural difference: when the spot moves, a [[local-volatility]] model implies the smile slides in the *opposite* direction (flattening), while SABR implies the smile slides *with* the spot (sticky-strike-like). Empirically, real markets behave more like SABR. As a result, SABR produces more stable P&L when delta-hedging, especially for short-dated [[volatility-skew|skew]] plays and barrier options.

## Limitations and Extensions

SABR has well-known weaknesses:

- **Negative density problem** — for very low strikes, the Hagan approximation can imply negative probabilities. This became acute in negative-rate environments (post-2014 EUR rates) and led to corrections such as the **Shifted SABR** and **Free-Boundary SABR** variants.
- **Single expiry per fit** — basic SABR is calibrated per expiry; constructing a self-consistent [[volatility-surface]] across expiries requires extensions like **SABR with time-dependent parameters** or **Dynamic SABR**.
- **Limited tail behaviour** — for very deep OTM strikes (especially in equity index puts), SABR systematically underprices the [[tail-risk|tail]]; jump-diffusion or rough-vol models are often used as overlays.

Extensions used in practice include **Dynamic SABR**, **Shifted SABR**, **Free-Boundary SABR**, and **Rough SABR** (incorporating fractional Brownian motion, which empirically fits short-dated equity vol better).

## Use in AI / ML Options Trading

Modern AI-driven options desks rarely use SABR alone, but it remains relevant in three ways:

1. **As a feature generator** — SABR-implied parameters (especially `ρ` and `ν`) are useful inputs to ML models forecasting future smile movements.
2. **As a baseline** — neural-network [[options-pricing-models|option pricing surrogates]] are typically benchmarked against SABR for accuracy and arbitrage-free behaviour.
3. **As a regulariser** — hybrid models combine a SABR backbone for arbitrage-free structure with an ML correction term for residual smile features the parametric form cannot capture.

## Related

- [[black-scholes]] — the model SABR generalises
- [[volatility-smile]], [[volatility-skew]] — what SABR is designed to fit
- [[volatility-surface]] — the broader object
- [[implied-volatility]] — what SABR ultimately produces
- [[local-volatility]] — alternative smile model with worse dynamics
- [[options-pricing-models]] — broader category
- [[gamma-scalping]], [[delta-hedge]] — hedging activities affected by choice of vol model
- [[deep-learning-option-pricing]] — modern ML alternative / complement

## Sources

*No raw sources ingested yet. This page summarises Hagan, Kumar, Lesniewski, Woodward (2002) "Managing Smile Risk" and standard quantitative-finance references on SABR.*
