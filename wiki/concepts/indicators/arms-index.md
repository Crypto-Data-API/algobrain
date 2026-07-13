---
title: "Arms Index (TRIN)"
type: concept
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [indicators, technical-analysis, volume, liquidity]
aliases: ["TRIN", "Arms Index", "Trading Index", "Short-Term Trading Index", "arms-index"]
domain: [indicators, market-microstructure]
prerequisites: ["[[market-breadth]]", "[[volume]]"]
difficulty: intermediate
related: ["[[richard-arms]]", "[[market-breadth]]", "[[trin]]", "[[mcclellan-oscillator]]", "[[volume]]", "[[advance-decline-line]]"]
---

The Arms Index, also known as **TRIN** (Trading Index or Short-Term Trading Index), is a [[market-breadth]] indicator created by [[richard-arms|Richard Arms]] in 1967. It measures the relationship between advancing/declining issues and advancing/declining [[volume]] to gauge whether buying or selling pressure is broadly distributed across the market or concentrated in a few names (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). Because it folds conviction (volume) into participation (issue count), TRIN captures something a raw [[advance-decline-line|advance/decline count]] cannot: the *quality* of a rally or selloff.

## The Formula

The Arms Index is a **ratio of two ratios**:

```
            (Advancing Issues / Declining Issues)
TRIN  =  ---------------------------------------------
            (Advancing Volume / Declining Volume)
```

The numerator (the **AD ratio**) measures breadth: how many stocks are up versus down. The denominator (the **volume ratio**) measures where the volume is going. Dividing one by the other answers: *is the volume flowing into the advancers in proportion to how many advancers there are?*

- If volume is perfectly proportional to the advance/decline split, the two ratios are equal and **TRIN = 1.0**.
- If advancing stocks are attracting *more* than their proportional share of volume, the denominator outruns the numerator and **TRIN falls below 1.0** (bullish — money is committed to the gainers).
- If declining stocks are absorbing disproportionate volume, the denominator shrinks and **TRIN rises above 1.0** (bearish — money is committed to the losers).

