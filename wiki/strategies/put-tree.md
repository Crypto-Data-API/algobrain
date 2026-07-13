---
title: "Put Tree (Long Put Ratio Tree)"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, derivatives, volatility, risk-management]
aliases: ["Long Put Tree", "Put Ratio Tree", "Three-Strike Put Spread", "Christmas Tree Put Spread"]
strategy_type: quantitative
timeframe: position
markets: [options]
complexity: advanced
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "Stack defined-debit put exposure across three strikes so the structure pays max in a moderate-to-large drawdown but caps the cost of the deepest tail; the seller of the lower legs is a market-maker absorbing far-OTM put inventory at structurally low premiums."
data_required: [spx-options-chain, vix-spot, skew-data]
min_capital_usd: 25000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: -0.3
expected_max_drawdown: 0.03
breakeven_cost_bps: 150
related: ["[[spx-puts]]", "[[vix-call-spreads]]", "[[tail-risk-hedging]]", "[[options-concentration-risk]]", "[[long-vol-vs-short-vol]]", "[[long-vol-overlay]]", "[[ratio-spread]]", "[[debit-spread]]", "[[put-spread]]", "[[skew]]", "[[implied-volatility]]", "[[universa-investments]]", "[[convexity]]", "[[gamma]]", "[[vega]]", "[[1x2-ratio-spread]]"]
---

A **put tree** (or "Christmas tree put spread") is a defined-cost long-vol structure that stacks put exposure across three strikes: long one put at a higher strike, short one put at a middle strike, and long two puts at a lower strike — or variants of this 1×1×2 / 1×2×1 ratio. The structure is engineered to **maximize convex payoff in the 5-15% drawdown zone** while remaining funded (small debit) and capping the deepest-tail exposure. It is the structure of choice for traders who want long-vol overlay payoff but cannot stomach the bleed of a continuous OTM [[spx-puts|SPX put]] program — and is an explicit recommendation in the [[itpm|ITPM]] / [[options-concentration-risk]] long-vol overlay menu.

## Edge Source

The edge is **structural** with a **risk-bearing** component. The middle short strike is priced at the steep part of the [[skew|put skew]] curve — relatively expensive due to systemic put-buying — while the lower long strike, despite being further OTM, is priced at the *flatter* far-tail portion of the skew where premium per unit of notional protection is structurally cheap. By selling the expensive middle strike to fund the cheap deep-tail strikes, the structure captures a skew-shape arbitrage in addition to its directional payoff.

## Why This Edge Exists

1. **Skew is non-linear.** The implied volatility of equity index puts rises steeply from 25-delta to 5-delta but flattens out beyond 1-delta. This creates a "kink" in the skew curve that put trees exploit.
2. **Hedger demand concentrates in the 5-15% OTM zone.** Pension funds and risk-parity allocators systematically buy puts at this zone because their VaR models are calibrated to 1-month, 95-99% confidence intervals — exactly the zone where the put tree is short. The far-tail (15%+ OTM) is comparatively under-bought.
3. **Market-maker inventory dynamics.** Market makers sitting long deep-tail puts (from accumulating retail short-put-spread flow) are willing to sell them at structurally suppressed premiums to clear inventory. The put tree's lower long legs benefit from this.
4. **Defined cost makes the structure scalable.** Unlike a naked OTM put program, the put tree's cost is locked in at the moment of trade construction. This makes it easier for institutional allocators to budget and for retail traders to size correctly.

## Null Hypothesis

Under random / no-edge conditions, the put tree should bleed at a rate proportional to its net debit divided by tenor — typically 1-2% of capital allocated per month for a 30-60 DTE structure. The structure exhibits an edge if (a) realized monetization shows higher payoff frequency in the 5-15% drawdown zone than Gaussian models predict, and (b) the skew kink between middle and lower strikes persists across regimes.

## Rules

### Construction (1×1×2 Long Put Tree)

| Leg | Strike (relative to spot) | Position |
|---|---|---|
| Long put | 5-7% OTM | +1 |
| Short put | 10-12% OTM | -1 |
| Long puts | 15-20% OTM | +2 |

For SPX at 5,000:
- Long 1 SPX 4,700 put (6% OTM)
- Short 1 SPX 4,500 put (10% OTM)
- Long 2 SPX 4,100 puts (18% OTM)

Net result: small debit (typically $0.50-$2.00 per tree), defined cost, and a payoff curve that:

- Starts gaining intrinsic value as SPX falls through the upper long strike (~-6%)
- Reaches a first plateau near SPX -10% (the upper-minus-middle strike width, locked in once both are ITM)
- Stays roughly flat between -10% and -18% (mid-life marks can sag slightly here as the short middle strike gains value fastest)
- Re-accelerates below -18% as the two lower long legs activate
- Continues to gain unboundedly to the downside (net +2 puts below the lower strike)

