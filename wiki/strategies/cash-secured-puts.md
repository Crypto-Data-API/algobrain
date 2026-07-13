---
title: "Cash-Secured Puts"
type: strategy
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [options, derivatives, volatility, swing-trading]
strategy_type: technical
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Put buyers systematically overpay for downside insurance (the volatility risk premium); the cash-secured seller is paid to bear crash risk that hedgers are desperate to shed."
data_required: [options-chain, ohlcv-daily, iv-rank, earnings-calendar]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.35
breakeven_cost_bps: 20
aliases: ["Cash-Secured Puts", "Cash Secured Puts", "CSP", "Naked Put with Cash"]
related: ["[[options]]", "[[assignment]]", "[[covered-calls]]", "[[put-option]]", "[[theta-decay]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[wheel-strategy]]", "[[credit-spread]]", "[[edge-taxonomy]]"]
---

# Cash-Secured Puts

A cash-secured put is an [[options]] income strategy where the trader sells a [[put-option|put option]] while holding enough cash in the account to purchase the underlying shares if [[assignment|assigned]]. It is often described as "getting paid to place a limit buy order" -- the trader collects premium today in exchange for the obligation to buy shares at the strike price if the stock falls below that level. Maximum profit is the premium received (if the put expires worthless), and maximum loss is the strike price minus the premium received (if the stock goes to zero).

## Edge source

Per the [[edge-taxonomy]], cash-secured put selling draws on two edge categories:

- **Risk-bearing**: the put seller collects the volatility risk premium -- the persistent, well-documented gap between implied volatility and subsequently realized volatility in equity index and single-name options. The premium is compensation for bearing left-tail (crash) risk and for posting capital that may be conscripted into stock ownership at the worst moment.
- **Behavioral**: demand for puts is structurally inelastic. Institutions mandated to hedge, and retail investors who overweight recent crash memories, buy downside protection at prices above actuarial fair value, especially after volatility spikes.

## Why this edge exists

The other side of a cash-secured put is a put **buyer**, and most put buyers are not trying to win the trade in expectation:

1. **Portfolio hedgers** (pensions, funds with drawdown mandates, structured-product desks) must own downside protection regardless of price. They knowingly pay an insurance premium, the same way homeowners pay more than expected losses for fire insurance.
2. **Loss-averse retail investors** overpay for puts after selloffs (when IV is already elevated), driven by recency bias and prospect-theory loss aversion -- they keep "losing" because the protection is bought when it is most expensive.

Because this insurance demand never goes away, implied volatility has exceeded realized volatility in most months for decades, and systematic put-write benchmarks like the CBOE PUT index have captured the difference. The seller's edge is real but is explicitly payment for crash exposure: the strategy collects steadily and then takes large, clustered losses in fast selloffs.

## Null hypothesis

If puts were fairly priced (implied volatility = expected realized volatility, no risk premium), the premium collected would exactly offset expected assignment losses, and a cash-secured put program would earn only the risk-free rate on its cash collateral plus market beta on assigned shares -- i.e., it would match a blended T-bill/equity portfolio with no excess return. Under the null, the high win rate (~70-75% of 0.25-0.30 delta puts expiring worthless) is fully paid for by the rare large losses, and after commissions and bid-ask spread the program underperforms a simple buy-and-hold equivalent. Any claimed edge must show up as *risk-adjusted* outperformance versus that blended benchmark, not as a high win rate alone.

## Rules

### Entry
1. Only sell puts on underlyings you genuinely want to own at the strike price. Selling puts on stocks you would not hold turns an income strategy into unwanted position acquisition -- this is the most common retail mistake.
2. Target **30-45 DTE** for optimal [[theta-decay|theta]] capture.
3. Sell strikes around the **0.25-0.30 delta** level (roughly 70-75% probability of expiring OTM), typically below visible support.
4. Prefer elevated [[implied-volatility]] (e.g., IV rank > 30-50) so the premium collected is rich relative to history; the underlying should have strong fundamentals if assignment is acceptable.
5. Hold the full cash collateral (strike × 100 per contract) -- the position is only "cash-secured" if the cash is actually reserved.

