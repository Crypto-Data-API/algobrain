---
title: "CDS-Bond Basis Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, bonds, derivatives, quantitative]
aliases: ["Negative Basis Trade", "CDS Basis Trade", "Bond-CDS Basis"]
strategy_type: quantitative
timeframe: position
markets: [bonds, derivatives]
complexity: advanced
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "CDS and cash bond markets price the same credit risk but are intermediated by different dealers, funded differently, and held by different investors; the basis compensates the arbitrageur for funding, balance sheet, and liquidity risk -- not for credit risk."
data_required: [cds-quotes, bond-quotes, repo-rates, funding-spreads, treasury-curve]
min_capital_usd: 10000000
capacity_usd: 5000000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.5
breakeven_cost_bps: 15
related: ["[[credit-default-swap]]", "[[repo-market]]", "[[ltcm-collapse-1998]]", "[[fixed-income-arbitrage]]", "[[dealer-balance-sheet]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[arbitrage]]"]
---

# CDS-Bond Basis Arbitrage

CDS-Bond Basis Arbitrage trades the spread between a company's **cash bond spread** (yield over the matching Treasury or [[asset-swap-spread]]) and its **[[credit-default-swap|CDS]] spread** for the same maturity. In theory these should be equal because both instruments compensate for the same default risk. In practice a residual **basis** -- positive when CDS trades rich to bonds, negative when CDS trades cheap -- can be tens to hundreds of basis points. The classic **negative basis trade** buys the cash bond and buys CDS protection to "lock in" a riskless spread above Treasuries. It is a flagship [[fixed-income-arbitrage]] / [[convergence-arbitrage]] strategy and a sibling of capital-structure-arbitrage within [[relative-value-arbitrage]] — and its 2008 blowup is one of the most-studied cautionary tales of [[limits-to-arbitrage]].

At a glance:

| Attribute | Value |
|---|---|
| Definition | Basis = CDS spread − cash-bond [[z-spread]] (matched maturity) |
| Negative-basis trade | Long bond + buy [[credit-default-swap\|CDS]] protection (synthetic risk-free) |
| Positive-basis trade | Short bond + sell CDS protection (rarer, harder to fund) |
| Edge sources | [[edge-taxonomy\|Structural + risk-bearing]] |
| Funding | Cash bond financed in [[repo-market\|repo]]; CDS posts [[initial-margin]] |
| Canonical blowups | 2008 GFC (-250 to -600 bps), March 2020 COVID (-150 bps) |
| Key risk | Funding/margin spiral — basis can widen further while "cheap" |

### Sign convention and the two trades

| Basis sign | Meaning | The trade | Funding profile |
|---|---|---|---|
| **Negative** (CDS cheap vs bond) | Bond spread > CDS spread | **Buy bond + buy protection** → lock spread over Treasuries | Must fund bond in repo; vulnerable to haircut/funding shocks |
| **Positive** (CDS rich vs bond) | CDS spread > bond spread | Short bond + sell protection | Needs bond borrow; harder, less common |

The negative-basis trade is the workhorse because it is "long credit + hedged" and looks like a synthetic Treasury — which is exactly what made it dangerous in 2008 when the funding leg, not the credit leg, blew up.

## Edge Source

**Structural** and **risk-bearing** (see [[edge-taxonomy]]).

| Edge | Where it comes from | Who pays it |
|---|---|---|
| **Structural** | Segmented markets and dealer balance-sheet constraints: cash bonds fund via [[repo-market\|repo]], CDS posts [[initial-margin]], and the two clear through different plumbing. Basel III [[leverage-ratio]] charges capital on both legs even when economically hedged. | Dealers who won't arb their own balance sheet |
| **Risk-bearing** | The arbitrageur warehouses funding, counterparty, and liquidity risk the marginal buyer/seller won't hold. The basis is the *price of that warehousing service*, not credit risk. | Forced sellers and capital-constrained dealers |

Critically, the negative basis is **not** compensation for credit risk — the position is credit-hedged. It is compensation for funding and balance-sheet risk, which is why it explodes precisely when funding markets seize.

## Why This Edge Exists

- **Funding asymmetry.** A cash bond must be funded in repo; CDS is an unfunded derivative. If repo rates widen or haircuts increase, the cost of holding the cash bond rises without a symmetrical change in CDS, pushing the basis negative.
- **Dealer balance-sheet cost.** Under Basel III [[leverage-ratio]], dealers pay capital on both the cash bond and the offsetting CDS even when economically hedged. This reduces their willingness to arbitrage the basis themselves.
- **Cheapest-to-deliver option.** CDS contracts settle on any deliverable bond; if multiple bonds trade at different levels, CDS is priced to the cheapest, making CDS spread structurally lower than the specific bond's spread (the "CTD option" in the CDS).
- **Counterparty risk.** When buying CDS from a dealer, the buyer takes dealer credit risk -- during 2008, this risk was priced explicitly into a negative basis.
- **Who is on the other side?** Bond holders forced to sell (mutual funds in outflows, banks reducing RWAs), dealers reducing inventory, or insurance companies buying CDS for regulatory capital relief.