### Variant: 1×2×1 (Christmas Tree)

| Leg | Strike | Position |
|---|---|---|
| Long put | 5-8% OTM | +1 |
| Short puts | 10-12% OTM | -2 |
| Long put | 15-18% OTM | +1 |

This is the classic "Christmas tree" — narrower payoff cone, no unbounded gain. Cheaper but with a defined max gain. Used when a smaller, more predictable hedge is preferred. **Caution:** the wings must be kept near-equidistant from the middle strike; if the lower wing is materially wider than the upper (a broken-wing tree), the structure carries a deep-tail *liability* equal to the width difference, which defeats the hedging purpose.

### Sizing

- Allocate **2-3% of NAV per year** (~0.2-0.25% per month) to put trees, in line with other long-vol overlay budgets — this is what produces the -2% to -3% calm-regime annual cost shown under Performance.
- Granularity matters: one full-size SPX tree costs roughly $1,500-$2,500 of debit. Books under ~$1M should ladder with [[xsp|XSP]] (1/10th-size) trees monthly, or build full SPX trees quarterly, to stay inside the budget.
- For a $1M book: one SPX tree per month at ~$1,500-$2,500 debit ≈ 2-3% of NAV per year.
- Stack 2-3 expiry ladders so a portion of the structure is always 30+ DTE.

### Tenor

- **30-60 DTE** is the standard zone — best balance of [[gamma]] convexity and roll frequency.
- **90+ DTE** versions exist but lose the [[gamma]] kicker that makes the structure attractive.

### Roll / Exit

- **Monetize when SPX drops 5-12%** — the sweet spot of the structure. Sell the entire tree.
- **Hold to expiry** if drawdown is mild or recovers — let the structure run its full theta.
- **Roll forward monthly** as expiries close in.

## Implementation Pseudocode

```python
def construct_put_tree(account_nav, spx_spot, target_dte=45):
    monthly_budget = account_nav * 0.002  # ~0.2% / month, ~2.5% / year

    # Construction: 1x1x2 long put tree
    upper_strike = round_to_25(spx_spot * 0.94)   # 6% OTM
    middle_strike = round_to_25(spx_spot * 0.90)  # 10% OTM
    lower_strike = round_to_25(spx_spot * 0.82)   # 18% OTM

    expiry = next_monthly_expiry(target_dte)

    # Get prices at mid
    upper_price = get_put_price(upper_strike, expiry)
    middle_price = get_put_price(middle_strike, expiry)
    lower_price = get_put_price(lower_strike, expiry)

    # Net debit = +1*upper - 1*middle + 2*lower
    net_debit = upper_price - middle_price + 2 * lower_price

    if net_debit <= 0:
        return "structure prices as a credit — strike selection error or skew distortion"

    # Size to budget
    trees = int(monthly_budget / (net_debit * 100))

    return submit_combo_order(
        legs=[
            ("BUY", upper_strike, expiry, trees),
            ("SELL", middle_strike, expiry, trees),
            ("BUY", lower_strike, expiry, trees * 2),
        ],
        net_debit=net_debit,
    )
```

## Indicators / Data Used

- SPX options chain — full skew surface
- Spot [[vix]] level
- 25-delta vs 5-delta skew slope
- Realized vs implied vol comparison at the relevant tenors
- Historical drawdown distribution (1-month, 3-month) for context

## Payoff & Greeks

The defining property of the 1×1×2 put tree is a payoff that is **tuned to the 5-15% drawdown zone**: it ramps up as spot falls through the upper long strike, plateaus through the short-strike region, then re-accelerates and runs unbounded once the two lower long legs activate. The 1×2×1 Christmas-tree variant caps the gain instead of running unbounded.

1×1×2 long put tree, at-expiry payoff (strikes: upper U, middle M, lower L):

```
   P&L
    |                                    *   <- below L: net +2 puts, unbounded
    |                                 *
    |                               *
    |        ___________          *
    |       /           \___     *           <- plateau / slight sag through M
    |      /                 \  *
  0 +-----/--------------------\*---------------  spot at expiry
    |    /  (5-15% zone gains)  (L)  (M)  (U)
    |  _/  net debit (max loss = debit paid)
    |  (-debit)
```

Net Greeks of the 1×1×2 tree, and how they map to the loss distribution:

| Greek | Sign (at entry, calm) | Behaviour |
|---|---|---|
| [[delta]] | Slightly negative | Grows negative as spot falls into the upper/middle strike band; the net +1 put above the short strike dominates first |
| [[gamma]] | Mixed → net long | The short middle strike subtracts gamma in the plateau zone, but the two lower long legs make the structure strongly **long gamma** in the deep tail |
| [[theta]] | Negative (small) | The bleed is the net debit amortized over tenor — far smaller than a naked [[spx-puts|OTM put]] program because the short middle leg funds it |
| [[vega]] | Net long | An IV spike marks the whole tree up; but the short middle strike (priced on the steep part of the [[skew]]) gives back some vega, which is *why* the tree underperforms naked puts in a vol explosion |

