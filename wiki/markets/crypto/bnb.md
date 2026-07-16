---
title: "BNB (Binance Coin)"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: excellent
tags: [binance, bnb, crypto, exchange-token, layer1, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, defi, altcoins]
entity_type: protocol
aliases: ["BNB", "BNB-Chain", "BSC", "Binance-Coin"]
website: "https://www.bnbchain.org"
related: ["[[binance]]", "[[bitcoin]]", "[[bnb-chain]]", "[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[hyperliquid]]", "[[layer-1]]", "[[solana]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[cash-and-carry]]"]
founded: 2017
headquarters: "Decentralized"
---

# BNB (Binance Coin)

**BNB** (ticker **BNB**) is the native token of [[bnb-chain|BNB Chain]] (formerly Binance Smart Chain), an EVM-compatible [[layer-1|Layer 1]], and the utility token of the [[binance|Binance]] exchange ecosystem. Originally launched as an ERC-20 token on [[ethereum]] in 2017, BNB migrated to its own blockchain and consistently ranks among the top 5 cryptocurrencies by market capitalization. It serves as gas for BNB Chain transactions, provides trading fee discounts on Binance, and powers a large [[defi]] ecosystem anchored by PancakeSwap.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #4 |
| **Market Cap** | ~$79.03B |
| **Current Price** | $586.25 |
| **24h Volume** | ~$715.68M |
| **24h Change** | +2.07% |
| **7d Change** | -2.77% |
| **Circulating Supply** | 134.78M BNB |
| **Max Supply** | 200.00M BNB |
| **All-Time High** | $1,369.99 (2025-10-13) — current ~-57.2% |
| **All-Time Low** | $0.0398 (2017-10-19) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: the broader market sits in **extreme fear** ([[crypto-fear-and-greed-index|Fear & Greed]] = 23) within an **Established Bear Market** regime as of 2026-06-20. BNB is up ~2% over 24h but down ~2.8% on the week, holding its #4 rank better than most large caps in the drawdown — consistent with its exchange-token cash-flow backing and quarterly burn support. It is ~57% below its October-2025 all-time high. See [[market-regime]].

---

## Key Features

| Feature | Detail |
|---|---|
| **Chain** | [[bnb-chain|BNB Chain]] -- EVM-compatible [[layer-1|Layer 1]] |
| **Consensus** | Proof of Staked Authority (PoSA) -- ~21-45 active validators ("Cabinet") |
| **Block Time** | ~3 seconds, fast finality |
| **Use Cases** | Gas fees, Binance fee discounts, BNB Chain DeFi, Launchpad participation, staking |
| **Token Burns** | Quarterly **Auto-Burn** + real-time **BEP-95** gas-fee burn |
| **DeFi Ecosystem** | PancakeSwap, Venus, Alpaca Finance |

---

## Tokenomics & Burn Mechanism

BNB launched in 2017 with a fixed **200M max supply** (50% public ICO, 40% founders, 10% angels) and a permanent commitment to burn down toward a **100M floor**. As of 2026-06-20, ~134.78M BNB circulates (~67% of max), and the protocol is **net-deflationary** through two parallel mechanisms:

1. **Quarterly Auto-Burn** — a formula-driven burn that replaced the old "20% of profits" discretionary buyback. The amount is calculated from BNB's price and the number of blocks produced on BNB Chain during the quarter, so the burn auto-scales with on-chain activity and is fully transparent/auditable on-chain. It runs every quarter until total supply reaches 100M.
2. **BEP-95 real-time burn** — a fixed fraction (~10%) of every block's gas fees is burned continuously, analogous to [[ethereum]]'s EIP-1559 base-fee burn. This ties BNB's supply contraction directly to BNB Chain usage.

Because circulating ≈ total supply (MC/FDV ≈ 1.0), there is **no unlock overhang** — the supply trajectory is monotonically *downward*, a structural contrast to dilution-heavy tokens like [[starknet|STRK]]. This deflationary backstop is a core part of BNB's relative resilience in drawdowns.

---

## BNB Chain Ecosystem

BNB Chain became popular during 2021 as a low-cost alternative to [[ethereum]] for [[defi]] activity. PancakeSwap (a Uniswap fork) is the dominant DEX. The chain's validator set is small (21 nodes), leading to criticism about centralization, but this enables fast block times and low fees.

The relationship between BNB Chain and [[binance|Binance]] (the exchange) means the chain benefits from Binance's massive user base and distribution, but also inherits regulatory risks associated with Binance.

