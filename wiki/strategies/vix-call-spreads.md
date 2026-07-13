---
title: "VIX Call Spreads"
type: strategy
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, volatility, derivatives, risk-management]
aliases: ["VIX Call Spread", "Long VIX Call Spread", "VIX Bull Call Spread"]
strategy_type: quantitative
timeframe: swing
markets: [options]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, structural]
edge_mechanism: "Buy a cheap convex hedge that pays off in vol regime shifts; the seller of the upper call is a market-maker recycling vega from short-vol books and structured-product inventory."
data_required: [vix-futures-quotes, vix-options-chain, spx-options-chain]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: low
expected_sharpe: -0.5
expected_max_drawdown: 0.04
breakeven_cost_bps: 50
related: ["[[vix]]", "[[vix-futures]]", "[[vix-calls]]", "[[long-volatility-strategies]]", "[[tail-risk-hedging]]", "[[options-concentration-risk]]", "[[long-vol-vs-short-vol]]", "[[long-vol-overlay]]", "[[put-tree]]", "[[call-spread]]", "[[debit-spread]]", "[[implied-volatility]]", "[[vvix]]", "[[vega-budgeting]]", "[[options-selection-framework]]", "[[strike-selection]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[universa-investments]]", "[[contango]]", "[[backwardation]]", "[[sharpe-ratio]]"]
---

A **VIX call spread** is a long-vol overlay structure: buy a near-the-money or modestly out-of-the-money [[vix-calls|VIX call]] and sell a higher-strike call against it for the same expiry, paying a small net debit in exchange for a defined-risk payoff if the VIX index spikes. The structure is the cheapest convex hedge widely used by [[options-concentration-risk|concentrated short-premium books]] and [[long-vol-vs-short-vol|short-vol portfolios]]: it caps the upside relative to a naked long call, but it also caps the cost — and the cost is what kills tail hedges over multi-year holding periods. It is the single most popular structure cited by the ITPM / institutional playbook as a [[long-vol-overlay|long-vol overlay]] on a short-strangle book.

## Edge Source

The edge is **structural** plus a small **risk-bearing** premium reversal. VIX options are priced off [[vix-futures|VX futures]], which sit in [[contango]] roughly 80-85% of trading days. The seller of an upper-strike VIX call is typically a market-maker recycling vega from short-vol books, autocallables, or structured-product inventory; they are paid to absorb crash risk that the rest of their book is structurally short. The buyer of the spread accepts a small persistent bleed in exchange for owning a very specific shape: a payoff that activates exactly during vol regime shifts (VIX 25-40+) without paying for the parts of the distribution that rarely matter (VIX 60-80+).

## Why This Edge Exists

The structural reason VIX call spreads remain priced reasonably:

1. **Hedger demand is asymmetric.** Most institutional flow in VIX options is *sellers* — funds harvesting [[variance-risk-premium|VRP]], structured-product issuers offloading vega, and CTAs running short-vol overlays. The buying flow is fragmented across [[universa-investments|tail funds]], pension overlays, and retail hedgers. Sellers price patiently; buyers cross spreads.
2. **The upper call is overpriced for funded reasons.** Skew on VIX is positive — calls are priced above puts. Selling a far-OTM VIX call to fund a near-OTM long call captures part of this skew distortion.
3. **Term-structure dynamics suppress front-month premium.** When the VX curve is in steep [[contango]], front-month VIX call IV is suppressed because spot VIX is mean-reverting. This is a structurally cheap entry point.
4. **Crisis-alpha is uncrowded.** Long-vol structures lose money most months; career risk for managers running them is severe. The trade does not arbitrage away because the buying side is structurally limited.

## Null Hypothesis

Under random / no-edge conditions, the strategy should bleed at the rate implied by the put-call parity-equivalent fair value of the spread: roughly 1-3% of NAV per year for a 2-3% allocation, with positive payoffs occurring randomly. The edge case is rejected if (a) crash periods systematically *fail* to drive VIX through the long strike and (b) the bleed exceeds the implied premium drift on simulated random walks of VX futures.

## Rules

### Construction

| Leg | Strike | Tenor |
|---|---|---|
| Long call | 1-3 points above current spot VIX (or M1 VX futures) — typically VIX 18-22 strike when VIX is at 14-18 | 30-60 DTE |
| Short call | 8-15 points above the long strike — typically VIX 28-35 strike | Same expiry as long |

Net debit: typically $0.40-$1.20 per spread (each VIX option = $100 multiplier).

