---
title: "Earnings Volatility"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, volatility, earnings, derivatives, stocks]
aliases: ["Earnings IV", "Earnings Vol Cycle"]
domain: [derivatives, market-microstructure]
prerequisites: ["[[implied-volatility]]", "[[options-greeks]]", "[[vega]]"]
difficulty: intermediate
related: ["[[implied-volatility]]", "[[iv-crush]]", "[[implied-earnings-move]]", "[[earnings-volatility-trading]]", "[[earnings-iv-crush]]", "[[volatility-term-structure]]", "[[volatility-skew]]", "[[volatility-regime]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[earnings-calendar]]", "[[options-portfolio-construction]]", "[[long-vol-vs-short-vol]]", "[[variance-risk-premium]]"]
---

Earnings volatility is the cyclical pattern of [[implied-volatility|implied volatility]] inflation and collapse that wraps every scheduled corporate earnings announcement. It is one of the most predictable, well-documented features of the single-name [[options]] market: front-cycle IV ramps for days or weeks before the print, peaks in the final hour of the regular session ahead of the report, and crushes 30–50% in the seconds after the headline regardless of the direction of the stock move. The cycle is not an anomaly — it is the rational price of a binary information event — but the *magnitude* and *timing* of the ramp and crush create persistent trading opportunities for both [[short-volatility|short-vol]] and [[long-volatility|long-vol]] participants.

## Overview

A scheduled earnings release is a planned discontinuity in the price-discovery process. For minutes, the market does not know the firm's revenue, EPS, guidance, or qualitative tone. Once the print hits the tape (and especially after the conference call), uncertainty resolves and the realised post-event distribution narrows sharply. Options pricing reflects this in three connected phenomena:

1. **Pre-earnings IV ramp** — the implied volatility on the contracts that span the report rises in the days and hours leading up to it, driven by event-uncertainty hedging and speculative demand.
2. **Implied earnings move** — the market quotes a one-standard-deviation move embedded in the front-expiry [[straddle]] price; on liquid single names this is roughly *1.0 × ATM straddle / spot*. See [[implied-earnings-move]].
3. **Post-earnings IV crush** — once the headline prints, the front-cycle IV collapses — typically 30–50% in absolute IV points, sometimes more on names where the pre-event ramp was extreme. See [[iv-crush]].

The cycle is the canonical reason that *long calls and long puts bought before earnings frequently lose money even when the directional call is correct*: the IV crush erases extrinsic value faster than the directional move adds it. Conversely, [[options-premium-selling|short-premium]] structures harvest that crush — the entire architecture of the [[earnings-iv-crush]] strategy is built on it.

This page is the **conceptual** reference for the cycle. For the systematic *trading* application, see [[earnings-volatility-trading]] and [[earnings-iv-crush]]. For the broader vol-regime context, see [[volatility-regime]] and [[volatility-term-structure]].

## How It Works

### The pre-earnings IV ramp

In the weeks before an earnings release, two effects raise IV on the contracts that *span* the report (and only those contracts; see [[volatility-term-structure]] below):

- **Hedging demand** — institutional holders of the underlying buy puts to hedge gap risk over the report. Dealers absorb that supply and re-mark IV upward to clear the imbalance.
- **Speculative demand** — retail and discretionary traders buy short-dated calls and puts as binary-event lottery tickets, anchoring on prior outsized prints.

The ramp is not uniform across the surface. It is concentrated in the **front weekly or front monthly cycle** that contains the announcement date, while back-month IV stays comparatively stable. The result is a steeply *inverted* [[volatility-term-structure|term structure]] in the days before the report: front-week IV at 80%, next-month IV at 35%, three-months-out at 28%. This inversion is itself a useful detection signal — if the term structure of an option chain is inverted by more than ~10 vol points, an event is priced in.

For a [[options-premium-selling|short-premium book]] holding the front cycle through earnings, the ramp is a **vega headwind**: the position bleeds mark-to-market even as it accrues theta, because IV expansion outpaces decay. This is the empirical backbone of the rule that *pre-earnings theta is unrealised income, not collected income* (see [[theta-targeting]]).

### The implied earnings move

