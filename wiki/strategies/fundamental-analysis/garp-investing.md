---
title: "GARP (Growth at a Reasonable Price)"
type: strategy
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, momentum, stocks, position-trading]
aliases: ["GARP", "Growth at a Reasonable Price", "GARP Investing", "GARP Strategy"]
strategy_type: fundamental
timeframe: position
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[growth-investing-strategy]]", "[[value-investing-strategy]]", "[[value-vs-growth-investing]]", "[[peg-ratio]]", "[[peter-lynch]]", "[[quality-factors]]", "[[momentum-value-combination]]", "[[return-on-equity]]", "[[free-cash-flow]]", "[[fundamental-analysis]]"]
---

# GARP (Growth at a Reasonable Price)

GARP — **G**rowth **A**t a **R**easonable **P**rice — is a hybrid equity style that sits between [[value-investing-strategy|value]] and [[growth-investing-strategy|growth]] investing. A GARP investor wants companies that are genuinely growing earnings, but refuses to pay the sky-high multiples that pure growth investors will accept. The goal is to capture most of growth's upside while keeping a [[value-investing-strategy|value-style]] discipline on the price paid, so the position is not wiped out if growth slows and the multiple compresses. The approach is most associated with [[peter-lynch]], who ran Fidelity Magellan and popularised the [[peg-ratio|PEG ratio]] as a quick test of whether a growth stock is reasonably priced.

## Edge source

GARP blends a **behavioral** and **analytical** edge (see [[edge-taxonomy]]). The behavioral component is that the market tends to over-pay for the fastest, most exciting "story" growth stocks and under-pay for steady, less glamorous compounders growing at a solid-but-unspectacular pace. The analytical component is the discipline of paying only when growth is reasonably priced relative to that growth — refusing both the value trap (cheap because the business is dying) and the growth trap (expensive because expectations are euphoric).

## Why this edge exists

Investors are drawn to extremes. Pure growth crowds chase narrative and momentum, bidding hyper-growth names to valuations that require near-perfect execution for years. Pure deep-value crowds buy statistical cheapness and sometimes catch declining businesses. The "boring middle" — a company compounding earnings at, say, 12-20% a year at a sensible multiple — attracts less attention, so it is more often fairly or modestly priced. The person on the other side is the momentum buyer overpaying for acceleration and the value buyer who screens GARP names out for being "too expensive" on a raw P/E basis. GARP harvests the gap by insisting on growth *and* a reasonable price together, rather than one or the other.

## Null hypothesis

Under the null, GARP is simply a re-labelled blend of the value and quality factors with a growth tilt, and any apparent outperformance disappears once returns are regressed on the standard size, value, profitability/quality and momentum factors. To reject the null, a GARP portfolio must show risk-adjusted results that are not fully explained by being long moderate-value, high-[[quality-factors|quality]] stocks. If the result is fully absorbed by factor exposures, GARP is a perfectly sensible way to *combine* known premia — but not a standalone edge.

## What GARP looks for

- **Earnings growth that is real and durable** — typically a sustainable rate around 10-20% a year, supported by revenue growth, rather than one-off boosts from buybacks or cost-cutting.
- **A reasonable price for that growth** — the signature test is the [[peg-ratio|PEG ratio]] (P/E divided by the expected earnings-growth rate). A PEG near or below 1.0 is the classic GARP sweet spot; a high P/E is acceptable *only* if growth is fast enough to justify it.
- **Quality underneath the growth** — healthy [[return-on-equity|return on equity]], consistent [[free-cash-flow|free cash flow]], manageable debt, and stable or expanding margins, so the growth is financed internally rather than by leverage or dilution.
- **Moderate, not extreme, multiples** — GARP deliberately avoids both the deep-value bargain bin and the most expensive momentum darlings.

## Rules

### Entry
1. **Growth screen:** projected and trailing EPS growth in a sustainable band (commonly ~10-20%+), confirmed by revenue growth — not financial engineering.
2. **Valuation screen:** [[peg-ratio|PEG]] near or below 1.0-1.5; P/E reasonable relative to the company's own history and its sector.
3. **Quality screen:** positive and consistent [[free-cash-flow|free cash flow]], solid [[return-on-equity]], and a balance sheet that can fund growth without excessive debt.
4. **Sanity check the growth story:** make sure the growth rate is achievable and not an analyst extrapolation of a single hot quarter.

### Exit
1. **Valuation runs away:** trim or sell when the multiple expands so far that the PEG is no longer reasonable — the stock has graduated into pure-growth pricing.
2. **Growth decelerates:** exit if earnings growth slows materially below the rate that justified the entry multiple.
3. **Thesis break:** sell on deteriorating margins, rising debt, or a structural threat to the franchise.

### Position sizing
Hold a diversified basket (often 15-30+ names) rather than a few concentrated bets, since GARP is a probabilistic tilt rather than a high-conviction punt. Cap single-name and sector weights to avoid concentration in whatever sector currently screens cheapest-for-its-growth.

