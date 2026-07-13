---
title: "Earnings Announcement"
type: concept
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [stocks, options, earnings, derivatives, behavioral-finance, volatility]
aliases: ["Earnings", "Earnings Event", "Earnings Date", "Earnings Release"]
related: ["[[earnings-volatility]]", "[[earnings-iv-crush]]", "[[earnings-volatility-trading]]", "[[earnings-calendar]]", "[[implied-earnings-move]]", "[[implied-volatility]]", "[[iv-crush]]", "[[options-risk-budgeting]]", "[[options-portfolio-construction]]", "[[stress-test]]", "[[scenario-analysis]]", "[[volatility-term-structure]]", "[[volatility-skew]]", "[[straddle]]", "[[strike-selection]]", "[[moneyness-selection]]", "[[delta]]", "[[post-earnings-announcement-drift]]", "[[earnings-per-share]]", "[[earnings-revision]]", "[[news-and-sentiment-sources]]"]
domain: [market-microstructure, behavioral-finance]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]"]
difficulty: intermediate
---

An earnings announcement is the scheduled release of a company's quarterly or annual financial results — revenue, EPS, guidance, and accompanying commentary — that resolves a substantial chunk of information uncertainty in a single discrete moment. For options markets the announcement is a *binary information event*: a planned discontinuity in the underlying's price-discovery process that produces predictable pre-event [[implied-volatility|IV]] inflation, a discrete spot move at the print, and post-event IV collapse. For [[options-portfolio-construction|options books]], scheduled earnings concentrate tail-event risk in a known calendar of dates, and a coherent [[options-risk-budgeting|risk budget]] must explicitly account for them.

This page treats the **event itself** — its mechanics, scheduling, market dynamics, and risk-budget implications. For the cyclical IV behaviour wrapping the event see [[earnings-volatility]]. For trading strategies that exploit the cycle see [[earnings-volatility-trading]] and [[earnings-iv-crush]].

## Overview

Public US companies are required by SEC Regulation FD to release material earnings information through a Form 8-K filing on a publicly disclosed schedule. Most large-caps announce on a near-quarterly cadence (every 13 weeks), with the exact dates falling roughly 2-7 weeks after each fiscal-quarter close. The announcement is *the* canonical scheduled event in single-name equities — known in advance, dense in information, and reliably followed by an outsized stock move.

Three properties make earnings announcements operationally distinct from other information arrivals:

1. **Scheduled timing.** The announcement date is published days or weeks in advance. Unlike Fed decisions or geopolitical surprises, the *when* is known; only the *what* is uncertain.
2. **Concentrated information content.** A single 8-K filing contains revenue, EPS, guidance, and qualitative commentary that collectively often move the stock 5-10% (sometimes >20% on tech and biotech). The conditional volatility on the announcement window is typically 3-6× the unconditional daily volatility.
3. **Asymmetric impact across the option surface.** Front-week options that *span* the announcement absorb a large IV ramp; back-month options barely move. The result is a deeply *inverted* [[volatility-term-structure|term structure]] in the days before the print — an unmistakable surface signal that an event is priced in.

Because the timing is scheduled, the event can be *budgeted*. A trader who finds themselves accidentally short volatility into a high-uncertainty earnings print has failed at risk budgeting; the same exposure is acceptable when entered intentionally with a sized vega budget and an understood scenario range.

## Definition / Mechanics

### Scheduled vs unscheduled

| Type | Examples | Frequency | Vol response |
|---|---|---|---|
| **Scheduled earnings** | Quarterly 10-Q, annual 10-K, accompanying 8-K | ~4 per year per company | Front-cycle IV ramp + post-print crush |
| **Pre-announcement** | Pre-release of partial results, "fireside chat" comments | Sporadic | Mid-event vol expansion; harder to time |
| **Earnings warning** | Negative pre-announcement (typically days before scheduled date) | Rare; legally constrained | Spot drop + IV spike *before* the scheduled date |
| **Unscheduled material announcement** | M&A, FDA, lawsuit, restatement | Rare | Often larger spot move than scheduled earnings; no IV ramp pre-event |

