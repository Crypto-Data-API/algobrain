---
title: "Nano"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, altcoins]
aliases: ["RaiBlocks", "XNO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://nano.org"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[fear-and-greed-index]]", "[[layer-1]]", "[[proof-of-stake]]", "[[stablecoins]]", "[[binance]]", "[[dca-strategy]]", "[[range-trading]]"]
---

# Nano

**Nano** (ticker **XNO**, formerly RaiBlocks) is a **feeless, low-latency Layer-1 cryptocurrency** built on an innovative **block-lattice** data structure (a [[bitcoin|Bitcoin]]-alternative payments coin rather than a smart-contract platform). Each account has its own blockchain, and consensus is reached via **Open Representative Voting (ORV)** — a delegated, balance-weighted vote similar to Proof-of-Stake but **without inflationary rewards and without locking the native coin**. The design goal is simple: a fast, fee-free, energy-light digital cash for everyday payments.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | XNO |
| **Current Price** | $0.365365 |
| **Market Cap** | $48.68M |
| **Market Cap Rank** | #464 |
| **24h Volume** | $80,751 |
| **24h Change** | +2.74% |
| **7d Change** | -0.21% |
| **Fully Diluted Valuation** | $48.68M |
| **All-Time High** | $33.69 (2018-01-02) — now ~-98.9% |
| **All-Time Low** | $0.026179 (2017-07-16) — now ~+1,296% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the backdrop is risk-off — the Crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** in an **established bear market**. XNO is up modestly on the day and roughly flat on the week. Note the **very thin 24h volume (~$81K)** against a ~$49M cap (a ~0.0017 volume/mcap ratio) — a serious liquidity red flag (see Risks). Because supply is fixed and fully circulating, market cap equals FDV with no dilution.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~133.25M XNO |
| **Total Supply** | ~133.25M XNO |
| **Max Supply** | ~133.25M XNO |
| **Market Cap / FDV** | 1.00 |

Nano is **fully distributed** — circulating, total and max supply are identical (~133.25M), giving a **MC/FDV of exactly 1.00 and zero future dilution.** There is no mining issuance and no staking inflation: all coins were distributed via an early faucet, and the supply is fixed. ORV validators ("representatives") secure the network for free, which is what enables the feeless model — but it also means there is **no block reward to fund security**, relying instead on aligned-incentive volunteer/representative operation.

### All-Time Range

| Metric | Value |
|---|---|
| **All-Time High** | $33.69 (2018-01-02) |
| **All-Time Low** | $0.026179 (2017-07-16) |

XNO trades ~99% below its 2018 ATH — a stark illustration of how far the once-hyped feeless-payments narrative has retraced. Notably, XNO is still ~1,296% above its 2017 all-time low ($0.026179), reflecting that it remains far above its earliest faucet-era pricing despite the long post-2018 decline.

---

## Technology & Consensus

Nano's architecture is unusual among [[layer-1]] coins and is the source of both its strengths and its limits:

- **Block-lattice:** instead of one shared chain, **each account has its own blockchain** that only its owner can write to. A transaction is a *pair* of blocks — a "send" on the sender's chain and a matching "receive" on the recipient's. This per-account structure is what enables asynchronous, parallel processing and removes the need for global block production.
- **Open Representative Voting (ORV):** consensus is a delegated, balance-weighted vote. Holders delegate their voting weight to "representatives" (validator nodes); representatives vote on conflicting transactions. It is conceptually similar to delegated [[proof-of-stake]] but with **no inflationary rewards and no locking** of the coin — delegation is non-custodial and reversible at any time.
- **Feeless by design:** because there is no mining and no block reward, there are no transaction fees. Spam is instead mitigated by a small proof-of-work nonce attached to each transaction (recently augmented by mechanisms to prioritize transactions during saturation).
- **Low energy:** the absence of competitive mining makes Nano one of the lowest-energy cryptocurrencies per transaction.

