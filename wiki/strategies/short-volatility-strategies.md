---
title: "Short Volatility Strategies"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, volatility, derivatives, quantitative, risk-management]
aliases: ["Short Vol", "Short Volatility", "Net Short Options Strategies"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, options, futures]
complexity: advanced
backtest_status: cost-corrected
edge_source: [risk-bearing, behavioral, structural]
edge_mechanism: "Sellers of options collect a persistent premium (the variance risk premium) for absorbing the tail risk that buyers are mandate-driven or behaviorally compelled to lay off."
data_required: [options-chain, implied-volatility-surface, vix-term-structure, ivr, ohlcv-daily, earnings-calendar]
min_capital_usd: 10000
capacity_usd: 10000000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.5
breakeven_cost_bps: 25
related: ["[[long-vol-vs-short-vol]]", "[[long-volatility-strategies]]", "[[options-premium-selling]]", "[[premium-selling-systematic]]", "[[short-strangle]]", "[[iron-condor]]", "[[short-put-spread]]", "[[covered-calls]]", "[[cash-secured-puts]]", "[[vix-futures]]", "[[long-vol-overlay]]", "[[variance-risk-premium]]", "[[volatility-risk-premium]]", "[[volatility-regime-classification]]", "[[market-regime]]", "[[tom-sosnoff]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[ljm-preservation-and-growth]]", "[[xiv-velocity-shares]]", "[[itpm-framework]]"]
---

# Short Volatility Strategies

Short volatility strategies are options structures that are **net short premium**: short [[gamma]], short [[vega]], long [[theta]], with **concave** payoff. They make money most days collecting [[theta-decay|theta]] and lose multiples of accumulated theta during vol shocks. This page is the survey/landing page for the family; each canonical implementation has its own page. For the mirror category, see [[long-volatility-strategies]]. For the comparative discussion, see [[long-vol-vs-short-vol]].

## Overview

A book is "short volatility" when its options exposure is structurally short [[gamma]] and short [[vega]]. The defining empirical fact: **short-vol books make money most days and lose multiple years of P&L in a week** during vol shocks. Stand-alone, most short-vol strategies have **positive expected return** (5-12% per year on portfolio NAV) -- the harvest of the [[variance-risk-premium]] -- but **negative skew**: the loss distribution has a fat left tail with non-trivial probability of catastrophic loss in any given decade.

The strategic case for short vol rests on the persistence of the [[variance-risk-premium]] (often called the [[volatility-risk-premium]]): implied vol on equity index options has averaged 1-3 vol points above subsequently realized vol, a statistically significant and economically meaningful premium that does not arbitrage away because the buyer side ([[pension-fund]] hedgers, structured-product issuers, retail crash-protection buyers) is structurally non-economic. The risk is that the same shocks that cause buyers to suddenly bid puts ([[volmageddon|Feb 2018]], [[vix-august-2024-spike|Aug 2024]], [[covid-crash|Mar 2020]]) cause short-vol books to lose 30-100% of NAV before they can react. The institutional discipline (see [[itpm-framework]]) is to run a short-vol core paired with a [[long-vol-overlay]].

## Edge source

Per the [[edge-taxonomy]], short vol draws on three of the five edge categories, in order of importance:

1. **Risk-bearing (primary)** -- the seller is paid an insurance premium for warehousing crash risk. This is genuine compensation for a genuine risk, not a free lunch: the [[variance-risk-premium]] exists because the left tail is real and someone must hold it. The edge is the *overpricing* of that insurance, not the insurance business itself.
2. **Behavioral** -- option buyers systematically overpay for lottery-like payoffs and crash protection (probability weighting per [[prospect-theory]]; salience of recent crashes). OTM index puts are the canonical overpriced asset in the empirical literature (Bondarenko 2014).
3. **Structural** -- mandate-constrained flows: pension funds and insurers required to hedge, structured-product issuers who must buy back vol they are short to retail, and portfolio-insurance-style rules that buy protection after drawdowns at the worst prices. These buyers are not trying to maximize expected return on the option trade itself.

