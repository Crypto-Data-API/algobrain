---
title: "Grid Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-27
status: excellent
tags: [mean-reversion, grid-trading, automation, bots, range-trading, quantitative, market-microstructure, crypto]
aliases: ["Grid Bot", "Grid Strategy", "Grid Bot Trading", "Range-Bound Grid", "ADX-Filtered Grid"]
strategy_type: quantitative
timeframe: intraday|swing
markets: [crypto, forex]
complexity: intermediate
backtest_status: paper-traded
edge_source: [structural, risk-bearing]
edge_mechanism: "Within range-bound regimes, you are paid the bid-ask spread and volatility premium for absorbing oscillating flow; the entire edge is conditional on the regime filter being correct"
data_required: [ohlcv-1m, adx-14, bollinger-bands, atr-14, mark-price]
min_capital_usd: 1000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 1.0
expected_max_drawdown: 0.25
breakeven_cost_bps: 10
decay_evidence: "Strategy proliferation via 3Commas/Pionex consumer bots since ~2020 has compressed grid edges; modern viability depends on regime filter quality"
related: ["[[dollar-cost-averaging]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[range-trading]]", "[[market-making]]", "[[market-making-strategy]]", "[[regime-detection]]", "[[adx]]", "[[bollinger-bands]]", "[[atr]]", "[[adverse-selection]]", "[[bid-ask-spread]]", "[[edge-taxonomy]]", "[[funding-rate]]", "[[hyperliquid]]", "[[pionex]]"]
---

# Grid Trading

Grid trading is a systematic, no-directional-view strategy that places a ladder of buy and sell limit orders at fixed price intervals around a reference price. As price oscillates inside a range, the grid mechanically buys dips and sells rallies, harvesting the spacing between adjacent levels as realized profit on each completed cycle. The strategy is mathematically equivalent to a constrained, discretized form of [[market-making]]: the operator stands ready to provide passive liquidity on both sides and is paid the bid-ask spread plus a volatility premium for absorbing oscillating flow.

Grid trading has become enormously popular in [[crypto]] markets through automated grid bots offered by [[pionex|Pionex]], 3Commas, KuCoin, [[bybit|Bybit]], and increasingly on perp DEXs like [[hyperliquid|Hyperliquid]]. In [[forex]], grid bots have been used for decades on range-bound currency pairs. The "set and forget" appeal masks a sharp, regime-dependent risk profile: a grid is a profitable structural strategy in tight, range-bound regimes and a catastrophic inventory accumulator in trends. The reference live bot, currently OFF, addresses this exact failure mode with a strict regime filter (ADX(14) < 20 and Bollinger Bandwidth percentile rank < 20) and a 2.0x ATR break-cancel rule.

## Edge source

The edge is **structural** and **risk-bearing** (see [[edge-taxonomy]]):

- **Structural** — by quoting symmetric limit orders around the mark price, the operator captures the bid-ask spread on every completed round-trip cycle. The grid-spacing is, in effect, a synthetic spread the operator chooses to charge for providing liquidity. Each cycle (one buy fill at level N, one sell fill at level N+1) earns one grid-spacing of P&L gross of fees, regardless of starting price. This is the same accounting that drives any inventory-based market-making book (see [[market-making]]).
- **Risk-bearing** — in exchange for the spread, the operator absorbs directional flow. When informed flow pushes the market through the grid, every fill on the wrong side accumulates losing inventory (the classic [[adverse-selection]] problem). The grid is paid spread for taking the trend regime risk that no other liquidity provider wants to hold during a breakout. The 2.0x ATR break-cancel acts as an explicit cap on this risk-bearing exposure.

Critically, the strategy has **no informational** or **analytical** edge. It does not predict direction. It does not need to. It is a pure regime-conditional liquidity-provision business.

## Why this edge exists

Range-bound markets exhibit short-horizon mean reversion: order flow noise (cancellations, retail market orders, liquidations of marginal positions, MM inventory rebalancing) generates oscillations around a stable reference price without an informed directional impulse. Under those conditions, a passive limit-order ladder is a near-optimal strategy class — it is the discretized, "model-free" cousin of the continuous quoting policy derived in [[avellaneda-stoikov-model|Avellaneda & Stoikov (2008)]] for a high-frequency market maker in a limit order book.

