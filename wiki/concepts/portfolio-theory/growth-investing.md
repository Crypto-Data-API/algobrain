---
title: Growth Investing
type: concept
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags:
  - portfolio-theory
  - fundamental-analysis
  - valuation
aliases:
  - growth-stocks
  - Growth Stocks
  - Growth Stock
  - growth-strategy
  - Growth Investing
domain: [portfolio-theory]
prerequisites: ["[[fundamental-analysis]]", "[[valuation]]"]
difficulty: beginner
related: ["[[value-investing]]", "[[value-vs-growth-investing]]", "[[growth-investing-strategy]]", "[[momentum]]", "[[value-factor]]"]
---

# Growth Investing

Growth investing is an equity style that buys companies whose revenue and earnings are expanding far faster than the market average, accepting elevated valuation multiples (high P/E, P/S, EV/Sales) on the thesis that rapid compounding of the business will more than justify the premium paid today. It is the natural counterpart to [[value-investing]] -- where value buys cheapness relative to current fundamentals, growth pays up for future fundamentals -- and the two together form the principal axis of the [[value-factor|value/growth factor]] spectrum. For systematic strategy implementation, see [[growth-investing-strategy]].

## Key Metrics

Growth investors evaluate companies using metrics that emphasize expansion over current cheapness:

- **Revenue growth rate**: Year-over-year top-line growth, often looking for 20%+ annually.
- **PEG ratio** ([[peg-ratio|Price/Earnings to Growth]]): Divides the P/E ratio by the earnings growth rate. A PEG below 1.0 suggests the stock may be undervalued relative to its growth.
- **Total addressable market (TAM)**: Growth investors favor companies attacking large markets with low penetration.
- **Gross margins**: High and expanding margins suggest pricing power and scalability.

The table contrasts what a growth investor screens for against the value style on the other side of the [[value-factor|value/growth]] axis:

| Metric | Growth tilt | Value tilt | What it signals |
|--------|-------------|------------|-----------------|
| Revenue growth (YoY) | 20%+ | Single digits OK | Demand and runway |
| P/E ratio | High (30–100+) | Low (< 15) | Premium paid for future earnings |
| [[peg-ratio\|PEG ratio]] | Watched; < 1.0 = cheap growth | Often not applicable | Valuation relative to growth |
| P/S (price/sales) | High (10–30 for SaaS) | Low | Useful for pre-profit firms |
| Gross margin | High and expanding (70%+ for software) | Stable | Pricing power, scalability |
| Dividend yield | Usually 0% (reinvests) | Higher | Capital-return policy |
| Rule of 40 (SaaS) | growth% + margin% ≥ 40 | n/a | Growth-vs-profitability balance |

### Worked Example: PEG Ratio

A software company trades at a P/E of 45 and is growing earnings 30% per year. Its [[peg-ratio|PEG]] = 45 / 30 = **1.5**. A pure value screen would reject a 45× P/E outright, but the PEG of 1.5 reframes it: you are paying 1.5× the growth rate. A competitor at P/E 60 growing 50% has PEG = 60/50 = **1.2** — *cheaper* on a growth-adjusted basis despite the higher headline multiple. A PEG below 1.0 (e.g., P/E 25 growing 30% → 0.83) is the classic "growth at a reasonable price" ([[garp|GARP]]) sweet spot. The caveat: PEG is only as good as the forward-growth estimate, which is exactly where growth theses most often break.

## Growth vs Value Investing

Growth and [[value-investing]] represent opposite ends of the investing spectrum. Value investors buy cheap stocks trading below intrinsic value; growth investors pay premium valuations for companies expected to grow into (and beyond) their prices. The debate over which approach is superior is one of the longest-running in finance. See [[value-vs-growth-investing]] for a detailed comparison.

Historically, value outperformed growth from the 1920s through the early 2000s (the [[value-factor|value premium]] documented by Fama and French). However, growth stocks -- particularly mega-cap tech -- dominated from 2010 through 2021, driven by low interest rates and digital transformation. The relationship is **cyclical**, not permanent: leadership rotates with the macro regime, and the relative outperformance can persist for a decade in either direction before reverting, which is why style timing is so difficult.

| Era | Leader | Driver |
|-----|--------|--------|
| 1920s–1990s | Value (broadly) | Mean-reversion, mispricing of "boring" cash generators |
| Late 1990s | Growth | Dot-com mania (ended in the 2000–02 bust) |
| 2000–2007 | Value | Post-bubble reversion, commodities cycle |
| 2010–2021 | Growth | [[zero-interest-rate-policy\|Zero rates]], FAANG/mega-cap tech, digital transformation |
| 2022 | Value | Rate-hiking cycle crushed long-duration growth |
| 2023–2024 | Growth (AI mega-caps) | The "Magnificent Seven," AI capex theme |

### Quality-Growth and GARP

Not all growth is equal. **Quality-growth** investors (e.g., Terry Smith, the Nifty Fifty thesis in its sound form) demand that rapid growth be accompanied by high return on capital, durable competitive moats, and self-funding cash flow — avoiding the cash-burning, story-driven names that dominate speculative growth manias. **[[garp|GARP]]** (growth at a reasonable price), associated with Peter Lynch, blends the two styles by buying growth only when the [[peg-ratio|PEG]] is reasonable, sitting deliberately between pure growth and pure [[value-investing]].

## Interest-Rate Sensitivity and the Duration Analogy