> **The counter-intuitive convention:** lower TRIN is bullish, higher TRIN is bearish. This inversion trips up newcomers and is the single most important thing to memorize about the indicator (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

### Worked Example

Suppose on the NYSE at midday:

| Component | Value |
|---|---|
| Advancing issues | 1,800 |
| Declining issues | 1,200 |
| Advancing volume | 900M shares |
| Declining volume | 1,500M shares |

Step 1 — AD ratio: 1,800 / 1,200 = **1.50**
Step 2 — Volume ratio: 900 / 1,500 = **0.60**
Step 3 — TRIN: 1.50 / 0.60 = **2.50**

Interpretation: more stocks are up than down (breadth is positive), yet the *volume* is pouring into the decliners. TRIN at 2.50 is a strongly bearish internal reading — the advance is broad but hollow, and the heavy down-volume warns the rally is not supported by real commitment. A reading this elevated also flags possible **short-term selling exhaustion** (see contrarian use below).

## Reading the Scale

| TRIN reading | Internal condition | Typical interpretation |
|---|---|---|
| **< 0.50** | Volume heavily favors advancers | Strong bullish breadth; at extremes, possible buying climax / overbought |
| **0.50 – 0.90** | Advancing volume leads | Bullish bias |
| **~1.00** | Volume proportional to breadth | Neutral / balanced tape |
| **1.00 – 2.00** | Declining volume leads | Bearish bias |
| **> 2.00** | Volume heavily favors decliners | Strong bearish breadth; at extremes, possible selling climax / capitulation |
| **> 3.00** | Indiscriminate panic selling | Often near-term capitulation bottom (contrarian buy zone) |

These thresholds are conventions, not hard rules — the meaningful band differs between the NYSE and NASDAQ and between intraday and end-of-day readings. Many traders smooth the raw number with a moving average (e.g., the **Open TRIN / open arms index** uses cumulative sums, and a 10-day moving average of closing TRIN is a classic intermediate-term breadth gauge).

## Key Signals

- **Extremes mark exhaustion.** Readings above ~2.0 (panic selling) or below ~0.50 (euphoric buying) often coincide with short-term turning points rather than continuation.
- **Contrarian capitulation buys.** A TRIN spike above 2.5–3.0 during a sharp selloff signals indiscriminate, panic-driven selling and is one of the classic markers of a capitulation low — used by mean-reversion and index traders as a contrarian buy filter.
- **Confirmation, not standalone.** Best read alongside the [[mcclellan-oscillator|McClellan Oscillator]] and [[advance-decline-line]] for a complete internals picture. TRIN answers "where is the volume?"; the AD line answers "how broad is the move?"; together they confirm or contradict the index price.

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## How Traders Use It

Primarily used by **index, futures, and options traders** monitoring NYSE or NASDAQ market internals in real time. Practical applications:

1. **Intraday tape gauge.** Day traders keep TRIN on a watchlist as a live read on conviction. A TRIN sliding steadily below 1.0 through the morning confirms a healthy trend day to the upside; a TRIN that refuses to drop on a green index warns the rally is thin and prone to reversal.
2. **Divergence with price.** If the index is making new highs but TRIN is also rising (toward/above 1.0), the up-move is losing volume support — a non-confirmation similar in spirit to an [[relative-strength-index|RSI]] or [[money-flow-index|MFI]] divergence but at the whole-market level.
3. **Capitulation timing.** Combined with a [[vix]] spike and heavy down-volume, an extreme TRIN print helps time entries into oversold bounces.
4. **Smoothed breadth regime.** A 10-day moving average of closing TRIN persistently above 1.0 indicates an environment where rallies keep failing — a [[market-regime]] filter for tilting toward defensive or [[mean-reversion]] tactics.

## Common Pitfalls

- **Forgetting the inversion.** The most frequent error is reading high TRIN as bullish. Lower is stronger.
- **Reading single prints in a vacuum.** Intraday TRIN is noisy; the open-of-day value is often distorted. Trends in TRIN and smoothed averages are more reliable than spot readings.
- **Exchange mismatch.** NYSE TRIN and NASDAQ TRIN behave differently because NASDAQ breadth is dominated by small, illiquid names; do not apply NYSE thresholds to NASDAQ.
- **Treating extremes as immediate reversal triggers.** An extreme TRIN flags *potential* exhaustion, not a precise turn — markets can stay panicked. Use it as a contrarian *filter*, paired with a price trigger and a stop.
- **Capitalization weighting blind spot.** Because volume is share-count based, a few mega-cap stocks with huge volume can dominate the volume ratio and distort the read versus the breadth picture.

## Trading Relevance

Because TRIN combines breadth (issues) with conviction (volume), it adds a dimension that a raw advance/decline count misses: a market can be up on net advancers but with weak volume behind the gainers (TRIN > 1), warning that the rally lacks participation. Intraday traders use TRIN as a real-time tape gauge — a TRIN spiking above 2-3 during a selloff often coincides with panic-driven, indiscriminate selling and flags potential short-term exhaustion. The signal is most actionable at extremes and is typically combined with the [[mcclellan-oscillator]] and [[advance-decline-line]] for confirmation rather than traded in isolation. Note the inverse convention: the Arms Index is one of the few indicators where lower readings are bullish.

## TRIN vs Other Breadth Tools

| Indicator | What it measures | Strength | Limitation |
|---|---|---|---|
| **Arms Index / TRIN** | Volume-weighted breadth (issues ÷ volume ratio) | Captures conviction behind a move; great at extremes | Counter-intuitive scale; noisy intraday |
| [[advance-decline-line]] | Cumulative net advancers | Clean trend of participation | Ignores volume / conviction |
| [[mcclellan-oscillator]] | EMA-smoothed breadth momentum | Smooths noise; good for divergences | Slower, lagging |
| **Up/Down volume ratio** | Just the volume side | Direct read on volume flow | Ignores issue count |

TRIN is essentially the [[advance-decline-line|AD breadth]] and the up/down volume ratio combined into one number, which is why it is favored when a trader wants a single real-time gauge of internal health.

## Sources

- Arms, Richard W. Jr. (1989), *The Arms Index (TRIN): An Introduction to the Volume Analysis of Stock and Bond Markets* (Dow Jones-Irwin) — the original book-length treatment by the indicator's creator.
- Murphy, John J. (1999), *Technical Analysis of the Financial Markets* (NYIF) — covers TRIN within the market-internals/breadth toolkit.
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)

## Related

- [[richard-arms]]
- [[market-breadth]]
- [[mcclellan-oscillator]]
- [[volume]]
