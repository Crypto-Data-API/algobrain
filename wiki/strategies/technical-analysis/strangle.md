---
title: "Strangle"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, volatility, derivatives, swing-trading, quantitative]
aliases: ["Strangle", "Long Strangle"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, risk-bearing, structural]
edge_mechanism: "Symmetric two-leg structure that isolates volatility from direction; the long variant pays for convexity ahead of expected vol expansion, the short variant collects the variance risk premium when the market overpays for that same convexity."
data_required: [options-chain, implied-volatility-surface, earnings-calendar, vix-term-structure]
min_capital_usd: 5000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.30
breakeven_cost_bps: 25
related: ["[[short-strangle]]", "[[long-straddle]]", "[[short-straddle]]", "[[straddle-strangle]]", "[[iron-condor]]", "[[iron-fly]]", "[[options-premium-selling]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[managing-winners]]", "[[implied-volatility]]", "[[probability-of-touch]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[gamma-explosion]]"]
---

# Strangle

A strangle is a two-leg [[options]] structure consisting of an [[out-of-the-money|OTM]] [[call-option|call]] and an OTM [[put-option|put]] at **different strikes** but the **same expiration**. It is the canonical pure-volatility play: the position has roughly zero net [[delta]] at entry but large [[vega]] and large [[gamma]] (long strangle) or large negative [[vega]] and short [[gamma]] (short strangle). Where a [[long-straddle|straddle]] uses two ATM options at the *same* strike, the strangle separates the two strikes to widen the structure -- cheaper to buy, lower premium to sell, but with a wider zone of either profit or loss depending on the direction of the trade.

This page is the **hub** for the strangle structure. It describes the construction generically, then compares the long and short variants, and links out to the dedicated [[short-strangle]] page for the income-trader's full treatment. Long strangles are covered in detail here.

## Overview

The strangle's defining feature is the **gap between the two strikes**. That gap creates a region of underlying prices over which both options are out-of-the-money. The long strangle owner *needs* the underlying to escape that region; the short strangle seller *needs* it to stay inside.

| Variant | Action | Greeks at entry | Bet |
|---|---|---|---|
| **Long strangle** | Buy OTM call + buy OTM put | +vega, +gamma, -theta | The market will move *more* than IV implies, in either direction |
| **Short strangle** | Sell OTM call + sell OTM put | -vega, -gamma, +theta | The market will move *less* than IV implies, in either direction |

Both variants share the same payoff *shape* -- a "V" for the long, an inverted "V" with a flat top for the short -- but flipped in sign. The choice between them is fundamentally a choice between paying for [[implied-volatility|implied volatility]] (long) or being paid for it (short).

## Edge source

Per [[edge-taxonomy]], the strangle's edge differs by variant:

- **Risk-bearing** (short variant, dominant) -- the short strangle seller is an insurer, collecting the [[variance-risk-premium]]: the persistent gap between [[implied-volatility|implied]] and subsequently realised volatility on liquid index products. The premium is compensation for bearing negatively skewed, gap-risk-laden P&L.
- **Behavioral** (both variants) -- option buyers systematically overpay for OTM optionality as crash insurance and lottery tickets (the short seller's edge), while the same crowd systematically *underprices* regime change at the bottom of vol cycles (the long buyer's edge). The long strangle's behavioral edge is conditional: it exists mainly when IV sits in the bottom decile of its range and the market extrapolates calm.
- **Structural** (both) -- hedging mandates and structured-product flows create persistent, price-insensitive demand for index puts (rich premium for sellers) and persistent suppression of vol via overwriting flows (cheap convexity for buyers in specific windows).

The long and short variants are *not* symmetric in expectancy: the unconditional long strangle pays the variance risk premium and loses on average; the unconditional short strangle collects it and wins on average but with fat left tails. Both can be positive-expectancy **conditionally** -- the long when bought in cheap-vol regimes ahead of catalysts, the short when sold into elevated IV.

## Why this edge exists

