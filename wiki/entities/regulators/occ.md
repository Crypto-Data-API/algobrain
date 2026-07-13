---
title: "OCC (Options Clearing Corporation)"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [options, derivatives, regulation, market-microstructure]
aliases: ["Options Clearing Corporation", "The Options Clearing Corp"]
entity_type: company
founded: 1973
headquarters: "Chicago, IL and Dallas, TX, USA"
website: "https://www.theocc.com"
related: ["[[options-disclosure-document]]", "[[sec]]", "[[cftc]]", "[[finra]]", "[[cboe]]", "[[cboe-global-markets]]", "[[memx]]", "[[nyse]]", "[[nasdaq]]", "[[assignment-and-exercise]]", "[[flex-options]]", "[[counterparty-risk]]", "[[equity-options]]"]
---

# OCC (Options Clearing Corporation)

The Options Clearing Corporation (OCC) is the world's largest equity derivatives clearing organization and the sole central counterparty (CCP) for all standardized listed options on US securities exchanges. Founded in 1973 alongside the launch of the [[cboe|Chicago Board Options Exchange]], the OCC issues, guarantees, clears, and settles every listed [[equity-options|equity option]] contract traded in the United States, eliminating bilateral [[counterparty-risk]] for option buyers and writers.

## Overview

The OCC sits between every option buyer and seller through a process called **novation** — once a trade is executed on an exchange, the OCC becomes the buyer to every seller and the seller to every buyer. This means the credit risk of an option contract is the credit risk of the OCC, not of the original counterparty. Because the OCC guarantees performance, market participants can write options to anonymous counterparties without performing credit due diligence.

The OCC is owned by its participant exchanges — including [[cboe-global-markets|Cboe]], [[nyse|NYSE]] (NYSE Arca and NYSE American Options), [[nasdaq|Nasdaq]] (Nasdaq PHLX, Nasdaq ISE, Nasdaq BX, Nasdaq GEMX, Nasdaq MRX), MIAX (MIAX Options, MIAX Pearl, MIAX Emerald, MIAX Sapphire), [[memx|MEMX Options]], and BOX Options Exchange — and is jointly regulated by the [[sec|SEC]] (for securities options) and the [[cftc|CFTC]] (for futures options it clears).

In 2012, the Financial Stability Oversight Council (FSOC) designated the OCC as a **Systemically Important Financial Market Utility (SIFMU)** under Title VIII of the Dodd-Frank Act, recognizing that a failure of the OCC could threaten US financial stability. SIFMU designation imposes heightened risk-management, capital, and supervisory requirements.

## What OCC Does

| Function | Description |
|---------|-------------|
| **Issuance** | When two parties agree to an option trade on an exchange, the OCC issues the contract. The OCC is the legal issuer of every listed US equity option. |
| **Novation** | The OCC becomes counterparty to both sides via novation, replacing the original bilateral relationship. |
| **Clearing** | Matches and confirms trade details from member exchanges within the same trading day. |
| **Settlement** | Handles cash settlement of premiums (T+1) and physical settlement of underlying shares on exercise/assignment. |
| **Margining** | Calculates and collects margin from clearing members daily (and intraday during stress) using the STANS (System for Theoretical Analysis and Numerical Simulations) risk model. |
| **Exercise and Assignment** | Processes [[assignment-and-exercise|exercise notices]] from long holders and randomly assigns short holders within a clearing member's account pool. |
| **Default Management** | Maintains a default fund (Clearing Fund) and liquidity facilities to mutualize losses if a clearing member fails. |

## Member Exchanges

As of 2025, the OCC clears options for the following US options exchanges (in alphabetical order):

- **BOX Options Exchange**
- **Cboe Options Exchange (C1)** — see [[cboe]]
- **Cboe BZX Options**
- **Cboe C2 Options**
- **Cboe EDGX Options**
- **MEMX Options** — see [[memx]] (added June 2024)
- **MIAX Options Exchange**
- **MIAX Pearl Options**
- **MIAX Emerald Options**
- **MIAX Sapphire Options**
- **Nasdaq BX Options**
- **Nasdaq GEMX**
- **Nasdaq ISE**
- **Nasdaq MRX**
- **Nasdaq PHLX**
- **NYSE American Options** — see [[nyse]]
- **NYSE Arca Options**

The OCC also clears futures options for selected derivatives exchanges.

## Regulatory Status

The OCC is regulated as:

- A **registered clearing agency** under Section 17A of the Securities Exchange Act of 1934 (SEC oversight)
- A **derivatives clearing organization (DCO)** for futures options (CFTC oversight)
- A **Systemically Important Financial Market Utility (SIFMU)** designated by FSOC in 2012 (Federal Reserve oversight added)

This triple regulatory regime makes the OCC one of the most heavily supervised entities in US capital markets. The Federal Reserve Bank of Chicago participates in OCC supervision under SIFMU rules.

