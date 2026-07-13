---
title: "Theta Targeting"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, itpm, income]
aliases: ["Theta Goal", "Daily Theta Target", "Theta Budgeting"]
related: ["[[options-risk-budgeting]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[portfolio-greeks-aggregation]]", "[[theta-decay]]", "[[options-premium-selling]]", "[[options-income]]", "[[variance-risk-premium]]", "[[expiration-laddering]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]", "[[theta-decay]]"]
difficulty: advanced
---

Theta targeting is the discipline of setting a desired daily [[theta]] income for a short-premium [[options]] book and sizing positions (see [[position-sizing]]) so the aggregate theta meets that target without breaching the [[vega-budgeting|vega budget]] or the book's [[delta]] and [[gamma]] limits. Where vega budgeting answers *"how much volatility risk can I take?"*, theta targeting answers the complementary question *"how much premium decay do I need to harvest, and is the structure of my book efficient at producing it?"*. Together the two form the core engineering loop of an income-seeking [[options-premium-selling|premium-selling]] portfolio in the [[itpm-trading-philosophy|ITPM]] tradition: vega is the constraint, theta is the objective, and every position is evaluated on how well it converts one into the other.

## Quick-Reference: The Four Metrics That Steer the Book

A theta-targeted book is governed by four numbers. Together they answer "am I earning enough, am I earning it efficiently, and how much path-risk am I carrying to do so?" Each is an aggregate computed via [[portfolio-greeks-aggregation]].

| Metric | Formula | Role | Illustrative guide rail |
|---|---|---|---|
| **Daily theta target ($/day)** | annual income target ÷ 252 (or 365) | The *objective* — how much decay the book is engineered to harvest | Derived top-down from an 8–18% annual return target on book capital |
| **Theta-to-vega ratio (T/V)** | \|portfolio [[theta]]\| ÷ \|portfolio [[vega]]\| | *Efficiency* — dollars of decay per dollar of vol risk | Floor of ~0.06; reject trades that pull it below ~0.05 |
| **Gamma-to-theta ratio (Γ/θ)** | \|portfolio [[gamma]]\| ÷ \|portfolio [[theta]]\| | *Path-risk* — how much convexity exposure you carry per unit of decay | Rises sharply as the book drifts front-cycle; a trending-up Γ/θ is an early theta-trap warning |
| **Realisation ratio** | actual P&L over a window ÷ cumulative target theta | *Honesty* — how much theoretical theta you actually keep | Sustained < 60% means edge is leaking to dealer [[gamma-scalping]] |

The objective (theta) is pursued *subject to* the constraints (T/V floor, Γ/θ ceiling, [[vega-budgeting|vega budget]]), and audited after the fact (realisation ratio). The rest of this page is the mechanics of each.

## Why Theta as a Target Instead of P&L

The instinctive metric for an income trader is daily mark-to-market P&L. It is also the wrong metric for steering a short-premium book on any horizon shorter than a month or two, because P&L is dominated by **path noise** that has nothing to do with the structural edge being harvested:

- **[[gamma|Gamma]] noise** — short-premium books are short gamma. A 1% move in the underlying re-prices the entire book, often by multiples of a day's theta. The P&L on any single day is mostly a quote on realised volatility, not a measurement of how much decay was captured.
- **[[vega|Vega]] noise** — a 1-point move in [[implied-volatility|IV]] revalues every option in the book. On an earnings week, vega P&L can swamp theta P&L by an order of magnitude.
- **Skew and term-structure noise** — even when ATM IV is stable, a steepening [[volatility-skew|skew]] or a shifting [[volatility-term-structure|term structure]] can mark the book up or down.

Theta is far less noisy. The decay that an option *should* shed in a calendar day is a deterministic function of its current price, [[time-to-expiration|DTE]], moneyness, and surface — given those inputs, theta is essentially a derivative of the [[black-scholes-model|Black-Scholes]] formula with respect to time. It is a smoother, more stable signal of *how much structural [[variance-risk-premium|variance-risk-premium]] the book is collecting*. P&L tells you what the market did to you yesterday; theta tells you what the book is engineered to earn if the world stays the same. As [[itpm-trading-philosophy|ITPM]] practitioners put it, *manage to theta, get judged on P&L*.

