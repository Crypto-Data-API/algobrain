---
title: "Exchange-Traded Fund (ETF)"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [stocks, commodities]
aliases: ["ETF", "ETFs", "Etfs", "Exchange-Traded Fund", "Exchange Traded Fund", "Exchange-Traded Funds"]
related: ["[[index-investing]]", "[[s-and-p-500]]", "[[asx-200]]", "[[mutual-funds]]", "[[expense-ratio]]", "[[tracking-error]]", "[[etf-arbitrage]]", "[[leveraged-etf-rebalancing]]"]
domain: [portfolio-theory]
difficulty: beginner
prerequisites: ["[[stocks]]", "[[index-investing]]"]
---

An exchange-traded fund (ETF) is a pooled investment vehicle that trades on a stock exchange like an ordinary share. ETFs typically track an index, sector, commodity, or other asset class, allowing investors to gain diversified exposure without buying each underlying component individually. The first ETF, the SPDR S&P 500 ETF Trust (SPY), launched in 1993 and remains the most traded security in the world by dollar volume, with daily turnover frequently exceeding $30 billion. As of 2025, global ETF assets under management surpassed $14 trillion across more than 10,000 products.

## Structure: Creation and Redemption

ETFs maintain their price close to net asset value (NAV) through a unique creation/redemption mechanism involving authorised participants (APs) -- typically large broker-dealers. When an ETF trades at a premium to its NAV, APs can deliver a basket of the underlying securities to the ETF issuer in exchange for new ETF shares (creation), then sell those shares on the open market at the higher price, pocketing the difference. When the ETF trades at a discount, APs buy cheap ETF shares on the exchange and redeem them for the underlying basket, again profiting from the arbitrage.

This process keeps the ETF's market price tightly aligned with NAV during normal market conditions. Deviations are typically less than 0.05% for large, liquid ETFs, though they can widen during periods of market stress or for ETFs tracking illiquid underlying assets. The premium/discount arbitrage is itself a tradable strategy -- see [[etf-arbitrage]] -- and the breakdown of this mechanism is what produced the [[2020-03-bond-etf-dislocation|March 2020 bond-ETF dislocation]].

## Types of ETFs

- **Index ETFs**: Track a market index such as the [[s-and-p-500]], [[asx-200]], or MSCI World. These are the most common type. Examples: SPY, IVV, VTI, VAS.
- **Sector and industry ETFs**: Focus on a specific sector (e.g., XLF for financials, XLK for technology).
- **Bond ETFs**: Track fixed income indices (e.g., AGG for US aggregate bonds, TLT for long-term Treasuries).
- **Commodity ETFs**: Provide exposure to physical commodities like gold (GLD) or oil (USO), either through physical holdings or futures contracts.
- **Leveraged ETFs**: Use derivatives to deliver 2x or 3x the daily return of an index (e.g., TQQQ for 3x Nasdaq-100). These suffer from volatility decay over longer holding periods and are designed for short-term trading, not buy-and-hold.
- **Inverse ETFs**: Deliver the opposite daily return of an index (e.g., SH for -1x S&P 500), used for hedging or bearish bets.
- **Thematic ETFs**: Target investment themes such as artificial intelligence (BOTZ), clean energy (ICLN), or blockchain (BLOK).
- **Active ETFs**: Managed by a portfolio manager who makes discretionary investment decisions rather than tracking an index. Cathie Wood's ARK funds popularised this category.

## Advantages Over Mutual Funds

| Feature | ETF | Mutual Fund |
|---|---|---|
| Trading | Intraday at market price | Once daily at NAV |
| Expense ratio | Typically 0.03%-0.50% | Typically 0.50%-1.50% |
| Tax efficiency | Higher (in-kind redemption minimises capital gains distributions) | Lower (fund must sell holdings to meet redemptions) |
| Minimum investment | One share (often $50-$500) | Often $1,000-$3,000 |
| Transparency | Holdings disclosed daily (most ETFs) | Holdings disclosed quarterly |

## Key Metrics

- **Expense ratio**: The annual fee expressed as a percentage of assets. Vanguard's VOO charges 0.03%, meaning $3 per year on a $10,000 investment. Expense ratios are the single most reliable predictor of future fund performance (lower is better).
- **[[tracking-error]]**: The standard deviation of the difference between the ETF's return and its benchmark's return. A well-run index ETF should have tracking error below 0.10% annually.
- **Spread**: The bid-ask spread when trading. Highly liquid ETFs like SPY have spreads of $0.01 (essentially zero cost), while niche ETFs may have spreads of 0.10-0.50%.
- **Premium/discount**: The difference between the market price and NAV. Persistent premiums or discounts indicate the creation/redemption mechanism is not functioning efficiently.

## Limitations

- **Leveraged ETF decay**: Due to daily rebalancing, leveraged ETFs lose value in choppy, sideways markets even if the underlying index ends flat. A 2x leveraged ETF tracking an index that goes up 10% then down 10% would lose approximately 2% rather than breaking even.
- **Commodity ETF contango**: Futures-based commodity ETFs (like USO for oil) can suffer from negative roll yield when the futures curve is in contango, causing persistent underperformance versus spot prices.
- **Illiquid underlying assets**: ETFs tracking high-yield bonds, emerging market debt, or small-cap stocks may see significant NAV deviations during market stress when the underlying securities are hard to price or trade.

## Related

- [[index-investing]] -- the investment philosophy most associated with ETFs
- [[s-and-p-500]] -- the most widely tracked ETF benchmark
- [[asx-200]] -- Australian market ETF benchmark
- [[mutual-funds]] -- the predecessor investment vehicle that ETFs largely displaced for index investing
- [[expense-ratio]] -- the primary cost metric for ETFs
- [[tracking-error]] -- the primary quality metric for index ETFs
- [[etf-arbitrage]] -- trading the premium/discount to NAV
- [[leveraged-etf-rebalancing]] -- exploiting the daily-rebalance decay
- [[commodity-futures-vs-etfs]] -- contango drag on futures-based ETFs

## Sources

- SPDR S&P 500 ETF Trust (SPY) prospectus and State Street fact sheets, ssga.com
- BlackRock / iShares, "What is an ETF?", ishares.com
- Vanguard, "ETF vs. mutual fund: How to choose," vanguard.com
- Investment Company Institute (ICI), *Investment Company Fact Book* (2025 edition) -- global ETF AUM and flow data
- U.S. SEC Investor Bulletin, "Exchange-Traded Funds (ETFs)," sec.gov
