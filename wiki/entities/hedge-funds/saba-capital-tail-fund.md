---
title: "Saba Capital Tail Fund"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [options, volatility, risk-management, company]
aliases: ["Saba Capital Tail Hedge", "Saba Tail Fund", "Saba Capital Management"]
entity_type: fund
founded: 2009
headquarters: "New York, New York, USA"
website: "https://www.sabacapital.com"
related: ["[[boaz-weinstein]]", "[[saba-capital]]", "[[tail-risk-hedging]]", "[[long-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[crisis-alpha]]", "[[credit-default-swap]]", "[[convexity]]", "[[universa-investments]]", "[[longtail-alpha]]", "[[covid-crash]]", "[[london-whale]]", "[[deutsche-bank]]", "[[capital-structure-arbitrage]]", "[[volmageddon]]", "[[vix-calls]]"]
---

Saba Capital Tail Fund is the dedicated tail-hedging vehicle within **Saba Capital Management**, the credit and volatility hedge fund founded by **Boaz Weinstein** in 2009. The strategy combines deeply-out-of-the-money equity puts and VIX optionality with cheap [[credit-default-swap|credit default swap]] convexity, expressing tail risk through both equity-vol and credit-vol channels. The vehicle attracted unusually large institutional inflows in 2020 after delivering reported returns above 90% in the first quarter during the [[covid-crash|COVID crash]], and is now one of the larger publicly known dedicated tail vehicles alongside [[universa-investments|Universa]] and [[longtail-alpha|LongTail Alpha]].

## Overview

Saba Capital was spun out of Deutsche Bank's proprietary credit trading group, which Weinstein had built and run before the GFC. The firm's broader product line spans credit relative-value, capital-structure arbitrage, and closed-end fund activism, but the **tail-hedge sleeve** is a distinct mandate offered as a standalone fund (and as an overlay to other Saba strategies). The pitch is that Saba is one of the few tail managers whose convex hedge is sourced from **credit and equity vol simultaneously**, capturing crisis-alpha that purely equity-derivative tail funds do not always pick up.

The fund came to public prominence in March-April 2020 when Weinstein was widely profiled as one of the few hedge fund managers to have a profitable Q1 2020. Saba subsequently raised meaningful AUM into the tail product, with industry reporting indicating the dedicated tail vehicle grew from low hundreds of millions pre-COVID to multiple billions over 2020-2022.

## Strategy / Mechanics

The Saba tail book is more diversified across instruments than the Universa or LongTail Alpha equity-put cores:

- **Equity vol convexity**: OTM SPX puts and put spreads, plus [[vix-calls|VIX call]] structures sized for explosive monetization in vol shocks.
- **Credit convexity**: Long protection on investment-grade and high-yield CDX indices, single-name CDS, and out-of-the-money credit options. In normal regimes credit spreads are tight and CDS protection is cheap; in stress regimes spreads can widen 5-10x, producing large convex P&L on small premium outlays. See [[credit-default-swap]].
- **Capital-structure arbitrage tilt**: Some positions express the same tail view through both the credit and equity capital-structure of the same issuer, exploiting the [[capital-structure-arbitrage|relative pricing]] of equity puts vs. credit protection.
- **Active monetization**: Like LongTail Alpha, Saba sells convex exposures into stress and re-establishes them after vol normalizes -- the fund is not a buy-and-hold put owner.
- **Negative carry**: The book pays carry every quiet quarter -- both the option premium bleed and the running cost of CDS protection. The carry cost has historically been comparable to other dedicated tail funds (1-3% per year of allocated capital).

The book is **net long premium, net long convexity** in two dimensions (equity vol AND credit vol). This is the structural feature that distinguishes it from pure-equity tail vehicles. See [[long-volatility-strategies]] and [[long-vol-vs-short-vol]].

## Track Record

Performance figures for the Saba tail strategy are reported through institutional fund letters and industry coverage. Headline numbers cited in public sources:

- **Q1 2020 (COVID crash)**: The Saba tail vehicle reportedly returned approximately **+92% to +99%** in Q1 2020, depending on share class and reporting period. Both the equity-vol and credit-vol legs contributed materially as VIX spiked above 80 and IG/HY credit spreads roughly tripled in March 2020.
- **Calm regimes (2021, 2023)**: The fund bled premium and CDS carry as is structurally expected. Annualized losses in calm years have been in the low-to-mid single digits, in line with other dedicated tail funds.
- **March 2023 regional bank stress**: The credit-protection leg was a meaningful contributor as financials CDS widened sharply on SVB and follow-on bank concerns. Saba was again profiled in *Bloomberg* and *FT* for delivering positive returns into the stress.
- **Saba's broader fund family** (relative value and credit funds) has a much longer track record extending to 2009 and beyond, but those vehicles are different mandates and not directly comparable to the dedicated tail product.

## Crisis Performance

Saba is one of the better-documented examples of **two-channel** tail hedging in action. The COVID crash specifically showed the value of carrying both equity-vol and credit-vol convexity:

- **Equity puts** captured the SPX drawdown from late February through mid-March 2020.
- **Credit protection** captured the violent widening of IG and HY spreads in mid-March 2020 -- a move that was even more extreme than the equity sell-off in standard-deviation terms.
- **Vol-of-vol** in VIX options paid as the term structure went into deep backwardation.
- The combined book monetized into multiple stages of the crash rather than depending on a single Greek paying off.