**For the short strangle**: the other side is the universe of hedgers, structured-product issuers, vol-targeting funds, and retail buyers of protection and lottery tickets. They are not stupid -- they are buying insurance, and insurance carries a premium over actuarial cost. The variance risk premium on SPX has been documented since at least Bakshi & Kapadia (2003) and persists because the buyers are utility-driven (they *want* the protection) rather than expectancy-driven. They "keep losing" in expectation the same way home-insurance buyers do: deliberately, in exchange for tail protection.

**For the long strangle**: the other side is the premium-selling crowd itself, plus overwriting programs that mechanically suppress IV in calm regimes. Late in a low-vol regime, the marginal seller is selling because theta income has worked for months, not because the price of convexity is fair. When IV sits in its bottom decile, the distribution of future IV is asymmetric -- it can fall one or two points or rise twenty. Sellers at that point are picking up pennies at the steamroller's narrowest clearance; the long strangle buys the steamroller's path. See [[vix-august-2024-spike]] and [[volmageddon]] for the two canonical recent payoffs to that asymmetry.

## Null hypothesis

If implied volatility exactly equalled subsequently realised volatility on average, both variants would have **zero expected P&L before costs and negative after costs** -- every strangle would be a fair coin flip minus the bid-ask spread on two legs, twice (entry and exit). Under the null:

- Short strangles would still *appear* to work most of the time (high win rate is a property of the payoff shape, not of edge) but the occasional full-loss tail would exactly cancel the accumulated credits.
- Long strangles would still occasionally print spectacular multi-bagger wins, but the steady theta bleed would exactly cancel them.

A backtest that shows an 80%+ win rate on short strangles is therefore **not evidence of edge by itself** -- the null predicts the same win rate. Evidence of edge is positive *expectancy* after realistic costs across regimes that include at least one vol shock. Conversely, a long-strangle program is only better than random if its conditional entries (cheap IV, pre-catalyst) capture moves the surface failed to price.

## Rules

### Construction

Strikes are typically chosen by [[delta]] rather than by absolute distance from spot, which makes the structure self-scaling across different underlyings and IV levels:

1. **Pick an expiration**. 30-60 [[time-to-expiration|DTE]] is the canonical window for short strangles (see [[options-premium-selling]] and [[theta-targeting]]); 60-180 DTE is more common for long strangles where the buyer needs time for the thesis to play out.
2. **Pick a delta**. The standard [[tastytrade]] / [[itpm-trading-philosophy|ITPM]] short-strangle convention is **16 [[delta|delta]] per side** (~1 standard-deviation strikes, ~84% [[probability-of-touch|probability]] each leg expires OTM in isolation, ~70% probability both do). Long strangles are often bought closer (25-40 delta per side) to keep the breakeven moves attainable.
3. **Sell or buy each leg** at the resulting strikes, on the same expiration cycle.
4. **Net premium** = (call price + put price). Paid as a debit for long; received as a credit for short.
5. **Breakevens at expiration** = upper strike + total premium (upside); lower strike − total premium (downside). The width between breakevens is wider than the structure's strike gap by exactly the premium paid or received.

A typical SPX 45-DTE 16-delta short strangle in a 16-VIX environment might sell the 5,425 call and 4,950 put for a combined ~$34 credit ($3,400/contract). The corresponding *long* strangle, bought at the same strikes, costs that same $3,400 -- but as a debit. The two are mirror images at the moment of entry.

### Long strangle entry

The long strangle is purchased when the trader expects a **larger move than IV implies**, with no strong directional view. Common contexts:

- **Pre-earnings** on single-name stocks, expecting the post-announcement move to exceed the IV-implied straddle price. (Note: this is a contested edge; the [[earnings-volatility]] surface usually prices earnings well, and the post-announcement [[earnings-iv-crush|IV crush]] punishes the long unless the move is genuinely large.)
- **Pre-event** for catalyst-driven setups -- FDA decisions, merger votes, central-bank meetings -- where the *direction* is unknown but a meaningful gap is likely.
- **Cheap-vol regimes** where [[implied-volatility|IV]] is in the bottom decile of its 252-day range, the [[vix-term-structure|VIX term structure]] is depressed, and the trader believes the next regime change is more likely to expand vol than compress it further. See [[vix-august-2024-spike]] for the canonical recent example -- a long strangle held through that event paid out 8-15x its cost depending on strikes and DTE.
- **Tail-risk hedge** for an otherwise-short-vol book -- a small allocation to [[long-vol-overlay|long strangles]] caps the [[volmageddon]]-style worst case.

