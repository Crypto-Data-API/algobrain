---
title: "Tariff Persistence → Long US Domestic Manufacturers, Short Global Supply Chain"
type: narrative
created: 2026-05-09
updated: 2026-05-09
status: proposed
side: long
tickers_primary: [NUE, MLM, VMC]
tickers_secondary: [CMC, EME, FIX, X, STLD, EXP]
tickers_hedge: [NKE, F, FXI, SPY]
time_horizon_days: 180
catalysts:
  - "Any new tariff round / executive order"
  - "USMCA / WTO ruling on reimposed Liberation Day duties"
  - "China Politburo / commerce ministry retaliation"
  - "US midterms (Nov 2026) — political incentive structure"
  - "Q2 2026 earnings — domestic-margin vs global-margin spread visible in prints"
sources:
  - "[[2025-04-02-liberation-day-tariffs]]"
  - "[[2026-02-20-supreme-court-tariff-ruling]]"
  - "[[2025-tariff-market-volatility]]"
  - "[[2026-market-regime-overview]]"
invalidation:
  - "Comprehensive US-China tariff deal announced (formal joint statement)"
  - "Supreme Court second ruling strikes down reimposed duties under alternative authority"
  - "USMCA-blanket exemption extended to all reshored manufacturing inputs"
  - "Dollar weakens >5% in 30 days — neutralizes the domestic-margin advantage"
  - "Long basket rallies > 25% before entry — already priced, chasing risk"
summary: "Tariffs on imported goods give US-only manufacturers (steel, cement, electrical services) a pricing edge, while companies importing from Asia or Europe (Nike, Ford, Chinese stocks) eat the cost. Long the domestic basket (NUE, MLM, EME, FIX), short the importers and FXI. The reshoring boom adds a multi-year tailwind for the long side."
risk_reward_target: "3:1"
created_by: "slash-command"
---

# Tariff Persistence → Long US Domestic Manufacturers, Short Global Supply Chain

## Headline

The Liberation Day tariffs (April 2025) were struck down by the Supreme Court ([[2026-02-20-supreme-court-tariff-ruling]]) on 20 February 2026 — and the administration **reimposed equivalent duties under alternative authority the next day**. The ruling-then-reimposition sequence telegraphs that tariff *uncertainty* is structural through the 2026 midterms and likely beyond. The trade is the natural tilt: long US domestic manufacturers and reshoring beneficiaries (NUE, MLM, VMC) capturing margin from input-cost shielding and pricing power; short globally-exposed names (NKE, F, FXI) eating the friction. Hedge with SPY puts to neutralize broad-market beta.

## Thesis

Tariff persistence creates a measurable margin spread between domestic and global cost structures:

1. **Domestic margin shield** — US-sourced steel, aggregates, cement, and electrical-services don't pay the duty. NUE / STLD have explicit pricing power as the marginal supplier when imported steel is duty-burdened. MLM / VMC / EXP get the same dynamic in aggregates / cement.
2. **Global margin compression** — companies with Asian / European supply chains (NKE shoes from Vietnam, F components from China, FXI consumer-staples) bear the duty cost, can pass through only partially, and lose share to domestic substitutes.
3. **Reshoring tailwind** — companies servicing the reshoring buildout (EME, FIX) have multi-year backlogs from data center + reshored manufacturing capex.
4. **Dollar dynamics** — tariffs strengthen the dollar (DXY) at the margin, which compounds the long basket's competitive advantage and amplifies the short basket's translation losses.

The pair structure isolates the spread from broad market beta. SPY put hedge sized to neutralize the residual beta in the long basket (NUE / MLM are cyclical; need market hedge in case the broader macro turns down for unrelated reasons).

## Why now

- **Two months post-ruling-and-reimposition** — markets initially treated the Supreme Court ruling as a win for global-supply-chain names; the next-day reimposition reversed that, but the read-through to single-name margin spreads has not yet been fully priced into Q2 prints.
- **Q2 2026 earnings cycle (June–August)** is the first cycle where the *reimposed* tariff structure shows up in domestic-vs-global margin attribution. Domestic names should print clean; global names should miss.
- **Midterms loom (Nov 2026)** — the political incentive structure favors the administration *intensifying* tariff messaging, not softening, into the election. Adds a tactical 6-month tailwind to the trade.
- **Dollar has not yet broken out** — DXY around its multi-month range. A breakout would amplify the trade further, but entering before the breakout captures both the tariff and FX leg.
- **180-day horizon** covers two earnings cycles + the midterm catalyst + at least one major USMCA / WTO procedural window.

## Expression

- **Long basket** (~50–60% of strategy capital):
  - **NUE** — primary US steel; long calls or call verticals 90–180 DTE
  - **MLM, VMC** — aggregates duopoly; long calls or share positions; lower-vol long
  - **CMC, STLD** — secondary steel/scrap; smaller positions
  - **EME, FIX** — reshoring/electrical services; multi-year tailwind
  - **EXP** — cement; smaller position
- **Short basket** (~40–50% of strategy capital):
  - **NKE** — bear put verticals 60–90 DTE; Asian supply chain + retail sales pressure
  - **F** — bear put verticals; Chinese components + EV margin compression
  - **FXI** — China large-cap ETF; bear put verticals; broad China exposure
  - Optionally **TGT** or other global-sourced retailers
- **Beta hedge**: SPY puts sized to neutralize +0.4 to +0.6 net beta from the long basket. The pair is *not* market neutral — it has a positive beta tilt because reshoring is a cyclical-with-tailwind story.

The bot's Stage 5 (structure) and Stage 6 (sizing) will confirm specific strikes against R:R ≥ 3:1.

## Risks

- **Tariff deal** — unlikely pre-midterms but possible. Cleanest invalidator. Monitor formal joint-statement language between US-China.
- **Recession dominates** — if the broader economy tips into recession, NUE / MLM are cyclical and get hit alongside the global names. SPY put hedge mitigates but doesn't fully insulate. Watch ISM Manufacturing, Architecture Billings Index.
- **Crowded trade** — domestic-manufacturer long is a known consensus theme. Watch IV-rank and managed-money positioning. Don't pay 80th-percentile vega.
- **Dollar reversal** — sustained DXY weakness would erode the margin advantage and amplify the short basket's translation gains, both wrong way. Hedge with smaller short DXY (UUP puts) if directional FX risk concerns.
- **Take-private wave / M&A** — single-name short positions exposed to take-private bids. Mitigation: basket structure, diversify within sub-buckets, cap single-name exposure at 5%.
- **Second-court-ruling** — another Supreme Court ruling striking down the alternative-authority duties is the binary tail that kills the structural premise.

## Signals generated

[Auto-populated by the bot. Append-only.]

## See also

- [[2026-02-20-supreme-court-tariff-ruling]] — the catalyst event
- [[2025-04-02-liberation-day-tariffs]] — the original tariff regime
- [[2025-tariff-market-volatility]] — historical pattern
- [[2026-market-regime-overview]] — the broader stagflation regime this sits in
- [[itpm-framework]] — top-down macro derivation (Stages 2-3, geographic + sector)
- [[stagflation-tail-hedge-long-vol-overlay]] — the overlay this narrative sits underneath
- [[bull-call-spread]], [[bear-put-spread]] — primary expression structures
- [[long-short-equity]] — portfolio archetype