The structure is **long gamma, long vega, mildly short theta** — the long-vol signature — but with a deliberate notch cut out of the deep-tail vega via the short middle strike. That notch is the funding mechanism (cheaper carry) and simultaneously the disadvantage (deep-tail underperformance versus naked puts). The trade is, in Greeks terms, a bet that drawdowns resolve in the 5-15% band more often than the far tail — which historical [[market-regime|regime]] data broadly supports for typical corrections.

## Example Trade

**Setup (calm regime, May 2025-style):**

- SPX: 5,000
- VIX: 14
- Account NAV: $1,000,000
- Monthly tree budget: $2,000 (~2.4% of NAV per year)

**Construction (45 DTE, one tree):**

- Long 1 SPX 4,700 put @ $20.00 = -$2,000
- Short 1 SPX 4,500 put @ $9.00 = +$900
- Long 2 SPX 4,100 puts @ $2.75 = -$550
- **Net debit: $16.50 per tree = $1,650** (under budget)

Defined cost: $1,650. Defined max risk: $1,650. (SPX options carry a $100 multiplier; prices above are in index points.)

**Outcome A (calm — most months):** SPX drifts in 4,900-5,200. All puts expire worthless. Loss: $1,650 (~0.17% of NAV).

**Outcome B (8% correction):** SPX falls to 4,600 over 4 weeks. At expiry: the 4,700 put is worth 100 points ($10,000); the 4,500 and 4,100 puts expire worthless. Tree value: **$10,000 gross**, **+$8,350 net**. ~5x the debit.

**Outcome C (15% crash):** SPX falls to 4,250 with [[implied-volatility|IV]] spiking. Mid-life marks: 4,700 put ~470 pts (+$47,000); 4,500 put ~280 pts (-$28,000); 2 × 4,100 puts ~95 pts each (+$19,000). Tree value: **~$38,000 gross**, **+$36,350 net**. ~22x.

**Outcome D (30% crash, 2020-style):** SPX falls to 3,500 with VIX > 60. Marks: 4,700 put ~1,250 pts (+$125,000); 4,500 put ~1,050 pts (-$105,000); 2 × 4,100 puts ~650 pts each (+$130,000). Tree value: **~$150,000 gross**, **+$148,350 net**. ~90x.

Below the lower strike the 1×1×2 is net long two puts, so absolute payoff keeps growing in the deepest tail. But note the *relative* tradeoff: the same $1,650 spent on 4,100-strike puts alone (6 contracts @ $2.75) would be worth ~$360,000 at SPX 3,500 — naked deep-OTM puts dominate per premium dollar in a catastrophic crash. The put tree gives up deep-tail efficiency in exchange for a far better payoff in the **5-15% drawdown zone** (Outcomes B and C), which is where most equity drawdowns historically resolve.

## Performance Characteristics

| Metric | Pure put tree | In a blended book |
|---|---|---|
| Hit rate (months profitable) | 8-15% | n/a |
| Annualized cost (calm regime) | -2% to -3% of NAV | -1% net (offset by short-vol core) |
| Best-month payoff | 20-50x debit (mid-tail crash) | Materially reduces book drawdown |
| Worst case | Bounded at debit paid | n/a |
| Sharpe (standalone) | -0.3 to -0.7 | n/a |
| Sharpe (combined book over cycle) | n/a | Adds 0.2-0.4 over short-vol core alone |

### Behaviour by market regime

| Regime | Put-tree result | Versus naked [[spx-puts]] |
|---|---|---|
| Low-vol grind | Small defined bleed (the net debit) | Cheaper carry — the tree wins on cost |
| 5-15% correction | Best zone — 5-20x debit payoff | Tree wins decisively here |
| 30%+ crash with vol spike | Strong absolute gain, but short middle leg drags | Naked deep-OTM puts dominate per premium dollar |
| Slow-grind bear stalling near lower strike | Payoff already committed; underperforms | Naked puts keep gaining with continued decline |

The structure is therefore a **correction-insurance** instrument, not a **catastrophe-insurance** instrument — the opposite emphasis from the far-OTM [[spx-puts]] program. Books that want both layer the two (see "Stacks well with other overlays" under Advantages) against a [[long-vol-vs-short-vol|short-vol core]].

## Capacity Limits

For SPX-based put trees, capacity is essentially unlimited at retail and small-fund scale. Institutional-scale users rotating $100M+ of put-tree notional may face execution slippage on the deeper-OTM legs but can generally still execute. The structure is more bespoke than naked SPX puts, so larger institutional users typically prefer single-strike puts for execution simplicity.

