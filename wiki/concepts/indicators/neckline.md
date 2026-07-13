---
title: "Neckline"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [indicators, technical-analysis]
aliases: ["Neckline", "Neckline Break", "Pattern Neckline"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]", "[[support-and-resistance]]", "[[chart-patterns]]"]
difficulty: beginner
related: ["[[head-and-shoulders]]", "[[double-top]]", "[[chart-patterns]]", "[[reversal-patterns]]", "[[support-and-resistance]]", "[[measured-move]]", "[[breakout]]", "[[trading-volume]]", "[[false-signals]]", "[[technical-analysis]]", "[[market-structure]]"]
---

A **neckline** is the [[support-and-resistance|support or resistance]] line drawn through the reaction lows (or highs) of a reversal [[chart-patterns|chart pattern]] — most famously the [[head-and-shoulders]] and [[double-top]]/double-bottom. It is the line whose decisive break **confirms** the pattern: until price closes through the neckline, the formation is only potential. The neckline therefore doubles as the trigger level for entries, the anchor for [[measured-move|measured-move]] price targets, and the reference for where a failed pattern is invalidated.

## How It Is Drawn

The neckline connects the **pivots between the pattern's peaks/troughs**:

- **[[head-and-shoulders]] top** — connect the two reaction lows (troughs) that sit between the left shoulder, head, and right shoulder. A break *below* this line confirms a bearish reversal.
- **Inverse head and shoulders** — connect the two reaction highs between the troughs. A break *above* it confirms a bullish reversal.
- **[[double-top]]** — the neckline is the horizontal support at the intervening trough (the "valley" between the two peaks). A double-bottom's neckline is the resistance at the intervening peak.

A neckline can be **horizontal or sloped**. A slightly upward-sloping neckline on a head-and-shoulders top is generally read as weaker (less bearish) than a flat or down-sloping one; the reverse holds for bottoms. Because the slope changes *where* price actually breaks the line, it also changes the [[measured-move]] projection — so consistent, well-anchored drawing matters.

## Why It Matters

The neckline encodes the [[support-and-resistance|support/resistance]] level that the prevailing [[trend]] has been leaning on. A clean break signals that the level can no longer hold — and per the principle of **polarity**, broken support becomes new resistance (and vice versa). That role-reversal is why a **retest** of the neckline from the other side is such a common and high-quality entry: the level that was support is now expected to cap any pullback.

Confirmation conventions traders apply to a neckline break:

- **Close beyond the line**, not just an intrabar poke, to filter [[false-signals|fakeouts]].
- **Expanding [[trading-volume]]** on the break (especially important for upside breaks of an inverse pattern).
- Optionally a **filter** — a fixed percentage or ATR buffer, or a wait for the retest — to avoid being trapped by [[whipsaw|whipsaws]] around a heavily-watched level.

## Measured-Move Target

The neckline is the launch point for the conventional [[measured-move]] target. The pattern's height is measured vertically from the extreme (the head, or the peak/trough) to the neckline, then projected from the **break point** in the direction of the break:

```
# Head-and-shoulders top (bearish)
height  = head_high - neckline_under_head
target  = neckline_break_price - height        # projected DOWN

# Inverse head-and-shoulders (bullish)
height  = head_low_below_neckline ... ->
target  = neckline_break_price + height         # projected UP
```

The projection is taken from where price actually breaks the neckline (which a sloped line shifts), not from the extreme — see [[measured-move]] for the full method.

## Worked Example

*(Illustrative, not from a specific source.)*

A stock forms a [[head-and-shoulders]] top: left shoulder peak $108, first trough $100, head $115, second trough $99, right shoulder $107. The trader draws the **neckline** through the two troughs (≈ $100, roughly flat).

- Price closes at **$98.50**, below the ~$100 neckline, on a [[trading-volume|volume]] surge — the break is confirmed.
- **Entry**: at the confirmed break ($98.50), or on a retest back up toward $100 (now resistance) for a tighter stop.
- **Stop**: just above the right shoulder ($107) — if price reclaims that high the breakdown has failed.
- **Target**: pattern height = $115 − $100 = $15; [[measured-move|measured target]] = $100 − $15 = **$85**.

The neckline thus supplies the trigger, the invalidation reference, and the basis for the target all at once.

## How Traders Use It

- **Entry trigger** — trade only the *confirmed* neckline break, or its retest; trading the right shoulder beforehand is anticipatory.
- **Invalidation** — a move back through the neckline (re-entering the pattern) is a common signal that the break failed.
- **Target anchor** — combine with the [[measured-move]] for a first objective.
- **Confluence** — a neckline break that coincides with a broken trendline, a moving average, or a prior [[support-and-resistance]] level is higher quality (see [[confluence]]).

## Common Pitfalls and False Signals

- **Subjective drawing.** Different analysts pick different troughs or slopes, shifting the break price, the target, and the stop. Prefer obvious, well-tested anchors and be consistent.
- **Intrabar fakeouts.** Price often spikes through a neckline and snaps back. Requiring a *close* beyond the line (and ideally a retest) filters many of these [[false-signals]].
- **Stop clustering.** Because so many traders watch the same neckline, clustered stops just beyond it invite liquidity hunts / stop-runs before the genuine move.
- **Break on weak volume.** A neckline break — particularly to the upside — on *falling* [[trading-volume]] is suspect and more likely to fail.
- **Lower-timeframe noise.** Necklines on intraday charts break and fail constantly; daily/weekly necklines are materially more reliable.

## Sources

- Robert D. Edwards & John Magee, *Technical Analysis of Stock Trends* — the canonical treatment of necklines in reversal patterns.
- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — reversal patterns, neckline breaks, and volume confirmation.
- General market knowledge; the worked example above is illustrative, not from a specific ingested source.

## Related

- [[head-and-shoulders]] — the pattern most associated with the neckline
- [[double-top]] — the neckline here is the support at the intervening trough
- [[chart-patterns]] — the broader family of price formations
- [[reversal-patterns]] — the category whose breaks the neckline confirms
- [[support-and-resistance]] — the neckline is a support/resistance line
- [[measured-move]] — the target method anchored on the neckline break
- [[breakout]] — a neckline break is a type of pattern breakout
- [[trading-volume]] — volume confirmation of a neckline break
- [[false-signals]] — failed neckline breaks are a classic fakeout
- [[market-structure]] — a neckline break marks a structural shift
