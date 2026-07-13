---
title: "Black-Derman-Toy Model"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [derivatives, quantitative, bonds, volatility]
aliases: ["Bdt Model", "BDT Model", "Black-Derman-Toy", "Black Derman Toy"]
domain: [quantitative]
prerequisites: ["[[interest-rate-derivatives]]", "[[yield-curve]]", "[[volatility]]"]
difficulty: advanced
related: ["[[interest-rate-derivatives]]", "[[yield-curve]]", "[[term-structure]]", "[[binomial-tree]]", "[[ho-lee-model]]", "[[hull-white-model]]", "[[options-pricing]]", "[[bonds]]", "[[volatility]]"]
---

The **Black-Derman-Toy (BDT) model** is a one-factor short-rate model used to price interest-rate derivatives — bond options, caps, floors, swaptions, and callable bonds. Published in 1990 by Fischer Black, Emanuel Derman, and Bill Toy at Goldman Sachs, it was one of the first models to be **calibrated simultaneously to the observed [[yield-curve]] and to a term structure of interest-rate volatilities**, making it a practical desk tool rather than a purely theoretical construct.

## Mechanics

BDT models the evolution of the **short rate** (the instantaneous risk-free rate) on a recombining [[binomial-tree]]. Its defining choice is that the short rate is **lognormally distributed**, which guarantees rates stay positive (a feature, historically, though a limitation in negative-rate regimes). The continuous-time dynamics of the log short rate are:

```
d(ln r) = [ θ(t) + (σ'(t)/σ(t))·ln r ] dt + σ(t) dW
```

where:
- **θ(t)** is a time-dependent drift chosen so the model reproduces today's yield curve exactly,
- **σ(t)** is the time-dependent short-rate volatility, calibrated to market cap/swaption volatilities,
- **σ'(t)/σ(t)** is the mean-reversion term — uniquely in BDT, the speed of mean reversion is *tied to* the slope of the volatility term structure rather than being an independent parameter.

In practice the model is built as a binomial lattice: at each node the rate can move up or down, the up/down spacing is set by σ(t), and the level is shifted by θ(t) so that discounting back through the tree reprices the current zero-coupon bond curve. Once calibrated, any rate-contingent payoff (a callable bond, a cap) is valued by backward induction through the lattice.

## Place Among Short-Rate Models

- **[[ho-lee-model|Ho-Lee]] (1986)** — the first arbitrage-free, yield-curve-fitting short-rate model; normal rates, no mean reversion. BDT extends it with lognormal rates and volatility fitting.
- **BDT (1990)** — lognormal, fits curve + vol term structure; mean reversion implied by vol slope.
- **Black-Karasinski (1991)** — generalizes BDT by decoupling mean reversion from the volatility structure.
- **[[hull-white-model|Hull-White]] (1990)** — normal/extended-Vasicek, analytically tractable, the more common modern choice; allows independent mean reversion and (unlike BDT) closed-form bond-option prices.

## Trading Relevance

For a fixed-income or rates trader, the value of a model like BDT is **relative-value pricing and hedging of rate options**: it produces an arbitrage-free, market-consistent surface from which to price exotic or illiquid instruments (callable/putable bonds, Bermudan swaptions) and to extract hedge ratios. Because BDT is calibrated to *both* the curve and the vol term structure, it is naturally used where the volatility smile/term structure matters. Its limitations explain why desks largely migrated to Hull-White and multi-factor / LIBOR-market models: BDT lacks closed-form solutions (everything is lattice-based and slow), its mean reversion cannot be controlled independently of volatility, and its strictly-positive lognormal rates cannot represent the negative-rate environments seen in EUR and JPY markets post-2014. It remains pedagogically central and a clear illustration of arbitrage-free calibration — the principle that any usable derivatives model must first reprice the liquid instruments it will be used to hedge against.

## Related

- [[interest-rate-derivatives]] — the instruments BDT prices
- [[yield-curve]] / [[term-structure]] — what the model is calibrated to
- [[binomial-tree]] — the numerical lattice BDT is built on
- [[ho-lee-model]] / [[hull-white-model]] — the neighbouring short-rate models
- [[volatility]] — the term structure BDT additionally fits

## Sources

- Black, F., Derman, E. & Toy, W. (1990), "A One-Factor Model of Interest Rates and Its Application to Treasury Bond Options," *Financial Analysts Journal*.
- John C. Hull, *Options, Futures, and Other Derivatives* — chapter on interest-rate models (Ho-Lee, BDT, Hull-White).
- Emanuel Derman, *My Life as a Quant* (2004) — first-person account of the model's development at Goldman Sachs.
- Damiano Brigo & Fabio Mercurio, *Interest Rate Models — Theory and Practice* (2006).
