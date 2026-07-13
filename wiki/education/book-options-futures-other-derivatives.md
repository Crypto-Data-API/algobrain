---
title: "Options, Futures, and Other Derivatives (John C. Hull)"
type: source
created: 2026-04-15
updated: 2026-06-20
status: good
tags: [book, education, options, futures, derivatives]
source_type: book
source_author: "John C. Hull"
source_date: 1988
confidence: high
aliases: ["Options, Futures, and Other Derivatives", "Hull's Derivatives", "The Hull Book", "John Hull Derivatives"]
related: ["[[options]]", "[[futures]]", "[[derivatives]]", "[[black-scholes]]", "[[greeks]]", "[[risk-management]]", "[[volatility]]"]
---

*Options, Futures, and Other Derivatives* by John C. Hull is the most widely used textbook on [[derivatives]] pricing and [[risk-management|risk management]], often referred to as "the bible" of derivatives. First published in 1988, it is now in its 11th edition (2022) and is a required text in virtually every MBA program, quantitative finance curriculum, and derivatives training program worldwide.

## Overview

The book provides a comprehensive treatment of derivatives markets, pricing theory, and risk management, covering both the theory and practical application of [[options]], [[futures]], swaps, and exotic instruments. Hull's approach is distinctive for making rigorous quantitative concepts accessible without sacrificing mathematical precision — the main text uses intuitive explanations and examples, while appendices provide the formal proofs and derivations for more advanced readers.

## Key Topics Covered

### Fundamentals
- Mechanics of futures and forward markets — contract specs, margins, settlement, delivery
- Hedging strategies using [[futures]] — basis risk, cross-hedging, optimal hedge ratio
- Interest rate markets — Treasury bonds, day count conventions, duration and convexity
- Determination of forward and futures prices — cost of carry model

### Options
- Mechanics of [[options]] markets — calls, puts, exchange-traded vs. OTC
- Properties of stock options — bounds, put-call parity, early exercise
- Trading strategies involving options — spreads, combinations, covered calls, protective puts
- The [[binomial-trees|binomial tree]] model — one-step and multi-step pricing, risk-neutral valuation
- The [[black-scholes|Black-Scholes-Merton]] model — derivation, assumptions, implications, and the BSM formula
- The [[greeks|Greeks]] — delta, gamma, theta, vega, rho — and their use in hedging and risk management

### Advanced Topics
- Volatility smiles and surfaces — why Black-Scholes implied [[volatility]] varies by strike and maturity
- Exotic options — barrier options, Asian options, lookback options, compound options, chooser options
- Credit derivatives — credit default swaps, CDOs, and their role in the 2008 financial crisis
- Interest rate derivatives — caps, floors, swaptions, the LIBOR market model, Hull-White model
- Value at Risk (VaR) — historical simulation, model-building approach, Monte Carlo methods
- Real options — applying options pricing to capital budgeting decisions
- Energy and commodity derivatives

### Later Editions
More recent editions have expanded coverage of:
- OIS discounting and the transition from LIBOR to SOFR/risk-free rates
- Central clearing and its impact on derivatives markets post-2008 regulation
- Machine learning applications in derivatives pricing and risk management
- Climate finance and ESG derivatives
- Cryptocurrency derivatives

## Why It Matters

Hull's text is significant for several reasons:

1. **Industry standard** — It is the reference text for the CFA, FRM (Financial Risk Manager), and most quantitative finance certifications. Practitioners and academics speak a common language because of this book.
2. **Bridges theory and practice** — Hull includes real-world examples, case studies (including Barings Bank, Long-Term Capital Management, and the 2008 crisis), and practical considerations like transaction costs and model limitations.
3. **Black-Scholes treatment** — The book's explanation of the [[black-scholes|Black-Scholes]] model, including its derivation via Ito's lemma and risk-neutral pricing, is considered one of the clearest available and has shaped how generations of practitioners understand options pricing.
4. **Greek management** — Hull's treatment of the [[greeks|Greeks]] and dynamic hedging is the basis for how options traders and risk managers think about portfolio exposure.

## Who It's For

The book is written to scale across audiences, which is part of why it became the standard:

- **Students** — MBA, master's-in-finance, and financial-engineering students use it as the core derivatives text; the worked examples and end-of-chapter problems make it self-teachable.
- **Certification candidates** — those sitting the CFA and especially the FRM (Financial Risk Manager) exams rely on it; Hull's notation and framing are echoed in those curricula.
- **Practitioners** — options market makers, [[risk-management|risk managers]], and quants use it as a reference for pricing conventions, [[greeks|Greek]] definitions, and hedging logic.
- **Self-directed retail traders** — the early chapters on the mechanics of [[options]] and [[futures]] markets, trading strategies, and [[put-call-parity|put-call parity]] are accessible without heavy mathematics; the later chapters (stochastic calculus, interest-rate models) demand more background.

A reader who wants the same content with less mathematics is usually pointed to Hull's shorter companion, *Fundamentals of Futures and Options Markets*.

## Companion Resources

- **Student Solutions Manual** — Worked solutions to end-of-chapter problems
- **DerivaGem** — Software included with the book for pricing options, building binomial trees, and running Monte Carlo simulations
- **Fundamentals of Futures and Options Markets** — A shorter, less mathematical companion text by Hull aimed at undergraduate and practitioner audiences

## Related

- [[options]] — primary subject of the book
- [[futures]] — extensively covered in the early chapters
- [[derivatives]] — the broader asset class treated
- [[black-scholes]] — the central pricing model explained in detail
- [[greeks]] — practical risk metrics for options traders
- [[risk-management]] — Hull's framework for managing derivatives risk
- [[binomial-trees]] — the discrete pricing model Hull builds toward Black-Scholes
- [[put-call-parity]] — a no-arbitrage relationship covered in the options-properties chapters
- [[value-at-risk]] — covered in Hull's risk-measurement chapters
- [[volatility]] — implied vol, smiles, and surfaces treated in the advanced chapters

## Sources

- *Options, Futures, and Other Derivatives*, John C. Hull (Pearson) — the book itself; first edition 1988, latest editions extend to OIS/SOFR, central clearing, and machine-learning topics. Bibliographic facts (author, publisher, edition history, companion titles, DerivaGem software) are matters of public record.
- General market knowledge; no specific wiki source ingested yet.
