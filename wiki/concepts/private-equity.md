---
title: "Private Equity"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, leverage, company]
aliases: ["Private Equity", "PE", "private equity", "private equity firm", "PE fund", "Buyout Funds"]
domain: [fundamental-analysis]
prerequisites: ["[[valuation]]", "[[leverage]]"]
difficulty: intermediate
related: ["[[venture-capital]]", "[[leveraged-buyout]]", "[[valuation]]", "[[hedge-funds]]", "[[productivity-j-curve]]", "[[discounted-cash-flow]]", "[[ipo]]", "[[capital-structure]]"]
---

Private equity (PE) refers to investment funds and firms that acquire ownership stakes in companies not publicly traded on stock exchanges, or that take public companies private through buyout transactions. PE firms raise capital from institutional investors, pool it into closed-end funds with a defined ~10-year life, and deploy it to buy, restructure, and ultimately sell portfolio companies at a profit. For public-market traders, PE matters because it shapes the supply of [[ipo|IPOs]], drives take-private deal flow, and is a competing destination for institutional capital.

## Overview

PE firms (general partners, GPs) raise capital from institutional investors and high-net-worth individuals (limited partners, LPs) — pension funds, endowments, sovereign wealth funds, insurers — pooling it into funds with a defined lifespan, typically 10-12 years. The fund **commits** capital that is then **called** ("drawn down") over a 3-5 year investment period as deals close, and **distributed** back as portfolio companies are exited.

The standard fee structure is **"2 and 20"**: a ~2% annual management fee on committed capital plus 20% **carried interest** (carry) on profits above a **hurdle rate** (preferred return, usually ~8%). Carry is often subject to a high-water mark and a GP catch-up. This structure aligns GP incentives toward large absolute gains but also rewards simply gathering assets.

## Strategies

| Strategy | Description |
|---|---|
| **Leveraged buyout ([[leveraged-buyout|LBO]])** | Acquire a mature, cash-generative company using significant debt; improve operations and margins; exit via sale or IPO in 3-7 years. The flagship PE strategy. |
| **Growth equity** | Minority stakes in already-profitable companies needing capital to scale. Lower leverage, lower risk than LBO. |
| **[[venture-capital]]** | Early-stage, high-risk/high-reward equity in startups; returns follow extreme [[power-laws|power laws]]. |
| **Distressed / special situations** | Buy debt or equity of troubled companies at a discount, often to control via restructuring. |
| **Secondaries** | Buy existing LP fund stakes from investors seeking liquidity before fund maturity. |

Major firms include Blackstone, KKR, Apollo, Carlyle, TPG, and Ares, collectively managing trillions in assets.

## The LBO and value-creation mechanics

An LBO sponsor typically funds an acquisition with 40-70% debt secured against the target's own cash flows and assets. Returns are generated through three levers:

1. **Deleveraging** — using the company's free cash flow to pay down acquisition debt, transferring enterprise value from creditors to equity over the hold.
2. **EBITDA growth** — operational improvement, bolt-on acquisitions, margin expansion.
3. **Multiple expansion** — exiting at a higher EV/EBITDA multiple than the entry multiple (the least controllable, most market-dependent lever).

[[leverage]] magnifies equity returns but also magnifies risk: a modest operating shortfall can wipe out the thin equity layer, which is why over-levered LBOs are vulnerable in rising-rate or recessionary regimes.

## Performance measurement

PE returns are not measured by simple time-weighted returns because cash flows are irregular and GP-controlled:

- **IRR (internal rate of return)** — the discount rate that sets the net present value of all cash flows to zero. Sensitive to timing and can be flattered by early distributions or subscription-line financing.
- **MOIC / TVPI (multiple of invested capital / total value to paid-in)** — total value returned per dollar invested, ignoring timing.
- **DPI (distributions to paid-in)** — realized cash returned, the "money in the bank" figure.
- **PME (public market equivalent)** — benchmarks PE against what the same cash flows would have earned in a public index, the fairest apples-to-apples comparison.

## The J-curve

A defining feature is the **J-curve**: fund net returns are negative in early years (management fees charged, investments held at cost) before turning positive as portfolio companies mature and exit. This is conceptually distinct from — but named after the same shape as — the [[productivity-j-curve]] in technology adoption. The illiquidity of PE (LPs cannot redeem before fund term) is one justification for an **illiquidity premium**, though academic literature debates whether realized PE returns actually beat leveraged public-equity benchmarks after fees.

## Trading relevance

- **IPO supply and exit windows.** PE and VC exits are a primary source of new public listings. Heavy PE-backed IPO calendars can signal sponsors selling at perceived market tops; thin calendars signal closed exit windows (a market-stress tell).
- **Take-private deal flow.** Public companies trading below sponsors' intrinsic-value estimates become LBO targets; rumored or announced take-privates create event-driven, [[merger-arbitrage|merger-arb]]-style opportunities and re-rate comparable names.
- **Listed PE as a tradeable proxy.** Blackstone (BX), KKR, Apollo (APO), Carlyle (CG), and Ares (ARES) are publicly traded; their stocks offer liquid exposure to PE economics (fee-related earnings + carry) and are sensitive to rates, credit spreads, and fundraising cycles.
- **Credit-cycle sensitivity.** LBO debt feeds the leveraged-loan and high-yield markets; PE health is tightly coupled to credit spreads and refinancing conditions. A credit crunch starves new deals and stresses existing portfolios.
- **The "privatization" of markets.** Companies staying private longer (Stripe, SpaceX, etc.) shrinks the public opportunity set and concentrates early growth gains with PE/VC LPs rather than public investors — a structural shift in where equity returns are captured.
- **Valuation lag.** PE marks are reported quarterly and smoothed, creating an artificial appearance of low volatility ("volatility laundering") that flatters Sharpe ratios versus daily-marked public equities.

## Related

- [[venture-capital]] — early-stage cousin of PE
- [[leveraged-buyout]] — the core PE transaction type
- [[valuation]] — the discipline underlying entry/exit pricing
- [[discounted-cash-flow]] — the model used to underwrite deals
- [[hedge-funds]] — the other major alternative-asset class
- [[ipo]] — the primary PE exit route
- [[productivity-j-curve]] — same J-curve shape, different domain
- [[capital-structure]] — debt/equity layering central to LBOs

## Sources

- Kaplan, S. & Strömberg, P. (2009). "Leveraged Buyouts and Private Equity." *Journal of Economic Perspectives* — academic survey of PE returns and mechanics.
- Phalippou, L. *Private Equity Laid Bare* — critical analysis of PE fee structures, IRR manipulation, and benchmark comparisons.
- Rosenbaum, J. & Pearl, J. *Investment Banking: Valuation, LBOs, M&A* — standard LBO modeling reference.
