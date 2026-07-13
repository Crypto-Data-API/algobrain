---
title: "ITPM Framework"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [strategy-development, itpm, portfolio-theory, risk-management, options, long-short-equity]
aliases: ["ITPM Methodology", "Kreil Framework", "Institute of Trading and Portfolio Management Framework", "Anton Kreil Framework"]
related: ["[[itpm]]", "[[anton-kreil]]", "[[itpm-trade-construction-playbook]]", "[[options-portfolio-construction]]", "[[itpm-five-principles]]", "[[long-vol-vs-short-vol]]", "[[long-short-equity]]", "[[long-vol-overlay]]", "[[barbell-portfolio]]", "[[risk-management-overview]]"]
domain: [strategy-development, portfolio-theory, risk-management]
prerequisites: ["[[options-greeks]]", "[[long-short-equity]]"]
difficulty: intermediate
---

The ITPM framework is the top-down, professional-style trading methodology taught by [[anton-kreil|Anton Kreil]] and the [[itpm|Institute of Trading and Portfolio Management]]. It is not a single strategy but an *operating model* for converting macro views into a hedged book of equity and options positions, sized against pre-budgeted portfolio risk limits and managed under the same discipline used at the bulge-bracket banks where Kreil and his co-mentors trained. This page is the index for that methodology: the five principles, the seven-stage construction sequence, and the connection to the more detailed playbooks already in the wiki.

## Overview

