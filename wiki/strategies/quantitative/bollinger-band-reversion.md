---
title: "Bollinger Band Reversion"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [mean-reversion, bollinger-bands, volatility, quantitative, john-bollinger, crypto]
aliases: ["Bollinger Band Mean Reversion", "Bollinger Bounce", "BB Reversion Strategy"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: beginner
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Overreacting, leveraged crypto flow pushes price to a volatility-scaled extreme (the band); the reversion trader fades the overshoot back toward the moving-average mean, paid to provide liquidity when the band touch coincides with exhausted flow — but only in ranging regimes."
data_required: [ohlcv-1h, ohlcv-daily, atr, adx, volatility-regime]
min_capital_usd: 1000
capacity_usd: 15000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.30
breakeven_cost_bps: 20
decay_evidence: "The single most common retail crypto reversion signal, so band touches are heavily front-run and 'walking the bands' in crypto's frequent strong trends punishes naive faders. Its edge survives only with a strict ranging/regime filter; without one it is a coin-flip minus costs."
kill_criteria: |
  - rolling 12-month net Sharpe < 0
  - drawdown > 25% of allocated capital
  - win rate < 45% over trailing 100 trades
  - share of trades stopped by 'walking the band' rising above ~40% (regime turned trending)
  - median realized round-trip cost > 20 bps for a full month
related: ["[[bollinger-bands]]", "[[rsi-mean-reversion]]", "[[mean-reversion]]", "[[keltner-channels]]", "[[donchian-channel-breakout]]", "[[regime-detection]]", "[[volatility]]", "[[cryptodataapi]]"]
---

# Bollinger Band Reversion

Bollinger Bands, created by **John Bollinger** in the 1980s, are a 20-period [[simple-moving-average|SMA]] (middle band) with upper and lower bands at 2 standard deviations. Because standard deviation measures volatility, the bands widen when volatility rises and contract when it falls — a property that suits crypto's regime-shifting volatility well. The **Bollinger Band Reversion** strategy is a [[mean-reversion]] approach: buy when price pierces the lower band (statistically cheap vs recent history) and sell/exit when it reaches the upper band or reverts to the middle. The premise is that band touches are unsustainable and price reverts toward the SMA — a premise that holds in ranging crypto markets and fails catastrophically in the strong trends crypto produces so often. It is the most accessible reversion strategy in this wiki and, precisely because it is so widely used, one of the most cost- and regime-sensitive.

## Edge source

Per [[edge-taxonomy]], BB reversion draws on two edge categories, both shared with the broader [[mean-reversion]] family:

- **Behavioral** — a band touch marks a point where leveraged, narrative-chasing crypto flow has pushed price to a volatility-scaled extreme. The fade exploits the overreaction and recency bias of traders who chase the move to the band.
- **Risk-bearing (liquidity provision)** — buying the lower-band touch means absorbing the last tranche of forced/impatient selling when spreads are widest; the reversion trader is paid a small premium for warehousing that inventory until the patient bid returns.

The band itself contains no edge — it is a volatility-scaled z-score with a chart. The edge is entirely in the **regime filter** that keeps you from fading a trend, plus the discipline to wait for exhaustion.

## Why this edge exists

In a ranging crypto market, the marginal seller at the lower band is usually a stop-out or a small liquidation, not a valuation-driven exit; when that flow exhausts, price snaps back to the SMA. Who is on the other side? Traders who sell the low because the tape is red and buy the high because it is green — the recency-driven crowd — plus forced sellers with no price sensitivity. They keep paying because the impulse to chase never disappears. The edge is thin and fragile because the *same* band touch means the opposite thing in a trending market: there, the lower band is being "walked" downward and every fade is run over. This is why the strategy's economics live or die on the ranging filter.

## Null hypothesis

If crypto prices were a random walk, band touches would carry no predictive information: buying the lower band and selling the upper would net zero gross and lose costs times turnover. Under the null, the win rate is ~50%, average post-touch return at any horizon is ~0, and adding an [[rsi]] or [[adx]] filter would not improve the entry distribution. Empirically the null is *not* rejected for crypto without a regime filter — naive band-touch fading in trending crypto is a coin flip minus fees. The edge appears only conditional on a **ranging regime** ([[adx]] < 25, flat 200-SMA, [[volatility]] regime = `mean_reverting`/`normal`); a strategy that only works after that gate is a regime bet, and the gate is doing the real work.

## Rules

### Entry
1. **Long:** price closes at or below the lower Bollinger Band. For confirmation, wait for the next candle to close back inside the bands (a "touch and recover").
2. **Short/sell:** price closes at or above the upper band; wait for a close back inside.
3. **RSI confirmation (strongly recommended in crypto):** combine with [[rsi]]. Long only when price touches the lower band AND [[rsi]](14) < 30; short only when upper band AND RSI(14) > 70. Dual confirmation sharply cuts false signals.
4. **Regime gate (mandatory in crypto):** trade only when [[adx]] < 25 (ranging) and the [[volatility]] regime is not `strong_trend`/`vol_shock`. This is the difference between an edge and a coin flip.

### Exit
1. **Middle-band exit:** close at the 20-period SMA — the conservative, reliable "reversion to mean" target.
2. **Opposite-band exit:** hold for the opposite band for maximum profit (lower→upper) in a confirmed range.
3. **Stop-loss:** 1–2× [[atr]] beyond the entry band (e.g., long at lower band → stop at lower band − 1.5× ATR). In crypto, honor the stop mechanically — walked bands do not forgive.

### Sizing
- Risk ≤ 0.5% of equity to the ATR stop; cap any coin at 5% of the book; 1–2× notional. Scale down 50% when the vol regime is `expanding`.

### Bollinger Squeeze (separate setup)
1. Identify a squeeze: band width (upper − lower)/middle drops to its lowest in 3–6 months.
2. Wait for the squeeze to "fire" — a decisive close outside a band with expanding volume.
3. Trade the breakout direction. This is a **momentum/breakout** play, not reversion — do not fade a firing squeeze.

## Implementation pseudocode

```python
# Bollinger Band reversion — crypto, 1h or 1d bars, regime-gated
for coin in liquid_universe:                       # top-30 by OI + spot volume
    px    = close[coin]
    mid   = sma(px, 20)
    sd    = std(px, 20)
    upper = mid + 2*sd
    lower = mid - 2*sd
    rsi14 = rsi(px, 14)
    ranging = adx(coin, 14) < 25 and vol_regime(coin) in ("normal", "mean_reverting")

    pos = positions.get(coin)
    if pos is None and ranging:
        if px[-2] <= lower[-2] and px[-1] > lower[-1] and rsi14[-1] < 30:      # touch & recover
            buy(coin, size=risk_budget(0.005, stop_dist=1.5*atr(coin)),
                target=mid[-1], stop=lower[-1] - 1.5*atr(coin))
        elif px[-2] >= upper[-2] and px[-1] < upper[-1] and rsi14[-1] > 70:
            sell_short(coin, size=risk_budget(0.005, stop_dist=1.5*atr(coin)),
                       target=mid[-1], stop=upper[-1] + 1.5*atr(coin))
    elif pos is not None:
        if reached(pos.target) or hit(pos.stop):
            close_position(coin)
        elif not ranging:                          # regime flipped to trending — walking-band risk
            close_position(coin)
```

## Indicators / data used

- **[[bollinger-bands]]** (20-period SMA, 2σ) — the core volatility-scaled band.
- **[[rsi]](14)** — oversold/overbought confirmation; see [[rsi-mean-reversion]].
- **[[atr]]** — stop placement, scaled to current volatility.
- **[[adx]]** and the **[[volatility]] regime** — the mandatory ranging gate (crypto's walking-band defense).
- **Band width / %B** — squeeze detection.
- **Volume** and **[[liquidation]] activity** — a liquidation-driven band spike is exhaustion; a steady volume-backed break is a trend.

## Example trade

**Asset:** SOL, 1h chart.
1. SOL has ranged $140–$160 for a week. Bollinger Bands: upper $161, middle $150, lower $139. [[adx]] = 18 (ranging); vol regime `normal`.
2. A brief cross-market risk-off flush drops SOL to $137, closing below the lower band. [[rsi]](14) = 27 (oversold). Dual confirmation.
3. Next hour SOL opens $138 and closes $141 (back inside the bands). Enter long at $141.
4. Stop: lower band ($139) − 1.5× ATR ($3.00) = $134.50. Risk ≈ $6.50/coin.
5. Over ~6 hours SOL reverts to the middle band at $150. Exit at $150.
6. **Result:** +$9/coin (+6.4%) risking $6.50 → ~1.4:1 reward:risk. Round-trip perp cost ~12 bps taker + ~4 bps slippage ≈ 16 bps — inside the move.

## Performance characteristics

Realistic, cost-corrected expectations (not a backtest of this exact spec):

- **Win rate:** 52–62% *with* RSI + regime confirmation; 45–50% (coin-flip) without. The filters are the strategy.
- **Profit factor:** ~1.2–1.7 to the conservative middle-band target.
- **Sharpe:** net ~0.3–0.5 (frontmatter assumes 0.4) — low, because the signal is popular, front-run, and only edges out costs in ranging regimes.
- **Best conditions:** range-bound, low-ADX crypto (chop between catalysts).
- **Worst conditions:** strong trends where price walks the band for many sessions (crypto does this often).

**Cost overlay (crypto, per round trip):**

| Component | Magnitude | Note |
|---|---|---|
| Taker fee (perp, entry + exit) | ~8–11 bps | Maker quoting the band touch cuts this |
| Slippage | 2–5 bps majors, 10–30 bps alts | Band touches happen when the book is thin |
| Funding carry during hold | ±1–3 bps/day | Short-side touches can bleed funding |
| **All-in round trip** | **~12–25 bps** | vs a modest target; the middle-band exit must clear it |

Because the target (middle band) is conservative and the signal is popular, cost discipline and maker execution matter more here than in almost any other reversion variant.

## Capacity limits

Modest and instrument-dependent. On liquid majors (BTC, ETH, SOL), band-touch entries absorb into the low tens of millions before your own fill moves price off the band; on alts the absorbable size collapses because the touch coincides with the thinnest part of the book. Frontmatter assumes **$15M** blended. Because so many retail bots trade the same 20/2 default, the *timing* capacity (how much you can get filled inside the brief touch-and-recover window) is tighter than the notional capacity implies.

## What kills this strategy

- **Walking the bands (trending regime).** The dominant failure: in a strong crypto trend, price closes at/beyond a band for many sessions and every fade is run over. The ranging gate ([[adx]]/vol regime) is the only real defense; drop it and the strategy inverts.
- **Fat-tailed breakouts.** Standard deviation assumes normality; crypto returns are fat-tailed, so a "2σ" touch is not rare — real moves blow through the band and the ATR stop.
- **Front-running / crowding.** The 20/2 default is the most-used retail reversion signal; band touches are anticipated, compressing the edge.
- **Catalyst dislocations.** Fading a band touch caused by a hack, unlock, or delisting — an informational move that does not revert.
- **Cost creep.** Wider alt spreads or adverse funding pushing net edge below the ~20 bps breakeven on a conservative target.

## Kill criteria

- Rolling 12-month net Sharpe < 0.
- Drawdown > 25% of allocated capital.
- Win rate < 45% over the trailing 100 trades.
- Share of trades stopped by "walking the band" rising above ~40% (regime has turned trending) — pause reversion, the market is not ranging.
- Median realized round-trip cost > 20 bps for a full month.

See [[when-to-retire-a-strategy]].

## Advantages

- Statistically grounded — the bands are a volatility-scaled z-score with a clear mathematical basis.
- Dynamically adapts to crypto's volatility regimes (bands widen/narrow automatically).
- The squeeze offers a separate high-probability breakout setup.
- Combines naturally with [[rsi-mean-reversion|RSI]] and [[adx]] for dual/triple confirmation.
- Low minimum capital; accessible to solo operators.

## Disadvantages

- **Walking the bands** traps faders in crypto's frequent strong trends — the defining risk.
- The 20/2 defaults are not optimal per instrument and are heavily front-run.
- Targets are modest (middle band) unless you hold for the opposite band in a confirmed range.
- Standard deviation assumes normality, but crypto returns are fat-tailed.
- Best setups (lower band + RSI < 30 + confirmed range) are infrequent; the strategy is mostly waiting.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/indicators/technical` — price-structure state (SMA/BB/RSI) across assets
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN state (the ranging/trending gate)
- `GET /api/v1/volatility/regime` — per-asset vol regime (the mandatory reversion gate)

**Historical data:**
- `GET /api/v1/indicators/technical/{symbol}` — per-asset detail + 60d history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — raw OHLCV to compute your own bands
- `GET /api/v1/backtesting/klines` — full OHLCV archive for backtesting band + regime filters

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/technical"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-indicators]].

**Live dashboards:** [technical structure](https://cryptodataapi.com/technical-structure) · [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/indicators/technical` classifies the whole universe's SMA/BB/RSI structure in one call: screen for lower-band touches with oversold RSI instead of recomputing bands per coin, then confirm the touch-and-recover on `GET /api/v1/market-data/klines?symbol=...&interval=1h`
- **Regime gate** — `GET /api/v1/volatility/regime` (trade only `mean_reverting`/`normal`, never `vol_shock`) plus `GET /api/v1/indicators/signum-rgg` — GREY is the tradeable chop; RED/GREEN flags the trending regimes where bands get walked
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) covers the strategy's 1h design timeframe across multiple range/trend cycles; pair entries with point-in-time regimes from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid [[lookahead-bias]]
- **Tips** — `/indicators/technical/{symbol}` carries a 60-day state history to measure how long oversold readings persist before committing a rule; respect `insufficient_history` flags on newly listed coins before trusting a 20-bar σ

## Related
- [[rsi-mean-reversion]] — the ideal companion for dual confirmation
- [[bollinger-bands]] — the indicator itself
- [[mean-reversion]] — the parent strategy family
- [[stretch-revert]] — the same band-fade thesis generalised: swap the SMA centreline for any of 14 adaptive baselines, which is where "walking the bands" is either mitigated or made worse
- [[z-score]] · [[median-absolute-deviation]] · [[adaptive-moving-averages]] · [[half-life-of-mean-reversion]] · [[time-stop]]
- [[regime-detection]] — the ranging/trending gate that makes or breaks this strategy
- [[volatility]] — the bands are a volatility measure; regime drives everything
- [[donchian-channel-breakout]] — a breakout (not reversion) channel strategy for contrast
- [[keltner-channels]] — ATR-based channels that pair with Bollinger Bands for squeeze detection
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
