---
title: "Manifold Markets"
type: entity
created: 2026-05-03
updated: 2026-06-10
status: good
tags: [behavioral-finance, event-driven, company]
aliases: ["Manifold", "Manifold Markets"]
entity_type: company
founded: 2022
headquarters: "San Francisco, USA"
website: "https://manifold.markets"
related: ["[[polymarket]]", "[[kalshi]]", "[[prediction-markets]]", "[[behavioral-finance]]", "[[prediction-market-strategies]]"]
---

Manifold Markets is a play-money prediction market platform where any user can create a market on any question. Because participation costs nothing in real currency, Manifold has the lowest entry friction of any major forecasting venue, which makes it useful as a sentiment leading indicator and as a sandbox for testing [[prediction-market-strategies]] before deploying real capital on [[polymarket]] or [[kalshi]].

## Overview

Manifold was founded in 2022 by Austin Chen and brothers James and Stephen Grugett, and went through Y Combinator's Winter 2022 batch. The platform operates with a stated mission centered on calibration research, forecasting infrastructure, and broad public access to probabilistic thinking — closer in spirit to a research nonprofit than a typical exchange, though it is incorporated as a company.

The currency is "mana" (denoted M$), a play-money token that users earn through correct forecasting, daily login bonuses, market creation, and (historically) one-way conversion from charitable donations. Mana cannot be purchased with cash for direct trading use, which legally distinguishes Manifold from real-money venues like [[polymarket]] and CFTC-regulated [[kalshi]].

## How It Works

**Mana economy.** Users start with a fixed mana grant and earn more by trading profitably or creating popular markets. Mana has no direct cash value but has historically had charitable utility — until 2024, mana could be donated to a curated list of charities at a 1:100 mana-to-cents conversion rate (M$100 = $1 of charitable donation). In 2024 Manifold significantly reduced this conversion rate and changed the mana economics to address inflationary pressures from accumulated balances. The donation pathway remains the closest thing to mana having external value.

**User-created markets.** Anyone can spend mana to create a market on any question — political outcomes, AI capability milestones, sports, personal predictions, conditional questions ("If X happens, will Y?"). The creator sets the resolution criteria and is responsible for resolving the market. This permissionless creation is Manifold's defining structural feature and has no equivalent on Polymarket or Kalshi.

**Liquidity.** Markets use an automated market maker (a variant of [[lmsr]] — the Logarithmic Market Scoring Rule) so trades are always possible without a counterparty. Users can act as liquidity providers by subsidizing markets, earning fees in exchange for absorbing some of the AMM's risk. See [[market-making]] for the broader mechanism family.

## The Sweepstakes Pivot and Reversal (2024–2025)

In 2024 Manifold attempted a real-money pivot. On September 25, 2024 it launched **Manifold Sweepstakes**: parallel markets denominated in "sweepcash", a sweepstakes currency redeemable at 1.00 sweepcash = 1.00 USD (minus a 5% redemption fee), modeled on the sweepstakes-casino legal structure used by apps like Fliff. Sweepstakes markets were limited to US residents 18+ (excluding DC, Delaware, Idaho, Michigan, and Washington), used a curated set of unambiguous questions, and ran alongside the free mana market on each question. The pivot accompanied a roughly 10:1 devaluation of mana and the reduction of the charitable donation program.

The experiment was short-lived: **Manifold sunset sweepstakes trading on March 28, 2025**, returning to a pure play-money model. The episode is a useful data point on the regulatory and economic difficulty of converting a play-money community into a real-money venue — the same period in which [[kalshi]] and [[polymarket]] were scaling real-money event trading aggressively. As of mid-2026 Manifold continues to operate as the largest permissionless play-money prediction market.

## Key Features

- **LMSR-style market maker** — guarantees liquidity even on thinly traded niche markets
- **Multi-outcome markets** — beyond binary YES/NO, including numeric range markets and free-response markets where users add new answer options
- **Conditional markets** — "P(A | B)" structures where resolution depends on a second event
- **User creation and resolution** — fully permissionless, with reputation and dispute mechanisms layered on top
- **Public API** — programmatic market creation and trading is supported, enabling bots and research tools
- **Calibration dashboards** — site-wide stats on how well market prices have matched eventual outcomes

## Calibration and Forecasting Quality

Despite using play-money, Manifold publishes calibration plots showing that aggregate market prices track realized outcome frequencies reasonably well — markets that close at 70% resolve YES roughly 70% of the time. Independent comparisons (including with [[metaculus]], a curated play-money platform with a different scoring system) suggest Manifold's headline markets are roughly competitive in accuracy with curated forecasting platforms, even without monetary stakes.

