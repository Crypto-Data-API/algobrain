---
title: "Jane Street"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [market-maker, quantitative, options, etf, company]
entity_type: company
aliases: ["Jane Street Capital", "Jane Street Group"]
founded: 2000
headquarters: "New York, USA"
website: "https://www.janestreet.com"
related: ["[[market-maker]]", "[[etf]]", "[[options]]", "[[bid-ask-spread]]", "[[citadel-securities]]", "[[jump-trading]]", "[[quantitative-trading]]", "[[arbitrage]]"]
---

Jane Street is a quantitative trading firm and one of the world's largest [[etf|ETF]] and [[options]] market makers. The firm trades over $17 billion notional daily across equities, bonds, options, ETFs, and currencies, handling a significant portion of global ETF trading volume. Jane Street operates as a proprietary trading firm, risking only its own capital.

## Overview

Founded in 2000 in New York City, Jane Street began as an options market maker on the American Stock Exchange and grew into one of the most profitable trading firms globally. Unlike [[citadel-securities|Citadel Securities]], Jane Street does not handle retail order flow via [[payment-for-order-flow]]; instead, it provides liquidity directly on exchanges and through institutional channels.

The firm is known for its distinctive culture: extensive use of the OCaml programming language, puzzle-based recruiting, and a collaborative rather than hierarchical trading floor. Jane Street reportedly generated over $10 billion in net trading revenue in 2022, driven by [[volatility]] in bond and equity markets.

## Financial Performance (2023-2026)

Jane Street's disclosed results (via bond-investor documents reported by Bloomberg) show explosive growth:

| Year | Net trading revenue | Notes |
|---|---|---|
| 2023 | $10.6B | |
| 2024 | $20.5B | ~$13B net income — exceeded Citigroup and Bank of America's trading desks |
| 2025 | **$39.6B (record)** | Topped JPMorgan's trading revenue by ~11%; adjusted EBITDA ~$31.2B; compensation ~$9.38B; ~3,500 employees (>$11M revenue per employee); Q4 2025 alone was $15.5B |
| Q1 2026 | $16.1B (record quarter) | Reported May 2026 |

Because Jane Street funds part of its trading capital with high-yield bonds, it publishes financials to bondholders — making it unusually transparent for a private prop firm. Its multi-billion-dollar note issuances have grown alongside its balance sheet.

## India / SEBI Case (2025-2026)

A defining regulatory event for the prop-trading industry:

- **3 July 2025:** SEBI issued an interim order banning Jane Street and four affiliates from Indian securities markets, alleging manipulation of Bank Nifty index/options expiries (marking the index with cash/futures trades while holding much larger options positions). SEBI estimated ~₹4,843 crore (~$550-565M) of unlawful gains on the examined days, out of roughly $4B+ Jane Street earned in India overall.
- **14 July 2025:** Jane Street deposited the full ₹4,843.57 crore into escrow while reserving its right to appeal.
- **21 July 2025:** SEBI lifted the trading ban conditional on compliance.
- **2026:** The case remains before the Securities Appellate Tribunal (hearing adjourned February 2026). The episode triggered broader SEBI scrutiny of index-expiry trading and contributed to reforms in India's options market — relevant to anyone trading Indian index derivatives, where prop-firm flow had dominated expiry-day volumes.

## How Traders Get Exposure

Jane Street is private and employee-owned; there is no equity ticker. Indirect exposure/observation channels: its high-yield bonds (rated, publicly traded), and its visible footprint in ETF creation/redemption baskets, options market quality, and crypto liquidity (Jane Street was an early authorized participant for spot Bitcoin ETFs).

## Trading Activities

### ETF Market Making

Jane Street is the dominant authorized participant and market maker in the global ETF ecosystem. Their market making keeps ETF prices closely tracking their net asset value (NAV), and their [[arbitrage]] activity between ETFs and underlying baskets provides the mechanism that makes ETFs function. This is particularly important in:

- **Bond ETFs** (e.g., LQD, HYG) — where underlying bonds trade infrequently but the ETF trades continuously
- **International ETFs** — where underlying markets may be closed during US trading hours
- **Leveraged and inverse ETFs** — which require complex daily rebalancing

### Options Market Making

Jane Street provides liquidity on equity and index options across multiple exchanges. Their quoting affects [[bid-ask-spread|bid-ask spreads]] that retail and institutional options traders encounter. Understanding that a small number of firms (Jane Street, [[citadel-securities|Citadel]], Susquehanna, Wolverine) dominate options market making helps traders understand why spreads widen during high-volatility events: these firms pull quotes to manage inventory risk.

### Quantitative Strategies

Beyond pure market making, Jane Street engages in [[quantitative-trading|quantitative]] strategies including statistical [[arbitrage]], relative value, and cross-asset strategies. Their technology infrastructure is designed for speed and reliability, though they are not primarily a latency-focused [[high-frequency-trading|HFT]] firm like [[jump-trading]].

## Trading Relevance

For active traders, Jane Street's activities matter in several ways:

- **ETF spread behavior**: When Jane Street and other major authorized participants tighten or widen their ETF quotes, it directly affects execution costs for any ETF-based strategy
- **Options liquidity**: Jane Street's options market making determines available liquidity and spreads, particularly for less liquid names
- **End-of-day flows**: ETF rebalancing and creation/redemption activity concentrated at market close creates predictable [[order-flow]] patterns that other traders can observe

## Related

- [[market-maker]] — Jane Street's primary role in market structure
- [[etf]] — the asset class where Jane Street has the largest footprint
- [[arbitrage]] — ETF arbitrage is a core Jane Street activity
- [[options]] — Jane Street's options market making business
- [[bid-ask-spread]] — directly affected by Jane Street's quoting
- [[citadel-securities]] — peer market-making firm
- [[jump-trading]] — peer proprietary trading firm
- [[quantitative-trading]] — Jane Street's analytical approach

## Sources

- [Jane Street's $20.5 billion trading haul tops Citigroup, BofA](https://www.bloomberg.com/news/articles/2025-04-23/jane-street-s-20-5-billion-trading-haul-tops-citigroup-bofa) — Bloomberg, Apr 2025
- [Jane Street snatches Wall Street crown with record $39.6 billion trading haul](https://www.bloomberg.com/news/articles/2026-04-24/jane-street-snatches-wall-street-crown-with-record-39-6-billion-trading-haul) — Bloomberg, Apr 2026
- [Jane Street notches record quarter with $16.1 billion of trading revenue](https://www.bloomberg.com/news/articles/2026-05-08/jane-street-pulls-in-record-16-1-billion-quarterly-trading-haul) — Bloomberg, May 2026
- [Jane Street and the expiry day trap: SEBI's crackdown](https://blogs.law.ox.ac.uk/oblb/blog-post/2025/07/jane-street-and-expiry-day-trap-unpacking-sebis-crackdown-algorithmic) — Oxford Law Blogs, Jul 2025
- [Jane Street vs SEBI: SAT adjourns hearing](https://www.businesstoday.in/markets/story/jane-street-vs-sebi-sat-adjourns-hearing-in-market-manipulation-case-517925-2026-02-25) — Business Today, Feb 2026
- Verified via Perplexity (sonar) and web research, 2026-06-10
