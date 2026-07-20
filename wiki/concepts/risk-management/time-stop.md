---
title: "Time Stop"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [risk-management, mean-reversion, quantitative, crypto, perpetual-futures, funding-rate, execution]
aliases: ["Time Stop", "Time-Based Exit", "Time Exit", "Max Holding Period", "Bar Stop", "Holding Period Limit", "Scratch Rule"]
related: ["[[stop-loss]]", "[[trailing-stop]]", "[[atr-trailing-stop]]", "[[half-life-of-mean-reversion]]", "[[stretch-revert]]", "[[mean-reversion]]", "[[ornstein-uhlenbeck]]", "[[position-sizing]]", "[[funding-aware-position-sizing]]", "[[liquidation-price-aware-sizing]]", "[[z-score]]", "[[hurst-exponent]]", "[[risk-of-ruin]]", "[[overfitting]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[opportunity-cost]]", "[[transaction-cost-modeling]]", "[[false-signals]]", "[[regime-detection]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [risk-management, quantitative]
prerequisites: ["[[stop-loss]]", "[[mean-reversion]]"]
difficulty: intermediate
---

# Time Stop

A time stop closes a position after a fixed elapsed duration — a bar count, a clock interval, a session boundary — regardless of whether it is winning, losing, or flat. It is the third axis of exit logic alongside price stops ([[stop-loss]]) and volatility-scaled stops ([[atr-trailing-stop]]), and it is the only one that limits **how long you are exposed** rather than **how much you can lose**.

The rationale is simple and often skipped: a trading thesis carries an implied horizon. If a signal claims "this dislocation will revert", it is claiming reversion within some timeframe. A position that has not worked within that timeframe is **evidence against the thesis**, not merely a trade that has not finished yet.

## The core argument

Consider a reversion entry at a −2.5σ [[z-score|stretch]] with an expected reversion horizon of roughly ten bars. Fifty bars later, price is unchanged. What does the strategy believe?

Under the naive reading: nothing has happened, the trade is still open, the thesis is intact. Under the correct reading: the model predicted reversion within ten bars and the market did not deliver it across five such windows. **The absence of the predicted event is information.** The most likely explanation is that the dislocation was not a dislocation — the market repriced, the level held, and what looked like a temporary displacement was a permanent one measured against a stale baseline.

A price stop does not capture this at all. Price stops fire on *adverse movement*. A position that goes nowhere never triggers one, so a thesis can be comprehensively falsified while the trade sits untouched, consuming margin and paying carry, until it eventually resolves in whichever direction the market happens to pick — which is by then a coin flip, not the edge that was entered for.

The time stop is the mechanism that converts "the predicted thing did not happen" into an exit.

## How it differs from a price stop

| | Price stop | Volatility stop | **Time stop** |
|---|---|---|---|
| Triggers on | Adverse price move | Adverse move scaled by [[atr-trailing-stop\|ATR]] | Elapsed duration |
| Caps | Loss per trade | Loss, vol-adjusted | **Exposure duration** |
| Fires when trade is flat | No | No | **Yes** |
| Parameterised from | Risk budget, structure | Recent volatility | [[half-life-of-mean-reversion\|Half-life]], thesis horizon |
| Typical exit P/L | A loss | A loss | **Near zero — a scratch** |
| Protects against | Being wrong quickly | Being wrong in a vol regime | **Being wrong slowly** |

They are complements, not alternatives. A well-formed reversion position carries both: a hard price stop for the case where the dislocation was real information and price kept going, and a time stop for the far more common case where nothing happens and the thesis quietly expires. The [[stretch-revert]] family runs three stop layers for exactly this reason — a time stop, a hard band stop, and a regime stop — and treats all three as load-bearing.

The most important structural difference: **a time stop caps something a price stop cannot even see.** Capital tied up in a stale position is capital not deployed on the next signal, margin not available for the next entry, and — in perps — a funding bill accruing on a position with no expected return. None of that appears in a per-trade P/L attribution, which is why time stops are routinely omitted from strategies that would benefit most from them.

## Setting one from the half-life

The natural parameterisation comes from [[half-life-of-mean-reversion]]. If a series' half-life is `t½` bars, the expected time to close *half* the gap is `t½`, and full reversion is a 3–4 half-life event.

A defensible construction:

| Exit target | Suggested time stop | Reasoning |
|---|---|---|
| Partial reversion (z → ±1) | ~1–2 × `t½` | One half-life closes half the gap |
| Full reversion (z → 0) | ~3–4 × `t½` | Three half-lives close ~87.5%, four ~94% |
| Hard ceiling | ~5 × `t½` | Beyond this the model has been rejected by the data |

The boundaries matter in both directions:

- **Too tight (below ~1× `t½`)** — the stop fires before the modelled reversion has had time to occur. The strategy systematically scratches trades that were working. In the results this shows up as a mysteriously low win rate on a signal that backtests well, and it is usually misdiagnosed as signal decay.
- **Too loose (beyond ~5× `t½`)** — the stop stops binding and provides no protection. Trades exit on the price stop or on reversion anyway, and the time stop becomes a parameter that does nothing except appear in the optimisation grid.

**The half-life is an order-of-magnitude input, not a precision one.** Its estimate is a quotient of noisy quantities and is unstable near the random-walk boundary. Use it to distinguish "give this ten bars, not a hundred" — a robust and useful conclusion — rather than to derive a stop of 34.2 bars. Any strategy whose profitability depends on the exact multiple is fitted to noise; see [[overfitting]].

```python
def should_time_stop(pos, cfg):
    """Time stop keyed to the estimated reversion horizon.

    cfg.half_life is in the SAME bar units as pos.bars_held. Mixing a
    15m-estimated half-life with 1m bars is a silent factor-of-15 error.
    """
    max_bars = cfg.time_stop_mult * cfg.half_life      # mult ~2-4
    if pos.bars_held < max_bars:
        return None

    # Distinguish a scratch from a stop-out for attribution purposes
    reason = "time_stop_scratch" if abs(pos.unrealised_pct) < cfg.scratch_band \
             else "time_stop_loss"
    return close(pos, reason=reason)
```

## Why reversion strategies need this most

Reversion is the strategy family where the time stop earns its keep, for two reasons that compound.

**1. Unreverted reversion is increasingly likely to be information.**

The entry premise is that a displacement is temporary — driven by forced or impatient flow rather than by a change in fair value. That premise has a shelf life. Forced flow is, by construction, fast: a liquidation engine closes a position in seconds, a stop cascade resolves in minutes, an index rebalance completes at the close. If the displacement persists well past the timescale on which that flow operates, the flow explanation has been exhausted, and the remaining explanations are all versions of "the market repriced".

Put differently: the probability that a given displacement is noise rather than information **decays with the time it persists**. A reversion position held far past its half-life is a position whose conditional probability of being right has fallen since entry, held at unchanged or larger size. That is the wrong direction for a risk position to move.

This is also the mechanism behind the [[stretch-revert]] family's dominant failure mode — walking the bands, where price rides an extreme through a strong trend and "oversold" gets more oversold. The time stop is not a substitute for the [[hurst-exponent]] regime gate that is meant to prevent that entry, but it is the backstop for when the gate lets one through, which it will.

**2. In crypto perps, a held position bleeds funding.**

Spot equities have a clean carrying cost of roughly zero over short horizons. Perpetual futures do not. Funding accrues at each interval — hourly on Hyperliquid — and it accrues in the direction that punishes the crowded side, which for a fade strategy is frequently the side you are on ([[funding-aware-position-sizing]], [[perpetual-futures]]).

That converts "no harm in holding" into a measurable and continuous cost. A reversion trade targeting a 1.5% move that pays 0.01% per hour has given back a fifth of its target in three days of doing nothing. The time stop bounds this directly, and it is the reason a time stop is more important in crypto perps than in most other markets — the cost of patience is metered.

Leverage compounds the case. At the 3–5× the [[stretch-revert]] members typically run, funding is levered along with everything else, and a stale position is also margin that is not available elsewhere while sitting closer to a liquidation price than the entry implied ([[liquidation-price-aware-sizing]]).

## Scratch versus stop

A distinction worth encoding in the execution layer and in the trade log:

- **A stop-out** is an exit at a material loss because price moved against the position. It confirms the trade was wrong about direction and it consumes risk budget.
- **A scratch** is an exit near breakeven because the thesis expired without resolving. It confirms the trade was wrong about *timing* or about the setup existing at all, and it costs approximately the round-trip spread.

Time stops produce mostly scratches, and that is the intended behaviour. The consequences for how a strategy is evaluated are non-trivial:

- **Win rate becomes harder to read.** A scratch is neither a win nor a loss. Bucketing scratches as losses understates the signal; bucketing them as wins is straightforwardly dishonest. Track them as a third category.
- **Scratch rate is a diagnostic in its own right.** A high scratch rate means the signal is firing on setups that do not resolve — a precision problem at the entry, not an exit problem. Tightening the entry threshold is the fix; loosening the time stop is not.
- **Costs are real even when P/L is zero.** Every scratch pays a round trip. A strategy with a 60% scratch rate is paying spread on six trades out of ten for no directional exposure at all, which can dominate the economics ([[transaction-cost-modeling]]).
- **The [[opportunity-cost]] recovered is the actual benefit.** Freed capital redeployed on fresh signals is where the time stop pays, and it is invisible in per-trade attribution — it only shows up at the portfolio level.

## The failure mode: exiting a valid thesis too early

The time stop has a real and symmetrical cost, and it should be stated as plainly as the benefit.

**A time stop cuts winners that were about to work.** Reversion is a distribution of outcomes, not a schedule. If the half-life is ten bars, a meaningful fraction of genuine reversions take thirty. A stop at 2× `t½` exits those at breakeven, and the strategy never learns they would have paid — the counterfactual is not in the log.

Specific ways this goes wrong:

- **Truncating the right tail.** In a distribution where slow reversions are also large ones — plausible, since larger displacements take longer to close — a tight time stop preferentially removes the biggest winners. That is a direct attack on the payoff ratio of a strategy that already wins small and loses large.
- **Cutting through a regime change in your favour.** A position that goes nowhere for 20 bars and then reverts violently is common in crypto, where reversion often waits for a catalyst. The time stop exits at bar 15.
- **Mistaking a clock for a model.** Time is a proxy for "the thesis has been falsified", not the thesis itself. Where a direct falsification test exists — the regime gate flipping, [[open-interest]] expanding into the stretch, the baseline itself moving to meet price — that test is strictly better information than elapsed bars. The time stop is the fallback for when no such test fires.
- **Optimising the parameter.** The time-stop length is another cell in the grid, and it is a particularly seductive one because the sweep always finds a value that improves the backtest. Anchor it to the half-life and leave it alone; a time stop tuned to the sample is worse than no time stop, because it looks principled.

**The honest framing:** a time stop trades expected value for variance reduction and capital velocity. It will cost some winners. It is justified when the carrying cost is real (perps funding), when the capital has alternative uses (a multi-signal book), and when the thesis genuinely has a horizon (reversion does; trend-following largely does not). It is unjustified when applied reflexively to a position whose thesis has no natural clock.

## Beyond mean reversion

Time stops appear elsewhere, with the same logic and different horizons:

- **Event-driven trades** — a catalyst trade has a defined window. If the catalyst passes without the expected move, the thesis is exhausted by definition.
- **Breakout entries** — a breakout that does not follow through within a few bars is a failed breakout, which is a different and often opposite setup.
- **Session and calendar boundaries** — flattening before a weekend, a known low-liquidity window, or a scheduled macro release is a time stop with an exogenous clock.

**Where they fit poorly:** [[trend-following]] positions, whose whole premise is that the holding period is unbounded and that the rare very long hold carries the entire expectancy. Imposing a time stop on a trend follower truncates precisely the tail the strategy exists to capture. The distinction is whether the thesis has an implied horizon — reversion does, trend does not.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the bar clock the stop counts against, and the series the half-life that parameterises it is estimated from; the interval here defines the stop's units
- `GET /api/v1/derivatives/funding-rates?coin=X` — the accruing carry a time stop bounds; multiply the rate by the proposed holding window to price the cost of patience before setting the stop
- `GET /api/v1/derivatives/open-interest?coin=X` — OI expanding while a fade sits unreverted is direct evidence the displacement is real flow, which is better falsification than the clock
- `GET /api/v1/volatility/regime/{symbol}` — reversion horizons are regime-dependent, so a stop calibrated in one volatility state is mis-sized in another

**Historical data:**
- `GET /api/v1/backtesting/klines` — for measuring the empirical distribution of *time to reversion*, which is the only defensible basis for a time-stop length
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels, for checking whether reversion time differs enough between labelled states to justify a regime-conditional stop

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [market regimes](https://cryptodataapi.com/market-regimes) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can set and audit a time stop empirically rather than by feel:

- **Derive the length, do not sweep it.** Estimate the [[half-life-of-mean-reversion|half-life]] on the residual from `GET /api/v1/hyperliquid/candles`, then set the stop at 2–4× and freeze it. An agent that grid-searches time-stop lengths against a P/L curve is fitting a parameter that was supposed to be an anchor.
- **Measure the reversion-time distribution, not just its mean.** From `GET /api/v1/backtesting/klines`, compute the full histogram of bars-to-reversion after threshold stretches. The right tail of that histogram *is* the population of winners a given stop will cut — report that cost explicitly alongside the stop recommendation.
- **Price the funding over the window before accepting the stop.** Pull `GET /api/v1/derivatives/funding-rates?coin=X` and multiply by the stop length. If accumulated funding is a large fraction of the reversion target, the correct response is a shorter stop or no trade — not a longer one.
- **Prefer a live falsification test to the clock where one exists.** `GET /api/v1/derivatives/open-interest?coin=X` rising into an unreverted stretch falsifies the noise thesis directly and should exit before the time stop does. Log which of the two fired; if the clock always fires first, the direct test is mis-tuned.
- **Log scratches as a third outcome category.** Report win / loss / scratch separately with the round-trip cost attached to each. A win-rate figure that silently absorbs scratches is uninformative and, on a strategy family already known to have a misleading win rate, actively harmful.

## Related

- [[stop-loss]] — the price-based exit; caps loss rather than duration
- [[trailing-stop]] · [[atr-trailing-stop]] — the volatility-scaled exits; the other two axes of the exit design
- [[half-life-of-mean-reversion]] — the estimate a time stop should be sized from
- [[ornstein-uhlenbeck]] — the model the half-life comes out of
- [[stretch-revert]] — the strategy family where the time stop is one of three mandatory stop layers
- [[mean-reversion]] — the thesis with a natural horizon
- [[z-score]] — the stretch measurement whose failure to revert the clock is timing
- [[hurst-exponent]] — the regime gate the time stop backstops
- [[funding-aware-position-sizing]] · [[funding-rate]] · [[perpetual-futures]] — the carry that makes patience expensive in crypto
- [[liquidation-price-aware-sizing]] — why a stale levered position is worse than a stale unlevered one
- [[position-sizing]] · [[risk-of-ruin]] — the wider risk framework
- [[transaction-cost-modeling]] · [[opportunity-cost]] — where the cost and the benefit of scratches actually land
- [[overfitting]] — why the stop multiple should be anchored, not swept
- [[false-signals]] — a high scratch rate is an entry problem, not an exit one
- [[regime-detection]] — reversion horizons are regime-dependent
- [[failure-modes]] · [[when-to-retire-a-strategy]] — the strategy-level analogue of the same "the thesis has expired" logic

## Sources

- The half-life-to-holding-period link follows Chan, Ernest P. (2013), *Algorithmic Trading: Winning Strategies and Their Rationale*, which uses the Ornstein-Uhlenbeck half-life to set holding horizons and stops for mean-reverting spreads.
- The three-layer stop design (time stop, hard band stop, regime stop) and the "reversion that hasn't happened is increasingly likely to be information" framing are recorded on [[stretch-revert]] (2026-07-20). No source-summary page exists for that family's live data.
- The funding-drag argument draws on the vault's [[funding-aware-position-sizing]] and [[perpetual-futures]] pages.
- No published study of time-stop effectiveness in crypto perpetuals has been reviewed for this page. The scratch-rate diagnostics and the right-tail-truncation cost are analytical arguments, not measured results, and the vault holds no backtest supporting a specific stop multiple.
- No vault source-summary page covers time-based exits; time stops have no prior coverage anywhere in this vault, which is why this page exists.
