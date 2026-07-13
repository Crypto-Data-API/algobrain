---
title: "Form 4 (Insider Transactions)"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [stocks, regulation, market-microstructure, event-driven]
aliases: ["Form 4", "SEC Form 4", "Insider Transaction Report", "Section 16 Filing", "Statement of Changes in Beneficial Ownership"]
domain: [market-microstructure, fundamental-analysis]
difficulty: beginner
related: ["[[insider-trading]]", "[[edgar]]", "[[sec]]", "[[8-k]]", "[[10-k]]", "[[information-arbitrage]]", "[[event-driven-trading]]", "[[fundamental-analysis]]"]
---

**SEC Form 4** is the filing that corporate insiders — officers, directors, and shareholders owning more than 10% of a company's stock — must submit when they buy or sell that company's securities. It reports *legal* insider transactions and is filed publicly on [[edgar|EDGAR]] within two business days, making it one of the few near-real-time windows into what the people who know a company best are actually doing with their own money. Form 4 should not be confused with *illegal* [[insider-trading|insider trading]]: Form 4 transactions are disclosed precisely because they are permitted, provided the insider is not acting on material non-public information.

## Overview

Form 4 exists under **Section 16** of the Securities Exchange Act of 1934, which governs the reporting and short-swing-profit rules for insiders ("Section 16 insiders"). It is one of three related forms:

- **Form 3** — the *initial* statement of holdings, filed when someone first becomes an insider.
- **Form 4** — a report of *changes* in holdings (a purchase, sale, option exercise, grant, or gift). This is the one traders watch.
- **Form 5** — an *annual* clean-up for certain transactions exempt from immediate Form 4 reporting.

Because Form 4 is filed within two business days and published immediately, aggregators and screeners turn it into a continuously updated "insider buying / selling" feed.

## What It Contains

A Form 4 identifies the insider, their relationship to the company (director, officer with title, or 10% owner), and lists each transaction in two tables:

- **Table I — Non-Derivative Securities**: direct trades in the common stock (open-market buys and sells, share grants).
- **Table II — Derivative Securities**: options, warrants, RSUs, and convertibles, including exercises and conversions.

Each line carries a **transaction code** that tells you *what kind* of trade it was — and this is the single most important field to read:

- **P — open-market or private Purchase** (the insider chose to spend their own cash; the strongest bullish tell).
- **S — open-market or private Sale**.
- **A — grant, award, or other acquisition** (compensation, not a conviction buy).
- **M — exercise of a derivative** such as options or RSUs.
- **F — shares withheld to pay taxes** on a vesting (mechanical, not a discretionary sale).
- **G — gift**; **C — conversion** of a derivative.

The form also shows the price, the number of shares, and the insider's **total holdings after the transaction**, plus whether ownership is "direct" or "indirect" (e.g., through a trust).

## What an Investor Looks For

- **Open-market purchases (code P), not grants or option exercises.** An executive spending personal cash to buy shares is a far stronger signal than receiving a stock award (code A) or exercising options (code M).
- **Cluster buying.** Several different insiders buying within a short window — especially across the CEO, CFO, and multiple directors — historically carries more signal than a single isolated purchase.
- **Size relative to the insider's wealth and existing stake.** A purchase that meaningfully increases an insider's holdings is more telling than a token buy.
- **Sales context.** Insider *selling* is noisier than buying — executives sell for diversification, taxes, or liquidity, and much selling is pre-scheduled under a **Rule 10b5-1 plan** (a checkbox on the form). Routine 10b5-1 sales are weak signals; large, unscheduled, opportunistic sales are more notable.
- **The "F" and "M" codes.** Tax-withholding (F) and option-exercise (M) lines are mechanical and should usually be filtered out before drawing any conclusion.

The academic basis for watching insider buying is long-standing (e.g., Lakonishok & Lee, 2001, "Are Insider Trades Informative?"), but the edge has compressed as the data became free and widely scraped — see [[insider-trading]] for the detail.

## Timing and Cadence

Form 4 must be filed **within two business days** of the transaction, electronically through [[edgar|EDGAR]], where it becomes public almost immediately. There is no fixed calendar — filings appear whenever insiders trade — so, like the [[8-k|8-K]], it is consumed as a real-time stream rather than a periodic report.

## Common Pitfalls

- **Treating all "buys" the same.** A grant (A) or option exercise (M) is not the same as an open-market purchase (P). Read the transaction code before reacting.
- **Over-reading insider selling.** Insiders sell for many benign reasons; absent unusual size or timing, a sale — especially a scheduled 10b5-1 sale — is a weak signal.
- **Ignoring 10b5-1 plans.** Pre-arranged trading plans remove discretion from the transaction, so they carry little informational content even though they appear on the form.
- **Chasing stale signals.** The two-day reporting lag plus widespread scraping means the obvious cluster-buying signal is often already in the price by the time a retail screener surfaces it.
- **Confusing legal disclosure with illegal trading.** A Form 4 is evidence of *permitted* trading; it is not, by itself, evidence of [[insider-trading|insider dealing]]. The two are opposites in legality.

## A Hypothetical Example

Imagine **XYZ Corp** (fictional). Over three trading days its CEO, CFO, and two independent directors each file Form 4s reporting **code P** open-market purchases totalling several million dollars, none of them under a 10b5-1 plan, each meaningfully increasing the insider's personal stake. That cluster of discretionary, cash-funded buying — visible on EDGAR within two business days — is the textbook bullish insider pattern. Contrast this with a single Form 4 showing the CFO selling shares under **code F** to cover taxes on a vesting grant: mechanical, scheduled, and essentially no signal at all. Reading the transaction codes is what separates the two interpretations.

## Related

- [[insider-trading]] — the legal/illegal distinction; Form 4 reports the *legal* transactions
- [[edgar]] — the real-time feed where Form 4s publish
- [[sec]] — the regulator and the Section 16 framework
- [[8-k]] — another real-time disclosure to cross-check against insider activity
- [[10-k]] — the annual report whose Part III covers insider ownership
- [[information-arbitrage]] — building signals from public insider-flow data
- [[event-driven-trading]] — strategies that trade around disclosed insider and corporate events
- [[fundamental-analysis]] — insider conviction as one input among many

## Sources

- SEC, Form 4 and "Fast Answers: Forms 3, 4, 5" (sec.gov) — official description of Section 16 reporting and transaction codes.
- Securities Exchange Act of 1934, Section 16 — statutory basis for insider reporting and short-swing-profit rules; SEC Rule 10b5-1 for pre-arranged trading plans.
- Lakonishok, J. & Lee, I. (2001), "Are Insider Trades Informative?" *Review of Financial Studies* 14(1) — evidence on the signal value of legal insider transactions.
