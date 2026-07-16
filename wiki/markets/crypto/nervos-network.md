---
title: "Nervos Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["CKB", "Nervos"]
entity_type: protocol
founded: 2019
headquarters: "Decentralized"
website: "http://nervos.org"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[layer-1]]", "[[layer-2]]", "[[proof-of-stake]]", "[[proof-of-work]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[oi-confirmed-trend]]"]
---

# Nervos Network

**Nervos Network** (ticker **CKB**) is a [[proof-of-work]] [[layer-1]] built around the **Common Knowledge Base (CKB)** — a UTXO-style "store of assets" chain whose generalized **Cell model** extends [[bitcoin|Bitcoin's]] UTXO design to hold arbitrary state and run smart contracts. Nervos is architected as a layered crypto-economy: CKB (layer 1) serves as a secure, censorship-resistant trust and value-preservation root, while higher [[layer-2]] generation layers handle high-throughput transactions. It is designed for sustainable security and decentralization, and carries quantum-resistance among its design goals.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | CKB |
| **Market Cap Rank** | #443 |
| **Market Cap** | $51.35M |
| **Current Price** | $0.00104816 |
| **24h Change** | -0.34% |
| **7d Change** | -8.58% |
| **24h Volume** | $3.47M |
| **Circulating Supply** | ~48.99B CKB |
| **Fully Diluted Valuation** | ~$52.20M |
| **All-Time High** | $0.0437 (2021-03-31) — now -97.6% |
| **All-Time Low** | $0.00099 (2026-06-06) — now +5.6% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. CKB is the *weakest* 7-day performer in this peer group (-8.58%). It trades roughly 6% above its fresh all-time low (~$0.00099, set 2026-06-06) and about 98% below its March-2021 all-time high of $0.0437.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~48.99B CKB |
| **Total Supply** | ~49.81B CKB |
| **Max Supply** | Uncapped base + capped hard cap (see note) |
| **Fully Diluted Valuation (FDV)** | ~$52.20M |
| **Market Cap / FDV** | ~0.98 |

CKB uses a distinctive **dual-issuance** model. There is a hard-capped **"base issuance" of 33.6B CKB** released to miners on a halving schedule (Bitcoin-like), plus a **"secondary issuance" of 1.344B CKB/year** that continues indefinitely to pay for state-storage rent. Crucially, CKB tokens represent on-chain **storage capacity** (1 CKB ≈ 1 byte of state), so holding state on-chain consumes CKB — a state-rent design that ties token demand to actual data storage. Secondary issuance effectively charges occupied state space, while CKB locked in the Nervos DAO is shielded from this inflation. MC/FDV ≈ 0.98 indicates near-full circulation of the currently issued supply.

---

## How & Where It Trades

**Spot venues.** CKB is listed on [[binance]] (CKB/USDT), Upbit (CKB/KRW), Bitget, KuCoin, and Crypto.com, among others.

**Derivatives.** CKB perpetuals are available on major centralized derivatives venues. The wiki's prior snapshot did **not** record a CKB perp on [[hyperliquid]], so do not assume one exists — verify the live venue list before trading derivatives. With a ~$51M market cap and ~$3.1M daily volume, liquidity is thin; funding/OI should be checked live before any leveraged exposure.

---

## Technology & Consensus

Nervos CKB is secured by **[[proof-of-work]]** using **Eaglesong**, a custom hash function intended to resist early ASIC centralization. Distinctive elements:

- **Cell model.** A generalization of [[bitcoin|Bitcoin's]] UTXO: each "Cell" can store arbitrary data and is governed by lock/type scripts, enabling general smart contracts on a UTXO substrate while preserving UTXO's parallelism and verifiability.
- **CKB-VM.** A RISC-V–based virtual machine that runs scripts as native binaries, giving developers broad language flexibility and forward-compatibility (e.g., adding new cryptographic primitives, including quantum-resistant signatures, without hard forks).
- **Layered design.** CKB is the trust/settlement layer-1; throughput scales via [[layer-2]] generation layers, and Nervos has pursued Bitcoin-interoperability initiatives positioning CKB as a programmability layer adjacent to Bitcoin.

---

## Use Case, Narrative & Category

Nervos sits in the **store-of-value / interoperability L1** category, with a Bitcoin-adjacent thesis: a [[proof-of-work]], UTXO-based, quantum-resistant chain optimized for asset preservation and as a programmable settlement root. More recent positioning has leaned into **Bitcoin layer-2 / RGB++**-style interoperability narratives. Tagged categories include Smart Contract Platform, Interoperability, Layer 2 (L2), Rollup, Proof of Work (PoW), Quantum-Resistant, Made in China, plus VC-portfolio tags (Multicoin, DragonFly, Sequoia, Blockchain Capital, Polychain).

---

## Valuation Framing (qualitative)

- **MC/FDV ~0.98:** near-full circulation of currently issued supply, so there is little near-term unlock overhang on the *issued* tokens. However, CKB is *not* hard-capped — the perpetual secondary issuance (1.344B CKB/year) means supply grows indefinitely to fund state-rent, a slow structural dilution distinct from a one-time unlock.
- **State-demand-as-value:** uniquely, CKB's fundamental demand is tied to *on-chain storage* (1 CKB ≈ 1 byte of state). In principle, more applications storing state = more CKB locked = tighter float. In practice, low application traction means this demand sink is largely theoretical today.
- **At the floor:** trading only ~6% above a fresh all-time low ($0.00099, 2026-06-06) and ~98% below ATH. Recovery to prior highs implies a ~42x move, so the realistic bull case is a partial re-rating on the Bitcoin-L2/RGB++ interoperability narrative rather than a return to peak.
- **Security-budget reflexivity:** as a smaller PoW chain, a depressed CKB price weakens miner economics and the security budget — a reflexive risk that compounds in deep drawdowns (see Risks).

---

## Peer Comparison

CKB against other small/mid-cap L1s in this cohort (data as of 2026-06-21):

| Token | Ticker | Price | Market Cap | Rank | 7d % | MC/FDV | Consensus / category |
|---|---|---|---|---|---|---|---|
| **Nervos** | CKB | $0.00104816 | $51.3M | #443 | -8.58% | 0.98 | PoW UTXO / store-of-value |
| [[oasis-network]] | ROSE | $0.0066718 | $52.0M | #439 | +4.12% | 0.78 | PoS / confidential compute |
| [[dusk-network]] | DUSK | $0.085452 | $50.4M | #449 | -5.68% | 1.00 | PoS / regulated RWA |
| [[aelf]] | ELF | $0.064383 | $52.9M | #432 | -0.72% | 0.82 | DPoS / AI L1 |
| [[theta-token\|Theta]] | THETA | $0.15476 | $154.8M | #206 | -3.34% | 1.00 | PoS / DePIN compute |

CKB is the only [[proof-of-work]] chain in this group; all peers are [[proof-of-stake]] variants. It was the weakest 7-day performer of the cohort, reflecting both the soft RGB++ narrative and PoW security-budget concerns under sustained price weakness.

---

## Notable History

- Founded in 2019; the CKB mainnet ("Lina") launched on **2019-11-15** (genesis date).
- CKB printed its all-time high of **$0.0437 on 2021-03-31** during the prior bull cycle.
- It has since declined ~98%, reaching a fresh all-time low of **$0.00099 on 2026-06-06**.
- As of 2026-06-21 it trades at ~$0.00105, about 6% off the low, with a soft -8.6% weekly print amid the broad bear regime.

---

## Risks

- **Proof-of-work cost / sustainability.** As a smaller PoW chain, CKB's security budget depends on token price and miner economics; depressed prices can pressure hashrate and security.
- **State-rent complexity.** The CKB-as-storage / secondary-issuance model is unusual and can be hard for users and developers to reason about, raising adoption friction.
- **Adoption gap.** Despite a long track record, on-chain application traction has been modest relative to leading smart-contract platforms.
- **Narrative dependence.** Recent upside has hinged on the Bitcoin-L2/RGB++ interoperability narrative, which is competitive and unproven at scale.
- **Severe drawdown / liquidity.** Down ~98% from ATH, only ~6% above a fresh all-time low, with thin (~$3.5M/day) volume under an extreme-fear macro backdrop.

---

## Trading Profile

### Venues & liquidity

CKB is tradable on [[binance]] — **spot** (CKB/USDT) and a **USD-margined perpetual** with the associated derivatives telemetry (funding, open interest, liquidations). It is **not** listed on [[hyperliquid]], so Binance is the **primary leveraged venue** and the reference point for any funding/OI/liquidation signal. With a small-cap footprint (~$44M market cap, ~$2–3M daily spot volume), the CKB perp book is thin: leverage amplifies slippage on size, funding can whip sharply on modest positioning shifts, and liquidation clusters resolve fast. Practical implication — size down, use limit entries and staged fills rather than market sweeps, and treat the single-venue concentration as an execution risk (no cross-venue depth to absorb a cascade). Verify live funding/OI on Binance before opening any leveraged exposure.

### Applicable strategies

- [[funding-rate-harvest]] — thin, retail-driven CKB perp funding on Binance can run persistently one-sided, letting a delta-neutral spot-vs-perp position collect the carry.
- [[crowded-long-funding-fade]] — CKB rallies on RGB++/BTC-L2 narrative pops tend to over-extend perp longs; fade elevated positive funding into mean reversion.
- [[liquidation-cascade-fade]] — low float plus concentrated Binance liquidity makes CKB prone to sharp forced-liquidation flushes that overshoot, offering rebound entries.
- [[oi-confirmed-trend]] — pairing Binance open-interest expansion with price direction filters genuine CKB breakouts from thin-liquidity fakeouts.
- [[cash-and-carry]] — when the CKB perp trades at a funding/basis premium to spot, a long-spot / short-perp carry captures the spread with hedged directional risk.
- [[rsi-mean-reversion]] — trading ~6% above a fresh all-time low in a bounded low-volatility range, CKB spot often reverts from oscillator extremes.

### Volatility & regime character

Small-cap (rank ~472) [[proof-of-work]] infrastructure/L1 token with high beta to BTC and broad-altcoin risk appetite. Price action is narrative-reflexive — swings hinge on the Bitcoin-L2 / RGB++ interoperability story rather than fundamentals — but without memecoin-style pure-reflexivity; the state-rent tokenomics give it a (largely theoretical) demand anchor. As the only PoW chain in its peer cohort, it carries added security-budget reflexivity in deep drawdowns. Realized volatility is elevated on thin liquidity, and directional moves are strongly conditioned on the overall crypto regime (currently an established bear market with extreme-fear sentiment).

### Risk flags

- **Liquidity / venue concentration:** Binance is effectively the sole deep leveraged venue; thin books mean high slippage and fast, disorderly liquidations. No [[hyperliquid]] fallback.
- **Emissions / dilution:** uncapped design — perpetual secondary issuance (~1.344B CKB/year) is a slow structural dilution distinct from discrete unlocks; MC/FDV ~0.98 means little near-term unlock overhang on issued supply.
- **Narrative dependence:** upside is tightly coupled to the competitive, unproven Bitcoin-L2/RGB++ interoperability thesis; a fading narrative removes the main bid.
- **Drawdown / floor risk:** down ~98% from ATH and only marginally above a fresh all-time low, with PoW security-budget reflexivity compounding downside in sustained weakness.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CKBUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=CKBUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=CKB` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=CKB` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CKBUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=CKBUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=CKB"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

## See Also

- [[crypto-markets]]
- [[bitcoin]]
- [[layer-1]]
- [[layer-2]]
- [[proof-of-work]]
- [[proof-of-stake]]
- [[oasis-network]]
- [[dusk-network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CKB |
| **Market Cap Rank** | #472 |
| **Market Cap** | $44.27M |
| **Current Price** | $0.00090079 |
| **Genesis Date** | 2019-11-15 |
| **Categories** | Smart Contract Platform, Interoperability, Layer 2 (L2), Rollup, Proof of Work (PoW), Made in China, Quantum-Resistant |
| **Website** | [http://nervos.org](http://nervos.org) |

---

## Overview

Nervos is a layered crypto-economy network. Nervos separates the infrastructure of a crypto-economy into two layers: a verification layer (layer 1) that serves as a trust root and smart custodian, and a generation layer (layer 2) for high-performance transactions and privacy protection.

This document provides an overview of the Nervos Common Knowledge Base (CKB), a public permissionless blockchain and layer 1 of Nervos. CKB generates trust and extends this trust to upper layers, making Nervos a trust network. It's also the value store of the Nervos network, providing public, secure and censorship-resistant custody services for assets, identities and other common knowledge created in the network.

The Nervos Common Knowledge Base (Nervos CKB for short) is a preservation focused, "Store of Assets" blockchain. Architecturally, it's designed to best support on-chain state and off-chain computation; economically, it's designed to provide sustainable security and decentralization. Nervos CKB is the base layer of the overall Nervos Network.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 49.14B CKB |
| **Total Supply** | 49.97B CKB |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $45.01M |
| **Market Cap / FDV Ratio** | 0.98 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0437 (2021-03-31) |
| **Current vs ATH** | -97.94% |
| **All-Time Low** | $0.00085009 (2026-07-01) |
| **Current vs ATL** | +6.13% |
| **24h Change** | -0.27% |
| **7d Change** | +0.53% |
| **30d Change** | -21.79% |
| **1y Change** | -79.20% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CKB/USDT | N/A |
| Upbit | CKB/KRW | N/A |
| Bitget | CKB/USDT | N/A |
| KuCoin | CKB/USDT | N/A |
| Crypto.com Exchange | CKB/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://nervos.org](http://nervos.org) |
| **Twitter** | [@nervosnetwork](https://twitter.com/nervosnetwork) |
| **Reddit** | [https://www.reddit.com/r/NervosNetwork/](https://www.reddit.com/r/NervosNetwork/) |
| **Telegram** | [nervosnetwork](https://t.me/nervosnetwork) (10,467 members) |
| **GitHub** | [https://github.com/nervosnetwork/ckb](https://github.com/nervosnetwork/ckb) |
| **Whitepaper** | [https://github.com/nervosnetwork/rfcs/blob/master/rfcs/0002-ckb/0002-ckb.md](https://github.com/nervosnetwork/rfcs/blob/master/rfcs/0002-ckb/0002-ckb.md) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,140 |
| **GitHub Forks** | 226 |
| **Commits (4 weeks)** | 100 |
| **Pull Requests Merged** | 3,141 |
| **Contributors** | 58 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.27M |
| **Market Cap Rank** | #472 |
| **24h Range** | $0.00089801 — $0.00092390 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