Growth stocks behave like long-duration assets. Because the bulk of their expected cash flows lie far in the future, their present value is acutely sensitive to the discount rate: when the [[risk-free-rate]] rises, the denominator in a [[dcf-analysis|discounted cash flow]] grows and distant earnings are discounted more heavily, compressing growth multiples disproportionately. This is why the 2022 rate-hiking cycle hit unprofitable, long-dated growth names (ARK-style innovation, recent IPOs) far harder than cash-generative value stocks -- a textbook display of the "long-duration equity" dynamic. Conversely, the 2010-2021 era of [[zero-interest-rate-policy|zero rates]] flattered growth valuations.

## Portfolio Relevance

In a factor framework, the growth/value axis is one of the canonical equity style tilts (see [[value-factor]]). A portfolio's net exposure can be measured as a value-minus-growth factor loading, and managers deliberately tilt the book toward growth in disinflationary, falling-rate, secular-innovation regimes and toward value in rising-rate, late-cycle, inflationary regimes. Because growth and value tend to be negatively correlated in their relative performance, blending the two ([[diversification|style diversification]]) smooths the equity sleeve of a portfolio. Growth's higher volatility and drawdown profile also means its [[geometric-mean|geometric (compounded) return]] can lag its headline arithmetic return more than value's -- a consideration for long-horizon compounding.

## Risks and Pitfalls

- **Valuation / multiple-compression risk.** The entire thesis rests on paying a premium that future growth will justify. If growth merely *decelerates* (not even reverses), the high multiple can compress violently — a stock can fall 50% while earnings still rise. This is the dominant risk in growth investing.
- **Long-duration interest-rate sensitivity.** As detailed below, growth multiples are acutely sensitive to the [[risk-free-rate]]; a rising-rate regime is structurally hostile (see the 2022 drawdown).
- **Growth-trap / story stocks.** Companies that perpetually "grow into" a valuation that never arrives — burning cash on the promise of future scale. The 2021 SPAC and unprofitable-tech cohort is the cautionary cohort.
- **Crowding and momentum unwinds.** Growth and [[momentum]] overlap heavily; when a crowded growth/momentum trade unwinds, the same names sell off together, raising correlation exactly when diversification is wanted.
- **Forecast fragility.** Every growth valuation embeds a forward-growth estimate. Analysts systematically over-extrapolate recent growth, so the [[peg-ratio|PEG]] and DCF inputs are biased optimistic.
- **Volatility drag on compounding.** Growth's higher volatility means its [[geometric-mean|geometric (compounded)]] return can lag its arithmetic return by more than value's — a real cost over long holding periods.

## How Investors Use Growth Investing

- **As a style sleeve / factor tilt.** Allocate a deliberate portion of the equity book to growth (via factor ETFs or stock selection) and measure the net value-minus-growth loading; rebalance the tilt as the macro regime shifts.
- **GARP screening.** Combine a growth screen (revenue/earnings acceleration) with a valuation gate ([[peg-ratio|PEG]] < 1.5, reasonable P/S) to avoid the most speculative names.
- **Style diversification.** Pair a growth sleeve with a [[value-investing|value]] sleeve; because their *relative* performance is roughly negatively correlated, the blend smooths the equity ride (see [[diversification]]).
- **Regime-aware timing.** Lean into growth in disinflationary, falling-rate, secular-innovation regimes; lean toward value in rising-rate, inflationary, late-cycle regimes — accepting that such timing is hard and often wrong.

## Famous Growth Investors

- **Peter Lynch**: Managed Fidelity Magellan Fund, achieving 29% annual returns over 13 years (Source: [[book-one-up-on-wall-street]]). Coined the term "ten-bagger" for stocks that return 10x.
- **Cathie Wood**: Founder of ARK Invest, known for concentrated bets on disruptive innovation (Tesla, genomics, AI). Her ARK Innovation ETF gained over 150% in 2020 before declining sharply in 2022.
- **Philip Fisher**: Author of *Common Stocks and Uncommon Profits*, pioneered qualitative growth analysis through his "scuttlebutt" method (Source: [[book-common-stocks-and-uncommon-profits]]).
- **CANSLIM** (William O'Neil): A systematic growth screening method that combines Current earnings, Annual earnings, New products, Supply/demand, Leader/laggard, Institutional sponsorship, and Market direction (Source: [[book-how-to-make-money-in-stocks]]).

## Sources

- [[book-one-up-on-wall-street]] — Lynch's practical guide to finding growth stocks in everyday life; origin of the GARP/PEG framing
- [[book-common-stocks-and-uncommon-profits]] — Fisher's pioneering qualitative growth analysis framework
- [[book-how-to-make-money-in-stocks]] — O'Neil's systematic CANSLIM approach to growth stock selection
- General market knowledge for the growth-vs-value cycle and interest-rate/duration framing; no further specific wiki source ingested yet.

## Related

- [[growth-investing-strategy]]
- [[value-vs-growth-investing]]
- [[value-investing]]
- [[fundamental-analysis]]
- [[momentum]]
- [[peg-ratio]] — the core growth-adjusted valuation metric
- [[garp]] — growth at a reasonable price, the value/growth hybrid
- [[value-factor]] — the factor spectrum growth sits on
- [[dcf-analysis]] — why long-dated cash flows make growth rate-sensitive
- [[geometric-mean]] — the compounding cost of growth's higher volatility
