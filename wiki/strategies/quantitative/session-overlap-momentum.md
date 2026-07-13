---
title: "Session Overlap Momentum"
type: strategy
created: 2026-05-16
updated: 2026-06-20
status: excellent
tags: [crypto, quantitative, day-trading, derivatives, market-microstructure, mean-reversion]
aliases: ["LNY Overlap Fade", "Asia-Range-Break Fade", "Session Breakout Fade"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Asian-session retail breakout buyers chase late-Asia momentum into thin late-Asia books; professional liquidity arriving with the London-NY overlap fades the false breakout against a measurable depth and funding backdrop."
data_required: [ohlcv-1m, funding-rates, order-book-l2]
min_capital_usd: 5000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 0.4  # conservative prior only — UNTESTED; net-of-costs prior range 0.3-0.6 given funding drag and short-side asymmetry (see Performance Characteristics)
expected_max_drawdown: 0.20
breakeven_cost_bps: 25
kill_criteria: |
  - drawdown > 20%
  - rolling 3-month Sharpe < 0
  - win rate < 40% over a 50-trade rolling sample
  - funding regime shifts to sustained-negative on the targeted asset for >2 consecutive weeks (short-side carry flips from earner to payer)
  - structural regime shift: spot-led, ETF-flow-dominated tape where Asia ranges consistently hold into London
related:
  - "[[crypto-trading-sessions]]"
  - "[[session-overlap-liquidity]]"
  - "[[funding-by-hour]]"
  - "[[liquidation-cascade-fade]]"
  - "[[crypto-perp-backtesting-pitfalls]]"
  - "[[funding-rate]]"
  - "[[perpetual-futures]]"
  - "[[spot-vs-derivatives-volume-ratio]]"
---

# Session Overlap Momentum

Session overlap momentum is an intraday crypto strategy that **fades failed late-Asia breakouts into the London-NY overlap**. It operationalises the empirical observation that Asian-session ranges are often broken on thin books in late Asia / early London, then reversed once professional flow arrives with the London and New York sessions, by entering short on failed upside breakouts and managing the trade around [[funding-by-hour|funding stamps]].

## Edge Source

The edge has two components, both drawn from the [[edge-taxonomy]]:

- **Behavioral**: Asian retail traders chase late-session momentum after long ranging periods, producing breakouts that are not backed by real flow. This is a well-documented [[crypto-trading-sessions|Asia-session characteristic]]: lower liquidity, tighter ranges, and a higher rate of false breakouts (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).
- **Structural**: the London-NY overlap is the most liquid window of the crypto day, with deeper books and tighter spreads (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]). The arrival of LNY-overlap liquidity creates a measurable depth gradient — the same order size that punched through the late-Asia book is absorbed and faded by the LNY-overlap book.

The strategy is therefore neither pure behavioral nor pure structural alpha — it is the interaction of a behavioral pattern (retail breakout chasing) with a structural feature (the LNY liquidity step-up).

## Why This Edge Exists

Who is on the other side, and why do they keep losing?

