---
title: "Catalyst Hedged Futures Strategy Fund"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [company, options, volatility, regulation, history]
aliases: ["Catalyst Hedged Futures", "HFXAX", "HFXIX", "Catalyst Capital Advisors", "Walczak fund"]
entity_type: fund
founded: 2005
headquarters: "Huntington, New York, USA"
website: "https://catalystmf.com"
related: ["[[edward-walczak]]", "[[short-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[ljm-preservation-and-growth]]", "[[malachite-capital]]", "[[xiv-velocity-shares]]", "[[short-call]]", "[[options-premium-selling]]", "[[variance-risk-premium]]", "[[sec]]", "[[gap-risk]]", "[[failure-modes]]", "[[universa-investments]]", "[[mutual-fund]]", "[[stress-testing]]"]
---

Catalyst Hedged Futures Strategy Fund (tickers HFXAX / HFXIX, among other share classes) was a U.S. mutual fund advised by Catalyst Capital Advisors and sub-advised by **Edward Walczak** that ran a short-S&P-500-call strategy as its core engine. After several years of strong reported returns the fund suffered an outsized loss of roughly **-20% in early 2017** on a relatively modest market move, then had a still-larger drawdown in **early 2018** during the run-up to [[volmageddon|Volmageddon]] -- both of which were the kinds of losses the fund's risk disclosures had told investors should not happen at the position sizes used. The [[sec|SEC]] subsequently brought a fraud enforcement action against Walczak in connection with risk representations made to investors and the fund board; a federal jury found him liable in April 2022, and a court ordered him to pay $11.2 million in November 2024.

## Overview

Catalyst Capital Advisors, headquartered on Long Island, sponsors a family of liquid-alternative '40 Act mutual funds. The Hedged Futures Strategy Fund was one of its flagship products and grew rapidly in the mid-2010s as advisors and retirement accounts allocated to "non-correlated" alternatives. Reported peak AUM exceeded **$3.5 billion** in 2016-early 2017. The fund's core engine was a systematic [[short-call|short-call]] overlay on S&P 500 futures, marketed as a [[options-premium-selling|premium-selling]] strategy with risk controls intended to limit drawdowns to single digits.

For most of 2013-2016 the strategy delivered a profile that looked like the marketing: low correlation to equities, modest positive returns, low headline volatility. The fund was held in retail brokerage accounts, retirement plans, and advisor-managed model portfolios precisely because the wrapper appeared to make a hedge-fund-style strategy safe for retail use.

## Strategy / Mechanics

The strategy as described in fund prospectuses and subsequent SEC filings:

- **Core position**: Short call spreads / outright short calls on S&P 500 (ES) futures, OTM, monthly expirations.
- **Income source**: The structural [[variance-risk-premium]] embedded in OTM SPX call premia.
- **Risk overlay**: The fund's prospectus described risk controls -- stop-out levels, position-size limits, and stress tests -- that were intended to bound losses when the market rallied (i.e., when short calls move against the book).
- **Implicit assumption**: The strategy was robust to the kinds of one-directional rallies that had occurred historically. The 2017 melt-up violated this assumption.

The book was **net short premium, net short vega, net short gamma** in one direction (calls) -- effectively a bet that the market would not rally too quickly. See [[short-volatility-strategies]] and [[long-vol-vs-short-vol]].

## Track Record

- **2013-2016**: Reported strong returns and the AUM growth that followed. The strategy benefitted from chop and modest declines, both of which produce profits in a short-call book.
- **February 2017**: The S&P 500 rallied sharply in the early weeks of 2017 as part of the post-election melt-up. The Catalyst Hedged Futures Fund reported a single-month loss of approximately **-12% to -20%** depending on share class -- many multiples of the maximum drawdown the fund's risk framework had implied was possible at the position sizes used.
- **December 2017 - February 2018**: The continued rally and rising vol pressure produced further losses. By the time of Volmageddon in February 2018, the fund had been bleeding for more than a year.
- **2018-2019 wind-down**: AUM collapsed from over $3.5B to a small fraction as redemptions and performance losses compounded. The fund continued to operate at much-reduced size.

## Blow-Up / Notable Events

The Catalyst story differs from [[ljm-preservation-and-growth|LJM]] and [[malachite-capital|Malachite]] in two important ways:

1. **The losses were spread across two distinct events** (early 2017 and late 2017-early 2018), each of which was supposed to be a tail event under the fund's risk model. This is consistent with a **misspecified stress test** rather than a single freak shock.
2. **The wrapper was a retail-distributed mutual fund.** Investors held it through advisor accounts and retirement plans. The harm distribution was therefore much wider than a typical hedge-fund blow-up, and the regulatory response was correspondingly more public.

The regulatory record (verified June 2026):

