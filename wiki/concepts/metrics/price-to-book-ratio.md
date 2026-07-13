---
title: "Price-to-Book Ratio"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, value-investing, valuation]
aliases: ["P/B Ratio", "Price-Book Ratio", "Price-to-Book", "price-to-book", "PB Ratio"]
related: ["[[price-to-earnings-ratio]]", "[[value-investing]]", "[[fundamental-analysis]]", "[[margin-of-safety]]", "[[benjamin-graham]]", "[[book-value]]", "[[valuation]]", "[[return-on-equity]]"]
domain: [fundamental-analysis]
difficulty: beginner
---

The price-to-book ratio (P/B) is a valuation metric calculated by dividing a company's stock price by its book value per share. Book value represents shareholders' equity on the balance sheet — total assets minus total liabilities. A P/B below 1.0 means the stock trades below its net asset value, which was one of [[benjamin-graham]]'s most important criteria for identifying undervalued securities.

## Overview

P/B ratio measures what investors are willing to pay for each dollar of a company's accounting net worth. A P/B of 2.0 means investors pay $2 for every $1 of book value; a P/B of 0.7 means they pay only $0.70 — implying the market values the company at less than its liquidation value.

Graham and [[david-dodd]] emphasized P/B in [[book-security-analysis|Security Analysis]] (1934) as a way to find stocks trading below their "net-net" value — companies whose current assets minus all liabilities exceeded their market capitalization. These "cigar butt" investments offered a quantifiable [[margin-of-safety]] because even in liquidation, investors would theoretically recover more than they paid.

In [[book-the-intelligent-investor|The Intelligent Investor]], Graham recommended that defensive investors limit purchases to stocks with P/B ratios below 1.5 (or alternatively, P/E x P/B should not exceed 22.5). This screen aimed to prevent overpaying for assets regardless of earnings projections.

## How It Works

**Calculation**: P/B = Market Price per Share / Book Value per Share

Where Book Value per Share = (Total Assets − Total Liabilities − Preferred Equity) / Common Shares Outstanding

