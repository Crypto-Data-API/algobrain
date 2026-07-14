---
title: "Options Portfolio Construction"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, portfolio-theory]
aliases: ["Building an Options Book", "Options Book Construction"]
related: ["[[options-risk-budgeting]]", "[[portfolio-greeks-aggregation]]", "[[vega-budgeting]]", "[[theta-targeting]]", "[[expiration-laddering]]", "[[options-concentration-risk]]", "[[options-stress-testing]]", "[[portfolio-margin]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[options-position-sizing]]", "[[options-greeks]]"]
difficulty: advanced
---

Options portfolio construction is the discipline of running a *book* of options positions as a single coordinated risk system rather than as a stack of independent trades. Where [[options-position-sizing]] answers "how big should this trade be?", portfolio construction answers the harder question: "given the trades I already have on, what does *this* one do to my net risk, and is that something I want?" Professional trading desks treat this as the dividing line between hobbyists, who size each trade in isolation, and professionals, who size each trade against a pre-budgeted portfolio.

## Why a Portfolio View Matters

The single most common error among self-taught options traders is treating each position as an independent risk. Three positions that look diversifying on paper routinely stack into a single concentrated bet at the book level:

1. **Correlated short vega.** A short iron condor on SPY, a short strangle on QQQ, and a covered call on AAPL are not three independent premium-selling trades. They are one massive short-vol position, because index IV and large-cap single-name IV are 80%+ correlated. When VIX spikes, all three lose together. Position-level Greeks reported by the broker are misleading; the trader has to mentally aggregate to a beta-weighted view (see [[portfolio-greeks-aggregation]]).
2. **Expiration cliffs.** Each individual trade was sized to a 1-2% risk budget on its own expiry. But if the trader keeps reaching for the same monthly because it has the most liquidity, the book ends up with 60-80% of theta and gamma loaded onto a single Friday. A normal pin-risk move on that one expiry produces a portfolio-level loss far larger than any single trade's max loss. The fix is [[expiration-laddering]].
3. **Sector overlap.** Five "different" tech names — NVDA, AMD, AVGO, MU, TSM — are one semiconductor bet. Five "different" energy names are one oil bet. The illusion of breadth disappears the moment a sector ETF moves 4%.
4. **Hidden directional exposure.** Each trade was put on as "delta-neutral at entry," but six weeks later, after the underlyings have drifted, the book carries thousands of net deltas. Without portfolio-level monitoring, this drift is invisible.
5. **Correlated tail risk.** The actual loss-generating event is rarely the small move you sized for; it's the gap, the FOMC, the earnings cluster, the index reweight. These events hit *every* position at once.

A portfolio view exists to convert these hidden stack-ups into explicit, budgeted exposures. If you want net short vega across the book, fine — but it should be a deliberate choice with a number attached, not an emergent consequence of putting on whatever looked attractive that week.

## The Top-Down Portfolio Framework

Institutional books are built through a strict top-down construction sequence. Every position is a *child* of a higher-level decision, and every higher-level decision constrains what positions are allowed:

```
1. Macro thesis        →  net long / short / flat the world
2. Geographic split    →  US / EU / EM / Japan weights
3. Sector allocation   →  which sectors to overweight long, which to short
4. Name selection      →  strongest names in long sectors, weakest in short
5. Structure           →  options structure that matches view + vol regime
6. Sizing              →  Greeks contribution against pre-set portfolio limits
7. Hedge layer         →  beta / vega / sector hedges to clean up unwanted risk
```

At the portfolio level, steps 6 and 7 are the construction work. The first five stages produce a *candidate* trade. The portfolio framework decides whether and how to *fit* it into the existing book.

The key principles for the portfolio layer:

