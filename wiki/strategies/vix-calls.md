---
title: "VIX Calls"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, risk-management, futures]
aliases: ["VIX Calls", "VIX Call Options", "Volatility Hedge", "Tail-Risk Hedge"]
related: ["[[vix]]", "[[vix-futures]]", "[[vix-call-spreads]]", "[[long-vol-overlay]]", "[[long-volatility-strategies]]", "[[volatility-trading]]", "[[risk-management]]", "[[protective-puts]]", "[[implied-volatility]]", "[[options]]", "[[variance-risk-premium]]", "[[tail-risk-hedging]]", "[[contango]]", "[[backwardation]]", "[[options-selection-framework]]", "[[strike-selection]]", "[[sharpe-ratio]]"]
strategy_type: technical
timeframe: swing
markets: [options, futures]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, risk-bearing]
edge_mechanism: "Buys crash convexity from volatility sellers harvesting the variance risk premium; the hedger knowingly pays negative expected value standalone in exchange for cash exactly when equities crater, improving portfolio-level compounding."
data_required: [options-chain, vix-futures-term-structure, ohlcv-daily]
min_capital_usd: 10000        # sensible only as an overlay on a portfolio of this size or larger
capacity_usd: 500000000       # annual premium spend before moving VIX option/futures markets
crowding_risk: medium
expected_sharpe: -0.2         # STANDALONE the hedge sleeve has negative carry; value is portfolio-level convexity
expected_max_drawdown: 0.03   # worst-case annual portfolio drag = full loss of a 3% hedge budget
breakeven_cost_bps: 200       # round-trip spread + roll cost as share of premium the overlay can absorb
kill_criteria: |
  - rolling 3-year hedge bleed exceeds 4%/yr of total portfolio value
  - in any S&P 500 drawdown deeper than 15%, the hedge pays out less than 2x the trailing 12 months of premium spent
  - VIX futures curve in persistent backwardation > 6 months (systematic call buying then buys the peak)
---

# VIX Calls

VIX calls are call options on the [[vix|CBOE Volatility Index (VIX)]] used primarily as a tail-risk hedge to protect portfolios against sharp market declines. Because the VIX tends to spike dramatically when equity markets sell off -- it rose from 14 to 82 in a single month during March 2020 -- owning VIX calls provides convex, leveraged exposure to volatility increases that can offset equity losses during crises. However, VIX calls are expensive to hold on an ongoing basis due to the structural headwinds of [[contango]] in VIX futures and the mean-reverting nature of volatility: standalone, systematic VIX call buying has **negative expected value**, and the strategy only makes sense as a portfolio overlay.

## Overview

The VIX Index measures the 30-day expected volatility of the S&P 500, derived from the prices of SPX options. It is often called the "fear gauge" because it tends to be inversely correlated with the S&P 500 -- when stocks drop sharply, the VIX spikes. Historically, the VIX has averaged around 19-20, but during acute market stress it can surge to 40, 60, or even above 80 (closing high: 82.69 on 16 March 2020; it also closed at 80.86 in November 2008).

VIX options are European-style, cash-settled options that trade on the CBOE. Critically, VIX options are priced off VIX futures, not the spot VIX itself. This distinction is essential: because VIX futures are typically in contango (longer-dated futures trade above spot), VIX call options are priced relative to an already-elevated futures level, making them more expensive than a naive look at spot VIX would suggest.

Despite their cost, VIX calls remain one of the most effective tail-risk hedges available to retail and institutional investors. A small allocation to VIX calls can produce outsized returns during market crashes, offsetting a significant portion of equity losses. The key challenge is sizing and timing the hedge to avoid excessive premium bleed during normal markets.

## Edge source

Per the [[edge-taxonomy]]: **structural** and **risk-bearing** -- but in an unusual, inverted sense. The VIX call buyer is *paying* the [[variance-risk-premium]] to volatility sellers, so the sleeve has negative standalone expected return (frontmatter Sharpe -0.2). The structural edge claimed is at the **portfolio level**: the payoff arrives precisely when equity capital is cheapest (crashes), so a disciplined hedger can rebalance crash winnings into depressed equities, raising long-run compound growth and cutting maximum drawdown. The edge, if it exists for a given investor, comes from (a) convexity -- 5-10x+ payoffs concentrated in the states of the world where a marginal dollar is most valuable -- and (b) the option to stay fully invested in equities (or run modest leverage) because tail risk is insured.

## Why this edge exists

