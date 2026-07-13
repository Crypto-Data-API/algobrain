---
title: "Zero DTE Options"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, derivatives, volatility, scalping, sp500, market-microstructure]
aliases: ["0DTE", "Zero DTE", "0-DTE", "Same-Day Expiration", "Daily Options"]
strategy_type: quantitative
timeframe: scalp
markets: [stocks, options]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, behavioral, structural]
edge_mechanism: "Selling extreme-decay short-dated optionality to a flow that is dominated by retail directional bets and dealer hedging demand; the seller is paid for absorbing concentrated gamma and pin risk over the final hours of an option's life."
data_required: [options-chain-tick, implied-volatility-surface, dealer-positioning, opex-calendar, intraday-vix]
min_capital_usd: 10000
capacity_usd: 500000000
crowding_risk: high
expected_sharpe: 0.3
expected_max_drawdown: 0.50
breakeven_cost_bps: 50
related: ["[[options-premium-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[iron-fly]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[gamma-explosion]]", "[[gamma-scalping]]", "[[managing-winners]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[dealer-gamma-positioning]]", "[[pin-risk]]", "[[implied-volatility]]", "[[cboe]]", "[[itpm-trading-philosophy]]"]
---

Zero-DTE (0DTE) options are options that expire **on the same trading day they are traded**. The 0DTE phenomenon refers specifically to the explosive growth in volume of these same-day-expiry contracts on broad index products -- principally SPX, SPY, QQQ, and increasingly NDX -- following [[cboe|Cboe's]] completion of SPX expirations across all five weekdays in 2022 (Tuesday and Thursday expiries added in April-May 2022, joining the Monday and Wednesday weeklys listed since 2016). By 2024-2025, 0DTE volume routinely accounted for **40-50% of total SPX options volume**, making the 0DTE tape its own distinct market microstructure with measurable feedback into the underlying. Selling 0DTE premium is the front-end of the [[options-premium-selling|premium-selling]] world: the highest theta-per-dollar available on the listed surface, paired with the highest [[gamma-explosion|gamma]] of any tradeable structure.

This page treats 0DTE as a strategy class -- predominantly the **short-premium** variant ([[iron-condor|condors]], [[iron-fly|flies]], credit spreads) since that is where the structural edge is hypothesised to live. Long-premium 0DTE is briefly discussed in *Common Mistakes*.

## Edge source

Mixed: **risk-bearing** (selling end-of-life optionality), **behavioral** (the buyer flow is heavily retail-directional), and **structural** (dealer hedging demand at expiration creates a persistent bid for short-dated gamma).

- **Risk-bearing** -- the 0DTE seller absorbs gamma in the most concentrated form available. Time-value evaporates within hours; if the underlying drifts in the wrong direction, the loss is fast and severe.
- **Behavioral** -- the buyer side of the 0DTE flow is dominated by retail traders making intraday directional bets on SPX/SPY. JPMorgan and Goldman flow notes (2023-2024) consistently show retail [[call-option|call]]-buying volume spiking around economic releases, with delta-hedging by dealers amplifying the underlying's moves.
- **Structural** -- structured-product hedgers and dealer market-makers must continuously rebalance gamma exposure into the close; this creates predictable demand for short-dated optionality on the expiration tape.

## Why this edge exists

The deeper cause of 0DTE's expansion is twofold. First, [[cboe]] gradually rolled out daily SPX expirations: Monday and Wednesday weeklys were listed in 2016, and the five-day week was completed with Tuesday and Thursday expirations in April-May 2022. Each expansion converted what had been a Friday-plus-a-few-weekdays product into a five-days-a-week product with the same notional but compressed time. Second, a generation of retail traders (the post-pandemic / [[robinhood|Robinhood]] cohort) embraced 0DTE as a low-capital, high-leverage way to express intraday views, replacing what had previously been a mix of futures day-trading and weekly options.

The result is a market where:

- Buy-side flow is 60-70% retail by contract count (per Cboe and OCC data through 2024).
- Sell-side flow is dominated by professional market-makers, systematic income desks, and a growing class of retail premium-sellers running automated rules-based strategies.
- Realised volatility on the 0DTE tape is **persistently above** the implied volatility priced into the morning open, in calm-vol regimes -- but the tail of large adverse moves is far worse than buy-and-hold realised vol would suggest.

The [[variance-risk-premium]] that the 0DTE seller harvests is structurally rich (the buyer is overpaying), but the [[gamma]] that must be absorbed to harvest it is also structurally large. The net edge is positive in calm regimes and decisively negative in shocks -- an asymmetry that makes 0DTE the textbook *high mean, fat-left-tail* trade.

## Null hypothesis

If 0DTE [[implied-volatility|IV]] correctly priced subsequent intraday realised volatility on average, selling 0DTE premium would earn **zero before costs** and **negative after costs**. The position would still have negative skew (from the gamma profile) but the long-run expectation would be flat. Empirical tests on SPX 0DTE since 2023 show positive expectancy at the open of about 0.3-0.6% per session before costs on credit spreads; cost-corrected, the edge ranges from 0.1% to slightly negative depending on slippage and the trader's discipline at the close.

## Rules

**Universe**: SPX (or its options-equivalent SPY), QQQ, RUT/IWM. Single-name 0DTE is mostly an event-day novelty; structural edge does not exist.

**Entry**:

- Open in the morning (typically 09:45-10:30 ET, after the opening volatility settles).
- Sell short-premium structures: 16-25 delta credit spreads, 10-30 point wide [[iron-condor|condors]] on SPX, or [[iron-fly|iron flies]] for very high theta and very high gamma.
- Avoid the day before and morning of major events (FOMC, CPI, NFP, earnings days for major index components).
- Skip days where the [[vix]] term-structure is steeply backwardated -- the 0DTE / overnight VIX ratio above 1.0 signals stress regime and 0DTE shorting is a much worse trade.

**Position sizing**:

- Per-trade max loss capped at **0.5-1% of NAV** (smaller than 30-45 DTE structures because the gamma path is more violent).
- Aggregate 0DTE exposure capped at a fraction of the [[options-premium-selling|core short-premium book's]] vega budget -- 0DTE adds little vega but enormous gamma, so it is sized against a separate gamma budget.
- Use [[portfolio-margin]] for capital efficiency; Reg-T margin makes the structure so capital-inefficient that the edge disappears.

**Exit**:

- Take profit at **50% of max profit** for spreads, **25% for iron flies** -- mechanical, fast.
- **Hard stop on credit spreads** at 1.5-2x credit collected; close, do not roll, do not "give it room".
- **Close all positions by 15:30 ET** unless the position is already so deep in profit that early exercise risk is negligible. The final 30 minutes of the day is the [[gamma-explosion|gamma]] singularity zone.
- **Never carry 0DTE positions through the close on the wrong side** -- assignment of an in-the-money short call or put on SPX is cash-settled, but on SPY/QQQ it is share-settled and can produce overnight gap exposure many multiples of the credit.

## Implementation pseudocode

```python
def daily_0dte_loop(book, market):
    # 0. Day filter
    if today_is_macro_event_day() or vix_term_structure_backwardated():
        return

    # 1. Wait for opening volatility to settle
    if market.minutes_since_open() < 30:
        return

    # 2. Open new position if book is under target gamma exposure
    if book.gamma_dollars_at_risk() < book.gamma_budget_0dte():
        spot = market.spot("SPX")
        expected_move = market.expected_move_today("SPX")  # ATM straddle / 100
        # Sell 16-delta credit spread on each side
        short_call = nearest_strike(spot + 1.2 * expected_move)
        short_put  = nearest_strike(spot - 1.2 * expected_move)
        wing_width = 25  # SPX points

        condor = build_iron_condor(
            underlying="SPX",
            short_call=short_call, long_call=short_call + wing_width,
            short_put=short_put,   long_put=short_put - wing_width,
            dte=0,
        )
        book.open(condor, size=size_by_max_loss(target_pct_nav=0.005))

    # 3. Manage open positions every minute
    for trade in book.open_trades_0dte():
        if trade.pct_max_profit_realized() >= 0.50:
            book.close(trade, reason="50pct_profit_target")
        elif trade.pnl <= -1.5 * trade.credit:
            book.close(trade, reason="1.5x_stop")
        elif market.time() >= "15:30":
            book.close(trade, reason="end_of_day_close")
```

## Indicators / data used

- Tick-level [[options-chain]] with greeks for 0DTE strikes (theta, gamma, vega, delta updated intraday).
- [[expected-move]] for the day (ATM straddle price, or 1-day VIX value × spot / 16).
- Intraday [[vix]] level and 1-day VIX (VIX1D) -- 1-day VIX above 30 is a strong "step aside" signal.
- [[dealer-gamma-positioning]] estimates from SpotGamma, Tier1Alpha, etc. -- short-dealer-gamma days have larger swings.
- Macro event calendar (FOMC, CPI, NFP, OPEX, quad-witching).
- [[volume-profile]] and order-flow tape for SPX/SPY.

## Payoff & Greeks

This page treats the **short-premium** 0DTE variant (credit spreads, [[iron-condor|condors]], [[iron-fly|flies]]). At same-day expiry the payoff diagram is identical in shape to the longer-dated [[iron-condor]] — a flat-topped tent capped by the wings — but every Greek is compressed into a single trading session, so the *path* is far more violent than the static diagram suggests.

### Payoff sketch (at the 0DTE close)

```
 P/L
  │        ┌──────────────────┐          ← max profit = net credit (full theta in hours)
  │       /                    \
 0│──────/──────────────────────\───────  spot →
  │     /                        \
  │____/                          \______ ← max loss = wing width − credit (realised in MINUTES)
       LP SP                  SC LC
   profit zone narrow ≈ ±1.0–1.3× the day's expected move
```

The structure is **delta-neutral at open, short [[vega]] (small — little time value left), and extreme negative [[gamma]]** — the highest gamma of any listed structure. The whole edge is the rich front-end [[theta]], collected against gamma so large that a 1% intraday move can move the position from near-max-profit to near-max-loss within minutes.

### Net-Greeks table (intraday 0DTE short condor / spread)

| Greek | Sign / magnitude | Intraday behaviour | Implication |
|-------|------------------|--------------------|-------------|
| [[theta]] | Positive, **very high per dollar** | Bulk accrues across the 6.5-hour session | The reason to be in the trade — highest theta velocity on the surface |
| [[gamma]] | Negative, **extreme** (largest near short strikes and into the close) | Explodes in the final 30-60 minutes — the singularity zone | A small adverse move flips P&L violently; the close-by-15:30 rule exists for this |
| [[delta]] | ≈ 0 at open | Whips to ±large as spot nears a short strike | Becomes a fast directional loser when tested |
| [[vega]] | Negative but **small** | Little time value to lose | 0DTE is gamma-dominant, not vega-dominant — budgeted against a separate gamma cap, not the [[vega-budgeting\|vega budget]] |

Because vega is negligible and gamma is enormous, 0DTE is the purest **short-gamma** expression available. It carries the same [[theta]]-positive / [[gamma]]-negative signature as the longer-dated [[iron-condor]] and [[short-strangle]], but with the theta/gamma trade-off of [[managing-winners]] compressed from weeks into a single afternoon — which is why the exit rules (50%-of-credit, hard stop, close-by-15:30) are non-negotiable rather than advisory. See [[gamma-explosion]] for the path-risk mechanism.

## Example trade

*Illustrative only -- not a recommendation. Numbers consistent with a 16-VIX SPX environment.*

- **Date**: 2026-04-15. SPX = 5,200. VIX = 16. VIX1D = 12. No scheduled events.
- **Time**: 10:00 ET. Expected move (from ATM straddle) = ~$26.
- **Trade**: SPX 0DTE iron condor, 1 contract:
  - Sell 5,235 call ($1.80), buy 5,260 call ($0.50). Net call-spread credit = $1.30.
  - Sell 5,165 put ($1.70), buy 5,140 put ($0.55). Net put-spread credit = $1.15.
  - Total credit: $2.45 per condor ($245).
  - Wing width: 25 points each side. Max loss: $25 − $2.45 = $22.55 = $2,255 per condor.
- **Greeks at entry**: theta ~$80/day (most of which accrues in 6.5 hours), vega ~−$8/IV pt, gamma extreme.
- **By 14:30 ET**: SPX has drifted to 5,205. Both spreads have decayed; condor marks at $1.20. Profit = $1.25 per condor ($125 = ~51% of credit). Close per 50% rule.
- **Realised P&L**: $125 per condor on $2,255 max risk = 5.5% return on risk in 4.5 hours.

The defining feature of the 0DTE example is **how fast it played out**. Compared to a 45-DTE condor producing similar P&L over 2-3 weeks, the 0DTE delivered the same percentage return in an afternoon -- *if* the market cooperated. The same speed cuts in the other direction: a 1% adverse move at 11:00 ET typically produces a 60-90% loss on credit spreads before the trader can react.

## Performance characteristics

- **Hit rate**: ~70-80% in calm regimes, dropping to 40-50% in elevated-vol regimes.
- **Win/loss ratio**: highly asymmetric; average winner ~50% of credit, average loser ~150% of credit (on credit spreads with stops). Profit factor 1.0-1.4 in mixed regimes.
- **Sharpe**: in-sample, before costs, 1.0-2.0; cost-corrected and stress-adjusted, **0.2-0.6**. The Sharpe is materially below the headline because [[gamma-explosion]] days produce the entire downside.
- **Best regime**: low VIX, no scheduled events, post-shock mean reversion, OPEX days with short dealer gamma stabilising the tape.
- **Worst regime**: vol-shock days, FOMC-surprise sessions, [[vix-august-2024-spike|vol expansion]] regimes. A single 4σ session can wipe out a year of 0DTE income.
- **Cost sensitivity**: 0DTE is the most cost-fragile of the premium-selling strategies. Every 5 bps of average spread crossing per round-trip costs roughly 1-2% on the credit collected. **Bid-ask discipline is non-negotiable.**

## Capacity limits

- SPX 0DTE: enormous capacity at the index level -- daily volume routinely exceeds 1M contracts. Single funds run 9-figure books on 0DTE without measurable price impact, and the strategy capacity is limited by NAV's gamma absorption rather than market depth.
- SPY 0DTE: nominally large but more retail-flow-sensitive; cross-spread is wider relative to credit. Practical fund-level cap is mid-9-figure NAV.
- The strategy's **structural** capacity is constrained by the buy-side flow: as more capital sells 0DTE premium, [[variance-risk-premium|VRP]] at the 0DTE tenor compresses. There is empirical evidence (JPMorgan flow notes, 2024) that VRP at the 0DTE tenor has compressed by roughly 30-40% from its 2023 peak as systematic premium-selling capital has scaled.

## What kills this strategy

The dominant failure modes (see [[failure-modes]] and [[gamma-explosion]]):

1. **Intraday vol shock** -- a single news event (geopolitical, central-bank, terror) that gaps SPX 1.5%+ during the session. The credit spread max loss is realised in minutes; the iron fly max loss is realised in seconds.
2. **OPEX gamma flip** -- on quad-witch and major OPEX days, dealer gamma positioning can flip from short to long across the session, producing characteristic pin-and-then-break behaviour that traps premium sellers on the wrong side.
3. **VIX1D / VIX inversion** -- when 1-day VIX prints above the 30-day VIX (backwardation), the 0DTE tape is in a stress regime and the structural edge inverts.
4. **Crowding** -- when too many retail and systematic 0DTE sellers run the same playbook, they all hit stops simultaneously, accelerating moves into a feedback loop. Goldman flow notes (2024) document this dynamic on multiple sessions during the [[vix-august-2024-spike]].
5. **Discretionary intervention** -- traders who deviate from the close-by-15:30 rule routinely take outsized losses by holding "almost-expiring" positions through the final gamma surge. See the parallel in [[ljm-preservation-and-growth]].
6. **Cost drift** -- broker commissions and SPX exchange fees on 4-leg round-trip can consume 30-50% of credit on small accounts; the strategy is uneconomic below $25K NAV in most retail brokerage setups.
7. **Regulatory action** -- the [[cftc|CFTC]] and [[sec|SEC]] have both signalled interest in 0DTE retail flow; future position limits or margin requirement changes could materially compress edge.

## Kill criteria

Mechanical retirement triggers (see [[when-to-retire-a-strategy]]):

- **Drawdown**: strategy-level drawdown exceeds 20% -> halve size; 30% -> halt new entries pending review.
- **Realised hit rate** below 50% on a rolling 50-trade window -> review entry filters and DTE selection.
- **Average winner / average loser ratio** falls below 0.4 (i.e., losers more than 2.5x winners) -> the gamma profile is too aggressive; widen wings or reduce size.
- **Round-trip cost** rises above 50 bps of credit -> review; above 80 bps -> retire on this product.
- **0DTE implied/realised ratio**: rolling 3-month average of the morning implied move divided by the realised intraday move falls below 1.0 -> the 0DTE-tenor VRP has eroded; pause and review.

## Advantages

- **Highest theta velocity** on the listed surface -- positions resolve in hours, freeing capital for redeployment.
- **No overnight risk** -- positions close before market close (per the rules), eliminating gap exposure that haunts 30-45 DTE books.
- **Capital-efficient** under [[portfolio-margin]]; small NAV can produce significant theta dollars per session.
- **High frequency of resolution** -- 250+ trading sessions per year, each a fresh trade, makes statistical convergence faster than longer-dated strategies.
- **Non-correlated** with overnight macro flow -- 0DTE P&L is essentially driven by intraday SPX path, decoupling it from longer-dated short-vol positions.

## Disadvantages

- **Highest [[gamma]]** of any common short-premium structure. A 1% adverse move can produce a max loss in minutes.
- **Cost-fragile** -- 4-leg round-trip on 0DTE eats 30-50% of credit; brokerage and exchange fees can dominate the edge.
- **Cognitive load** -- requires intraday monitoring; cannot be run set-and-forget. A trader managing 0DTE during the workday is the canonical failure mode.
- **Tail risk is unbounded in time** -- even with defined-risk spreads, a series of 5-6 max-loss days in a row (stress regime) can produce a 30-50% drawdown in weeks.
- **Crowded** -- the post-2023 expansion has attracted enormous systematic capital, compressing the structural edge.
- **Regulatory uncertainty** -- the CFTC and SEC have both opened reviews of 0DTE retail flow; future rule changes could meaningfully alter the playing field.
- **Behaviorally hostile** -- the strategy's high hit rate and fast resolution feel rewarding; this tempts size increases right before the inevitable shock day.

## Sources

- [[cboe]] research notes on the SPX daily-expirations rollout (Mon/Wed weeklys 2016; Tue/Thu added April-May 2022) and 0DTE volume share.
- [[occ|OCC]] options volume statistics, 2023-2025.
- JPMorgan equity-derivatives strategy notes (Marko Kolanovic and successors), 2023-2024, on retail 0DTE flow and dealer hedging feedback.
- Goldman Sachs equity derivatives flow reports (2023-2024), 0DTE volume by participant type; Asym500 / Rocky Fishman 0DTE volume research, 2023-2024.
- [[vix-august-2024-spike]] -- the most recent textbook 0DTE gamma shock.
- [[volmageddon]] -- the 2018 short-vol blowup; not a 0DTE event but the canonical failure mode for short-gamma flow.
- [[options-premium-selling]] -- the broader VRP context.
- [[itpm-trading-philosophy]] -- the institutional view on why 0DTE concentrates rather than diversifies risk.

## Related

- [[options-premium-selling]] -- the umbrella strategy class.
- [[short-strangle]] / [[strangle]] -- the longer-dated equivalent on the same VRP.
- [[iron-condor]] / [[iron-fly]] -- the structural building blocks used at 0DTE tenors.
- [[theta-targeting]] -- 0DTE is treated as the "front-end of the theta trap" in the targeting framework.
- [[vega-budgeting]] -- 0DTE is gamma-dominant, not vega-dominant; budgeted separately.
- [[gamma-explosion]] -- the path-risk mechanism that defines 0DTE outcomes.
- [[gamma-scalping]] / [[managing-winners]] -- the long-gamma counterparty strategy and the 50%-of-credit / end-of-day rules.
- [[dealer-gamma-positioning]] / [[pin-risk]] -- structural context and end-of-day exercise risk.
- [[volmageddon]] / [[vix-august-2024-spike]] -- the two recent regimes most punishing to short-gamma flow.
- [[long-call]] / [[long-put]] -- the long-premium counterparties that buy the convexity 0DTE sellers short.
- [[market-regime]] -- 0DTE edge is positive in calm regimes and inverts in vol shocks.
- [[theta]] / [[gamma]] / [[vega]] / [[delta]] -- the position's intraday Greek profile.
- [[implied-volatility]] -- the morning IV that sets the credit; VIX1D the key step-aside signal.