The Avellaneda-Stoikov framework formalizes the intuition: an inventory-aware market maker chooses bid and ask quotes to maximize expected utility subject to inventory risk. The optimal quotes are symmetric around an "indifference price" that is *skewed* away from the mid by accumulated inventory. A symmetric grid with no inventory skew is the special case where (i) inventory aversion is zero or (ii) the operator believes price-process drift is exactly zero (perfect range). The closer the regime is to those assumptions — exactly what the ADX/BB filter tries to detect — the closer the simple grid is to optimal.

The deeper foundation traces to [[market-microstructure|Garman (1976) "Market microstructure"]], which modeled buyer and seller arrivals as Poisson processes and derived dealer survival conditions: a dealer who quotes both sides earns the spread per round-trip and survives as long as buy and sell arrivals are roughly balanced. This is exactly the grid-trader's payoff when the regime is genuinely range-bound. When arrivals are *unbalanced* (i.e., a trend), the dealer accumulates inventory and dies — which is precisely why the regime filter is the entire game.

The "who is on the other side" question: counterparties are taker-flow market participants — retail momentum, market-order liquidations, latency-arb traders, and even other algos rebalancing inventory. They are paying the spread because they value immediacy more than the small price improvement available by waiting. Grid traders sell immediacy. They keep losing as a class because immediacy is genuinely valuable to many flow types and because the cost of waiting (carry, opportunity cost, opportunity to improve quotes elsewhere) is real for the taker. This is the same mechanism that pays HFT market makers; the grid trader is just a much slower, much less sophisticated version operating at human-readable spacings rather than tick-level.

## Null hypothesis

What would performance look like with no actual mean reversion — i.e., if price were a pure martingale random walk inside the grid's range?

Under a driftless random walk:
- The grid still completes cycles. A round trip from level N to N+1 and back to N earns one grid spacing minus two crossings of fees, regardless of path.
- Cycle frequency scales with realized volatility: higher vol = more crossings = more cycles. (This is why grid traders are long realized variance.)
- Win rate per round trip is high (the same level fills both sides eventually) but **expected P&L per *time interval* is dominated by adverse selection**: the random walk eventually drifts out of the range and accumulates inventory that closes only at a loss.

Net of costs, a pure random-walk grid earns approximately:
$$E[\text{PnL}] \approx \text{spacing} \times \text{cycles} - 2 \cdot \text{fee} \cdot \text{cycles} - \text{adverse selection loss}$$

If spacing > 2x fee, gross-of-adverse-selection P&L is positive and grows linearly with cycles. The *adverse selection loss* is what eats the spread: when price exits the range, the open inventory is typically closed (or marked) at a worse price than where it was acquired. Empirical Avellaneda-Stoikov calibrations and academic backtests of grid trading on Bitcoin (see Sources) show this loss is roughly equal to or larger than the gross spread capture in unfiltered regimes — i.e., naive grids are roughly break-even or negative.

**The filter is the entire edge.** The strategy's performance over null is purely a function of how reliably ADX < 20 + BB-compression identifies regimes where the next N hours are mean-reverting. A perfectly noisy filter (no regime detection skill) collapses the strategy to its zero-edge null. A very accurate filter pushes expected adverse selection toward zero and lets the spread capture flow to the bottom line.

## Rules

The "grid" is a family of strategies. The reference bot implements the **Filtered Grid (canonical)**.

### Generic neutral grid

1. Pick a reference price (the mark or recent mid).
2. Choose grid spacing (fixed dollar, percent, or ATR-multiple) and number of levels N (e.g., N=10, 5 above and 5 below).
3. Place a buy limit at every level below the mark and a sell limit at every level above.
4. On any fill at level k, cancel that order and place the matching opposite-side limit at level k+1 (sell) or k-1 (buy) with the same notional.
5. Run indefinitely until a manual exit or a hard stop.

### Filtered grid (the reference bot — canonical)

1. **Regime gate.** Only deploy when both:
   - ADX(14) on the 1-hour timeframe is **< 20** (no trend strength), and
   - Bollinger Band width percentile rank (252-hour lookback) is **< 20** (current volatility is in the bottom quintile of recent history — i.e., the market is compressed).