### Sizing

- Allocate **0.5-2% of NAV per month** to rolling VIX call spreads.
- For a $250K book that wants ~$25K of crash payoff: buy ~30-50 spreads at $0.50 debit = $1,500-$2,500 monthly cost.
- Stack 2-3 expiries continuously so a portion of the ladder is always 30+ DTE.

### Entry Timing

- **Best entry:** when [[vix]] is below 16 *and* VX curve is in steep contango. Premium is suppressed; convexity is highest.
- **Worst entry:** during ongoing vol shocks (VIX 25+). Premium is already spiked; structure is overpriced for what is left of the move.

| Spot VIX | VX curve (M2/M1) | Action | Rationale |
|---|---|---|---|
| <16 | > 1.05 (steep [[contango]]) | **Enter** (ideal) | Suppressed front-month IV, cheapest convexity |
| 16-22 | 1.02-1.05 | Enter normal tranche | Acceptable; standard sizing |
| 16-22 | < 1.02 (flat) | Skip | Hedge already implied in spot; curve gives no edge |
| >22 | Any | Skip | Premium spiked; little move left to capture |
| Any | < 1.0 ([[backwardation]]) | Skip / monetize | Crisis already underway; do not add |

### Exit / Roll

- **Monetize at 3-5x the debit paid** if VIX spikes meaningfully (e.g., VIX 25-30+).
- **Let losers expire worthless** if spot stays calm. Do not sell in the last week — gamma collapses anyway.
- **Roll monthly** as new front-month becomes available. Maintain the ladder.

### Position Sizing Rule of Thumb

Cap monthly spend at **0.25-0.5% of NAV** per expiry. The annualized cost target is **2-4% of NAV** for a robust overlay; less is insufficient, more starts to dominate the [[long-vol-vs-short-vol|short-vol core]].

## Implementation Pseudocode

```python
# Monthly roll on a discretionary or systematic VIX call spread overlay
def roll_vix_call_spreads(account_nav, vix_spot, vx_term_structure):
    monthly_budget = account_nav * 0.003  # 0.3% per month, ~3.6% annualized

    # Anchor strikes to spot VIX with skew filter
    long_strike = round(max(vix_spot + 2, 18))
    short_strike = long_strike + 10  # 10-point wide spread

    # Skip if regime is already stressed (VIX > 22) — premium too rich
    if vix_spot > 22:
        return "skip — premium spiked, wait for mean reversion"

    # Skip if curve is flat / inverted — overlay underperforms here
    if vx_term_structure["m2_m1_ratio"] < 1.02:
        return "skip — curve flat, hedge already implied in spot"

    # Target 30-45 DTE expiry
    target_expiry = next_monthly_expiry(min_dte=30, max_dte=45)

    # Compute spread debit at mid
    debit = get_spread_quote(long_strike, short_strike, target_expiry)

    # Size to budget
    contracts = int(monthly_budget / (debit * 100))

    return submit_spread_order(
        long_strike, short_strike, target_expiry, contracts, debit
    )
```

## Payoff & Greeks

### Payoff sketch (long VIX call spread: long Kᴸ, short Kᴴ)

```
P/L
  ^
  |                         _________________  <- max profit = (Kᴴ - Kᴸ) - debit
  |                        /
  |                       /
  |                      /
0 +----------------+---/------+-----------------> VIX future at expiry
  |                |  /       | Kᴴ (e.g. 28)
  |________________|_/        (short call caps the payoff here)
  -debit            Kᴸ (e.g. 18)
                    breakeven = Kᴸ + debit
```

The structure is a [[debit-spread|long debit call spread]] on the [[vix-futures|VX future]]. Below the long strike Kᴸ the loss is the (small) net debit; between Kᴸ and Kᴴ the payoff ramps up; above Kᴴ the short call caps the payoff at the strike width minus the debit. Maximum payoff multiple is therefore `(Kᴴ − Kᴸ − debit) / debit` — e.g. a 10-point spread bought for $0.55 caps at ~17x. The trade-off versus a naked [[vix-calls|VIX call]] is explicit: lower carry cost, bounded upside.

### Net-Greeks table (long VIX call spread, low-vol entry)