- **Professional-grade discipline.** Set the risk limits *before* the market opens, write them down, and reject any trade that breaches them — even if the trade looks good. Most retail traders override their own rules in the moment; a disciplined framework treats this as the central skill to defeat.
- **Greeks dominate dollar P&L thinking.** A "small" trade by premium can be a "large" trade by vega or gamma. Always size against the relevant Greek for the strategy, not just the cash outlay (see [[options-position-sizing]]).
- **Net before gross.** Every metric is computed at the *book* level first. Position-level numbers are an input, not a target.
- **Hedges are explicit positions.** Don't assume "the longs hedge the shorts." Compute the residual and decide whether you want it.
- **Sleep test.** If the realistic worst-day P&L (from the stress scenarios below) is a number that would change your behavior tomorrow, the book is too big — independent of whether each individual trade was correctly sized.

## Building Blocks: The Five Pre-Trade Inputs

Before any new trade is considered, the trader has set five numbers for the portfolio. These are not derived from the next trade — the next trade is filtered through them.

### 1. Maximum Portfolio Vega

The total dollar P&L per 1-vol-point move in implied volatility, aggregated across the book and (ideally) beta-weighted to a single benchmark like SPY or VIX.

A typical book budget for a $250K account:
- Net long vega: up to +$2,000 per vol point (i.e., a 5-vol crush costs $10K, or 4% of the account)
- Net short vega: up to -$1,500 per vol point (a 10-vol spike costs $15K, or 6%)

The asymmetry is deliberate: short vega has unbounded loss potential during stress events and a fatter left tail than long vega does on the right tail. Professional books typically run flat-to-slightly-long vega in compressed VIX regimes and flat-to-slightly-short vega in elevated VIX regimes (see [[volatility-regime-classification]] and [[variance-risk-premium]]).

The vega number is checked daily, beta-weighted, and broken down by tenor bucket: front-month vega behaves very differently from 90-day vega, and a "flat vega" book that's actually short front-month and long back-month is a [[expiration-laddering|term structure trade]] in disguise. See [[vega-budgeting]] for the full sub-buckets.

### 2. Theta Target

The intended daily P&L from time decay, expressed in dollars per day and as a percentage of capital.

Common targets:
- Theta-positive book: +0.10% to +0.25% of capital per day net theta
- Theta-neutral book: |theta| < 0.05% of capital per day
- Theta-negative book: -0.10% to -0.30% per day (paying for long convexity)

A $250K account with a +0.20%/day theta target is collecting +$500/day, or roughly +$10K/month before P&L from gamma, vega, and direction. The trap is that theta and short vega are usually two ways of describing the same exposure: a trader who chases a $700/day theta target on a $250K book has, by construction, taken on a vega exposure that will lose $20K-$40K in any meaningful vol spike. [[theta-targeting]] discusses the right way to set this number against an explicit vega budget rather than instead of one.

### 3. Maximum Expiration Concentration

The cap on Greeks (especially gamma and theta) loaded into any single expiry.

A defensible rule:
- No single expiration carries more than 30-40% of total book theta
- No single expiration carries more than 25-30% of total book gamma
- No two consecutive weekly expiries together carry more than 50% of total book gamma

The reason is structural: expiration week gamma explodes, pin risk concentrates, and any single news event (CPI print, FOMC, earnings) on that day moves the entire stack at once. [[expiration-laddering]] shows how to spread tenor across weekly, monthly, and quarterly buckets.

### 4. Maximum Sector Concentration

The cap on net Greek exposure to any single sector or correlated group.

Typical rules:
- No more than 25% of net beta-weighted delta in any one GICS sector
- No more than 30% of net vega in any one sector (especially relevant for tech and energy, which have distinct vol regimes)
- No more than 15-20% of total max-loss exposure in correlated themes (e.g., "AI winners," "China reopening," "rate-sensitive REITs")

This prevents the "five different tech names = one semi bet" trap. A trader who is long calls on NVDA, MSFT, GOOGL, META, and AMZN does not have five trades; they have one mega-cap-tech long. See [[options-concentration-risk]].

### 5. Maximum Single-Name Notional

The cap on dollar notional exposure (not premium) to any single underlying.

Notional matters because options give leveraged exposure to the underlying price, not just the premium paid. A trader long 10 ATM AAPL calls at $5 has paid $5,000 but controls roughly $180,000 of AAPL stock — a 6% gap on AAPL is a $10,800 P&L event regardless of the premium. Professional books typically cap single-name *notional* exposure (delta × shares × price, summed across all positions on that name) at 5-10% of account.

