---
title: "Dividend Reinvestment Plan"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, fundamental-analysis]
aliases: ["DRP", "DRIP", "Dividend Reinvestment", "Dividend Reinvestment Plan"]
domain: [portfolio-theory]
prerequisites: ["[[dividend-yield]]", "[[compounding]]"]
difficulty: beginner
related: ["[[dividend-yield]]", "[[compounding]]", "[[two-portfolio-strategy]]", "[[total-return]]", "[[dollar-cost-averaging]]"]
---

A Dividend Reinvestment Plan (DRP, or DRIP in the US) is a company- or broker-administered scheme that automatically uses a shareholder's cash [[dividend|dividends]] to buy additional shares of the same company, usually at little or no brokerage cost and sometimes at a small discount (commonly 1-5%) to the prevailing market price. It is one of the simplest mechanical ways to harness [[compounding]], converting income into an ever-larger equity base without the investor lifting a finger. Fred McNaught uses DRPs across all of his infrastructure-fund holdings, treating them as a low-friction compounding engine within the income sleeve of his [[two-portfolio-strategy]].

## How a DRP Works

When a company declares a [[dividend]], an enrolled shareholder receives new shares instead of (or in addition to) cash. The number of shares allocated equals the dividend amount divided by the DRP issue price (the volume-weighted average price over a defined pricing period, sometimes less the discount). Fractional entitlements are typically either issued as fractional shares, carried forward as a residual cash balance, or rounded — terms vary by plan. Because the reinvestment is internal, the investor avoids the bid-ask spread and brokerage they would pay to manually reinvest, which is the DRP's main cost advantage at small dividend sizes where flat brokerage fees would otherwise dominate.

### DRP vs. Cash Dividend at a Glance

| Feature | DRP (reinvest) | Cash dividend (take cash) |
|---------|----------------|---------------------------|
| Share count | Grows automatically each period | Static unless you manually buy |
| Brokerage on reinvestment | Usually nil | Pay each time you reinvest manually |
| Possible discount to market | Often 1-5% (where offered) | None |
| Compounding | Automatic | Requires discipline |
| Tax on the dividend | Still owed (no cash received) | Owed, but cash is in hand to pay it |
| Position concentration | Increases over time | Unchanged |
| Suits | Accumulators, long horizon | Retirees / income spenders |

## Why DRPs Compound Returns

The power of a DRP comes from the same mechanism as [[compounding]]: reinvested dividends generate their own future dividends, and so on. Over multi-decade horizons, reinvested dividends historically account for a large share of total equity returns — for the [[sp500|S&P 500]], reinvested dividends have contributed roughly a third to a half of total return depending on the period measured, versus price appreciation alone (see [[total-return]]). A DRP automates the reinvestment decision, removing the behavioral leak where investors spend dividend cash rather than redeploying it. It also enforces a form of [[dollar-cost-averaging]]: shares are bought at each dividend date regardless of price, buying more shares when the price is low and fewer when high.

### Worked Example: A DRP Compounding Over Time

Consider **1,000 shares** of a stock at **$20.00** (a $20,000 holding) paying a **4% annual yield** ($0.80/share), with the price growing **5% per year** and dividends reinvested at year-end via DRP (ignoring the discount and tax for clarity).

| Year | Shares (start) | Price | Dividend ($0.04 × price × shares) | New shares bought | Shares (end) |
|------|----------------|-------|-----------------------------------|-------------------|--------------|
| 1 | 1,000.0 | $20.00 | $800.00 | 38.1 (at $21.00) | 1,038.1 |
| 2 | 1,038.1 | $21.00 | $872.0 | 39.6 (at $22.05) | 1,077.7 |
| 3 | 1,077.7 | $22.05 | $950.6 | 41.1 (at $23.15) | 1,118.8 |

After 3 years the holder owns ~1,119 shares vs. the original 1,000 -- a **~12% increase in share count** purely from reinvestment, on top of price appreciation. The two effects multiply: more shares each earn the next dividend, and each dividend grows with the price. Over 20-30 years this share-count growth dwarfs the early years -- the hallmark of [[compounding]]. (Numbers are illustrative round figures, not a forecast.)

