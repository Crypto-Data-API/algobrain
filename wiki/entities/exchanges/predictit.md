---
title: "PredictIt"
type: entity
created: 2026-05-03
updated: 2026-06-10
status: good
tags: [regulation, event-driven, exchange]
aliases: ["PredictIt", "PredictIt.org"]
entity_type: exchange
founded: 2014
headquarters: "Wellington, New Zealand"
website: "https://www.predictit.org"
related: ["[[polymarket]]", "[[kalshi]]", "[[prediction-markets]]", "[[cftc]]", "[[polymarket-vs-kalshi]]", "[[prediction-market-strategies]]"]
---

PredictIt is a real-money political [[prediction-markets|prediction market]] operated by Victoria University of Wellington (New Zealand) under a 2014 [[cftc|CFTC]] no-action letter granted for academic research purposes. Long the dominant US-legal venue for political event contracts, it operates under tight structural constraints — historically an $850 per-market position cap, raised to $3,500 after a July 2025 settlement with the CFTC — that create persistent, exploitable mispricings versus uncapped venues like [[polymarket]] and [[kalshi]].

## Overview

PredictIt was launched in 2014 as a research project of Victoria University of Wellington, with execution and platform operations handled in partnership with Aristotle International. The CFTC granted a no-action letter that permitted real-money trading of political event contracts on the explicit condition that the platform remain small, non-commercial, and tied to academic research. That research framing is the legal foundation for the entire venue: every constraint below flows from it.

Markets are binary "Yes/No" event contracts that settle at $1 or $0 on resolution. Pricing is in cents, representing implied probability. The platform's traditional focus has been US political events — presidential elections, primaries, control of Congress, cabinet appointments, and similar — though it has also listed economic and international politics markets.

## Key Constraints

These constraints define the trading environment and are the *direct cause* of the arbitrage opportunities discussed below.

**Original (2014–2025) terms:**

- **$850 per-market position cap** — no individual trader could have more than $850 at risk in any single contract. This was the binding constraint that prevented sophisticated capital from pricing markets efficiently.
- **5,000 traders per market cap** — once a market hit 5,000 unique participants, no new traders could enter (existing traders could still trade).
- **10% withdrawal fee** — applied on funds withdrawn from the platform (not on principal, but a meaningful drag on net returns).
- **5% fee on profits** — taken on net trading profit per market.
- **US-only** — verified US residency required.
- **No leverage, no margin, no shorting** — to short "Yes," you buy "No"; the two sides must sum to $1 minus fees.

**Updated terms after the July 2025 CFTC settlement (CFTC Letter No. 25-20, 14 July 2025):**

- **Position cap raised to $3,500 per contract** — the cap is now tied to the federal individual campaign contribution limit under the Federal Election Campaign Act (currently $3,500), which the FEC adjusts for inflation every two years.
- **5,000-trader-per-contract limit removed** entirely.
- The relief remains tied to political-event contracts and is non-transferable to a different operator.
- Fee structure (5% profit fee, 10% withdrawal fee) remained in place as of mid-2026.

Even at $3,500, the combined effect of the position cap and the fee structure is that traders who identify a clear mispricing cannot deploy enough capital to fully correct the price. This remains the core structural feature of PredictIt — and the reason it is a useful venue for studying retail [[behavioral-finance|behavioral biases]] in real-money markets, though the 4x larger cap has narrowed the most egregious gaps versus uncapped venues.

## Regulatory History

PredictIt operated quietly under its 2014 no-action letter for nearly eight years. Then:

