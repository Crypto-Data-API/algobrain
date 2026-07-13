---
title: "Price-to-Cash-Flow Ratio"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, metrics]
aliases: ["P/CF", "P/CF ratio", "price to cash flow", "price-to-cash-flow", "Price-to-Cash-Flow", "P/OCF", "price to operating cash flow", "price-to-free-cash-flow", "P/FCF"]
domain: [fundamental-analysis]
prerequisites: ["[[free-cash-flow]]", "[[price-to-earnings-ratio]]"]
difficulty: intermediate
related: ["[[price-to-earnings-ratio]]", "[[free-cash-flow]]", "[[free-cash-flow-yield]]", "[[ev-ebitda]]", "[[earnings-per-share]]", "[[cash-flow-statement]]", "[[fundamental-analysis]]"]
---

**Price-to-cash-flow (P/CF)** values a stock against the cash its operations generate rather than against its accounting earnings. It is computed as share price divided by cash flow per share, and it serves as a sturdier alternative to the [[price-to-earnings-ratio|P/E ratio]] in situations where non-cash charges — heavy depreciation, amortization, or write-downs — distort reported earnings. Because cash flow is harder to manipulate than net income, P/CF is a favoured "reality check" multiple, especially for capital-intensive businesses.

## Formula

$$\text{P/CF} = \frac{\text{Share Price}}{\text{Operating Cash Flow per Share}}$$

equivalently:

$$\text{P/CF} = \frac{\text{Market Capitalization}}{\text{Operating Cash Flow}}$$

The denominator is usually **cash flow from operations** (the top section of the cash flow statement). A closely related variant, **price-to-free-cash-flow (P/FCF)**, uses [[free-cash-flow|free cash flow]] (operating cash flow minus capital expenditures) instead, which is stricter because it charges the business for the capex needed to sustain itself.

## Relationship to Other Multiples

- **vs. [[price-to-earnings-ratio|P/E]]** — P/E divides price by net income (which includes non-cash charges like depreciation); P/CF adds those charges back. For a company with large, "soft" non-cash expenses, P/CF can look far cheaper than P/E, and the *gap* between the two multiples hints at how cash-rich the reported earnings really are.
- **vs. [[ev-ebitda|EV/EBITDA]]** — EV/EBITDA uses enterprise value (capturing debt) over a pre-capex cash proxy; P/CF uses equity value over operating cash flow. EV/EBITDA is preferred for cross-capital-structure comparison, while P/CF is a quicker equity-holder gauge.
- **vs. [[free-cash-flow-yield|FCF yield]]** — P/FCF is simply the reciprocal of the equity free-cash-flow yield. A P/FCF of 20x equals a 5% FCF yield.

## Worked Example

A company has:

- Share price: $60
- Operating cash flow: $1.2 billion
- Shares outstanding: 400 million → operating cash flow per share = $3.00

$$\text{P/CF} = \frac{60}{3.00} = 20\times$$

Investors are paying $20 for every $1 of annual operating cash flow. If the same company reported only $2.00 of EPS — because depreciation is heavy — its P/E would be 30x, far richer than its P/CF of 20x, revealing that a large chunk of the "expense" gap is non-cash.

## Typical Ranges

P/CF norms vary by sector and capital intensity, so compare within an industry and against a company's own history:

- A broad-market P/CF has historically sat in the low-to-mid teens.
- **Single digits** often flag value or a distressed/cyclical situation.
- **20x+** implies high growth expectations or a premium-quality business.

Capital-intensive sectors (telecom, utilities, real estate, energy) are where P/CF shines, because their large depreciation charges make P/E misleadingly high while cash generation remains strong.

## Interpretation

- A **lower P/CF** relative to peers or to the stock's own history suggests the market is paying less per dollar of cash generation — potentially cheap, but check *why*.
- A **rising P/CF** can mean multiple expansion (the market re-rating the cash stream higher) or deteriorating cash flow with a sticky price.
- Always confirm the cash flow is **operational and recurring**, not flattered by a one-off working-capital release or a stretch in payables.

## Limitations

1. **Operating cash flow ignores capex.** A telecom can show a low P/CF yet consume nearly all that cash just maintaining its network — P/FCF or EV/EBITDA−capex is more honest there.
2. **Working-capital noise.** A single year's cash flow can be inflated by drawing down inventory or delaying supplier payments. Average across a cycle.
3. **Stock-based compensation** is added back in operating cash flow but is a real cost to shareholders.
4. **Not meaningful for banks/insurers**, where the cash-flow statement does not map cleanly to operating performance.
5. **No single "cash flow" definition** — operating cash flow, free cash flow, and "cash earnings" all produce different multiples, so always confirm which the quoted figure uses.

## Trading Relevance

P/CF (and its stricter sibling P/FCF) is a standard ranking factor in systematic **value** strategies, often blended with [[price-to-earnings-ratio|P/E]], P/B, and [[ev-ebitda|EV/EBITDA]] into a composite cheapness score; cash-based multiples add robustness because they are less easily managed than earnings. Discretionary investors use the **P/E-minus-P/CF spread** as an earnings-quality tell — a P/E far above P/CF can flag aggressive accruals or heavy non-cash adjustments. In capital-intensive sectors where P/E is structurally distorted by depreciation, P/CF is frequently the primary equity multiple traders quote.

## Related

- [[price-to-earnings-ratio]]
- [[free-cash-flow]]
- [[free-cash-flow-yield]] — the reciprocal yield (FCF yield = 1 / P/FCF)
- [[ev-ebitda]]
- [[earnings-per-share]]
- [[cash-flow-statement]] — source of the operating cash flow in the denominator
- [[fundamental-analysis]]

## Sources

- Damodaran, Aswath. *Investment Valuation* (Wiley) — cash-flow multiples and their relation to earnings and enterprise-value multiples.
- CFA Institute, *Equity Valuation* curriculum — price multiples including price-to-cash-flow.
- O'Shaughnessy, James. *What Works on Wall Street* — historical performance of price-to-cash-flow as a value screen.
