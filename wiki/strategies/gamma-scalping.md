---
title: "Gamma Scalping"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, quantitative]
aliases: ["Gamma Scalping", "Gamma Trading", "Long Gamma Strategy", "Long Gamma Scalping", "Volatility Scalping"]
related: ["[[options]]", "[[delta-hedging]]", "[[implied-volatility]]", "[[volatility-trading]]", "[[theta-decay]]", "[[straddle]]", "[[strangle]]", "[[variance-swaps]]"]
strategy_type: quantitative
timeframe: intraday
markets: [stocks, options, futures]
complexity: advanced
backtest_status: untested
edge_source: [analytical, behavioral]
edge_mechanism: "Profits when realized volatility exceeds the implied volatility paid for the options; the counterparty is the systematic vol seller harvesting the variance risk premium, who underprices movement ahead of catalysts and regime shifts."
data_required: [options-chain, ohlcv-intraday, implied-volatility-surface]
min_capital_usd: 25000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.20
breakeven_cost_bps: 5
---

# Gamma Scalping

Gamma scalping is an [[options]] trading strategy in which a trader purchases a [[straddle]] or [[strangle]] (establishing a long gamma position) and then continuously [[delta-hedging|delta-hedges]] the resulting stock position to lock in profits from realized price movement. The strategy is profitable when the underlying asset's realized volatility exceeds the [[implied-volatility]] priced into the options at the time of purchase.

## Edge source

Per [[edge-taxonomy]], gamma scalping is primarily an **analytical** edge with a **behavioral** assist:

- **Analytical** — the trader must forecast realized volatility better than the options market's implied vol. Since index implied vol *usually* exceeds subsequent realized vol (the [[variance-risk-premium]] runs against the long-gamma trader), the edge only exists in selectively identified spots where IV underprices coming movement: pre-catalyst lulls, post-crash IV crush overshoots, or single names with persistent RV > IV.
- **Behavioral** — systematic premium sellers (covered-call funds, put-write ETFs, retail income traders) mechanically supply options regardless of upcoming event risk, periodically leaving IV too low into binary catalysts. The gamma scalper takes the other side of that flow.

## Why this edge exists

- **Who is on the other side**: yield-seeking option sellers — covered-call and put-write programs, short-vol ETPs, and retail "income" strategies — whose mandate is to sell premium continuously, not to forecast vol. Dealer desks short gamma from structured-product issuance also suppress IV in certain names and tenors.
- **Why they keep losing (when they do)**: mandate-driven sellers do not condition on catalysts; they sell the same delta-targeted options into an earnings week as into a quiet one. When positioning is crowded short-vol, realized moves get amplified (dealers hedging short gamma chase price), handing the long-gamma trader outsized scalps.
- **Why it isn't free money**: on average the variance risk premium pays the *seller* — long-dated, always-on long-gamma programs bleed. The edge exists only episodically, which is why selectivity (cheap IV vs. credible RV forecast) is the entire game.

## Null hypothesis

If implied volatility equals subsequent realized volatility, a continuously hedged long straddle has expected P&L of **exactly zero** before costs — gamma revenue (0.5 × Γ × S² × σ²_realized per unit time) exactly offsets theta bleed. After hedge transaction costs and the option's bid-ask spread, expected P&L is **negative**. Worse, the unconditional base rate is adverse: index IV has exceeded realized vol in roughly 80–85% of months historically, so a gamma scalper with no vol-forecasting skill should expect to lose the variance risk premium plus costs. Any claimed edge must show RV > entry IV on selected trades at a rate far above this hostile baseline.

## Payoff & Greeks

A gamma scalp is **long gamma, long vega, short theta** with delta managed back to zero. The full Greek profile of the canonical long ATM [[straddle]] before any hedging:

| Greek | Sign (long straddle) | What it means here | Managed how |
|-------|----------------------|--------------------|-------------|
| [[delta]] (Δ) | ≈ 0 at inception, drifts | The directional exposure the scalp loop continuously flattens | Trade underlying to re-flatten |
| [[gamma]] (Γ) | **positive** | The engine — convexity that lets you buy dips / sell rallies profitably | Decays as price leaves the strike; peaks ATM |
| [[theta]] (Θ) | **negative** | The rent paid per day for holding gamma | Accelerates near expiry; the cost the scalp must beat |
| [[vega]] (ν) | **positive** | Exposure to a rise in [[implied-volatility]] | A windfall if IV expands; a second loss source if IV crushes |
| Vanna / Volga | nonzero | Cross-sensitivities (Δ to vol, vega to vol) | Usually ignored at retail scale, material for desks |

