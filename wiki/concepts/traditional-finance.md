---
title: "Traditional Finance (TradFi)"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [defi, crypto, market-microstructure, education]
aliases: ["TradFi", "traditional finance", "CeFi", "legacy finance", "traditional-finance"]
domain: [market-microstructure]
prerequisites: ["[[defi]]"]
difficulty: beginner
related: ["[[defi]]", "[[forex]]", "[[bonds]]", "[[options-overview]]", "[[macroeconomics]]", "[[market-microstructure]]", "[[cefi-yield-vs-defi-yield]]"]
---

**Traditional finance (TradFi)** refers to the established, intermediated financial system — banks, broker-dealers, stock exchanges, clearing houses, central banks, and regulators — that channels the majority of global capital. The term is used chiefly as a contrast to [[defi|decentralized finance]] and crypto-native systems. The defining distinction is **trust architecture**: TradFi relies on trusted intermediaries (banks, custodians, regulators) backed by the legal system, while DeFi aims to replace them with smart contracts and on-chain logic ("trustless" / "code is law").

## TradFi, CeFi, and DeFi

The crypto ecosystem usually distinguishes three tiers:

- **TradFi** — the legacy banking and securities system (JPMorgan, NYSE, the Fed).
- **CeFi (centralized finance)** — crypto-native but still custodial and company-operated (centralized exchanges like Coinbase, lenders like the former Celsius/BlockFi). CeFi reintroduces an intermediary's counterparty risk on crypto rails.
- **DeFi** — non-custodial, permissionless protocols (Uniswap, Aave) where users retain custody and rules execute on-chain.

"TradFi" and "CeFi" both denote intermediated systems, but TradFi specifically means the regulated, fiat-denominated legacy world.

## Key Differences: TradFi vs. DeFi

| Dimension | TradFi | DeFi |
|-----------|--------|------|
| **Intermediation** | Banks, brokers, custodians | Smart contracts, protocols |
| **Settlement** | T+1 (US equities since 2024), T+0–T+2 (FX) | Near-instant (block confirmation) |
| **Trading hours** | Market hours (9:30–16:00 ET for US equities) | 24/7/365 |
| **Identity** | KYC/AML required | Pseudonymous (wallet addresses) |
| **Custody** | Custodians hold assets (DTCC, banks) | Self-custody or smart-contract custody |
| **Regulation** | Extensive (SEC, CFTC, FCA, ASIC) | Emerging, fragmented |
| **Recourse** | Legal system, insurance (FDIC, SIPC) | Limited — "code is law," exploits often irreversible |
| **Leverage** | Regulated margin (Reg T: 50% initial) | Often unconstrained (100x+ perps) |
| **Access** | Accredited-investor gates on some products | Permissionless (anyone with a wallet) |
| **Failure mode** | Bank run, clearing failure, fraud | Smart-contract exploit, oracle manipulation, depeg |

## Convergence

The TradFi/DeFi boundary is blurring rapidly:

- **Tokenized treasuries and money funds** (BlackRock BUIDL, Ondo, Franklin's BENJI) bring TradFi yield on-chain.
- **Spot Bitcoin and Ether ETFs** (approved 2024) bring crypto into TradFi brokerage accounts.
- **Institutional / permissioned DeFi** (Aave Arc, Maple) layers KYC/AML onto DeFi protocols.
- **CBDC and tokenized-deposit projects** apply distributed-ledger technology inside central-bank and bank frameworks.
- **Stablecoins** sit at the seam — fiat-backed claims (TradFi balance sheets) transacting on DeFi rails.

## Trading Relevance

- **Arbitrage between systems.** Funding-rate and basis differences between TradFi futures (CME) and DeFi perps, and yield gaps between TradFi T-bills and on-chain stablecoin yields, are persistent arbitrage targets (see [[cefi-yield-vs-defi-yield]]).
- **Counterparty-risk mapping.** Knowing whether a venue is TradFi (segregated custody, SIPC), CeFi (custodial, company solvency risk — the FTX/Celsius failures), or DeFi (smart-contract risk) is the first risk question for any crypto position.
- **Macro linkage.** As tokenized treasuries and ETFs grow, crypto markets become more sensitive to TradFi rates and [[fed-policy]], reducing the historical "uncorrelated" narrative.
- **Settlement and operational edge.** TradFi's T+1 cycle and limited hours create gaps DeFi's 24/7 settlement can exploit (weekend gaps, after-hours repricing).

## Related

- [[defi]] — decentralized finance, the primary contrast to TradFi
- [[cefi-yield-vs-defi-yield]] — comparison of intermediated vs. on-chain yield
- [[forex]] — TradFi foreign exchange
- [[bonds]] — TradFi fixed income
- [[macroeconomics]] — the macro framework TradFi operates within
- [[market-microstructure]] — how TradFi venues actually clear and settle

## Sources

- BIS, *Annual Economic Report* — on tokenization and the financial system.
- General financial-market reference knowledge; FTX/Celsius collapses (2022) for the CeFi counterparty-risk distinction.
