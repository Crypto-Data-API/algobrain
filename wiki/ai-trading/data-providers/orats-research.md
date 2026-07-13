---
title: "ORATS Research"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [data-provider, options, volatility, backtesting, research]
aliases: ["ORATS Research"]
related:
  - "[[orats]]"
  - "[[cboe-livevol]]"
  - "[[livevol]]"
  - "[[tastytrade]]"
  - "[[options-premium-selling]]"
  - "[[implied-volatility]]"
  - "[[volatility-skew]]"
  - "[[volatility-term-structure]]"
  - "[[backtesting]]"
  - "[[earnings-iv-crush]]"
  - "[[theta-targeting]]"
source_type: data
source_url: "https://orats.com/research"
source_author: "ORATS / Matt Amberson"
source_date: 2026-05-07
source_file: "n/a (live web property)"
confidence: high
claims_count: 8
---

ORATS Research is the public-facing research and education arm of [[orats|ORATS (Option Research & Technology Services)]], hosted at orats.com/research. It packages the firm's smoothed implied-volatility surface and historical chains into a small library of named "studies" — most prominently the Wheel research, the Long Strangle Backtest, the Calendar Backtest, and the Earnings Effect database — together with an interactive Backtests Generator and ranked-ticker scanners that sort the optionable US universe by IV-rank, IV-percentile, term-structure slope, and skew. The research output is free to read and is widely cited inside the [[tastytrade]] ecosystem, by retail YouTube educators, and in published options blogs because the underlying data is research-grade and the methodology is documented.

## Overview

[[orats|ORATS]] is primarily a data and analytics business; the Research arm exists to demonstrate what the firm's data can do and to drive subscriptions to the [[orats|core ORATS]] platform. Editorially the research is consistent with the [[options-premium-selling|premium-selling]] thesis popularised by [[tastytrade]] and the wider retail options community: short-premium structures harvested mechanically over many trades produce positive expectancy when implied volatility is rich relative to subsequent realised volatility. Where ORATS Research differs is in the rigour of the data layer — the studies use ORATS' proprietary smoothed [[implied-volatility|IV]] surface rather than raw OPRA mid-quotes, which materially reduces the noise that contaminates retail-sourced backtests.

The four flagship outputs:

- **The Wheel** — long-running backtest of the wheel strategy (cash-secured puts rolled into covered calls when assigned) across a curated universe of liquid US underlyings, with sensitivity to delta selection, DTE, and management rules.
- **Long Strangle Backtest** — a study of long-vol structures across underlyings and regimes, used as a counter-example to the firm's predominantly short-vol research.
- **Calendar Backtest** — front-month-short / back-month-long [[calendar-spread|calendar]] performance across underlyings, with sensitivity to entry [[volatility-term-structure|term structure]] slope.
- **Earnings Effect database** — historical record of pre-event [[implied-volatility|IV]] ramp and post-event crush per ticker, used to rank which names have the most reliable [[earnings-iv-crush]].

Beyond the named studies, the research site exposes weekly and monthly rankings of the entire optionable US universe by metrics that are ORATS-specific: implied earnings move, post-earnings IV slope, slope of skew, contango/backwardation in the term structure, and "delta cost" (a proprietary measure of how expensive it is to buy delta exposure via options versus stock).

## Key Features / Capabilities

- **Backtests Generator** — interactive tool where the user picks an underlying, structure (short put, short strangle, iron condor, calendar, etc.), DTE band, delta selection, and management rule (50% profit take, 21-DTE close, etc.), and ORATS runs the backtest against its historical surface. Results are displayed as equity curves, win rate, average P&L per trade, and distribution of outcomes.
- **The Wheel research** — pre-built backtest of cash-secured puts → covered calls across liquid names, broken down by delta and DTE. Probably the single most-cited ORATS study in the retail premium-selling community.
- **Earnings Effect database** — searchable per-ticker history of implied earnings move vs realised move, post-earnings IV crush magnitude, and the historical edge of selling [[short-strangle|strangles]] or [[iron-condor|iron condors]] into the announcement.
- **Ticker rankings** — daily/weekly tables ordered by IV-rank, IV-percentile, term-structure slope (contango vs backwardation), 30-day skew, and earnings-implied-move. Used as a pre-screen for premium-selling candidates.
- **Long Strangle Backtest** — counterweight study of long-vol structures, useful for context in regime-switching discussions.
- **Calendar Backtest** — calendar performance keyed to entry term-structure slope; the headline finding is that calendars tend to work best entered with a relatively flat or slightly contangoed term structure.
- **Methodology pages** — written explanations of how each study is constructed, what assumptions are made about commissions, slippage, and fills, and where the data comes from.
- **API tie-in** — research metrics (IV rank, term-structure slope, earnings dates, skew) are exposed via the [[orats|ORATS]] API, so the same numbers driving the public research can be consumed programmatically.

## Pricing & Access

