---
title: "Ethereum Name Service"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, nft]
aliases: ["ENS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://ens.domains/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[base]]", "[[governance-token]]", "[[decentralized-identity]]", "[[the-graph]]"]
---

# Ethereum Name Service

**Ethereum Name Service** (ticker **ENS**) is a distributed, open, and extensible naming system built on **[[ethereum]]**. Its core job is to map human-readable names like `alice.eth` to machine-readable identifiers — Ethereum addresses, other-chain addresses, content hashes, and metadata — functioning as crypto's equivalent of DNS. The **ENS** token is the governance token of the ENS DAO, which controls the protocol's treasury, registrar pricing, and roadmap. ENS is the dominant naming / [[decentralized-identity|decentralized-identity (DID)]] primitive in crypto.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ENS |
| **Price** | $4.81 |
| **Market Cap** | $194.45M |
| **Market Cap Rank** | #181 |
| **24h Volume** | $44.87M |
| **24h Change** | -7.91% |
| **7d Change** | -3.06% |
| **Fully Diluted Valuation** | ~$481.00M (at 100M max supply) |
| **Market Cap / FDV** | ~0.40 |
| **All-Time High** | $83.40 (2021-11-11) |
| **All-Time Low** | $4.29 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

ENS is trading near its all-time low ($4.29), down ~94% from the November 2021 ATH. The -7.9% 24h drop is consistent with the prevailing **extreme fear (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = 23)** and "Established Bear Market" backdrop on 2026-06-21, with very high relative turnover (~23% of market cap in 24h) signaling active repricing.

---

## Technology & Protocol

ENS is a system of smart contracts on Ethereum, not a single application. Its main components:

- **Registry** — the root contract mapping every name (a `namehash`) to its owner, resolver, and TTL.
- **Registrars** — contracts that govern how subnodes (e.g. `.eth` second-level names) are allocated. The `.eth` registrar runs an auction-then-renewal model with annual fees.
- **Resolvers** — translate a name into the records it points to (ETH address, multi-chain addresses, content hash for IPFS sites, text records like avatar/email/Twitter).
- **Namehash / normalization** — a recursive hashing algorithm (EIP-137) plus a normalization standard (ENSIP-15) that make name lookups deterministic and Unicode-safe.

Each `.eth` name is itself an **NFT** (ERC-721), so names are tradable, transferable, and composable with the wider NFT ecosystem. ENS resolution is expanding cross-chain via **CCIP-Read** (EIP-3668) off-chain resolvers, letting names resolve cheaply or with off-chain data while remaining trust-minimized. The protocol has announced its own L2, **"Namechain,"** to scale name issuance and slash registration gas costs. Indexers such as [[the-graph]] are commonly used to query ENS data at scale.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~40.41M ENS |
| **Total Supply** | 100.00M ENS |
| **Max Supply** | 100.00M ENS (hard cap) |
| **Market Cap / FDV** | ~0.40 |

ENS launched in November 2021 with one of the most-discussed airdrops in crypto history, distributing ~25% of supply to `.eth` name holders. With a fixed 100M max supply and ~40% circulating, remaining tokens vest to the DAO treasury, core contributors, and the foundation over a multi-year schedule (**~60% of supply not yet circulating — a real forward-dilution overhang**). Crucially, the token is **governance-only** — it does not capture `.eth` registration revenue directly; that revenue accrues to the DAO treasury, which token-holders govern. This is the key valuation nuance: ENS value is a claim on governance over a large, fee-generating treasury rather than a direct cash-flow stream.

---

## Market Structure & Derivatives

**Spot venues:** Binance, Kraken, Upbit (KRW), Bitget, KuCoin, and Crypto.com list ENS. On-chain, ENS has deep DEX liquidity across Uniswap V2/V3, Sushiswap, and Balancer V2 on Ethereum (`0xc18360217d8f7ab5e7c516566761ea12ce7f9d72`). Korean retail flow (Upbit KRW pair) can drive outsized intraday moves.

