---
title: "Historical Stress Test"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [risk-management, options, history, volatility, derivatives]
aliases: ["Historical Stress Test", "Historical Replay", "Historical Scenario Replay"]
related: ["[[stress-test]]", "[[scenario-analysis]]", "[[reverse-stress-test]]", "[[value-at-risk]]", "[[expected-shortfall]]", "[[options-risk-budgeting]]", "[[options-portfolio-construction]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[covid-crash]]", "[[black-monday]]", "[[long-term-capital-management]]", "[[gfc]]", "[[flash-crash]]", "[[china-devaluation-2015]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[volatility-term-structure]]", "[[monte-carlo-simulation]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]", "[[stress-test]]", "[[implied-volatility]]"]
difficulty: intermediate
---

A historical stress test re-prices the *current* portfolio under the actual market moves observed during a specific past episode — Black Monday 1987, Long-Term Capital Management 1998, the 2008 GFC peak, the 2010 Flash Crash, the 2018 Volmageddon, the COVID March 2020 sequence, the August 2024 yen-carry unwind. It is a special case of [[scenario-analysis]] in which the scenarios are not chosen arbitrarily but lifted from history's tape. Historical replay is the most regime-honest stress test available because the joint movement of spot, [[implied-volatility|IV]], skew, term structure, and correlation in a real crisis is something that no analytical model, including [[monte-carlo-simulation]], reliably reproduces.

## Overview

The case for historical stress testing is straightforward: the joint distribution of moves in a real crash is path-dependent, regime-specific, and structurally non-Gaussian in ways that even sophisticated parametric models miss. When the trader writes "spot -10%, IV +20" as a [[stress-test|stress scenario]], they are guessing at correlations they cannot fully model. When they replay 2020-03-16, they are using *exactly* the joint move that the market produced — including the skew steepening, the term-structure inversion, the bid-ask blowout, and the cross-asset spillovers that no analytical scenario would capture cleanly.

The case against treating historical replay as sufficient is equally important: each historical episode is **a sample of one**. The next crash will not be 2008, it will not be COVID, it will not be August 2024. Tail events have surface similarities (vol up, spot down, correlations spike) but their underlying drivers — banking stress, pandemic, FX-carry unwind — produce different joint distributions across the option surface. Historical replay therefore complements but does not replace forward-looking [[stress-test|stress tests]] that imagine *new* tail scenarios. The two together give a useful picture; either alone is incomplete.

This page treats historical replay as a daily operational discipline. For the broader scenario framework, see [[scenario-analysis]]. For forward-looking stress, see [[stress-test]] and [[reverse-stress-test]].

## Definition / Mechanics

### What is replayed

A historical stress test reads from a chosen past date the moves that actually happened on that date — not the prices, but the **shocks** — and applies them to the current book. The shocks include:

- **Spot move** — percentage change in each underlying (or beta-weighted to a benchmark for multi-name books).
- **IV move** — change in [[implied-volatility|IV]] at each strike and expiration. For a parallel approximation, use the change in ATM front-month IV; for a richer replay, use the full surface change.
- **Skew move** — change in the differential between OTM-put IV and OTM-call IV (e.g., 25-delta skew).
- **Term-structure move** — change in the differential between front- and back-month IV.
- **Correlation move** — for multi-name books, change in the average pairwise correlation.
- **Bid-ask widening** — change in the realised spread, often 3-10× normal in crisis sessions.

The book's Greeks are then re-priced under these joint shocks using the [[black-scholes-model|pricing model]] (see [[scenario-analysis]] for the repricing methodology). The output is a single P&L number per historical event, comparable to the forward-looking stress cells.

### Distinguishing from forward-looking stress

| Test type | Source of shocks | Strength | Weakness |
|---|---|---|---|
| **Forward-looking stress** | Operator imagination, calibrated to plausible moves | Can imagine new regimes; flexible | Operator may miss correlations or be over-optimistic |
| **Historical replay** | Real moves from a tagged date | Uses true joint dynamics | Each event is sample-of-one; future may not look like past |
| **[[monte-carlo-simulation\|Monte Carlo]]** | Sampled from a fitted distribution | Many paths; statistically rich | Distribution-dependent; tails depend on choice of fit |

