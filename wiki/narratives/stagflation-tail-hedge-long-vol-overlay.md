---
title: "Stagflation Tail Hedge → Long-Vol Overlay (SPX Puts + VIX Calls)"
type: narrative
created: 2026-05-09
updated: 2026-05-09
status: proposed
side: long
tickers_primary: [SPY, VIX]
tickers_secondary: [QQQ, IWM, UVXY]
tickers_hedge: []
time_horizon_days: 180
catalysts:
  - "Iran conflict escalation (Hormuz incident; oil → $150+)"
  - "BLS print confirming further labor weakness"
  - "AI cohort re-rating (any Mag 7 capex cut → cohort -10%+)"
  - "Tariff renegotiation breakdown / new tariff round"
  - "Fed forced pivot in either direction (cut or hike)"
sources:
  - "[[itpm-framework]]"
  - "[[long-vol-overlay]]"
  - "[[long-vol-vs-short-vol]]"
  - "[[2026-market-regime-overview]]"
  - "[[2026-02-citrini-tech-selloff]]"
  - "[[ai-layoff-trap]]"
  - "[[geopolitical-risk-premium]]"
invalidation:
  - "VIX averages > 25 for 30+ consecutive sessions (overlay too expensive; resize, don't kill)"
  - "Realized regime resolves favorably across all three axes (oil < $80, tariff deal, Fed cuts) — overlay can be reduced but not eliminated"
  - "Portfolio's other narratives all close out → overlay must be sized down proportionally with the book"
summary: "The VIX is sitting around 18-22 even though the macro and geopolitical backdrop (Iran, tariffs, weak jobs data) is the worst in years. That makes long-volatility hedges (SPY puts, VIX calls) unusually cheap right now. This isn't a return-seeking trade — it's insurance that pays off if any of the other narratives blow up the book."
risk_reward_target: "5:1"
created_by: "slash-command"
---

# Stagflation Tail Hedge → Long-Vol Overlay (SPX Puts + VIX Calls)

## Headline

The [[2026-market-regime-overview|early-April 2026 regime overview]] documents stagflationary conditions across three converging axes: Iran-driven oil at $100–120, tariff uncertainty post-Supreme Court ruling, and Fed at 0 cuts for 2026. Historically these regimes resolve via tail events (1973, 1979, 2008, 2022), not glide paths. This narrative is **the canonical [[itpm-framework|ITPM]] long-vol overlay**: a continuously-laddered SPX put structure plus VIX call spreads sized at ~1.5% of NAV per year, designed to leave the book inside acceptable drawdown limits during a 30%+ equity drawdown. It is **not a directional bet** — it is the defensive overlay every other narrative in the book sits underneath.

## Thesis

Per [[itpm-framework]] §"non-negotiable synthesis": *"any book that has ever earned theta should also have spent on a long-vol overlay."* The synthesis is non-negotiable; running directional or premium-selling positions without it produces unbounded tail risk. Three reasons the overlay is mispriced *right now*:

1. **VIX is range-bound at 17–22 despite the regime** — markets habituate to persistent threats ([[geopolitical-risk-premium]] §"crying wolf effect"), so realized geopolitical/macro risk is not in implied vol. The cost of the overlay is below historical fair value for the regime.
2. **Tail-skew has compressed** — 5-delta SPX puts trade at lower vol than 25-delta puts on a dispersion-adjusted basis. The wing is cheap relative to the body.
3. **Cross-asset confirmation** — bond vol (MOVE), oil vol (OVX), and FX vol (CVIX) are all elevated relative to equity vol. Equity vol is the under-priced leg of the cross-asset complex.

The overlay's payoff is not "VIX up = profit." It is **survival of the book during the 5–10% of sessions that account for 80%+ of tail-event drawdowns**. Sized correctly, the overlay's bleed is the cheapest insurance available.

## Why now

- **Existing narratives have built the long side** — `crm-workforce-cut-ai-margin` (long), `ai-layoff-trap-capex-beneficiaries` (long), `iran-war-persistence-energy-defense-long` (long). Without an overlay, the book is structurally unhedged against a regime-break event.
- **Vol is cheap relative to the regime** — VIX 18–20 in a stagflation regime is anomalous. The 2022 inflation regime traded VIX 25–35 baseline.
- **180-day horizon** matches the typical ITPM overlay rebalance cadence — quarterly review, monthly add-ons, no panic resizing.
- **Two major catalyst windows fall inside the horizon**: Iran/oil resolution timing and Q3 2026 earnings + tariff midterm-politics window.

## Expression

Continuous laddered structure — not a single trade but a maintained overlay:

- **SPX put ladder**: 6-month rolling structure. Each month, buy ~$300/month notional of SPY 3-6m 10–15-delta puts. Roll 60 DTE; never let any leg expire untouched.
- **VIX call vertical**: 60-90 DTE long VIX 25/35 call spreads, ~$200/month notional. Captures the explosive convexity (VIX spot → 30+ episodes in tail events).
- **Optional augmentation** during regime stress: if VIX < 17 (cheap), double the next month's add. If VIX > 25, skip a month (don't pay 80th-percentile vega).
- **Annual NAV target**: ~1.5% of NAV/year spend (per [[itpm-framework]] worked example).
- **Sizing rule**: overlay must cover ~30% drawdown across the rest of the book. As other narratives' positions grow, overlay scales proportionally.

The bot's Stage 5 (structure) and Stage 6 (sizing) will confirm specific strikes; this narrative defines the *overlay shape*, not single trades.

## Risks

- **Vol bleed in calm regimes** — 1.5% NAV/year is the cost; in a quiet 12-month window, that's pure drag on returns. Mitigation: it's *insurance*, not alpha. Don't measure it against directional trades' P&L.
- **Volatility risk premium reversal** — if realized vol consistently exceeds implied for 6+ months, overlay becomes net-positive but the book has bigger problems. Re-evaluate the entire portfolio construction at that point.
- **Path-dependence on rebalance** — overlay legs that get rolled at the *wrong time* (e.g., rolling a put one day before a vol spike) hurt; rule is monthly ladder, no exceptions, no tactical timing.
- **Single-tail bias** — SPX puts capture *equity* tail. They don't capture a Treasury crisis (TLT collapse) or a USD crisis (DXY shock). For multi-asset tail coverage, separate overlays needed.
- **Crowding in tail hedges** — when too many funds run the same overlay, the put skew gets bid up and overlay becomes expensive. Watch SKEW index and CBOE VIX of VIX (VVIX) for crowding signals.

## Signals generated

[Auto-populated by the bot. Append-only.]

## See also

- [[itpm-framework]] — parent methodology (the non-negotiable synthesis)
- [[long-vol-overlay]] — overlay construction details
- [[long-vol-vs-short-vol]] — short-vol-core + long-vol-overlay synthesis
- [[options-portfolio-construction]] — book-level risk budgeting
- [[2026-market-regime-overview]] — current regime
- [[2026-02-citrini-tech-selloff]] — recent tail-event precedent (energy +12% YTD as tech sold off)
- [[ai-layoff-trap]] — Falk-Tsoukalas tail-risk anchor (justifies non-trivial probability weight on extreme outcomes)
- [[geopolitical-risk-premium]] — supply-side tail anchor
- [[volatility]], [[skew]], [[vix]] — supporting concepts
- [[barbell-portfolio]] — higher-level book shape
- All other narratives in this directory — this overlay sits underneath them
