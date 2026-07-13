---
title: "Value: The Four Cornerstones of Corporate Finance — Koller, Goedhart, Wessels (2010)"
type: source
created: 2026-04-15
updated: 2026-04-28
status: good
tags: [book, education, fundamental-analysis, valuation, corporate-finance]
source_type: book
source_author: "Tim Koller, Marc Goedhart, David Wessels (McKinsey & Company)"
source_date: 2010
confidence: high
aliases: ["Value Four Cornerstones", "McKinsey Value", "Value Koller"]
related:
  - "[[valuation]]"
  - "[[discounted-cash-flow]]"
  - "[[fundamental-analysis]]"
  - "[[return-on-invested-capital]]"
  - "[[value-investing]]"
  - "[[free-cash-flow]]"
  - "[[wacc]]"
  - "[[economic-profit]]"
---

## Overview

**Value: The Four Cornerstones of Corporate Finance** by Tim Koller, Marc Goedhart, and David Wessels (McKinsey & Company), published in 2010, is the executive-friendly companion to McKinsey's longer institutional textbook *Valuation: Measuring and Managing the Value of Companies* (now in its 7th edition, 2020). Where the longer book is a 900-page reference for analysts and bankers, *Value* is a 250-page argument aimed at CEOs, CFOs, and senior managers about what really creates economic value — and what only appears to.

The "four cornerstones" framework:

1. **The core of value is [[return-on-invested-capital|ROIC]] and growth.** Value is created when a company invests capital at returns above its [[wacc|cost of capital]], and the magnitude of value creation scales with growth — but only if ROIC > WACC. Growth at returns below cost of capital destroys value.

2. **The conservation of value.** Restructurings, capital structure changes, accounting choices, and financial engineering don't create value unless they change the underlying cash flows or risk profile. EPS-accretive deals can be value-destroying; share buybacks don't create value out of thin air.

3. **The expectations treadmill.** Stock price moves on changes in *expectations*, not on absolute performance. A company beating its own targets but missing market expectations underperforms. CEOs who manage to expectations rather than to value get whipsawed.

4. **Best owners.** A given asset is worth different amounts to different owners depending on synergies, capabilities, and capital structure. Value is created when assets move to their best owners (M&A, divestitures, spin-offs).

## Key Takeaways

- **ROIC vs. WACC is the central question.** Companies earning ROIC above WACC create value; those earning below destroy it. Growth multiplies whichever direction you're going. Most CEO/board attention goes to growth; the more important question is the ROIC differential.
- **Accounting earnings are not cash flows.** Net income includes non-cash charges, capitalized vs. expensed choices, and accruals. [[free-cash-flow]] is what investors actually receive and is the right basis for valuation.
- **DCF is the only economically correct valuation methodology.** Multiples (P/E, EV/EBITDA) are shortcuts that work when the comparables are truly comparable. They fail when companies differ in growth, ROIC, risk, or capital structure.
- **Buybacks don't create value mechanically.** A buyback creates value only if shares are repurchased below intrinsic value. Buying back overvalued shares destroys value. EPS accretion is mechanical and irrelevant.
- **EPS-accretive M&A often destroys value.** Issuing low-multiple debt to buy a high-multiple company increases EPS but doesn't create value. The premium paid + integration costs + synergy execution all matter; EPS accretion is a vanity metric.
- **Capital structure has second-order effects.** The Modigliani-Miller theorems hold approximately: capital structure mostly redistributes risk between shareholders and bondholders rather than creating value. Tax shields and bankruptcy costs create modest exceptions.
- **Diversified conglomerates trade at a discount for a reason.** Markets pay a premium for focused businesses with clear ROIC profiles. Conglomerate structures destroy value when capital allocation is internal and opaque.
- **Communication and transparency matter.** CEOs who clearly communicate their value-creation thesis and stick to it outperform those who manage to short-term EPS targets.

## Who Should Read This

Investors, analysts, and corporate executives who want to think clearly about what creates economic value vs. what creates accounting illusions. The book is short (~250 pages) and accessible to readers with basic finance background — the audience is intelligent generalists, not specialists.

For analysts who want the operational depth (multi-stage DCF, terminal value calibration, peer benchmarking, restructuring), the longer companion *Valuation* (Koller, Goedhart, Wessels) is the go-to reference.

## How It Applies to AI Trading

The four-cornerstones framework is the conceptual foundation of fundamental quant equity factor design:

1. **ROIC and growth as factors.** Quality factors (gross profitability, operating margin, asset turnover) and growth factors (revenue, earnings, FCF growth) are measurable proxies for the ROIC × growth combination Koller emphasizes. A quality-growth screen is a Koller-style screen.
2. **Cash-flow-based valuation factors.** [[discounted-cash-flow|DCF]]-derived intrinsic-value-to-price ratios outperform simpler P/E-based value factors in academic research. Building DCF-based value signals at scale is a current frontier in systematic equity.
3. **Expectations vs. realizations.** The "expectations treadmill" maps directly onto [[earnings-revisions]] and [[post-earnings-announcement-drift]] strategies. Stocks beat or miss expectations, and prices move on the surprise.
4. **Best-owners thinking and M&A arbitrage.** [[merger-arbitrage]] and spinoff/divestiture strategies operationalize Koller's "best owner" cornerstone.

For long-term fundamental investors using LLMs to analyze 10-Ks, the Koller framework gives the LLM a structured prompt: classify a company by its ROIC vs. WACC, growth, capital structure, and best-owner status — and value follows.

## Editions

- **1st edition (2010)** — Original; cited above
- **Companion: *Valuation* (1st edition 1990, 7th edition 2020)** — The McKinsey institutional textbook; vastly more detail on DCF, multiples, restructuring, M&A modeling

## Rating

**8/10** — Clear, principled, and short. The four-cornerstones framework is genuinely useful as a mental model. Pair with *Valuation* for operational depth and with [[the-intelligent-investor|The Intelligent Investor]] for the broader value-investing tradition.

## Sources

- Koller, Tim; Goedhart, Marc; and Wessels, David (2010). *Value: The Four Cornerstones of Corporate Finance*. McKinsey & Company / Wiley.

## Related

- [[valuation]] — The discipline
- [[discounted-cash-flow]] — The methodology Koller advocates
- [[fundamental-analysis]] — The broader investment approach
- [[return-on-invested-capital]] — Core metric
- [[value-investing]] — The Graham-Dodd tradition
- [[free-cash-flow]] — The cash-flow basis for valuation
- [[wacc]] — Weighted average cost of capital
- [[economic-profit]] — ROIC × invested capital - WACC × invested capital
- [[the-intelligent-investor]] — Companion classic on value investing
- [[security-analysis]] — Graham-Dodd foundational text
