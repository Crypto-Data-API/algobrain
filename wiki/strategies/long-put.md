---
title: "Long Put"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, derivatives, volatility, risk-management]
aliases: ["Long Put", "Buy Put", "Protective Put"]
related: ["[[long-call]]", "[[bear-put-spread]]", "[[options-greeks]]", "[[implied-volatility]]", "[[options-risk-budgeting]]", "[[long-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[volatility-skew]]", "[[tail-risk-hedging]]", "[[vix-calls]]", "[[protective-puts]]", "[[theta]]", "[[gamma]]", "[[vega]]", "[[delta]]"]
strategy_type: technical
timeframe: swing
markets: [stocks, options, indices]
complexity: beginner
backtest_status: untested
edge_source: [analytical, behavioral, risk-bearing]
edge_mechanism: "The put seller is structurally short crash-risk and is paid a [[volatility-risk-premium|VRP]] for warehousing it. The buyer wins when realized downside exceeds the implied distribution -- particularly in correlated tail regimes."
data_required: [options-chain, ohlcv-daily, implied-vol-surface, skew-data]
min_capital_usd: 500
capacity_usd: 100000000
crowding_risk: low
expected_sharpe: 0.3
expected_max_drawdown: 1.0
breakeven_cost_bps: 150
---

A long put is the canonical bearish [[options]] position and the simplest portfolio-level downside hedge: the buyer pays a premium for the right to sell 100 shares of the underlying at the strike price on or before expiration. The position has **bounded loss** (premium paid), **maximum profit at zero** (strike minus premium times 100), and serves a dual role: as a directional bet on a decline and as a [[tail-risk-hedging|tail-risk hedge]] for a long-stock or long-beta portfolio. Long puts on equity indices are the single most common institutional hedging instrument in existence.

## Edge Source

**Primary**: analytical (mispricing of left-tail risk vs. realized crash distribution), **behavioral** (the put seller is systematically short convexity and short the [[volatility-skew|negative skew]] of equity returns), and **risk-bearing** (the buyer is paid in expected return foregone -- the [[volatility-risk-premium|VRP]] -- to hold the right tail of payoff).

Long puts on broad equity indices systematically *lose* money in calm regimes -- the historical [[volatility-risk-premium]] on SPX puts is roughly 3-5 vol points, meaning held-to-expiry SPX puts have negative expected return. Edge comes from (a) being correct on a forecastable left-tail catalyst, (b) using the put as a *hedge* whose value is in correlation regime change (offsetting losses elsewhere), or (c) exploiting [[volatility-skew]] mispricings such as buying low-IV puts on names where the historical crash distribution is fatter than the surface implies.

## Why This Edge Exists

The other side of the trade is dominantly:

- **Cash-secured put writers** harvesting income on cash holdings; they are systematically short crash-risk in exchange for a known premium. See [[cash-secured-put]].
- **Equity index premium sellers** ([[short-put]], [[bull-put-spread]], [[iron-condor]] put-side wings) running income strategies that price in calm regimes and pay out in crashes.
- **Market makers** who hedge inventory but charge a [[bid-ask-spread]] and a skew premium to warehouse left-tail risk.
- **Portfolio insurance underwriters** -- pension and insurance balance sheets that sell index puts to fund liabilities, structurally short the equity-crash factor.

The put buyer wins precisely when the put seller's structural short-vol position blows up. Pricewise this is asymmetric: the seller's left tail is the buyer's right tail.

## Null Hypothesis

Under [[geometric-brownian-motion]] with vol equal to implied vol and zero drift, the discounted expected payoff of a long put equals the premium paid; net P&L is zero pre-cost. After the [[volatility-risk-premium]] (3-5 vol points on equity indices, larger on OTM strikes due to skew), the unconditional expected return of a held-to-expiry long put is **strongly negative**. Hedging value is real but is paid for in expected return -- the long-put hedge buyer is rationally giving up roughly 0.5-1.5%/year of expected portfolio return for downside protection.

## Rules

**Entry (speculative)**:
- Direction: bearish thesis with defined catalyst (earnings miss expectation, macro deterioration, technical breakdown, credit spread widening).
- Strike selection (see [[strike-selection]]):
  - **ATM** (delta -0.50): balanced gamma/theta/vega for short-dated speculation.
  - **OTM** (delta -0.10 to -0.30): cheap, high-convexity tail bet; popular for crash speculation.
  - **ITM** (delta -0.65 to -0.80): leveraged short-stock substitute with capped loss.
- DTE: 30-90 DTE for swing speculation; 90-365 DTE for [[tail-risk-hedging]].
- IV/skew check: SPX put skew is *always* negative -- OTM puts are richer than OTM calls. Buy when skew is *flat by historical standards* (see [[volatility-skew]]).

