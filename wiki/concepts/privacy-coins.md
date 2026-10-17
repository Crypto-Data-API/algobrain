---
title: "Privacy Coins"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: review
tags: [crypto, privacy, regulation, on-chain, altcoins]
aliases: ["Anonymous Cryptocurrencies", "Privacy Tokens", "Shielded Transactions"]
domain: [crypto, market-microstructure]
difficulty: intermediate
prerequisites: ["[[zero-knowledge-proofs]]", "[[blockchain]]"]
---

# Privacy Coins

**Privacy coins** are cryptocurrencies that use cryptographic techniques to obscure transaction metadata — sender address, receiver address, and/or transaction amount — making on-chain flows untraceable or significantly harder to analyse than on transparent blockchains like Bitcoin or Ethereum. The three dominant privacy coins are **Monero (XMR)**, **Zcash (ZEC)**, and historically **Dash (DASH)**, each using different cryptographic approaches. Privacy coins represent a fundamental design trade-off: transparency (which enables on-chain analysis, regulatory compliance, and auditability) vs. financial privacy (which enables censorship resistance and confidential transactions).

## How They Work

### Monero (XMR) — Ring signatures + stealth addresses + RingCT

Monero's privacy is **mandatory and default** for all transactions. Three techniques combine:

1. **Ring signatures:** Each transaction input is signed by a "ring" of 16 possible signers drawn from the UTXO set. Observers see that *one of* the 16 signed, but cannot determine which.
2. **Stealth addresses:** The receiver generates a one-time address for each incoming transaction, so their public address never appears on-chain.
3. **RingCT (Ring Confidential Transactions, 2017):** Hides transaction amounts using Pedersen commitments, verifiable by the network without revealing the value.

Result: Monero transactions are computationally untraceable; chain analysis firms (Chainalysis, Elliptic) have had limited success breaking Monero's privacy beyond heuristics.

### Zcash (ZEC) — zk-SNARKs shielded pools

Zcash uses **zk-SNARKs** ([[zero-knowledge-proofs]]) to verify "shielded" transactions without revealing any transaction detail. However, Zcash has two address types: transparent (t-addresses, identical to Bitcoin) and shielded (z-addresses). The vast majority of Zcash transactions (historically 80-90%) use transparent addresses, meaning most ZEC activity is fully traceable. The network's privacy is opt-in and concentrated in a small fraction of activity. The Electric Coin Company (ECC) and Zcash Foundation manage the protocol. *(Update 2026-10-17: [[zcash]] records that shielded adoption surged in 2025, with **over 30% of ZEC supply** held in fully shielded pools. Unified Addresses and the Orchard pool (Halo proofs, no trusted setup) made shielding the default in modern wallets. The "80-90% transparent" figure describes earlier transaction counts. See Contradictions.)*

### Dash — CoinJoin (PrivateSend)

Dash's **PrivateSend** feature is a coin-mixing service (CoinJoin) built into the wallet. It is optional, requires multiple mixing rounds, and provides weaker privacy than XMR or shielded ZEC because the mixing can sometimes be traced through transaction graph analysis.

## Concrete Examples

