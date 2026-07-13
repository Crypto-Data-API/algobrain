---
title: "Solvency"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [fundamental-analysis, risk-management, valuation, leverage]
aliases: ["Solvency Analysis", "Long-Term Solvency", "Financial Solvency"]
domain: [risk-management]
prerequisites: ["[[liquidity]]"]
difficulty: beginner
related: ["[[liquidity]]", "[[risk-management]]", "[[bonds]]", "[[basel-iii]]"]
---

Solvency is a company's ability to meet its long-term financial obligations, distinct from [[liquidity]] which addresses short-term commitments. A solvent company generates sufficient cash flow to service its debt and continue operations indefinitely. Solvency analysis is a fundamental component of credit analysis and equity [[risk-management]], as insolvency leads to bankruptcy, restructuring, or liquidation -- the permanent loss of capital for equity investors. Solvency indicators matter most when evaluating entities that have recently raised capital or operate in capital-intensive industries — a lesson that transfers directly to assessing crypto counterparties (exchanges, lenders, stablecoin issuers).

## Key Solvency Ratios

The most commonly used solvency ratios include:

- **Debt-to-Equity Ratio** -- Total debt divided by total shareholders' equity. Measures the proportion of financing from debt versus equity. A ratio above 2.0 is generally considered highly leveraged, though acceptable levels vary significantly by industry (utilities and REITs routinely operate at higher leverage than technology companies)
- **Interest Coverage Ratio** -- EBIT (or EBITDA) divided by interest expense. Measures how many times over the company can cover its interest payments from operating earnings. Below 1.5x is a warning sign; below 1.0x means the company cannot cover interest from operations
- **Debt-to-Assets Ratio** -- Total debt divided by total assets. Shows what percentage of the company's assets are financed by debt. Higher ratios indicate greater financial risk and less capacity to absorb losses
- **Free Cash Flow to Debt** -- FCF divided by total debt. Indicates how quickly the company could theoretically repay all its debt from free cash flow. Higher is safer

## Solvency vs Liquidity

Solvency and [[liquidity]] are related but distinct concepts. Liquidity measures the ability to meet short-term obligations (within 12 months) and is assessed through metrics like the current-ratio (current assets / current liabilities) and quick ratio. Solvency measures the ability to meet long-term obligations and is assessed through the ratios above. A company can be liquid but insolvent (generating enough cash to pay this quarter's bills but unable to service its long-term debt load) or illiquid but solvent (temporarily short on cash but with strong long-term fundamentals and asset backing). In practice, liquidity crises often precipitate solvency crises -- short-term funding problems cascade into an inability to refinance long-term debt, leading to default.

## Banking Sector: Capital Adequacy

Solvency in the banking sector is governed by the Basel III framework, which sets minimum capital requirements. The key metric is the **Common Equity Tier 1 (CET1) ratio** -- the bank's core equity capital as a percentage of risk-weighted assets. Basel III requires a minimum CET1 ratio of 4.5%, plus a capital conservation buffer of 2.5%, for an effective minimum of 7.0%. Systemically important banks (G-SIBs) face additional surcharges of 1.0-3.5%. Australian major banks (CBA, NAB, ANZ, Westpac) typically maintain CET1 ratios of 11-13%, well above minimums. Bank solvency analysis is fundamentally different from corporate solvency analysis because banks are inherently leveraged institutions (assets/equity ratios of 10-20x are normal) and rely on depositor confidence and interbank funding markets.

## The Altman Z-Score

The best-known composite solvency/bankruptcy-prediction model is the **Altman Z-Score** (Edward Altman, 1968), which combines five ratios into a single distress score for manufacturing companies:

```
Z = 1.2·X1 + 1.4·X2 + 3.3·X3 + 0.6·X4 + 1.0·X5

X1 = working capital / total assets
X2 = retained earnings / total assets
X3 = EBIT / total assets
X4 = market value of equity / total liabilities
X5 = sales / total assets
```

Interpretation zones for the original model:

- **Z > 2.99** — "safe" zone, low bankruptcy probability
- **1.81 ≤ Z ≤ 2.99** — "grey" zone, monitor
- **Z < 1.81** — "distress" zone, elevated bankruptcy risk within ~2 years

Variants exist for private firms (Z') and non-manufacturers/emerging markets (Z''). The Z-score is a screening tool, not a verdict — it flags candidates for deeper analysis and is most useful for ranking a universe rather than pronouncing a single name doomed.

## Trading Relevance

Solvency analysis is fundamentally about avoiding the *permanent* loss of capital, which sits at the top of the [[risk-management]] hierarchy because no position-sizing or stop discipline recovers from an issuer going to zero.

- **Equity screening:** Filter out names in the Z-score distress zone or with interest coverage below ~1.5x before they ever enter a fundamental watchlist. Insolvency is a left-tail event that volatility-based risk metrics underweight.
- **Distressed/value plays:** The mirror trade — deliberately buying near-insolvent names where the market has over-discounted recovery value — depends on getting the solvency math (liquidation value, refinancing runway, covenant triggers) more right than the consensus. High reward, high ruin risk.
- **Credit and bond selection:** Solvency ratios drive credit spreads. A deteriorating interest-coverage trend is an early-warning signal that a [[bonds|bond]] is heading toward a downgrade and forced institutional selling.
- **Capital-raise dilution risk:** A company sliding toward insolvency typically does a dilutive capital-raise at the worst time, transferring value from existing equity holders. Spotting the looming raise (covenant breach, exhausted FCF, maturity wall) lets a trader exit or short ahead of it.
- **Short candidates:** Persistent free-cash-flow-negative companies with a debt maturity wall and no refinancing path are classic short setups — the catalyst is the moment the market prices the solvency cliff.

## Related

- [[risk-management]] -- broader risk management framework
- [[liquidity]] -- short-term counterpart to long-term solvency
- [[bonds]] -- credit instruments priced off solvency
- [[basel-iii]] -- banking-sector solvency / capital-adequacy framework

## Sources

- Altman, E. (1968), "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy" — *Journal of Finance* (the original Z-score model)
- Basel Committee on Banking Supervision, *Basel III: A global regulatory framework for more resilient banks and banking systems* — CET1 and capital-adequacy requirements
- Damodaran, A., *Investment Valuation* — solvency and distress in DCF / valuation
- CFA Institute curriculum, *Financial Statement Analysis* — solvency vs liquidity ratio definitions and interpretation
