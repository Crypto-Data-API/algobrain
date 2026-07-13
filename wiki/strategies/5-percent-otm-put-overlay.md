---
title: "5% OTM Put Overlay"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, risk-management, sp500, indicators, derivatives, volatility]
aliases: ["5% OTM Put Overlay", "SPY Put Overlay", "Shallow OTM Put Hedge", "5% Put Protection Program"]
related: ["[[index-options]]", "[[spx-options]]", "[[spy-options]]", "[[xsp-options]]", "[[long-put]]", "[[protective-puts]]", "[[long-vol-overlay]]", "[[long-vol-vs-short-vol]]", "[[universa-investments]]", "[[mark-spitznagel]]", "[[tail-risk-hedging]]", "[[volatility-skew]]", "[[itpm-trade-construction-playbook]]", "[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[hedging-cost-budget]]", "[[barbell-portfolio]]", "[[volatility-risk-premium]]"]
strategy_type: hybrid
timeframe: position
markets: [stocks, options, index-options, sp500]
complexity: intermediate
backtest_status: live
edge_source: [risk-bearing, structural]
edge_mechanism: "Pays an explicit, budgeted hedging premium in exchange for a stream of fast-monetising payouts during 5-15% drawdowns; sits between the cheap-but-slow Universa-style 20%+ OTM tail hedge and the expensive at-the-money put which monetises every wiggle."
data_required: [options-chain, implied-volatility, volatility-skew, sp500-spot]
min_capital_usd: 50000
capacity_usd: 1000000000
crowding_risk: low
expected_sharpe: -0.4
expected_max_drawdown: 0.05
breakeven_cost_bps: 0
deploy_date: 2026-05-07
capital_allocation: "1-3% of NAV per year on premium budget"
kill_criteria: |
  - annual hedging cost exceeds 4% of NAV (skew became too rich)
  - hedge has produced zero monetisation across 24+ months (regime change in tail behaviour)
  - the underlying long book has materially shrunk such that overlay no longer matches notional
last_review: 2026-05-07
next_review: 2026-08-07
---

A **5% OTM put overlay** is a continuous tail-hedging program that maintains long [[long-put|put options]] roughly 5% out-of-the-money on [[spx-options|SPX]], [[spy-options|SPY]], or [[xsp-options|XSP]], rolled at 60-90 [[days-to-expiration|DTE]], and sized to spend 1-3% of NAV per year on premium. It sits in the middle of the protective-put spectrum — shallower (and faster to monetise) than the 20%+ OTM "[[universa-investments|Universa]]-style" deep-tail hedge, and cheaper (with less convexity) than a near-the-money protective put. It is the canonical [[tail-risk-hedging|tail hedge]] / [[long-vol-overlay|long-vol overlay]] used to offset the left-tail exposure of a long-equity book or of short-premium sleeves elsewhere in the portfolio.

## Quick Reference

| Parameter | Value |
|---|---|
| **Instrument** | Long puts on [[spx-options\|SPX]] / [[spy-options\|SPY]] / [[xsp-options\|XSP]] |
| **Strike** | ~5% OTM (4-6% range acceptable) |
| **DTE** | 60-90 days, rolled at ~30 DTE remaining |
| **Premium budget** | 1-3% of NAV per year (a hard, pre-committed line item) |
| **Notional coverage** | 80-150% of long-book notional |
| **Edge source** | [[edge-taxonomy\|Risk-bearing (in reverse) + structural]] — pays [[volatility-risk-premium\|VRP]] for fast convex payouts |
| **Standalone expectancy** | Negative — it is insurance, not alpha |
| **Portfolio effect** | Raises combined Sharpe ~0.1-0.3 (illustrative); cuts long-book max drawdown materially |
| **Tax** | [[section-1256-contracts\|Section 1256]] 60/40 when on SPX/XSP |
| **Position in spectrum** | Middle: faster than [[universa-investments\|20%+ Universa deep tail]], cheaper than ATM protective put |

### Where it sits in the protective-put spectrum

| Hedge | Strike | Cost (indicative) | Monetises on | Convexity / payoff per $ |
|---|---|---|---|---|
| Near-the-money protective put | ~0-2% OTM | High (5%+/yr) | Every wiggle | Low — pays for noise |
| **5% OTM overlay (this page)** | ~5% OTM | Moderate (1-3%/yr) | Garden-variety -7% to -15% drawdowns | Medium — the middle ground |
| [[universa-investments\|Universa-style deep tail]] | 20%+ OTM | Low (<1%/yr) | Only 1-in-20-year crashes | Very high — explosive in true tails |