The market's consensus view of *how much the stock will move on the announcement* is encoded in the [[straddle|ATM straddle]] price for the first expiration after the report. The standard formula is:

```
Implied earnings move ≈ ATM straddle price / spot
```

A more precise approximation that adjusts for the price of the back-month vol embedded in the same contracts is:

```
Implied move ≈ 0.85 × ATM straddle / spot
```

(The 0.85 multiplier strips out the non-event vol baked into the contract; see Augustin, Brenner & Subrahmanyam (2014) for the academic derivation.) Brokers and platforms vary in which formula they display. In practice, traders use the implied move as a **strike-selection anchor**: short [[short-strangle|strangles]] are typically placed at strikes ≥ 1.0 × implied move from spot; defined-risk [[iron-condor|iron condors]] place wings 1.5–2.0× the implied move out.

### The post-earnings IV crush

Within seconds of the headline, IV on the front-cycle contracts collapses. Typical magnitudes on liquid US single names:

| Name characteristic | Typical front-cycle IV crush | Notes |
|---|---|---|
| Mega-cap, well-covered (AAPL, MSFT) | -25% to -40% absolute | Large analyst coverage, smaller surprise distribution |
| High-flyer growth (NFLX, NVDA) | -40% to -60% absolute | Larger pre-event ramps, larger crushes |
| Small-cap with thin analyst coverage | -50% to -70% absolute | Most surprise distribution, biggest ramp and crush |
| Already inverted into the print | crush extends back into the back month for a session | Contagion across DTE buckets |

The crush is largely independent of the *direction* of the stock move. A name can gap +8%, gap -12%, or stay flat — front-week IV crushes in all three cases because the *information* that drove the ramp has resolved. This is the crucial structural observation for the [[earnings-iv-crush]] short-vol trade: the crush is not contingent on the directional outcome.

What is *not* independent of direction:

- The **realised P&L** of an unhedged short straddle, which depends on whether the stock moves more or less than the implied move.
- The **gamma scalping** opportunity for a long-vol holder, which is a function of realised path.
- The **skew dynamics** post-print — left-tail puts often retain elevated IV after the announcement if the report was negative, even as ATM IV crushes.

## Examples / Empirical Evidence

### Augustin, Brenner & Subrahmanyam (2014)

The cleanest academic study of earnings-event implied moves vs realised moves. Across thousands of US earnings announcements 1996–2010, the average **implied move exceeds the average realised move by 5–20%** depending on regime and liquidity tier. The discrepancy is the empirical foundation of the [[earnings-iv-crush]] systematic short-vol trade. The paper also documents that the *cross-section* of the spread — which names have the richest implied-vs-realised premium — is not stable; mega-cap tech has tightened over time as more capital piled into the trade.

### tastytrade earnings research (multi-year studies)

[[tastytrade]]'s public research consistently finds that, on a portfolio basis across the S&P 500, selling 1-SD short strangles into liquid single-name earnings and closing the next morning produces a **positive expected value with 65–75% win rate** and a long left tail. The same studies caveat the result with the size of the worst-case losers — a single NFLX-style outlier print can erase 20+ winning trades. The implication for sizing is well-developed in [[earnings-volatility-trading]].

### NFLX 2022-04-19 — the canonical short-vol blow-up

Front-week IV ramped from ~50% to ~115% into the close on 2022-04-19. ATM straddle priced an ~8% implied move. The stock gapped **-35%** on the print (subscriber loss revelation). Short-strangle sellers at 1-SD strikes saw the put leg blow through the wing on a defined-risk condor or beyond the strike on a naked strangle by a multiple of the credit. A full year of disciplined earnings-vol harvesting could be erased on this single name. See [[failure-modes]].

### NVDA 2024 cycle

Through 2024, NVDA repeatedly printed implied moves of 9–11% and *realised* moves at or beyond the implied move on more than half of cycles, despite richer-than-average premium. This is an example of the [[earnings-iv-crush]] edge being *underpriced relative to actual surprise distribution* on a single name during a structural regime — AI capex revisions made the realised distribution wider than any backward-looking premium model would have anticipated.

### Term-structure inversion as a leading indicator

