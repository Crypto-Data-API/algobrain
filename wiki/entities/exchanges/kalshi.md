---
title: "Kalshi"
type: entity
created: 2026-04-14
updated: 2026-06-10
status: good
tags: [prediction-markets, regulation, event-driven, exchange]
aliases: ["Kalshi", "Kalshi Exchange", "KalshiEX"]
entity_type: exchange
founded: 2018
headquarters: "New York City, USA"
website: "https://kalshi.com"
related: ["[[polymarket]]", "[[prediction-markets]]", "[[polymarket-vs-kalshi]]", "[[cftc]]", "[[robinhood]]"]
---

# Kalshi

**Kalshi** is a CFTC-regulated [[prediction-markets|prediction market]] exchange headquartered in New York City, founded in 2018 by Tarek Mansour and Luana Lopes Lara and launched to the public in July 2021 after receiving CFTC Designated Contract Market (DCM) status in November 2020. Unlike [[polymarket|Polymarket]], Kalshi has operated as a federally regulated derivatives exchange since launch, accepting USD via traditional bank accounts rather than settling on-chain. As of May 2026 Kalshi carries a reported **$22 billion valuation** after a $1 billion Series F — up from ~$2 billion in mid-2025, one of the fastest private-market re-ratings on record.

## Overview

Kalshi allows users to trade on the outcomes of real-world events — politics, sports, economics (CPI, Fed decisions), weather, and finance. It differs from Polymarket in several structural ways:

- **Centralized architecture** — no blockchain settlement; accepts crypto deposits but settles in USD
- **CFTC-regulated since founding** — no consent decree or retroactive licensing required
- **Trading fees** — charges fees on transactions (higher than Polymarket's zero-fee model, attributed to compliance costs)
- **Historically US-focused** — sports, politics, finance categories; less global/geopolitical coverage than Polymarket
- **Centralized dispute resolution** — no oracle vulnerability; Kalshi resolves disputes internally

(Source: [[polymarket-wiki-guide]])

## Key Events 2024–2026

- **Oct 2024 — election markets legalized**: Kalshi won its landmark case against the [[cftc|CFTC]] (*KalshiEX LLC v. CFTC*), with the D.C. district court ruling the agency could not block its congressional-control contracts. The D.C. Circuit declined to stay the ruling, allowing Kalshi to list US election markets ahead of the November 2024 vote — the first legal US election betting in roughly a century.
- **Jan 2025 — sports contracts**: Kalshi self-certified sports event contracts (single-game outcomes), triggering cease-and-desist letters from state gaming regulators. Donald Trump Jr. joined as a strategic adviser the same month.
- **2025 — state-law battles**: Kalshi won preliminary injunctions against Nevada and New Jersey regulators on federal pre-emption grounds (CEA exclusive jurisdiction), while other states (e.g., Maryland, Arizona) continued to challenge; litigation remained unresolved as of mid-2026, with 20+ cases across multiple states.
- **Mar 2025 — Robinhood partnership**: [[robinhood|Robinhood]] launched its prediction-markets hub powered by Kalshi, distributing Kalshi contracts (Fed decisions, March Madness, later NFL and elections) to Robinhood's tens of millions of users. Webull and other brokers followed with similar integrations.
- **Funding trajectory**: ~$185M at ~$2B valuation (June 2025) → $300M at $5B (October 2025) → ~$1B at ~$11B led by Sequoia and CapitalG (December 2025) → **$1B Series F at $22B valuation (May 2026)**, reflecting surging institutional demand for event contracts.
- **Volume**: trading volume exploded through the 2024 election and the 2025 sports push; sports quickly became the dominant volume category, putting Kalshi in direct competitive tension with sportsbooks like DraftKings and FanDuel (the latter partnering with CME on rival event contracts).

## Competitive Position

Kalshi focuses on **regulatory distribution channels and traditional brand exposure** (brokerage integrations, US licensing), while Polymarket focuses on **decentralized infrastructure and ecosystem**. Both face simultaneous legal challenges from state gaming regulators attempting to classify prediction markets as gambling (20+ lawsuits across multiple US states as of 2026). (Source: [[polymarket-wiki-guide]])

| Dimension | Kalshi | Polymarket |
|-----------|--------|------------|
| **Valuation** | ~$2B (mid-2025) → $22B (May 2026) | ~$9B (ICE investment, Oct 2025) |
| **Regulation** | CFTC-regulated DCM since 2020 | CFTC-compliant via QCEX acquisition (2025) |
| **Settlement** | USD (bank accounts) | USDC (on-chain) |
| **Fees** | Yes | 0% |
| **Scope** | Primarily US | Global |
| **Architecture** | Centralized | Decentralized (Polygon) |
| **Big backer** | Sequoia, CapitalG, Paradigm | ICE ($2B) |

See [[polymarket-vs-kalshi]] for a detailed comparison.

## Regulatory Context

The [[cftc|CFTC]] has filed amicus briefs supporting the classification of prediction markets (including Kalshi) as federally regulated derivatives exchanges rather than gambling entities, and under the 2025 administration shifted to a notably permissive posture (dropping its appeal of the election-markets ruling in May 2025). The central open legal question in 2026 is whether federal CEA jurisdiction pre-empts state gambling law for sports event contracts. (Source: [[polymarket-wiki-guide]]; court rulings cited below)

## Why It Matters to Traders

- **Tradable event probabilities**: CPI, FOMC, GDP, government-shutdown and election contracts give a direct, real-money-implied probability for macro catalysts — usable as both a hedging instrument and a sentiment input alongside options-implied moves.
- **Cross-venue arbitrage**: persistent small price gaps vs Polymarket and sportsbook lines create arbitrage and relative-value opportunities (see [[prediction-market-strategies]]).
- **Regulated US access**: the only way for a US retail trader to take positions on elections/events inside a brokerage stack (via Robinhood/Webull) without offshore or crypto rails.

## AI Integration

Kalshi markets are accessible to AI agents on Solana through Jupiter's prediction market infrastructure via `sol predict` commands, alongside Polymarket. See [[ai-prediction-markets]] for details. (Source: [[polymarket-wiki-guide]])

## See Also

- [[polymarket]] — Main competitor (decentralized)
- [[polymarket-vs-kalshi]] — Head-to-head comparison
- [[prediction-markets]] — The broader concept
- [[prediction-market-strategies]] — Strategies applicable to both platforms
- [[cftc]] — primary regulator

## Sources

- [[polymarket-wiki-guide]] — Primary wiki source (structure, fee model, AI integration)
- Kalshi announcement, "$1 billion raise at $22 billion valuation" (May 2026): https://news.kalshi.com/p/kalshi-raises-1-billion-22-billion-valuation-institutional-demand-surges
- Blockhead, "Kalshi hits $22B valuation with $1B raise" (8 May 2026): https://www.blockhead.co/2026/05/08/institutional-money-floods-prediction-markets-kalshi-hits-22b-valuation-with-1b-raise/
- *KalshiEX LLC v. CFTC*, D.D.C. (Sept 2024) — election-contract ruling
- Verified via Perplexity (sonar), 2026-06-10.