The corollary: an honest income trader tracks **realised theta capture** — actual P&L over a window divided by cumulative target theta — as a long-horizon scorecard. A book whose realised capture is consistently below 60% of its theoretical theta is leaking edge to gamma scalping by the dealers on the other side. See [[theta-realisation-ratio]] and [[gamma-scalping]].

## Setting the Daily Theta Target

The daily target is derived top-down from an annual return objective and the proportion of that return expected from premium-selling. A common ITPM-style framework:

1. **Annual return target from options income** — set as a percentage of options-allocated capital, typically **8–18% per year** for a diversified short-premium book trading index-options and large-cap equity options. Anything materially above 18% implies leverage, concentration, or a vega budget large enough to make the strategy a vol-selling fund rather than an income overlay.
2. **Convert to daily** — divide by ~252 trading days, or 365 calendar days if positions accrue weekend decay (most do).
3. **Express as $/day** — multiply by capital allocated to the book.

| Capital | Annual target | Calendar-day theta | Trading-day theta |
|---|---|---|---|
| $100,000 | 12% | $33/day | $48/day |
| $250,000 | 12% | $82/day | $119/day |
| $500,000 | 10% | $137/day | $198/day |
| $1,000,000 | 8% | $219/day | $317/day |
| $2,500,000 | 8% | $548/day | $794/day |

Two refinements practitioners make:

- **Buffer for realisation slippage**. If the historical realisation ratio is 70%, the theoretical theta target should be the income target divided by 0.7. A $82/day income target therefore becomes a $117/day *gross theta* target.
- **Carve out a vol-event reserve**. Set the running target ~20% below the long-run target so that the book has dry powder during [[implied-volatility|IV]] expansion regimes, when both opportunity and risk are highest.

The target is not a floor — there will be days, especially on the back side of an [[implied-volatility|IV]] crush, when getting back to target safely is impossible. It is a **steering reference** the book is rebalanced toward, not a quota.

## Theta-to-Vega Ratio (T/V)

The single most important efficiency metric in a short-premium book is the **theta-to-vega ratio**:

```
T/V = |portfolio theta ($/day)| / |portfolio vega ($/IV point)|
```

T/V measures how many dollars of decay the book captures per dollar of [[vega]] exposure it carries. A book with $100/day theta and $2,000 vega has a T/V of 0.05 — every IV point that ticks against it wipes out 20 days of decay. A book with $100/day theta and $500 vega has a T/V of 0.20 — only 5 days of decay are at risk per IV point.

Empirical ranges on liquid index products:

| T/V regime | Interpretation | Typical structures |
|---|---|---|
| < 0.04 | Inefficient — too much vol risk per unit of decay | Far-dated long-vol, calendar-heavy, skew trades, deep-OTM tails |
| 0.04 – 0.08 | Normal back-month short-premium | 60-90 DTE [[iron-condor|iron condors]], 45-60 DTE [[strangle|strangles]] |
| 0.08 – 0.15 | Sweet spot for a 30–45 DTE book | [[iron-condor|iron condors]], [[short-strangle|short strangles]], credit spreads |
| 0.15 – 0.30 | High-decay regime — late-cycle, gamma-heavy | 7–21 DTE structures, [[short-straddle|short straddles]], 0DTE [[iron-fly|iron flies]] |
| > 0.30 | Danger zone — gamma will dominate | 0DTE / [[zero-dte-options|0DTE]] short premium, [[pin-risk|pin-risk]] structures |

ITPM-style practitioners typically *target a T/V floor* — for example, **T/V > 0.06 at all times, and reject any new trade that would lower portfolio T/V below 0.05**. This forces the book to remain efficient even as the trader is tempted to "buy theta" by chasing front-week premium.

