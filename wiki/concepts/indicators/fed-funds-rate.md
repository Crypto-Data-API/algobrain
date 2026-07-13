---
title: "Federal Funds Rate"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [indicators, portfolio-theory, risk-management]
domain: [portfolio-theory]
prerequisites: ["[[interest-rates]]"]
difficulty: intermediate
aliases: ["Fed Funds Rate", "Fed Rate", "Federal Funds Rate", "FFR"]
related: ["[[interest-rates]]", "[[rba]]", "[[ecb]]", "[[yield-curve]]", "[[us-treasury-bonds]]", "[[economic-indicators]]", "[[sector-rotation]]", "[[federal-reserve]]", "[[monetary-policy]]", "[[inflation]]", "[[us-dollar]]", "[[interest-rate-risk]]"]
---

The federal funds rate is the interest rate at which US banks lend reserves to each other overnight. The [[federal-reserve|Federal Reserve]] sets a target *range* for this rate, making it the primary tool of US [[monetary-policy]] and the benchmark that influences global [[interest-rates]], bond prices, and equity valuations. Changes in the fed funds rate affect [[yield-curve]] shape, drive [[sector-rotation]] between rate-sensitive sectors, and influence the [[us-dollar|USD]] exchange rate.

> **Data disclaimer:** This page is structural and educational. It deliberately does **not** quote a specific current target range or specific dated FOMC decisions, which change over time. For the live level consult the Federal Reserve, the New York Fed's daily EFFR, or the CME FedWatch tool.

## How It Works

The Federal Open Market Committee (FOMC) meets eight times per year to set the target range for the fed funds rate (expressed as a 25 bp-wide band, e.g. an illustrative 5.25%-5.50%). The committee comprises the seven Board of Governors plus a rotating set of regional Reserve Bank presidents; the New York Fed president holds a permanent vote. Decisions are announced in a post-meeting statement, followed by a press conference and, four times a year, the Summary of Economic Projections.

The Fed no longer enforces the range through reserve scarcity. In the post-2008 "ample reserves" regime it steers the effective rate using **administered rates**:

| Tool | Role | Who it targets |
|------|------|----------------|
| **IORB** (interest on reserve balances) | Effective ceiling | Banks holding reserves at the Fed |
| **ON RRP** (overnight reverse repo) rate | Effective floor | Money-market funds, GSEs, non-banks |
| **Discount rate** (primary credit) | Backstop above the range | Banks borrowing directly from the Fed |
| **Open market operations** | Manage aggregate reserves | System-wide liquidity |

The actual transacted rate is published daily by the New York Fed as the **effective federal funds rate (EFFR)** -- a volume-weighted median of overnight interbank lending. The EFFR normally prints inside the target band, between the ON RRP floor and the IORB ceiling.

### How a rate change transmits to markets

The fed funds rate cascades through the financial system in a fairly predictable chain:

1. **Money-market rates** -- SOFR and other overnight rates move almost one-for-one with the target.
2. **Prime rate** -- the rate banks charge their best customers typically sits ~3 percentage points above the upper bound of the fed funds range, so credit-card, HELOC, and floating-rate loan costs follow.
3. **Short end of the [[yield-curve]]** -- 2-year Treasury yields track the *expected* policy path, not just today's level.
4. **Long end** -- 10- and 30-year yields are driven more by growth, [[inflation]] expectations, and term premium, so an aggressive hiking cycle can **invert** the curve when short rates rise above long rates (a classic recession signal).
5. **Risk assets** -- the rate sets the [[risk-free-rate|risk-free]] discount rate in valuation models, so it flows into equity multiples, credit spreads, and the [[us-dollar]].

## Trading Relevance

