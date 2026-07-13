---
title: "Head and Shoulders"
type: concept
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [indicators, technical-analysis]
aliases: ["H&S", "head and shoulders top", "inverse head and shoulders"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]", "[[support-and-resistance]]"]
difficulty: beginner
related: ["[[trend]]", "[[trading-volume]]", "[[support-and-resistance]]", "[[double-top]]", "[[technical-analysis]]", "[[candlestick-patterns]]", "[[reversal-patterns]]", "[[neckline]]", "[[measured-move]]", "[[market-structure]]", "[[swing-high]]", "[[swing-low]]"]
---

The head and shoulders is a classic [[reversal-patterns|reversal]] chart pattern made of three consecutive peaks in which the middle peak (the head) is higher than the two flanking peaks (the shoulders), signalling a shift from an uptrend to a downtrend. Its inverse — three troughs with the deepest in the middle — marks a bottom and signals a bullish reversal. It is built entirely from [[swing-high|swing highs]] and [[swing-low|swing lows]], making it a pure [[market-structure]] pattern, and it sits in the same family as the [[double-top]]/double-bottom.

## Structure

1. **Left shoulder** — price rises to a peak ([[swing-high]]) on strong [[trading-volume|volume]], then declines.
2. **Head** — price rises to a higher peak, then declines again (often on lighter volume than the left shoulder — an early divergence warning).
3. **Right shoulder** — price rises but fails to reach the head's height, typically on still-lighter volume, then declines.
4. **[[neckline|Neckline]]** — the [[support-and-resistance|support]] line connecting the two troughs (reaction lows) between the peaks. It can be horizontal or sloped.

The pattern is only **confirmed** when price closes below the [[neckline]], ideally on expanding [[trading-volume]]. Until that break, the formation is incomplete and trading the right shoulder is anticipatory.

### Anatomy at a Glance

| Component | What it is | Typical volume | Trader's read |
|---|---|---|---|
| Left shoulder | First peak, end of prior [[trend|uptrend]] | High | Last gasp of strong demand |
| Trough 1 | Reaction low after left shoulder | Falling | First [[neckline]] anchor |
| Head | Highest peak | Lower than left shoulder | Buyers commit, but with less force (divergence) |
| Trough 2 | Reaction low after head | Falling | Second [[neckline]] anchor |
| Right shoulder | Lower peak, fails to exceed head | Lowest | Demand exhausted; supply in control |
| [[neckline\|Neckline]] break | Close below the two-trough line | Rising (ideal) | Confirmation; [[support-and-resistance\|support flips to resistance]] |

## How It Works

The structure encodes the exhaustion of an [[trend|uptrend]]: each successive rally attracts fewer buyers (visible as declining volume into the head and right shoulder), while sellers defend progressively lower highs. The [[neckline]] break confirms that demand can no longer hold prior [[support-and-resistance|support]], flipping the support level into resistance.

### Inverse Head and Shoulders

The mirror image at market bottoms: three troughs with the deepest in the middle, confirmed by a breakout *above* the [[neckline]]. Volume should ideally expand on the breakout. It signals accumulation and a bullish reversal. Everything in this page applies symmetrically — flip "high" for "low", "below" for "above", and "[[resistance]]" for "[[support]]".

## Measured-Move Target

The conventional **[[measured-move]] target** equals the vertical distance from the head to the [[neckline]], projected from the breakout point in the direction of the break:

```
# For a top (bearish)
height  = head_high - neckline_under_head      # the pattern's "height"
target  = neckline_break_price - height        # projected DOWN from the break

# For an inverse (bullish)
height  = neckline_over_head - head_low
target  = neckline_break_price + height         # projected UP from the break
```

The projection is taken from where price actually *breaks* the neckline, not from the head, because a sloped neckline changes the break price. The height is measured vertically beneath the head — the single biggest distance in the pattern.

## Worked Example (illustrative)

A stock tops out after a long [[trend|uptrend]]. The pattern prints these levels:

| Point | Price |
|---|---|
| Left shoulder peak | $108 |
| Trough 1 (neckline anchor) | $100 |
| Head peak | $115 |
| Trough 2 (neckline anchor) | $99 |
| Right shoulder peak | $107 |
| Neckline (≈ flat) | ~$100 |

