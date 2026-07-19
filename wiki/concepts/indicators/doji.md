---
title: "Doji"
type: concept
created: 2026-07-01
updated: 2026-07-19
status: review
tags: [indicators, technical-analysis]
aliases: ["Doji", "Doji Candle", "Doji Candlestick", "Gravestone Doji", "Dragonfly Doji", "Long-Legged Doji"]
domain: [indicators]
prerequisites: ["[[candlestick-patterns]]", "[[technical-analysis]]"]
difficulty: beginner
related: ["[[candlestick-patterns]]", "[[hammer]]", "[[pin-bar]]", "[[evening-star]]", "[[reversal-patterns]]", "[[support-and-resistance]]", "[[technical-analysis]]", "[[price-action]]", "[[trading-volume]]", "[[consolidation]]", "[[munehisa-homma]]"]
---

A **doji** is a single [[candlestick-patterns|candlestick]] in which the open and close are virtually equal, producing a tiny (or non-existent) real body that looks like a cross, plus sign, or thin horizontal line. It represents a session of **indecision** — buyers and sellers fought to an effective stalemate, ending the period roughly where it began. A doji is not directional on its own; its meaning comes entirely from where it appears (after an extended [[trend]], at [[support-and-resistance|support/resistance]]) and from the candle that follows it.

## How It Works

The defining feature is a **negligible real body**: |close − open| is close to zero relative to the candle's total range. The wicks (shadows) can be any length, and their geometry defines the doji's variants. Because the session opened and closed at nearly the same price despite intraday movement, the market has signalled that the prevailing pressure may be weakening — a potential pause or [[reversal-patterns|reversal]] point, especially after a strong directional run.

A doji is meaningful only **in context**:

- After a sustained [[trend|uptrend]] or downtrend it warns that momentum is stalling.
- Inside a [[consolidation|range]] or chop it is common noise and carries little information.
- At a tested [[support-and-resistance]] level or [[confluence]] zone it gains weight.

### Recognition Criteria (Checklist)