2. **Setup.** Place 10 limit orders symmetric around the mark price: 5 buys below, 5 sells above. Spacing is a fraction of ATR(14) (e.g., 0.5x ATR per level) or a fixed percent (e.g., 0.4%).
3. **Sizing.** 1x leverage, total grid capital = 15% of book equity. Per-level notional = (15% of equity) / 10.
4. **Replenishment.** On a fill, replace it with the matching opposite-side limit at the next level.
5. **Range break exit.** If |price - grid_center| > **2.0 x ATR(14)**, cancel all open grid orders immediately and close any residual inventory at market. Wait for regime filter to re-trigger before redeploying.
6. **Hold horizons.** Individual fills hold minutes. The full grid lifespan is hours to days, until either filled-out, manually re-centered, or stopped by the range-break rule.

### Long-biased grid (DCA-style)

A grid with only buy orders at descending levels and a smaller set of take-profit sell orders above. Used by long-term accumulators (e.g., spot BTC DCA bots). Equivalent to systematic [[dollar-cost-averaging]] with mechanized profit-taking. No exit on range break — the operator expects to hold the accumulated bag.

### Short-biased grid

The mirror image: ascending sells with take-profit buys below. Used in fade-the-rally setups, often with strict size limits given unbounded short risk.

### Geometric / percentage grid

Spacing scales as a percent of price rather than a fixed dollar amount. For an asset that ranges from $10,000 to $100,000 over a year, fixed-dollar spacing breaks down; percentage spacing self-adjusts. Most modern crypto grid bots (Pionex, KuCoin) default to geometric grids on long timeframes.

### Trailing grid

The grid center is anchored to a slow-moving average (e.g., 50-hour EMA) and the entire ladder shifts as the mean shifts. Useful when the range is itself drifting, but adds a parameter (the trailing speed) and can introduce whipsaw inventory if poorly tuned.

## Implementation pseudocode

```python
# === Filtered grid for crypto perp DEX ===
# Regime filter: ADX(14) < 20 AND BB-width percentile < 20
# Exit: |price - center| > 2.0 * ATR(14)

GRID_LEVELS    = 10               # 5 above, 5 below
GRID_PCT_EQUITY = 0.15            # total grid notional as fraction of equity
LEVERAGE       = 1.0
ADX_MAX        = 20
BBW_PERCENTILE_MAX = 0.20
BREAK_ATR_MULT = 2.0
SPACING_ATR_FRAC = 0.5            # spacing per level = 0.5 * ATR(14)

def is_range_bound(ohlcv_1h):
    adx = ADX(ohlcv_1h, period=14)[-1]
    bbw = BBwidth(ohlcv_1h, period=20, k=2)
    bbw_now = bbw[-1]
    bbw_rank = percentile_rank(bbw[-252:], bbw_now)  # 0..1
    return (adx < ADX_MAX) and (bbw_rank < BBW_PERCENTILE_MAX)

def deploy_grid(symbol, mark_px, equity, ohlcv_1h):
    if not is_range_bound(ohlcv_1h):
        return None
    atr = ATR(ohlcv_1h, period=14)[-1]
    spacing = SPACING_ATR_FRAC * atr
    notional_per_level = (equity * GRID_PCT_EQUITY) / GRID_LEVELS
    grid = {"center": mark_px, "spacing": spacing, "atr": atr,
            "active_orders": {}, "inventory": 0}
    for k in range(1, GRID_LEVELS // 2 + 1):
        buy_px  = mark_px - k * spacing
        sell_px = mark_px + k * spacing
        grid["active_orders"][("buy",  k)] = place_limit(symbol, "buy",
                                                         buy_px, notional_per_level / buy_px)
        grid["active_orders"][("sell", k)] = place_limit(symbol, "sell",
                                                         sell_px, notional_per_level / sell_px)
    return grid

def on_fill(grid, side, level, qty, fill_px):
    # cancel filled, replace with opposite-side limit at same level number
    if side == "buy":
        grid["inventory"] += qty
        new_px = fill_px + grid["spacing"]
        grid["active_orders"][("sell", level)] = place_limit(grid["symbol"],
                                                             "sell", new_px, qty)
    else:
        grid["inventory"] -= qty
        new_px = fill_px - grid["spacing"]
        grid["active_orders"][("buy", level)] = place_limit(grid["symbol"],
                                                            "buy", new_px, qty)

def cancel_grid_if_range_break(grid, mark_px):
    if abs(mark_px - grid["center"]) > BREAK_ATR_MULT * grid["atr"]:
        cancel_all(grid["active_orders"])
        if grid["inventory"] != 0:
            market_close(grid["symbol"], grid["inventory"])
        return True   # grid retired
    return False

# Main loop
while True:
    mark = fetch_mark_price(symbol)
    ohlcv = fetch_ohlcv(symbol, "1h", lookback=300)
    if grid is None:
        grid = deploy_grid(symbol, mark, equity, ohlcv)
    else:
        for fill in poll_fills(grid):
            on_fill(grid, fill.side, fill.level, fill.qty, fill.px)
        if cancel_grid_if_range_break(grid, mark):
            grid = None  # wait for next regime trigger
    sleep(60)
```