**Entry (hedging)**:
- Hedge ratio: typically 0.5-1.0 portfolio delta worth of put protection. A $1M long-equity portfolio (beta 1.0) is hedged with roughly $1M notional of SPX puts -- e.g., 2 SPX puts at strike 5,000 (each contract = 100 × $5,000 = $500k notional, so 2 puts hedge $1M).
- Strike: 5-15% OTM is the typical "shoulder" -- cheap enough to roll continuously, far enough OTM to avoid normal market noise.
- DTE: 60-180 DTE rolled monthly or quarterly (continuous protection).
- Budget: 1-3% of portfolio NAV per year is the standard institutional allocation to put-based tail hedging. See [[tail-risk-hedging]].

**Exit**:
- Speculative: take profit at 50-100% of premium gain or roll down-and-out to lock in. Stop at -50% premium or thesis invalidation. Time stop at 21 DTE (avoid the [[gamma-risk|gamma trap]]).
- Hedging: roll on a fixed schedule (monthly/quarterly) regardless of market conditions; *do not* time the hedge. Discretionary "dehedging" defeats the purpose.

## Implementation Pseudocode

```python
def long_put_signal(underlying, iv_surface, portfolio, today, mode):
    if mode == "speculative":
        # Directional bearish thesis required
        if not bearish_thesis(underlying, today):
            return None
        iv_pct = iv_surface.percentile(underlying, lookback_days=90)
        if iv_pct > 0.70:
            return None  # IV already elevated, premium too rich
        skew = iv_surface.skew_25d(underlying, dte=30)
        if skew > skew.historical_p80:
            return None  # Put skew too steep, OTM puts overpriced
        catalyst = next_bearish_catalyst(underlying, max_days=60)
        target_dte = max(catalyst.days_until + 14, 30) if catalyst else 45
        target_delta = -0.30  # OTM for convexity
        strike = strike_for_delta(underlying.last, target_dte, target_delta, iv_surface)
        contracts = floor((0.01 * account_equity) / (price_put(...) * 100))
        return Order(side="BUY", type="PUT", strike=strike,
                     dte=target_dte, contracts=contracts)

    elif mode == "hedge":
        # Continuous tail hedge -- rolled on schedule
        portfolio_beta_notional = portfolio.long_equity_notional * portfolio.beta
        target_strike = underlying.last * 0.90  # 10% OTM
        target_dte = 90
        contracts = ceil(portfolio_beta_notional / (target_strike * 100))
        # Apply 2%-of-NAV annual budget cap
        max_premium = 0.02 * portfolio.nav / 4  # 4 quarterly rolls
        contracts = min(contracts, max_premium / (price_put(...) * 100))
        return Order(side="BUY", type="PUT", strike=target_strike,
                     dte=target_dte, contracts=contracts, rolling=True)
```

## Indicators / Data Used

- **Underlying price series** ([[ohlcv]]) and trend regime indicators.
- **Options chain** with bid/ask, IV, Greeks per strike/expiry.
- **[[volatility-skew|Skew]] -- 25-delta put IV minus 25-delta call IV** is the canonical equity-skew measure.
- **[[iv-rank]] / [[iv-percentile]]** for entry timing.
- **Macro stress indicators**: [[vix]], [[move-index|MOVE]], [[credit-spread|HY credit spreads]] -- correlated tail signals.
- **Realized-vol vs. implied-vol gap** -- the empirical [[volatility-risk-premium]].

## Payoff & Greeks

### Payoff sketch (at expiration)

A long put is a hockey stick that pays off to the *downside*: loss is capped at the premium paid above the strike, and profit grows dollar-for-dollar (×100) as spot falls below the strike, reaching its maximum if the underlying goes to zero. Below breakeven the position is effectively a leveraged short.

```
 P/L
  │\
  │ \                                  ← profit grows as spot falls
  │  \                                   (max = (strike − premium) × 100 at spot 0)
 0│───\────────────────────────────────  spot →
  │    \________________________________ ← max loss = premium paid (flat above strike)
  │   BE  K
  │   ↑   ↑
  │  break strike
  │  even
   BE = strike − premium  (profit below this line at expiry)
```

The long put is **negative [[delta]], long [[gamma]], long [[vega]], and negative [[theta]]** — the mirror image of the short-premium [[iron-condor]] wing on the put side, and the structural opposite of a [[short-put]] / [[cash-secured-put]]. Its defining feature for hedgers is **convexity**: as spot falls, delta becomes more negative (long gamma), so the hedge "grows teeth" exactly when it is needed, and the IV spike that typically accompanies a sell-off adds a long-vega tailwind (the [[leverage-effect]]).

