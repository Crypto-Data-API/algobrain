---
title: Circuit Breakers
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - regulation
  - risk-management
aliases:
  - trading-halts
  - market-circuit-breakers
  - circuit-breaker
  - LULD
domain: [market-microstructure]
prerequisites: ["[[volatility]]", "[[order-types]]"]
difficulty: intermediate
---

# Circuit Breakers

**Circuit breakers** are automatic trading halts triggered when the market drops too fast, designed to prevent panic selling and give participants time to assess information. See [[crashes]] for historical events that prompted their adoption.

## U.S. Market-Wide Circuit Breakers

Based on the S&P 500 index decline from the prior day's close:

- **Level 1 (7% decline)** -- trading halts for 15 minutes. If triggered after 3:25 PM ET, trading continues without a halt.
- **Level 2 (13% decline)** -- trading halts for 15 minutes. Same 3:25 PM rule applies.
- **Level 3 (20% decline)** -- trading halts for the remainder of the day, regardless of the time.

These thresholds were implemented after the **1987 Black Monday crash**, when the Dow Jones fell 22.6% in a single session with no mechanism to slow the decline. The specific percentage levels have been updated over the years, most recently after the 2010 Flash Crash.

## Individual Stock Halts (LULD)

The Limit Up-Limit Down (LULD) mechanism halts individual stocks when their price moves beyond a set percentage from a rolling reference price. The bands vary by stock price and market cap -- typically 5% for large-caps and 10-20% for smaller or more volatile names. LULD halts last 5 minutes and are designed to prevent erroneous trades and mini flash crashes in individual names.

## Crypto Markets

Cryptocurrency markets notably do **not** have circuit breakers. Exchanges like Binance and Coinbase operate 24/7 without market-wide halts, which means crypto assets can experience cascading liquidations and extreme drawdowns (20-50% intraday) without any pause mechanism. This is an important structural difference that traders transitioning from equities to [[crypto-markets]] must understand.

## Related

- [[flash-crashes]] — the phenomenon that drove circuit breaker reform
- [[flash-crash-2010]] — the 2010 crash that produced the LULD mechanism
- [[flash-crash-2015-etf]] — the 2015 ETF crash where circuit breakers made things worse
- [[crashes]] — broader crash history
- [[crypto-flash-crashes]] — crypto markets notably lack circuit breakers
- [[volatility]] — what circuit breakers are designed to contain
- [[market-manipulation]] — manipulation can trigger the cascades that circuit breakers pause
- [[risk-management]]

## Trading Relevance

For active traders, circuit breakers create a discrete, non-tradeable gap in the market: once a halt triggers, no fills occur until the auction reopens, so stop-loss orders provide no protection during the pause and may reopen at a far worse price. This makes halts a key risk for leveraged and stop-dependent strategies — the price you "see" before a halt is not a price you can transact at. Around individual-stock LULD halts, traders watch for the reopening auction imbalance, which often signals the next directional move. The absence of circuit breakers in [[crypto-markets|crypto]] is a primary reason cascading liquidations run further there than in regulated equity markets, and is a structural input to position sizing and leverage decisions for 24/7 assets.

## Sources

- NYSE, "Market-Wide Circuit Breakers" and Nasdaq Trading Halts FAQ — exchange rulebooks specifying Level 1/2/3 thresholds.
- SEC, "Investor Bulletin: Measures to Address Market Volatility" — overview of market-wide circuit breakers and the LULD plan.
- SEC, "Limit Up-Limit Down" National Market System Plan — the regulatory basis for individual-stock bands.
- Report of the Presidential Task Force on Market Mechanisms (Brady Report, 1988) — the post-1987 analysis that drove circuit breaker adoption.
