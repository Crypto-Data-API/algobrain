---
title: "S&P 500"
type: market
created: 2026-04-06
updated: 2026-06-17
status: excellent
tags: [stocks, sp500, indices, benchmark]
aliases: ["sp500", "SPX", "S&P 500 (index)", "Standard and Poor's 500"]
related: ["[[spy]]", "[[qqq]]", "[[dow-jones]]", "[[nasdaq]]", "[[value-investing]]", "[[warren-buffett]]", "[[federal-reserve]]", "[[2008-global-financial-crisis]]", "[[index-funds]]", "[[sector-rotation]]", "[[spx-options]]", "[[spy-options]]", "[[index-options]]", "[[vix]]", "[[es-futures]]", "[[micro-futures]]"]
---

# S&P 500

The S&P 500 (Standard & Poor's 500) is a float-adjusted, market-capitalization-weighted index of roughly 500 large U.S. companies that serves as the single most important benchmark for the American stock market and the global equity landscape. It represents approximately 80% of total U.S. equity market capitalization and is the index against which virtually every active equity strategy, fund, and portfolio manager is measured. When traders, journalists, and economists say "the market," they almost always mean the S&P 500.

## What It Tracks / Methodology

The index is maintained by **S&P Dow Jones Indices** and tracks the equity performance of approximately 500 of the largest U.S.-listed companies. Key methodology points:

- **Float-adjusted market-cap weighting** — each constituent's weight is proportional to its *investable* market cap (shares available to the public, excluding insider/strategic holdings). Larger companies therefore dominate index returns.
- **Committee-selected, not purely rules-based** — a company must clear quantitative hurdles (U.S. domicile, market cap above a periodically-raised threshold, positive *sum* of trailing four-quarter GAAP earnings plus a positive most-recent quarter, sufficient public float, and adequate liquidity), but a selection committee makes the final call. This is a crucial distinction from a fully systematic index: inclusion/exclusion is discretionary and can be timed.
- **Quarterly rebalancing** — share counts and float factors are reviewed and reset on the third Friday of March, June, September, and December (coinciding with "triple/quadruple witching"). Constituent *changes* can happen at any time when a company is acquired, drops below thresholds, or a more suitable candidate emerges.
- **Index divisor** — like the [[dow-jones|Dow]], the S&P uses a published divisor that is adjusted for corporate actions (splits, spinoffs, constituent swaps) so the index level stays continuous. Unlike the Dow, splits do *not* change an S&P constituent's weight, because weighting is by market cap, not share price.

### Index Addition Effect

Because hundreds of billions of dollars in passive [[index-funds]] mechanically replicate the index, an addition forces a wave of forced buying. [[tesla|Tesla]]'s December 2020 inclusion (added at full weight in a single rebalance due to its size) is the canonical example — index funds had to buy ~$80B of stock at once, and the stock ran up sharply into the event. This "index effect" is a tradeable, if shrinking, phenomenon.

## Composition & Concentration

The S&P 500 is diversified across all 11 [[gics|GICS]] sectors, but cap-weighting has pushed it to record top-heaviness. As of 2025-2026 the top 10 stocks have represented roughly **35-40%** of the index — the highest concentration in its history — meaning a handful of mega-cap AI/technology names drive index-level returns.

| Aspect | Approximate state (2025-2026) |
|--------|-------------------------------|
| **Largest constituents** | [[apple\|Apple]], [[microsoft\|Microsoft]], [[nvidia\|NVIDIA]], [[amazon\|Amazon]], Alphabet, Meta, [[tesla\|Tesla]], Broadcom |
| **Top-10 weight** | ~35-40% (record high) |
| **Heaviest sector** | [[technology\|Information Technology]] (~30%+), plus tech-like names in Comm. Services and Consumer Discretionary |
| **Lightest sectors** | [[materials\|Materials]], [[utilities\|Utilities]], [[real-estate\|Real Estate]] (each low-single-digit %) |
| **Effective number of stocks** | Far below 500 once cap-weighting is accounted for — concentration risk is real |

The practical consequence: the S&P is increasingly a *long-duration growth* bet at the top, even though it is nominally "the broad market." Equal-weight versions (e.g. RSP) behave quite differently and have lagged the cap-weighted index during the mega-cap era.

### Constituents by Sector

| Sector | Count | Largest Constituents |
|--------|-------|---------------------|
| [[communication-services\|Communication Services]] | 23 | [[charter-communications]], [[comcast]], [[disney]] |
| [[consumer-discretionary\|Consumer Discretionary]] | 51 | [[airbnb]], [[amazon]], [[aptiv]] |
| [[consumer-staples\|Consumer Staples]] | 38 | [[archer-daniels-midland]], [[brown-forman]], [[bunge-global]] |
| [[energy\|Energy]] | 22 | [[apa]], [[baker-hughes]], [[conocophillips]] |
| [[financials\|Financials]] | 74 | [[arch-capital]], [[aflac]], [[aig]] |
| [[healthcare\|Health Care]] | 60 | [[agilent-technologies]], [[abbvie]], [[abbott-laboratories]] |
| [[industrials\|Industrials]] | 78 | [[automatic-data-processing]], [[allegion]], [[ametek]] |
| [[technology\|Information Technology]] | 69 | [[apple]], [[accenture]], [[adobe]] |
| [[materials\|Materials]] | 26 | [[albemarle]], [[amcor]], [[air-products]] |
| [[real-estate\|Real Estate]] | 31 | [[american-tower]], [[alexandria-real-estate-equities]], [[avalonbay-communities]] |
| [[utilities\|Utilities]] | 31 | [[ameren]], [[american-electric-power]], [[aes]] |

```dataview
TABLE ticker AS "Ticker", sector AS "Sector", industry AS "Industry"
FROM "wiki/entities/companies"
WHERE sp500 = true
SORT sector ASC, title ASC
```

## History & Long-Run Returns

The S&P 500 in its 500-stock form launched in 1957 (its lineage of S&P composite indices runs back to the 1920s). Over the long run it has returned **approximately 10% annually in nominal terms including dividends** (~6-7% real after inflation) — the benchmark figure cited for U.S. equity expected return. [[warren-buffett]]'s famous 2007-2017 bet that an S&P 500 index fund would beat a basket of [[hedge-funds]] (it did, decisively) underscored how hard this benchmark is to beat after fees.

### Notable Drawdowns & Recoveries

| Episode | Peak-to-trough | Approx. drawdown | Recovery context |
|---------|----------------|------------------|------------------|
| 1973-74 bear (oil shock, stagflation) | 1973-1974 | ~-48% | Multi-year recovery |
| Black Monday [[1987-crash]] | Oct 1987 | ~-34% (peak-to-trough); -20.5% on Oct 19 alone | Recovered within ~2 years |
| Dot-com bust ([[dot-com-bubble]]) | 2000-2002 | ~-49% | Did not reclaim highs until 2007 |
| Global Financial Crisis ([[2008-global-financial-crisis]]) | 2007-2009 | ~-57% | Bottomed Mar 2009; full recovery by 2013 |
| COVID crash | Feb-Mar 2020 | ~-34% | Fastest bear-and-recovery on record (~5 months) |
| 2022 rate-hiking bear | Jan-Oct 2022 | ~-25% | Inflation/Fed-driven multiple compression |

The pattern: equity drawdowns are frequent and occasionally brutal, but the index has recovered every prior decline and made new highs. This is the empirical backbone of buy-and-hold indexing — and also the reason hedging and position sizing matter, since recoveries can take years.

## Ways to Trade

The S&P 500 is the most heavily traded underlying in global finance, accessible across every instrument class:

| Instrument | Ticker(s) | Notes |
|------------|-----------|-------|
| **ETFs** | [[spy\|SPY]], VOO, IVV | SPY = most-traded ETF and deepest options; VOO/IVV = ultra-low-cost buy-and-hold |
| **Futures** | [[es-futures\|E-mini (ES)]], [[micro-futures\|Micro E-mini (MES)]] | ES is among the most liquid instruments in the world, ~23h/day; MES is 1/10 the size |
| **Index options** | [[spx-options\|SPX]] | Cash-settled, European-style, 60/40 tax treatment, ~$5-6K-per-point notional; institutional standard |
| **ETF options** | [[spy-options\|SPY options]] | Physically settled, American-style, smaller notional, retail-friendly; see [[index-options]] |
| **Volatility** | [[vix\|VIX]], VIX futures/options | The VIX is derived from SPX option prices — the market's 30-day implied vol gauge |
| **Leveraged ETFs** | SSO (2x), SPXL/UPRO (3x), SH/SDS/SPXU (inverse) | Daily-rebalanced; suffer decay in choppy markets — trading tools, not holds |
| **CFDs / international** | Various | Used by non-U.S. traders without direct U.S. market access |

For the difference between cash-settled index options and ETF options (settlement, exercise style, tax), see [[spx-options]] vs [[spy-options]] and the overview at [[index-options]].

## Valuation & Regime Behavior

- **Monetary policy is the dominant macro driver.** Rate-cut expectations lift the multiple (the P/E the market pays for forward earnings); hawkish surprises compress it. [[fomc|FOMC]] decisions and the [[federal-reserve|Fed]] dot plot are the dominant scheduled catalysts.
- **Earnings set the "E."** Quarterly earnings seasons, led by mega-cap tech, drive the denominator. A handful of names ([[nvidia|NVDA]], [[apple|AAPL]], [[microsoft|MSFT]]) can swing the entire index on a single report.
- **Bond yields are the discount rate.** The [[treasuries|10-year Treasury yield]] discounts equity cash flows; rising *real* yields are a headwind, especially for long-duration growth names that now dominate the top of the index.
- **The dollar (inverse).** A stronger [[us-dollar|dollar]] pressures S&P earnings since ~40% of constituent revenue is international.
- **Valuation mean-reversion is slow and unreliable for timing.** Elevated CAPE/forward P/E has historically predicted *lower long-run returns* but is nearly useless for short-term timing — markets can stay expensive for years.

### Regime tells

- **Risk-on**: [[qqq|QQQ]]/SPY ratio rising, [[vix|VIX]] low and falling, cyclicals leading defensives, credit spreads tight.
- **Risk-off**: VIX spiking, defensives ([[utilities]], [[consumer-staples]], healthcare) outperforming, the index undercutting its 200-day moving average. The stock/bond correlation, normally negative in risk-off, *broke positive in 2022* when both fell together under inflation-driven hiking — a regime change worth watching.

## Notable Episodes

- **Tesla's December 2020 inclusion** — the largest single addition in index history, a textbook demonstration of the index-addition effect and the power of passive flows.
- **The 2022 multiple compression** — the index fell ~25% with corporate *earnings roughly flat*; almost the entire decline was P/E compression from rising rates, a clean lesson in the discount-rate channel.
- **The COVID V (2020)** — fastest crash-to-recovery on record, driven by unprecedented fiscal and monetary support.
- **Mega-cap concentration (2023-2026)** — a narrow group of AI/tech leaders ("Magnificent 7") drove the bulk of index returns, pushing top-10 weight to records and reviving concentration-risk debates last seen at the 2000 peak.

## Trading Strategies & Uses

- **Core benchmark / passive holding** — the default low-cost equity allocation via VOO/IVV/SPY; the thing alpha is measured against.
- **Portfolio hedging** — buying [[spx-options|SPX]] or [[spy-options|SPY]] puts, or shorting [[es-futures|ES]] futures, to reduce net market (beta) exposure cheaply and reversibly.
- **Premium selling / volatility harvest** — selling SPX/SPY options to capture the [[volatility-risk-premium]]; the S&P's deep, liquid options chain is the canonical venue. 0DTE SPX options have exploded to a large share of total volume.
- **Sector rotation** — using the index as the neutral benchmark against the 11 [[gics|GICS]] sector ETFs (XLK, XLF, XLE, etc.) for relative-value [[sector-rotation]] trades.
- **Pair / relative-value trades** — long [[qqq|QQQ]] / short SPY to express growth-vs-broad-market views; long a stock/sector vs short SPY to isolate alpha from beta ([[long-short-equity]]).
- **Index arbitrage** — exploiting basis between SPY, ES futures, and the underlying 500 stocks ([[index-arbitrage]], [[etf-arbitrage]]).

## Risks / Limitations

- **Concentration risk** — record top-10 weight means the "diversified" index is increasingly a bet on a few mega-cap names; a leadership stumble can drag the whole index.
- **U.S.-only, large-cap-only** — no small-caps, no international; over-weighting it concentrates a portfolio in one country and one size factor.
- **Survivorship/committee discretion** — the committee can add hot names near peaks and drop laggards near troughs, subtly affecting reported long-run returns.
- **Sequence-of-returns risk** — the ~10% long-run average masks decade-long stretches (e.g. 2000-2012) of roughly flat real returns; timing of contributions/withdrawals matters enormously.
- **Crowded passive flows** — the sheer scale of index replication can amplify both melt-ups and forced selling, a structural fragility debated since the 2010s.

## Related

- [[spy]] — the dominant S&P 500 ETF and the most-traded security in the world
- [[qqq]] — Nasdaq-100 ETF, the tech-heavy comparison
- [[dow-jones]] — 30-stock price-weighted blue-chip index
- [[index-funds]] — passive vehicles built on the index
- [[sector-rotation]] — rotating between the 11 GICS sectors
- [[spx-options]] / [[spy-options]] / [[index-options]] — the options complex on the index
- [[es-futures]] / [[micro-futures]] — the futures complex
- [[vix]] — implied volatility derived from SPX options

## Sources

- S&P Dow Jones Indices — S&P 500 index methodology and factsheet
- CBOE — SPX options volume data
- Berkshire Hathaway shareholder letters — Buffett's 10-year index-fund bet
- General market knowledge for long-run return and drawdown figures