The trade-off is that there is **no protocol-funded security budget**: representatives operate voluntarily, so the network's resilience depends on aligned-incentive operation by exchanges, services, and large holders rather than on economic reward.

---

## How & Where It Trades

XNO is a **spot** asset. On-file CoinGecko venues:

### Centralized Exchanges
| Exchange | Pair |
|---|---|
| Binance | XNO/USDT |
| Kraken | NANO/USD |
| KuCoin | XNO/USDT |
| Crypto.com Exchange | XNO/USD |

Despite top-tier listings, **observed daily volume is extremely low (~$81K)**. No perpetual-futures / [[hyperliquid|Hyperliquid]] listing is recorded on file, so [[funding-rate|funding]]/open-interest metrics are not applicable — exposure is purely spot. The combination of major-CEX listings with paper-thin volume means the order books can be shallow; sizable trades risk meaningful slippage, and the asset is sensitive to single-actor flows. Among the six coins in this cohort, XNO has by far the **lowest absolute turnover and the lowest volume/market-cap ratio**, making it the most liquidity-constrained name in the group.

---

## Use Case / Narrative / Category

CoinGecko tags Nano under **Layer 1, Payment Solutions, Directed Acyclic Graph (DAG), and "Made in USA."** The pitch is **instant, feeless peer-to-peer cash**: no transaction fees, near-instant confirmation, and very low energy use (no Proof-of-Work mining). Nano (as RaiBlocks) was among the earliest DAG-style cryptocurrencies, alongside Byteball and IOTA, breaking the linear-blockchain mold to improve throughput. Its enduring use case is micropayments and remittance-style transfers where fee-free settlement matters — but it competes directly with [[stablecoins|stablecoins]] and [[layer-2|Layer-2]] payment rails that have captured much of the "fast cheap payments" demand.

---

## Valuation Framing (qualitative)

Nano is one of crypto's purest **"fixed-supply, no-dilution, single-purpose"** assets: there is no emission schedule, no unlock cliff, no staking yield, and no smart-contract revenue — so there is no cash-flow or token-velocity model to anchor a valuation. Its ~$49M cap is essentially a pure read on residual demand for a feeless-payments coin. The bear case is structural: stablecoins on fast L1s/L2s now deliver near-instant, low-cost transfers *with a price-stable unit*, removing Nano's original edge for the payments use case. The bull case is narrower — a fixed-supply, feeless, low-energy bearer asset for niche micropayment or censorship-resistant transfer contexts. The ~$81K daily volume suggests the market currently treats it as a low-attention legacy name. This is framing, not a price target.

---

## Peer Comparison

| Token | Symbol | Category | Mkt Cap | Rank | MC/FDV | 24h Vol | Notes |
|---|---|---|---|---|---|---|---|
| **Nano** | XNO | Feeless payments L1 (DAG) | ~$48.7M | #464 | ~1.00 | ~$0.08M | Fixed supply; lowest liquidity |
| [[ontology\|Ontology]] | ONT | DID / trust L1 | ~$45.8M | #487 | ~1.00 | ~$4.8M | Dual-token; also no overhang |
| [[berachain-bera\|Berachain]] | BERA | DeFi-native L1 (PoL) | ~$63.5M | #381 | ~0.51 | ~$18.1M | Newer, heavy dilution |
| [[sonic-3\|Sonic]] | S | High-TPS EVM L1 | ~$107.9M | #258 | ~0.97 | ~$29.8M | Ex-[[fantom\|Fantom]] |

*(Comparison figures from the same 2026-06-21 snapshot.)* XNO and [[ontology|ONT]] are the two fixed/fully-distributed legacy L1s; XNO stands out for its uniquely thin turnover.

---

## Notable History

- Original **RaiBlocks** paper and beta published **December 2014** — one of the first DAG-based cryptocurrencies.
- Rebranded from RaiBlocks to **Nano** in 2018.
- ATH of **$33.69** on 2018-01-02 during the prior bull mania; never reclaimed.
- Ongoing open-source development (GitHub repo on file: `nanocurrency/raiblocks`), with active contributors and merged PRs recorded.

