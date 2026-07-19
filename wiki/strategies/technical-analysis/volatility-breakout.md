---
title: Volatility Breakout Strategy
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: review
tags:
  - breakout
  - volatility
  - atr
  - nr7
  - larry-williams
  - contraction-expansion
  - crypto
strategy_type: breakout
timeframe: swing
markets:
  - crypto
  - futures
complexity: intermediate
backtest_status: untested
related:
  - "[[opening-range-breakout]]"
  - "[[channel-breakout]]"
  - "[[support-resistance-breakout]]"
  - "[[bollinger-bands]]"
  - "[[perpetual-futures]]"
  - "[[funding-rate]]"
  - "[[dvol]]"

# Edge characterization
edge_source: [analytical, behavioral]
edge_mechanism: "Analytical: volatility is mean-reverting; NR7/BB-squeeze contraction identifies a low-vol regime that statistically precedes expansion with high reliability (~70% of cases). By entering just after the first expansion candle, the trade captures the bulk of the expansion move with a defined risk limited to the contraction range. Behavioral: after prolonged contraction, participants reduce position sizes and stop watching closely; the expansion catches them off-guard, producing momentum without early exits."

# Data and infrastructure requirements
data_required: [ohlcv, funding-rates, volatility-regime]
min_capital_usd: 1000
capacity_usd: 300000000
crowding_risk: low

# Performance expectations
expected_sharpe: 0.5
expected_max_drawdown: 0.25
breakeven_cost_bps: 20

# Kill criteria
kill_criteria: |
  - NR7 expansion fails (false breakout) > 55% of the time over rolling 20 signals → tighten the contraction filter (require Bollinger squeeze simultaneously)
  - rolling 90-day P&L negative → pause; assess if ATR multiplier needs adjustment for current crypto vol regime
  - DVOL in vol_shock regime → pause new entries; the "contraction" may be artificial pre-spike suppression
---

# Volatility Breakout Strategy

## Edge source

**Analytical (primary)**: Volatility is empirically mean-reverting in all liquid markets. Low-volatility contraction (NR7 or Bollinger Band squeeze) is statistically followed by expansion roughly 65–70% of the time, making the NR7 an objective, scannable setup with positive expectancy. The ATR-based entry threshold and stop ensure that the risk/reward is predefined and consistent across regimes.

**Behavioral (secondary)**: After prolonged contraction, participants reduce their position sizes, trim monitoring attention, and psychologically adjust to the "quiet" regime. The expansion move catches this reduced attention and forces position adjustments — shorts must cover, breakout chasers must enter — producing momentum without early exits that would truncate the move.

**Crypto-specific**: Crypto's volatility is particularly "spiky" — DVOL can sit at 35–45 for weeks (extreme compression) then spike to 80–110 in days (extreme expansion). This contraction-expansion cycle is more pronounced than in equity indices, making the NR7 setup more reliably followed by a genuine expansion in crypto. However, crypto's expansion can be 3–5× the ATR estimate (during a cascade), making wide stops or defined-risk structures essential. The direction of the expansion is genuinely uncertain in crypto, particularly around macro prints — a FOMC can produce a violent ATR expansion in either direction.

## Null hypothesis

Under the null, NR7 days occur at random and the subsequent day's range is drawn from the same distribution as any other day — narrow ranges are not followed by expansions more often than wide ranges are. The counter-argument: the vol-mean-reversion principle is well-established empirically; the NR7 identifies a specific percentile of daily ranges that is below the historical median, and mean reversion to the median is statistically predictable. However, the null remains a live challenge in crypto: if DVOL is structurally low (a genuine low-vol regime, not just contraction before expansion), multiple consecutive NR7s may all be followed by small moves rather than large ones, and the strategy will accumulate small losses. The vol-regime filter (pause in DVOL vol_shock) exists to prevent entering contraction trades during a regime that has no planned expansion.

## Overview

The Volatility Breakout strategy enters trades when price moves more than **X times the Average True Range (ATR)** from the previous close, capturing the explosive expansion that follows periods of contraction. Markets cycle between **contraction** (low volatility, tight ranges) and **expansion** (high volatility, trending moves). This strategy, refined by **Larry Williams** and other system traders, identifies contraction setups using patterns like **NR7** (the narrowest range of the last 7 days) and then trades the inevitable expansion. The core principle: volatility is mean-reverting, so extreme contraction reliably precedes explosive movement.

