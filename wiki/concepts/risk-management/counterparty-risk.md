---
title: Counterparty Risk
type: concept
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [risk-management, counterparty-risk, credit-risk]
aliases: [counterparty credit risk, default risk]
related:
  - "[[systemic-risk]]"
  - "[[liquidity-risk]]"
  - "[[insurance-fund]]"
  - "[[black-swan]]"
---

# Counterparty Risk

Counterparty risk is the possibility that the other party in a financial transaction will fail to fulfill their obligations, whether through default, insolvency, or fraud.

## Where It Appears

- **OTC Derivatives** - Uncleared swaps and forwards depend on the counterparty's ability to pay
- **Brokerage/Exchange** - Your broker or exchange holds your funds and must remain solvent
- **Lending/Borrowing** - DeFi protocols and prime brokers carry counterparty exposure
- **Settlement** - Between trade execution and settlement, either party could default

## Notable Failures

- **Lehman Brothers (2008)** - Counterparties holding Lehman OTC derivatives faced massive losses
- **MF Global (2011)** - Brokerage misused customer funds, leaving traders unable to access their capital
- **FTX (2022)** - Crypto exchange collapsed, and customers lost billions in deposited funds
- **Archegos Capital (2021)** - Prime brokers took billions in losses from a single client's default

## Trading Relevance

Counterparty risk is often invisible until it materializes. Traders should:

- Diversify across multiple brokers and exchanges
- Prefer regulated, well-capitalized institutions
- Understand whether an [[insurance-fund]] or deposit insurance covers their assets
- Minimize funds held on any single platform beyond what is needed for active trading
- Use central clearinghouses when available (reduces bilateral counterparty exposure)

## Crypto-Specific Considerations

In crypto markets, counterparty risk is elevated due to less regulation, comingling of exchange and customer funds, and the absence of traditional investor protections. "Not your keys, not your coins" reflects this reality.

## Exchange Counterparty Risk Scorecard (April 2026)

For arbitrage strategies requiring capital on multiple venues, quantified risk assessment per exchange is essential. See [[multi-venue-capital-management]] for allocation guidelines based on these scores.

| Exchange | Regulatory | Insurance Fund | Transparency | Clawback Risk | Track Record | **Score** |
|---|---|---|---|---|---|---|
| [[coinbase]] | 10 (Nasdaq-listed, SEC-regulated, NY BitLicense) | 8 (crypto insurance, FDIC for USD) | 9 (public company, audited financials) | 2 (low — regulated entity) | 9 (no major incidents) | **8.5/10** |
| Kraken | 9 (SOC 2, multiple licenses, strong compliance) | 7 (proof of reserves, no published fund size) | 8 (PoR audits, Armanino) | 2 (low) | 9 (no major incidents, 10+ years) | **8.0/10** |
| Deribit | 8 (Panama-based but EU-compliant, Dutch oversight) | 7 (insurance fund, cold storage policy) | 7 (proof of reserves) | 3 (moderate) | 8 (no major incidents, dominant crypto options venue) | **7.5/10** |
| [[hyperliquid]] | 4 (no KYC, no corporate entity, no regulatory framework) | 7 (HLP vault on-chain, transparent balance) | 10 (fully on-chain, auditable) | 1 (no clawback — smart contract governs) | 6 (young platform, 2023 launch, vault losses possible) | **7.0/10** |
| [[binance]] | 6 (DOJ settlement 2023, licensed in some jurisdictions, banned in others) | 8 (SAFU fund ~$1B) | 6 (proof of reserves but corporate opacity) | 5 (socialized loss provisions in ToS) | 7 (no customer fund loss, but regulatory issues) | **6.8/10** |
| OKX | 6 (Seychelles-registered, some jurisdiction licenses) | 7 (proof of reserves) | 6 (PoR, limited audit) | 5 (possible in ToS) | 7 (no major incidents) | **6.5/10** |
| Bybit | 5 (Dubai VARA license, limited regulatory clarity) | 6 (insurance fund exists, size undisclosed) | 5 (PoR, limited detail) | 5 (possible) | 7 (no major incidents) | **6.0/10** |

### Scoring Methodology

| Dimension | Weight | 10 = Best | 1 = Worst |
|---|---|---|---|
| **Regulatory status** | 25% | Public company, multiple tier-1 licenses | No registration, actively evading regulators |
| **Insurance fund** | 20% | Published, adequate (>10x avg daily liquidation volume), independently audited | No fund or undisclosed |
| **Transparency** | 20% | Audited financials, real-time proof of reserves, open-source where possible | Opaque corporate structure, no PoR |
| **Clawback risk** | 15% | No socialized loss provisions, regulated with deposit insurance | Explicit socialized loss clauses, history of clawback |
| **Track record** | 20% | 10+ years, no customer fund losses, clean regulatory history | New (<2 years), unresolved regulatory actions, or history of fund loss |

### Risk-Adjusted Allocation Caps

Based on scores above, recommended maximum allocation per [[multi-venue-capital-management]]:

| Score Range | Risk Tier | Max Allocation (% of arb portfolio) |
|---|---|---|
| 8.0-10.0 | Tier 1 | ≤ 30% |
| 7.0-7.9 | Tier 2 | ≤ 20% |
| 6.0-6.9 | Tier 3 | ≤ 15% |
| 5.0-5.9 | Tier 4 | ≤ 5% |
| < 5.0 | Avoid | 0% (unacceptable counterparty risk) |

### Early Warning Signals

Monitor these for deterioration in any exchange's risk profile:

| Signal | What It Indicates | Action |
|---|---|---|
| Withdrawal delays > 2x normal | Liquidity stress | Reduce exposure by 50% immediately |
| Proof-of-reserves delayed or withdrawn | Transparency erosion | Cap at Tier 4, prepare full withdrawal |
| Regulatory enforcement action filed | Legal/operational risk | Reassess within 24 hours, reduce if material |
| Insurance fund balance declining without disclosure | Systemic losses absorbing buffer | Reduce exposure |
| Executive departures (CFO, compliance) | Internal instability | Heightened monitoring |
| Unusual token movements from exchange wallets | Possible insolvency preparation | Withdraw to minimum trading balance |
| Social media bank-run sentiment | Reflexive risk | Withdraw immediately to safe threshold |