The counterparty is the volatility-selling complex: option overwriters, variance-swap desks, and short-VIX ETP flows harvesting the variance risk premium (implied volatility persistently exceeds subsequently realized volatility by roughly 2-4 vol points on average in SPX). They are not "losing" in expectation -- they are being paid to bear crash risk, and the hedger is the one paying. What the hedger receives in exchange is state-contingent liquidity: cash delivered in the worst states. The trade persists on both sides because the two parties value the crash state differently: a leveraged or drawdown-constrained investor rationally pays an actuarially unfair premium for insurance, just as homeowners do. Volatility sellers periodically do lose catastrophically (the February 2018 "Volmageddon" wiped out the XIV short-vol ETN, which lost ~95% in a day), which is the payoff the call buyer is positioned for.

### Why VIX calls are expensive

Several structural factors make VIX calls persistently costly:

1. **Contango in VIX futures**: VIX futures typically trade 2-5 points above spot VIX. A VIX call with a strike of 25 might require VIX futures (not spot VIX) to exceed 25 to be profitable. If spot VIX is 15 but the relevant futures contract is at 19, the call is closer to the money than it appears, but the holder still needs a meaningful volatility spike to profit.

2. **Mean reversion of volatility**: Unlike stock prices, volatility is strongly mean-reverting. A VIX spike from 15 to 40 will almost certainly be followed by a decline back toward the long-run average. This limits the window during which VIX calls are in the money and makes it difficult to capture the full value of a spike.

3. **Volatility-of-volatility premium**: The market charges a premium for options on volatility itself, since volatility is volatile. This "vol-of-vol" premium means VIX options tend to be expensive relative to the actual realized movement of VIX futures.

4. **Roll cost**: If a trader maintains an ongoing VIX call hedge, they must roll to new expirations each month. Each roll resets the theta clock and incurs transaction costs, creating a persistent drag.

## Null hypothesis

Under the null -- no portfolio-level value to convexity, or an inability to monetize spikes -- systematic VIX call buying is simply a slow donation of the variance risk premium to vol sellers. The evidence for the null is strong on a standalone basis: long-VIX-futures products (e.g., buy-and-hold VXX since its 2009 inception) have lost essentially all of their value through roll decay, and the CBOE VIX Tail Hedge Index (VXTH), which systematically allocates ~1% of a portfolio to 30-delta VIX calls, has lagged the plain S&P 500 over long bull-market stretches. The strategy only beats the null if (1) spikes are actually sold near the highs rather than held to mean-reversion, and (2) proceeds are redeployed into depressed equities. A hedger who cannot demonstrate both behaviours should expect pure negative carry of 1-3% of portfolio value per year.

## Rules

### When to buy (entry)

VIX calls are most cost-effective and offer the best risk/reward when:

- **VIX is low (12-16 range)**: Calls are cheapest when complacency is high and protection is least demanded. This is also when the next vol spike is statistically most likely to be large, since it starts from a compressed base.
- **VIX term structure is steep**: When front-month VIX futures are well below back-month futures (steep contango), it signals complacency. Buying calls on the front month or second month can provide leveraged exposure to a contango-to-backwardation shift during a crisis.
- **Ahead of known catalysts**: Elections, central bank meetings, debt ceiling deadlines, or other events with binary outcomes can trigger vol spikes. Buying VIX calls before these events can be a targeted hedge.

Avoid initiating when:

- **VIX is already elevated (above 25-30)**: Calls are expensive, and mean reversion works against the holder. Much of the vol spike may already be priced in.
- **Term structure is in backwardation**: When front-month VIX is above back-month VIX, the market is already in crisis mode. Buying calls here often means buying the peak.

### Entry decision table

| Spot VIX | Term structure | Action | Rationale |
|---|---|---|---|
| 12-16 | Steep [[contango]] | **Buy** (best entry) | Cheap premium, maximum convexity, spike starts from a compressed base |
| 16-22 | Mild contango | Buy normal tranche | Acceptable; size to budget |
| 22-28 | Flat | Reduce / wait | Premium rich, less room for mean-reversion edge |
| >28 | [[backwardation]] | **Do not initiate** | Buying the peak; pay-up just before reversion |
| Any | Backwardation >6 months | Suspend program | Systematic buying is chasing a sustained crisis |

### Contract selection and mechanics

1. **Select the expiration**: 1-3 months out. Shorter expirations have more gamma (react faster to VIX moves) but decay faster. Longer expirations are more expensive but less sensitive to timing.
2. **Select the strike**: OTM calls (e.g., strike of 25-35 when VIX is at 15-18) provide the most leverage but require a larger VIX move to profit. ATM calls are more expensive but profit from smaller moves.
3. **Buy the calls**: Pay the premium upfront. This is the maximum loss on the hedge.

