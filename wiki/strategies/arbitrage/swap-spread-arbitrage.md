---
title: "Swap Spread Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-07-19
status: excellent
tags: [arbitrage, bonds, treasuries, derivatives, history]
aliases: ["Swap Spread Trade", "IRS-Treasury Basis", "Negative Swap Spread Trade"]
strategy_type: quantitative
timeframe: position
markets: [bonds, treasuries]
complexity: advanced
backtest_status: paused
edge_source: [structural, risk-bearing]
edge_mechanism: "Interest-rate swap rates should trade above Treasury yields of the same maturity to compensate for bank credit risk; when the spread dislocates, an arb receives or pays fixed swap and hedges with the Treasury."
data_required: [swap-curve-intraday, treasury-yield-curve, repo-rates, sofr-fixings]
min_capital_usd: 10000000
capacity_usd: 5000000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.35
breakeven_cost_bps: 1
decay_evidence: "Swap spreads went persistently negative after 2008 bank-balance-sheet regulation (SLR, Basel III); textbook arbitrage broke"
related: ["[[ltcm-collapse-1998]]", "[[interest-rate-swap]]", "[[on-off-the-run-treasury-arbitrage]]", "[[relative-value-arbitrage]]", "[[tips-treasury-arbitrage]]", "[[sofr]]", "[[libor]]", "[[basel-iii]]", "[[supplementary-leverage-ratio]]", "[[failure-modes]]", "[[edge-taxonomy]]"]
---

# Swap Spread Arbitrage

Swap spread arbitrage trades the **swap spread** ([[swap-spread]]) — the difference between the fixed leg of a plain-vanilla [[interest-rate-swap]] and the yield on a Treasury of the same maturity. It is one of the canonical fixed-income [[relative-value-arbitrage|relative-value]] (RV) trades, sitting alongside [[on-off-the-run-treasury-arbitrage|on/off-the-run]] and [[tips-treasury-arbitrage|TIPS-Treasury]] basis. Classical theory held that the swap rate should exceed the Treasury yield by a small positive amount (5-50 bps), reflecting bank credit risk embedded in the old LIBOR-based swap curve. When the spread strayed far from fair value, an arbitrageur would **receive fixed on the swap** and **short the Treasury** (or vice versa), financing the Treasury leg in repo. Post-2008 regulation shattered the textbook: swap spreads at 10Y and 30Y tenors went **persistently negative**, a mathematical embarrassment that has never fully re-inverted — the single cleanest case study in the [[limits-to-arbitrage]] literature.

### Definition and sign convention

> **Swap spread (tenor T) = par swap rate(T) − Treasury yield(T)**, in basis points.
>
> Positive → swap rate above Treasury (classical, pre-2008). Negative → swap rate below Treasury (post-2008 regime, especially long end).

| Tenor | Classical (pre-2008) typical | Modern (post-2008) regime |
|-------|------------------------------|---------------------------|
| 2Y | small positive | near zero / slightly positive |
| 5Y | ~+30-50 bps | near zero / mildly negative |
| 10Y | ~+45 bps median, +30-60 bps range | persistently mildly negative |
| 30Y | positive | deeply negative (≈ -70 to -90 bps late 2025/early 2026, per Sources) |

## Edge Source

**Structural** (intended) and **risk-bearing** (actual). The classical trade was structural — an arb on the relationship between unsecured bank-credit rates and risk-free government rates. Post-2008 the residual edge is risk-bearing: the arbitrageur is paid to warehouse balance-sheet-constrained positions that banks can no longer hold. See [[edge-taxonomy]].

## Why This Edge Exists

Before 2008, the model was clean:
- **Swap rate** = expected path of LIBOR + credit premium for bank counterparty risk.
- **Treasury yield** = the risk-free rate (nearly).
- Swap rate > Treasury yield → positive swap spread of 30-60 bps at the 10Y tenor.

After 2008 three things broke this:

1. **Dealer balance-sheet cost** — the [[supplementary-leverage-ratio]] and [[basel-iii]] capital rules made it expensive for banks to hold Treasuries. Dealer fixed-income market-making inventories shrank by well over half between 2007 and 2015.
2. **Pension and insurance receive-fixed demand** — long-duration liabilities drove massive receive-fixed flows in the 30Y swap, pushing swap rates *below* Treasury yields.
3. **Treasury supply glut** — ballooning US deficits pushed Treasury yields *up*, not down. With nobody to arb the trade (balance sheet scarce), the negative spread persisted.

The counterparty is now structural: **liability-driven pension funds** receive fixed, **the US Treasury** issues bonds, and **bank dealers** cannot arb the two together. The arbitrageur is paid to rent balance sheet to the system. This is a classic example of a post-GFC [[limits-to-arbitrage]].

