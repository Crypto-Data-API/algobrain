---
title: "Portfolio Greeks Aggregation"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, indicators, itpm]
aliases: ["Net Greeks", "Book-Level Greeks", "Aggregating Greeks"]
related: ["[[options-greeks]]", "[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[vega-budgeting]]", "[[theta-targeting]]", "[[delta-neutral]]", "[[vega-hedging]]", "[[beta-weighted-delta]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]"]
difficulty: advanced
---

**Portfolio Greeks aggregation** is the process of combining the [[options-greeks|Greeks]] of every position in a book into a single, comparable, dollar-denominated risk picture. The core insight is that **net Greeks are not the sum of raw Greeks**: a +0.50 delta on AAPL is not the same risk as a +0.50 delta on TLT, and -100 vega on a single-name biotech is not interchangeable with -100 vega on an SPX iron condor. Without proper aggregation -- dollar conversion, beta weighting, and vega normalization -- a trader looking at their book-level number is reading a meaningless scalar. This page covers the mechanics of doing it correctly.

## Overview

Every options trading platform shows you a column called "delta" or "vega" next to each position, and most will sum that column at the bottom of the screen. That sum is almost always wrong as a measure of portfolio risk. The reason is simple: Greeks are local, per-contract, per-share derivatives. Before you can compare them across underlyings -- and certainly before you can sum them -- you have to translate them into a common currency. That common currency is **dollars**: dollar delta, dollar gamma, dollar theta, and a normalized vega number that respects the fact that one vol point on an emerging-markets ETF means something very different than one vol point on a Treasury fund.

For directional exposure, the additional step is **beta weighting** -- expressing every position's delta in terms of how it would move against the SPX, so you get a single book-level beta-adjusted dollar delta. This is the number that tells you "if SPX moves 1%, my book moves $X." Without it, a long-tech, short-defensive book might look balanced when summing raw deltas, but actually carry substantial market beta.

This is bread-and-butter institutional [[risk-management]]. Market makers, [[volatility]] funds, and serious retail options traders all live on a screen that shows aggregated Greeks in dollar terms, refreshed every few seconds. The [[itpm-trading-program|ITPM]] options curriculum, [[hari-krishnan]]'s work on tail risk, and any market-making textbook treat this aggregation as table stakes -- the floor below which you cannot meaningfully discuss [[options-risk-budgeting|risk budgeting]], [[position-sizing]], or [[vega-hedging]]. The aggregated book number is also the input to everything downstream: it sizes hedges, it is what [[portfolio-margin]] charges against, and it is the baseline that [[options-stress-testing]] perturbs.

## The Trap of Summing Raw Greeks

The single most common mistake among intermediate options traders is to look at a broker screen, see a "Total Vega: -250" at the bottom of the position list, and treat that as a unified risk measurement. It is not.

**Vega example**: Suppose you have:

- Short 10 AAPL 30-DTE iron condors, vega per condor = -15. Total: **-150 vega**
- Short 10 TLT 30-DTE iron condors, vega per condor = -15. Total: **-150 vega**

The screen shows -300 net vega. But these two -150 vega exposures are not the same risk:

- AAPL has IV around 28 and realized vol around 25. A 1-point IV move (from 28 to 29) is a roughly 3.5% relative change in vol.
- TLT has IV around 9 and realized vol around 8. A 1-point IV move (from 9 to 10) is a roughly 11% relative change in vol.

A "1 vol point shock" on TLT is a far more extreme event than a 1 vol point shock on AAPL. So while raw vega adds to -300, the **risk-adjusted** vega exposure is much more concentrated in TLT than the number suggests. The same trap applies across virtually every cross-asset comparison.

**Delta example**: 100 deltas long on a $30 stock and 100 deltas long on a $300 stock are the same number of "deltas" but represent **10x different dollar exposures** ($3,000 vs $30,000 of effective stock).

**Gamma example**: Per-share gamma on a $5 biotech and per-share gamma on a $500 megacap are on completely different scales. Summing them is meaningless.

The fix is to **convert each Greek into a dollar (or normalized) quantity** before aggregating. This is the entire point of the aggregation workflow.

### Aggregation Methods at a Glance