## Trade-offs and Considerations

- **Tax**: In most jurisdictions, reinvested dividends are taxed as income in the year received even though no cash is received — the investor must fund the tax bill from elsewhere. (In Australia, franking credits attached to a franked dividend still apply to the reinvested amount.)
- **Cost-base tracking**: Each reinvestment creates a new parcel of shares with its own purchase price and date, complicating capital-gains record-keeping. Investors must keep records of every DRP allocation.
- **Concentration**: A DRP mechanically increases the position in a single company over time. For an investor focused on [[diversification]], unchecked reinvestment can quietly overweight a holding; periodic rebalancing may be needed.
- **No discretion**: Capital is redeployed into the same stock regardless of valuation. For a holding that has become overvalued or whose thesis has broken, automatic reinvestment may be inferior to taking the cash and allocating elsewhere.

## Portfolio Relevance

DRPs are most useful in the long-horizon, income-oriented part of a portfolio — quality dividend payers, infrastructure, REITs, and index funds — where the goal is steady compounding rather than active trading. They suit accumulation-phase investors who do not need the income for living expenses. In a [[two-portfolio-strategy]] that separates a stable income book from a more active growth/trading book, the DRP is a natural fit for the income book, automating reinvestment while the investor's attention goes to the active sleeve. Investors approaching or in retirement often switch DRPs off so dividends arrive as spendable cash.

## How Traders and Investors Use DRPs

- **Set-and-forget accumulation.** Enrol quality compounders and let the position grow without manual intervention -- the core "income-sleeve" use case.
- **Capture the discount.** Where a plan offers a 1-5% discount to market, the DRP is effectively a small guaranteed return on the reinvested amount each period.
- **Selective enrolment.** Run DRPs only on holdings you would happily buy more of at any price; take cash on holdings near fair value or with a deteriorating thesis.
- **Toggle by life stage.** Reinvest during accumulation; switch to cash dividends at retirement to fund living expenses without selling shares.
- **Pair with manual rebalancing.** Because a DRP only ever buys *more of the same stock*, periodically review whether reinvestment has overweighted a position and trim if needed (see [[rebalancing]] and [[diversification]]).

## Common Pitfalls and Risks

- **Phantom tax bill.** Reinvested dividends are taxable in most jurisdictions even though no cash arrives -- the investor must fund the tax from elsewhere, which can be a nasty surprise.
- **Cost-base sprawl.** Every reinvestment is a new tax parcel; over decades a single holding can accumulate dozens of parcels, complicating capital-gains calculations. Keep meticulous records.
- **Silent concentration.** Unchecked reinvestment quietly overweights the best-performing holding, eroding [[diversification]] and raising single-stock risk.
- **Valuation-blind buying.** Capital is redeployed regardless of price; for an overvalued or broken stock, taking cash and allocating elsewhere beats automatic reinvestment.
- **Capital raising in disguise.** A DRP issues new shares, mildly diluting non-participants; for the company it is a cheap way to retain capital, which is occasionally a red flag if the firm leans on it to fund a stretched payout.
- **Discount can mask weakness.** A persistently deep DRP discount may signal a company eager to conserve cash -- worth investigating, not just harvesting.

## Sources

- ASX. "Dividend reinvestment plans" investor education — mechanics, pricing periods, and discounts for ASX-listed DRPs.
- McNaught, F. ITPM curriculum — use of DRPs in the income sleeve of a two-portfolio approach.

## Related

- [[dividend-yield]] — the income stream a DRP reinvests
- [[compounding]] — the mechanism a DRP automates
- [[dollar-cost-averaging]] — DRPs buy at each dividend date regardless of price
- [[total-return]] — reinvested dividends are a major component of long-run total return
- [[two-portfolio-strategy]] — DRPs suit the income sleeve
- [[dividend]] — the income stream being reinvested
- [[diversification]] — DRPs can quietly erode it via concentration
- [[rebalancing]] — needed to offset DRP-driven position drift
