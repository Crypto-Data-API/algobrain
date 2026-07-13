---
title: "IMC Trading"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [market-maker, quantitative, options, etf, derivatives, company, hft]
entity_type: company
aliases: ["IMC", "International Marketmakers Combination", "IMC Financial Markets"]
founded: 1989
headquarters: "Amsterdam, Netherlands"
website: "https://www.imc.com"
related: ["[[market-maker]]", "[[options]]", "[[etf]]", "[[delta-hedge]]", "[[volatility-surface]]", "[[optiver]]", "[[jane-street]]", "[[citadel-securities]]", "[[susquehanna-international-group]]", "[[hudson-river-trading]]"]
---

IMC Trading is a global proprietary trading firm and major [[market-maker|market maker]] in [[options]], [[etf|ETFs]], futures, equities and bonds. Founded in Amsterdam in 1989, IMC is — alongside [[optiver]] — one of the two large Dutch options market makers that emerged from the European Options Exchange (EOE) era and grew into globally-significant electronic liquidity providers.

## Overview

IMC operates trading floors in Amsterdam, Chicago, Sydney, Mumbai and Hong Kong with roughly 1,000 employees globally. Like [[optiver]], [[susquehanna-international-group|SIG]] and [[jane-street]], IMC trades only its own capital and accepts no external client orders. Its core business is providing two-sided liquidity in listed derivatives across European, US and Asian venues.

The firm is structured around tightly-integrated trading desks where traders, quantitative researchers and software engineers sit together. IMC publishes regularly on quantitative finance topics through its tech blog and is well known for sponsoring the IMC Prosperity competitions, large-scale algorithmic trading puzzles run for university students.

## Use of AI and Quantitative Methods

IMC's options pricing infrastructure rebuilds the [[volatility-surface]] for each underlying continuously and quotes thousands of strikes simultaneously. Public talks and engineering job postings indicate the firm uses:

- Real-time vol-surface fitting with proprietary smoothing and arbitrage-free constraints
- Machine-learning models for [[order-flow]] toxicity, [[adverse-selection]] detection and inventory management
- Reinforcement learning ([[reinforcement-learning-trading]]) for execution and quoting
- Low-latency C++ and FPGA-based pricing engines for quote-update speed
- In-house simulators for stress-testing strategies under historical and synthetic regimes

For ETF market making, IMC is one of the major authorized participants on European-listed ETFs and a significant US ETF liquidity provider.

## Trading Activities

### Listed Options Market Making

IMC markets-makes options on Eurex, Euronext, CBOE, ASX and other venues. The firm is particularly strong in European index options (Euro Stoxx 50, AEX, DAX) and has grown its US options share substantially over the past decade.

### ETF Market Making

IMC is one of the larger authorized participants in European ETFs, providing primary-market creation/redemption and continuous secondary-market quoting.

### Equity and Futures

IMC also makes markets in cash equities, equity futures, fixed income futures and bond ETFs, using these instruments primarily as hedges for its options book.

## 2025-2026 Developments

- **Record 2025 results:** IMC Global Holdings reported net trading revenue of **US$3.12 billion for 2025, up 40%** year-on-year, as the firm benefited from the volatility surge; net profit attributable to shareholders was **US$968 million** (vs US$686 million in 2024), with costs up 35% (Bloomberg, March 2026). 2025 revenues were roughly 90% above 2020 levels — IMC and [[optiver]] both grew profits more than 30% in 2025.
- **Expansion:** During 2025 IMC expanded to **10 offices across 4 continents**, including a larger Hong Kong office in Central, and accelerated investment in quant research.
- **Crypto build-out:** In March 2026 IMC hired Alex Casimo as chief commercial officer for its crypto business; the firm trades roughly **US$3 billion per day across ~50 crypto exchanges**, making it one of the largest traditional-finance crypto market makers.
- **Recognition:** Named Top Market Maker and Top Principal Trading Group at the 2026 HKEX Awards.

Note: as a private partnership-style firm, IMC publishes limited financials; figures above come from Dutch filings reported by Bloomberg. Traders cannot get direct equity exposure — IMC matters as a counterparty and liquidity-regime indicator, not as an investable name.

## Trading Relevance

For active options traders, IMC's behaviour matters in several ways:

- **European options liquidity** — IMC and [[optiver]] dominate European listed option market making; spreads and depth in Euro Stoxx 50 and DAX options reflect their competitive equilibrium.
- **ETF spread tightness** — IMC's authorised-participant activity in European-listed ETFs is one of the main reasons UCITS ETF spreads compress to a few basis points in liquid names.
- **Cross-listed option arbitrage** — IMC's presence on multiple venues makes most simple cross-exchange arbitrages in liquid names uneconomic for non-co-located traders.

## Related

- [[market-maker]] — IMC's primary role
- [[options]] — core asset class
- [[etf]] — major IMC business line
- [[volatility-surface]] — what IMC continuously fits
- [[delta-hedge]] — primary risk-management tool
- [[optiver]], [[jane-street]], [[susquehanna-international-group]], [[citadel-securities]], [[hudson-river-trading]] — peer firms
- [[reinforcement-learning-trading]] — public area of IMC quant research
- [[adverse-selection]] — primary risk IMC manages

## Sources

*No raw sources ingested yet. This page is based on public information about IMC's trading operations, IMC Prosperity competition material, and engineering blog posts.*

- Bloomberg, "Market Maker IMC's Trading Revenue Rises 40% on Volatility Surge" (26 Mar 2026) — https://www.bloomberg.com/news/articles/2026-03-26/market-maker-imc-s-trading-revenue-rises-40-on-volatility-surge
- CoinDesk, "IMC Trading hires Alex Casimo as chief commercial officer for its crypto business" (19 Mar 2026) — https://www.coindesk.com/business/2026/03/19/market-maker-imc-trading-hires-alex-casimo-as-chief-commercial-officer-for-its-crypto-business
- Rupak Ghose, "The Traders of Amsterdam" — https://rupakghose.substack.com/p/the-traders-of-amsterdam
- IMC corporate news — https://www.imc.com/us/corporate-news
- Verified via web search, 2026-06-10
