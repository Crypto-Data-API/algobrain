---
title: "Tellor Tributes"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, oracle, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["TRB", "Tellor"]
entity_type: protocol
headquarters: "Decentralized"
website: "http://www.tellor.io/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[oracle-manipulation]]", "[[pyth-network]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[short-liquidation-squeeze]]"]
---

# Tellor Tributes

**Tellor Tributes** (ticker **TRB**) is the staking and dispute token of Tellor, an [[ethereum|Ethereum]]-based decentralized oracle that brings off-chain data on-chain through a **crypto-economic, dispute-driven mechanism**. Originally a proof-of-work-style oracle where miners competed to submit data, Tellor now runs a **staking-based** model: reporters stake TRB to submit values, and any incorrect data can be challenged and slashed via on-chain disputes. Tellor's design prioritizes censorship resistance and permissionless reporting over update speed.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | TRB |
| **Current Price** | $13.78 |
| **Market Cap** | $38.52M |
| **Market Cap Rank** | #543 |
| **24h Volume** | $9.00M |
| **24h Change** | -1.25% |
| **7d Change** | +2.44% |
| **Fully Diluted Valuation** | $39.54M |
| **All-Time High** | $593.09 (2023-12-31) |
| **All-Time Low** | $0.0100 (2019-11-01) |
| **Chain** | [[ethereum\|Ethereum]] (+ Polygon, Arbitrum, Optimism, Gnosis, others) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

TRB is down ~1.3% on the day and up ~+2.4% over the week, holding up while the **Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] reads 23 (extreme fear)** in an **established bear market**. At ~$13.78 the token trades roughly -98% below its late-2023 ATH of $593.09, but is up enormously (>137,000%) from its 2019 all-time low of $0.0100. Notably, daily volume (~$9.0M) is **~23% of the entire market cap** ($38.52M) — an unusually high turnover ratio that reflects TRB's reputation as a speculative, low-float trading vehicle rather than a buy-and-hold.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.79M TRB |
| **Total Supply** | ~2.87M TRB |
| **Max Supply** | Uncapped (inflationary reporting rewards) |
| **Fully Diluted Valuation** | $39.54M |
| **Market Cap / FDV** | ~0.97 |
| **All-Time High** | $593.09 (2023-12-31) |
| **All-Time Low** | $0.0100 (2019-11-01) |

TRB has a **small, low-float supply** (~2.8M tokens) and is **inflationary**: new TRB is minted as rewards for reporters who submit data and for tipping data requests. The low absolute supply makes TRB notoriously volatile and historically a target of squeeze/manipulation episodes. The MC/FDV near 0.97 reflects that nearly all supply is circulating. TRB is staked by **reporters** (collateral that can be slashed for bad data) and by **disputers** who challenge incorrect submissions.

---

## Technology — dispute-based oracle

