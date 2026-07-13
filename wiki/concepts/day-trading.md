---
title: "Day Trading"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [day-trading, scalping, technical-analysis, market-microstructure]
aliases: ["Day Trading", "Daytrading", "Intraday Trading"]
related: ["[[day-trading-overview]]", "[[scalping]]", "[[momentum]]", "[[risk-management]]", "[[swing-trading]]", "[[pattern-day-trader]]", "[[leverage]]", "[[vwap]]"]
domain: [technical-analysis, market-microstructure]
prerequisites: ["[[technical-analysis]]", "[[risk-management]]"]
difficulty: beginner
---

Day trading is a trading style in which all positions are opened and closed within the same trading session, with no overnight exposure. By ending the day flat (holding no positions), day traders avoid overnight gap risk -- the possibility that prices move significantly between the market close and the next open due to after-hours news, earnings reports, or global events. Day trading is practised across all major asset classes including stocks, [[forex]], [[futures]], [[options]], and [[crypto-markets|crypto]], and ranges from discretionary manual trading to fully [[algorithmic]] execution.

## Regulatory Requirements

### Pattern Day Trader Rule (US)

In the United States, FINRA's Pattern Day Trader (PDT) rule requires that any margin account executing four or more day trades within five business days -- where day trades constitute more than 6% of total trading activity -- must maintain a minimum equity balance of $25,000. Accounts that fall below this threshold are restricted to three day trades per rolling five-day period. This rule applies only to margin accounts; cash accounts can day trade without the $25,000 minimum but are subject to settlement delays (T+1 for US equities), which limits capital recycling.

The PDT rule does not apply to futures or forex accounts, which is one reason day traders outside the US or with limited capital often gravitate toward those markets. Crypto markets are also exempt from PDT rules, and trade 24/7, making them accessible for day traders in any time zone.

### Other Jurisdictions

Australia, the UK, and most European countries have no equivalent of the PDT rule. Traders in these markets can day trade in margin accounts without a $25,000 minimum, though brokers may impose their own margin requirements.

## Common Day Trading Strategies

- **Momentum trading**: Identifying stocks or assets with strong intraday directional moves (driven by news, earnings, or volume surges) and riding the move. Momentum traders look for high relative volume (2-5x average) and clear catalysts.
- **[[scalping]]**: Taking very short-term trades (seconds to minutes) for small price increments, relying on high win rates and tight stops. Scalpers may execute 50-200 trades per day, requiring low commissions and fast execution.
- **Range trading**: Identifying support and resistance levels on intraday charts and buying at support, selling at resistance. This works best in low-[[volatility]] environments when price oscillates within a defined band.
- **Breakout trading**: Entering trades when price breaks above resistance or below support with confirming volume. False breakouts are common, so many traders wait for a retest of the broken level before entering.
- **VWAP reversion**: Using the volume-weighted average price as an intraday fair-value anchor. Price significantly above VWAP attracts mean-reversion shorts; price significantly below attracts longs. Institutional traders frequently benchmark execution against VWAP.

## Required Tools and Infrastructure

Day trading demands specific infrastructure that is less critical for longer-term traders:

- **Direct market access (DMA)**: Routing orders directly to exchanges rather than through a market maker, enabling faster execution and access to Level 2 order book data.
- **Low-latency execution**: Round-trip order latency should ideally be under 50ms for active day trading. Platform choice matters: popular platforms include Interactive Brokers (TWS), TD Ameritrade (thinkorswim), and DAS Trader.
- **Real-time data**: Level 1 quotes (bid/ask), Level 2 market depth, and time & sales data. Monthly data feed costs range from $0 (delayed data from most brokers) to $100-300+ for premium real-time feeds.
- **Risk management tools**: Position sizing calculators, automatic stop-loss orders, daily loss limits. Professional day traders commonly risk 0.5-2% of account equity per trade and set a daily maximum loss of 3-5%.

## Failure Rate and Realistic Expectations

Day trading has a well-documented high failure rate. Academic studies consistently show that the majority of day traders lose money:

- A 2019 study by Barber, Lee, Liu, and Odean examining Taiwanese day traders found that approximately 97% of day traders lost money over a given year, with only the top 1% earning consistent profits after costs.
- A Brazilian study (Chague, De-Losso, and Giovannetti, 2020) found that 97% of persistent day traders (those who traded for more than 300 days) lost money.

The primary reasons for failure include transaction costs (commissions + spread erosion), overtrading, poor [[risk-management]], and the psychological difficulty of maintaining discipline under real-time pressure. Survivors tend to be those who treat day trading as a business with strict rules, adequate capitalisation (typically $50,000-$100,000+ for equities), and a tested edge rather than intuition.

## Day Trading vs. Other Styles

| Feature | Day Trading | [[swing-trading|Swing Trading]] | [[scalping|Scalping]] |
|---|---|---|---|
| Holding period | Minutes to hours | Days to weeks | Seconds to minutes |
| Overnight risk | None | Yes | None |
| Trades per day | 2-20 | 0-3 | 50-200 |
| Capital requirement (US) | $25,000 (PDT rule) | No minimum | $25,000 (PDT rule) |
| Time commitment | Full trading session | 30-60 min/day | Full trading session |

## Related

- [[scalping]] -- the shortest-timeframe variant of day trading
- [[momentum]] -- a core strategy used by day traders
- [[risk-management]] -- essential discipline for surviving as a day trader
- [[swing-trading]] -- the next longer timeframe after day trading
- [[leverage]] -- frequently used by day traders to amplify returns on small intraday moves
- [[pattern-day-trader]] -- the regulatory classification in the US
- [[day-trading-overview]] -- the strategy hub covering intraday setups in depth

## Sources

- Barber, B., Lee, Y., Liu, Y., Odean, T. (2014). "The Cross-Section of Speculator Skill: Evidence from Day Trading." *Journal of Financial Markets*.
- Chague, F., De-Losso, R., Giovannetti, B. (2020). "Day Trading for a Living?" SSRN working paper.
- FINRA. "Pattern Day Trader." finra.org investor education materials.
- U.S. SEC. "Day Trading: Your Dollars at Risk." sec.gov investor bulletins.