## Null Hypothesis

Under a world with abundant dealer balance sheet, no credit risk, and no regulatory frictions, the swap spread should equal the expected excess of LIBOR/SOFR over a repo-financed Treasury. Empirically that's a small positive number (~5-15 bps). Any persistent deviation — especially persistent negativity — is direct evidence of [[limits-to-arbitrage]] binding.

## Rules

### Direction cheat-sheet

| Regime | Signal | Swap leg | Treasury leg | Profits if | Carry |
|--------|--------|----------|--------------|-----------|-------|
| Classical | Spread too **wide** (>~60 bps) | Receive fixed | Short (reverse-repo borrow) | Spread **narrows** | Mixed |
| Modern | Spread deeply **negative** | Pay fixed | Long (term-repo financed) | Spread **normalizes toward 0** | Positive (Treasury yield > swap rate) |

In both cases the position is built DV01-neutral, so it has no outright duration view — only a view on the *spread*.

### Entry (Classical, Pre-2008)
1. Monitor the 10Y swap spread. Enter when it exceeds ~60 bps (above historical median of 45 bps).
2. **Receive fixed on the swap, short the Treasury** (profits if the spread narrows: swap rate falls relative to Treasury yield).
3. Borrow the Treasury via reverse repo to deliver the short; pay floating on nothing — the swap's floating leg is received against the repo earned on short-sale proceeds.
4. DV01-neutral hedge between swap and Treasury.

### Entry (Modern, Post-2008, Negative Spreads)
1. When the swap spread is deeply negative (e.g. 30Y below -60 bps outright, or more than 30 bps below its own trailing 5Y median), **pay fixed on the swap, buy the Treasury** — this locks in the Treasury yield over the swap rate as positive carry and profits if the spread normalizes toward zero.
2. Finance the Treasury in term repo; the floating leg received on the (SOFR-based) swap approximately offsets the repo cost.
3. Accept that the trade may **never converge** — size for carry, not convergence.

### Exit
1. Classical: spread returns to 40-50 bps → take profit.
2. Modern: spread normalizes toward zero, or financing terms deteriorate, or position size exceeds prime broker haircut capacity.

### Position Sizing
The trade must be financed; DV01 of swap and Treasury legs can both run into six figures per $100M notional. Size so that a 30 bp adverse spread move (2008 scale) does not exceed 20% of equity. [[ltcm-collapse-1998|LTCM]] had swap spread positions that lost hundreds of millions in 1998.

## Implementation Pseudocode

```python
def swap_spread_trade(tenor_years, mode="modern"):
    swap_rate = get_par_swap_rate(tenor_years)
    tsy_yield = get_treasury_yield(tenor_years, on_the_run=False)
    spread_bps = (swap_rate - tsy_yield) * 1e4

    if mode == "classical" and spread_bps > 60:
        # spread too wide: bet on narrowing
        return Trade(receive_fixed_swap=True, short_treasury=True,
                     notional=size_to_dv01(tenor_years))
    if mode == "modern" and spread_bps < trailing_median(spread_bps, years=5) - 30:
        # spread deeply negative: lock in positive carry, bet on normalization
        return Trade(pay_fixed_swap=True, buy_treasury_repo_financed=True,
                     notional=size_to_dv01(tenor_years),
                     warning="may not converge; size for carry")
    return None
```

## Indicators / Data Used

- Par swap curve at standard tenors (2Y, 5Y, 10Y, 30Y) — SOFR-based post-2021
- [[treasury-yield-curve]] for off-the-run comparables
- **Repo-GC spread** and term repo rates
- [[sofr]] fixings and realized vs expected path
- Bank CDS and credit spreads (relevant for the old LIBOR-based curve)
- SLR-constrained dealer balance sheet capacity (proxied by primary-dealer Treasury holdings from NY Fed H.4.1)

## Example trade

> Illustrative, round numbers — not a backtest. Applies the modern (post-2008, negative-spread) rules from this page.

**Setup:** The 10Y SOFR swap spread is reading **−18 bps** (swap rate 2.82%, 10Y Treasury yield 3.00%). This is 23 bps below the trailing 5-year median of +5 bps — well past the "deeply negative" entry threshold from the Rules section. A hedge fund with prime-broker repo access enters the trade.

**Position (DV01-neutral, $100M notional):**