### Exit

4. If VIX spikes, **sell some or all of the calls to lock in gains**. Do not wait for expiration -- VIX spikes are typically short-lived (days to weeks), and the special opening quotation (SOQ) settlement may land far from the spike high. A practical rule: scale out in thirds at 3x, 5x, and 8x cost.
5. If calls approach expiration with VIX still low, let them expire and roll to the next cycle.
6. **Roll periodically**: replace expiring calls with new ones to maintain continuous protection.

### Position sizing

A common guideline for portfolio-level VIX call hedging is to allocate **1-3% of total portfolio value per year** to the hedge. This keeps the bleed manageable while providing meaningful crisis protection. Deploy the budget in quarterly (or monthly) tranches rather than all at once, and never exceed the annual budget chasing a spike already underway.

**Example sizing**: A $1 million equity portfolio allocating 2% ($20,000) per year to VIX calls. The trader buys $5,000 in VIX calls each quarter, rolling before expiration. During a market crash where VIX spikes from 15 to 50, the calls might return 5-10x, generating $25,000-$50,000, which offsets a significant portion of the portfolio's equity losses (which might be $150,000-$250,000 in a 15-25% drawdown).

## Implementation pseudocode

```python
# Quarterly hedge cycle for portfolio P
ANNUAL_BUDGET = 0.02 * P          # 1-3% of portfolio per year
TRANCHE       = ANNUAL_BUDGET / 4

def quarterly_roll(spot_vix, curve):
    if curve.is_backwardated() or spot_vix > 28:
        hold_cash(TRANCHE)         # don't buy the peak; wait for normalization
        return
    expiry = pick_expiry(months_out=2)             # 1-3 months
    strike = round_to_strike(spot_vix + 10)        # ~25-35 when VIX is 15-18 (OTM)
    qty    = TRANCHE // premium(expiry, strike)
    buy_vix_calls(expiry, strike, qty)

def monitor(position):
    m = position.mark / position.cost
    if m >= 3:  sell_fraction(position, 1/3)       # scale out into the spike
    if m >= 5:  sell_fraction(position, 1/2)       # of remainder
    if m >= 8:  sell_all(position)
    if position.days_to_expiry <= 5 and m < 1:
        let_expire(position)                       # bleed is the insurance cost
    redeploy_gains_into_equities()                 # the rebalancing step that makes it work
```

## Payoff & Greeks

### Payoff sketch (long VIX call, single leg)

```
P/L
  ^
  |                                    /
  |                                  /
  |                                /
  |                              /
0 +----------------------+----/----------------> VIX futures at expiry
  |                      | K /  (strike, e.g. 25)
  |______________________|_/
  -premium                        breakeven = K + premium
```

The payoff is the canonical long-call hockey stick, but with two VIX-specific distortions: (1) the x-axis is the **VIX futures** price at settlement (via the [[vix-futures|SOQ]]), not spot [[vix|VIX]], so a call looks further OTM than spot suggests when the curve is in [[contango]]; and (2) the realized profit window is short because volatility mean-reverts, so the holder rarely captures the theoretical peak intrinsic value.

### Net-Greeks table (long VIX call, low-vol entry)

| Greek | Sign | Magnitude | Trading meaning |
|---|---|---|---|
| Delta (vs VIX future) | + | 0.20-0.45 for a 1-3pt OTM call | Position gains as the relevant VIX future rises; delta accelerates into a spike |
| Gamma | + | High near the strike; rises into a spike | Convexity engine — delta ramps up fast, the source of 5-10x payoffs |
| Theta | − | Persistent daily bleed | The insurance cost; the reason base-case P/L is negative every calm year |
| Vega (vol-of-vol) | + | Material; the option is long [[vvix\|vol-of-vol]] | Gains when VVIX (the IV of VIX options) rises, even before VIX moves much |
| Rho | ~0 | Negligible | Short tenor and small notional make rate sensitivity immaterial |

Net exposure: **long convexity (long gamma + long vega), short theta.** This is the mirror image of the variance seller, who is short gamma/vega and long theta. See [[long-vol-vs-short-vol]] for the framework and [[long-vol-overlay]] for how the net Greeks combine with a short-vol core.

## Indicators / data used