## Indicators / data used

- [[adx|ADX(14)]] — trend-strength filter; the gate condition is ADX < 20
- [[bollinger-bands|Bollinger Bands]] (20-period, 2 sigma) — used to compute Bollinger Bandwidth, then ranked over a rolling 252-bar window. Compression (low percentile) = consolidating regime. See `## ADX + Bollinger Compression Filter` below.
- [[atr|ATR(14)]] — sets per-level spacing and the 2.0x ATR break-cancel threshold
- [[mark-price]] / mid-price — the grid's center anchor; reset on each redeploy
- [[funding-rate|Funding rate]] (perp DEX only) — monitored as a cost; persistent funding bias against accumulated inventory is a kill signal
- 1-minute OHLCV for execution-grade fill simulation, 1-hour OHLCV for regime filter

## ADX + Bollinger Compression Filter

This is the single most important component of the strategy. The two indicators are deliberately chosen because they capture **orthogonal** dimensions of "range-bound":

- **ADX(14)** measures *directional movement strength*, normalized as a 0-100 score. Wilder's original interpretation: ADX < 20 = no trend, 20-25 = transitional, > 25 = trending, > 40 = strong trend. The grid wants ADX < 20 — i.e., the market is making no net progress in either direction over the lookback.
- **Bollinger Bandwidth** (BBW = (upper - lower) / middle) measures *realized volatility* relative to its own recent history. A market can have low ADX (no trend) but high BBW (chaotic chop); a grid placed in chop with single ticks larger than the spacing gets shredded by adverse selection. We require *low* BBW — explicitly that today's BBW is in the bottom 20th percentile of the last 252 hours of BBW values.

Why both, not either:

| Regime | ADX | BBW percentile | Grid behavior |
|---|---|---|---|
| Tight consolidation (ideal) | < 20 | < 20 | Many small cycles, adverse selection minimal — strategy works |
| Quiet trend (ADX-only false-pass) | < 20 | < 20 but slowly drifting | Slow grind out the side, controlled by 2x ATR exit |
| Volatile chop (BBW-only false-pass) | > 25 | < 20 | Avoided — ADX kicks it out |
| Breakout / strong trend | > 25 | > 50 | Avoided — both filters reject |
| Volatility expansion | < 20 lagging | > 80 | Avoided — BBW kicks it out before ADX catches up |

The percentile-rank step is critical. Absolute BBW thresholds do not transfer between assets or epochs (BTC's 2021 vol regime is not BTC's 2024 regime). A rolling-percentile rank makes the filter self-calibrating to whatever the asset's current vol environment looks like.

The 2.0x ATR break-cancel acts as a **post-filter regime check**: even if ADX and BBW say "range," realized price action that pushes more than 2.0 ATR away from the grid center is empirical evidence the regime broke. ATR-normalization here matters for the same reason percentile-rank matters in BBW: the threshold transfers across assets and epochs because it's measured in volatility units.

## Example trade

**Asset:** ETH-PERP on a perp DEX, 1-hour timeframe, filtered-grid reference bot.

