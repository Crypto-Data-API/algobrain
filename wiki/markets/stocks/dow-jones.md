---
title: "Dow Jones Industrial Average"
type: market
created: 2026-04-06
updated: 2026-06-17
status: excellent
tags: [stocks, indices, benchmark, history, sp500]
aliases: ["DJIA", "Dow", "the Dow", "Dow Jones", "Dow 30"]
related: ["[[s-and-p-500]]", "[[nasdaq]]", "[[qqq]]", "[[spy]]", "[[equity-index]]", "[[1987-crash]]", "[[2008-global-financial-crisis]]", "[[paul-tudor-jones]]", "[[index-funds]]", "[[futures]]", "[[index-options]]", "[[es-futures]]", "[[micro-futures]]", "[[sector-rotation]]"]
---

# Dow Jones Industrial Average

The Dow Jones Industrial Average (DJIA or "the Dow") is a **price-weighted** index of 30 large, blue-chip U.S. companies and the oldest continuously published stock-market index in the world. While far less representative than the [[s-and-p-500]], it remains the most widely recognized market indicator in popular culture and financial media — the number quoted on the evening news. Professionals largely ignore it as a benchmark in favor of the cap-weighted S&P 500, but it remains a tradeable, history-rich instrument.

## Overview

Created by Charles Dow and Edward Jones in **1896**, the DJIA originally tracked 12 industrial companies. It now includes 30 companies selected by the editors of *The Wall Street Journal* (in conjunction with S&P Dow Jones Indices) to represent the breadth of the U.S. economy. Current components include [[apple|Apple]], [[microsoft|Microsoft]], Goldman Sachs, UnitedHealth, JPMorgan Chase, [[nvidia|NVIDIA]], and others. No company is in the Dow forever — the average constituent tenure spans decades, but the roster turns over as the economy evolves (General Electric, an original-era member, was removed in 2018).

## What It Tracks / Methodology

### Price-weighting (the defining quirk)

Unlike the market-cap-weighted [[s-and-p-500]], the Dow is **price-weighted** — a stock's influence is proportional to its *share price*, not its company size. A $1 move in a $500 stock moves the index exactly as much as a $1 move in a $50 stock, even if the latter company is ten times larger. Consequences:

- A high-priced constituent (e.g. UnitedHealth, Goldman Sachs) can dominate the index's daily move regardless of its economic weight.
- Stock splits *reduce* a company's index influence (price halves → weight halves) even though nothing changed about the business — the opposite of economic logic.
- The methodology is widely criticized as an 1890s relic, but the index's longevity and name recognition keep it prominent.

### The Dow Divisor

The index level is the **sum of the 30 component share prices divided by the Dow Divisor**, a published adjustment factor maintained by S&P Dow Jones Indices. The divisor changes whenever a stock split, constituent swap, or corporate action would otherwise create an artificial jump, keeping the index continuous. After decades of adjustments the divisor is now well below 1 (around ~0.16), meaning a $1 move in any single component currently moves the index by roughly **6 points**. To prevent any one name from overwhelming the basket, the Dow effectively caps inclusion of very-high-priced shares — a reason NVIDIA's pre-split price kept it out until its **10-for-1 split in 2024** brought its share price low enough.

### Selection & reconstitution

The Dow is reshuffled **infrequently and at committee discretion** — there is no fixed rebalance calendar and no quantitative inclusion formula. The committee favors large, reputable, "blue-chip" companies that broadly represent U.S. industry (excluding transportation and utilities, which have their own Dow averages). Notable recent changes:

- **February 2024** — **[[amazon|Amazon]]** replaced Walgreens Boots Alliance (partly to offset reduced retail-sector weighting after Walmart's 3-for-1 split).
- **November 2024** — **[[nvidia|NVIDIA]]** replaced Intel, and **Sherwin-Williams** replaced [[dow|Dow Inc.]] — adding mega-cap AI-chip exposure and reflecting the index's lag in capturing the AI capex cycle relative to the [[s-and-p-500]] and [[nasdaq]].

## Composition & Concentration

The 30 components span most of the economy but, because of price-weighting, the *index's* tilt does not match the *economy's*:

| Aspect | Approximate state (2025-2026) |
|--------|-------------------------------|
| **Components** | 30 blue-chip U.S. companies |
| **Heaviest by index weight** | The highest *share-priced* names (e.g. Goldman Sachs, UnitedHealth, Microsoft) — *not* necessarily the biggest companies |
| **Under-represented** | Mega-cap growth/tech as a *group* — the Dow holds fewer of them and price-weighting can understate them |
| **Excluded by mandate** | Transportation and utilities (tracked by the separate Dow Transports and Dow Utilities) |
| **Sector feel** | Industrials, financials, health care, and consumer names feature heavily; it skews more "old economy" than the S&P |

This is why the Dow can **lag in mega-cap-tech-led rallies** — it under-weights the largest growth names relative to the cap-weighted [[s-and-p-500]] and especially [[qqq|QQQ]]. Traders monitor Dow-vs-S&P divergences as a rough value-vs-growth tell.

## History & Long-Run Returns

The Dow's 130-year record makes it the canonical long-run chart of U.S. equities. Like the broad market, it has compounded at roughly **~10% nominal annualized including dividends** over the long run, punctuated by severe drawdowns.

### Notable drawdowns & recoveries

| Episode | Approx. drawdown | Recovery context |
|---------|------------------|------------------|
| 1929 Crash & Depression | ~-89% (1929-1932) | Did **not** reclaim its pre-crash high until **1954** — 25 years |
| 1973-74 bear | ~-45% | Multi-year recovery |
| Black Monday [[1987-crash]] | **-22.6% in a single day** (Oct 19, 1987) | The single worst one-day percentage drop; recovered within ~2 years. The crash that made [[paul-tudor-jones]]'s reputation |
| Dot-com bust | ~-38% (2000-2002) | Milder than the tech-heavy [[nasdaq]] because the Dow under-weighted dot-coms |
| Global Financial Crisis ([[2008-global-financial-crisis]]) | ~-54% | Fell from 14,164 (2007) to **6,547** (Mar 2009); recovered by 2013 |
| COVID crash | ~-37% | Feb-Mar 2020; recovered to new highs within months |

The 1929 → 1954 recovery is the most-cited reminder that index recoveries can take a *generation*, and that the Dow's headline level says nothing about dividends reinvested along the way.

## Ways to Trade

| Instrument | Ticker(s) | Notes |
|------------|-----------|-------|
| **ETF** | DIA ("Diamonds") | State Street SPDR; ~0.16% expense ratio; holds the 30 components in price-weighted proportion; pays a **monthly** dividend |
| **Futures** | [[es-futures\|E-mini Dow (YM)]] | CME; $5 × index multiplier; the primary derivative |
| **Micro futures** | [[micro-futures\|Micro E-mini Dow (MYM)]] | $0.50 × index; for smaller accounts |
| **Options** | DIA options; DJX index options; YM futures options | DIA = ETF options; DJX = cash-settled index options (1/100 of the Dow); see [[index-options]] |

For most professional purposes the [[spy|SPY]]/[[es-futures|ES]]/[[spx-options|SPX]] complex on the [[s-and-p-500]] is deeper and more liquid; Dow instruments are used mainly for headline-driven trades, Dow-specific exposure, or historical/technical analysis.

## Valuation & Regime Behavior

- **Same macro drivers as the broad market** — monetary policy, the [[treasuries|10-year yield]] as discount rate, earnings, and the dollar all drive the Dow as they do the [[s-and-p-500]] (see [[s-and-p-500#Valuation & Regime Behavior]]).
- **Old-economy / value tilt** — the Dow's roster and price-weighting give it a mild value/cyclical lean, so it tends to *outperform* the S&P and QQQ in value-led, rising-rate regimes and *underperform* in mega-cap-growth-led regimes.
- **Lower beta to tech** — because it under-weights long-duration growth, the Dow is somewhat less rate-sensitive than [[qqq|QQQ]].

## Notable Episodes

- **Black Monday, October 19, 1987** — the Dow's -22.6% single-day collapse remains the largest one-day percentage drop in its history and a defining moment in market-structure history (portfolio insurance, circuit breakers).
- **GFC 14,164 → 6,547** — the 2007-2009 halving is the modern reference point for a blue-chip bear market.
- **Dow Theory lineage** — the index anchors **Dow Theory**, the original framework of technical analysis (the Dow Industrials confirming/diverging from the **Dow Transports** as a trend signal).
- **NVIDIA's 2024 entry** — only possible after a 10-for-1 split lowered its share price enough to fit the price-weighted basket — a vivid illustration of the price-weighting quirk.

## Trading Strategies & Uses

- **Headline / sentiment trades** — the Dow drives media coverage and retail sentiment; "the Dow is down 500 points" moves the public mood even when the S&P barely moves.
- **Dow-vs-S&P divergence** — monitoring the Dow against the cap-weighted [[s-and-p-500]] as a coarse value-vs-growth / breadth signal feeding [[sector-rotation]] views.
- **Dow Theory confirmation** — using the Industrials vs Transports relationship as a trend-confirmation overlay.
- **Tradeable exposure** — YM/MYM futures and the DIA ETF for those who specifically want price-weighted blue-chip exposure or to trade the headline index.
- **Pairs** — long DIA / short [[qqq|QQQ]] to express a value/old-economy-over-growth view.

## Risks / Limitations

- **Price-weighting is economically arbitrary** — a stock's index influence depends on its (split-adjustable) share price, not its size, distorting what the index "represents."
- **Only 30 stocks** — far less diversified and representative than the [[s-and-p-500]]'s ~500; idiosyncratic single-name moves matter more.
- **Committee discretion & infrequent rebalancing** — the roster can lag structural shifts in the economy (e.g. slow to add mega-cap tech, as the AI cycle showed).
- **Headline ≠ total return** — the quoted index level excludes dividends; long-run "recovery" comparisons can mislead without reinvested-dividend context.
- **Shallower liquidity** — Dow derivatives (YM, DIA, DJX) are liquid but thinner than the S&P complex for large size.

## Related

- [[s-and-p-500]] — the cap-weighted broad-market benchmark professionals prefer
- [[spy]] — the dominant S&P 500 ETF
- [[qqq]] — the tech-heavy Nasdaq-100 ETF; the Dow's growth-tilted opposite
- [[nasdaq]] — the tech-heavy exchange and index
- [[equity-index]] — index-construction concepts (price- vs cap-weighting)
- [[index-options]] — the cash-settled index options family (DJX)
- [[es-futures]] / [[micro-futures]] — the futures complex (YM/MYM)
- [[1987-crash]] — the 22.6% single-day drop
- [[2008-global-financial-crisis]] — the 14,164 → 6,547 decline

## Sources

- S&P Dow Jones Indices — DJIA methodology and divisor
- Perplexity sonar query, 2026-06-12 (recent constituent changes)
- General market knowledge for long-run return and historical drawdown figures