Entry filter: only buy when IV percentile is **below 25** (252-day lookback) *or* a dated binary catalyst sits inside the expiration window and the implied move is demonstrably below the historical realised move for that catalyst class.

### Long strangle exit

- **Profit**: take off half at 100% gain on the debit; trail the remainder. After a vol spike, sell *into* the spike -- IV mean-reverts faster than price.
- **Time stop**: exit at **21 DTE** if the catalyst has not fired; theta acceleration past that point dominates the remaining optionality.
- **Loss**: hard stop at **−50% of the debit paid**. A long strangle that has lost half its value without the catalyst firing is a thesis failure, not a dip.

### Short strangle entry, exit, sizing

Treated in full on the dedicated [[short-strangle]] page; the canonical setup (per [[options-premium-selling]] and [[theta-targeting]]): 45 DTE, 16-delta short strikes on SPX/SPY/RUT/QQQ, entered when IV Rank > 30, managed at **50% of max profit**, closed at **21 DTE** regardless. See [[managing-winners]].

### Position sizing

- **Long**: total debit at risk per trade capped at **1% of NAV**; aggregate long-premium budget (the annual "vol-buying budget") capped at 3-5% of NAV per year.
- **Short**: undefined-risk -- size by stress-test, not by margin. A 2x-credit stop and a book-level rule that a 3-standard-deviation overnight move costs < 5% of NAV. Requires [[portfolio-margin]] for efficient sizing; T-Reg margin makes the structure capital-inefficient.

### When to use each

| Condition | Long strangle | Short strangle |
|---|---|---|
| IV is *low* (bottom 25% of 252-day range) | Favour | Avoid -- premium too thin |
| IV is *high* (top 25% of range) | Avoid -- paying full price | Favour -- rich premium, often crushes |
| A binary catalyst is approaching | Favour, *only if* IV is not already richly priced | Avoid until after the event |
| You have no directional view | Either, depending on IV regime | Favour if the underlying is range-bound |
| Account is undersized for undefined risk | Long only | Use [[iron-condor]] instead |
| You need positive carry to fund a hedge | -- | Favour as core, paired with [[long-vol-overlay]] |
| Earnings on a single-name stock | Avoid (IV crush usually dominates) | Avoid (single-name gap risk) |
| [[vix-august-2024-spike|Vol shock just printed]] | Favour *after* the spike for the next leg | Favour *gradually*, into the post-shock IV decay |

The deeper rule: *long and short strangles are not opposites in trader-time, they are opposites in regime-time*. The long strangle is the trade for a regime that has not yet expanded; the short strangle is the trade for a regime that has expanded *and is now reverting*. Holding them simultaneously on the same expiration cancels the position; holding them across different DTE ladders is the foundation of [[expiration-laddering|term-structure]] trades like [[calendar-spread|calendars]] and [[diagonal-spread|diagonals]].

## Implementation pseudocode

```python
def open_strangle(market, underlying="SPX", variant="long"):
    iv_pctile = market.iv_percentile(underlying, lookback_days=252)
    chain = market.options_chain(underlying)

    if variant == "long":
        # Buy convexity only when it is cheap or a catalyst is mispriced
        if iv_pctile > 25 and not mispriced_catalyst_in_window(underlying):
            return None
        dte = pick_expiry(chain, target=90, range=(60, 180))   # time for thesis
        call = chain.strike_by_delta(dte, +0.30)               # 25-40 delta legs
        put  = chain.strike_by_delta(dte, -0.30)
        debit = call.ask + put.ask
        if debit > 0.01 * account.nav():                       # 1% NAV cap
            return None
        return buy(call), buy(put)

    else:  # short -- see [[short-strangle]] for full management
        if market.iv_rank(underlying) < 30:
            return None                                        # the theta trap
        dte = pick_expiry(chain, target=45, range=(30, 60))
        call = chain.strike_by_delta(dte, +0.16)               # ~1-sigma strikes
        put  = chain.strike_by_delta(dte, -0.16)
        if stress_loss_3_sigma(call, put) > 0.05 * account.nav():
            return None
        return sell(call), sell(put)

def manage(position):
    if position.variant == "long":
        if position.pnl_pct >= +1.00: scale_out(position, 0.5)  # take half at 2x
        if position.pnl_pct <= -0.50: close(position)           # thesis failed
        if position.dte <= 21 and not position.catalyst_fired:
            close(position)                                     # time stop
    else:
        if position.pnl_pct_of_max >= 0.50: close(position)     # 50% of max profit
        if position.loss >= 2 * position.credit: close(position)
        if position.dte <= 21: close(position)                  # gamma window
```

