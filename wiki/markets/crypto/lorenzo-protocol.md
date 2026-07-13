---
title: "Lorenzo Protocol"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, bitcoin]
aliases: ["BANK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lorenzo-protocol.xyz/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[bitcoin]]", "[[liquid-staking]]", "[[liquid-restaking]]", "[[restaking]]", "[[stablecoin]]", "[[real-world-assets]]", "[[defi]]", "[[governance-token]]"]
---

# Lorenzo Protocol

**Lorenzo Protocol** (BANK) is a [[bitcoin|Bitcoin]] [[liquid-staking|liquid-staking]] and on-chain asset-management protocol that positions itself as a **"financial abstraction layer"** for tokenized, yield-bearing financial products. It lets users stake/restake BTC to receive liquid representations (such as **stBTC** and the wrapped **enzoBTC**) and provides structured, fund-like on-chain products (e.g., **USD1+** yield funds). Built in the [[bnb|BNB Chain]] ecosystem and backed by YZi Labs (formerly Binance Labs), it sits in the **BTCfi** (Bitcoin DeFi) category. **BANK** is its [[governance-token|governance token]].

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, BANK traded at **$0.03796252**, ranked **#916** by market capitalization with a market cap of approximately **$16,125,028**. It declined over the short term — **-1.68% over 24 hours** and **-5.58% over the trailing 7 days** — against an "Extreme Fear" market (Fear & Greed Index **21**). BANK trades well below its October 2025 all-time high near $0.23, having retraced sharply since launch.

---

## What Lorenzo Protocol Does

Lorenzo is a BTCfi and on-chain asset-management platform with two intertwined pillars:

1. **Bitcoin liquid staking / restaking** — users deposit BTC and receive liquid, transferable tokens that represent the staked position and accrue yield. The protocol separates principal and yield concepts so that the liquid token can be used elsewhere in [[defi]] while the underlying BTC earns rewards. Key tokens include **stBTC** (a liquid staked-BTC representation) and **enzoBTC** (a wrapped/standardized BTC representation for use across chains and products).
2. **Financial Abstraction Layer (on-chain asset management)** — Lorenzo packages strategies into tokenized, fund-like products. Its **USD1+** offering is a stablecoin-denominated yield fund concept that abstracts underlying yield strategies into a single on-chain token, giving holders exposure to managed yield without operating the strategies themselves.

The "financial abstraction layer" framing means Lorenzo aims to be the issuance and accounting layer that turns off-chain and on-chain yield strategies into composable, tokenized products — effectively bringing structured-product and fund mechanics on-chain.

---

## Mechanism and Architecture

- **Liquid staking tokens (LSTs)** — staking BTC mints a liquid receipt token ([[liquid-staking]]). This preserves capital efficiency: the staked BTC keeps earning while its tokenized form remains usable as collateral or in other protocols.
- **Principal/yield separation** — Lorenzo's design distinguishes principal tokens from yield-accruing tokens, enabling structured-product construction.
- **Wrapped/standardized BTC (enzoBTC)** — a normalized BTC representation that improves composability across chains and within Lorenzo's product suite.
- **Tokenized funds (USD1+ and similar)** — on-chain vehicles that route deposits into yield strategies and represent ownership with a single fund token, with NAV/accounting handled by the protocol's abstraction layer.
- **Bitcoin-staking foundation** — Lorenzo's BTC yield is connected to the broader Bitcoin-staking trend (e.g., Babylon-style BTC staking infrastructure), which underpins much of the current BTCfi wave.

---

## Token Role: BANK

BANK is Lorenzo's [[governance-token|governance token]]:

- **Governance** — voting on protocol parameters, product approvals, and treasury decisions, commonly via a vote-escrow (veBANK) model that rewards long-term lockups with greater voting weight.
- **Incentives** — directing emissions/rewards across the protocol's products and liquidity.
- **Value alignment** — tying long-term holders to the growth of Lorenzo's staking and asset-management products.

### Value accrual and veBANK

- **Vote-escrow (veBANK).** BANK uses a [[curve-finance|Curve]]-style vote-escrow design: locking BANK for a time period mints non-transferable veBANK, whose weight scales with lock duration. veBANK confers heavier voting power and a larger share of protocol incentives/rewards, aligning governance influence with long-term commitment.
- **Fee / incentive direction.** veBANK holders steer where emissions and incentives flow across Lorenzo's products (stBTC, enzoBTC, USD1+ funds and their liquidity), analogous to gauge-voting in other DeFi protocols. This makes BANK a meta-token over Lorenzo's product suite rather than a direct claim on a single asset.
- **Real-yield dependency.** Durable BANK value accrual depends on Lorenzo capturing fees from genuine asset-management activity (AUM in its funds, BTC-staking flows) rather than on emissions alone — the same emissions-vs-fees tension that defines the BTCfi category.