This page focuses on **scheduled** announcements; unscheduled material events follow different microstructure (no pre-event IV ramp because the timing was unknown) and are treated separately under their own news-driven frameworks.

### BMO vs AMC

Most US companies announce in one of two windows:

- **BMO** — *Before Market Open*, typically between 6:00 and 9:00 ET. Stock price reacts in pre-market and gaps at the 9:30 open.
- **AMC** — *After Market Close*, typically between 16:01 and 18:00 ET. Stock price reacts in post-market and gaps at the next morning's open.

A small minority announce *during* the regular session (rare, often considered poor practice because of the disorderly tape it produces) or *intraday halted* (used during major surprises to allow orderly digestion).

The BMO/AMC choice matters operationally:

- BMO releases produce *opening gaps*; the implied earnings move is realised at the 9:30 open with substantial overnight risk for any holder. Liquid trading begins immediately.
- AMC releases produce *post-market moves* in thinly-traded sessions, then a *gap to the next morning open*. The implied move is realised over a longer window with lower realised liquidity in between. Several large-caps (AAPL, AMZN, GOOG, META, MSFT, NVDA) typically announce AMC.

For [[options-risk-budgeting|options risk-budgeting]], AMC events have higher operational risk because the trader cannot react during the immediate post-print window with normal liquidity.

### The pre-event IV ramp

In the days before the announcement, IV on the **front weekly or front monthly cycle that contains the announcement** rises systematically while back-month IV stays roughly stable. Two effects drive the ramp:

- **Hedging demand.** Institutional holders buy front-cycle puts to hedge gap risk over the announcement. Dealers absorb the supply and re-mark IV upward.
- **Speculative demand.** Retail and short-term participants buy front-cycle straddles, calls, and puts as binary-event tickets, anchoring on prior outsized prints.

The cycle produces a sharply inverted term structure. A typical example for a liquid large-cap reporting in 2 days:

- Front-week IV: 80%
- Next-week IV: 38%
- Front-month IV: 35%
- Three-month IV: 30%

The ~50-vol-point inversion is the empirical fingerprint of an upcoming binary event. The same shape appears around FDA decisions and other scheduled binary catalysts. See [[volatility-term-structure]].

### The implied earnings move

The market's consensus view of *how much the stock will move on the announcement* is encoded in the front-cycle ATM straddle:

```
Implied earnings move ≈ (ATM call + ATM put) / spot
```

A more precise approximation — see [[implied-earnings-move]] — backs out the post-event-only component by netting the *ex-earnings* IV (interpolated from cycles that do not span the event) embedded in the same contracts.

For a stock at $100 with the front-week 100-strike straddle priced at $7, the implied move is ~7%. The market is pricing roughly a 1-standard-deviation move of $7 over the announcement window. A $14 move is roughly a 2-sigma realisation; anything beyond is in the rare tail.

### The post-event IV crush

Once the print hits the tape and uncertainty resolves, front-cycle IV collapses. Typical magnitudes:

- Routine crush: 30-50% relative drop in front-cycle IV in the first 5 minutes after the print.
- Extreme crush: 60-80% drop on names where pre-event IV had risen most aggressively.

The crush happens regardless of *whether the stock moves up or down* — both directions reduce uncertainty, which was the source of the IV premium. This is the empirical reason that *long calls and long puts bought before earnings frequently lose money even when the directional call is correct*: extrinsic value evaporates faster than directional move adds it. See [[earnings-iv-crush]].

### Beat / miss / inline frequencies

Aggregate statistics across S&P 500 reports (rough decade-average figures):

- Companies that *beat* consensus EPS: 70-80%
- Companies that *meet* consensus EPS: 5-10%
- Companies that *miss* consensus EPS: 15-25%

The high beat rate is well-documented evidence of *guidance management* — companies guide slightly below realistic expectations so they can beat at the print. See [[earnings-management]]. The actual *information content* therefore lives less in the EPS number than in revenue, guidance, and qualitative commentary on the call.

The directional reaction does not map cleanly to beat/miss. Names regularly *beat* and trade down (because guidance disappointed), or *miss* and trade up (because guidance was reassuring). Empirical evidence: roughly 60% of beats produce positive reactions and 40% are flat-to-negative; similarly noisy in reverse. The market is pricing the *full information bundle*, not the EPS surprise alone.