- **Forward guidance**: Market participants watch the FOMC "dot plot" (individual member rate projections) and CME FedWatch probabilities to anticipate moves. Markets price the *expected path*, so the **surprise relative to expectations** -- not the level itself -- moves prices on decision day.
- **Equity valuation**: Rate-hiking cycles compress equity multiples and tend to favour value over growth (high-duration growth stocks are most sensitive to discount-rate changes). Rate cuts are generally bullish for risk assets -- but context matters: emergency cuts during a crisis carry different signals than gradual normalisation cuts.
- **Risk-free anchor**: The rate is the basis for the risk-free rate used in options pricing models and [[dcf-valuation|DCF valuations]], making it foundational to virtually all asset pricing.
- **Sector rotation**: Banks benefit from a steeper curve and higher rates; utilities, REITs, and other bond proxies suffer when rates rise. Traders rotate accordingly across the cycle.
- **Carry and FX**: A widening rate differential versus other central banks ([[rba]], [[ecb]], BoJ) strengthens the dollar and drives carry-trade flows.

### Sector sensitivity cheat-sheet

| Environment | Tends to benefit | Tends to suffer |
|-------------|------------------|-----------------|
| **Rising rates / steepening** | Banks, insurers, value, energy, cash | Long-duration growth/tech, REITs, utilities, long bonds |
| **Falling rates / easing** | Growth/tech, REITs, utilities, gold, long bonds | Bank net-interest margins, money-market yields |
| **Inverted curve** | Defensives, quality, short-duration credit | Cyclicals, small caps (early recession signal) |

### Worked example: pricing the surprise

Suppose (illustrative) FedWatch implies a **90% probability of "no change"** and **10% of a 25 bp cut** going into a meeting. The market is essentially positioned for no move. Two scenarios:

- **The Fed holds** (the expected outcome): little price reaction to the *decision*; the press conference and dot plot become the real market drivers.
- **The Fed cuts 25 bp** (the 10% tail): a genuine surprise -- short-term yields fall, the dollar typically weakens, and rate-sensitive equities pop, because the market had only partially priced it. The size of the move scales with how unexpected it was, not the 25 bp itself.

This is the core trading insight: **what is already priced is already in the market.** Edge around FOMC comes from a differentiated view on the *path* versus consensus, or from positioning for the post-statement repricing of the dot plot.

## Common Pitfalls and Risks

- **Trading the level, not the surprise**: a hike can rally stocks if it was smaller/more dovish than feared, and vice versa. Always reference expectations (FedWatch, OIS-implied path).
- **Fighting the curve**: betting on cuts while the policy path is still tightening (or vice versa) is fighting a powerful trend; let the dot plot and incoming data confirm.
- **Over-reading a single decision**: the *trajectory* across meetings matters more than any one move; "one and done" vs. a sustained cycle have very different asset implications.
- **Press-conference whipsaw**: the statement and the Chair's Q&A often move markets in opposite directions within the same hour; sizing positions for that intraday volatility is essential.
- **Assuming long rates follow**: the Fed controls the short end; long yields can rise *or* fall after a cut depending on growth and inflation expectations.

## Related

- [[federal-reserve]] — the central bank that sets the target range
- [[monetary-policy]] — the broader toolkit the rate sits within
- [[interest-rates]] — the broader concept the fed funds rate anchors
- [[yield-curve]] — shaped by the short-rate path the Fed controls
- [[us-treasury-bonds]] — priced off the rate path and term premium
- [[inflation]] — the variable the FOMC's dual mandate targets
- [[economic-indicators]] — the data the FOMC reacts to (NFP, CPI, GDP)
- [[sector-rotation]] — rate cycles drive leadership between sectors
- [[interest-rate-risk]] — duration exposure created by rate changes
- [[us-dollar]] — strengthens/weakens with the rate differential
- [[rba]] / [[ecb]] — peer central banks whose differentials drive FX

## Sources

- Federal Reserve — FOMC statements, the Summary of Economic Projections ("dot plot"), and policy implementation notes (federalreserve.gov).
- Federal Reserve Bank of New York — daily effective federal funds rate (EFFR) and reference-rate methodology.
- CME Group FedWatch Tool — market-implied probabilities of FOMC rate decisions from fed funds futures.
