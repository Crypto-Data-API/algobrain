---
title: "Altman Z-Score"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [fundamental-analysis, risk-management, valuation]
domain: [fundamental-analysis, risk-management]
prerequisites: ["[[balance-sheet]]", "[[income-statement]]", "[[working-capital]]"]
difficulty: intermediate
aliases: ["Altman Z-Score", "altman-z-score", "Z-Score", "Z-Score Model"]
related: ["[[credit-risk]]", "[[interest-coverage-ratio]]", "[[working-capital]]", "[[leverage]]", "[[fundamental-analysis]]", "[[solvency]]", "[[balance-sheet]]", "[[cash-flow-statement]]", "[[short-selling]]"]
---

The Altman Z-Score is a multivariate bankruptcy-prediction model published by NYU finance professor Edward Altman in 1968. It combines five financial ratios — each weighted by a fixed coefficient — into a single score that estimates how close a company is to financial distress. It was one of the first widely-adopted applications of multiple discriminant analysis to corporate credit, and it remains a standard first-pass screen in [[fundamental-analysis]] and [[credit-risk]] work.

## What it is

Altman built the model on a sample of manufacturing firms, half of which had gone bankrupt, and used discriminant analysis to find the weighted combination of balance-sheet and income-statement ratios that best separated the survivors from the failures. The output is a single number: higher scores indicate financial health, lower scores indicate rising distress risk. Because it compresses profitability, liquidity, leverage, solvency, and asset efficiency into one figure, it functions as a quick, rules-based proxy for a firm's probability of default over roughly a one- to two-year horizon.

## The formula (classic manufacturing model)

The original public-manufacturer model is:

**Z = 1.2·X₁ + 1.4·X₂ + 3.3·X₃ + 0.6·X₄ + 1.0·X₅**

| Ratio | Definition | What it captures |
|-------|------------|------------------|
| X₁ | Working Capital / Total Assets | Short-term liquidity — the buffer of current assets over current liabilities relative to size ([[working-capital]]) |
| X₂ | Retained Earnings / Total Assets | Cumulative profitability and age — how much the firm has self-funded over its life ([[retained-earnings]]) |
| X₃ | EBIT / Total Assets | Operating productivity of assets, independent of tax and financing ([[ebit]]) |
| X₄ | Market Value of Equity / Total Liabilities | Solvency cushion — how far equity value can fall before liabilities exceed assets ([[market-capitalization]], [[leverage]]) |
| X₅ | Sales / Total Assets | Asset turnover — revenue generated per dollar of assets |

The X₃ term carries the largest coefficient, reflecting that operating earnings power is the strongest single discriminator between healthy and failing firms in Altman's data.

## The zones

The score maps to three interpretive bands:

| Zone | Range | Interpretation |
|------|-------|----------------|
| **Distress** | Z < 1.81 | High probability of bankruptcy within ~2 years |
| **Grey** | 1.81 ≤ Z ≤ 2.99 | Ambiguous — no clear signal either way |
| **Safe** | Z > 2.99 | Low near-term bankruptcy risk |

The grey zone is deliberate: the model does not claim to classify every firm, and scores in the 1.81–2.99 band should be treated as "watch, gather more evidence" rather than a verdict.

## Variants

Because the market-value term (X₄) and the sales term (X₅) do not travel well across firm types, Altman published two recalibrations:

- **Z'-Score (private firms).** Replaces the *market* value of equity in X₄ with the *book* value of equity, so the model can be applied to companies without a traded stock price. The coefficients are re-estimated: **Z' = 0.717·X₁ + 0.847·X₂ + 3.107·X₃ + 0.420·X₄ + 0.998·X₅**, with zones of Distress < 1.23, Grey 1.23–2.90, Safe > 2.90.
- **Z''-Score (non-manufacturers / emerging markets).** Drops the sales-to-assets ratio (X₅) entirely, because asset turnover varies too much across industries to be comparable — retailers, service firms, and asset-light businesses would be penalised or flattered unfairly. The four-factor model is **Z'' = 6.56·X₁ + 3.26·X₂ + 6.72·X₃ + 1.05·X₄** (using book equity in X₄), with zones of Distress < 1.1, Grey 1.1–2.6, Safe > 2.6. An emerging-market variant adds a constant of +3.25 to shift the scale.