| Criterion | Requirement |
|---|---|
| **Real body** | Open ≈ close; body is a thin line, ideally < ~5–10% of the candle's range |
| **Context** | Most informative after an extended trend or at a key level |
| **Shadows** | Any length; their shape determines the variant (see below) |
| **Confirmation** | The *next* candle should resolve the indecision (close beyond the doji's range) |
| **Participation** | Higher [[trading-volume]] makes the indecision more significant |

### Doji Variants

| Variant | Shape | Typical reading |
|---|---|---|
| **Standard / common doji** | Small upper and lower wicks, body a cross | General indecision |
| **Long-legged doji** | Long wicks both sides, body in the middle | Violent two-way fight, strong indecision |
| **Dragonfly doji** | Long *lower* wick, little/no upper wick, body at the top | Sellers rejected; potential bullish reversal after a downtrend (cousin of the [[hammer]]) |
| **Gravestone doji** | Long *upper* wick, little/no lower wick, body at the bottom | Buyers rejected; potential bearish reversal after an uptrend (cousin of the shooting star) |
| **Four-price doji** | Open = high = low = close, a single horizontal line | Extreme illiquidity or a very quiet period; often a data artifact |

## Worked Example

*(Illustrative, not from a specific source.)*

A stock has rallied from 80 to 100 over three weeks. The next session opens at 100.10, trades as high as 101.50 and as low as 98.80, then closes at 100.05.

- Body: |100.10 − 100.05| = **0.05**
- Total range: 101.50 − 98.80 = **2.70**
- Body-to-range ratio = 0.05 / 2.70 ≈ **1.9%** — a clear doji.

After a strong uptrend, this long-legged doji says buyers could no longer extend the advance and the session ended in deadlock. A trader would **not** act on the doji alone. They would wait for the *next* candle: a close below 98.80 (the doji's low) would confirm a possible reversal and offer an entry with a stop above 101.50 (the doji's high); a close back above 101.50 would instead suggest the uptrend is resuming. The doji marks the *decision point*; the following candle casts the deciding vote.

## How Traders Use It

A doji is a **timing and location cue**, not a standalone signal. Practitioners typically:

1. **Demand context** — only weigh a doji that appears after a stretched trend or at a known level.
2. **Wait for confirmation** — the next candle (or two) must resolve the indecision before acting.
3. **Combine with structure** — a doji at [[support-and-resistance]], a trendline, or a [[fibonacci-extensions|Fibonacci]] level carries more weight (see [[confluence]]).
4. **Use the doji's range for risk** — the high/low of the doji often provides a natural stop placement.

Dojis are building blocks of larger candle formations: a doji is the middle candle of the [[evening-star]]/morning-star, and the dragonfly/gravestone variants overlap conceptually with the [[hammer]] and shooting star. The candlestick tradition is widely credited to Japanese rice trader [[munehisa-homma]].

## Doji vs Look-Alike Candles

| Candle | Body | Distinguishing feature | Implication |
|---|---|---|---|
| **Doji** | Negligible (open ≈ close) | Cross/plus shape | Indecision; needs context + confirmation |
| **[[hammer]]** | Small but real, at top of range | Long lower wick | Directional rejection (bullish in a downtrend) |
| **Spinning top** | Small *but visible* body | Wicks both sides | Mild indecision (weaker than a doji) |
| **[[pin-bar]]** | Small, at one end | One dominant wick | Generalised rejection candle |

The key distinction from a hammer or spinning top is the **absence of a real body**: a doji signals a true stalemate (open = close), whereas a hammer/pin-bar shows directional rejection (close pushed away from the wick).

## Common Pitfalls and False Signals

- **Trading the doji alone.** Without the confirming next candle, a doji is just a pause; acting on it pre-emptively invites [[false-signals|whipsaws]].
- **Ignoring context.** Dojis appear constantly inside ranges and on quiet days, where they carry no edge. Their information content lives at trend extremes and key levels.
- **Low-volume dojis.** A doji on thin [[trading-volume]] reflects little real participation and is more likely to be noise.
- **Lower-timeframe overload.** Intraday charts print dojis incessantly; they are far more reliable on daily/weekly timeframes.
- **The four-price doji trap.** A single-line doji often just signals illiquidity or a bad data print, not a meaningful market message.

## Sources

- Steve Nison, *Japanese Candlestick Charting Techniques* (1991) — the foundational Western reference on the doji and its variants.
- Thomas Bulkowski, *Encyclopedia of Candlestick Charts* — statistical study of candlestick pattern reliability.
- General market knowledge; the worked example above is illustrative, not from a specific ingested source.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=2` — latest candles for a live doji check

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV for pattern scans
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=2"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this pattern directly:

- **Compute** — flag bars where |close − open| / (high − low) < ~0.1 in `GET /api/v1/market-data/klines` output, then classify the variant from wick geometry (dragonfly, gravestone, long-legged)
- **Context gate** — only score dojis after an extended run or at a tested level; quantify "extended" as N consecutive closes in one direction before the doji
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) measures confirmation-candle follow-through rates by variant and context
- **Tip** — 24/7 crypto daily bars are arbitrary UTC slices with no true session close, so weigh a daily doji more lightly than its equity equivalent and always require the next-candle confirmation, as the page insists

## Related

- [[candlestick-patterns]] — the broader family of candle formations
- [[hammer]] — a single-candle rejection pattern often confused with a doji
- [[pin-bar]] — the generalised single-wick rejection candle
- [[evening-star]] — a three-candle pattern that often centres on a doji
- [[reversal-patterns]] — the category a confirmed doji can signal
- [[support-and-resistance]] — context that gives a doji meaning
- [[price-action]] — the discipline of reading candles like the doji
- [[trading-volume]] — confirmation dimension for a significant doji
- [[consolidation]] — where stray dojis are usually just noise
- [[munehisa-homma]] — the trader credited with candlestick analysis
