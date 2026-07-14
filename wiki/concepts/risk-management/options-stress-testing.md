---
title: "Options Stress Testing"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, portfolio-theory, stress-testing]
aliases: ["Options Scenario Analysis", "Options Risk Scenarios", "Options What-If Analysis"]
related: ["[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[portfolio-greeks-aggregation]]", "[[vega-budgeting]]", "[[options-concentration-risk]]", "[[value-at-risk]]", "[[expected-shortfall]]", "[[portfolio-margin]]", "[[vix-august-2024-spike]]", "[[tail-risk]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]", "[[value-at-risk]]"]
difficulty: advanced
---

Options stress testing is the practice of revaluing an options book under specific, large, joint moves in spot, implied volatility, term structure, skew, and correlation — the moves that the [[options-greeks|Greeks]] cannot describe because Greeks are local first-order (and at most second-order) sensitivities. A delta/gamma/vega report tells you what the book does for a 1% spot move and a 1-point IV change *near current conditions*; a stress test tells you what the book does when SPX falls 12% in two days and front-month VIX prints 65, which is a different question with a different answer. Any serious options trader runs scenarios pre-trade and re-runs them daily; on a [[portfolio-margin]] account, the broker is *already* running them against you to compute margin, so you may as well run the same battery yourself before they do.

## Why Greeks Alone Are Insufficient

The Greeks are a Taylor expansion of the option price around the current state of the world:

$$\Delta P \approx \delta \cdot \Delta S + \tfrac{1}{2}\gamma \cdot (\Delta S)^2 + \nu \cdot \Delta\sigma + \theta \cdot \Delta t + \rho \cdot \Delta r$$

That expansion is *local*. It works for small moves. It breaks for large moves in three specific ways:

1. **Higher-order terms matter.** A short-gamma book has P&L that is quadratically punishing in $\Delta S$. The delta+gamma approximation misses third-order [[speed]] and [[color]] effects that become material beyond ~2σ moves.
2. **Greeks themselves change.** Vega is not constant. As spot falls and IV rises, an OTM put's vega expands ([[vanna]]). A book that looks vega-balanced at S=100 can be heavily long or short vega at S=85.
3. **Cross-effects compound.** Spot and vol are not independent in a crash. The realistic crash scenario is *spot down + IV up + skew steepening + bid-ask widening simultaneously*. No single Greek captures the joint move.

Stress testing skips the Taylor approximation entirely. You re-price every option at the new spot, the new vol surface, the new term structure, the new rates, and sum the P&L. That is the *true* P&L the book would print under those conditions, model error aside.

> **The blunt version:** Greeks are for managing the position day to day. Stress tests are for figuring out whether the position will survive at all.

## Greeks vs Scenarios

| Tool | What it tells you | When it fails |
|------|-------------------|---------------|
| **Delta** | P&L per $1 spot move | Fails for any move large enough that gamma kicks in |
| **Gamma** | How delta changes per $1 spot move | Itself changes; ignores vega-of-gamma effects in crashes |
| **Vega** | P&L per 1-point IV change | Assumes parallel surface shift; misses skew steepening and term-structure dislocation |
| **Theta** | P&L per day of decay | Assumes no spot/vol move; useless during a real selloff |
| **Greeks combined** | Local P&L surface near current state | Diverges from true P&L beyond ~5% spot or ~10 IV points |
| **Scenario** | Exact P&L under a specified joint move | Only as good as the scenarios you imagine |

The two tools are complementary. Greeks are a continuous, real-time risk dashboard. Scenarios are discrete, larger, and more honest about the tails. A professional options book uses both; relying on Greeks alone is the most common path to a [[risk-of-ruin|blow-up]].

## Scenario Types

A complete stress matrix covers single-variable shocks, joint shocks, and structural shifts. The minimum battery for a discretionary options book:

### 1. Spot shocks (univariate)

Re-price the book at:
- Spot −20%, −10%, −5%, −2%, +2%, +5%, +10%, +20%

This is the standard SPAN-style grid. Most retail platforms generate this for free. It catches gross gamma exposure but *understates* tail loss because it holds IV constant.

### 2. IV shocks (univariate)