### Net-Greeks table (at/near entry)

| Greek | Sign | Behaviour as spot falls | Implication |
|-------|------|-------------------------|-------------|
| [[delta]] | Negative (−0.10 to −0.80 by strike) | Becomes more negative (toward −1.0) | Directional short exposure that intensifies in a decline |
| [[gamma]] | Positive (largest ATM / near expiry) | Accelerates delta in the buyer's favour | The convexity that makes the put an effective tail hedge |
| [[vega]] | Positive | Rises with the [[volatility-skew\|skew]]-driven IV spike in a sell-off | A "right" thesis can pay even before spot moves; conversely IV crush erodes a stalled hedge |
| [[theta]] | Negative | Bleeds daily; accelerates inside ~21 DTE | The carrying cost of the hedge — the [[volatility-risk-premium]] paid to the seller |

The put buyer is **long convexity and long volatility**; the carry cost (negative theta + the [[volatility-risk-premium]]) is the price of that convexity. This is why an unconditional, always-on long-put program has negative expectancy but real portfolio-level value: it converts a thin steady bleed into a large convex payoff precisely in the correlated-tail regimes where it offsets losses elsewhere.

## Example Trade

**Setup (speculative)**: 2026-04-15. AAPL is at $192 after a strong rally; trader's view is that the upcoming May earnings will disappoint on services growth. 30-day ATM IV is 24 (40th percentile, low for AAPL given upcoming earnings); 25-delta put skew is +3.5 vol points (slightly below historical median).

**Trade**: Buy 10x AAPL May 2026 $185 puts (32 DTE) at $3.20 each.

| Field | Value |
|---|---|
| Premium paid | 10 × $3.20 × 100 = $3,200 |
| Breakeven (at expiry) | 185 - 3.20 = $181.80 (-5.3% from spot) |
| Max loss | $3,200 (full premium) |
| Max gain | (185 - 3.20) × 10 × 100 = $181,800 (if AAPL → 0) |
| Initial delta (per contract) | ~-0.32, total Δ ≈ -320 |
| Initial gamma | ~+0.022/contract; position delta moves ~22 per $1 of spot |
| Initial vega | total V ≈ +$200/vol-pt |
| Initial theta | total Θ ≈ -$45/day |

**Outcome A -- AAPL misses earnings, drops to $172, IV spikes from 24 to 32.**
Puts now ~$13.50. P&L = 10 × ($13.50 - $3.20) × 100 = +$10,300 (+322%). Trader sells immediately; do not wait for IV crush to follow the move.

**Outcome B -- AAPL beats slightly, drifts to $194, IV crushes from 24 to 19.**
Puts drop to ~$1.10. P&L = 10 × ($1.10 - $3.20) × 100 = -$2,100 (-66%). Stops out at the -50% rule before reaching this point.

**Outcome C -- AAPL flat to $191 into expiration; puts expire worthless.**
P&L = -$3,200 (-100%). Time-stop at 21 DTE would have salvaged ~$0.80 × 10 × 100 = $800.

**Setup (hedging)**: $2M long-equity portfolio, beta 1.0 to SPX. SPX at 5,400.

**Trade**: Buy 4x SPX 5,000 puts (90 DTE) at $35 each.
- Premium: $14,000 (0.7% of NAV per quarter; ~2.8% annualized).
- Covers 4 × 5,000 × 100 = $2.0M notional at the 5,000 strike.
- If SPX drops 15% to 4,590, puts pay 4 × (5,000 - 4,590) × 100 = $164,000 -- offsetting roughly half of the portfolio's $300k loss. Convexity grows nonlinearly past the strike.

## Performance Characteristics

A naive "buy 30-day ATM SPX puts every day" backtest loses 40-70% per year -- the strategy is structurally negative-expectancy in calm regimes. However:

- **Selective speculative entries** (event-conditional, IV-rank-conditional, skew-conditional) can produce positive expectancy with **low hit rate (25-40%)** and **high payoff ratio (3-10x)**.
- **Held as a hedge**, a continuously-rolled OTM-put program reduces portfolio drawdown by 30-60% in crash regimes at a cost of 1-3% of NAV annually -- *worsening* unconditional Sharpe but improving risk-adjusted compound growth across full cycles by reducing the [[sequence-of-returns-risk|sequence-of-returns]] tax of large drawdowns.
- **Path dependence is severe**: a put bought at IV 14 and held through a 5-vol-point IV rise without spot moving is still profitable on vega even if delta is unrealized.

Realistic cost: 1-2 vol points slippage on entry/exit + commissions; on OTM puts with wider spreads, 3-5% round-trip is realistic.

## Capacity Limits