The losing side is **late-Asia / early-London retail perp buyers** on venues like [[binance]] USDⓈ-M and Bybit. They see a slow grind through the Asia high on the 1m chart, infer continuation, and market-buy with leverage. The book they hit is thin: market makers have already widened in anticipation of the European open, and depth at the top 10–25 bps around mid has fallen relative to LNY-overlap depth (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

The winning side is **LNY-overlap professional flow**: market makers who quote into the deeper European/US book, basis traders unwinding overnight longs, and discretionary desks fading the obvious move. Once depth restores at the London open, the breakout has no follow-through; the asset rolls back into and through the Asia range; late-Asia breakout buyers are stopped out or liquidated; their forced selling drives the move that the strategy harvests.

This edge does *not* exist when:

- Asian retail flow is part of a real trend (alt-season, [[crypto-weekday-weekend-etf-era|weekend ETF-gap reversion]] days, or any session where the late-Asia breakout reflects genuine demand)
- ETF-driven US-session flow is sustained directional and reaches back into London
- Funding flips to sustained-negative on the short side (so holding shorts becomes a cost, not a carry)

The strategy is essentially a bet that on the *median* day the Asia-LNY handoff is a depth-gradient mean-reversion, not a trend-continuation.

## Regime Fit

This is a **fade / mean-reversion** strategy, and per the [[regime-matrix]] it shares the short-volatility-like profile of the broader [[mean-reversion]] family: it thrives in choppy, range-respecting tapes and bleeds when ranges resolve into trends. Mapping it onto the standard regime dimensions:

| Regime dimension | Fit | Reason |
|---|---|---|
| **Sideways / chop** | Best | Asia ranges hold their character; false breakouts revert cleanly |
| **Trending up/down** | Worst | The late-Asia breakout *is* the trend; fading it loses repeatedly |
| **High vol / panic** | Mixed | Wider ranges = bigger reverts, but fatter short-side tail (ADL risk) |
| **Low vol** | Good | Tight Asia ranges and clean LNY-overlap absorption |
| **Risk-off / cascade** | Dangerous | A downside cascade is the one time a short *would* pay — but ADL can close it at the worst moment (see [[#What Kills This Strategy]]) |

Crucially it is **regime-conditional on the funding regime too** (an axis specific to perps): a positive-funding regime makes the short a passive earner; a sustained-negative-funding regime turns the carry from tailwind to drag. This second axis is why the strategy needs the explicit funding filter in the [[#Rules]] rather than relying on price regime alone. See [[long-vol-vs-short-vol]] for why a fade book like this should be paired with a convex, trend-loving sleeve (e.g., [[trend-following-cta]] or [[liquidation-cascade-fade]]) rather than run standalone.

## Null Hypothesis

Under the null hypothesis (no edge), late-Asia breakouts are an unbiased indicator of forward direction. Breakouts hold and fail in proportion to baseline drift, and the strategy's gross P&L approximates a random walk. Net of:

- Round-trip [[binance]] USDⓈ-M taker fees of ~4.5-5 bps each leg (0.045-0.05% standard tier; lower with VIP/BNB discounts)
- [[funding-rate]] payments at one or more 8-hour stamps during the LNY hold (positive funding charges the short; only negative funding earns)
- 5–10 bps of execution slippage on top alts

…the strategy loses roughly 20–40 bps per round trip on average. A successful backtest must beat this drag by a margin large enough to deflate for multiple-testing and parameter selection (see [[crypto-perp-backtesting-pitfalls]]).

If observed live P&L is statistically indistinguishable from the null after 50 trades, the strategy is dead.

## Rules

Targeted instrument: BTC, ETH, or top-20 alt perps on [[binance]] USDⓈ-M. Avoid microcaps where late-Asia momentum can carry on real altcoin-season flow.

**Entry**:

1. Define the Asia session range as the 1m high (`AH`) and low (`AL`) over 00:00–07:00 UTC.
2. Compute ATR(14) on the 1m close at 07:00 UTC as `atr_asia`.
3. Wait for a breakout: 1m close above `AH` between 08:00 UTC and 10:00 UTC (early London / LNY pre-overlap).
4. Wait up to 60 minutes from the breakout for the move to fail: trigger short if a subsequent 1m close prints back inside the Asia range (below `AH`) within that window.
5. Confirmation filter: skip the trade if [[funding-rate]] on the venue is negative at entry (you'd pay to be short). Skip if [[spot-vs-derivatives-volume-ratio]] is unusually high — that signals a spot-led, ETF-flow day on which Asia breakouts tend to hold.

**Exit**:

- Scale out 50% at the Asia midpoint `(AH + AL) / 2`.
- Scale out the remainder at `AL` or at the New York close (21:00 UTC), whichever comes first.
- Hard stop: 1m close above `AH + 1.0 * atr_asia`.

**Sizing**:

- 1–2% account risk per trade defined as `entry_price − stop_price`, applied to a USDⓈ-M perp position.
- Leverage selected to make the stop loss equal the chosen risk percentage, not maximum allowed leverage.

## Implementation Pseudocode

```python
# Session Overlap Momentum — illustrative pseudocode (NOT production code)
# Universe: BTC/ETH/top-20 alt USD-M perps on Binance

asia_start, asia_end = "00:00", "07:00"  # UTC
london_window = ("08:00", "10:00")       # entry window
ny_close = "21:00"

for day in trading_days:
    bars_asia = bars_1m(day, asia_start, asia_end)
    AH, AL = max(bars_asia.high), min(bars_asia.low)
    atr_asia = atr(bars_1m(day, "00:00", "07:00"), period=14)

    breakout_time = None
    for bar in bars_1m(day, *london_window):
        if bar.close > AH:
            breakout_time = bar.time
            break

    if breakout_time is None:
        continue  # no setup today

    # Funding/regime filter
    if funding_rate_now(asset, venue="binance") < 0:
        continue
    if spot_deriv_ratio_24h(asset) > regime_threshold:
        continue  # spot-led day, edge likely absent

    # Wait up to 60m for the breakout to fail back inside Asia range
    for bar in bars_1m_after(breakout_time, minutes=60):
        if bar.close < AH:
            entry = bar.close
            stop = AH + 1.0 * atr_asia
            risk_per_unit = stop - entry
            qty = (account_equity * 0.01) / risk_per_unit  # 1% risk
            open_short(asset, qty, stop=stop)

            tp1 = (AH + AL) / 2  # Asia midpoint
            tp2 = AL              # Asia low
            manage_trade(
                scale_out_at=[tp1, tp2],
                force_close_at=ny_close,
            )
            break
```

This pseudocode omits production-critical details: order types, partial-fill handling, funding-stamp avoidance, exchange-specific minimum tick/lot sizes, and reconnection logic. It is a sketch of the decision logic, not deployable code.

## Indicators / Data Used

- 1m OHLCV for the targeted perp, full 24h (sessions need contiguous data)
- Asia-session high / low / midpoint, recomputed daily at 07:00 UTC
- ATR(14) on 1m bars over the Asia session
- Live [[funding-rate]] from the venue (and predicted next-stamp rate from [[coinglass]])
- L2 [[order-book]] depth around mid at entry (sanity check — abort if late-Asia book has freakishly *high* depth, which would invalidate the depth-gradient assumption)
- [[spot-vs-derivatives-volume-ratio]] 24h rolling, as a regime filter

## Example Trade

*Illustrative only — these numbers are not from any real trade or backtest.*

Hypothetical setup on ETHUSDT perp on [[binance]]:

- 00:00–07:00 UTC: ETH oscillates 3,420–3,455. `AH = 3,455`, `AL = 3,420`, `atr_asia = 6.5`.
- 08:42 UTC: 1m close at 3,461 — breakout fires.
- 09:14 UTC: 1m close at 3,453 — back inside the Asia range. Funding currently +0.012%/8h (positive — short earns at the next stamp). Spot/deriv ratio at 0.45, below the regime cutoff.
- Entry short at 3,453. Stop at `3,455 + 1.0 * 6.5 = 3,461.5`. Risk per unit = 8.5.
- Account equity $10,000, 1% risk = $100. Position size: $100 / 8.5 = 11.76 ETH notional → roughly $40,600 notional → ~4× effective leverage on USDⓈ-M.
- TP1 at Asia mid `(3,455 + 3,420)/2 = 3,437.5` → +15.5 reward per unit on 50% of position.
- TP2 at `AL = 3,420` → +33 reward per unit on remainder.
- 16:00 UTC funding stamp passes during the hold: short receives +0.012% on remaining notional.

Outcome scenarios are not given because no live or backtested data supports them. The point of the example is to show the *shape* of the trade, not its expected P&L.

## Performance Characteristics

This strategy has **not** been backtested for this wiki entry. No Sharpe, hit-rate, or drawdown number quoted below is from observed data — all numbers are *cost-floor assumptions* that any backtest must clear.

The cost floor on a single round trip:

| Cost source | Magnitude (illustrative) | Notes |
|-------------|--------------------------|-------|
| [[binance]] USDⓈ-M taker fee | ~4.5-5 bps per side, ~9-10 bps round trip (standard tier) | Maker fees lower if entry can be limit-filled |
| Execution slippage | 5–10 bps round trip on top alts | Higher on smaller-cap alts and in thin sessions |
| [[funding-rate]] (in your favour) | up to +0.05% per 8h stamp in stressed regimes (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]) | Short earns this when funding is positive; *pays* it when funding is negative |
| Funding (against you) | symmetric — up to -0.05%/8h paid by the short side when funding flips | This is the most under-appreciated risk; in negative-funding regimes the carry collapses |

A trade entered around 09:30 UTC and held to 21:00 UTC crosses the 16:00 UTC funding stamp. In a positive-funding regime, the short collects funding at 16:00. In a negative-funding regime, the trader pays. Strategies that ignore the funding regime overstate their expected P&L by exactly the funding term, every stamp.

The breakeven cost floor of ~25 bps in the frontmatter assumes a benign funding regime (short receives or pays nothing net) and clean execution. A regime with sustained negative funding pushes the breakeven materially higher; a regime with reliable positive funding lowers it.

## Capacity Limits

Capacity is structural and venue-dependent. Indicative ceilings before market impact dominates:

- BTC, ETH on [[binance]] USDⓈ-M during LNY overlap: roughly $5M per trade without material impact on the entry fill
- Top-20 alts: $0.5M–$2M per trade depending on the specific pair
- Late-Asia / pre-LNY entry window: capacity drops by roughly half versus the deep LNY overlap, which is part of the edge

Above these thresholds, the trader's own entry order becomes part of the false breakout the strategy is designed to fade — a clear capacity wall.

## What Kills This Strategy

The most likely failure modes, drawn from [[failure-modes]] and the crypto-specific [[crypto-perp-backtesting-pitfalls]] list:

1. **Strong-trend regimes**. In alt-season or post-ETF-approval rallies, Asia ranges hold and the breakout *is* the trend. Fading it loses money repeatedly and quickly.
2. **ETF-driven gap days**. Large net ETF inflows or outflows produce US-session moves that reach back into London hours, overwhelming the LNY-overlap fade signal (see [[crypto-weekday-weekend-etf-era]]).
3. **Funding regime flips negative**. The short side stops being a passive earner of funding and becomes a payer. Net P&L compresses; on persistent negative-funding regimes, edge disappears.
4. **Altcoin season**. Late-Asia retail momentum on small-cap alts can carry through London and into NY. The strategy is most vulnerable on smaller-cap targeted alts in these regimes.
5. **Auto-deleveraging during cascade events**. A short on a venue with shallow [[insurance-fund]] coverage can be ADL'd out at the worst possible moment in a downside cascade — paradoxically the moment when the trade would have paid the most (see [[perpetual-futures#Auto-Deleveraging-ADL]]).
6. **Liquidity regime shift**. If the [[crypto-weekday-weekend-etf-era|weekday-US-hours liquidity concentration]] continues to deepen, the depth gradient between late-Asia and LNY-overlap widens further — initially helpful, but as more participants notice and trade the same edge, crowding (medium crowding risk in the frontmatter) erodes the spread.

## Kill Criteria

Quantitative retirement triggers (see [[when-to-retire-a-strategy]]):

- Drawdown exceeds 20% from peak account equity
- Rolling 3-month Sharpe falls below 0
- Win rate falls below 40% over any 50-trade rolling sample
- Funding regime shifts to sustained-negative on the targeted asset for more than 2 consecutive weeks
- [[spot-vs-derivatives-volume-ratio]] for the targeted asset shifts structurally higher (sustained spot-led tape) for more than 4 consecutive weeks

Any one trigger pauses the strategy pending review; two triggers retires it.

## Advantages

- Clear timing edge that maps directly to a session framework and is easy to communicate
- Easy to backtest with widely available 1m perp OHLCV data
- Naturally short-biased, which complements long-biased crypto books in a portfolio context
- Funding carry on the short side in positive-funding regimes provides a modest, passive boost
- Capacity limit is well-defined and observable from book depth data

## Disadvantages

- **Asymmetric short-side loss**: a crypto perp short can lose more than the initial margin on a violent upside breakout (subject to ADL); the loss tail is fatter on the short side than the long side. This is the dominant risk and must not be under-stated.
- **Funding drag is regime-dependent**: in negative-funding regimes the short pays at every stamp; backtests using benign-regime funding history will overstate returns
- Highly regime-dependent overall — works in choppy, perp-dominated tapes; fails in trending, spot-led tapes
- Requires precise execution at entry and stop; sloppy fills eat the edge
- Requires constant monitoring around funding stamps and US-session macro releases
- Crowding risk: as session-effect strategies become more publicised, the LNY-overlap fade attracts copycats and the depth gradient may narrow

## Comparison to Adjacent Strategies

This strategy is one member of a family of intraday crypto microstructure fades. Knowing how it differs from neighbours clarifies when to deploy which:

| Strategy | Trigger | Horizon | Side bias | Edge mechanism | Key difference |
|---|---|---|---|---|---|
| **Session Overlap Momentum** (this page) | Failed late-Asia breakout into LNY | Intraday (hours) | Short | Behavioral × structural depth gradient | Session-time-specific; funding-aware |
| [[liquidation-cascade-fade]] | Forced-liquidation cascade | Minutes–hours | Mean-revert (often long after downside flush) | Structural fragility of thin books | Event-driven, not time-of-day; convex/long-vol-like |
| [[opening-range-breakout]] | First-N-minutes range break | Intraday | Either | Momentum continuation | *Buys* the breakout this strategy *fades* — regime-inverse |
| [[funding-rate-arbitrage]] | Funding extreme | Days | Delta-neutral | Carry / structural | Carry harvest, not a directional fade |
| [[grid-trading]] | Range definition | Continuous | Either | Mean-reversion within a band | No session timing; passive band-fading |

The cleanest pairing inside a crypto book is with [[liquidation-cascade-fade]] (which *wants* the high-vol cascade this strategy is exposed to via ADL) and an explicit long-vol/trend sleeve — this is the [[regime-matrix#The Long-Vol / Short-Vol Master Axis|long-vol/short-vol complementarity]] principle applied to perps. Running this fade alongside [[opening-range-breakout]] on the same universe is a regime-inverse conflict and should be toggled, never stacked.

## Sources

- (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]])

## Related

- [[crypto-trading-sessions]] — the hub framework this strategy operationalises
- [[session-overlap-liquidity]] — the depth-gradient mechanism the strategy harvests
- [[funding-by-hour]] — funding timing that defines the carry
- [[liquidation-cascade-fade]] — adjacent strategy that exploits the same thin-session fragility on a longer horizon
- [[crypto-perp-backtesting-pitfalls]] — required reading before any backtest
- [[funding-rate]] — mechanism
- [[perpetual-futures]] — instrument and ADL risk context
- [[spot-vs-derivatives-volume-ratio]] — regime filter
- [[regime-matrix]] — where this fade sits across market regimes
- [[mean-reversion]] — the parent strategy family
- [[long-vol-vs-short-vol]] — why a fade book pairs with a convex sleeve
- [[opening-range-breakout]] — the regime-inverse strategy that buys what this fades
- [[failure-modes]] — generic failure-mode taxonomy
- [[when-to-retire-a-strategy]] — kill-criteria methodology
