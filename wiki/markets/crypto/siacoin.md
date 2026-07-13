---
title: "Siacoin"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["SC", "Sia"]
entity_type: protocol
founded: 2015
headquarters: "Decentralized"
website: "https://sia.tech/"
related: ["[[crypto-markets]]", "[[depin]]", "[[decentralized-storage]]", "[[filecoin]]", "[[arweave]]", "[[proof-of-work]]", "[[bitcoin]]"]
---

# Siacoin

**Siacoin** (SC) is the native token of **Sia**, one of the oldest [[depin|DePIN]] (Decentralized Physical Infrastructure) projects — a decentralized cloud-storage network launched in 2015. Instead of renting storage from a centralized provider like Dropbox or AWS S3, Sia lets clients rent unused disk space from a global network of independent hosts, with the Sia blockchain enforcing storage contracts via smart-contract-style "file contracts." Data is encrypted, erasure-coded into redundant pieces, and distributed across many hosts; SC is used to pay hosts and post collateral. It belongs to the **decentralized-storage / DePIN** category and competes most directly with [[filecoin|Filecoin]].

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | SC |
| **Market Cap Rank** | #566 |
| **Market Cap** | $36.07M |
| **Current Price** | $0.00072508 |
| **24h Volume** | $4.28M |
| **24h Change** | +5.16% |
| **7d Change** | -0.77% |
| **Circulating Supply** | ~49.75B SC |
| **Fully Diluted Valuation** | $36.07M (MC = FDV) |
| **All-Time High** | $0.092868 (2018-01-06) — ~99% below |
| **All-Time Low** | $0.00001262 (2015-12-28) |
| **Native Chain** | Sia (own Proof-of-Work Layer 1) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

SC bounced ~+5.2% on the day but was roughly flat over the prior week (-0.77%), against a risk-off tape — **extreme fear** (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = 23) inside an **Established Bear Market** as of 2026-06-21. As a long-lived, fundamentals-driven storage network, SC tends to track real network usage (storage utilization and contract volume) over the long run, though in bear regimes it trades primarily on macro crypto beta. At ~$0.000725 it remains ~99% below its 2018 ATH but vastly above its 2015 ATL. Note the rank slipped from #481 to #566 since the prior April snapshot as smaller-cap names re-shuffled in the bear tape.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~49.75B SC |
| **Total Supply** | ~49.75B SC |
| **Max Supply** | Uncapped (inflationary, PoW emissions) |
| **Market Cap / FDV Ratio** | ~1.00 |
| **Consensus** | Proof-of-Work (Blake2b) |
| **Genesis** | 2015-06-06 |

Siacoin has a very large, **uncapped and inflationary** supply (~49.75B SC), with new coins minted as Proof-of-Work block rewards, which is why each unit is priced in fractions of a cent. There was no ICO premine controversy of note; the project distributed coins through mining and a small "Siafund" mechanism that routes a percentage of storage-contract revenue to early backers. The MC/FDV ≈ 1.00 reflects that essentially all supply is already mined/circulating. SC also has a historical burn mechanism tied to host collateral on failed contracts.

---

## How & Where It Trades

- **Spot (CEX):** Trades on [[binance|Binance]] (SC/USDT), [[kraken|Kraken]] (SC/USD), Upbit (SC/KRW — Korean-market presence), and Crypto.com. CEX liquidity dominates given Sia is its own non-EVM chain.
- **Spot (DEX):** Limited native DEX presence (Sia is a standalone PoW chain, not an EVM/Solana ecosystem token); most liquidity is on centralized venues.
- **Derivatives:** SC perpetuals have appeared on some exchanges historically, but derivatives liquidity is thin for a ~$36M sub-penny token; expect wide spreads and unstable funding if trading perps. There is no liquid [[hyperliquid|Hyperliquid]] perp dominating price discovery — SC is effectively a spot CEX-driven asset, with Upbit (KRW) providing a notable Korean-retail liquidity pocket.

---

## Use Case / Narrative / Category