- Spot VIX level and the **VIX futures term structure** (contango/backwardation, front- vs back-month spread)
- VIX options chain (strikes, expirations, premiums, implied vol-of-vol)
- S&P 500 level for portfolio-loss offset estimation
- Event calendar (elections, FOMC, fiscal deadlines) for catalyst-timed tranches
- Note: VIX options expire Wednesdays and settle to a special opening quotation (SOQ), not the prior close

## Example trade

A trader manages a $500,000 equity portfolio and budgets 2% ($10,000) per year for VIX call hedging. In January, with VIX at 14 and April VIX futures at 17:

- **Buy**: 20 April VIX $25 calls at $1.20 each ($2,400 total)
- These calls need VIX futures to rise above $26.20 at April expiration to profit

**Scenario 1 -- Market remains calm**: VIX stays around 14-16. The calls expire worthless. Loss: $2,400. The trader buys a new batch for the next quarter.

**Scenario 2 -- Market correction in March**: The S&P 500 drops 12%. VIX spikes from 14 to 38. April VIX futures surge to 34. The VIX $25 calls are now worth approximately $10.00 each. The trader sells for $20,000, an 8.3x return on the $2,400 investment. This $17,600 profit offsets roughly 30% of the portfolio's $60,000 equity loss.

**Scenario 3 -- Flash crash**: VIX spikes to 60 for two days. The calls briefly trade at $35+ each. If the trader acts quickly, the $2,400 investment returns $70,000 -- more than covering the portfolio's equity losses.

## Performance characteristics

- **Base case (most years)**: the hedge loses 50-100% of its annual budget -- i.e., a 1-3% drag on portfolio return. This matches the frontmatter `expected_max_drawdown: 0.03` (full loss of a 3% budget) and the negative standalone Sharpe.
- **Crisis years**: payoffs of 5-10x deployed premium are realistic for OTM calls bought in low-vol regimes and sold into the spike (March 2020, Q4 2008); poorly timed monetization can cut this in half because spikes retrace within days.
- **Cost overlay**: VIX option markets are liquid but spreads on OTM wings run $0.05-$0.10 on a ~$1.00-1.50 premium -- roughly 4-8% of premium per side. Add 4-12 rolls per year and total friction consumes on the order of 10-20% of the annual budget; the frontmatter `breakeven_cost_bps: 200` (2% of premium notional round-trip per leg beyond which edge erodes materially) reflects this tolerance. The convex payoff profile means the strategy survives wide spreads that would kill a fine-edged strategy.
- **Portfolio level**: studies of VIX hedging (Szado 2009, on the 2008 crisis) found that small (~3%) allocations to VIX calls or futures meaningfully cut portfolio drawdown and improved risk-adjusted returns *across the crisis window* -- while long bull markets see the hedged portfolio lag an unhedged one by roughly the bleed.

### VIX calls vs alternative tail hedges

| Hedge | Convexity | Carry cost | Upside cap | Main weakness |
|---|---|---|---|---|
| **VIX calls** (this page) | Very high | High | None | Mean-reversion; SOQ settlement; monetization timing |
| [[vix-call-spreads\|VIX call spreads]] | High | Lower (short call funds it) | Capped at strike width | Saturates in extreme spikes (VIX 50+) |
| [[protective-puts\|SPX/SPY puts]] | High | High | None | Slower to fire than VIX; path-dependent |
| [[long-vol-overlay\|Long-vol overlay]] | High (blended) | 2-3.5%/yr | Partial | Requires monetization discipline; not stand-alone |
| Short-VIX-futures (inverse) | Negative | Positive carry | n/a | Blows up in a spike ([[volmageddon\|Volmageddon]]) — the opposite trade |

VIX calls offer the most uncapped convexity of the listed-options hedges, which is why they pay the most in a true tail event but also bleed the hardest in calm regimes. The [[vix-call-spreads]] variant trades some of that uncapped upside for a materially lower carry cost.

## Capacity limits

VIX options are among the most liquid volatility instruments in the world, with daily volumes routinely in the hundreds of thousands of contracts. A systematic program spending up to a few hundred million dollars of annual premium (frontmatter: $500M) can execute without materially moving the vol-of-vol surface; famous large buyers (e.g., the "50 Cent" buyer of 2017, widely attributed to Ruffer LLP, who bought ~$0.50 VIX calls in enormous size) operated at this scale visibly but executably. Beyond that, persistent bid pressure on OTM VIX wings steepens the call skew against the buyer, raising the bleed -- market impact shows up as worse pricing rather than failed fills. Retail and mid-size institutional users face no practical capacity constraint.

