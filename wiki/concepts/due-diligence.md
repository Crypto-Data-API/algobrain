---
title: "Due Diligence"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, risk-management, valuation, crypto]
aliases: ["Due Diligence", "DD", "DYOR", "Investment Due Diligence"]
related: ["[[rug-detection-checklist]]", "[[risk-management-overview]]"]
domain: [fundamental-analysis, risk-management]
prerequisites: []
difficulty: beginner
---

Due diligence (DD) is the systematic investigation an investor or trader performs to verify the facts, risks, and value of an asset before committing capital. It spans reading financial statements, checking management quality and legal/regulatory exposure, stress-testing the bull case against the bear case, and — in crypto — verifying that a project is not an outright scam. The retail crypto shorthand is **DYOR** ("do your own research"). Skipping due diligence is one of the most reliable ways to lose money.

## Overview

Due diligence is the verification step between an *idea* and a *position*. A thesis ("this stock is cheap", "this token is the next narrative leader") is a hypothesis; due diligence is the evidence-gathering that either confirms it or kills it. The depth scales with the size and illiquidity of the commitment — a day trade in a liquid large-cap needs less than a multi-year position in a micro-cap or a private-market allocation.

It is distinct from, but feeds into, valuation: due diligence establishes whether the *inputs* to a valuation are trustworthy before the valuation itself is performed.

## Domains of due diligence

### Equities / fundamentals

- **Financial-statement review** — income statement, balance sheet, cash-flow statement; reconcile reported earnings against actual cash generation (see earnings-quality).
- **Earnings quality and accounting red flags** — accruals far exceeding cash flow, frequent restatements, aggressive revenue recognition, off-balance-sheet vehicles (earnings-management).
- **Competitive position** — durable advantages, the economic-moat, pricing power, customer concentration.
- **Management and governance** — track record, insider ownership and trading, board independence, related-party transactions.
- **Legal / regulatory** — pending litigation, regulatory investigations, antitrust exposure (relevant to merger-arbitrage deals via hsr-review / ec-merger-regulation).
- **Valuation cross-check** — multiples vs peers and history, scenario / DCF sensitivity.

### Crypto / on-chain (DYOR)

Crypto due diligence is largely adversarial — the base rate of scams is high — and leans on the [[rug-detection-checklist]]:

- **Contract verification** — is the contract source verified and audited? Are mint, blacklist, or honeypot functions present? Can the owner drain liquidity?
- **Tokenomics** — supply schedule, [[token-unlocks|vesting/unlock cliffs]], team/insider allocation, concentration of holdings ([[whale-onchain-flows|whale wallets]]).
- **Liquidity** — is LP locked, and for how long? Depth vs market cap.
- **Team** — doxxed or anonymous; prior projects; reputation.
- **Audits** — by whom, and do the findings actually matter or are they cosmetic.

### Fund / counterparty / operational

- **Manager DD** — strategy, track record, AUM, fee structure, key-person risk.
- **Operational DD** — custody, auditor, fund administrator, segregation of assets. (The lack of this is a recurring theme in blow-ups like FTX and Madoff.)
- **Counterparty / exchange risk** — solvency, proof-of-reserves quality, withdrawal history.

## Trading relevance

- **Asymmetry of error.** A failed due-diligence process rarely costs you the upside you gave up; it costs you the catastrophic, often un-recoverable downside (fraud, insolvency, a rug). DD is therefore primarily a [[risk-management-overview|risk-management]] discipline, not an alpha-generation one.
- **Position sizing follows DD depth.** The conviction earned through thorough due diligence is what justifies a larger allocation; thin DD should map to small, defined-risk exposure.
- **Pre-mortem / disconfirmation.** Good DD actively hunts for the bear case rather than confirming the bull case — a direct antidote to [[confirmation-bias]] and [[overconfidence-bias]].
- **Event-driven trades.** In merger-arbitrage, due diligence on antitrust and financing risk *is* the edge — the spread compensates for the deal-break risk you assess.
- **It is not infallible.** Even rigorous DD can be defeated by outright fraud (falsified statements, fake audits). DD reduces, never eliminates, risk — which is why diversification and sizing remain essential.

## A practical checklist

1. Can I explain the bear case as well as the bull case?
2. Do reported earnings convert into cash? (accruals check)
3. Who is on the other side of this trade, and why are they wrong?
4. What single fact, if false, breaks the thesis — and have I verified it?
5. What is the worst realistic outcome, and can I survive it?
6. (Crypto) Could the team rug me tomorrow, and would I be able to exit?

## Related

- [[rug-detection-checklist]] — the crypto DYOR equivalent
- [[risk-management-overview]] — DD as risk control

## Sources

- Graham & Dodd, *Security Analysis* — the foundational text on investment due diligence.
- Howard Marks, *The Most Important Thing* — second-level thinking and risk-first analysis.
- CFA Institute curriculum, Equity and Alternative Investments readings on manager and operational due diligence.