### Post-earnings announcement drift (PEAD)

A robust empirical pattern documented since Ball & Brown (1968): stocks that beat continue to drift up for several weeks after the announcement; stocks that miss continue to drift down. The effect is roughly 1-3% in the weeks following the print, after controlling for the immediate move. The drift is one of the most replicated [[anomalies|anomalies]] in the empirical asset-pricing literature and persists despite being widely known.

Augustin, Brenner, and Subrahmanyam (2014, "Informed options trading prior to takeover announcements") show that informed-trading evidence around earnings is mixed: while options-volume signals do predict announcement returns, the pattern is much weaker for scheduled earnings than for unscheduled M&A events, consistent with the view that scheduled earnings dispersion is harder to obtain inside-information edge on.

For options books, PEAD provides a (small) directional alpha in the front weeks after the announcement — typically captured by stock positions rather than option positions because the IV crush has already removed the option premium. It is *not* a pre-event signal.

## Methodology / How To Apply

### Step 1 — Identify earnings events on the book

For every position in the book, check whether the underlying has an earnings event before the position's expiration. Sources:

- **Broker calendars** ([[interactive-brokers|IBKR]], [[thinkorswim]]) — flag confirmed dates.
- **[[earnings-whispers]]**, **Zacks**, **Estimize** — third-party calendars; cover unconfirmed dates and consensus expectations.
- **Company IR pages** — most reliable source for confirmed dates and BMO/AMC.

Confirm the date, BMO/AMC, and whether the event is *before or after* each option position's expiration. Options expiring before the event have no event risk; options that span the event do.

### Step 2 — Quantify event exposure per position

For each position spanning an earnings event:

```
event vega exposure  = position vega × (front-cycle IV − ex-earnings IV)
event spot exposure  = position delta × implied earnings move × spot
event scenario loss  = book P&L re-priced at (spot move = ±2 × implied move, IV crush = -50%)
```

The third number is the relevant one for [[options-risk-budgeting|risk budgeting]]: the worst-case scenario is a 2-sigma move *plus* the IV crush, which is the canonical earnings disaster for short-premium positions.

### Step 3 — Budget the event in advance

A coherent options book pre-allocates risk to known earnings events in the same way it pre-allocates [[vega-budgeting|vega]] and [[theta-targeting|theta]] more generally:

- **Maximum concurrent earnings vega.** Cap the total vega exposure across all simultaneously-running earnings events at, e.g., 25% of total book vega budget. A book that is short vega across 8 different earnings events in the same week is one trade, not eight.
- **Maximum single-name earnings scenario loss.** Cap the worst-case scenario loss for any single earnings event at, e.g., 3% of NAV. No single name's print should be able to drive a meaningful drawdown alone.
- **Sector concentration.** All-tech-earnings weeks (last week of January, last week of April, etc.) cluster correlation. Treat them as a single beta-weighted bet; cap accordingly.

### Step 4 — Run scenario grids around each event

For each earnings event ≤ 5 days out, run an event-specific [[scenario-analysis|scenario grid]]:

- Spot axis: -2× / -1× / 0 / +1× / +2× the implied earnings move.
- IV axis: -50% / -25% / 0 (parallel crush of front cycle).
- Time: instantaneous (the print is a discontinuity; multi-day decay is irrelevant).

The output cells tell the trader the conditional P&L under each plausible reaction. Compare the worst cell to the event's allocated scenario budget; if it exceeds, cut size or hedge.

### Step 5 — Decide hold vs close vs hedge

For each event-spanning position, three options:

- **Close before the event.** Captures the IV ramp's accrued vega P&L; eliminates event risk. Standard for short-premium books that did not enter the event intentionally.
- **Hedge before the event.** Add an offsetting long-vol or long-gamma overlay (front-cycle long straddle or bear put spread) sized so the worst-cell scenario fits the event budget.
- **Hold through.** Keep the position unhedged. Only sensible when the position was entered specifically to harvest the IV crush ([[earnings-iv-crush]]) and the size has been pre-budgeted for the event.

