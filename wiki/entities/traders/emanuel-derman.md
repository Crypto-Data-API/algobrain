---
title: "Emanuel Derman"
type: entity
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [person, quantitative, derivatives, volatility, options, education]
entity_type: person
aliases: ["Emanuel Derman", "Derman"]
website: "https://emanuelderman.com"
related: ["[[goldman-sachs]]", "[[volatility-smile]]", "[[black-derman-toy]]", "[[derman-kani]]", "[[black-scholes]]", "[[fischer-black]]", "[[local-volatility]]", "[[model-risk]]", "[[my-life-as-a-quant]]", "[[quantitative-trading]]", "[[implied-volatility]]", "[[bruno-dupire]]"]
---

# Emanuel Derman

Emanuel Derman (born 1945, Cape Town, South Africa) is a physicist-turned-quant who became one of the most influential figures in quantitative finance, co-creating the [[black-derman-toy|Black-Derman-Toy]] interest-rate model and the [[derman-kani|Derman-Kani]] [[local-volatility|local volatility]] model at [[goldman-sachs|Goldman Sachs]]. His memoir *[[my-life-as-a-quant|My Life as a Quant]]* (2004) defined the public image of the Wall Street quant, and his later writing made him the field's leading critic of model overconfidence — essential reading for any trader using [[model-risk|models]] to price or trade [[derivatives]].

## Key Facts

| | |
|---|---|
| **Name** | Emanuel Derman |
| **Born** | 1945, Cape Town, South Africa |
| **Education** | PhD theoretical particle physics, Columbia University (1973) |
| **Pre-finance** | Academic physics; AT&T Bell Laboratories |
| **Wall Street** | [[goldman-sachs\|Goldman Sachs]] 1985–2002 (MD, head of Quantitative Strategies); Salomon Brothers 1988–90 |
| **Known for** | [[black-derman-toy\|Black-Derman-Toy]] model (1990); [[derman-kani\|Derman-Kani local volatility]] (1994) |
| **Signature book** | *[[my-life-as-a-quant\|My Life as a Quant]]* (2004) |
| **Honors** | IAFE/SunGard Financial Engineer of the Year (2000); *Risk* Hall of Fame (2002) |
| **Academia** | Columbia University, directed Financial Engineering MSc 2003–2023; now Professor of Practice Emeritus |
| **Theme** | [[model-risk\|Model risk]] — models are analogies/interpolation, not laws of nature |

## Overview

Derman earned a PhD in theoretical particle physics from Columbia University (1973) and spent the following decade in academic physics and at AT&T Bell Laboratories before joining Goldman Sachs in 1985. At Goldman — apart from a stint at Salomon Brothers (1988-1990) — he spent 17 years in quantitative research, eventually leading the Quantitative Strategies group and becoming a managing director. Key contributions:

