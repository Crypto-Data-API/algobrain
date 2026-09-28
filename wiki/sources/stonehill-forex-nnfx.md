---
title: "Stonehill Forex — NNFX Method and Indicator Library"
type: source
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [education, forex, indicators, methodology, backtesting, trend-following, risk-management]
aliases: ["Stonehill Forex NNFX", "Stonehill Indicator Library", "NNFX Flow Chart"]
related: ["[[stonehill-forex]]", "[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[mcginley-dynamic]]", "[[schaff-trend-cycle]]", "[[vortex-indicator]]", "[[waddah-attar-explosion]]", "[[choppiness-index]]", "[[repainting]]", "[[external-strategy-sources]]"]
source_type: article
source_url: "https://stonehillforex.com/indicator-library/"
source_author: "Stonehill Forex (Dan Stone); NNFX flow chart by Rui Silva (nnfxalgotester.com), method by VP (nononsenseforex.com)"
source_date: 2026-09-28
confidence: medium
claims_count: 20
---

Stonehill Forex is a forex-education site built around the **No Nonsense Forex (NNFX)** trading algorithm. Its most reusable assets for this wiki are (1) a free, role-classified **indicator library** (baseline, confirmation, volume/volatility, miscellaneous) with a blog post per indicator that tests it *in its NNFX role*, (2) a documented **indicator-testing protocol**, and (3) a **Repainting Indicator Register**. The rule set itself originates with the NNFX YouTube channel ("VP", nononsenseforex.com); the widely circulated NNFX entry/exit flow chart used below was compiled by Rui Silva of nnfxalgotester.com. This summary was harvested on 2026-09-28 from the Stonehill site (index pages, testing-settings page, and several indicator profiles) plus the public NNFX flow-chart PDF.

## Source Details

| Field | Value |
|---|---|
| Site | https://stonehillforex.com |
| Key pages | `/indicator-library/`, `/indicator-testing-settings/`, `/repainting-indicator-register/`, `/nnfx-algo-tester/`, per-indicator blog posts under `/category/indicator/` |
| Flow chart | "No Nonsense Forex Flow Charts" PDF, hosted at nononsensetrader.com (Rui Silva) |
| Fetched | 2026-09-28 |
| Access | Library and blog free; Stonehill 201 course and algo tester are paid / waitlisted |

## Claims

### About the site

1. [MEDIUM] Stonehill Forex is run by Dan Stone (M.A.T., Ed.S.), who self-describes as trading forex since 2003; the site frames itself as structured trading education. (Self-description on the home page.)
2. [HIGH] The indicator library is organised by NNFX role: Confirmation (50+ indicators), Baseline (20+), Volume/Volatility (12+), and Miscellaneous (e.g. ATR). Listed baselines include Hull MA, McGinley Dynamic, ALMA, KAMA and SuperSmoother; confirmations include Kalman filter, zero-lag MACD, Fisher, Schaff Trend Cycle and Vortex; volume/volatility tools include ADX, Waddah Attar Explosion, Choppiness Index and Williams VIX Fix. (Observed on `/indicator-library/`, 2026-09-28.)
3. [HIGH] The site maintains a Repainting Indicator Register flagging indicators whose historical plots change after the fact. (Observed; see [[repainting]].)
4. [MEDIUM] Stonehill promotes an "NNFX Algo Tester" for filtering indicators and testing whole algorithms; as of the fetch date the page is a waitlist. (Observed `/nnfx-algo-tester/`.)

### Testing protocol

5. [HIGH] Current Stonehill protocol (stated in 2025–2026 profiles, e.g. FRAMA as a baseline): daily timeframe, 3-year span, USD 100,000 starting balance, 2% risk per signal split into two half-size trades, 20:1 leverage, open-of-period pricing, stop at 1.25–1.5 x ATR depending on asset, assets EUR/USD, BTC/USD, XAU/USD and SPX500. Metrics: long/short signal counts, win/loss % excluding "chalk" (breakeven) trades, ROI %.
6. [HIGH] Results are published at **default settings** to show an indicator's "natural state before optimizing", and Stonehill cautions that individual results will vary.
7. [MEDIUM] An older protocol (2022 Vortex profile) tested EUR/USD, BTC/USD and XAU/USD over 1 year daily and 3 months 4-hour, and recommended a five-pair validation basket: EUR/USD, AUD/NZD, EUR/GBP, AUD/CAD, CHF/JPY — pairs chosen for differing behaviour (trending majors, ranging crosses, a yen cross).
8. [HIGH] The `/indicator-testing-settings/` page lists, per indicator, its role, the signal-reading method used in testing ("Zero Cross", "Two Lines Cross", "Histogram/Color") and the default parameters, but does not itself publish results.