## Risk Limits

The five pre-trade inputs above collapse into a single written limit sheet that the book is measured against every morning. The exact numbers are a function of account size, vol regime, and risk appetite — the figures below are *illustrative for a hypothetical $250K discretionary book in a low-vol regime*, not prescriptions or real data. The point is the structure: a number on every axis, with an action attached when it breaches.

| Axis | Illustrative limit ($250K book) | Beta-weighted to | Breach action |
|------|---------------------------------|------------------|---------------|
| Net vega | flat-to-+$2,000 (long) / -$1,500 (short) per IV pt | SPX/VIX | Stop adding short premium; add long vega — see [[vega-budgeting]] |
| Net beta-weighted delta | ±2% of NLV per 1% SPX move | SPX | Hedge with ES futures or index options |
| Theta target | +0.10% to +0.25% of NLV/day | — | Re-check vega; theta and short vega are the same trade — see [[theta-targeting]] |
| Single-expiry gamma | ≤ 25-30% of book gamma | per expiry | Roll/close concentrated expiry — see [[expiration-laddering]] |
| Single-expiry theta | ≤ 30-40% of book theta | per expiry | Ladder tenor |
| Sector net delta | ≤ 25% of net beta-wtd delta | per GICS sector | Trim or sector-hedge — see [[options-concentration-risk]] |
| Sector net vega | ≤ 30% of net vega | per sector | Diversify vol exposure |
| Single-name notional | ≤ 5-10% of NLV | per underlying | Cap or restructure |
| Cumulative max-loss | ≤ 15-25% of NLV | book | Reduce open positions |
| Stress drawdown (2σ) | ≤ 8-12% of NLV | book | [[stress-test]]; cut the binding Greek |
| 95% daily VaR | ≤ 3-5% of NLV | book | Reduce gross or hedge — see [[value-at-risk]] |

Two governance rules sit above the table. First, **keep each axis at 60-70% of its limit in normal conditions** so there is headroom to add hedges or absorb an adverse move without triggering forced action across multiple axes at once. Second, **every limit maps to a pre-committed action** — a limit with no action attached is decoration, not risk management (see [[risk-management]]).

## Position Layering

When a new trade is proposed, the construction question is not "is this a good trade?" but "what does the book look like *after* I put this on?"

The mechanical process:

1. Compute current book Greeks (delta, gamma, vega, theta), beta-weighted and broken down by sector and expiry.
2. Compute the candidate trade's contribution to each Greek bucket.
3. Compute *post-trade* book Greeks.
4. Check post-trade values against all five pre-trade limits.
5. If any limit is breached, the choices are:
   - **Skip the trade.** Highest discipline, lowest opportunity.
   - **Resize the trade** down so the post-trade book stays in budget.
   - **Restructure the trade** to express the same view with different Greeks (e.g., swap a long ATM call for a debit spread to halve the vega).
   - **Adjust the existing book** — close or hedge a different position to make room. This is preferred when the new trade is a higher-conviction expression of the existing view.

The crucial insight: net Greeks beat individual Greeks for risk decisions, but individual Greeks still matter for *attribution*. You want to know not just "the book is short $1,200 of vega" but "the book is short $2,000 of vega from the SPY iron condor and long $800 of vega from the AMZN earnings calendar." When vol moves, you need to know which leg drove the P&L.

A common trap: layering trades that each individually pass the limits but collectively land at the limit on every dimension. A book at 95% of vega budget, 95% of theta budget, 95% of single-name notional, and 95% of sector concentration is *not* a robust book — any small adverse move pushes multiple metrics into breach simultaneously, removing the trader's ability to add hedges or new positions during stress. Disciplined risk practice keeps each axis at 60-70% of limit so there's room to maneuver.

## Hedging at the Book Level vs Trade Level

The hedge decision lives in two places:

### Trade-Level Hedges
A trade-level hedge is part of the structure itself: a long put bought against a long stock position, the short call wing of a vertical spread, the protective long wing of an iron condor. These hedges are decided when the trade is constructed and don't aggregate cleanly with other trades.

Use trade-level hedges when:
- The hedge is conditional on a specific catalyst tied to that name (earnings, FDA decision)
- The position is a defined-risk structure where the hedge defines the max loss
- The underlying has idiosyncratic tail risk uncorrelated with the broader book

### Book-Level Hedges
A book-level hedge is a single overlay position designed to neutralize an unwanted aggregate exposure across many positions. Examples:

- **Net delta hedge.** The book has +1,400 net beta-weighted deltas after a week of drift. Sell 3 ES futures (each ~$240K notional, ~480 SPY-equivalent deltas at current SPY) to flatten. Cheaper, cleaner, and more capital-efficient than trying to delta-hedge each individual position with stock.
- **Net vega hedge.** The book is short $1,800 of vega, mostly from premium-selling trades. Add a small VIX call position or buy long-dated SPX puts to take some short vega off without unwinding the income trades.
- **Tail hedge.** The book is short premium across many names. Buy a small package of OTM SPY puts 60-90 DTE — too small to matter in normal markets, but that pays multiples in a crash.
- **Sector hedge.** Net long $80K of beta-weighted tech delta. Short some QQQ shares or buy QQQ puts as a sector overlay.

The rule: hedge at the level where the risk lives. If five positions each have idiosyncratic tail risk, hedge each one. If five positions all have the same systematic short-vol risk, hedge once at the book level.

Book-level hedges are where professional construction differs most from retail. Retail traders typically hedge each trade individually and end up with hedge premium drag of 2-4x what's needed. Professional books concentrate hedging into one or two efficient overlays, often using futures (for delta) and index options (for vol/tail), because index vol is consistently cheaper than the basket of single-name vols.

## Capital Allocation: Per-Trade vs Total-Risk

Two distinct percentages, frequently confused:

**Per-trade capital at risk.** The maximum dollar loss on a single trade as a fraction of total account. Common professional practice: 1-2% per trade for directional discretionary, 0.5-1% per trade for premium-selling positions (because their tail loss is larger than their stated max-loss in any non-defined-risk structure, and even defined-risk losses cluster in correlated stress events).

**Total portfolio risk.** The fraction of total account at risk *across all simultaneous positions* under a stress scenario. This is the sum that actually matters and is often missed by retail.

The math illustrates why:

A $250K account running 20 trades each at 2% max-loss has $100K (40%) in cumulative max-loss exposure. In normal markets, max losses are uncorrelated and the *expected* drawdown is far smaller. But in a correlated stress event (March 2020, August 2024 yen carry unwind, any future volatility shock), losses correlate sharply, and the expected drawdown approaches the cumulative max-loss number. A 40% drawdown on a 20-trade book is not a tail event — it's the natural consequence of treating max-loss as an independent number per trade.

Standard rules:
- Cumulative max-loss across all open positions: cap at 15-25% of account
- Expected portfolio drawdown in a 2-sigma stress (computed via stress test): cap at 8-12% of account
- Single-day VaR (95th percentile): cap at 3-5% of account

The expected-loss framing matters more than max-loss. A $1,000 max-loss trade with a 70% win rate and 2x average win/loss has a much smaller risk contribution than a $1,000 max-loss trade with a 30% win rate and 0.5x ratio, even though they have identical max-loss. Sizing on max-loss alone over-allocates to high-win-rate, fat-left-tail trades — exactly the failure mode that destroys premium-selling accounts.

## Review Cadence

A well-run book imposes three nested review loops:

### Daily: Greeks Check
Five-to-ten minute review every trading morning before the open:
- Current net beta-weighted delta, gamma, vega, theta (all five from the limits above)
- Largest single-name notional exposures (top 5)
- Top three sector concentrations
- Theta vs. yesterday's theta (rate of decay tells you whether you're in the meat of expiry or not)
- Any expiry within 7 DTE that has more than 20% of book gamma (if so, plan close/roll today)
- Overnight news scan for any underlying in the book