## Null Hypothesis

In frictionless markets the **no-arbitrage basis is zero**. Observed basis should be pure noise with zero expected return. Any systematic profit therefore compensates for (a) real frictions (funding, balance sheet, counterparty) or (b) temporary dislocations where the price-insensitive side is particularly active. A random-no-edge world: basis distribution is symmetric around zero, trades earn the bid-ask less funding.

## Rules

**Entry (negative basis).**
1. Screen IG and HY universe daily. Compute basis = CDS spread - Z-spread of cash bond (matching maturity).
2. Enter negative basis trade (buy bond + buy CDS) when basis < -30 bps for IG or < -100 bps for HY, and z-score of trailing-year basis < -2.
3. Verify bond is actually repo-able and that CDS is liquid (tier-1 reference entity, cleared via [[ice-clear-credit]]).
4. Fund the bond via term repo matching the holding horizon (avoid overnight funding roll risk, the lesson of 2008).

**Positioning.**
- Notional matched 1:1 between bond face value and CDS notional.
- Duration-hedge the Treasury component of bond yield using [[treasury-futures]] if isolating spread is the goal.
- Scale by z-score and liquidity score of each leg.

**Exit.** Close when basis mean-reverts to within -10 bps (or to historical mean), or at bond maturity, or if funding cost exceeds locked spread.

## Implementation Pseudocode

```python
for ticker, bond in universe:
    cds_5y = cds_mid(ticker, tenor=5)
    z_spread = z_spread_from_bond(bond)  # asset-swap spread equivalent
    basis = cds_5y - z_spread
    z = zscore(basis, window=252)
    funding_cost = repo_rate(bond) - ois_rate()  # bps
    net_carry = -basis - funding_cost  # for negative-basis trade
    if basis < -30 and z < -2 and net_carry > 15:
        buy_bond(bond, notional=N, funding="term_repo_3m")
        buy_cds_protection(ticker, notional=N, tenor=5)
    # Monitor daily; unwind on basis >= -10 or if repo rate spikes
```

## Indicators / Data Used

- CDS mid from ICE, Markit/IHS, dealer runs
- Bond quotes from TRACE, Bloomberg, MarketAxess
- Asset-swap spread or [[z-spread]] to Treasury curve
- Repo rates (general collateral + specials) and bond-specific haircuts
- [[ois-rate]] as funding benchmark
- [[libor-ois-spread]] historically (stress indicator)

## Example Trade

**2008-2009 negative basis blowout.** Pre-crisis, IG basis oscillated in a +5 to -10 bps range. During September-October 2008, as Lehman's collapse froze [[repo-market|repo markets]] and dealers dumped bond inventory, the basis on IG names blew out to **-250 to -400 bps** for liquid names and beyond -600 bps for some financials. A trader who bought $100 mm of IBM 5Y bonds at a basis of -300 bps, funded in repo, and bought IBM CDS locked in a ~3% annual carry over Treasuries until maturity.

However, **many funds that entered the trade in late 2008 were margin-called out of it in the following weeks** as the basis widened further (-400 to -600 bps), repo haircuts jumped from 2% to 10%+, and dealers demanded additional collateral. [[boaz-weinstein]] at Saba, Citadel, and others reportedly earned substantial profits by sizing the trade conservatively and holding to maturity, while over-leveraged basis funds liquidated at the worst possible moment. Academic work (Mitchell-Pulvino 2012, "Arbitrage Crashes and the Speed of Capital") shows the basis took **~15 months to fully mean-revert** -- a brutal duration for margin-financed capital.

The 2008 blowup is the canonical [[failure-modes|margin-spiral failure]] and the textbook illustration of [[limits-to-arbitrage]]: the trade was correct on convergence yet ruined leveraged holders on the path.

| Phase (2008-09) | IG basis (liquid names) | Repo haircut | What happened |
|---|---|---|---|
| Pre-crisis | +5 to -10 bps | ~2% | Basis is noise; small carry |
| Lehman week (Sep 2008) | -250 to -400 bps | rising | Dealers dump inventory; repo freezes |
| Peak stress (Oct-Nov 2008) | -400 to -600 bps (financials worse) | 10%+ | Margin calls force liquidation at the worst level |
| Recovery (through ~2010) | back toward -20 bps | normalizing | ~15 months to fully mean-revert |

**Lesson:** the position was *right* — the basis converged — but path risk (mark-to-market + funding) destroyed leveraged holders. Survivors used **term repo** matched to horizon, conservative sizing, and capital that could not be pulled. This is the single most important practical takeaway of the strategy.

