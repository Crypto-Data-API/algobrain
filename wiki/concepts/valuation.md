---
title: "Valuation"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, stocks]
aliases: ["Valuation", "Business Valuation", "Equity Valuation", "valuation"]
related: ["[[discounted-cash-flow]]", "[[price-to-earnings]]", "[[price-to-book]]", "[[fundamental-analysis]]", "[[intrinsic-value]]", "[[value-investing]]", "[[margin-of-safety]]", "[[economic-moat]]"]
domain: [fundamental-analysis]
prerequisites: ["[[fundamental-analysis]]", "[[intrinsic-value]]"]
difficulty: intermediate
---

Valuation is the analytical process of estimating the economic worth of an asset, business, or security. In financial markets, valuation is the foundation of [[fundamental-analysis]] -- the discipline of determining whether a security is overpriced, fairly priced, or underpriced relative to its intrinsic value. The core principle is that the value of any financial asset is the present value of the cash flows it will generate for its owner, though in practice, multiple methodologies exist because future cash flows are inherently uncertain and different situations call for different approaches.

## Discounted Cash Flow (DCF)

The [[discounted-cash-flow]] method is considered the most theoretically rigorous approach. It projects a company's future free cash flows (typically for 5-10 years), then discounts them back to present value using the weighted average cost of capital (WACC). A terminal value captures cash flows beyond the explicit forecast period, usually comprising 60-80% of total DCF value.

**When to use**: Companies with predictable cash flows, mature businesses, infrastructure assets. Less suitable for early-stage companies with no earnings or highly cyclical businesses where projecting cash flows is unreliable.

**Key challenge**: Small changes in assumptions (growth rate, discount rate, terminal value multiple) produce large swings in the output. A 1% change in the discount rate can shift the valuation by 15-25%.

## Comparable Company Analysis (Comps)

Relative valuation compares a company to its peers using standardised multiples:

- **[[price-to-earnings|P/E ratio]]**: Market price per share divided by earnings per share. The S&P 500 has historically averaged a P/E of approximately 15-17x. A company trading at 10x when peers trade at 20x may be undervalued -- or it may face legitimate problems the market is pricing in.
- **EV/EBITDA**: Enterprise value (market cap + net debt) divided by earnings before interest, taxes, depreciation, and amortisation. Preferred over P/E because it is capital-structure-neutral and unaffected by depreciation policy. Typical ranges vary widely by industry: technology (15-25x), utilities (8-12x), retail (6-10x).
- **[[price-to-book|P/B ratio]]**: Market price divided by book value per share. Most useful for financial institutions (banks, insurance companies) where balance sheet assets are marked close to market value.
- **P/S ratio (price-to-sales)**: Used for unprofitable or early-stage companies where earnings-based multiples are not meaningful.

**When to use**: When a peer group of similar companies exists and markets are reasonably efficient in pricing that sector. Best for quick relative assessments and sanity-checking DCF outputs.

## Asset-Based Valuation

This approach values a company based on the net value of its assets (total assets minus total liabilities). It comes in two forms:

- **Book value**: Uses balance sheet values, which may diverge significantly from market values for assets like real estate, intellectual property, or brand equity.
- **Liquidation value**: Estimates what assets would fetch in a forced sale, typically at a 20-50% discount to book value. This represents a floor valuation.

**When to use**: Holding companies, asset-heavy businesses (real estate, natural resources), distressed situations, or as a downside valuation floor.

## Precedent Transaction Analysis

Examines prices paid in past acquisitions of comparable companies. A premium is typically paid over trading multiples: acquisition P/E or EV/EBITDA multiples are usually 20-40% above public market comps due to the control premium (the buyer pays more for the ability to control the company's operations and strategy).

**When to use**: M&A situations, estimating takeout value, or assessing what a strategic or financial buyer might pay.

## Practical Considerations

No single valuation method is definitive. Professional analysts typically use multiple methods and triangulate:

1. Run a DCF for an intrinsic value estimate
2. Compare the result to trading comps for a market-based check
3. Look at precedent transactions for an M&A-based reference point
4. Use asset-based valuation as a floor

If all methods converge on a similar range, confidence in the valuation is high. Wide divergence suggests either model assumptions need refinement or the company is in a situation (rapid growth, distress, structural change) where standard methods struggle.

## Trading Relevance

Valuation is the engine of [[value-investing]] and most fundamental long/short equity: the trade is the *gap* between a security's price and its estimated intrinsic value, with the [[margin-of-safety]] dictating how wide that gap must be before committing capital.

- **Mispricing as the edge.** A position is justified only when price diverges materially from a defensible valuation range; the [[economic-moat]] and growth durability determine whether that gap closes or persists.
- **Multiples as a fast screen.** Relative multiples (P/E, EV/EBITDA, P/B, P/S) are used to screen large universes and to flag rich or cheap names quickly before deeper DCF work — and to time mean reversion in pairs and sector-rotation trades.
- **Re-rating catalysts.** Valuation-driven traders look for events (earnings beats, margin inflection, capital returns, multiple re-rating) that force the market to reprice toward intrinsic value.
- **Garbage-in caveat.** Because DCF is hyper-sensitive to assumptions, professionals stress-test the bear/base/bull range rather than trusting a single point estimate; a "precise" valuation is usually false precision.
- **Limits in fast-moving regimes.** In bubbles, distress, or rapid technological change, prices can stay far from intrinsic value for years — valuation tells you *what* is mispriced, not *when* it corrects, which is why it pairs poorly with short timeframes and well with patient capital.

## Related

- [[discounted-cash-flow]] -- the primary intrinsic valuation method
- [[dividend-discount-model]] -- intrinsic valuation from expected dividends
- [[terminal-value]] -- the post-forecast component that dominates a DCF
- [[discount-rate]] -- the rate that converts future cash flows to present value
- [[owner-earnings]] -- Buffett's cash-flow definition for intrinsic value
- [[price-to-earnings]] -- the most widely cited valuation multiple
- [[price-to-book]] -- book-value-based relative valuation
- [[fundamental-analysis]] -- the broader discipline that valuation supports
- [[intrinsic-value]] -- the conceptual output of a valuation exercise
- [[value-investing]] -- the philosophy that acts on valuation gaps
- [[margin-of-safety]] -- the buffer demanded between price and value

## Sources

- Aswath Damodaran, *Investment Valuation* and *The Little Book of Valuation* — standard references on DCF, relative, and asset-based methods.
- McKinsey & Company, Koller et al., *Valuation: Measuring and Managing the Value of Companies*.
- Benjamin Graham & David Dodd, *Security Analysis* — origins of intrinsic-value and margin-of-safety thinking.