| Greek | Sign | vs naked [[vix-calls\|VIX call]] | Trading meaning |
|---|---|---|---|
| Delta | + | Lower (short call offsets) | Net long VIX-future exposure, but muted above Kᴴ |
| Gamma | + then − | Lower net | Long gamma near Kᴸ, short gamma near Kᴴ; convexity is bounded |
| Theta | − | **Less negative** (short call earns theta) | The short upper call funds 30-60% of the bleed — the core advantage |
| Vega (vol-of-vol) | + | Lower net | Long [[vvix\|vol-of-vol]] near Kᴸ, short near Kᴴ; partly self-financed |
| Rho | ~0 | ~same | Negligible |

Net exposure: **bounded long convexity, reduced carry.** Selling the upper call deliberately gives up the deep-tail (VIX 50-80+) payoff to claw back theta and vega cost. This is why the spread "saturates" in a [[volmageddon|Volmageddon]]-scale event but still pays many multiples of premium. See [[long-vol-vs-short-vol]] and [[vega-budgeting]].

## Indicators / Data Used

- Spot [[vix]] level and 30-day realized vol of vol
- [[vix-futures|VX futures]] term structure: M1, M2, M3-M9 contract prices
- VIX options [[implied-volatility|IV]] surface and skew snapshot
- SPX 30-day [[implied-volatility|IV]] and realized vol for cross-validation
- VVIX (vol of VIX) — current level vs 1-year history

## Example Trade

**Setup (May 2025-style calm regime):**

- Spot VIX: 14.5
- M1 VX future: 16.2; M2 VX future: 17.4 (steep contango)
- Account NAV: $250K
- Monthly hedge budget: $750

**Trade:**

- Long 14 VIX June 18 calls @ $0.85
- Short 14 VIX June 28 calls @ $0.30
- Net debit: $0.55 × 14 × $100 = **$770** (just over the $750 monthly tranche; acceptable)

**Outcome A (calm — most months):** VIX drifts in 13-17 range. Both legs expire worthless. Loss: $770.

**Outcome B (mild stress):** VIX rises to 24 around June expiry. Long 18C worth ~$6.00; short 28C worth ~$0.10. Spread value ~$5.90. Sell at $5.50 = $7,700 gross, **$6,930 net profit** on $770 risked. ~9x.

**Outcome C ([[vix-august-2024-spike|2024 yen-carry-style]] shock):** VIX gaps to 50 intraday. Long 18C worth $32+; short 28C worth $22+. Spread caps at ~$10.00 = $14,000 gross, **$13,230 net profit**. ~17x. The 10-point cap binds; the upside is bounded but a single ladder rung already pays for years of monthly debits and offsets a large slice of a short-vol core's shock loss.

## Performance Characteristics

- **Hit rate:** 10-20% of expirations produce meaningful gains; 80-90% expire worthless or near-zero.
- **Average bleed (calm year):** -2% to -4% of NAV in pure-overlay sizing.
- **Average payoff (crash year):** +5% to +20% of NAV depending on shock magnitude and roll discipline.
- **Sharpe (standalone):** Negative (-0.3 to -0.8) over calm periods.
- **Sharpe (in blended book):** Adds 0.2-0.5 to a [[long-vol-vs-short-vol|short-vol core]] over a full cycle by fixing the negative-skew tail.
- **Max bleed in calm year:** Bounded at total monthly debits = ~3-4% of NAV.

### VIX call spread vs related long-vol structures

| Structure | Carry cost | Upside | Best regime | Note |
|---|---|---|---|---|
| **VIX call spread** (this page) | Low-moderate | Capped at strike width | Calm, steep [[contango]] | Cheapest convex hedge; saturates in extreme spikes |
| [[vix-calls\|Naked VIX calls]] | High | Uncapped | Calm, very low VIX | Full convexity, highest bleed |
| SPX puts | High | Uncapped | Slow equity crash | Path-dependent; fires slower than VIX |
| [[put-tree\|Put trees / ratio]] | Very low / credit | Asymmetric, capped zone | Moderate selloffs | Adds short gamma in deep tail — careful |
| [[long-vol-overlay\|Full long-vol overlay]] | 2-3.5%/yr | Blended | All | Combines VIX calls + SPX puts on a short-vol core |

A practitioner typically does not choose one structure but **ladders several** (see [[long-vol-overlay]] and [[universa-investments]]) so that no single tenor or saturation point dominates the tail payoff.

## Capacity Limits

The VIX options market is liquid — listed open interest in front-month VIX calls regularly exceeds 500K contracts. A single trader running $50M+ of VIX-call-spread notional can begin to move the bid-ask on individual strikes; institutional [[universa-investments|tail funds]] running $1B+ rotate across multiple structures (VIX calls, SPX puts, [[put-tree|put trees]], variance swaps) to spread market impact. For retail and small-fund users, capacity is effectively unlimited.