- **2026-03-10 14:00 UTC.** ETH has been ranging $3,000-$3,500 for two weeks. ADX(14) on 1H = 14.2. BBW percentile rank (252h) = 0.08. Both gates pass; bot deploys.
- **Grid center:** $3,250 (current mark). ATR(14) = $42. Spacing = 0.5 x $42 = $21, but rounded to $50 for clean tick alignment. 10 levels.
- Buy limits: $3,200, $3,150, $3,100, $3,050, $3,000.
- Sell limits: $3,300, $3,350, $3,400, $3,450, $3,500.
- **Capital:** book = $50,000. Grid notional = 15% = $7,500. Per level = $750 (size in ETH ~0.23 at $3,250).
- **Days 1-6.** ETH oscillates inside $3,050-$3,420. 18 buy/sell cycles complete. Gross spacing capture = 18 x $50 x 0.23 ETH = $207. Maker rebates of 0.01% on perp DEX add ~$1.50; taker fills (forced re-quotes after partial cancels) cost ~$8 in fees. Funding paid on net long inventory (avg +0.3 ETH for 4 days at +0.01%/8h) = ~$3. **Net P&L = ~$197 (2.6% of grid capital, 0.4% of book in 6 days).**
- **2026-03-17 09:00.** ETH spikes to $3,665 on macro headline. |$3,665 - $3,250| = $415 = 9.9 x ATR. Break-cancel fires at the 2.0 x ATR threshold ($3,334). All open limits cancelled.
- **Residual position:** 1.4 ETH long (accumulated from earlier dip-buying). Closed at market at $3,640. Realized closure P&L on residual = +$320. Combined with the $197 in cycle profit, the session netted **+$517** before any further fees on the market close. The grid sits idle until ADX drops below 20 again — which doesn't happen for the next 11 days.

This example is the "regime-filter-works" case. The other relevant case is the regime-filter-misses case, in which the post-deploy break happens *fast and against the grid's accumulated inventory* — typically a slow build of long inventory over a multi-day flat tape that ends in a flush. In those cases, the 2.0x ATR exit caps loss but doesn't prevent it; expected loss on a misfired grid is roughly 1.5-2.5% of grid capital, or 0.2-0.4% of book per misfire.

## Performance characteristics

Performance is sharply regime-dependent and must be reported segmented:

**Range-bound regimes (the design environment):**
- Win rate per cycle: 75-90% (cycles that complete profitably).
- Cycles per day in compressed regimes: 3-15 on liquid majors, depending on spacing and realized vol.
- Realized Sharpe (in-regime only): 2.0-4.0 on backtests, before regime-classification error.
- Equity curve: smooth, near-linear during qualifying windows.
- Per-session expected return: 0.2-1.0% of grid capital per day.

**Trending regimes (filter failures):**
- The 2.0x ATR exit caps single-session loss, but cumulative misfire P&L can be substantial if the filter has poor precision.
- Without the exit (naive grid), drawdowns of 20-50% on grid capital in a single trend leg are documented in the academic literature on Bitcoin grid backtesting.

**Cost overlay (perp DEX, 2026 typical):**
- Maker rebate / taker fee: -0.01% / +0.04% (varies by venue and tier).
- Funding rate cost on accumulated inventory: highly variable, but in negative-funding longs or positive-funding shorts the drag can dominate gross spread capture.
- Slippage on emergency closure (at the 2x ATR exit): typically 5-15 bps on liquid majors during normal trend break, 30-100 bps during liquidation cascades.
- **Breakeven cost per round trip:** spacing must be at least 2 x effective fee per side. With 0.04% taker on each leg, spacing must exceed 8 bps. Most live grids run 30-100 bps spacing to give a comfortable margin.

**Net Sharpe (full strategy including regime mistakes):** realistic estimates 0.7-1.3 in 2026 conditions, depending on filter quality. Naive (no filter) grids on crypto are roughly Sharpe 0 to negative after costs; the entire edge is the filter.

## Capacity limits

Grid trading is moderately capacity-constrained. The binding constraints:

1. **Per-level depth.** Each limit order must fit inside the resting depth at its price level without becoming the dominant resting size (which would reveal the grid and allow front-running).
2. **Number of levels.** Wider grids on thin pairs cause the operator's own fills to move the local price, creating a market-impact loop where the grid is paying the spread to itself.
3. **Cross-venue fragmentation.** A single grid on a single venue is the natural unit. Multi-venue grids face inventory-reconciliation latency that can produce phantom fills.

