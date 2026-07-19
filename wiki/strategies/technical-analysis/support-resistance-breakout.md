---
title: Support and Resistance Breakout Strategy
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: review
tags:
  - breakout
  - support-resistance
  - volume
  - fakeout
  - retest
  - crypto
strategy_type: breakout
timeframe: swing
markets:
  - crypto
  - forex
complexity: beginner
backtest_status: untested
related:
  - "[[channel-breakout]]"
  - "[[opening-range-breakout]]"
  - "[[volatility-breakout]]"
  - "[[rsi-divergence]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
  - "[[perpetual-futures]]"
  - "[[funding-rate]]"
  - "[[liquidations]]"

# Edge characterization
edge_source: [behavioral, structural]
edge_mechanism: "Behavioral: participants cluster stops and limit orders around previously tested horizontal levels; when the level breaks with conviction volume, a cascade of triggered stops plus breakout-chasing new entries produces a sustained directional move that is self-reinforcing until the next major level is reached. Structural: in crypto, the cascade is literal — leveraged perp long positions auto-liquidate through support levels, amplifying the move; the stop-hunt pattern (price probing through a level before reversing) is a crypto-native behavioral feature where large players deliberately collect retail stops before the true breakout direction emerges."

# Data and infrastructure requirements
data_required: [ohlcv, volume, funding-rates, liquidations]
min_capital_usd: 1000
capacity_usd: 300000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 0.4
expected_max_drawdown: 0.25
breakeven_cost_bps: 20

# Kill criteria
kill_criteria: |
  - false-breakout rate > 60% over rolling 20 signals → prefer retest entries only; no aggressive breakout chasing
  - 3 consecutive false breakouts at the same level → the level is being manipulated; abandon it
  - vol-shock regime or active liquidation cascade → no new breakout entries; reduce to flat if short near major support
---

# Support and Resistance Breakout Strategy

## Edge source

**Behavioral (primary)**: Horizontal support and resistance levels are human coordination points — participants agree they are meaningful because they have been tested and respected repeatedly. This agreement concentrates stops (just beyond the level from existing positions) and limit orders (for those waiting to enter on confirmation). When the level breaks on strong volume, the stop-cascade fires, triggering market orders in the breakout direction; breakout-chasing entries amplify this; the combined flow produces a directional move that continues until the next level.

**Structural (crypto-specific)**: In crypto perp markets, the cascade is literal and mechanical. Leveraged long positions have liquidation prices below support levels; when support breaks, the auto-liquidation engine triggers forced closes, producing selling that drives price further below support and triggering the next tier of liquidations — a waterfall effect. This structural liquidation cascade makes crypto support breakdowns more violent and more sustained than equity support breaks (where the mechanism is primarily behavioral, not mechanical). A similar dynamic operates on breakouts above resistance: leveraged short positions face forced covering (short liquidations), amplifying the move upward.

**Stop-hunt pattern (crypto behavioral)**: At obvious, widely-watched levels, large crypto players deliberately probe through the level to collect retail stops before the true breakout direction reverses. This creates the characteristic "fakeout" pattern — a sudden break below support that immediately recovers above the level. The retest entry strategy (waiting for the level to hold after the initial break) is specifically designed to avoid entering on these manufactured fakeouts.

## Null hypothesis

Under the null, support and resistance levels are arbitrary horizontal lines drawn on noise — price breaks through them at random and the apparent edge from "confirmed breakouts" is selection bias (only remembering the breakouts that worked). The counter-argument is structural in crypto: the liquidation cascade is a real, mechanical phenomenon that makes support breaks self-reinforcing in a way that exceeds random; and the concentration of stop orders around obvious levels (observable in exchange orderbook depth before the break) is not random. However, the null is hard to reject purely from price data; edge confirmation requires order-flow confirmation (volume spike + liquidation activity at the break) to distinguish genuine breakouts from fakeouts.

## Overview

