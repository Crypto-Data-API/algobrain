---
title: "Dividend Payout Ratio"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, metrics, dividends, income-investing]
aliases: ["Payout Ratio", "payout ratio", "dividend payout ratio"]
domain: [fundamental-analysis]
prerequisites: ["[[earnings-per-share]]", "[[free-cash-flow]]"]
difficulty: beginner
related: ["[[dividend-yield]]", "[[dividend]]", "[[earnings-per-share]]", "[[free-cash-flow]]", "[[franking-credits]]", "[[two-portfolio-strategy]]"]
---

The **dividend payout ratio** is the share of a company's earnings paid out to shareholders as cash dividends, expressed as a percentage. Its complement is the **retention ratio** (the fraction of earnings reinvested in the business). It is the primary gauge of dividend *sustainability* and the natural partner metric to [[dividend-yield]], which measures the dividend relative to price rather than to earnings.

## Formula

```
Payout Ratio = Dividends Per Share / Earnings Per Share
            = Total Dividends / Net Income

Retention Ratio = 1 − Payout Ratio
```

A company earning $4.00 EPS and paying $1.20 in dividends has a 30% payout ratio and a 70% retention ratio.

A more conservative variant divides by [[free-cash-flow]] rather than accounting net income, because dividends are paid in cash and earnings can be inflated by non-cash accruals:

```
Cash Payout Ratio = Dividends / Free Cash Flow
```

## Interpretation

| Payout Ratio | Interpretation |
|---|---|
| < 40% | Conservative — ample room to reinvest and to grow the dividend |
| 40% – 60% | Healthy, typical for mature profitable firms |
| 60% – 80% | Stretched but generally sustainable |
| > 80% | Cut risk elevated; little buffer for an earnings downturn |
| > 100% | Unsustainable — the firm is funding the dividend from debt, cash reserves, or asset sales |

Young, fast-growing companies typically pay nothing (0% payout, 100% retention) because they earn higher returns reinvesting internally than shareholders could earn elsewhere. Mature, cash-generative firms with few growth options return more. **[[reit|REITs]] are a structural exception**: U.S. REITs must distribute at least 90% of taxable income to retain their tax-advantaged status, so a 90%+ payout there is normal rather than alarming.

## Link to Sustainable Growth

The payout ratio connects directly to the **sustainable growth rate** of equity:

```
Sustainable Growth Rate = Retention Ratio × Return on Equity (ROE)
```

A firm retaining 60% of earnings at a 15% [[return-on-equity|ROE]] can self-fund roughly 9% growth without raising external capital. This is why a rising payout ratio can be an early warning that a company has run out of high-return reinvestment opportunities.

## Trading Relevance

The payout ratio is the first thing income-focused traders check to distinguish a sustainable [[dividend-yield|yield]] from a **yield trap**. A high yield backed by a >100% payout ratio almost always precedes a dividend cut — and the announced cut typically triggers a sharp price drop as income funds and dividend ETFs forced-sell the position. Dividend-quality indices (e.g., the underlying screens for high-quality dividend ETFs) explicitly filter out companies with payout ratios above a threshold to avoid these traps. Conversely, a low and stable payout ratio combined with consistent dividend growth is the signature of the **dividend-growth** factor. In the Australian market, the payout ratio is examined alongside [[dividend-yield]] and [[franking-credits]] when building the income leg of a [[two-portfolio-strategy]].

## Limitations

- **Earnings volatility** distorts the ratio for cyclicals — a fixed dividend produces a payout ratio that swings wildly with the cycle. Average across a full cycle.
- **Net income vs cash** — accrual earnings can diverge from cash; prefer the cash-flow-based payout ratio for capital-intensive firms.
- **Buybacks ignored** — total shareholder yield (dividends + net buybacks) is a more complete picture of capital return than the dividend payout ratio alone.

## Related

- [[dividend-yield]] — dividend relative to price; always read alongside the payout ratio
- [[dividend]], [[earnings-per-share]], [[free-cash-flow]]
- [[return-on-equity]] — combines with retention to set sustainable growth
- [[franking-credits]], [[two-portfolio-strategy]]

## Sources

- CFA Institute curriculum, *Equity Investments* — dividend policy, payout/retention ratios, and the sustainable growth rate
- Damodaran, A., *Investment Valuation* — payout policy and its link to growth and reinvestment
- U.S. Internal Revenue Code §856–§859 — REIT 90% distribution requirement
