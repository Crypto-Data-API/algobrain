---
title: "Measured Move"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [indicators, technical-analysis]
aliases: ["Measured Move", "Measured Move Target", "Price Projection", "Measured Objective", "Price Target Projection"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]", "[[chart-patterns]]", "[[support-and-resistance]]"]
difficulty: beginner
related: ["[[head-and-shoulders]]", "[[double-top]]", "[[flags-and-pennants]]", "[[chart-patterns]]", "[[fibonacci-extensions]]", "[[support-and-resistance]]", "[[neckline]]", "[[breakout]]", "[[take-profit]]", "[[technical-analysis]]", "[[risk-reward-ratio]]", "[[trading-volume]]"]
---

A **measured move** is a price-projection technique that estimates how far price is likely to travel after a [[chart-patterns|chart pattern]] completes or a [[breakout]] occurs, by taking a measurable distance on the chart and projecting it forward from a reference point. The simplest form is "the move after the pattern equals the size of the pattern (or the prior move) that produced it." It is one of the most common ways traders set a first [[take-profit|profit target]] and judge a setup's [[risk-reward-ratio|reward-to-risk]] before entering.

## The General Idea

A measured move has three ingredients:

1. **A measured distance (the "height" or "leg").** A vertical price distance taken from the chart — the height of a pattern, the length of an impulse leg, or the depth of a flagpole.
2. **A projection origin (the launch point).** The price level from which the distance is added or subtracted — usually the [[breakout]] / [[neckline]] break point, not the pattern's extreme.
3. **A direction.** Up for bullish patterns/breakouts, down for bearish ones.

```
target = launch_point ± measured_distance
#   + for an upside break, - for a downside break
```

The logic is that a pattern (or an impulse leg) reflects a certain magnitude of supply/demand imbalance, and once price resolves, a *similar* magnitude often plays out again. It is a heuristic, not a law — a *first objective*, not a ceiling.

## Common Forms

### Pattern-height projection

Used for reversal and continuation patterns. Measure the pattern's height and project it from the breakout.

- **[[head-and-shoulders]]** — height = head to [[neckline]]; project from the neckline break (down for a top, up for an inverse).
- **[[double-top]] / double-bottom** — height = peak (or trough) to the neckline; project from the neckline break.
- **Rectangles / ranges** — height = top to bottom of the range; project from the breakout edge.
- **Triangles** — project the widest part (the base) of the triangle from the breakout point.

### Flagpole projection (continuation patterns)

For [[flags-and-pennants|flags and pennants]], the "pole" — the sharp impulse move that preceded the consolidation — is the measured distance. It is projected from the point where price breaks out of the flag, on the theory that the second leg mirrors the first. This is the classic "flags fly at half-mast": the flag forms around the midpoint of the total move.

### ABCD / swing-equality projection

In swing trading and harmonic analysis, the **AB = CD** measured move assumes the second leg (C→D) of a zig-zag equals the length of the first leg (A→B). After an A→B advance, a B→C pullback, the projected D target is `C + (B − A)`.

### Relationship to Fibonacci

A pure measured move uses a 1:1 (100%) projection of the prior leg. [[fibonacci-extensions|Fibonacci extensions]] generalise this, projecting common ratios (61.8%, 100%, 127.2%, 161.8%) of the measured leg, giving a cluster of objectives rather than a single one.

## Worked Example

*(Illustrative, not from a specific source.)*

A stock breaks out of a **bull flag**. The flagpole ran from a base at **$40** up to **$52** (a $12 impulse). Price then drifted sideways-down into a flag between $50 and $49, and finally breaks out above the flag at **$50.50**.

- **Measured distance** = flagpole height = $52 − $40 = **$12**.
- **Launch point** = the breakout level = **$50.50**.
- **Measured-move target** = $50.50 + $12 = **$62.50**.

If the trader enters at $50.50 with a stop below the flag at $48.80, the risk is ~$1.70 and the reward to the $62.50 target is ~$12 — roughly **7:1** on the measured objective, the kind of favorable [[risk-reward-ratio]] that makes the projection worth using as a *first* target. Partial profit-taking at $62.50 and trailing the remainder is common, since strong trends frequently run past the measured move.

## How Traders Use It

- **Set a first target.** The measured move is typically the *initial* [[take-profit]] level, not a hard exit for the whole position.
- **Pre-trade screening.** Comparing the measured move (potential reward) against the stop distance (risk) gives a [[risk-reward-ratio]] used to accept or reject a setup *before* entering.
- **Scale out and trail.** Take partial profit at the measured target and trail the rest, because trends often extend well beyond a single projection.
- **Confluence.** A measured-move target that lands on a prior [[support-and-resistance]] level, a [[fibonacci-extensions|Fibonacci extension]], or a round number is higher-conviction (see [[confluence]]).

## Common Pitfalls and Limitations

- **It is a probability, not a guarantee.** Many moves fall short of, or overshoot, the projected target. The measured move estimates a *typical* magnitude, not a promised one.
- **Garbage-in from a mis-drawn pattern.** The target inherits all the subjectivity of the pattern: a different [[neckline]] slope or a different chosen swing changes the height and therefore the target. Be consistent in how you measure.
- **Wrong launch point.** Projecting from the pattern's extreme instead of the actual breakout/neckline point (which a sloped line shifts) produces a wrong target.
- **Ignoring context.** A measured move into a major overhead [[support-and-resistance|resistance]] level is less likely to be reached cleanly; a target in open space has fewer obstacles.
- **Treating it as a ceiling.** Strong trends frequently blow through measured-move targets; exiting the entire position there can leave large gains on the table.
- **Lower-timeframe noise.** Projections are more reliable on daily/weekly charts than on noisy intraday patterns.

## Sources

- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — measured-move objectives for reversal and continuation patterns.
- Robert D. Edwards & John Magee, *Technical Analysis of Stock Trends* — pattern-height price targets.
- Thomas Bulkowski, *Encyclopedia of Chart Patterns* — statistical study of pattern targets and how often they are met.
- General market knowledge; the worked example above is illustrative, not from a specific ingested source.

## Related

- [[head-and-shoulders]] — uses a head-to-neckline measured move
- [[double-top]] — projects pattern height from the neckline break
- [[flags-and-pennants]] — the flagpole measured move ("half-mast")
- [[chart-patterns]] — the formations measured moves project from
- [[fibonacci-extensions]] — a generalised, ratio-based projection method
- [[neckline]] — the common launch point for reversal-pattern projections
- [[breakout]] — measured moves project the post-breakout target
- [[support-and-resistance]] — context that can stall a measured move
- [[take-profit]] — the measured move is a common first target
- [[risk-reward-ratio]] — the measured target sizes the reward side