The intuition: in a vol-expansion event, vega P&L overwhelms theta P&L by orders of magnitude. The book that survives is the one that bought a lot of decay per unit of vega. T/V is the engineer's metric for that ratio.

See also [[gamma-to-theta-ratio]] for the complementary risk metric (path-risk per unit of decay).

## Theta Across DTE

Theta is not uniform across the [[time-to-expiration|expiration]] curve, and the *shape* of theta vs DTE is what creates the trade-off space.

### Front-week (0-7 DTE)

- **Theta is enormous in absolute terms** — an ATM weekly option might lose 30-50% of its value over a single trading day in the final 48 hours.
- **Gamma is also enormous** — gamma scales as 1/√t, so the same option that decays $50/day might take a $400 hit on a 1% move against you.
- **T/V looks great on paper but is fragile** — a small move in spot or IV reprices the position by far more than a day's theta.
- **Realisation ratio is poor** — front-week theta is what dealers actively scalp; realised P&L often comes in at 30-50% of theoretical theta on liquid products.

### 30–45 DTE — the sweet spot

This is the canonical short-premium window used by tastytrade, [[itpm-trading-philosophy|ITPM]] practitioners, and most published [[options-premium-selling|premium-selling]] research:

- Theta has begun its meaningful acceleration but [[gamma]] is still manageable.
- Vega per dollar of theta is reasonable — T/V typically lands in the 0.08–0.15 range.
- [[bid-ask-spread|Bid-ask spreads]] are tight on monthly cycles in liquid underlyings.
- Time to manage — a 30-DTE position can be adjusted, rolled, or closed without expiry pressure dictating the decision.

The classical heuristic is *"sell the front month, manage at 21 DTE"*: open at ~45 DTE and close or roll at ~21 DTE, before the gamma curve turns vertical. See [[expiration-laddering]] and [[managing-winners]].

### Back-month (60+ DTE)

- Theta in absolute terms is small — a 90-DTE ATM option may shed under $1/day.
- Vega is large — back-month options are nearly pure vega plays.
- T/V is low (often < 0.04), making them inefficient as decay vehicles in isolation.
- Useful as **diversifiers** of vol exposure (term-structure plays), as **wings** in [[iron-condor|iron condors]], or as the long leg in [[calendar-spread|calendars]] and [[diagonal-spread|diagonals]].

### Theta as a function of DTE — illustrative

For a $50 ATM option in a 20-vol environment:

| DTE | Approx theta ($/day) | Approx vega ($/IV pt) | T/V |
|---|---|---|---|
| 90 | 0.04 | 0.20 | 0.20 |
| 60 | 0.05 | 0.16 | 0.31 |
| 45 | 0.06 | 0.14 | 0.43 |
| 30 | 0.08 | 0.11 | 0.73 |
| 14 | 0.13 | 0.08 | 1.63 |
| 7 | 0.20 | 0.05 | 4.00 |
| 1 | 0.50 | 0.01 | 50.00 |

(*These are unitised per-contract values; the same shape holds at the book level.*) The T/V column is misleading without context — front-week T/V is high because [[gamma]] is the dominant risk, not vega. At 1 DTE, a 1% move in the underlying will dwarf the theoretical theta for the day. See [[gamma-explosion]].

## Adjustments When Below Target

A book consistently below target in a stable vol regime is **under-deployed** relative to its mandate. Standard responses, in order of preference:

1. **Add diversifying short-premium positions**. New names, new sectors, new expiry cycles. This adds theta without concentrating vega in any single underlying. See [[options-portfolio-construction]] and [[diversification-in-options]].
2. **Tighten short strikes inward** on existing structures. Selling 25-delta strangles instead of 16-delta strangles roughly doubles theta and credit, at the cost of higher [[probability-of-touch|touch probability]] and modestly higher vega. Acceptable if vega budget has room.
3. **Add front-cycle layers**. If the book is currently 45 DTE only, layer in a 21–30 DTE tranche to harvest the steeper part of the [[theta-decay-curve|decay curve]]. Done modestly, this raises T/V; done aggressively, it concentrates [[gamma]] risk.
4. **Increase position size proportionally** — only if the [[vega-budgeting|vega budget]] permits. The discipline is hard: never solve a theta deficit by violating the vega ceiling.
5. **Switch structures**. Replace a [[credit-spread|defined-risk credit spread]] (capped theta) with an [[iron-condor]] or [[short-strangle|short strangle]] (higher theta per unit of capital deployed) where the [[options-buying-power-reduction|buying power]] and tail-risk profile permit.

What **not** to do:

- Do not sell deep-OTM tails to "boost" theta. Far-OTM short options have tiny theta and disproportionate tail risk — terrible T/V, terrible [[expected-shortfall|expected shortfall]].
- Do not move into 0–2 DTE without explicit gamma sizing. Front-week theta is real but the realisation ratio is low and the path risk is unbounded. See [[zero-dte-options]] and [[the-theta-trap]] below.
- Do not double up on a single underlying just because it has rich [[implied-volatility|IV]]. Vega concentration trumps theta opportunity.

## Adjustments When Above Target

Counter-intuitively, **being well above the theta target is itself a signal to reduce risk**. Theta is a near-linear function of premium, and premium is a near-linear function of [[implied-volatility|IV]]. A book whose theta has surged 50–100% above target almost always reflects an [[implied-volatility|IV]] expansion that simultaneously:

- Inflated theta (numerator) — looks great.
- Inflated vega (denominator) — and vega is the risk.

T/V often does not improve much during a vol spike, because vega rises in tandem with theta. What changes is the **dollar magnitude of both**, which means both the reward *and* the path-risk of the book have grown. A trader who anchors only on theta will mistake the rich premium environment for free money and end up over-sized into the very regime where short-vol books detonate. See [[volatility-regime]] and [[volmageddon]].

The disciplined response when theta is well above target:

1. **Trim or close back-month vega** first, especially [[short-strangle|naked strangles]] where vega is largest. Closing back-month positions reduces vega faster than theta, which actually *raises* T/V.
2. **Shift into defined-risk** structures. Convert short strangles into [[iron-condor|iron condors]] by buying wings. Theta drops modestly, but [[expected-shortfall|tail risk]] drops a lot.
3. **Roll near-the-money short strikes outward** to re-centre delta and reduce gamma.
4. **Hold dry powder** rather than re-deploying immediately. Vol expansions usually mean-revert; the more attractive trade is often *after* the spike, with smaller size and richer terms.

A useful heuristic: when realised theta is more than ~150% of target for a given week, run a [[stress-test|stress test]] of the book through a 5-vol-point IV-up shock. If the simulated drawdown exceeds the [[vega-budgeting|vega budget]], reduce size mechanically until it does not, regardless of how much "income" is being foregone.

## The Theta Trap

The theta trap is the failure mode that catches every novice income trader and re-catches experienced ones in low-vol regimes. The mechanism:

1. The book is **below theta target**.
2. The trader looks for ways to "buy more theta" without thinking carefully about vega.
3. Two paths look attractive:
   - **Path A** — sell more front-week / 0DTE premium. Theta per contract is high, capital required is low. T/V looks fine on a static measurement.
   - **Path B** — sell premium in a low-IV underlying anyway, accepting thin credits.
4. **Path A** loads the book with [[gamma]]. The first 1.5σ move in the underlying produces a P&L hit equal to weeks of theta. Realisation ratio collapses.
5. **Path B** sells premium that is below the [[variance-risk-premium]] threshold — at low [[implied-volatility|IV]], the implied-vs-realised cushion is thin or negative. The trader is now selling vol that the market is *correctly* pricing, with no edge. See [[volatility-risk-premium-decay]].

