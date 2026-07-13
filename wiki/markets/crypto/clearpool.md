---
title: "Clearpool"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, lending, ethereum]
aliases: ["CPOOL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://clearpool.finance/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[lending]]", "[[real-world-assets]]", "[[defi]]", "[[aave]]", "[[usdc]]", "[[governance-token]]", "[[solana]]"]
---

# Clearpool

**Clearpool** ([[cpool|CPOOL]]) is a decentralized capital-markets ecosystem where vetted **institutional borrowers** can access **uncollateralized (unsecured) loans** directly from the [[defi]] ecosystem, while liquidity providers earn yield. It is one of the leading [[lending|institutional-credit]] and [[real-world-assets|real-world-asset (RWA)]] protocols, bridging traditional capital markets with on-chain liquidity. Unlike overcollateralized lenders such as [[aave]] or [[compound]], Clearpool's permissioned pools extend credit to whitelisted entities based on off-chain creditworthiness and KYC, making counterparty/credit risk — not just smart-contract risk — central to its model.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Price $0.0212149 · rank #796 · market cap $21,366,847 · 24h -4.13% · 7d -12.78%. Market-wide sentiment: Fear & Greed Index 21 (Extreme Fear).*

As of 2026-06-22, CPOOL trades at **$0.0212149**, ranked **#796** by market capitalization with a market cap of **$21,366,847**. The token fell **-4.13%** over the prior day and **-12.78%** over the week — a sharp underperformance of the broad tape during an Extreme-Fear regime (Fear & Greed Index 21). For a credit-risk-bearing asset, this kind of drawdown is worth watching: CPOOL sentiment is closely tied to perceived borrower-default risk, so an outsized weekly fall can signal either general risk-off pressure or heightened concern about pool/borrower health.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CPOOL |
| **Market Cap Rank** | #796 |
| **Market Cap** | $21,366,847 |
| **Current Price** | $0.0212149 |
| **24h Change** | -4.13% |
| **7d Change** | -12.78% |
| **Primary risk** | Credit / borrower-default risk (uncollateralized lending) |
| **Categories** | Decentralized Finance (DeFi), Real World Assets (RWA), Lending/Borrowing Protocols, Ethereum Ecosystem, Solana Ecosystem, DaoMaker Launchpad, Sequoia Capital Portfolio, Binance Alpha Spotlight, Made in USA |
| **Website** | [https://clearpool.finance/](https://clearpool.finance/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Fear & Greed Index 21 (Extreme Fear). Note the -12.78% 7d drawdown.*

---

## Overview

Clearpool is a decentralized capital markets ecosystem, where institutional borrowers can access unsecured loans directly from the DeFi ecosystem. Clearpool introduces a dynamic interest model driven by market supply and demand forces.

Liquidity providers on Clearpool can earn attractive yields, with pool interest rates enhanced by additional LP rewards paid in CPOOL - Clearpool's utility and governance token.

Clearpool LP tokens, called cpTokens, are the building blocks for a system of tokenized credit that will provide Clearpool LPs with risk management and hedging capabilities.

As more institutions begin to realize the benefits that decentralized finance can bring to their organizations, Clearpool will provide the new architecture to facilitate flows between the $120 trillion traditional capital markets, and the burgeoning DeFi ecosystem.

The CPOOL Token

- CPOOL is the utility and governance token for the Clearpool protocol.
- CPOOL holders will vote on the whitelisting of new borrowers, a process that will qualify participants to earn additional CPOOL through an incentive reward scheme.
- Eventually, a full system of decentralized governance will be introduced, allowing CPOOL holders to propose, vote and implement future changes and upgrades to the protocol.
- CPOOL staking will be a required action for borrowers, who must stake an amount of CPOOL to access the area of the protocol where they can make a proposal to be whitelisted.
Liquidity providers earn additional CPOOL rewards, enhancing pool interest rates to attractive levels.
- Clearpool will announce a buyback program, where a share of protocol revenue will be used to buy CPOOL in the open market, to perpetually sustain reward pools.

---

## Mechanism & Architecture

Clearpool operates two main product lines:

- **Permissionless single-borrower pools** — each whitelisted institutional borrower opens its own pool. Liquidity providers (LPs) deposit stablecoins (e.g., [[usdc]]) and receive **cpTokens** representing their share. A dynamic, utilization-based interest model raises rates as a pool draws down available liquidity, incentivizing LPs and signaling borrower demand. Because the loans are **uncollateralized**, repayment depends on the borrower's solvency and reputation — there is no on-chain collateral to liquidate.
- **Clearpool Prime / Credit Vaults (RWA)** — a permissioned, KYC-gated venue connecting institutional lenders and borrowers for [[real-world-assets|RWA]] and private-credit deals, designed to satisfy compliance requirements that fully open DeFi pools cannot.

**cpTokens** are the building blocks of a tokenized-credit system intended to give LPs risk-management and hedging capabilities. The protocol is multi-chain, with deployments including [[ethereum]] and [[solana]] ecosystems.

### Why this is fundamentally different from Aave/Compound

Overcollateralized lenders like [[aave|Aave]] and [[compound|Compound]] never face credit risk in normal operation: a borrower posts more collateral than they borrow, and if the collateral value falls toward the loan value, the protocol **liquidates** it automatically. The lender's risk is essentially smart-contract and oracle risk, not "will the borrower pay me back."

Clearpool inverts this. Loans are **uncollateralized**, so there is nothing to liquidate. Repayment depends entirely on the borrower's off-chain solvency, reputation and willingness to pay. That trade — accepting [[lending|credit-default risk]] — is precisely what lets Clearpool offer the higher yields and capital-efficient borrowing that traditional [[real-world-assets|RWA]]/private-credit deals require. **Credit risk is the product, not a bug.**

### Worked example (illustrative)

An LP deposits 100,000 [[usdc|USDC]] into a single-borrower pool for an institutional trading firm and receives cpTokens. The pool's **utilization-based** rate means that as the borrower draws the pool down (say to 90% utilized), the interest rate climbs — rewarding the LP and signalling that fresh liquidity is wanted. The LP earns the pool rate plus CPOOL incentives.

Two adverse scenarios show the risk profile:
- **Liquidity crunch** — if utilization is at 95% and the LP wants out, there may be too little idle liquidity to withdraw until the borrower repays. The LP is locked in, not wiped out.
- **Default** — if the borrower fails to repay, there is no collateral to seize. The LP can face a partial or total, *unrecoverable* loss of principal. This is the defining difference from overcollateralized DeFi and the reason borrower vetting and concentration matter so much.

---

## Comparison vs Competitors

| Protocol | Segment | Collateralization | Distinctive edge | Primary risk |
|---|---|---|---|---|
| **Clearpool (CPOOL)** | On-chain institutional credit / RWA | Uncollateralized (vetted borrowers) | Permissionless single-borrower pools + compliant Prime/Credit Vaults | Borrower default (concentrated) |
| Maple Finance | Institutional credit | Under/uncollateralized, pool-delegate model | Delegate-managed pools, cash-management products | Borrower default; delegate judgement |
| Goldfinch | Real-world / emerging-market credit | Off-chain collateral, backer model | Real-world borrowers, tranche structure | Off-chain credit assessment |
| Centrifuge | RWA tokenization | Asset-backed (tokenized RWAs) | Securitization of real assets on-chain | Asset quality; legal enforceability |
| TrueFi | Uncollateralized credit | Uncollateralized | Early mover in on-chain unsecured lending | Borrower default |
| [[aave\|Aave]] / [[compound\|Compound]] | Money market | Overcollateralized | Auto-liquidation, deep liquidity | Smart-contract / oracle (not credit) |

The whole left group (Clearpool, Maple, Goldfinch, Centrifuge, TrueFi) competes for the **RWA / private-credit** narrative — a major DeFi growth theme but still small relative to the overcollateralized money-market giants on the right.

---

CPOOL is Clearpool's utility and [[governance-token]]:

- **Governance** — holders vote on borrower whitelisting and, over time, protocol upgrades and parameters.
- **Borrower staking** — borrowers must stake CPOOL to access the whitelisting-proposal process, aligning incentives.
- **Incentives** — LPs earn additional CPOOL rewards that enhance pool yields.
- **Buybacks** — a share of protocol revenue is earmarked to buy CPOOL on the open market to sustain reward pools.

Supply is largely circulating (~975M of 1B), giving a market-cap/FDV ratio near 1.0, so dilution overhang from future unlocks is limited.

### Value accrual

CPOOL value accrual leans on three legs: **borrower staking demand** (borrowers must stake CPOOL to enter the whitelisting process), **fee-funded buybacks** (a share of protocol revenue earmarked to buy CPOOL on the open market to sustain reward pools), and **governance utility** over borrower whitelisting and parameters. All three strengthen as lending volume and active pools grow, and weaken when borrowing demand contracts — the same reflexivity seen across revenue-linked DeFi tokens, but here additionally exposed to credit-cycle sentiment.

---

## History & Notable Events

- **2021** — Clearpool launches its decentralized capital-markets protocol; backed by investors including Sequoia Capital, and listed via the DAOMaker launchpad. CPOOL reaches its all-time high of **$2.55 on 2021-11-16** during the bull market.
- **2022–2023** — Builds out the permissionless single-borrower pool model with utilization-based dynamic rates; weathers the broad crypto-credit stress of 2022 (when several centralized lenders and some on-chain credit pools faced defaults), printing an all-time low near **$0.0160 on 2023-10-16**.
- **2023–2024** — Launches **Clearpool Prime / Credit Vaults**, a permissioned, KYC-gated venue for compliant institutional [[real-world-assets|RWA]] and private-credit deals, and expands to the [[solana|Solana]] ecosystem.
- **2025–2026** — Operates as a leading on-chain institutional-credit/RWA protocol; CPOOL trades ~$0.021 as of 2026-06-22, down a sharp -12.78% on the week amid Extreme-Fear conditions (Fear & Greed 21).

---

## Competitive Position

Clearpool sits in the **on-chain institutional credit / RWA** segment alongside protocols such as Maple Finance, Goldfinch, Centrifuge, and TrueFi. Its differentiators are a permissionless single-borrower pool model, dynamic utilization-based pricing, and a dedicated compliant venue (Prime/Credit Vaults) for regulated institutions. The RWA narrative — bringing off-chain credit and tokenized assets on-chain — is a major DeFi growth theme, but the segment is competitive and small relative to overcollateralized lending.

---

## Risks

- **Credit / default risk (primary)** — loans are uncollateralized; a borrower default can impose direct, unrecoverable losses on LPs. This is fundamentally different from the smart-contract-only risk of overcollateralized DeFi.
- **Borrower concentration** — pools are single-borrower, so LP outcomes hinge on one counterparty's health.
- **Liquidity / withdrawal risk** — if a pool is highly utilized, LPs may be unable to withdraw until the borrower repays.
- **Regulatory risk** — institutional lending, KYC, and RWA tokenization sit squarely in the path of evolving securities and lending regulation.
- **Smart-contract and microcap risk** — standard DeFi contract risk, plus a small (~$22M) market cap that makes CPOOL volatile and thinly traded.

This is not investment advice; figures are point-in-time and crypto assets are highly volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 975.38M CPOOL |
| **Total Supply** | 1.00B CPOOL |
| **Max Supply** | 1.00B CPOOL |
| **Fully Diluted Valuation** | $23.93M |
| **Market Cap / FDV Ratio** | 0.98 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.55 (2021-11-16) |
| **Current vs ATH** | ~-99.2% |
| **All-Time Low** | $0.0160 (2023-10-16) |
| **24h Change** | -4.13% |
| **7d Change** | -12.78% |
| **30d Change (2026-04-09 snapshot)** | +14.59% |
| **1y Change (2026-04-09 snapshot)** | -77.51% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x66761fa41377003622aee3c7675fc7b5c1c2fac5` |
| Solana | `AeXrLftu8chuY4ctc6oDeG4dUx6Yr4aqeakUMFNvACdg` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | CPOOL/USD | N/A |
| Upbit | CPOOL/KRW | N/A |
| Bitget | CPOOL/USDT | N/A |
| KuCoin | CPOOL/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X66761FA41377003622AEE3C7675FC7B5C1C2FAC5/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://clearpool.finance/](https://clearpool.finance/) |
| **Twitter** | [@ClearpoolFin](https://twitter.com/ClearpoolFin) |
| **Telegram** | [clearpoolofficial](https://t.me/clearpoolofficial) (10,239 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.0212149 |
| **Market Cap** | $21,366,847 |
| **Market Cap Rank** | #796 |
| **24h Change** | -4.13% |
| **7d Change** | -12.78% |
| **24h Range (2026-04-09 snapshot)** | $0.0231 — $0.0248 |
| **CoinGecko Sentiment (2026-04-09 snapshot)** | 100% positive |
| **Last Updated** | 2026-06-22 (price/cap); intraday range/sentiment from 2026-04-09 snapshot |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Related

- [[lending]]
- [[real-world-assets]]
- [[defi]]
- [[governance-token]]
- [[aave]]
- [[usdc]]
- [[solana]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot). Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no specific wiki source ingested yet.