> *Additional dated events will be added through the wiki's source-ingestion workflow as relevant articles are processed.*

---

## Risks

- **Severe liquidity risk** — ~$81K daily volume on a ~$49M cap is dangerously thin; entry/exit slippage and price-manipulation risk are elevated, especially in extreme fear ([[fear-and-greed-index|Fear & Greed]] = 23).
- **Narrative obsolescence** — feeless payments are now contested by [[stablecoins]] and [[layer-2|L2s]]; XNO has lost mindshare since 2018.
- **Security-funding model** — no block reward and no fees means network security depends on voluntary representative operation; spam-mitigation has been a recurring engineering challenge for feeless chains.
- **No smart-contract utility** — pure payments coin; limited composability versus L1 ecosystems.
- **Deep, persistent drawdown** — down ~99% from ATH reflects sustained loss of speculative interest.

---

## Related

- [[crypto-markets]]
- [[bitcoin]] — a payments-coin reference point
- [[layer-1]]
- [[stablecoins]] — the main competitive threat to feeless payments
- [[proof-of-stake]] — ORV is a delegated, vote-based relative
- [[fear-and-greed-index]] — macro sentiment gauge
- [[ontology]], [[berachain-bera]], [[sonic-3]] — L1 peers

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko; `raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XNO |
| **Market Cap Rank** | #477 |
| **Market Cap** | $43.82M |
| **Current Price** | $0.3289 |
| **Hashing Algorithm** | Directed Acyclic Graph (DAG) |
| **Categories** | Layer 1 (L1), Payment Solutions, Made in USA, Directed Acyclic Graph (DAG) |
| **Website** | [https://nano.org](https://nano.org) |

---

## Overview

Nano, a low-latency cryptocurrency built on an innovative block-lattice data structure offering unlimited scalability and no transaction fees. Nano by design is a simple protocol with the sole purpose of being a high-performance cryptocurrency. The Nano protocol can run on low-power hardware, allowing it to be a practical, decentralized cryptocurrency for everyday use. It uses an ORV (Open Representative Voting) consensus algorithm, which is similar to PoS (Proof of Stake) but without inflationary rewards not locking of the native coin XNO.

The original Nano (RailBlocks) paper and first beta implementation were published in December, 2014, making it one of the first Directed Acyclic Graph (DAG) based cryptocurrencies [6]. Soon after, other DAG cryptocurrencies began to develop, most notably DagCoin/Byteball and IOTA. These DAG-based cryptocurrencies broke the blockchain mold, improving system performance and security. Byteball achieves consensus by relying on a “main-chain” comprised of honest, reputable and user-trusted “witnesses”, while IOTA achieves consensus via the cumulative PoW of stacked transactions. Nano achieves consensus via a balance-weighted vote on conflicting transactions. This consensus system provides quicker, more deterministic transactions while still maintaining a strong, decentralized system. Nano continues this development and has positioned itself as one of the highest performing cryptocurrencies.

Nano is a trustless, feeless, low-latency cryptocurrency that utilizes a novel blocklattice structure and delegated Proof of Stake voting. The network requires minimal resources, no high-power mining hardware, and can process high transaction throughput. All of this is achieved by having individual blockchains for each account, eliminating access issues and inefficiencies of a global data-structure. We identified possible attack vectors on the system and presented arguments on how Nano is resistant to these forms of attacks.

Check out CoinBureau...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 133.25M XNO |
| **Total Supply** | 133.25M XNO |
| **Max Supply** | 133.25M XNO |
| **Fully Diluted Valuation** | $43.82M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $33.69 (2018-01-02) |
| **Current vs ATH** | -99.02% |
| **All-Time Low** | $0.0262 (2017-07-16) |
| **Current vs ATL** | +1155.80% |
| **24h Change** | +4.61% |
| **7d Change** | -0.01% |
| **30d Change** | -15.15% |
| **1y Change** | -65.87% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | XNO/USDT | N/A |
| Kraken | NANO/USD | N/A |
| KuCoin | XNO/USDT | N/A |
| Crypto.com Exchange | XNO/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://nano.org](https://nano.org) |
| **Twitter** | [@nano](https://twitter.com/nano) |
| **Reddit** | [https://www.reddit.com/r/nanocurrency](https://www.reddit.com/r/nanocurrency) |
| **Telegram** | [nanocurrency](https://t.me/nanocurrency) (4,024 members) |
| **GitHub** | [https://github.com/nanocurrency/raiblocks](https://github.com/nanocurrency/raiblocks) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 3,522 |
| **GitHub Forks** | 807 |
| **Commits (4 weeks)** | 18 |
| **Pull Requests Merged** | 3,250 |
| **Contributors** | 90 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $930,783.00 |
| **Market Cap Rank** | #477 |
| **24h Range** | $0.3132 — $0.3338 |
| **CoinGecko Sentiment** | 25% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

XNO is **tradable on Binance SPOT only** among liquid venues — there is **no liquid perpetual venue**, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding/basis/liquidation strategies do **not** apply. With no perp to hedge or express directional shorts, exposure is effectively long-only spot, and any bearish view must be expressed by exiting or reducing spot rather than shorting. Because observed turnover is extremely thin, venue concentration on a single spot book means order-book depth is shallow: sizing must be small, execution should be patient (limit orders, VWAP-style scaling), and market orders risk meaningful slippage. Position sizing should assume you may be the marginal buyer/seller and that liquidity can vanish in a risk-off tape.

### Applicable strategies

- [[dca-strategy]] — for a fixed-supply, no-dilution legacy name, averaging in over time smooths the thin-liquidity entry problem and avoids paying up on shallow books.
- [[buy-and-hold]] — XNO's zero-emission, fully-distributed supply makes it a clean long-only bearer thesis with no unlock/dilution overhang to erode a hold.
- [[range-trading]] — with a low-attention, mean-reverting price and no perp leverage to force trends, XNO often oscillates in a band that spot range trades can harvest.
- [[rsi-mean-reversion]] — thin-volume spot names spike and fade around single-actor flows, so oscillator extremes tend to revert, favoring fade entries on stretched RSI.
- [[breakout-and-retest]] — because liquidity is fragile, waiting for a breakout to retest confirms real demand before committing size, reducing false-breakout risk on a shallow book.
- [[vwap-trading]] — execution-focused: scaling entries/exits toward VWAP is essential on a single thin spot book to minimize slippage and market impact.

### Volatility & regime character

XNO is a **micro-cap, single-purpose Layer-1 payments coin** (DAG/block-lattice), not a DeFi or memecoin. It behaves as a **low-attention legacy altcoin** with **high idiosyncratic, low-turnover volatility**: with no perpetual market and paper-thin spot volume, price is driven more by sporadic single-actor flows than by leveraged positioning. Its beta to [[bitcoin|BTC]]/ETH is real in broad risk-on/risk-off swings but noisy, and it lacks the reflexive leverage cascades of perp-heavy names. Regime character is best described as **illiquid mean-reversion punctuated by low-liquidity gaps** rather than sustained, trending momentum.

### Risk flags

- **Liquidity / venue concentration** — spot-only on essentially one liquid book with very thin daily turnover; shallow depth means high slippage and elevated single-actor manipulation risk (see Risks section).
- **No perp / long-only** — no liquid perpetual venue means limited short/hedge access; bearish views can only be expressed by selling spot.
- **Narrative dependence** — the feeless-payments thesis is contested by [[stablecoins]] and [[layer-2|L2]] rails; mindshare and speculative interest have faded since 2018.
- **Security-funding model** — no block reward or fees; network security relies on voluntary representative operation, a structural risk versus incentivized chains.
- **No unlock/emission overhang** — a *positive* flag: fully distributed, fixed supply means no token-unlock or emission dilution to trade around.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=XNOUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=XNOUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=XNOUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=XNOUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---