## What Kills This Strategy

- **Skew compression.** If the kink between 10-delta and 5-delta IV flattens, the funding from the short middle leg disappears and the tree becomes uneconomic.
- **Slow-grind drawdown beyond the lower strike.** A drawdown that pierces the 4,100 strike but stays there (rather than continuing lower with vol expansion) underperforms a naked OTM put because the structure's payoff is already committed.
- **Catastrophic crash (relative underperformance).** The short middle leg drags on deep-tail proceeds: the 1×1×2 keeps gaining below the lower strike, but per premium dollar a 2020-style 35% crash pays naked deep-OTM puts a multiple of what the tree pays. If the mandate is catastrophe insurance rather than correction insurance, the tree is the wrong structure.
- **Wrong-tenor risk.** A 30 DTE tree provides poor protection against a 6-month drawdown.
- **Pin risk at middle strike.** If SPX settles exactly at the middle strike at expiry, the trader is left long 1 ITM put and long 2 OTM puts with uncertain assignment — manage by closing 2-3 days before expiry.

## Kill Criteria

- **Cumulative bleed > 8% of NAV over 36 months** without monetization opportunities.
- **Combined-book Sharpe gain over 5 years < 0.1** vs short-vol-only counterfactual.
- **Skew kink (10-delta IV minus 5-delta IV) compresses to < 1.5 vol points** sustained — structural edge has eroded.
- **Net debit at construction exceeds 4% of upper-lower strike width** — the structure no longer offers convex value over a naked put.

## Advantages

- **Defined cost.** Maximum loss = net debit. No margin call risk, no [[gap-risk]].
- **Optimized for moderate drawdowns.** Pays best in the 5-15% zone — exactly where most equity drawdowns historically resolve.
- **Cheaper than naked OTM puts.** Net debit is typically 30-60% of an equivalent naked put position.
- **Captures skew kink.** Unique among long-vol structures in monetizing the put-skew non-linearity.
- **Stacks well with other overlays.** Combine with [[vix-call-spreads]] for vol-spike coverage and [[spx-puts|naked OTM puts]] for catastrophic crash coverage; the trio covers different parts of the loss distribution.
- **Funded structure.** Allocators allergic to "all bleed, no payoff most years" can get convex protection at a much lower premium.

## Disadvantages

- **Inefficient in the deepest tail.** In a Volmageddon-style or 1987-style crash, naked puts dominate the put tree per premium dollar (the short middle leg gives back a large slice of proceeds).
- **Pin risk at middle strike.** Requires active management near expiry.
- **Skew-shape dependence.** If skew kink compresses, the structural funding edge disappears.
- **Complex to construct and monitor.** Three legs in different ratios are harder to roll than a single strike.
- **Liquidity at deep strikes can be thin.** Bid-ask on 18-20% OTM SPX puts during normal hours can be 10-15% of mid; widens substantially in stress.
- **Behavioural cost.** Like all long-vol structures, most months produce zero payoff. Over a 5-year calm regime, cumulative bleed feels like dead weight.

## Sources

- Cohen, Guy. *Options Made Easy* (2005) — practitioner guide to ratio and tree spreads
- McMillan, Lawrence. *Options as a Strategic Investment* (5th ed., 2012) — covers ratio backspreads and put trees
- Natenberg, Sheldon. *Option Volatility and Pricing* (2nd ed., 1994)
- Bhansali, Vineer. *Tail Risk Hedging* (2014) — covers structured tail hedges including ratio variants
- [[itpm-trade-construction-playbook]] — long-vol overlay menu
- Cboe Global Markets, *SPX Skew Reports* — input data for construction

## Related

- [[spx-puts]] — naked OTM put alternative
- [[vix-call-spreads]] — alternative defined-debit long-vol overlay
- [[tail-risk-hedging]] — broader strategy class
- [[options-concentration-risk]] — the problem this addresses
- [[long-vol-vs-short-vol]] — philosophical framework
- [[long-vol-overlay]] — overlay sizing approach
- [[ratio-spread]] — the structural type
- [[debit-spread]] — the funding mechanism
- [[put-spread]] — simpler 2-leg variant
- [[skew]] — the structural input the trade exploits
- [[implied-volatility]] — input to construction
- [[universa-investments]] — fund using long-vol structures of this family
- [[convexity]] — the payoff property
- [[gamma]] — the Greek that drives the mid-life payoff
- [[vega]] — the Greek that drives IV-spike P&L
- [[delta]] — directional sensitivity as spot falls into the strike band
- [[theta]] — the small amortized bleed of the net debit
- [[market-regime]] — determines whether correction- or catastrophe-insurance is wanted
- [[premium-selling-systematic]] — the short-vol engine a put tree commonly hedges