- **Monero and ransomware:** Since ~2017, most professional ransomware groups (REvil, DarkSide, Conti) have shifted payment demands from Bitcoin to Monero because Bitcoin transactions are now traceable enough for law enforcement to recover (as demonstrated with Colonial Pipeline's BTC payment recovery in June 2021). Monero's mandatory privacy makes recovery significantly harder.
- **Zcash Sapling upgrade (Oct 2018):** Reduced the computational cost of generating shielded proofs from 40 seconds to under 3 seconds, making z-address transactions practical. Adoption of shielded transactions slowly increased post-Sapling.
- **Exchange delistings:** Major regulated exchanges (Bittrex 2021, Kraken UK 2020, OKX Japan) have delisted XMR, ZEC, and DASH in response to regulatory pressure — particularly from FATF's Travel Rule requirements. This has materially impacted liquidity and price performance relative to transparent-ledger assets. *(Update: Binance delisted XMR in 2024, and OKX and Kraken (EEA) followed earlier moves elsewhere. See [[monero]].)*
- **Tornado Cash sanctions reversed (2024-25):** in November 2024 the US Fifth Circuit ruled that immutable smart contracts are not sanctionable "property". OFAC lifted the Tornado Cash designation on **2025-03-21**, and TORN rose ~60% intraday ([[narratives-by-direction]], [[regulatory-bans]]). This is the clearest dated case of a privacy *de-risking* catalyst.
- **2025-26 privacy cycle:** despite delistings, the sector led a privacy-narrative rally. [[monero|XMR]] set an all-time high near **$798 on 2026-01-14**, and ZEC re-rated sharply as shielded usage grew. On **2026-06-05** the disclosure of a Zcash Orchard counterfeiting bug cut ZEC ~38% in a single day ([[2026-06-05-zcash-orchard-counterfeiting-bug]]). For privacy coins, *protocol* risk sits on top of regulatory risk.

## Trading Relevance

Privacy coins are a high-risk, regulatory-headline-driven sub-sector with distinct trading characteristics:

- **Regulatory binary risk:** Privacy coins face binary delisting events — a single regulatory announcement (FATF guidance, SEC action, major exchange compliance review) can remove a large fraction of liquidity overnight. This creates both tail-risk *and* potential mispricing opportunities for traders who analyse regulatory timelines carefully. The [[arbitrage]] opportunity is between the current market price and the post-delisting equilibrium accessible on DEXs (e.g., XMR on Haveno, a Monero-native decentralised exchange).
- **On-chain analysis limitations:** Privacy coins are explicitly outside the scope of on-chain analytics tools (Chainalysis, Nansen, Glassnode) — those tools provide near-zero signal for XMR. Strategies relying on [[on-chain-analysis]] signals must exclude privacy coins from their universe.
- **Correlation to regulation regime:** Privacy coins tend to underperform BTC/ETH during regulatory-tightening regimes and over-perform during privacy-narrative regimes (e.g., government surveillance news, CBDC rollout debates). The [[contrarian-extremes]] strategy should treat privacy coin readings separately from the broader index.
- **[[zero-knowledge-proofs]] and the privacy landscape shift:** Ethereum-native privacy is emerging via ZK-based privacy pools (e.g., Tornado Cash successors, Aztec Network) and rollup privacy features. If mainstream L1/L2 chains gain meaningful privacy, the unique value proposition of dedicated privacy coins narrows — a long-term structural headwind.
- **[[multi-strategy-crypto-portfolio]]:** Privacy coins are typically absent from institutional-grade crypto portfolios due to compliance risk. Any exposure in the memecoin/convexity sleeve requires explicit regulatory-risk accounting and venue diversification to non-KYC DEX alternatives in case CEX delistings close the exit.
- **[[privacy-basket]]:** the Hyperliquid perp basket for the sector (XMR, ZEC and peers). Its rules drop a constituent and halve exposure on any OFAC designation or major-exchange delisting, and they require checking Hyperliquid perp availability before every weekly screen because privacy perps can be removed suddenly.
- **[[mythos-release-window-exploit-short]]:** shorts protocol-vulnerability risk around frontier-AI release windows. The thesis is that models strong at offensive security shorten the time to find exploitable bugs. The Zcash Orchard counterfeiting bug, found by an AI model, is its motivating case.
- **Perp access:** spot liquidity is fragmented by delistings, so the cleanest venue for hedges and shorts is often a perp. A delisting of the perp itself is a forced-exit event, so size so that you can exit on one day's volume.

## Contradictions

> **Claim A** (Source: this page, original text, confidence: LOW): "The vast majority of Zcash transactions (historically 80-90%) use transparent addresses... privacy is... concentrated in a small fraction of activity."
> **Claim B** (Source: [[zcash]], confidence: MEDIUM): "Privacy adoption has surged in 2025, with over 30% of total ZEC supply now held in fully shielded pools."
> **Resolution**: The claims measure different things (share of transactions historically vs share of supply in 2025), so both can hold. Claim A no longer describes current Zcash. Claim B is favoured for the post-2025 state, pending a dated shielded-supply series.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/coins/category-groups` — curated **privacy** group (XMR, ZEC, DASH and peers) with price, market cap, rank and 24h/7d change
- `GET /api/v1/policy/regime/score` — market-wide policy/regulatory-stress composite, the regime gate for delisting risk
- `GET /api/v1/policy/headlines` — policy and regulatory headlines feeding that score
- `GET /api/v1/news/coin/XMR?hours=168` — per-coin headlines (delistings, sanctions, protocol bugs)
- `GET /api/v1/security/events?symbol=ZEC` — recent hack and security events
- `GET /api/v1/hyperliquid/meta` — current Hyperliquid perp universe. It still lists delisted perps, so confirm a live market (e.g. via `/api/v1/hyperliquid/prices`) before relying on a listing.

**Historical data:**
- `GET /api/v1/backtesting/news-events?symbol=ZEC&start=2025-01-01` — dated news events for regulatory event studies
- `GET /api/v1/backtesting/klines?symbol=ZECUSDT&interval=1d&start=2022-01-01` — Binance OHLCV. XMR has no Binance spot history after its 2024 delisting.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/policy/regime/score"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-coins]], [[cryptodataapi-news]], [[cryptodataapi-regimes]]. On-chain flow data is structurally unavailable for XMR and for shielded ZEC.

## Related

- [[monero]] — the dominant privacy-by-default coin
- [[zcash]] — the zk-SNARK shielded-pool coin
- [[zero-knowledge-proofs]] — the cryptographic technology underlying Zcash and modern privacy protocols
- [[on-chain-analysis]] — the analytical discipline that privacy coins are specifically designed to defeat
- [[regulation]] — the primary risk driver for privacy coin valuations
- [[layer-1]] — privacy coins as their own L1 blockchains
- [[contrarian-extremes]] — regulatory panic can create sentiment extremes in privacy coins
- [[multi-strategy-crypto-portfolio]] — compliance constraints on privacy coin inclusion

## Sources

- General crypto/privacy knowledge; no specific wiki source ingested yet.
