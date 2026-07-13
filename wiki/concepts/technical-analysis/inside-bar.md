---
title: "Inside Bar"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [technical-analysis, indicators, breakout, volatility]
aliases: ["Inside Bar", "inside bars", "inside candle", "volatility contraction bar"]
domain: [technical-analysis]
prerequisites: ["[[candlestick-patterns]]"]
difficulty: beginner
related: ["[[harami]]", "[[candlestick-patterns]]", "[[outside-bar-strategy]]", "[[arc-strategy]]", "[[support-and-resistance]]"]
---

# Inside Bar

An **inside bar** is a two-candle pattern in which the second bar's entire high-low range falls completely within the first bar's range: its high is lower than the prior high and its low is higher than the prior low. It signals **volatility contraction** — a pause in which neither buyers nor sellers extend the range — and is most often traded as a coiled spring ahead of a breakout. It is the range-based cousin of the body-based [[harami]] and the opposite of the range-expanding [[outside-bar-strategy|outside bar]].

## Pattern Definition

```
high[i] < high[i-1]   # inside bar high below prior high
low[i]  > low[i-1]    # inside bar low above prior low
```

The first (larger) bar is the **mother bar**; the contained bar is the **inside bar**. The defining test is on the *complete range* (high to low), not just the real body — this is the key distinction from a [[harami]], which only requires the second candle's *real body* to sit inside the first candle's body (Source: gap-finder Perplexity research 2026-06-19). Multiple consecutive inside bars indicate sustained compression and an increasingly likely range expansion.

## Trading Logic

An inside bar represents balance and indecision after a directional move. Traders typically:

- **Breakout entry**: buy a break above the mother bar's high or sell a break below its low, treating the contraction as stored energy about to release.
- **Continuation context**: an inside bar after a strong trend leg often acts as a brief consolidation before the trend resumes (a "pennant"-like pause on a single bar).
- **Stop placement**: stops are placed on the opposite side of the mother bar (or the inside bar itself for tighter risk), benefiting from the naturally compressed range to keep risk small.

Reliability improves when the inside bar forms at a meaningful location — a [[support-and-resistance]] level, a [[box-and-swing-structure|box edge]], or a [[vwap]] reference — rather than mid-range.

## Worked Example (illustrative)

The numbers below are hypothetical, shown only to make the mechanics concrete — they are not real market data.

A stock trends up and prints a strong mother bar with a high of $45.00 and a low of $43.50. The next bar trades only between $44.20 and $44.80 — its high is below $45.00 and its low is above $43.50, so the entire range nests inside the mother bar. That is an **inside bar**: after the strong push, neither side extended the range, and volatility contracted into a coil.

Two ways a trader might play it:

- **Breakout (continuation):** place a buy stop a tick above the mother bar's high ($45.00) and a protective stop below the mother bar's low ($43.50), or tighter, below the inside bar's low ($44.20) for smaller risk. If price breaks $45.00, the stored energy releases in the trend's direction.
- **Failure/false break:** if instead price pokes above $45.00 and immediately closes back inside the mother bar's range, that is a failed breakout — a common trap on lower timeframes — and an aggressive trader might fade it back toward the mother bar's low.

If this inside bar had formed *at a [[box-and-swing-structure|box high]]* after a qualifying up-move, a break of the inside bar's **low** could instead set up a short into the box, reinforced by a [[john-wick-candle|wick rejection]] — illustrating how location flips the same pattern from a continuation-buy into a reversal-sell.

## Relationship to ARC

In the [[arc-strategy|ARC (Area-Range-Candle)]] framework, an inside bar at a box high after a strong up-move can be read as the market deciding whether to break through resistance or revert into the box. A break of the inside bar's low at that level can align with a short entry, especially when reinforced by a [[john-wick-candle|wick rejection]] or volume confirmation (Source: gap-finder Perplexity research 2026-06-19). It serves as one of ARC's optional candle triggers alongside outside bars and wick-rejection candles.

## Inside Bar vs. Harami

| Feature | Inside Bar | [[harami\|Harami]] |
|---------|-----------|--------|
| Containment test | Full **range** (high-low) inside prior range | Real **body** inside prior body |
| Shadows | Must also be contained | May extend beyond the first candle's shadows |
| Primary read | Volatility contraction / breakout setup | Reversal or momentum-pause signal |
| Origin | Western price-action / Larry Williams lineage | Japanese candlestick tradition |

Every harami where the shadows are also contained is technically also an inside bar; the terms emphasize different things — the harami emphasizes body/reversal, the inside bar emphasizes range/breakout.

## Advantages

- Mechanically simple (two price comparisons), easy to scan and [[backtesting|backtest]]
- Naturally tight stops due to the compressed range
- Pairs well with level- and trend-based filters

## Disadvantages

- Very common, especially on lower timeframes — many are noise
- Breakout direction is not predicted by the pattern alone; requires context
- Prone to false breakouts in choppy, rangebound markets

## Related Concepts

- [[harami]] — body-based counterpart
- [[outside-bar-strategy]] — range-expansion opposite
- [[engulfing-candle]] — the range-expansion / reversal sibling
- [[breakout]] — what the coiled inside bar is setting up for
- [[volatility]] — inside bars are a visual signature of volatility contraction
- [[average-candle-range]] — quantifies the contraction the inside bar shows
- [[price-action]] — the discipline inside-bar trading sits within
- [[candlestick-patterns]]
- [[arc-strategy]]
- [[john-wick-candle]]
- [[support-and-resistance]]

## Sources

- gap-finder Perplexity deep research (2026-06-19)
- Source video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge
