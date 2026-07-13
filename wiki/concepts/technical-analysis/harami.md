---
title: "Harami"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [technical-analysis, indicators, mean-reversion]
aliases: ["Harami", "harami pattern", "bullish harami", "bearish harami", "pregnant candle"]
domain: [technical-analysis]
prerequisites: ["[[candlestick-patterns]]"]
difficulty: beginner
related: ["[[candlestick-patterns]]", "[[inside-bar]]", "[[arc-strategy]]", "[[support-and-resistance]]"]
---

# Harami

A **harami** is a two-candle Japanese candlestick pattern in which the second candle's **real body** sits entirely within the real body of the first (larger) candle. It signals a loss of momentum — a pause or potential reversal — after a directional move. The name comes from the old Japanese word for "pregnant": the large first candle is the "mother," carrying the small second candle inside it.

## Pattern Definition

The test is on the **real body** (open-to-close), not the full high-low range:

```
# the second candle's body is contained in the first candle's body
max(open[i], close[i]) < max(open[i-1], close[i-1])
min(open[i], close[i]) > min(open[i-1], close[i-1])
```

The second candle's **shadows (wicks) may extend beyond** the first candle's shadows without invalidating the pattern — only the bodies must be nested (Source: gap-finder Perplexity research 2026-06-19). This is the crucial distinction from an [[inside-bar]], where the *entire range* (including wicks) must be contained.

### Bullish vs. Bearish

- **Bullish harami**: appears in a downtrend — a large down (red) candle followed by a small up (green) body inside it. Suggests selling pressure is fading; potential bottom.
- **Bearish harami**: appears in an uptrend — a large up (green) candle followed by a small down (red) body inside it. Suggests buying pressure is fading; potential top.
- **Harami cross**: the special case where the second candle is a doji (near-zero body), generally treated as a stronger indecision/reversal signal.

## Trading Logic

A harami marks a sudden contraction of conviction: after a strong directional bar, the market fails to extend, and the small inside body shows hesitation. Traders typically:

- Wait for **confirmation** on the next candle (a close back through the small body in the reversal direction) rather than acting on the harami alone.
- Use it as a **momentum-pause / reversal** signal, most reliable at a [[support-and-resistance]] level or trend extreme rather than mid-trend.
- Place stops beyond the mother candle's extreme.

Like most single patterns, a harami in isolation is weak; its value rises sharply with location and confirmation.

### Entry, Stop, and Target (concrete framing)

For a **bullish harami** read as a reversal:

- **Trigger:** wait for the candle *after* the harami to close back above the small inside body (confirmation that buyers have stepped in), rather than entering on the harami itself.
- **Entry:** on that confirmation close, or on a break of the inside candle's high.
- **Stop:** just below the **mother candle's low** (the large prior down candle), since a move below it negates the "selling exhausted" thesis.
- **Target:** the prior swing, a [[support-and-resistance]] level above, or a measured multiple of risk. The setup is highest quality at a trend extreme or established support, lowest quality mid-trend.

The **bearish harami** mirrors this: confirmation is a close back below the small body, stop above the mother candle's high, targets toward support below.

## Worked Example (illustrative)

The price levels below are hypothetical and used only to demonstrate the mechanics — they are not real market data.

A stock has been falling for several sessions and prints a large red candle that opens at $30.00 and closes at $28.00 (a $2.00 body). The next session opens at $28.60 and closes at $29.20 — a small green body sitting entirely inside the prior body's $28.00–$30.00 span. That is a **bullish harami**: the strong selling of the prior day did not continue, and the market hesitated.

The trader does *not* buy yet. They wait for the following candle. If it closes above $29.20 (back through the small body), that is confirmation; they enter long around $29.30 with a stop just under the mother candle's low (below $28.00, allowing a little buffer, say $27.85). If instead the next candle closes back below $28.00, the harami failed — selling resumed — and the trade is abandoned. This shows the pattern's nature: it flags a *pause*, and only confirmation plus a sensible location (here, perhaps a prior support shelf near $28) turns that pause into an actionable reversal idea.

## Harami vs. Inside Bar

| Feature | Harami | [[inside-bar\|Inside Bar]] |
|---------|--------|-----------|
| Containment test | Real **body** within prior body | Full **range** (high-low) within prior range |
| Shadows | May exceed the first candle's shadows | Must be contained |
| Color | Often emphasizes opposite-color second candle | Color-agnostic |
| Primary read | Reversal / momentum pause | Volatility contraction / breakout |
| Tradition | Japanese candlestick lore | Western price-action lineage |

The two overlap: a harami whose wicks happen to be contained is also an inside bar. The labels signal different intent — reversal (harami) versus breakout (inside bar).

## Relationship to ARC

In the [[arc-strategy|ARC (Area-Range-Candle)]] ecosystem, a harami is one of the compression/pause patterns that can appear at a box or swing level after a sufficient range move, hinting that the prior leg is stalling before a reversal back into the box. It complements [[john-wick-candle|wick-rejection candles]] and [[inside-bar|inside bars]] as a confirmation trigger at key areas (Source: gap-finder Perplexity research 2026-06-19).

## Advantages

- Simple, well-known, easy to identify and scan
- Effective at flagging momentum exhaustion at extremes
- Body-only test catches reversals that a strict range test would miss

## Disadvantages

- Low standalone reliability; needs confirmation and good location
- Common on noisy timeframes
- Subjective "small body" threshold unless coded with explicit ratios

## Related Concepts

- [[candlestick-patterns]]
- [[inside-bar]] — range-based counterpart
- [[engulfing-candle]] — the opposite relationship (second candle engulfs the first)
- [[john-wick-candle]] — wick-rejection reversal trigger that pairs with harami at levels
- [[price-action]] — the broader discipline harami belongs to
- [[arc-strategy]]
- [[support-and-resistance]]

## Sources

- gap-finder Perplexity deep research (2026-06-19)
- Source video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge
