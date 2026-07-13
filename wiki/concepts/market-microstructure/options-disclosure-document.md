---
title: "Options Disclosure Document"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [regulation, options, education]
aliases: ["ODD", "Characteristics and Risks of Standardized Options"]
domain: [regulation, options, market-microstructure]
difficulty: beginner
related: ["[[occ]]", "[[finra]]", "[[sec]]", "[[memx]]", "[[regulation]]", "[[equity-options]]", "[[options-greeks]]", "[[assignment]]", "[[flex-options]]"]
---

The Options Disclosure Document (ODD), formally titled *Characteristics and Risks of Standardized Options*, is the FINRA/SEC-mandated risk disclosure that brokers must deliver to every retail customer before approving them to trade exchange-listed options. It is published and maintained by [[occ|The Options Clearing Corporation (OCC)]] on behalf of the US options exchanges, and is the legal source-of-truth for what risks the customer was warned about prior to opening an options-enabled account.

## Overview

The ODD exists because options carry asymmetric and sometimes unbounded risks that ordinary equity disclosures do not address — gamma exposure, assignment risk, total loss of premium, and unlimited loss potential for uncovered writers. FINRA Rule 2360 and SEC rules require that the current ODD be furnished to a customer at or prior to the time the account is approved for options trading, and that customers receive any subsequent supplements within the regulatory delivery window. Brokers maintain delivery records as compliance evidence.

The master document is amended over time through numbered **supplements** rather than full reprints. Supplements are issued as the listed-options landscape changes — new exchanges, new product types, settlement-cycle changes, exercise-procedure updates — and are eventually folded into a consolidated reissue.

## What It Covers

The ODD is organized as a series of chapters describing the structure and risks of each major standardized options product category:

- **Standardized options characteristics** — contract size, strike intervals, expirations, exercise styles (American vs European), the role of the OCC as central counterparty.
- **Settlement rules** — physical delivery for most equity options; cash settlement for index, certain ETF, and FLEX options; exercise-by-exception thresholds.
- **Types of options covered:**
  - Equity options
  - Index options
  - Debt options (interest-rate products)
  - Foreign currency options
  - Cash-settled and physically-settled FLEX options
- **Tax considerations** — high-level summary of US federal tax treatment, including Section 1256 60/40 treatment for broad-based index options.
- **Principal risks** — total loss of premium, leverage, liquidity risk, early assignment, exercise cutoffs, corporate-action adjustments, dividend risk on short calls.
- **Special statements for uncovered option writers** — explicit warning that naked short calls have theoretically unlimited loss, and naked short puts have loss limited only by the underlying going to zero. This is a separately-acknowledged section that brokers typically gate behind a higher options-approval level.

## Recent Updates (June 2024)

The June 2024 ODD revision is the most material update in recent memory for active traders and compliance teams:

- **MEMX LLC added as a listed options market** — [[memx|MEMX Options]] was added to the enumerated list of US options exchanges in the ODD, reflecting MEMX's launch of an options exchange and the further fragmentation of US options venue routing. Brokers and order-routing systems referencing the ODD's exchange list had to update accordingly.
- **T+1 settlement clarification** — The ODD was updated to reflect the move to **T+1 settlement for options-related cash flows**, aligning with the broader US securities transition from T+2 to T+1 that took effect in May 2024. Premium payments and exercise-related settlements now follow the T+1 cycle.
- **Cash-settled FLEX options supplement** — Earlier 2024 supplements added language covering cash-settled [[flex-options|FLEX options]], a category that had grown in institutional usage and required clearer retail-facing disclosure.
- **Exercise-procedure language** — Modifications around exercise-by-exception mechanics and timing windows were tightened to reflect current OCC operational practice.

Per OCC convention, these changes were first issued as numbered supplements appended to the existing master document before being merged into the next consolidated reissue.

## Why It Matters for Traders

1. **Account approval prerequisite** — A broker cannot legally approve a retail customer for options trading until the current ODD has been delivered (electronically or on paper). New customers will see ODD acknowledgment as a step in any options-application flow at IBKR, Schwab, Fidelity, E*TRADE, Webull, Robinhood, tastytrade, and others.
2. **Legal source-of-truth for disclosed risks** — In any dispute, arbitration, or FINRA complaint about losses in an options account, the broker's defense will reference the ODD as evidence the customer was warned of the relevant risk. Reading it materially changes one's standing in such a dispute.
3. **Compliance reference** — Compliance officers, registered options principals (ROPs), and broker reps reference the ODD when answering customer questions about settlement, assignment mechanics, exercise procedures, and corporate-action adjustments.
4. **Tracking regulatory and structural change** — Because supplements are issued whenever the listed-options ecosystem changes, monitoring ODD supplements is a low-effort way to track:
   - New exchange entrants (e.g., MEMX in 2024)
   - Settlement-cycle shifts (e.g., T+2 to T+1)
   - New eligible product categories (e.g., expanded FLEX coverage)
   - Changes to exercise-by-exception thresholds
5. **Counterparty understanding** — The ODD is also where the role of the [[occ|OCC]] as central counterparty and guarantor is explained, which matters for any trader thinking about clearing-system risk.

## How To Access

The current ODD and all supplements are published on the OCC website:

- **Primary URL:** <https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document>

The OCC page hosts:
- The consolidated master document (PDF)
- All numbered supplements issued since the last consolidation
- Translated versions (e.g., Spanish, Chinese) where applicable

Brokers also embed or link the current ODD inside their options-application workflows. When a new supplement is issued, brokers are required to deliver it to existing options-approved customers within the prescribed window, typically by email with a link to the OCC-hosted document.

## Related

- [[occ]] — the publisher and central clearing counterparty for all US listed options
- [[finra]] — the SRO whose Rule 2360 mandates ODD delivery
- [[sec]] — the federal regulator whose rules underpin options-customer disclosures
- [[memx]] — added to the ODD's listed-exchange roster in the June 2024 revision
- [[flex-options]] — covered in dedicated ODD supplements, including 2024 cash-settled FLEX language
- [[equity-options]] — the most common product category covered by the ODD
- [[options-greeks]] — risk dimensions the ODD describes in plain-English terms
- [[assignment]] — early-assignment risk is a key principal-risks topic in the ODD
- [[regulation]] — broader US securities-regulation context

## Sources

- The Options Clearing Corporation, *Characteristics and Risks of Standardized Options* — <https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document>
- FINRA Rule 2360 (Options) — delivery requirements for the ODD
- OCC ODD Supplement series, 2024 revisions (MEMX listing, T+1 settlement, cash-settled FLEX)

_No raw sources ingested into `raw/` for this page; content based on the public OCC ODD page and FINRA rule references. Verify current supplement numbering on the OCC site before citing in any compliance context._