- **August 2022** — The CFTC's Division of Market Oversight announced it was rescinding PredictIt's no-action letter, citing alleged violations of the original conditions. The order set a wind-down deadline of February 15, 2023, by which all markets were to be closed.
- **Late 2022** — Aristotle International, Clarke Capital Group, and several individual traders filed suit against the CFTC, arguing the rescission was arbitrary, capricious, and procedurally improper.
- **July 2023** — The 5th Circuit Court of Appeals issued a preliminary injunction blocking enforcement of the wind-down order, allowing PredictIt to continue operating while litigation proceeds.
- **2024–early 2025** — Litigation continued through remand and further filings. PredictIt remained operational throughout, but in a state of regulatory limbo with no clear long-term path.
- **14 July 2025** — The CFTC issued **Letter No. 25-20**, amended no-action relief that resolved the dispute on terms favourable to PredictIt: position limits raised from $850 to $3,500 (tied to the FECA individual campaign contribution limit), the 5,000-trader-per-contract cap removed, and continued operation of political-event contracts permitted.
- **21 July 2025** — The District Court granted PredictIt's proposed motion for judgment in favour of the plaintiffs, formally ending the litigation that began with the 2022 rescission.
- **Late 2025** — PredictIt rolled out a redesigned app and website (informally "PredictIt 2.0"). In December 2025 the CFTC granted additional no-action relief to PredictIt, Polymarket, and LedgerX regarding certain data-reporting requirements.

The 2025 settlement transformed PredictIt's posture: it now operates under current, affirmative CFTC no-action relief rather than a court injunction. Shutdown tail risk is far lower than in 2022–2024, though no-action relief remains weaker than full DCM registration (which [[kalshi]] holds).

## Trading Dynamics & Arbitrage with Polymarket

The position cap ($850 historically; $3,500 since July 2025) is the dominant feature of PredictIt's price formation. Because no single participant can deploy meaningful capital, prices are set largely by the aggregate behavior of small, unsophisticated retail traders. This produces several persistent biases:

- **Longshot bias** — low-probability outcomes (5–15c contracts) systematically overpriced, mirroring the favorite-longshot bias seen in racetrack betting.
- **Favorite underpricing** — high-probability outcomes (85–95c) often underpriced because the capped upside (~$0.10 per contract) makes it tedious to deploy $850 for a small absolute gain.
- **Slow news incorporation** — major news can take hours to fully reflect in price, where [[polymarket]] often re-prices in seconds.
- **Persistent gaps vs Polymarket** — on identical or near-identical contracts (US presidential winner, control of Senate, etc.) PredictIt and Polymarket prices can diverge by 5–10 percentage points for extended periods.

The classic [[prediction-market-strategies|cross-venue arbitrage]] trade: when PredictIt and Polymarket list equivalent contracts, take the cheap side on each venue. The trade is not riskless — fees, settlement timing differences, contract definition mismatches, and PredictIt's regulatory tail risk all matter — but the gross spread is often well above transaction costs. This is one of the cleanest examples of a structural [[arbitrage-opportunity-map|arbitrage]] in retail-accessible markets.

## Comparison Table

| Feature | PredictIt | [[polymarket]] | [[kalshi]] |
|---|---|---|---|
| Regulatory status | CFTC no-action letter (rescinded 2022; restored/amended July 2025 via Letter 25-20) | Offshore 2022–2024; re-entered US via acquisition of CFTC-licensed QCEX (2025) | CFTC-regulated DCM (designated contract market) |
| Position cap | $3,500 per contract (was $850 pre-July 2025) | None | None (subject to general DCM rules) |
| Trader cap | None (5,000/market cap removed July 2025) | None | None |
| Profit fee | 5% | None | None |
| Withdrawal fee | 10% | Network fees only | None |
| US legal access | Yes (under court injunction) | No (geo-blocked) | Yes |
| Settlement | USD via ACH | USDC on-chain | USD |
| Typical depth | Thin (cap-limited) | Deep on major events | Growing, deep on political events |
| Price efficiency | Lowest | Highest | High |

See [[polymarket-vs-kalshi]] for a deeper comparison of the two main competitors.

## Trading Relevance

Specific strategies that exploit PredictIt's structure:

