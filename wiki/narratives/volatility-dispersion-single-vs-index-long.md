---
title: "Volatility Dispersion → Long Single-Name Vol, Short Index Vol"
type: narrative
created: 2026-05-09
updated: 2026-05-09
status: proposed
side: long
tickers_primary: [NVDA, MSFT, META]
tickers_secondary: [AAPL, GOOGL, AMZN, TSLA]
tickers_hedge: [SPY, SPX]
time_horizon_days: 90
catalysts:
  - "Q2 2026 earnings cycle (each Mag 7 print is a single-name vol catalyst)"
  - "Hyperscaler capex guidance updates"
  - "Anthropic / OpenAI product cycle events"
  - "Any Mag 7 antitrust action / DOJ filing"
  - "Macro shock (Iran escalation, Fed pivot) — index vol regime change tests"
sources:
  - "[[itpm-framework]]"
  - "[[options-portfolio-construction]]"
  - "[[long-vol-vs-short-vol]]"
  - "[[2026-04-09-saas-agent-selloff]]"
  - "[[2026-05-08-cloudflare-ai-layoff-selloff]]"
  - "[[volatility]]"
invalidation:
  - "Realized correlation rises above 0.85 for 30+ days (correlation collapse to crisis-mode unwinds dispersion alpha)"
  - "VIX > 35 sustained (regime change; both legs reprice; reset position)"
  - "Single-name IVs uniformly compress > 30% in 30 days (no idiosyncratic risk priced)"
  - "Sector ETF correlations collapse to < 0.30 (dispersion already realized; chasing risk)"
risk_reward_target: "3:1"
created_by: "slash-command"
---

# Volatility Dispersion → Long Single-Name Vol, Short Index Vol

## Headline

The 2026 regime has produced **violent single-name moves inside a range-bound index**: [[2026-04-09-saas-agent-selloff|April 9 2026 SaaSpocalypse]] (NET -12%, SNOW -9%, NOW -7%, CRM -4% in a session that left SPX nearly flat), [[2026-05-08-cloudflare-ai-layoff-selloff|Cloudflare May 8 2026]] (NET -24% with SPX +0.3%), AMD -17.3% in a single session, ServiceNow -11% intraday on a beat. **Index vol is suppressed by Mag 7 dispersion compensating for non-Mag-7 weakness**; single-name vol is rich. Long single-name calls/puts on Mag 7 names against short SPX vol via straddle/strangle sells is the canonical **vol dispersion** trade. This is the most ITPM-canonical *pure options* expression on the list.

## Thesis

Volatility dispersion captures a specific structural mispricing:

**Realized correlation has dropped to ~0.40–0.55 in 2026** (crisis regimes run 0.80+; calm regimes run 0.30; current is mid-range). When correlation drops, the **weighted average of single-name vols stays high** while **index vol compresses** because the offsetting moves cancel out. The arithmetic:

- Index variance ≈ Σwᵢ²σᵢ² + 2ΣΣwᵢwⱼσᵢσⱼρᵢⱼ
- When ρ drops, the cross-term shrinks; index variance compresses; index vol compresses
- Single-name vols don't compress at the same rate

The trade harvests this structural spread. **Long single-name vol** captures the next major Mag 7 print (any Mag 7 has 3–7σ event risk on earnings or AI catalyst). **Short index vol** captures the index-vol suppression from dispersion. The two legs hedge each other's directional exposure (vega is offsetting); the residual is **pure dispersion alpha**.

The persistent Mag 7 + ex-Mag-7 bifurcation (per [[margin-expansion-disparity]]) is exactly the dispersion-favorable regime. As long as that bifurcation holds, dispersion alpha exists.

## Why now

- **Q2 2026 earnings cycle (June–August)** is dense in single-name event risk — Mag 7 prints span 6–8 weeks with binary catalysts.
- **Realized correlation is at favorable levels** — not so low that dispersion is exhausted, not so high that the trade is mid-cycle.
- **ITPM framework explicitly recommends** dispersion-style expression: per [[itpm-framework]] §"non-negotiable synthesis," the canonical book is short premium (index theta) + long single-name premium (single-name vega) — exactly this construction.
- **90-day horizon** matches the typical earnings-driven dispersion window. Beyond 90 days, vega bleeds; under 90, not enough event density.

## Expression

This is **explicitly an options-only narrative** — there is no equity directional bet.

- **Long single-name vol leg** (~50% of strategy vega):
  - **NVDA** — long ATM straddle 30–60 DTE, spanning earnings. Highest IV in Mag 7; richest convexity.
  - **MSFT** — long ATM strangle 30–60 DTE; smaller position, lower IV
  - **META** — long ATM straddle 30–60 DTE; high event-driven IV
  - Optional smaller: **AAPL, GOOGL, AMZN, TSLA** — diversification at lower individual sizes
- **Short index vol leg** (~50% of strategy vega):
  - **SPY** — short ATM straddle 30–60 DTE, defined-risk via wing protection (iron condor structure)
  - **SPX** — alternative for large-account expression with cash settlement
- **Net Greeks target**:
  - **Vega**: ~zero net vega across the book (long single-name vega ≈ short index vega)
  - **Delta**: ~zero net delta (rebalance daily)
  - **Theta**: positive (short index theta exceeds long single-name theta because index has higher absolute open interest)
  - **Gamma**: positive single-name, negative index — net depends on weighting; typically mildly positive

The bot's Stage 5 (structure) and Stage 6 (sizing) will confirm specific strikes; the construction here is the *structure shape*, not specific strikes.

## Risks

- **Correlation spike** — any "everything goes down together" event (2008-style, 2020-March-style, or 2022-October-style) collapses the dispersion alpha. Single names move in lockstep with index; dispersion P&L goes negative. Mitigation: defined-risk via iron condors on the index leg; hard kill on realized correlation > 0.85 for 30+ days.
- **Single-name short squeeze** — if a long-vol single-name position (e.g., long NVDA straddle) gets hit by a vol-crush event (post-earnings IV collapse without big realized move), the leg bleeds. Standard event-vol risk; partial mitigation via straddle/strangle vs naked call.
- **Index vol gap-up** — short SPX vega can be hit by an unexpected macro event (Iran escalation, BLS shock, Fed surprise). Defined-risk wings (iron condors not naked straddles) cap the loss.
- **Realized vol < implied** — if both legs roll over (single names AND index realize < implied), both legs bleed through theta. Time-decay risk.
- **Operational complexity** — dispersion requires daily Greeks rebalancing across 5–10 positions; not a "set and forget" trade. Operational discipline (per [[itpm-framework]] Principle 2) is the binding constraint.
- **Crowded short index vol** — short-vol consensus is heavy in 2026; index theta bid is rich but a sudden regime change can squeeze the short side. Watch VVIX (vol-of-vol).

## Signals generated

[Auto-populated by the bot. Append-only.]

## See also

- [[itpm-framework]] — parent methodology; this is the canonical pure-options expression
- [[options-portfolio-construction]] — book-level Greek budgeting
- [[long-vol-vs-short-vol]] — short-vol-core + long-vol-overlay synthesis
- [[volatility]], [[correlation]], [[dispersion]] — supporting concepts
- [[2026-04-09-saas-agent-selloff]] — recent dispersion-favorable event
- [[2026-05-08-cloudflare-ai-layoff-selloff]] — single-name -24% with SPX flat (textbook dispersion print)
- [[stagflation-tail-hedge-long-vol-overlay]] — sibling narrative; overlay vs dispersion distinction
- [[iron-condor]], [[straddle]], [[strangle]] — primary expression structures