BANK has a large max supply (2.10B) with only a portion circulating, so future unlocks and emissions represent a meaningful dilution consideration.

---

## Competitive Position

Lorenzo competes in the fast-growing **BTCfi / Bitcoin liquid-staking** arena alongside protocols such as Lombard (LBTC), Solv, pStake, and other BTC-yield issuers, as well as broader on-chain asset managers. Its differentiators are the "financial abstraction layer" framing (structured, fund-like products rather than a single LST), the stBTC/enzoBTC token suite, USD1+ funds, and backing from YZi Labs within the [[bnb|BNB Chain]] ecosystem. The category is competitive and depends on the durability of [[bitcoin|Bitcoin]]-staking yield sources; share is not yet settled among the leaders.

| Protocol | Liquid token(s) | Underlying yield source | Distinguishing angle | Chain focus |
|---|---|---|---|---|
| **Lorenzo** | stBTC, enzoBTC; USD1+ fund | Babylon-style BTC staking + managed strategies | "Financial abstraction layer": tokenized fund/structured products, principal/yield separation | [[bnb\|BNB Chain]] |
| **Lombard** | LBTC | Babylon BTC staking | Largest BTC-LST by adoption; DeFi-integration breadth | Multi-chain |
| **Solv Protocol** | SolvBTC (+ yield variants) | Aggregated BTC yield (staking, basis, RWA) | BTC "yield aggregator" / reserve abstraction | Multi-chain |
| **pStake (BTCfi)** | yBTC / stkBTC | Babylon BTC staking | Persistence-team BTC staking | Multi-chain |
| **Babylon** | (native staking) | Bitcoin self-custodial staking (security layer) | The base BTC-staking infrastructure others build on | Bitcoin + BSNs |

Lorenzo's positioning is less "just an LST" and more an **on-chain asset manager**: stBTC/enzoBTC are inputs, and the headline product is the packaging of yield strategies into single fund tokens (USD1+ and similar). That broadens its addressable market beyond pure BTC stakers but also means it competes with on-chain asset managers and structured-product issuers, not only BTC-LST rivals.

---

## Risks

- **Smart-contract and bridging risk** — liquid-staking and wrapped-BTC systems involve complex contracts and cross-chain components; exploits or bridge failures can cause loss of underlying BTC.
- **Peg / redemption risk** — stBTC and enzoBTC rely on maintaining a tight peg and reliable redemption to underlying BTC; stress events can cause depegs.
- **Yield-source / counterparty risk** — fund products (e.g., USD1+) depend on underlying strategies whose returns and counterparties carry risk; advertised yields are not guaranteed.
- **Micro-cap token volatility** — at ~$16.4M (rank #912), BANK is a small-cap that has fallen sharply from its all-time high.
- **Dilution overhang** — a large gap between circulating and max supply implies future emissions/unlocks.
- **Dependence on BTC-staking infrastructure** — Lorenzo's core yield is tied to the broader Bitcoin-staking ecosystem; changes there propagate to Lorenzo.

> **Data disclaimer:** Figures above are point-in-time market snapshots (2026-06-22) and qualitative descriptions of mechanism. TVL, yields/APY, peg status, and audit details are not independently verified here and should be confirmed against official documentation and on-chain analytics before any decision.

---

## Platform & Chain Information

**Native Chain:** [[bnb|BNB Chain]] (Binance Smart Chain)

### Contract Addresses

| Chain | Address |
|---|---|
| BNB Chain | `0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf` |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Max Supply** | 2.10B BANK |
| **Market Cap / FDV** | Partial supply circulating (dilution overhang) |

*Note: exact circulating supply and FDV change with each snapshot; re-verify at source.*

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | BANK/USDT |
| Bitget | BANK/USDT |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lorenzo-protocol.xyz/](https://lorenzo-protocol.xyz/) |
| **Twitter** | [@LorenzoProtocol](https://twitter.com/LorenzoProtocol) |
| **Telegram** | [LorenzoProtocol](https://t.me/LorenzoProtocol) |
| **Docs** | [https://docs.lorenzo-protocol.xyz/](https://docs.lorenzo-protocol.xyz/) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[bitcoin]]
- [[liquid-staking]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot); Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