Each Greek requires a different normalization before it can be summed across underlyings. This is the master cheat-sheet for the rest of the page:

| Greek | Raw unit (per contract) | Correct aggregation unit | Transformation | Can you sum the broker column? |
|-------|------------------------|--------------------------|----------------|-------------------------------|
| [[delta\|Delta]] | per-share Δ | dollar delta, then **beta-weighted** dollar delta | `Δ × Spot × Mult × Contracts`, then `× β_SPX` | No — needs spot scaling **and** beta weighting |
| [[gamma\|Gamma]] | per-share Γ | dollar gamma per 1% | `0.5 × Γ × (Spot×0.01)² × Mult × Contracts` | No — needs spot² scaling |
| [[theta\|Theta]] | $/day already | $/day | `Θ_share × Mult × Contracts` | **Yes** — dollars are dollars |
| [[vega\|Vega]] | $/1 vol pt | %-vega (`$Vega / IV`) or RV-normalized | divide by IV level, or scale by realized vol | No — a vol point is not a fixed unit of risk |
| [[vanna]] | per-share | dollar vanna | `Vanna × Spot × Mult × Contracts × 0.01` | No |
| Charm | per-share/day | dollar charm | spot-scale like delta | No |
| Vomma / Volga | $/vol pt² | normalize like vega | scale by IV² | No |

The single most important takeaway: **only [[theta]] sums cleanly off the broker screen.** Every other Greek requires a spot-, beta-, or IV-level transformation first.

## Dollar Delta

Dollar delta converts a per-share delta into the actual dollar P&L per 1% move (or per $1 move) in the underlying. It is the basic unit of directional exposure.

**Formula (per $1 move)**:

```
$Δ = Δ × Spot × Multiplier × Contracts
```

Where:
- **Δ** is the per-share delta of the option (e.g., 0.45)
- **Spot** is the underlying price (e.g., $180)
- **Multiplier** is the contract multiplier (100 for US equity options, 100 for SPX, varies for futures options)
- **Contracts** is the number of contracts held (signed: positive for long, negative for short)

**Worked example**: Long 10 AAPL 180 calls, delta = 0.55, spot = $180.

```
$Δ = 0.55 × 180 × 100 × 10 = $99,000
```

This means a $1 move in AAPL produces roughly $550 of P&L (10 contracts × 100 shares × 0.55), and the position represents about $99,000 of effective long stock exposure.

**Why it matters**: When you compare positions, dollar delta lets you say "this AAPL call position has $99k of long exposure, that TSLA put position has $40k of short exposure." Those are commensurable numbers. Raw deltas of 5.5 and -2.0 are not.

**Per 1% formulation** (more useful for portfolio comparison):

```
$Δ_per_1% = $Δ × 0.01 = Δ × Spot × Multiplier × Contracts × 0.01
```

This tells you book P&L per 1% underlying move, which is the natural unit when comparing exposures across very different price levels.

## Dollar Gamma

[[gamma|Gamma]] measures how much delta changes per $1 underlying move. Like delta, raw gamma is not directly comparable across underlyings. **Dollar gamma** expresses convexity exposure in P&L terms, typically per 1% move.

**Formula (per 1% move, the standard convention)**:

```
$Γ_1% = 0.5 × Γ × (Spot × 0.01)² × Multiplier × Contracts
```

This comes from the second-order Taylor term: P&L from gamma ≈ 0.5 × Γ × ΔS². For a 1% move, ΔS = Spot × 0.01.

**Worked example**: Long 10 SPX 4500 straddles, gamma per share = 0.005, SPX spot = 4500.

```
$Γ_1% = 0.5 × 0.005 × (4500 × 0.01)² × 100 × 10
     = 0.5 × 0.005 × 2025 × 100 × 10
     = $5,062.50
```

So for every 1% move in SPX (in either direction), the position gains roughly $5,063 from convexity alone (separate from delta P&L).

**Alternative formulation**: Some desks use **gamma dollars** = `Γ × Spot² × Multiplier × Contracts × 0.01` (without the 0.5), which gives "delta change per 1% move in dollar terms." This is the form quoted on many dealer gamma exposure (GEX) reports. The 0.5 factor matters when you are trying to estimate actual P&L; drop it when you are trying to estimate **dealer hedging flow**.

