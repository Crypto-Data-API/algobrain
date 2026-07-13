---
title: "Chris Quill"
type: entity
created: 2026-04-07
updated: 2026-05-07
status: good
tags: [traders, person, itpm, quantitative, options, volatility, indicators]
entity_type: person
aliases: ["Christopher Quill"]
related: ["[[anton-kreil]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[options]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[long-vol-vs-short-vol]]", "[[raj-malhotra]]"]
---

Chris Quill is the Research and Quantitative Analyst at the Institute of Trading and Portfolio Management and a Senior Trading Mentor. He is the lead instructor for ITPM's Professional Options Trading Masterclass (POTM 2.0), co-teaches the Professional Trading Masterclass (PTM) alongside [[anton-kreil]], and is the ITPM mentor most associated with the quantitative side of the curriculum — particularly the [[realized-volatility|realized]] vs. [[implied-volatility]] gap as a tradable signal (Source: [[itpm-education-methodology-overview]]).

## Background

Quill's role at ITPM is unusual among the mentoring staff: he is positioned explicitly as the *research and quantitative* partner to a faculty otherwise dominated by former sell-side discretionary traders. He is responsible for the data work that backs ITPM's published methodology — vol calculations, options-curriculum design, and the empirical case studies used in mentor calls.

His most public-facing teaching artefacts are:

- **POTM 2.0 — Professional Options Trading Masterclass.** A "doubled in size, remastered" rebuild of ITPM's options program, designed to take students from directional equity setups to options-structured expressions of those views with explicit Greek and vol-regime control (Source: [[itpm-education-methodology-overview]]).
- **"How to Calculate Realized & Implied Volatility and Why It's Important"** — a free ITPM presentation that walks retail traders through the actual arithmetic of computing [[realized-volatility]] on the right window and comparing it to current [[implied-volatility]] to identify mispricings.
- **"Chinese Year of the Slaughtered Pig"** — a premium presentation on the macro / single-stock landscape framed around the Chinese zodiac year, used as a vehicle for top-down regime calls and concrete trade ideas.
- **Trading Legends interviews.** Quill himself conducted at least one Trading Legends interview (with David Perlin), in addition to being a frequent contributor to ITPM's longer-form video content.

## The Realized-vs-Implied Volatility Methodology

The core quantitative workflow Quill teaches is the [[realized-volatility|realized]] vs. [[implied-volatility]] gap. The shape of the workflow, reconstructed from the ITPM curriculum (Source: [[itpm-education-methodology-overview]]):

### 1. Compute realized vol on the right window

- Use the standard close-to-close log-return method: take daily log returns over a chosen lookback window, compute the standard deviation, annualize by multiplying by the square root of the number of trading periods (typically 252 for daily data).
- Window choice matters: a 20-day window captures recent regime; 60-day smooths into longer-term character; 252-day approximates the long-run vol of the name. For options work, the window should roughly match the [[expected-move|expected holding period]] of the position, which in the ITPM framework is 20-60 days.

### 2. Read implied vol off the chain

- Pull the [[implied-volatility]] of the [[at-the-money]] option for the relevant expiry, or use a vendor's 30-day constant-maturity IV series. Make sure the IV is measured against a comparable horizon to the realized window — comparing 5-day RV to 90-day IV produces noise.

### 3. Compute the gap

- The signal is `IV − RV`. When implied is materially above realized, the [[volatility-risk-premium]] is wide and selling premium has a structural tailwind (with caveats below). When implied is below realized, options are *cheap* relative to what the underlying is actually doing — the long-vol side is favoured.
- Sign and magnitude both matter. A two-vol-point gap is noise; a ten-vol-point gap with a clear regime story behind it is the kind of setup the methodology is designed to find.

### 4. Filter by regime

- The gap is not always tradable. A wide IV-RV spread on the eve of an earnings report or [[fomc-meetings|FOMC]] decision reflects a known catalyst, not a mispricing — selling the spread is selling tail risk for a small premium.
- The methodology pairs the quantitative gap with a qualitative filter on what catalysts are pending and what the [[long-vol-vs-short-vol]] regime is. This is where Quill's quantitative work meets [[raj-malhotra]]'s vol-regime framing and Kreil's macro overlay.

## Volatility as an Edge — When the Gap Is Tradable

