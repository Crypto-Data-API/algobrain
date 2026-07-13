---
title: Relative Strength
type: concept
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [technical-analysis, momentum, sector-rotation]
aliases: [RS, comparative relative strength, relative performance, relative-strength]
related:
  - "[[momentum-trading]]"
  - "[[momentum-screening]]"
  - "[[trend]]"
  - "[[market-breadth]]"
  - "[[relative-strength-rating]]"
  - "[[rsi]]"
  - "[[relative-strength-index]]"
  - "[[sector-rotation]]"
  - "[[pairs-trading]]"
domain: [technical-analysis]
prerequisites: ["[[trend]]", "[[momentum]]"]
difficulty: beginner
---

Relative strength is a measure of how one asset's price performance compares to another asset or benchmark over a given period, used to identify leaders and laggards. It is the conceptual foundation for momentum investing, sector rotation, and pairs trading, and should not be confused with the [[rsi|Relative Strength Index]], which is a single-asset oscillator.

## How It Works

Relative strength is calculated by dividing the price of one security by the price of a benchmark and tracking the ratio over time:

**RS line = price(asset) / price(benchmark)**

A rising RS line means the asset is outperforming the benchmark; a falling RS line means underperformance. The absolute level of the ratio is meaningless — only its slope and trend carry information. A common variant is **relative return spread**: the asset's percentage return over a lookback (e.g., 3, 6, or 12 months) minus the benchmark's return over the same window. Cross-sectional momentum screens rank an entire universe by this spread and hold the top decile.

## Relative Strength vs. RSI — Do Not Confuse Them

The single most common source of confusion in technical analysis is that two very different tools share the words "relative strength." They measure unrelated things:

| Feature | **Relative Strength (this page)** | **[[relative-strength-index|Relative Strength Index (RSI)]]** |
|---------|----------------------------------|--------------------------------------------------------------|
| What it compares | One asset **vs. another asset/benchmark** (e.g., AAPL vs. S&P 500) | One asset **vs. its own recent price history** |
| Inputs | Two price series (ratio or return spread) | One price series (average gains vs. average losses, default 14 periods) |
| Output | An unbounded **RS line** (ratio) or a return-spread ranking | A bounded **oscillator, 0-100** |
| What it tells you | Who is leading and who is lagging — *outperformance* | Overbought (>70) / oversold (<30) — *momentum extremes* |
| Primary use | [[momentum-trading]], [[sector-rotation]], stock selection, [[pairs-trading]] | Mean-reversion timing, divergence signals |
| Created/popularized by | R. A. Levy (1967); [[william-oneil\|O'Neil]]'s RS line | J. Welles Wilder (1978) |

Bottom line: **Relative Strength is cross-asset (comparative); RSI is single-asset (internal).** A stock can have a high RS line (crushing the market) while its RSI is overbought — they are answering different questions. A third related-but-distinct term is the [[relative-strength-rating|RS Rating]], IBD's proprietary 1-99 percentile rank of a stock's price performance against the entire market over the trailing ~12 months.

## How It Is Measured

Two common formulations of comparative relative strength:

1. **RS line (ratio).** `RS = price(asset) / price(benchmark)`, plotted over time. A new high in the RS line means the asset is making new *relative* highs vs. the benchmark even if its absolute price has not — a classic leadership tell. [[william-oneil|O'Neil]] popularized watching the RS line confirm a price breakout.
2. **Return spread (cross-sectional).** `RS = return(asset, lookback) − return(benchmark, lookback)` over 3, 6, or 12 months. This is the form used in quantitative [[momentum-screening]]: rank the whole universe by spread and hold the top decile.

### Worked Example

*Illustrative, rounded numbers.* Over the last 6 months the S&P 500 returned **+8%**. Stock A returned **+20%**, stock B returned **+9%**, stock C returned **−4%**.

- **Return spreads:** A = +20 − 8 = **+12%** (strong leader), B = +9 − 8 = **+1%** (roughly in line — beta, not leadership), C = −4 − 8 = **−12%** (clear laggard).
- **RS line read:** A's `price/SPX` ratio is making higher highs (rising line); C's ratio is making lower lows (falling line) even on any short bounces.

Note that B was *up* in absolute terms yet has almost no relative strength — in a +8% market, simply rising is not leadership. This is exactly why momentum screens use RS rather than raw return: it strips out market beta and surfaces the names with genuine, idiosyncratic outperformance.

## Applications

- **Sector Rotation** - Identifying which sectors are leading or lagging the broad market
- **Stock Selection** - Within a strong sector, choosing stocks with the highest RS
- **Pair Trading** - Going long the strong name and short the weak one
- **Market Regime** - When defensive sectors show rising RS, it may signal risk-off conditions

## Trading Relevance

Relative strength is central to [[momentum-trading]] strategies. Stocks showing persistent RS leadership tend to continue outperforming (momentum effect). Fund managers use RS rankings to overweight strong sectors and underweight weak ones.

## How Traders Use This

- **Leadership screening.** Buy strength, avoid weakness: rank a universe by RS and concentrate on the top decile/quintile, the core input to [[momentum-screening]].
- **RS-line breakout confirmation.** A stock breaking out on price while its RS line also makes new highs has institutional sponsorship behind the move; a price breakout *without* RS confirmation is suspect.
- **[[sector-rotation]].** Plot each [[gics-sectors|sector]] ETF's RS vs. the broad index to see where money is flowing. Rising RS in cyclicals/tech signals risk-on; rising RS in staples, utilities, and healthcare signals risk-off.
- **[[pairs-trading]].** Within a correlated pair, go long the high-RS leg and short the low-RS leg to express relative outperformance while hedging market beta.
- **Regime read.** Defensive sectors gaining RS while the index still rises is an early breadth warning that the rally is narrowing.

## Common Pitfalls and Risks

- **Backward-looking.** RS measures past outperformance; chasing it can mean buying late in a rotation just before mean reversion.
- **No valuation or fundamental check.** A name can have stellar RS while fundamentals quietly deteriorate; pair RS with [[earnings-revision]] or quality screens.
- **Confusion with [[relative-strength-index|RSI]].** As detailed above, they are different tools — using an overbought RSI to "fade" a high-RS leader is a frequent and costly error.
- **Benchmark sensitivity.** RS depends entirely on the chosen benchmark; the wrong benchmark (e.g., comparing a small cap to the S&P 500) produces misleading reads. Match the comparison to the asset's peer group.
- **Whipsaw at inflections.** Near market turns, RS rankings reshuffle violently (momentum crashes), so RS-driven books need [[trend]] and [[market-breadth]] overlays for context.

## Related

- [[momentum-trading]] — strategy family built on persistence of relative strength
- [[momentum-screening]] — ranks a universe by RS / return spread
- [[relative-strength-rating]] — IBD's percentile-ranked implementation
- [[relative-strength-index]] / [[rsi]] — the differently-named single-asset oscillator (not the same thing)
- [[sector-rotation]] — RS applied across sectors
- [[pairs-trading]] — long the strong leg, short the weak leg
- [[trend]] / [[market-breadth]] — confirming context

## Sources

- Jegadeesh, N. and Titman, S., "Returns to Buying Winners and Selling Losers," *Journal of Finance* (1993) — foundational evidence for the relative-strength / momentum effect
- O'Neil, W. J., *How to Make Money in Stocks* — popularized the RS line and RS-based stock selection
- Levy, R. A., "Relative Strength as a Criterion for Investment Selection," *Journal of Finance* (1967) — early academic treatment of relative-strength selection