## Use in practice

- **Distress screening** — running the Z-Score across a portfolio or watchlist flags names whose fundamentals are deteriorating toward the distress band, prompting deeper review before a covenant breach or downgrade is public.
- **Credit analysis** — it complements the standard toolkit of [[interest-coverage-ratio]], [[leverage]] ratios, [[current-ratio|liquidity ratios]], and [[cash-flow-statement|cash-flow]] analysis, giving a single trend line that credit analysts can track quarter over quarter. It is one of several signals discussed in [[credit-risk]] for how distress reaches equity holders.
- **Short-candidate screening** — a persistently low or falling Z-Score, especially alongside negative operating cash flow and high leverage, is a common ingredient in a [[short-selling]] thesis. It is a screen, not a trigger: many low-Z firms survive for years.
- **Complement, not substitute** — analysts pair it with the [[piotroski-f-score]], solvency and coverage ratios, and a read of the [[cash-flow-statement]] rather than relying on the single number.

## Worked example

Consider an illustrative public manufacturer (round numbers, not a real company):

- Total Assets = $1,000m
- Working Capital = $50m → X₁ = 0.05
- Retained Earnings = $100m → X₂ = 0.10
- EBIT = $40m → X₃ = 0.04
- Market Value of Equity = $150m; Total Liabilities = $750m → X₄ = 0.20
- Sales = $700m → X₅ = 0.70

Applying the classic coefficients:

```
Z = 1.2(0.05) + 1.4(0.10) + 3.3(0.04) + 0.6(0.20) + 1.0(0.70)
  = 0.060    + 0.140     + 0.132     + 0.120     + 0.700
  = 1.15
```

Z ≈ **1.15**, which sits below 1.81 and therefore lands in the **distress zone**. The low market-equity-to-liabilities term (0.20) and thin operating margin are the main drags — the firm is heavily levered and its assets are only modestly productive. A healthy peer with stronger earnings power, more retained equity, and a larger market-value cushion would clear the 2.99 threshold and score in the safe zone.

## Limitations

- **Built on 1960s manufacturers.** The coefficients were estimated on a small sample of industrial firms from that era; they do not transfer cleanly to modern business models. The Z'' variant exists precisely because the original mis-scores non-manufacturers.
- **Weak for banks, insurers, and asset-light software.** Financials carry leverage and working-capital structures the model was never designed for, and asset-light software or platform companies have little in the way of the tangible assets and working capital the ratios assume — so the score is unreliable for both.
- **Point-in-time and backward-looking.** It reads a single balance sheet and income statement, so it lags reality and can miss a fast-developing liquidity crisis between reporting dates.
- **Gameable.** Because the inputs are accounting figures, they are subject to the same distortions as any [[fundamental-analysis|fundamental]] ratio — off-balance-sheet financing, one-off items, and aggressive revenue recognition can flatter the score.
- **Not a substitute for full credit analysis.** The Z-Score is a screen and a summary statistic, not a rating. Serious credit work still requires reading covenants, maturity walls, [[cash-flow-statement|cash-flow generation]], and the [[balance-sheet]] in detail.

## Related

[[credit-risk]] · [[interest-coverage-ratio]] · [[working-capital]] · [[leverage]] · [[solvency]] · [[fundamental-analysis]] · [[balance-sheet]] · [[income-statement]] · [[cash-flow-statement]] · [[current-ratio]] · [[return-on-assets]] · [[short-selling]] · [[market-capitalization]] · [[piotroski-f-score]]

## Sources

- Edward I. Altman, "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy," *Journal of Finance* 23(4), 1968 — the original paper introducing the five-ratio Z-Score model and its coefficients. The later Z'- and Z''-Score recalibrations appear in Altman's subsequent work and are reproduced in standard corporate-finance and credit-analysis texts. The coefficients and zone thresholds stated here are the published, widely-taught values.
