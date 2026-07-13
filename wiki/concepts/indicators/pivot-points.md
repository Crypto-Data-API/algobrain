---
title: "Pivot Points"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [indicators, technical-analysis, day-trading]
aliases: ["Pivot Point", "Floor Trader Pivots", "PP", "pivot-point"]
domain: [indicators]
prerequisites: ["[[support-and-resistance]]", "[[technical-analysis]]"]
difficulty: intermediate
related: ["[[support-and-resistance]]", "[[vwap]]", "[[day-trading]]", "[[breakout]]", "[[trend]]", "[[fibonacci-retracements]]", "[[gap-trading]]", "[[range-trading]]"]
---

Pivot points are a set of horizontal [[support-and-resistance]] levels calculated mechanically from the *prior period's* high, low, and close. The central **pivot point (PP)** is the average of those three prices; a ladder of support (S1, S2, S3) and resistance (R1, R2, R3) levels is then derived around it. Because they are objective, recompute once per session, and are watched by many traders (the standard formula originated with floor traders), pivot points are a staple intraday reference for stock, futures, and forex [[day-trading]].

## How It Works

The most common ("standard" or "floor-trader") pivot set uses the previous period's High, Low, and Close. For an intraday trader, "previous period" usually means the prior trading day; the levels are fixed for the whole of the next session.

```
PP = (High + Low + Close) / 3

R1 = (2 × PP) − Low
S1 = (2 × PP) − High

R2 = PP + (High − Low)
S2 = PP − (High − Low)

R3 = High + 2 × (PP − Low)
S3 = Low  − 2 × (High − PP)
```

- **PP** is the equilibrium level — the market's perceived "fair" price carried over from the prior session.
- **R1/R2/R3** are projected resistance above; **S1/S2/S3** are projected support below.
- The levels are static for the session, which is what makes them useful: every trader watching standard pivots sees the same numbers.

### Worked Example (illustrative)

Prior day: High = 102, Low = 98, Close = 101.

```
PP = (102 + 98 + 101) / 3 = 100.33
R1 = (2 × 100.33) − 98  = 102.67
S1 = (2 × 100.33) − 102 = 98.67
R2 = 100.33 + (102 − 98) = 104.33
S2 = 100.33 − (102 − 98) = 96.33
```

Next session, a trader treats 100.33 as the pivot: trading above it leans bullish (first target R1 = 102.67), trading below it leans bearish (first target S1 = 98.67). (Illustrative numbers only.)

## Variants

| Variant | Difference |
|---|---|
| **Standard / Floor** | The formulas above; the most widely used. |
| **Woodie** | Weights the close more heavily: PP = (High + Low + 2 × Close) / 4. |
| **Camarilla** | Tighter levels using fixed multipliers of the prior range; popular for mean-reversion / fade setups. |
| **Fibonacci** | Support/resistance placed at [[fibonacci-retracements\|Fibonacci]] ratios (38.2%, 61.8%, 100%) of the prior range around the pivot. |
| **DeMark** | Conditional on whether the prior close was above, below, or at the open; produces a single projected high/low band rather than a full ladder. |

## How Traders Use It

- **Bias filter.** Price above PP is read as a bullish session bias, below PP as bearish. Many traders only take longs above the pivot and shorts below it.
- **Entries, targets, and stops.** S1/R1 act as the first reaction levels — common spots to fade a move (range day) or to take partial profit on a trend day. S2/R2 and S3/R3 are stretch targets. Stops are often placed just beyond the next pivot level.
- **Breakout confirmation.** A decisive break and hold above R1 (or below S1) signals trend continuation toward the next level; this pairs naturally with [[breakout]] and [[gap-trading]] setups.
- **Confluence.** Pivots are strongest where they line up with other reference levels — the prior day's high/low, round numbers, a moving average, or [[vwap|VWAP]]. A pivot alone is a weak signal; a pivot stacked with [[vwap|VWAP]] and a round number is a high-attention level.

## Common Pitfalls and Risks

- **Self-fulfilling, until it isn't.** Pivots "work" partly because many traders watch them, but that same crowding makes them magnets for stop-hunts and [[false-signals|fakeouts]] — price can spike through a level to trigger stops, then reverse.
- **Weak in strong trends and after gaps.** On a strong trend day, price can blow through several pivot levels without pausing; on a large overnight [[gap-trading|gap]], the prior session's range may be irrelevant and the levels mis-placed.
- **Session-boundary sensitivity.** The result depends entirely on which High/Low/Close you feed in. Including or excluding the pre-/post-market session, or choosing a daily vs. weekly basis, shifts every level. Be consistent.
- **24/7 markets.** For crypto and other continuously-traded assets there is no clean daily close, so the choice of "session" materially changes the pivots — use with caution.
- **A reference, not a system.** Pivot points locate *where* to pay attention, not *whether* to buy or sell. They need a trigger (price action, volume, a [[trend]] read) layered on top.

## Sources

- General technical-analysis and intraday-trading literature on floor-trader pivot points and their Woodie, Camarilla, Fibonacci, and DeMark variants. Formulas are standard; the worked example uses illustrative numbers, not a specific ingested wiki source.

## Related

- [[support-and-resistance]] — pivot points are a mechanical way to project these levels
- [[vwap]] — the other dominant intraday reference; strongest in confluence with pivots
- [[day-trading]] — pivots are most used on intraday timeframes
- [[breakout]] / [[range-trading]] — the two trade styles pivots support (break vs. fade)
- [[fibonacci-retracements]] — basis of the Fibonacci-pivot variant
- [[gap-trading]] — large gaps degrade prior-session pivot relevance