A complete stress discipline runs all three. Historical replay is the *empirical anchor* — it shows the trader what real distributions of joint moves have looked like in episodes the market has already lived through.

## Methodology / How To Apply

### Step 1 — Curate the historical menu

A standard historical stress menu for a US equity-options book includes the following episodes. For each, the table records the canonical *single-day* shock; multi-day sequences (e.g., the 2020-03-09 → 2020-03-23 selloff) should also be replayed as sequential shocks where the book has open positions at each step.

| Date | Event | Spot move | IV move (VIX) | Notes |
|---|---|---|---|---|
| 1987-10-19 | [[black-monday\|Black Monday]] | S&P 500 -20.5% | VIX retroactive ~36 → 150 | Pre-VIX era; portfolio insurance feedback loop. Worst single-day equity loss in modern history. |
| 1998-09 | [[long-term-capital-management\|LTCM / Russia]] | S&P -7% over Aug-Sep; VIX 22 → 45 | Skew steepens dramatically | Quant-driven liquidity crisis; correlations spike across asset classes. |
| 2008-09-15 | [[gfc\|Lehman]] | S&P -4.7% on the day; -25% over Sep-Oct | VIX 25 → 80 over weeks | Skew inversion (puts > calls in vol); banking-stress episode. |
| 2008-10-15 | GFC peak | S&P -9% | VIX 55 → 70 | Multi-day extreme; liquidity collapse on listed options. |
| 2010-05-06 | [[flash-crash\|Flash Crash]] | S&P -9% intraday, recovered to -3% close | VIX 26 → 41 intraday | Microstructure event; intraday extremes far worse than close-to-close. |
| 2015-08-24 | [[china-devaluation-2015\|China devaluation]] | S&P -3.9% | VIX 28 → 53 intraday, opened with limit-down futures | Cross-asset; pre-open futures gap. |
| 2018-02-05 | [[volmageddon\|Volmageddon]] | S&P -4.1% | VIX 17 → 37 (closed at 37, intraday spike higher) | XIV blow-up; rebalancing-feedback episode. |
| 2018-12-24 | Q4 2018 crash | S&P -2.7% on the day; -16% over Q4 | VIX 18 → 36 over weeks | Hawkish-Fed scare; rolling stress over weeks. |
| 2020-03-12 | [[covid-crash\|COVID first leg]] | S&P -9.5% | VIX 41 → 75 | Pandemic onset; first multi-day crash since 2008. |
| 2020-03-16 | COVID peak | S&P -12% | VIX 57 → 82 | Largest single-session vol expansion of the cycle. |
| 2020-03-18 | COVID trough | S&P -5.2% | VIX peaked 85 | Multi-day sequence ends; subsequent rally extreme. |
| 2022-09-13 | CPI shock | S&P -4.3% | VIX 24 → 27 | Macro-data shock with surprisingly muted vol response — informative as a *vol-quiet* large-spot move. |
| 2024-08-05 | [[vix-august-2024-spike\|Yen-carry unwind]] | S&P -3% | VIX 23 → 65 intraday, closed 38 | FX-driven stress; intraday vol spike well above close-to-close. |

Most desks maintain 8-15 events covering different *types* of crisis: flash crashes, banking stress, vol-product feedback, pandemic, FX-carry, geopolitical. The diversity matters more than the count — running 30 different replays of equity selloffs from the same regime gives no incremental signal over running 2 of them.

### Crisis archetypes — choose for diversity of *mechanism*

The reason diversity beats count is that each archetype has a distinct joint-move signature. A menu heavy in one archetype is blind to the others. Curate the menu to span the archetypes, not the calendar.

