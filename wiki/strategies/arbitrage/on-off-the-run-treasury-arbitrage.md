---
title: "On-the-Run vs Off-the-Run Treasury Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, bonds, treasuries, liquidity, leverage, history]
aliases: ["OTR/OFR Arb", "On/Off the Run Trade", "Treasury Liquidity Arb", "29.75 vs 30 Year Trade"]
strategy_type: quantitative
timeframe: position
markets: [bonds, treasuries]
complexity: advanced
backtest_status: retired
edge_source: [structural, risk-bearing]
edge_mechanism: "Newly-issued Treasuries trade at a liquidity premium over seasoned bonds with near-identical cash flows; the arb captures the spread as it decays, but requires bearing the risk that the premium widens in a flight-to-quality."
data_required: [treasury-quotes-intraday, repo-rates, cusip-level-positions]
min_capital_usd: 5000000
capacity_usd: 2000000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.50
breakeven_cost_bps: 2
decay_evidence: "Liquidity premium documented academically by Amihud & Mendelson (1991) and Krishnamurthy (2002); post-2008 the spread averages 2-4 bps, largely competed away by HFT and RV funds; LTCM's 1998 blow-up is the canonical failure case"
related: ["[[ltcm-collapse-1998]]", "[[convergence-arbitrage]]", "[[swap-spread-arbitrage]]", "[[tips-treasury-arbitrage]]", "[[relative-value-arbitrage]]", "[[basis-trading]]", "[[repo-market]]", "[[flight-to-quality]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[limits-to-arbitrage]]", "[[liquidity-premium]]"]
---

# On-the-Run vs Off-the-Run Treasury Arbitrage

The on-the-run vs off-the-run (OTR/OFR) Treasury arbitrage exploits the persistent yield gap between the most recently auctioned Treasury security (**on-the-run**) and an otherwise nearly-identical seasoned issue (**off-the-run**) of the same maturity. Because the on-the-run bond is more liquid and heavily used as a benchmark, hedging instrument, and repo collateral, it trades at a premium — i.e., a lower yield — of typically 3-15 basis points. The arb shorts the rich on-the-run, buys the cheap off-the-run, and waits for the spread to mean-revert as the current issue ages and loses its "specialness." It is the archetypal [[convergence-arbitrage]] / [[relative-value-arbitrage]] trade and the one most associated with the [[ltcm-collapse-1998|LTCM]] story: a tiny, near-certain spread harvested with heavy leverage, whose dominant risk is the [[limits-to-arbitrage|limit to arbitrage]] that the spread can *widen* before it converges.

### Anatomy of the spread (how the same cash flows yield differently)

The cleanest way to see the trade is to line up the two legs as the desk does:

| Feature | On-the-run (OTR) | Off-the-run (OFR) | Direction of the spread |
|---|---|---|---|
| Auction recency | Most recent | One or more auctions older | OTR newer |
| Liquidity / bid-ask | ~0.5 bp | ~3-5 bp | OTR richer |
| Repo financing | Often "special" (cheap to borrow) | General collateral | OTR holder subsidized |
| Benchmark / hedging use | Primary benchmark | Rarely quoted | OTR demand chronic |
| Index / mandate demand | Forced inclusion | Optional | OTR bid up |
| Yield | Lower (price higher) | Higher (price lower) | **3-15 bp gap** |
| The trade | **Short** (sell rich) | **Long** (buy cheap) | Capture convergence |

The two bonds are not perfectly identical — they differ slightly in coupon and exact maturity date — which is why the position is hedged on a [[dv01]] basis rather than notional. After DV01 matching, the residual exposure is almost purely the [[liquidity-premium]].

## Edge Source

**Structural** (primary) and **risk-bearing** (secondary). The edge is a textbook example of a [[liquidity-premium]]: a structural mispricing driven by demand for liquidity, search costs in the Treasury market, and the use of the on-the-run as the *de facto* hedging instrument for dealers. There is no informational or behavioral edge here — the spread is public and has been documented academically at least since Amihud & Mendelson's 1991 *Journal of Finance* study of Treasury liquidity and yields, with the on-the-run/off-the-run spread analyzed in depth by Krishnamurthy (2002). See [[edge-taxonomy]].

## Why This Edge Exists

Two Treasury bonds maturing six months apart and paying near-identical coupons should yield nearly the same thing. But the **on-the-run** benefits from:

1. **Repo specialness** — dealers short the OTR to hedge other positions, creating chronic demand to borrow it. Repo rates on a special OTR can trade 50-200 bps below general collateral, subsidizing its holder.
2. **Benchmark status** — traders quote the OTR as the benchmark, so it clears huge volume. Bid-ask spreads are ~0.5 bps on the OTR vs 3-5 bps on seasoned issues.
3. **Index inclusion and mandate** — many passive and indexed portfolios must hold the current issue.
4. **Search frictions** — finding a specific off-the-run CUSIP takes work; the OTR is always available.