Default for every other case: close or hedge before the event. Holding a position through earnings *without intent* is one of the most reliable ways for a short-premium book to take an outsized loss.

### Decision matrix — what to do with an event-spanning position

| Position type | Pre-event posture | Recommended action | Rationale |
|---|---|---|---|
| Short premium, *unintended* event exposure | Short vega, short gamma | **Close before print** | Captures accrued IV-ramp P&L; eliminates the -2σ × crush tail (see [[iv-crush]]) |
| Short premium, *intended* IV-crush harvest | Short vega, sized to event budget | **Hold through** | This is the trade; the crush is the alpha source ([[earnings-iv-crush]]) |
| Long premium ([[straddle]]/strangle) bought for the move | Long vega, long gamma | **Hold only if directional edge > full premium** | [[iv-crush]] removes extrinsic regardless of direction |
| Directional debit spread spanning the event | Net long delta, modest vega | **Hold if conviction high; spread caps vega bleed** | Defined-risk; less crush exposure than naked long |
| Any position with worst-cell scenario > event budget | Any | **Cut size or add tail hedge** | Hard budget rule overrides directional view |
| No position; tempted to initiate pre-print | n/a | **Wait until after crush** unless harvesting ramp | Fresh entry adds event risk to a book already carrying it |

### Event-vol concepts at a glance

| Concept | What it measures | Page |
|---|---|---|
| Implied earnings move | 1σ move priced into the front-cycle straddle | [[implied-earnings-move]] |
| Pre-event IV ramp | Systematic front-cycle [[implied-volatility|IV]] inflation before the print | [[earnings-volatility]] |
| Post-event IV crush | Collapse of front-cycle IV once uncertainty resolves | [[iv-crush]] / [[earnings-iv-crush]] |
| Term-structure inversion | Front-cycle IV > back-month IV — the surface fingerprint of an event | [[volatility-term-structure]] |
| PEAD | Post-print directional drift in the realised return direction | [[post-earnings-announcement-drift]] |

## Worked Example

A trader runs a $250k options book. On Monday morning the calendar shows three earnings events scheduled for the coming week:

- **NVDA** (Wednesday AMC) — front-week IV 95%, ex-earnings IV 50%, implied move 9%.
- **AAPL** (Thursday AMC) — front-week IV 55%, ex-earnings IV 28%, implied move 4.5%.
- **TSLA** (Wednesday AMC, same session as NVDA) — front-week IV 85%, ex-earnings IV 60%, implied move 8%.

**Existing book exposure**:

- 3x NVDA short strangles, 30 DTE, 16-delta wings: -$280 vega each = -$840 total event vega.
- 2x AAPL short put credit spreads, 30 DTE: -$95 vega each = -$190 total event vega.
- No TSLA position.

**Event scenario analysis** (run for each):

- NVDA: book P&L at -2σ event move (-18%) with 50% IV crush = **-$8,400** (3.4% of NAV).
- AAPL: book P&L at -2σ event move (-9%) with 50% IV crush = **-$2,200** (0.9% of NAV).
- Combined NVDA + AAPL on consecutive days: -$10,600 if both move -2σ.

**Budget check**: the trader's policy is max 3% of NAV per single event. NVDA is *at* the limit; AAPL is well inside. The combined exposure (4.3% of NAV across two events on consecutive days) is acceptable but stretched.

**Decision**: hold AAPL through; partially de-risk NVDA. Specifically, close 1 of the 3 NVDA strangles and replace with a long NVDA front-week put as a tail hedge. This reduces NVDA scenario loss to ~$5,000 and brings combined two-event exposure to ~3% of NAV.

**TSLA**: no position; do not initiate one Monday-Wednesday because the IV ramp is already priced in and a fresh short would be *adding* event risk to a book that already has NVDA and AAPL events that week. Wait until after the prints if a TSLA short-vol thesis is desired post-crush.

This is the full operational loop: identify, quantify, scenario-test, budget, act.

## Limitations / Common Pitfalls

