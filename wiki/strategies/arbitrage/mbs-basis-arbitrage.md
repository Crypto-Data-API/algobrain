---
title: "MBS Basis Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, bonds, derivatives, quantitative, history]
aliases: ["MBS Basis Trade", "Mortgage Basis Arb", "OAS Arbitrage", "Mortgage Spread Trade"]
strategy_type: quantitative
timeframe: position
markets: [bonds]
complexity: advanced
backtest_status: paused
edge_source: [risk-bearing, analytical, structural]
edge_mechanism: "Agency MBS trade at an option-adjusted spread over Treasuries that compensates holders for negative convexity and prepayment model uncertainty; the arb captures the OAS while hedging duration with Treasuries or swaps, rebalancing delta as prepayment speeds shift."
data_required: [tba-prices, treasury-yields, swap-curve, prepayment-models, primary-mortgage-rates, ginnie-fannie-freddie-pools]
min_capital_usd: 25000000
capacity_usd: 10000000000
crowding_risk: high
expected_sharpe: 0.7
expected_max_drawdown: 0.40
breakeven_cost_bps: 5
decay_evidence: "Fed QE 2009-2014 and 2020-2022 compressed MBS OAS to historic lows; 2022 rate shock reversed with extreme convexity pain"
related: ["[[ltcm-collapse-1998]]", "[[liars-poker]]", "[[salomon-brothers]]", "[[relative-value-arbitrage]]", "[[on-off-the-run-treasury-arbitrage]]", "[[swap-spread-arbitrage]]", "[[tips-treasury-arbitrage]]", "[[option-adjusted-spread]]", "[[negative-convexity]]", "[[prepayment-risk]]", "[[tba-market]]", "[[financial-crisis-2008]]", "[[quantitative-easing]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
---

# MBS Basis Arbitrage

MBS basis arbitrage is a [[relative-value-arbitrage|relative-value]] [[convergence-arbitrage|convergence trade]] that buys **agency mortgage-backed securities** (Fannie Mae, Freddie Mac, Ginnie Mae pass-throughs) and hedges the interest-rate exposure with Treasuries or interest-rate swaps, earning the **[[option-adjusted-spread|option-adjusted spread (OAS)]]** — the mortgage yield premium that compensates holders for bearing **[[prepayment-risk|prepayment risk]]** and **[[negative-convexity|negative convexity]]**. Pioneered by [[salomon-brothers|Salomon Brothers]]' mortgage desk in the 1980s (memorialized in [[liars-poker|*Liar's Poker*]]), it was a core profit engine for [[ltcm-collapse-1998|Long-Term Capital Management]] and remains central to every major fixed-income hedge fund and REIT today. The trade requires sophisticated prepayment modeling, daily delta rehedging, and deep pockets for balance-sheet financing. Like all [[limits-to-arbitrage|limits-to-arbitrage]] trades it pays a real premium for bearing a real risk — it is *not* a riskless arbitrage.

## Edge Source

**Risk-bearing** (primary), **analytical** (model-driven hedging), and **structural** (agency market plumbing). The MBS OAS is compensation for bearing real economic risks — convexity, prepayment model uncertainty, liquidity — not a true "arbitrage" in the risk-free sense. The analytical edge comes from better prepayment models than the street average. See [[edge-taxonomy]].

## Why This Edge Exists

An agency MBS is **an amortizing bond with an embedded short call option**: the homeowner can prepay (refinance, move, die) at par regardless of current market value. This makes the MBS:

1. **Negatively convex** — when rates fall, prepayments accelerate, shortening duration right when the holder wants long duration. When rates rise, prepayments slow, extending duration right when the holder wants short duration. The bond always shortens into rallies and lengthens into sell-offs.
2. **Model-dependent** — option-adjusted spread requires a prepayment model; different models disagree by 10-30 bps OAS. Practitioners with better models earn the analytical edge.
3. **Liquidity-tiered** — [[tba-market|TBA]] contracts are deeply liquid; specified pools, CMOs, and IO/PO strips are much less so.

Natural holders (banks, REITs, money managers) demand a premium (typically 25-75 bps OAS) for this complexity. The arb captures the OAS while hedging away duration. The counterparty is the **homeowner with a prepayment option** and the **real-money investor unwilling to delta-hedge daily**.

