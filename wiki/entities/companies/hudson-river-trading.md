---
title: "Hudson River Trading"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [market-maker, hft, quantitative, options, derivatives, company, algorithmic-trading]
entity_type: company
aliases: ["HRT", "Hudson River Trading LLC"]
founded: 2002
headquarters: "New York, USA"
website: "https://www.hudson-trading.com"
related: ["[[market-maker]]", "[[high-frequency-trading]]", "[[hft]]", "[[citadel-securities]]", "[[jane-street]]", "[[jump-trading]]", "[[optiver]]", "[[smart-order-routing]]", "[[options]]", "[[market-making]]"]
---

Hudson River Trading (HRT) is a New York-based proprietary trading firm and one of the largest [[high-frequency-trading|high-frequency]] electronic [[market-maker|market makers]] in US equities, ETFs, options, futures, fixed income and crypto. Founded in 2002 by a group of MIT computer scientists and mathematicians, HRT is estimated to handle roughly 10% of all US equity trading volume on some days and is a top-five participant in US options market making.

## Overview

HRT is a pure proprietary trading firm — it trades only its own capital and accepts no external client orders or assets under management. The firm's core business is providing two-sided liquidity across public markets, capturing [[bid-ask-spread|bid-ask spreads]], and managing inventory risk via cross-asset hedging. HRT's culture is heavily research- and engineering-driven, with the firm publicly emphasising that its competitive edge comes from algorithms, infrastructure and statistical modelling rather than from any privileged information channel.

The firm employs over 800 people, with major offices in New York, Chicago, Austin, London, Singapore, Mumbai, Dublin and Boulder. It is known for paying among the highest compensation packages of any quant firm to entry-level engineers and quantitative researchers, and for its open-source contributions in the systems and networking space.

## Use of AI and Quantitative Methods

HRT operates one of the most sophisticated machine-learning trading stacks in the industry. Public job postings and conference talks indicate the firm uses:

- Deep-learning and gradient-boosting models on microsecond-resolution market data for short-horizon price prediction
- Reinforcement-learning approaches to execution and inventory management ([[reinforcement-learning-trading]])
- Custom hardware (FPGAs, kernel-bypass networking) to deliver ML inference within nanoseconds of a market event
- Automated [[smart-order-routing]] across hundreds of venues, with routing decisions driven by per-venue fill-probability models

For options trading specifically, HRT's models continuously price the [[volatility-surface]] for thousands of underlyings and quote across multiple exchanges, with cross-product hedges against the underlying equity, ETFs and futures.

## Trading Activities

### Equity and ETF Market Making

HRT is one of the largest US equity market makers by volume, providing liquidity on NYSE, NASDAQ, IEX, MEMX and other lit venues, as well as off-exchange.

### Options Market Making

HRT operates a large options market-making business, competing directly with [[citadel-securities|Citadel Securities]], [[susquehanna-international-group|Susquehanna]], [[optiver]] and [[jane-street]]. Its options activity is heavily integrated with its underlying-equity book — a single risk system manages delta exposure across both.

### Crypto and FX

HRT entered crypto market making in 2018 via its HRT Crypto unit and is a major liquidity provider on US-regulated venues such as CME crypto futures, Coinbase and on regulated crypto options venues.

## 2025-2026 Developments

- **Record 2025 revenue:** Bloomberg reported HRT's 2025 net trading revenue was on track for a record **~$12.3 billion** (vs ~$8 billion in 2024), driven by elevated volatility and global market-making share gains — putting HRT in the same revenue league as Citadel Securities and [[jane-street]].
- **Strategy broadening:** HRT continued expanding beyond classic short-horizon HFT into longer-hold systematic strategies, including credit and other multi-asset trades — mirroring the industry-wide convergence of HFT firms and quant hedge funds.
- **Headcount and office growth** continued across New York, London, Singapore and Mumbai, with entry-level quant/dev compensation packages reported among the highest in the industry.
- As a private partnership, HRT discloses no audited public financials; revenue figures are press estimates and should be treated as approximate.

## Trading Relevance

For active options traders, HRT matters in several ways:

- **Speed-driven [[adverse-selection]]** — HRT's microsecond-scale models update quotes faster than retail can respond. Stale-quote arbitrage that worked against floor market makers in the 2000s is essentially closed by HRT-style firms.
- **Quote depth in liquid names** — HRT participating in a name correlates with tighter spreads and deeper top-of-book size.
- **Liquidity withdrawal in stress** — During flash events and macro releases, HRT (along with peers) widens or pulls quotes; this is a major contributor to the [[liquidity-evaporation]] pattern observed in [[circuit-breakers|circuit-breaker]] events.

## Related

- [[market-maker]] — HRT's primary role
- [[high-frequency-trading]], [[hft]] — HRT is one of the canonical HFT firms
- [[smart-order-routing]] — central to HRT's equity execution
- [[citadel-securities]], [[jane-street]], [[jump-trading]], [[optiver]], [[susquehanna-international-group]], [[imc-trading]] — peer firms
- [[options]] — major HRT business line
- [[reinforcement-learning-trading]] — relevant to HRT's research stack
- [[adverse-selection]] — primary risk HRT manages

## Sources

- Bloomberg: HRT 2025 trading revenue set for record $12.3B (Jan 2026): https://www.bloomberg.com/news/articles/2026-01-13/hudson-river-s-2025-trading-revenue-set-for-record-12-3-billion
- Business Insider: HRT $8B trading revenue in 2024: https://www.businessinsider.com/hudson-river-trading-hrt-8-billion-trading-revenue-2025-3
- HRT disclosures: https://www.hudsonrivertrading.com/disclosures/
- Verified via Perplexity (sonar), 2026-06-10

*No raw sources ingested yet. This page is otherwise based on public information about HRT's trading operations, regulatory filings and recruiting materials.*
