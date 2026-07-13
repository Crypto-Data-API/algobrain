---
title: "ITPM Options Portfolio Management"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [strategy-development, itpm, portfolio-theory, risk-management, options, long-short-equity]
aliases: ["ITPM Options Portfolio Management", "ITPM Options Approach", "ITPM Options Book Methodology"]
related: ["[[itpm-framework]]", "[[itpm-trade-construction-playbook]]", "[[itpm-trading-philosophy]]", "[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[options-position-sizing]]", "[[itpm-ratio-calendar-spread]]", "[[ratio-calendar-spread]]", "[[long-short-equity]]", "[[anton-kreil]]", "[[itpm]]", "[[long-vol-overlay]]", "[[long-vol-vs-short-vol]]", "[[barbell-portfolio]]", "[[expiration-laddering]]", "[[portfolio-greeks-aggregation]]", "[[theta-targeting]]", "[[5-percent-otm-put-overlay]]", "[[volatility-risk-premium]]"]
domain: [strategy-development, portfolio-theory, options]
prerequisites: ["[[itpm-framework]]", "[[options-greeks]]", "[[long-short-equity]]"]
difficulty: advanced
---

This page is the **options-specific overlay** on the broader [[itpm-framework|ITPM framework]]. Where [[itpm-framework]] describes the seven-stage construction sequence (macro → geographic → sector → name → structure → sizing → hedge) at the methodology level, and [[options-portfolio-construction]] describes the practical book-construction work (pre-trade Greek limits, expiration laddering, stress tests), this page focuses narrowly on **how options as instruments fit into that framework**: when they replace stock, when they complement stock, how the Greeks become inputs at each stage, and what the canonical ITPM options structures look like as portfolio building blocks.

## The Options Question at Each Framework Stage

The ITPM seven-stage flow is instrument-agnostic at the macro layers and increasingly options-aware as it descends:

| Stage | Options-specific decision |
|---|---|
| 1. Macro thesis | Does the macro view favor long-vol or short-vol expression? Are options the right vehicle at all? |
| 2. Geographic split | Which index/single-name options have liquidity in the target geography? US large-cap = SPX/SPY; emerging markets = limited options availability |
| 3. Sector allocation | Which sector ETF options are liquid enough for hedging? Which sector single-names have tradable options? |
| 4. Name selection | Does this name have weekly options? What is the IV rank? Are catalysts (earnings, FDA, Fed) in the right window? |
| 5. **Structure** | This is the heart of the options-specific work — choose between long calls/puts, vertical spreads, ratio calendars, condors, butterflies based on directional confidence and vol regime |
| 6. Sizing | Greeks-based, not premium-based. Theta budget, vega budget, gamma budget — see [[options-risk-budgeting]] |
| 7. Hedge layer | Long-vol overlay, beta hedges, sector hedges as explicit options positions |

The framework's key insight is that *options are not a substitute for stock at any stage* — they are a different instrument class with their own Greek profile and own portfolio role. A trader who replaces every stock position with a "synthetic" via options has not run the ITPM process; they've just changed instruments without changing the underlying process.

## When to Use Options vs Stock at Each Layer

ITPM treats this as one of the more important real-time decisions:

### Use stock when:
- The view is *purely directional* with high confidence and a long-horizon catalyst (the simpler vehicle is better when complexity adds no value)
- Tax considerations favor long-term holding (long-term capital gains rate preferred over Section 1256 60/40 if held >12 months)
- Liquidity in the underlying options chain is poor (single-name small-cap, EM)
- The trade is being held for non-options reasons (dividend capture, voting rights, share-buyback front-running)
- Position is being held >6 months and the time-value cost of long options exceeds the benefit of leverage

### Use long options (calls/puts) when:
- The view has a defined catalyst window (3-6 months) and asymmetric expected payoff
- Capital efficiency matters — getting equivalent directional exposure with less cash outlay
- A defined-risk position is required (max loss = premium paid)
- The trade is a *tail* expression of the macro view rather than a core position
- See [[long-call]], [[long-put]] for the structures

