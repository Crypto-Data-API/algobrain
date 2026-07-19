---
title: "Wedge Patterns (Rising and Falling)"
type: concept
created: 2026-06-30
updated: 2026-07-19
status: review
tags: [indicators, technical-analysis]
aliases: ["Rising Wedge", "Falling Wedge", "Wedge Pattern", "wedge-pattern"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]", "[[trend]]", "[[support-and-resistance]]"]
difficulty: intermediate
related: ["[[chart-patterns]]", "[[flags-and-pennants]]", "[[ascending-triangle]]", "[[trend]]", "[[trading-volume]]", "[[breakout]]", "[[trendline]]", "[[support-and-resistance]]", "[[divergence]]", "[[false-signals]]", "[[double-top]]"]
---

A **wedge** is a chart pattern bounded by two converging [[trendline|trendlines]] that *both slope in the same direction*. A **rising wedge** has both lines sloping up (and is generally bearish); a **falling wedge** has both lines sloping down (and is generally bullish). The shared-direction slope is what distinguishes a wedge from a [[ascending-triangle|triangle]] (which has at least one roughly flat boundary) and from a [[flags-and-pennants|flag or pennant]] (which is shorter and slopes *against* the prior move). Wedges can act as either reversal or continuation patterns depending on context.

## Structure

- **Rising wedge** — price makes higher highs and higher lows, but the lower [[trendline|support line]] rises *faster* than the upper resistance line, so the two converge upward. The narrowing range and slowing upside momentum hint that buyers are losing steam; the expected resolution is a **breakdown below support**. It is most bearish when it appears at the end of an uptrend (reversal), but also forms as a bearish continuation during a downtrend's counter-rally.
- **Falling wedge** — price makes lower highs and lower lows, but the upper resistance line falls *faster* than the lower support line, so they converge downward. Selling momentum is fading; the expected resolution is a **breakout above resistance**. Most bullish at the end of a downtrend (reversal), but also forms as a bullish continuation during an uptrend's pullback.

[[trading-volume|Volume]] typically *declines* as the wedge develops (range contracts) and should *expand* on the breakout/breakdown to confirm it.

### Anatomy at a Glance

| Feature | Rising wedge | Falling wedge |
|---|---|---|
| Both trendlines slope | Up | Down |
| Which line is steeper | Lower (support) | Upper (resistance) |
| Bias | Bearish | Bullish |
| Expected resolution | Break **down** through support | Break **up** through resistance |
| Volume into the apex | Declining | Declining |
| Confirmation | Close below support on rising volume | Close above resistance on rising volume |

## How It Works

The converging lines show a range that is *narrowing while still trending*. In a rising wedge, each new high is only marginally above the last even as the lows keep climbing — buyers are paying up for progressively smaller gains, a momentum exhaustion signal often accompanied by bearish [[divergence]] on an oscillator like the [[relative-strength-index|RSI]]. The falling wedge is the inverse: sellers drive lower lows but with shrinking follow-through, setting up a bullish reversal.

## Measured-Move Target

A common (rule-of-thumb) target projects the **maximum height of the wedge** — the widest vertical distance between the two trendlines, usually near the start of the pattern — from the breakout point:

```
height = (upper line − lower line) at the wedge's widest part
# Falling wedge (bullish):  target = breakout_price + height
# Rising wedge  (bearish):  target = breakdown_price − height
```

This is a first objective, not a guarantee. Some traders instead target a return to the level where the wedge began.

## Worked Example (illustrative)

A stock in a downtrend carves a falling wedge: the upper line drops from $30 to $26 while the lower line drops only from $27 to $25, converging near $25.50. The widest part of the wedge spans about $3 (≈ $30 − $27 early on). Price then closes at **$26.20**, above the upper line, on a volume surge — confirmation.

- **Entry** = $26.20 on the breakout (or a retest of the broken upper line for a tighter stop).
- **Stop** = below the most recent low inside the wedge (~$25).
- **Measured target** = $26.20 + $3.00 ≈ **$29.20**.

(Illustrative numbers only — not a recommendation or a backtest result.)

## How Traders Use It

- **Entry** — on the confirmed [[breakout]] (falling wedge) or breakdown (rising wedge), or on a retest of the broken line for better risk/reward.
- **Stop** — beyond the opposite side of the wedge (below the last swing low for a falling-wedge long; above the last swing high for a rising-wedge short).
- **Confirmation** — require a close beyond the trendline on expanding [[trading-volume]]; look for supporting [[divergence]] and broader [[trend]] context.
- **Timeframe** — like other classical patterns, wedges are more reliable on daily/weekly charts than on noisy intraday data.

## Common Pitfalls and Risks

- **Direction ambiguity.** A wedge can resolve as a reversal *or* a continuation; the slope tells you the *likely* break direction, but you must wait for the actual break rather than assuming.
- **Subjective trendlines.** Which highs and lows you connect changes the wedge's shape, apex, and target. Different analysts draw different wedges; prefer obvious, well-tested touch points.
- **Premature entry and [[false-signals]].** Entering before the boundary breaks risks the pattern continuing or breaking the *other* way; close-based breaks on rising volume filter many [[whipsaw|whipsaws]].
- **Confusion with triangles and flags.** A wedge needs *both* lines sloping the same way; if one line is roughly flat it is a [[ascending-triangle|triangle]], and a brief counter-trend channel after a sharp move is a [[flags-and-pennants|flag]], not a wedge.
- **Volume that does not confirm.** A breakout on falling volume is suspect and raises the odds of a failed pattern.

## Sources

- General technical-analysis literature on classical chart patterns (rising and falling wedges as reversal/continuation formations). Structure, interpretation, and the worked example are standard material; the example uses illustrative numbers, not a specific ingested wiki source.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — OHLCV bars for detecting converging-trendline structure and the volume contraction into the apex

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep kline archive for measuring wedge resolution rates

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — detect wedges from `GET /api/v1/market-data/klines`: fit lines through recent swing highs and swing lows, require both slopes in the same direction with converging gap, and check the volume column for the decline-into-apex signature
- **Confirm** — the confirmation rule is fully mechanical on the same bars: a close beyond the boundary line with volume above its rolling average
- **Backtest** — measure actual break-direction and measured-move hit rates on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) before trusting the rising-bearish/falling-bullish convention on any given interval
- **Tip** — codify the trendline-subjectivity pitfall away: fix the pivot window and minimum-touch parameters up front, or two runs of the same agent will find different wedges on the same chart

## Related

- [[chart-patterns]] — the broader catalogue of price patterns
- [[flags-and-pennants]] — shorter continuation patterns that slope against the trend
- [[ascending-triangle]] — a triangle has a flat boundary; a wedge does not
- [[trendline]] — wedges are defined by two converging trendlines
- [[breakout]] — the trade trigger when a wedge resolves
- [[trading-volume]] — declines into the apex, expands on the break
- [[divergence]] — often accompanies a rising wedge's loss of momentum
- [[false-signals]] — premature or low-volume wedge breaks frequently fail
- [[double-top]] — a classic two-peak reversal pattern in the same family