- **January 27, 2020**: The [[sec|SEC]] charged portfolio manager **Edward Walczak** with fraud for telling investors the fund employed safeguards to prevent losses of more than 8% when no such safeguards consistently limited losses, and for claiming he stress-tested the portfolio daily with modeling software when he did not. The CFTC brought a parallel action. The SEC complaint tied the misrepresentations to at least **$500 million** of investor losses (press reports put the Dec 2016 - Feb 2017 loss above **$700 million**, over 20% of the fund's value).
- **Same day**: **Catalyst Capital Advisors LLC and CEO Jerry Szilagyi settled** the companion SEC/CFTC charges for a combined **$10.5 million** — CCA paying disgorgement of $8,176,722 plus $731,759 prejudgment interest and a $1.3 million civil penalty, and Szilagyi a $300,000 penalty — without admitting or denying the findings.
- **April 2022**: Walczak litigated. After a five-day trial in the U.S. District Court for the Western District of Wisconsin, a **jury found him liable for negligence-based securities fraud** (verdict April 15, 2022); the CFTC won a parallel jury verdict in its commodity pool fraud case.
- **November 19, 2024**: The court entered final judgment ordering Walczak to pay **$11.2 million** and restricting him from managing or advising investments for others. (Contrary to some early summaries, the outcome was a litigated jury verdict and court judgment, not a settled administrative bar.)

The case is now cited alongside LJM as the canonical example of '40-Act-wrapped short-vol strategies whose published risk controls did not match the realized loss distribution of the strategy.

## Why It Matters / Lessons

1. **Short-vol blow-ups can come from the call side, not just the put side.** Most discussion of short-vol failure focuses on the put side (the [[gap-risk]] of selling puts into a crash). Catalyst is the canonical example of the **call side** of the same trade -- a strong, fast rally is the equivalent gap-risk for short-call books.
2. **'40 Act / mutual-fund wrappers do not de-risk underlying short-vol strategies.** The retail distribution channel widens the harm without changing the math. Subsequent SEC commentary explicitly addressed this misalignment.
3. **Risk reporting must match the realized loss distribution.** Catalyst's stress tests reportedly under-modeled the kinds of fast directional rallies that actually destroyed the strategy. This is a [[stress-testing]] failure as much as a strategy failure.
4. **Two-event blow-ups are diagnostic.** When a strategy's "should not happen" loss event happens twice within 18 months, that is unambiguous evidence the underlying model is wrong. Many investors held through the first event in 2017 because they trusted the published risk framework. The second event in late 2017-early 2018 produced redemptions but also destroyed remaining NAV before exits could be executed.
5. **Compliance lineage.** The Walczak SEC action is now used in compliance training for liquid-alternative funds running short-vol mandates. The standard now is more explicit alignment between marketing materials, risk reports, and the realized stress-loss profile of the strategy.

Catalyst sits in the same conceptual neighborhood as [[ljm-preservation-and-growth|LJM]] (different shock, same wrapper-and-strategy mismatch) and is the structural counterpart to Universa-style books on the short-vol side. See [[long-vol-vs-short-vol]] for the side-by-side framing.

## Key People

- **[[edward-walczak]]** -- Portfolio manager of the Catalyst Hedged Futures Strategy Fund. Background as a futures and options trader. Found liable by a federal jury for negligence-based securities fraud (April 2022) over risk representations made to investors and the fund's board; ordered in November 2024 to pay $11.2 million and restricted from managing or advising investments for others.
- **Jerry Szilagyi** -- CEO of Catalyst Capital Advisors, the fund's adviser. Settled SEC/CFTC charges in January 2020 (combined $10.5 million with CCA; $300,000 personal penalty). Catalyst as a firm continues to operate other mutual funds.

## Related

- [[edward-walczak]] -- the portfolio manager
- [[ljm-preservation-and-growth]] -- the matching put-side blow-up
- [[malachite-capital]] -- the matching dispersion/short-vol blow-up
- [[xiv-velocity-shares]] -- the matching exchange-traded short-vol failure
- [[short-volatility-strategies]] -- the strategy archetype
- [[short-call]] -- the canonical structure
- [[long-vol-vs-short-vol]] -- comparison and synthesis page
- [[options-premium-selling]] -- the broader doctrine
- [[variance-risk-premium]] -- the premium being harvested
- [[universa-investments]] -- the structural opposite
- [[sec]] -- the regulator that brought the action
- [[gap-risk]] -- the failure mechanism
- [[stress-testing]] -- what was insufficient at Catalyst
- [[failure-modes]] -- failure-mode taxonomy
- [[mutual-fund]] -- the wrapper type

## Sources

- SEC Press Release 2020-21, "SEC Charges Portfolio Manager and Advisory Firm with Misrepresenting Risk in Mutual Fund" (Jan 27, 2020) — https://www.sec.gov/newsroom/press-releases/2020-21
- SEC Litigation Release LR-26179 / LR-25327 and final judgment (Nov 19, 2024, $11.2M) — https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26179
- SEC Director of Enforcement statement on the Walczak jury verdict (Apr 18, 2022) — https://www.sec.gov/newsroom/speeches-statements/grewal-walczak-202204180
- CFTC Press Releases 8109-20 (Catalyst/Szilagyi $10.5M combined settlement) and 8515-22 (jury verdict) — https://www.cftc.gov/PressRoom/PressReleases/8109-20
- Citywire, "SEC fines PM and fund shop for misleading investors after $700m loss" (2020)
- Catalyst Hedged Futures Strategy Fund prospectus and shareholder reports (2014-2019), via SEC EDGAR.
- *Wall Street Journal*, "Catalyst Fund Drops 13% in Day, Burning Investors in 'Black Box'" (February 2017).
- *Bloomberg*, follow-on coverage of Catalyst losses and AUM decline (2017-2018).
- *InvestmentNews* and *Citywire RIA* coverage of Catalyst's distribution channels and advisor exposures.
- Verified via Perplexity (sonar) and web search, 2026-06-10.