**Why it matters**: A book that is "long 50 gamma" tells you nothing without knowing what underlying. A book with $20,000 of dollar gamma per 1% means you make $20k on a 1% move in either direction (and lose $20k if you are short gamma). That is a meaningful number.

## Beta-Weighted Delta

Even with dollar delta, you still cannot meaningfully add a long AAPL position and a short XLU position into a single "book delta" number, because AAPL has roughly 1.2 beta to SPX and XLU has roughly 0.5 beta. A 1% SPX move does not translate to 1% in either name.

**Beta-weighted delta** converts every per-name dollar delta into **SPX-equivalent dollars** so you can sum them.

**Formula**:

```
$Δ_SPX = $Δ × β_to_SPX
```

Where β is the rolling regression beta of the underlying's returns to SPX returns (commonly 90-day or 180-day).

**Worked example**: Three positions, each with $50,000 of long dollar delta:

| Position | $Δ | β to SPX | β-weighted $Δ_SPX |
|----------|----|----|----|
| AAPL long | +$50,000 | 1.20 | +$60,000 |
| KO long | +$50,000 | 0.55 | +$27,500 |
| NVDA long | +$50,000 | 1.65 | +$82,500 |
| **Net** | **+$150,000** | -- | **+$170,000** |

The raw sum says you have $150k of long exposure. The beta-weighted sum says you actually have $170k of SPX-equivalent exposure -- because the NVDA piece moves 1.65x harder than SPX, and that compensates for the soft KO beta.

**The market-maker's number**: Most institutional risk systems display the book's beta-weighted dollar delta as the single most-watched directional metric. It answers the question, "If SPX moves 1%, what is my P&L?" To make the book [[delta-neutral]] in the market-relevant sense, you hedge with **SPX or ES futures** sized to offset this aggregate, not the raw per-name delta.

**Caveats**:
- Beta is unstable. It changes through regimes ([[beta-instability]]). Use rolling windows and recompute frequently.
- Beta is symmetric. In a crash, correlations spike to 1 and "low-beta" positions stop hedging you. Beta weighting is a fair-weather metric.
- For non-equity instruments (rates, FX, commodities), you need separate beta-to-relevant-factor calculations or a multi-factor model.

See [[beta-weighted-delta]] for deeper treatment, including its abuse by retail platforms that beta-weight without disclosing the lookback window.

## Vega Normalization

Vega is the trickiest Greek to aggregate. The per-contract vega number tells you the dollar P&L per 1 vol point (1 IV point) move. But as the AAPL/TLT example above showed, **a vol point is not a fundamental unit of risk** -- its meaning depends on the absolute level of IV.

There are three common normalization approaches, in increasing order of sophistication.

### 1. Raw Dollar Vega (Naive)

```
$Vega = Vega_per_share × Multiplier × Contracts
```

This is the broker-screen sum. It treats a vol point as a vol point regardless of underlying. **Acceptable only when all positions are on the same or very similar underlyings** (e.g., a book entirely in SPX/SPY).

### 2. Percentage Vega (IV-Normalized)

Normalize by dividing vega by the current IV level, giving you P&L per **percentage** change in vol rather than per absolute vol point.

```
%Vega = $Vega / IV
```

So a -150 vega position on AAPL with IV = 28 becomes -150/28 = **-5.4 percentage-vega**, while a -150 vega position on TLT with IV = 9 becomes -150/9 = **-16.7 percentage-vega**. The TLT position carries roughly 3x the proportional vol risk of the AAPL position, which matches intuition.

This is the workhorse normalization. Most institutional desks track both raw dollar vega and percentage vega, and use percentage vega for cross-underlying comparison.

### 3. Realized-Vol-Normalized Vega

For more sophisticated desks: scale vega by the realized vol of the underlying, on the theory that what really matters is "how big are the typical IV moves this underlying experiences?" This is closer to a [[volatility-of-volatility]]-adjusted exposure.

```
RV_Vega = $Vega × (RV_underlying / RV_benchmark)
```

