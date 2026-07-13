---
title: "Bank Run"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, risk-management, history]
aliases: ["bank runs", "run on the bank", "deposit run"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[liquidity]]", "[[counterparty-risk]]"]
difficulty: beginner
related: ["[[federal-reserve]]", "[[liquidity]]", "[[counterparty-risk]]", "[[2008-global-financial-crisis]]", "[[ftx-collapse]]", "[[liquidity-risk]]", "[[moral-hazard]]"]
---

# Bank Run

A bank run occurs when a large number of depositors simultaneously withdraw their funds from a financial institution due to fears that it will become insolvent. Because banks operate on fractional reserves — lending out most deposits — they cannot satisfy all withdrawal requests at once, making bank runs self-fulfilling prophecies where the fear of failure causes the failure itself.

## Mechanics

Banks typically hold only a fraction (3-10%) of deposits as liquid reserves, lending the rest as mortgages, business loans, and investments. This maturity mismatch — short-term liabilities (deposits that can be withdrawn anytime) funding long-term assets (loans that cannot be recalled) — creates inherent fragility. When confidence erodes, the rational response for each individual depositor is to withdraw immediately, creating a coordination problem that can destroy even solvent institutions.

## Historical Examples

- **1930s Great Depression**: Thousands of U.S. bank failures prompted the creation of FDIC deposit insurance.
- **bear-stearns (2008)**: A modern "institutional bank run" where counterparties and prime brokerage clients pulled assets in 72 hours, collapsing the firm.
- **lehman-brothers (2008)**: Clients and counterparties fled, draining [[liquidity]] and accelerating the bankruptcy.
- **Silicon Valley Bank (2023)**: $42 billion withdrawn in a single day via digital banking, demonstrating how technology accelerates bank runs. Social media amplified the panic.
- **[[ftx-collapse]] (2022)**: A crypto exchange version — user withdrawals triggered a liquidity crisis that exposed fraud and insolvency.

## Contagion

Bank runs rarely stay contained. When one institution fails, depositors at similar institutions preemptively withdraw, creating contagion. The 2023 banking crisis saw SVB's failure quickly spread to Signature Bank and First Republic.

## Trading Relevance

Bank runs create extreme, fast-moving trading opportunities and risks. Monitoring CDS spreads, deposit outflows, and social media panic can provide early warning signals. For traders, understanding that financial institutions are inherently fragile — and that confidence, once lost, is nearly impossible to restore — is a core [[risk-management]] principle. The speed of modern digital bank runs (hours, not days) makes this dynamic more dangerous than ever.

## Related

- [[ftx-collapse]] — a crypto-exchange analog of a deposit run
- [[liquidity]], [[liquidity-risk]] — the underlying vulnerability
- [[counterparty-risk]] — what counterparties flee in a wholesale run
- [[moral-hazard]] — created by deposit insurance and bailouts
- [[federal-reserve]] — lender of last resort

## Sources

- Diamond, D. & Dybvig, P. — "Bank Runs, Deposit Insurance, and Liquidity" (1983), the canonical model of self-fulfilling runs (Nobel 2022)
- Bernanke, B. — *Essays on the Great Depression* (banking panics and the real economy)
- FDIC — public reports on the 2023 failures of Silicon Valley Bank, Signature Bank, and First Republic
- Gorton, G. — *Slapped by the Invisible Hand: The Panic of 2007* (the wholesale/repo run of 2007-2008)