### Exit
6. **Profit target**: close when 50% of the maximum profit has been captured. For a $1.50 credit put, buy it back at $0.75. This locks in the majority of the profit while freeing capital and eliminating late-cycle [[gamma-risk]]. (Source: [[recovering-losing-options-positions]])
7. **The 21-DTE rule**: mechanically close or roll at approximately **21 DTE**, even when profitable -- see Rolling and Adjustments below. (Source: [[recovering-losing-options-positions]])
8. **Assignment**: accept assignment when it matches the original thesis (see "When to Take Assignment").

### Position sizing
9. Total potential assignment value across all short puts must not exceed the cash you are willing to deploy into stock; a common cap is 50% of account equity in aggregate short-put notional, with no single underlying above 10%.
10. Treat each contract as a commitment to buy $strike × 100 of stock -- size by that notional, not by the premium.

## Implementation pseudocode

```python
# systematic cash-secured put program
for symbol in watchlist:                      # stocks you WANT to own
    if not fundamentals_ok(symbol):           continue
    if iv_rank(symbol, 252) < 30:             continue   # premium too thin
    if earnings_within(symbol, days=45):      flag_or_skip(symbol)

    chain  = get_option_chain(symbol)
    expiry = chain.expiry(closest_to_dte=38)            # 30-45 DTE window
    put    = expiry.put(closest_to_delta=-0.27)         # 0.25-0.30 delta

    notional = put.strike * 100
    if cash_reserved + notional > 0.50 * equity:  continue   # aggregate cap
    if notional > 0.10 * equity:                  continue   # single-name cap

    sell(put); reserve_cash(notional)

# daily management
for pos in open_puts:
    if pos.value <= 0.50 * pos.credit:        close(pos)     # 50% profit target
    elif dte(pos) <= 21:
        if thesis_intact(pos.symbol):         roll_out(pos, dte=38, prefer_credit=True)
        else:                                 close(pos)     # take the loss
    elif deep_itm(pos) and roll_credit_impossible(pos):
        take_assignment_or_convert_to_spread(pos)            # buy lower put = bull put spread
```

## Indicators / data used

- **Options chain** with greeks (delta for strike selection, theta, gamma)
- **IV rank / IV percentile** (252-day lookback) -- entry filter for premium richness
- **Earnings and dividend calendar** -- early [[assignment]] risk rises near ex-dividend dates; earnings gaps blow through strikes
- **Daily OHLCV** and support levels of the underlying
- **Fundamentals** of the underlying (the trader must be willing to own it)
- Account-level cash and reserved-collateral tracking

## Payoff & Greeks

A cash-secured put is a single short put: capped gain (the premium), and a loss profile identical to owning 100 shares below the strike (minus the premium). The payoff is the same as a [[covered-calls|covered call]] by put-call parity. Maximum profit is the credit if the put expires OTM; maximum loss is (strike − premium) × 100, realized only if the underlying goes to zero.

Short put, P&L vs underlying at expiry (strike K, breakeven B = K − premium):

```
   P&L
    |        ___________________________        <- max gain = premium
    |       /
    |      /
  0 +-----B-------- K --------- spot ----------  underlying at expiry
    |    /
    |   /   (assigned: long stock below K,
    |  /     loss = short-put loss)
    | /
    |/   <- max loss = (K - premium) x 100 (stock -> 0)
```

Net Greeks of one short cash-secured put:

| Greek | Sign | Behaviour |
|---|---|---|
| [[delta]] | **Positive** (e.g. +0.25 to +0.30 at the 0.25-0.30-delta entry) | Bullish-to-neutral; rises toward +1.0 (full long-stock equivalent) as the put goes deeper ITM |
| [[gamma]] | **Short** | The source of the "gamma trap" — gamma spikes in the final weeks, which is exactly why the 21-DTE rule exists ([[gamma-risk]]) |
| [[theta]] | **Positive** | The primary profit driver ([[theta-decay]]); the put loses value with each calm day, accruing to the seller |
| [[vega]] | **Short** | An [[implied-volatility]] spike marks the short put against the seller — losses cluster precisely when IV explodes in a selloff |

The seller is **long delta, short gamma, short vega, long theta**: a directional-bullish short-vol position. This is the single-leg, conservative end of the same [[volatility-risk-premium|VRP]]-harvesting spectrum as [[premium-selling-systematic|systematic premium selling]] and the short-vol variants of [[volatility-trading]] — the cash collateral simply removes the leverage that turns the structure into account-destroying naked short puts in a [[volmageddon]]-style event.

## How it works

The trader identifies a stock they would be willing to own at a lower price, then sells an out-of-the-money put at or near that target purchase price. For example, if a stock trades at $50 and the trader would buy at $45, they sell the $45 put for $1.50. If the stock stays above $45 at expiration, the trader keeps the $1.50 premium. If the stock falls below $45, the trader is assigned and buys 100 shares at $45, with an effective cost basis of $43.50 ($45 strike minus $1.50 premium). The cash to cover the purchase ($4,500 per contract) must be held in the account, hence "cash-secured."

Cash-secured puts are fundamentally an income strategy that benefits from [[theta-decay|time decay]] and stable or rising underlying prices. The strategy is functionally equivalent to a [[covered-calls|covered call]] from a risk/reward perspective (both have the same payoff diagram as a short put, by put-call parity). The key advantage over simply placing a limit buy order is that the trader collects premium while waiting. If the stock never reaches the target price, the trader earns income from repeated put sales. If assigned, the trader acquires shares at a discount to the market price at the time the put was sold.

## The "Wheel" strategy

Cash-secured puts are often combined with [[covered-calls|covered calls]] in a rotation known as the [[wheel-strategy|"wheel" strategy]]. The trader sells puts until assigned, then sells covered calls against the acquired shares until called away, then returns to selling puts. This creates a continuous income cycle. The wheel works best on high-quality stocks with moderate volatility in a range-bound or gently rising market.

## Rolling and adjustments

Cash-secured puts are frequently rolled rather than held to expiration or assigned. Rolling is the primary adjustment technique and is often the difference between a profitable CSP program and an account full of underwater stock positions. See [[trade-repair-and-rolling]] for the complete adjustment framework.

### Rolling down and out (defensive roll)

When the stock drops toward or below the short put strike, the trader can roll to avoid assignment and reduce the breakeven:

**Example**: Sold $45 put for $1.50, stock drops to $43.
1. Buy back the $45 put for $3.50 (realizes a $2.00 loss on this leg)
2. Sell a $42 put 45 days out for $3.00
3. Net: paid $0.50 debit on the roll, but lowered the strike from $45 to $42

The new $42 put must be evaluated as a *fresh trade* -- does the thesis still hold at this price? Is the stock one you'd still want to own at $42? If the fundamental thesis is broken, take the loss instead of rolling. (Source: [[recovering-losing-options-positions]])

**Key rule**: Aim to roll for a net credit whenever possible. A net credit means you collect additional premium that lowers your overall breakeven. Rolling for a debit adds risk to an already losing position -- only do this when the strike reduction is substantial enough to justify the cost.

### The 21-DTE rule

Many professional put sellers mechanically close or roll at approximately **21 DTE**, even when the position is profitable. At this point [[theta-decay|theta]] decay accelerates but [[gamma-risk|gamma risk]] spikes -- the "gamma trap." A put that is 3% OTM at 21 DTE can be tested and deep ITM within a single session at 7 DTE, with gamma amplifying the delta shift on every tick down. Rolling at 21 DTE captures roughly 60-70% of the available theta while avoiding the zone where gamma dominates. (Source: [[recovering-losing-options-positions]])

### When to take assignment

Assignment is the expected outcome in certain scenarios and should not always be avoided:
- The stock has reached a price you genuinely want to own it at (your original thesis)
- The cost of rolling exceeds the benefit -- rolling a deep ITM put for a credit is often impossible
- You are running the [[wheel-strategy|wheel]] and assignment is the planned transition to selling [[covered-calls]]
- The stock has strong support at or near the strike and you expect a rebound

### Converting to a spread

If the stock drops significantly and the short put is deep ITM, the trader can convert the position to a [[credit-spread|bull put spread]] by buying a further OTM put below the short strike. This caps the maximum loss at the spread width minus net credit, preventing catastrophic loss if the stock continues declining. The cost is the premium paid for the long put. (Source: [[recovering-losing-options-positions]])

## Example trade

Stock XYZ trades at $50 on day 0. The trader is willing to own it at $45.

- **Sell**: 1 XYZ $45 put, 38 DTE, delta ≈ -0.27, for **$1.50** ($150 credit); reserve $4,500 cash
- **Day 20** (18 DTE): XYZ at $51, the put trades at $0.70 -- the 50% profit target ($0.75) has been hit and the 21-DTE rule is triggered. Buy to close at $0.70.
- **Result**: +$80 per contract in 20 days on $4,500 collateral ≈ 1.8% (≈ 32% annualized on collateral), before ~$1.30 of commissions and roughly $5 of bid-ask spread cost.