The gamma–theta identity that governs the whole trade, in continuous time:

> dP&L ≈ 0.5 × Γ × S² × (σ²_realized − σ²_implied) × dt + ν × dσ_implied

The first term is the realized-vs-implied vol bet (positive when [[realized-volatility]] beats entry [[implied-volatility]]); the second is the mark-to-market vega P&L. Because Γ × S² × σ²_implied × dt **equals** the theta bleed under Black–Scholes, the position is structurally a wager that realized variance exceeds implied variance over the holding period — exactly the inverse of [[delta-hedging|short-vol delta hedging]] and the mirror image of harvesting the [[variance-risk-premium]].

**Why discrete hedging matters**: continuous hedging perfectly captures `0.5 × Γ × (ΔS)²`. Discrete hedging captures only the realized squared moves *at the hedge points*, introducing the Boyle–Emanuel (1980) hedging error whose standard deviation scales as ≈ 1/√N of premium for N hedges. Hedging too rarely misses gamma; hedging too often pays spread on noise. See [[delta-hedging#Hedging frequency tradeoff]].

## Hedge-band selection

The single most consequential implementation choice. Three canonical regimes:

| Method | Trigger | Pros | Cons |
|--------|---------|------|------|
| Fixed delta band | Re-hedge when |net Δ| > X | Cost-efficient; trades only when needed | Band must be re-tuned as Γ and vol change |
| Fixed time interval | Re-hedge every Δt (hourly, EOD) | Simple, predictable cost | Misses fast moves; over-trades quiet periods |
| Fixed price grid | Re-hedge every k × expected move | Captures swings symmetrically | Whipsaw if grid spacing mismatches realized chop |
| Whalley–Wilmott band | Band ∝ (cost / Γ)^(1/3) | Cost-optimal asymptotic rule | Requires live Γ and cost estimates |

Wider bands capture larger swings but risk giving accumulated delta back on a reversal; tighter bands monetize chop but pay more spread. The optimal band **widens with transaction costs and narrows with gamma** — the same asymptotic result that governs [[delta-hedging]] (Whalley–Wilmott; Zakamouline). Practically, scale the band to a fraction of the underlying's current expected daily move.

## Rules

**Entry**
- Buy a 20–45 DTE at-the-money [[straddle]] (or slightly OTM [[strangle]] for lower theta) only when forecast realized vol exceeds current ATM implied vol by a margin, e.g., RV forecast ≥ IV + 2 vol points, or IV is in the bottom quintile of its 1-year range with an identifiable catalyst inside the option's life.
- Position should be approximately delta-neutral at inception (ATM straddle starts near zero delta).

**Hedging (the scalp loop)**
- Define delta thresholds at which to re-hedge. Common approaches: fixed delta increments (e.g., every ±20 deltas per straddle lot), fixed time intervals, or fixed price intervals (e.g., every 0.5 × expected daily move).
- When the threshold is breached, trade shares or futures to flatten delta back to zero: **sell** shares after an up-move, **buy** shares after a down-move. Each hedge locks in a small realized profit from the price swing.
- Wider thresholds capture bigger swings but risk giving back accumulated delta on reversals; tighter thresholds capture chop but pay more in spread. Calibrate to current realized vol and the underlying's transaction costs.

**Exit**
- Close by 7–10 DTE: gamma concentrates at the strike and theta accelerates, making hedging erratic near expiry.
- Close early on an IV spike that puts the position at a vega windfall (e.g., IV up 5+ points) — selling the now-expensive options is usually better than continuing to scalp.
- Hard stop: close when cumulative theta paid exceeds a set fraction of premium (see Kill criteria).

**Position sizing**
- Risk the premium: size so that a total loss of the straddle premium costs ≤ 2% of capital per position; theta bleed across all open positions ≤ 0.15% of capital per day.

## Implementation pseudocode

```python
# Long-gamma scalp with delta-threshold hedging
DELTA_BAND = 20        # deltas per straddle lot before re-hedge
VOL_EDGE   = 0.02      # required RV forecast - IV to enter
MAX_THETA  = 0.0015    # max daily theta bleed as fraction of NAV

def maybe_enter(chain, rv_forecast):
    iv = chain.atm_iv(dte=30)
    if rv_forecast >= iv + VOL_EDGE and theta_budget_ok(MAX_THETA):
        pos = buy_straddle(chain, dte=30, lots=size_by_premium_risk())
        pos.hedge_shares = -pos.net_delta()   # ~0 at inception
        return pos
    return None

def on_tick(pos, spot):
    net_delta = pos.options_delta(spot) + pos.hedge_shares
    if abs(net_delta) > DELTA_BAND * pos.lots:
        trade_underlying(-net_delta)          # sell into rallies, buy dips
        pos.hedge_shares += -net_delta        # locks in the scalp

def maybe_exit(pos, chain):
    if pos.dte() <= 8:                        close_all(pos)   # gamma/theta endgame
    elif chain.atm_iv(pos.dte()) >= pos.entry_iv + 0.05:
        close_all(pos)                        # vega windfall - take it
    elif pos.theta_paid() > 0.60 * pos.premium and pos.scalp_pnl() < pos.theta_paid():
        close_all(pos)                        # bleeding without movement
```

## Indicators / data used

- **Options chain with live Greeks** — delta, gamma, theta, vega per strike/expiry; ATM IV by tenor
- **Implied volatility history** — IV rank/percentile over a 1-year window to identify "cheap" vol
- **Realized volatility estimators** — close-to-close, Parkinson, or Yang–Zhang over 10–30 days for the RV forecast; intraday RV for hedge-band calibration
- **Catalyst calendar** — earnings dates, FOMC, CPI, product events falling inside the option's life
- **Intraday underlying prices** — tick/1-minute bars to trigger threshold hedges
- **Cost model** — underlying spread and commission per hedge; options spread at entry/exit

## Example trade

A trader buys a 30-day at-the-money straddle on SPY at $500 with implied volatility at 15%. Using the standard ATM approximation (0.8 × S × σ × √T), the straddle costs about $17.20 per share (≈ $8.60 each for the call and put), with initial theta of roughly $0.29 per day and straddle gamma of about 3.7 shares per $1 move per contract.

On Day 1, SPY rises $3.00 to $503. Delta accumulates to approximately +11 shares; the trader sells 11 shares at $503 to re-flatten. On Day 2, SPY drops $4.00 to $499. Delta swings to approximately −15 from the new neutral; the trader buys 15 shares at $499. The net stock trading has generated a small profit from systematically buying low and selling high, funded by the options' gamma. If realized vol over the life of the trade averages 18% versus the 15% implied at entry, cumulative gamma scalps (proportional to 18² = 324) exceed the theta paid (priced off 15² = 225) by roughly 40% of carry — turning the $17.20 premium outlay into a net profit of a few dollars per share before costs.

## Performance characteristics

The fundamental P&L equation for a gamma scalp over a single day is approximately:

> Daily P&L = 0.5 × Gamma × (Realized Move)² − Theta

The strategy makes money when the squared realized move is large enough to offset the daily theta bleed. A straddle priced at 25% implied vol on a $100 stock implies roughly a $1.58 daily expected move (25% / √252 × $100); the position profits on days the stock moves more than that and bleeds on days it moves less.

With a realistic cost overlay:

- Each hedge pays the underlying's half-spread (≈ 0.5–1 bp on SPY, 2–10 bps on mid-cap single names). At 2–4 hedges/day over 20 days, hedging costs consume roughly 5–15% of gross gamma revenue on liquid underlyings and substantially more on illiquid ones — the frontmatter `breakeven_cost_bps: 5` reflects the round-trip cost per hedge above which a 3-point RV-IV edge in a liquid name stops paying.
- The options bid-ask spread (often 1–3% of premium on liquid ATM SPY straddles, far wider on single names) is paid twice and must be amortized over the trade.
- Because the unconditional variance risk premium runs against the long-gamma side, an always-on version of this strategy historically loses money. Run selectively, a realistic net expectation is Sharpe ≈ 0.4 with ~20% peak drawdown (matching frontmatter) — a positively skewed return profile: frequent small theta losses, occasional large wins when vol erupts (e.g., long-gamma books were among the few winners in February 2018 and March 2020).

| Driver | Impact |
|--------|--------|
| Realized vol > Implied vol | Profitable — gamma revenue exceeds theta cost |
| Realized vol < Implied vol | Unprofitable — theta bleed exceeds gamma revenue |
| Large intraday swings | Favorable — more hedging opportunities capture more gamma |
| Low intraday movement | Unfavorable — theta dominates |
| Transaction costs | Reduce profitability — each hedge incurs spread and commission |
| Vega changes (IV expansion) | Windfall profits if IV rises after position is established |

## Capacity limits

Moderate. In index products (SPY/SPX, ES) the hedge flow is negligible up to tens of millions of premium at risk; the binding constraint is the *options* side — buying enough cheap vol without moving IV. In single names, both legs bind: ATM option open interest caps position size at low single-digit $millions of premium per name, and hedge trades in the stock start incurring impact beyond ~1–2% of ADV. A realistic aggregate capacity for a selective multi-name program is on the order of $50M (frontmatter `capacity_usd`); beyond that, entry IV impact erodes the very cheapness the strategy depends on. Crowding risk is medium: when many funds buy vol into the same well-flagged catalyst, IV is bid up and the edge disappears before entry.

## What kills this strategy

- **Vol never shows up** — the most common death: IV looked cheap, the catalyst fizzled, and theta ground the premium away. Repeated across positions, this is the variance risk premium collecting its toll.
- **IV crush on entry mistiming** — buying "cheap" vol that gets cheaper (e.g., post-event IV normalization continuing further than expected) loses on vega even before theta.
- **Whipsaw between hedge bands** — price oscillates inside the threshold without triggering hedges, or repeatedly reverses just after hedges, realizing vol in a pattern the discrete hedger cannot monetize.
- **Transaction cost creep** — spread widening on the underlying or the options quietly pushes the breakeven RV-IV gap beyond anything achievable (see [[failure-modes]]).
- **Gamma endgame mishandling** — holding into the final week, where gamma is violent at the strike and zero elsewhere; hedging errors there can give back a month of scalps.
- **Edge crowding** — pre-catalyst vol buying becomes consensus and IV is no longer cheap when you arrive.

## Kill criteria

- Rolling 12-month net P&L < 0 across ≥ 20 completed trades → stop and review the RV forecast model
- Average (realized vol − entry IV) across the last 20 trades < +0.5 vol points → entry filter has lost its edge
- Hedging costs > 25% of gross gamma revenue over a rolling quarter → widen bands or restrict to more liquid underlyings
- Peak-to-trough drawdown > 20% of allocated capital
- Theta paid on any single position > 60% of premium with scalp P&L below theta paid → close that position (also encoded in pseudocode)

## When to use

Gamma scalping is most attractive in **low implied volatility environments** where options are cheap relative to expected future movement. Common setups include:

- Before an anticipated increase in volatility (e.g., ahead of earnings season, FOMC meetings, or geopolitical events) when IV has not yet risen
- When a stock has been range-bound for an extended period and options premiums have compressed, but a catalyst is approaching
- In markets where historical (realized) volatility consistently exceeds implied volatility

The strategy is least attractive when implied volatility is elevated and options are expensive — the theta cost is high and the stock needs to move significantly just to break even.

Use [[iv-rank-and-iv-percentile|IV rank / IV percentile]] as the entry screen: long gamma is conditionally attractive when IV rank is in the bottom quintile (cheap vol) *and* a credible RV catalyst sits inside the option's life. A low IV rank alone is not a signal — vol can be cheap for good reason (see [[iv-rank-and-iv-percentile#Common Mistakes]]).

## Variants

| Variant | Structure | When preferred |
|---------|-----------|----------------|
| Classic straddle scalp | Long ATM call + put, scalp delta | General-purpose, max gamma per dollar |
| Strangle scalp | Long OTM call + put | Lower theta, lower gamma; cheaper carry in range-bound names |
| Calendar-financed | Long near-dated gamma, short far-dated vega | Reduces net theta; adds term-structure risk |
| Ratio / back-spread | Asymmetric long gamma | Directional lean with positive gamma |
| Index vs single-name | Long single-name gamma, short index vol | Bleeds into [[implied-correlation|implied-correlation]] and [[dispersion-trading|dispersion]] territory |
| [[variance-swaps|Variance swap]] | Pure realized-vs-implied exposure | Removes path dependence and hedge-band noise entirely |

## Relationship to delta hedging and short-vol

Gamma scalping is the **long-gamma mirror image** of a short-vol [[delta-hedging|delta-hedged]] book. The two share the same machinery (continuous delta neutralization) but opposite signs on every dimension:

| Dimension | Gamma scalping (long gamma) | Short-vol delta hedge |
|-----------|-----------------------------|------------------------|
| Gamma / theta | +Γ, −Θ | −Γ, +Θ |
| Bets that | RV > IV | IV > RV |
| Skew of returns | Positive (small bleeds, big wins) | Negative (small wins, violent losses) |
| Base-rate friend/foe | Foe — pays the [[variance-risk-premium]] | Friend — collects it |
| Worst environment | Quiet, IV-rich tape | Vol-regime break ([[volmageddon]], Mar 2020) |
| Hedge re-cost interpretation | Each hedge **locks in** a scalp | Each hedge **realizes** a small loss |

## Advantages

- **Non-directional**: profits from movement in either direction, not from predicting price direction
- **Defined risk on options leg**: the maximum loss on the options position is the premium paid
- **Positively skewed**: losses are capped at premium; vol explosions deliver outsized wins — the opposite tail profile of short-vol strategies
- **Scalable across underlyings**: can be applied to multiple names simultaneously
- **Edge is measurable**: the realized-vs-implied vol spread can be tracked and modeled quantitatively

## Disadvantages

- **Theta decay is relentless**: the position bleeds money every day the stock does not move enough
- **The base rate is hostile**: implied vol exceeds realized vol most of the time, so unselective gamma buying loses on average
- **Transaction costs accumulate**: frequent delta hedging generates significant commissions and slippage
- **Requires active management**: not a set-and-forget strategy; needs continuous intraday monitoring
- **Gamma declines near expiration**: as options approach expiry, gamma concentrates at the strike but vanishes elsewhere, making hedging erratic
- **Difficult to execute in illiquid options**: wide bid-ask spreads on options and underlying erode the edge

## Sources

- Sinclair, E. (2013), *Volatility Trading* (2nd ed.), Wiley — practitioner treatment of gamma scalping, hedge-band selection, and the RV-vs-IV bet
- Bennett, C. (2014), *Trading Volatility* — straddle/strangle mechanics and vol-premium empirics
- Hull, J., *Options, Futures, and Other Derivatives* — Greeks and dynamic hedging fundamentals
- Carr, P. & Wu, L. (2009), "Variance Risk Premiums", *Review of Financial Studies* — documents that index implied vol persistently exceeds realized vol, the headwind this strategy must overcome
- Boyle, P. & Emanuel, D. (1980), "Discretely Adjusted Option Hedges", *Journal of Financial Economics* — discrete hedging error

## Related

- [[volatility-trading]] — broader overview of vol strategies
- [[delta-hedging]] — the hedging technique underlying gamma scalping
- [[implied-volatility]] — the key pricing input the strategy bets against
- [[realized-volatility]] — the quantity the strategy is long
- [[variance-risk-premium]] — the structural headwind to long-gamma trading
- [[options]] — the instruments used
- [[straddle]] — the typical options structure for this strategy
- [[strangle]] — lower-theta alternative structure
- [[theta-decay]] — the cost of carrying the position
- [[variance-swaps]] — an alternative instrument for trading realized vs implied vol
- [[delta]] — the directional exposure the scalp loop flattens
- [[gamma]] — the convexity engine of the strategy
- [[theta]] — the daily carry cost
- [[vega]] — the IV-expansion windfall (or crush risk)
- [[greeks]] — the full Greek framework
- [[iv-rank-and-iv-percentile]] — the entry screen for "cheap" vol
- [[implied-correlation]] — relevant to single-name-vs-index gamma structures
- [[dispersion-trading]] — long single-name gamma vs short index vol
- [[market-regime]] — vol regime determines when long gamma pays
- [[volmageddon]] — the kind of vol explosion long-gamma books are positioned for
- [[failure-modes]] — generic strategy failure modes
- [[edge-taxonomy]] — classification of the edge categories referenced above
