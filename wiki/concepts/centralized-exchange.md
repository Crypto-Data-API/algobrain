---
title: "Centralized Exchange"
type: concept
created: 2026-07-17
updated: 2026-08-19
status: draft
tags: [crypto, exchange, market-microstructure, liquidity, regulation]
aliases: ["CEX", "Custodial Exchange"]
domain: [crypto, market-microstructure]
prerequisites: ["[[decentralized-exchanges]]", "[[liquidity]]"]
difficulty: beginner
---

# Centralized Exchange

A **centralized exchange (CEX)** is a custodial trading venue — [[binance|Binance]], [[coinbase|Coinbase]], [[okx|OKX]], Kraken, Bybit — that operates a central limit order book, matches buyers and sellers internally, and holds user funds on their behalf, in contrast to a [[decentralized-exchanges|decentralized exchange (DEX)]] where users retain custody and trade directly against on-chain contracts. CEXs remain the dominant venue for crypto price discovery and liquidity despite a long history of custodial failures, because centralized order matching is faster, cheaper, and more capital-efficient than any fully on-chain alternative has yet matched at scale.

## How It Works

A CEX combines four functions that a DEX splits apart or omits entirely:

1. **Custody.** User deposits are pooled into exchange-controlled wallets (often an omnibus hot/cold wallet split); the exchange's internal ledger — not the blockchain — tracks who owns what. This is the source of both the CEX's speed advantage (no on-chain settlement per trade) and its central risk (users hold an IOU, not the asset itself).
2. **Matching engine.** Orders are matched off-chain in a central limit order book, typically at sub-millisecond latency, enabling market making, algorithmic trading, and deep liquidity that on-chain AMMs struggle to replicate for anything beyond the largest pairs.
3. **Onboarding and compliance.** KYC/AML identity verification, fiat on/off ramps (bank transfer, card), and jurisdiction-specific licensing gate access — the mechanism through which most new capital enters crypto markets, and the primary point of regulatory leverage over the industry.
4. **Revenue model.** Trading fees (typically 0.02-0.10% per side, discounted for token holders — see [[exchange-tokens]]), withdrawal fees, margin/lending interest, listing fees paid by new token projects, and launchpad allocations.

**Custody risk is the structural trade-off.** Because the exchange controls the private keys, a CEX failure — insolvency, hack, or fraud — can make user balances unrecoverable regardless of what the exchange's dashboard displayed the day before. Since November 2022, most major exchanges publish **proof-of-reserves** (Merkle-tree attestations that customer balances are backed 1:1) as a partial mitigant, though proof-of-reserves does not prove the absence of matching liabilities.

## Concrete Examples

- **Binance (founded 2017):** the largest exchange by volume; paid a **$4.3 billion settlement** with the U.S. Department of Justice in November 2023 for AML/sanctions violations, with founder Changpeng Zhao (CZ) stepping down as CEO and later serving prison time — the exchange continued operating throughout.
- **Coinbase:** went public via a direct listing on Nasdaq in April 2021 (ticker COIN), the most regulated large U.S. exchange and a bellwether for institutional crypto sentiment.
- **FTX collapse (November 2022):** the largest CEX failure in crypto history. FTX's affiliated trading firm Alameda Research had used customer deposits and the FTT exchange token as collateral for leveraged bets; a CoinDesk report on Alameda's FTT-heavy balance sheet triggered a bank run, FTX filed Chapter 11 on November 11, 2022, and an estimated **$8-10 billion** in customer funds was frozen. Founder Sam Bankman-Fried was convicted of fraud and sentenced to 25 years.
- **Mt. Gox (2014):** the original cautionary tale — then the world's largest Bitcoin exchange lost roughly **850,000 BTC** (worth ~$450M at the time) to a years-long undetected hack; creditor rehabilitation payouts were still being distributed a decade later, into 2024.
- **OKX, Bybit, KuCoin, Bitget:** tier-2 global CEXs each with their own native [[exchange-tokens|exchange token]] (OKB, BGB, KCS) tied to trading-fee discounts and profit-funded buyback-and-burn programs.

## Trading Relevance

- **[[cross-exchange-arbitrage]] and [[triangular-arbitrage]]:** CEX order books are the primary venue for both — deep, fast-matching liquidity makes latency and fee structure, not settlement delay, the binding constraint, unlike cross-chain arb.
- **[[funding-rate-arbitrage]] and [[cash-and-carry]]:** CEX perpetual futures and spot markets sit on the same exchange with shared margin, making basis and funding trades operationally simpler on a CEX than splitting legs between a CEX and a DEX.
- **[[exchange-tokens]]:** BNB, OKB, KCS, and BGB are direct proxy bets on a specific exchange's trading volume and regulatory survival — a distinct sub-asset class from protocol [[governance-token|governance tokens]].
- **Counterparty concentration risk:** every dollar resting on a CEX order book (not just leveraged positions) is exposed to that exchange's solvency; the FTX and Mt. Gox precedents make **proof-of-reserves** monitoring and exchange diversification a standard risk-management input for any strategy that custodies capital on a CEX between trades.
- **Venue selection for execution:** strategies that need deep, fast-filling liquidity (large size, low latency) default to CEX order books; strategies that need self-custody, composability, or permissionless access default to a [[decentralized-exchanges|DEX]] — the CEX/DEX split is itself a first-order design decision for any execution pipeline.

## Related

- [[decentralized-exchanges]] — the non-custodial alternative venue model
- [[exchange-tokens]] — native tokens issued by centralized exchanges
- [[binance]] — the largest centralized exchange by volume
- [[ftx]] — the largest CEX collapse in crypto history
- [[coinbase]] — the most regulated large U.S. exchange
- [[okx]] — issuer of the OKB exchange token
- [[liquidity]] — the core structural advantage CEX order books hold over most on-chain venues
- [[cross-exchange-arbitrage]] — the primary CEX-native arbitrage strategy

## Sources

- General crypto market-structure knowledge; no specific wiki source ingested yet.