## Key Publications

| Publication | Purpose |
|-------------|---------|
| **[[options-disclosure-document|Options Disclosure Document (ODD)]]** | "Characteristics and Risks of Standardized Options" — the prospectus-equivalent disclosure that brokers MUST deliver to every retail customer before approving them to trade options. Updated periodically; most recent material updates June 2024. |
| **Daily Volume and Open Interest Statistics** | Industry-standard volume figures published every trading day, broken down by exchange, product type (equity/index/ETF), and put/call. |
| **OCC Annual Report** | Financial statements, risk disclosures, and operational summaries for clearing members and the public. |
| **Information Memos and Bylaws** | Rule changes, contract specification updates, corporate action adjustments. |
| **Special Memos for Corporate Actions** | Adjustments to option terms following splits, mergers, special dividends, and spin-offs. |

The OCC cleared more than **12 billion contracts in 2024**, then a record annual volume — and 2025 broke it again with total cleared volume on the order of **13.8+ billion contracts**, a sixth consecutive annual record. 2025 also produced the two largest single days in options history: roughly **102 million contracts on April 4, 2025** (the tariff-shock selloff) and about **110 million contracts on October 10, 2025**. Market-wide average daily volume ran near **59 million contracts** through the first three quarters of 2025, up over 20% from 2024.

## Why It Matters for Traders

1. **Counterparty risk eliminated** — When you buy a call from an anonymous market maker on [[cboe]] and hold it to expiration, you are relying on the OCC (not the market maker) to deliver shares on exercise. This is the foundational reason listed options are tradable at all.
2. **Standardized contracts** — The OCC enforces uniform contract terms (100-share multiplier, standard strikes, standard expirations) so that any option of the same series is fungible across all exchanges. This enables a deep secondary market.
3. **Automatic exercise** — The OCC's "exercise-by-exception" rule automatically exercises any equity option that is $0.01 or more in-the-money at expiration unless the holder explicitly instructs otherwise. Traders must understand this to avoid surprise assignments.
4. **Random assignment** — When you write (sell) an option, the OCC assigns exercise notices randomly within the broker's pool of short positions. You cannot predict when assignment will occur.
5. **Margin via STANS** — The OCC's risk model determines the minimum margin clearing members must hold against client positions, which flows through to retail margin requirements at brokers.

## Recent Initiatives

- **T+1 Settlement (May 2024)** — The OCC supported the industry-wide transition from T+2 to T+1 settlement for options on equities, aligning option exercise settlement with the underlying stock settlement cycle (set by SEC Rule 15c6-1).
- **[[flex-options|FLEX Options]] Expansion** — The OCC has expanded FLEX options (customizable strike, expiration, exercise style) to broader product sets, enabling institutional users to create non-standard contracts that still benefit from CCP clearing.
- **MEMX Options Onboarding (June 2024)** — Added [[memx|MEMX Options]] as a cleared exchange, reflected in the June 2024 [[options-disclosure-document|ODD]] update.
- **Risk Model Modernization** — Multi-year project to replace STANS with a next-generation margin model.
- **Stress Testing and Default Fund Sizing** — Quarterly stress tests against extreme but plausible market scenarios; the OCC has multiple times publicly increased its Clearing Fund size in response to volatility events.
- **Record Volume Handling (2025)** — The OCC processed back-to-back record volume days in 2025 (April 4 and October 10) without operational incident, a real-world stress test of CCP infrastructure during the retail-driven [[0dte|0DTE]] and tariff-volatility era.

## Related

- [[options-disclosure-document]] — The ODD is the OCC's flagship retail disclosure
- [[sec]] — Primary federal regulator
- [[cftc]] — Co-regulator for futures options
- [[finra]] — Sets broker-dealer rules including options approval levels
- [[cboe]] — Largest options exchange, founding shareholder of the OCC
- [[memx]] — Newest OCC member exchange (options market launched 2023)
- [[assignment-and-exercise]] — Mechanics governed by OCC rules
- [[flex-options]] — OCC-cleared customizable contracts
- [[counterparty-risk]] — OCC novation eliminates this for listed options
- [[equity-options]] — OCC clears all US-listed equity options

## Sources

- OCC official site: https://www.theocc.com
- OCC, "Annual 2025 and December 2025 Volume" (Jan 5, 2026): https://www.theocc.com/newsroom/views/2026/01-05-occ-annual-2025-and-december-2025-volume
- OCC Historical Volume Statistics: https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics
- OCC 2025 Annual Report: https://annualreport.theocc.com/
- Cboe Insights, "The State of the Options Industry: Quarter Three 2025": https://www.cboe.com/insights/posts/the-state-of-the-options-industry-quarter-three-2025/
- FSOC SIFMU designation order (2012); SEC filings
- 2025 volume figures verified via web search, 2026-06-10
