---
title: "Siacoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, altcoins]
aliases: ["SC", "Sia"]
entity_type: protocol
founded: 2015
headquarters: "Decentralized"
website: "https://sia.tech/"
related: ["[[arweave]]", "[[bitcoin]]", "[[crypto-markets]]", "[[decentralized-storage]]", "[[depin]]", "[[filecoin]]", "[[proof-of-work]]", "[[binance]]", "[[dca-strategy]]", "[[crypto-beta-rotation]]"]
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

## Trading Profile

**Venues & liquidity** — SC is tradable on Binance SPOT only among top venues with reliable depth — there is no liquid perpetual venue, so leverage and clean short access are limited and this is a **spot-primary** asset. Perp funding/basis/liquidation strategies do NOT apply. With a sub-penny price (~$0.0006), a ~$30–36M cap and only a few million dollars of daily volume, the SC/USDT book is thin: expect wide relative spreads, meaningful slippage on size, and price-discovery concentration on that single book (plus a Korean-retail pocket on Upbit KRW). Practical implication — size small, prefer limit/VWAP execution over market orders, and treat the Binance spot book as the reference price; shorting is effectively unavailable outside spot inventory, so bearish views are hard to express directly.

**Applicable strategies**
- [[dca-strategy]] — spot-only, fundamentals-anchored storage/DePIN token where cost-averaging suits accumulation without needing leverage or perps.
- [[buy-and-hold]] — a decade-old survivor thesis tied to real storage utilization; a long-horizon spot hold is the natural expression given no perp venue.
- [[breakout-and-retest]] — after long sub-penny basing, spot breakouts from multi-month ranges can be traded on retest to control the wide-spread entry risk.
- [[volatility-targeting]] — high small-cap beta and episodic vol argue for scaling position size to realized volatility rather than fixed notional.
- [[atr-trailing-stop]] — thin-book gaps make a volatility-scaled trailing stop more robust than a fixed percentage stop for managing spot exits.
- [[crypto-beta-rotation]] — SC trades largely on broad crypto beta in bear regimes, fitting a rotation framework that shifts exposure by regime rather than SC-specific catalysts.

**Volatility & regime character** — Small-cap (~$30–36M), high-beta infrastructure token in the decentralized-storage / [[depin|DePIN]] category — not a memecoin and with limited reflexive supply mechanics, but its sub-penny price amplifies percentage swings. In risk-on tapes it can rally sharply as retail rotates into long-tail infra names; in bear regimes (e.g. the 2026-06 extreme-fear tape) it bleeds with broad crypto beta and tracks BTC/ETH direction more than protocol-specific news. Long-run behavior leans toward real network usage (storage contracts) but short/medium-term price is dominated by macro crypto beta and liquidity conditions.

**Risk flags**
- **Liquidity / venue concentration:** effectively single-venue spot depth (Binance) plus an Upbit KRW pocket; thin book means high slippage and fragile execution on size.
- **No liquid perps:** no clean leverage or short access — bearish/hedged expression is limited to spot inventory.
- **Emissions / dilution:** uncapped, inflationary [[proof-of-work|PoW]] emissions continuously add supply, structurally capping per-unit price appreciation.
- **Narrative dependence:** value thesis hinges on decentralized-storage adoption converting committed capacity into paid utilization; demand has stayed niche versus hyperscaler clouds.
- **Regulatory / regional:** notable Korean-retail (Upbit KRW) exposure means regional exchange or regulatory shifts can move liquidity disproportionately.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SCUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=SCUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SCUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=SCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

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

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SC |
| **Market Cap Rank** | #633 |
| **Market Cap** | $30.62M |
| **Current Price** | $0.00061569 |
| **Genesis Date** | 2015-06-06 |
| **Hashing Algorithm** | Blake2b |
| **Categories** | Smart Contract Platform, Storage, DePIN, Proof of Work (PoW), Made in USA |
| **Website** | [https://sia.tech/](https://sia.tech/) |

---

## Overview

Sia is a decentralized cloud storage platform similar in concept to Dropbox and other centralized storage provider where instead of renting storage space from a centralized entity, clients rent storage space from other peers. The only difference is Sia uses blockchain to facilitate transactions Nodes provide storage to clients using the Sia blockchain as contracts. Before storing the data, the data is encrypted into many pieces and uploaded to different hosts. 

Siacoin is created by David Vorick and Luke Champine of Nebulous Inc. As the traditional storage platforms are higher in cost, more expensive and data is not well protected. Siacoin promises to offer secured storage transactions with smart contracts which is more affordable and reliable. Moreover, it is completely open source which means many individuals have contributed to Siacoin’s software hence there will be an active community building innovative applications on top if the Sia API. 

In 2018, Siacoin aims to introduce file sharing and be the go-to cloud storage platform for companies. Their goal is divided into 3 time frames which are short-term, medium-term and long-term development. Short-term development focuses on file sharing between Sia users. This allows Sia users to share files in the platform without having to take it off the cloud while increasing network utilization. Medium-term development’s goal is to enhance partnerships. This means reaching out to large companies like Netflix and Dropbox to hopefully be able to be their storage and distribution framework. Lastly, long-term development aims to expand its horizon to share files with non-Sia users and support mobile wallets.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 49.75B SC |
| **Total Supply** | 49.75B SC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $30.62M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0929 (2018-01-06) |
| **Current vs ATH** | -99.34% |
| **All-Time Low** | $0.00001262 (2015-12-28) |
| **Current vs ATL** | +4775.98% |
| **24h Change** | +1.08% |
| **7d Change** | +0.01% |
| **30d Change** | -15.58% |
| **1y Change** | -82.03% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SC/USDT | N/A |
| Kraken | SC/USD | N/A |
| Upbit | SC/KRW | N/A |
| Crypto.com Exchange | SC/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://sia.tech/](https://sia.tech/) |
| **Twitter** | [@siafoundation](https://twitter.com/siafoundation) |
| **Reddit** | [https://www.reddit.com/r/siacoin](https://www.reddit.com/r/siacoin) |
| **GitHub** | [https://github.com/SiaFoundation](https://github.com/SiaFoundation) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.80M |
| **Market Cap Rank** | #633 |
| **24h Range** | $0.00060722 — $0.00062022 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