**Adverse path**: XYZ gaps to $41 on bad news at 25 DTE. The put trades at $4.60. The trader either (a) takes assignment near expiry at an effective basis of $43.50 and begins selling covered calls (wheel), (b) rolls down-and-out to a $42 put if it can be done near even, or (c) buys a $38 put to convert to a defined-risk bull put spread.

## Performance characteristics

The strongest long-run evidence is the **CBOE S&P 500 PutWrite Index (PUT)**, which systematically sells one-month ATM SPX puts against T-bill collateral:

- The original CBOE/Ibbotson study reported PUT at about **10.3% annualized return with 9.9% volatility vs 8.8% return with 15.4% volatility for the S&P 500** (1986 onward); a later study through 2018-2019 showed **9.5% return / 10.0% vol for PUT vs 9.8% return / 14.9% vol for the S&P 500** -- equity-like returns at roughly two-thirds the volatility, implying a Sharpe near 0.6-0.7.
- **Crash behavior**: in 2008 the PUT index drew down roughly **-33% vs about -51% for the S&P 500**. The strategy is *less* volatile than equities but still deeply exposed to crashes -- hence the frontmatter drawdown estimate of 0.35.
- (Verified via Perplexity (sonar), 2026-06-10: cxoadvisory.com PutWrite performance review; Cboe/Validus PutWrite paper 2023; CBOE/Ibbotson study.)

Practical overlays for a retail/single-name program:

- **Win rate** at 0.25-0.30 delta: ~70-75% of puts expire worthless or are closed at the profit target, but losers are several times larger than winners; the P&L distribution is strongly left-skewed.
- **Costs**: ~$0.65/contract commission each way plus typically $0.02-0.10 of bid-ask spread on liquid names ≈ $5-15 per round trip, small relative to a $150 credit (3-10%) but material for low-premium strikes. Single-name CSPs on illiquid chains can lose half the edge to spread crossing.
- **Cash drag**: returns on collateral depend heavily on the interest earned on the reserved cash; at 4-5% T-bill yields the collateral itself contributes a large share of total return, as it does in the PUT index.
- Single-name programs carry idiosyncratic gap risk the index benchmark does not show.

### Behaviour by market regime

CSP returns are strongly conditioned on the [[market-regime]]; the IV-rank entry filter is itself a partial regime gate:

| Regime | CSP result | Notes |
|---|---|---|
| Rising / range-bound, moderate IV | Best — puts expire worthless, premium banked | The strategy's home regime |
| Low, compressed IV (e.g. 2017) | Thin premium barely beats T-bills; crash risk persists | A kill-criterion regime (IV rank < 20) |
| Fast selloff / crash | Worst — whole book assigned near the highs while IV spikes | The signature clustered loss ([[volmageddon]], 2020) |
| Post-crash high-IV recovery | Re-widened premium; richest entries | Re-arm here if collateral discipline held |

Because the loss tail concentrates in the crash regime, a CSP book is the natural client for a long-vol overlay (spx-puts / [[put-tree]]) at the portfolio level — the same pairing that defines [[premium-selling-systematic|systematic premium selling]].

## Capacity limits

- **Index/ETF level** (SPX, SPY): effectively institutional-scale -- put-write funds run billions against SPX options, the deepest options market in the world. Capacity is not the binding constraint there; thinning premium (crowding) is.
- **Single-name level**: capacity is bounded by per-strike open interest and the trader's willingness to take assignment. A diversified 15-25 name CSP book can deploy roughly **$10-50M** of collateral before order sizes routinely exceed displayed depth at 0.25-delta strikes and rolls become expensive; the frontmatter uses $50M as the upper bound.
- **Crowding**: put-selling has been heavily popularized (wheel communities, premium-harvesting funds). Crowding compresses the volatility risk premium in calm regimes -- rated `medium` -- though the premium has historically re-widened after every volatility shock.

## What kills this strategy

