---
title: Jane Street
type: entity
entity_type: fund
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [hedge-funds, market-making, ai-trading]
related: ["[[two-sigma]]", "[[jump-trading]]", "[[de-shaw]]", "[[wintermute]]"]
---

# Jane Street

Jane Street is a quantitative market maker that trades approximately $17 billion per day and is the largest ETF market maker globally. The firm is private, consistently profitable, and famously secretive about its strategies — but unusually open about its technical culture.

## Overview

| Detail | Value |
|--------|-------|
| Founded | 2000 |
| Headquarters | New York City |
| Type | Proprietary trading firm |
| Daily trading volume | ~$17B |
| Employees | ~2,500+ |
| Key markets | ETFs, options, equities, bonds, crypto |
| Programming language | OCaml |

## Market Making Model

Jane Street is a **market maker**, not a hedge fund. The distinction matters:

- Market makers provide liquidity by continuously quoting bid and ask prices
- They profit from the spread between buy and sell prices, not from directional bets
- They aim to remain market-neutral — hedging away directional exposure
- Revenue comes from volume and pricing accuracy, not from predicting market direction

Jane Street is dominant in **ETF market making**, pricing and trading thousands of ETFs by modeling the relationships between ETFs and their underlying basket of securities. When an ETF price diverges from its net asset value, Jane Street arbitrages the difference.

## The OCaml Anomaly

Jane Street famously uses **OCaml** as its primary programming language — a functional programming language that is virtually unknown in finance. Most trading firms use C++, Python, or Java.

Why OCaml:
- **Strong type system** catches bugs at compile time rather than in production (where bugs cost money)
- **Functional programming** produces more predictable, testable code
- **Pattern matching** is well-suited for handling complex market data structures
- **Performance**: Compiled OCaml is fast enough for their latency requirements

Jane Street has become the largest commercial user of OCaml and contributes extensively to the ecosystem, including the Jane Street Core library.

## Recruiting and Culture

Jane Street is legendary for its **recruiting process**:

- Targets math olympiad winners, puzzle competition champions, and competitive programmers
- Interview process includes trading games, probability puzzles, and mental math challenges
- Recruits from math, CS, physics, and quantitative fields — not finance programs
- Intern compensation is among the highest in any industry ($16K+/month)

The firm runs an open, collaborative trading floor where information flows freely. Traders and developers work side by side.

## Strategies

Beyond ETF market making:

- **Options market making**: Pricing and trading options across equities and indices
- **Fixed income**: Bond and credit trading
- **Cryptocurrency**: Significant crypto trading operations
- **Quantitative research**: Fundamental factor models and statistical arbitrage

## Privacy

Despite its massive trading volume and profitability, Jane Street remains a private partnership. It does not manage outside capital, does not publish financial results, and rarely makes public statements about its business. Revenue estimates place it among the most profitable financial firms per employee in the world.

## See Also

- [[two-sigma]] — peer quantitative firm with different structure (hedge fund vs prop firm)
- [[jump-trading]] — another major proprietary trading firm
- [[wintermute]] — crypto market making parallel