All cost figures are indicative and regime-dependent (skew drives them); see the disclaimer in Performance Characteristics.

## Edge Source

The 5% OTM put overlay is *not* a positive-expectancy trade in isolation. Like all explicit hedging programs, its expected return on the standalone leg is negative. The edge it provides at the *portfolio* level comes from two sources in the [[edge-taxonomy]]:

1. **Risk-bearing edge (in reverse)** — The overlay buyer pays the [[volatility-risk-premium|VRP]] to other market participants in exchange for fast access to convex payoffs in left-tail scenarios. The cost of this insurance is real and recurring; the value is realised only when the equity book is suffering. In efficient markets the standalone NPV is negative, but the *portfolio* Sharpe can rise materially because the hedge releases capital exactly when the rest of the book is impaired.
2. **Structural edge** — Funds with explicit drawdown limits, prop desks with VaR caps, and family offices with stated "no double-digit drawdowns" mandates derive utility from the hedge that exceeds the dollar cost. The overlay converts an unbudgetable tail risk into a budgeted line item, which has structural value even when the dollars net negative.

Compare the design choices on the [[long-vol-vs-short-vol]] spectrum: a 5% OTM overlay sits at "cheap insurance, useful in 1-in-5-year events"; a 20%+ Universa-style overlay sits at "very cheap insurance, useful only in 1-in-20-year events but with much higher payoff."

## Why This Edge Exists

The hedge is needed because:

1. The S&P 500 has experienced 14 drawdowns of 10%+ since 1980 — roughly one every 3 years. A 5% OTM put rolled continuously will monetise meaningful payouts on most of these events.
2. Long-equity portfolios cannot reliably reduce exposure during a stress event without crystallising losses. A pre-positioned put overlay monetises into cash without disturbing the underlying book.
3. Pension and institutional capital is structurally short the put: their liabilities are convex while their equity holdings are roughly linear. Buying a put overlay shifts the convexity profile to match the liability stream.

The overlay is *not* an arbitrage — it costs money in expectation. The strategy works because the buyer values the cash flow timing of the payouts (in a stress event) more than the dollars cost of the premium (in calm weeks).

## Null Hypothesis

Under the null that put options are fairly priced and the equity book has no special covariance with shocks, the overlay is a pure cost: ~1-3% of NAV per year forgone, with statistical breakeven only when realised tail magnitude exceeds the implied tail. Backtests since 1990 show that on average the overlay loses money on a standalone basis — the volatility risk premium is real and runs against the buyer. The strategy is justified only if (a) the holder believes their realised tail risk exceeds the market's implied tail, or (b) the holder values cash payoff in stress events at a higher utility than dollars cost in calm.

## Rules

### Sizing

| Parameter | Value | Notes |
|---|---|---|
| Strike distance from spot | 5% OTM (puts) | At SPX 5000, buy 4750 strike |
| DTE at entry | 60-90 days | Optimal trade-off between gamma decay and theta cost |
| Annual premium budget | 1-3% of NAV | "Insurance line item" |
| Notional coverage | 80-150% of long book notional | Typically slight over-hedge for convexity |
| Rolling frequency | At ~30 DTE remaining or upon -50% premium loss (theta) | Whichever first |

### Entry Mechanics

1. **Compute long book notional.** Sum the dollar value of all long-equity exposure in the book to be hedged. SPY equivalents work for diversified large-cap; for tilted books beta-weight to the S&P first.
2. **Choose product.** [[spx-options|SPX]] for tax efficiency (Section 1256 60/40 treatment) and large-account scale; [[spy-options|SPY]] for sub-$100K accounts where the smaller multiplier and penny tick matter; [[xsp-options|XSP]] for small accounts wanting Section 1256 treatment.
3. **Strike selection.** Buy the strike closest to 5% below current index level. Round to nearest available strike interval. The "5%" is a guideline; in practice 4-6% range is acceptable.
4. **Expiry selection.** 60-90 DTE. Avoid 30 DTE or shorter (gamma decay too fast); avoid 180+ DTE (vega exposure too large for hedge purpose).
5. **Position size.** N puts where N × strike × multiplier ≈ 80-150% of long-book notional. For SPX with $100 multiplier and a $10M long book at SPX 5000, N ≈ 20-30 contracts.