A practitioner heuristic: when an option chain is inverted by 10+ vol points front vs back, an event is priced. Confirming with the [[earnings-calendar|earnings calendar]] is mandatory before assuming it's an earnings ramp — biotech approvals, FDA decisions, and litigation events can produce identical surface signatures (see [[binary-event-trading]]).

## Implications for Strategy / Common Mistakes

### Implications

- **Premium-selling income books** should explicitly decide whether to *include* or *exclude* earnings exposure. Including it captures the IV-crush premium but adds a fat-left-tail risk that is poorly diversified. Excluding it forfeits the premium and forces the book to find decay elsewhere. ITPM-style and [[tastytrade]]-style practitioners typically split: the *index-options* core book excludes single-name earnings, while a sized *single-name event-vol* sleeve harvests the crush within strict per-position and concentration limits. See [[options-portfolio-construction]] and [[diversification-in-options]].
- **Theta-targeted books** must not count pre-earnings theta as collected income. The full decay only realises in the post-print IV crush. A position carried through the ramp is a vega bet, not a theta bet. See [[theta-targeting]].
- **DTE laddering** should explicitly span or avoid earnings dates depending on the desired exposure. A 45 DTE [[iron-condor]] that crosses an earnings date is a different product from one that does not.
- **Strike selection** anchors on the implied move, not on a fixed delta. A 16-delta strike that sits *inside* the implied move offers far less margin than the same delta on a non-event week.

### Common mistakes

- **Buying calls/puts before earnings hoping for a directional pop**. The IV crush typically erases gains from a correct directional call unless the move is *at least* the implied move. Net expectancy is negative across most names after costs.
- **Selling naked strangles at 1-SD strikes without sizing for the tail**. Over enough cycles a 3-SD or 4-SD print arrives and the position loses many cycles of edge in a single trade.
- **Treating earnings vol as theta**. The decay component is small relative to the vega exposure; the trade is a short-vol trade dressed up as an income trade. Sizing it in the [[theta-targeting|theta-targeted]] framework alone underestimates the true risk.
- **Over-concentration in one sector**. A "diversified" earnings-vol book that holds short-vol on AAPL, MSFT, GOOG, META, NVDA in the same week is one factor bet. See [[diversification-in-options]].
- **Holding through the call**, not just the print. The conference call (typically 30–60 minutes after the headline) often produces a second leg of realised move and IV repricing. Many practitioners exit at the print or wait until the next morning's open after the call has fully digested.
- **Ignoring [[volatility-skew|skew]]**. A name with a heavy put skew is signalling a left-tail concern; the symmetric short strangle is silently asymmetric in risk.

## Related

- [[implied-volatility]] — the underlying input
- [[implied-earnings-move]] — how the cycle is quantified
- [[iv-crush]] — the post-event collapse phenomenon in isolation
- [[earnings-volatility-trading]] — the broader strategy class (long-vol and short-vol flavours)
- [[earnings-iv-crush]] — the focused short-vol systematic trade
- [[volatility-term-structure]] — how the cycle distorts the term structure
- [[volatility-skew]] — cross-strike pricing during the ramp
- [[theta-targeting]] — why pre-earnings theta is unrealised income
- [[vega-budgeting]] — how to size single-name event vol within a book vega budget
- [[earnings-calendar]] — the calendar that drives entry timing
- [[options-portfolio-construction]] — where event vol fits in a multi-strategy book
- [[diversification-in-options]] — why single-name event-vol concentration matters
- [[long-vol-vs-short-vol]] — the strategic frame of taking either side of the cycle
- [[variance-risk-premium]] — the structural edge underlying short event vol
- [[failure-modes]] — historical blow-ups that calibrate sizing

## Sources

- Augustin, P., Brenner, M., & Subrahmanyam, M. (2014) *Informed Options Trading prior to Takeover Announcements: Insider Trading?* and related work on pre-event implied moves.
- [[tastytrade]] — multi-year published research on earnings-vol short-premium expected value and win rate.
- [[book-option-volatility-and-pricing]] — Natenberg's treatment of event vol and surface dynamics.
- [[itpm-trading-philosophy]] — practitioner framework for sizing event-vol within a multi-strategy options book.