## Why this edge exists

The mechanism is an insurance market with a captive, price-insensitive buyer side:

- **Who is on the other side**: pension funds and insurers hedging equity books under regulatory or board mandate; banks hedging the embedded short-vol exposure of [[autocallables]] and other structured products they sold; retail buyers of crash protection and lottery-ticket calls; risk managers forced to buy protection *after* drawdowns when it is most expensive.
- **Why they keep paying**: they are not playing the same game. A pension fund buying puts is buying regulatory capital relief and career insurance, not positive expected value. Retail buyers overweight small probabilities. Structured-product hedging flow is mechanical. None of these flows respond to the put being 1-3 vol points "too expensive" -- so the premium persists.
- **Why it doesn't arbitrage away**: collecting the premium requires warehousing tail risk through the shocks. Most capital cannot: leverage constraints, margin spirals, investor redemptions at the bottom, and career risk force sellers out exactly when the premium is richest. The survivors of [[volmageddon]] earned the right to collect the premium afterward; the dead did not. The edge is rationed by the ability to survive the left tail, which is why pairing with a [[long-vol-overlay]] is the institutional standard.

## Null hypothesis

Under no-edge conditions, implied volatility would equal subsequently realized volatility on average (zero [[variance-risk-premium]]). Selling delta-hedged premium would then be zero expected value before costs and negative after spreads and commissions. Critically, the *surface behavior* of the strategy would look almost identical for years: a no-edge short strangle program still wins 70-90% of months (theta accrues mechanically), so **a high hit rate is exactly what the null predicts and proves nothing**. The discriminating test is whether long-run total P&L net of tail losses and costs is positive -- i.e., whether the average IV-minus-subsequent-RV spread on the options actually sold is reliably above zero. Empirically it has been (Carr & Wu 2009 document significantly negative variance-swap returns for buyers across equity indices), which is the rejection of the null; but any individual track record shorter than a full vol cycle, including at least one major shock, cannot distinguish edge from unexercised tail risk.

## Profile

| Dimension | Profile |
|---|---|
| **Net options position** | Net short premium |
| **[[gamma]]** | Negative (penalized by realized moves) |
| **[[vega]]** | Negative (loses on IV expansion) |
| **[[theta]]** | Positive (collects premium daily) |
| **P&L skew** | Strongly negative |
| **Hit rate (months profitable)** | High (~70-90%) |
| **Expected stand-alone return** | +5% to +12% per year (VRP capture) before shocks |
| **Best months** | Calm regimes with realized vol crush: +3% to +6% NAV |
| **Worst months** | Vol shocks: -30% to -100% NAV in a single session |
| **Stand-alone Sharpe (calm regime, in-sample)** | 1.5-3.0 |
| **Stand-alone Sharpe (full cycle including shocks)** | 0.4-0.8 |
| **Regime fit (see [[volatility-regime-classification]])** | Calm and Normal regimes |
| **Capital efficiency** | High in calm regimes (10-15% NAV margin); margin spikes 5-10x in stress |
| **Margin call risk** | Severe; portfolio margin reprices instantly |
| **Liquidity in stress** | Position becomes illiquid; bid-ask widens 10x |
| **Psychology** | Daily dopamine hits; sudden ruin |
| **Crowding risk** | High and rising (0DTE flow concentration) |
| **Survivor bias in track records** | Severe |

## Payoff and Greeks

The defining signature of short vol is a **concave payoff**: bounded gains, unbounded (or large-defined) losses. For a short strangle, profit is maximized when the underlying expires between the strikes and IV has fallen; loss accelerates as the underlying moves through either strike.

```
Short strangle P&L at expiry (concave tent, capped at the credit):

  P&L
   |        _______________
   |       /               \
 0 +------/-----------------\------ underlying price
   |     /                   \
   |    /                     \
   |   / (loss grows ~linearly  \  ... but pre-expiry, vol/gamma
   |  /   below put strike)       \    losses are convex against you)
        ^put strike        ^call strike
```