### NNFX algorithm structure (flow chart)

9. [HIGH] The algorithm has six slots: ATR (trade management), Baseline, main Confirmation (C1), second Confirmation (C2), Volume indicator, Exit indicator; an optional Continuation indicator defaults to C1.
10. [HIGH] Standard entry: C1 signals, baseline agrees, price within 1 x ATR of the baseline, C2 agrees, volume agrees.
11. [HIGH] Baseline-cross entry: price closes across the baseline, C1 agrees, within 1 x ATR, C2 and volume agree, and C1's own signal was fewer than 7 candles earlier ("a bridge too far" — the 7-candle rule).
12. [HIGH] Pullback entry: baseline signals but price is beyond 1 x ATR; if the next candle closes back within 1 x ATR with C1, C2 and volume agreeing, enter.
13. [HIGH] One-candle rule: on standard and baseline-cross entries, filters may lag by at most one candle; if all agree on the next candle and price has retraced, enter. Continuation entries (after a prior entry, baseline not crossed since, new C1 signal, C2 agrees) ignore both the 1 x ATR and one-candle rules and do not need volume.
14. [HIGH] Money management: 2% risk per trade split into two 1% orders, both with stop 1.5 x ATR; order 1 takes profit at 1 x ATR; order 2 has no target. When order 1 fills its target, order 2's stop moves to breakeven; a trailing variant trails order 2 at 1.5 x ATR once it is 2 x ATR in profit, stepping each further 0.5 x ATR.
15. [HIGH] Exits: new exit-indicator signal, close across the baseline, or C1 (or C2) flipping to the opposite signal; with no exit indicator, C1's opposite signal is the exit. A stop hit closes both orders.
16. [MEDIUM] Trades are taken near the daily close (the flow chart cites 23:40 broker time, i.e. just before the New York 5 pm daily roll).

### Indicator-profile findings

17. [MEDIUM] McGinley Dynamic is described as "underrated" yet among the most reliable baselines; developed by John R. McGinley (1997, *Journal of Technical Analysis*); Stonehill default period 12.
18. [MEDIUM] Schaff Trend Cycle (Doug Schaff, late 1990s) combines MACD with a stochastic cycle, bounded 0–100 with 25/75 trigger levels; profiled as a confirmation indicator.
19. [MEDIUM] Waddah Attar Explosion (Ahmad Waddah Attar, 2007) combines MACD-difference momentum with a Bollinger-width "explosion line" and a dead-zone filter; Stonehill stresses never trading on a volume indicator alone. Its WAE profile states results were still "in process".
20. [LOW] Individual profile remarks: Cross Roads' default settings were the best tested on daily BTC; TopTrend was strong on XAU, soft on EUR/USD and SPX500, average on BTC; Vortex produced no positive-ROI setting on 4-hour XAU over 3 months. Single-window, default-setting, pre-cost observations.

## Assessment

The **rule structure** (claims 9–15) is high-confidence because it is a documented, internally consistent public rule set. The **indicator results** are low-to-medium confidence as edge evidence: they are short (1–3 year) windows, few assets, pre-cost, and — because many indicators are screened against the same data — subject to heavy [[data-snooping-and-p-hacking|multiple-testing bias]]. Stonehill's inclusion of BTC/USD in its test basket since 2022 makes it directly relevant to crypto, but no Stonehill result should be treated as a validated edge without re-testing out of sample with costs (see [[overfitting-detection]]).

## Entities, concepts and pages touched

- Entity: [[stonehill-forex]]
- Method: [[nnfx-method]]
- Strategy: [[nnfx-crypto-daily-system]]
- Indicators created: [[mcginley-dynamic]], [[schaff-trend-cycle]], [[vortex-indicator]], [[waddah-attar-explosion]], [[choppiness-index]]
- Indicators annotated with NNFX roles: [[atr]], [[kama]], [[hull-moving-average]], [[alma]], [[jurik-moving-average]], [[frama]], [[adx]], [[chandelier-exit]]
- Related: [[repainting]], [[external-strategy-sources]]

## Related

- [[nnfx-method]] · [[nnfx-crypto-daily-system]] · [[stonehill-forex]] · [[external-strategy-sources]]
