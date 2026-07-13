---
title: "Reading an ALFRED Report (FAQ)"
type: concept
created: 2026-06-30
updated: 2026-06-30
status: draft
tags: [alfred, fundamental-analysis, valuation, education, methodology]
aliases: ["ALFRED Report FAQ", "ALFRED Verdict FAQ", "How to Read an ALFRED Report", "ALFRED Grades", "ALFRED Scores"]
domain: [fundamental-analysis, valuation]
difficulty: beginner
related: ["[[alfred]]", "[[alfred-report-methodology]]", "[[alfred-fundamental-analysis]]", "[[alfred-investment-philosophy]]", "[[fred-mcnaught]]", "[[fundamental-analysis]]", "[[valuation]]", "[[return-on-equity]]", "[[debt-to-equity]]", "[[price-to-earnings-ratio]]"]
---

A plain-English FAQ for anyone reading an [[alfred|ALFRED]] stock report and wondering *what the ratings actually mean*. ALFRED reports are fundamental-analysis write-ups built on [[fred-mcnaught|Fred McNaught's]] investing framework. This page answers the most common questions about how to interpret them. For the full structural template, see [[alfred-report-methodology]]; for the metric formulas, see [[alfred-fundamental-analysis]].

> ALFRED reports are for information purposes only, not investment advice. Every report restates this; treat the ratings as a structured summary of the data, not a recommendation to buy or sell.

## What is the "ALFRED Verdict"?

The **ALFRED Verdict** is the headline rating grid at the top of every company report. Rather than a single score, it is a **multi-dimensional summary** that separates the question of *what a stock is worth* from *what you should do about it*, because the right action depends on whether you already own the stock. The verdict is **derived from the quantitative analysis** across the whole report — it is a summary of the data, not a standalone opinion.

The five dimensions are:

| Dimension | What it answers | Typical values |
|-----------|-----------------|----------------|
| **VALUATION** | Is the price fair relative to intrinsic value? | Undervalued / Fair Value / Fully Priced / Overvalued |
| **FORECASTS** | How confident is the forward outlook? | Good / Uncertain / Poor |
| **OWNER** | If you already hold it, what now? | Buy More / Hold / Sell |
| **NON-OWNER** | If you're considering it, what now? | Buy / Wait / Avoid |
| **RISK** | How risky is it overall? | Low / Medium / High |

The exact wording can vary slightly from report to report (for example a richly-priced stock may be tagged "Fully Priced" or "Overpriced", and a "Non-Owner: Wait" may appear as "Watchlist"). The *meaning* is consistent — see the [[alfred-reports-overview|reports index]] for how real reports have been rated.

## Why are there separate "Owner" and "Non-Owner" verdicts?

Because the right move depends on your starting position. A stock that has become **Fully Priced** might be a **Hold** for an existing owner (no reason to sell a quality business you already own at a fair price) but a **Wait** for a non-owner (no margin of safety to justify buying in today). Splitting the two prevents the common mistake of treating "don't buy" and "sell" as the same signal.

## What does "Fully Priced" mean — is that the same as "Overvalued"?

No. They are different points on the valuation scale:

- **Undervalued** — the price sits below ALFRED's estimate of intrinsic value; there is a margin of safety.
- **Fair Value** — price roughly matches intrinsic value.
- **Fully Priced** — the price already reflects the company's own fundamentals. Per Fred's definition, **further upside now depends on external factors you can't control** (the commodity price, the macro cycle, sentiment) rather than the company's own results improving. It is "priced for perfection."
- **Overvalued / Overpriced** — the price exceeds what the fundamentals justify on any reasonable assumptions.

The distinction matters: "Fully Priced" is not a sell signal so much as a warning that you are no longer being paid to wait — the easy value has been realised.

## What is the "Poker Hand" in some reports?

Some reports add a **Poker Hand analogy** as a qualitative flavour on top of the numeric verdict — for example "Pocket Jacks" to convey *a strong holding, but not all-in material*. It is a memory aid for the strength-and-conviction of the case, not a separate calculation.

## How does ALFRED assess valuation?

ALFRED triangulates several independent angles rather than trusting one number (see [[alfred-report-methodology]] §Valuation Metrics):

- **[[price-to-earnings-ratio|P/E ratio]]** versus the stock's own history *and* its sector average. A P/E above the sector average implies greater risk (and potentially greater reward) — it becomes a risk-reward judgement, not an automatic "expensive."
- **Discounted cash flow (DCF)** and intrinsic-value estimates — the gold standard, but highly sensitive to assumptions.
- **[[dividend-yield|Dividend yield]]** and franking, compared to benchmarks.

A key nuance from Fred's framework: a **low P/E is not automatically attractive** — it can signal a value trap or structural decline. Valuation is always *relative* — to history, to the sector, and to the quality of the business.

## How does ALFRED assess management?

The **Management Matters** section judges how effectively management turns shareholder capital into profit, primarily through:

- **[[return-on-equity|ROE]]** — return on shareholders' equity. Fred's test: ROE should **comfortably exceed the cash rate**. If management can't earn meaningfully more on your equity than a bank deposit would, they aren't earning their keep. (In one worked review, an ROE of 7% was flagged as a **red flag**.)
- **[[return-on-assets|ROA]]** — return on all assets, debt- and equity-funded.
- **Management compensation, tenure, and insider transactions** — are incentives aligned, and are insiders buying or selling?

A guiding principle from [[alfred-investment-philosophy|Fred's philosophy]]: *when you buy equity, you are buying the management team.*

## How does ALFRED assess financial strength?

The **Financial Strength (Solvency)** section checks whether the company can survive and self-fund, using:

- **[[debt-to-equity|Debt-to-equity (D/E)]]** — leverage. ALFRED's default comfort threshold is D/E below ~0.5, though acceptable levels are industry-dependent.
- **Current ratio and quick ratio** — short-term liquidity (can it cover near-term obligations?).
- **Net interest cover** — how many times operating earnings cover interest payments; below ~1.5 is dangerous, above ~3 is comfortable.
- **Cash on hand and net operating cash flow** — real cash generation, which is harder to manipulate than accounting profit.

## What benchmarks does ALFRED compare a stock against?

ALFRED uses a tiered set of yardsticks rather than absolute pass/fail lines (see [[alfred-report-methodology]] §Benchmarks):

| Benchmark | Role |
|-----------|------|
| **ALFRED defaults** | Standard thresholds: P/E < 20, D/E < 0.5, ROE > 13.4%, current ratio > 2.0, interest cover > 2.0 |
| **Sector average** | Industry-specific comparison (a "high" P/E for a bank differs from a tech firm) |
| **Market average** | A broad baseline (e.g. the ASX average) |
| **Peer group** | Hand-picked competitors with overlapping business segments |

Sectors are organised using the **GICS** classification (11 sectors down to 163 sub-industries), so a stock is always judged against the right peers.

## Does ALFRED give a single letter grade or star rating?

No. ALFRED deliberately uses the **multi-dimensional verdict** (Valuation / Forecasts / Owner / Non-Owner / Risk) rather than collapsing everything into one letter or score. The reasoning, consistent with Fred's philosophy, is that a single grade hides the trade-offs — a stock can be *high quality* yet *fully priced*, or *cheap* yet *high risk*. The grid keeps those tensions visible so you can weigh them against your own situation and time horizon.

## What is the philosophy behind the ratings?

The verdicts encode [[fred-mcnaught|Fred McNaught's]] core axioms (see [[alfred-investment-philosophy]] in full):

- **Two parts to investing:** find the best stocks, then buy them for *less than they are worth*.
- **Value over momentum**, and **know why you buy** — only sell when the reasons you bought have changed.
- **Growth to eat, dividends to sleep** — growth drives appreciation, dividends provide income certainty.
- **Cash is always an asset** — keep reserves to act when the market is pessimistic.

The verdict grid is the structured output of applying these principles to a single company.

## How fresh is the data?

Each report works from the most recent fiscal reports and market data available at the time of writing, and ends with a **Company Calendar** of upcoming reporting dates. Fundamentals are restated every [[earnings-season|earnings season]], so a verdict reflects the picture *as at the report date* — always check the date and the latest results before acting.

## Related

- [[alfred]] — the ALFRED assistant overview
- [[alfred-report-methodology]] — the full report structure and verdict system
- [[alfred-fundamental-analysis]] — metric formulas and a worked example
- [[alfred-investment-philosophy]] — Fred McNaught's axioms behind the ratings
- [[alfred-reports-overview]] — index of real ALFRED reports and their verdicts
- [[fundamental-analysis]] — the broader discipline ALFRED applies
- [[valuation]] — how price relates to intrinsic value
- [[return-on-equity]] / [[debt-to-equity]] / [[price-to-earnings-ratio]] — the core metrics behind the verdict

## Sources

- [[alfred-report-methodology]] and [[alfred-fundamental-analysis]] — the existing ALFRED methodology pages this FAQ summarises.
- [[alfred-investment-philosophy]] — Fred McNaught's documented investing axioms and verbal benchmarks.