Sia is a **decentralized cloud storage / DePIN** protocol. Clients form file contracts with hosts, paying SC over time as hosts prove (via storage proofs) that they still hold the data; hosts post collateral that is slashed if they fail to deliver. The pitch is cheaper, censorship-resistant, redundant storage versus centralized incumbents. Sia's modern stack (Sia Foundation software: `renterd`, `hostd`, `walletd`) targets developers and enterprises, and the project has also promoted **S3-compatible** decentralized storage to ease migration from AWS S3. The long-term thesis for SC is that real storage demand drives recurring on-chain payment to hosts and supports token value, distinguishing it from purely speculative tokens.

---

## Valuation Framing

Siacoin is a **fundamentals-anchored utility token** in theory — its long-run value should reflect the dollar value of storage contracts paid in SC and the collateral hosts must lock. In practice, two structural facts cap re-rating: (1) the ~49.75B uncapped supply means per-unit price stays sub-penny even at meaningful aggregate cap, and (2) PoW emissions continuously dilute. At a ~$36M cap the market prices Sia as a long-tail survivor with modest realized storage revenue rather than a credible AWS S3 challenger. Versus [[filecoin|Filecoin]] (far larger cap, larger committed storage but heavy emission/lockup dynamics) and [[arweave|Arweave]] (pay-once permanent storage, different economic model), Sia's pitch is mature, audited software (`renterd`/`hostd`) and S3 compatibility. The bull case is enterprise/developer adoption converting committed capacity into paid utilization; the bear case is that decentralized storage demand remains a niche dwarfed by hyperscaler clouds.

---

## Peer Comparison

| Token | Model | Mkt-cap rank | Supply | Differentiator |
|---|---|---|---|---|
| **Siacoin (SC)** | Rented host storage, file contracts | #566 | ~49.75B, uncapped PoW | Mature software, S3-compatible, oldest |
| **[[filecoin]] (FIL)** | Proof-of-replication storage market | large-cap | Capped 2B, heavy vesting | Largest committed capacity, IPFS link |
| **[[arweave]] (AR)** | Pay-once permanent storage | mid-cap | ~66M capped | "Permaweb" permanence model |
| Storj (STORJ) | Distributed S3-style storage | small/mid | Capped | Enterprise S3 gateway focus |

*SC rank reflects the 2026-06-21 snapshot; peers shown qualitatively.*

---

## Notable History

- Founded in 2015 by **David Vorick** and **Luke Champine** (originally under Nebulous Inc.; now stewarded by the **Sia Foundation**), making it one of the earliest decentralized-storage projects, predating [[filecoin|Filecoin]].
- **All-time high** of ~$0.0929 on 2018-01-06, during the 2017–18 crypto mania.
- Down roughly **-99%** from that ATH at the current ~$0.000725 — a sub-penny token for most of its life despite continuous protocol development.
- The 2020s saw a full software rewrite and a transition to the nonprofit Sia Foundation governance/treasury model.

---

## Risks

- **Adoption vs. incumbents:** competing with AWS/Google/Dropbox on price and reliability is extremely hard; real paid storage demand has remained modest relative to expectations.
- **Inflation:** uncapped [[proof-of-work|PoW]] emissions continuously dilute holders; the very large supply caps per-unit price appreciation.
- **Competition:** [[filecoin|Filecoin]], [[arweave|Arweave]], Storj and others contest the same [[decentralized-storage]] market.
- **PoW / mining economics:** as a Proof-of-Work chain, security depends on miner participation; low coin price can pressure mining viability.
- **Liquidity & macro:** thin liquidity for a sub-penny token, plus high beta to the broader market — and as of 2026-06-21 the regime is **extreme fear / Established Bear Market** (F&G 23), which weighs on small-cap infrastructure tokens.

> Cryptocurrency is highly volatile and speculative. Nothing here is financial advice. Always verify live data before trading.

---

## See Also

- [[crypto-markets]]
- [[depin]]
- [[decentralized-storage]]
- [[filecoin]]
- [[arweave]]
- [[proof-of-work]]
- [[bitcoin]]
- [[binance]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko (Storage & Data category snapshot).
