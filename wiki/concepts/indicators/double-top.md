---
title: "Double Top and Double Bottom"
type: concept
created: 2026-06-30
updated: 2026-07-19
status: review
tags: [indicators, technical-analysis]
aliases: ["Double Top", "Double Bottom", "M pattern", "W pattern", "double-bottom", "double top and bottom"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]", "[[support-and-resistance]]"]
difficulty: beginner
related: ["[[head-and-shoulders]]", "[[support-and-resistance]]", "[[trading-volume]]", "[[trend]]", "[[divergence]]", "[[breakout]]", "[[swing-high]]", "[[swing-low]]", "[[chart-patterns]]", "[[false-signals]]", "[[market-structure]]", "[[wedge]]"]
---

A **double top** is a bearish [[chart-patterns|reversal pattern]] in which price makes two distinct peaks at roughly the same level, separated by a moderate trough, signalling that an [[trend|uptrend]] has failed to push to new highs and may reverse. Its mirror image, the **double bottom**, is a bullish reversal made of two troughs at a similar level with a peak between them. The double top resembles the letter "M"; the double bottom resembles a "W". Both are pure [[market-structure]] patterns built from [[swing-high|swing highs]] and [[swing-low|swing lows]], and they sit in the same reversal family as the [[head-and-shoulders]].

## Structure

**Double top (M):**

1. **First peak** — price rises to a high ([[swing-high]]) on strong [[trading-volume|volume]], then pulls back.
2. **Intervening trough** — a reaction low (the "valley"); the line through it is the **[[support-and-resistance|support]]** (sometimes called the neckline).
3. **Second peak** — price rallies again but stalls at roughly the same level as the first peak (often on *lighter* volume — an early divergence warning), then turns down.
4. **Confirmation** — the pattern completes only when price **closes below the intervening trough's low**, ideally on expanding volume. Until that break, it is just two highs and could resume the uptrend.

**Double bottom (W)** is the same logic inverted: two troughs at a similar level, a peak between them, and confirmation on a **close above the middle peak's high**.

### Anatomy at a Glance (double top)

| Component | What it is | Typical volume | Trader's read |
|---|---|---|---|
| First peak | End of prior [[trend\|uptrend]] | High | Strong demand, then profit-taking |
| Trough (valley) | Reaction low between peaks | Falling | Defines the [[support-and-resistance\|support]] line |
| Second peak | Retest of the first high | Lower | Buyers fail to make a new high — exhaustion |
| Support break | Close below the trough low | Rising (ideal) | Confirmation; [[support-and-resistance\|support flips to resistance]] |

## How It Works

The two peaks mark a level where supply repeatedly overwhelms demand: buyers cannot drive price above the prior high, so the [[trend|uptrend]] stalls. The second peak forming on lighter volume, or with a lower reading on a momentum indicator like the [[relative-strength-index|RSI]], is a classic [[divergence]] that hints the rally is weakening. The break of the intervening trough confirms that demand can no longer hold support, flipping that level into [[support-and-resistance|resistance]].

## Measured-Move Target

The conventional target equals the pattern's height — the distance from the peaks down to the intervening trough — projected from the breakdown point:

```
# Double top (bearish)
height = peak_level − trough_low
target = trough_low − height        # projected DOWN from the support break

# Double bottom (bullish)
height = peak_between − trough_level
target = peak_between + height       # projected UP from the resistance break
```

This is a *first* objective, not a ceiling. As with the [[head-and-shoulders]], the height is the largest vertical distance in the pattern.

## Worked Example (illustrative)

A stock tops out after an extended uptrend:

| Point | Price |
|---|---|
| First peak | $52.00 |
| Intervening trough (support) | $48.00 |
| Second peak | $51.80 |
| Confirmed close below support | $47.50 |

- **Pattern height** = $52.00 − $48.00 = **$4.00**.
- **Measured target** = support ($48.00) − height ($4.00) = **$44.00**.
- **Entry** = $47.50 on the close below the $48 trough (or on a retest of $48 from below for a tighter stop).
- **Stop** = just above the second peak (~$52.10): if price reclaims the peaks, the pattern has failed.

(Illustrative numbers only — not a recommendation or a backtest result.)

## How Traders Use It

- **Entry** — on the confirmed support break (double top) or resistance break (double bottom), or on a retest of the broken level for better risk/reward.
- **Stop** — above the second peak (double top) or below the second trough (double bottom).
- **Confirmation** — pair the break with [[trading-volume]] expansion and [[divergence]] on a momentum oscillator; the more the two peaks/troughs align and the cleaner the break, the higher the reliability.
- **Timeframe** — like most classical patterns, double tops/bottoms are materially more reliable on daily/weekly charts than on noisy intraday data.

## Common Pitfalls and Risks

- **Trading before confirmation.** Two peaks at a similar level are *not* a double top until price closes below the intervening trough. Anticipating the reversal at the second peak risks the "top" simply becoming a higher high that resumes the [[trend|uptrend]].
- **Failed breaks / [[false-signals]].** Price can break the trough and immediately reverse back inside the pattern — a [[whipsaw]]. A close-based break on rising volume, plus waiting for a retest, filters many of these.
- **Peaks rarely match exactly.** Real double tops have peaks within a few percent of each other, not at identical prices; demanding an exact match misses valid patterns, while accepting too much divergence catches noise.
- **Triple tops and rounded tops.** What looks like a double top can extend into a third peak; do not assume completion until the support break.
- **Clustered stops / stop-hunting.** Because so many traders watch the same trough level, stops cluster there and liquidity hunts ([[false-signals|fakeouts]]) are common before the genuine move.

## Sources

- Robert D. Edwards & John Magee, *Technical Analysis of Stock Trends* — canonical treatment of double tops and bottoms.
- John J. Murphy, *Technical Analysis of the Financial Markets* — reversal patterns, volume confirmation, and measured-move targets.
- General market knowledge; the worked example above is illustrative, not from a specific ingested wiki source.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — OHLCV for swing-pivot detection
- `GET /api/v1/market-data/volume-history?days=90` — volume for peak and break confirmation
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this pattern directly:

- **Detect** — find swing pivots in `GET /api/v1/market-data/klines` output and flag two highs within a small tolerance (~2-3%) separated by a trough; confirm only on a close below the trough
- **Confirm** — compare the second peak's volume against the first via `GET /api/v1/market-data/volume-history`; a lighter second peak is the early divergence warning described above
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) measures completion rates and measured-move accuracy over full cycles
- **Tip** — crypto's stop-hunting around obvious trough levels is severe; test entering on the retest of the broken level rather than the first break to filter the fakeouts the page warns about

## Related

- [[head-and-shoulders]] — a related (three-peak) reversal pattern
- [[chart-patterns]] — the broader catalogue of price patterns
- [[support-and-resistance]] — the trough/peak level whose break confirms the pattern
- [[trading-volume]] — volume confirmation is central to the pattern
- [[divergence]] — a lighter-volume or lower-RSI second peak is a classic divergence
- [[trend]] — the prior trend the pattern reverses
- [[swing-high]] / [[swing-low]] — the pivots the pattern is built from
- [[false-signals]] — failed support/resistance breaks are a classic fakeout
- [[wedge]] — a converging-trendline pattern that can also resolve as a reversal