---

## Trading Relevance

- BNB price is closely tied to Binance's business health, trading volumes, and regulatory standing
- Quarterly token burns reduce circulating supply, creating predictable supply-side events
- BNB Chain activity (TVL, DEX volume) serves as a leading indicator for BNB token performance
- BNB Launchpad token sales historically generate buying pressure as participants acquire and lock BNB
- Regulatory actions against Binance directly impact BNB price (e.g., the 2023 DOJ/SEC settlement)

---

## Market Structure & Derivatives

- **Spot venues**: deepest liquidity is on [[binance|Binance]] itself (BNB/USDT, BNB/FDUSD, BNB/BTC), with secondary depth on Kraken, Bitget, KuCoin and Crypto.com. As an exchange-native token, the bulk of BNB's organic flow is concentrated on Binance — a liquidity strength and a single-venue concentration risk.
- **On-chain / DEX**: PancakeSwap (BNB Chain) is the dominant DEX for BNB and BEP-20 pairs.
- **Derivatives**: BNB has perpetual futures on most major venues including a perp on [[hyperliquid]] (BNB-PERP) plus Binance Futures, Bybit, OKX, etc. As a top-5 large cap, BNB carries deep [[open-interest]] and tighter, more two-sided [[funding-rate|funding]] than the small caps in this loop; funding leans positive in risk-on phases and flips negative in fear regimes like the current one. See [[perpetual-futures]] and [[funding-rate-arbitrage]].
- **Liquidity profile**: ~$715M/24h volume on a ~$79B cap (turnover ~0.9%) — far deeper and more resilient than mid/small caps, so large orders clear with modest impact relative to its size.

---

## Valuation Framing (Qualitative)

BNB is unusual among L1 tokens in having a **quasi-equity backing**: its value is tied to [[binance|Binance]]'s exchange business (the largest crypto exchange by volume) plus BNB Chain's on-chain economy, and that value is concentrated into a *shrinking* supply via burns. Qualitative anchors:

- **Cash-flow proxy.** The Auto-Burn scales with BNB price and BNB Chain block production, and BEP-95 burns scale with gas usage — so BNB behaves partly like a buyback-supported equity whose "yield" is supply reduction rather than dividends. This underpins its relative drawdown resilience.
- **Deflation + no overhang.** ~67% of max supply circulating with a downward trajectory (toward 100M) and MC/FDV ≈ 1.0 means no dilution pressure — the supply curve is a tailwind, not a headwind.
- **Binance beta is the swing factor.** The dominant valuation driver is Binance's health: trading volumes, market share, and regulatory standing. Adverse Binance news compresses BNB regardless of on-chain metrics; the 2023 DOJ/SEC settlement is the canonical example.
- **Regulatory discount.** BNB carries an "Alleged SEC Securities" tag and the exchange-token regulatory overhang, which applies a persistent discount versus a "pure" decentralized L1.

## Peer Comparison

| Token | Type | Backing / Driver | Max Supply | Supply Trend | Notes |
|---|---|---|---|---|---|
| **BNB** | Exchange token + L1 | [[binance|Binance]] business + BNB Chain | 200M (→100M) | Deflationary (burns) | #4 cap; PoSA L1; PancakeSwap DeFi hub |
| [[ethereum]] (ETH) | Smart-contract L1 | Largest DeFi/L2 ecosystem | none | Mildly deflationary (EIP-1559) | Decentralized; no single-company link |
| [[solana]] (SOL) | Smart-contract L1 | High-throughput L1 ecosystem | none | Inflationary (declining) | Fast, low-fee; broad app ecosystem |
| OKB | Exchange token | OKX exchange business | capped | Deflationary (burns) | Direct exchange-token peer |
| Cronos (CRO) | Exchange token + L1 | Crypto.com business | capped | Deflationary | Exchange-token peer with own chain |

BNB's distinctive position is the combination of a **large, profitable parent exchange**, a **busy L1/DeFi ecosystem**, and an **aggressive deflationary burn** — a mix none of the pure-L1 majors (ETH/SOL) replicate, at the cost of the centralization and regulatory exposure that come with the Binance link.

---

## Risks