Equivalently, at the whole-company level, P/B = [[market-capitalization|Market Cap]] / [[book-value|Total Common Shareholders' Equity]] — the two formulations are identical.

### Worked example

Suppose a bank has total assets of $50,000M, total liabilities of $45,000M, no preferred stock, and 200M shares outstanding:

- Book value (common equity) = $50,000M − $45,000M = **$5,000M**
- Book value per share = $5,000M / 200M = **$25.00**
- If the stock trades at **$20.00**, then P/B = $20 / $25 = **0.80** — it trades at a 20% discount to its accounting net worth.
- If instead it trades at **$45.00**, P/B = $45 / $25 = **1.80** — a premium that implies the market expects [[return-on-equity|ROE]] above the cost of equity.

### Tangible book value

For firms carrying large goodwill or intangibles from acquisitions, analysts strip those out to get a harder number:

```
Tangible Book Value = Total Equity − Goodwill − Intangible Assets − Preferred
Price-to-Tangible-Book (P/TBV) = Market Cap / Tangible Book Value
```

P/TBV is the standard for banks and insurers, because goodwill cannot absorb loan losses — only tangible capital can. A bank trading at 1.5x stated book but 2.5x *tangible* book is far less of a bargain than the headline P/B suggests.

### The P/B–ROE link

P/B does not float free of profitability. In the Gordon-growth framing, justified P/B ≈ (ROE − g) / (r − g), where r is the cost of equity and g the growth rate. The practical takeaway: **a high P/B is justified by high [[return-on-equity|ROE]]; a low P/B paired with low ROE is a value trap, not a bargain.** A firm earning 5% ROE *should* trade below book; one earning 25% ROE deserves a multiple of book.

**Interpreting P/B values**:

- **P/B < 1.0**: Stock trades below net asset value. May indicate undervaluation, financial distress, or impaired assets. Classic Graham deep-value territory.
- **P/B 1.0-3.0**: Typical range for mature industrial, financial, and utility companies.
- **P/B > 5.0**: Common for asset-light businesses (technology, services) where intellectual property, brand value, and human capital are not captured on the balance sheet.
- **Negative book value**: Possible when accumulated losses exceed initial capital. Makes P/B meaningless — often signals severe financial distress or heavy share buybacks funded by debt.

**Sector considerations**: P/B is most useful for asset-heavy industries (banking, insurance, real estate, manufacturing) where book value meaningfully approximates the value of tangible assets. It is less useful for technology and service companies where the most valuable assets (software, patents, talent) do not appear on the balance sheet.

### Typical P/B by sector

Illustrative order-of-magnitude bands (not live data — verify against current figures):

| Sector | Typical P/B | Why |
|---|---|---|
| Banks / insurers | 0.7 – 1.5x | Balance sheet *is* the business; P/TBV is the real gauge |
| REITs / real estate | 0.8 – 2.0x | Asset-backed; NAV often replaces book |
| Utilities | 1.0 – 2.0x | Heavy regulated asset base |
| Industrials / manufacturing | 1.5 – 4x | Tangible plant plus going-concern premium |
| Consumer staples | 3 – 8x | Brand value not on the balance sheet |
| Software / internet | 5 – 20x+ | Asset-light; book value nearly meaningless |

Because the spread is so wide, **P/B is only comparable within a sector or against a company's own history** — never across industries.

## Pitfalls and Value Traps

- **Low P/B ≠ cheap.** Pair it with [[return-on-equity|ROE]]. Persistently low ROE justifies a sub-1 P/B; the discount is the market pricing in poor returns, not a free lunch.
- **Book value is historical cost.** Land bought decades ago, depreciated buildings, and impaired-but-not-written-down assets distort book value in both directions.
- **Intangible-heavy firms.** For tech/pharma/services, book value omits the assets that matter (code, patents, brand, talent), so a high P/B is structural, not a bubble signal.
- **Buyback distortion.** Repurchasing shares above book value *reduces* equity and can push P/B up or even drive book value negative, making the ratio meaningless.
- **Negative book value.** Accumulated losses or debt-funded buybacks can produce negative equity; P/B then has no economic meaning.
- **Mark-to-market lag (banks).** A bank's stated book may not yet reflect deteriorating loan quality. A P/B well below 1 is often the market front-running write-downs, as in 2008-09 financials.

## Trading Applications

- **Value factor**: In academic finance, low P/B (or equivalently, high book-to-market) is one of the Fama-French factors that historically generated excess returns. The "value premium" — the tendency of low P/B stocks to outperform high P/B stocks over time — is one of the most documented anomalies in finance.
- **Bank valuation**: P/B is the primary valuation metric for banks and financial institutions, where the balance sheet (loans, deposits, securities) directly drives earnings. Banks trading below book value often signal credit quality concerns.
- **Net-net investing**: Graham's most extreme value strategy — buying stocks at less than net current asset value (current assets minus all liabilities). [[warren-buffett]] used this approach early in his career before shifting to quality-focused investing.
- **Screening**: P/B combined with [[price-to-earnings-ratio|P/E]], [[dividend]] yield, and debt ratios creates a robust multi-factor value screen. No single metric is sufficient in isolation.
- **Cyclical timing**: P/B is useful for valuing cyclical companies whose earnings fluctuate wildly. When earnings are depressed, P/E may look high, but P/B reveals whether the stock is cheap relative to its asset base.

## Related

- [[price-to-earnings-ratio]] — Companion valuation metric based on earnings
- [[book-value]] — The denominator; shareholders' equity
- [[return-on-equity]] — The profitability that justifies a P/B level
- [[value-investing]] — Investment philosophy built around buying below intrinsic value
- [[margin-of-safety]] — The gap between price and intrinsic value
- [[valuation]] — Broader valuation framework
- [[fundamental-analysis]] — Analytical framework for evaluating company worth
- [[benjamin-graham]] — Pioneer of P/B-based value investing

## Sources

- (Source: [[book-the-intelligent-investor]]) — Graham's P/B screening criteria for defensive investors
- (Source: [[book-security-analysis]]) — Graham and Dodd's original net-net and book value analysis framework