## Indicators / data used

- **Options chain with Greeks** -- strikes selected by delta, not price distance.
- **[[implied-volatility|IV]] percentile / IV Rank** (252-day) -- the primary regime filter for both variants.
- **[[vix-term-structure|VIX term structure]]** -- contango/backwardation state; backwardation generally vetoes new short strangles.
- **[[earnings-calendar|Earnings calendar]] and macro calendar** (FOMC, CPI, NFP) -- catalyst timing for longs, event-avoidance for shorts.
- **Implied vs. historical realised move** for the catalyst class -- the long buyer's mispricing test.
- **[[probability-of-touch|Probability of touch]]** -- roughly 2x the delta of the short strike; sizing input for shorts.

## Payoff diagram & Greeks profile

The strangle's two variants are exact reflections of each other through the zero-P&L axis. The **long strangle** is a "V" with a flat bottom — flat (the debit, fully lost) across the gap between the two strikes, then rising on both wings as the underlying escapes the zone. The **short strangle** is the inverted "V" with a flat top — a maximum profit (the credit) across the gap, then falling away on both sides without bound.

```
 Long strangle                Short strangle
 P&L                          P&L
  \                  /          ____________  <- max profit (credit)
   \                /          /            \
    \              /          /              \
 ____\____________/____      /                \____
     put K    call K        /  put K   call K   \
  (lose debit in the gap)   (lose without bound outside strikes)
```

| Feature | Long strangle | Short strangle |
|---|---|---|
| Entry | Pay debit (call + put) | Receive credit (call + put) |
| Max profit | Unlimited (up) / large (down) | The credit received |
| Max loss | The debit paid (defined) | **Undefined** both directions |
| Wins when | Underlying escapes the strike gap by more than the premium | Underlying stays inside the breakevens |
| Breakevens | Upper strike + premium; lower strike − premium | Same formula, but the *profit* zone |

### Greeks profile (mirror images)

| Greek | Long strangle | Short strangle |
|---|---|---|
| [[delta]] | ~0 at entry (rises with the move) | ~0 at entry (the bet is non-directional) |
| [[gamma]] | Positive — large moves accelerate gains | Negative — the [[gamma-explosion]] tail that kills it in a shock |
| [[theta]] | Negative — bleeds 0.5-2% of debit/day, accelerating into expiry | Positive — the income engine ([[theta-targeting]]) |
| [[vega]] | Positive — an IV expansion is the dominant early-payoff path | Negative — an IV spike marks the book down even before spot moves |

The two variants are **opposites in regime-time, not trader-time**: the long is the trade for a regime that has not yet expanded ([[implied-volatility|IV]] in its bottom decile, pre-catalyst); the short is the trade for a regime that *has* expanded and is now reverting (IV Rank > 30). The short variant harvests the same [[volatility-risk-premium]] as [[covered-calls]], the [[iron-condor]], and every other structure in [[options-income]]; the long variant *pays* it in exchange for convexity, exactly as the [[long-volatility-strategies|long-vol]] book does. The defined-risk version of the short strangle is the [[iron-condor]] — strongly preferred for undersized accounts that cannot bear undefined-risk margin. See [[options-portfolio-construction]] for sizing strangles inside a book.

## Example trade

**Pre-FOMC long strangle:**