**Derivatives:** ENS-PERP trades on **[[hyperliquid]]** and other perp venues; monitor [[funding-rate|funding]] and open interest for positioning extremes near the ATL. With ~$45M of 24h spot volume against a ~$194M cap, ENS is one of the more liquid names in the naming/identity category.

**Native chain:** Ethereum, with cross-chain resolution via CCIP-Read and a planned "Namechain" L2.

---

## Use Case, Narrative & Category

ENS is the dominant **naming / [[decentralized-identity|decentralized-identity]]** primitive in crypto. A `.eth` name replaces a long hexadecimal address with a memorable handle, and increasingly serves as a portable Web3 username, profile, and avatar standard adopted across wallets and dapps. Its moat is incumbency and network effects: nearly every major wallet resolves `.eth` names. Because each name is an NFT, ENS straddles both the identity (DID) and NFT narratives. The investment thesis is a bet on (1) continued Web3 adoption increasing name demand and (2) the DAO converting treasury value and registration fees into token-holder value.

---

## Valuation Framing

ENS is hard to value on cash flows because the token does not directly receive revenue. The cleaner lenses are:

- **Treasury-backed governance** — the DAO treasury (a mix of ETH, stablecoins, and accrued `.eth` fees) backs a portion of the ~$194M cap; the token is effectively an option on the DAO returning that value (buybacks, fee redirection) to holders.
- **Registration-fee multiple** — value ENS as a multiple of annualized `.eth` registration/renewal revenue, which is highly cyclical with bull-market name demand.
- **Drawdown / mean-reversion** — at ~94% below ATH and pennies above the ATL, ENS is priced as a deep-bear-market governance asset; upside is leveraged to a return of Web3 identity demand.

---

## Peer Comparison

| Token | Category | Mkt Cap | Rank | MC/FDV | 7d | Note |
|---|---|---|---|---|---|---|
| **ENS** | Naming / identity | $194M | #181 | 0.40 | -3.1% | Incumbent `.eth` standard; governance-only token |
| [[arkham]] (ARKM) | On-chain intel + CEX | $86M | #297 | 0.66 | +1.1% | Data product with direct token utility |
| [[kaito]] (KAITO) | AI / InfoFi attention | $115M | #243 | 0.24 | +6.0% | Heavy unlock overhang |
| [[the-graph]] (GRT) | Data indexing | — | — | — | — | Often used to index ENS data |

---

## Notable History

- **2017** — ENS launches on Ethereum mainnet.
- **2021-11-09** — ENS token airdrop and DAO formation; **ATH $83.40 on 2021-11-11**.
- **2022** — Record `.eth` registrations during the identity/NFT boom.
- **2024-2025** — Cross-chain resolution (CCIP-Read) and L2 ("Namechain") roadmap announced to lower fees and scale issuance.
- **2026-02** — ENS prints fresh lows near $4-5 in the bear market.
- **2026-06-21** — Trades ~$4.81, just above the all-time low ($4.29).

---

## Risks

- **Governance-only token** — no direct revenue claim; value depends on DAO decisions to return treasury value to holders.
- **Drawdown depth** — ~94% below ATH and near the ATL; weak price momentum.
- **Competition** — alternative naming systems (other L1/L2 name services, Web2 handles) could fragment the standard.
- **Unlock schedule** — ~60% of supply not yet circulating.
- **Demand cyclicality** — name registrations are highly correlated with bull-market speculation; bear markets sharply reduce new-name demand and fee revenue.

---

## Related

- [[ethereum]] — the chain ENS is built on
- [[base]] — ecosystem for cross-chain resolution
- [[hyperliquid]] — where ENS-PERP trades
- [[governance-token]] — ENS is a DAO governance token
- [[decentralized-identity]] — ENS is a core DID primitive
- [[the-graph]] — used to index ENS data
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
