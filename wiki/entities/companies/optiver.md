---
title: "Optiver"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [market-maker, quantitative, options, derivatives, etf, company, hft]
entity_type: company
aliases: ["Optiver Holding B.V.", "Optiver V.O.F."]
founded: 1986
headquarters: "Amsterdam, Netherlands"
website: "https://www.optiver.com"
related: ["[[market-maker]]", "[[options]]", "[[delta-hedge]]", "[[gamma-scalping]]", "[[volatility-surface]]", "[[jane-street]]", "[[citadel-securities]]", "[[susquehanna-international-group]]", "[[imc-trading]]", "[[hudson-river-trading]]", "[[volatility-skew]]"]
---

Optiver is a global proprietary trading firm and one of the largest electronic [[options]] [[market-maker|market makers]] in the world. Founded in Amsterdam in 1986 by a single floor trader on the European Options Exchange, Optiver now operates trading desks in Amsterdam, Chicago, Sydney, Shanghai, Hong Kong, Mumbai, Taipei, Austin and London, and is consistently ranked among the top liquidity providers in listed equity and index options.

## Overview

Optiver risks only its own capital and accepts no client orders. Its core business is making continuous two-sided markets in tens of thousands of options series across equity indices, single stocks, ETFs, futures and bonds. Like [[jane-street]] and [[susquehanna-international-group]], the firm derives most of its profit from capturing the [[bid-ask-spread]] while continuously hedging the resulting risk via [[delta-hedge|delta hedging]], [[gamma-scalping|gamma scalping]] and cross-product offsets.

The firm is known for hiring heavily out of mathematics, physics and computer science, running a graduate trading program in Amsterdam, and for being one of the early adopters of fully automated quoting in European listed options. Optiver's trading floors are organised by underlying (e.g. SPX, AEX, Nikkei) rather than by strategy, with quants, traders and developers sitting together on the same desk.

## Use of AI and Quantitative Methods

Optiver was a pioneer in moving options market making from voice-driven floor trading to automated electronic quoting through the late 1990s and 2000s. Modern Optiver pricing systems combine:

- Real-time [[volatility-surface]] fitting and recalibration on every trade
- Statistical models that translate observed [[order-flow]] into short-horizon price forecasts
- Machine-learning models for inventory risk, [[adverse-selection]] detection, and quote-adjustment logic
- Cross-product hedge optimisation between options, futures and the underlying

Optiver publishes regularly on quantitative finance topics through its tech blog, and runs the well-known Optiver "Trading Challenge" used as a recruiting funnel. Several open-source tools (such as the `dwave` SDK contributions and the public Optiver Realized Volatility Prediction Kaggle competition in 2021) originate from the firm's research teams.

## Trading Activities

### Listed Options Market Making

Optiver provides liquidity in equity and index options on Eurex, Euronext, CBOE, ASX, HKEX and other venues. The firm is one of the dominant quoters in European index options (AEX, Euro Stoxx 50, DAX) and a major participant in US options.

### ETF and Futures Market Making

Optiver also markets-makes ETFs and futures, using these instruments as hedges for its options book and as standalone profit centres.

### Asia-Pacific Expansion

Sydney has historically been Optiver's second-largest office and a hub for trading Asian options markets, including Hang Seng, KOSPI 200, Nikkei 225 and ASX index options.

## Financial Results (2024-2025)

Optiver is private (no ticker — traders cannot get direct exposure), but unusually for a prop firm it publishes annual results:

| Year | Net trading income | Net profit (equity holders) | Total equity |
|---|---|---|---|
| 2023 | €2.773B | €1.158B | €4.10B |
| 2024 | €3.494B (+26%) | €1.369B (+18%) | €4.905B |
| 2025 | €4.556B (+30%) | €1.769B (+29%) | €5.490B |

The 2025 result — published March 2026, coinciding with the firm's 40th anniversary — reflected elevated volatility regimes through 2025, continued expansion into US capital markets (including a new New York office), entry into new asset classes, and a deepening presence in China and India. These numbers are a useful benchmark for the profitability of top-tier options market making and for sizing the competitive moat around retail-visible spreads (Verified via web sources, 2026-06-10).

## Trading Relevance

For active options traders, Optiver's behaviour matters in several ways:

- **Tight spreads in liquid names** — Optiver, [[susquehanna-international-group|SIG]], [[citadel-securities|Citadel]] and [[imc-trading|IMC]] competing on the same SPX strike is a major reason retail SPX spreads are typically a few cents wide.
- **Spread widening into events** — automated quoters pull or widen quotes around earnings, FOMC, and macro releases as their inventory risk models flag elevated [[adverse-selection]].
- **Vol-surface arbitrage** — Optiver's continuous recalibration of the [[volatility-surface]] suppresses many simple smile/skew arbitrages that retail traders read about in textbooks.

## Related

- [[market-maker]] — Optiver's primary role
- [[options]] — core asset class
- [[delta-hedge]] — primary risk-management tool
- [[gamma-scalping]] — major intraday P&L source for vol market makers
- [[volatility-surface]] — what Optiver continuously fits and trades against
- [[jane-street]], [[susquehanna-international-group]], [[citadel-securities]], [[imc-trading]], [[hudson-river-trading]] — peer firms
- [[adverse-selection]] — primary risk for any market maker
- [[high-frequency-trading]] — Optiver competes with HFT firms in some products

## Sources

*No raw sources ingested yet. This page is based on public information about Optiver's trading operations, conference talks and recruiting materials.*

- [Optiver reports robust financial results for 2025 (optiver.com)](https://optiver.com/optiver-reports-robust-financial-results-for-2025/)
- [Optiver reports strong financial results for 2024 (optiver.com)](https://optiver.com/optiver-reports-strong-financial-results-for-2024/)
- [Optiver Annual Review 2025 (PDF)](https://optiver.com/wp-content/uploads/2026/03/Optiver_Annual_Review_2025.pdf)
- Verified via web sources, 2026-06-10