## Null Hypothesis

In a world with no prepayment option (bullet MBS), the MBS yield should equal a Treasury of matched duration plus a small credit/liquidity premium. The empirical OAS of 25-75 bps is the measure of what the market charges for bearing convexity and prepayment model risk. When OAS widens to 100+ bps (2008, 2022), something has gone structurally wrong and the arb is especially attractive *if* you have the capital to hold through.

## Rules

### Entry
1. Compute current-coupon 30Y MBS [[option-adjusted-spread|OAS]] using an industry-standard prepayment model (Yield Book, Andrew Davidson, internal).
2. Enter when OAS > 60 bps (above 10-year median ~45 bps, adjusted for regime).
3. **Buy** TBAs of the current-coupon production (most liquid).
4. **Hedge duration** — short a mix of 5Y and 10Y Treasury futures or pay-fixed on 5Y/10Y swap. The exact ratio comes from the model's effective-duration estimate.
5. **Hedge convexity** — optionally buy payer swaptions to offset the embedded short call (expensive but reduces tail risk).

### Daily Management
1. Recompute effective duration and rebalance the Treasury/swap hedge.
2. Monitor primary-secondary mortgage rate spread — if primary rates lag secondary, refi wave is delayed.
3. Track aggregate mortgage duration (Bloomberg MBDI index) — large spikes signal convexity-hedge flows from other holders, compounding pain.

### Exit
1. OAS tightens to < 30 bps → take profit.
2. Prepayment model shifts → recompute and exit if thesis breaks.
3. Financing pulled → forced exit (see [[ltcm-collapse-1998]]).

### Position Sizing
Stress: the 2022 rate shock moved MBS OAS from ~30 bps to ~85 bps in 9 months. Size so a 60 bp OAS widening does not exceed 25% of equity. Mortgage REITs (mREITs) sized at 6-8x leverage in 2013 lost 30-45% of market value when OAS widened ~30 bps during the [[taper-tantrum]].

## Implementation Pseudocode

```python
def mbs_basis_arb():
    oas = compute_current_coupon_oas(model="davidson", coupon=6.0, term=30)
    if oas < 60:
        return None

    mbs_position = buy_tba(coupon=6.0, settle="front_month", notional=500_000_000)

    effective_duration = mbs_position.effective_duration  # e.g., 4.5y (shorter than nominal 30y!)
    dv01 = mbs_position.dv01

    # Hedge with 5Y and 10Y Treasury futures
    short_5y = calculate_hedge_leg(dv01, tenor=5, weight=0.4)
    short_10y = calculate_hedge_leg(dv01, tenor=10, weight=0.6)

    # Optional: buy convexity
    convexity_hedge = buy_payer_swaption(strike_oom=50bp, expiry=3m, cost_bps=8)

    return Portfolio(
        long=mbs_position,
        hedges=[short_5y, short_10y, convexity_hedge],
        rebalance="daily_on_duration_drift",
    )
```

## Indicators / Data Used

- [[tba-market]] prices for current-coupon and adjacent coupons (5.0, 5.5, 6.0, 6.5)
- Agency pool-level prepayment speeds (CPR, PSA) from eMBS
- Prepayment model outputs (duration, convexity, OAS) — proprietary or vendor
- **Primary mortgage rate** (Freddie PMMS, MND surveys) vs **secondary** current-coupon yield
- [[mbs-duration-index]] (Bloomberg MBDI) for market-wide convexity stress
- [[treasury-yield-curve]] and swap curve for hedging
- FICO/LTV composition of deliverable pool — affects prepay speed

## Example Trade: LTCM's Mortgage Book (1997-1998)

LTCM held an enormous MBS basis position alongside its [[on-off-the-run-treasury-arbitrage|OTR/OFR]] and [[swap-spread-arbitrage|swap spread]] books. Rough reconstruction from Lowenstein (2000) and MacKenzie (2003):

- **Long** ~$30-50B face of agency MBS (principally FNMA current-coupon).
- **Hedged** via pay-fixed on interest rate swaps of matched effective duration.
- **Target OAS capture**: ~40-50 bps on a modest-duration book.
- **Leverage**: ~20-25x through repo financing.
- **Expected P&L**: ~10% return on capital at the strategy level.

