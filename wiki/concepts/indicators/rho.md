---
title: "Rho"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, indicators]
aliases: ["Rho", "interest-rate sensitivity", "rho greek"]
related: ["[[options-greeks]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[black-scholes]]", "[[put-call-parity]]", "[[leaps]]"]
domain: [derivatives, risk-management]
prerequisites: ["[[options-greeks]]", "[[interest-rates]]"]
difficulty: intermediate
---

**Rho** measures the sensitivity of an option's price to a change in the risk-free [[interest-rates|interest rate]], conventionally expressed as the change in option value for a 1-percentage-point (100 bps) move in rates. It is generally the least significant of the primary [[options-greeks]] for short-dated contracts, but becomes material for long-dated options such as [[leaps|LEAPS]] and in high-rate or rapidly shifting rate environments.

## Overview

Interest rates enter option pricing through the cost of carry: holding the underlying ties up capital, and the option's fair value reflects the financing cost of replicating the position. Higher rates increase the forward price of the underlying, which raises call values and lowers put values.

- **Calls have positive rho** — their value rises as rates rise.
- **Puts have negative rho** — their value falls as rates rise.

Rho is small relative to [[delta]], [[gamma]], [[theta]], and [[vega]] for most retail-tenor options, which is why it is often the last Greek considered. Its importance scales with time to expiration and with the level and volatility of short-term rates.

## How It Works

### Mathematical Definition

Rho is the partial derivative of the option value V with respect to the risk-free rate r:

**Rho = dV/dr**

In the [[black-scholes]] model, for a non-dividend-paying underlying:

```
Rho_call = +K * T * e^(-rT) * N(d2)
Rho_put  = -K * T * e^(-rT) * N(-d2)
```

where K is the [[strike-price|strike]], T is time to expiration in years, r is the risk-free rate, and N(·) is the cumulative normal distribution. By convention, the figure is divided by 100 to express the change per 1-percentage-point rate move.

The presence of T in the formula is the key intuition: **rho grows roughly linearly with time to expiration.** A 2-year LEAPS has far more rho than a weekly option, all else equal. Deep in-the-money options also carry larger absolute rho because N(d2) approaches 1.

### Rho and Put-Call Parity

Rho is the Greek most directly tied to [[put-call-parity]]. Parity states:

> Call − Put = Spot − Strike × e^(−rT)

Differentiating with respect to r shows that the difference in rho between a call and put at the same strike and tenor equals the discounted strike's rate sensitivity. This is why call and put rho have opposite signs and why the magnitudes are governed by the discounted strike term.

## When Rho Matters

- **LEAPS and long-dated options**: with T measured in years, rho can rival vega in size. A surprise rate cut or hike meaningfully repaths long-dated option values.
- **High-rate regimes**: when short rates move from ~0% to 5%+, the cumulative effect on the forward and on discounting is large enough to shift even medium-dated option values.
- **Box spreads and synthetic financing**: traders use [[options]] structures (e.g., box spreads) as synthetic borrowing/lending instruments; rho is the operative Greek for valuing that embedded financing.
- **Rate-event positioning**: around FOMC decisions, the rho component of a long-dated book can be a deliberate or unintended exposure.

## Trading Relevance

For most short-dated directional and income strategies, rho is negligible and traders focus on delta, theta, and vega. Rho becomes a real consideration when:

- Running a book of **long-dated calls** (positive rho) that benefits from rising rates, or **long-dated puts** (negative rho) that suffers from them.
- Using deep-ITM LEAPS calls as a **stock replacement** — the position carries embedded financing and therefore rho exposure that behaves differently from holding the shares outright.
- Holding large notional structures where the discounting term materially affects valuation and a parallel rate shift moves the mark.

Professional desks aggregate net rho across the portfolio alongside the other Greeks, but for typical retail option tenors (under ~90 days) it rarely drives decisions.

## Related

- [[options-greeks]] — the full family of sensitivities
- [[delta]] — sensitivity to the underlying price
- [[gamma]] — rate of change of delta
- [[theta]] — time decay
- [[vega]] — sensitivity to implied volatility
- [[black-scholes]] — pricing model that produces rho
- [[put-call-parity]] — relationship governing call vs put rho
- [[leaps]] — long-dated options where rho is most relevant
- [[interest-rates]]

## Sources

- Hull, J. C., *Options, Futures, and Other Derivatives* (10th ed.) — derivation of rho and the Black-Scholes Greeks
- Natenberg, S., *Option Volatility and Pricing* — practitioner treatment of rho and interest-rate effects on option value
- Black, F. and Scholes, M., "The Pricing of Options and Corporate Liabilities," *Journal of Political Economy* (1973) — original model from which rho is derived