ITPM was founded in 2011 by Kreil (a former [[goldman-sachs|Goldman Sachs]] proprietary trader and trader on the BBC's *Million Dollar Traders*) along with co-mentors [[jason-mcdonald|Jason McDonald]] and others. Its central pedagogical claim is that retail traders fail because they trade *bottom-up* (chart pattern, "looks cheap," a tip) without ever building the macro and sector view that institutional traders take as the starting point of any position. The framework is designed to invert that order: every trade is a *child* of a higher-level decision, and every higher-level decision constrains what trades are even allowed.

The methodology has two layers:

1. **Trade construction** — how a single trade is generated from a macro view. Covered in detail in [[itpm-trade-construction-playbook]].
2. **Portfolio construction** — how trades are sized and combined into a coherent book under explicit Greek and concentration limits. Covered in detail in [[options-portfolio-construction]].

This page is the umbrella: it explains the *why* (the five principles), the *what* (the seven-stage sequence), and points to where each stage is fleshed out. It sits inside the broader [[itpm-playbook|ITPM playbook]], one layer below the [[itpm-trading-philosophy|philosophy]] and one layer above the [[itpm-options-portfolio-management|options-portfolio-management]] and trade-construction layers.

## The Framework in One Page

| Layer | Question it answers | Where it lives |
|---|---|---|
| Five principles | *Why* trade this way | This page, §Core Principles; [[itpm-trading-philosophy]] |
| Seven-stage sequence | *What* order to decide in | This page, §Top-Down Process |
| Trade construction | *How* one trade is built | [[itpm-trade-construction-playbook]] |
| Portfolio construction | *How* trades become a book | [[options-portfolio-construction]], [[itpm-options-portfolio-management]] |
| Review cadence | *How* the book is maintained | [[itpm-playbook]] §Review Cadence |

## Core Principles

ITPM rests on five foundational principles that Kreil articulates as the underlying logic behind the more famous "10 Secrets" content (Source: [[itpm-five-principles]]). Restated for the trading-desk context:

### 1. Asymmetric Risk/Reward

Every trade must have a *minimum 3:1* reward-to-risk ratio. A 3:1 trade only needs a 25% hit rate to break even; a 1:1 trade needs 50% even before costs. Most retail traders pursue high hit rates with negative skew (selling premium without overlays, picking-up-pennies setups), which is mathematically the wrong end of the trade. The ITPM bias is toward *positive-skew* expressions of a view — long options, debit spreads, ratio structures — paid for by the income leg of the book rather than dominating it. Where short premium is used, it sits inside an explicit risk budget alongside a long-vol overlay (see [[long-vol-vs-short-vol]] and [[long-vol-overlay]]).

### 2. Professional Discipline

The hard skill ITPM emphasizes is not idea generation but *adherence*. Risk limits are written down before the open; trades that breach them are rejected even when they look attractive; drawdowns shrink the book, never grow it; the action list for the day is set before market and not re-routed by intra-day price action. ITPM-style traders pre-commit to behavior in calm minutes so the book survives the panicked ones.

### 3. Top-Down Process

A position without a macro reason is a hope. ITPM forces the trader through six macro inputs (global growth, inflation regime, central-bank trajectory, liquidity conditions, risk appetite, currency dynamics) before any single name is considered. Sectors are ranked next, then stocks within favored sectors, then catalysts, then options structure, then size, then hedge layer. The seven-stage flow:

```
1. Macro thesis        →  net long / short / flat the world
2. Geographic split    →  US / EU / EM / Japan weights
3. Sector allocation   →  which sectors to overweight long, which to short
4. Name selection      →  strongest names in long sectors, weakest in short
5. Structure           →  options structure that matches view + vol regime
6. Sizing              →  Greeks contribution against pre-set portfolio limits
7. Hedge layer         →  beta / vega / sector hedges to clean up unwanted risk
```

This is the same flow described in [[itpm-trade-construction-playbook]] for a single trade and in [[options-portfolio-construction]] at the book level. Stages 1-5 generate a *candidate*; stages 6-7 fit it into the book.

The structure choice at stage 5 is not free-form — it is dictated by the *intersection of directional view and volatility regime*. The ITPM-style decision grid:

| Directional view | IV rich (high vs realised) | IV cheap (low vs realised) | Neutral / no edge in vol |
|---|---|---|---|
| Strongly bullish | Bull call spread (debit, vega-light) | Long calls / call diagonal (long vega) | Risk reversal / long stock + collar |
| Mildly bullish | Short put spread (sell rich premium) | Call calendar (own back-month vega) | Covered call / [[cash-secured-puts]] |
| Neutral / range | [[iron-condors]] / strangle (sell vega) | Long straddle / [[long-straddle]] (buy vega) | Sit out — no edge |
| Mildly bearish | Bear call spread / short call spread | Put calendar | Protective collar on existing longs |
| Strongly bearish | Bear put spread (debit) | Long puts / put diagonal / [[put-tree]] | Short stock + long call cap |

The grid encodes the asymmetric-risk principle: where implied vol is rich, the structure *sells* premium inside a defined-risk wrapper; where it is cheap, the structure *buys* convexity. A trader who buys long calls in a rich-vol regime, or sells naked premium in a cheap-vol regime, is fighting both the directional and the volatility edge at once.

### 4. Institutional Infrastructure

Retail traders typically operate with Reg-T margin, brokers that lack scenario tooling, no portfolio Greeks aggregation, and no journaling. ITPM treats these as solvable problems: get a [[portfolio-margin]] account once equity allows ($125-200K minimum), use a platform with risk-graph and book-level scenarios (thinkorswim Analyze, IBKR Risk Navigator, OptionVue), keep a daily Greeks snapshot CSV, and run the same monthly P&L attribution that institutional desks run. The infrastructure choices compound: a trader without portfolio margin cannot run a hedged options book at any reasonable capital efficiency, and a trader without scenario tooling cannot tell whether their book's actual risk equals its budgeted risk.

### 5. Capital Preservation

The first job of any book is to still be there next year. ITPM-aligned rules:

- Per-trade max loss: 1-2% of capital for directional discretionary trades, 0.5-1% for premium-selling trades (because tail loss exceeds stated max-loss in stress).
- Cumulative max-loss across all open positions: 15-25% of capital.
- Single-day VaR (95th percentile, stress-tested): 3-5% of capital.
- Drawdowns *shrink* position size; they never trigger martingale add-ons.
- Hedges are explicit positions with their own Greeks, not assumed offsets.

The principle traces directly to Kreil's experience watching prop traders blow up at Goldman: the survivors were not the highest-conviction traders but the ones who size cautiously, hedge explicitly, and refuse to add to losers.

## The Five Pre-Trade Limits as a Risk Budget

Stage 6 (sizing) is mechanically a *budget check*: each candidate trade contributes to five running totals, and the book is only allowed to grow if all five stay inside their pre-committed caps. This is the operational heart of the framework — the place where discipline either holds or fails. Indicative limit ranges (each book sets its own, written before the open):

| Limit | What it caps | Indicative cap | Why it exists | Fails into |
|---|---|---|---|---|
| Net portfolio vega | Sensitivity to a 1-pt IV move | $800–$1,500 per vol-pt (per $250K) | A vol spike must not exceed the overlay's offset | [[hedging-program-failure-modes]] FM4 |
| Theta target | Daily decay income | Positive, ≤ ~0.1% NAV/day | Income leg pays for the overlay, not the reverse | Over-selling premium |
| Expiration concentration | Notional in any single cycle | ≤ 30% of option notional | One bad expiry cannot dominate P&L | Pin / gamma blow-up |
| Sector concentration | Net delta in one sector | ≤ 20–25% of net beta-weighted delta | The macro thesis, not one sector, drives risk | Hidden factor bet |
| Single-name notional | Exposure to one underlying | ≤ 5–10% of capital | No idiosyncratic shock is fatal | Concentration ruin |

These limits connect directly to [[vega-budgeting]], [[theta-targeting]], and the book-level mechanics in [[options-portfolio-construction]]. The discipline is not the *numbers* — desks differ — but the *act of writing them down before the open and rejecting any trade that breaches them*. This is the applied face of [[position-sizing]] and [[risk-of-ruin|risk-of-ruin]] avoidance at the book level.

## Regime Fit

ITPM is deliberately a *survive-every-regime* methodology rather than a regime-timing one — but the framework's emphasis shifts with the volatility and macro backdrop. See the wiki-wide [[regime-matrix]] for the cross-strategy view.

| Regime | What the ITPM book does | Dominant leg |
|---|---|---|
| Low-vol grind / melt-up | Earn theta on the short-vol core; keep the overlay on despite drag | Income core + small overlay |
| High-vol / stressed | Overlay monetises; resize the income core down; harvest convexity | Long-vol overlay |
| Range-bound / choppy | Premium selling shines; tight expiration laddering | Income core |
| Macro regime change | Re-run stage 1; rotate sector/name selection; widen overlay | Macro thesis + hedge layer |

The framework's *signature* is that none of these regimes should produce a catastrophic outcome — the overlay caps the downside in stress, and the income core funds the overlay in calm. That is the same survival-first geometry described in [[barbell-portfolio]] and [[long-vol-vs-short-vol]].

## How To Apply

For a trader adopting the ITPM framework from scratch, the practical sequence is:

1. **Write a macro one-pager.** A single page covering the six macro inputs and what they imply for asset-class bias, refreshed monthly. Without this, stages 2-7 cannot start.
2. **Pick 2-4 thematic positions.** Translate the macro into specific trades: "long US large-cap tech because the Fed is on hold and AI capex is accelerating," "short European banks because the ECB is behind the curve." These themes are the *parents* of every individual position.
3. **Set the five pre-trade portfolio limits.** Maximum portfolio vega, theta target, maximum expiration concentration, maximum sector concentration, maximum single-name notional. These are inputs to every subsequent trade decision; see [[options-portfolio-construction]].
4. **Build a candidate trade through stages 4-5.** Strongest stock in a favored sector, options structure matched to vol regime and time horizon, defined entry/target/stop with R/R ≥ 3:1.
5. **Run the post-trade portfolio check (stage 6).** Compute the book's Greeks *after* the candidate trade is added. If any of the five limits is breached, resize or restructure or reject.
6. **Add the hedge layer (stage 7).** Net delta hedge with futures, net vega hedge with index puts or VIX calls, sector hedge with sector ETF if needed. Hedges are book-level overlays, not per-trade insurance.
7. **Run the daily / weekly / monthly review loops.** Daily Greeks check before the open; weekly thesis review; monthly book rebalance. The cadence is documented in [[options-portfolio-construction#Review Cadence|the portfolio construction page]].

The framework is software-agnostic but deliberately not platform-agnostic: it requires portfolio margin, beta-weighted Greeks across the book, and stress-test tooling. Trying to run it without those tools is the most common failure mode.

## Connection to Options Portfolio Construction

The ITPM framework is the macro-and-process *layer*; [[options-portfolio-construction]] is the risk-budgeting *layer* that sits underneath it. The two map cleanly:

| ITPM stage | Where it lives in the wiki |
|---|---|
| Stages 1-3 (macro, geography, sector) | [[itpm-trade-construction-playbook]] §1-3 |
| Stage 4 (name selection) | [[itpm-trade-construction-playbook]] §4 |
| Stage 5 (structure) | [[itpm-trade-construction-playbook]] §7 |
| Stage 6 (sizing) | [[options-portfolio-construction#Position Layering]] |
| Stage 7 (hedging) | [[options-portfolio-construction#Hedging at the Book Level vs Trade Level]] |
| Vol-overlay design | [[long-vol-overlay]], [[long-vol-vs-short-vol]] |
| Risk budgeting per Greek | [[vega-budgeting]], [[theta-targeting]] |

The [[long-vol-vs-short-vol#The Synthesis: Short-Vol Core + Long-Vol Overlay|short-vol-core-plus-long-vol-overlay]] construction described on the long-vs-short page is the *canonical ITPM-aligned options book*: a premium-selling core sized against an explicit vega budget, with a continuously-laddered long-vol overlay sized so a 30%+ equity drawdown leaves the combined book inside acceptable drawdown limits. ITPM does not invent this construction — it borrows it from how options market-makers and hedge-fund overlay desks have run books for decades — but it is the most accessible packaging of the discipline available to retail traders.

## Worked Example

A trader has a $250K account. Macro view (May 2026 hypothetical): Fed on hold, growth slowing but not recessionary, AI capex still elevated, Europe lagging, China stimulus uncertain.

Thematic positions:

- **Long US mega-cap tech** (NVDA, MSFT, GOOGL) — the AI capex thesis.
- **Short European autos** (relative weakness, China demand uncertainty).
- **Net long-vol bias** — equity vols compressed, asymmetric setup.

Construction (sized to ITPM limits):

1. **Long tech expression**: 3 long call diagonals on NVDA/MSFT/GOOGL, 60-90 DTE long leg, 30 DTE short leg, debit ~$1,500 per name = $4,500 total (1.8% of account at risk).
2. **Short Europe expression**: long EUFN puts, 60 DTE, ~$2,000 debit (0.8% of account).
3. **Premium-selling core**: 3 SPX 16-delta strangles, 45 DTE, ~$15K margin, ~$30/day theta. Sized to fit a $1,200/vol-point net-short-vega budget.
4. **Long-vol overlay**: 6-month SPY put ladder, $300/month spend = $3,600/year (~1.4% of NAV).
5. **Net delta**: book is +400 net beta-weighted deltas after construction. Optionally short 1 ES future to flatten; or hold the residual as a deliberate small long-equity tilt consistent with the macro view.
6. **Daily Greeks check**: written before open. Action list: roll any position inside 21 DTE; close any single-name position whose thesis has been invalidated; rebalance overlay if it has drifted out of the 5%-of-NAV band.

The book has a defined macro story, a defined risk budget per Greek, an explicit overlay against the worst-case scenario, and a written review cadence. It is not optimized for any single regime — it is built to *survive* every regime and continue compounding. That survival-first construction is the ITPM-framework signature.

## Common Misapplications

The framework is publicly visible, but the most common ways traders mis-implement it are:

1. **Top-down theatre, bottom-up reality.** A trader writes a macro one-pager, then trades whatever setups they would have traded anyway. The macro is decoration, not a constraint. Detection: the trades have no logical connection to the stated macro view.
2. **Skipping the hedge layer.** Stages 1-6 are intellectually satisfying; stage 7 is boring. Many ITPM-trained retail traders run unhedged long-only books with a long-short label. The book performs like the underlying market because it *is* the underlying market.
3. **Confusing the framework with the curriculum.** ITPM sells courses. The framework on this page is what professional trading desks have done for decades; the courses are one packaging of it. Adopting the framework does not require buying the courses, and buying the courses does not guarantee adopting the framework.
4. **Running it without portfolio margin.** Reg-T margin makes hedged option books prohibitively expensive. A trader trying to run ITPM-style construction at $50K with strategy-based margin will be capacity-constrained in a way that destroys the methodology's risk math.
5. **Pretending discipline at $25K then losing it at $250K.** Position-size discipline is easy when small mistakes are recoverable. The test is whether the rules survive the first time the trader is tempted to override them at 10x the size. ITPM frames this as the central skill of the profession; most retail adopters underestimate it.
6. **Selling premium with no overlay and calling it ITPM.** ITPM does *not* teach naked premium selling as a stand-alone strategy. Any book that has ever earned theta should also have spent on a long-vol overlay. The synthesis is non-negotiable; see [[long-vol-vs-short-vol]] and the failure-mode catalogue in [[hedging-program-failure-modes]].

## How This Connects to the Rest of the Wiki

The ITPM framework is a *discipline-and-process* methodology, so it sits naturally alongside the wiki's general strategy-development methodology. Its top-down stage 1 (macro thesis) is a structured form of the [[hypothesis-workflow|hypothesis workflow]] — a position must descend from a stated view, never the reverse. Its insistence on naming why a trade should work maps onto [[edge-taxonomy|edge taxonomy]] (a position with no identifiable edge source fails stage 1). Its capital-preservation principle is the applied face of [[risk-management]] and [[position-sizing]], and its sizing gate (stage 6) is a Greek-budgeted form of position sizing at the book level. The framework's downstream layers are [[itpm-options-portfolio-management]] (the options view of the book) and [[options-portfolio-construction]] (the risk-budgeting mechanics); its hedge layer is catalogued for failure in [[hedging-program-failure-modes]]; and the question of when an ITPM-style book should retire a sleeve is governed by [[when-to-retire-a-strategy]]. The philosophical load-bearing layer underneath everything is [[itpm-trading-philosophy]], and the whole set is indexed by [[itpm-playbook]].

## Related

- [[itpm]] — the school
- [[anton-kreil]] — the founder
- [[itpm-trade-construction-playbook]] — the single-trade workflow
- [[options-portfolio-construction]] — the book-level risk-budgeting layer
- [[itpm-five-principles]] — primary source for the five principles
- [[long-vol-vs-short-vol]] — the canonical synthesis the framework recommends
- [[long-vol-overlay]] — the overlay leg of the recommended construction
- [[barbell-portfolio]] — the higher-level shape an ITPM-aligned book takes
- [[long-short-equity]] — the underlying portfolio archetype
- [[options-greeks]] — the risk dimensions being budgeted
- [[portfolio-margin]] — the infrastructure prerequisite
- [[variance-risk-premium]] — the source of the premium-selling income
- [[risk-management-overview]]
- [[itpm-trading-philosophy]] — the worldview layer this framework rests on
- [[itpm-playbook]] — the umbrella index for all ITPM material
- [[itpm-options-portfolio-management]] — the options-specific view of the book
- [[hedging-program-failure-modes]] — how the stage-7 hedge layer fails
- [[hypothesis-workflow]] — the general-methodology analogue of stage 1
- [[edge-taxonomy]] — the discipline of naming why a trade should work
- [[risk-management]] / [[position-sizing]] — the applied basis of principle 5
- [[when-to-retire-a-strategy]] — governing the kill decision for a book sleeve

## Sources

- [[itpm]] — ITPM company page and curriculum overview
- [[anton-kreil]] — primary articulator of the framework
- [[itpm-five-principles]] — the underlying discipline framework
- [[itpm-ten-secrets]] — companion source covering the popular packaging of the principles
- [[itpm-education-methodology-overview]] — broader methodology context
- [[itpm-professional-traders-amazing-advice]] — practitioner notes
- [[itpm-trade-construction-playbook]] — single-trade workflow
- [[options-portfolio-construction]] — book-level workflow