Where benchmark is typically SPX or some chosen reference. This yields a "vega in SPX-equivalent vol points" number that can be aggregated.

### Cross-Term-Structure Vega

Even within one underlying, vega is not homogeneous: a 30-day option's vega and a 365-day option's vega both move on a "1 vol point" shock, but in reality the **vol surface does not shift uniformly**. Front-end IV is far more volatile than back-end IV. Sophisticated risk systems decompose vega by tenor bucket (e.g., 0-30d, 30-90d, 90-180d, 180d+) and display vega in each bucket separately.

A common heuristic: a 1-point shock to front-month IV typically corresponds to about a 0.3-point shock to 6-month IV. So **adding raw front and back vega together overstates aggregate sensitivity by 2-3x** for typical shocks. See [[term-structure-of-volatility]] and [[vega-bucketing]].

## Theta

[[theta|Theta]] is the easy one. Theta is already quoted as a dollar-per-day number on most platforms (per-share theta × multiplier × contracts). Across underlyings, a dollar of decay is a dollar of decay -- there is no scaling issue analogous to delta-spot or vega-IV-level.

**Formula**:

```
$Θ = Θ_per_share × Multiplier × Contracts
```

You sum dollar theta directly across the book to get **total daily decay** (positive for net premium-sellers, negative for net premium-buyers). This is one of the few aggregations where the broker screen sum is correct.

**Caveats**:
- Theta is non-linear in time. The decay accelerates as expiration approaches, particularly for ATM options. A book's "today" theta is not the same as its "next week" theta.
- Theta is partially compensated by [[gamma]]: long-gamma positions pay theta in exchange for convexity. So aggregate theta is meaningless without aggregate dollar gamma context. This is why desks track the **theta/gamma ratio** as a key book-level metric.
- Theta is paid only if vol stays at current implied. If realized vol exceeds implied, gamma profits offset theta. See [[gamma-scalping]].

For the purpose of [[theta-targeting]] (sizing the book to harvest a desired daily decay), aggregate $Θ is exactly the number to target.

## Cross-Greek Concerns

First-order Greeks (delta, gamma, theta, vega) are the bare minimum. At the book level, several second-order Greeks become material and require aggregation:

### Vanna (∂Δ/∂σ or ∂Vega/∂Spot)

Vanna captures how delta changes as IV changes (or equivalently, how vega changes as spot changes). At the book level, **a delta-hedged book is not necessarily vanna-hedged**: a vol move can re-introduce delta exposure that was hedged at the previous IV level.

Aggregate vanna in dollar terms:

```
$Vanna = Vanna_per_share × Spot × Multiplier × Contracts × 0.01
```

(The 0.01 normalizes to a 1% spot move per 1 vol point.)

Books with significant downside skew (long puts) tend to be **negative vanna**: when vol rises, the puts gain delta (become more bearish), forcing the hedger to sell more underlying into the falling market. This is the mechanical driver of crash dynamics.

### Charm (∂Δ/∂t)

Charm is delta decay -- how much delta drifts as time passes, holding everything else constant. At the book level, charm tells you how much rebalancing you need to do **just from the calendar moving forward**. Significant for multi-leg structures held into expiration; especially relevant for [[opex|OPEX]] gamma squeezes.

### Vomma / Volga (∂Vega/∂σ)

Vomma is the convexity of vega -- vega's sensitivity to IV itself. Long-OTM options have high positive vomma; ATM options have near-zero vomma. A book that is "vega-flat" on small IV moves can still gain or lose substantially on large IV moves if its vomma is non-zero. Critical for tail-risk books.

### Higher-Order Aggregation Rule

These cross-Greeks all need the **same dollar / normalization treatment** as the first-order Greeks. Naive summing of raw vanna or vomma across underlyings is just as broken as naive summing of raw vega.

## Worked Example: A 5-Position Book

Let's aggregate Greeks for a real-looking book. Spot prices, IVs, and Greeks below are illustrative but realistic for a normal-vol regime.

**Positions**:

1. **AAPL short call** -- 10 contracts of AAPL 200 calls (30 DTE), spot $185, IV 26%, β = 1.20
2. **TLT long put** -- 20 contracts of TLT 90 puts (45 DTE), spot $93, IV 11%, β = -0.20
3. **SPX iron condor** -- 5 condors, SPX 4400/4450/4600/4650, spot 4525, IV 14%, β = 1.00
4. **NVDA short strangle** -- 5 contracts each side, NVDA 850P/1000C, spot $920, IV 48%, β = 1.65
5. **MSTR long call** -- 3 contracts of MSTR 1500 calls (60 DTE), spot $1380, IV 75%, β = 2.50

### Per-Position Greeks (Dollar-Converted)

| Position | $Δ (per $1) | $Γ (per 1%) | $Θ (per day) | $Vega (per 1pt) | %Vega (vega/IV) |
|----------|-------------|-------------|--------------|-----------------|-----------------|
| AAPL short call | -$3,700 | -$420 | +$180 | -$220 | -8.5 |
| TLT long put | +$10,200 (delta is -, so $Δ on put is negative as price rises = +$Δ exposure to falling rates? careful sign) -- short bond long put = +$10,200 short bond exposure | -$95 (long gamma) | -$60 | +$340 | +30.9 |
| SPX iron condor | +$2,200 (slight long bias from skew) | -$1,150 | +$420 | -$680 | -48.6 |
| NVDA short strangle | +$800 | -$3,800 | +$650 | -$540 | -11.3 |
| MSTR long call | +$2,070 | +$310 | -$45 | +$185 | +2.5 |

(Sign conventions: positive $Δ = profits from underlying going up; negative $Γ = short gamma; positive $Θ = collects decay; negative $Vega = profits from IV falling.)

### Step 1: Raw Sums (the misleading numbers)

```
Sum $Δ        = -3,700 + 10,200 + 2,200 + 800 + 2,070 = +$11,570
Sum $Γ (1%)   = -420 - 95 - 1,150 - 3,800 + 310       = -$5,155
Sum $Θ (day)  = +180 - 60 + 420 + 650 - 45            = +$1,145
Sum $Vega     = -220 + 340 - 680 - 540 + 185          = -$915
Sum %Vega     = -8.5 + 30.9 - 48.6 - 11.3 + 2.5       = -35.0
```

Reading this naively: "I'm long $11.5k of delta, short $5.2k of gamma per 1%, collecting $1,145/day in theta, short $915 of raw vega, short 35 percentage-vega units."

### Step 2: Beta-Weighted Delta (the directional truth)

| Position | $Δ | β | β-weighted $Δ |
|----------|------|---|--------------|
| AAPL short call | -$3,700 | 1.20 | -$4,440 |
| TLT long put | +$10,200 | -0.20 | -$2,040 |
| SPX iron condor | +$2,200 | 1.00 | +$2,200 |
| NVDA short strangle | +$800 | 1.65 | +$1,320 |
| MSTR long call | +$2,070 | 2.50 | +$5,175 |
| **Beta-weighted Net** | -- | -- | **+$2,215** |

The raw delta said +$11,570 long. The **beta-weighted** delta says only +$2,215 SPX-equivalent long. Why? Because the TLT put has negative beta to SPX -- it's a defensive position that hedges, not adds to, market beta. The AAPL short call is also a market-short position. The book is much closer to delta-neutral on SPX than the raw sum suggested.

If you wanted to fully neutralize this book against SPX, you would short roughly **$2,215 / (4525 × 0.01 × 50)** ≈ **0.1 ES futures contracts per 1% move** -- i.e., not a meaningful hedge at this scale. The raw delta would have suggested a much bigger hedge that would have actually **made the book net short** in beta-weighted terms.

### Step 3: Normalized Vega (the true vol risk)

The raw -$915 vega looks small. But spread across very different IV regimes:

- AAPL (IV 26): -8.5 percentage-vega
- TLT (IV 11): +30.9 percentage-vega
- SPX (IV 14): -48.6 percentage-vega
- NVDA (IV 48): -11.3 percentage-vega
- MSTR (IV 75): +2.5 percentage-vega

The book is **net long percentage vega in TLT** (a low-vol underlying where vol has historically expanded sharply) and **massively short percentage vega in SPX** (where the iron condor is concentrated). The raw -35 net percentage-vega is a number you can actually risk-budget against; the raw -$915 is not.