## Implementation pseudocode

```python
def garp_candidate(stock):
    return (
        0.10 <= stock.expected_eps_growth <= 0.30      # real, durable growth
        and stock.revenue_growth > 0                   # growth confirmed by sales
        and stock.peg_ratio <= 1.5                     # reasonable price for that growth
        and stock.roe >= 0.12                          # quality underneath
        and stock.free_cash_flow > 0                   # self-funding
        and stock.net_debt_to_ebitda < 3.0             # not levered to grow
    )

def manage(portfolio):
    for pos in portfolio:
        if pos.peg_ratio > 2.0:                        # graduated into pure-growth pricing
            trim_or_sell(pos)
        elif pos.eps_growth < 0.05:                    # growth has stalled
            sell(pos)
    rebalance_periodically(portfolio)
```

## Indicators / data used

- [[peg-ratio|PEG ratio]] (the central GARP metric)
- P/E ratio, both absolute and relative to the company's history and sector
- Trailing and forward EPS growth; revenue growth (to confirm the earnings growth)
- [[return-on-equity]] and margin trend (quality check)
- [[free-cash-flow]] and net debt / EBITDA (sustainability check)

## Example trade (hypothetical)

This is an illustrative, fictional example, not a recommendation or a real result.

A mid-cap software firm grows EPS around 18% a year with revenue growth confirming it. It trades at a P/E of 22, giving a [[peg-ratio|PEG]] of roughly 1.2 — expensive on raw P/E, but reasonable for the growth. [[return-on-equity]] is healthy, [[free-cash-flow]] is positive, and debt is modest. A GARP investor buys it as part of a diversified basket. A pure-value screener would have rejected it (P/E too high); a pure-growth buyer might prefer a flashier name at a PEG of 3. If, over the next two years, the multiple re-rates toward a PEG of 2 while growth holds, the GARP investor trims. If growth instead decelerates toward single digits, the thesis breaks and the position is sold.

## Performance characteristics

GARP is best thought of as a *cycle-smoothing* style rather than a return-maximiser. Because it owns growing businesses but refuses to overpay, it tends to behave between value and growth: it usually gives up some of the explosive upside of pure-growth in roaring bull markets, but typically suffers less of the brutal multiple compression that hits expensive growth when sentiment turns or rates rise. Its return is driven by earnings growth compounding plus the avoidance of overpayment, rather than by multiple expansion alone. (No backtested figures are asserted here — see the null hypothesis above for the factor-replication caveat.)

## What kills this strategy

- **Overpaying anyway** — sloppy growth estimates make a stock look reasonably priced when it is not; the PEG is only as good as the growth forecast feeding it.
- **Growth that evaporates** — the "reasonable price" was reasonable only for the assumed growth; if growth stalls, the stock re-rates as a value name.
- **Factor subsumption** — the edge may be fully explained by value + quality exposure, leaving no standalone alpha.
- **Style drift** — gradually relaxing the price discipline turns a GARP book into an expensive growth book.

## Kill criteria

- A holding's [[peg-ratio|PEG]] persistently exceeds the reasonable-price threshold and growth no longer justifies it.
- Portfolio-level earnings growth decelerates below the band that justified the multiples paid.
- Factor-adjusted alpha is indistinguishable from a value-plus-quality blend over a long rolling window — at which point a cheaper factor implementation is preferable.

## Advantages

- Captures much of growth's upside while keeping a valuation guardrail against overpaying.
- Avoids both the value trap (cheap and dying) and the growth trap (expensive and euphoric).
- Intuitive, FAQ-friendly framework — the [[peg-ratio|PEG]] gives a single, teachable yardstick.
- Tends to draw down less than pure growth when expensive multiples compress.

## Disadvantages

- Underperforms pure growth in strong, momentum-driven bull markets.
- Wholly dependent on the quality of the growth forecast — a bad estimate makes the PEG meaningless.
- May be little more than a value + [[quality-factors|quality]] tilt once factor-adjusted.
- The "reasonable price" judgement is subjective and prone to style drift.

## Sources & further reading

This page describes a well-known investing style and does not assert any backtested results. For primary descriptions of the philosophy, see the widely read works of [[peter-lynch]] (who popularised the PEG ratio and the "growth at a reasonable price" framing) and the broader value/growth literature referenced on the [[value-vs-growth-investing]] and [[fundamental-analysis]] pages.

## Related

- [[value-vs-growth-investing]] — the two poles GARP sits between
- [[growth-investing-strategy]] — the pure-growth approach GARP tempers with price discipline
- [[value-investing-strategy]] — the value discipline GARP applies to growing companies
- [[peg-ratio]] — the central GARP metric
- [[peter-lynch]] — the practitioner most associated with GARP
- [[quality-factors]] — the quality tilt GARP relies on
- [[momentum-value-combination]] — a systematic way to blend opposing styles
- [[fundamental-analysis]] — the analytical toolkit behind the screens
