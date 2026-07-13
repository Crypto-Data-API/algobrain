---
title: "Interest Coverage Ratio"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, leverage, risk-management, valuation]
aliases: ["interest coverage ratio", "times interest earned", "TIE", "EBIT/Interest", "interest cover"]
domain: [fundamental-analysis]
difficulty: beginner
prerequisites: ["[[operating-income]]", "[[debt-to-equity]]"]
related: ["[[debt-to-equity]]", "[[ebitda]]", "[[operating-income]]", "[[free-cash-flow]]", "[[current-ratio]]", "[[balance-sheet]]", "[[net-income]]", "[[financial-statement-analysis]]"]
---

The **interest coverage ratio** measures how many times over a company can pay the interest on its outstanding debt from its operating earnings. It is one of the most direct tests of solvency and a core input to credit analysis: a company can survive low profitability for a while, but a company that cannot cover its interest bill is on a path to default. It is also called **times interest earned (TIE)**.

## Formula

The most common form divides operating income ([[operating-income|EBIT]]) by interest expense:

$$\text{Interest Coverage} = \frac{\text{EBIT}}{\text{Interest Expense}}$$

Both figures come from the income statement. **EBIT** (earnings before interest and taxes) is operating profit before financing costs; **interest expense** is the periodic cost of servicing debt. Some analysts substitute [[ebitda|EBITDA]] for EBIT to approximate cash available for debt service:

$$\text{EBITDA Coverage} = \frac{\text{EBITDA}}{\text{Interest Expense}}$$

A stricter, more conservative variant uses **(EBIT − capex)** in the numerator, recognising that maintenance capital spending competes with lenders for cash, or pairs coverage with [[free-cash-flow|free cash flow]] to capture true cash service capacity.

## Worked Example (illustrative round numbers)

A manufacturer reports the following for a fiscal year:

| Line item | $ |
|-----------|---|
| Operating income (EBIT) | 240M |
| Interest expense | 40M |
| Depreciation & amortization | 60M |

| Ratio | Calculation | Result |
|-------|-------------|--------|
| Interest coverage (EBIT) | 240 / 40 | **6.0×** |
| EBITDA coverage | (240 + 60) / 40 | **7.5×** |

A coverage of 6.0× means operating profit could fall by roughly five-sixths before the company would struggle to pay interest — a comfortable cushion for a stable industrial. If a downturn cut EBIT in half to $120M, coverage would still be 3.0×, adequate but worth watching.

## Interpretation

The ratio answers: *how much room does the company have before interest payments threaten it?*

- **> 5×** — strong; ample cushion, typical of healthy investment-grade firms
- **3× – 5×** — comfortable for most established businesses
- **1.5× – 3×** — adequate but leaves little margin for an earnings shock
- **1× – 1.5×** — stretched; a modest downturn could leave the firm unable to cover interest
- **< 1×** — earnings do not cover interest at all; the firm is funding its debt service from cash reserves, asset sales, or new borrowing — a classic distress signal

Lenders and bond covenants frequently set a **minimum coverage threshold** (e.g., "EBITDA/interest must stay above 2.5×"); breaching it can trigger default even while the company is still operating. As with most ratios, the **trend** matters more than any single reading — coverage sliding quarter after quarter is a leading indicator of credit deterioration.

## Typical Ranges by Sector

- **Software / asset-light tech**: very high or not meaningful — many carry little or no debt
- **Consumer staples / utilities**: 3× – 6× — stable cash flows support steady leverage
- **Capital-intensive industrials**: 3× – 8× through the cycle, but volatile
- **Highly leveraged / LBO-owned firms**: deliberately run at 1.5× – 3×, by design close to covenant limits
- **Distressed or deep-cyclical names in a downturn**: can fall below 1×

These are rough order-of-magnitude bands, not a substitute for live peer comparison.

## Limitations

1. **EBIT is not cash.** Operating income includes non-cash items and excludes capex and working-capital swings. A firm can show healthy coverage while bleeding cash — pair it with [[free-cash-flow]].
2. **Interest expense can be lumpy.** Variable-rate debt, refinancing, and capitalised interest distort the denominator; rising rates can crush coverage even with flat earnings.
3. **Ignores principal repayment.** The ratio only tests interest, not the maturity wall of principal coming due — a firm can cover interest yet face a refinancing crisis.
4. **Cyclicality.** A single strong year can flatter a business whose earnings collapse in a recession; assess coverage at trough earnings, not the peak.
5. **EBITDA versions flatter capital-intensive firms.** Using EBITDA ignores the real capex needed to keep the business running (see the [[ebitda]] critique).

Always read interest coverage alongside [[debt-to-equity]] (how much leverage), the [[current-ratio]] (short-term liquidity), and the debt maturity schedule.

## Trading Relevance

Interest coverage is a frontline credit-quality screen. In credit and distressed trading, deteriorating coverage anticipates rating downgrades, covenant breaches, and forced refinancing — events that re-price both bonds and equity. For equity traders, a coverage ratio falling toward 1× while debt rolls over into higher rates is a classic short-candidate filter, because the firm may be forced to raise equity (dilution), cut the dividend, or sell assets. Conversely, improving coverage during a deleveraging cycle is a tailwind that often precedes credit-spread tightening and equity re-rating. Because it is built from income-statement figures, it complements [[balance-sheet]] leverage measures like [[debt-to-equity]] and is a key input to distress models.

## Related

- [[debt-to-equity]] — the leverage level that the coverage ratio stress-tests
- [[ebitda]] — alternative numerator for cash-based coverage
- [[operating-income]] — EBIT, the standard numerator
- [[free-cash-flow]] — the truest test of debt-service capacity
- [[current-ratio]] — short-term liquidity complement
- [[net-income]] — bottom line after interest and taxes
- [[balance-sheet]] — source of debt and maturity data
- [[financial-statement-analysis]]

## Sources

- CFA Institute, *Financial Statement Analysis* curriculum — solvency and coverage ratio definitions
- Aswath Damodaran, *Investment Valuation* — interest coverage in credit risk and synthetic ratings
- General market knowledge; no additional specific wiki source ingested yet.