What went wrong in August-September 1998:
1. OAS widened from ~45 bps to ~90+ bps during [[flight-to-quality]].
2. Simultaneously, OTR/OFR and swap spread trades moved against LTCM — correlated fixed-income RV.
3. Repo financing was pulled by counterparties who sniffed weakness.
4. Forced liquidation into illiquid markets deepened the OAS move.
5. The MBS book was one of the single largest loss contributors in the fund's final months.

## Example Trade: 2022 mREIT Pain

In 2022 the Fed hiked 425 bps and stopped MBS purchases. The MBS OAS widened from ~25 bps (QE-compressed) to ~85 bps by October 2022 (nominal current-coupon spreads to Treasuries widened far more, 100-150+ bps). Mortgage REITs — levered 6-8x buying MBS and hedging with swaps — posted severe book-value declines:

- **AGNC Investment Corp**: tangible book value per share down ~25-35% over 2022
- **Annaly Capital (NLY)**: book value per share down ~25-30% over 2022
- **ARMOUR Residential (ARR)**: among the hardest hit, down ~30-35%+ peak-to-trough

Those with *cash* in October 2022 (few) bought at generational OAS levels and earned 20-30% through 2024 as spreads normalized.

### OAS regime map (current-coupon agency MBS, indicative)

| Regime | Approx. current-coupon OAS | Trade implication |
|--------|----------------------------|-------------------|
| QE-compressed (2012-13, 2020-21) | ~10-30 bps | Crowded, thin carry; Fed is the marginal buyer — fade or stand aside |
| Normal / median | ~40-50 bps | Base-case carry-and-hedge book |
| Wide / attractive (entry zone) | > 60 bps | Add, *if* funding and convexity-hedge capacity exist |
| Stress / dislocation (1998, 2008, Mar 2020, Oct 2022) | 85-150+ bps | Generational entry for the capitalized; forced exit for the levered |

The cruel asymmetry of the trade: OAS is widest exactly when financing is scarcest and convexity hedging is most expensive, so the best entry points coincide with the moments levered holders are being forced out. Surviving to deploy at the wide is the entire game. Values are indicative of historical regimes, not live quotes (2022 figures verified — see Sources).

### Why negative convexity is the whole story

A normal bond *gains* duration-adjusted value symmetrically as rates move. An MBS does the opposite because the homeowner's [[prepayment-risk|prepayment option]] is short to the holder:

- **Rates fall →** homeowners refinance → principal returns early → the bond shortens precisely when the holder wanted to be long duration. Upside is capped near par (the call strike).
- **Rates rise →** refis dry up → the bond extends precisely when the holder wanted to be short duration. Downside extends.

So the position is *short an option straddle on rates*. Every large move, in either direction, costs the delta-hedger money on the rehedge (you systematically buy duration high and sell it low). The OAS is the premium collected for writing that straddle; [[negative-convexity]] is what you pay out in any volatile regime. This is why the trade's true risk is **realized rate volatility**, not the level or direction of rates.

## Performance Characteristics

- **Long-run Sharpe**: 0.5-0.9 for well-capitalized players; higher for those with better models.
- **Drawdowns**: 20-40% in regime shifts (1998, 2008, 2013 taper tantrum, 2022 hiking cycle).
- **Tail risk**: "negative convexity convexity" — losses in big moves are worse than linear in the underlying rate move.
- **Capacity**: $5-10B per fund; market-wide trillions (MBS market is ~$8T).

## Capacity Limits

Agency MBS market is ~$8-9T outstanding. Daily TBA volumes exceed $200B. Capacity is enormous but so is competition — every major bank, REIT, and macro fund plays in this space. Execution alpha and financing cost dominate rather than position-size limits.

## What Kills This Strategy

