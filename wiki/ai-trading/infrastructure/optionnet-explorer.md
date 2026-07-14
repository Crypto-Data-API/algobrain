---
title: "OptionNet Explorer (ONE)"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [options, backtesting, risk-management, company]
entity_type: company
headquarters: "United Kingdom"
website: "https://www.optionnetexplorer.com"
aliases: ["ONE", "OptionNet", "OptionNet Explorer"]
related:
  - "[[tastytrade-platform]]"
  - "[[thinkorswim]]"
  - "[[options-premium-selling]]"
  - "[[portfolio-greeks-aggregation]]"
  - "[[theta-targeting]]"
  - "[[vega-budgeting]]"
  - "[[backtesting]]"
  - "[[implied-volatility]]"
---

OptionNet Explorer (universally abbreviated **ONE**) is a Windows desktop options analytics application aimed at serious retail and small-shop professional options traders who need a richer planning, [[backtesting|backtest]], and position-monitoring environment than what their broker provides. ONE's distinguishing capabilities are its **time-and-price P&L grids** (visualising portfolio P&L across underlying-price and date axes simultaneously), portfolio-level [[portfolio-greeks-aggregation|Greeks aggregation]] across multiple underlyings, and a historical-data-driven simulator that can replay any options trade against actual end-of-day chains stretching back over a decade. It sits in the price-and-feature gap between free broker tooling (e.g. [[thinkorswim]]) and institutional platforms like Cboe LiveVol Pro.

## Overview

ONE is published by OptionNet Limited (UK) and has been a fixture of the [[options-premium-selling|premium-selling]] community since the early 2010s. The software is Windows-only desktop (with workarounds for Mac via virtualisation) and is purchased on a subscription basis with a permanently installed local client. ONE's core value proposition is that it does not need to be connected to a broker to be useful — its primary job is **planning and replaying trades** against historical EOD options data, not executing them.

The platform is most associated with the tastytrade-style discretionary income trader who runs a portfolio of [[iron-condor|iron condors]], [[short-strangle|strangles]], [[calendar-spread|calendars]], and [[butterfly|butterflies]] across SPX, RUT, and large-cap names. ONE's strength is letting that trader visualise the entire book's P&L surface, stress-test it across IV and spot moves, and **walk a hypothetical position day by day** through actual historical price action to see how the position would have evolved.

ONE bundles a multi-year historical options database covering optionable US equities and indices — the vendor states the data is at **5-minute intervals** (early versions were more EOD-centric) — which is what enables the historical replay and backtest features without requiring a separate data subscription. Live data integration is supported but optional. The product remains actively sold and maintained as of June 2026.

## Key Features / Capabilities

- **Time-and-price P&L grid** — the signature feature. A 2D matrix where rows are dates (today through expiration) and columns are underlying price levels, with each cell showing the projected portfolio P&L. The grid lets the trader see at a glance how the position behaves across both axes — vital for [[calendar-spread|calendars]], [[diagonal-spread|diagonals]], and other multi-expiration structures where time and price interact non-trivially.
- **Portfolio Greeks aggregation** — sum of delta, gamma, theta, vega, and rho across all positions in the loaded book, with the ability to subset by underlying, expiration, or strategy tag. Beta-weighting to a benchmark (typically SPX) is supported.
- **Historical simulator / backtester** — pick a structure (e.g. 45-DTE 16-delta SPX iron condor), pick a start date, and the simulator replays the trade day-by-day against actual historical chains, applying configurable management rules (close at 50% profit, manage at 21 DTE, roll on touch, etc.). Outputs include equity curve, win rate, average P&L, max drawdown, and the per-trade ledger.
- **Position tracker / monitor** — load real or hypothetical positions and update them with current or end-of-day prices; ONE recomputes Greeks, P&L, and the time-and-price grid in real time.
- **Multi-leg strategy builder** — interactive chain interface for constructing verticals, condors, strangles, calendars, diagonals, butterflies, ratios, and arbitrary custom structures.
- **What-if scenarios** — overlay hypothetical IV shifts (parallel surface moves), spot moves, and date advances on the existing book to project Greeks and P&L under stress.
- **Trade log / journal** — tag, annotate, and review past trades with the same time-and-price grid the live tool uses.
- **Volatility surface display** — view IV by strike and expiry, with skew and term-structure overlays. Less polished than LiveVol Pro or orats but adequate for retail planning.
- **Multiple "tabs" / sandboxes** — keep separate working books for live positions, paper trades, and backtest scenarios in parallel.

## Pricing & Access

Published pricing as of 2025-2026 (OptionNet Limited is UK-based; prices in GBP, VAT extra):

- **Quarterly subscription** — **£150 + VAT** per quarter (~$50-65/month equivalent depending on FX).
- **Annual subscription** — **£500 + VAT** per year (saves £100 vs paying quarterly).
- **Trial** — a fully functional **10-day trial** is available for **£10**.
- **Historical data** — multi-year options history (5-minute intervals per the vendor) for optionable US equities and indices is included in the standard subscription.
- **Platform** — Windows desktop only (minimum ~4GB RAM, 500MB disk); Mac users run it under Parallels, VMware Fusion, or a Windows VM.
- **Live data** — optional integration with broker feeds for real-time chains; live quotes are not strictly required for the planning and backtest workflow.
- **No mobile / web client** — ONE is a single-user, single-machine desktop tool.

This pricing places ONE between free broker tooling (where the [[thinkorswim]] analyse tab and the [[tastytrade-platform|tastytrade]] curve view are sufficient for many traders) and institutional analytics (where Cboe LiveVol Pro starts at several times the price).

