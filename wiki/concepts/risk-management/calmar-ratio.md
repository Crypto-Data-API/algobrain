---
title: "Calmar Ratio"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [risk-management, quantitative, backtesting, portfolio-theory]
aliases: ["Calmar", "Drawdown Ratio", "MAR Ratio"]
domain: [risk-management, quantitative]
prerequisites: ["[[maximum-drawdown]]", "[[sharpe-ratio]]"]
difficulty: intermediate
related:
  - "[[sharpe-ratio]]"
  - "[[sortino-ratio]]"
  - "[[maximum-drawdown]]"
  - "[[drawdown]]"
  - "[[risk-adjusted-return]]"
  - "[[volatility]]"
  - "[[risk-of-ruin]]"
---

# Calmar Ratio

The **Calmar ratio** measures risk-adjusted return by dividing a strategy's annualized return by its worst peak-to-trough loss — its [[maximum-drawdown]]. Where the [[sharpe-ratio|Sharpe ratio]] penalizes *volatility* and the [[sortino-ratio|Sortino ratio]] penalizes *downside volatility*, the Calmar ratio penalizes the single most painful experience an investor actually lives through: the deepest decline. That makes it a favourite of managed-futures and trend-following traders, and an intuitive answer to the common trader question *"how much return am I getting for the worst loss I'd have had to sit through?"*

## Formula

```
Calmar ratio = Annualized return / | Maximum drawdown |
```

Both terms are usually measured over the same window — conventionally a **trailing 36 months (3 years)** in the original definition, though backtests often report it over the full sample.

- **Numerator:** compound annual growth rate (CAGR) of the strategy.
- **Denominator:** the [[maximum-drawdown]] over the window, expressed as a positive number (e.g., a −25% drawdown is entered as 0.25).

A closely related metric, the **MAR ratio**, uses the same formula but over the *entire* track record rather than a rolling 3-year window.

## How to Interpret It

| Calmar ratio | Rough interpretation |
|---|---|
| < 0.5 | Weak — the worst drawdown is large relative to the return earned |
| 0.5 – 1.0 | Modest risk-adjusted performance |
| 1.0 – 3.0 | Solid; commonly seen in respected systematic strategies over good periods |
| > 3.0 | Excellent — but treat with suspicion over short or lucky samples |

Higher is better: more annual return per unit of worst-case pain. A Calmar of 2.0 means the strategy earned, per year, twice its deepest historical decline.

### Worked example (hypothetical)

A strategy compounds at **18% per year** over three years and, somewhere in that window, suffered a **−12% peak-to-trough drawdown**:

```
Calmar ratio = 0.18 / 0.12 = 1.5
```

Now compare two strategies with the *same* 18% annual return but different worst losses: one with a −12% drawdown scores 1.5, while one with a −36% drawdown scores only 0.5. Identical returns, very different lived experience — and the Calmar ratio is what surfaces that difference, where a returns-only comparison would hide it. (Numbers are illustrative.)

## Why It Matters

- **It targets the failure mode investors actually quit on.** Most people abandon a strategy at the bottom of a deep drawdown, not because of day-to-day [[volatility]]. By scoring on [[maximum-drawdown]], the Calmar ratio rewards strategies an investor can realistically hold through.
- **It is intuitive and hard to game with smooth-but-fragile returns.** A strategy that sells volatility and clips small steady gains can post a flattering [[sharpe-ratio|Sharpe]] right up until a crash; the Calmar ratio reflects that crash directly in the denominator.
- **It connects to [[risk-of-ruin]] and [[position-sizing]].** Because the denominator is the worst loss, the Calmar ratio is naturally aligned with capital-survival thinking.

## Calmar vs Sharpe vs Sortino

| Ratio | Risk measure in denominator | Punishes |
|---|---|---|
| [[sharpe-ratio\|Sharpe]] | Total standard deviation | All volatility, up and down |
| [[sortino-ratio\|Sortino]] | Downside deviation | Only downside volatility |
| **Calmar** | Maximum drawdown | The single worst peak-to-trough loss |

The three are complementary. Sharpe and Sortino summarise the *typical* path; Calmar summarises the *worst* path. A complete review looks at all three: a strategy can have a good Sharpe yet an alarming Calmar if its losses, though infrequent, are catastrophic.

## Limitations

- **Driven by a single observation.** The maximum drawdown is one event in the sample, so the Calmar ratio is **statistically fragile** — extend or shorten the window and it can swing sharply. It is far noisier than Sharpe, which uses the whole return distribution.
- **Sample-length bias.** A longer track record has more chances to print a deep drawdown, mechanically lowering Calmar. Comparing strategies over different-length histories is misleading.
- **Backward-looking.** The worst drawdown *so far* is not the worst drawdown *possible*; the next one can be larger. The ratio says nothing about the [[tail-risk|unrealized tail]].
- **Ignores drawdown duration.** A −20% drop recovered in a month and one that takes three years to recover score identically, yet the second is far harder to endure. Pairing it with drawdown *duration* (time underwater) gives a fuller picture.

## Related

- [[maximum-drawdown]] — the denominator; the worst peak-to-trough loss
- [[drawdown]] — the underlying concept of decline from a high-water mark
- [[sharpe-ratio]] — risk-adjusted return using total volatility
- [[sortino-ratio]] — risk-adjusted return using only downside volatility
- [[volatility]] — the alternative risk measure the Calmar ratio deliberately avoids
- [[risk-of-ruin]] — the survival question the Calmar ratio's denominator speaks to
- [[risk-adjusted-return]] — the broader family of metrics this belongs to

## Sources

- Young, T. W. (1991). "Calmar Ratio: A Smoother Tool." *Futures* magazine — the article that introduced the ratio; the name derives from the author's company, California Managed Accounts Reports.