The trader watches the right shoulder fade on the lowest [[trading-volume]] of the three peaks. Price then closes at **$98.50**, below the ~$100 neckline, on a [[trading-volume|volume]] surge — confirmation.

- **Pattern height** = head ($115) − neckline ($100) = **$15**.
- **[[measured-move|Measured target]]** = neckline break ($100) − height ($15) = **$85**.
- **Entry** = $98.50 on the close below the neckline.
- **Stop** = $107.10, just above the right shoulder (invalidation: if price reclaims the right-shoulder high, the breakdown has failed).
- **Risk** = $98.50 − $107.10 ≈ $8.60 per share. **Reward to target** = $98.50 − $85 = $13.50. That is roughly a **1.6 : 1** reward-to-risk; a retest entry near the neckline ($100) would tighten the stop and lift the ratio.

The measured move is a *first* target, not a ceiling — trends that reverse from a major H&S often run well beyond it; partial profit-taking at the projected level is common.

## How Traders Use It

- **Entry** — on the confirmed [[neckline]] break, or on a retest of the broken neckline (now [[resistance]]) for a tighter stop and better risk/reward.
- **Stop** — above the right shoulder for a top (below it for the inverse). Some traders use the head itself for a wider, lower-probability-of-shakeout stop.
- **Confirmation** — pair the break with [[trading-volume]] expansion, [[confluence]] from a broken trendline, and broader [[trend]] / [[market-structure]] context (a lower-high, lower-low sequence forming).
- **Targets** — take the [[measured-move]] as a first objective; trail the rest along new [[swing-high|swing highs]] (for a downtrend, lower swing highs).

Head and shoulders is among the most-studied patterns in [[technical-analysis]], with relatively higher reliability on longer (daily/weekly) timeframes than on noisy intraday charts.

## Common Pitfalls and Risks

- **Failed breaks / [[false-signals]].** Price can break the [[neckline]] and immediately reverse back inside the pattern — a [[whipsaw]]. A close-based break on rising volume, plus waiting for (or scaling on) a retest, filters many of these.
- **Trading the right shoulder early.** The pattern is valid only on completion; entering before the neckline break is anticipatory and carries higher risk of the right shoulder simply becoming a higher high that resumes the [[trend|uptrend]].
- **Subjective necklines.** Different analysts draw the [[neckline]] differently (which troughs, sloped vs flat), which shifts the break price, the [[measured-move]] target, and the stop. Be consistent and prefer obvious, well-tested anchors.
- **Reflexivity and stop-hunting.** Because so many traders watch the same level, the neckline attracts clustered stops; liquidity hunts ([[false-signals|fakeouts]]) around it are common before the genuine move.
- **Volume that does not confirm.** A neckline break on *falling* volume is suspect — it raises the odds of a failed pattern.
- **Lower-timeframe noise.** Intraday H&S patterns fire constantly and fail often; daily/weekly patterns are materially more reliable.

## Caveats

- Partial or **failed** patterns are common — price can break the neckline and immediately reverse.
- The pattern is valid only on completion; trading the right shoulder before the neckline break is higher risk.
- Necklines are subjective; different analysts draw them differently, affecting targets and stops.
- Self-fulfilling reflexivity (many traders watching the same level) cuts both ways — it can also attract stop-hunting around the neckline.

## Sources

- Robert D. Edwards & John Magee, *Technical Analysis of Stock Trends* — the canonical treatment of the head and shoulders pattern.
- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — reversal patterns, volume confirmation, and measured-move targets.
- General market knowledge; worked example above is illustrative, not from a specific ingested wiki source.

## Related

- [[reversal-patterns]] — the family this pattern belongs to
- [[neckline]] — the support/resistance line whose break confirms the pattern
- [[measured-move]] — the target-projection method used above
- [[double-top]] — a related two-peak reversal pattern
- [[support-and-resistance]] — the neckline is a support/resistance level
- [[trading-volume]] — volume confirmation is central to the pattern
- [[trend]] — the prior trend that the pattern reverses
- [[market-structure]] — H&S is a structural lower-high/lower-low transition
- [[swing-high]] / [[swing-low]] — the pivots the pattern is built from
- [[false-signals]] — failed neckline breaks are a classic fakeout
