---
title: "IOST"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["IOST", "IOStoken", "Internet of Services Token"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "http://iost.io/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# IOST

**IOST** (Internet of Services Token) is a high-throughput [[layer-1|Layer-1]] smart-contract blockchain designed to provide scalable infrastructure for decentralized services and applications. Its defining feature is a custom consensus mechanism called **Proof-of-Believability (PoB)** — a [[proof-of-stake|stake]]-and-reputation hybrid Byzantine-fault-tolerant scheme intended to deliver higher transaction throughput than first-generation chains while keeping node participation broad. The IOST token is the native asset used to pay transaction fees, stake for network resources (via "GAS"/"RAM"-style resource models), and participate in node election and governance. As of 2026-06-21 IOST trades at **$0.0007811**, ranked **#693** with a market cap of **$26,559,497**; it is **+1.85%** over 24h and **-2.71%** over 7 days.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | IOST |
| **Market Cap Rank** | #693 |
| **Market Cap** | $26,559,497 |
| **Current Price** | $0.0007811 |
| **24h Change** | +1.85% |
| **7d Change** | -2.71% |
| **Genesis Date** | 2018-01-11 |
| **Consensus** | Proof-of-Believability (PoB), a [[proof-of-stake|PoS]]-reputation hybrid |
| **Categories** | [[layer-1|Layer 1 (L1)]], [[smart-contracts|Smart Contract Platform]], BNB Chain Ecosystem |
| **Website** | [http://iost.io/](http://iost.io/) |

---

## Overview

IOST ("Internet of Services Token") is a [[layer-1|Layer-1]] [[smart-contracts|smart-contract]] platform launched in 2018 with the stated goal of providing ultra-high-throughput blockchain infrastructure for a decentralized economy. The project was backed by venture investors including Sequoia and Matrix Partners.

Its signature consensus algorithm, **Proof-of-Believability (PoB)**, is a [[proof-of-stake|stake]]-plus-reputation Byzantine-fault-tolerant design. Rather than ranking validators purely by stake, PoB factors in a node's IOST balance, a reputation-based "Servi" token balance, network contributions, and behavior — the aim being to keep block production fast while discouraging misbehavior and preserving broad participation. IOST's architecture also describes complementary scaling techniques such as a fast BFT finality mechanism, microstate blocks, an Atomic Commit protocol, and a sharding approach ("Efficient Distributed Sharding") intended to raise throughput and reduce validator resource requirements.

The platform supports dapps and smart contracts and has historically promoted itself on transaction speed and low fees for consumer-facing services. The project was co-founded by **Terrence Wang, Jimmy Zhong, Ray Xiao**, and others. Beyond its own native chain, IOST is also available as a wrapped token on the BNB Chain ecosystem.

---

## Architecture — How It Works

IOST's design is a bundle of techniques aimed at one goal: raising throughput without forcing validators to run expensive hardware, so that node participation can stay broad. The main components are:

- **Proof-of-Believability (PoB) consensus.** Rather than ranking validators purely by stake (as in classic [[proof-of-stake|PoS]]) or by hashpower (as in [[proof-of-work|PoW]]), PoB computes a "believability" score for each node from several inputs: its IOST balance, its balance of a non-transferable reputation token called **Servi**, its historical contributions to the network, and its behavior/reviews. Higher-believability nodes are placed into a fast "believable league" that produces blocks quickly, while a "normal league" verifies and finalizes. The Servi system is meant to be a sybil-resistant reputation layer — Servi is earned by good behavior and is destroyed (reset to zero) after a node serves, so reputation must be continuously re-earned.
- **Efficient Distributed Sharding (EDS).** IOST's sharding scheme partitions validators into committees that process transactions in parallel, with the protocol periodically and unpredictably reshuffling membership to resist targeted attacks on any one shard.
- **Atomix / Atomic Commit.** A cross-shard commit protocol designed to keep transactions that touch multiple shards consistent (all-or-nothing), which is the hard part of any sharded execution model.
- **Microstate blocks.** A technique to shrink the state each node must store and transmit, lowering bandwidth and storage requirements so that more participants can run nodes.
- **Account & resource model.** IOST uses an account-based model (similar in spirit to EOS) with a staking-for-resources design: users stake IOST to obtain **GAS** (a regenerating compute allowance) and **RAM** (storage), letting some interaction patterns proceed without a direct per-transaction fee. Smart contracts are written primarily in **JavaScript**, which lowers the barrier for mainstream web developers relative to chains that require Solidity, Rust, or Move.

Net effect: IOST is an EOS/Tendermint-era "high-TPS L1" whose differentiation is the reputation-weighted PoB validator selection and a JavaScript-friendly contract environment. As with all such chains, the theoretical TPS headline matters far less than realized, fee-paying demand for blockspace.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 32.72B IOST |
| **Total Supply** | 32.72B IOST |
| **Max Supply** | 90.00B IOST |
| **Fully Diluted Valuation** | $34.88M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1298 (2018-01-24) |
| **Current vs ATH** | ~-99.4% |
| **All-Time Low** | $0.00100592 (2026-03-29) |
| **24h Change** | +1.85% |
| **7d Change** | -2.71% |

> IOST trades roughly 99% below its January-2018 peak. The 7-day change of -2.71% is consistent with broad small-cap weakness under the current **Extreme Fear** regime (Fear & Greed 22, [[btc-bitcoin|BTC]] ~$64,180 on 2026-06-21). Max supply (90B IOST) exceeds circulating supply, so some future dilution remains.

---

## Value Accrual & Governance

IOST has three primary demand sinks, all of which are gated by actual usage of the chain:

- **Fees / resources.** Using the network consumes GAS, which is obtained by staking IOST. Net new demand for blockspace therefore increases the amount of IOST that must be locked to obtain GAS, removing float from the tradeable supply.
- **Node staking and election.** To become or back a block-producing node, IOST must be staked. Token holders vote for "Servi nodes," and stakers share in block rewards. This is the largest structural lock-up mechanism but is sensitive to the staking yield versus the market price of IOST.
- **Governance.** IOST holders vote on protocol parameters and node election. Because PoB blends stake with reputation, governance is not purely plutocratic, but stake remains a major input.

The central weakness of IOST's value-accrual story is the same as its peers: in the absence of large, sticky, fee-generating applications, the GAS sink is small and the token's value rests mostly on speculative and staking-yield demand rather than on cash-flow-like fee burn.

---

## Comparison vs Peer High-Throughput L1s

IOST is best understood against the 2017–2018 cohort of "Ethereum-killer" high-TPS chains and their modern successors. It does not compete with [[bitcoin|Bitcoin]]; it competes for smart-contract developers and consumer dApps.

| Dimension | **IOST** | [[solana|Solana]] | BNB Chain | [[tron|Tron]] |
|---|---|---|---|---|
| Consensus | Proof-of-Believability (PoS + reputation, BFT) | PoS + Proof-of-History | PoS (BSC, 21+ validators) | Delegated PoS (27 SRs) |
| Contract language | JavaScript | Rust / C | Solidity (EVM) | Solidity (EVM) |
| Throughput positioning | High TPS via sharding (claimed) | Very high TPS, single global state | High TPS, low fees | High TPS, very low fees |
| Ecosystem scale | Small / long-tail | Large (DeFi, NFTs, memecoins) | Large (retail DeFi) | Large (stablecoin rails, USDT) |
| Mkt-cap tier (2026-06-21) | ~$27M micro-cap | Top-10 | Top-5 | Top-10 |
| Key differentiator | Reputation-weighted validators; JS contracts | PoH ordering, raw speed | Binance distribution | Dominant USDT settlement |

Takeaway: IOST's technical ideas (reputation-weighted consensus, JS contracts) are credible, but it lost the adoption race to chains with stronger distribution (BNB via Binance, Tron via USDT) or raw performance plus a cultural moment (Solana). Its survival as a micro-cap reflects brand recognition from the 2018 cycle more than current on-chain demand.

---

## Narrative, Category & Catalysts

IOST sits in the **legacy high-throughput L1** bucket — a 2018-vintage smart-contract platform now far from the frontier of the L1/L2 debate. It carries secondary tags such as **BNB Chain ecosystem** (via its wrapped representation) and occasionally rides broad "alt-L1 rotation" flows when capital cycles down the market-cap curve in risk-on phases.

Potential catalysts (each speculative): a credible mainnet/protocol upgrade or rebrand that revives developer interest; a flagship consumer dApp that actually generates fee demand; renewed Korean retail interest (IOST has historically had strong Upbit/Korean volume); or a beta-driven rally if BTC reverses out of the current bear regime and capital rotates into dormant small-caps. Absent a fundamental usage catalyst, IOST trades primarily as a high-beta proxy on overall crypto risk appetite.

---

## History / Timeline

| Date | Event |
|---|---|
| 2018-01-11 | IOST genesis / token generation; ICO-era launch backed by investors including Sequoia China and Matrix Partners |
| 2018-01-24 | All-time high of $0.1298 reached during the peak of the 2017–2018 bull cycle |
| 2019-02 | IOST mainnet ("Olympus") goes live, transitioning IOST from an ERC-20 token to its native chain |
| 2020-03-13 | COVID-crash period drawdown across crypto (broad-market context) |
| 2026-03-29 | All-time low of $0.00100592 recorded |

> Dates above are drawn from market-data snapshots and widely reported project history. Undated narrative items are deliberately omitted to avoid fabricating a timeline.

---

## Trading Playbook (current regime)

- **Regime read (2026-06-22).** Market in **Extreme Fear** (Fear & Greed 21), long-horizon **Established Bear**, BTC ~16% below its 200-day MA. Micro-cap, low-liquidity L1s like IOST are among the highest-beta, lowest-conviction assets in this tape: thin order books mean both rallies and drawdowns are exaggerated.
- **What to watch.** BTC's reclaim of the 200-day MA (a precondition for broad alt rotation); IOST 24h volume relative to its ~$5M baseline (volume spikes precede the sharp moves); Korean/Upbit flow (KRW pairs historically drive IOST); any concrete protocol-upgrade or dApp announcement.
- **Risk posture.** In an Established Bear, the base case for a usage-light micro-cap is continued bleed punctuated by sharp, unsustainable bounces. Position sizing should reflect that a sub-$30M-cap token can lose most of its value with little warning and that exits can be slippage-heavy.
- **Bull-case trigger.** A durable BTC trend reversal plus a fundamental catalyst (new flagship app, exchange/derivatives expansion, or credible roadmap) would be required to turn IOST from a beta trade into a thesis.

---

## Platform & Chain Information

**Native Chain:** IOST [[layer-1|Layer-1]] mainnet; also a wrapped ERC-20/BEP-20 representation (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xaf48b7e315a52518cfbf7d96c455d9dfad94cb48` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | IOST/USDT | N/A |
| Upbit | IOST/KRW | N/A |
| Bitget | IOST/USDT | N/A |
| KuCoin | IOST/USDT | N/A |
| Crypto.com Exchange | IOST/USD | N/A |

**How & where it trades.** IOST's deepest spot liquidity historically sits on **Binance** (IOST/USDT) and the Korean exchange **Upbit** (IOST/KRW), which gives the token a notable Korean-retail flow component. Perpetual-futures markets on IOST have existed on major derivatives venues (Binance Futures, Bitget, KuCoin) but are thin relative to large-cap perps; funding and open interest are small, so derivatives are not the dominant price-discovery venue. With a sub-$30M cap and ~$5M daily volume, IOST is a low-liquidity asset: realized slippage on larger orders is material, and price can gap on modest flow.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://iost.io/](http://iost.io/) |
| **Reddit** | [https://www.reddit.com/r/IOStoken/](https://www.reddit.com/r/IOStoken/) |
| **GitHub** | [https://github.com/iost-official/go-iost](https://github.com/iost-official/go-iost) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 571 |
| **GitHub Forks** | 116 |
| **Pull Requests Merged** | 1,052 |
| **Contributors** | 24 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.75M |
| **Market Cap Rank** | #665 |
| **24h Range** | $0.00106515 — $0.00110741 |
| **Last Updated** | 2026-04-09 |

---

## Distinguishing Features

- **Proof-of-Believability consensus** — a [[proof-of-stake|stake]]-plus-reputation BFT design that weighs node behavior and contributions, not just stake.
- **Throughput emphasis** — sharding, microstate blocks, and fast BFT finality aimed at high TPS for consumer-scale dapps.
- **Resource model** — staking-for-resources (GAS/RAM-style) lets users transact without per-tx fees in some patterns.
- **Cross-ecosystem presence** — native L1 plus wrapped representation on BNB Chain.

## Risks

- **Throughput claims vs. real usage** — high theoretical TPS has not translated into a large, sticky dapp ecosystem; demand for blockspace remains modest.
- **Competitive landscape** — competes against far larger high-throughput L1s ([[solana|Solana]], BNB Chain, Sui, Aptos) for developers and users.
- **Future dilution** — circulating supply is below the 90B max supply.
- **Liquidity / small-cap risk** — ~$27M market cap (rank #693) implies thin liquidity and high volatility, amplified in the current Extreme-Fear regime.

> *This page is informational, not investment advice. Small-cap crypto assets are highly volatile and can lose most of their value rapidly.*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

IOST is tradable on **Binance** — both **spot** (IOST/USDT) and a **USD-margined perpetual**, which exposes funding rates, open interest, and liquidation data. It is **NOT** listed on Hyperliquid, so **Binance is the primary leveraged venue** for the token. Because leveraged price discovery is concentrated on a single major venue (with secondary perp/spot listings on Bitget, KuCoin, and Korean spot via Upbit), execution and sizing should treat Binance funding/OI as the reference signal. With a sub-$30M cap and roughly $5M daily volume, the perp is thin relative to large-cap contracts: available leverage tiers are lower and liquidation-driven wicks are exaggerated, so position sizing must assume material slippage on larger orders and gap risk on modest flow. The venue concentration also means a change in Binance derivatives status (leverage caps, delistings) would meaningfully alter tradability.

### Applicable strategies

- [[funding-rate-harvest]] — the small, single-venue IOST perp lets a spot-long/perp-short setup collect funding when the crowded-retail long bias pushes funding positive.
- [[crowded-long-funding-fade]] — high-beta micro-cap retail longs (notably Korean flow) periodically over-crowd the Binance perp; fading persistently positive funding is a repeatable edge.
- [[liquidation-cascade-fade]] — thin OI and low liquidity mean forced liquidations produce outsized wicks; fading exhaustion after a cascade targets the mean-reversion rebound.
- [[oi-confirmed-trend]] — pairing Binance open-interest expansion with price direction filters low-conviction chop from genuine leveraged trend legs in a usage-light token.
- [[rsi-mean-reversion]] — in the current range-bound Established Bear regime, oscillator extremes on IOST tend to snap back given the absence of fundamental trend drivers.
- [[breakout-and-retest]] — volume spikes (often Upbit/KRW-led) precede sharp moves, so trading confirmed breakouts with a retest entry captures the reflexive small-cap thrust.

### Volatility & regime character

IOST is a **micro-cap, legacy high-throughput L1** that trades as a **high-beta proxy on overall crypto risk appetite** rather than on its own fundamentals. It has strong positive correlation to [[btc-bitcoin|BTC]]/[[ethereum|ETH]] direction and amplifies broad-market moves in both directions because of thin order books. It carries a notable Korean-retail (Upbit/KRW) flow component that can decouple it briefly from global tape. Realized volatility is elevated relative to large caps, and rallies are typically sharp, liquidity-driven, and non-durable absent a fundamental catalyst.

### Risk flags

- **Liquidity / venue concentration** — sub-$30M cap, ~$5M daily volume, and leveraged discovery concentrated on Binance; exits can be slippage-heavy and price can gap on modest flow.
- **Emissions / dilution** — max supply (90B IOST) exceeds circulating supply, leaving residual future dilution.
- **Narrative dependence** — no large, sticky fee-generating dApp base; price rests on speculative/beta demand and periodic alt-L1 rotation rather than on-chain usage.
- **Beta / regime risk** — in an Established Bear with Extreme Fear, a usage-light micro-cap can lose most of its value with little warning; bounces are frequently unsustainable.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=IOSTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=IOSTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=IOST` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=IOST` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=IOSTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=IOSTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=IOST"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[proof-of-stake]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no additional specific wiki source ingested yet.