The counterparty is **anyone who pays up for liquidity**: pension funds doing immediate portfolio transitions, dealers hedging swap books, foreign central banks managing reserves. They pay the premium willingly because the cost of *not* getting executed dwarfs the 5-10 bp liquidity tax. The arbitrageur provides liquidity by warehousing the cheap, illiquid off-the-run.

## Null Hypothesis

Under frictionless markets with no search costs or mandate constraints, Treasuries with identical cash flows and maturity dates should trade at identical yields. The null hypothesis is an OTR/OFR spread of zero. The empirically observed spread of 3-15 bps is the **measure** of structural friction.

## Rules

### Entry
1. Identify an OTR Treasury (e.g., the 30-year auctioned today) and the immediately preceding issue (e.g., the 29.75-year, auctioned three months prior).
2. Confirm the yield spread: OFR yield minus OTR yield. Enter when the spread is ≥ 8 bps (above the ~5 bp historical median).
3. **Short the OTR** — borrow it in repo, sell it in cash market.
4. **Buy the OFR** — finance the long in repo.
5. Size the short to be **DV01-neutral** to the long, not notional-neutral. A small coupon difference can swing the hedge ratio.

### Exit
1. Wait for the next auction. When a new 30-year is auctioned, the previous 30-year becomes off-the-run and the spread to the NEW seasoned bond collapses toward zero.
2. Target ~50% of the spread as the realistic capture. E.g., enter at 10 bps, expect to unwind at 4-5 bps.
3. Hold period: typically one auction cycle (3-6 months for long-end Treasuries).

### Position Sizing
Because the trade is levered 20-50x through repo, size so that a 20 bp adverse move (historical stress) does not exceed 15% of capital. [[ltcm-collapse-1998|LTCM]] sized at 30x+ and the trade consumed them when the spread went the wrong way.

## Implementation Pseudocode

```python
def otr_ofr_spread_signal(otr_cusip, ofr_cusip, repo_book):
    otr_yield = get_yield(otr_cusip)
    ofr_yield = get_yield(ofr_cusip)
    spread_bps = (ofr_yield - otr_yield) * 1e4

    otr_dv01 = dv01(otr_cusip)
    ofr_dv01 = dv01(ofr_cusip)
    hedge_ratio = ofr_dv01 / otr_dv01

    if spread_bps > 8 and repo_book.can_borrow(otr_cusip):
        return Trade(
            long=(ofr_cusip, 1.0),
            short=(otr_cusip, hedge_ratio),
            financing="repo",
            target_spread_bps=4,
            stop_spread_bps=20,  # critical — LTCM had no stop
        )
    return None
```

## Indicators / Data Used

- [[treasury-yield-curve]] at CUSIP granularity (not par curve)
- **Repo specialness** — the rate at which the OTR can be borrowed vs GC repo
- **Fails-to-deliver** data from DTCC — signals acute shorting demand
- **Auction calendar** — the next auction date caps the expected holding period
- [[dv01]] for hedge ratio
- Bid-ask spread differential as a proxy for liquidity premium

## Example Trade: LTCM's 29.75 vs 30-Year

LTCM's signature trade, executed dozens of times with dozens of CUSIPs, ran roughly as follows (1997):

- **Long**: $500M face of the 29.75-year off-the-run 30-year (auctioned three months prior), yielding 6.77%.
- **Short**: ~$490M face of the on-the-run 30-year auctioned today, yielding 6.70%.
- **Spread captured**: 7 bps, DV01-neutral.
- **Financing**: 20x leverage via repo; capital at risk ~$25M.
- **P&L per bp of convergence**: ~$700K.
- **Expected convergence**: 4-5 bps over ~3 months = $2.8-3.5M profit on $25M capital ≈ 11-14% quarterly.

This was the template. LTCM scaled it across dozens of pairs (nominal Treasuries, [[tips-treasury-arbitrage|TIPS vs nominals]], [[swap-spread-arbitrage|swap spreads]], [[mbs-basis-arbitrage|MBS]]).

## Performance Characteristics

- **Pre-1998**: realized Sharpe ~1.5-2.0 for disciplined, size-constrained practitioners. Spread mean-reverted reliably every auction cycle.
- **1998 stress**: spread widened from ~6 bps to 19+ bps in 6 weeks as [[flight-to-quality]] bid up OTR liquidity. See [[ltcm-collapse-1998]].
- **Post-2008**: spread averages ~2-4 bps, sometimes briefly inverts. Edge largely competed away by HFT market makers and large hedge funds with cheap repo. **No longer a standalone strategy** — embedded inside relative-value books.
- **Capacity**: perhaps $1-2B gross notional before the trade itself moves the spread.

### Return shape and the leverage trap