Re-price the book at:
- IV +25%, +50%, +100% (relative — i.e. 20 vol → 30, 40, [[vega]] becomes the dominant P&L driver)
- IV −10%, −25% (vol crush — the realistic scenario the day after a feared event passes)

### 3. Joint spot + IV shocks (the realistic crash)

This is the one that matters. In a real selloff, spot and IV move together with a strong negative correlation:

| Scenario | Spot | IV change | Skew | Realistic? |
|----------|------|-----------|------|------------|
| Mild dip | −3% | +15% | slight steepen | Tuesday |
| Correction | −7% | +40% | moderate steepen | Quarterly |
| Crash | −12% | +80% | sharp steepen | 2020-03 grade |
| Black Monday | −20% | +200% | extreme | 1987 grade |
| Vol-only spike | flat | +60% | flat | Aug-2024 grade |
| Melt-up | +6% | −20% | flatten | post-FOMC relief |

The "Crash" and "Black Monday" rows are where short-vol books die. A book that is short 100 SPX 5-delta puts looks innocuous at delta=−5 per contract; under the Crash scenario each put becomes ~25-delta and IV doubles, so what looked like a $50k risk becomes a $400k drawdown plus margin call.

### 4. Term-structure shifts

The vol surface is not a single number. Front-month and back-month vol move differently:

- **Front-month spike, back-month flat** (Aug-2024 archetype) — punishes short front-month vol, leaves long-dated vol roughly unchanged. [[calendar-spread|Calendar spreads]] short the front and long the back get crushed.
- **Parallel shift** — entire term structure up or down equally. Easier on calendars, hardest on delta-1 vol exposure.
- **Backwardation flip** — front-month exceeds back-month. Indicates panic. Long-dated puts gain less than expected from the IV move.

### 5. Skew steepening

Implied vol of OTM puts rises faster than ATM. A short put-skew trade (short OTM puts, long ATM puts, positive carry in normal regimes) blows up in any real selloff. Skew steepening should be tested as a separate scenario from a parallel IV shift.

### 6. Sector rotations and correlation regime flips

For multi-name books, the dangerous scenario is **correlation going to 1**. In a normal regime, a long-short book might be 30% correlated; in a crisis everything sells off together and correlation spikes to 0.9. Diversification benefits evaporate at exactly the moment they are most needed. See [[correlation-breakdown]].

The stress version: revalue the entire equity book under "all longs −15%, all shorts −12%" — the asymmetric crash where shorts don't hedge as much as expected.

### 7. Forward-looking idiosyncratic scenarios

- **Fed surprise hike** — front-end rates +100bp, equity index −5%, IV +30%
- **Election volatility** — IV +50% with no spot move (event risk priced in)
- **Geopolitical shock** — oil +20%, equities −7%, gold +5%, USD +3%
- **Single-name earnings miss** — one underlying gaps −25% with IV crush in that name only
- **Liquidity event** — bid-ask widens 5–10×, no fills available at mid

The last one is rarely modeled and is the most likely to actually happen.

### The Master Scenario Grid

Rather than run each shock in isolation, a mature desk maintains a single consolidated grid that specifies *all five surface dimensions at once* for every named scenario — because the whole point of stress testing is to capture the joint move. A spot shock with the [[volatility-skew|skew]] and [[term-structure-of-volatility|term structure]] held at today's shape is not a real crash; it is a marginal that understates the loss. The grid below is the canonical battery to revalue any equity-index options book against. Numbers are illustrative archetypes, not forecasts or live data.

| Scenario | Spot | ATM IV (relative) | Skew (25Δ put − ATM) | Term structure | Realistic frequency |
|----------|------|-------------------|----------------------|----------------|---------------------|
| **Calm baseline** | flat | flat | normal | mild contango | the default state |
| **Mild dip** | −3% | +15% | slight steepen | flatten slightly | several times/quarter |
| **Correction** | −7% | +40% | moderate steepen | front rises faster | 1–2×/year |
| **Vol-only spike** | flat to −3% | +80–180% | sharp steepen | sharp backwardation | rare; Aug-2024 grade |
| **Crash** | −12% | +80–100% | sharp steepen | backwardation | once every few years; 2020 grade |
| **Black Monday tail** | −20% | +200% | extreme steepen | deep backwardation | once-a-generation; 1987 grade |
| **Melt-up / relief** | +6% | −20% | flatten | re-contango | post-FOMC, post-event |
| **Vol crush** | flat to +2% | −25% | flatten | re-contango | day after a feared event passes |
| **Slow grind bear** | −25% over months | +30 avg, sustained | persistent steepen | mild backwardation | secular, e.g. 2000–02 |
| **Liquidity event** | −5% with no fills | +60% + spreads ×5–10 | erratic | dislocated | flash-crash grade |