For listed index puts (SPX, NDX, RUT), capacity is effectively unlimited at any retail or small-institutional scale. SPX put volume routinely exceeds $100B of notional per day. For single-name puts, capacity tracks with the call side (mega-cap: low millions per trade; mid-cap: hundreds of thousands; small-cap: tens of thousands). Put strategies on broad indices are a primary destination for billions of dollars of institutional hedging flow without measurable price impact.

## What Kills This Strategy

- **Persistent low-vol regime** -- continuous put hedging in a multi-year bull market with no drawdown produces years of premium bleed before any payout (2017, 2019, much of 2024-25).
- **Crash that ends as quickly as it starts** -- a one-day spike followed by immediate reversion can leave a put holder with theoretical gains they can't realize at scale (intraday illiquidity).
- **Skew compression after a crisis** -- buying puts when skew is already extreme (post-crash) means paying near peak prices for left-tail protection that will mean-revert.
- **Single-name idiosyncratic blowups** that affect one's *long* book but not the *index* used to hedge (basis risk between hedge and exposure).
- **Counterparty default in extreme regimes** -- not a concern for listed options (clearinghouse-guaranteed) but real for OTC put structures.

See [[failure-modes]].

## Kill Criteria

- Speculative: hit rate below 25% over 50 trades; payoff ratio below 2.5x.
- Hedging: re-evaluate the hedge program if cumulative cost exceeds 5% of NAV per year over a rolling 3-year window without payout (the program is over-allocated for the actual realized tail-risk of the underlying portfolio).
- Permanent: structural change to skew or VRP that makes long puts categorically more expensive without a corresponding rise in realized tail risk.

See [[when-to-retire-a-strategy]].

## Advantages

- **Bounded loss**: maximum loss is the premium paid.
- **Convex downside payoff**: profit grows nonlinearly as spot falls past strike.
- **Capital efficient hedging**: a small put position can hedge a much larger long-equity portfolio.
- **Long vega**: profits from rising IV that typically accompanies declines (the [[leverage-effect]]).
- **Simplicity**: single-leg trade, transparent payoff, suitable for beginners.
- **Diversification benefit at the portfolio level**: even with negative standalone expectancy, puts can improve a long-equity portfolio's risk-adjusted return.
- **Liquidity** on listed index puts is among the deepest in any derivatives market.

## Disadvantages

- **Negative theta** -- the position bleeds daily.
- **Strongly negative unconditional expectancy** -- the [[volatility-risk-premium]] is largest on the put side of the surface (especially OTM).
- **IV crush risk** -- after a feared event passes, IV collapses and a "right" thesis can lose money.
- **Skew tax** -- OTM puts on equities are persistently expensive due to crash-skew demand.
- **Hedge basis risk** -- a put on SPX may not perfectly hedge a long book of single names.
- **Path/timing requirement** -- being right on direction but late on timing still loses to theta.
- **Discipline tax for hedgers** -- the temptation to "skip a roll" in calm times is the most common failure mode of long-put hedge programs.

## Sources

- [[book-options-as-a-strategic-investment]] (McMillan).
- [[book-option-volatility-and-pricing]] (Natenberg) -- pricing, skew, term structure.
- [[book-dynamic-hedging]] (Taleb) -- convexity, the case for systematic tail-hedging.
- [[universa-investments]] / Mark Spitznagel -- the canonical institutional case for permanent put-based tail hedging.
- [[cboe]] specifications for SPX/NDX/RUT puts.

## Related

- [[long-call]] -- the bullish counterpart
- [[bear-put-spread]] -- the capped-payoff, lower-cost variant
- [[protective-puts]] -- long puts paired with stock for hedging
- [[tail-risk-hedging]] -- the broader framework for left-tail protection
- [[vix-calls]] -- alternative tail-hedge vehicle on volatility itself
- [[options-greeks]] -- delta, gamma, vega, theta primer
- [[implied-volatility]] -- the pricing input
- [[volatility-skew]] -- why equity puts are persistently expensive
- [[volatility-risk-premium]] -- the headwind for long puts
- [[options-risk-budgeting]] -- portfolio-level integration
- [[long-volatility-strategies]] -- sleeve-level vol-long allocation
- [[long-vol-vs-short-vol]] -- the structural decision
- [[sequence-of-returns-risk]] -- why drawdown reduction compounds
- [[iron-condor]] -- a short-premium structure whose put-side wing is the counterparty to a long put
- [[leaps]] -- long-dated puts can serve as multi-quarter portfolio insurance
- [[managing-winners]] -- exit discipline (take-profit / time-stop) that also applies to speculative long puts
- [[market-regime]] -- long puts pay in falling, high-correlation regimes and bleed in calm trends
- [[delta]] / [[gamma]] / [[theta]] / [[vega]] -- the position's Greek profile