The output of the daily check is a written list of *required actions* for the day, not a feeling. Actions are: close X, roll Y, hedge Z, do nothing. The discipline is to write the action list before the market opens so that intra-day price action doesn't reroute the plan.

### Weekly: Thesis Review
Once a week (Friday close or Sunday afternoon):
- Is each position's original thesis still intact?
- Has the catalyst occurred? If yes, why is the trade still on?
- Has the macro regime shifted in a way that contradicts any trade's thesis?
- Are there any positions where the answer to "would I open this trade today?" is no? Close them.
- Update the trade journal with this week's P&L attribution by Greek (delta P&L, vega P&L, theta P&L) — this is the feedback loop for whether the book's risk profile is delivering as designed.

### Monthly: Book Rebalance
Once a month, a deeper structural review:
- Are the five pre-trade limits still appropriate given account size and current vol regime?
- Is the book's actual realized risk (drawdown, daily P&L volatility) consistent with the budgeted risk?
- Sector allocations: rebalance if any sector has drifted outside its band
- Vol regime check: have we shifted from a [[volatility-regime-classification|low-vol regime]] to high-vol or vice versa? If so, the vega/theta budget needs to change.
- Strategy mix: is one strategy (e.g., short premium) generating too much of the book's P&L variance? Diversify the strategy mix.

## Common Mistakes

The mistakes that destroy options books are predictable and most are portfolio-level, not trade-level:

1. **Over-correlated short premium.** The trader sells a SPY iron condor, an IWM strangle, a QQQ put-credit spread, and a few single-name covered calls. All look like independent income trades. They are one short-vol position, and they all lose on the same day.
2. **Expiration cliffs.** 70% of theta loaded into a single weekly because that's where the most liquidity is. One bad print and the entire month's premium evaporates.
3. **Ignoring net vega.** Each trade was sized "vega-neutral" at entry, but as IV moved and trades aged, net vega drifted to ±$2,000/point. The trader didn't notice until vol moved.
4. **Sizing on max-loss instead of expected-loss.** Treating a 0.10-delta short put with $500 max loss as the same risk as a long ATM call with $500 max loss. The short put has a fat left tail; the long call doesn't.
5. **Hedging trade-by-trade instead of book-level.** Buying a protective put on every long stock position rather than running one index put overlay against the net long book. The premium drag is 3-4x.
6. **Adding to a losing book.** A trade goes against you, and the response is to add a "hedge" that's actually a new directional position. The book gets larger, not smaller, during drawdowns. The rule: drawdowns shrink the book, never grow it.
7. **No record of net Greeks over time.** The book's Greeks are computed only on the day a trade is added or removed. The drift between is invisible. A daily snapshot file (CSV, journal entry) is the minimum.
8. **Confusing theta with edge.** A book that collects theta is not, by that fact, a book with edge. Theta is the *price* paid by long convexity holders. Whether you have edge depends on whether realized vol is below implied — see [[variance-risk-premium]]. A book that runs +$500/day theta in a regime where realized vol exceeds implied is losing money on every trade despite the positive theta.
9. **Concentration creep.** The thesis was "long quality tech." Six weeks later it's "long NVDA, AMD, AVGO, MU, TSM" — same trade, less diversified, more risk.
10. **Forgetting the hedge has Greeks too.** A long SPY put hedge adds long vega, long gamma, and short theta to the book. If you didn't include the hedge in your portfolio Greeks, your numbers are wrong.

## Tools

The framework is software-agnostic but requires a few categories of tooling:

### Portfolio Margin
For accounts above $125K (the SEC minimum, often $150-200K in practice), [[portfolio-margin]] is the difference between a workable options book and a Reg-T-strangled one. Portfolio margin computes margin based on a stress-tested view of the entire book (-12% to +10% on equities, with vol-up and vol-down scenarios), giving 3-6x more buying power than Reg-T strategy-based margin for hedged books. Brokers offering portfolio margin: IBKR, Schwab (formerly thinkorswim), TastyTrade for accounts that qualify.

