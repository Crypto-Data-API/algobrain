---
title: "Expiration Laddering"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, portfolio-theory]
aliases: ["Expiry Laddering", "Expiration Distribution", "Laddered Expirations"]
related: ["[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[pin-risk]]", "[[gamma-scalping]]", "[[calendar-spread]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]", "[[theta-decay]]"]
difficulty: intermediate
---

Expiration laddering is the practice of distributing an [[options]] book's expirations across multiple weeks or months — rather than concentrating positions in a single expiry — in order to avoid [[gamma]] cliffs near expiration, smooth daily [[theta]] income, and reduce [[assignment-risk|assignment-clustering risk]]. It is a standard portfolio construction practice among professional premium sellers. The principle is simple: a book whose risk all rolls off the same Friday is exposed to a single, concentrated event; a book that breathes through expirations week after week behaves more like an annuity.

## The Problem That Laddering Solves

A premium-selling book — short [[straddle-strangle|strangles]], [[iron-condor|iron condors]], short puts, or ratio calendar spreads — looks placid for most of its life. The Greeks change slowly, the daily P&L is small, and the trader collects steady [[theta]]. Then, in the final week of any given expiration, three things happen at once:

1. **[[Gamma]] explodes** — the rate of change of [[delta]] grows hyperbolically as time-to-expiry approaches zero
2. **Liquidity thins** — bid/ask spreads widen as market makers price in pin risk and assignment risk
3. **Assignment risk concentrates** — every short option that finishes [[in-the-money]] settles on the same Friday afternoon

A book holding 20 short strangles all expiring the same week experiences all three pressures simultaneously on a single underlying calendar event. A book with the same 20 strangles spread evenly across six weekly expirations experiences a steady, manageable trickle of these pressures every week. Laddering converts a cliff into a slope.

## The Gamma Cliff

[[Gamma]] for a near-the-money short option is roughly proportional to `1 / sqrt(T)` where T is time to expiration. The implication is dramatic:

| Days to Expiry | Relative Gamma (vs 45 DTE) |
|---------------:|---------------------------:|
| 45             | 1.00x                      |
| 30             | 1.22x                      |
| 21             | 1.46x                      |
| 14             | 1.79x                      |
| 7              | 2.54x                      |
| 3              | 3.87x                      |
| 1              | 6.71x                      |
| 0 (intraday)   | unbounded                  |

A position that is comfortably sized at 45 [[days-to-expiration|DTE]] becomes terrifying at 3 DTE *without the trader doing anything*. Time alone has multiplied the gamma — and therefore the daily P&L variance — by ~4x. In the final hours, [[zero-dte-options|0DTE]] short options carry effectively unbounded gamma and can move from credit to max loss on a single 1% intraday move in the underlying.

If an entire book sits in the same expiration week, the book's gamma quadruples or quintuples in the final stretch as a single, correlated phenomenon. There is no escape via diversification across underlyings — every position is racing toward the same calendar wall.

A laddered book has only ~1/N of its positions in the danger zone at any one time, where N is the number of rungs. The remaining positions sit comfortably in their stable, low-gamma middle life. The book's *aggregate* gamma stays roughly flat over the calendar.

See [[gamma]] and [[gamma-scalping]] for the underlying mechanics.

## Concentration Risks

A single-expiry book carries three correlated risks that disappear under laddering:

### 1. Assignment Clustering

If 12 short puts on different underlyings all expire the same Friday and 4 of them finish [[in-the-money]], the trader receives 4 simultaneous assignment notices over the weekend, each requiring same-day Monday capital and stock-management decisions. The trader's brokerage may also auto-liquidate positions if margin runs short during the unsorted Saturday/Sunday window.

A laddered book sees at most 1-2 assignments in any given week, well-spaced and individually manageable. See [[assignment-risk]] and [[pin-risk]].

### 2. Theta Lumpiness

Most of an option's [[theta]] decay happens in the final 30 days, and the bulk of that in the final week. A book concentrated in one expiry generates almost no theta in weeks 1-3 of the cycle, then earns the bulk of its income in week 4. From a P&L attribution standpoint:

- The Sharpe ratio looks artificially high (low variance in early weeks, big spike in last week)
- Cash flow is unpredictable for capital-allocation purposes
- A loss in the last week wipes out the cycle's earnings before they were ever booked