## Rules

### Entry Rules
1. **Contraction Identification:** Identify days where the daily range (high - low) is the narrowest of the last 7 days (**NR7 pattern**). Alternatively, look for 2+ consecutive days with [[atr]] declining and [[bollinger-bands]] squeezing.
2. **Breakout Trigger:** The next day, place a buy stop at the previous close + (X * ATR) and a sell stop at the previous close - (X * ATR). Typical X values range from 0.5 to 1.0.
3. **Volume Confirmation:** The breakout bar should have above-average [[volume]] (>1.5x the 20-day average volume).
4. **Direction Filter:** Prefer breakouts in the direction of the higher-timeframe trend. Use a 50-period [[moving-average]] on the daily chart to determine bias.
5. **One Side Only:** If the trend filter is bullish, only place the buy stop. If bearish, only the sell stop. This avoids whipsaw entries.

### Exit Rules
1. **ATR Target:** Set profit target at entry price + 2-3x ATR (for longs), capturing the expansion move.
2. **Time Exit:** If the trade hasn't reached 1R profit within 3-5 bars, the expansion has likely failed. Exit at market.
3. **Stop Loss:** Place the initial stop at the opposite side of the breakout (e.g., if long, stop at the sell stop level). Risk per trade = 2x ATR.
4. **Trailing Stop:** After 1R in profit, trail the stop using a [[chandelier-exit]] at 2x ATR from the highest close.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[atr]] | 14-period | Breakout threshold and stop/target |
| NR7 (Narrowest Range 7) | 7-day lookback | Contraction identification |
| [[bollinger-bands]] | 20, 2.0 | Visual contraction/squeeze detection |
| [[volume]] | 20-day average | Confirm breakout conviction |
| [[moving-average]] | 50-period | Trend direction filter |

## Example Trade

*Illustrative round numbers — crypto-scoped.*

**Setup:** BTC/USDT perpetual, daily chart. The last 7 daily ranges are: $2,200, $1,900, $1,700, $1,400, $1,100, $900, $750. Today's range ($750) is the narrowest of the 7 days (NR7 confirmed). ATR(14) = $2,100. Bollinger Bands (20,2) are squeezing — width at a 30-day low. BTC is above the 50-period SMA ($64,500) and daily close is $65,200. Perp funding is mildly positive (+0.006% per 8h, confirming no strong short pressure).

**Entry:** Place a long buy stop at yesterday's close ($65,200) + 0.6 × ATR ($1,260) = **$66,460**. Next session the expansion fires; stop triggered at $66,500.

**Management:** Stop loss at $65,200 − 0.6 × ATR = **$63,940**. Risk = $2,560. Target = $66,500 + (2 × $2,100) = **$70,700**. R/R = 1.64:1.

**Exit:** BTC expands to $71,200 over 3 days. Target hit. Trailing stop alternative: after $69,060 (1R profit), trail stop to $69,060 − 2 × ATR = $64,860 (highest close minus 2× ATR).

*TradFi context (historical reference only)*: the original setup was developed for ES/S&P 500 futures and equity daily charts; the NR7 + ATR-stop + 2× target rules are directly portable to crypto perps. The primary difference is that crypto ATR is 5–10× larger in percentage terms than equity index ATR, so position sizing by ATR naturally reduces unit size in a crypto regime.

## Performance Characteristics

- **Win Rate:** 45-55%; the strategy relies on large winners from expansion moves to offset frequent small losses
- **Best Conditions:** After prolonged consolidation (2+ weeks of declining ATR) followed by a catalyst
- **Worst Conditions:** Choppy markets that expand briefly then contract again, producing multiple small losses
- **Average Holding Period:** 1-5 days for the expansion phase
- **Edge:** The NR7 pattern identifies setups with statistical reliability; expansion after NR7 occurs ~70% of the time

## Advantages

- Grounded in the well-established principle that [[volatility]] is mean-reverting
- NR7 and similar patterns provide objective, scannable setup criteria
- Excellent risk/reward when expansion materializes -- large moves from tight stops
- Works across stocks, [[futures]], and [[crypto]] markets
- Can be fully systematized and backtested with clear rules