The Greeks are the precise language for *why* the payoff is concave:

| Greek | Sign | What it means for the book | Where it bites |
|-------|------|----------------------------|----------------|
| **[[delta]]** | Near zero at entry | Structure is roughly direction-neutral when balanced | Drifts as the underlying moves; must be managed |
| **[[gamma]]** | Negative | Delta worsens *against* you as price moves — losses accelerate | Worst near expiry (gamma cliff) and during large moves |
| **[[vega]]** | Negative | Loses when [[implied-volatility]] expands | Catastrophic in a vol shock; the primary kill vector |
| **[[theta]]** | Positive | Collects time decay every day the underlying sits still | The source of the daily "income"; the bait |
| **Vomma / vol-of-vol** | Negative | Loses when vol *itself* becomes volatile | The hidden tail — convexity of vega works against the seller |

The trader is, in effect, **selling insurance**: paid a small premium ([[theta]]) day after day to absorb a rare, large loss (negative [[gamma]]/[[vega]] in a shock). The whole discipline of short vol is managing the gap between the steady positive [[theta]] and the explosive negative [[vega]]/[[gamma]] — which is exactly what [[vega-budgeting]] and the [[long-vol-overlay]] exist to do.

### Regime-conditional behavior

Short vol is not regime-symmetric. Its expected return flips sign across the [[volatility-regime-classification|volatility regime]] (and across the broader [[market-regime]]):

| Regime (see [[volatility-regime-classification]]) | Short-vol expected return | Posture |
|---|---|---|
| **Calm** | Strongly positive (max [[variance-risk-premium\|VRP]] / theta-per-vega) | Full size |
| **Normal** | Positive, thinner margin of safety | Full size + overlay |
| **Elevated** | Marginal / negative; transition zone | Reduce; add convexity |
| **Stressed** | Strongly negative (vega and gamma both bleed) | Flatten; let [[long-volatility-strategies]] work |

This is the single most important operational fact about the family: **the same structure that prints in Calm is the structure that ruins the book in Stressed.** Regime awareness is not optional.

## Canonical implementations

Each entry links to its detailed strategy page or category page.

### Short strangles ([[short-strangle]])

Sell OTM call + OTM put on the same underlying, same expiration. The canonical undefined-risk short-vol structure. Default tenor 30-45 DTE, default strikes 16 [[delta]] each side. The dominant retail premium-selling structure popularized by tastytrade. Capacity is the trader's [[buying-power]]; risk is undefined and was the dominant blow-up profile in [[volmageddon]] and [[vix-august-2024-spike]].

### Iron condors ([[iron-condor]])

Short strangle plus protective long wings further OTM = defined-risk short-vol structure. Caps both the credit collected and the maximum loss. Lower buying-power requirement, lower expected return per dollar of margin, much lower tail risk than naked strangles. The institutional default for retail-accessible short vol.

### Short put credit spreads ([[short-put-spread]])

Sell ATM/ITM put + buy further-OTM put. Directionally bullish short-vol structure. The dominant short-vol implementation among traders who want to avoid call-side risk and are explicitly also taking a directional view.

### Covered calls ([[covered-calls]] / [[covered-call-strategy]])

Long stock + short OTM call against it. Caps upside in exchange for premium income. The most retail-accessible short-vol structure; popularized via covered-call ETFs (JEPI, QYLD). Net delta is positive (long the stock dominates), but the structure is short [[gamma]] and short [[vega]] in the call leg.

### Cash-secured puts ([[cash-secured-puts]])

Short put fully cash-collateralized. Effectively "buy-the-dip with income": the seller collects premium and either keeps it or buys the underlying at a discount if assigned. Foundational [[wheel-strategy]] component.

### The wheel ([[wheel-strategy]])

Sequential cash-secured puts -> if assigned, covered calls on the resulting long stock -> if called away, restart with cash-secured puts. Income-extraction loop popular in retail; structurally net short vol throughout the cycle.