### Use short options or credit spreads when:
- The view is "this won't happen" rather than "this will happen" (high-probability, low-payoff)
- IV rank is elevated and likely to compress
- The position is being sized as part of an income overlay rather than a directional bet
- The book has a long-vol overlay elsewhere to absorb the tail risk
- See [[short-strangle]], [[iron-condor]], [[credit-spread]]

### Use ratio structures (calendars, ratio spreads) when:
- The view combines both an income component and a directional component with a known catalyst
- The IV term structure has a meaningful slope to exploit
- The trader has the platform support and the book context to manage the shape-shifting Greeks
- This is the canonical ITPM expression — see [[itpm-ratio-calendar-spread]]

### Use options as hedges (long puts, ratio put spreads) when:
- The book has substantial long-equity exposure and explicit drawdown limits
- The hedge is meant to monetise into cash without disturbing the long book
- The premium budget is acceptable as a portfolio cost line
- See [[5-percent-otm-put-overlay]], [[long-vol-overlay]]

### Instrument-selection decision table

The prose above as a single lookup. The choice is driven by *view shape* (directional vs probabilistic), *vol regime*, *horizon*, and *role in the book*:

| Vehicle | Use when | View shape | Vol regime | Book role | Greek signature |
|---|---|---|---|---|---|
| Stock | Long horizon, pure direction, tax/liquidity reasons | Directional, high conviction | Any | Core | Pure delta |
| Long call / put | Defined catalyst window, asymmetric payoff, defined risk | Directional, asymmetric | Low IV preferred | Tail / catalyst | +gamma, +vega, −theta |
| Credit spread / short premium | "This won't happen", high IV rank | Probabilistic | High IV (to compress) | Income overlay | −gamma, −vega, +theta |
| Ratio calendar / ratio spread | Income + direction + term-structure slope | Mixed | Sloped term structure | Primary catalyst | Shape-shifting |
| Long put / ratio put spread (hedge) | Long-equity book with drawdown limits | Tail protection | Buy when cheap | Tail-hedge overlay | +gamma, +vega, −theta |

The unifying rule from the framework: **direction → long options or stock; probability → short premium; income-plus-direction → ratio structures; insurance → long puts sized to a budget.** Each row's Greek signature is what makes the book-level aggregation table (below) add up.

## The Options-Specific Book Architecture

ITPM books that are options-heavy follow a specific architecture:

```
Book = Core Long-Short Equity Layer
     + Options Income Overlay
     + Long-Vol / Tail-Hedge Overlay
     + Tactical Catalyst Trades
```

### Core Long-Short Equity Layer
- 5 longs in favored sectors, 5 shorts in unfavored sectors
- Mostly stock for liquidity and tax-efficiency
- Some positions expressed as deep-ITM calls or LEAPS as stock-replacement

### Options Income Overlay
- Premium-selling structures sized to a [[theta-targeting|theta budget]]
- Canonical structures: 16-delta strangles on SPX, iron condors on liquid index, ratio calendars on single names with views
- Theta budget typically 10-20% of expected monthly P&L
- Diversified across expirations (see [[expiration-laddering]])

### Long-Vol / Tail-Hedge Overlay
- 5% OTM SPX puts, deep-OTM call wings, or VIX call spreads
- Sized to spend 1-3% of NAV per year
- Functions as the "explicit hedge" mandated by ITPM principle 5 (capital preservation)
- See [[5-percent-otm-put-overlay]], [[long-vol-overlay]]

### Tactical Catalyst Trades
- 1-3 ratio calendar spreads or directional debit spreads on names with imminent catalysts
- Sized as 5-10% positions
- The ratio calendar is the dominant structure — see [[itpm-ratio-calendar-spread]]

### Layer-sizing summary

The four layers as a budget. Figures are *illustrative conventions* from the ITPM corpus, not a prescribed allocation or a track record:

| Layer | Typical sizing convention | Primary instrument | Budget basis |
|---|---|---|---|
| Core long-short equity | ~5 longs / ~5 shorts | Stock, deep-ITM calls, LEAPS | Net-delta target |
| Income overlay | Theta ≈ 10-20% of expected monthly P&L | 16-delta strangles, iron condors, ratio calendars | [[theta-targeting\|Theta budget]] |
| Long-vol / tail-hedge overlay | ~1-3% of NAV/year in premium | 5% OTM SPX puts, deep-OTM call wings, VIX call spreads | Premium budget (a cost line) |
| Tactical catalyst | 5-10% per position, 1-3 positions | Ratio calendars, directional debit spreads | Defined-risk per position |

The defining constraint: **the long-vol overlay's premium budget is a non-negotiable cost line, not a P&L target.** When a trader judges that overlay by its standalone (negative) P&L and cuts it, the book silently becomes the short-tail structure the framework exists to prevent — the [[the-theta-trap|theta trap]].

## Greek Aggregation Across the Layers

Each layer contributes to total book Greeks:

| Layer | Delta | Gamma | Vega | Theta |
|---|---|---|---|---|
| Long-short equity | Net long (~+0.3 to +0.6) | ~0 | ~0 | ~0 |
| Income overlay | ~0 (delta-neutral target) | Negative | Negative | Positive |
| Long-vol overlay | Slightly negative | Positive | Positive | Negative |
| Tactical catalyst | Variable | Variable | Variable | Variable |

The book-level objective is roughly:
- **Net delta**: aligned with macro view (positive if bullish, negative if bearish, near zero if neutral)
- **Net gamma**: ideally slightly positive or near zero — net negative gamma is a red flag
- **Net vega**: aligned with vol view; ITPM books typically run slightly long-vega via the overlay
- **Net theta**: positive (the book is paid daily for the income overlay net of long-vol overlay cost)

A book that has accidentally drifted to large net negative gamma or vega is failing the framework — the income overlay has overwhelmed the long-vol overlay and the book is now structurally short tail risk.

## Illustrative Book Walk-Through (Hypothetical)

The following is a qualitative sketch of how the four layers assemble into one book. All Greek directions are illustrative; no specific dollar figures are implied as a track record.

Imagine a trader whose macro view is mildly constructive on US large-cap with compressed implied vol. The book might be built layer by layer:

1. **Core long-short equity** — a handful of longs in favored sectors and shorts in unfavored ones, mostly held as stock for tax and liquidity reasons. This layer contributes the book's intended *net long delta* and almost no option Greeks.
2. **Income overlay** — a small set of delta-neutral premium-selling structures on liquid index products, sized to a [[theta-targeting|theta budget]] and laddered across expirations. This layer adds *positive theta* but *negative gamma and vega*.
3. **Long-vol / tail-hedge overlay** — a continuously-rolled put ladder (or VIX-call spreads) sized to a fixed annual premium budget. This layer *costs* theta but restores *positive vega and gamma*, deliberately offsetting the income overlay's tail exposure.
4. **Tactical catalyst trades** — one or two defined-risk structures (e.g., a ratio calendar) on names with a known catalyst, each a small percentage of the book.

The intended book-level profile after assembly: net delta aligned with the macro view, net theta slightly positive (income overlay net of overlay cost), and net vega slightly long via the hedge. The point of the walk-through is the *interaction*: layer 2 alone would be a short-tail book; layer 3 is what converts it into something that can survive a shock. If the trader were ever tempted to cut layer 3 because it bleeds in calm regimes, they would silently turn the whole book into the very short-vol structure the framework forbids — the exact mechanism catalogued in [[hedging-program-failure-modes]].

The Greek *signs* (not magnitudes — all illustrative) make the interaction explicit:

| Layer | Delta | Gamma | Vega | Theta | What it contributes |
|---|---|---|---|---|---|
| 1. Core long-short equity | + (macro-aligned) | ~0 | ~0 | ~0 | The book's intended directional tilt |
| 2. Income overlay | ~0 | − | − | + | Carry / income, but *short tail* |
| 3. Long-vol / tail hedge | slightly − | + | + | − | Converts the book from short-tail to survivable |
| 4. Tactical catalyst | variable | variable | variable | variable | View-specific tilt |
| **Net (target)** | **macro-aligned** | **≥ 0** | **≥ 0** | **+** | A paid-to-wait book that survives a shock |