### Step 4: Book-Level Summary (the right dashboard)

```
Beta-weighted $Δ (vs SPX, per 1%):  +$2,215    [near-neutral, slight long]
Total $Γ (per 1%, SPX-equivalent):  ~ -$5,000 [short gamma, sharp 1% moves cost]
Total $Θ (per day):                 +$1,145   [premium collector]
Total %Vega (IV-normalized):        -35       [short vol, concentrated in SPX/NVDA]
Front-month vega bucket (0-30d):    -$400     [most of the vega is short-dated]
Back-month vega bucket (30-90d):    -$515     [rest is medium-tenor]
```

This is the dashboard a serious options trader watches. It tells a coherent story: a slightly long-biased, short-gamma, short-vol book collecting about $1,145/day in theta, with most of the vol short concentrated in SPX index condors. Now you can ask: is the gamma exposure within budget? Is the percentage-vega within my [[vega-budgeting]] limits? Does the beta-weighted delta align with my market view?

## Daily Aggregation Workflow

Aggregation is a process, not a one-time calculation. The book changes every day even if you place no trades — spot drifts, IV moves, the calendar advances, and Greeks decay or flip sign. Run this checklist daily (and pre-trade for any new position):

1. **Pull per-position Greeks at current marks.** Per-share Δ, Γ, Θ, vega, plus second-order vanna/charm/vomma for any book with meaningful OTM exposure. Mark at mid only if liquid; haircut illiquid names.
2. **Convert to dollars.** Apply `× Spot × Mult × Contracts` for delta, the `0.5 × Γ × (Spot×0.01)²` form for gamma, and `× Mult × Contracts` for theta. Never aggregate raw per-share numbers.
3. **Beta-weight every dollar delta to a common benchmark** (SPX/SPY for equity books; the relevant factor for rates/FX/commodities). Use a consistent rolling window and record which window. See [[beta-weighted-delta]].
4. **Normalize vega.** Divide each position's dollar vega by its IV to get %-vega, and bucket by tenor (0-30d / 30-90d / 90-180d / 180d+). Do **not** add front-month and back-month raw vega as if a vol point shifts the whole surface in parallel. See [[term-structure-of-volatility]].
5. **Sum into a single dashboard.** Beta-weighted dollar delta, dollar gamma per 1%, total dollar theta, total %-vega, vega-by-tenor, and the **theta/gamma** and **theta/vega** ratios.
6. **Check against limits.** Compare each aggregate to your [[options-risk-budgeting]] ceilings: net beta-weighted delta band, max short gamma, vega budget, single-name and sector concentration ([[options-concentration-risk]]).
7. **Stress beyond the linear approximation.** Aggregated Greeks are local; pass the same book through [[options-stress-testing]] (e.g. -10% spot + 10 vol points + skew steepen) to read the non-linear tail loss the Greeks understate.
8. **Act.** If a limit is breached, hedge (size SPX/ES against the beta-weighted delta), trim the offending exposure, or use [[trade-repair-and-rolling]] to reshape positions back inside budget.

The discipline is that steps 1-5 are mechanical and should be automated; steps 6-8 are where judgment lives.

## Connection to Position Sizing & Risk Budgeting

Aggregated Greeks are the bridge between an individual trade and the book. [[position-sizing]] for options is fundamentally *Greek sizing*: you do not size to "number of contracts" or even to defined-risk max loss alone, you size so that each new position moves the **book-level** aggregates by an acceptable amount.

- **Pre-trade marginal contribution.** Before adding a position, compute how much it shifts beta-weighted dollar delta, dollar gamma, and %-vega. A trade that looks small standalone can blow the vega budget if it concentrates in an underlying the book is already short. This is the core link to [[options-concentration-risk]].
- **The vega budget is the binding constraint, theta is the objective.** [[theta-targeting]] sizes the book to harvest a target daily decay; [[vega-budgeting]] caps the vol risk taken to get it. Aggregation produces both numbers in commensurable units so the trade-off is explicit.
- **Beta-weighted delta sets the hedge.** Once the book's net beta-weighted dollar delta is known, the hedge size in SPX/ES falls straight out of it — see the worked example's Step 2. Raw per-name delta would over- or under-hedge.
- **The aggregate is what margin charges against.** [[portfolio-margin]] (TIMS/SPAN-style) effectively re-prices the whole book under shocks; a book whose aggregated Greeks are inside budget will usually sit inside margin too, but the two are not identical — margin is non-linear and expands in stress. Aggregation is necessary but not sufficient; pair it with stress testing.