- Underlying: SPX at 5,200, 7 DTE, VIX = 14.
- Buy 5,275 call for $9.00, buy 5,125 put for $8.00. Total debit = $17.00 / $1,700 per strangle.
- Breakevens at expiration: 5,292 (up) and 5,108 (down). The market needs to move ~1.7% in either direction by expiry to break even.
- FOMC delivers a hawkish surprise: SPX gaps to 5,140 next session; IV jumps from 14 to 18.
- Position marks at ~$24.00: the call is now near-worthless ($1.50), but the put is in-the-money and revalued at $22.50 with the higher IV. **+$700 / +41% in one day** despite not being deep enough in the money to fully cash in.

This is the typical long-strangle path: the **vega expansion** does most of the early P&L work, with directional [[gamma]] adding to it as the move continues. Had the FOMC been a non-event, the same position would have bled roughly $150-250/day of theta into the weekend -- which is why the time stop matters as much as the entry.

## Performance characteristics

### Greeks evolution (long)

- **+ Vega**: an IV expansion of 5 points can mark the position up by multiples of its theta debit per day. This is the dominant profit path in practice.
- **+ Gamma**: large directional moves are profitable on either side, with profit accelerating as the position moves further OTM.
- **− Theta**: the position bleeds daily, often 0.5-2% of the debit paid per day, accelerating into expiration. **Time is the enemy** of a long strangle -- if the move does not materialise, the position decays toward zero.

### Expectancy with realistic costs

- **Short strangle (index, 16-delta, 45 DTE, managed at 50% / 21 DTE)**: practitioner studies ([[tastytrade]]-style) report win rates in the 80-90% range with positive expectancy before costs; the unconditional [[variance-risk-premium]] on SPX supports a net Sharpe in the **0.3-0.6** range after slippage, with severe negative skew. A single 2018- or 2020-class shock can return 1-3 years of accumulated theta. These figures are directionally consistent with the VRP literature but are **not independently backtested for this wiki** (frontmatter `backtest_status: untested`).
- **Long strangle (unconditional)**: negative expectancy -- the buyer pays the same VRP the seller collects, plus two bid-ask spreads each way. On weekly single-name options the spread alone can be 5-10% of the debit per side.
- **Long strangle (conditional: bottom-decile IV, mispriced catalyst)**: positive skew with low win rate (~30-40% of entries profitable), where the winners (3-15x payoffs in vol shocks) must carry the bleed. The honest framing: this is a **payoff-shape trade**, not a high-Sharpe trade; its book-level value is largest as a hedge against a short-vol core.
- **Cost overlay**: the frontmatter `breakeven_cost_bps: 25` reflects round-trip friction on liquid index strangles (SPX/SPY); single names can run 3-5x that, which is usually fatal to the long variant's expectancy.

### Why long strangles often disappoint

Even when the trader is "right" that vol will expand, the long strangle has three persistent enemies:

1. **IV crush after the event** -- the same expansion that created the opportunity often reverses violently *the moment uncertainty resolves*. Buying a strangle the day before earnings and holding through the print is usually a losing trade because the post-print IV crush more than offsets the price move. See [[earnings-iv-crush]].
2. **Theta decay accelerates** as DTE shrinks. Short-dated long strangles must move *fast* to outrun the bleed.
3. **Bid-ask drag**. Long strangles are paying the spread on entry *and* exit; on weekly options this can be 5-10% of the debit each way.

The empirical reality is that long strangles work best when bought **early** (in cheap-vol regimes, well before the catalyst) and **off** (with the long-vol thesis already partly proven). Buying them at peak fear or right at the catalyst is usually overpaying.

### Short strangle profile (summary)

The short strangle sells the same two OTM options. It is the income-trader's instrument of choice and is treated in full on the dedicated [[short-strangle]] page:

