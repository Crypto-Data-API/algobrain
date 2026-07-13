---
title: "Interest Rate Models"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [derivatives, volatility, quantitative, bonds]
aliases: ["Interest Rate Models", "Short-Rate Models", "Term Structure Models", "interest-rate-models"]
domain: [portfolio-theory, quantitative-finance]
prerequisites: ["[[interest-rates]]", "[[yield-curve]]", "[[stochastic-calculus]]"]
difficulty: advanced
related: ["[[interest-rates]]", "[[yield-curve]]", "[[interest-rate-risk]]", "[[interest-rate-swaps]]", "[[interest-rate-options]]", "[[duration]]", "[[bonds]]", "[[black-scholes]]", "[[volatility]]"]
---

Interest rate models are mathematical descriptions of how interest rates -- or the entire [[yield-curve|term structure]] -- evolve through time, used to price interest-rate derivatives (swaptions, caps, floors, bond options), to value fixed-income securities consistently, and to manage [[interest-rate-risk|rate risk]]. They range from single-factor "short-rate" models that describe the instantaneous overnight rate as a stochastic process, to multi-factor and market models that describe the whole forward curve. Their defining challenge is reproducing the observed term structure and its [[volatility]] while remaining arbitrage-free.

## Why Rate Models Differ from Equity Models

Unlike a single stock price, an interest-rate market is a *curve* of related quantities (overnight, 1y, 5y, 10y, 30y) that must move in a mutually consistent, no-arbitrage way -- you cannot model the 10y rate in isolation. Rates also exhibit features equities lack: mean reversion toward a long-run level, occasional negative values (post-2014 Europe/Japan), and a volatility term structure of their own. This is why the [[black-scholes]] geometric-Brownian-motion assumption is inappropriate for rates and a dedicated model class exists.

## Short-Rate Models (single factor)

These model the instantaneous short rate `r(t)` as a stochastic differential equation. The whole yield curve is then derived as the expected discounted value of future short rates under the risk-neutral measure.

| Model | SDE for dr | Key property |
|---|---|---|
| **Vasicek (1977)** | `dr = a(b − r)dt + σ dW` | Mean-reverting (to `b` at speed `a`); Gaussian, so rates can go negative; closed-form bond prices |
| **Cox-Ingersoll-Ross (CIR, 1985)** | `dr = a(b − r)dt + σ√r dW` | Mean-reverting; `√r` term keeps rates non-negative; vol rises with rate level |
| **Ho-Lee (1986)** | `dr = θ(t)dt + σ dW` | First model calibrated to fit the *initial* curve exactly via time-dependent drift `θ(t)` |
| **Hull-White (1990)** | `dr = (θ(t) − a r)dt + σ dW` | Mean-reverting extension of Ho-Lee; fits initial curve; the workhorse for swaption pricing |
| **Black-Karasinski (1991)** | `d ln r = (θ(t) − a ln r)dt + σ dW` | Log-normal short rate; rates stay positive but no closed form |

In the mean-reversion drift `a(b − r)`, `b` is the long-run mean rate and `a` is the speed of reversion -- larger `a` pulls rates back to `b` faster, which damps long-end volatility.

## Forward-Rate and Market Models (multi factor)

- **Heath-Jarrow-Morton (HJM, 1992)** -- a general framework that models the evolution of the *entire forward-rate curve* directly; the no-arbitrage condition fixes the drift as a function of the volatility structure. Short-rate models are special cases of HJM.
- **LIBOR Market Model / BGM (Brace-Gatarek-Musiela, 1997)** -- models discrete forward rates (the rates actually quoted in the market) as log-normal processes, making it consistent with the Black formula traders use to quote caps and swaptions. The market-standard for exotic rate derivatives, now adapted to SOFR/RFR benchmarks after the LIBOR transition.

## Calibration

A model is only useful once *calibrated* -- its parameters (`a`, `b`, `σ`, the `θ(t)` curve) are fitted so the model reproduces today's observed bond prices and the implied-volatility surface of liquid swaptions and caps. A model that fits the current curve and vol surface can then price illiquid or exotic instruments by interpolation/extrapolation under no-arbitrage.

## Trading and Portfolio Relevance

- **Derivatives pricing** -- swaptions, caps, floors, callable bonds, and mortgage prepayment options all require a term-structure model; the choice of model materially affects the price of optionality.
- **Risk management** -- scenario generation for [[interest-rate-risk|rate risk]], [[duration]]/convexity hedging, and computing rate sensitivities (DV01, key-rate durations) for a bond or [[interest-rate-swaps|swap]] book.
- **Relative value** -- a calibrated model flags rich/cheap points on the curve or vol surface, the basis for curve and butterfly trades and vol arbitrage.
- **Asset-liability management** -- pension funds and insurers use rate models to project liability discount rates and stress-test funding ratios.

The practical caution mirrors all quant modelling: a model that fits today's prices is not a forecast of future rates, and model risk (wrong dynamics, mis-calibration, regime change such as the move to negative rates or the LIBOR-to-SOFR transition) is a first-order exposure.

## Related

- [[interest-rates]] -- the underlying quantity being modelled
- [[yield-curve]] -- the term structure the models reproduce
- [[interest-rate-risk]] -- the exposure the models help quantify and hedge
- [[interest-rate-swaps]] -- a core instrument priced with these models
- [[interest-rate-options]] -- caps, floors, and swaptions valued via rate models
- [[duration]] -- the first-order rate sensitivity these models refine
- [[black-scholes]] -- the equity-option analogue with different dynamics

## Sources

- Vasicek, O. (1977) "An Equilibrium Characterization of the Term Structure," *Journal of Financial Economics*.
- Cox, J., Ingersoll, J., Ross, S. (1985) "A Theory of the Term Structure of Interest Rates," *Econometrica*.
- Hull, J. & White, A. (1990) "Pricing Interest-Rate-Derivative Securities," *Review of Financial Studies*.
- Heath, D., Jarrow, R., Morton, A. (1992) "Bond Pricing and the Term Structure of Interest Rates," *Econometrica*.
- Brace, A., Gatarek, D., Musiela, M. (1997) "The Market Model of Interest Rate Dynamics," *Mathematical Finance*.
- Hull, J. *Options, Futures, and Other Derivatives* -- chapters on interest-rate derivatives and term-structure models.
- Brigo, D. & Mercurio, F. *Interest Rate Models -- Theory and Practice* (2006).