Practical capacity: ~$5M per pair on a top-3 liquidity perp like ETH-PERP; ~$500K-$1M on mid-cap alts; <$100K on long-tail alts where the grid would *be* the order book. A 15%-of-book allocation on a $50K account ($7,500) is comfortably within capacity on liquid pairs.

## What kills this strategy

In rough order of historical lethality:

1. **Trend breakout (canonical failure).** A strong directional move drives one side of the grid to repeated fills while the other never executes. Inventory accumulates in the wrong direction, and the operator either eats the breakout loss at the 2.0x ATR exit or, without the exit, the loss compounds until liquidation. This is the failure mode the regime filter is built to prevent.
2. **Volatility regime expansion.** BBW expands suddenly. Individual ticks become larger than grid spacing, so a single price move skips multiple levels and crystallizes the spacing of *several* levels in losses. The 2x ATR exit helps but is reactive — the loss is taken before the exit fires.
3. **Stuck inventory at the boundary.** If the 2.0x ATR exit isn't fast enough (e.g., a flash crash that gaps through the threshold), the residual position is closed deep into the move, well past the planned stop. Crypto perp DEXs with no liquidation backstop are particularly exposed.
4. **Fee and funding drain.** A neutral-bias grid on a positive-funding-rate asset slowly bleeds funding payments on long inventory it never fully unwinds. This is more dangerous than it looks: a -10 bps/day funding bleed on persistently held inventory equals ~3.5% per month, comfortably erasing typical spacing capture.
5. **Filter regime drift.** The ADX/BBW filter is calibrated on a specific historical vol regime. As the broader market's character shifts (e.g., from 2022 high-vol crypto to 2024 lower-vol crypto), the absolute thresholds may no longer mean the same thing. Percentile-ranking BBW helps; ADX < 20 as an absolute is more fragile.
6. **Crowding.** Pionex/3Commas/KuCoin retail grids on the same liquid pairs all queue at similar levels. Their aggregate accumulation/unloading footprint is now itself a (small) component of the breakout dynamic — when retail grids get stopped en masse, the residual liquidations exacerbate the move that stopped them. See [[crowding-risk]].

## Kill criteria

Numerical conditions for retiring or pausing the grid (see [[when-to-retire-a-strategy]]):

- **3 consecutive grid sessions stopped out** by the 2.0x ATR break rule. Suggests the regime filter is misclassifying.
- **Rolling 30-day P&L negative.** Even if the filter is precise, costs may have eaten the edge.
- **ADX never drops below 20 across the deployment universe** for >7 consecutive days. Means the filter no longer triggers — the strategy is dormant by design, but if it stays dormant with no work to do, capital should be reallocated.
- **Realized cycle Sharpe (in-regime only) < 0.5** over the trailing 90 days. The base rate has shifted; spacing and filter need recalibration.
- **Funding-rate carry exceeds gross spacing capture** for 14 consecutive days on the deployment pair. A sign that perp DEX inventory cost dominates.
- **Capacity erosion.** If the operator's fills consistently move the level by >25% of spacing, capacity has been hit and capital must be reduced.

## Advantages

- Fully automated and 24/7 — perfect fit for crypto's continuous markets.
- No directional view required; orthogonal to most other equity-style strategies, providing genuine diversification when the regime filter is honest.
- Frequent realized small profits create a smooth equity curve in qualifying windows — psychologically easy to run.
- Mechanically simple: the entire decision logic fits in <50 lines of code.
- Well-supported by exchange tooling — most major venues offer native grid bots, simplifying operations.
- Inherits the structural-edge logic of [[market-making]] without requiring HFT-grade infrastructure.

## Disadvantages

- **Trending market risk** is severe and structural; without the regime filter, expected value is roughly zero or negative net of costs.
- **Capital inefficient.** Most of the 15% allocation sits in unfilled limit orders at any moment. The economic return on *deployed* capital is much lower than gross P&L on the resting capital suggests.
- **Fee-intensive.** Dozens of round trips per day mean fees are a meaningful drag; the strategy requires maker rebates or very low taker fees to be viable.
- **Funding/carry exposure.** On perp venues, accumulated inventory drags funding cost that is invisible in spot-only mental models.
- **Filter quality is the entire edge.** This is a one-parameter strategy in disguise: if the regime filter is wrong, nothing else matters.
- **Limited upside.** Profits are bounded by spacing x cycles. A grid does not benefit from a clean directional move in either direction; the operator gives up trend P&L by design.
- **Crowded.** Retail grid bots are now ubiquitous; the easiest regime windows have been arbitraged toward the breakeven of the marginal participant.
- **False sense of profitability.** Realized cycle profits accrue while open inventory marks deeper losses — operators fixated on realized P&L often miss the deteriorating mark-to-market until the 2x ATR exit fires.