- **Goal**: collect the [[variance-risk-premium]] -- the persistent gap between [[implied-volatility|IV]] and subsequently realised volatility on liquid index products.
- **Greeks**: short vega, short gamma, **long theta**. Bleeds on vol expansion and large moves; profits on theta decay and IV crush.
- **Capital**: undefined-risk -- requires [[portfolio-margin]] for efficient sizing; T-Reg margin makes the structure capital-inefficient.
- **Failure mode**: catastrophic in a [[gamma-explosion|gamma]] / vol shock. See [[volmageddon]] (Feb 2018, naked short vol blowup) and [[vix-august-2024-spike]] (the most recent textbook short-strangle drawdown).

The defined-risk version of the short strangle is the [[iron-condor]] (add long wings outside the short strikes); the ATM-strikes variant is the [[short-straddle]] (more premium, narrower profit zone, much higher gamma); the symmetric version with ATM short strikes plus wings is the [[iron-fly]].

## Capacity limits

Index strangles (SPX, SPY, QQQ, RUT) are among the deepest options markets in the world: SPX alone trades millions of contracts daily across the chain, and a 16-delta strangle program in the **low hundreds of millions of dollars of notional** can be worked without materially moving the surface -- hence `capacity_usd: 500000000` as a conservative frontmatter estimate for an index-only program. Constraints arrive earlier in practice:

- **Single names**: open interest at 16-delta strikes is often a few thousand contracts; programs beyond low single-digit $millions per name start paying material impact.
- **Crowding**: the short-vol trade itself is crowded (overwriting funds, 0DTE sellers, retail income traders); in stress, *everyone's* exit is the same doorway, so effective capacity in a shock is far below quiet-market capacity. This is why `crowding_risk: medium` rather than low despite the deep market.
- **Long strangles** have higher capacity in calm markets (buying from a willing seller crowd) but the *exit* into a vol spike is capacity-constrained -- spreads gap wide exactly when the long wants to monetise.

## What kills this strategy

**Structural failure modes:**

- **Gamma/vol shock (short variant)** -- the defining tail. A [[volmageddon]]- or [[vix-august-2024-spike]]-class event can run a naked short strangle through its strike with losses of many multiples of the credit. [[gamma-explosion]] is the mechanism: as spot approaches the short strike near expiry, delta swings violently and hedging losses compound.
- **Variance risk premium compression** -- if VRP stays thin (structurally lower IV due to overwriting-fund supply), the short variant's expectancy shrinks below its cost floor.
- **Regime persistence (long variant)** -- a multi-year low-vol grind (2013-2014, 2017) bleeds a systematic long-strangle program to death before any payoff arrives.

**Operator errors (the classic mistakes):**