Both paths "produce theta" in the daily snapshot. Neither produces *risk-adjusted* edge. The deeper failure is that theta on the screen is being treated as if it were income on the bank statement, when in fact it is a **theoretical accrual** that is only realised if [[gamma]] and vega behave themselves over the holding period.

Symptoms a trader is in the theta trap:

- DTE distribution of the book is collapsing toward the front cycle.
- T/V has been trending down for several weeks.
- [[gamma-to-theta-ratio]] has been trending up.
- Realisation ratio has been declining month over month.
- The trader is using phrases like *"I need to make up the income"* or *"there's just no premium out there"*.

The exit from the theta trap is to **lower the income target** until the vol regime improves. A 12% annual target in a 12-VIX environment is not the same trade as a 12% target in a 22-VIX environment — capacity is regime-dependent. Forcing the target through a low-vol regime is the single most reliable way to blow up a premium-selling book. See [[when-to-retire-a-strategy]] and [[volatility-regime-switching]].

## Worked Example — $50/Day Theta Target on a $150K Book

**Account**: $150,000 dedicated to a short-premium overlay.
**Annual income target**: 12% → $18,000/year → ~$50/day calendar-day theta.
**Vega budget**: $1,500 per IV point (1% of account = max acceptable loss on a 1-point vol shock).
**T/V floor**: 0.06.
**Universe**: SPX index options (no single-name idiosyncratic risk).

### Step 1 — Pick a base structure.

Sell 45-DTE SPX [[iron-condor|iron condors]], 16-delta short strikes, 50-point wings. Per contract, in a 16-VIX environment:

- Credit: ~$6.50
- Theta: ~$13/day
- Vega: ~$110/point
- Max loss: $50 wing − $6.50 credit = $43.50/contract = $4,350
- T/V (per contract): 13/110 = **0.118** — comfortably above floor.

### Step 2 — Size to the target.

Theta needed: $50/day. Per contract: $13/day. → **4 iron condors**.

Aggregate book Greeks at entry:
- Theta: $52/day. Hits target.
- Vega: $440/point. Well below $1,500 budget — 30% utilisation.
- Buying power reduction: ~$17,400. ~12% of account. Plenty of dry powder.
- T/V: **0.118**. Healthy.

### Step 3 — Stress test.

| Scenario | Approx P&L |
|---|---|
| 1-day, +1% SPX, IV flat | −$200 (gamma, partly offset by theta) |
| 1-day, −2% SPX, IV +3 pts | −$1,800 (gamma + vega) |
| 5-day drift, IV flat | +$260 (theta) |
| 1-day, IV +5 points (vol shock) | −$2,200 (vega) |
| Black-Monday tail (−7%, IV +20) | -$10,000+ (max loss approached on put side) |

The 5-pt vol shock exceeds the daily [[vega-budgeting|vega budget]] but is within the worst-case wing-defined max loss. Acceptable for the mandate.

### Step 4 — VIX moves from 16 to 22 a week later.

New per-contract values (existing positions, partly aged):
- Theta has risen to ~$18/day per contract.
- Vega has risen to ~$130/point per contract.

Aggregate book at this point (still 4 condors, but with running P&L of -$1,400 from the vol expansion):
- Theta: $72/day — **44% above target**.
- Vega: $520/point — still under budget, but climbing.
- T/V: 0.138 — slightly improved (theta grew faster than vega in the short window).

The discipline says: *do not add more contracts to "lock in" the rich premium*. The book is already over its theta target, and the existing positions now carry meaningfully more vega in dollar terms. The correct adjustment:

1. **Close one condor at a small loss**. Removes ~$130 vega and ~$18 theta.
2. **Roll one condor's untested side closer** to harvest more theta on the put side without adding new contracts.
3. **Open one new 60-DTE condor at the higher IV**, locking in richer premium for the next decay cycle while shifting the DTE ladder.