## What Kills This Strategy

- **Structurally expensive vol regime.** A multi-year period with VIX persistently above 25 (e.g., late 2008, mid-2020) makes the spreads expensive to roll and reduces convexity. The hedge becomes a high-cost insurance product.
- **Persistent backwardation.** When the VX curve is in [[backwardation]], the front-month future trades above the back, removing the cheap-front-month entry advantage.
- **Compressed skew.** If the upper call (e.g., VIX 30 strike) becomes systematically rich, the spread debit widens and cost rises.
- **Fed-suppressed vol regime.** Quantitative-easing-style central-bank backstops can suppress VIX for years at a time (2013-2017 was such a period). The strategy bleeds through these regimes.

## Kill Criteria

- **Annualized bleed > 6% of NAV** sustained over 24 months with no monetization opportunities.
- **Realized sharpe contribution to combined book < 0.0** over 36 months (overlay is not paying for itself).
- **Spread debit > 8% of upper-lower strike width** consistently — premium has become unattractive vs. raw SPX put alternatives.
- **VIX options bid-ask widens to >25% of mid** during normal hours — liquidity has degraded enough to make rolling impractical.

## Advantages

- **Defined cost.** Maximum loss = debit paid. No margin call risk, no [[gap-risk]], no forced liquidation.
- **Convex payoff in vol regime shifts.** Pays multiples of premium during VIX spikes — exactly the regime that hurts [[options-concentration-risk|short-premium books]].
- **Cheaper than naked VIX calls.** The short upper call funds 30-60% of the long lower call premium.
- **Capital-light.** A 2-3% NAV allocation is sufficient for meaningful protection.
- **Listed and liquid.** Trades on Cboe, cash-settled, no counterparty risk.
- **Complements other long-vol structures.** Stacks well with SPX puts and [[put-tree|put trees]] for diversified tail protection.

## Disadvantages

- **Capped upside.** Unlike a naked long call, the spread's payoff is bounded at (upper strike - lower strike) × $100. In a Volmageddon-style move where VIX hits 50+, the spread saturates and leaves money on the table.
- **Persistent bleed.** Most months the spread expires worthless. Multi-year bleed is psychologically punishing.
- **Settlement quirk.** VIX options settle to the [[vix-futures|VIX SOQ]] on Wednesday morning, not to spot VIX at close. The settlement print can differ from what traders see on-screen at expiry.
- **Wrong-tenor risk.** The hedge expires monthly; a slow grind-down crash that takes 3+ months to develop may not produce a single profitable expiry.
- **Settlement basis risk** between VX futures and SPX volatility — VIX can fail to spike even if SPX falls (rare but documented).

## Sources

- Cboe Global Markets, *VIX Options Methodology and Specifications*
- Spitznagel, Mark. *Safe Haven: Investing for Financial Storms* (2021)
- Bhansali, Vineer. *Tail Risk Hedging* (2014) — practitioner construction notes on VIX spreads
- [[itpm-trade-construction-playbook]] — long-vol overlay sizing within a portfolio
- US Joint CFTC/SEC Staff Report, *February 5, 2018 VIX Volatility Event*

## Related

- [[vix]] — the underlying index
- [[vix-futures]] — the futures the options price off
- [[vix-calls]] — the naked-long-call alternative
- [[tail-risk-hedging]] — the broader strategy class
- [[options-concentration-risk]] — the problem this hedges
- [[long-vol-vs-short-vol]] — the philosophical framework
- [[long-vol-overlay]] — the overlay sizing approach
- [[put-tree]] — another defined-risk long-vol structure
- [[call-spread]] — the underlying structure type
- [[long-volatility-strategies]] — the broader family of long-vol trades
- [[debit-spread]] — the generic structure this is an instance of
- [[vvix]] — the vol-of-vol that drives VIX-option vega
- [[vega-budgeting]] — sizing the overlay vega against the core
- [[options-selection-framework]] — the general strike/expiry funnel
- [[strike-selection]] — anchoring the long and short strikes by delta
- [[sharpe-ratio]] — why the stand-alone Sharpe is negative
- [[universa-investments]] — the canonical tail fund using VIX-call structures alongside SPX puts
- [[volmageddon]] — the 2018 event that validated VIX call spreads
- [[vix-august-2024-spike]] — recent example of payoff magnitude