- **Buying long strangles into earnings** without modelling the [[earnings-iv-crush|IV crush]]. The straddle implied move usually prices the announcement reasonably well; the long buyer needs a *bigger* move to win, not just a move.
- **Selling short strangles in a 12-VIX regime** to "buy theta" because the book is below target. This is the [[theta-targeting#The Theta Trap|theta trap]] -- the [[variance-risk-premium]] is thin to negative at extreme low-vol levels, and the next gamma shock will unwind years of harvested theta.
- **Ignoring earnings or events on single-name short strangles**. A pre-earnings short strangle that gaps through a strike can produce a loss many multiples of the credit collected.
- **Not laddering DTE**. Concentrating an entire short-strangle book in one expiration cycle is a single-point-of-failure for [[gamma-explosion|gamma]] near expiry.
- **Closing long strangles too late**. Time decay accelerates non-linearly into the last 21 days; if the catalyst has not produced the expected move, the time-correct exit is *before* the gamma curve turns vertical, not into it.
- **Treating the structure as directional**. The strangle is a vol bet first; if a directional view is the primary driver, a vertical [[debit-spread]] or [[credit-spread]] is more capital-efficient than paying for both wings.

## Kill criteria

**Per-position:**

- Long: close at **−50% of debit**, or at **21 DTE** with no catalyst fired, whichever comes first.
- Short: close at **2x credit received** loss, at **50% of max profit**, or at **21 DTE** -- whichever comes first.

**Program-level (retire the strategy):**

- Short-strangle program: drawdown exceeds **30% of allocated capital** (matches `expected_max_drawdown` with buffer), or rolling 12-month expectancy is negative across **> 50 trades**, or a single event loss exceeds **3 years of trailing theta income** (evidence the sizing model understates tail risk).
- Long-strangle program: cumulative bleed exceeds the pre-committed annual vol-buying budget (**3-5% of NAV**) with no offsetting payoff, or two consecutive vol shocks occur in which the program's positions failed to pay at least 3x (evidence of systematically wrong strike/DTE selection).
- Either: average realised round-trip cost exceeds **25 bps** of notional (the frontmatter breakeven), making the structural edge unharvestable at this account's execution quality.

## Advantages

- **Direction-agnostic** -- isolates the volatility view from the directional view; no need to call the move's sign.
- **Self-scaling construction** -- delta-based strike selection adapts automatically across underlyings and IV regimes.
- **Cheaper convexity than a straddle** (long) -- the OTM legs cost less per unit of vega than ATM options.
- **Higher win rate and wider profit zone than a straddle** (short) -- the strike gap gives the seller room to be wrong on direction.
- **Regime-complementary pair** -- the long and short variants together span the vol cycle, and a book can rotate between them as IV percentile moves through its range.
- **Deep, liquid market** at the index level; execution friction is among the lowest of any multi-leg options structure.

## Disadvantages

- **The long variant fights negative carry** -- theta bleed of 0.5-2% of the debit per day, plus double bid-ask costs, means most long strangles expire worthless or near it.
- **The short variant carries unbounded tail risk** -- undefined-risk margin requirements, gap risk through strikes, and a payoff profile that hides risk inside a high win rate.
- **Low standalone Sharpe** (~0.4 expected) -- both variants are payoff-shape trades more than expectancy machines; sizing discipline does most of the work.
- **Capital-inefficient without portfolio margin** (short variant) on Reg-T accounts.
- **Psychologically hard in both directions** -- the long bleeds daily and demands patience; the short prints small wins daily and demands the discipline to stay small.
- **Single-name application is mostly uneconomic** -- spreads and gap risk consume the edge outside liquid indices.

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg on the structural Greeks of strangles and their relationship to straddles.
- [[tastytrade]] -- the published research archive on 16-delta / 45-DTE / 50%-profit short strangles.
- [[itpm-trading-philosophy]] -- institutional treatment of the strangle inside a [[options-portfolio-construction|portfolio]] context.
- [[options-premium-selling]] -- the variance-risk-premium framework that justifies the short variant.
- Bakshi, G. & Kapadia, N. (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium", *Review of Financial Studies* -- the academic anchor for the variance risk premium that drives the short variant's expectancy.

## Related

- [[short-strangle]] -- the dedicated income-trader's page; full setup, management, and risk treatment.
- [[long-straddle]] -- ATM-strike long-vol equivalent; more premium, narrower breakevens, no strike gap.
- [[short-straddle]] -- ATM-strike short-vol equivalent; more credit, narrower zone.
- [[iron-condor]] -- defined-risk version of the short strangle (with bought wings).
- [[iron-fly]] -- defined-risk version of the short straddle.
- [[straddle-strangle]] -- generic comparison page.
- [[options-premium-selling]] / [[options-income]] -- the broader strategy classes the short strangle anchors.
- [[covered-call]] / [[cash-secured-put]] -- single-leg short-premium relatives.
- [[calendar-spread]] / [[diagonal-spread]] -- term-structure trades built from strangles across DTE ladders.
- [[long-volatility-strategies]] -- the class the long strangle belongs to.
- [[options-portfolio-construction]] -- sizing strangles inside a book.
- [[volatility-risk-premium]] -- the premium the short variant harvests.
- [[theta-targeting]] -- how short strangles are sized inside an income book.
- [[vega]] / [[vega-budgeting]] -- the IV-sensitivity Greek and the complementary risk constraint.
- [[managing-winners]] -- the 50%-of-max-profit and 21-DTE management rules.
- [[implied-volatility]] / [[probability-of-touch]] -- core concepts for sizing.
- [[volmageddon]] / [[vix-august-2024-spike]] -- the two recent regimes most punishing to short strangles.
- [[gamma-explosion]] -- the path-risk mechanism that kills naked short strangles in shocks.
