---
title: "ITPM Playbook"
type: index
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [strategy-development, itpm, education, options, risk-management, person]
aliases: ["ITPM Playbook", "Kreil Playbook", "Institute of Trading and Portfolio Management Playbook", "ITPM Curriculum Hub"]
related:
  - "[[itpm]]"
  - "[[anton-kreil]]"
  - "[[itpm-trading-philosophy]]"
  - "[[itpm-framework]]"
  - "[[itpm-trade-construction-playbook]]"
  - "[[itpm-options-portfolio-management]]"
  - "[[itpm-five-principles]]"
  - "[[itpm-ten-secrets]]"
  - "[[itpm-ratio-calendar-spread]]"
  - "[[options-portfolio-construction]]"
  - "[[long-vol-vs-short-vol]]"
  - "[[long-vol-overlay]]"
  - "[[theta-targeting]]"
  - "[[the-theta-trap]]"
  - "[[capital-preservation]]"
  - "[[asymmetric-risk-reward]]"
  - "[[professional-vs-retail-mindset]]"
  - "[[fees-and-friction]]"
  - "[[barbell-portfolio]]"
  - "[[strategy-development-overview]]"
---

The ITPM playbook is the umbrella index for the [[itpm|Institute of Trading and Portfolio Management]] material in this wiki — the philosophy, the operational framework, the trade-construction workflow, the portfolio-management layer, the canonical structures, the source corpus, and the supporting interview material. ITPM, founded in 2011 by [[anton-kreil|Anton Kreil]] (former [[goldman-sachs|Goldman Sachs]] equity trader, [[lehman-brothers|Lehman Brothers]] proprietary trader, and on-screen trader on the BBC's *Million Dollar Traders*) and co-mentors drawn from London bulge-bracket trading floors, packages the desk practices of pre-2008 sell-side proprietary trading into a curriculum aimed at retail traders. This page exists to orient a reader to the materials in the order they should be read, and to make the connections between the philosophy layer, the operational layer, and the canonical structures explicit.

## The Playbook in One Page

The ITPM playbook, compressed to a single sequence:

```
Philosophy           →  Why preserve capital, why asymmetric, why professional discipline
Framework            →  The seven-stage top-down construction process
Trade construction   →  Single-trade workflow from macro view to executed position
Portfolio management →  Book-level Greek budgeting, hedging, overlays, review cadence
Review cadence       →  Daily Greeks, weekly thesis, monthly attribution, quarterly book
```

A trader who reads only the strategies and skips the philosophy implements the structures without the load-bearing logic underneath, and abandons them in the first stress event. A trader who reads only the philosophy and skips the operational layers has a worldview without the discipline to express it. The playbook is the integration: each layer presupposes the one above it, and each enables the one below it.

### The five layers as a map

| Layer | Question it answers | Core pages | What breaks if skipped |
|---|---|---|---|
| 1. Philosophy | *Why* preserve capital, why asymmetric | [[itpm-trading-philosophy]], [[capital-preservation]], [[asymmetric-risk-reward]], [[professional-vs-retail-mindset]], [[fees-and-friction]] | Structures abandoned in first drawdown |
| 2. Framework | *What* is the construction process | [[itpm-framework]], [[itpm-five-principles]], [[itpm-ten-secrets]] | Trades with no gate; ad-hoc entries |
| 3. Trade construction | *How* a single trade is built | [[itpm-trade-construction-playbook]], [[itpm-ratio-calendar-spread]] | Reverse-engineered theses; [[curve-fitting]] |
| 4. Portfolio management | *How* trades combine into a book | [[itpm-options-portfolio-management]], [[options-portfolio-construction]], [[long-vol-overlay]], [[theta-targeting]] | Long-only-with-extra-steps; short-tail book |
| 5. Review cadence | *When* to act and re-justify | [[itpm-framework#How To Apply]], [[options-portfolio-construction#Review Cadence]], [[when-to-retire-a-strategy]] | Upstream layers become theatre |

The dependency runs strictly top-down: each layer *presupposes* the one above (you cannot construct a trade without a framework gate) and *enables* the one below (the framework is inert without a review cadence to enforce it). Skipping any single layer is the most reliable way to convert the playbook from a discipline into a costume.

## Layer 1: Philosophy

The philosophical layer answers the *why* questions: why capital preservation outranks return, why asymmetric expected value is the only edge worth pursuing, why professionals behave so differently from retail, and why the median retail account loses money to fees-and-friction even in bull markets. The relevant pages:

- [[itpm-trading-philosophy]] — the central synthesis. Five tenets: capital preservation, asymmetric R/R, professional vs retail, the punter→trader→risk-manager arc, and fees-and-friction as structural cause.
- [[capital-preservation]] — the first tenet expanded. Geometric vs arithmetic returns, drawdown circuit breakers, position sizing as fraction of equity.
- [[asymmetric-risk-reward]] — the second tenet expanded. The breakeven hit-rate hyperbola, positive skew, why options are the natural expression.
- [[professional-vs-retail-mindset]] — the third tenet expanded. The dimension-by-dimension table of inversions, the closing-the-gap recipe, the 70-90% retail-loss statistic.
- [[fees-and-friction]] — the structural-side companion to the behavioural divergence. The cost stack layer-by-layer.

These five pages are the philosophical core. A trader who internalises only this layer has the worldview but not the implementation.

## Layer 2: Framework

The framework layer answers the *what* questions: what is the construction process, what are the stages, what are the gates between stages, what are the limits at each stage. The relevant pages:

- [[itpm-framework]] — the umbrella operational page. The five principles in their operational form, the seven-stage top-down sequence, the worked example.
- [[itpm-five-principles]] — the source articulation of the five principles ([[anton-kreil|Kreil]]'s May 2018 London seminar transcript).
- [[itpm-ten-secrets]] — the popular packaging of the principles for general audiences.

The framework is *upstream* of any specific trade. It defines the gates that every candidate position must clear before it enters the book.

## Layer 3: Trade Construction

The trade-construction layer is the per-trade workflow. The relevant pages:

- [[itpm-trade-construction-playbook]] — the eleven-stage workflow from macro view to exit. Macro thesis → geographic split → sector → name → catalyst → R/R geometry → options structure → sizing → hedging → management → exit.
- [[itpm-ratio-calendar-spread]] — the canonical positive-skew options structure, illustrating the asymmetric-R/R principle with a concrete 2:1 trade.

Trade construction is the single most published piece of the ITPM material, because it is the most teachable. The workflow is *deterministic* given a macro view; the macro view itself is the discretionary part.

## Layer 4: Portfolio Management

The portfolio-management layer is the book-level integration of trades. The relevant pages:

- [[itpm-options-portfolio-management]] — the book-level page covering position layering, hedging, and review cadence in the ITPM frame.
- [[options-portfolio-construction]] — the broader risk-budgeting layer that the ITPM framework sits inside. Vega budgeting, theta targeting, expiration concentration, sector concentration, single-name concentration.
- [[long-vol-vs-short-vol]] — the canonical book shape: short-vol core (premium-selling) plus continuously-laddered long-vol overlay.
- [[long-vol-overlay]] — the explicit hedge layer, sized so a 30%+ equity drawdown leaves the combined book inside acceptable drawdown limits.
- [[theta-targeting]] — the income-side discipline that funds the overlay.
- [[the-theta-trap]] — the canonical failure mode for traders who skip the philosophy and run the income layer naked.
- [[barbell-portfolio]] — the higher-level shape an ITPM-aligned book takes (heavy cash + tail-protected book).

A trader who runs the framework and the trade-construction layer but skips the portfolio-management layer ends up with a long-only-with-extra-steps book. The portfolio layer is what makes the overall structure professional.

## Layer 5: Review Cadence

The review-cadence layer is the day-to-day expression of the discipline:

- **Daily**: Greeks snapshot before the open; written action list; roll any position inside 21 DTE; close any position whose thesis is invalidated. See [[itpm-framework#How To Apply]].
- **Weekly**: Thesis review — every position re-justified against its original thesis. Positions whose thesis is dead are exited even if the price has not moved.
- **Monthly**: Book rebalance — gross exposure, sector concentration, single-name concentration, and overlay sizing checked against limits and rebalanced.
- **Quarterly**: P&L attribution decomposed into edge, fees, slippage, and noise. Strategies whose realised edge is materially below backtest are flagged for review.

| Cadence | Focus | Key actions | Trigger to act |
|---|---|---|---|
| Daily | Greeks + thesis integrity | Pre-open Greeks snapshot, written action list, roll <21 DTE, close dead theses | Any Greek outside band; thesis invalidated |
| Weekly | Thesis re-justification | Every position re-argued from its original thesis | Thesis dead → exit even if price flat |
| Monthly | Book rebalance | Re-check gross, sector, single-name concentration, overlay sizing | Any limit breached → rebalance |
| Quarterly | P&L attribution | Decompose into edge, fees, slippage, noise | Realised edge << backtest → flag for review |

The cadence is documented in [[options-portfolio-construction#Review Cadence]] and is the daily-life expression of the philosophy. It is also the ITPM-flavoured instance of the general [[strategy-monitoring]] discipline (daily performance, periodic edge-health review) and of [[when-to-retire-a-strategy]] (the quarterly attribution is the kill gate). Without it, the upstream layers are theatre.

## Source Corpus

The ITPM material is drawn from a public corpus: [[anton-kreil|Kreil]]'s YouTube interviews and seminars, the InstaTrader free-trial videos, the *Trading Legends* interview series, and the published syllabus of the *Professional Trading Masterclass* and *Professional Options Trading Masterclass*. The relevant source pages in this wiki:

### Core Sources

- [[itpm-five-principles]] — May 2018 London seminar; the philosophical core
- [[itpm-ten-secrets]] — popular packaging of the principles
- [[itpm-education-methodology-overview]] — broader methodology context
- [[itpm-professional-traders-amazing-advice]] — practitioner notes and corpus extracts

### Trading Legends Interview Series

The *Trading Legends* series interviews ITPM mentors and other professionals on their careers, philosophy, and operational practices. These are the richest sources of *how the desk actually worked* material:

- [[itpm-trading-legends-raj-malhotra]] — head of institutional options at [[bank-of-america|Bank of America]] / [[nomura]]
- [[itpm-trading-legends-jason-mcdonald]] — ITPM co-mentor
- [[itpm-trading-legends-ben-berggreen]] — proprietary equity trader
- [[itpm-trading-legends-chris-cathey]] — ITPM mentor
- [[itpm-trading-legends-hichem-djouhri]] — proprietary trader

### Commentary and Critique

Kreil's *War on YouTube Mentors* (WOYM) series and related videos critique the broader retail-education ecosystem. Useful for understanding the philosophy in opposition to its targets:

- [[itpm-annihilates-retail-brokers]]
- [[itpm-investment-banks-destroyed]]
- [[itpm-goldman-sachs-tells-truth]]
- [[itpm-god-like-trader-status]]
- [[itpm-meet-dieter-the-doubler]]
- [[itpm-master-compounding]]
- [[itpm-woym-ep27-recession-narrative]]

The commentary material is partly entertainment, partly philosophical reinforcement. The repeated targets — broker PFOF models, guru content, options-prop-firm pitches, "10x your account" YouTube — are the same negative-space from which the ITPM positive philosophy is constructed.

## Reading Sequence

For a reader new to the ITPM material, the recommended sequence:

1. **Start with [[itpm-trading-philosophy]]** — ~30 minutes. The philosophical core. If the philosophy does not resonate, the rest of the playbook will not adopt.
2. **Read the five tenet pages** — [[capital-preservation]], [[asymmetric-risk-reward]], [[professional-vs-retail-mindset]], [[fees-and-friction]], plus the punter→trader→risk-manager arc material in the philosophy page itself.
3. **Move to [[itpm-framework]]** — the operational umbrella. This is where the philosophy becomes a process.
4. **Read [[itpm-trade-construction-playbook]]** — the per-trade workflow. The longest single page in the playbook.
5. **Read the portfolio-management layer** — [[options-portfolio-construction]], [[long-vol-vs-short-vol]], [[long-vol-overlay]], [[theta-targeting]], [[itpm-options-portfolio-management]].
6. **Study the canonical structures** — [[itpm-ratio-calendar-spread]] and the related options-structure pages linked from there.
7. **Sample the source corpus** — at least [[itpm-trading-legends-raj-malhotra]] and [[itpm-five-principles]]. The interviews are the most concrete *how the desk worked* material.

A reader who completes this sequence has the worldview, the framework, and the operational tools. The remaining work is *adherence over years*, which the published material consistently identifies as the binding constraint.

### Reading sequence as a table

| Step | Page | Layer | Why read it here |
|---|---|---|---|
| 1 | [[itpm-trading-philosophy]] | 1 | The load-bearing *why*; if it doesn't resonate, stop |
| 2 | [[capital-preservation]], [[asymmetric-risk-reward]], [[professional-vs-retail-mindset]], [[fees-and-friction]] | 1 | The four tenets expanded |
| 3 | [[itpm-framework]] | 2 | Philosophy becomes process |
| 4 | [[itpm-trade-construction-playbook]] | 3 | The per-trade workflow (longest page) |
| 5 | [[options-portfolio-construction]], [[long-vol-vs-short-vol]], [[long-vol-overlay]], [[theta-targeting]], [[itpm-options-portfolio-management]] | 4 | Book-level integration |
| 6 | [[itpm-ratio-calendar-spread]] | 3/4 | The canonical positive-skew structure |
| 7 | [[itpm-trading-legends-raj-malhotra]], [[itpm-five-principles]] | source | "How the desk worked" primary material |

### Entry point by reader type

The full sequence is for a reader new to the material. Readers arriving with a specific need can jump in:

| Reader | Start here | Then |
|---|---|---|
| New to ITPM entirely | [[itpm-trading-philosophy]] | Follow the full sequence above |
| Already trades options, wants the book layer | [[itpm-options-portfolio-management]] | [[options-portfolio-construction]], [[long-vol-overlay]] |
| Wants one concrete structure | [[itpm-ratio-calendar-spread]] | [[itpm-trade-construction-playbook]] for context |
| Sceptical / wants the critique | [[professional-vs-retail-mindset]], the WOYM commentary | [[itpm-trading-philosophy]] |
| Comparing to other frameworks | [[#How the Playbook Maps to General Methodology]] | [[edge-taxonomy]], [[strategy-development-overview]] |
| Worried about the hedge failing | [[hedging-program-failure-modes]] | [[long-vol-overlay]], [[the-theta-trap]] |

## How the Playbook Maps to General Methodology

The ITPM playbook is one school's packaging of ideas that recur throughout the wiki's general [[strategy-development-overview|strategy-development methodology]]. The mapping is worth making explicit so a reader does not treat ITPM as a closed system:

| ITPM layer | General-methodology analogue |
|---|---|
| Philosophy (asymmetric R/R, capital preservation) | [[edge-taxonomy]], [[risk-management]], [[position-sizing]] |
| Framework stage 1 (macro thesis) | [[hypothesis-workflow]] — a position must descend from a stated view |
| Trade construction | The disciplined, pre-specified rules that defend against [[curve-fitting]] |
| Portfolio management / hedge layer | [[options-portfolio-construction]], [[hedging-program-failure-modes]] |
| Review cadence / kill discipline | [[when-to-retire-a-strategy]], P&L attribution |

The value of the playbook, by its own framing, is *integration and adherence*, not novelty — every individual idea has an independent home elsewhere in the wiki.

## What This Playbook Is Not

A few clarifications, because the ITPM material is sometimes mis-characterised:

1. **It is not a strategy.** ITPM does not have a "trade." It has a worldview, a process, and a portfolio shape. Inside that shape, many strategies are valid; outside it, even good strategies fail.
2. **It is not a guarantee.** Adherence to the framework reduces the realised tail and improves the geometric-return distribution; it does not make a trader infallible. Bulge-bracket desks blow up regularly.
3. **It is not platform-agnostic.** The framework requires [[portfolio-margin]], book-level Greeks aggregation, and scenario tooling. Running it on Robinhood with no tools is a category error.
4. **It is not coursework-dependent.** The philosophy and framework are publicly visible across the YouTube and seminar corpus. The ITPM courses are *one packaging* and a *coaching loop*; they are not the only path to the discipline.
5. **It is not retail-friendly below ~$125-200K.** The math of hedged options books and portfolio margin requires this floor. Below it, the framework runs at a different — typically negative — expected return because [[fees-and-friction]] dominates.
6. **It is not unique to ITPM.** Every tenet is in [[book-trading-in-the-zone|*Trading in the Zone*]], [[market-wizards|Schwager's *Market Wizards* series]], Natenberg, and Taleb. The value is in the *integration* and *adherence loop*, not the originality of any single tenet.

## Related

- [[itpm]] — the school
- [[anton-kreil]] — the founder
- [[itpm-trading-philosophy]] — philosophical core
- [[itpm-framework]] — operational umbrella
- [[itpm-trade-construction-playbook]] — per-trade workflow
- [[itpm-options-portfolio-management]] — book-level layer
- [[itpm-five-principles]] / [[itpm-ten-secrets]] — primary sources
- [[itpm-ratio-calendar-spread]] — canonical structure
- [[options-portfolio-construction]] — risk-budgeting layer
- [[long-vol-vs-short-vol]] — canonical book shape
- [[long-vol-overlay]] — hedge layer
- [[theta-targeting]] — income layer
- [[the-theta-trap]] — canonical failure mode
- [[capital-preservation]] — first tenet
- [[asymmetric-risk-reward]] — second tenet
- [[professional-vs-retail-mindset]] — third tenet
- [[fees-and-friction]] — structural side
- [[barbell-portfolio]] — book-level shape
- [[strategy-development-overview]] — the broader strategy-development methodology
- [[hedging-program-failure-modes]] — how the portfolio-layer hedge fails
- [[edge-taxonomy]] — where edge actually comes from
- [[hypothesis-workflow]] — the general analogue of the macro-thesis stage
- [[curve-fitting]] — the research-discipline failure the playbook guards against
- [[when-to-retire-a-strategy]] — the kill discipline behind the review cadence

## Sources

- [[itpm]] — ITPM company page and curriculum overview
- [[anton-kreil]] — founder; primary articulator across all public artefacts
- [[itpm-five-principles]] — primary articulation of the five-principle framework
- [[itpm-ten-secrets]] — popular packaging
- [[itpm-education-methodology-overview]] — broader methodology
- [[itpm-professional-traders-amazing-advice]] — practitioner corpus
- [[itpm-trading-legends-raj-malhotra]] / [[itpm-trading-legends-jason-mcdonald]] / [[itpm-trading-legends-ben-berggreen]] / [[itpm-trading-legends-chris-cathey]] / [[itpm-trading-legends-hichem-djouhri]] — interview series
- *Real Vision* / *Chat With Traders* / *Trading Nut* / *Capital Mind* interview corpus 2017-2024 — public-domain articulations
- The *Professional Trading Masterclass*, *Professional Forex Trading Masterclass*, and *Professional Options Trading Masterclass* curriculum overviews — public syllabi
- [[goldman-sachs]] / [[lehman-brothers]] — institutional background informing the desk-practice claims