| Archetype | Canonical replay | Distinctive joint-move signature | What it stresses in your book |
|---|---|---|---|
| Microstructure flash crash | [[flash-crash\|2010-05-06]] | Violent intraday spot air-pocket, fast recovery, modest IV | Gap/liquidity, intraday stops, [[gap-risk]] |
| Vol-product feedback | [[volmageddon\|2018-02-05]] | Spot down modest, IV explodes, rebalance loop | Short [[vega]], short-vol crowding |
| Banking / credit stress | [[gfc\|2008]] | Multi-week grind, skew inversion, correlations to 1 | Wing exposure, credit-linked names, duration |
| Pandemic / exogenous shock | [[covid-crash\|2020-03]] | Multi-day cascade, term-structure inversion, even Treasuries dislocate | Multi-day sequence, cross-asset hedges |
| FX-carry unwind | [[vix-august-2024-spike\|2024-08-05]] | Funding-currency snap, intraday VIX 5σ, fast partial reversal | [[short-strangle]], yen-linked exposure |
| Sovereign / political | 2011 EU crisis | Slow-burn, rates and FX leading, equities lagging | Rate sensitivity, sovereign-linked names |
| Quant-driven liquidity | [[long-term-capital-management\|1998 LTCM]] | Spread blowouts, correlation spikes across "unrelated" assets | Relative-value, dispersion, hidden correlation |
| Portfolio-insurance cascade | [[black-monday\|1987]] | One-day −20% with feedback loop; outside all later envelopes | The absolute tail; tests whether the book survives the worst case |

### Step 2 — Decide what to replay precisely

A real historical event has many possible "shocks" depending on what the trader cares about. Common choices:

- **Close-to-close** — the cleanest data; typically understates intraday extremes.
- **Open-to-close** — shows the gap risk visible to retail; misses overnight moves.
- **Intraday peak shock** — the worst point during the session; relevant for books that might be liquidated at midday.
- **Multi-day window** — replay sequential daily shocks from N days into the event (e.g., 2020-03-09 through 2020-03-23 as 11 sequential daily moves with the book responding each day).
- **First-leg only** — the initial down-leg of a multi-day event (e.g., the first 3 days of COVID), to avoid commingling with the follow-on dynamics.

For pre-trade screening, *intraday peak* is the most conservative choice. For daily monitoring, *close-to-close* is operationally cleanest. For position-sizing of multi-day books, the *multi-day sequence* is the most informative.

### Step 3 — Source the historical surfaces

The accuracy of historical replay depends on the quality of the historical option surface data:

- **orats** and **[[ivolatility]]** — historical surfaces back to the 2000s for US equity options, including skew and term-structure.
- **cboe-livevol** / **CBOE DataShop** — granular tick-level option data back to ~2004 for index and ETF options.
- **[[bloomberg]] OVDV / OVME** — institutional surfaces with full-fit; scenario engines support replay directly.
- **CME and ICE** — futures and futures-options historical data for cross-asset replay.
- **Reconstructed from option chains** — for older episodes (pre-2003), reconstruct from end-of-day option chains and ATM straddle prices; lose skew and term-structure granularity.

For events before continuous historical option-chain coverage (e.g., 1987, 1998), the surface must be approximated. Practitioners typically use the pricing of the *closest available proxy* (e.g., spot move plus an estimated VIX shock) and accept that the deeper skew/term dimensions are unavailable for replay.

### Step 4 — Apply and read

Each event becomes one row in the daily report:

```
Event              Spot     IV     Skew    Book P&L     vs Limit
2008-10-15         -9%     +30    +12     -$28,200     OK
2018-02-05         -4.1%   +20     +5     -$22,800     OK
2020-03-16         -12%    +24    +18     -$36,200     OK (close)
2024-08-05         -3%     +42     +5     -$33,000     OK
```

The book passes the replay if every event's loss is inside the [[options-risk-budgeting|risk budget]]. A breach on any single replay is an immediate signal: either size down, hedge, or accept that the book is not historically robust at current size.

## Worked Example

**Book**: $250k SPX-only options book, currently running:

- 5x SPX iron condors, 30 DTE, 1-sigma wings.
- 3x QQQ short strangles, 21 DTE, 16-delta.
- 2x bond ETF (TLT) short puts at support.
- 5x SPX long puts at -10% strike (overlay).

**Aggregate Greeks**: delta +120, gamma -150, vega -$800/IV pt, theta +$95/day. Drawdown limit: -15% NAV = -$37,500.

**Historical replay output** (close-to-close, 1-day horizon):

