---
title: "Earnings Growth"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, stocks, momentum]
aliases: ["Earnings Growth", "EPS Growth", "Earnings Per Share Growth", "Profit Growth"]
related: ["[[earnings-per-share]]", "[[earnings-quality]]", "[[price-to-earnings]]", "[[peg-ratio]]", "[[growth-investing]]", "[[earnings-surprise-prediction]]", "[[economic-moat]]", "[[valuation]]"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[earnings-per-share]]"]
difficulty: beginner
---

Earnings growth is the rate at which a company's profits (most often measured per share) increase over time. It is the single most important driver of long-run equity returns: over multi-year horizons, stock prices track the trajectory of earnings far more closely than they track sentiment or multiples. Both the *level* and the *acceleration/deceleration* of earnings growth are tradable signals.

## Overview

Earnings growth is typically expressed as a year-over-year (YoY) or quarter-over-quarter percentage change in [[earnings-per-share|EPS]] or net income:

```
YoY EPS Growth = (EPSₜ − EPSₜ₋₁) / |EPSₜ₋₁|
```

For multi-year horizons, the compound annual growth rate (CAGR) smooths volatility:

```
EPS CAGR = (EPS_end / EPS_start)^(1/n) − 1
```

Common variants:

- **Trailing growth** — realized YoY change from reported results.
- **Forward growth** — analyst consensus expectation for next year / next quarter.
- **Sustainable growth rate** — ROE × retention ratio; the rate a firm can grow without external financing.
- **Organic vs inorganic** — internally generated growth vs growth bought through acquisitions.

## What drives earnings growth

1. **Revenue growth** — more units, higher prices, new markets.
2. **Margin expansion** — operating leverage, cost discipline, mix shift toward higher-margin products.
3. **Share-count reduction** — buybacks raise EPS even when net income is flat (a key reason EPS growth ≠ profit growth).
4. **Financial leverage** — debt-funded growth amplifies EPS but adds risk.

The composition matters enormously for quality: revenue-and-margin-driven growth is far more durable than buyback-driven or leverage-driven EPS growth. This is the bridge to [[earnings-quality]].

## Valuation linkage

Earnings growth is the numerator of growth-adjusted valuation. The [[price-to-earnings|P/E]] multiple a market awards is largely a function of expected growth, so the [[peg-ratio|PEG ratio]] normalizes for it:

```
PEG = (P/E) / (annual EPS growth rate %)
```

A PEG near 1 is the rough heuristic for "growth fairly priced." High-growth names command premium multiples precisely because more of their value sits in distant cash flows — making them long-"duration" equities sensitive to discount-rate changes (see [[duration]] and [[interest-rate-risk]]).

## Trading relevance

- **Post-earnings-announcement drift (PEAD).** Stocks that report growth well above consensus tend to *keep* outperforming for weeks after the print — one of the most robust documented [[anomalies-overview|anomalies]]. This is the basis for momentum-style [[earnings-plays|earnings plays]] and for [[earnings-surprise-prediction|surprise-prediction]] models.
- **Growth acceleration/deceleration.** The market often pays more for the *second derivative* — the inflection from decelerating to accelerating growth — than for a high but stable rate. Detecting the turn early is the edge in [[growth-investing]].
- **Expectations, not absolutes.** Price reacts to growth *relative to what was already priced in*. A company growing EPS 30% can fall hard if consensus expected 40%. The trade is always in the gap between realized growth and expectations.
- **Quality filter.** Screen growth against [[earnings-quality]]: high reported EPS growth funded by accruals, one-offs, or aggressive recognition ([[earnings-management]]) tends to mean-revert and reverse — a short setup, not a long one.
- **Mega-cap concentration.** In recent cycles, index-level earnings growth has been dominated by a handful of [[economic-moat|wide-moat]] mega-caps; breadth of earnings growth is itself a regime signal.

## Pitfalls

- **Low-base distortion** — growth off a tiny or negative prior-year base produces meaningless percentages.
- **Non-GAAP inflation** — "adjusted" EPS growth can far exceed GAAP growth; reconcile the two.
- **Buyback masking** — falling net income can still produce rising EPS via shrinking share count.
- **Cyclicality** — peak-cycle growth rates are not extrapolatable; growth investors who buy at the cyclical peak multiple get hurt twice.

## Related

- [[earnings-per-share]] — the metric most growth rates are computed on
- [[earnings-quality]] · [[earnings-management]] — is the growth real?
- [[price-to-earnings]] · [[peg-ratio]] — pricing growth
- [[growth-investing]] — the strategy built around it
- [[earnings-plays]] · [[earnings-surprise-prediction]] — trading the growth surprise
- [[economic-moat]] — what makes growth durable

## Sources

- Penman, *Financial Statement Analysis and Security Valuation* — earnings growth and its valuation linkage.
- Bernard & Thomas (1989/1990) — foundational research on post-earnings-announcement drift.
- CFA Institute curriculum, Equity Valuation readings on growth and the PEG ratio.