The Support and Resistance Breakout strategy trades price breaking through established horizontal levels that have previously acted as barriers. When price breaks above [[resistance]] with strong [[volume]], former resistance becomes new support, offering a high-probability continuation setup. Conversely, when price breaks below [[support]], it becomes new resistance. The **retest** of the broken level is often the safest entry point, as it confirms the breakout is genuine rather than a **false breakout (fakeout)**. This strategy is foundational to [[technical-analysis]] and forms the basis of many other breakout approaches (Source: [[book-technical-analysis-of-the-financial-markets]]).

## Rules

### Entry Rules
1. **Identify Key Levels:** Mark horizontal [[support-resistance]] levels that price has tested at least **2-3 times**. The more touches, the more significant the level.
2. **Breakout Entry:** Enter when price closes **above resistance** (for longs) or **below support** (for shorts) on a candle with above-average [[volume]] (>1.5x the 20-bar average).
3. **Retest Entry (Preferred):** Wait for price to break through the level, then pull back to retest the broken level (former resistance becomes support). Enter on the retest candle that holds the level. This avoids fakeouts.
4. **Volume Confirmation:** The breakout candle must show a meaningful volume spike. Low-volume breakouts have a high probability of failure (Source: book-how-to-make-money-in-stocks).
5. **Multiple Timeframe Alignment:** The breakout on the entry timeframe should align with the trend on one timeframe higher (e.g., break out on the 4H, trend is bullish on the daily).

### Exit Rules
1. **Measured Move:** Target the distance equal to the height of the prior range (from support to resistance) projected from the breakout point.
2. **Next Level Target:** Set the target at the next significant support/resistance level above (longs) or below (shorts).
3. **Stop Loss:** Place the stop just below the broken resistance level (for longs) or above the broken support (for shorts). The broken level should now hold as support/resistance.
4. **Failure Exit:** If price breaks back through the level on heavy volume and closes on the other side, the breakout has failed. Exit immediately.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[support-resistance]] (horizontal) | Manual identification | Key breakout levels |
| [[volume]] | 20-bar average | Breakout confirmation |
| [[moving-average]] | 20 and 50 EMA | Trend context |
| [[rsi]] | 14-period | Avoid buying into overbought breakouts |
| [[candlestick-patterns]] | N/A | Retest confirmation |

## Example Trade

**Setup:** SOL/USD daily chart. A clear resistance level at $175 has been tested and rejected 3 times over the past 6 weeks. Price is in a higher-low pattern, indicating building pressure. The 20 EMA is above the 50 EMA (bullish trend structure).

**Entry (Aggressive):** Price closes above $175 at $177.50 on volume that is 2.1x the 20-day average. Enter long at $177.50.

**Entry (Conservative/Retest):** Price breaks to $182, then pulls back to $176 over 2 days. A bullish [[hammer]] candle forms at $175.80 -- the old resistance holding as new support. Enter long at $176.50.

**Management:** Stop loss at $172 (below the breakout level). Risk = $4.50. Target = $175 + ($175 - $152 range height) = $198. R/R = 4.8:1.

**Exit:** Price rallies to $198 target over 12 days. Or: if price closes back below $175 on strong volume, exit immediately as a failed breakout.

## Performance Characteristics

- **Win Rate:** 55-65% for retest entries; 40-50% for aggressive breakout entries
- **Best Conditions:** Markets emerging from extended consolidation ranges with building volume
- **Worst Conditions:** Low-liquidity environments, news-driven chop, or markets with wide spreads
- **Average Holding Period:** 3-20 days depending on the range width and target distance
- **Key Insight:** Retests offer dramatically better risk/reward and win rate than aggressive breakout entries

## Advantages

- Conceptually simple and intuitive; beginner-friendly entry into [[technical-analysis]]
- Clear, predefined levels remove ambiguity from trade planning
- Works on all timeframes and all liquid markets (stocks, [[crypto]], [[forex]])
- The retest entry provides excellent risk/reward with tight stops
- Breakout levels are visible to many traders, creating self-reinforcing dynamics

## Disadvantages