### Risk Graph and Scenario Software
- **thinkorswim Analyze tab.** Free with a Schwab account, accepts beta-weighted portfolio views and lets you simulate vol-up, vol-down, and price-shock scenarios across the book.
- **OptionVue, OptionNet Explorer, ONE.** Paid platforms ($50-200/mo) with deeper scenario testing and historical replay.
- **IBKR Risk Navigator.** Built into TWS, runs portfolio-level scenarios with custom shock scenarios.
- **Bloomberg / FactSet (institutional).** What pros use; not relevant to retail.

### Journaling
A daily Greeks snapshot file (CSV), a weekly thesis log, and a monthly P&L attribution. The attribution should decompose each week's P&L into delta P&L, vega P&L, theta P&L, and gamma P&L — without this decomposition, the trader cannot tell whether the book's actual risk is the budgeted risk.

### Stress Testers
[[options-stress-testing]] covers the specific scenarios. The minimum set:
- ±5%, ±10%, ±20% spot moves (with appropriate gamma and vanna re-pricing)
- IV +10, +20, +50% multiplicative shocks (compressed term structure)
- Combined: -10% spot + IV +50% (the standard equity stress)
- Single-name gap: +30% / -30% on largest single-name positions
- Earnings cluster: simultaneous IV crush across all positions reporting in a given week

The output is a P&L grid that should fit the budgeted drawdown limit. If it doesn't, the book is too big — independent of how each individual trade looks.

## Quick Reference: The Construction Loop

A one-screen summary of the discipline this page describes:

| Step | Question | Tool / page |
|------|----------|-------------|
| 1. Set limits | What is the book *allowed* to carry on each axis? | [[#Risk Limits]], [[vega-budgeting]], [[theta-targeting]] |
| 2. Aggregate | What does the book carry *now*, beta-weighted and bucketed? | [[portfolio-greeks-aggregation]] |
| 3. Evaluate candidate | What does the book look like *after* this trade? | [[#Position Layering]] |
| 4. Check limits | Does post-trade breach any axis? | [[#Risk Limits]] |
| 5. Decide | Skip / resize / restructure / make room | [[#Position Layering]] |
| 6. Hedge residual | Is there unwanted aggregate exposure to overlay? | [[#Hedging at the Book Level vs Trade Level]] |
| 7. Stress | Does the worst-day P&L fit the drawdown budget? | [[stress-test]], [[options-stress-testing]] |
| 8. Review | Daily Greeks, weekly thesis, monthly rebalance | [[#Review Cadence]] |

The loop is what converts a stack of individually-reasonable trades into a coherently-budgeted book. A trader who runs steps 1-8 every session is doing the work that separates the [[professional-vs-retail-mindset|professional]] from the retail approach; a trader who runs only steps 3 and 5 (evaluate and decide) is sizing in isolation, which is precisely the failure this page exists to prevent. See also [[fees-and-friction]] for why low-friction execution is a precondition for the construction math to hold.

## Related

- [[options-position-sizing]] — sizing math for individual positions
- [[options-greeks]] — the risk dimensions being budgeted
- [[portfolio-greeks-aggregation]] — beta-weighting and bucketing
- [[vega-budgeting]] — setting and enforcing the vega limit
- [[theta-targeting]] — setting an income target without over-leveraging vol
- [[expiration-laddering]] — spreading risk across tenors
- [[options-concentration-risk]] — single-name and sector caps
- [[options-stress-testing]] — scenario analysis at the book level
- [[portfolio-margin]] — capital efficiency for hedged books
- [[variance-risk-premium]] — the theoretical edge behind theta-positive books
- [[volatility-regime-classification]] — how regime selection drives portfolio bias
- [[options-risk-budgeting]] — companion concept page
- [[risk-management-overview]]
- [[risk-management]] — the general discipline this specialises
- [[stress-test]] — the scenario engine that validates the limit sheet
- [[fees-and-friction]] — execution-cost precondition for the construction math
- [[professional-vs-retail-mindset]] — the discipline gap this framework addresses

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on portfolio Greeks aggregation and stress testing
