---
title: Genesis Global
type: entity
entity_type: company
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags:
  - crypto
  - lending
  - collapse
aliases:
  - genesis
  - genesis-trading
  - genesis-global
related: ["[[ftx]]", "[[three-arrows-capital]]", "[[digital-currency-group]]", "[[contagion]]", "[[counterparty-risk]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Genesis Global

**Genesis Global** (Genesis Global Capital / Genesis Trading) was a major cryptocurrency **prime broker and lender** serving institutional clients. A subsidiary of [[digital-currency-group|Digital Currency Group (DCG)]], it was for years the dominant institutional lending desk in crypto. Genesis collapsed in the [[crypto-winter|crypto winter]] of 2022–2023, halting withdrawals in November 2022 after the [[ftx|FTX]] failure and filing for Chapter 11 bankruptcy in January 2023. Its downfall is a textbook case of [[contagion|lending contagion]] and concentrated [[counterparty-risk]] in an interconnected crypto credit system.

## Business Model and Scale

Genesis was the lending and trading arm of [[digital-currency-group|DCG]], the crypto conglomerate that also owns **Grayscale Investments** (issuer of the Grayscale Bitcoin Trust, GBTC) and, formerly, **CoinDesk**. At its peak Genesis facilitated over **$200 billion** in cumulative crypto loans and offered OTC spot trading, derivatives, custody, and lending to hedge funds, trading desks, and other institutions.

Its core lending engine acted as a **maturity- and credit-transforming intermediary**: it borrowed crypto and dollars from retail-facing programs (most importantly **Gemini's "Earn"** product) and from other institutions, and lent to leveraged borrowers, earning the spread. This works in a bull market but concentrates [[counterparty-risk]] — a few large borrowers and a thin equity cushion against losses.

### The DCG group structure

Genesis did not operate in isolation; it sat inside a tightly interlinked conglomerate, which is central to why its failure was so damaging:

| Entity | Role within DCG | Link to Genesis |
|--------|-----------------|-----------------|
| **Digital Currency Group (DCG)** | Parent holding company | Owner; issued the ~$1.1B promissory note |
| **Genesis Global Capital** | Lending desk | The insolvent entity that filed Chapter 11 |
| **Genesis Global Trading** | OTC / spot trading arm | Wound down separately |
| **Grayscale Investments** | Asset manager, issuer of GBTC | Sibling; GBTC discount fed group stress |
| **CoinDesk** | Media (later sold) | Sibling; sale helped DCG raise cash |

Because these balance sheets were intertwined — Genesis was both a major DCG asset and a DCG debtor — problems at the lending desk threatened the value of the whole group, and vice versa.

## The Collapse

| Date | Event |
|------|-------|
| **Jun 2022** | [[three-arrows-capital|Three Arrows Capital (3AC)]] defaults; Genesis is left with a **~$1.2B** loss on loans to 3AC |
| **Jun–Jul 2022** | Parent [[digital-currency-group|DCG]] assumes the 3AC liability via a ~$1.1B promissory note, papering over but not curing the hole |
| **Nov 2022** | [[ftx|FTX]] collapses; Genesis has additional exposure and faces a run; it **halts withdrawals** on its lending platform on Nov 16, 2022 |
| **Jan 19, 2023** | Genesis Global Capital files for **Chapter 11 bankruptcy** with liabilities estimated at ~**$3.4B** |
| **2023–2024** | Litigation with Gemini and DCG; SEC charges Genesis and Gemini over the unregistered "Earn" program; settlement returns assets to creditors |

The largest creditor group was roughly **340,000 users of Gemini Earn**, who had deposited crypto with Gemini that was then lent to Genesis. After protracted negotiations and litigation, the bankruptcy plan ultimately aimed to return assets to creditors, with Gemini stating Earn users would recover the full amount of their original crypto-denominated claims in kind.

### Litigation and enforcement

The collapse spawned a web of legal actions that illustrate the regulatory and counterparty fallout:

| Actor | Action |
|-------|--------|
| **SEC** | Charged Genesis and **Gemini** (Jan 2023) over the unregistered offer/sale of securities via the Gemini Earn program; Genesis later agreed to a settlement |
| **NYAG (New York Attorney General)** | Sued Genesis, Gemini, and DCG for allegedly defrauding Earn investors; secured a settlement directing funds back to investors |
| **Gemini vs. Genesis/DCG** | Disputes over collateral (notably GBTC shares pledged against Earn loans) and the terms of creditor recovery |
| **Genesis bankruptcy estate vs. DCG** | Claims to claw back value from the parent over intercompany loans and the 3AC promissory note |

The recurring theme is that **retail yield products were treated by regulators as unregistered securities**, and that intercompany loans between affiliates became contested assets in bankruptcy.

## Why It Matters — Contagion

The Genesis failure is the clearest illustration of how interconnected the 2022 [[crypto-winter|crypto winter]] became. A single chain of leverage ran: [[terra-luna|Terra/LUNA]] collapse (May 2022) → [[three-arrows-capital|3AC]] insolvency (June 2022) → losses at lenders including Genesis, Celsius, and Voyager → the [[ftx|FTX]] failure (November 2022) → the final destruction of the institutional lending layer itself. Each domino transmitted losses through **uncollateralized or under-collateralized lending** and shared exposures, the defining feature of crypto [[contagion]].

## Genesis vs. Other 2022 Lender Failures

Genesis was one of several centralized lenders that collapsed in the same wave; comparing them clarifies the shared failure mode:

| Lender | Filed | Headline cause | Notable feature |
|--------|-------|----------------|-----------------|
| **Celsius** | Jul 2022 | Risky DeFi yield-chasing, illiquid CEL token, leverage | Retail-facing; "Earn" marketing; rehypothecation |
| **Voyager Digital** | Jul 2022 | Concentrated loan to [[three-arrows-capital|3AC]] | Acquired/wound down post-bankruptcy |
| **BlockFi** | Nov 2022 | [[ftx|FTX]]/Alameda exposure after FTX bailout line | Earlier SEC settlement over its lending product |
| **Genesis** | Jan 2023 | 3AC default + FTX run; Gemini Earn funding | **Institutional** desk inside [[digital-currency-group|DCG]] |

The common pattern: **uncollateralized or under-collateralized lending funded by retail yield products, with concentrated counterparty exposure and no lender-of-last-resort.** Genesis was distinctive in being the *institutional* layer — the desk that other desks borrowed from — so its failure removed the connective tissue of crypto credit.

## Trading and Risk Lessons

1. **Counterparty concentration is the real risk in crypto lending.** A handful of borrowers (3AC) and one funding source (Gemini Earn) were enough to bring down the largest desk.
2. **Parent-company backstops are not capital.** DCG's promissory note absorbed the 3AC loss on paper but left Genesis structurally insolvent.
3. **"Earn" yield is credit risk in disguise.** Retail yield products were a senior claim on an opaque, leveraged loan book — and regulators later deemed several of them unregistered securities.
4. **Affiliated structures amplify stress.** Genesis, Grayscale, and DCG's intertwined balance sheets meant problems at one threatened the GBTC discount and the whole group.
5. **Opacity hides leverage until the run.** Off-exchange institutional lending had little public reporting, so the scale of interlinked exposure was invisible until withdrawals were halted — the on-chain transparency traders rely on does not extend to CeFi balance sheets.

## Related

- [[ftx]] — its November 2022 collapse triggered the run on Genesis
- [[three-arrows-capital]] — the ~$1.2B default that first holed Genesis's balance sheet
- [[digital-currency-group]] — Genesis's parent conglomerate
- [[contagion]] — the dynamic Genesis exemplifies
- [[counterparty-risk]] — the core exposure that sank the firm
- [[crypto-winter]] — the 2022–2023 cascade Genesis was part of

## Sources

- General market knowledge; no specific wiki source ingested yet.