- **Exchange concentration risk** — BNB's value is structurally tied to [[binance|Binance]]'s health, trading volumes, and regulatory standing. Adverse action against Binance flows directly into BNB.
- **Regulatory / securities risk** — BNB has been alleged to be an unregistered security by the SEC; the 2023 DOJ/SEC settlement against Binance is the canonical precedent.
- **Centralization** — only 21 validators secure BNB Chain (Proof of Staked Authority), a recurring criticism versus more decentralized L1s like [[ethereum]] and [[solana]].
- **Bridge / DeFi exploit history** — BNB Chain suffered a major cross-chain bridge exploit in October 2022 (~$570M), illustrating smart-contract and bridge attack surface.
- **Macro / regime risk** — as a top-5 large cap, BNB is exposed to the prevailing **Established Bear Market** and extreme-fear sentiment (Fear & Greed 23) as of 2026-06-20.

---

## Trading Profile

**Venues & liquidity.** BNB is a genuine two-venue perp market. On [[binance|Binance]] it trades as deep spot (BNB/USDT, BNB/FDUSD, BNB/BTC) plus a USD-margined perpetual with very high leverage and the deepest [[open-interest]] and book depth for the asset. On [[hyperliquid]] it lists as BNB-PERP with leverage up to ~40-50x and a transparent on-chain order book. Having both a CEX and a decentralized perp venue means execution can be split across books: large clips clear on Binance with modest impact given its dominant depth, while Hyperliquid offers on-chain settlement and an independent [[funding-rate|funding]] print. The dual venue is what makes CEX-vs-DEX [[funding-rate]] and basis comparisons tradable rather than theoretical, and it lets sizing lean on Binance depth while hedging or arbing on Hyperliquid.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — BNB funding is quoted on both Binance and Hyperliquid, so gaps between the two venue prints are directly harvestable on a top-5 name with reliable depth on each side.
- [[cash-and-carry]] — deep Binance spot plus a liquid perp lets you hold spot BNB and short the perp to capture positive carry with tight execution slippage.
- [[basis-trading]] — the large-cap two-venue structure keeps perp-vs-spot basis measurable and mean-reverting, suitable for systematic basis capture on BNB.
- [[funding-rate-harvest]] — as a top-5 asset, BNB funding leans positive in risk-on phases and flips negative in fear, giving a repeatable delta-neutral carry to collect.
- [[oi-confirmed-trend]] — BNB's deep, two-sided [[open-interest]] makes OI-confirmed breakouts and trend continuation reads more trustworthy than on thin alts.
- [[liquidation-cascade-fade]] — Binance-driven leverage flushes on BNB produce sharp overshoots into deep books, offering fade setups back toward fair value.

