---
title: "Stonehill Forex"
type: entity
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [company, education, forex, indicators, methodology, backtesting]
aliases: ["Stonehill", "stonehillforex.com"]
related: ["[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[stonehill-forex-nnfx]]", "[[repainting]]", "[[external-strategy-sources]]"]
entity_type: company
founded: ""
headquarters: ""
website: "https://stonehillforex.com"
---

Stonehill Forex is a forex trading-education website best known as a companion resource for the **No Nonsense Forex ([[nnfx-method|NNFX]])** algorithmic trading method. It publishes a free indicator library organised by NNFX role, a blog profile testing each indicator in that role, a register of repainting indicators, and paid courses (Source: [[stonehill-forex-nnfx]]).

## Overview

The site is run by Dan Stone, who describes himself as an educator (M.A.T., Ed.S.) trading forex since 2003 (Source: [[stonehill-forex-nnfx]]). Founding year and location are not stated on the site. Stonehill did not originate NNFX — the method comes from the NNFX YouTube channel run by "VP" (nononsenseforex.com) — but it is one of the largest public repositories of indicators *classified and tested by NNFX role*, which is what makes it useful here.

## What it offers

| Resource | What it is | Relevance to this wiki |
|---|---|---|
| Indicator Library | Free MT4-oriented downloads grouped as Baseline (20+), Confirmation (50+), Volume/Volatility (12+), Miscellaneous | Source list for [[indicators-overview|indicator]] candidates per role |
| Indicator profiles (blog) | One post per indicator: construction, settings, and a test in its NNFX role | Default-settings, pre-cost results; treat as hypotheses |
| Indicator Testing Settings | Table of each indicator's role, signal-reading method (zero cross, two-line cross, histogram/colour) and default parameters | Makes the tests reproducible in principle |
| Repainting Indicator Register | List of indicators whose historical values change after the bar closes | Directly relevant to [[repainting]] and [[lookahead-bias]] |
| Stonehill 201 course, newsletter | Paid / email education | Not reviewed |
| NNFX Algo Tester | Tool to test indicator stacks; waitlist as of 2026-09-28 | Not reviewed |

## Testing protocol

Stonehill's current protocol (2025–2026 profiles) tests each indicator on the **daily** timeframe over **3 years**, with 2% risk split into two half trades, ATR-based stops (1.25–1.5 x ATR), and — notably for this wiki — **BTC/USD** alongside EUR/USD, XAU/USD and SPX500. Earlier profiles recommended a five-FX-pair basket (EUR/USD, AUD/NZD, EUR/GBP, AUD/CAD, CHF/JPY). Results are reported at default settings as win/loss % (excluding breakeven "chalk" trades) and ROI (Source: [[stonehill-forex-nnfx]]). The full method is described on [[nnfx-method#Testing an indicator in isolation]].

## Assessment

- **Strength**: a disciplined, role-based way to evaluate one component at a time, and a large, free, consistently documented indicator catalogue.
- **Weakness**: short windows, few instruments, no transaction costs, and a large number of indicators screened against the same data — so the "winners" carry substantial [[data-snooping-and-p-hacking|selection bias]]. Treat published results as a shortlist to re-test, not evidence of edge.
- **Scope note**: the site is forex-first; SPX500 appears only as a test instrument and is out of scope here.

## Getting the Data (CryptoDataAPI)

Stonehill's per-indicator test can be replicated on crypto with daily OHLCV. Live: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000`. Historical: `GET /api/v1/backtesting/klines` (archive since 2020) and `GET /api/v1/backtesting/funding` to add perp carry, which Stonehill's FX tests do not model. See [[cryptodataapi-market-data]] and [[cryptodataapi-backtesting]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

## Related

- [[nnfx-method]] — the algorithm structure Stonehill's library is organised around
- [[nnfx-crypto-daily-system]] — a concrete crypto configuration built from Stonehill-profiled indicators
- [[mcginley-dynamic]] · [[schaff-trend-cycle]] · [[vortex-indicator]] · [[waddah-attar-explosion]] · [[choppiness-index]] — indicators harvested from the library
- [[repainting]] · [[overfitting-detection]] · [[external-strategy-sources]]

## Sources

- [[stonehill-forex-nnfx]] — harvest of stonehillforex.com and the NNFX flow chart, 2026-09-28
