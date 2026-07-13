---
title: "Market Crashes"
type: index
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [history, crashes, index]
aliases: ["Stock Market Crash", "stock-market-crash", "Crashes Overview", "Market Crashes Overview", "crashes-overview"]
related: ["[[market-crashes]]", "[[flash-crashes]]", "[[history-overview]]", "[[circuit-breakers]]", "[[deleveraging]]"]
---

# Market Crashes

Documented market crashes, flash crashes, and systemic failures throughout financial history. This is the catalogue/index; for the *trading framework* on treating crashes as buying opportunities, see [[market-crashes]].

Crashes are the most dramatic events in financial markets — sudden, violent declines that destroy wealth, expose hidden risks, and reshape regulation. Almost every crash shares a common skeleton: a **leverage buildup** during the boom, a **trigger**, a **[[deleveraging]] cascade** of forced selling, **liquidity evaporation**, capitulation, and (for broad indices, historically) eventual recovery. What differs is the plumbing — margin loans in 1929, portfolio insurance in 1987, opaque counterparty exposure in 2008, perpetual-futures liquidation engines in crypto.

Studying crashes is essential preparation. The traders who survive them are those who understood the risks — and sized their leverage — before the panic started.

## Equity & Systemic Crashes

| Event | Date | Magnitude | Defining mechanism |
|-------|------|-----------|--------------------|
| [[1929-crash\|Wall Street Crash of 1929]] | Oct 1929 | -89% peak-to-trough (to 1932) | 10%-margin leverage cascade; monetary contraction → Great Depression |
| [[black-monday\|Black Monday]] | Oct 19, 1987 | DJIA -22.6% in one day | Portfolio-insurance feedback loop; birth of circuit breakers |
| [[asian-financial-crisis\|Asian Financial Crisis]] | 1997-98 | Currencies -50 to -80% | Broken currency pegs; contagion; unhedged FX borrowing |
| [[long-term-capital-management\|LTCM Collapse]] | 1998 | $4.6B fund loss | Extreme leverage + convergence trades + Russian default |
| [[dot-com-bubble\|Dot-Com Bust]] | 2000-02 | Nasdaq -78% | Tech-valuation bubble unwind |
| [[2008-global-financial-crisis\|Global Financial Crisis]] | 2007-09 | S&P -57% | Subprime, opaque leverage, counterparty contagion, Lehman |
| [[covid-crash\|COVID Crash]] | Mar 2020 | S&P -34% in ~1 month | Pandemic shock; 4 circuit-breaker halts; fastest-ever bear |

## Flash Crashes

- [[flash-crashes]] — Hub page: anatomy, timeline, structural causes, lessons
- [[flash-crash-2010]] — The original: DJIA -1,000 points in 36 minutes
- [[flash-crash-2015-etf]] — ETFs trade 20-35% below NAV at the open
- [[flash-crash-2016-gbp]] — GBP -6% in 2 minutes during the Asian session
- [[volmageddon-2018]] — VIX +115%, XIV terminated, short-vol trade wiped out
- [[crypto-flash-crashes]] — Liquidation cascades in a market with no circuit breakers

## Commodity Market Crises

- [[1973-oil-crisis]] — OPEC embargo: oil quadruples $3 → $12/bbl; stagflation; the first oil shock
- [[2020-negative-oil-price]] — WTI May futures settle at -$37.63/bbl on storage saturation
- [[2022-lme-nickel-squeeze]] — Nickel doubles to $100k/t; LME cancels $3.9B in trades and suspends the market for a week
- [[hunt-brothers-silver-corner]] — 1979-80 silver corner attempt (see also [[notable-trades-overview|Notable Trades]])

## Crypto Crashes

- [[terra-luna]] — Algorithmic-stablecoin death spiral; $50B+ wiped (May 2022)
- [[ftx-collapse]] — Exchange insolvency and the $8B hole (Nov 2022)
- [[crypto-flash-crashes]] — Recurring liquidation cascades hub
- [[2025-10-crypto-liquidation-cascade]] — Largest forced-liquidation event ever (~$20B); first systemic ADL crisis

## Market Manipulation (crash triggers)

- [[market-manipulation]] — Full taxonomy: spoofing, wash trading, pump & dump, front-running, cornering
- [[spoofing]] — Phantom orders: from Navinder Sarao to JPMorgan's $920M fine

## All Pages in This Section

```dataview
TABLE status, updated, tags
FROM "wiki/history/crashes"
WHERE type != "index" AND type != "redirect"
SORT updated DESC
```

## Related

- [[market-crashes]] — the "buy the crash" trading framework
- [[flash-crashes]] — flash-crash hub
- [[circuit-breakers]] — the safeguard born from 1987
- [[deleveraging]] — the forced-selling mechanism common to nearly all crashes
- [[history-overview]] — broader financial-history index