**Volatility & regime character.** BNB is a **large-cap, lower-beta major** rather than a high-beta alt or memecoin. It carries a quasi-equity backing (Binance's exchange cash flows plus a deflationary burn) that dampens drawdowns, so it typically holds its rank better than mid/small caps in fear regimes. Correlation to BTC/ETH is high directionally but its beta is muted versus speculative alts; idiosyncratic moves cluster around Binance news, regulatory headlines, and quarterly burn events. In risk-off regimes it behaves like a defensive large cap within the crypto complex.

**Risk flags.**
- **Venue/liquidity concentration** — the bulk of organic BNB flow is Binance-native, so any Binance disruption, outage, or regulatory action hits both the token and its primary book at once.
- **Regulatory / exchange-token overhang** — BNB carries an "Alleged SEC Securities" tag and inherits Binance's regulatory risk; adverse Binance news transmits directly into price regardless of on-chain metrics.
- **Narrative dependence** — price is driven heavily by Binance's health and market share; on-chain BNB Chain metrics matter less than exchange sentiment.
- **Perp funding dislocations** — leverage flushes and one-sided positioning can spike funding and trigger liquidation cascades; the two-venue structure means Binance and Hyperliquid funding can diverge sharply during stress.
- **Supply is deflationary (not a dilution flag)** — no unlock overhang (MC/FDV ~1.0), so unlike emission-heavy tokens the trading risk is concentration and narrative, not supply dumps.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=BNB` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BNB` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BNB&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BNB&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BNB"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

## See Also

- [[binance]] -- The exchange behind BNB
- [[ethereum]] -- The chain BNB Chain is modeled after
- [[defi]] -- DeFi ecosystem on BNB Chain
- [[crypto-markets]] -- Broader market context

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BNB |
| **Market Cap Rank** | #4 |
| **Genesis Date** | 2017-07-08 |
| **Categories** | Smart Contract Platform, Exchange-based Tokens, BNB Chain Ecosystem, Centralized Exchange (CEX) Token, Layer 1 (L1), Ethereum Ecosystem, Alleged SEC Securities, FTX Holdings, Proof of Stake (PoS), GMCI Layer 1 Index, GMCI 30 Index, GMCI Index, Made in China |
| **Website** | [https://www.binance.com](https://www.binance.com) |

> *Live price/cap/volume figures are consolidated in the **Market Data** block above (2026-06-20). Tables below carry historical and supply detail.*

---

## Overview

BNB is the native utility token of the BNB Chain ecosystem, acting as a multi-chain asset that powers decentralized applications and facilitates value exchange across its network. It serves as the primary asset for paying transaction gas and smart contract deployment fees while providing users with tiered fee discounts on the Binance exchange. The project’s main value proposition lies in its unified multi-chain architecture, which integrates a smart contract platform, a Layer 2 scaling solution, and a decentralized data storage network into a cohesive settlement and data availability layer.

The network operates on a Proof of Staked Authority consensus mechanism, utilizing a group of 21 active validators known as the Cabinet to verify transactions and produce blocks every 3 seconds. Validators are elected daily based on the amount of BNB staked or delegated to them, and the system employs fast finality and slashing penalties to maintain security and integrity. To manage its long-term economy, the project uses a programmatic dual-burn strategy that permanently removes tokens through real-time fee destruction and quarterly buybacks.

Launched in 2017 by the Binance platform, the project initially distributed 50% of its 200 million token supply to the public, while the founding team received 40% and angel investors were allocated 10%. Though it began as a token on the Ethereum network, it eventually migrated to its own autonomous architecture that remains fully compatible with the Ethereum Virtual Machine. Today, the token's utility includes paying for network gas, participating in staking rewards, and enabling decentralized governance through which holders can vote on technical upgrades and economic changes.

---

## Supply Snapshot

| Metric | Value |
|---|---|
| **Circulating Supply** | 134.78M BNB |
| **Total Supply** | 134.78M BNB |
| **Max Supply** | 200.00M BNB (burning toward 100M) |
| **Circulating / Max Supply** | ~67% |
| **Market Cap / FDV Ratio** | 1.00 (no unlock overhang) |

> *See **Tokenomics & Burn Mechanism** above for how the Auto-Burn and BEP-95 burns drive supply down over time.*

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1,369.99 (2025-10-13) |
| **Current vs ATH** | ~-57.2% |
| **All-Time Low** | $0.0398 (2017-10-19) |
| **Current vs ATL** | ~+1,472,000% |
| **24h Change** | +2.07% |
| **7d Change** | -2.77% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xb8c77482e45f1f44de1745f52c74426c631bdd52` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BNB/USDT | N/A |
| Kraken | BNB/USD | N/A |
| Bitget | BNB/USDT | N/A |
| KuCoin | BNB/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | BNB-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.binance.com](https://www.binance.com) |
| **Twitter** | [@binance](https://twitter.com/binance) |
| **Reddit** | [https://www.reddit.com/r/binance](https://www.reddit.com/r/binance) |
| **GitHub** | [https://github.com/binance-exchange/binance-official-api-docs](https://github.com/binance-exchange/binance-official-api-docs) |
| **Whitepaper** | [https://github.com/bnb-chain/whitepaper/blob/master/WHITEPAPER.md](https://github.com/bnb-chain/whitepaper/blob/master/WHITEPAPER.md) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 4,243 |
| **GitHub Forks** | 2,044 |
| **Pull Requests Merged** | 55 |
| **Contributors** | 26 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$715.68M |
| **Market Cap Rank** | #4 |
| **CoinGecko Sentiment** | 40% positive |
| **Last Updated** | 2026-06-20 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original snapshot
- Market data as of 2026-06-20: `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko snapshot); market backdrop (Fear & Greed 23, "Established Bear Market") from `raw/data/crypto-loop/_digest.md`.

---

## Related

- [[binance]] — the exchange behind BNB
- [[bnb-chain]] — the EVM-compatible Layer 1
- [[ethereum]] — the chain BNB Chain is modeled after
- [[solana]] — competing high-throughput L1
- [[defi]] — DeFi ecosystem on BNB Chain
- [[hyperliquid]] — venue for BNB-PERP
- [[crypto-markets]] — broader market context

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 133.17M BNB |
| **Total Supply** | 133.17M BNB |
| **Max Supply** | 200.00M BNB |
| **Fully Diluted Valuation** | $76.84B |
| **Market Cap / FDV Ratio** | 1.00 |

---