Reading the table top-to-bottom shows the design: layer 2's negative gamma/vega is *deliberately* offset by layer 3's positive gamma/vega, so the net book collects theta (layer 2) while keeping non-negative gamma and vega (layer 3). Remove layer 3 and the "Net" row inverts to negative gamma/vega — the short-tail book the framework forbids.

## The Role of Options as Primary vs Hedge Instruments

ITPM makes an explicit distinction:

### Options as Primary Instruments
When options are the *preferred expression* of a view (catalyst trades, ratio calendars, conviction long-vol bets), they are sized as primary positions with a 5-10% capital allocation, P&L attributed at the position level, and managed as the central asset.

### Options as Hedge Instruments
When options are *insurance* on the rest of the book (5% OTM put overlay, sector ETF puts, beta hedges), they are sized to a **premium budget** rather than a P&L expectation. Their negative expected return is acceptable because they reduce drawdown variance at the book level.

The most common error ITPM corrects in retail traders: treating *every* options position as a primary instrument and judging each by its standalone P&L. This causes traders to abandon hedges precisely when the hedge is producing the (negative) standalone P&L it was bought to produce.

## Discipline Specific to Options Books

The ITPM principles applied through an options lens:

1. **Asymmetric R/R holds at the position level** — every options position should target ≥3:1 reward to risk. This is harder for credit-side trades, which is why ITPM caps the credit-overlay at a fraction of the book.
2. **Pre-budgeted Greeks** — net vega, net theta, max gamma, max single-expiration concentration all set before market open.
3. **Top-down still applies** — options structures are the *output* of the macro/sector/name process, not the input. Never put on a structure first and reverse-engineer the thesis.
4. **Institutional infrastructure** — portfolio margin, scenario analysis tools, Greeks aggregation. See [[options-portfolio-construction]].
5. **Capital preservation** — the long-vol overlay is non-negotiable. A short-vol-only options book violates the framework regardless of returns.

### Pre-Open Greeks Checklist

A daily discipline distilled from the principles above:

- [ ] **Net delta** is within the band implied by the current macro view.
- [ ] **Net gamma** is positive or near zero — large net negative gamma is a stop-and-fix signal.
- [ ] **Net vega** is non-negative (the overlay has not been overwhelmed by the income layer).
- [ ] **Net theta** is positive but *funded by* a still-intact long-vol overlay, not by removing it.
- [ ] **No single expiration** concentrates more than the pre-set share of risk (avoid cliff risk).
- [ ] **No single name** exceeds its notional cap.
- [ ] Any position inside ~21 DTE is queued to roll or close; any position whose thesis is dead is exited regardless of price.

If any box fails, the fix is made before new risk is added — never the other way around.

## Distinction from Tastytrade-Style Premium-Selling

The [[tastytrade|tastytrade]] doctrine (45 DTE, 50% profit-take, mechanical strangles and condors) is a *single layer* of an ITPM-style options book — specifically the income overlay. Critics from the ITPM camp argue that tastytrade's omission of an explicit long-vol overlay leaves the book structurally short tail risk and exposed to occasional catastrophic drawdowns that erase years of premium income. ITPM's options portfolio approach can be thought of as "tastytrade's premium-selling discipline plus an explicit long-vol hedge plus a top-down view-driven directional layer." See [[tastytrade-mechanics]] and [[tastytrade-spx-research]].

## Common Failure Modes Specific to Options Books

From [[failure-modes]] and [[hedging-program-failure-modes]]:

| Failure mode | Mechanism | Pre-open checklist box that catches it | Defense |
|---|---|---|---|
| Over-reliance on theta | Net + theta achieved by being short tail | Net gamma / net vega box | Keep gamma/vega ≥ 0 via overlay |
| Neglected hedge layer | Overlay cut because it bleeds in calm | Net vega box (overlay intact) | Treat overlay as a non-negotiable cost line |
| Greek drift | Delta-neutral entries stack into net delta/gamma | Net delta box | Book-level [[portfolio-greeks-aggregation\|aggregation]], not per-position |
| Expiration pile-up | Liquidity convenience concentrates one monthly | Single-expiration concentration box | [[expiration-laddering]] |
| IV-rank chasing | Selling premium because IV high, no view | (Upstream: top-down view first) | Require a fundamental thesis before any sale |

