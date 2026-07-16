---
title: "EXOD (Exodus)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stocks]
aliases: ["EXOD", "Exodus", "Exodus Movement"]
entity_type: company
headquarters: "United States"
website: "https://www.exodus.com/"
related: ["[[arbitrum]]", "[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[self-custody]]"]
---

# EXOD (Exodus)

**EXOD** is the tokenized common stock of **Exodus Movement, Inc.** (NYSE American: EXOD), a US financial-technology company best known for its self-custodial, multi-asset **Exodus crypto wallet** (founded 2015). Unusually, EXOD is **both a US-listed equity and a tokenized security on-chain**: the company tokenized its Class A common stock on [[arbitrum|Arbitrum One]] (with an Algorand representation), making it one of the first US public companies to put its shares on a public blockchain. Each on-chain EXOD token represents a real share of Exodus stock — so this is *not* a typical utility token but a **tokenized equity / [[real-world-assets|RWA]]**.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | EXOD |
| **Price (USD)** | $8.18 |
| **Market Cap** | $85.45M |
| **Market Cap Rank** | #300 |
| **24h Volume (on-chain)** | $0 (see note) |
| **24h Change** | 0.00% (stale on-chain feed) |
| **7d Change** | 0.00% (stale on-chain feed) |
| **Fully Diluted Valuation** | $85.45M |
| **All-Time High** | $13.09 (2026-02-03) — ~-38% below ATH |
| **All-Time Low** | $6.10 (2026-04-04) |
| **Categories** | Tokenized equity, Wallets, Arbitrum & Algorand Ecosystems |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Important data nuance:** the CoinGecko/crypto snapshot shows **$0 on-chain 24h volume and 0.00% price changes** for EXOD. This does **not** mean the stock is untraded — it reflects that EXOD's real price discovery and liquidity occur on the **NYSE American national securities exchange**, not on crypto venues. The on-chain token price tracks the equity, but on-chain trading is minimal, so the crypto feed is effectively stale/illiquid (the snapshot price of $8.18 has been static across recent refreshes). Backdrop: the crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** in an "Established Bear Market," but EXOD's price is ultimately set by equity-market dynamics, not crypto sentiment.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.45M EXOD |
| **Total Supply** | 10.45M EXOD |
| **Max Supply** | 10.45M EXOD |
| **Market Cap / FDV** | ~1.00 |

EXOD's "supply" is its **share count** (~10.45M shares represented on-chain), not a crypto emission schedule — circulating, total, and max are identical, and market cap equals FDV. There is no buyback/burn or fee-utility mechanic in the crypto sense; value derives from Exodus's equity fundamentals (revenue from in-wallet swaps/exchange fees, business products, etc.). This makes EXOD fundamentally different from the exchange/wallet *utility* tokens elsewhere in this set ([[bitkub-coin|KUB]], [[coinex-token|CET]], [[backpack|BP]], [[safepal|SFP]]).

---

## How & Where It Trades

EXOD's primary, regulated market is the **NYSE American (a US national securities exchange)**, where it trades as Exodus Movement common stock during US market hours. The tokenized version lives on **Arbitrum One** (`0x116998824ff90532906bab91becea4a8e4ce06db`) and **Algorand** (asset ID `213345970`), but on-chain liquidity is thin — hence the $0 crypto-feed volume. There is no meaningful crypto-native derivatives, funding, or open-interest market; instead, EXOD behaves like an equity and is subject to **US securities regulation, SEC reporting, market hours, and trading halts** rather than 24/7 crypto microstructure.

### Tokenized-Equity / RWA Peer Context (2026-06-21)

| Asset | What it is | Primary venue | On-chain presence |
|---|---|---|---|
| **EXOD (Exodus)** | Tokenized US-listed common stock | NYSE American | [[arbitrum\|Arbitrum]] + Algorand |
| Backed / Galaxy (via [[superstate-short-duration-us-government-securities-fund-ustb\|Superstate Opening Bell]]) | Tokenized SEC-registered shares | Equity primary | Solana / Ethereum |
| [[superstate-short-duration-us-government-securities-fund-ustb\|USTB]] | Tokenized US Treasury fund | Primary subscribe/redeem | Ethereum / Plume |

EXOD is distinctive because it is a **live, exchange-listed company stock** that has been wrapped on-chain — versus tokenized funds or newly issued tokenized shares. Its price is set by the regulated equity market, with the token a thin mirror.

---

## Use Case / Narrative / Category

