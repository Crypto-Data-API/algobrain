---
title: Rehypothecation
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - leverage
  - risk-management
  - margin
aliases:
  - rehypothecation
  - re-pledging
  - collateral reuse
domain: [market-microstructure]
prerequisites: ["[[margin]]", "[[securities-lending]]"]
difficulty: advanced
related:
  - "[[securities-lending]]"
  - "[[leverage]]"
  - "[[counterparty-risk]]"
  - "[[margin]]"
  - "[[shadow-banking]]"
  - "[[dodd-frank-act]]"
---

# Rehypothecation

**Rehypothecation** is the practice in which a broker, dealer, or other financial intermediary re-uses collateral that a client has pledged to it — typically securities posted to secure a [[margin]] loan or prime-brokerage relationship — to fund the intermediary's own borrowing, [[securities-lending]], or trading activity. It is the engine that turns a single pool of client assets into multiple overlapping claims, and is one of the most important amplifiers of [[leverage]] in the financial system.

## Hypothecation vs. Rehypothecation

- **Hypothecation** is the original pledge: a client pledges an asset as collateral while retaining ownership (e.g., posting shares to back a margin loan). The lender gains a lien but not title.
- **Rehypothecation** is the second-order move: the lender, now holding that collateral, re-pledges it to a third party to secure its *own* financing. That third party may rehypothecate again, producing a **collateral chain** in which the same underlying asset backs several layers of borrowing simultaneously.

## How It Works

A typical chain in prime brokerage:

1. A hedge fund posts $100m of securities as collateral to its prime broker for a margin loan.
2. The prime broker rehypothecates those securities — lending them out via [[securities-lending]] to short sellers, or posting them as collateral to a bank to fund its own balance sheet.
3. The receiving party may further re-pledge the same assets.

Each link adds [[leverage]] because the same collateral supports new credit at every step. Economists describe the resulting multiplier as **collateral velocity** — the number of times a unit of collateral is reused across the system. The higher the velocity, the more credit a fixed pool of assets can support, and the more fragile the chain becomes when one link fails.

## Regulatory Limits

- **United States:** SEC Rule 15c3-3 caps a broker-dealer's rehypothecation of customer securities at **140% of the customer's debit balance** (the amount the customer actually owes). Fully paid-for securities cannot be rehypothecated at all without explicit consent.
- **United Kingdom / pre-2008:** UK rules historically imposed **no statutory cap**, allowing intermediaries to rehypothecate client assets without limit. This jurisdictional gap was central to the Lehman failure.

## The Lehman Brothers Example

The collapse of **Lehman Brothers** in September 2008 exposed rehypothecation risk on a systemic scale. Lehman's London entity (LBIE) rehypothecated client assets aggressively under the permissive UK framework. When Lehman filed for bankruptcy, prime-brokerage clients discovered their collateral had been re-pledged into chains entangled in the insolvency estate — converting what clients believed were segregated assets into unsecured claims. The litigation ran for years and contributed to a sharp, system-wide contraction in collateral reuse as funds pulled assets from prime brokers.

## Trading Relevance

- **Counterparty risk assessment:** A trader's collateral posted to a broker is only as safe as the chain it enters. In a default, rehypothecated assets can become part of the bankruptcy estate rather than being returned. This is the core of [[counterparty-risk]] for leveraged traders and is why funds diversify prime brokers and negotiate caps on reuse.
- **Short-squeeze fragility:** Rehypothecation in [[securities-lending]] is part of how aggregate [[short-interest]] can exceed 100% of a stock's [[float]] — the same shares are lent, sold short, re-borrowed, and lent again. This dynamic was visible in the [[gamestop-short-squeeze]].
- **Systemic signal:** Falling collateral velocity (as measured in IMF and BIS studies) is a deleveraging indicator — it tightens funding conditions across the [[shadow-banking]] system even when central-bank rates are unchanged.
- **Crypto parallel:** The 2022 failures of **FTX**, Celsius, and Voyager were, in substance, uncontrolled rehypothecation of customer deposits — reused as collateral for the platforms' own trading. This drove the post-2022 push toward [[self-custody]] and proof-of-reserves.

## Regulatory Response

Post-2008 reforms tightened collateral-reuse rules. The [[dodd-frank-act]] and parallel EU regulation (notably SFTR, the Securities Financing Transactions Regulation) imposed reporting requirements and consent rules on rehypothecation. The Financial Stability Board has repeatedly flagged collateral reuse as a [[shadow-banking]] vulnerability requiring ongoing monitoring.

## Related

- [[securities-lending]]
- [[leverage]]
- [[counterparty-risk]]
- [[margin]]
- [[shadow-banking]]
- [[dodd-frank-act]]

## Sources

- US Securities and Exchange Commission, Rule 15c3-3 (Customer Protection — Reserves and Custody of Securities).
- Singh, Manmohan. "Velocity of Pledged Collateral: Analysis and Implications." IMF Working Paper WP/11/256 (2011).
- Financial Stability Board, "Strengthening Oversight and Regulation of Shadow Banking" (2013), section on rehypothecation and collateral reuse.
- Court filings and analyses of Lehman Brothers International (Europe) administration, 2008–2014.