## Strengths & Weaknesses

**Strengths:**

- **Time-and-price grid** is genuinely unique — no free broker tool exposes the time/price P&L surface in the same readable form.
- **Historical replay** allows realistic, actual-data backtests of management rules without writing code.
- **Aggregates across underlyings** — the portfolio view sums Greeks across heterogeneous symbols, which most broker analyse tools do not.
- **Affordable for retail** — the price point is reachable for serious individual traders (£500 + VAT/year on the annual plan, roughly $650–$800 all-in) compared to the multi-thousand-per-month institutional alternatives.
- **Discretionary-trader-friendly** — workflow is designed around how a human plans and reviews trades, not around an API.
- **Strong community** — heavy adoption among [[options-premium-selling|premium-selling]] educators (Sheridan Mentoring, SMB, OptionAlpha-adjacent traders); shared backtest screenshots and configurations are common.

**Weaknesses:**

- **Windows-only** — Mac and Linux users must virtualise.
- **Single-user desktop** — no cloud sync, no multi-device, no team collaboration.
- **5-minute data resolution ceiling** — historical chains are at 5-minute intervals, so backtests against tick or sub-minute data are not possible; for tick-level work, orats, livevol, or raw [[databento]] data are better.
- **UI is dense** — the steep first-week learning curve is a common complaint; the time-and-price grid in particular takes practice to read fluently.
- **No execution layer** — ONE is analytics only; trades must be entered in the broker platform separately, which means double entry and the risk of position drift between ONE and the broker of record.
- **No API / scriptability** — strategies are defined through the UI; users wanting programmatic backtests should look at orats' Backtests Generator or build their own tooling on [[polygon-io]] / [[databento]] data.
- **Limited international coverage** — US options focus.

## How Practitioners Use It

A representative workflow for a discretionary [[options-premium-selling|premium seller]]:

1. **Plan a new position.** Pick the underlying and structure (e.g. 45-DTE 1-SD [[short-strangle|short strangle]] on SPX). Build it in ONE's strategy builder; inspect the time-and-price grid to confirm the P&L behaviour around the expected move and through expiration.
2. **Stress-test it.** Apply a +5 IV-point shock and a -3% spot move simultaneously; check that the worst-case P&L is within the [[vega-budgeting|vega budget]] and overall risk tolerance.
3. **Backtest the structure.** Run the same structure with the same management rules (50% profit take, 21-DTE close) over the past 5 years on the same underlying. Inspect the equity curve, win rate, and worst drawdown to set expectations and decide on sizing.
4. **Open the trade in the broker.** Execute in [[thinkorswim]], [[tastytrade-platform]], or interactive-brokers — ONE does not execute.
5. **Mirror the live position into ONE.** Load the actual fill into ONE's position tracker so the time-and-price grid and Greeks reflect the real book.
6. **Daily monitoring.** Update prices end-of-day; review the aggregated portfolio Greeks (sum of theta, vega, gamma across all positions) against [[theta-targeting|theta targets]] and [[vega-budgeting|vega budgets]]. The time-and-price grid is consulted to decide whether to roll, manage, or close.
7. **Post-trade review.** When a trade closes, review the historical playback in ONE to see how the position evolved and what the outcome would have been under alternative management rules. Lessons feed back into the rule set.
8. **Periodic strategy research.** Use the simulator to test variants — different deltas, different DTE, different profit-take thresholds — over rolling historical windows.

For a small advisory or family-office shop running discretionary options income, ONE is often the **single most important piece of analytical software** in the workflow, paired only with the broker platform and a market-data terminal. For purely systematic shops it is less central; programmatic backtests on orats or LiveVol data are the better fit.

## Related

- [[tastytrade-platform]] — broker-native analytics with a good "curve" view and Probability of Profit but weaker portfolio aggregation.
- [[thinkorswim]] — broker-native analyse tab; closer to ONE in feature scope but tied to the broker.
- [[options-premium-selling]] — the strategy class ONE most directly supports.
- [[portfolio-greeks-aggregation]] — ONE is one of the canonical retail tools for this.
- [[theta-targeting]] — ONE's portfolio Greeks view is consumed in this workflow.
- [[vega-budgeting]] — same.
- [[backtesting]] — ONE's historical simulator is the backbone of strategy validation for discretionary retail.

## Sources

- OptionNet Explorer product website — https://www.optionnetexplorer.com (feature documentation, pricing, supported underlyings).
- OptionNET Explorer User Guide — https://help.optionnetexplorer.com/
- DayTrading.com, "OptionNet Explorer Review" — https://www.daytrading.com/optionnet-explorer
- Options Trading IQ, "OptionNet Explorer Review 2025 — Complete Guide" — https://optionstradingiq.com/optionnet-explorer/
- Bullish Bears, "OptionNet Explorer Review (2026): Features, Pricing & Tools" — https://bullishbears.com/optionnet-explorer-review/
- SteadyOptions, "OptionNET Explorer (ONE) — Options Backtesting Software" — https://steadyoptions.com/articles/optionnet-explorer-one-options-backtesting-software-r743/
- Sheridan Mentoring and SMB Capital published case studies that demonstrate ONE workflows.
- Retail options education community references (Tastylive, OptionAlpha, Capital Discussions forums).
- Pricing (£150+VAT/quarter, £500+VAT/year, £10 trial), Windows-only requirement, and 2026 active status verified via web search, 2026-06-10.