1. **Treating earnings as priced-in.** The market prices a *consensus* expectation; the realised move regularly exceeds the implied. A 9% implied move on NVDA is the 1σ band; 18% moves happen multiple times per year on volatile names.
2. **Ignoring AMC liquidity gaps.** The post-print window for AMC announcers (16:01 ET to next-day open) has thin liquidity and 5-10× normal spreads. Hedging in this window is operationally costly.
3. **Confusing implied move with maximum move.** The implied move is roughly 1σ. Approximately 32% of prints will exceed 1σ; ~5% will exceed 2σ. Sizing for the implied move alone is sizing for 1σ, not for the 95% case.
4. **Overlooking pre-announcement leaks.** Earnings warnings and unintentional disclosures occasionally produce material moves *before* the scheduled date. A position sized for "no event before Wednesday" can take a Monday gap.
5. **Counting earnings vega as ordinary vega.** Earnings vega is *event vega* — its decay profile is concentrated at one moment, not spread over time. A book that sums event and non-event vega and treats the total as comparable misallocates risk.
6. **Concentrated sector clusters.** Tech earnings weeks (Jan-end, Apr-end, Jul-end, Oct-end) put 5-10 mega-cap announcements within 5 days. Sector beta dominates; the book may have 10× the apparent concentration for that week.
7. **Mispricing skew on event names.** Front-cycle skew on event names is materially steeper than non-event names, especially on biotech/binary-event names. A skew-aware stress test is required; parallel IV shocks understate the put-side scenario loss.
8. **Forgetting that the IV crush is bidirectional.** Both up and down moves crush IV. Long-volatility positions ([[straddle|straddles]], strangles bought into earnings) lose the crush regardless of direction. The directional move must exceed the *full* premium paid (intrinsic + extrinsic) for the position to profit.
9. **Treating PEAD as actionable on the option side.** The post-earnings-drift signal is real but small (1-3% over weeks); it is dwarfed by the IV crush and option-side carry. PEAD is captured better in stock than in options.

## Related

- [[earnings-volatility]] — the cyclical IV behaviour wrapping the event
- [[earnings-iv-crush]] — strategy that harvests the post-event IV collapse
- [[earnings-volatility-trading]] — broader trading framework around earnings cycles
- [[earnings-calendar]] — calendar tooling for tracking events
- [[implied-earnings-move]] — formal definition and computation
- [[implied-volatility]] — variable that ramps and crushes
- [[options-risk-budgeting]] — risk-budget frame for events
- [[options-portfolio-construction]] — book-level construction
- [[stress-test]] — stress testing for events
- [[scenario-analysis]] — event-specific scenario grids
- [[volatility-term-structure]] — inversion is the event signal
- [[volatility-skew]] — event-skew dynamics
- [[straddle]] — natural instrument for implied-move quoting
- [[post-earnings-announcement-drift]] — empirical drift after the event
- [[earnings-per-share]] — the headline metric reported
- [[earnings-revision]] — analyst-revision dynamics around announcements
- [[earnings-management]] — guidance-management context
- [[earnings-whispers]] — third-party expectations data
- [[iv-crush]] — the post-event volatility collapse mechanism
- [[strike-selection]] — choosing strikes relative to the implied move
- [[moneyness-selection]] — ATM vs OTM choice for event structures
- [[delta]] — directional exposure that interacts with the gap
- [[news-and-sentiment-sources]] — earnings calendars and event data feeds

## Sources

- Ball & Brown (1968) "An Empirical Evaluation of Accounting Income Numbers" — original PEAD documentation
- Augustin, Brenner & Subrahmanyam (2014) "Informed options trading prior to takeover announcements" — empirical evidence on informed trading around scheduled vs unscheduled events
- Patell & Wolfson (1979, 1981) — early empirical work on earnings-announcement IV behaviour
- Bernard & Thomas (1989) "Post-earnings-announcement drift: delayed price response or risk premium?" — canonical PEAD reference
- SEC Regulation FD — disclosure framework requiring scheduled, simultaneous releases
- [[earnings-volatility]] — companion concept page on the IV cycle
- [[earnings-volatility-trading]] / [[earnings-iv-crush]] — companion strategy pages
- Hull, *Options, Futures, and Other Derivatives* — chapter on event-driven volatility
