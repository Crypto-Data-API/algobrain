---
title: Commodity Channel Index (CCI)
type: concept
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags: [cci, indicators, technical-analysis, momentum]
aliases: [CCI, "Commodity Channel Index"]
domain: [indicators]
prerequisites: ["[[oscillators]]", "[[moving-averages]]"]
difficulty: intermediate
related:
  - "[[divergence]]"
  - "[[momentum-trading]]"
  - "[[momentum]]"
  - "[[trend]]"
  - "[[donald-lambert]]"
  - "[[rsi]]"
  - "[[stochastic]]"
  - "[[macd]]"
  - "[[oscillators]]"
---

# Commodity Channel Index (CCI)

The Commodity Channel Index (CCI) is a momentum-based [[oscillators|oscillator]] developed by [[donald-lambert|Donald Lambert]] in 1980 that measures how far price has deviated from its statistical mean, used to identify cyclical trends and overbought/oversold conditions. Lambert's design goal was to detect the *beginning and end of cyclical turns* in commodity markets — he assumed commodities trade in repeating seasonal cycles, and CCI was meant to time entries within those cycles.

## How It Works

CCI is calculated by taking the difference between the typical price (average of high, low, close) and its simple [[moving-averages|moving average]], divided by the mean deviation, then scaled by a constant (0.015):

```
Typical Price (TP) = (High + Low + Close) / 3
CCI = (TP − SMA(TP, n)) / (0.015 × Mean Deviation)

where:
  SMA(TP, n)     = simple moving average of TP over the last n periods
  Mean Deviation = (1/n) × Σ | TP_i − SMA(TP, n) |   over the last n periods
```

`n` is the lookback (Lambert used 20), and the **0.015 constant** is a scaling factor chosen so that roughly 70-80% of readings fall within the ±100 band, making excursions beyond ±100 statistically notable. Note that "mean deviation" is the *average absolute deviation*, not the standard deviation — this is a common point of confusion, and it is what makes CCI more responsive (and more volatile) than a z-score built on standard deviation. Unlike bounded oscillators such as [[rsi|RSI]] or [[stochastic]], CCI is **unbounded** — it can read far beyond ±200 (or below −200) in strong trends.

- **CCI above +100** — Overbought territory / strong upward momentum
- **CCI below −100** — Oversold territory / strong downward momentum
- **CCI near zero** — Price is close to its average

### Worked Example

Suppose a 5-period CCI (small `n` chosen for a hand-calculable illustration). The typical prices for the last five sessions are:

| Session | High | Low | Close | TP = (H+L+C)/3 |
|---|---|---|---|---|
| 1 | 24.2 | 23.8 | 24.0 | 24.00 |
| 2 | 24.6 | 24.0 | 24.5 | 24.37 |
| 3 | 25.0 | 24.4 | 24.9 | 24.77 |
| 4 | 25.4 | 24.8 | 25.3 | 25.17 |
| 5 | 26.0 | 25.2 | 25.9 | 25.70 |

**Step 1 — SMA of TP:** (24.00 + 24.37 + 24.77 + 25.17 + 25.70) / 5 = **24.80**

**Step 2 — Mean deviation** (average of absolute deviations from 24.80):
|24.00−24.80| + |24.37−24.80| + |24.77−24.80| + |25.17−24.80| + |25.70−24.80|
= 0.80 + 0.43 + 0.03 + 0.37 + 0.90 = 2.53; ÷ 5 = **0.506**

**Step 3 — CCI** (using the latest TP = 25.70):
CCI = (25.70 − 24.80) / (0.015 × 0.506) = 0.90 / 0.00759 ≈ **+118.6**

A reading of +118.6 is above +100, signalling that price has pushed into overbought/strong-momentum territory — in a confirmed uptrend a trader treats this as trend strength, not an automatic short. (Illustrative numbers only.)

## Trading Applications

CCI is interpreted two opposite ways depending on the prevailing [[trend]] — this is the central skill in using it:

| Use case | Signal | Interpretation |
|---|---|---|
| Mean-reversion (range markets) | CCI crosses back below +100 (or above −100) | Fade the extreme — exhaustion likely |
| Trend-following (Lambert's intent) | CCI crosses *above* +100 | Momentum confirmation — enter/stay long |
| Zero-line cross | CCI crosses 0 upward / downward | Bias flips bullish / bearish |
| [[divergence]] | CCI lower high vs. price higher high | Weakening momentum — top warning |
| Extreme readings | CCI beyond ±200 / ±300 | Climactic move; reversal risk rising |

- **Overbought/Oversold** — readings beyond ±100 or ±200 flag stretched conditions; in a range they signal potential reversals, in a trend they signal strength.
- **Zero-line crossover** — crossing above zero is a bullish bias signal, below is bearish.
- **[[divergence]]** — CCI making lower highs while price makes higher highs warns of weakening [[momentum]] (and vice versa for bottoms).
- **Trend identification** — sustained readings above +100 indicate a strong uptrend; Lambert's original system bought when CCI rose above +100 and sold when it fell back below.

## Trading Relevance

Despite its name, CCI is widely used across stocks, forex, and crypto — not just commodities. It is particularly effective for identifying the start and end of cyclical price movements and works well in conjunction with [[trend]] analysis. Practitioners frequently pair CCI with a longer-term trend filter (e.g. the 200-day [[moving-averages|MA]]) so that ±100 crosses are only taken in the direction of the dominant trend, and with a separate [[momentum]] confirmation such as [[macd|MACD]] or [[rsi|RSI]]. A popular two-timeframe approach uses a higher-timeframe CCI for trend direction and a lower-timeframe CCI for entry timing.

## Common Pitfalls

- **Treating ±100 as automatic reversal levels.** In strong trends CCI can sit above +100 (or below −100) for extended stretches; fading every such reading bleeds capital. Always condition the signal on the trend regime.
- **Short lookbacks whipsaw.** Small `n` produces a hyperactive line full of false zero-line crosses; longer `n` lags. Lambert's 20 is a compromise, not a law.
- **Confusing mean deviation with standard deviation.** CCI uses *average absolute* deviation; substituting standard deviation changes the scaling and breaks the ±100 convention.
- **Low standalone win rate.** Like other trend-following tools, CCI generates many small losses and a few large wins (see *Backtesting Evidence* below) — judge it on risk-adjusted return, not hit rate.

## About the Creator

[[donald-lambert|Donald Lambert]] introduced CCI in *Commodities* magazine in 1980, originally designed to identify cyclical turns in commodity markets. Despite its commodity-focused origins, CCI is now used broadly across stocks, forex, and crypto (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study across US equities reported CCI(20) with a 35.1% win rate — among the lowest of the indicators tested. The low win rate reflects CCI's trend-following characteristics: like MACD, it generates most P&L from infrequent large winners rather than consistent small gains. CCI's value is better judged by risk-adjusted returns than by win rate alone (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Limitations

Like most [[oscillators]], CCI generates frequent false signals in strongly trending markets. An "overbought" reading in an uptrend does not necessarily mean price will reverse — it may simply indicate strong momentum. The unbounded scale also means there is no fixed "maximum" extreme to anchor against, so context (trend regime, [[volume]], [[support-and-resistance]]) is essential. Always use additional context and confirmation.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h high/low/close for the current typical price

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV bars (high, low, close feed the typical price)
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100`, form TP = (H+L+C)/3 and apply Lambert's formula with n = 20 and the 0.015 constant
- **Regime gate** — condition ±100 crosses on trend state from `GET /api/v1/indicators/signum-rgg`: follow crosses in GREEN/RED trends, fade extremes only in GREY chop — the trend-vs-range flip this page stresses
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) covers full cycles; expect the low-win-rate, fat-winner profile documented above
- **Tip** — CCI is unbounded, so normalise extremes per asset (e.g. a rolling percentile of readings) before comparing signals across the universe

## Related

- [[donald-lambert]] — CCI's creator
- [[oscillators]] — the broader indicator family CCI belongs to
- [[rsi]] — bounded momentum oscillator often used alongside CCI
- [[stochastic]] — another bounded oscillator for overbought/oversold
- [[macd]] — trend/momentum confirmation pairing
- [[divergence]] — the primary CCI warning pattern
- [[momentum]] — the property CCI measures
- [[trend]] — the regime that flips CCI between fade and follow

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Lambert attribution, *Commodities* magazine publication, win-rate data.
- Lambert, D. (1980), "Commodity Channel Index: Tools for Trading Cyclic Trends," *Commodities* magazine — the original publication introducing CCI.
- General market knowledge — formula derivation, mean-deviation vs. standard-deviation distinction, and trend-vs-range interpretation are standard technical-analysis material.
