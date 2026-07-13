---
title: "TIPS-Treasury Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, bonds, treasuries, quantitative, history]
aliases: ["TIPS Arb", "Breakeven Inflation Arb", "Real vs Nominal Trade", "Inflation Swap Arbitrage"]
strategy_type: quantitative
timeframe: position
markets: [bonds, treasuries]
complexity: advanced
backtest_status: pilot
edge_source: [structural, risk-bearing, behavioral]
edge_mechanism: "TIPS breakeven (nominal yield minus TIPS yield) should equal inflation swap rate; when they dislocate due to TIPS liquidity or forced selling, arbitrage the gap by combining TIPS, nominal Treasury, and inflation swap."
data_required: [tips-yields, nominal-yields, inflation-swaps, cpi-data, repo-rates]
min_capital_usd: 10000000
capacity_usd: 3000000000
crowding_risk: medium
expected_sharpe: 0.8
expected_max_drawdown: 0.30
breakeven_cost_bps: 3
decay_evidence: "2008 GFC produced >100 bp TIPS-inflation-swap dislocation; converged over 18 months"
related: ["[[ltcm-collapse-1998]]", "[[on-off-the-run-treasury-arbitrage]]", "[[swap-spread-arbitrage]]", "[[relative-value-arbitrage]]", "[[inflation-swap]]", "[[breakeven-inflation]]", "[[financial-crisis-2008]]", "[[cpi]]", "[[limits-to-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
---

# TIPS-Treasury Arbitrage

TIPS-Treasury arbitrage exploits mispricings between **Treasury Inflation-Protected Securities ([[tips|TIPS]])** and **nominal Treasury** bonds of the same maturity, usually combined with an [[inflation-swap]] to synthesize a risk-free package. In theory, a nominal Treasury equals a TIPS plus an [[inflation-swap]] paying realized CPI. When these three instruments dislocate — as they did catastrophically in late 2008 — the arbitrage is one of the cleanest in fixed income: buy the cheap synthetic, sell the rich, pocket the spread over the remaining maturity. It is the canonical fixed-income example of [[convergence-arbitrage]] and of how the [[limits-to-arbitrage]] can turn a "risk-free" trade into a fund-killer at exactly the wrong moment.

### The three-legged identity

| Instrument | Pays | Role in the package |
|------------|------|---------------------|
| Nominal Treasury | Fixed nominal coupon + par | The "rich/cheap" reference leg |
| [[tips|TIPS]] | Real coupon + CPI-indexed principal | Real-yield leg of the synthetic |
| Zero-coupon [[inflation-swap]] | Fixed vs realized CPI | Converts the TIPS into a synthetic nominal |

**TIPS + receive-fixed inflation swap = synthetic nominal Treasury.** If the synthetic yields more than the actual nominal, the actual nominal is rich: long the synthetic, short the nominal. At maturity the package converges by construction (the only residual risk is inflation-swap counterparty credit and CPI-methodology change). This is what makes the trade *look* free — and what makes its 2008 blow-up so instructive.

## Edge Source

**Structural** (primary), **risk-bearing** (secondary), **behavioral** (during panics). The mispricing is a textbook example of [[limits-to-arbitrage]] binding during stress. TIPS are structurally less liquid than nominal Treasuries and become punishingly illiquid in crises, while inflation swaps (over-the-counter, bank balance sheet) become hard to price. See [[edge-taxonomy]].

| Edge component | Category | Source | Counterparty |
|----------------|----------|--------|--------------|
| TIPS liquidity premium | Structural | ~$2T TIPS vs ~$28T nominal market; wider bid-ask | Investors paying up for nominal-Treasury liquidity |
| Crisis dislocation | Risk-bearing | Spread blows out when balance sheet is scarcest | The arbitrageur willing to warehouse the basis through stress |
| Forced-deleveraging overshoot | Behavioral | Levered holders dump TIPS regardless of fair value | Panicked levered seller (a 2008 hedge fund) |
| Maturity convergence | Structural | Package is mathematically pinned at maturity | Time itself, modulo swap counterparty credit |

The defining feature is that the edge is *largest exactly when it is hardest to hold* — the hallmark of a risk-bearing, [[limits-to-arbitrage]]-driven trade rather than a free lunch.

## Why This Edge Exists

**Fisher identity**: Nominal Treasury yield ≈ TIPS real yield + expected inflation + inflation risk premium.

By buying a TIPS and receiving fixed on an inflation swap (paying CPI), you synthesize a **nominal bond**. The synthetic and actual nominal should yield within a few bps. In practice, three forces drive them apart:

1. **TIPS liquidity premium** — TIPS market is ~$2T vs ~$28T nominal Treasury market; TIPS bid-ask is 5-15x wider. TIPS trade at a liquidity discount (higher real yields) that widens in stress.
2. **CPI seasonality and reporting lag** — TIPS principal accretes with a roughly three-month CPI indexation lag (interpolated). Inflation swaps reference CPI with a similar lag. Mismatches around large seasonal swings (gasoline, shelter) create short-term noise.
3. **Forced selling by levered holders** — hedge funds (notably in 2008) held TIPS long / nominal short on basis spread trades; when forced to deleverage, they dumped TIPS regardless of fair value. See [[lehman-brothers-bankruptcy]] and [[financial-crisis-2008]].

The counterparty during dislocations is a **panicked levered seller** — usually a hedge fund meeting redemptions or margin calls. In normal times, the counterparty is an insurance company or pension fund paying a liquidity premium for nominal-Treasury exposure.

## Null Hypothesis

Under frictionless markets, the spread between a nominal Treasury and a (TIPS + inflation swap) synthetic should be zero. Empirically it's 5-15 bps in normal conditions — the baseline TIPS liquidity premium. Any deviation beyond ~30 bps signals a dislocation worth trading.

## Rules

### Entry
1. Compute the **synthetic-nominal yield**: TIPS real yield + inflation swap fixed rate of matched tenor.
2. Compare to the actual matched-maturity nominal Treasury yield.
3. Enter when the spread exceeds ~30 bps — typically:
   - **Long TIPS + receive fixed inflation swap**
   - **Short nominal Treasury** (financed via repo)
4. DV01- and breakeven-neutral hedge ratios.
5. Require term repo financing long enough to survive a stress widening (at least 6 months).

### Exit
1. Spread narrows to ~10 bps or less → close.
2. Hold to maturity if necessary — the trade is guaranteed to converge at maturity modulo inflation-swap counterparty risk.
3. Roll inflation swap if needed to match Treasury duration.

### Position Sizing
Stress scenario: the 2008 dislocation widened the spread by **>200 bps briefly**. Size so a 150 bp adverse move does not bust the fund. Krishnamurthy (2010) documented that many funds that had the *correct* trade in 2008 were forced to liquidate into the dislocation.

## Implementation Pseudocode

```python
def tips_treasury_arb(tenor_years):
    tips_yield = get_tips_real_yield(tenor_years)
    infl_swap = get_zc_inflation_swap(tenor_years)
    synth_nominal = tips_yield + infl_swap

    actual_nominal = get_nominal_treasury_yield(tenor_years, on_the_run=False)
    spread_bps = (actual_nominal - synth_nominal) * 1e4

    if spread_bps > 30:
        # synthetic is cheap; nominal is rich
        return Trade(
            long_tips=True,
            receive_inflation_swap=True,
            short_nominal=True,
            hedge="dv01_and_breakeven_neutral",
            financing="term_repo_6m_minimum",
        )
    if spread_bps < -30:
        # synthetic is rich; nominal is cheap
        return Trade(
            short_tips=True,
            pay_inflation_swap=True,
            long_nominal=True,
        )
    return None
```

## Indicators / Data Used

- [[tips]] yields at standard maturities (5Y, 10Y, 30Y)
- [[treasury-yield-curve]] nominal yields
- Zero-coupon [[inflation-swap]] curve
- [[breakeven-inflation]] curve derived from TIPS and nominals
- [[cpi]] release calendar and historical seasonality
- Repo rates (general collateral and TIPS-specific special repo)
- TIPS bid-ask spreads as a liquidity indicator

## Example Trade: The 2008 TIPS Dislocation

In October-November 2008, after the [[lehman-brothers-bankruptcy|Lehman bankruptcy]], TIPS yields *rose* violently while nominal Treasury yields *fell* — the opposite of the textbook response to a deflation scare. The 10Y breakeven inflation rate collapsed from ~2.4% in mid-2008 to approximately zero by late November 2008, and the 5Y breakeven went outright negative (roughly -2% at the trough) — the cash TIPS market was pricing in years of deflation.

Meanwhile, the 10Y inflation swap still quoted positive inflation (~1.2%) because swap dealers priced from the Fed's expected response, not panicked cash-bond flows. The synthetic-vs-nominal spread blew out to **~150 bps** at some tenors.

Trade construction (example, 10Y):
- **Long** $100M face 10Y TIPS at real yield 3.00%.
- **Receive fixed** 10Y zero-coupon inflation swap at 1.20%.
- **Short** $100M face 10Y nominal Treasury at yield 3.20%.
- Synthetic nominal yield: 3.00% + 1.20% = **4.20%** vs actual 3.20% → **100 bps pickup**.

Over the following 18 months, as TIPS liquidity returned, the spread compressed to ~10 bps. A patient holder earned approximately **~90 bps × DV01 × notional × leverage** — for a well-financed fund at 10x leverage, several percent at the fund level.

**The catch**: anyone who put on this trade *before* October 2008 (at, say, 30 bps) was staring at 150 bp adverse move by November. Many were margined out at the worst possible point. Krishnamurthy (2010) and Fleckenstein, Longstaff & Lustig (2014) formalized the opportunity in hindsight.

## Performance Characteristics

> **No fabricated backtest.** The ranges below are qualitative descriptions of how the trade behaves across regimes and figures attributed to the academic literature (Fleckenstein, Longstaff & Lustig 2014; Krishnamurthy 2010) — not a verified return series produced here. The "50-100%" figure is a reported, post-hoc characterisation of funds that deployed *after* the 2008 peak, not a guaranteed outcome.

The trade has two completely different return profiles depending on regime:

| Regime | Spread behaviour | Return character | Dominant risk |
|--------|------------------|------------------|---------------|
| Normal | 5-20 bp oscillation (the baseline liquidity premium) | Modest carry; Sharpe modest with careful sizing | Mark-to-market noise from CPI lag/seasonality |
| Dislocation onset (e.g. Oct-Nov 2008) | Blows out to 100-200+ bp | Large *adverse* mark-to-market for early entrants | Forced liquidation into the widening |
| Post-peak convergence (2009-2010, mid-2020) | Compresses back toward baseline | The exceptional, lumpy returns the literature documents | Needing to have *survived* the onset with capital intact |

- **Cost sensitivity**: `breakeven_cost_bps: 3` (frontmatter) — this is a tiny-edge, high-balance-sheet trade; inflation-swap bid-ask normally ~3 bps and TIPS repo specialness can erode carry quickly.
- **Capacity**: $1-3B gross per fund before TIPS market impact; market-wide perhaps $30-50B of basis can trade without moving breakevens.
- **The asymmetry that matters**: the same dislocation that creates the opportunity is what margins out the people who held the trade before it. Krishnamurthy (2010) documented that many funds with the *correct* trade in 2008 were forced to liquidate into the dislocation.

## Capacity Limits

TIPS market is only ~$2T face outstanding vs $28T nominal Treasuries. The full market only supports perhaps 5-8 large players running this trade. In 2008 Barclays estimated total hedge-fund TIPS-nominal basis positions at ~$100B; unwinds of 20-30% of that were enough to widen spreads by 100+ bps.

| Constraint | Magnitude | Why it binds |
|------------|-----------|--------------|
| TIPS float | ~$2T face | Small relative to the basis people want to run |
| Per-fund gross | $1-3B | Beyond this, your own footprint moves TIPS prices |
| Market-wide tradeable basis | ~$30-50B | Above this, breakevens move materially |
| Inflation-swap dealer capacity | bank balance sheet | OTC; capital charges widen bid-ask in stress |

The capacity is *negatively correlated with opportunity*: when the spread is widest (a balance-sheet-scarce crisis), dealer and prime-broker capacity is most constrained, so realisable capacity shrinks precisely when the gross edge is largest. This is the [[limits-to-arbitrage]] expressed as a capacity constraint.

## What Kills This Strategy

1. **Forced liquidation in stress** — the single worst scenario. The trade looks amazing exactly when you can't size it. See [[financial-crisis-2008]].
2. **Inflation swap counterparty default** — OTC inflation swaps require a swap counterparty; Lehman's OTC book was resolved painfully.
3. **CPI methodology changes** — if BLS changes CPI calculation (e.g., chained CPI for TIPS), cash flows on existing TIPS and swaps diverge.
4. **Repo financing pulled** — similar to [[on-off-the-run-treasury-arbitrage]] and [[swap-spread-arbitrage]] — all fixed-income RV trades share this exposure.
5. **Regulatory changes to bank inflation-swap books** — increased capital charges on inflation derivatives widen bid-ask and break the hedge.

See [[failure-modes]].

## Kill Criteria

- Spread widens by >80 bps against entry within 90 days **and** financing terms tighten.
- Inflation swap bid-ask exceeds 15 bps (normal ~3 bps) — can't unwind cleanly.
- Prime broker raises TIPS haircut above 10%.
- Strategy rolling 12-month return < -15%.

## Advantages

- **Maturity-convergent**: if held to maturity, the trade is mathematically guaranteed to converge (modulo swap counterparty credit).
- **Dislocation-driven**: the biggest returns come from rare but well-defined events.
- **Real economic hedge**: the arb book is partially inflation-neutral, a useful diversifier against macro-exposed portfolios.
- **Clean edge identification**: the mispricing is publicly quoted and easy to measure.

## Disadvantages

- **Severe liquidity risk**: TIPS illiquidity is the enemy of a levered arbitrageur.
- **Swap counterparty risk**: inflation swaps are OTC, bilateral; CSA terms matter enormously.
- **CPI lag and seasonality**: short-term mark-to-market noise can mask fundamental convergence.
- **Opportunities are rare**: large dislocations happen every ~5-10 years; carry-only returns are modest.
- **Balance sheet intensive**: three instruments (TIPS, Treasury, swap) times DV01 hedging consumes significant capital.
- **Correlated with other fixed-income RV**: in 2008, [[on-off-the-run-treasury-arbitrage|OTR/OFR]], [[swap-spread-arbitrage|swap spreads]], [[mbs-basis-arbitrage|MBS basis]], and TIPS basis all widened simultaneously.

## Sources

- Fleckenstein, Longstaff & Lustig (2014), *The TIPS-Treasury Bond Puzzle*, Journal of Finance — seminal paper documenting the mispricing
- Krishnamurthy (2010), *How Debt Markets Have Malfunctioned in the Crisis*, JEP
- D'Amico, Kim & Wei (2018), *Tips from TIPS* — Fed research on TIPS liquidity
- [[financial-crisis-2008]] — context for the canonical dislocation
- [[ltcm-collapse-1998]] — earlier fixed-income RV blow-up (pre-TIPS-market existence)

## Related

- [[arbitrage]] — parent concept
- [[convergence-arbitrage]] — the general family (model fair value pins at maturity)
- [[tips]] — the instrument
- [[inflation-swap]] — the hedge instrument
- [[breakeven-inflation]] — the derived quantity
- [[on-off-the-run-treasury-arbitrage]] — sister RV trade
- [[swap-spread-arbitrage]] — sister RV trade
- [[mbs-basis-arbitrage]] — sister RV trade
- [[relative-value-arbitrage]] — umbrella category
- [[cpi]] — the reference inflation index
- [[financial-crisis-2008]] — context for the 2008 dislocation
- [[ltcm-collapse-1998]] — the prototype of a "risk-free" RV trade margined out in a crisis
- [[limits-to-arbitrage]] — theoretical framework
- [[edge-taxonomy]]
- [[failure-modes]]