### Rolling Mechanics

The overlay is continuously maintained — you do not "let it expire."

1. **Monthly review.** At the start of each calendar month, check days remaining on each layer.
2. **Roll trigger.** When DTE remaining ≤ 30, OR when premium has decayed to ≤ 50% of entry value, roll forward.
3. **Roll mechanics.** Sell the existing put, buy a new 60-90 DTE 5% OTM put. The roll is a debit if vol has been calm (premium has decayed) and may be a credit if vol has expanded.
4. **Layer rolling for smoothness.** Sophisticated implementations roll in tranches — divide the hedge into 3 or 4 layers, each rolled at a different month, so the program is never wholly expiring at once. This dampens the path dependence of single-roll timing.
5. **Vol-regime adjustment.** When VIX is structurally elevated (>25), some implementations reduce the hedge size by 25-50% because puts become expensive and skew is rich; restore full size when VIX returns under 18.

### Monetisation Rules

When the underlying drops materially:

1. **Threshold trigger.** If the index falls 5%+ from when the put was bought, the put is at-the-money or in-the-money. Decide whether to monetise the gain or hold for further drop.
2. **Partial monetisation.** Common rule: sell half the puts when the underlying is 7-10% below entry strike, hold the rest as a continuing tail hedge.
3. **Re-establish the overlay.** After monetisation, the hedge layer is missing. Re-buy 5% OTM puts at the *new* lower index level to maintain the program. This "reset" mechanic is the secret to compounding the hedge through a multi-leg drawdown.
4. **Cash deployment.** The cash from monetised puts can be (a) added back to the long book at lower prices (rebalance), (b) used to buy more hedges, or (c) held as dry powder.

## Implementation Pseudocode

```python
def five_pct_otm_put_overlay(
    long_book_notional_usd: float,
    nav_usd: float,
    annual_premium_budget_pct: float = 0.02,  # 2% of NAV
    target_dte: int = 75,
    layers: int = 4,
):
    chain = get_options_chain("SPX")
    spot = chain.spot
    target_strike = round_to_strike_interval(spot * 0.95, interval=5)
    target_expiry = today + timedelta(days=target_dte)

    # Notional coverage 100% by default, can scale up to 150%
    contracts_total = ceil(long_book_notional_usd / (target_strike * 100))

    # Layer the hedge across 4 monthly tranches for smoothness
    contracts_per_layer = ceil(contracts_total / layers)

    # Premium budget check
    quote = chain.quote(strike=target_strike, expiry=target_expiry, right="P")
    annualised_cost = (quote.mid * 100 * contracts_total) * (12 / 3)  # quarterly roll
    cost_pct = annualised_cost / nav_usd
    if cost_pct > annual_premium_budget_pct * 1.5:
        warn(f"Overlay costing {cost_pct:.2%} — exceeds budget. Reduce size or wait for vol mean-revert.")

    # Place the bottom layer (this month's tranche)
    return Order(
        action="BUY",
        underlying="SPX",
        right="P",
        strike=target_strike,
        expiry=target_expiry,
        qty=contracts_per_layer,
    )
```

## Indicators / Data Used

- SPX or SPY spot level (continuous)
- [[implied-volatility|IV]] of 60-90 DTE 5% OTM puts (the entry premium)
- [[volatility-skew]] of the put wing — informs whether the strike is rich or cheap
- VIX level — rough check on whether the hedge is in a "buy" or "wait" regime
- Long book beta-adjusted notional — denominator for sizing
- Realised drawdown of the long book — trigger for monetisation decisions

## Example Trade

**Reference scenario: $5M long-equity book, deploying overlay in January 2026.**

- January 2026: SPX at 5000. Long book notional $5M. Annual premium budget 2% of $5M = $100K.
- Buy 10 SPX 4750 puts at 75 DTE for $25 each = $25,000 total cost (premium = 0.5% of NAV).
- Quarterly cycle would cost $100K, matching budget exactly.
- February 2026: SPX drops to 4700 on banking-stress headlines.
  - 4750 puts now at $90 each. Position value: $90,000 (3.6x return on the put leg).
  - Sell 5 puts at $90 = $45,000 cash booked.
  - Re-establish overlay: buy 5 new SPX 4465 puts (5% OTM at 4700) at 75 DTE for $22 each = $11,000.
  - Net cash captured: $45,000 - $11,000 = $34,000 = 0.68% of NAV.