Tellor is a **dispute-based oracle**, conceptually closer to [[uma|UMA's]] optimistic model than to the always-on push feeds of [[chainlink|Chainlink]]. The lifecycle of a data point:

- **Data request & report** — A dApp tips (in TRB) for a data point (e.g., ETH/USD); **staked reporters** submit values on-chain. Each reporter must lock TRB collateral to participate.
- **Dispute window** — Any party can stake TRB to dispute a value they believe is wrong; disputes are resolved by TRB-holder vote, with the loser's stake slashed.
- **Security via cost-to-corrupt** — Manipulating Tellor requires acquiring and risking TRB stake, and bad actors can be slashed. The model trades latency for **censorship resistance and permissionlessness** — there is no privileged node-operator set.

**Evolution from PoW.** Tellor originally ran a **proof-of-work-style** competition where miners raced to submit data (the source of the "Tributes" name). The **Tellor X / Tellor 360** upgrades (2022) replaced mining with the current **stake-and-dispute** model, removing energy-intensive mining and tightening the crypto-economic design. Tellor is deployed across [[ethereum|Ethereum]], Polygon, Arbitrum, Optimism, Gnosis and other EVM chains, and is frequently used as a **fallback / backup feed** for protocols that want redundancy against a single oracle's failure.

This positions Tellor as a more decentralized, slower oracle option versus the higher-frequency [[chainlink]], [[pyth-network]], and [[redstone-oracles]].

---

## Market Structure & Derivatives

**Spot venues.** TRB lists on Binance (TRB/USDT), Bitget, KuCoin, and Crypto.com. On-chain liquidity sits on [[uniswap]] V3 against WETH.

**Derivatives.** A **TRB-PERP** perpetual trades on [[hyperliquid]] and several CEX futures venues. Given TRB's tiny ~2.8M float and history of violent squeezes, the perp can see extreme funding swings and rapid liquidations; open interest and funding should be checked live before trading, as the low float makes the contract prone to dislocation from spot.

**Liquidity / float dynamics.** TRB's defining market feature is its **~2.8M-token float** combined with high relative turnover (~$9M/day, ~23% of cap). This makes the token exceptionally squeeze-prone: a relatively small amount of buying pressure against thin order books and crowded shorts can drive outsized moves, as in the December 2023 spike to $593. Traders should treat TRB as a high-beta, manipulation-prone instrument where price action often decouples from oracle-protocol fundamentals.

---

## Use Case, Narrative & Category

Tellor sits in the **oracle / DeFi-infrastructure** category. Its narrative emphasizes **maximal decentralization and censorship resistance**: anyone can report or dispute data without permission, and there is no privileged node operator set. This makes it attractive as a fallback or backup oracle and for protocols that prioritize trust-minimization over speed. The TRB token itself is also widely known among traders as a **high-volatility, low-float instrument** that has repeatedly seen dramatic price spikes and squeezes, somewhat independent of protocol fundamentals.

### Peer comparison — oracle protocols

| Protocol | Token | Model | Update latency | Specialism | Mkt cap rank |
|---|---|---|---|---|---|
| [[chainlink]] | LINK | Decentralized push feeds + CCIP | Fast (heartbeat) | Blue-chip standard | Top-20 |
| [[pyth-network]] | PYTH | Pull (first-party publishers) | Sub-second | High-frequency price feeds | Top-100 |
| [[redstone-oracles]] | RED | Modular pull (signed data) | On-demand | LST/LRT collateral | #476 |
| **Tellor** | **TRB** | **Stake + dispute (ex-PoW)** | **Slow (dispute window)** | **Censorship-resistant fallback** | **#543** |
| [[uma]] | UMA | Optimistic, dispute-based | Slow (challenge window) | Arbitrary assertions | #549 |

Tellor and UMA occupy the **slow, dispute-based, trust-minimized** corner of the oracle landscape, contrasting with the fast push/pull feeds of Chainlink, Pyth, and RedStone. Tellor's edge is being a credibly neutral, permissionless **backup**, not a primary high-frequency feed.

### Valuation framing (qualitative)

TRB trades at ~$38.5M with MC/FDV near 0.97 (almost fully circulating), so dilution is minimal — unlike high-FDV peers such as [[redstone-oracles|RED]]. The challenge is **value accrual**: Tellor's actual protocol revenue (tips for data requests) is small relative to the token's trading float, and much of TRB's price is driven by its low-float squeeze dynamics rather than fundamental oracle demand. A sober frame treats TRB as a **niche decentralization premium plus a high-volatility trading instrument**, where the protocol's "backup oracle" positioning is real but monetarily thin, and the token's price is unusually disconnected from usage.

---

## Notable History

- **2019** — Tellor launches as a proof-of-work-style oracle; TRB sets its all-time low of $0.0100 (2019-11-01). Backed by YZi Labs (formerly Binance Labs) among others.
- **2020-2021** — Adoption as a decentralized oracle and backup feed across DeFi; deployment to multiple chains (Polygon, Arbitrum, Optimism, Gnosis, etc.).
- **2022 ("Tellor X" / "Tellor 360")** — Migration from PoW mining to a **staking-and-dispute** model, removing energy-intensive mining and tightening the crypto-economic security design.
- **2023-12-31** — TRB spiked to its all-time high of **$593.09**, a move widely attributed to a low-float squeeze rather than fundamentals; the price subsequently collapsed.
- **2026** — Trades around $13.78 in the broad bear market, far below its ATH but resilient on the week.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — Tellor's security rests on the cost to acquire TRB stake and on disputers catching bad data within the window. A motivated actor could submit false values and try to ride out the dispute window, or accumulate stake to influence dispute votes. See [[oracle-manipulation]].
- **Latency risk** — The dispute-based model is slower than push feeds; protocols using Tellor for fast-moving prices (e.g., liquidations) must account for the delay and dispute period.
- **Low-float volatility / squeeze risk** — With only ~2.8M tokens, TRB is extremely volatile and has a documented history of squeezes (notably the 2023 spike to $593); the [[hyperliquid]] perp amplifies this with leverage.
- **Reporter-set concentration risk** — If too few reporters stake, data availability and decentralization suffer.
- **Macro risk** — In an extreme-fear, established-bear regime ([[crypto-fear-and-greed-index|Fear & Greed]] 23), thin low-cap oracle tokens are prone to liquidity drought despite Tellor's recent weekly strength.

---

## Trading Profile

**Venues & liquidity.** TRB is tradable on **both Binance and [[hyperliquid]]**. Binance offers a **TRB/USDT spot** market plus a **USD-margined TRB perpetual**, while Hyperliquid runs the on-chain **TRB-PERP** at up to **~40-50x** leverage. This is a genuinely **two-venue derivatives market**, which is unusual for a sub-$50M-cap token and gives it deeper aggregate perp liquidity than most rank-~500 alts. In practice the dual-venue structure means orders can be split across books, but TRB's **~2.8M-token float** keeps spot depth thin — so large size still moves price, and the perps (not the shallow spot) carry most of the executable liquidity. Traders should size to the thinner of the two books at any given moment and expect wider effective spreads during volatility.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — TRB trades as a perp on both Hyperliquid and Binance, so funding can diverge sharply between the two venues, creating a market-neutral capture opportunity.
- [[cash-and-carry]] — Binance spot plus a USD-margined perp lets a long-spot / short-perp carry harvest positive funding when the low-float perp trades rich to spot.
- [[crowded-short-funding-fade]] — TRB is a chronic short target given its "overvalued oracle" reputation; deeply negative funding flags crowded shorts vulnerable to a squeeze, the setup behind its historic spikes.
- [[short-liquidation-squeeze]] — With a tiny float and history of violent squeezes (the 2023 run to $593), stacked short liquidations can cascade upward fast on either venue.
- [[volatility-breakout]] — TRB's low float produces frequent explosive range expansions, favouring breakout entries over passive mean-reversion in trending phases.
- [[liquidation-cascade-fade]] — Leveraged perp positioning on a thin token makes forced-liquidation flushes overshoot, offering fade entries once the cascade exhausts.

**Volatility & regime character.** TRB is a **high-beta, low-float DeFi-infrastructure (oracle) token** whose price is driven far more by reflexive squeeze/liquidation dynamics than by protocol fundamentals — behaviour closer to a reflexive small-cap than a typical infra token. It broadly tracks **BTC/ETH risk-on/risk-off beta** at the regime level, but its idiosyncratic low-float mechanics regularly decouple it from the majors during squeeze episodes, producing amplitude well beyond large-cap alts.

**Risk flags.**
- **Low-float squeeze/manipulation risk** — ~2.8M-token float makes TRB exceptionally prone to engineered squeezes and sharp reversals; position sizing must assume gap risk.
- **Venue-concentration & liquidity risk** — Despite two venues, real spot depth is thin; a liquidity drought (extreme-fear regimes) can widen spreads and amplify slippage.
- **Perp funding dislocations** — The low float lets the perp decouple from spot, driving extreme funding swings and rapid liquidations; check live funding/OI before entry.
- **Narrative/fundamental disconnect** — Value accrual is thin relative to trading float, so price is largely narrative- and flow-driven rather than usage-driven.
- **Inflationary emissions** — TRB has uncapped reporter-reward inflation, a slow structural supply headwind independent of trading dynamics.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=TRB` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=TRB` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=TRB&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=TRB&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=TRB"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[chainlink]]
- [[pyth-network]]
- [[redstone-oracles]]
- [[api3]]
- [[uma]]
- [[oracle-manipulation]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

