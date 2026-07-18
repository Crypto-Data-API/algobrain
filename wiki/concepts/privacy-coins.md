---
title: "Privacy Coins"
type: concept
created: 2026-07-17
updated: 2026-07-19
status: draft
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

Zcash uses **zk-SNARKs** ([[zero-knowledge-proofs]]) to verify "shielded" transactions without revealing any transaction detail. However, Zcash has two address types: transparent (t-addresses, identical to Bitcoin) and shielded (z-addresses). The vast majority of Zcash transactions (historically 80-90%) use transparent addresses, meaning most ZEC activity is fully traceable. The network's privacy is opt-in and concentrated in a small fraction of activity. The Electric Coin Company (ECC) and Zcash Foundation manage the protocol.

### Dash — CoinJoin (PrivateSend)

Dash's **PrivateSend** feature is a coin-mixing service (CoinJoin) built into the wallet. It is optional, requires multiple mixing rounds, and provides weaker privacy than XMR or shielded ZEC because the mixing can sometimes be traced through transaction graph analysis.

## Concrete Examples

- **Monero and ransomware:** Since ~2017, most professional ransomware groups (REvil, DarkSide, Conti) have shifted payment demands from Bitcoin to Monero because Bitcoin transactions are now traceable enough for law enforcement to recover (as demonstrated with Colonial Pipeline's BTC payment recovery in June 2021). Monero's mandatory privacy makes recovery significantly harder.
- **Zcash Sapling upgrade (Oct 2018):** Reduced the computational cost of generating shielded proofs from 40 seconds to under 3 seconds, making z-address transactions practical. Adoption of shielded transactions slowly increased post-Sapling.
- **Exchange delistings:** Major regulated exchanges (Bittrex 2021, Kraken UK 2020, OKX Japan) have delisted XMR, ZEC, and DASH in response to regulatory pressure — particularly from FATF's Travel Rule requirements. This has materially impacted liquidity and price performance relative to transparent-ledger assets.

## Trading Relevance

Privacy coins are a high-risk, regulatory-headline-driven sub-sector with distinct trading characteristics:

- **Regulatory binary risk:** Privacy coins face binary delisting events — a single regulatory announcement (FATF guidance, SEC action, major exchange compliance review) can remove a large fraction of liquidity overnight. This creates both tail-risk *and* potential mispricing opportunities for traders who analyse regulatory timelines carefully. The [[arbitrage]] opportunity is between the current market price and the post-delisting equilibrium accessible on DEXs (e.g., XMR on Haveno, a Monero-native decentralised exchange).
- **On-chain analysis limitations:** Privacy coins are explicitly outside the scope of on-chain analytics tools (Chainalysis, Nansen, Glassnode) — those tools provide near-zero signal for XMR. Strategies relying on [[on-chain-analysis]] signals must exclude privacy coins from their universe.
- **Correlation to regulation regime:** Privacy coins tend to underperform BTC/ETH during regulatory-tightening regimes and over-perform during privacy-narrative regimes (e.g., government surveillance news, CBDC rollout debates). The [[contrarian-extremes]] strategy should treat privacy coin readings separately from the broader index.
- **[[zero-knowledge-proofs]] and the privacy landscape shift:** Ethereum-native privacy is emerging via ZK-based privacy pools (e.g., Tornado Cash successors, Aztec Network) and rollup privacy features. If mainstream L1/L2 chains gain meaningful privacy, the unique value proposition of dedicated privacy coins narrows — a long-term structural headwind.
- **[[multi-strategy-crypto-portfolio]]:** Privacy coins are typically absent from institutional-grade crypto portfolios due to compliance risk. Any exposure in the memecoin/convexity sleeve requires explicit regulatory-risk accounting and venue diversification to non-KYC DEX alternatives in case CEX delistings close the exit.

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