The reason calibration holds without real money is that mana itself is a scarce reputational currency: leaderboards, profile statistics, and the social capital of being a top forecaster create real incentives to predict accurately. This is a useful data point for [[behavioral-finance]] — it suggests financial stakes are sufficient but not strictly necessary for crowd accuracy.

## Trading-Adjacent Uses

Even traders who never deploy capital on Manifold can use it as an information source:

1. **Leading indicator for real-money markets.** Manifold often lists speculative or early-stage questions weeks before [[polymarket]] or [[kalshi]] adds them. Watching where Manifold prices diverge from public consensus can flag opportunities to position early on real-money venues once those markets open.
2. **Strategy sandbox.** Test [[prediction-market-strategies]] — fade-the-frontrunner, late-resolution arbitrage, news-driven momentum — risk-free before risking real capital. Mana P&L is a noisy but cheap proxy for real-money skill.
3. **Sentiment aggregation.** The forecasting community on Manifold overlaps with rationalist, AI-safety, and quant-curious crowds, which means certain technology and policy markets price information that mainstream platforms miss.
4. **Question discovery.** Browsing Manifold's user-created markets surfaces under-explored questions; if a Manifold market shows a surprising probability, that thesis can sometimes be expressed via correlated trades in real markets (equities, crypto, options).
5. **Cross-venue arbitrage signal.** Persistent price gaps between Manifold and Polymarket on equivalent markets indicate either an information edge on one side or a structural cost (Polymarket withdrawal frictions, mana hoarding) — both are tradeable.

## Comparison to Polymarket, Kalshi, and Metaculus

| Feature | Manifold | [[polymarket]] | [[kalshi]] | [[metaculus]] |
|---------|----------|----------------|------------|---------------|
| Currency | Play-money (mana) | Real (USDC) | Real (USD) | Play-money (points) |
| Regulator | None (play-money) | Offshore / unregulated in US | CFTC-regulated | None |
| Market creation | Any user | Curated by team | Curated, CFTC-approved | Curated by community + admins |
| Mechanism | LMSR-style AMM | CLOB | CLOB | Aggregated forecasts (no trading) |
| Liquidity | Always available (AMM) | Depends on book | Depends on book | N/A |
| Best for | Idea discovery, sentiment | Real P&L on macro events | Regulated US event contracts | Long-horizon expert forecasts |

## Notable Markets and Events

- **AI capability and timeline markets** — Manifold has hosted hundreds of markets on AI milestones, model releases, and benchmark scores, often pricing in information weeks before mainstream coverage
- **Election forecasting** — markets covered the 2024 US election cycle in parallel with Polymarket and Kalshi, providing a play-money comparison benchmark
- **Crypto price markets** — milestone markets ("BTC above $X by date Y") that mirror real-money venues
- **Internal Manifold markets** — meta-markets on platform changes, mana economy updates, and feature launches

## Limitations

- **Different incentive structure** — without real money, edge cases (small-stakes manipulation, low-effort resolution disputes) appear that don't exist on Polymarket
- **Thin liquidity on niche markets** — the AMM guarantees a price exists, but moving M$1,000 on an obscure market can shift it dramatically
- **Whale distortion** — mana hoarders accumulated from years of activity can move markets without strong conviction, especially low-traffic ones
- **Resolution risk** — user-created markets depend on the creator (or moderator process) for fair resolution; ambiguous criteria sometimes cause disputed outcomes
- **No direct cash payout** — the 2024 charity-rate change reduced even the indirect monetary value of mana, weakening incentives somewhat
- **Selection bias in users** — the user base skews toward rationalist, tech, and AI-interested crowds, which can produce biased pricing on cultural or political questions outside that worldview

## See Also

- [[prediction-markets]] — the broader category and theory
- [[polymarket]] — primary real-money competitor
- [[kalshi]] — CFTC-regulated US alternative
- [[metaculus]] — curated play-money forecasting platform
- [[prediction-market-strategies]] — strategies that apply across venues
- [[behavioral-finance]] — why play-money calibration works
- [[lmsr]] — the market maker mechanism
- [[market-making]] — general market-making concepts

## Sources

- Manifold, "Cash prizes are here!" (Sep 25, 2024) — https://news.manifold.markets/p/cash-prizes-are-here
- Manifold Sweepstakes FAQ (eligibility, 5% redemption fee) — https://docs.manifold.markets/sweepstakes
- Wikipedia, "Manifold (prediction market)" — sweepstakes launched Sep 2024, sunset Mar 28, 2025 — https://en.wikipedia.org/wiki/Manifold_(prediction_market)
- Prediction News, "Manifold Markets Raises the Stakes with Cash Rewards" (2024) — https://predictionnews.com/manifold/manifold-markets-raises-the-stakes-with-cash-rewards/
- Manifold calibration stats — https://manifold.markets/calibration
- Verified via web search, 2026-06-10