- **[[black-derman-toy|Black-Derman-Toy model]] (1990)**: with [[fischer-black]] and Bill Toy, one of the first no-arbitrage interest-rate models, developed for bond options trading at Goldman and still a textbook short-rate model
- **Derman-Kani implied tree / [[derman-kani|local volatility]] model (1994)**: with Iraj Kani, a model fitting option prices across strikes to explain the post-1987 [[volatility-smile|volatility smile]] — foundational for equity derivatives desks (developed in parallel with [[bruno-dupire|Bruno Dupire]]'s continuous-time formulation)
- Influential papers on the [[volatility-smile]], [[model-risk|model risk]] ("Model Risk," 1996), and the sociology of quant work

He was named the IAFE/SunGard Financial Engineer of the Year (2000) and elected to the *Risk* magazine Hall of Fame (2002). In 2003 he moved to Columbia University, where he directed the Master's program in Financial Engineering for two decades (2003-2023). He is now **Professor of Practice Emeritus** at Columbia (Source: Columbia Engineering faculty directory; emanuelderman.com).

## The Models, Explained

**[[black-derman-toy|Black-Derman-Toy (BDT)]]** is a single-factor, no-arbitrage *short-rate* model. Rather than assuming a process and hoping it matches the market, BDT is *calibrated* so that the model reproduces today's observed yield curve and the term structure of interest-rate volatility. It is built on a binomial lattice of the short rate in which rates are lognormally distributed (so rates stay positive) and mean-revert; option-embedded instruments like callable bonds, caps, floors, and swaptions can then be priced consistently on that tree. Its practicality — calibrate to market data, then price exotics off the same tree — made it a workhorse on fixed-income desks and a standard teaching model.

**[[derman-kani|Derman-Kani local volatility]]** addresses the central post-1987 puzzle: [[black-scholes|Black-Scholes]] assumes a single constant volatility, yet market option prices imply *different* volatilities for different strikes and maturities — the [[volatility-smile|volatility smile/skew]]. Derman and Kani's "implied binomial tree" inverts the problem: it reads the observed prices of options across all strikes and expiries and backs out a *local volatility function* σ(S, t) — a volatility that depends on the underlying's price and time — such that a single tree reprices the entire smile with no arbitrage. This let a desk price and hedge exotic options (barriers, lookbacks) consistently with the vanilla options actually trading in the market. [[bruno-dupire|Bruno Dupire]] independently derived the equivalent result in continuous time (the Dupire equation) the same year; together their work founded the local-volatility paradigm that still anchors equity-derivatives modeling.

## Books

- ***[[my-life-as-a-quant|My Life as a Quant]]: Reflections on Physics and Finance* (Wiley, 2004)** — memoir of the physicist migration to Wall Street; a Business Week top-ten book and the canonical account of quant culture
- ***Models.Behaving.Badly* (Free Press, 2011)** — written after the 2008 crisis; distinguishes models (analogies, always partial) from theories (descriptions of reality), arguing financial models must be used with skepticism. Includes his "Financial Modeler's Manifesto" (2009, with Paul Wilmott): "I will remember that I didn't make the world, and it doesn't satisfy my equations"
- ***The Volatility Smile* (Wiley, 2016, with Michael B. Miller)** — graduate textbook on modern options theory, smile models, and their limits
- ***Brief Hours and Weeks* (2025)** — a memoir of his youth in the Polish-Jewish immigrant community of 1940s-60s Cape Town, praised by Nobel laureate J. M. Coetzee — his most recent publication, marking a turn to literary writing in semi-retirement

## Trading Relevance

- **Options desks live in Derman's framework**: the [[volatility-smile]] and [[local-volatility]] models he co-developed underpin how equity index and single-stock options are marked, hedged, and arbitraged
- **Fixed-income**: Black-Derman-Toy remains a reference model for pricing bond options and callable bonds
- **[[model-risk|Model risk]] discipline**: his core practical lesson — models are interpolation tools calibrated to today's market, not laws of nature — is the standard intellectual defense against blowups from over-trusted pricing models (LTCM, 2008 CDO models)
- His career arc (physics → Bell Labs → Goldman → academia) is the template for the quant career path; *[[my-life-as-a-quant|My Life as a Quant]]* remains the standard cultural onboarding text for systematic traders

## Influence and Legacy

Derman is one of the people who turned "quant" from a niche backroom role into a recognized profession and intellectual tradition. The [[derman-kani|local-volatility]] framework he co-founded is still the baseline for marking and hedging equity-index and single-stock options across the industry, and [[black-derman-toy|BDT]] remains a textbook reference for short-rate modeling. As director of Columbia's Financial Engineering program for two decades, he trained a generation of practitioners. Equally influential is his role as the field's conscience: *Models.Behaving.Badly* and the "Financial Modelers' Manifesto" (with Paul Wilmott) articulated, before and after the 2008 crisis, the discipline of [[model-risk|model risk]] — that a financial model is a deliberately partial *analogy* calibrated to current prices, never a law of nature, and must be used with humility. That distinction is now standard intellectual armor against the over-trusted models implicated in blowups such as LTCM and the 2008 structured-credit crisis.

## Related

- [[goldman-sachs]] — where he built his models (1985-2002)
- [[fischer-black]] — co-author of the Black-Derman-Toy model
- [[black-derman-toy]] — his no-arbitrage short-rate model
- [[derman-kani]] — the implied-tree local volatility model
- [[bruno-dupire]] — independent co-founder of local volatility
- [[volatility-smile]] — the phenomenon his work explained
- [[local-volatility]] — the model class he co-founded
- [[implied-volatility]] — the surface his models calibrate to
- [[black-scholes]] — the baseline model the smile contradicts
- [[model-risk]] — the concept he formalized for finance
- [[my-life-as-a-quant]] — his canonical memoir of quant culture
- [[quantitative-trading]] — the field he helped legitimize

## Sources

- Emanuel Derman, personal site / "About Me" — https://emanuelderman.com/about/
- Columbia Engineering faculty directory, "Emanuel Derman" (Professor of Practice Emeritus; directed financial engineering program 2003-2023) — https://www.engineering.columbia.edu/faculty-staff/directory/emanuel-derman
- Wikipedia, "Emanuel Derman" — https://en.wikipedia.org/wiki/Emanuel_Derman
- *My Life as a Quant: Reflections on Physics and Finance* (Wiley, 2004) — ISBN 978-0471394204
- Derman & Wilmott, "The Financial Modelers' Manifesto" (2009) — SSRN 1324878
- Verified via Perplexity + web search, 2026-06-10 (emeritus status and 2025 memoir *Brief Hours and Weeks* confirmed)