**2020 COVID dislocation.** On 18 March 2020 the IG basis spiked to -150 bps before the [[federal-reserve|Fed]]'s Primary Market and Secondary Market Corporate Credit Facilities were announced. Funds that had capacity to add to the trade earned exceptional returns by June 2020 as basis compressed back to -20 bps.

## Performance Characteristics

> **Data disclaimer:** the figures below are drawn from academic literature (Duarte-Longstaff-Yu, Mitchell-Pulvino) and realistic order-of-magnitude estimates, not a reproducible in-house backtest. The Sharpe figures are for *fixed-income arbitrage broadly* pre-crisis and were negative through 2008. Treat all numbers as illustrative; this strategy's distribution has fat left tails that summary statistics hide.

| Metric | Range | Note |
|---|---|---|
| Locked carry (negative-basis, normal) | 10-60 bps/yr | Often barely above funding cost |
| Crisis dislocation | 200-600 bps at peak | The opportunity *and* the danger zone |
| Sharpe (Duarte-Longstaff-Yu 2007) | 1.0-1.5 pre-crisis | For FI-arb broadly; negative in 2008 |
| Drawdown in dislocation | 30-50% possible | Basis can widen while already "cheap" |

**Realistic costs:** bond bid-ask 5-25 bps, CDS bid-ask 2-10 bps, repo spread over OIS 5-30 bps in normal times and **100+ bps in stress** — and the stress cost is the one that matters, since it arrives exactly when the position is largest and most underwater. The `breakeven_cost_bps: 15` in frontmatter applies to normal conditions only.

## Capacity Limits

Large -- multiple billions per name for IG, hundreds of millions for HY. Total strategy capacity across a multi-name book is in the $5-20 bn range for top hedge funds. Limits come from: (a) single-name CDS notional outstanding (often $50-200 bn for top IG names), (b) bond float, (c) dealer balance sheet available for repo.

## What Kills This Strategy

- **Funding shock**: repo haircuts jump, term repo disappears, forcing mark-to-market losses and margin calls. 2008 and March 2020 are the canonical events.
- **Counterparty default**: if the CDS protection seller defaults before the reference entity, hedge evaporates. Most CDS now clear via [[ice-clear-credit]], mitigating this.
- **Restructuring / auction risk**: definitional disputes (e.g. the 2014-15 Caesars credit-event determinations, 2019 Sears CDS auction) can produce outcomes where CDS payout is less than bond loss. See [[succession-event]].
- **Regulatory capital changes**: new [[basel-iii]] / [[leverage-ratio]] rules can push dealers to stop quoting the trade, widening spreads.
- **[[failure-modes|Margin spiral]]**: forced liquidation at worse levels than entry.

## Kill Criteria

- Repo funding cost > locked carry + 10 bps.
- Basis widens > 100 bps beyond entry without fundamental catalyst.
- 3-month rolling return < -10%.
- Counterparty CDS on dealer > 200 bps (signals stress at protection-seller).
- Aggregate leverage > 8x (deleverage trigger).

## Advantages

| Advantage | Why it matters |
|---|---|
| Defined max loss in principle | Bond + CDS hedge is a synthetic Treasury — credit-hedged |
| Positive carry + crisis upside | Earns small carry normally, large returns in dislocations for patient capital |
| Clear economic rationale | Basis compensates a specific, identifiable friction (funding/balance sheet) |
| Scalable | Works for large hedge funds, bank prop desks, and insurers |

## Disadvantages

| Disadvantage | Why it matters |
|---|---|
| Balance-sheet & funding intensive | Needs sophisticated repo/treasury ops; can't run casually |
| Mark-to-market path risk | Can force liquidation before convergence (the 2008 lesson) |
| Correlation spikes in stress | Diversification collapses exactly when needed — see [[failure-modes]] |
| Counterparty & legal risk | CDS definitions, auctions, [[succession-event\|succession events]] |
| Basel III drag | [[leverage-ratio]] made the trade much less attractive for banks post-2015 |

## Sources

- Mitchell, M. and Pulvino, T. (2012). "Arbitrage Crashes and the Speed of Capital." *Journal of Financial Economics*.
- Duarte, J., Longstaff, F., Yu, F. (2007). "Risk and Return in Fixed Income Arbitrage." *Review of Financial Studies*.
- Bai, J. and Collin-Dufresne, P. (2019). "The CDS-Bond Basis." *Financial Management*.
- Fontana, A. (2011). "The Negative CDS-Bond Basis and Convergence Trading during the 2007/09 Financial Crisis." SSRN.
- [[ltcm-collapse-1998]] lessons on convergence trading and funding.

## Related

- [[credit-default-swap]]
- [[repo-market]]
- [[convergence-arbitrage]]
- [[relative-value-arbitrage]]
- [[ltcm-collapse-1998]]
- [[fixed-income-arbitrage]]
- [[dealer-balance-sheet]]
- [[limits-to-arbitrage]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[arbitrage]]
