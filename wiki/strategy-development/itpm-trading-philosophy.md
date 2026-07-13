---
title: "ITPM Trading Philosophy"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [strategy-development, itpm, behavioral-finance, risk-management, education, person]
aliases: ["ITPM Philosophy", "Anton Kreil Philosophy", "Kreil Philosophy", "Professional Trader Mindset"]
related: ["[[itpm-framework]]", "[[anton-kreil]]", "[[options-portfolio-construction]]", "[[theta-targeting]]", "[[the-theta-trap]]", "[[long-vol-vs-short-vol]]", "[[capital-preservation]]", "[[asymmetric-risk-reward]]", "[[professional-vs-retail-mindset]]", "[[ergodicity]]", "[[fees-and-friction]]"]
domain: [strategy-development, behavioral-finance, risk-management]
prerequisites: []
difficulty: beginner
---

The ITPM trading philosophy is the *worldview* underpinning the [[itpm-framework|operational framework]] taught by [[anton-kreil|Anton Kreil]] and the Institute of Trading and Portfolio Management. It answers the *why* questions — why capital preservation outranks return, why asymmetric expected value is the only edge worth pursuing, why professional traders behave so differently from retail, and why the median retail account loses money to fees-and-friction even in bull markets — rather than the *how* questions of book construction, which are covered in [[itpm-framework]] and [[options-portfolio-construction]]. The philosophy is the part of the curriculum that is publicly visible across [[anton-kreil|Kreil]]'s YouTube interviews and the InstaTrader trial videos; the operational machinery is downstream of it.

## Overview

