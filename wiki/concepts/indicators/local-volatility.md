---
title: "Local Volatility"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, volatility]
aliases: ["Local Volatility", "Local Vol", "Dupire Model", "Local Volatility Model", "Derman Kani", "Derman-Kani"]
domain: [indicators]
prerequisites: ["[[implied-volatility]]", "[[volatility-surface]]", "[[volatility-smile]]"]
difficulty: advanced
related: ["[[implied-volatility]]", "[[volatility-surface]]", "[[volatility-smile]]", "[[volatility-skew]]", "[[historical-volatility]]", "[[realized-volatility]]", "[[options]]"]
---

# Local Volatility

Local volatility is a deterministic function σ(S, t) that gives the instantaneous volatility of an asset as it depends on the current spot price S and time t. Unlike the single constant volatility of the Black-Scholes model, a local volatility model lets volatility vary with price level and time, which allows it to reproduce the entire observed [[volatility-surface]] of option [[implied-volatility|implied volatilities]] exactly. It is the simplest model class that is consistent with the market's [[volatility-smile|smile]] and [[volatility-skew|skew]].

## Overview

Black-Scholes assumes a single constant volatility for all strikes and maturities, but real option markets show that implied volatility varies systematically with strike (the smile/skew) and with maturity (the term structure). Local volatility, introduced by **Bruno Dupire (1994)** and independently by **Derman and Kani (1994)**, resolves this by making volatility a function of the underlying's level and time rather than a constant. The model remains a complete, arbitrage-free, one-factor diffusion — the only randomness is the asset price itself — so it stays tractable while fitting the surface.

## How It Works

Under the local volatility model the asset follows the risk-neutral diffusion:

```
dS_t = (r - q) S_t dt + σ(S_t, t) S_t dW_t
```

where σ(S, t) is the local volatility function, r the risk-free rate, q the dividend yield, and W a Brownian motion.

The central result is the **Dupire formula**, which recovers the unique local volatility function consistent with a continuum of European call prices C(K, T) across all strikes K and maturities T:

```
                 ∂C/∂T + (r - q) K ∂C/∂K + q C
σ²(K, T) = 2 · ─────────────────────────────────
                        K² ∂²C/∂K²
```

In words: local variance at strike K and maturity T is determined by the calendar-time decay of the option price relative to its convexity in strike. Because the formula requires first and second derivatives of an interpolated price surface, the practical challenge is producing a smooth, arbitrage-free input surface — small noise in quoted prices is amplified violently by the second derivative in the denominator.

Once σ(S, t) is calibrated, exotic and path-dependent options (barriers, lookbacks, cliquets) can be priced by Monte Carlo or finite-difference PDE methods on a model that, by construction, reprices every vanilla option correctly.

## Local vs. Implied vs. Stochastic Volatility

- **[[implied-volatility|Implied volatility]]** is the single constant that, plugged into Black-Scholes, reproduces *one* option's market price. It is a quote convention, not a model of dynamics.
- **Local volatility** is the instantaneous volatility as a deterministic function of spot and time — the model that fits the *whole* surface with no extra randomness.
- **Stochastic volatility** (Heston, SABR) makes volatility itself a random process. Local-vol models are static in their volatility dynamics, so they tend to predict that the smile *flattens* as spot moves ("sticky" behavior that flattens too fast), mispricing the forward smile relative to what is observed. Practitioners often use **local-stochastic volatility (LSV)** hybrids that combine a stochastic-vol backbone with a local-vol correction term so the model both fits the vanilla surface exactly and produces realistic smile dynamics.

A key identity (Gatheral) links the two: local variance is approximately a *forward, conditional expectation of instantaneous variance* — local vol is the market's best estimate of variance conditional on the spot being at a given level at a given time.

## Trading Relevance

- **Exotics pricing and hedging**: Local volatility is the workhorse for marking and risk-managing barrier options, autocallables, and other path-dependent structures, because it is the model that is automatically consistent with the desk's vanilla marks. A trader who priced an exotic on flat Black-Scholes vol would be arbitrageable against the vanilla market.
- **Skew/smile risk**: Local vol makes explicit how a position's value changes as spot moves *through* the skew, capturing the difference between sticky-strike and sticky-delta hedging assumptions that flat models ignore.
- **Model risk awareness**: Because local vol mis-predicts forward smile dynamics, vol traders treat the gap between local-vol and stochastic-vol prices for a given exotic as a measure of model risk and a source of [[volatility-arbitrage|relative-value]] opportunity. Understanding which model a counterparty marks against can itself be an edge.

## Sources

- Dupire, B. (1994). "Pricing with a Smile." *Risk* 7 (1): 18-20. — the original local-volatility formula.
- Derman, E. and Kani, I. (1994). "Riding on a Smile." *Risk* 7 (2). — independent binomial-tree formulation.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley. — definitive treatment of local vol, the Dupire formula, and local-vs-stochastic dynamics.
- Sheldon Natenberg, *Option Volatility and Pricing* (see [[book-option-volatility-and-pricing]]). — practitioner background on volatility surfaces.

## Related

- [[implied-volatility]] -- the market quotes local vol calibrates to
- [[volatility-surface]] -- the input local vol reproduces exactly
- [[volatility-smile]], [[volatility-skew]] -- the surface features local vol explains
- [[historical-volatility]], [[realized-volatility]] -- backward-looking volatility measures
- [[options]] -- instruments priced with local vol
