---
title: "Hammer"
type: concept
created: 2026-04-15
updated: 2026-07-19
status: excellent
tags: [indicators, technical-analysis]
aliases: ["Hammer", "Hammer Candlestick", "Inverted Hammer", "Hanging Man"]
domain: [indicators]
prerequisites: ["[[candlestick-patterns]]", "[[technical-analysis]]"]
difficulty: beginner
related: ["[[candlestick-patterns]]", "[[reversal-patterns]]", "[[support-and-resistance]]", "[[pin-bar]]", "[[technical-analysis]]", "[[bullish-engulfing]]", "[[doji]]", "[[volume]]"]
---

A hammer is a single-candle **bullish [[reversal-patterns|reversal pattern]]** in [[candlestick-patterns|candlestick analysis]]: a small body sitting at the top of the candle's range with a long lower wick (shadow) at least twice the length of the body, and little or no upper wick. The shape tells a story of rejection — sellers pushed price sharply lower during the session, but buyers absorbed the selling and drove price back up to close near the open, suggesting demand has stepped in at lower levels.

## How It Works

The defining geometry:

- **Body** — small, located in the upper third of the range. Colour (bullish green / bearish red) is secondary; a green-bodied hammer (close > open) is marginally more bullish.
- **Lower wick** — long, ideally ≥ 2× the body height. This is the "failed" sell-off.
- **Upper wick** — minimal or absent (no more than ~10% of the range).

The pattern is meaningful only **in context**: it must appear after a measurable downtrend or at a known [[support-and-resistance|support]] level. A hammer floating in the middle of a range carries little information. The long lower wick represents a probe to lower prices that buyers fully reversed — evidence that the supply/demand balance may be shifting toward bulls.

### Recognition Criteria (Checklist)

| Criterion | Requirement |
|---|---|
| **Prior trend** | A clear preceding downtrend (or test of support) — context is mandatory |
| **Real body** | Small; positioned in the upper third of the total range |
| **Lower shadow** | Long; at least 2× the body height (3× is higher quality) |
| **Upper shadow** | Little to none |
| **Body colour** | Either, but bullish (close > open) is slightly preferred |
| **Confirmation** | Next candle closes above the hammer's body (ideally on rising [[volume]]) |

### Worked Example

A stock has fallen from 50 to 40 over two weeks. On the next session it opens at 40.20, sellers drive it down to a low of 38.00, but buyers reverse the move and it closes at 40.00.

- Body: |40.20 − 40.00| = **0.20**
- Lower wick: 40.00 (close, the body bottom) − 38.00 = **2.00**
- Upper wick: 40.20 (high?) — here the high equals the open, so ~0

Lower-wick-to-body ratio = 2.00 / 0.20 = **10×**, far exceeding the 2× minimum, with no upper wick — a textbook hammer at the bottom of a downtrend. A trader would wait for the *next* candle to close above 40.20 before going long, place the stop just below 38.00 (the wick low), and target the prior swing high or a measured move. The setup risks ~2 points to reach for a multi-point reversal — the favourable, defined-risk structure that makes the pattern attractive.

### Variants

- **Inverted hammer** — small body at the *bottom* of the range with a long *upper* wick, appearing after a downtrend. Same bullish implication (sellers could not hold the lows of the candle), but it requires stronger confirmation.
- **Hanging man** — structurally identical to the standard hammer but appearing at the *top* of an uptrend. The long lower wick signals that sellers are beginning to challenge the bulls; it is a bearish warning.
- **Doji / [[pin-bar]]** — the [[pin-bar]] (Western terminology) generalises the hammer and inverted hammer; a [[doji]] has essentially no body and signals indecision rather than directional rejection.

## Trading Relevance

A hammer is a **timing and location signal**, not a standalone system. Practitioners typically:

1. Wait for the **next candle to close above the hammer's body** before going long — an unconfirmed hammer that is followed by another decline ("failed hammer") is common.
2. Require **elevated [[trading-volume|volume]]** on the hammer candle, indicating the rejection involved real participation.
3. Place the **stop-loss below the hammer's low** (the wick extreme), giving a defined, often tight, risk.
4. Confirm with surrounding [[technical-analysis]] context — a hammer at a multi-touch support level or after a stretched downtrend is far higher quality than one in noise.

