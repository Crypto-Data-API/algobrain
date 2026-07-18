---
title: "Stablecoin Attestation Standards"
type: concept
created: 2026-04-09
updated: 2026-06-11
status: good
tags: [stablecoins, regulation, risk-management]
aliases: ["Stablecoin Attestations", "Reserve Attestation"]
domain: [risk-management]
difficulty: intermediate
related: ["[[usdc]]", "[[usdt]]", "[[circle]]", "[[blackrock]]", "[[stablecoins]]", "[[stablecoin-regulation]]", "[[stablecoin-depegs]]"]
---

# Stablecoin Attestation Standards

**Reserve attestations** are third-party reports that verify a stablecoin issuer holds sufficient reserves to back all tokens in circulation. They are the primary mechanism by which fiat-backed [[stablecoins]] demonstrate that each token is redeemable 1:1 for the underlying currency. The quality, frequency, and scope of these attestations vary dramatically between issuers and are a key risk factor for traders.

## Attestation vs Audit

This distinction is critical and frequently misunderstood:

| | Attestation | Full Audit |
|---|---|---|
| **Scope** | Point-in-time snapshot of specific claims | Comprehensive review of financial statements and controls |
| **Depth** | "Reserves exceed liabilities as of date X" | Examines internal controls, transactions, counterparty risk |
| **Standard** | AICPA AT-C 205 (examination) | GAAS / PCAOB standards |
| **Duration** | Completed in days-weeks | Takes months |
| **Limitation** | Does not verify what happens between report dates | Covers an entire reporting period |
| **Cost** | Lower | Significantly higher |

**No major stablecoin issuer has undergone a full audit** as of early 2026. All publish attestations, not audits.

## Issuer Comparison

| Issuer | Stablecoin | Attestor | Frequency | Quality Rating |
|--------|-----------|----------|-----------|----------------|
| [[circle|Circle]] | [[usdc|USDC]] | **Deloitte** (Big Four) | Monthly | HIGH |
| [[tether-limited|Tether]] | [[usdt|USDT]] | **BDO Italia** (mid-tier) | Quarterly | MEDIUM |
| PayPal | [[pyusd|PYUSD]] | **Withum** (mid-tier) | Monthly | MEDIUM-HIGH |
| MakerDAO | [[dai|DAI]] | On-chain verifiable | Real-time | HIGH (transparent) |
| Paxos | USDP | **Withum** | Monthly | MEDIUM-HIGH |

### USDC (Circle / Deloitte)

- **Monthly** attestation reports by Deloitte, a Big Four firm
- Reports confirm reserves equal or exceed USDC in circulation
- Reserve composition disclosed: US Treasuries (via [[blackrock|BlackRock]] Circle Reserve Fund) and regulated bank deposits
- Most transparent and frequent reporting of any major centralized stablecoin

### USDT (Tether / BDO Italia)

- **Quarterly** attestation reports by BDO Italia, a mid-tier accounting firm
- Reports confirm reserves exceed liabilities but reserve composition has changed over time
- Historically held commercial paper (phased out by 2023), now primarily US Treasuries
- Tether has faced regulatory actions related to transparency: $18.5M NYAG settlement (2021), $41M CFTC fine (2021)
- Has never engaged a Big Four firm for attestation

## Why Attestation Quality Matters for Trading

1. **De-peg risk**: Lower transparency increases the risk of confidence crises (see [[stablecoin-depegs]])
2. **Regulatory compliance**: [[stablecoin-regulation|Regulations]] like MiCA require specific reserve standards — attestation quality determines compliance
3. **Counterparty risk**: Traders holding large stablecoin positions need to assess the reliability of the backing claims
4. **Market pricing**: During stress events, USDC and USDT trade at different premiums/discounts partly reflecting perceived attestation credibility

## Limitations of Current Standards

- Attestations are point-in-time — they don't capture intraday reserve movements or lending between attestation dates
- No standardized framework existed specifically for stablecoin attestations until recently (see AICPA criteria below)
- The attestor's reputation matters: Big Four firms face greater reputational and legal risk from false attestations than smaller firms
- On-chain stablecoins like [[dai|DAI]] offer real-time verifiability that centralized attestations cannot match

## The Emerging Standard: AICPA Stablecoin Reporting Criteria

The "no standardized framework" gap is now being closed. The **AICPA** (American Institute of CPAs) published dedicated **criteria for reporting on stablecoins** in March 2025, then expanded them in January 2026 to add **controls criteria over token operations** (minting, burning, and reserve management), not just a point-in-time reserve-sufficiency snapshot. This is the first purpose-built assurance framework for stablecoins; previously attestors applied the generic AT-C 205 examination standard. As these criteria are adopted, traders should expect attestation *scope* (not just frequency) to become a differentiator between issuers.

Even with this framework, the attestation-vs-audit gap remains: as of mid-2026 no major fiat-backed issuer has completed a full GAAP financial-statement audit — they publish attestations under examination standards, which is a narrower assurance product than an audit.

> **Note on regulation:** US federal stablecoin legislation and the EU's [[mica|MiCA]] regime impose their own reserve and reporting obligations on issuers; the exact statutory attestation/audit requirements are tracked on [[stablecoin-regulation]] and should be confirmed there rather than assumed from accounting-standard developments alone.

## Related

- [[usdc]] — Monthly Deloitte attestations, gold standard for centralized stablecoins
- [[usdt]] — Quarterly BDO Italia attestations, controversy over transparency
- [[stablecoin-regulation]] — Regulatory frameworks mandating reserve standards
- [[stablecoin-depegs]] — When confidence in reserves breaks down
- [[blackrock]] — Manages Circle Reserve Fund backing USDC
- [[stablecoins]] — Overview of the stablecoin ecosystem

## Sources

- AICPA, *Criteria for the description and design of controls relevant to stablecoin reporting* (March 2025; expanded January 2026) — first purpose-built assurance framework for stablecoin issuers (aicpa-cima.com)
- AICPA AT-C section 205, *Assertion-Based Examination Engagements* — the generic examination standard under which existing reserve attestations are performed
- Circle, monthly USDC reserve attestation reports (Deloitte) and Circle Reserve Fund disclosures (managed by [[blackrock|BlackRock]])
- Tether, quarterly USDT reserve attestation reports (BDO Italia)
- NYAG (2021, $18.5M) and CFTC (2021, $41M) settlements with Tether regarding reserve-disclosure representations
- See [[stablecoin-regulation]] for the statutory (US federal and EU [[mica|MiCA]]) reserve and reporting obligations

> Verification note (2026-06-11): the attestation-not-audit framing, Circle's Deloitte monthly cadence, and the existence of the 2025/2026 AICPA stablecoin criteria are corroborated by current sources. Tether's BDO Italia / quarterly cadence reflects Tether's own published reports and prior reporting; confirm the current attestor on each issuer's latest transparency page before relying on it for a live trade.