- **Market crashes**: fast, deep selloffs (October 1987, autumn 2008, February 2018 "Volmageddon", March 2020) assign the entire book near the highs while IV explodes, producing the strategy's signature clustered losses. Premium collected over many months can be surrendered in weeks.
- **Single-name blowups**: earnings gaps, fraud revelations, or sector shocks send a stock far below the strike -- the put seller owns the full move below breakeven.
- **Broken-thesis rolling**: serially rolling a put on a deteriorating company converts a small loss into a large concentrated one; the strategy dies by a thousand defensive rolls.
- **Volatility regime compression**: extended low-IV periods (e.g., 2017) shrink premiums until the return on collateral barely beats T-bills, while crash risk remains.
- **Insufficient collateral discipline**: selling puts on margin rather than cash-secured transforms the strategy into naked short puts -- the historical account-destroyer in events like Volmageddon.
- **Early assignment** around ex-dividend dates on deep ITM puts, forcing unplanned stock purchases.

## Kill criteria

Retire or pause the program when any of the following triggers:

- Rolling 12-month total return (premium + assigned-stock P&L + collateral interest) underperforms a 50/50 T-bill/index benchmark by **more than 3 percentage points** over **≥ 30 closed trades**
- Peak-to-trough drawdown on allocated capital exceeds **35%**
- More than **30% of open positions** are simultaneously ITM (the book has become a falling-knife collection -- stop opening new puts)
- Average IV rank at entry across the last 20 trades falls below **20** (premium environment too thin; stand down until vol returns)
- Any single underlying exceeds **15% of account equity** after assignment and cannot be reduced within one covered-call cycle

## Advantages

- **High win rate**: ~70-75% of 0.25-0.30 delta puts expire worthless or hit profit targets
- **Paid to wait**: collects premium while targeting a purchase price you wanted anyway; if assigned, cost basis is below the market price at trade entry
- **Lower volatility than stock ownership**: documented by the PUT index (≈ two-thirds of S&P 500 volatility historically)
- **Collateral earns interest**: T-bill yield on reserved cash adds to returns
- **Defined process**: mechanical strike selection, profit targets, and the 21-DTE rule make it highly systematizable, and it feeds naturally into the [[wheel-strategy]]

## Disadvantages

- Full downside exposure below the strike (minus premium) -- not a protective strategy
- [[assignment]] can occur before expiration (American-style options), especially near ex-dividend dates
- Opportunity cost of holding cash as collateral rather than investing it
- In a sharp selloff, the trader is forced to buy at above-market prices
- **Capped upside**: profit is limited to the premium no matter how far the stock rallies
- **Left-skewed P&L**: many small wins punctuated by occasional large losses; psychologically and statistically easy to misjudge from a short track record

## Sources

- [[recovering-losing-options-positions]] -- rolling framework, 21-DTE rule, 50% profit target, spread conversion
- CBOE / Ibbotson Associates, studies of the CBOE S&P 500 PutWrite Index (PUT), 1986-2019 -- return, volatility, and drawdown statistics cited above
- Cboe/Validus, "PutWrite" performance summary (2023) -- 2008 drawdown comparison
- Verified via Perplexity (sonar), 2026-06-10: https://www.cxoadvisory.com/equity-options/performance-of-cboe-putwrite-indexes/ ; https://www.validusrm.com/wp-content/uploads/2023/11/Cboe-Validus-PutWrite_0323.pdf ; https://en.wikipedia.org/wiki/CBOE_S%26P_500_PutWrite_Index
- McMillan, Lawrence. *Options as a Strategic Investment* (5th ed., 2012) -- cash-secured put mechanics and management

## Related

- [[options]] -- options market overview
- [[covered-calls]] -- the mirror-image strategy (sell calls against long stock)
- [[wheel-strategy]] -- the full put-call income cycle (CSP → assignment → covered call → repeat)
- [[trade-repair-and-rolling]] -- complete rolling and adjustment framework
- [[gamma-risk]] -- the risk that drives the 21-DTE rule
- [[credit-spread]] -- converting a CSP to a defined-risk spread
- [[assignment]] -- when puts are exercised
- [[theta-decay]] -- the primary profit driver
- [[put-option]] -- put option mechanics
- [[edge-taxonomy]] -- the five edge categories referenced above
- [[volatility-risk-premium]] -- the premium the strategy harvests
- [[premium-selling-systematic]] -- the mechanical, multi-leg index version of the same edge
- [[volatility-trading]] -- the broader short-vol / long-vol family
- spx-puts, [[put-tree]] -- long-vol overlays that hedge a CSP book's crash tail
- [[market-regime]] -- the regime that drives the clustered-loss tail
- [[implied-volatility]] -- the entry-filter and vega-exposure driver
- [[theta]], [[delta]], [[vega]] -- the Greeks of a short put