This multi-channel design also helps in **non-equity-led shocks** -- e.g., regional bank stress, sovereign credit events -- where pure-equity tail funds may be slower to monetize. See [[crisis-alpha]].

## Why It Matters / Lessons

1. **Tail risk is not a one-Greek problem.** A serious institutional tail hedge can express convex protection through both equity vol and credit vol. Allocators with credit-heavy books in particular benefit from credit-channel tail hedging rather than retrofitting an equity-only hedge.
2. **The London Whale lineage matters.** Weinstein is best known publicly for being on the other side of JPMorgan's 2012 [[london-whale]] trade -- a trade structurally similar to a short-credit-vol position. He profited from understanding how concentrated short-vol books mispriced their tail. That lineage informs the firm's ongoing hunt for [[capital-structure-arbitrage|cap-structure mispricings]] that look like cheap tail.
3. **Liquidity design matters in shocks.** Both CDS and SPX options become illiquid in stress, but in different ways and at different times. Diversifying across the two reduces the chance that the book is "right but unable to monetize."
4. **Same compounding case as Universa.** The institutional pitch is the familiar one: a small allocation to a convex hedge raises the geometric return of an equity- or credit-heavy book by reducing the depth of compoundable drawdowns.

## Recent Developments (2024–2026)

Saba Capital Management (firm-wide AUM reported around **$6.5 billion** in recent coverage) has been in the news primarily for its **closed-end fund (CEF) discount-arbitrage activism**, a separate strategy from the tail fund but run by the same firm and informing its reputation for exploiting structural mispricings:

- **2024 — BlackRock proxy fights**: Saba ran the most aggressive activist campaign in the US closed-end fund sector, targeting ten BlackRock CEFs trading at persistent discounts to NAV, demanding tender offers, buybacks, and board changes.
- **January 2025 — BlackRock settlement**: BlackRock agreed to conduct self-tenders at two of its funds in exchange for a Saba standstill lasting through the **2027 proxy season at 48 of the 49 remaining BlackRock CEFs** (ISS Governance coverage).
- **December 2024 – early 2025 — UK investment trust campaign**: Saba disclosed stakes of **19–29%** in seven UK investment trusts and requisitioned general meetings to replace their boards. Shareholders **rejected Saba's proposals at all seven trusts** in early 2025 — a high-profile setback.
- **February 2025 — pivot**: Saba relaunched against four trusts (two original targets plus Middlefield Canadian Income and Schroder UK Mid Cap), shifting strategy to demand conversion into open-ended funds.
- **April 2026 — first UK board win**: Saba succeeded in replacing the board of **Edinburgh Worldwide Investment Trust** at its third attempt (MoneyWeek).
- **September 2025**: Saba prepared an active ETF launch to extend its discount-capture strategy into a retail wrapper (QuotedData).

For the tail fund specifically, no major public monetization event has been reported since the March 2023 regional-bank stress; the August 5, 2024 yen-carry VIX spike (VIX 65 intraday) was the largest vol event of the period and favored long-vol books generally.

## Key People

- **[[boaz-weinstein]]** -- Founder, CIO. Former co-head of credit trading at Deutsche Bank, where he ran the proprietary credit book that was spun out into Saba. Famous as the manager who took the other side of JPMorgan's [[london-whale]] credit-derivatives position in 2012. Public chess player and frequent media commentator.
- Multiple senior partners in credit-trading and structured-credit roles, several with backgrounds at Deutsche Bank and other large dealer credit desks.

## Related

- [[boaz-weinstein]] -- founder and CIO
- [[saba-capital]] -- the parent firm and other strategies
- [[universa-investments]] -- the canonical equity-vol tail fund
- [[longtail-alpha]] -- the second equity-vol tail fund
- [[tail-risk-hedging]] -- the strategy
- [[long-volatility-strategies]] -- the strategy archetype
- [[long-vol-vs-short-vol]] -- comparison and synthesis page
- [[crisis-alpha]] -- the return profile
- [[convexity]] -- the payoff property
- [[credit-default-swap]] -- the credit-side instrument
- [[capital-structure-arbitrage]] -- a related Saba activity
- [[london-whale]] -- the trade that made Weinstein famous
- [[deutsche-bank]] -- the firm where Weinstein built the credit franchise
- [[covid-crash]] -- the headline monetization event
- [[volmageddon]] -- a smaller monetization event
- [[vix-calls]] -- one component of the book

## Sources

- Saba Capital Management firm filings and ADV.
- *Wall Street Journal*, "Saba's Boaz Weinstein Pulls In Cash After Pandemic Win" (2020) and follow-on coverage.
- *Bloomberg*, "Boaz Weinstein's Saba Returns 99% in First Quarter" (April 2020).
- *Financial Times*, profiles of Saba tail hedging (2020-2024).
- *Institutional Investor*, coverage of Saba's tail strategy and AUM growth.
- Coverage of the JPMorgan [[london-whale]] trade (2012-2013) for context on Weinstein's lineage.
- ISS Governance, "Activism in the UK — The Saba saga" (2025) — https://insights.issgovernance.com/posts/activism-in-the-uk-the-saba-saga-and-implications-for-the-investment-trust-sector/
- MoneyWeek, "Saba claims first victory in UK investment trust takeover attempts" (April 2026) — https://moneyweek.com/investments/investment-trusts/saba-claims-first-victory-uk-investment-trust-takeover-attempts
- QuotedData, "Activist Saba Capital prepares active ETF launch" (September 2025)
- Verified via Perplexity (sonar) and web search, 2026-06-10