A laddered book generates near-constant daily theta — see the [[#Theta Smoothing]] section below.

### 3. Front-Week Liquidity Drying Up

In the final 5 trading days, market makers reduce their willingness to take on the gamma risk of expiring options. Bid/ask spreads on the front week typically double or triple, and sometimes quadruple in the last 48 hours. A trader who waits until expiration week to roll positions pays this widened spread on every close.

A laddered book closes its [[#Roll Cadence|front rung]] at 21 DTE — well before the liquidity dries — and pays mid-market spreads. See [[options-liquidity]].

## Laddering Structure

Two common ladder structures dominate professional premium-selling:

### Standard 6-Rung Ladder (Monthly Cycle)

Equal weight across six expirations spaced ~7 days apart:

| Rung | DTE at entry | Position weight | Role |
|-----:|-------------:|----------------:|------|
| 1    | 7            | 1/6 of book     | Closing soon — about to roll |
| 2    | 14           | 1/6 of book     | Active management zone |
| 3    | 21           | 1/6 of book     | Standard close target |
| 4    | 28           | 1/6 of book     | Mid-life, low gamma |
| 5    | 35           | 1/6 of book     | Recently entered |
| 6    | 45           | 1/6 of book     | Newest rung |

Each Friday (or rolling weekly), the trader closes the front rung, recycles the capital, and opens a new 45 DTE position to refill the back. The ladder slides down by one week.

### Weekly Ladder (Aggressive Premium Capture)

One position per weekly expiration for 6 weeks. Useful for indices with deep weekly options markets ([[spx]], spy, qqq). Generates higher annualized [[theta]] but requires more active management because positions enter the gamma-cliff zone faster.

### Monthly Ladder (Lower Touch)

Equal weight at 30, 60, 90, 120 DTE. Easier to manage but loses the sweet spot of [[theta]] decay (which lives in the 21-45 DTE band). Better suited to longer-dated [[ratio-spread|ratio calendars]] or [[diagonal-spread|diagonals]] than to pure premium-selling structures.

### Hybrid: Long/Short Ratio-Calendar Ladder

Another approach spreads roughly 10 positions across 3-6 monthly expirations with ratio calendar spreads as the building block. The structure layers expiration laddering on top of long/short equity selection: every long-leaning position has a short-leaning counterpart on a different rung, balancing both directional and time exposure.

## Theta Smoothing

A toy example shows the difference clearly. Consider $6,000 of total credit collected from short premium, expressed as theta per day:

**Single-expiry book (all positions at 30 DTE on day 0):**

| Days elapsed | Theta/day | Cumulative income |
|-------------:|----------:|------------------:|
| 1-7          | $40       | $280              |
| 8-14         | $80       | $840              |
| 15-21        | $160      | $1,960            |
| 22-28        | $360      | $4,480            |
| 29-30        | $760      | $6,000            |

**Laddered book (6 positions at 7/14/21/28/35/45 DTE):**

| Days elapsed | Theta/day | Cumulative income |
|-------------:|----------:|------------------:|
| 1-7          | $200      | $1,400            |
| 8-14         | $200      | $2,800            |
| 15-21        | $200      | $4,200            |
| 22-28        | $200      | $5,600            |
| 29-30        | $200      | $6,000            |

Both books earn $6,000. The laddered book earns it as a near-constant flow rather than a back-loaded spike. From a [[risk-management]] standpoint:

- **Variance of daily theta** drops dramatically (from a multi-fold range to a flat line)
- **Maximum daily P&L exposure** drops because no single day is doing the heavy lifting
- **Cash flow becomes plannable** for taxes, withdrawals, and capital reallocation
- **Sharpe attribution** is no longer corrupted by a single-day spike

See [[theta-targeting]] for the broader framework of setting a target daily theta as a fraction of [[options-position-sizing|portfolio capital]].

## Vega and DTE Distribution

A back-month option carries more [[vega]] per dollar of premium than a front-month option. A 45 DTE [[at-the-money]] option might have vega of 0.18; a 7 DTE ATM option might have vega of 0.04. So a laddered book's vega is *not* evenly distributed across rungs — the back rungs carry more.

This is usually desirable because it concentrates [[implied-volatility|IV]] sensitivity in the longest-dated, most liquid options, where IV mean-reverts most reliably. But it has consequences:

| Risk | Effect on Laddered Book |
|------|-------------------------|
| **IV spike** | Back rungs lose more than front rungs (worst case for short premium) |
| **IV crush** | Back rungs gain more than front rungs (best case) |
| **Gamma cliff** | Front rungs dominate, back rungs almost unaffected |
| **Theta decay** | Front rungs decay faster per day, but back rungs decay much faster per week |

A common adjustment is to *underweight* the back rung in volatile environments — instead of 1/6, hold 1/8 in the 45 DTE rung and 1/4 in the 14 DTE rung. This trades smoother [[vega]] for slightly higher gamma exposure. See [[vega-budgeting]].

For ratio calendar spreads, the structure already builds in vega imbalance (long back-month vega, short front-month vega), so the ladder is constructed primarily over the long-leg expirations rather than the short-leg ones.

## Roll Cadence

The mechanics of *rolling* the front rung determine whether a ladder works in practice. Three common triggers:

### 1. Time-Based: Close at 21 DTE

The classic tastytrade rule. At 21 DTE, [[gamma]] starts to accelerate sharply but is not yet in the dangerous zone. Closing here:

- Captures the bulk of the [[theta]] decay (the steepest part of the curve up to that point)
- Avoids the gamma cliff
- Pays mid-market spreads (front-week liquidity hasn't dried yet)
- Forces a disciplined cadence — every position has a deterministic exit date

### 2. Profit-Based: Close at 50% of Max Credit

Independent of DTE — close as soon as the position has captured 50% of the credit received at entry. Backtest evidence (Source: [[tastytrade-mechanics-research]]) shows 50% profit-taking on short premium structures roughly doubles the Sharpe vs holding to expiration, because it reduces tail-loss exposure without giving up much theta.

### 3. Defensive: Close at Strike Test

If the underlying tags one of the short strikes, close immediately regardless of DTE or profit level. The position has lost its [[delta-neutral|delta-neutral]] character and is now a directional bet. Roll out to a new 45 DTE rung at fresh strikes.

### Combined "First-Trigger" Rule

In practice, professional traders use whichever fires first:

```
close_position when (DTE <= 21) OR (profit_pct >= 50%) OR (underlying_tagged_short_strike)
```

After closing, immediately open a fresh 45 DTE position to refill the back rung. The ladder slides forward by one rung. Capital is recycled within the same week. See [[trade-repair-and-rolling]].

## Worked Example: 6-Rung SPX Iron Condor Ladder

A trader runs a $250,000 portfolio of [[iron-condor|SPX iron condors]] using a 6-rung ladder. Each rung is a $50-wide condor sold at the 16-delta strikes (roughly 1 standard deviation OTM on each side).

### Initial Build

| Rung | Entry DTE | Credit | Position theta | Position vega |
|-----:|----------:|-------:|---------------:|--------------:|
| 1    | 7         | $1,000 | $90/day        | -$80          |
| 2    | 14        | $1,000 | $65/day        | -$140         |
| 3    | 21        | $1,000 | $50/day        | -$200         |
| 4    | 28        | $1,000 | $40/day        | -$260         |
| 5    | 35        | $1,000 | $30/day        | -$320         |
| 6    | 45        | $1,000 | $25/day        | -$420         |

**Aggregate book:**
- Total credit at risk: $6,000
- Total theta: ~$300/day
- Total vega: -$1,420 per IV point
- Max loss (all rungs simultaneously breach): $30,000 - $6,000 = $24,000 (~10% of account)

### Daily Behavior

Every day the book earns roughly $300 in theta, with low variance. The front rung (Rung 1) decays fastest but is also the closest to the [[gamma]] cliff. As days pass, each rung slides one position toward the front:

- Day 7: Rung 1 closes at 0 DTE (or earlier per roll cadence), Rung 6 (now 38 DTE) becomes the new Rung 5, and a fresh 45 DTE rung is added.
- Capital from closing Rung 1 funds the new Rung 6.
- Aggregate Greeks stay approximately constant.

### Comparison: Single-Expiry Book

If the same $6,000 of credit were concentrated in one 30 DTE expiration:

- Total theta: ~$200/day on day 0, growing to ~$1,200/day by day 28 (highly back-loaded)
- Total gamma: 6x higher in the final week than a laddered book on the same week
- Pin risk concentrates on a single Friday across 6 condors

The laddered book sacrifices ~30% in early-cycle theta in exchange for dramatically smoother variance and far lower [[tail-risk]]. For most premium sellers running [[options-position-sizing|properly sized]] books, this is the right trade.

## Ladder Structure Comparison

The three common ladder constructions trade off theta richness against management touch and gamma exposure. Choose by liquidity, account size, and the building-block structure:

| Structure | Rungs / spacing | Theta capture | Management touch | Gamma exposure | Best for |
|---|---|---|---|---|---|
| **Weekly ladder** | 6 rungs × ~7 DTE apart (7-45 DTE) | Highest annualised | High — rungs hit the gamma zone fast | Higher (short rungs near cliff sooner) | Deep weekly markets ([[spx]], spy, qqq) |
| **Standard 6-rung (monthly cycle)** | 6 rungs, ~7 days apart, slid weekly | High (lives in 21-45 DTE band) | Moderate — one roll per week | Balanced | The default premium-selling ladder |
| **Monthly ladder** | 30/60/90/120 DTE | Lower (misses the 21-45 DTE sweet spot) | Low | Lowest | [[diagonal-spread\|Diagonals]], [[ratio-spread\|ratio calendars]] |
| **Long/short hybrid** | 10 positions across 3-6 monthly expiries | Moderate, balanced by long/short pairing | Moderate-high | Balanced by construction | Ratio-calendar books |

### Single-Expiry vs Laddered: The Core Trade-Off

| Dimension | Single-expiry book | Laddered book |
|---|---|---|
| Daily theta profile | Back-loaded (spike in final week) | Near-constant flow |
| Aggregate gamma over cycle | Quadruples/quintuples into expiry | Roughly flat (only ~1/N in danger zone) |
| Assignment notices | Clustered on one Friday | 1-2 per week, spaced |
| Front-week liquidity cost | Pays widened spread on every close | Closes at 21 DTE before spreads widen |
| Sharpe attribution | Corrupted by single-day spike | Clean, low-variance |
| Capital required | 1x per-position size | ~6x (one full rung per week) |
| Early-cycle theta | Higher | ~30% lower (the price of smoothness) |

The single takeaway: **laddering converts a calendar cliff into a calendar slope**, trading a modest amount of early-cycle theta for a dramatic reduction in daily P&L variance and [[tail-risk]].

## Interaction with Volatility Carry

Expiration laddering is the portfolio-construction layer that makes systematic [[volatility-carry]] / [[variance-risk-premium|VRP]] harvesting survivable. A short-vol book that concentrates every position in a single expiry is short a single, correlated [[gamma]] event; the laddered version spreads that event across the calendar so that no single Friday — or single overnight gap — can detonate the whole book. The canonical short-vol carry rules (open new positions every 1-2 weeks, close at 21 DTE or 50% of max credit) *are* a laddering cadence. See [[volatility-carry]] for the full strategy and [[options-premium-selling]] for the broader category. For the instrument-level building block on the institutional side, the [[variance-swap]] (and its term-structure cousin the [[forward-variance-swap]]) plays an analogous role: laddering variance-swap tenors smooths the roll the same way option-expiry laddering smooths gamma.

## When NOT to Ladder

Laddering is a portfolio-construction principle for *recurring, theta-driven* books. It is the wrong choice when:

### 1. Directional Trades Tied to a Specific Thesis

If a trader buys [[long-call|long calls]] expecting a stock to rally over the next 6 weeks, the long-call expiration should match the thesis horizon — not be split across 6 weekly rungs. Splitting dilutes the directional payoff and adds management complexity. One thesis, one expiry.

### 2. Event Trades Sized to a Catalyst Date

If the trade is built around an earnings release, [[fomc]] decision, [[fda]] announcement, or [[sec-decision]], the expiration should be picked relative to the event — typically 1-2 weeks past the event date for short premium, exactly the event week for [[straddle-strangle|long straddles]]. Laddering across weeks dilutes the event capture.

### 3. Single-Position Calendar Spreads

A standalone calendar spread already carries an internal expiration structure (short near, long far). Laddering across multiple calendar spreads is fine; trying to ladder *within* one calendar makes no sense.

### 4. Tail Risk / Convex Long-Vol Trades

Long [[strangle|strangles]] or [[straddle|straddles]] held for [[volatility]] expansion are paying daily theta to wait for a vol spike. Laddering would force constant rolling and burn the structure. Single-expiry trades held to a defined event are correct here.

### 5. Capital-Constrained Accounts

A 6-rung ladder requires 6x the capital of a single position to maintain the same per-position size. Accounts under ~$25,000 generally cannot run a meaningful ladder with ratio calendars or [[iron-condor|iron condors]]; they should run a single rung and rotate.

## Common Mistakes

### 1. Laddering Across Uncorrelated Underlyings

Spreading 6 positions across AAPL, MSFT, AMZN, JPM, XOM, and TSLA is *diversification*, not laddering. The expirations all line up on the same monthly Friday. The book still has the gamma cliff. To get the laddering benefit, the *expiration weeks* must differ — picking different underlyings is a separate axis.

### 2. Letting the Front Rung Roll into 0DTE

A ladder is only as safe as its discipline. Traders who skip the 21 DTE close because "the position is still profitable" find themselves holding [[zero-dte-options|0DTE]] positions in week 1 with unbounded gamma. The whole point of the ladder is to *never* hold a position into the danger zone. Mechanical roll cadence — same DTE every cycle — eliminates this discretion.

### 3. Ignoring Expiration-Day Liquidity

Front-week SPX options may be liquid; front-week single-stock options on a small-cap name are often not. A trader who builds a ladder on a thinly-traded ticker discovers at 7 DTE that the bid/ask spread is 30%+ of the option price, and rolling the position destroys the [[theta]] earnings. Laddering only works on underlyings with real weekly or daily liquidity — [[spx]], spy, qqq, and the top ~50 single names by options volume.

### 4. Building the Ladder All at Once

A trader who opens all 6 rungs on day 0 has not built a ladder — they have built 6 positions that *will become* a ladder once the first rung is closed and rolled. For the first 6 weeks, the book behaves like a single-expiry book in stages. The clean way is to build gradually — open one new rung per week — accepting lower starting [[theta]] in exchange for proper structure from the start.

### 5. Re-Entering Strikes Too Aggressively After a Loss

When a rung closes at a loss because the underlying breached a short strike, the temptation is to immediately re-sell at the same delta on the new 45 DTE expiration. But [[implied-volatility]] has likely re-priced — the safer move is to either skip a cycle, reduce position size, or move further [[out-of-the-money|OTM]]. See [[trade-repair-and-rolling]] and [[when-to-retire-a-strategy]].

### 6. Confusing Laddering with Diversification

Diversification spreads risk across uncorrelated assets; laddering spreads risk across uncorrelated *time*. Both reduce variance, but they do not substitute for one another. A robust premium-selling book uses both axes simultaneously: 6 expiration rungs *and* 5-10 underlyings per rung, for a total of 30-60 positions managed as a single cash-flow engine.

## Tools

Most retail platforms offer calendar views that visualize expiration distribution. Useful tools:

| Platform | Feature | Notes |
|----------|---------|-------|
| IBKR | Portfolio expiration grid | Filterable by underlying and DTE |
| tastytrade | "Expirations" tab | Color-coded DTE buckets |
| [[optionnet-explorer]] | Risk graph by expiration | Best-in-class for ladder visualization |
| [[thinkorswim]] | "Beta Weighted" portfolio view | Shows aggregate Greeks by expiration |
| Custom Python ([[risk-management|risk-management]] tooling) | Pull positions via broker API, group by expiry | For traders who want full programmatic control |

The minimum useful view shows: each expiration on the x-axis, total position theta/vega/gamma per expiration on the y-axis. Any rung that is dramatically taller than the others signals a concentration that needs to be smoothed.

## Related

- [[options-portfolio-construction]] — broader framework for building options books
- [[options-risk-budgeting]] — allocating risk across Greeks and positions
- [[options-position-sizing]] — sizing individual positions within a portfolio
- [[theta-targeting]] — setting a target daily theta as a fraction of capital
- [[vega-budgeting]] — managing aggregate IV exposure
- [[pin-risk]] — the specific risk that laddering reduces near expiration
- [[assignment-risk]] — assignment-clustering risk
- [[gamma]] — the Greek whose cliff laddering is designed to avoid
- [[gamma-scalping]] — the opposite practice (deliberately taking on gamma)
- [[theta-decay]] — the decay curve that laddering smooths
- [[calendar-spread]] — the simplest two-rung ladder
- [[trade-repair-and-rolling]] — how to handle rungs that move against the book
- [[zero-dte-options]] — the danger zone laddering is designed to avoid holding into
- [[iron-condor]] — common structure laddered across expirations
- [[when-to-retire-a-strategy]] — kill criteria for a laddered book
- [[volatility-carry]] — the systematic short-vol strategy whose cadence is a laddering discipline
- [[variance-risk-premium]] — the premium a laddered short-premium book harvests
- [[options-premium-selling]] — the broader category laddering serves
- [[variance-swap]] — the institutional analogue; laddering variance-swap tenors smooths the roll

## Sources

- [[tastytrade-mechanics-research]] — empirical evidence for 21 DTE close and 50% profit-taking rules on short premium
- [[book-option-volatility-and-pricing]] — Natenberg's treatment of gamma and theta curves near expiration