| Event | SPX move | IV move | Skew move | Book P&L | % NAV |
|---|---:|---:|---:|---:|---:|
| 1987-10-19 (estimated) | -20.5% | +50 IV (proxy) | +25 | -$60,400 | -24.2% **FAIL** |
| 1998-08-31 (LTCM/Russia) | -6.8% | +18 | +8 | -$22,300 | -8.9% OK |
| 2008-09-29 | -8.8% | +20 | +10 | -$26,900 | -10.8% OK |
| 2008-10-15 | -9.0% | +30 | +12 | -$31,400 | -12.6% OK |
| 2010-05-06 (close) | -3.2% | +15 | +5 | -$13,200 | -5.3% OK |
| 2010-05-06 (intraday) | -9% | +20 | +8 | -$32,800 | -13.1% OK (close to limit) |
| 2015-08-24 | -3.9% | +28 | +10 | -$22,400 | -9.0% OK |
| 2018-02-05 | -4.1% | +20 | +6 | -$22,800 | -9.1% OK |
| 2018-12-24 | -2.7% | +14 | +4 | -$11,800 | -4.7% OK |
| 2020-03-09 | -7.6% | +20 | +10 | -$25,400 | -10.2% OK |
| 2020-03-12 | -9.5% | +21 | +12 | -$30,800 | -12.3% OK |
| 2020-03-16 | -12% | +24 | +18 | -$36,200 | -14.5% OK (close to limit) |
| 2022-09-13 | -4.3% | +5 | +2 | -$8,400 | -3.4% OK |
| 2024-08-05 (close) | -3% | +14 | +5 | -$15,200 | -6.1% OK |
| 2024-08-05 (intraday) | -4.5% | +42 | +12 | -$33,000 | -13.2% OK (close to limit) |

**Reading**: the book passes 14 of 15 historical replays at the close-to-close level, with three replays (2010-05-06 intraday, 2020-03-16, 2024-08-05 intraday) within ~$5,000 of the limit. **The book fails the 1987 Black Monday replay**, which is unsurprising — Black Monday is materially outside the joint-move envelope of any post-1987 episode. The trader has to make an explicit judgment: size for "robust to all post-1987 events" (acceptable) or "robust to 1987 itself" (which would require dramatic size cuts).

The standard discipline is to accept the post-1987 envelope as the operating standard, while monitoring the gap between the worst tolerated event (here ~ -$36k on 2020-03-16) and the limit ($37,500). A 4% buffer is workable but tight; if any other replay drifts toward the limit over the next week, the trader cuts size proactively.

For multi-day exposure, the same engine is run as a *sequence*: replay 2020-03-09, then 2020-03-12, then 2020-03-16 in order, with the book Greeks updated after each replay (no rebalancing assumed). Over the three-day sequence the cumulative loss is well in excess of any single-day stress, which is why books that look robust to single-day replays sometimes fail in multi-day events.

## Where Historical Replay Fits in the Risk Stack

Historical replay is the empirical anchor of a layered risk process. It answers "would today's book have survived the crises the market has already produced?" — but it is silent on probability and on novel regimes. Pair it with the other tools, each of which answers a question replay cannot.

| Question | Right tool | Replay's contribution |
|---|---|---|
| Would I survive 2008 / 2020 / 2024 again? | **Historical replay** (this page) | The whole point |
| What if a *new* tail happens? | [[stress-test]] (forward-looking) | Replay calibrates how big "big" really is |
| What's the smallest move that ruins me? | [[reverse-stress-test]] | Replay shows which historical events approach that boundary |
| What's my loss at the 99th percentile? | [[value-at-risk\|VaR]] | Replay sanity-checks whether VaR captured the historical tails |
| What's my *average* loss in the tail? | [[expected-shortfall\|ES]] | Replay events populate the empirical tail ES summarises |
| What's the full distribution of outcomes? | [[monte-carlo-simulation\|Monte Carlo]] | Replay validates whether the simulated tails are wide enough |

The cadence that ties these together: run the **scenario grid** ([[scenario-analysis]]) and **historical replay** *daily*, recompute **VaR/ES** *daily*, run a **reverse stress test** *weekly* or after any large position change, and refresh the **historical menu** at least *annually* (and immediately after any new tail-event candidate). [[expected-shortfall]] computed under stressed correlations is the binding metric; the historical replays are the reality check that the ES number is not understating the tail.