Quill's curriculum is explicit that the realized-vs-implied gap is a *conditional* edge, not a constant one. The gap is tradable when:

- The pricing reflects an inefficiency rather than a known event (no upcoming catalyst large enough to justify the IV)
- The underlying's [[realized-volatility]] regime is stable or mean-reverting, not in the middle of a structural break
- The position can be sized so that a single adverse realization does not break the [[risk-of-ruin|risk budget]]

It is *not* tradable — and is in fact a trap — when:

- A catalyst is imminent and the IV is the market's price for that catalyst
- The name has a [[options-concentration-risk|liquidity / float / borrow]] regime that makes the option chain non-representative (cf. gamestop in early 2021)
- The trader cannot articulate the *fundamental* reason the IV is wrong, only the statistical observation

This is the structural reason ITPM teaches the vol gap *inside* the broader [[itpm-five-principles|fundamental-first]] framework rather than as a standalone systematic edge.

## "Chinese Year of the Slaughtered Pig"

Quill's macro-framing premium presentation uses the Chinese zodiac year as a narrative device for a top-down market thesis — a regime call mapped onto specific equity and options trade structures. The format mirrors ITPM's broader top-down approach: macro view → sector view → name view → options structure, with the vol-regime overlay applied at the structure step.

The presentation is also one of the cleanest worked examples of how Quill integrates his quantitative work into the [[itpm-trading-philosophy|ITPM philosophy]] — fundamentals dictate direction, vol math dictates whether to express the view through stock, long options, short options, or spreads.

## Quantitative vs. Discretionary Perspective

Quill's role at ITPM is best understood by contrast:

| Mentor | Lens | Default question |
|---|---|---|
| [[anton-kreil]] | Buy-side fundamental discretionary | "What is the long-short structure that fits this macro view?" |
| [[raj-malhotra]] | Sell-side options market-maker | "What [[volatility]] regime are we in, and which side of vol pays me?" |
| **Chris Quill** | **Research / quantitative** | **"What does the realized-vs-implied gap say, and is the gap a real edge or a known catalyst?"** |
| [[edward-shek]] | EM / cross-region equity | "Where is the cross-market [[correlation]] mispricing?" |

Quill's perspective complements Kreil's discretionary fundamental view by providing the empirical anchor — the actual numbers that say whether an option structure is paying enough for the risk. Where Kreil might describe a setup qualitatively, Quill's job is to compute whether the math agrees.

## Lessons for Options Traders

Specific operational lessons from Quill's published material that retail options traders consistently get wrong:

1. **Most retail traders underestimate implied vol.** They look at option prices and compare them to recent stock moves, not to forward-looking [[implied-volatility]]. The result: they buy options that look "cheap" the day after a quiet week and watch them decay.
2. **[[realized-volatility]] is not a number — it is a window choice.** The same name can show 18% RV on a 20-day window and 32% on a 5-day window. Pick the window that matches your holding period.
3. **The vol surface tells you what the market expects.** Skew, term structure, and the relative pricing of [[at-the-money]] vs. wing options all encode forecasts. Reading the surface is the options-specific analogue to reading order flow in equities. See [[options-portfolio-construction]] and [[vega-budgeting]] for how ITPM operationalizes this.
4. **Vol mispricings shrink as the catalyst approaches.** If you see a wide gap two months out, it often closes well before expiry as the market re-prices. Trades sized for "hold to expiry" miss most of the move.
5. **Selling premium is not free money.** The [[volatility-risk-premium]] is real on average, but the realized distribution has a long left tail. Sizing must reflect tail risk, not the median outcome.

## Trading Relevance

Quill's work is most relevant for:

- Options traders who want to move from "buy calls when bullish" to actually pricing the structure they take
- Retail traders trying to understand why their long-premium strategies have bled in low-vol regimes (answer: they were paying for IV that exceeded subsequent RV)
- ITPM students who have completed PTM and are progressing into POTM 2.0
- Anyone building an [[options-portfolio-construction|options portfolio]] who needs an explicit vol-budget framework rather than ad-hoc strike selection

## Sources

- (Source: [[itpm-education-methodology-overview]]) — ITPM mentor profile, POTM 2.0 curriculum, methodology framework
- (Source: [[itpm-trading-legends-raj-malhotra]]) — context on how Quill's quantitative vol work fits with Malhotra's regime framework