Read across the row, not down the column: the loss a short-vol book takes in the **Crash** row is the *joint* product of spot down, IV up, [[volatility-skew|skew]] steepening, and backwardation — each of which independently hurts a short-premium book and which compound when they arrive together. The right-hand frequency column exists to keep the exercise honest: a book that cannot survive the "once-a-generation" row at *some* size still needs to know that number, because the entire job of [[position-sizing]] is to set size so that even the rare rows stay inside tolerance.

### How to Construct a Stress Scenario (step-by-step)

A scenario is not a single number; it is a fully specified alternate state of the world. Build each one with this checklist so you never accidentally hold a surface dimension constant:

1. **Name the event and its narrative.** "Carry-trade unwind," "hyperscaler guidance miss," "Fed surprise hold." A scenario you can name is a scenario you can argue about and refine.
2. **Set the spot move** for every underlying — not just the index. Single names move more than the index ([[options-concentration-risk|concentration]] and beta amplify); shorts in a long-short book don't fall as far as longs.
3. **Set the ATM IV move** *jointly* with spot. Use the empirical −0.7 to −1.0 spot/vol correlation: a −10% index day historically lifts ATM IV sharply. Never hold IV flat in a down-spot scenario.
4. **Reshape the [[volatility-skew|skew]].** OTM put IV rises faster than ATM in any selloff. Steepen the put wing explicitly — a parallel IV shift understates the punishment to short-put-skew structures.
5. **Reshape the [[term-structure-of-volatility|term structure]].** Front-month spikes more than back-month and can flip into backwardation. This is what kills short-front-month [[calendar-spread|calendars]].
6. **Add the rate / cross-asset legs** where the book is exposed: rates, FX (JPY for carry), oil, gold, credit spreads.
7. **Force correlation to crisis levels.** Re-run the multi-name book with all pairwise correlations pushed to ~0.9 (see [[correlation-breakdown]]).
8. **Apply a liquidity haircut.** Widen modeled exit prices by the realistic crisis bid-ask (5–10×) on any position you would actually need to unwind.
9. **Re-price every option from scratch** at the new surface — do not Taylor-extrapolate from current [[options-greeks|Greeks]]. Sum the P&L.
10. **Re-compute margin at the stressed surface too** (see below) — the loss number and the margin-expansion number are two different constraints, and either can force liquidation.

The discipline is to write the scenario down *before* the move, not to reverse-engineer it after one happens. See [[scenario-analysis]] and [[reverse-stress-test]] for the complementary "find the scenario that breaks the book" direction.

## Historical Replay

The most honest stress test is to take your *current book* and replay it through actual historical crisis windows. The platforms that support this either provide canned historical surfaces or let you import them. The standard battery:

| Event | Window | Spot move | Peak IV | Notes |
|-------|--------|-----------|---------|-------|
| **Black Monday** | 1987-10-19 | SPX −22.6% in one day | VIX-equivalent ~150 | The benchmark tail event; most modern stress tests don't even contemplate it |
| **LTCM / Russia** | 1998-08 to 1998-10 | SPX −19% peak-to-trough | VIX peak 45 | Correlation regime flip; see [[ltcm]] |
| **Dot-com unwind** | 2000-03 to 2002-10 | SPX −49% over 30 months | VIX peak 45 | Slow grind, not a single shock |
| **GFC / Lehman** | 2008-Q4 | SPX −38% in 6 weeks | VIX peak 89 | Joint spot + IV + credit spread blowout |
| **Flash Crash** | 2010-05-06 | SPX −9% intraday, recovered | VIX +30% | Liquidity collapse; short-dated options went no-bid |
| **August 2015** | 2015-08-24 | SPX −5% open, ETFs dislocated | VIX 53 | ETF NAV disconnect; many products halted |
| **Volmageddon** | 2018-02-05 | SPX −4%, VIX +116% intraday | VIX 50 | XIV terminated; short-vol ETPs blew up |
| **COVID crash** | 2020-02 to 2020-03 | SPX −34% in 5 weeks | VIX peak 82 | Fastest bear market in history; vol moved before spot |
| **August 2024** | 2024-08-05 | SPX −3%, VIX intraday spike to 65 | VIX +180% intraday | Vol-only spike with limited spot move; carry-trade unwind. See [[vix-august-2024-spike]] |
| **April 2025 tariffs** | 2025-04-02 to 2025-04-09 | SPX −12%, VIX peak 60 | sustained elevated IV | Policy-driven, multi-day grind |

For each event you compute: *what would my current book have done if held through this period?* That number is the right answer to "how much can I actually lose." The 1987 number in particular is the one that separates books that will survive a tail event from books that won't.

The August 2024 spike is uniquely instructive because the spot move was small (−3%) but VIX tripled intraday. A book that was hedged for spot moves but short front-month vol (very common configuration) printed losses that no spot-shock matrix would have shown. See [[vix-august-2024-spike]] for the post-mortem.

## Forward-Looking Scenarios

Historical replay tells you what already happened; forward-looking scenarios stress your specific book against *plausible* events that haven't happened yet. The discipline is to actually write them down before you trade, not after the move.

### Macro scenarios
- **Fed cuts surprise hold** — rates flat when 50bp was priced; equity −2%, IV +20%
- **Inflation print +0.4 surprise** — front-end rates +30bp, growth stocks −4%, IV +25%
- **Hard landing recession** — SPX −25% over 3 months, VIX averages 35
- **Soft landing extension** — IV crushes to 11, short-vol carry surges

### Event-driven scenarios
- **Election week** — IV +50% in the 5 trading days before, then −40% the day after
- **Earnings season concentration** — your top 3 single-name positions all report in same week
- **FOMC** — IV crush in front-month, term structure normalizes

### Geopolitical / black-swan scenarios
- **Taiwan event** — global equities −10%, defense +15%, semis −20%, USD +5%
- **Oil shock** — Brent +30%, equities −5%, transports −10%, energy +15%
- **Sovereign credit event** — flight to quality, USTs rally, EM equities −15%

### Idiosyncratic scenarios
- **Single-name fraud** — one position gaps −60% with no warning (Wirecard, Luckin)
- **Sector regulatory shock** — bank stress test failure, AI regulation, healthcare reform
- **Carry-trade unwind** — JPY +5% in a day, all yen-funded positions liquidate (Aug-2024 archetype)

## Setting Tolerance Limits

Stress numbers are useful only if they map to action thresholds. A standard professional framework:

| Limit type | Typical level | Action if breached |
|------------|---------------|--------------------|
| **Worst-case scenario loss** | ≤ 15% of equity | Reduce position before trade; hedge if already on |
| **Hard stop** | ≤ 25% of equity | Trade is not allowed under any sizing |
| **Single-name max loss** | ≤ 5% of equity in any one underlying | Cap per-name notional |
| **Single-scenario max loss** | ≤ 10% in any individual scenario | Diversify across uncorrelated trades |
| **Tail-vs-body asymmetry** | tail loss / expected gain ≤ 4× | Avoid trades where the tail dwarfs the prize |

The 15-25% range is widely cited in professional risk frameworks. Past 25% peak-to-trough drawdown, the math of recovery becomes brutal: a 25% drawdown requires a 33% rally to break even; a 50% drawdown requires 100%. Books that allow stress losses past that line tend not to come back.

## Scenario Design Pitfalls

Stress testing badly is worse than not stress testing — it produces false confidence. The most common errors:

### 1. Stressing one variable at a time

Spot −10% with IV held constant produces a P&L number that is much *smaller* than the realistic crash, where IV also explodes. SPAN's default grid stresses spot and IV jointly; many internal tools do not. Always test the joint scenario, not the marginals.