## Disadvantages

- The direction of the breakout is uncertain; NR7 identifies **when** expansion will occur, not **which way**
- False breakouts can trigger the entry then reverse, hitting the stop
- Requires patience -- NR7 setups may only appear a few times per month per instrument on the daily chart
- ATR multiplier (X) needs calibration for crypto; the raw NR7 parameters from equity index research may not transfer directly
- Crypto's 24/7 nature means there is no overnight-gap protection; gap-through-stop risk is continuous

## Capacity limits

Volatility-breakout trading in BTC/ETH perps is comfortably capacity-unlimited at individual-fund scale — the constraint is signal frequency (NR7 appears 4–8 times per month on the daily chart per asset). Expanding to 10–20 crypto perps adds signal diversity but introduces BTC-beta correlation. Per-position sizes of $5–50M are achievable without moving the market on expansion candles.

## What kills this strategy

1. **Structural low-vol regime with no catalyst**: if DVOL stays depressed for months with no macro catalyst, NR7s accumulate but expansions are small — all small-loss trades. The strategy requires genuine volatility cycles to find the large expansion winners.
2. **False breakout + immediate reversal**: the expansion fires, triggers the stop, then immediately reverses — a gap-and-trap. In crypto, this happens most often around the 08:00 UTC Deribit settlement, where price is sometimes manipulated into the settlement range and then reverses violently.
3. **Vol-shock expansion exceeds ATR estimate**: when a liquidation cascade or macro shock produces an expansion 3–5× ATR, the stop is hit on either side (buy-stop triggers, then gaps through the sell-stop) in a single candle. Defined-risk structures (ATR-based entry with hard cap) limit this, but slippage in a cascade can exceed theoretical max-loss.
4. **Correlated multi-asset losses**: if running NR7 across BTC + ETH + 5 correlated alts and a macro shock fires all of them simultaneously in the wrong direction, the portfolio max-loss is the sum of all ATR-based stops across all positions — correlation collapse in risk-off.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- NR7 expansion fails (price re-enters the NR7 range within 2 candles) > 55% of the time over rolling 20 signals → add the Bollinger Band squeeze as a simultaneous required filter; pure NR7 alone may be insufficient in the current regime.
- Rolling 90-day P&L negative with > 15 completed trades → pause; examine whether the ATR multiplier (X = 0.6) needs adjustment upward for a higher-vol crypto regime or downward for a compressed regime.
- CryptoDataAPI vol-regime = vol_shock → pause new entries; in a vol-shock the "contraction" may be artificial suppression before the spike, and the expansion direction is unpredictable.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30` — daily OHLCV for NR7 computation and ATR calculation
- `GET /api/v1/volatility/regime` — per-asset vol regime (pause in vol_shock)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding direction (directional bias filter)

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep archive for NR7 + ATR multiplier optimization

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-data]] and [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=30` → NR7 detection + ATR(14) entry stops; arm only the trend-side stop per the 50-MA filter from the same series.
- **Regime gate** — `GET /api/v1/volatility/regime` — this strategy *is* the `compressed` → `expanding` transition trade: enter from `compressed`, pause in `vol_shock` where "contraction" is pre-spike suppression.
- **Bias** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — arm the buy-stop when funding agrees with the trend filter, skip the counter-side.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) for NR7 base rates and X-multiplier optimization; `GET /api/v1/quant/regimes/history` (hourly since 2020, Pro Plus) separates true expansion setups from structural low-vol regimes with no catalyst.
- **Tips** — `GET /api/v1/event/calendar` flags the catalyst that turns a squeeze into an expansion; an NR7 with no dated catalyst and depressed universe vol is the small-loss accumulator to skip.

## Related

- [[opening-range-breakout]] — intraday breakout after a session contraction
- [[channel-breakout]] — geometric pattern version
- [[support-resistance-breakout]] — level-based breakout confirmation
- [[bollinger-bands]] — the visual contraction/squeeze detection tool
- [[perpetual-futures]] — primary crypto instrument
- [[funding-rate]] — directional bias overlay
- [[dvol]] — background vol regime context