### Short VIX futures and short-VIX ETPs ([[vix-futures]], [[xiv-velocity-shares]], [[svxy]])

Short [[vix-futures|VIX futures]] or its ETP wrappers (XIV, SVXY). Harvests the persistent [[contango]] in the [[vix-term-structure]]. The vehicle that ended in [[volmageddon|XIV's termination]] on Feb 5, 2018 (-96% intraday). SVXY survived after rebalancing its leverage; remains the canonical short-VIX vehicle but with materially reduced volatility-of-volatility exposure.

### Structured products and yield-enhancement notes ([[autocallables]], [[reverse-convertibles]], [[yield-enhancement-notes]])

Bank-issued notes that pay an above-market coupon in exchange for embedded short put exposure. Sold to retail and HNW clients as "income" products; structurally short vol with often poorly-understood tail risk. The structured-products complex was a major short-vol vehicle in the 2008 crisis.

### Calendar and diagonal short-vol ([[calendar-spread]] / [[diagonal-spread]])

Short shorter-dated options vs long longer-dated, same strike. Net negative [[gamma]] near expiration but more capital-efficient than outright. Used by sophisticated traders to harvest term-structure VRP rather than level VRP. See [[itpm-ratio-calendar-spread]].

### Jade lizards and ratio structures ([[jade-lizard]] / [[ratio-spread]])

Modified strangles that eliminate one-sided risk (jade lizard removes upside risk; ratio spreads modify the call side). Niche structures; useful when [[skew]] makes one wing relatively expensive.

### Systematic premium selling ([[premium-selling-systematic]])

The disciplined, mechanical implementation: 30-45 DTE, 16-delta wings, 50% profit target, 21 DTE time exit, [[ivr]] entry filter, paired with a [[long-vol-overlay]]. The institutional version of the tastytrade retail playbook.

## Rules

The representative disciplined implementation (the [[premium-selling-systematic]] rule set; individual structures vary per their own pages):

**Entry**
- Underlying: liquid index options (SPX/SPY/ES) or top-tier liquid single names; penny-wide or near-penny markets only.
- Filter: [[ivr|IV Rank]] > 30 on the underlying; no entry inside 7 calendar days of earnings on single names; no entry when the [[vix-term-structure]] is in [[backwardation]].
- Structure: sell 45 DTE (30-60 acceptable) strangle at 16-delta strikes each side, or the iron-condor equivalent with wings 25-50 points further OTM when defined risk is required.

**Exit**
- Profit target: buy back at 50% of credit received.
- Time exit: close or roll at 21 DTE regardless of P&L (avoids the gamma cliff of the final weeks).
- Stop-loss: close when the position trades at 2x the credit received (i.e., loss = 1x credit) on undefined-risk structures.

**Position sizing**
- Size by [[vega-budgeting]], not margin: total portfolio short vega <= 0.1% of NAV per vol point (so a 10-point IV spike costs <= ~1% NAV per unit of budget, scaled to tolerance).
- Per-position margin <= 5% of NAV in calm-regime buying power; total short-premium margin <= 25-35% of NAV, leaving headroom for the 5-10x stress repricing.
- Mandatory pairing with a [[long-vol-overlay]] (deep-OTM puts or VIX calls, budgeted at 0.5-1.5% of NAV per year) when running undefined-risk structures.

## Implementation pseudocode

```python
# Systematic short-premium core (strangle variant)
for underlying in liquid_universe:
    if ivr(underlying) < 30:            continue
    if days_to_earnings(underlying) < 7: continue
    if vix_term_structure() == "backwardation": continue

    chain = options_chain(underlying, target_dte=45)
    put_strike  = strike_at_delta(chain, -0.16)
    call_strike = strike_at_delta(chain, +0.16)
    credit = sell_strangle(put_strike, call_strike)

    if portfolio_short_vega() > 0.001 * nav:   # vega budget breached
        skip_or_reduce()

# Daily management
for pos in open_positions:
    if pos.value <= 0.50 * pos.credit:  close(pos)          # profit target
    elif pos.value >= 2.0 * pos.credit: close(pos)          # stop-loss
    elif pos.dte <= 21:                 close_or_roll(pos)  # time exit

# Overlay (always on)
maintain_long_vol_overlay(budget=0.01 * nav / year)
```

## Indicators / data used

- Full [[options-chain]] with greeks and bid/ask (entry construction, liquidity screening)
- [[implied-volatility]] surface and [[ivr|IV Rank]] / IV Percentile (entry filter)
- [[vix]] level and [[vix-term-structure]] (contango/backwardation regime gate)
- [[skew]] (wing selection; relative richness of put vs call side)
- Realized volatility (10/30-day) vs implied -- the live VRP estimate
- Daily OHLCV for the underlyings
- Portfolio margin / stress-test output from the broker (sizing constraint)

## Example trade

SPX at 5,900 after a 4% pullback; VIX 19, IVR 38, term structure still in contango. Sell the 45-DTE 16-delta strangle: short 5,350 put / short 6,250 call for $45.00 credit ($4,500 per strangle; SPX multiplier 100). Initial margin ~ $55,000 under portfolio margin (~2.5% of a $2.2M book; short vega ~ $1,900, inside a 0.1%-of-NAV vega budget). Over the next 23 days SPX drifts to 5,980 and 30-day IV falls 3 points; the strangle marks at $22.00. Buy back at 50% of credit: +$2,300 gross per strangle, less ~$15 commissions/fees and ~$50 of spread crossing round-trip, net ~ +$2,235 in 23 days. The same position held through a VIX-19-to-35 shock instead would have marked at roughly 3-5x the credit -- the 2x-credit stop and the overlay are what make the example survivable rather than lucky.

## Performance characteristics

All figures net of realistic costs (index options: ~1 tick spread crossing per leg per side plus exchange/clearing fees; breakeven cost tolerance ~25 bps round-trip on premium traded):

- **Full-cycle expectation**: +5% to +12% per year on NAV for a disciplined, vega-budgeted book; Sharpe **0.4-0.8 across a full vol cycle** including shocks. In-sample calm-regime Sharpe of 1.5-3.0 is an artifact of unexercised tail risk and must be deflated (see [[deflated-sharpe-ratio]]).
- **Benchmark evidence**: the CBOE PutWrite Index (PUT) -- mechanical monthly ATM cash-secured SPX puts since mid-1986 -- has delivered roughly equity-like long-run returns at about two-thirds of S&P 500 volatility, the standard institutional evidence that the VRP survives implementation costs. Academic estimates (Carr & Wu 2009; Bondarenko 2014) find the premium statistically significant across indices.
- **Distribution shape**: hit rate 70-90% of months; average losing month 2-5x the average winning month; worst sessions -30% to -100% NAV for naked, unhedged books (Feb 5 2018; Aug 5 2024; Mar 2020). Expected max drawdown for a disciplined defined-risk-plus-overlay book: ~50% in a generational shock, 15-25% in an ordinary vol event.
- **Cost sensitivity**: the strategy is cost-robust at index level (deep markets, wide premium per trade) but degrades fast on illiquid single names where spreads consume 10-30% of the credit.

## Capacity limits

The aggregate VRP across listed index options is one of the deepest premium pools in markets: SPX options alone trade ~3 million contracts/day (hundreds of billions of dollars of notional), and the strategy family supports **tens of billions of dollars** in aggregate. A single disciplined book runs ~$10B before its own flow measurably moves index IV (frontmatter `capacity_usd`). The binding constraint is not average-day liquidity but **stress capacity**: in a shock, the whole crowd exits simultaneously into a bid-ask that widens 10x, and the short-VIX ETP complex (~$3-4B in early 2018) demonstrated that even a few billion dollars of same-direction rebalancing flow can itself drive the terminal spike. Crowding risk is high and rising with 0DTE flow concentration -- effective capacity shrinks exactly when measured capacity looks largest.

## What kills this strategy

The likely failure modes (see [[failure-modes]]):

1. **Vol shock while naked** -- a multi-sigma IV spike (Feb 2018, Mar 2020, Aug 2024) imposing losses of 30-100% of NAV in a session before any reaction is possible. The dominant historical killer.
2. **Margin spiral** -- portfolio margin reprices 5-10x in stress, forcing liquidation into 10x-wide markets; losses are realized at the worst prints. Death by mechanism, not by mark.
3. **Crowding feedback** -- short-vol positioning itself fuels the spike (XIV's rebalancing in Feb 2018), so the strategy's popularity degrades its own tail.
4. **VRP regime erosion** -- structural compression of the IV-RV spread (e.g., from systematic seller crowding or 0DTE microstructure changes) turning a paid risk into an unpaid one; slow death disguised as "a flat year."
5. **Discipline failure** -- abandoning stops/exits under drawdown ("roll and pray"), the canonical retail account-death trajectory.
6. **Stacked exposure** -- running short vol on top of an already short-vol-equivalent book (levered long equity, illiquid credit), so the tail hits everything at once.

## Kill criteria

Numerical retirement/pause conditions (see [[when-to-retire-a-strategy]]):

- **Pause new entries** if strategy drawdown from high-water mark exceeds **25% of allocated NAV**, or whenever the [[vix-term-structure]] flips to backwardation (re-enter only after 5 consecutive sessions back in contango).
- **Retire** if drawdown exceeds **50% of allocated NAV** (frontmatter expected_max_drawdown is the boundary, not a budget).
- **Retire** if the trailing **24-month average implied-minus-realized spread** on the instruments traded falls below **+0.5 vol points** (the premium being harvested has structurally compressed).
- **Retire** if rolling 12-month Sharpe is **< 0 for 18 consecutive months** outside of a recognized shock window.
- **Hard structural stop**: never operate undefined-risk structures without a live [[long-vol-overlay]]; overlay lapse = flat the book.

## Common mistakes

1. **Running naked short vol with no overlay** -- the most common and most catastrophic mistake. See [[ljm-preservation-and-growth]] and the [[volmageddon]] cohort.
2. **Sizing by margin not by vega** -- [[portfolio-margin]] in calm regimes makes 5x leverage look harmless. Sizing by [[vega-budgeting]] (vega as % of NAV) reveals the actual tail exposure.
3. **Selling cheap premium** -- [[ivr|IV Rank]] under 20 means premium is statistically rich for the buyer, not the seller. Mechanical entry filters (IVR > 30) are essential.
4. **Discretionary management of losers** -- rolling out and down to "give the trade more time" is the canonical retail blow-up trajectory. Mechanical exits (stop-loss, 21 DTE time exit) save accounts.
5. **Selling around earnings on single names** -- single-stock event premium often correctly prices a binary outcome. The 16-delta strike is not protective when the stock gaps to 30 delta overnight.
6. **Ignoring [[skew]] and [[term-structure]]** -- selling the wing where IV looks rich on a level basis but is statistically cheap on a skew basis is a structural mistake.
7. **Confusing high hit rate with edge** -- a strategy that wins 90% of months and loses 5x average win on the 10% is mediocre. Hit rate is the most misleading metric in short vol.
8. **Sharpe ratio worship** -- a 2.5 in-sample Sharpe is meaningless if the strategy has a 10-sigma left tail. See [[deflated-sharpe-ratio]].

## When to use / avoid

**Use short vol when:**

- You are running a multi-strategy portfolio and want to harvest [[variance-risk-premium]] systematically.
- You have a [[long-vol-overlay]] in place to cap the left tail.
- Implied vol is rich relative to subsequently realized vol expectations ([[ivr]] elevated; vol regime is calm but not exhausted).
- You can size by [[vega-budgeting]] rather than by margin and tolerate the daily vega P&L volatility.

**Avoid short vol when:**

- You cannot or will not maintain an overlay -- naked short vol is leveraged tail exposure with positive expected return that asymptotically converges to ruin under [[ergodicity]].
- VIX is already in [[backwardation]] and [[skew]] is steep -- a vol shock is in progress and selling premium is selling at the worst possible price.
- You manage to a Sharpe metric and have not deflated it for [[negative-skew]].
- You cannot psychologically tolerate a single -25% to -50% session (the typical worst-case for naked structures even with discipline).
- You are running short vol on top of a structurally short-vol-equivalent book (e.g., 100% long equity, levered real estate). The short vol stacks the same risk.

## Advantages

- Harvests one of the most persistent, best-documented premia in markets ([[variance-risk-premium]]), with deep academic support.
- High hit rate and steady mark-to-market P&L in calm regimes; psychologically easy to hold *most* of the time.
- Enormous capacity and liquidity at the index level; implementable from $10k retail (defined-risk) to $10B institutional.
- Flexible structure menu: risk can be defined (condors, spreads), collateralized (CSPs, covered calls), or term-structure-based (calendars), matching almost any mandate.
- Diversifying carry stream when properly overlay-hedged: returns are driven by IV-vs-RV, not by market direction per se.

## Disadvantages

- Strongly negative skew: years of P&L can vanish in a session; the loss distribution punishes any sizing or discipline error catastrophically.
- Tail events are precisely when margin balloons, liquidity vanishes, and correlations go to one -- the strategy fails at the worst possible moment for the rest of the portfolio.
- Track records are systematically misleading (survivor bias, unexercised tail risk, calm-regime Sharpe inflation).
- High and rising crowding; the strategy's own popularity has twice (2018, 2024) amplified the shocks that kill it.
- Requires permanent overlay spend (0.5-1.5% NAV/year) and mechanical discipline that most discretionary traders demonstrably fail to maintain.

## Sources

- Carr, Peter and Wu, Liuren. "Variance Risk Premiums." *Review of Financial Studies* (2009).
- Bondarenko, Oleg. "Why Are Put Options So Expensive?" *Quarterly Journal of Finance* (2014).
- Spitznagel, Mark. *Safe Haven* (2021).
- CBOE PutWrite Index (PUT) methodology and long-run performance data, CBOE (index inception 1986; backfilled history from mid-1986).
- [[volmageddon]] post-mortem (Feb 5, 2018; XIV termination -96%).
- [[vix-august-2024-spike]] post-mortem (Aug 5, 2024).
- [[ljm-preservation-and-growth]] case study (-80%+ in Feb 2018).

## Related

- [[long-vol-vs-short-vol]] -- the canonical comparison.
- [[long-volatility-strategies]] -- the mirror category.
- [[options-premium-selling]] -- the canonical short-vol core strategy page.
- [[premium-selling-systematic]] -- systematic implementation.
- [[long-vol-overlay]] -- the overlay that turns naked short vol into a survivable strategy.
- [[options-portfolio-construction]] -- combining core and overlay.
- [[vega-budgeting]] -- sizing framework.
- [[variance-risk-premium]] / [[volatility-risk-premium]] -- the underlying premium being captured.
- [[implied-volatility]] / [[realized-volatility]] -- the two measures whose gap is the edge.
- [[volatility-regime-classification]] -- regime-conditional performance.
- [[market-regime]] -- the broader regime context that gates the strategy.
- [[itpm-framework]] -- institutional discipline overlay.
- [[ergodicity]] -- the time-vs-ensemble-average problem.
- [[edge-taxonomy]] -- edge categorization framework.
- [[short-strangle]], [[iron-condor]], [[short-put-spread]], [[covered-calls]], [[cash-secured-puts]] -- canonical implementations.
- [[volmageddon]], [[vix-august-2024-spike]], [[ljm-preservation-and-growth]] -- shock case studies.
- [[tom-sosnoff]], tastytrade -- popularization of retail short vol.
- [[mark-spitznagel]] -- the case for always pairing short vol with overlay.
