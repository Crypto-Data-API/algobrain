---
title: "2010 Flash Crash"
type: news
created: 2026-04-10
updated: 2026-06-12
status: good
tags: [history, crashes, market-microstructure, stocks]
event_date: 2010-05-06
markets_affected: [stocks, futures]
impact: high
aliases: ["Flash Crash", "May 6 2010 Flash Crash"]
related: ["[[flash-crashes]]", "[[1987-crash]]", "[[high-frequency-trading]]", "[[market-microstructure]]", "[[liquidity]]", "[[circuit-breakers]]", "[[spoofing]]", "[[market-manipulation]]", "[[algorithmic-trading]]", "[[book-flash-boys]]", "[[book-dark-pools]]"]
---

# 2010 Flash Crash

On the afternoon of **May 6, 2010**, the US equity market plunged and recovered roughly 1,000 points on the Dow Jones Industrial Average within a span of about 36 minutes. At the trough, the DJIA was down nearly 9% intraday — one of the largest intraday point declines in history at the time — before snapping back almost as quickly as it fell. The episode laid bare the fragility of modern, fragmented, electronically-traded markets and reshaped how regulators think about [[high-frequency-trading]] and [[market-microstructure]].

## What Happened

Markets had already opened lower on European debt-crisis fears (Greece). At around **2:32 PM ET**, sell pressure intensified abruptly in the E-mini S&P 500 futures contract, then rippled into the cash equities market. Liquidity in the order book evaporated within minutes. Some individual stocks printed at absurd prices — Accenture traded as low as **$0.01**, while Sotheby's traded as high as **$99,999.99**. By approximately **3:08 PM**, prices had largely recovered.

The episode was unique because:

- The selloff and recovery happened in **minutes, not days**
- Retail traders who placed market or stop-loss orders during the window were filled at catastrophic prices
- Many "broken trades" were later cancelled by exchanges (trades >60% away from the 2:40 PM reference price)

## Causes

The joint **CFTC–SEC report** (September 2010) identified a large institutional sell program — a $4.1 billion sale of E-mini S&P 500 futures executed by an algorithm tied to volume but not to price or time — as the immediate trigger. The algorithm dumped 75,000 contracts into a market with thin bid-side liquidity, and high-frequency market makers withdrew or flipped to sellers as they hit position limits, accelerating the cascade.

A second narrative emerged years later: in 2015, **Navinder Sarao**, a London-based trader operating from his parents' home, was arrested and accused of contributing to the crash through **spoofing** — placing and rapidly cancelling large sell orders in the E-mini to manipulate prices. He pled guilty in 2016. Whether Sarao's spoofing was a primary cause or an aggravating factor remains debated, but the case demonstrated how a single trader using off-the-shelf software could materially affect a market the size of the S&P 500 futures.

The deeper structural cause was the interaction of three features of modern market structure:

1. **Market fragmentation** — equities trade across dozens of venues; when liquidity vanishes in one, [[smart-order-routing]] cannot reliably backstop prices.
2. **HFT market makers without obligations** — unlike old NYSE specialists, modern HFT liquidity providers have no obligation to quote and routinely withdraw under stress.
3. **Algorithmic feedback loops** — execution algorithms, momentum-ignition strategies, and stop-loss cascades amplified the initial shock.

These themes are central to Michael Lewis's *Flash Boys* (Source: [[book-flash-boys]]) and Scott Patterson's *Dark Pools* (Source: [[book-dark-pools]]), both of which use the flash crash as the canonical illustration of how electronic market structure can fail.

## Aftermath and Reforms

- **Limit up–limit down (LULD)**: The SEC introduced single-stock circuit breakers, then in 2012 replaced them with the LULD mechanism that caps how far a stock can move outside a percentage band of its recent average price.
- **Market-wide [[circuit-breakers]] revised**: Existing index-level circuit breakers were tightened and recalibrated to trigger more responsively.
- **Consolidated audit trail (CAT)**: The SEC mandated a comprehensive cross-market trade-reporting system to allow regulators to reconstruct events like the flash crash. Implementation took years.
- **Spoofing prosecutions**: Dodd-Frank's anti-spoofing provisions gained teeth — Sarao's case was the first major test.

## Lessons for Traders

1. **Liquidity is not a guarantee** — quoted depth in electronic books can vanish in seconds. Echoes the [[1987-crash]] lesson at electronic speed.
2. **Market orders are dangerous in thin conditions** — stop-loss orders that converted to market orders at 2:45 PM produced catastrophic fills.
3. **HFT is structurally a fair-weather liquidity provider** — modern market makers reduce risk by withdrawing, not by absorbing inventory.
4. **Single-point-of-failure algorithms can move size markets** — both the institutional sell algorithm and (allegedly) Sarao's spoofing demonstrated this.

## Related

- [[flash-crashes]] — the broader flash crash phenomenon and all events
- [[flash-crash-2015-etf]] — the next major US equity flash crash (August 2015)
- [[volmageddon-2018]] — the volatility flash crash that killed XIV
- [[1987-crash]] — the predecessor: Black Monday and portfolio insurance
- [[high-frequency-trading]] — HFT's role as fragile liquidity provider
- [[algorithmic-trading]] — the feedback loops that amplified the cascade
- [[market-microstructure]] — the structural conditions that enabled it
- [[liquidity]] — the resource that vanished in seconds
- [[circuit-breakers]] — reformed after the crash (LULD mechanism)
- [[spoofing]] — Navinder Sarao's manipulation technique
- [[market-manipulation]] — the broader manipulation taxonomy
- [[smart-order-routing]]
- [[dodd-frank-act]] — anti-spoofing provisions born from this crash

## Sources

- (Source: [[book-flash-boys]]) — Michael Lewis's account of HFT and the structural conditions that produced the flash crash
- (Source: [[book-dark-pools]]) — Scott Patterson's history of electronic equities markets, dark pools, and the rise of HFT
- CFTC & SEC, *Findings Regarding the Market Events of May 6, 2010* (joint report, 30 September 2010) — the official reconstruction identifying the $4.1B E-mini sell algorithm as the immediate trigger.
- US Department of Justice / CFTC filings in *United States v. Navinder Singh Sarao* (2015-2016) — the spoofing prosecution; Sarao pleaded guilty in November 2016.
