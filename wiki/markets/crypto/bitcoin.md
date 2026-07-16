---
title: "Bitcoin"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, markets, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["BITCOIN", "BTC", "XBT"]
entity_type: protocol
founded: 2009
headquarters: "Decentralized"
website: "https://bitcoin.org"
related: ["[[bitcoin-etfs]]", "[[crypto-markets]]", "[[ethereum]]", "[[halving]]", "[[perpetual-futures]]", "[[proof-of-work]]", "[[hyperliquid]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# Bitcoin

**Bitcoin** (BTC) is the first and largest [[crypto-markets|cryptocurrency]] by market capitalization. Created in 2009 by the pseudonymous **Satoshi Nakamoto**, Bitcoin introduced the concept of a decentralized, peer-to-peer electronic cash system secured by cryptographic proof rather than trust in third-party institutions. It remains the dominant asset in crypto markets, consistently commanding 50-60% of total crypto market capitalization -- a metric known as **BTC dominance**.

Bitcoin is widely referred to as "digital gold" due to its fixed supply cap, censorship resistance, and role as a store of value in diversified portfolios. As the macro anchor of the asset class, BTC sets the risk tone for every other token: [[ethereum|ETH]], [[solana|SOL]], and the long tail of altcoins.

---

## Market Data

| Metric | Value |
|---|---|
| **Rank** | #1 |
| **Price** | $63,455 |
| **Market Cap** | $1.272 trillion |
| **24h Volume** | $21.28 billion |
| **24h Change** | +1.28% |
| **7d Change** | -0.51% |
| **Circulating Supply** | 20,045,346 BTC (~95.5% of cap) |
| **Total Supply** | 20,045,346 BTC |
| **Max Supply** | 21,000,000 BTC (hard cap) |
| **All-Time High** | $126,080 (2025-10-06) — currently -49.7% |
| **All-Time Low** | $67.81 (2013-07-06) — currently +93,478% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** The [[crypto-market-sentiment|Crypto Fear & Greed Index]] reads **22 (Extreme Fear)** and the long-horizon regime classifier flags an **Established Bear Market**. BTC trades roughly halfway below its October 2025 ATH of $126,080, consistent with a deep cyclical drawdown rather than a structural collapse. In extreme-fear regimes BTC dominance typically rises as capital rotates out of altcoins into the perceived safety of the largest asset.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BTC (also XBT on some platforms) |
| **Creator** | Satoshi Nakamoto (pseudonymous, identity unknown) |
| **Genesis Block** | January 3, 2009 |
| **Consensus** | [[proof-of-work]] (SHA-256 double hash) |
| **Max Supply** | 21,000,000 BTC (hard cap) |
| **Block Time** | ~10 minutes (target) |
| **Difficulty Adjustment** | Every 2,016 blocks (~2 weeks) |
| **Last [[halving]]** | April 2024 (block reward reduced to 3.125 BTC) |
| **Next [[halving]]** | Expected ~2028 (reward → 1.5625 BTC) |
| **Website** | [bitcoin.org](https://bitcoin.org) |

---

## Technology & Consensus

### Blockchain & Proof of Work

Bitcoin operates on a distributed [[blockchain]] -- a public, append-only ledger where every transaction is recorded in blocks linked cryptographically. Miners compete to find a block-header hash below a target value ([[proof-of-work]], SHA-256) to validate blocks and earn newly minted BTC plus transaction fees. This mechanism ensures network security without requiring a central authority: rewriting history would require out-computing the honest majority of global hashrate.

The mining **difficulty** adjusts every 2,016 blocks (~2 weeks) to maintain the target 10-minute block interval, regardless of how much total computing power (hashrate) is directed at the network. Sustained all-time-high hashrate is a common bull-market security signal; sharp hashrate drops (e.g., mining bans, energy shocks) can pressure miner balance sheets and force BTC selling.

### UTXO Model & Script

Bitcoin uses an **unspent transaction output (UTXO)** accounting model rather than the account-balance model used by [[ethereum|Ethereum]]. Transactions consume prior outputs and create new ones, validated by a deliberately limited scripting language. This conservative design prioritizes auditability and security over programmability — the opposite trade-off from EVM chains.

### Upgrades: SegWit & Taproot

| Upgrade | Year | Effect |
|---|---|---|
| **SegWit** | 2017 | Separated signature data, raised effective block capacity, fixed transaction malleability, enabled [[lightning-network|Lightning]] |
| **Taproot** | 2021 | Schnorr signatures + MAST; improved privacy, efficiency, and complex-spend flexibility; later enabled Ordinals/inscriptions |

### Scaling: The Lightning Network

The **Lightning Network** is a Layer 2 payment protocol built on top of Bitcoin for fast, low-cost transactions. By opening payment channels between participants and settling only the net result on the main [[blockchain]], Lightning addresses Bitcoin's base-layer throughput limit (~7 transactions per second). It has seen growing adoption for micropayments, point-of-sale, and cross-border remittances, though its volume remains a small fraction of total BTC settlement.

---

## Tokenomics & Supply Schedule

Bitcoin's monetary policy is hard-coded: only **21 million BTC** will ever exist, and roughly **95.5%** has already been mined. New supply enters circulation through block rewards, cut in half approximately every four years in an event called the [[halving]]. This predictable, disinflationary issuance is central to the "digital gold" thesis and contrasts sharply with discretionary fiat monetary policy.

### The Halving Cycle

The [[halving]] reduces miner block rewards by 50% roughly every 210,000 blocks (~4 years):

| Halving | Year | Block Reward | Cumulative Supply (approx.) |
|---|---|---|---|
| Genesis | 2009 | 50 BTC | -- |
| 1st | 2012 | 25 BTC | ~10.5M mined |
| 2nd | 2016 | 12.5 BTC | ~15.75M mined |
| 3rd | 2020 | 6.25 BTC | ~18.375M mined |
| 4th | 2024 | 3.125 BTC | ~19.7M mined |
| 5th (est.) | ~2028 | 1.5625 BTC | ~20.6M mined |

Historically, each [[halving]] has preceded a multi-year bull cycle, though past performance is not indicative of future results, and the [[bitcoin-etfs|ETF]] era may dampen or alter the classic four-year rhythm. The supply-shock narrative -- reduced new issuance meeting steady or growing demand -- remains one of the most discussed frameworks in crypto trading.

### The Fee-Security Transition

As block rewards approach zero over the coming decades, Bitcoin's security budget must transition from issuance to **transaction fees**. Whether organic fee demand (base-layer settlement, inscriptions, Lightning routing) can sustain the security budget post-2040 is a long-running open debate and a structural risk for the network.

---

## Ecosystem & Use Cases

- **Store of value / "digital gold"** — the dominant thesis; BTC as a non-sovereign, fixed-supply reserve asset.
- **Settlement layer** — final settlement for large-value transfers; Lightning for retail-scale payments.
- **Collateral** — BTC is the premier collateral asset across [[defi]], CeFi lending, and [[perpetual-futures|derivatives]] margin.
- **Inscriptions / Ordinals & BRC-20** — post-Taproot, arbitrary data and fungible-token experiments now drive periodic fee spikes.
- **Wrapped BTC** — wBTC and similar bring BTC liquidity onto [[ethereum|Ethereum]] and other smart-contract chains for [[defi]] use.
- **Legal tender / reserves** — El Salvador adopted BTC as legal tender; other states hold strategic reserves.

---

## Market Structure & Derivatives

Bitcoin trades **24/7/365** across hundreds of venues, with the deepest order books in crypto.

| Characteristic | Detail |
|---|---|
| **Liquidity** | Highest in the asset class; tightest spreads |
| **Volatility** | High by TradFi standards (~50-80% annualized), moderate by crypto standards |
| **Correlation** | Increasingly correlated with risk assets (equities, especially Nasdaq), but retains idiosyncratic behavior in crypto-specific events |
| **Dominance** | BTC dominance fluctuates ~40-65% of total crypto market cap |
| **Primary spot pairs** | BTC/USDT ([[binance]]), BTC/USD ([[coinbase]], Kraken) |
| **Primary perp** | BTC-PERP ([[hyperliquid]]), plus all major CEX perp venues |

### Spot Bitcoin ETFs

In January 2024, the [[sec|U.S. Securities and Exchange Commission]] approved the first spot [[bitcoin-etfs|Bitcoin ETFs]] -- a watershed for institutional access. Major issuers including **BlackRock** (iShares Bitcoin Trust, **IBIT**), **Fidelity** (FBTC), and **ARK/21Shares** launched products that collectively attracted tens of billions in AUM within the first year. Most use [[coinbase|Coinbase]] as custodian, making Coinbase critical institutional infrastructure.

Daily ETF **net flows** have become a leading short-term price indicator: persistent inflows absorb sell pressure and tighten float, while sustained outflows (common in extreme-fear regimes like the current one) amplify downside. *(Flow magnitudes vary daily and are not quoted here to avoid stale figures.)*

### Perpetual Futures & Funding

BTC-PERP is the single highest-volume market on [[hyperliquid|Hyperliquid]] and a bellwether across CEX venues. The [[funding-rate]] on BTC perps reflects positioning: persistently positive funding signals crowded longs (squeeze risk on a flush), while negative funding signals capitulation/short crowding. [[open-interest]] expansion alongside rising price is healthy; OI expansion into stalling price warns of leverage build-up and [[liquidation]] cascades.

---

## On-chain & Valuation Frameworks

Bitcoin has the richest set of on-chain valuation tools in crypto. These describe *which metrics matter*; live values are not invented here.

| Metric | What it measures | Trading use |
|---|---|---|
| **Realized Cap** | Aggregate cost basis (value of coins at last-moved price) | Floor/"fair value" reference vs market cap |
| **[[mvrv|MVRV]]** | Market cap ÷ realized cap | >3.5 historically frothy; <1 historically deep value |
| **[[nupl|NUPL]]** | Net Unrealized Profit/Loss across supply | Maps euphoria → capitulation zones |
| **SOPR** | Spent Output Profit Ratio | <1 = coins moving at a loss (capitulation) |
| **Dormancy / HODL waves** | Age distribution of moving coins | Long-term holder accumulation vs distribution |
| **Hashrate / Difficulty** | Network security spend | Miner stress and capitulation signals |
| **Exchange balances** | BTC held on exchanges | Falling = accumulation/self-custody; rising = sell intent |

In an **Established Bear Market** with **Extreme Fear (22)**, traders watch for MVRV/NUPL pressing into historical capitulation zones and long-term-holder accumulation as early base-building signals.

---

## Trading Playbook

- **Macro anchor first** — BTC trend dictates altcoin risk appetite; do not fight BTC direction with alt longs.
- **Dominance rotation** — rising BTC dominance = risk-off (alts bleed vs BTC); falling dominance = "alt season." Track in extreme fear, dominance usually grinds up.
- **ETF flow tape** — net inflows/outflows as a daily directional tell (US session sensitive).
- **Funding & OI** — fade extreme positive [[funding-rate]]; respect [[open-interest]]/[[liquidation]] clusters as magnet levels.
- **Regime-aware sizing** — in a confirmed bear/extreme-fear regime, favor smaller size, defined-risk longs near on-chain cost-basis zones, and avoid leveraged trend-chasing.
- **Cycle context** — position relative to [[halving]] timing and prior cycle drawdown depths, while acknowledging the ETF era may compress historical patterns.

---

## History & Cycles

| Date (approx.) | Price | Significance |
|---|---|---|
| 2009 | $0 | Genesis; no market price |
| Oct 2009 | $0.001 | First recorded exchange rate |
| Feb 2011 | $1.00 | Parity with US dollar |
| Nov 2013 | $1,000 | First four-figure price |
| Dec 2017 | $19,783 | First major retail mania peak |
| Mar 2020 | $3,800 | COVID crash low |
| Nov 2021 | $68,789 | Cycle peak (pre-ETF era) |
| Jan 2024 | -- | Spot [[bitcoin-etfs|Bitcoin ETFs]] approved by [[sec|SEC]] |
| Late 2024 | $100,000+ | Six-figure Bitcoin achieved |
| Oct 2025 | $126,080 | All-time high |
| Jun 2026 | $63,455 | Deep bear-market drawdown (~-50% from ATH) |

Bitcoin's price history is defined by multi-year boom-and-bust cycles, historically correlated with the [[halving]] schedule and broader macro liquidity conditions.

---

## Competitive Positioning

Bitcoin competes less with other crypto assets and more with traditional store-of-value assets (gold, sovereign bonds). Within crypto it is the benchmark against which all "betas" are measured.

| Asset | Rank | Mkt Cap | Consensus | Core thesis |
|---|---|---|---|---|
| **Bitcoin (BTC)** | #1 | $1.27T | [[proof-of-work]] | Digital gold / store of value |
| [[ethereum\|Ethereum (ETH)]] | #2 | $208B | [[proof-of-stake]] | Programmable settlement / "ultrasound money" |
| [[solana\|Solana (SOL)]] | #7 | $41.5B | PoH + [[proof-of-stake\|PoS]] | High-throughput monolithic L1 |
| [[tron\|TRON (TRX)]] | #8 | $30.6B | DPoS | Stablecoin settlement rail |

> Peer market data as of 2026-06-20 (CoinGecko). See [[bitcoin-vs-ethereum]] for the canonical BTC/ETH comparison.

---

## Regulatory

- **US**: BTC is treated as a **commodity** by the CFTC; spot ETFs are SEC-approved. Most regulatory attention now centers on custody, market structure, and tax (IRS treats BTC as property).
- **Global**: Adoption ranges from legal tender (El Salvador) to outright mining/trading bans (varies by jurisdiction). The EU's MiCA framework provides a comprehensive regime for crypto-asset service providers.
- **Mining**: Energy-use scrutiny and regional mining bans/incentives are recurring policy themes affecting hashrate geography.

---

## Risks

- **Macro/liquidity** — BTC is highly sensitive to global liquidity and risk sentiment; tightening cycles drive deep drawdowns (current Established Bear Market).
- **Regulatory** — adverse rulings on custody, ETFs, or mining can compress flows.
- **Security budget** — long-run reliance on fee revenue as block subsidy decays.
- **Concentration** — ETF/custodian concentration ([[coinbase]]) and large-holder ("whale") distribution risk.
- **Quantum (long-tail)** — future cryptographic threats to ECDSA/SHA-256, mitigated by potential protocol upgrades.
- **Volatility & leverage** — [[liquidation]] cascades on crowded [[perpetual-futures|perps]] amplify moves in both directions.

> **Risk warning:** Crypto assets are highly volatile and speculative. Nothing here is investment advice. In the current Extreme-Fear / bear regime, leveraged directional exposure carries elevated liquidation risk.

---

## Related

- [[ethereum]] -- Second-largest crypto; the other "blue chip" and primary BTC/ETH relative-value trade
- [[solana]] -- High-throughput Layer 1, major altcoin beta
- [[tron]] -- Stablecoin settlement rail, top-10 asset
- [[halving]] -- Bitcoin's supply-reduction mechanism
- [[bitcoin-etfs]] -- Spot Bitcoin ETFs and their market impact
- [[proof-of-work]] -- Bitcoin's consensus mechanism
- [[lightning-network]] -- Bitcoin's Layer 2 payments protocol
- [[hyperliquid]] -- DEX where BTC-PERP is the top market
- [[binance]] / [[coinbase]] -- Largest CEX venue and primary US-regulated exchange + ETF custodian
- [[perpetual-futures]] / [[funding-rate]] / [[open-interest]] / [[liquidation]] -- Derivatives toolkit
- [[crypto-markets]] -- Overview of the cryptocurrency market landscape
- [[bitcoin-vs-ethereum]] -- Detailed comparison of the two largest crypto assets

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original auto-generated entity data
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko bulk endpoints (`raw/data/crypto-loop/coingecko-markets.json`); macro backdrop from `raw/data/crypto-loop/_digest.md` (Fear & Greed = 22; regime = Established Bear Market)
- Hyperliquid market microstructure context — QuickNode SQL Explorer, 2026-04-06

## Overview

HarryPotterObamaSonic10Inu (Ticker: BITCOIN) is a endgame of crypto-assets (0 Tax). BITCOIN incentivizes the creation of novel and entertaining meme content. With ownership renounced and Liquidity locked, our robust growing community has taken the lead; we have successfully completed a full audit, an NFT collection, and are exploring partnerships with other tokens in the space, a one-of-a -kind website, and one-of-a-kind merchandise and ecommerce site in the works based on the legendary meme that inspired BITCOIN's creation. Our goal is to create an ecosystem for active community members to meet, collaborate, and share our rich lore (the archive of our token's storied history) with the world.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 999.80M BITCOIN |
| **Total Supply** | 999.80M BITCOIN |
| **Max Supply** | 1.00B BITCOIN |
| **Fully Diluted Valuation** | $12.70M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3734 (2024-10-13) |
| **Current vs ATH** | -96.57% |
| **All-Time Low** | $0.00066337 (2023-05-31) |
| **Current vs ATL** | +1830.94% |
| **24h Change** | +0.06% |
| **7d Change** | -1.52% |
| **30d Change** | -2.39% |
| **1y Change** | -86.31% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x72e4f9f808c49a2a61de9c5896298920dc4eeea9` |
| Berachain | `0x6b26f778bfae56cfb4bf9b62c678d9d40e725227` |
| Base | `0x2a06a17cbc6d0032cac2c6696da90f29d39a1a29` |
| Solana | `CTgiaZUK12kCcB8sosn4Nt2NZtzLgtPqDwyQyr2syATC` |
| Binance Smart Chain | `0xc4044d67585d421495fb0bf08c50b15683647003` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | HPOS10I/USD | N/A |
| KuCoin | HPOS10I/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X72E4F9F808C49A2A61DE9C5896298920DC4EEEA9/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X72E4F9F808C49A2A61DE9C5896298920DC4EEEA9/0XE0F63A424A4439CBE457D80E4F4B51AD25B2C56C | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hpos10i.com](https://hpos10i.com) |
| **Twitter** | [@hpos10ireturns](https://twitter.com/hpos10ireturns) |
| **Telegram** | [hpos10i](https://t.me/hpos10i) (13,273 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $585,256.00 |
| **Market Cap Rank** | #1033 |
| **24h Range** | $0.0123 — $0.0130 |
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

BTC is the deepest, most liquid market in crypto and trades as a **two-venue** book across both [[binance]] (spot BTC/USDT plus USD-margined BTC perpetual) and [[hyperliquid]] (BTC-PERP, leverage up to ~40-50x). Order-book depth and tight spreads on both venues let traders execute size with minimal slippage and split flow between a centralized and an on-chain venue. This dual availability underpins cross-venue basis, funding, and arbitrage plays: the same exposure can be built spot on Binance and hedged on Hyperliquid (or vice versa), and deep liquidity supports large clip sizing without disturbing the mark. Because BTC-PERP is Hyperliquid's single highest-volume market, its L2 book and funding are among the most reliable references in the asset class.

### Applicable strategies

- [[cash-and-carry]] — buy spot BTC on [[binance]] and short the perp/future to harvest the basis; BTC's deep two-venue liquidity makes the carry cheap to build and unwind.
- [[funding-rate-harvest]] — BTC perp funding is large and persistent enough (crowded-long episodes) that a delta-neutral spot-vs-perp position collects funding at scale.
- [[hl-vs-cex-funding-divergence]] — funding on [[hyperliquid]] BTC-PERP and Binance's USD-margined perp can diverge; the pair trades the spread with tight execution on both books.
- [[crowded-long-funding-fade]] — in euphoric BTC regimes, persistently positive funding flags over-levered longs vulnerable to a flush; fade the crowded side.
- [[liquidation-cascade-fade]] — BTC leverage clusters produce sharp [[liquidation]] wicks that mean-revert; deep books allow scaling into the flush and out on the rebound.
- [[oi-confirmed-trend]] — rising [[open-interest]] alongside BTC price confirms trend conviction, while OI expansion into stalling price warns of exhaustion.

### Volatility & regime character

BTC is the **large-cap benchmark** of crypto — the lowest-beta major asset and the reference against which every altcoin's beta is measured. Volatility is high by TradFi standards (~50-80% annualized) but moderate relative to smaller-cap crypto. It has essentially zero "correlation to BTC beta" because it *is* BTC beta; it leads [[ethereum|ETH]] and the alt complex, and in extreme-fear regimes BTC dominance rises as capital rotates out of alts into BTC. Increasingly correlated with macro risk assets (notably the Nasdaq) while retaining idiosyncratic behavior around crypto-specific events (halvings, ETF flows, on-chain shocks).

### Risk flags

- **Perp funding dislocations** — crowded-long funding on BTC perps precedes squeeze/liquidation flushes; extreme funding is a positioning warning, not a directional guarantee.
- **Liquidation cascades** — leveraged [[perpetual-futures]] positioning amplifies moves in both directions around OI/liquidation clusters.
- **Macro/liquidity sensitivity** — BTC drawdowns track global liquidity and risk sentiment (current Established Bear Market); tightening cycles drive deep declines.
- **Concentration** — ETF/custodian concentration ([[coinbase]]) and large-holder ("whale") distribution can move an otherwise deep market.
- **Regulatory** — adverse custody, ETF, or mining rulings can compress flows and shift the tape.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=BTC` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BTC&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BTC"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