In short: the per-contract Greeks are the raw material, aggregation is the manufacturing step, and [[position-sizing]] / [[options-risk-budgeting]] / [[theta-targeting]] are what you build with the finished product.

## Pitfalls and Failure Modes

The aggregation workflow fails in characteristic ways. Most blow-ups trace to one of these:

| Pitfall | What goes wrong | Fix |
|---------|-----------------|-----|
| **Summing the broker column** | Treating raw `Total Vega: -300` as a risk measure across mixed underlyings | Convert to dollar/%-normalized units first |
| **Undisclosed beta window** | Retail platforms beta-weight on an unknown lookback; beta is unstable across regimes | Use and record an explicit rolling window; recompute often ([[beta-instability]]) |
| **Parallel-surface vega** | Adding front- and back-month vega as if a vol point shifts the whole curve | Bucket vega by tenor; weight by historical surface response |
| **Fair-weather correlations** | Beta-weighting assumes historical betas; in a crash everything goes to beta 1 | Stress correlations to ~0.9; treat beta weighting as a calm-regime tool |
| **Ignoring second-order Greeks** | A delta-hedged book is not vanna-hedged; a vol move re-introduces delta | Aggregate vanna/charm/vomma in dollar terms for any OTM-heavy book |
| **Linear extrapolation to the tail** | "Short $5k dollar gamma per 1%" ≠ $25k on a 5% move; loss is quadratic | Always pair Greeks with [[options-stress-testing]] |
| **Mark-to-mid in stress** | Aggregation assumes you can trade out at model prices; spreads widen 5-10x | Apply a liquidity haircut to illiquid legs |
| **Stale aggregation** | Yesterday's dashboard does not describe today's book after drift/decay | Re-aggregate daily, not just when you trade |

## Tools

You can build aggregation infrastructure yourself, but several tools provide it out of the box:

### Broker Risk Pages

- **IBKR Risk Navigator** -- Interactive Brokers' built-in risk tool. Aggregates dollar Greeks, beta-weighted delta (user-configurable benchmark), and stress scenarios. Free for IBKR clients. Probably the most-used institutional-grade tool available to retail.
- **TastyTrade / TastyWorks Beta-Weighting** -- Native beta-weighting against SPY in the position view. Useful for retail users running theta-positive strategies. Caveats: black-box beta lookback.
- **ThinkOrSwim Analyze tab** -- Beta-weighting and stress P&L visualizations. Stronger on visualization than on customization.

### Dedicated Options Analytics

- **[[orats|ORATS]]** -- Implied volatility, Greeks, and surface analytics. Good for quants who want to compute their own aggregations from clean data.
- **[[greeks-live|Greeks.live]]** -- Real-time aggregated Greeks for crypto options (Deribit). Critical for crypto options traders running multi-strike books.
- **OptionNet Explorer** -- Position modeling and Greek aggregation; popular among independent options traders.
- **OptionVue** -- Older but well-regarded portfolio-level Greeks tool with stress testing.

### Build-Your-Own

- **CBOE / OPRA market data + Black-Scholes solver** -- A few hundred lines of Python (NumPy + py_vollib or QuantLib) gets you per-position Greeks; aggregation is straightforward dataframe arithmetic. Requires beta data from a separate source ([[yfinance]], [[polygon]], [[norgate-data]]).
- **QuantLib** -- Full term-structure-aware Greeks for serious quants. Steep learning curve.

## Limitations

Aggregated Greeks are **first-order, local linearizations**. They tell you what happens for **small** moves in the underlying or vol. They do not capture:

1. **Large-move risk** -- A book that is short -$5,000 of dollar gamma per 1% is not just $5k short on a 5% move. The actual loss is non-linear and explodes with move size. For tail risk, you need [[options-stress-testing]] -- pricing every position under specified shocks (e.g., -10% spot + 10 vol points + skew steepening) and reading the actual P&L.
2. **Cross-Greek interactions** -- Vanna, charm, and vomma move with shocks. A book that looks vega-flat at current spot can become heavily long or short vega after a 5% move.
3. **Liquidity and bid-ask** -- Aggregated Greeks assume you can mark and rebalance at mid. In a real shock, single-name option spreads widen 5-10x, and you cannot trade out at your model's prices.
4. **Skew and surface dynamics** -- A "1 vol point shift" assumes parallel surface moves. In reality, [[volatility-skew|skew]] steepens in selloffs (puts expand vol more than calls), and vol-of-vol regimes shift. Decompose vega into ATM-vega and skew-vega for any book with significant OTM exposure.
5. **Path dependency** -- Greeks tell you exposure now. They do not tell you what your exposure will be in 5 days after the position has drifted, decayed, and been partially hedged. That requires [[scenario-analysis]] and **path simulation**.
6. **Correlation breaks** -- Beta-weighting assumes historical correlations hold. In a crisis, every "low-beta" position becomes a 1-beta position to a falling market. The TLT-as-hedge in the worked example would help in a 2008-style flight-to-quality but **hurt** in a 2022-style yields-up-stocks-down regime.
7. **Discrete event risk** -- Earnings, FOMC, expiry. Greeks-based risk fails to capture jump risk; you need [[gap-risk]] and [[event-risk-budgeting]].

Aggregated Greeks are necessary but not sufficient. They are the daily heartbeat of options risk; they are not the cardiology workup. Pair them with [[options-stress-testing]], [[scenario-analysis]], and [[var|VaR]] / [[expected-shortfall]] for a complete picture.

## Related

- [[options-greeks]] -- The per-contract Greeks this page aggregates
- [[delta]], [[gamma]], [[vega]], [[theta]] -- The individual first-order Greeks
- [[position-sizing]] -- Greek-based sizing; aggregation is its book-level input
- [[options-portfolio-construction]] -- How to build a book whose aggregated Greeks meet your targets
- [[options-risk-budgeting]] -- Setting and enforcing limits on aggregated Greeks
- [[options-concentration-risk]] -- When aggregates hide a single concentrated bet
- [[vega-budgeting]] -- Specific application: limiting net vega exposure
- [[theta-targeting]] -- Sizing for a desired daily decay
- [[delta-neutral]] -- The state where (typically beta-weighted) book delta is zero
- [[vega-hedging]] -- Trading strategies to offset book-level vega
- [[beta-weighted-delta]] -- Detailed treatment of the beta-weighting technique
- [[gamma-scalping]] -- Strategy for harvesting gamma exposure on a delta-neutral book
- [[options-stress-testing]] -- The non-local complement to Greeks-based risk
- [[portfolio-margin]] -- What the aggregated book is margined against
- [[value-at-risk]] -- Statistical risk metric that complements aggregated Greeks
- [[trade-repair-and-rolling]] -- Reshaping positions to bring aggregates back inside budget
- [[volatility]] -- The risk dimension vega aggregation measures
- [[volatility-skew]] -- Why "1 vol point" does not mean a parallel shift
- [[term-structure-of-volatility]] -- Why front-month and back-month vega aggregate poorly
- [[margin]] -- Capital charged against the aggregated exposure
- [[risk-management]] -- The broader discipline

## Sources

- General knowledge -- portfolio Greeks aggregation, dollar conversion, and beta weighting are standard practice on every institutional options desk; treatments appear in Natenberg's *Option Volatility and Pricing*, Sinclair's *Volatility Trading*, and the [[itpm-trading-program|ITPM]] options professional curriculum.
- [[book-option-volatility-and-pricing]] -- Natenberg, ch. 18 ("Risk Considerations") covers per-position Greek calculation; book-level aggregation is implicit throughout.
- [[book-volatility-trading]] -- Sinclair, ch. 11-12 cover portfolio-level vega normalization and cross-underlying risk aggregation.