Post-adjustment: theta back near $55/day, vega around $400/point, T/V ~0.14, [[expiration-laddering|DTE laddered]] across 25 / 45 / 60. The book is still on target, has captured the [[implied-volatility|IV]] expansion as new premium rather than as mark-to-market loss, and has not exceeded its vega budget at any point.

### Step 5 — A week of calm; target slips to $40/day.

Two condors have aged into their [[managing-winners|profit-take zone]] (50% of max profit). They are closed for ~$650 each. Theta drops to ~$25/day temporarily. Two new 45-DTE condors are opened at the prevailing (now lower) IV. The book returns to ~$50/day theta with refreshed DTE.

This is the **steady-state cadence** of a theta-targeted book: open, age, harvest, close at a profit threshold, redeploy. The target is the steering rudder, not a quota — the book is allowed to drift below target during quiet weeks and is forcibly trimmed during loud ones.

## Connection to Position Sizing

Theta targeting and [[position-sizing]] are two ends of the same calculation, approached from opposite directions. Conventional [[position-sizing]] starts from *risk* ("how much can I lose on this trade, and what fraction of equity is that?") and backs into a contract count. Theta targeting starts from *reward* ("how much decay do I need per day?") and also backs into a contract count. A correctly run book sizes each position so that **both** answers agree — the contract count that delivers the needed theta must simultaneously sit inside the per-trade risk budget, the [[vega-budgeting|vega budget]], and the worst-case [[options-stress-testing|stress]] tolerance.

The reconciliation, in order of precedence:

1. **Risk caps bind first.** Compute the contract count theta *wants* (target $/day ÷ per-contract theta). Then check it against the hard sizing limits — per-trade max loss (commonly the 1–2% rule, see [[position-sizing]]), the [[vega-budgeting|vega ceiling]], [[options-concentration-risk|single-name and sector concentration]] limits, and the [[options-stress-testing|stress-test]] tolerance. **Whichever produces the smaller size wins.** Theta is never a reason to exceed a risk cap.
2. **The vega budget is the active constraint most of the time.** Because theta and vega scale together, the size that hits a theta target usually also defines the vega draw. If that vega draw breaches the budget, the deficit is solved by *adding diversifying positions* (which raise theta without concentrating vega) or by accepting a lower target — never by oversizing one name.
3. **[[portfolio-margin|Portfolio margin]] is a financing constraint, not a risk metric.** Buying-power reduction tells you whether a position *fits*, not whether it is *safe*. A book can be well inside its margin limit and still be wildly oversized on a [[options-stress-testing|stress]] basis. Size to the stress number and the Greeks, then confirm it fits in margin — not the reverse.
4. **Beta-weighted [[delta]] is the directional governor.** A short-premium book accretes [[delta]] as strikes are tested and rolled. Aggregate beta-weighted [[delta]] (see [[portfolio-greeks-aggregation]] and [[beta-weighted-delta]]) must stay inside the directional budget independent of the theta target; a book that is hitting its theta number but has drifted to a large net long or short [[delta]] is no longer the market-neutral income engine it was sized to be.

In short: **theta sets the size you want; [[position-sizing]] sets the size you are allowed.** When they conflict, the risk cap wins and the income target is lowered to match — exactly the [[the-theta-trap|theta-trap]] discipline. See [[options-position-sizing]] for the Greeks-based sizing mechanics this depends on, and [[trade-repair-and-rolling]] for how to adjust a position whose [[delta]] or vega has drifted without resizing the whole book.

## Process Checklist

A theta-targeted book runs on a repeatable cadence rather than ad-hoc reaction. The discipline is to look at the *steering metrics* before the P&L.

### Daily

