---
title: "Peter Steidlmayer"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [market-microstructure, technical-analysis, person, futures, history]
entity_type: person
aliases: ["J. Peter Steidlmayer", "Steidlmayer"]
related: ["[[market-profile]]", "[[order-flow]]", "[[volume-profile]]", "[[cme-group]]", "[[footprint-chart]]", "[[auction-market-theory]]", "[[value-area]]", "[[sierra-chart]]"]
---

J. Peter Steidlmayer is the creator of [[market-profile|Market Profile]], a method of organizing price and time data that he developed in the early 1980s at the [[cme-group|Chicago Board of Trade]] (CBOT). His work laid the conceptual foundation for [[auction-market-theory|auction market theory]] and influenced the development of modern [[volume-profile]] and [[footprint-chart|footprint chart]] analysis.

## Career

Steidlmayer, raised on a California farm, joined the CBOT as an independent trader in **1963** and traded its commodity pits for decades. He served as a **director of the CBOT from 1981 to 1983**, and in that role initiated two institutional projects that outlived his directorship:

- **Market Profile** — the TPO-based graphic, developed with the CBOT and released to members and the public in the mid-1980s (the CBOT marketed it as the Market Profile / CBOT Market Profile product from 1985 onward)
- **Liquidity Data Bank (LDB)** — the CBOT's cleared-volume database, which broke down daily volume by price and by participant category (locals, commercials, members filling customer orders, CTI codes), an early institutional order-flow dataset

After the 1980s he focused on teaching and on building charting/analytics software around profile concepts, working with co-author Steven B. Hawkins.

## Contributions

### Market Profile (TPO Charts)

Steidlmayer introduced Market Profile as a way to visualize how the market distributes price over time. Rather than conventional bar or candlestick charts, Market Profile uses **Time Price Opportunity (TPO)** letters — each half-hour period is assigned a letter, and the letters are stacked horizontally at each price level they traded during that period. The result is a distribution curve showing where the market spent the most time.

Key Market Profile concepts Steidlmayer developed:

- **Value Area** — the price range containing approximately 70% of the day's trading activity (one standard deviation of the TPO distribution). Represents where the market perceived "fair value" for that session
- **Point of Control (POC)** — the single price level with the highest TPO count; the price at which the most time was spent trading
- **Initial Balance** — the price range established in the first hour of trading. A narrow initial balance suggests potential for range extension; a wide initial balance suggests the day's range may already be set
- **Single Prints** — TPO letters that appear only once at a price level, indicating the market moved through that price quickly. Single prints often act as support/resistance on subsequent visits
- **Profile Shape** — normal (bell curve), trending (elongated), or double distribution (bimodal) days reveal different market conditions

### Auction Market Theory

Steidlmayer's deeper insight was that markets function as **two-way auctions** whose purpose is to facilitate trade. Price moves to find the level where buyers and sellers can transact most efficiently. When price moves away from value, it attracts responsive participants who push it back. When new information shifts perceived value, price trends to find new balance.

This framework distinguishes between:

- **Initiative activity** — trading that moves price away from a known value area, driven by new information or conviction
- **Responsive activity** — trading that returns price to value, driven by participants who believe the move was excessive

## Influence on Modern Trading

Steidlmayer's work directly influenced:

- **[[volume-profile]]** analysis — which replaces time-based TPOs with actual volume, giving a more accurate picture of where real capital was transacted
- **[[footprint-chart|Footprint charts]]** — which extend the auction concept by showing buy/sell imbalances at each price level
- **[[order-flow]] analysis** — the broader discipline of reading market transactions builds on Steidlmayer's insight that price exists to facilitate trade
- **Platforms**: [[sierra-chart]], [[atas-platform|ATAS]], and [[ninjatrader|NinjaTrader]] all incorporate Market Profile and volume profile tools descended from Steidlmayer's original concepts

## Trading Relevance

Market Profile reframed charts around the question "where is the market doing business?" rather than "where is price going?" — a shift that underlies most modern intraday futures methodology. Day-type classification, value-area rotation plays (80% rule), initial-balance breakout strategies, and POC-magnet behavior are all directly tradeable constructs descended from Steidlmayer's framework, and remain standard tools among ES, NQ, and crude oil futures day traders.

## Key Publications

- *Markets and Market Logic* (1986, with Kevin Koy) — the original Market Profile text
- *141 West Jackson* (1996) — part memoir, part market-logic treatise, named for the CBOT's address
- *Steidlmayer on Markets: Trading with Market Profile* (2nd ed. 2003, with Steven B. Hawkins, Wiley) — updated treatment of auction market theory
- CBOT Market Profile educational materials (1980s-1990s)

## Related

- [[market-profile]] — the analytical method Steidlmayer created
- [[volume-profile]] — modern evolution using volume instead of time
- [[order-flow]] — broader discipline influenced by auction market theory
- [[footprint-chart]] — advanced visualization building on Steidlmayer's concepts
- [[cme-group]] — the exchange where Steidlmayer traded and developed Market Profile
- [[sierra-chart]] — professional platform with advanced Market Profile tools
- [[absorption]] — order flow concept rooted in auction market theory

## Sources

- J. Peter Steidlmayer & Steven B. Hawkins, *Steidlmayer on Markets: Trading with Market Profile*, 2nd ed. (Wiley, 2003), ISBN 0471215562
- J. Peter Steidlmayer & Kevin Koy, *Markets and Market Logic* (Porcupine Press, 1986)
- Official biography — ProfileTrading.com (confirms 1963 CBOT entry, 1981-1983 directorship, Market Profile and Liquidity Data Bank initiation): https://www.profiletrading.com/about/
- Market profile — Wikipedia: https://en.wikipedia.org/wiki/Market_profile
- Verified via Perplexity (sonar) + web search, 2026-06-10. Note: no death notice or obituary could be found as of June 2026; no claim is made here about current activities.
