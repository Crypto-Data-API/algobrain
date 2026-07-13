---
title: "Debt-to-Equity Ratio"
type: concept
created: 2026-04-10
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, leverage, valuation, risk-management]
aliases: ["D/E", "D/E ratio", "debt to equity", "debt-to-equity", "leverage ratio", "Gearing Ratio"]
domain: [fundamental-analysis, risk-management]
difficulty: beginner
prerequisites: ["[[balance-sheet]]"]
related: ["[[current-ratio]]", "[[quick-ratio]]", "[[return-on-equity]]", "[[balance-sheet]]", "[[leverage]]", "[[ebitda]]", "[[interest-coverage-ratio]]", "[[net-debt]]", "[[financial-statement-analysis]]"]
---

The **debt-to-equity ratio (D/E)** is a core solvency metric that measures how much a company relies on borrowed money versus shareholder capital to finance its operations. It is one of the most widely cited gauges of financial leverage and balance-sheet risk.

## Formula

$$\text{D/E} = \frac{\text{Total Debt}}{\text{Total Shareholders' Equity}}$$

A critical distinction is *which* debt figure to use. The broadest definition uses **total liabilities**, but most analysts prefer **interest-bearing debt only** (short-term borrowings + long-term debt + capital leases), which strips out operational items like accounts payable and deferred revenue. The interest-bearing version is more comparable across firms and more meaningful for credit risk.

| Variant | Numerator | When to use |
|---------|-----------|-------------|
| Total-liabilities D/E | All liabilities (incl. payables, deferred revenue) | Quick conservative screen; broadest gross view |
| Interest-bearing D/E | Short-term + long-term debt + capital/finance leases | Standard for credit and leverage analysis |
| Net D/E | Interest-bearing debt − cash & equivalents | Best for cash-rich firms; reflects true net leverage |

## Worked Example (illustrative round numbers)

A company reports on its [[balance-sheet]]:

- Short-term debt: $50M
- Long-term debt: $250M
- Cash & equivalents: $100M
- Accounts payable + accrued (non-debt liabilities): $150M
- Total shareholders' equity: $300M

| Measure | Calculation | Result |
|---------|-------------|--------|
| Interest-bearing debt | 50 + 250 | $300M |
| Interest-bearing D/E | 300 / 300 | **1.0×** |
| Total liabilities | 300 + 150 | $450M |
| Total-liabilities D/E | 450 / 300 | **1.5×** |
| Net debt | 300 − 100 | $200M |
| Net D/E | 200 / 300 | **0.67×** |

The same firm looks materially riskier (1.5×) or safer (0.67×) depending purely on definition — which is why you must state the variant and benchmark against peers using the *same* one.

## Interpretation

D/E shows how each dollar of equity is matched by debt. A ratio of 1.0 means the firm is financed 50/50; 2.0 means twice as much debt as equity. [[leverage|Leverage]] is a double-edged sword: it amplifies [[return-on-equity]] when returns exceed the cost of debt, but it also amplifies losses and raises bankruptcy risk when cash flows weaken (the leverage term in the DuPont decomposition of [[return-on-equity|ROE]] is essentially 1 + D/E on a total-assets basis).

## Typical Ranges by Industry

| Sector | Typical D/E | Why |
|--------|-------------|-----|
| Software / tech | < 0.5 | Asset-light, equity-financed, little need for borrowing |
| Consumer staples | 0.5 – 1.0 | Stable demand supports moderate debt |
| Manufacturers | 0.5 – 1.0 | Capital intensive but cyclical, so debt kept moderate |
| Utilities | 1.0 – 2.0 | Regulated, very stable cash flows safely support high debt |
| REITs / private equity | > 2.0 (by design) | Property and buyout models are built on leverage |
| Banks | 8 – 12 | Deposits are recorded as liabilities; D/E is **not** the right lens — use capital ratios instead |

Cross-industry comparisons are misleading; always benchmark against peers using the same debt definition. A 1.0× D/E is conservative for a utility and aggressive for a cyclical commodity producer.

## Trading Relevance

D/E is a core input to solvency screens, credit analysis, and the [[leverage]] story behind [[return-on-equity]]. High and rising leverage makes a stock a *higher-beta* claim on the underlying business: equity holders are subordinated to debt, so when cash flows weaken, the equity absorbs losses first and can be wiped out while the enterprise survives. This is why over-leveraged names sell off hardest in risk-off regimes and credit-spread widening — the same dynamic that drives distress and short-candidate screens. Rising interest rates amplify the risk by raising refinancing costs that a static ratio cannot see, so D/E should always be paired with **interest coverage** (EBIT / interest) and **net debt / [[ebitda]]** to gauge whether earnings can actually service the debt. Fred McNaught noted Northern Star's D/E of 15.6 was "low as it should be for a commodity stock" — a reminder that the acceptable level is entirely sector- and cyclicality-dependent (Source: [[fred-sam-session-2024-04-25]]).

## Limitations

1. **Book equity is historical** — write-downs, goodwill, and [[stock-buybacks]] can distort the denominator. Aggressive buybacks reduce equity and mechanically inflate D/E even when the business is healthier.
2. **Off-balance-sheet obligations** (operating leases pre-ASC 842, pension deficits, contingent liabilities) are missed.
3. **Ignores cash** — a firm with $10B debt and $9B cash has very different risk than one with $10B debt and no cash. Use **net debt** instead.
4. **Rising interest rates** make high D/E far more dangerous by increasing refinancing costs, which a static ratio fails to capture.

## How Investors and Traders Use It

- **Quality / safety screens** — value and dividend investors set a maximum D/E (e.g. "< 1.0 ex-financials") to avoid balance-sheet fragility, echoing [[benjamin-graham|Graham's]] insistence on a strong financial position.
- **Credit analysis** — paired with [[interest-coverage-ratio]] and net debt / [[ebitda]], D/E feeds the assessment of default risk and credit ratings; rising leverage often precedes downgrades and credit-spread widening.
- **Short-candidate filters** — a high and *rising* D/E combined with a falling [[current-ratio]] and weak [[free-cash-flow]] is a classic distress screen.
- **Capital-allocation read** — a deliberate rise in D/E from buybacks or a debt-funded acquisition is a signal about management's risk appetite, not just an accounting number.

## Related Metrics

| Metric | Formula | Adds |
|--------|---------|------|
| Net debt / [[ebitda]] | (Debt − cash) / EBITDA | Cash-flow capacity to repay; safe < 3×, stressed > 5× |
| [[interest-coverage-ratio]] | EBIT / interest expense | Whether earnings can actually service the debt |
| Equity multiplier | Total assets / equity | The ROE-amplification term in DuPont |
| [[current-ratio]] / [[quick-ratio]] | Current assets / current liabilities | Short-term liquidity, the near-term complement |

## Related

- [[leverage]] — the broader concept D/E quantifies
- [[return-on-equity]] — leverage amplifies ROE (DuPont decomposition)
- [[balance-sheet]] — source of debt and equity figures
- [[current-ratio]] · [[quick-ratio]] — short-term liquidity complements
- [[net-debt]] — debt net of cash, the basis of net D/E
- [[interest-coverage-ratio]] — can earnings service the debt?
- [[ebitda]] — denominator in net-debt / EBITDA leverage
- [[financial-statement-analysis]]

## Sources

- CFA Institute, *Financial Statement Analysis* curriculum — solvency ratios
- Modigliani & Miller (1958, 1963) — capital structure and the value of leverage
- Aswath Damodaran, *Applied Corporate Finance* — optimal capital structure and leverage risk
- [[fred-sam-session-2024-04-25]] — D/E in a commodity-stock context
- General market knowledge; no additional specific wiki source ingested yet.