ITPM was founded in 2011 by [[anton-kreil|Kreil]] (a former Goldman Sachs equity-trading desk member, Lehman Brothers proprietary trader, and on-screen trader on the BBC's *Million Dollar Traders*) and co-founders drawn from London bulge-bracket trading floors. Its differentiator from the broader online-education industry is the explicit framing of trading as a **professional discipline**, modelled on the desk practices Kreil and his cohort observed at investment banks before the [[gfc|2008 crisis]] reshaped sell-side prop trading. The philosophy is summarised by Kreil himself in lines that recur across his published material:

> *"Trading is a profession. The professionals are doing something specific, and the retail crowd is doing the opposite of it. Until you stop doing the opposite, you cannot win."*

The structure is intentionally upstream of any specific strategy. ITPM does not have a "trade." It has a worldview about what constitutes an edge, a process for translating that worldview into positions, and a [[capital-preservation|capital-preservation]] discipline that is supposed to keep a trader in the chair long enough for the process to compound. The curriculum — the *Professional Trading Masterclass*, the *Professional Forex Trading Masterclass*, the *Professional Options Trading Masterclass*, the *InstaTrader* mentoring product — is a packaging of this philosophy into instruction; the philosophy itself does not require the courses, and the courses do not guarantee adoption of the philosophy.

## The Five Tenets at a Glance

| # | Tenet | One-line statement | Operational home |
|---|---|---|---|
| 1 | Capital preservation | Still be there next year; drawdowns shrink size, never grow it | [[itpm-framework]] §5; [[capital-preservation]] |
| 2 | Asymmetric R/R | Edge comes from skew, not from being right often | [[asymmetric-risk-reward]]; 3:1 minimum |
| 3 | Professional vs retail gap | The median retail trader is the behavioral inverse of the pro | [[professional-vs-retail-mindset]] |
| 4 | Punter → trader → risk manager | Long-run wealth only compounds from the risk-manager stage | [[itpm-framework]] |
| 5 | Fees-and-friction | Most retail loss is a structural cost stack, not stupidity | [[fees-and-friction]] |

Each tenet is expanded in its own section below and mapped to where it becomes operational in [[#Connection to ITPM Operational Layers]].

## Core Tenets

### 1. Capital preservation is objective number one

The first job of any book is to **still be there next year**. This is the principle Kreil places ahead of return generation in every public talk, and it is the principle most violated by retail traders. The reasoning is mechanical and non-negotiable:

- A 50% drawdown requires a 100% gain to recover. A 75% drawdown requires a 300% gain.
- Compounding is destroyed asymmetrically by drawdown — losses bite harder than equivalent gains.
- A trader who has blown up cannot trade, regardless of how good their next idea is. *Survival is the precondition for skill expression.*

ITPM-aligned position sizing therefore caps individual trade losses at 1-2% of capital, caps cumulative open-position max-loss at 15-25%, and treats drawdowns as signals to *shrink* exposure, never to "double down to make it back." Kreil routinely contrasts this with the retail YouTube ecosystem of "10x your account" content, which he characterises as the inverse of how professionals think about size.

### 2. Asymmetric risk/reward is the only edge worth pursuing

The second tenet is mathematical: a trade with reward-to-risk worse than 2:1 requires a hit rate above 33% just to break even *gross of costs*. Most retail strategies (selling cash-secured puts, scalping for "consistent income," picking-up-pennies setups) have hit rates well above 50% but reward-to-risk near 0.3:1 — i.e., they print small profits often and large losses rarely, with the large losses dominating the long-run distribution. The expected value is negative once costs and tail events are included.

ITPM enforces a **minimum 3:1 reward-to-risk ratio** on directional trades. A 3:1 trade only needs a 25% hit rate to break even before costs. This forces the trader toward *positive-skew expressions* — long options, debit spreads, ratio structures — and away from the pick-up-pennies-in-front-of-a-steamroller bias that catches the retail crowd.

The breakeven arithmetic is the whole argument in one table — the higher the reward-to-risk, the lower the hit rate you can survive:

| Reward : Risk | Breakeven hit rate (gross) | Typical expression |
|---------------|----------------------------|--------------------|
| 0.3 : 1 | ~77% | Naked premium selling, scalping "income" (retail tell) |
| 1 : 1 | 50% | Symmetric directional bet |
| 2 : 1 | ~33% | Minimum many desks accept |
| 3 : 1 | 25% | ITPM directional floor |
| 4 : 1 | 20% | Long-option / debit-spread expressions |

A trader who is right 30% of the time at 4:1 beats a trader right 60% at 1:1 — with smaller drawdowns. That is why hit-rate fixation is treated as a retail tell. Where short premium is used, it sits inside a budget alongside an explicit long-vol overlay (see [[long-vol-vs-short-vol]] and [[long-vol-overlay]]); naked premium selling without an overlay is treated as a category error, not a strategy choice.

The deeper philosophical point: **edge does not come from being right more often. It comes from being asymmetric.** A trader who is right 30% of the time at 4:1 makes more money than a trader who is right 60% at 1:1, with smaller drawdowns. Hit-rate fixation is a retail tell.

### 3. The professional vs retail mindset gap

The largest single claim of the ITPM philosophy is that **the median retail trader is behaviourally the inverse of the median professional**, and that almost all retail underperformance traces to this inversion rather than to information asymmetry. Examples Kreil and the ITPM mentors return to repeatedly:

| Dimension | Retail default | Professional default |
|---|---|---|
| Position rationale | "It looks cheap" / chart pattern / a tip | A macro thesis with a sector and stock expression |
| Hit rate target | High — wants to feel right often | Asymmetric — accepts being wrong often if pay-off justifies it |
| Position sizing | Conviction-based, often largest in worst trades | Risk-budgeted, capped per trade and per book |
| Reaction to drawdown | Adds to losers ("average down") | Cuts size; reviews thesis |
| Reaction to gains | Adds to winners aggressively, takes off too late | Trails risk, scales out into strength |
| Time horizon | Days, often hours; sometimes minutes | Weeks to months; trades are children of multi-month theses |
| Tools | Retail broker, no portfolio Greeks, no journal | Portfolio margin, beta-weighted Greeks, daily journal |
| Hedges | None ("hedges cost money") | Explicit overlay positions with their own Greeks |
| Costs | Ignored | First-pass filter on every strategy |

The professional behaviours are not difficult in isolation — most are written down on the desk procedure manuals of every bulge-bracket trading floor. They are difficult in **aggregate, sustained over years, in the face of psychological pressure**. The ITPM curriculum spends a disproportionate amount of time on the *adherence* skill rather than on idea generation, on the theory that ideas are abundant and the binding constraint is the trader's capacity to act on them consistently.

### 4. The journey: punters → traders → risk managers

A motif throughout Kreil's public material is the three-stage developmental arc:

1. **Punter** — trades for entertainment, dopamine, or to "be a trader." Position sizing is conviction-based. Hit rate is the metric. Drawdowns trigger martingale behaviour. Most retail accounts never leave this stage. Lifespan: typically <2 years before account is destroyed or abandoned.
2. **Trader** — has discovered that hit rate is not the metric, that asymmetric pay-off matters, that costs compound. Begins reading Natenberg, learning Greeks, journaling. Position sizing improves. Hit rate may *fall* (because they are taking better-skewed trades) while expectancy rises. Most ITPM students enter at this stage.
3. **Risk manager** — has internalised that the job is not *to make money on trades* but *to allocate risk capital across opportunities, including the opportunity of holding cash*. Sizes against book Greeks, not per-trade conviction. Treats hedges as positions, not insurance. Runs the book to survive *all* regimes rather than to optimise any one. This is the destination ITPM points toward, modelled on Kreil's experience of how the senior traders at Goldman and Lehman actually operated.

The philosophical claim is that stage 3 is the only stage from which long-run wealth compounds, and that the leap from 2 to 3 is the leap most retail-trained traders never make — they remain technically competent at stage 2 (good charts, decent setups) while never internalising the book-level risk-allocation mindset.

| Attribute | Punter | Trader | Risk manager |
|-----------|--------|--------|--------------|
| Core metric | Hit rate | Expectancy per trade | Book-level risk-adjusted return |
| Sizing basis | Conviction / gut | Per-trade risk budget | Book Greeks; opportunity cost of cash |
| View of hedges | "Hedges cost money" | Insurance, bought reluctantly | Positions with their own Greeks |
| Drawdown response | Martingale / average down | Cut size, review thesis | Re-allocate risk across the book |
| Cash | A failure to be invested | A position when no edge exists | A legitimate allocation |
| Typical lifespan | <2 years to blow-up | Indefinite but plateaus | The destination ITPM points toward |
| Most retail traders | Stay here | Some ITPM students reach | Few make the 2→3 leap |

### 5. Why most retail loses to fees-and-friction

A recurring ITPM data point: retail-broker [[robinhood|payment-for-order-flow]] disclosures, the [[finra]] / SEC retail performance studies, and the etoro / IB account-distribution statistics all converge on roughly **70-90% of retail accounts being net losers over a 12-month window**, even in bull-market years. The ITPM explanation is not that retail traders are stupid; it is that they are caught in a stack of frictions that compounds against them:

- **Commissions and bid-ask spreads** — small per trade, deadly per year on a high-turnover book.
- **Slippage on illiquid options** — wide spreads on single-name far-OTM options can burn 5-10% of premium per round-trip.
- **Tax drag** — short-term capital gains taxed as income; partial-year losses cannot offset prior gains.
- **Margin interest** — Reg-T margin in down moves at 8-13% APR.
- **Behavioural friction** — averaging down, exiting winners early, holding losers, chasing news. Each tilts the realised distribution lower than the theoretical.
- **Selection bias in education content** — the visible "winners" on social media are survivor-biased; the modal trader does not produce content because they are losing money. Aspiring traders calibrate to the visible distribution and underestimate the difficulty.

ITPM's framing is that a retail trader trying to compete *as an active trader* against this stack of frictions, without portfolio margin, without scenario tooling, without the institutional cost structure, is structurally disadvantaged. The recommended response is not to give up but to *acquire the institutional kit* (portfolio margin, beta-weighted Greeks, journaling, fewer-but-bigger trades, longer time horizons) so the friction stack is no longer the binding constraint.

## Empirical Evidence and Sources

The philosophy is articulated across several public artefacts, none behind paywalls:

- **[[anton-kreil|Kreil]]'s YouTube interviews** — the *Real Vision*, *Chat With Traders*, *Trading Nut*, and *Capital Mind* interviews from 2017-2024 form a coherent corpus on the philosophy. Recurring themes: capital preservation as objective #1, the inversion between retail and professional, the role of the bank training environment, the warning against guru content.
- **The *InstaTrader* free trial** — a multi-day video curriculum that previews the philosophy before the paid course pitch. Available on the itpm website and YouTube.
- **The *Professional Trading Masterclass* curriculum overview** — published syllabus available without purchase; covers the structural framing of the courses (macro → sector → stock → structure → size → hedge).
- **Goldman / Lehman background** — Kreil's pre-2008 prop-trading experience is the source of the *"this is how the desk did it"* claims that recur in the philosophy. The relevant practices (risk budgets, daily Greeks, end-of-day risk runs, written kill-criteria) are well-documented in the wider sell-side literature; ITPM packages them for retail.
- **The 70-90% retail-loss statistics** — from European [[esma|ESMA]] CFD broker disclosures (mandated since 2018), [[finra]] retail studies, and broker-specific publications. The number varies by broker and product but consistently sits in this range.

The philosophy itself does not have a single canonical text. It is reconstructed from the corpus and shows up in compressed form throughout the courses; this page captures the working summary used by ITPM-aligned practitioners.

## Common Misapplications

1. **Treating the philosophy as a strategy.** The philosophy is upstream of every strategy; it does not generate trades on its own. A trader who has watched the Kreil interviews and not built the [[itpm-framework|operational framework]] underneath will struggle to translate the worldview into action.
2. **Cargo-culting the language without the discipline.** "Capital preservation" and "asymmetric R/R" are easy to say. The test is whether the trader actually *cuts* on a 1% loss, *holds* a 3:1 winner through chop, *sizes* against book Greeks rather than gut feel, *spends* on overlays in calm regimes. Most adopters fail this test inside the first 3-6 months.
3. **Mistaking the InstaTrader pitch for the philosophy.** ITPM is a commercial school; its public videos are partly marketing. The philosophy survives without the courses, and the courses' value (by the school's own framing) is the *coaching loop* that helps a trader hold the philosophy under pressure, not the unique disclosure of secrets.
4. **Dismissing it because it is publicly available.** Conversely, some traders dismiss ITPM because nothing in the philosophy is novel — every tenet is in [[book-trading-in-the-zone|*Trading in the Zone*]], [[market-wizards]], Natenberg, or Taleb. That is correct *and* irrelevant: the value is in the *integration* and *adherence*, not the originality of any single tenet.
5. **Ignoring that retail underperformance also has structural causes.** The philosophy locates most retail failure in behaviour. A more complete account adds structural causes (no portfolio margin, inferior data, taxation, [[fees-and-friction]]) that no amount of mindset work can overcome without the [[itpm-framework#4 Institutional Infrastructure|infrastructure]] piece. The complete philosophy includes both halves.

## Each Tenet's Characteristic Failure Mode

The philosophy is most useful read defensively — each tenet exists because a specific, common, expensive mistake exists. The table maps tenet to the failure it prevents and where the wiki documents that failure:

| Tenet | Failure it prevents | Wiki cross-reference |
|-------|---------------------|----------------------|
| 1. Capital preservation | Blow-up from oversizing / averaging down | [[capital-preservation]], [[risk-of-ruin]] |
| 2. Asymmetric R/R | Negative-skew "income" books that bleed out in tails | [[asymmetric-risk-reward]], [[the-theta-trap]] |
| 3. Pro vs retail gap | Behavioural inversion (cut winners, hold losers) | [[professional-vs-retail-mindset]], [[behavioral-finance-overview]] |
| 4. Punter→risk-manager | Plateauing at competent-but-not-compounding stage 2 | [[itpm-framework]], [[when-to-retire-a-strategy]] |
| 5. Fees-and-friction | Death by a thousand frictions on a high-turnover book | [[fees-and-friction]], [[options-portfolio-construction]] |

## Connection to ITPM Operational Layers

| Philosophical tenet | Where it shows up operationally |
|---|---|
| Capital preservation | [[itpm-framework#5 Capital Preservation|ITPM framework §5]]; per-trade and book-level loss caps in [[options-portfolio-construction]] |
| Asymmetric R/R | 3:1 minimum on directional trades; positive-skew bias; avoidance of [[the-theta-trap]] |
| Professional discipline | Pre-written daily action lists; [[itpm-framework#How To Apply|review cadence]]; rejection of post-hoc sizing |
| Top-down process | The [[itpm-framework#3 Top-Down Process|seven-stage construction sequence]] |
| Institutional infrastructure | [[portfolio-margin]] requirement; portfolio Greeks tooling; [[itpm-framework#4 Institutional Infrastructure|stage-4 prerequisites]] |
| Punter → trader → risk manager | The progression encoded in the itpm curriculum sequencing |
| Fees-and-friction | The [[options-portfolio-construction|cost-discipline]] section; choice of liquid underlyings; turnover caps |

Each operational layer derives from the philosophy. A trader who tries to lift one layer without the philosophy underneath usually finds it does not produce results — the layer is shape without the load-bearing logic.

## How This Connects to the Rest of the Wiki

The philosophy is the top of the ITPM stack: it is the *why* that the [[itpm-framework|framework]] turns into a *what*, that [[itpm-options-portfolio-management|options portfolio management]] turns into a *how*, and that the [[itpm-playbook|playbook]] indexes end-to-end. Beyond the ITPM pages, the philosophy is an applied reading of the wiki's general methodology: tenet 2 is [[asymmetric-risk-reward]] and connects to [[edge-taxonomy]] (skew is itself a kind of edge); tenet 1 is the behavioral core of [[risk-management]] and [[position-sizing]]; tenet 3 draws directly on [[behavioral-finance-overview|behavioral finance]]; and tenet 4's "risk manager" end-state is the mindset behind [[when-to-retire-a-strategy]] and disciplined [[hypothesis-workflow|hypothesis-driven]] research. The philosophy's warning against cargo-culting language without discipline is the human-side analogue of [[curve-fitting]]: in both cases the *form* of rigor is mistaken for the *substance*.

## Related

- [[itpm-framework]] — the operational construction sequence built on this philosophy
- [[anton-kreil]] — the founder and primary articulator
- [[options-portfolio-construction]] — book-level risk-budgeting layer
- [[theta-targeting]] — income-side discipline that depends on this philosophy
- [[the-theta-trap]] — the canonical failure mode for traders who skip the philosophy
- [[long-vol-vs-short-vol]] — the canonical book shape this philosophy recommends
- [[capital-preservation]] — the central tenet
- [[asymmetric-risk-reward]] — the second tenet
- [[professional-vs-retail-mindset]] — the third tenet
- [[ergodicity]] — why time-average and ensemble-average diverge for leveraged traders
- [[fees-and-friction]] — the structural drag the philosophy targets
- [[behavioral-finance-overview]] — the broader literature this philosophy draws on
- [[itpm-playbook]] — the umbrella index that orders all ITPM material
- [[itpm-options-portfolio-management]] — the options-book expression of the philosophy
- [[risk-management]] / [[position-sizing]] — the applied basis of tenet 1
- [[edge-taxonomy]] — skew and the question of where edge actually comes from
- [[hypothesis-workflow]] — the research analogue of the top-down discipline
- [[when-to-retire-a-strategy]] — the risk-manager-stage kill discipline

## Sources

- [[anton-kreil]] — primary articulator across all public artefacts
- [[itpm-five-principles]] — the underlying discipline framework that compresses the philosophy
- [[itpm-ten-secrets]] — popular packaging of the principles
- [[itpm-education-methodology-overview]] — broader methodology context
- [[itpm-professional-traders-amazing-advice]] — practitioner notes and interview corpus
- *Real Vision* / *Chat With Traders* / *Trading Nut* interview corpus 2017-2024 — public-domain articulations of the philosophy