| Leg | Action | Rate/Yield | Notional |
|-----|--------|-----------|---------|
| Buy 10Y Treasury (off-the-run) | Long | 3.00% yield | $100M |
| Finance Treasury in term repo (3-month) | Borrow | SOFR + 8 bps ≈ 2.88% | $100M |
| Pay fixed on 10Y SOFR IRS | Pay fixed | 2.82% | $100M |
| Receive floating (SOFR) on IRS | Receive | SOFR ≈ 2.80% | $100M |

**Net daily carry (all four legs):**

| Leg | Daily cash flow (approx) |
|-----|--------------------------|
| Treasury coupon income | +$8,219/day (3.00% × $100M / 365) |
| Repo cost | −$7,890/day (2.88% × $100M / 365) |
| Pay fixed on swap | −$7,726/day (2.82% × $100M / 365) |
| Receive SOFR on swap | +$7,671/day (2.80% × $100M / 365) |
| **Net carry** | **+$274/day ≈ +$100k/year** |

This is approximately **+10 bps net per annum** on $100M notional, earned as long as the spread stays negative and repo-SOFR basis remains benign.

**Exit scenario (12 months later):** The spread normalises to −5 bps (swap rate 2.95%, Treasury yield 3.00%). The position is unwound:

| Item | P&L |
|------|-----|
| DV01 on 10Y ≈ $9,000 per bp; spread moved +13 bps | +$117,000 |
| 12 months carry (+$100k) | +$100,000 |
| Financing spread stress (repo-SOFR briefly widened +5 bps for 30 days) | −$4,100 |
| Transaction costs (bid-ask on Treasury + swap, ~0.5 bps × 2) | −$10,000 |
| **Net P&L** | **+$202,900** |

Return on equity: the fund's prime broker required ~$5M haircut to repo $100M of 10Y Treasury, so equity deployed ≈ $5M. Net return ≈ 4.1% on deployed equity — modest, but highly repeatable and uncorrelated to directional markets.

**Risk scenario:** If the spread instead widens a further 30 bps (to −48 bps), the DV01 loss is $9,000 × 30 = −$270,000, exceeding one year of carry. At that point the kill criterion (>30 bps adverse move within 6 months) fires and the position is closed for a loss. This is the LTCM scenario in reverse: the trade is right in fair-value terms but wrong in timing, and financing must survive the drawdown.

## Worked Example: The 2015 Negative Swap Spread

The numbers below are real market levels used to illustrate the carry mechanics; they are not a backtested P&L series.

In October 2015 the 10Y swap spread traded at approximately **-12 bps** — the 10Y swap fixed rate at 2.12% while the 10Y Treasury yielded 2.24%. In textbook terms this was impossible. A bank could buy the Treasury financed in repo, pay fixed on the swap, receive LIBOR against the repo cost, and lock in roughly 12 bps per year for ten years.

Why didn't they? **Leverage ratio**. Holding $100M of 10Y Treasury carries a leverage-ratio capital charge of ~$5M for a SIFI. The 12 bps return on $100M = $120K/year = 2.4% ROE on the capital consumed. Not worth doing.

A hedge fund with cheaper balance sheet (no SLR) could enter:
- **Pay fixed** on $100M 10Y swap at 2.12% (receive 3M LIBOR — this was pre-SOFR)
- **Buy** $100M 10Y Treasury at 2.24%, financed in term repo
- The LIBOR received approximately covers the repo paid (LIBOR then traded above GC repo, adding a few bps)
- Net carry: approximately +12 bps = $120K/yr per $100M, with the position roughly DV01-neutral.

The trade *was* put on at scale by a handful of hedge funds. It has not fully converged as of 2026 — long-end spreads have in fact deepened: the 30Y SOFR swap spread sits around **-70 to -90 bps** as of late 2025/early 2026.

## Performance Characteristics

