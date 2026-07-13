---
title: "Accumulation/Distribution Line"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [indicators, technical-analysis, volume]
aliases: ["A/D Line", "ADL", "Accumulation Distribution Line", "accumulation-distribution-line"]
domain: [indicators]
prerequisites: ["[[volume]]", "[[technical-analysis]]"]
difficulty: intermediate
related: ["[[volume]]", "[[obv]]", "[[chaikin-money-flow]]", "[[money-flow-index]]", "[[marc-chaikin]]", "[[divergence]]", "[[trend]]", "[[support-and-resistance]]", "[[trading-volume]]"]
---

The Accumulation/Distribution Line (A/D Line, or ADL) is a cumulative [[volume]]-based indicator developed by [[marc-chaikin|Marc Chaikin]] that estimates the flow of money into or out of a security. It weights each period's volume by *where the close falls inside the bar's high–low range*, then accumulates the result into a running line. A rising line implies net buying pressure (accumulation); a falling line implies net selling pressure (distribution). It is the foundation from which both [[chaikin-money-flow|Chaikin Money Flow]] and the Chaikin Oscillator are derived.

## How It Works

Each period the A/D Line is updated in three steps:

```
Money Flow Multiplier (MFM) = ((Close − Low) − (High − Close)) / (High − Low)
Money Flow Volume (MFV)     = MFM × Volume
A/D Line                    = previous A/D Line + MFV     (running cumulative total)
```

- The **Money Flow Multiplier** ranges from −1 to +1 and locates the close within the bar's range. A close at the high gives MFM = +1 (full accumulation); a close at the low gives MFM = −1 (full distribution); a close at the midpoint gives MFM = 0. If High = Low (no range), the multiplier is treated as 0.
- **Money Flow Volume** scales that multiplier by the period's [[volume]], so a strong close on heavy volume contributes far more than the same close on light volume.
- The line is **cumulative** — today's MFV is added to yesterday's total. Like [[obv|OBV]], its absolute value is arbitrary (it depends on the chosen starting point); only its *slope* and its *relationship to price* carry meaning.

### Worked Example (illustrative)

Two consecutive sessions:

| Session | High | Low | Close | Volume | MFM | MFV | A/D Line |
|---|---|---|---|---|---|---|---|
| 1 | 50 | 46 | 49 | 100,000 | +0.50 | +50,000 | +50,000 |
| 2 | 51 | 47 | 47.5 | 120,000 | −0.75 | −90,000 | −40,000 |

Session 1 closed in the upper part of its range on solid volume (accumulation, +50,000). Session 2 closed near its low on even heavier volume (distribution, −90,000), pulling the cumulative line negative. The line now slopes down — net distribution over the two bars. (Illustrative numbers only.)

## How to Read It

- **Slope is the signal.** A rising A/D Line says buyers are closing the security in the upper part of its range on meaningful volume; a falling line says sellers are closing it near the lows.
- **Confirmation.** When price and the A/D Line make new highs (or new lows) together, the move is well supported by volume.
- **[[divergence|Divergence]] — the highest-value signal.** If price makes a higher high while the A/D Line makes a lower high, the rally is running on weakening accumulation (bearish divergence). If price makes a lower low while the line makes a higher low, selling is losing conviction (bullish divergence).

## A/D Line vs. Related Volume Indicators

| Indicator | Built from | Bounded? | Key difference |
|---|---|---|---|
| **A/D Line** | MFM × volume, *cumulative* | No (running line) | Magnitude-aware via intrabar close location; ignores the prior close and gaps |
| **[[obv\|OBV]]** | full volume signed by close-vs-prior-close | No (running line) | Binary: uses only the *direction* of the close change, not the range location |
| **[[chaikin-money-flow\|CMF]]** | same MFM × volume, summed over N | −1 to +1 | The A/D Line normalized over a fixed window into an oscillator |
| **[[money-flow-index\|MFI]]** | typical-price money flow, RSI-style | 0 to 100 | A "volume-weighted RSI" with overbought/oversold bands |

The A/D Line and [[obv|OBV]] often disagree, and the disagreement is informative: OBV keys off the close-to-close *direction*, while the A/D Line keys off *where in the day's range* price closed. A stock that gaps up and closes mid-range adds positively to OBV but little to the A/D Line.

## Common Pitfalls and Risks

- **Ignores gaps and overnight moves.** The Money Flow Multiplier uses only the current bar's High, Low and Close — it never sees the gap between yesterday's close and today's open. A stock can gap up sharply, close mid-range, and register as *distribution*. This is the A/D Line's single biggest blind spot (compare [[obv|OBV]], which captures close-to-close direction).
- **Absolute level is meaningless.** The line's numeric value depends on an arbitrary start point; never compare A/D levels across securities or read into a specific number — only slope and [[divergence]] matter.
- **Divergences can persist.** Like most leading signals, an A/D divergence can run for weeks before price confirms; pair it with price [[trend]] structure rather than acting on it alone.
- **Illiquid / lumpy volume.** Sparse or erratic volume makes the volume weighting unreliable; the indicator assumes meaningful, comparable participation each period.
- **Not directional on its own.** A rising A/D Line inside a clear downtrend is a weak counter-signal, not a buy. Read it relative to [[trend]] and [[support-and-resistance]].

## Sources

- General technical-analysis literature on volume indicators (Marc Chaikin's accumulation/distribution methodology). Formula, interpretation, and the worked example above are standard material; the example uses illustrative numbers, not a specific ingested wiki source.

## Related

- [[marc-chaikin]] — developed the A/D Line, CMF, and the Chaikin Oscillator
- [[volume]] / [[trading-volume]] — the participation input the line weights by
- [[chaikin-money-flow]] — the A/D Line normalized into a bounded oscillator
- [[obv]] — the close-direction sibling that ignores intrabar range
- [[money-flow-index]] — the bounded 0–100 money-flow oscillator
- [[divergence]] — the A/D Line's most valuable signal type
- [[support-and-resistance]] — the A/D Line confirms breakouts through these levels