- **False breakouts (fakeouts)** are the primary risk -- price breaks through, triggers entries, then reverses sharply
- Requires patience to wait for proper retests; aggressive entries get caught in fakeouts more often
- Support/resistance identification has a subjective element -- different traders may draw levels differently
- Breakouts in low-[[volume]] environments are unreliable
- Stop placement just below the broken level may be too obvious, inviting [[stop-hunting]] by larger players
- Round numbers and obvious levels attract institutional manipulation and liquidity grabs

## Capacity limits

Support/resistance breakout trading in BTC/ETH perps has essentially no capacity constraint at the strategy level — multi-billion perp markets absorb large directional positions. The constraint is **trade frequency**: major S/R levels on BTC/ETH daily charts resolve 4–8 times per year, so the strategy produces modest annual trade count. Scaling requires running on multiple assets and timeframes, accepting that alt-crypto correlation reduces the diversification benefit substantially.

## What kills this strategy

1. **Stop-hunts and fakeouts**: in crypto, obvious levels with high stop-cluster density are prime targets for institutional stop-hunting; the fakeout rate on aggressive breakout entries can exceed 50% at the most-watched levels. Retest entries mitigate this but require more patience.
2. **Weekend / low-liquidity breakouts**: false breakouts are more common during thin weekend and late-night sessions when volume is insufficient to sustain the move; a Sunday evening "break" of a key BTC level often reverses by Monday open.
3. **Liquidation cascades that blow through multiple levels**: in extreme events (FTX, LUNA, 2025-10-10), price can blast through several major support levels in sequence, invalidating every planned retest entry. The strategy requires a vol-shock kill switch to avoid being the "retest buyer" during a cascade.
4. **Macro regime override**: FOMC, CPI, and broader risk-off events override technical levels; a key S/R that held for months can break instantly on a macro print, with no reliable retest because the fundamental regime has shifted.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- False-breakout rate (price re-enters the range within 3 candles) exceeds 60% over rolling 20 signals → shift exclusively to retest entries (no aggressive breakout chasing); require volume > 2× 20-day average for confirmation.
- Three consecutive false breakouts at the same specific level → that level is being actively manipulated; abandon it and identify the next structural level.
- CryptoDataAPI vol-regime-score > 75 or active liquidation cascade signal → no new breakout entries; reduce to flat if short-positioned near major support (cascade risk).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` — daily OHLCV for level identification and volume confirmation
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding direction (bias filter; positive funding biases breakout direction up)
- `GET /api/v1/market-intelligence/liquidations` — liquidation cascade data (distinguishes genuine breakouts from cascade-driven moves)
- `GET /api/v1/volatility/regime` — vol-regime filter; skip breakout entries in vol_shock regime

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep archive for identifying historically significant levels

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` → level detection (2-3+ touches) and the volume-confirmed close beyond the level; code the retest entry as the default, not the aggressive chase.
- **Break quality** — `GET /api/v1/market-intelligence/liquidations` — separates a genuine breakout from a cascade-driven overshoot; a live cascade means no retest buying (kill criterion three).
- **Bias** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding direction biases which side of the range to arm.
- **Regime gate** — `GET /api/v1/volatility/regime` — `vol_shock` suspends entries per the kill criteria; `GET /api/v1/quant/market` distinguishes trend-continuation breaks from range fakeouts.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) for level significance and false-break rates across cycles; pair with `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) so regime filters stay point-in-time.

## Related

- [[channel-breakout]] — geometric pattern version of the same breakout logic
- [[opening-range-breakout]] — session-window version
- [[volatility-breakout]] — ATR-based expansion from contraction
- [[rsi-divergence]] — oscillator companion for level-based entries
- [[perpetual-futures]] — primary crypto instrument
- [[funding-rate]] — directional bias filter
- [[liquidations]] — the cascade mechanism that amplifies crypto support breaks

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy's foundational treatment of support/resistance theory, role reversal (broken support becoming resistance and vice versa), and breakout confirmation techniques