Because the pattern offers a precise invalidation point (the low of the wick), it gives a favourable risk/reward structure when it works: small defined risk against the potential of a trend reversal. It is widely used in [[swing-trading]] and intraday reversal setups across stocks, [[forex]], and [[crypto]].

## Hammer vs Look-Alike Candles

| Pattern | Body location | Long wick | Where it appears | Implication |
|---|---|---|---|---|
| **Hammer** | Top of range | Lower | Bottom of downtrend | Bullish reversal |
| **Hanging man** | Top of range | Lower | Top of uptrend | Bearish warning |
| **Inverted hammer** | Bottom of range | Upper | Bottom of downtrend | Bullish reversal (needs confirmation) |
| **Shooting star** | Bottom of range | Upper | Top of uptrend | Bearish reversal |
| **[[doji]]** | Negligible body | Either/both | Anywhere | Indecision, not directional |
| **[[pin-bar]]** | Either end | Either | Anywhere | Generalised rejection candle |

The same geometry carries opposite meaning depending on the preceding trend — this is why **location is the pattern**, and a hammer read without its context is meaningless.

## Common Pitfalls

- **Ignoring context.** A small-body, long-lower-wick candle in the middle of a range or *during* an uptrend is not a hammer signal — it may even be a bearish hanging man.
- **Trading unconfirmed.** "Failed hammers" (no follow-through, next candle declines) are common. Waiting for a confirming close above the body filters many false signals at the cost of a slightly worse entry.
- **Low-volume hammers.** A rejection on thin volume reflects little real participation; demand confirmation with elevated [[volume]].
- **Over-tight stops.** Placing the stop at the body rather than below the wick low invites being shaken out on a normal retest of the lows. The wick extreme is the true invalidation.
- **Tiny-range candles.** On very low-volatility bars the "2× body" rule is trivially met by noise. The candle should also be of meaningful size relative to recent range.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=100` — OHLCV bars whose open/high/low/close geometry defines the hammer
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=4h&limit=100` — the same detection on Hyperliquid perp listings
- `GET /api/v1/market-data/volume-history?days=30` — daily volume with buy ratio to confirm real participation on the rejection candle

**Historical data:**
- `GET /api/v1/backtesting/klines` — full kline archive (Binance spot 1h/4h/1d back to 2017-08) for pattern-frequency and hit-rate studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=100"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Detect** — fetch bars via `GET /api/v1/market-data/klines` and apply the geometry checklist above (lower wick ≥ 2× body, body in the upper third, minimal upper wick) plus the mandatory prior-downtrend context test
- **Confirm** — only signal after the next candle closes above the hammer body; compare the hammer bar's volume to its 20-bar average from the same kline payload
- **Backtest** — replay detection over `GET /api/v1/backtesting/klines` (1h/4h/1d Binance spot back to 2017-08) and score follow-through against the "failed hammer" base rate per timeframe
- **Tip** — crypto wicks are frequently liquidation artifacts; cross-check large lower wicks against `GET /api/v1/market-intelligence/liquidations` — a wick made of forced selling is the strongest version of the rejection story

## Sources

- Steve Nison, *Japanese Candlestick Charting Techniques* (1991) — the foundational Western reference on the hammer, hanging man, and inverted hammer.
- Thomas Bulkowski, *Encyclopedia of Candlestick Charts* — statistical study of candlestick pattern reliability.

## Related

- [[candlestick-patterns]] — the broader family of candle formations
- [[reversal-patterns]] — the category the hammer belongs to
- [[pin-bar]] — the generalised single-wick rejection candle
- [[support-and-resistance]] — context that validates a hammer
- [[bullish-engulfing]] — a two-candle bullish reversal alternative
- [[doji]] — indecision candle often confused with reversal candles
- [[volume]] — confirmation dimension for a high-quality hammer