1. **Aggregate the book Greeks.** Pull net [[theta]], [[vega]], [[gamma]], and beta-weighted [[delta]] via [[portfolio-greeks-aggregation]]. P&L is read *last*, not first.
2. **Read theta vs target.** Below target → note it but do not chase intraday. Well above target → flag for risk reduction (the [[#Adjustments When Above Target|over-target playbook]]).
3. **Check the constraints.** T/V above its floor? Γ/θ stable, not trending up? [[vega-budgeting|Vega]] inside budget? Beta-weighted [[delta]] inside the directional band?
4. **Run the stress matrix.** A quick [[options-stress-testing|stress test]] — at minimum a ±5 [[volatility|IV]]-point shock and a 2σ spot move — to confirm the worst case is still survivable. The book changes even on days you don't trade.
5. **Manage tested strikes.** Roll or close anything that has breached its management trigger (e.g. 21 DTE, or a short strike tested) per [[trade-repair-and-rolling]].

### Weekly

1. **Review the realisation ratio.** Actual P&L over the trailing window ÷ cumulative target theta. A declining ratio is the canonical early signal of the [[the-theta-trap|theta trap]].
2. **Inspect the DTE ladder.** Is the book collapsing toward the front cycle? Re-ladder via [[expiration-laddering]] if so.
3. **Harvest winners.** Close positions that have reached the profit-take threshold (commonly 50% of max profit, see [[managing-winners]]) and redeploy into fresh DTE.
4. **Confirm diversification.** Check [[options-concentration-risk|concentration]] across name, sector, and vol-regime — eight short strangles in one sector is one position, not eight.

### Regime-change (event-driven)

1. **On a [[volatility|vol]] spike**, do not add to "lock in" rich premium. Trim back-month [[vega]] first, shift toward defined-risk structures, and hold dry powder for after the mean-reversion.
2. **On a [[volatility|vol]] collapse**, *lower the income target* rather than forcing it through a low-[[variance-risk-premium]] regime. Capacity is regime-dependent.
3. **Around known events** (earnings, [[fomc-meetings|FOMC]], CPI), shape the [[expiration-laddering|DTE ladder]] to span or avoid the date deliberately, and do not count pre-event theta as collected income.

## Theta Seasonality

Theta is not constant across the calendar. Several seasonality effects significantly affect both the realised decay and the appropriate target.

### Weekend decay

Most pricing models bake in some weekend decay — Friday afternoon premiums are typically lower than they would be without the weekend skip. But the **distribution** of weekend decay is asymmetric: pricing models partially anticipate it, so Friday close → Monday open theta is usually only 1.5–2x a normal day's theta, not 3x. Traders who naively expect "three days of theta over the weekend" overestimate Saturday-morning P&L. See [[weekend-effect]] and [[gap-risk]].

### Holiday decay

Around major US market holidays, several effects compound:

- **Anticipated decay** — dealers mark down extrinsic in advance of the closure.
- **IV compression** — short-dated IV often sags into long weekends.
- **Realised pin** — illiquid pre-holiday tape often produces small drift, which favours short premium.

The effect is to flatter realised P&L versus theoretical theta in the days *around* a holiday, then to claw some of it back when the market reopens.

### Pre-earnings IV ramp

In single-name options, [[implied-volatility|IV]] rises into earnings as the market prices in the binary event. The mechanical effect on theta:

- Premium **rises**, so theta per contract rises in absolute terms.
- But the IV ramp is a vega *headwind* — the position is bleeding to vega expansion at the same time it is accruing theta.
- **Realised** decay is muted or negative in the days before earnings; the genuine decay only arrives in the post-earnings IV crush.

ITPM-style premium sellers either avoid earnings windows entirely (dodge the binary event) or explicitly trade earnings-iv-crush as a separate strategy with its own sizing rules. For a normal income book, do not count pre-earnings theta as collected income — it is unrealised and at risk to the announcement.

### Macro events and central-bank dates

[[fomc-meetings|FOMC]] decisions, CPI prints, NFP, ECB meetings — each compresses or expands the [[volatility-term-structure|vol term structure]] in characteristic ways. A book with material exposure across one of these dates has a distorted theta profile in the lead-up; the genuine decay arrives after the event. Practitioners often **shape the DTE ladder** to either span or avoid these dates depending on the desired exposure.

### Holiday calendar effect on annualisation

The conversion from annual return target to daily theta should use **calendar days** for positions that decay over weekends (most short-premium positions), and **trading days** only for positions that are flat over weekends (rare in a passive income book). A 12% annual target on $250K is $82/day calendar-day theta or $119/day trading-day theta — the same target, but tracked on different denominators depending on whether the book holds positions through weekends.

## Tools

Modern brokers and analytics platforms expose portfolio theta directly:

- **Broker-native dashboards**:
  - [[thinkorswim]] — *Beta Weighting* + *Position Statement* shows aggregate theta, vega, and delta for the book in real time, beta-weighted to spy or another benchmark.
  - [[tastytrade-platform|tastytrade]] — *Portfolio Greeks* widget; the platform's *theta/day* number is the canonical reference for many tastytrade practitioners.
- **Dedicated analytics**:
  - orats — historical IV surfaces, [[backtesting|backtested]] theta-targeted strategies, scenario analysis. Useful for evaluating T/V and realisation across long histories.
  - [[optionnet-explorer]] — granular what-if analysis for portfolio Greeks over a planned holding period; supports [[expiration-laddering|DTE laddering]] visualisation.
  - [[deribit-position-builder]] — for crypto-options books, exposes equivalent portfolio-Greeks views.
- **Spreadsheet workflow** — many discretionary traders maintain a simple sheet with one row per position (DTE, short delta, theta, vega, max loss) and SUMs at the bottom for portfolio theta, vega, and T/V. This is sufficient for a 5–20 position book and forces the trader to confront each line item.

What to look for in a tool:
- Aggregate theta and vega across heterogeneous underlyings.
- T/V as a derived field, ideally with historical time series.
- DTE-bucketed views (front cycle vs back cycle).
- Stress scenarios for ±IV shocks and ±spot moves.
- Realisation tracking — actual P&L vs cumulative theoretical theta over a window.

## Related

- [[options-risk-budgeting]] — the umbrella discipline; theta target sits inside it.
- [[vega-budgeting]] — the complementary constraint to theta targeting.
- [[options-portfolio-construction]] — how the book is structured to deliver target theta efficiently.
- [[portfolio-greeks-aggregation]] — mechanics of summing Greeks across positions.
- [[theta-decay]] — the underlying phenomenon being harvested.
- [[options-premium-selling]] — the strategy class theta targeting governs.
- [[options-income]] — income-overlay framing for theta-targeted books.
- [[variance-risk-premium]] — the structural edge that makes long-run theta capture possible.
- [[expiration-laddering]] — diversifying across DTE buckets to smooth theta and vega.
- [[gamma-to-theta-ratio]] — the path-risk sister metric to T/V.
- [[managing-winners]] — closing at 50% of max profit as a realisation-locking rule.
- [[itpm-trading-philosophy]] — the methodological context most practitioners come from.
- [[options-position-sizing]] — Greeks-based sizing on which theta targeting depends.
- [[position-sizing]] — the general risk-first sizing discipline theta targeting must reconcile with.
- [[volatility-regime]] — why the right target is regime-dependent.
- [[zero-dte-options]] — the front-end of the theta trap.
- [[options-stress-testing]] — the worst-case check that bounds how much theta you may safely size for.
- [[portfolio-margin]] — the financing constraint a theta-targeted book sits inside.
- [[options-concentration-risk]] — why a high-theta book can still be one undiversified bet.
- [[trade-repair-and-rolling]] — adjusting drifted positions without resizing the whole book.
- [[value-at-risk]] — statistical risk metric complementary to the theta/vega steering numbers.
- [[volatility]] — the underlying driver of both the premium harvested and the risk carried.
- [[risk-management]] — the broader discipline theta targeting operates within.

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on theta, gamma, and the structure of decay across DTE.
- [[itpm-trading-philosophy]] — institutional-style portfolio construction with explicit theta and vega targets.
- orats-research — historical [[backtesting|backtests]] of theta-targeted index condor strategies.