### 2. Using the current vol surface as a baseline

The current surface bakes in *current* skew and term structure. In a stress event the surface itself dislocates — skew steepens, term structure inverts, OTM put IVs explode disproportionately. A scenario that just shifts the entire surface up by 50% understates the punishment to short-skew books. See [[skew-risk]].

### 3. Ignoring liquidity

In a real crisis bid-ask spreads widen 5-10×. A 0.05-wide ATM SPX option becomes 0.40 wide. If you need to roll or close during the stress, you pay that spread. The mark-to-market loss in your stress test does not include the additional cost to actually exit. Add a liquidity haircut: 10% extra loss on top of any scenario where the book needs to be unwound.

### 4. Treating margin as static

Under stress, [[portfolio-margin]] requirements *expand* (sometimes 2-3×) because the broker's own scenario engine produces larger numbers. A book that fits in margin today may not fit in stressed margin, forcing forced liquidations at the worst possible prices. Always stress your margin alongside your P&L.

### 5. Pre-existing correlation assumptions

Most stress engines use a long-window historical correlation matrix. In a crisis correlation goes to 1. Re-run your stress with all correlations forced to 0.9 to see what the book does when "diversification" stops working. See [[correlation-breakdown]].

### 6. Not stressing the model itself

If your pricing relies on a particular model (Black-Scholes, SABR, local-vol), and that model breaks in stress (volatility-of-volatility regime), your stress P&L is itself wrong. See [[model-risk]].

## Frequency

| Book type | Minimum frequency |
|-----------|-------------------|
| **Active discretionary options book** | Daily, plus pre-trade for every new position |
| **Slow swing options book** | Weekly, plus pre-trade |
| **Long-only protective puts** | Monthly, plus pre-trade |
| **Systematic / algorithmic** | Embedded in execution layer, runs continuously |
| **Around earnings or known event** | Pre-event, mid-event, post-event |
| **After significant market move** | Same day, even if no positions changed |

The point of daily stress is that the *book changes* even when you don't trade — gamma decays, vega flips, theta accumulates, nearby strikes drift in or out of the money. Last week's stress number does not describe this week's book.

## Worked Example: Pre-Trade Stress on an SPX Iron Condor

Trader is considering adding a 100-lot SPX iron condor, 30 DTE, short strikes at 1-delta and 99-delta on the puts, 1-delta and 99-delta on the calls — wait, more realistically: short the 10-delta put, long the 5-delta put, short the 10-delta call, long the 5-delta call. Width is $20 on each side. Credit collected: $1.40 per contract. Max loss per contract: $18.60. Total max loss: $186,000 on a $1M account.

**Greeks of the new position (per contract):**
- Delta: ~0
- Gamma: −0.02
- Vega: −$8
- Theta: +$15

**Greeks of full position (100 contracts):**
- Net vega: −$800 per IV point
- Net theta: +$1,500 per day
- Net gamma: −2.0

The book *looks* delta-neutral and the trader is collecting $14k credit, $1.5k theta per day. By Greeks alone it looks great.

**Run the stress matrix:**

| Scenario | Spot | IV | P&L on this position |
|----------|------|-----|----------------------|
| Today | flat | flat | −$2,000 (currently slightly red) |
| Mild dip | −3% | +15% | −$8,000 |
| Correction | −7% | +40% | −$45,000 |
| **Crash (2020)** | −12% | +80% | **−$140,000** |
| Aug-2024 spike | flat | +180% | −$95,000 |
| Black Monday | −20% | +200% | −$186,000 (max loss) |

The stress test reveals what the Greeks hide. A book that "looks" balanced has a worst-case loss of −$186k against a $1M account — 18.6% drawdown in a single tail event. The Aug-2024 scenario, with no spot move, still costs $95k just from vol expansion.

**Decision:** trader sizes down to 40 contracts. New max loss: −$74k (7.4% of account). New stress for Aug-2024: −$38k (3.8%). New stress for the 2020 crash: −$56k (5.6%). All inside the 15% tolerance limit. The 100-lot was over the line; the 40-lot is inside.