EXOD is a **"tokenized stock" / [[real-world-assets|RWA]] bellwether** as much as a fintech equity. The narrative is twofold: (1) Exodus the business — a long-running, [[self-custody|self-custodial]] multi-asset wallet (swap/buy/sell, Passkeys Wallet, XO Swap aggregation) monetizing crypto access; and (2) Exodus the precedent — one of the first US-listed companies to tokenize its own shares on a public blockchain, a proof-of-concept for on-chain equities. Investors get exposure to a regulated US crypto-fintech stock with an on-chain wrapper. Note Exodus the product is a flagship example of the [[self-custody]] thesis ("not your keys, not your coins"), which directly ties the company's fortunes to crypto-adoption and trading-volume cycles.

---

## Notable History

- Founded **2015**; the Exodus wallet became one of the most widely used desktop/mobile self-custody wallets.
- Listed on **NYSE American as EXOD** and tokenized its Class A common stock on Arbitrum — a landmark for tokenized US equities.
- **All-Time High:** $13.09 (2026-02-03); **All-Time Low:** $6.10 (2026-04-04). The stock fell sharply through spring 2026 (down ~40% over the prior 30 days in an earlier snapshot) before stabilizing around $8 — currently ~38% below ATH but ~34% above the April ATL.

> *Notable corporate events (earnings, SEC filings, product launches) will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **Equity / US securities risk (the key nuance):** EXOD is a regulated US-listed stock — subject to SEC oversight, periodic reporting, market hours, halts, and equity-market volatility — *in addition to* any crypto-specific risk. It does not trade 24/7 like a typical token, and the on-chain feed can be stale.
- **Business / fundamentals risk:** value depends on Exodus's revenue (largely in-wallet swap/exchange fees), which is sensitive to crypto trading activity and a bear market ([[crypto-fear-and-greed-index|F&G]] 23) that suppresses volumes.
- **On-chain liquidity risk:** the tokenized version is thinly traded on-chain ($0 snapshot volume); the Arbitrum/Algorand wrappers should not be assumed to have deep crypto liquidity.
- **Regulatory / tokenized-equity risk:** tokenized securities are a novel, evolving regulatory area; rules around on-chain equity transfer, eligibility, and custody could change.
- **Concentration:** small float (~10.45M shares) and small market cap make the stock volatile.

---

## Tokenomics Reference

| Metric | Value |
|---|---|
| **All-Time High** | $13.09 (2026-02-03) |
| **All-Time Low** | $6.10 (2026-04-04) |
| **Primary Market** | NYSE American (national securities exchange) |
| **On-chain Wrappers** | Arbitrum One, Algorand |
| **Arbitrum Contract** | `0x116998824ff90532906bab91becea4a8e4ce06db` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.exodus.com/](https://www.exodus.com/) |
| **Twitter** | [@exodus](https://twitter.com/exodus) |
| **Telegram** | [exodussupportann](https://t.me/exodussupportann) |

---

## Related

- [[crypto-markets]]
- [[arbitrum]]
- [[ethereum]]
- [[real-world-assets]] — tokenized-equity category
- [[self-custody]] — Exodus's core product thesis
- [[superstate-short-duration-us-government-securities-fund-ustb]] — adjacent tokenized-RWA reference
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko top-1000 markets snapshot, 2026-06-21.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EXOD |
| **Market Cap Rank** | #413 |
| **Market Cap** | $53.24M |
| **Current Price** | $5.10 |
| **Categories** | Infrastructure, Software as a service, Wallets |
| **Website** | [https://www.exodus.com/](https://www.exodus.com/) |

---

## Overview

Exodus (NYSE American: EXOD) is a financial technology leader empowering individuals and businesses with secure, user-friendly crypto software solutions. Since 2015, Exodus has made digital assets accessible to everyone through its multi-asset crypto wallets prioritizing design and ease of use. With self-custodial wallets, Exodus puts customers in full control of their funds, enabling them to swap, buy, and sell crypto. Its business solutions include Passkeys Wallet and XO Swap, industry-leading tools for embedded crypto wallets and swap aggregation. Exodus is committed to driving the future of accessible and secure finance.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.45M EXOD |
| **Total Supply** | 10.45M EXOD |
| **Max Supply** | 10.45M EXOD |
| **Fully Diluted Valuation** | $53.24M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $13.09 (2026-02-03) |
| **Current vs ATH** | -61.06% |
| **All-Time Low** | $4.82 (2026-07-14) |
| **Current vs ATL** | +5.80% |
| **24h Change** | -0.80% |
| **7d Change** | +0.93% |
| **30d Change** | -37.69% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Arbitrum One

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0x116998824ff90532906bab91becea4a8e4ce06db` |
| Algorand | `213345970` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $0.00000000 |
| **Market Cap Rank** | #413 |
| **24h Range** | $5.10 — $5.14 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[arbitrum]]

---
