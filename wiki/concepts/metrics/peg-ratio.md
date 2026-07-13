---
title: "PEG Ratio"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, momentum]
aliases: ["PEG", "PEG ratio", "price/earnings to growth", "peg-ratio"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[price-to-earnings-ratio]]", "[[earnings-per-share]]"]
difficulty: beginner
related: ["[[price-to-earnings-ratio]]", "[[earnings-per-share]]", "[[canslim]]", "[[price-to-sales-ratio]]", "[[fundamental-analysis]]"]
---

The **PEG ratio** (Price/Earnings to Growth) adjusts the [[price-to-earnings-ratio|P/E ratio]] for expected earnings growth. It was popularized by **Peter Lynch** in *One Up on Wall Street* (1989) as a quick way to determine whether a high-multiple stock is actually expensive once growth is accounted for.

## Formula

```
PEG = (Price / EPS) / Earnings Growth Rate (%)
    = P/E Ratio / Annual EPS Growth Rate (%)
```

Note: the growth rate is entered as a whole number, not a decimal. A stock with a P/E of 20 and 20% expected growth has a PEG of 20 / 20 = **1.0**.

## Lynch's Interpretation

Lynch's rule of thumb:

| PEG | Interpretation |
|---|---|
| < 0.5 | Very cheap, potential bargain |
| 0.5 – 1.0 | Undervalued relative to growth |
| ≈ 1.0 | Fairly valued |
| 1.0 – 2.0 | Getting expensive |
| > 2.0 | Overvalued |

The rationale is intuitive: a fast-growing company with a 30x P/E may actually be *cheaper* than a slow-growing one trading at 12x, because the earnings base beneath the multiple is compounding. PEG normalizes for that difference.

## Choosing the Growth Rate

Which growth rate you plug in matters enormously. Common choices:

- **Forward 5-year EPS growth estimate** (most common, typically from consensus analyst estimates)
- **Trailing 3-5 year historical growth** (more objective but backward-looking)
- **Forward 1-year growth** (noisy, too short to be meaningful)

Because PEG is linear in the denominator, halving the growth assumption doubles the PEG. This makes the metric highly sensitive to analyst optimism — a stock with "25% growth" per sell-side that actually delivers 12% will look twice as cheap as it really is.

## Limitations

1. **Negative or zero earnings break PEG entirely** — unusable for unprofitable growth companies (use [[price-to-sales-ratio|P/S]] instead).
2. **Ignores risk and capital structure** — a 20% grower with high leverage is not the same as a 20% grower with net cash.
3. **Ignores quality of earnings** — acquisitive companies can manufacture EPS growth that inflates the denominator.
4. **Growth mean-reverts** — high rates rarely persist for the full projection window.

## Variants

**PEGY** (Peter Lynch's own refinement) adds dividend yield to the denominator: PEGY = P/E / (Growth + Dividend Yield). This rewards dividend-paying compounders that straight PEG penalizes.

PEG is a key input in [[canslim]] and other growth-at-a-reasonable-price (GARP) frameworks.

## Trading Relevance

PEG is the workhorse ratio of **GARP (growth at a reasonable price)** trading — the middle ground between deep value and pure momentum. A practical PEG screen (e.g. PEG < 1 with positive and accelerating earnings revisions) tends to surface stocks that are both reasonably priced *and* have an earnings tailwind, which historically combines two rewarded factors: cheapness and earnings momentum. Because PEG is so sensitive to the growth input, the **edge comes from the denominator, not the headline number**: traders who can forecast that consensus growth is too low (and therefore PEG is overstated) get paid when estimates are revised up and the multiple re-rates. The most common failure mode in practice is mechanically buying low-PEG names whose "growth" is sell-side optimism that never materialises — so PEG is best used as a *filter into* further work, not a standalone buy signal. For unprofitable growth names where PEG breaks down entirely, switch to [[price-to-sales-ratio|P/S]] plus the Rule of 40.

## Related

- [[price-to-earnings-ratio]], [[earnings-per-share]]
- [[canslim]], [[fundamental-analysis]]

## Sources

- Lynch, Peter. *One Up on Wall Street* (Simon & Schuster, 1989) — origin of PEG and PEGY.
- Damodaran, Aswath. *Investment Valuation* (Wiley) — PEG, growth-adjusted multiples and their pitfalls.
- CFA Institute, *Equity Valuation* curriculum — relative valuation and the PEG ratio.