The detailed list:

1. **Over-reliance on theta** — running net positive theta across a book is good only if the gamma and vega are also managed; theta-rich books are short tail risk by definition.
2. **Neglected hedge layer** — when the overlay produces drag in calm regimes, traders cut it. When the shock comes, they have no hedge. ITPM's discipline addresses this directly.
3. **Greek drift** — without book-level monitoring, the option positions individually delta-neutral at entry can stack into large net delta or gamma over weeks.
4. **Expiration pile-up** — concentrating positions on one monthly because of liquidity convenience creates cliff risk.
5. **IV-rank chasing** — selling premium because IV rank is high without a fundamental view leads to averaged-up losses when the IV rank is high *because* a real shock is brewing.

## How This Connects to the Rest of the Wiki

This page is the options-instrument view of one layer of a larger stack. Above it sits the [[itpm-framework|ITPM framework]] (the seven-stage process) and the [[itpm-trading-philosophy|philosophy]] (the *why*); the whole set is indexed by [[itpm-playbook]]. Beside it sits [[options-portfolio-construction]], the general book-mechanics layer that the ITPM frame is a specialisation of, and [[options-risk-budgeting]], the Greek-budget discipline that stages 6 here depend on. The hedge layer's characteristic failures are catalogued in [[hedging-program-failure-modes]], and the general strategy-failure context is [[failure-modes]]. The non-negotiable long-vol leg is detailed in [[long-vol-overlay]] and [[5-percent-otm-put-overlay]]; the structural alternative of building the whole book tail-protected from the start is the [[barbell-portfolio]]. The discipline that decides when a sleeve should be retired or restructured is [[when-to-retire-a-strategy]], and the research discipline that keeps any quantified rule (theta budgets, IV-rank triggers) from being [[curve-fitting|curve-fit]] applies here as everywhere.

## Related

- [[itpm-framework]] — parent methodology
- [[itpm-trade-construction-playbook]] — single-trade construction work
- [[options-portfolio-construction]] — practical book mechanics
- [[options-risk-budgeting]] — Greek-budget discipline
- [[itpm-ratio-calendar-spread]] — canonical primary-instrument structure
- [[5-percent-otm-put-overlay]] — canonical hedge-instrument structure
- [[long-vol-overlay]] — the non-negotiable layer
- [[long-vol-vs-short-vol]] — philosophical context
- [[barbell-portfolio]] — Taleb-Spitznagel's parallel approach
- [[anton-kreil]], [[itpm]] — the source institution
- [[tastytrade-mechanics]], [[tastytrade-spx-research]] — the contrasted retail-quant approach
- [[itpm-trading-philosophy]] — the worldview layer above this page
- [[itpm-playbook]] — the umbrella index for all ITPM material
- [[hedging-program-failure-modes]] — how the hedge layer here fails in practice
- [[failure-modes]] — the broader strategy-failure taxonomy
- [[when-to-retire-a-strategy]] — the kill discipline for a book sleeve
- [[curve-fitting]] — keeping quantified rules from being fit to the sample
- [[the-theta-trap]] — the canonical failure of an income layer run naked
- [[expiration-laddering]] — diversifying expirations to avoid cliff risk
- [[theta-targeting]] — the income-layer budget basis
- [[strategy-monitoring]] — the live dashboard the pre-open checklist feeds

## Sources

- ITPM curriculum (Professional Options Trading Masterclass, Professional Trading Masterclass).
- Anton Kreil interviews and lectures (2014-2024).
- [[itpm-master-compounding]], [[itpm-god-like-trader-status]] — internal ITPM source documents covering ratio calendar deployment.
- McMillan, *Options as a Strategic Investment* (5th ed.) — supports the structural mechanics.
- Goldman Sachs equity derivatives research on book-level Greek management.
