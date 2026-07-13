---
title: "Net Asset Value (NAV)"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [valuation, indicators, liquidity, education]
aliases: ["NAV", "Net Asset Value", "net asset value", "iNAV", "intraday NAV", "indicative NAV"]
domain: [valuation, market-microstructure]
prerequisites: ["[[mutual-funds]]", "[[etf]]"]
difficulty: beginner
related: ["[[etf-arbitrage]]", "[[flash-crash-2015-etf]]", "[[mutual-funds]]", "[[etfs]]", "[[etf]]", "[[closed-end-fund]]", "[[liquidity]]", "[[index-fund]]"]
---

Net Asset Value (NAV) is the per-share value of a fund's total assets minus its liabilities. For mutual funds, NAV is calculated once daily after market close. For ETFs, an indicative NAV (iNAV) is published every 15 seconds during trading hours, and the market price can deviate from NAV — creating [[etf-arbitrage]] opportunities when premiums or discounts emerge.

## Calculation

```
NAV = (Total Assets - Total Liabilities) / Shares Outstanding
```

For an equity ETF:
- **Total assets** = market value of all held securities + cash
- **Total liabilities** = management fees accrued, expenses payable
- **Shares outstanding** = total ETF shares in circulation

## NAV and Market Crashes

NAV becomes critical during market stress. During the [[flash-crash-2015-etf|August 24, 2015 ETF Flash Crash]]:

- Hundreds of ETFs traded at **20-35% discounts to NAV** for extended periods
- The iNAV calculation failed because underlying stock prices were stale or halted
- Market makers widened spreads or stopped quoting because they couldn't price the underlying basket
- Investors who sold ETFs during the crash received prices far below what the underlying stocks were worth

This demonstrated that ETF prices and NAV can diverge dramatically when the arbitrage mechanism breaks down — usually in exactly the conditions when investors most need liquidity.

## Premium / Discount

| Condition | Price vs. NAV | Cause |
|-----------|---------------|-------|
| **Premium** | Price > NAV | Demand for ETF exceeds creation capacity; common in illiquid or international ETFs |
| **At NAV** | Price ≈ NAV | Normal conditions; arbitrageurs keep price aligned |
| **Discount** | Price < NAV | Selling pressure exceeds redemption capacity; stress conditions |

Authorized participants (APs) arbitrage premiums/discounts by creating or redeeming ETF shares in exchange for the underlying basket. This mechanism keeps ETF prices close to NAV in normal markets but can break during extreme stress.

## NAV across fund structures

| Structure | NAV pricing | Can trade vs NAV? |
|---|---|---|
| [[mutual-funds|Mutual fund]] (open-end) | Struck once daily after close; all orders fill at that NAV | No — NAV is the only price |
| [[etf]] | Official NAV daily; iNAV every ~15s intraday | Yes — market price floats; APs arbitrage the gap |
| [[closed-end-fund|Closed-end fund]] | NAV computed daily, but fixed share count | Persistent premium/discount is normal — no creation/redemption arbitrage |

The closed-end-fund discount is itself a documented anomaly: CEFs routinely trade at persistent discounts to NAV (often 5–15%), and the discount widening/narrowing is a tradable mean-reversion signal and a classic test case in [[behavioral-finance]].

## Trading relevance

- **iNAV as a fair-value anchor.** For ETFs, the published indicative NAV gives an intraday estimate of basket fair value. A market price meaningfully above iNAV (premium) or below it (discount) signals either a real supply/demand imbalance or a breakdown in the creation/redemption arbitrage.
- **Stale-NAV risk.** For ETFs holding assets that trade in a closed or different time zone (international equities, some bonds), the iNAV can be stale, so apparent premiums/discounts may be artifacts rather than opportunities. This is acute for fixed-income and emerging-market ETFs.
- **Discount as a stress gauge.** Sustained, broad ETF discounts to NAV are a real-time liquidity-stress indicator — the underlying is harder to sell than the fund, so the fund clears at a discount (see [[flash-crash-2015-etf]] and the [[2020-03-bond-etf-dislocation|March 2020 bond-ETF dislocation]]).
- **Arbitrage edge.** The premium/discount is the raw material for [[etf-arbitrage]]; APs capture it, and traders without AP status can sometimes express a view via the ETF-vs-basket spread.

## Related

- [[flash-crash-2015-etf]] — catastrophic NAV/price disconnection
- [[etf-arbitrage]] — the creation/redemption mechanism that maintains price-NAV alignment
- [[mutual-funds]] — open-end funds priced solely at daily NAV
- [[closed-end-fund]] — fixed-share funds that trade at persistent NAV premiums/discounts
- [[etf]] — intraday-traded funds with iNAV
- [[liquidity]] — NAV discounts widen when underlying liquidity dries up

## Sources

- U.S. Securities and Exchange Commission, *Investor Bulletin: Exchange-Traded Funds (ETFs)*
- Investment Company Institute, *Understanding Exchange-Traded Funds: How ETFs Work*
- BlackRock / iShares, *ETF Premium/Discount and iNAV* educational materials
- SEC and exchange post-mortems on the August 24, 2015 ETF flash crash
- Lee, Shleifer & Thaler, "Investor Sentiment and the Closed-End Fund Puzzle," *Journal of Finance* (1991)