## Sources

- Avellaneda, M. and Stoikov, S. (2008). "High-frequency trading in a limit order book." *Quantitative Finance*, 8(3): 217-224. Foundational continuous-time market-making model; grid trading is the discretized cousin of the AS optimal-quoting policy. [[avellaneda-stoikov-model]] *(verified via WebSearch — paper exists at Cornell ORIE preprint and Taylor & Francis)*.
- Garman, M. (1976). "Market microstructure." *Journal of Financial Economics*, 3(3): 257-275. Original Poisson-arrival dealer model that grounds why a two-sided quoter earns the spread per round-trip. *(verified via WebSearch — paper indexed in EconPapers, ScienceDirect)*.
- "The Feasibility of Grid Trading Approach for Bitcoin Based on Backtesting" (EAI / EUDL, 2022). Backtest of grid trading on BTC daily data 2019-2021. Concluded that grid trading is feasible during high-volatility periods but produces low or negative returns in low-volatility periods without a regime filter. *(verified via WebSearch).*
- Liu et al. (2025). "Dynamic Grid Trading Strategy: From Zero Expectation to Market Outperformance." arXiv:2506.11921. Proposes a dynamic-reset grid that materially outperforms static grids and buy-and-hold on minute-level BTC/ETH 2021-2024 data. Confirms the static-grid zero-expectation null and the value-add of regime adaptation. *(verified via WebSearch — paper at arXiv 2506.11921).*
- Pionex Help Center (Grid Trading Bot, Futures Grid Bot). Industry/practitioner reference; documents the standard parameter set used by the largest consumer grid platform. *(verified via WebSearch — pages exist at support.pionex.com).*
- Hyperliquid HLP vault risk-return analyses (Geronimo on Medium; KuCoin research desk; DefiLlama protocol page). Useful as a comparison: HLP is a sophisticated continuous-quoting market-making vault on the same venue category as the reference bot, and provides a benchmark for what professional market making looks like when the regime filter is replaced by an inventory-skewed Avellaneda-Stoikov-style policy. See [[hyperliquid-hlp-basis-arbitrage]]. *(verified via WebSearch).*
- Note on academic coverage: peer-reviewed grid-trading literature is sparse — most rigorous treatments are practitioner blogs, exchange documentation, and a handful of recent arXiv papers. The intellectual scaffolding sits in the broader market-microstructure / market-making literature rather than in a "grid trading" canon.

## Related

- [[market-making]] — the parent theoretical framework. A grid is a discretized, regime-conditional market-making book.
- [[market-making-strategy]] — adjacent active strategy with continuous quote updating.
- [[avellaneda-stoikov-model]] — the inventory-aware optimal quoting policy a grid approximates.
- [[mean-reversion]] — the regime-level assumption a grid bets on.
- [[bollinger-band-reversion]] — alternative range-bound strategy using BB envelopes for entry rather than a static ladder.
- [[range-trading]] — broader concept of trading inside a defined boundary.
- [[regime-detection]] — generalized framework for the ADX/BBW filter.
- [[adx]], [[bollinger-bands]], [[atr]] — the indicator stack.
- [[adverse-selection]] — the failure mode the filter is designed to avoid.
- [[bid-ask-spread]] — the basic unit of grid P&L.
- [[funding-rate]] — the carry cost on perp-DEX grids.
- [[dollar-cost-averaging]] — long-biased grid is mechanized DCA with profit-taking.
- [[crowding-risk]] — relevant given retail-bot proliferation.
- [[edge-taxonomy]] — places this strategy as structural + risk-bearing.
- [[when-to-retire-a-strategy]] — kill-criteria framework.
- [[hyperliquid]], [[hyperliquid-hlp-basis-arbitrage]] — same-venue professional comparable.
- [[pionex]] — primary consumer-grid platform.