- **Classical (pre-2008)**: Sharpe 1.0-1.5 over full cycles; occasional severe drawdowns around 1998 ([[ltcm-collapse-1998]]) and 2007.
- **Modern (post-2008)**: Sharpe 0.5-0.8 for well-financed funds; dominated by carry rather than convergence.
- **2008 stress**: 30Y spread moved from +50 bps to -20 bps in a matter of months — a ~70 bp adverse move for anyone long the spread (pay-fixed swap + long Treasury). Conversely, in 1998 spreads *widened* violently, ruining positions short the spread ([[ltcm-collapse-1998|LTCM]]'s receive-fixed/short-Treasury convergence book).
- **Capacity**: $2-5B gross per fund before repo haircut and dealer balance-sheet capacity constrain further scaling.

> The Sharpe figures above describe the *historical behavior of the trade across regimes*, not a backtest of this page's specific rules. The modern trade's expectancy is dominated by **carry**, not convergence — getting fair value right does not guarantee a timely payoff.

### Where the carry comes from / goes (modern trade)

| Leg | Cash flow | Sign |
|-----|-----------|------|
| Long Treasury | + Treasury coupon/yield | + |
| Term repo to finance Treasury | − repo rate | − |
| Pay-fixed swap | − swap fixed rate | − |
| Receive floating ([[sofr]]) on swap | + SOFR | + |
| **Net** | ≈ (Treasury yield − swap rate) ± (SOFR − repo) | **positive when spread is negative and financing is benign** |

The killer is the financing basis: a repo spike (Sept 2019, March 2020) widens `repo − SOFR`, turning the carry against the position and forcing levered unwinds precisely when haircuts rise.

## Capacity Limits

The trade is almost entirely balance-sheet-capacity-constrained rather than market-impact-constrained. A pod running $5B 10Y DV01 can enter without moving the market, but financing that position requires a dedicated prime broker relationship and tens of millions in repo haircut.

## What Kills This Strategy

1. **Repo financing disruption** — e.g., September 2019 SOFR spike forced unwinds of leveraged Treasury positions.
2. **Regulatory loosening** — SLR relief (granted temporarily in 2020-21; reform formally proposed by the Fed in mid-2025) would let dealers pile in and collapse the spread toward zero. That is a windfall for funds already long Treasury / pay-fixed at deep-negative spreads, but ruinous for anyone positioned the other way, and it would permanently shrink the opportunity set.
3. **Credit event at a major swap counterparty** — re-widens spreads dramatically.
4. **Prime broker haircut hikes** — forced unwinds at adverse spreads. See [[ltcm-collapse-1998]].
5. **Convergence trade reversals** — the spread can trend further from fair value for *years*. Being right on fair value is not the same as being right on timing.

See [[failure-modes]].

## Kill Criteria

- Spread moves >30 bps further from entry within any 6-month window.
- Financing cost (repo haircut + borrow fee) exceeds 60% of expected carry.
- Rolling 12-month return < -15% at the trade level.
- Regulatory shift signals imminent balance-sheet-capacity repricing.

## Advantages

- **Deep market** — global IRS market exceeds $400T notional; Treasury market is the deepest in the world.
- **Quantifiable edge** — the swap spread is directly observable and historically mean-reverting across cycles.
- **DV01-neutral** — no directional rate risk once hedged.
- **Carry component** persists even without convergence.

## Disadvantages

- **Capital-intensive** — requires prime broker balance sheet, ISDA, repo lines.
- **Regulatory dependence** — the post-2008 structure of the spread is a regulatory artifact; rule changes swing P&L by tens of bps overnight.
- **Convergence is not guaranteed** — the spread has been "wrong" in the negative-spread sense for over 15 years.
- **Correlation with other RV trades** — in stress, [[on-off-the-run-treasury-arbitrage|on/off-the-run]], swap spread, and [[mbs-basis-arbitrage|MBS basis]] all widen together.
- **Rolling financing risk** — repo is typically overnight-to-quarterly; a 10Y trade requires many rolls.

## Sources

- [[ltcm-collapse-1998]] — had large swap spread positions that contributed to the fund's losses
- Duffie (2018), *Post-Crisis Bank Regulations and Financial Market Liquidity* — explains the structural persistence of negative swap spreads
- Boyarchenko, Gupta, Steele, Yen (NY Fed, 2018), *Negative Swap Spreads*
- Jermann (2020), *Negative Swap Spreads and Limits to Arbitrage*, Journal of Finance
- Roger Lowenstein, *When Genius Failed* — LTCM's swap spread book
- Verified via Perplexity (sonar), 2026-06-10: 30Y SOFR swap spread approximately -70 to -90 bps as of late 2025/early 2026 (vs 30Y Treasury ~5.0%); Oct 2015 10Y swap spread negative in the -10 to -18 bps range confirmed.

## Related

- [[swap-spread]] — the spread being traded
- [[arbitrage]] — umbrella concept
- [[interest-rate-swap]] — the instrument itself
- [[on-off-the-run-treasury-arbitrage]] — sister RV trade
- [[tips-treasury-arbitrage]] — another fixed-income RV trade
- [[mbs-basis-arbitrage]] — another fixed-income RV trade
- [[relative-value-arbitrage]] — umbrella category
- [[ltcm-collapse-1998]] — classic failure case
- [[sofr]] — modern floating-rate benchmark
- [[libor]] — legacy floating-rate benchmark
- [[basel-iii]] and [[supplementary-leverage-ratio]] — regulatory constraints driving post-2008 regime
- [[limits-to-arbitrage]] — theoretical framework
- [[edge-taxonomy]]
- [[failure-modes]]