The defining feature of this trade — and the reason it appears throughout the [[limits-to-arbitrage]] literature — is its **negatively skewed, leptokurtic P&L**: many small, near-certain gains as spreads grind in, punctuated by rare, violent losses when [[flight-to-quality]] forces a widening. The table contrasts the regimes (illustrative magnitudes, not a backtest):

| Regime | Spread behavior | Unlevered P&L per cycle | Effect of 20-50x leverage |
|---|---|---|---|
| Normal convergence | 10 bp → 4-5 bp over one auction cycle | Small positive (a few bp of DV01) | Amplified to attractive double-digit quarterly returns |
| Quiet drift | Spread flat, carry from repo specialness | Marginally positive | Carry covers financing; modest gain |
| Flight-to-quality | 6 bp → 19+ bp in weeks (1998) | Moderate mark-to-market loss | **Catastrophic** — margin calls, forced unwind at the worst spread |

The cruel arithmetic: the leverage required to make the *normal* regime interesting (20-50x, because the raw spread is only a few bp) is the same leverage that makes the *stress* regime fatal. There is no cost overlay that produces an attractive standalone return without taking on the tail. This is the structural reason `expected_max_drawdown` is set to 0.50.

## Capacity Limits

The OTR float is typically $40-80B per issue at the long end. A fund running $2B of this trade is ~3-5% of float, which is the approximate ceiling before market impact dominates. LTCM ran multiples of this across correlated trades and learned the capacity lesson the hard way.

## What Kills This Strategy

1. **Flight-to-quality** — the single worst scenario. In panic, investors pay *more* for OTR liquidity, so the spread widens instead of converging. This killed [[ltcm-collapse-1998|LTCM]] in August-September 1998 after the Russian default.
2. **Repo financing pulled** — if prime brokers demand additional haircut on the off-the-run leg (which is what happened in September 1998), forced liquidation at the worst possible spread.
3. **Auction cancellation or schedule change** — removes the expected convergence catalyst.
4. **Structural liquidity changes** — Treasury buyback programs (2000-2002) collapsed the off-the-run discount and pushed spreads to zero for years.
5. **Correlation with other relative-value trades** — when OTR/OFR widens, so typically do [[swap-spread-arbitrage|swap spreads]], [[mbs-basis-arbitrage|MBS basis]], and [[tips-treasury-arbitrage|TIPS breakevens]]. A "diversified" RV book concentrates in one factor: liquidity.

See [[failure-modes]] for the general taxonomy.

## Kill Criteria

- Spread widens to >20 bps and financing terms tighten — **exit regardless of P&L**.
- Repo haircut raised by prime broker on the long leg.
- Rolling 6-month return < -10% at the trade level.
- Treasury issuance policy changes structurally (e.g., buyback programs).
- Median spread compresses below 3 bps for 12 months — edge no longer exists net of costs.

## Advantages

- **Transparent mispricing**: both sides are Treasury bonds — no credit risk, no model risk on the pricing of the instruments themselves.
- **Defined catalyst**: the next auction is scheduled and known.
- **High notional leverage** possible because Treasuries haircut cheaply in repo.
- **Near-perfect hedge**: after DV01 matching, the residual is purely liquidity spread.

## Disadvantages

- **Liquidity-premium is itself liquidity risk**: the spread is compensation for bearing the risk that it widens. In a crisis, it widens *dramatically*.
- **Extreme leverage required** to produce interesting returns, which amplifies any stress.
- **Correlated with every other fixed-income RV trade** in a crisis.
- **Competitive edge erosion**: HFT and dealers have decimated the easy 10 bp spread.
- **Repo roll risk**: financing is short-term (overnight to 3-month); can be pulled in a crisis.

## Sources

- [[ltcm-collapse-1998]] — the canonical case study for the trade and its failure mode
- Amihud & Mendelson (1991), *Liquidity, Maturity, and the Yields on U.S. Treasury Securities*, Journal of Finance — canonical documentation of the Treasury liquidity premium
- Krishnamurthy (2002), *The Bond/Old-Bond Spread*, Journal of Financial Economics — direct study of the on-the-run/off-the-run spread and its convergence
- Roger Lowenstein, *When Genius Failed* (2000) — narrative account of LTCM's on/off-the-run book

## Related

- [[ltcm-collapse-1998]] — the fund that made this trade famous and then infamous
- [[convergence-arbitrage]] — the parent strategy class
- [[relative-value-arbitrage]] — umbrella category
- [[swap-spread-arbitrage]] — correlated sister trade
- [[tips-treasury-arbitrage]] — another LTCM staple
- [[mbs-basis-arbitrage]] — the third leg of LTCM's RV triangle
- [[basis-trading]] — general concept
- [[repo-market]] — the financing mechanism
- [[flight-to-quality]] — the thing that kills the trade
- [[liquidity-premium]] — the underlying mispricing source
- [[limits-to-arbitrage]] — why the spread can widen before it converges
- [[edge-taxonomy]]
- [[failure-modes]]
