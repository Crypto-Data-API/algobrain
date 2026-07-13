---
title: "Market Hours"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [market-microstructure, stocks, liquidity, slippage]
aliases: ["Market Hours", "Trading Hours", "Pre-Market", "Pre-Market Trading", "After-Hours", "After-Hours Trading", "after-hours-trading", "Extended Hours", "Extended-Hours Trading", "Regular Trading Hours"]
domain: [market-microstructure]
prerequisites: ["[[liquidity]]", "[[bid-ask-spread]]"]
difficulty: beginner
related: ["[[liquidity]]", "[[bid-ask-spread]]", "[[gap-risk]]", "[[circuit-breakers]]", "[[nyse]]", "[[nasdaq]]", "[[earnings-season]]", "[[order-book]]", "[[slippage]]", "[[crypto-trading-sessions]]", "[[t-plus-one-settlement]]"]
---

**Market hours** are the times at which a securities exchange accepts and executes orders. For US stocks the day is split into a **regular session**, when liquidity and price discovery are at their fullest, and **extended-hours** sessions (pre-market and after-hours) when trading is thinner, wider, and riskier. Understanding which session you are trading in is one of the most practical things a dashboard user can know, because the *same order* behaves very differently depending on the clock.

## The US trading day

All times are US Eastern Time (ET); the [[nyse|NYSE]] and [[nasdaq|Nasdaq]] keep the same schedule.

| Session | Hours (ET) | Character |
|---------|-----------|-----------|
| **Pre-market** | ~4:00 AM – 9:30 AM | Thin liquidity, wide spreads; reacts to overnight news and BMO earnings |
| **Regular session** | 9:30 AM – 4:00 PM | Full liquidity, tightest [[bid-ask-spread\|spreads]], official price discovery |
| **After-hours** | 4:00 PM – 8:00 PM | Thin liquidity; reacts to AMC earnings and late news |

- The **opening bell** at 9:30 AM and the **closing bell** at 4:00 PM bracket the regular session.
- The **opening auction** and **closing auction** are single-price crossings that concentrate huge volume at the very start and end of the day. The **closing auction in particular is the highest-liquidity moment of the day** and sets the official closing price used for index calculation, fund NAVs, and benchmarks — which is why index funds and many institutions trade "on the close."
- The first and last 30–60 minutes of the regular session are typically the most volatile and highest-volume stretches; the midday lull ("lunchtime") is usually quietest.

## Extended hours: pre-market and after-hours

Pre-market and after-hours trading (collectively **extended-hours** or **after-hours trading**) let participants trade outside 9:30–4:00 through electronic communication networks (ECNs). They exist mainly so the market can react to news that breaks outside the regular session — most importantly **earnings reports**, which companies release **before market open (BMO)** or **after market close (AMC)** precisely so the initial reaction prints in extended hours rather than mid-session. See [[earnings-season]].

Extended-hours sessions carry materially higher risk than the regular session:

- **Thin [[liquidity]].** Far fewer participants means small orders move the price more.
- **Wide [[bid-ask-spread|spreads]].** The cost of immediacy can be many times the regular-session spread, so [[slippage]] is severe.
- **Sparse [[order-book|order books]] and jumpy prices.** A handful of trades can swing a quote, and an after-hours print often does **not** survive into the next regular open — the move can fully reverse.
- **Limit orders strongly advised.** Most brokers restrict extended-hours trading to **limit orders only**; a market order in a thin book can fill far from the last price.
- **Fragmented quotes.** Different ECNs may show different prices, and the consolidated tape you rely on intraday is less complete.

The practical rule: an after-hours price is an *indication*, not a settled price. A stock that "pops 8% after earnings" in after-hours may open meaningfully higher, lower, or flat once the full regular-session crowd weighs in.

## Holidays, half-days, and overnight gaps

- US equity markets close on roughly nine **market holidays** a year (New Year's Day, MLK Day, Presidents' Day, Good Friday, Memorial Day, Juneteenth, Independence Day, Labor Day, Thanksgiving, Christmas), and observe **half-days** (early 1:00 PM close) around some of them, such as the day after Thanksgiving and Christmas Eve.
- Because the regular session is only 6.5 hours, the market spends most of every 24 hours **closed**. News during that gap accumulates and is expressed all at once at the next open, producing **[[gap-risk|overnight gaps]]** — a key reason stop-loss orders cannot protect against earnings or weekend news. The price can open straight through a stop level.

## Other markets and the 24/7 contrast

Trading hours are venue-specific:

- **ASX (Australia):** regular trading roughly 10:00 AM – 4:00 PM Australian Eastern time, with opening and closing single-price auctions; relevant for the Australian stocks in [[alfred-investment-philosophy|ALFRED's]] coverage.
- **London (LSE), Tokyo (TSE), and other exchanges** each keep their own local sessions, so global investors face a near-continuous relay of regional opens and closes.
- **Futures** (e.g. equity-index futures) trade nearly around the clock on electronic platforms, which is why overnight futures are watched as a proxy for where stocks will open.
- **Crypto markets never close** — they trade 24 hours a day, 7 days a week, with no opening bell, no closing auction, and no holidays. This is a fundamental structural difference from equities: there is no "after-hours" because every hour is trading hours. See [[crypto-trading-sessions]] for how liquidity still varies by time of day even in a 24/7 market.

## When the market pauses: circuit breakers

Even within the regular session, trading can halt. Market-wide [[circuit-breakers|circuit breakers]] pause all US equity trading when the [[s-and-p-500|S&P 500]] falls a set percentage from the prior close (Level 1 at −7% and Level 2 at −13% trigger 15-minute halts; Level 3 at −20% closes the market for the day). Individual stocks also have **Limit Up-Limit Down** bands that briefly pause a single name when it moves too far too fast. See [[circuit-breakers]].

## Practical takeaways for dashboard users

- The **price you see** depends on the session. A pre-market or after-hours quote is thin and provisional; the **regular-session close** (set by the closing auction) is the authoritative price.
- **Use limit orders** in extended hours — never market orders into a thin book.
- **Earnings reactions** print in extended hours (BMO/AMC) and may not hold into the next open.
- **Overnight and weekend gaps** mean stops don't protect you while the market is closed; size positions accordingly.

## Related

- [[liquidity]] — collapses outside the regular session
- [[bid-ask-spread]] — widens sharply in pre-market and after-hours
- [[slippage]] — the cost of trading thin extended-hours books
- [[gap-risk]] — overnight and weekend gaps from the market being closed
- [[circuit-breakers]] — intraday halts that pause trading
- [[earnings-season]] — BMO/AMC reports drive most extended-hours activity
- [[order-book]] — sparse outside regular hours
- [[crypto-trading-sessions]] — the 24/7 contrast with equities
- [[t-plus-one-settlement]] — only business days count between trade and settlement
- [[nyse]] / [[nasdaq]] — the venues that set the US schedule

## Sources

- NYSE and Nasdaq published trading-hours and holiday schedules.
- SEC Investor.gov, "After-Hours Trading" investor bulletin — risks of extended-hours sessions.
- General market-microstructure knowledge for auction mechanics and the closing-auction's role; no additional specific wiki source ingested yet.
