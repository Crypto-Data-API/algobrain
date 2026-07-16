---
title: "Qtum"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["QTUM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://qtum.org/en/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[proof-of-stake]]", "[[zilliqa]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Qtum

**Qtum** (QTUM) is a decentralized, open-source [[layer-1]] smart-contract platform that fuses [[bitcoin]]'s UTXO transaction model with an Ethereum Virtual Machine, running on [[proof-of-stake]] consensus. It is governed via a Decentralized Governance Protocol (DGP) that lets the community vote to adjust certain on-chain parameters. The design aims to combine Bitcoin's security with [[ethereum]]-style programmability.

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | QTUM |
| **Current Price** | $0.723873 |
| **Market Cap** | $76,753,740 |
| **Market Cap Rank** | #326 |
| **24h Volume** | $4,729,030 |
| **24h Change** | +0.38% |
| **7d Change** | -0.15% |
| **Fully Diluted Valuation** | ~$78.0M |
| **Market Cap / FDV** | ~0.98 |
| **All-Time High** | $100.22 (2018-01-06), ~-99.3% |
| **All-Time Low** | $0.654592 |
| **Consensus** | Proof of Stake |
| **Categories** | Smart Contract Platform, Proof of Stake (PoS), Made in China |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** The 2026-06-21 snapshot is in an *Established Bear Market* with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **~23 (extreme fear)** and [[bitcoin]] dominance near 59%. QTUM was roughly flat over 24h (+0.4%) and 7d (-0.2%), but remains ~99.3% below its January 2018 all-time high of $100.22 and trades only ~11% above its all-time low.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~106.05M QTUM |
| **Total Supply** | ~107.82M QTUM |
| **Max Supply** | Uncapped (block-reward emissions) |
| **Fully Diluted Valuation** | ~$78.0M |
| **Market Cap / FDV Ratio** | ~0.98 |

Qtum's supply is near-fully circulating (MC/FDV ≈ 0.98), so there is **no meaningful unlock cliff** — but the **max supply is uncapped**: new QTUM is issued continuously as block rewards to stakers under its [[proof-of-stake]] model. This makes QTUM **mildly inflationary** indefinitely, diluting non-staking holders, in contrast to capped peers like [[zilliqa]] (21B cap) or [[immutable-x|IMX]] (2B cap). Token holders can stake to validate transactions and earn rewards, which provides yield while securing the chain. The original distribution came from a 2017 ICO: 51% of tokens were sold to the public (raising ~$15.7M in ~5 days), with 29% allocated to community incentives and 20% to early backers and the founding team.

---

## How & Where It Trades

### Spot venues

| Exchange | Pair |
|---|---|
| Binance | QTUM/USDT |
| Kraken | QTUM/USD |
| Upbit | QTUM/KRW |
| Bitget | QTUM/USDT |
| KuCoin | QTUM/USDT |
| Crypto.com Exchange | QTUM/USD |

QTUM maintains broad CEX coverage including Binance, Kraken, and the Korean Upbit KRW market. ~$4.7M in 24h volume at the snapshot is modest (turnover ~6% of cap). No active perpetual/derivatives listing on [[hyperliquid]] is recorded in the current snapshot, so leveraged exposure is constrained to whatever CEX perp markets exist off-snapshot.

---

## Technology & Consensus

Qtum is a [[layer-1]] hybrid that builds on a Bitcoin Core fork while adding smart-contract capability:

- **UTXO + EVM:** it retains [[bitcoin]]'s UTXO accounting (chosen for its simplicity and stability) and bridges it to a Turing-complete EVM via an Account Abstraction Layer, so Ethereum-style contracts and dApps run on top of a Bitcoin-derived base.
- **Proof-of-Stake:** node operators stake QTUM to validate blocks and earn rewards, rather than mining.
- **Decentralized Governance Protocol (DGP):** smart-contract-based on-chain governance that lets the community vote to modify certain network parameters (e.g. block size, gas schedules) without hard forks.

Co-founders include Patrick Dai, Neil Mahi, and Jordan Earls, with team members previously at Tencent, Alibaba, and Nasdaq.

---

## Use Case, Narrative & Category

Qtum's narrative is the **"Bitcoin-Ethereum hybrid"** — combining Bitcoin's battle-tested UTXO security with Ethereum's smart-contract flexibility, plus formal on-chain governance. It targets the smart-contract-platform category and competes with [[ethereum]] and other [[layer-1]] chains, with a "Made in China" regional association alongside peers like [[zilliqa]].

---

## Valuation Framing (Qualitative)

- **Fully-circulating legacy L1:** with MC/FDV ≈ 0.98 there is essentially no hidden dilution from locked allocations; the only ongoing dilution is the uncapped staking emission, which is gradual rather than cliff-shaped.
- **Deepest drawdown in the cohort:** QTUM is ~99.3% below its 2018 cycle peak of $100.22 — the largest ATH drawdown among the six pages in this batch — reflecting a chain that has held a niche but never recaptured first-cycle relevance.
- **"Hybrid" premium has compressed:** the UTXO+EVM design was differentiated in 2017; today EVM compatibility is commoditised and Bitcoin-security narratives are served by newer BTC-L2s, leaving QTUM priced as a durable but low-growth legacy small-cap (~$77M).

---

## Peer Comparison

| Token | Category | Price | Market Cap | Rank | MC/FDV | Max Supply |
|---|---|---|---|---|---|---|
| **Qtum (QTUM)** | UTXO+EVM [[layer-1]] | $0.7239 | ~$76.8M | #326 | ~0.98 | Uncapped |
| [[zilliqa\|Zilliqa (ZIL)]] | Sharded [[layer-1]] | $0.00312 | ~$61.0M | #392 | ~0.93 | 21.0B |
| [[metal-blockchain\|Metal (METAL)]] | Avalanche-fork [[layer-1]] | $0.1247 | ~$63.3M | #379 | ~0.76 | 666.67M |
| [[proton\|XPR Network (XPR)]] | DPoS [[layer-1]] payments | $0.00225 | ~$64.3M | #375 | ~0.89 | Uncapped |

*All figures from the 2026-06-21 snapshot. QTUM is the highest market cap and rank of the legacy small-cap L1 cluster, and (with XPR) one of two uncapped-supply chains in the group.*

---

## Notable History

- ICO in 2017 raised ~$15.7M, distributing 51M tokens to the public (11,156.766 BTC and 77,081.031 ETH collected).
- All-time high of **$100.22** on 2018-01-06; price is down ~99.3% from that peak as of the 2026-06-21 snapshot.

---

## Risks

- **Relevance & mindshare:** developer activity is modest and the project competes against far larger smart-contract ecosystems.
- **Inflationary issuance:** uncapped block-reward emissions dilute non-staking holders.
- **Regulatory exposure:** "Made in China" association carries Chinese crypto-policy risk.
- **Bear-market beta:** as a small-cap alt (rank #326), QTUM is highly sensitive to the prevailing extreme-fear regime (Crypto [[fear-and-greed-index|Fear & Greed]] ~23).
- **Liquidity:** ~$4.7M of 24h volume and no on-snapshot perp venue make large-size execution and hedging difficult.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Trading Profile

### Venues & liquidity

QTUM is tradable on [[binance]] as both **spot** (QTUM/USDT) and a **USD-margined perpetual**, so it carries the full perp data stack — funding, open interest, and liquidations. It is **not** listed on [[hyperliquid]], which makes Binance the primary (effectively sole liquid) leveraged venue. This venue concentration matters for execution: with only one deep perp market and thin spot volume (~$4–5M/24h, turnover only a few percent of a ~$77M cap), leverage should be sized conservatively — order books are shallow, funding can swing sharply on small directional flow, and there is no alternative perp venue to hedge or arbitrage against. Large tickets should be worked with [[vwap-trading]]-style slicing rather than crossed at market, and stops must account for wide intraday ranges and slippage.

### Applicable strategies

- [[funding-rate-harvest]] — a single-venue Binance perp with modest OI means funding can dislocate; delta-neutral spot-vs-perp harvesting captures the premium when longs crowd in.
- [[cash-and-carry]] — pair Binance spot QTUM against the USD-M perp to lock basis when the perp trades rich to spot, a clean carry on a fully-circulating legacy L1 with no unlock cliff.
- [[liquidation-cascade-fade]] — shallow single-venue liquidity makes QTUM prone to sharp forced-liquidation wicks; fading exhausted cascades back toward VWAP is a repeatable edge in a thin book.
- [[range-mean-reversion]] — a low-growth small-cap that spends long stretches chopping around its ATL zone reverts well to range midpoints absent a fresh catalyst.
- [[oi-confirmed-trend]] — using Binance open-interest changes to confirm (or reject) breakouts filters false moves in an illiquid name where price alone is noisy.
- [[crypto-beta-rotation]] — as a high-beta legacy alt, QTUM is a rotation candidate that outperforms on risk-on legs and should be underweighted in the prevailing extreme-fear regime.

### Volatility & regime character

QTUM is a **legacy small-cap [[layer-1]]** (rank ~#337, ~$77M cap) with high downside beta to [[bitcoin]] and broad-market risk sentiment. It is an infrastructure/smart-contract token rather than a memecoin, so its moves are driven by liquidity conditions and BTC/ETH correlation more than by reflexive social cycles. Having lost ~99% from its 2018 peak and trading near all-time lows, it behaves as a low-momentum, mean-reverting small-cap that amplifies market-wide drawdowns and offers sporadic sharp squeezes on thin liquidity rather than sustained independent trends.

### Risk flags

- **Venue concentration:** perp liquidity and derivatives data concentrate on Binance alone (no Hyperliquid, thin CEX perp depth), so a single-venue outage, delisting, or funding spike has outsized impact and no hedge alternative.
- **Liquidity:** ~$4–5M of 24h spot volume makes large-size execution and hedging difficult; expect slippage and gapping.
- **Inflationary emissions:** uncapped [[proof-of-stake]] block rewards dilute non-staking holders indefinitely (gradual, not cliff-shaped).
- **Narrative decay:** the UTXO+EVM "hybrid" thesis has largely commoditized, leaving weak independent catalysts and heavy dependence on broad-market beta.
- **Regulatory:** the "Made in China" association carries Chinese crypto-policy risk that can trigger listing or sentiment shocks.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=QTUMUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=QTUMUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=QTUM` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=QTUM` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=QTUMUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=QTUMUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=QTUM"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bitcoin]]
- [[ethereum]]
- [[layer-1]]
- [[proof-of-stake]]
- [[zilliqa]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | QTUM |
| **Market Cap Rank** | #336 |
| **Market Cap** | $71.60M |
| **Current Price** | $0.6751 |
| **Hashing Algorithm** | Proof of Stake |
| **Categories** | Smart Contract Platform, Proof of Stake (PoS), Made in China |
| **Website** | [https://qtum.org/en/](https://qtum.org/en/) |

---

## Overview

Qtum is a decentralized and open-source smart contracts platform and value transfer protocol. Qtum uses proof-of-stake consensus, meaning node operators are rewarded for validating transactions. It is a DGP governed blockchain where community participants can vote to change certain network parameters. Qtum is built on a bitcoin core fork, but the foundation has created its own hybrid blockchain with the help of several key tools. The coin uses bitcoin’s chain because of its simple and stable nature, allowing the foundation to build upon it more easily.

As the QTUM project is a hybrid of Bitcoin and Ethereum, its team comprises of members from both Bitcoin and Ethereum community. They also have team members who formerly worked with Tencent, Alibaba, Nasdaq etc. Apart from that, they are backed by some notable VCs and prominent people from the Blockchain community such as Patrick Dai (Project Co-Founder), Neil Mahi (Chief Blockchain Architect/Co-Founder) and Jordan Earls (Lead Developer/Co-Founder).

Qtum provides a Turing-complete blockchain stack and is able to execute smart contracts and decentralised applications like the Ethereum blockchain.

Qtum builds on Bitcoin's UTXO transaction model and uses the Proof-of-Stake algorithm. It is backed by some highly prominent members of the blockchain community such as Anthony Di Iorio, Xu Star, Bo Shen, David Lee, Jehan Chu and Roger Ver.

Qtum sold over 10 million dollars’ worth of its tokens after only 90 minutes, eventually raising a total value of $15.7 million before stopping the campaign early after only 5 days. They raised a total amount of 11,156.766 bitcoins (BTC) and 77,081.031 ether (ETH) in exchange for the 51 million Qtum tokens being distributed to the public. In Qtum’s whitepaper, 51% of the coins were distributed to the public via the crowdfunding campaign. Of the remaining 49%, 29% of the coins would be allocated as community incentives, and the remaining 20% would be distributed to the early backers and ...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 106.07M QTUM |
| **Total Supply** | 107.82M QTUM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $72.79M |
| **Market Cap / FDV Ratio** | 0.98 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $100.22 (2018-01-06) |
| **Current vs ATH** | -99.33% |
| **All-Time Low** | $0.6399 (2026-06-25) |
| **Current vs ATL** | +5.50% |
| **24h Change** | -1.49% |
| **7d Change** | -3.50% |
| **30d Change** | -10.31% |
| **1y Change** | -70.84% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | QTUM/USDT | N/A |
| Kraken | QTUM/USD | N/A |
| Upbit | QTUM/KRW | N/A |
| Bitget | QTUM/USDT | N/A |
| KuCoin | QTUM/USDT | N/A |
| Crypto.com Exchange | QTUM/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://qtum.org/en/](https://qtum.org/en/) |
| **Twitter** | [@qtum](https://twitter.com/qtum) |
| **Reddit** | [https://www.reddit.com/r/Qtum](https://www.reddit.com/r/Qtum) |
| **GitHub** | [https://github.com/qtumproject/qtum](https://github.com/qtumproject/qtum) |
| **Whitepaper** | [https://qtum.org/wp-content/uploads/2017/02/Qtum_blockchain_economy_whitepaper_20170209_EN.pdf](https://qtum.org/wp-content/uploads/2017/02/Qtum_blockchain_economy_whitepaper_20170209_EN.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,187 |
| **GitHub Forks** | 407 |
| **Pull Requests Merged** | 427 |
| **Contributors** | 30 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.82M |
| **Market Cap Rank** | #336 |
| **24h Range** | $0.6728 — $0.6977 |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
