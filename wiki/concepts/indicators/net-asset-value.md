---
title: "Net Asset Value"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [fundamental-analysis, valuation]
aliases: ["NAV"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[financial-statement-analysis]]"]
difficulty: beginner
related: ["[[intrinsic-value]]", "[[price-to-earnings-ratio]]", "[[etf]]", "[[mutual-funds]]", "[[value-investing]]"]
---

Net Asset Value (NAV) is the per-share value of a fund or company calculated as total assets minus total liabilities, divided by the number of shares outstanding. It is the standard valuation metric for mutual funds, [[etf|ETFs]], closed-end funds, and REITs.

## Formula

**NAV = (Total Assets - Total Liabilities) / Shares Outstanding**

For investment funds, "total assets" means the current market value of all securities held in the portfolio, plus cash and receivables. NAV is typically calculated once per day at market close for mutual funds, while ETF NAVs update throughout the trading day via the intraday indicative value (iNAV).

## NAV in Different Contexts

### Mutual Funds
- All mutual fund transactions (purchases and redemptions) occur at the end-of-day NAV
- There is no premium or discount -- investors always transact at NAV
- NAV changes daily based on the market value of the fund's holdings

### ETFs
- ETFs trade on exchanges at market prices that may differ slightly from NAV
- **Premium**: Market price > NAV (demand exceeds supply)
- **Discount**: Market price < NAV (supply exceeds demand)
- Authorized participants (APs) [[arbitrage]] premiums/discounts by creating/redeeming ETF shares, keeping market price close to NAV

### Closed-End Funds
- Trade on exchanges like stocks, but unlike ETFs, have no creation/redemption mechanism
- Frequently trade at persistent discounts (sometimes 10-20%) to NAV
- Discounts can represent opportunities: if the discount narrows, investors profit even if NAV stays flat
- Activist investors sometimes push closed-end funds to convert to open-end or liquidate to close the discount

### REITs (Real Estate Investment Trusts)
- NAV is estimated based on appraised property values, which may differ from book value
- REIT share prices can diverge significantly from estimated NAV during real estate cycles

## Graham's Net Current Asset Value (NCAV)

[[benjamin-graham|Benjamin Graham]] popularized a stricter version of NAV for deep [[value-investing|value investing]]:

**NCAV = Current Assets - Total Liabilities**

This ignores fixed assets entirely, asking: "If this company liquidated today, selling only current assets and paying all debts, what would shareholders receive?" Graham recommended buying stocks trading below 2/3 of NCAV -- a "net-net" strategy. These situations are rare in modern markets but historically produced exceptional returns. (Source: [[book-the-intelligent-investor]])

## Trading Applications

1. **Closed-end fund discount arbitrage**: Buy funds trading at wide discounts to NAV, especially when catalysts exist (activist campaigns, fund conversion, liquidation)
2. **ETF premium/discount monitoring**: Extreme premiums or discounts on ETFs signal market stress or illiquidity
3. **Net-net screening**: Screen for stocks trading below NCAV for deep value candidates (Source: [[book-security-analysis]])
4. **REIT valuation**: Compare REIT price to estimated NAV to identify over/undervaluation

## Limitations

- NAV is backward-looking -- it reflects current asset values, not future earning power
- For operating companies, NAV ignores intangible assets (brand, IP, human capital)
- Estimated NAV (for REITs, private equity) is subjective and may not reflect true liquidation value
- Graham's NCAV approach requires extreme patience and diversification; individual net-nets can be value traps

## Related

- [[intrinsic-value]] -- Broader concept of what a business is truly worth
- [[value-investing]] -- Investment philosophy that often uses NAV-based metrics
- [[financial-statement-analysis]] -- Required to calculate NAV from company filings
- [[etf]] -- Funds where NAV tracking is a key mechanism

## Sources

- (Source: [[book-the-intelligent-investor]]) -- Graham's framework for NAV and net-net investing
- (Source: [[book-security-analysis]]) -- Detailed treatment of NCAV as a margin of safety metric