- Long book at this point down ~6% on the SPX move = -$300K. Overlay monetisation offsets ~10% of that.
- April 2026: SPX recovers to 4900. Overlay puts decay. Roll forward as scheduled.

The example shows the overlay is *not* a profit centre — it offset 10% of the drawdown, far less than the long book's losses — but it provided the cash to rebalance into the dip without forcing a sale of the long book at distressed prices.

## Performance Characteristics

> **No fabricated backtest.** The figures below are *qualitative orders of magnitude* describing the well-understood shape of a continuous put-overlay program (negative standalone carry, episodic large monetisations, drawdown compression at the portfolio level). They are illustrative, not the output of a specific proprietary backtest, and the realised numbers depend heavily on the [[volatility-skew|skew]] regime, roll discipline, and the path of the drawdown. Treat them as "this is the characteristic profile," not "this is what you will earn."

The characteristic profile of a 5% OTM, 75-DTE rolling put overlay sized to a 1-2% NAV budget:

- **Annualised drag in calm regimes:** roughly -1.5 to -2.5% per year on the hedge leg in isolation (the cost of insurance; this is the [[volatility-risk-premium|VRP]] running against the buyer).
- **Monetisation events in 10%+ drawdowns:** a multiple (order of several×) return on the premium spent *in that month* — convex payoff is the point.
- **Long-book max-drawdown reduction:** materially lower combined drawdown — the overlay clips the left tail of the equity book rather than the body.
- **Sharpe of the overlay leg:** negative (frontmatter `expected_sharpe: -0.4`) — by construction; insurance has negative standalone expectancy.
- **Sharpe of long book + overlay (combined):** typically *improves* modestly vs the unhedged book, because the hedge releases cash exactly when the book is impaired.
- **Tax efficiency:** SPX/XSP-based overlay benefits from [[section-1256-contracts|Section 1256]] 60/40 treatment, materially improving after-tax economics vs SPY or single-name puts. See [[tax-implications-trading]].

The first-order takeaway is regime-dependent: in calm regimes the overlay is a steady, budgeted drag; in stress regimes it is a fast, convex source of cash. Judging it on its calm-regime Sharpe alone is the central analytical error — it is a portfolio component, not a standalone strategy.

## Monitoring Checklist

Run this review at least monthly (and intraday during a stress event):

1. **Coverage ratio.** Does current put notional still sit at 80-150% of the (beta-weighted) long-book notional? Drift here is the most common operational decay.
2. **Strike distance.** Has spot moved enough that the active layer is no longer ~5% OTM? Re-strike on the next roll.
3. **DTE ladder.** Are the layers staggered, or have they bunched into a single expiry (a hedge gap)?
4. **Budget tracking.** Year-to-date premium spend vs the 1-3% NAV budget. If on pace to breach 4%, the [[volatility-skew|skew]] has richened — float the strike to 7-8% OTM rather than overspend.
5. **Roll trigger status.** Any layer at ≤30 DTE remaining or ≤50% of entry premium? Roll it.
6. **Monetisation readiness.** If the index is within ~5% of the active strike, pre-decide the partial-monetisation and re-establishment plan before the move, not during it.
7. **Regime check.** [[vix|VIX]] level — in structurally elevated regimes (>25) consider trimming size 25-50%; restore when VIX returns under 18.

## Capacity Limits

- The 5% OTM SPX put market is the single deepest options market in the world; capacity is effectively unlimited for any individual or institutional account up to multi-billion-dollar scale.
- For SPY-based implementations, capacity is constrained at extreme size (>$1B notional) by put-side liquidity in the wing strikes, but well within reach for retail accounts.
- The strategy does not "saturate" the way alpha strategies do — it is a budgeted cost program, not an alpha extraction.

## What Kills This Strategy

Drawing from [[failure-modes]] and [[hedging-program-failure-modes]]:

1. **Skew steepening** — In persistent bear regimes, OTM put skew steepens dramatically and the 5% strike becomes much more expensive. Annual cost can balloon from 1.5% of NAV to 5%+ of NAV, breaking the budget. The fix is to cap the budget and let the strike float (e.g., 7-8% OTM in expensive regimes).
2. **Slow grinding declines** — A multi-month -25% drawdown that takes longer than the put's DTE drops the long book without the overlay ever monetising effectively. Each new put expires worthless before the underlying hits the strike. Universa addresses this with deeper OTM puts that compound rolls; the 5% overlay is more vulnerable.
3. **Vol regime change** — A regime where 5% drawdowns are common but 15%+ drawdowns are absent (the "boring volatility" regime of 2017) means continuous theta cost with no large-payoff events.
4. **Roll timing mistakes** — Rolling at the wrong DTE or not staggering layers can leave the program with hedge gaps. The August 2015 flash crash hit some overlay programs that had just rolled; the new put hadn't yet developed gamma when the move hit.
5. **Operational decay** — Hedging programs that aren't reviewed regularly drift in size relative to the long book, leaving the book under- or over-hedged.

## Kill Criteria

- Annual hedging cost exceeds 4% of NAV → reduce strike to 7-8% OTM or pause.
- Hedge has produced zero monetisation across 24+ months and underlying long book is materially smaller → review whether the overlay is still appropriate sizing.
- Realised Sharpe of *combined* long + overlay book is materially lower than unhedged comparable over 36+ months → audit.
- See [[when-to-retire-a-strategy]].

## Advantages

- Faster monetisation than [[universa-investments|Universa-style 20%+ OTM]] tail hedges — cash is realised on garden-variety -7% drawdowns that happen multiple times per decade.
- Strict premium budget — the cost is bounded and predictable.
- Tax-efficient when implemented on SPX or XSP (Section 1256 treatment).
- Liquid markets — execution is easy at any size up to billions of notional.
- Composable with short-vol income strategies elsewhere in the book — offsets the tail risk of [[short-strangle|strangles]] and [[iron-condor|condors]].
- Preserves the long book's compounding without forcing realisation of gains.

## Disadvantages

- Negative expectancy on the standalone leg — costs money in calm regimes.
- Lower convexity than deeper OTM hedges — a 30%+ shock pays out less per dollar spent than a 20%+ OTM Universa-style hedge would.
- Path-dependent monetisation — slow drawdowns may never produce a payout even when the index ultimately drops 25%.
- Roll mechanics matter — naive rolling at fixed dates loses to layered rolling.
- Skew can make the program structurally unaffordable in certain regimes.
- Compares unfavourably to deeper OTM tail hedges on shock-event Sharpe.

## Sources

- Spitznagel, Mark — *Safe Haven: Investing for Financial Storms* (2021). Chapter 10 on insurance-based portfolio construction. See [[safe-haven-spitznagel]].
- Cboe research notes on the [[bxm-index|BXM]] and [[put-index|PUT]] indices for benchmark hedging cost data.
- Goldman Sachs portfolio strategy research on tail-hedging cost-benefit (annual reports 2018-2024).
- Universa Investments client letters (multiple years) — comparison data on 20%+ OTM tail hedges. See [[universa-investments]].
- AQR research papers on the [[volatility-risk-premium|VRP]] and the cost of put-buying programs.
- ITPM curriculum on [[long-vol-overlay|long-vol overlays]] within institutional book construction.

## Related

- [[long-put]], [[protective-puts]] — the parent structures
- [[long-vol-overlay]] — broader category this overlay sits within
- [[universa-investments]], [[mark-spitznagel]] — deeper-tail comparison
- [[long-vol-vs-short-vol]] — the philosophical context
- [[index-options]], [[spx-options]], [[xsp-options]] — the preferred underlyings
- [[hedging-cost-budget]] — the budgeting framework
- [[volatility-skew]] — informs strike-distance economics
- [[barbell-portfolio]] — the broader Taleb/Spitznagel approach this overlay supports
- [[options-portfolio-construction]] — book-level integration
- [[itpm-trade-construction-playbook]] — institutional methodology
- [[tail-risk-hedging]] — the broad category this strategy implements
- [[options-risk-budgeting]] — the budget framework the tail-hedge sleeve sits inside
- [[the-theta-trap]] — the short-premium failure mode this overlay is designed to offset
- [[risk-of-ruin]] — why a budgeted tail hedge improves long-run survivability
- [[volatility-risk-premium]] — the premium the overlay buyer pays
- [[tax-implications-trading]] — Section 1256 treatment of SPX/XSP puts