- **Free tier** — the research blog, methodology pages, and most published study writeups are free to read at orats.com/research with no login required.
- **Backtests Generator** — gated behind ORATS subscriptions; running custom backtests requires a paid plan. As of June 2026 the consumer **Trading Tools** plan (which includes the Backtester, scanner, and trading tools) lists at ~$99/mo, with discounted ~$49/mo offers running through partner channels (e.g. Elite Trader, Spintwig). The **Delayed Data API** runs ~$49/mo; real-time and enterprise data feeds are priced higher and quoted separately.
- **Live ranked screener** — the daily IV-rank / term-structure / skew ranking tables are part of the broader ORATS platform subscription rather than the free research site.
- **Earnings Effect database** — searchable summaries are partially free; full per-ticker history and the ability to run earnings-strangle backtests sits behind subscription.
- **Enterprise / academic** — custom licensing for funds, prop desks, and academic researchers who want to cite the data in published work.

## Strengths & Weaknesses

**Strengths:**

- **Smoothed IV surface** — backtests run against ORATS' fitted surface avoid the quote-noise pathologies that plague free or scraped retail backtests.
- **Methodology transparency** — assumptions about commissions, mid-fills, and management rules are documented; results are reproducible against the same dataset.
- **Wide adoption** — heavily cited in [[tastytrade]] segments, retail YouTube channels, and options newsletters, so claims sourced to ORATS Research are familiar to most active options traders.
- **Coverage** — 5,000+ optionable US symbols, with history back to 2007 EOD and minute-level Greeks since August 2020.
- **Founder credibility** — Matt Amberson's market-making background informs the choice of metrics and the realism of the cost overlays.

**Weaknesses:**

- **Editorial bias** — like [[tastytrade]], ORATS Research leans short-vol; long-volatility strategies are under-represented and tail-risk scenarios are usually framed as drawdown footnotes rather than central case.
- **In-sample concerns** — many of the named studies cover the post-2007 period, which is heavy on QE and low-rate regimes; out-of-sample robustness across a true rates-up cycle is shorter.
- **US-equity focus** — futures, FX, and international options are not in the research universe.
- **Free tier is teaser-quality** — the most useful tools (Backtests Generator, full Earnings Effect, full ranked tables) require a paid ORATS subscription.
- **Not a substitute for original research** — practitioners should treat the studies as well-constructed null hypotheses, not as turnkey strategies; the canonical cost overlay still misses some regime-specific frictions.

## How Practitioners Use It

A typical premium-selling workflow that incorporates ORATS Research:

1. **Pre-screen the universe.** Pull the daily ranked table for IV-rank ≥ 50, contango term-structure (front IV < back IV), and skew within normal range. Discard names with imminent [[earnings-volatility|earnings]] unless the trade is explicitly an earnings play.
2. **Cross-reference the Earnings Effect database.** For names on the candidate list with earnings within the next 14 days, look up the historical implied-vs-realised move and post-event crush to decide whether to dodge the event or position for the crush.
3. **Validate structure choice with the relevant backtest.** If the plan is to sell a 45-DTE 16-delta [[short-strangle|strangle]] in the candidate name, run the Backtests Generator with those parameters across the past several years to confirm the historical expectancy and drawdown profile.
4. **Use the Wheel research as a comparison benchmark.** For traders running a [[options-premium-selling|premium-selling]] book, the Wheel results function as a "passive index" against which an active strategy's edge can be measured — outperforming the published Wheel curve net of costs is a meaningful bar.
5. **Feed metrics into a [[theta-targeting|theta-targeting]] worksheet.** ORATS' per-name implied-move and 30-day [[volatility-skew|skew]] estimates feed directly into the position-sizing and structure-selection logic of an income-overlay book.
6. **Cite in trade journals and LP reports.** Because ORATS data is research-grade and widely recognised, attributing IV-rank or skew claims to ORATS adds credibility to internal reviews and external communications.

The non-paying user can still extract real value from the free research site as a sanity check — the published equity curves and Earnings Effect summaries are usable as an external validation of in-house backtests built on cheaper data sources like [[polygon-io]] or scraped chains.

## Related

- [[orats]] — the parent platform; ORATS Research is its public face.
- [[cboe-livevol]] / [[livevol]] — institutional alternative on the data side.
- [[optionmetrics]] — academic-grade competitor with deeper history but less retail-friendly research.
- [[tastytrade]] — the firm whose published research methodology most resembles ORATS Research, and whose audience overlaps heavily.
- [[options-premium-selling]] — the strategy class most ORATS studies target.
- [[implied-volatility]] — the smoothed IV surface is the core ORATS asset.
- [[volatility-skew]], [[volatility-term-structure]] — primary ranking metrics in the screener.
- [[earnings-iv-crush]] — the strategy class the Earnings Effect database supports.
- [[theta-targeting]] — feeds into position-sizing using ORATS metrics.
- [[backtesting]] — methodology underpinning every published ORATS study.
- [[the-wheel-strategy]] — strategy whose canonical retail backtest is ORATS' Wheel research.

## Sources

- ORATS Research site (orats.com/research) — methodology pages, published study writeups, ranked screener tables.
- ORATS API documentation (api.orats.io) — defines the metrics surfaced in the research.
- [[tastytrade]] segments and retail options newsletters citing ORATS data (secondary references).