## What kills this strategy

- **Monetization failure**: holding through the spike. VIX mean-reverts within days; a hedger who waits for SOQ settlement frequently watches an 8x mark round-trip to zero. This is the single most common failure mode.
- **Buying high**: initiating or up-sizing hedges after volatility has already exploded (backwardation), locking in expensive protection right before mean reversion.
- **Budget creep**: letting the bleed exceed 3-4%/yr of the portfolio, which compounds into more damage than the drawdowns it insures against.
- **Regime of grinding losses without vol spikes**: slow bear markets (e.g., much of 2000-2002) can produce significant equity losses while VIX stays only moderately elevated -- equity drawdown with little hedge payoff.
- **Structural change in the VIX complex**: changes to SOQ settlement mechanics, ETP flows, or persistent flattening of contango altering the priced-in spike premium.

## Kill criteria

- Rolling **3-year** hedge bleed exceeds **4%/yr** of total portfolio value → halve the budget or stop.
- In any S&P 500 drawdown deeper than **15%**, the hedge pays out **less than 2x** the trailing 12 months of premium spent → the chosen strikes/expiries are not delivering convexity; redesign or retire.
- VIX futures curve in backwardation for **more than 6 consecutive months** → suspend systematic buying until contango resumes.

## Advantages

- **Convex payoff**: Small cost in normal markets, potentially massive returns during crises
- **Negative correlation with equities**: Provides genuine diversification when it matters most
- **Liquid market**: VIX options trade with tight spreads and high volume
- **Defined risk**: Maximum loss is the premium paid
- **Portfolio-level hedge**: One position can hedge an entire equity portfolio, unlike single-stock puts

## Disadvantages

- **Persistent cost**: Most of the time, VIX calls expire worthless, creating a steady drag on returns (negative standalone expected value)
- **Pricing off futures, not spot**: Contango means the strike price is misleading relative to spot VIX
- **Mean reversion**: VIX spikes are short-lived; slow to react and the opportunity passes
- **Complexity**: Understanding VIX options pricing, term structure, and settlement requires advanced knowledge
- **Roll cost**: Maintaining continuous protection requires periodic rolling, each cycle resetting the premium cost
- **Settlement quirk**: VIX options settle based on a special opening quotation (SOQ) that can differ significantly from the prior day's closing VIX level

## Sources

- CBOE, "The VIX Index and Volatility-Based Global Indexes and Trading Instruments" (VIX white paper) -- methodology and settlement mechanics.
- Szado, E. (2009). "VIX Futures and Options: A Case Study of Portfolio Diversification During the 2008 Financial Crisis." *Journal of Alternative Investments*, 12(2).
- CBOE VIX Tail Hedge Index (VXTH) methodology -- benchmark for systematic 30-delta VIX call overlay performance.
- Documented market events: VIX closing high 82.69 (16 Mar 2020) and 80.86 (20 Nov 2008); XIV ETN termination after ~95% one-day loss (5 Feb 2018, "Volmageddon"); the 2017 "50 Cent" VIX call buyer attributed to Ruffer LLP.

## Related

- [[vix]] -- the underlying index
- [[vix-futures]] -- the contracts VIX options actually price off
- [[vix-call-spreads]] -- the defined-cost, capped-upside variant of this strategy
- [[long-vol-overlay]] -- how a VIX call ladder blends with a short-vol core
- [[long-volatility-strategies]] -- the broader family of long-vol trades
- [[long-vol-vs-short-vol]] -- the conceptual frame (who is on each side)
- [[volatility-trading]] -- broader overview of vol strategies
- [[risk-management]] -- portfolio protection frameworks
- [[protective-puts]] -- an alternative hedging approach using equity puts
- [[implied-volatility]] -- the pricing input for VIX and VIX options
- [[vvix]] -- the vol-of-vol that drives VIX-option vega
- [[options]] -- the instruments used
- [[options-selection-framework]] -- the general strike/expiry funnel
- [[strike-selection]] -- choosing the OTM strike by delta
- [[variance-risk-premium]] -- the premium the hedger pays
- [[tail-risk-hedging]] -- the broader hedging discipline
- [[contango]] -- the term-structure headwind
- [[backwardation]] -- the regime signalling "do not buy the peak"
- [[volmageddon]] -- the 2018 short-vol blowup this trade is positioned for
- [[sharpe-ratio]] -- why the stand-alone sleeve has a negative Sharpe
- [[edge-taxonomy]] -- classification of where edges come from