1. **Large unexpected rate moves** — big rallies trigger refi waves that shorten duration faster than hedges can adjust; big sell-offs extend duration into losses. 1994, 2003, 2013, 2022 are the canonical shocks.
2. **Prepayment model failure** — a new refi technology (e.g., streamlined HARP in 2012) invalidates historical prepay models overnight.
3. **Repo financing disruption** — as in 1998 and March 2020.
4. **Policy regime change** — Fed MBS purchases (2009, 2020) or unwind (QT from 2022) shift OAS by dozens of bps without warning.
5. **Forced unwind by a big holder** — Orange County, LTCM, mREITs in 2013/2022.
6. **Correlated RV book** — in stress, MBS basis widens with [[on-off-the-run-treasury-arbitrage|OTR/OFR]], [[swap-spread-arbitrage|swap spreads]], and [[tips-treasury-arbitrage|TIPS basis]].

See [[failure-modes]].

## Kill Criteria

- OAS widens >40 bps against entry within 60 days.
- Repo haircut raised above 5% on agency MBS (normal 2-3%).
- Rolling 12-month strategy return < -20%.
- Fundamental prepayment model validation fails out-of-sample.
- Position size × mortgage DV01 exceeds 35% of equity on stressed scenario.

## Advantages

- **Deepest liquid spread product** in the world — $8T market, massive daily volume.
- **Government-guaranteed credit** (agency MBS) — no default risk at the bond level.
- **Carry component**: even without OAS convergence, holders earn the spread.
- **Well-developed hedging tools**: TBA market, swaps, futures, swaptions.
- **Rich analytical space**: modeling edge is real and persistent for disciplined shops.

## Disadvantages

- **Negative convexity**: the defining risk. Every surprise move costs money on the hedge.
- **Model risk**: prepayment models are wrong in the third decimal in normal times and wildly wrong during regime shifts.
- **Daily rehedging cost**: transaction costs drag on realized returns vs modeled returns.
- **Balance-sheet-intensive**: all fixed-income RV is capital-intensive.
- **Policy-sensitive**: Fed policy dominates OAS behavior post-2009.
- **Correlated with other fixed-income RV** in crises — diversification illusion.
- **Complex infrastructure**: pool-level analytics, TBA operations, pool allocation — a whole back-office stack.

## Sources

- [[liars-poker]] — Michael Lewis's narrative of Salomon Brothers' mortgage desk; the origin story of the trade
- [[salomon-brothers]] — where MBS arb was invented
- [[ltcm-collapse-1998]] — canonical case study of levered MBS basis in stress
- MacKenzie (2003), *Long-Term Capital Management and the Sociology of Arbitrage*
- Roger Lowenstein, *When Genius Failed* (2000)
- Gabaix, Krishnamurthy & Vigneron (2007), *Limits of Arbitrage: Theory and Evidence from the Mortgage-Backed Securities Market*, Journal of Finance
- [[financial-crisis-2008]] — MBS spreads widened 300+ bps
- Boyarchenko, Fuster & Lucca (2019), *Understanding Mortgage Spreads*
- Verified via Perplexity (sonar), 2026-06-10 — 2022 mREIT book-value declines (AGNC/NLY ~25-30%, ARR ~30-35%) and agency MBS spread widening of 100-150 bps by October 2022. Citation: https://www.sec.gov/Archives/edgar/data/1423689/000142368923000017/agnc-20221231.htm

## Related

- [[option-adjusted-spread]] — the measured quantity
- [[negative-convexity]] — the defining risk
- [[prepayment-risk]] — the driver of negative convexity
- [[tba-market]] — the liquid trading venue
- [[salomon-brothers]] — the pioneer
- [[liars-poker]] — the famous book
- [[ltcm-collapse-1998]] — the famous failure
- [[on-off-the-run-treasury-arbitrage]] — sister RV trade
- [[swap-spread-arbitrage]] — sister RV trade
- [[tips-treasury-arbitrage]] — sister RV trade
- [[covered-interest-arbitrage]] — sister balance-sheet-intensive RV trade
- [[convergence-arbitrage]] — the spread-convergence family this belongs to
- [[relative-value-arbitrage]] — umbrella category
- [[limits-to-arbitrage]] — why the OAS premium persists
- [[quantitative-easing]] — the Fed's thumb on the scale
- [[taper-tantrum]] — 2013 MBS basis event
- [[edge-taxonomy]]
- [[failure-modes]]
