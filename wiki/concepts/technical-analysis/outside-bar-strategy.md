---
title: "Outside Bar Strategy (External Candle)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [technical-analysis, indicators, breakout, backtesting]
aliases: ["Outside Bar", "External Candle", "Larry Williams external candle", "engulfing bar strategy"]
domain: [technical-analysis]
prerequisites: ["[[candlestick-patterns]]"]
difficulty: intermediate
related: ["[[candlestick-patterns]]", "[[inside-bar]]", "[[backtesting]]", "[[arc-strategy]]", "[[support-and-resistance]]"]
---

# Outside Bar Strategy (External Candle)

An **outside bar** (or "external candle") is a candle whose range fully engulfs the prior candle: its high is above the previous high *and* its low is below the previous low. The **outside bar strategy** popularized by Larry Williams trades the directional commitment such a bar signals when its close also breaks through the prior bar's extreme. It is the expansion-of-range counterpart to the contraction-based [[inside-bar]].

## Pattern Definition

For a bearish outside bar (short signal):

- high > prior high
- low < prior low
- close < prior low (the bar closes *through* the previous bar's low)

The bullish (long) version mirrors these conditions:

- high > prior high
- low < prior low
- close > prior high (close *through* the previous bar's high)

The defining feature is that the current bar both engulfs the prior bar's entire range and closes decisively beyond it, marking a decisive expansion of range and a directional commitment that often begins a strong move. This is distinct from a bullish/bearish engulfing pattern, which only requires the *body* to engulf the prior body; the outside bar requires the full high-low range to be engulfed.

## Trading Logic

The pattern is read as a sudden burst of one-sided pressure overwhelming the prior bar's participants. Entry is taken in the direction of the close-through; stops are commonly placed beyond the outside bar's opposite extreme or at a fixed distance. Because the bar by definition has a wide range, stops can be relatively far, so position sizing and reward expectations must account for the larger risk distance.

## Rules (Entry, Stop, Target)

These are conventional formulations; exact parameters should be confirmed with an independent [[backtesting|backtest]] before any live use.

- **Entry** — on confirmation of the close-through. A trader can either take the signal at the close of the outside bar itself, or wait for the *next* bar to trade through the outside bar's extreme (a stop-entry order above the bar high for longs / below the bar low for shorts) to filter false signals.
- **Stop** — placed beyond the opposite extreme of the outside bar (below the bar low for longs, above the bar high for shorts). Because the outside bar is by definition a wide-range bar, this stop is relatively distant; some traders instead use a fixed-distance stop (e.g., an ATR multiple) to bound risk.
- **Target / exit** — common approaches include a fixed [[risk-reward-ratio|reward-to-risk]] multiple, a trailing stop to ride range expansion, the next [[support-and-resistance]] level, or — as in the CodeTrading variant below — closing the trade on the first subsequent bar that closes favorably.
- **Position sizing** — sized off the (wide) stop distance so that per-trade risk stays within a fixed fraction of equity. The wide stop is the central sizing constraint of this setup.

## Implementation Pseudocode

```
# bearish external candle (Larry Williams style)
C0 = high[i]  > high[i-1]
C1 = low[i]   < low[i-1]
C2 = close[i] < low[i-1]
if C0 and C1 and C2:
    signal = SHORT
# bullish version flips C2 to close[i] > high[i-1] -> LONG
```

## Example (Hypothetical)

Consider a daily chart at a known [[support-and-resistance|resistance]] level. The prior bar trades in a tight range. The next bar opens, rallies above the prior high, sells off below the prior low, and closes near its low — *below* the prior bar's low. This is a bearish outside bar at resistance: range expanded, the bar engulfed the previous session entirely, and the close confirmed sellers in control. A trader using the wait-for-break variant places a sell-stop just under the outside bar's low; if the following session trades through it, the short is triggered, the stop sits above the outside bar's high, and the target is the next support level below. The wide bar means the stop is far, so the position is sized small. This is illustrative only — no specific instrument, price, or outcome is implied.

## The CodeTrading 7-Year Backtest Claim

A 2024 video by the educational creator **CodeTrading** implemented this Larry Williams external candle strategy on the daily timeframe and reported a seven-year backtest on forex pairs claiming positive overall profit and an aggregated win rate of approximately **87%** under its specific stop-loss (around 200-250 pips) and position-sizing rules (Source: gap-finder Perplexity research 2026-06-19).

> **Attribution and caveat:** This 87% / 7-year figure is a *single creator's claimed backtest result*, reported via a YouTube video, and has **not been independently verified**. High headline win rates on candle-only patterns are sensitive to stop-loss size, take-profit logic (CodeTrading's version closed trades on any later winning session rather than a fixed take-profit), survivorship in pair selection, and transaction-cost assumptions. Treat it as an illustrative demonstration that tightly specified candle patterns *can* be systematically tested — not as established edge. Anyone considering this strategy should re-run an independent, [[backtesting|cost-corrected backtest]] before drawing conclusions.

## Relationship to ARC

In an [[arc-strategy|ARC (Area-Range-Candle)]] context, an outside bar forming off a box low (for longs) or box high (for shorts) can act as confirmation that the level has held and a new directional leg is underway. It is one of several candle triggers — alongside [[john-wick-candle|"John Wick" wick-rejection candles]] and [[inside-bar]] breakouts — that a level-based trader can use at key areas after the required range move has unfolded (Source: gap-finder Perplexity research 2026-06-19).

## Advantages

- Mechanically unambiguous (four price comparisons), easy to code and [[backtesting|backtest]]
- Captures genuine range-expansion / directional-commitment moments
- Combines naturally with [[support-and-resistance]] and [[box-and-swing-structure|box/swing levels]]

## Disadvantages

- Wide bar means wide stops and larger per-trade risk
- Headline win rates from creator backtests can be misleading without cost and slippage modeling
- Frequent on noisy intraday charts; works best with a level or trend filter

## Limitations

- **Single-bar patterns are weak in isolation.** The outside bar's edge, if any, depends heavily on context — a level, a trend, or a volatility regime. Used as a standalone signal across all bars it tends to generate many low-quality trades.
- **Stop-distance variance** makes risk-normalization essential; without ATR- or stop-distance-based sizing, equal-share sizing distorts the risk profile.
- **Definition sensitivity.** Results change materially depending on whether you require the close-through (as here) or accept any engulfing of the prior range, and on the timeframe used.
- **Costs dominate the small edge.** As with most candle-only patterns, realistic spread, commission, and slippage assumptions can erase a naive backtest's apparent profitability; always validate with a [[backtesting|cost-corrected backtest]].

## Related

- [[candlestick-patterns]]
- [[inside-bar]] — the contraction counterpart
- [[arc-strategy]]
- [[john-wick-candle]]
- [[backtesting]]
- [[support-and-resistance]]

## Sources

- gap-finder Perplexity deep research (2026-06-19) — references a 2024 CodeTrading video and its claimed seven-year forex backtest (87% aggregated win rate, single-creator claim, not independently verified)
- Source video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge
