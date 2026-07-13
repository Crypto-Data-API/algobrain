---
title: "Earnings Yield"
type: concept
created: 2026-04-15
updated: 2026-06-17
status: good
tags: [valuation, fundamental-analysis, stocks]
aliases: ["Earnings Yield", "E/P", "Earnings-to-Price"]
domain: [valuation]
difficulty: beginner
related: ["[[price-to-earnings]]", "[[valuation]]", "[[treasuries]]", "[[fundamental-analysis]]"]
---

Earnings yield is an [[stocks|equity]] valuation metric equal to a company's earnings per share (EPS) divided by its share price — the exact inverse of the [[price-to-earnings|price-to-earnings (P/E) ratio]]. Expressed as a percentage, it tells an investor how many cents of earnings a company generates per dollar invested in its stock, making it directly comparable to the yield on a bond or cash deposit.

## Definition and Formula

$$\text{Earnings Yield} = \frac{\text{EPS}}{\text{Price per Share}} = \frac{1}{\text{P/E ratio}}$$

Equivalently, at the portfolio or index level it can be computed as **total earnings ÷ total market capitalisation**.

| Quantity | Example value |
|----------|---------------|
| Earnings per share (trailing 12-month) | $5.00 |
| Share price | $100.00 |
| **Earnings yield** | **5.0%** |
| **P/E ratio (inverse)** | **20.0×** |

A stock trading at a P/E of 25 has an earnings yield of 1 ÷ 25 = 4.0%. A stock at a P/E of 10 has an earnings yield of 10.0%. The two metrics carry identical information; the yield form is simply more intuitive when comparing equities against fixed-income alternatives, because both are then expressed in the same "percent return per dollar" units.

## Relationship to P/E

Because earnings yield is the reciprocal of the P/E ratio, the two move inversely:

| P/E ratio | Earnings yield | Interpretation |
|-----------|----------------|----------------|
| 5× | 20.0% | Deep value / distressed or cyclical trough |
| 10× | 10.0% | Cheap, often value stocks |
| 15× | 6.7% | Roughly the long-run S&P 500 average |
| 20× | 5.0% | Slight premium |
| 33× | 3.0% | Growth premium |
| 50× | 2.0% | High-growth / speculative |

A key advantage of the yield form: it remains meaningful (and orderable) when earnings approach zero or turn negative. A company with tiny positive EPS has an enormous, near-infinite P/E that is hard to interpret, but a near-zero earnings yield is easy to read. (Both metrics still break down for outright losses — see Limitations.)

Analysts often use **forward earnings yield** (based on estimated next-12-month EPS) rather than trailing earnings, and may use the cyclically-adjusted earnings yield — the inverse of the [[shiller-pe|Shiller CAPE]] — to smooth out the business cycle.

## The "Fed Model"

The most prominent use of earnings yield is in the so-called **Fed model**, which compares the earnings yield of a broad equity index against the yield on the 10-year [[treasuries|US Treasury note]]:

$$\text{Equity Risk Premium (proxy)} = \text{Earnings Yield}_{\text{S\&P 500}} - \text{10Y Treasury Yield}$$

The intuition is that stocks and bonds compete for the same capital, so when the equity earnings yield sits well above the risk-free Treasury yield, equities look relatively cheap (positive spread); when it falls below, bonds look more attractive.

| Scenario | S&P 500 earnings yield | 10Y Treasury yield | Spread | Reading |
|----------|------------------------|--------------------|--------|---------|
| Equities cheap | 7.0% | 3.0% | +4.0% | Stocks attractive vs bonds |
| Roughly fair | 5.0% | 4.5% | +0.5% | Balanced |
| Equities expensive | 4.0% | 5.0% | −1.0% | Bonds attractive vs stocks |

**Caveats.** The Fed model is widely used by practitioners but heavily criticised academically. It compares a *real* magnitude (earnings yield, which tends to rise with inflation as nominal earnings grow) against a *nominal* one (the Treasury yield, which embeds an inflation premium), creating a money-illusion bias. Empirical work (notably by Cliff Asness) finds the model has little power to forecast long-run equity returns; the relationship that held in the 1980s–1990s largely broke down afterward. It is best treated as a sentiment/relative-value gauge, not a precise fair-value tool.

## Use in Value Investing

Earnings yield is a cornerstone of quantitative [[value-investing|value investing]]. Joel Greenblatt's "Magic Formula" (from *The Little Book That Beats the Market*) ranks stocks on a combination of high earnings yield (using EBIT/Enterprise Value rather than simple EPS/Price, to neutralise capital structure) and high return on capital. The earnings-yield leg captures cheapness; the return-on-capital leg captures quality.

More broadly, a high earnings yield signals that the market is pricing in low growth, high risk, or both — the classic hunting ground for value investors looking for mispriced, out-of-favour companies. It is commonly screened alongside dividend yield, free-cash-flow yield, and book-to-market.

## Limitations

- **Accounting earnings are noisy.** EPS is sensitive to write-offs, one-time charges, and accounting choices; a single distorted year can make the yield meaningless. Many investors prefer free-cash-flow yield or EBIT/EV.
- **Negative earnings break the metric.** Loss-making companies produce a negative earnings yield, which cannot be sensibly ranked against bond yields.
- **Ignores growth.** A 4% earnings yield on a fast-growing company can beat a 10% yield on a declining one. Earnings yield says nothing about the *trajectory* of those earnings.
- **Not adjusted for leverage or risk.** Two firms with the same earnings yield can have very different balance-sheet risk.
- **Backward-looking when trailing.** Trailing EPS reflects the past; markets price the future.

## Related

- [[price-to-earnings]] — the reciprocal metric
- [[valuation]] — the broader discipline
- [[treasuries]] — the risk-free benchmark in the Fed model
- [[fundamental-analysis]] — the analytical framework earnings yield sits within
- [[value-investing]] — where earnings yield is most heavily used
- [[shiller-pe]] — cyclically-adjusted variant
- [[dividend-yield]] — a related cash-return metric

## Sources

- General market knowledge; no specific wiki source ingested yet.