## Limitations / Common Pitfalls

1. **Sample-of-one bias.** Each historical episode is *one realisation* of a tail event. The fact that COVID had a particular skew dynamic does not mean the next pandemic-style stress will. Replay is a useful empirical anchor, not a probability statement.
2. **Survivorship in the historical menu.** The events recorded in historical menus are the ones the market lived through; events that *would have* happened but were prevented (e.g., the avoided 2011 debt-ceiling default) do not appear. Forward-looking stress should also imagine near-misses.
3. **Surface availability before 2003.** Historical option surfaces are sparse before continuous data coverage starts. Replays of 1987, 1998, and earlier episodes use approximated surfaces and are correspondingly less reliable.
4. **Close-to-close understatement.** Most replays use close-to-close moves. Real intraday extremes (2010-05-06 intraday low, 2020-03-18 intraday, 2024-08-05 intraday) are 30-50% worse than close numbers. A book that liquidates at intraday lows in stress is exposed to those, not to close-to-close.
5. **Rebalancing assumption.** Replays typically hold the book static through the event. In reality the trader would be rebalancing — but rebalancing during stress is *expensive* (3-10× wider spreads; see [[liquidity-risk]]). Some replays should assume *no rebalancing* (worst case if the trader is paralysed) and others should assume *forced delevering* (worst case if margin is called).
6. **Single-asset replay on multi-asset books.** Replaying 2008-10-15 on the equity book ignores the simultaneous moves in rates, FX, and commodities. For multi-asset books the replay must include cross-asset shocks, ideally synced to the same dates.
7. **Skew and term-structure approximation.** A "VIX +30" parallel-IV replay misses the skew steepening and term-structure inversion that crashes always produce. The full surface change must be replayed for books with material wing or calendar exposure.
8. **Confusing replay with strategy backtest.** Historical replay applies the *event* to the current book; it does *not* test how the strategy itself performed in the past. A strategy backtest of the same period would also include the strategy's response (rebalancing, hedging) and ask "did the strategy survive?". Both are useful; they answer different questions. See [[backtesting]].
9. **Not refreshing the menu.** A historical menu compiled in 2019 misses COVID, the 2022 selloff, the 2024 yen-carry event. Refresh the menu at least annually after any new tail-event candidate.

## Related

- [[stress-test]] — broader stress-testing concept, of which historical replay is one variety
- [[scenario-analysis]] — broader scenario-grid framework
- [[reverse-stress-test]] — finds the smallest move producing a given loss
- [[value-at-risk]] — distribution-based risk metric, complement to replay
- [[expected-shortfall]] — tail expectation, complement to replay
- [[options-risk-budgeting]] — budget the replay verifies
- [[options-portfolio-construction]] — book-level construction
- [[volmageddon]] — 2018-02-05 episode, canonical short-vol replay
- [[vix-august-2024-spike]] — 2024-08-05 yen-carry replay
- [[covid-crash]] — 2020-03 sequence, multi-day replay reference
- [[black-monday]] — 1987-10-19, the historical extreme
- [[long-term-capital-management]] — 1998 quant-driven stress
- [[gfc]] — 2008 banking-stress sequence
- [[flash-crash]] — 2010-05-06 microstructure event
- [[china-devaluation-2015]] — 2015-08-24 cross-asset stress
- [[implied-volatility]] — variable being shocked
- [[volatility-skew]] — under-replayed dimension
- [[volatility-term-structure]] — under-replayed dimension
- [[monte-carlo-simulation]] — stochastic complement

## Sources

- [[options-portfolio-construction]] — book construction with historical replay
- Hull, *Options, Futures, and Other Derivatives* — chapter on historical simulation in risk management
- Jorion, *Value at Risk* (3rd ed.) — historical-simulation methodology
- *Basel Committee, Principles for sound stress testing practices and supervision* (2009) — institutional guidance
- *FRTB (Fundamental Review of the Trading Book)* — Basel framework with historical-stress component
- CCAR (Comprehensive Capital Analysis and Review) — Federal Reserve historical-and-hypothetical stress framework
- CBOE / CME stress methodologies — exchange-level historical replay for margin (SPAN, TIMS)