This is the professional workflow: the stress number is the binding constraint, not the [[risk-reward-ratio|R/R]] number, not the win-rate fantasy, not the Greeks. Size the position to make the worst stress survivable, then take the trade.

## Connection to Position Sizing & Margin

Stress testing is not a standalone diagnostic — it is the function that *sets the size knob*. The worked example above made this concrete: the trade was not rejected, it was **resized** until its worst-case stress loss fit inside the tolerance band. This is the entire mechanism by which stress testing connects to [[position-sizing]].

### Stress as the binding sizing constraint

Most retail sizing rules anchor on the *premium at risk* or a fixed dollar stop. Both understate the loss of a short-vol book, because the realistic crash is a joint move that the entry credit and the static Greeks both fail to capture. The professional sizing loop inverts the order of operations:

1. Choose the structure and a provisional size.
2. Run the full [[#The Master Scenario Grid|master scenario grid]].
3. Find the worst-case row.
4. If worst-case loss > tolerance (e.g. 15% of equity), **scale the size down linearly** until it fits — stress loss is approximately linear in contract count for a fixed structure, so halving the lots roughly halves every scenario loss.
5. Lock the size only once the worst row is inside tolerance.

In this loop the stress number — not [[delta]], not the [[risk-reward-ratio|R/R]] ratio, not [[theta-targeting|the theta target]] — is the constraint that actually determines how many contracts go on. Theta targeting tells you how much decay you'd *like* to harvest; stress testing caps how much you're *allowed* to. When the two conflict, stress wins. See [[options-position-sizing]] and [[options-risk-budgeting]].

### Stress-aware margin: the second constraint

A book can pass the P&L stress test and still fail the *margin* stress test, because [[portfolio-margin]] requirements expand non-linearly when [[volatility]] spikes. The broker's own [[span-margin|SPAN]]/TIMS scenario engine is itself a stress test — it reprices your book across a shock grid and charges the worst loss as margin. When you stress your P&L, stress your margin in the same run:

| Constraint | What it limits | Failure mode |
|------------|----------------|--------------|
| **Worst-case P&L** | How much equity a tail move erases | Drawdown past recovery math (a 50% loss needs a 100% rally back) |
| **Stressed margin** | Whether the book still *fits* after the move | Forced liquidation into the worst prices — even on positions that would have recovered |

The August 2024 spike is the archetype where both fired at once: short-vol books took a mark-to-market hit *and* saw margin requirements jump, so traders were liquidated mechanically rather than by choice. The defensive rule is to size to a fraction of buying power (commonly ≤50%) and stress the *margin* at 2× the standard grid, so the book survives the margin expansion, not just the P&L. See [[portfolio-margin]] for the margin-expansion mechanics and [[portfolio-greeks-aggregation]] for the daily Greeks dashboard that feeds the stress engine.

### Where it sits in the wiki

Stress testing is the enforcement layer that connects the rest of the options-risk stack: [[portfolio-greeks-aggregation]] produces the book-level Greeks, [[options-concentration-risk]] reveals the hidden single-bet exposures the scenarios then punish, [[theta-targeting]] and [[vega-budgeting]] set the objectives, [[options-portfolio-construction]] assembles the book, and stress testing is the gate that decides the final size and triggers [[trade-repair-and-rolling|repair or hedging]] when a live book's stress number drifts out of tolerance.

## Tools

| Tool | What it does | Cost |
|------|--------------|------|
| **IBKR Risk Navigator** | Built-in scenario tab in TWS; spot/IV grid, custom scenarios, historical replay | Free with IBKR account |
| **OptionVue / OptionNet Explorer** | Dedicated retail platforms for portfolio Greeks and scenarios | $50-200/month |
| **ORATS** | Historical surfaces, custom scenarios, API access | Subscription |
| **CBOE Risk Calculators** | Limited-scope scenario tools, useful for SPX specifically | Free / freemium |
| **thinkorswim Analyze tab** | Decent scenario grid, beta-weighted | Free with TDA / Schwab |
| **Tastytrade** | Curve and table views for portfolio Greeks across scenarios | Free with account |
| **QuantLib (Python)** | Full custom pricing engine, build any scenario you can write | Free, requires coding |
| **Bloomberg OVME / DLIB** | Institutional-grade scenario and historical replay | Bloomberg terminal |
| **Custom Python** | Full control, integrates with portfolio system | Build cost |

For most discretionary traders running portfolio-margined books, IBKR Risk Navigator's scenario tab plus a simple Python script for historical replay covers 90% of needs. Larger books move to ORATS or build internal tooling.

## Professional Practice

Professional risk practice treats the broker's static [[portfolio-margin|margin number]] as *not* a real risk metric — it's an arbitrary haircut the broker applies to comply with regulation. The *real* risk metric is the scenario stress test, run pre-trade and re-run daily. Specifically:

1. **Pre-trade stress on every new position.** No new position goes on without a worst-case scenario number computed before clicking buy. The trader has to be able to live with that number.
2. **Daily revisit of the entire book.** Even unchanged positions get re-stressed daily because the surface and the calendar moved.
3. **Stress is the binding constraint.** When the stress number exceeds the tolerance limit, the position is reduced or hedged — non-negotiable. Greeks may say it's fine, broker margin may say it's fine; the stress number is the one that controls.
4. **Stress replaces P&L targets as the daily metric.** The screen the trader looks at first thing is the stress matrix, not the unrealized P&L. P&L tells you what happened; stress tells you what could happen.
5. **The professional desk runs stress before lunch and again before close.** Retail traders run it never.

The connection to trade construction is direct: the position-sizing stage is *where* the stress test lives in the workflow. You pick a structure, you size it provisionally, you stress it, and the size is final only if the stress number is inside the tolerance limit.

## Stress Testing vs Other Risk Metrics

| Metric | What it captures | What it misses |
|--------|------------------|----------------|
| **[[options-greeks\|Greeks]]** | Local sensitivities | Anything beyond ~5% spot or ~10 IV points |
| **[[value-at-risk\|VaR]]** | Statistical percentile of P&L | The tail beyond the percentile, model error |
| **[[expected-shortfall]]** | Average tail loss | Joint shocks not in historical data |
| **Stress test** | Specific named scenarios | Scenarios you didn't think of |
| **[[reverse-stress-test]]** | What scenario destroys the book | Probability of that scenario |
| **[[portfolio-margin]]** | Broker's worst-case under their rules | Liquidity, model error, real-world joint shocks |

A complete risk framework uses all of them. Greeks for daily management, VaR for cross-book comparison, ES for tail awareness, scenario stress for joint-shock honesty, and reverse stress to find the things you didn't ask about.

## Related

- [[options-portfolio-construction]] — the workflow this stress-tests
- [[options-risk-budgeting]] — setting the tolerance limits stress is checked against
- [[portfolio-greeks-aggregation]] — the daily Greeks dashboard, complement to scenarios
- [[vega-budgeting]] — the specific vol-shock dimension of stress
- [[options-concentration-risk]] — single-name and single-scenario concentration
- [[value-at-risk]] — statistical risk metric that stress tests complement
- [[expected-shortfall]] — tail-loss metric, related but distinct from scenario loss
- [[portfolio-margin]] — the broker's own stress engine; mirror it
- [[vix-august-2024-spike]] — case study for vol-only stress scenarios
- [[tail-risk]] — what stress testing exists to manage
- [[reverse-stress-test]] — complementary "find the scenario" approach
- [[correlation-breakdown]] — the regime flip that breaks portfolio diversification
- [[skew-risk]] — the vol-surface dimension stress should explicitly cover
- [[model-risk]] — pricing-model failure during stress events
- [[position-sizing]] — the knob stress testing actually sets
- [[theta-targeting]] — the income objective stress testing caps
- [[trade-repair-and-rolling]] — what a live book's out-of-tolerance stress number triggers

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on the limitations of Greeks for large moves
- [[book-the-black-swan]] — Taleb on why local sensitivity measures (Greeks, VaR) miss the events that matter
- [[vix-august-2024-spike]] — empirical case study of a vol-only stress event
- CBOE / OCC margin methodology documentation — the SPAN scenario grid that brokers use, and which traders should mirror internally