1. **Cross-venue arbitrage (PredictIt vs Polymarket)** — match contracts across venues, take the cheap side of each. Constraint: the per-contract cap on PredictIt ($3,500 since July 2025, previously $850) limits total trade size; Polymarket leg can be much larger but creates net directional exposure. Hedge ratio matters.
2. **Longshot fade** — systematically short ($0.05–$0.15) longshot contracts when the implied probability is materially above any base-rate justification. Capacity is tiny but win rate is high.
3. **Favorite buy-and-hold** — buy ($0.90+) heavy favorites where the implied yield-to-resolution exceeds short-duration risk-free rates after fees. Boring but consistent.
4. **News latency capture** — first to react to political news that has already moved Polymarket. Window is short and shrinking.
5. **Resolution arbitrage** — exploit cases where PredictIt's contract definition resolves slightly differently than Polymarket's nominally equivalent contract (e.g. "next president sworn in" vs "winner of November election").

Position sizing is bounded by the per-contract cap ($3,500 since July 2025), so PredictIt is fundamentally a small-AUM venue. The edge is real but capacity-constrained — useful for individual traders, immaterial for any meaningful book size. The 2025 cap increase roughly quadrupled per-trade capacity but did not change the character of the venue.

## Decline / Current Status (June 2026)

Trading volume on PredictIt declined sharply after the August 2022 CFTC announcement, as traders rotated to [[polymarket]] (offshore, no US access but offered VPN routes) and especially to [[kalshi]] once Kalshi obtained CFTC approval to list political event contracts in late 2024. Kalshi and Polymarket now dominate US-relevant prediction market volume by orders of magnitude — a gap that widened further in 2025 as [[robinhood]] and other brokers routed retail flow into Kalshi-cleared event contracts.

The July 2025 CFTC settlement stabilised PredictIt's legal footing: it now operates under amended no-action relief (Letter 25-20) rather than a court injunction, with a $3,500 position cap, no trader cap, and a refreshed app/website launched late 2025. Markets continue to list, settle, and pay out. For traders, it remains a niche venue: useful for specific arbitrage and behavioral-edge plays against the deeper books at Polymarket and Kalshi, no longer a primary destination — but with materially lower shutdown tail risk than in 2022–2024.

## See Also

- [[polymarket]] — the offshore, uncapped competitor
- [[kalshi]] — the CFTC-regulated US competitor
- [[prediction-markets]] — concept overview
- [[polymarket-vs-kalshi]] — head-to-head comparison
- [[prediction-market-strategies]] — strategy catalog
- [[cftc]] — the regulator
- [[arbitrage-opportunity-map]] — broader arbitrage landscape
- [[behavioral-finance]] — biases that drive PredictIt's mispricings

## Sources

- CFTC Letter No. 25-20, amended no-action relief (14 July 2025) — https://www.cftc.gov/csl/25-20/download
- Prediction News, "Inside PredictIt's Settlement with the CFTC" — https://predictionnews.com/news/inside-predictit-settlement-with-the-cftc/
- Covers, "PredictIt, CFTC Reach Settlement in Longstanding Lawsuit" (July 2025) — https://www.covers.com/industry/predictit-and-cftc-reach-settlement-in-longstanding-lawsuit
- CoinDesk, "CFTC Gives No-Action Leeway to Polymarket, Gemini, PredictIt, LedgerX Over Data Rules" (11 Dec 2025) — https://www.coindesk.com/policy/2025/12/11/cftc-gives-no-action-leeway-to-polymarket-gemini-predictit-ledgerx-over-data-rules
- Prediction News, "PredictIt Releases App and Website Update" — https://predictionnews.com/news/predictit-releases-app-and-website-update/
- Verified via web search and Perplexity (sonar), 2026-06-10

Future ingestion targets: CFTC orders (Aug 2022 rescission, July 2025 amended relief), 5th Circuit ruling on the preliminary injunction, academic papers on PredictIt price efficiency vs Polymarket.
