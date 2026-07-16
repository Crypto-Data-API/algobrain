---
title: "UMA"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, oracle, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins, derivatives]
aliases: ["UMA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://uma.xyz/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[oracle-disputes]]", "[[pyth-network]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[cash-and-carry]]"]
---

# UMA

**UMA** (ticker **UMA**) is the governance and dispute-resolution token of the UMA protocol, an [[ethereum|Ethereum]]-based oracle platform best known for its **Optimistic Oracle** — a mechanism that brings arbitrary off-chain data on-chain by assuming proposed values are correct unless economically challenged. UMA powers "priceless" financial contracts and is the data backbone of [[polymarket]] and other dispute-driven DeFi applications.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | UMA |
| **Current Price** | $0.417532 |
| **Market Cap** | $37.85M |
| **Market Cap Rank** | #549 |
| **24h Volume** | $5.06M |
| **24h Change** | +2.40% |
| **7d Change** | +3.41% |
| **Fully Diluted Valuation** | $53.82M |
| **All-Time High** | $41.56 (2021-02-04) |
| **All-Time Low** | $0.3036 (2020-04-29) |
| **Chain** | [[ethereum\|Ethereum]] (also Avalanche, Polygon, Optimism) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

UMA is trading modestly green on the day (+2.4%) and week (+3.4%), an outlier of relative strength against a backdrop where the broad **Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] sits at 23 (extreme fear)** and analysts describe an **established bear market**. At ~$0.42 the token remains roughly -99% below its February 2021 all-time high of $41.56, but well above its 2020 cycle low of $0.30. Daily turnover of ~$5M against a $37.85M cap is a velocity of ~13% — typical for a low-cap infra token but thin enough that fills of size move the tape.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~90.67M UMA |
| **Total Supply** | ~128.93M UMA |
| **Max Supply** | Uncapped (governance-mintable) |
| **Fully Diluted Valuation** | $53.82M |
| **Market Cap / FDV** | ~0.70 |
| **All-Time High** | $41.56 (2021-02-04) |
| **All-Time Low** | $0.3036 (2020-04-29) |

UMA's supply is uncapped: the [[oracle-disputes|Data Verification Mechanism]] (DVM) can mint new tokens to fund the "51% attack is always more expensive than the corruptible value" security guarantee. In practice issuance is slow and governed by token-holder vote. The MC/FDV ratio near 0.70 reflects modest locked or treasury-held supply rather than aggressive future emissions.

The UMA token does two jobs:

- **Governance** — holders vote on supported contract types, asset whitelists, system parameters, and upgrades.
- **Dispute resolution** — when an Optimistic Oracle assertion is challenged, token holders are the final arbiters via the DVM, staking and voting on the correct value and earning rewards for honest participation.

---

## Technology — the Optimistic Oracle

UMA is not a price-feed oracle in the [[chainlink|Chainlink]] push model. Its core primitive is the **Optimistic Oracle (OO)**, which answers arbitrary questions — "did event X happen?", "what was the TWAP of asset Y?" — under an optimistic, game-theoretic assumption:

1. **Assertion** — a proposer posts an answer on-chain together with a **bond**.
2. **Challenge window** — a liveness period (often 2 hours to several days) during which anyone can dispute by posting a matching bond.
3. **Happy path** — if no dispute arrives, the assertion finalizes cheaply and the proposer recovers the bond. No on-chain computation of the "true" value is needed.
4. **Escalation** — a dispute escalates to the **Data Verification Mechanism (DVM)**, where UMA token holders stake and vote on the correct value over ~48-96 hours. The losing side forfeits its bond; honest voters earn rewards.

The economic security claim is that **the cost to corrupt always exceeds the value at stake**: the DVM can mint new UMA to keep the corruption cost above any single dispute's profit (see [[oracle-disputes]]). The trade-off versus push oracles is latency — the OO is built for **truth-on-demand**, not millisecond price streaming. This makes UMA ideal for subjective or hard-to-feed data: prediction-market resolution (it secures [[polymarket]]), insurance payouts, [[cross-chain]] [[bridge|bridges]], KPI options, and "priceless" synthetic tokens that track a reference index without a continuous on-chain feed.

Adjacent products built on the OO include **oSnap** (an optimistic governance executor that lets DAOs execute Snapshot votes on-chain without a multisig), **KPI options**, and **success tokens**.

---

## Market Structure & Derivatives

**Spot venues.** UMA lists on major centralized exchanges including Binance (UMA/USDT), Kraken (UMA/USD), Bitget, KuCoin, and Crypto.com. On-chain liquidity sits on [[uniswap]] V2/V3 and SushiSwap against WETH across Ethereum, Polygon, and Optimism.

**Derivatives.** A **UMA-PERP** perpetual trades on [[hyperliquid]], giving leveraged/short access to a token with a relatively thin ~$5.1M daily spot tape. Open interest and funding on a name this size are small and can swing sharply, so perp pricing can dislocate from spot during volatility. Treat UMA as a primarily spot-driven instrument; verify perp depth and funding live before sizing.

**Liquidity profile.** With ~$5M daily volume on a $37.85M cap, UMA is a low-cap, moderate-velocity infra token. Bid/ask depth thins quickly beyond a few tens of thousands of dollars on most venues.

---

## Use Case, Narrative & Category

UMA sits in the **oracle / DeFi-infrastructure** category alongside [[chainlink]], [[pyth-network]], [[api3]], [[redstone-oracles]], and [[tellor]]. Its differentiator is the optimistic, dispute-based design: instead of streaming prices, it provides truth-on-demand for arbitrary assertions at very low gas when unconfirmed. The dominant current narrative is its role as the **canonical resolution layer for prediction markets** — most visibly Polymarket — which ties UMA's relevance to the growth of event-driven and political/sports betting markets on-chain. Related products include KPI options, success tokens, and the oSnap optimistic governance executor used by DAOs.

### Peer comparison — oracle protocols

| Protocol | Token | Model | Specialism | Mkt cap rank |
|---|---|---|---|---|
| [[chainlink]] | LINK | Decentralized push feeds + CCIP | General-purpose, blue-chip standard | Top-20 |
| [[pyth-network]] | PYTH | Low-latency pull (first-party publishers) | High-frequency price feeds | Top-100 |
| **UMA** | **UMA** | **Optimistic, dispute-based** | **Arbitrary assertions / prediction-market resolution** | **#549** |
| [[tellor]] | TRB | Staking + dispute (ex-PoW) | Censorship-resistant fallback feeds | #543 |
| [[redstone-oracles]] | RED | Modular pull (signed off-chain data) | Yield-bearing / LST-LRT collateral | #476 |
| [[api3]] | API3 | First-party (dAPIs), OEV capture | First-party data + OEV | — |

UMA is the outlier: it is the only major oracle whose flagship product resolves **subjective, non-price assertions** rather than streaming numerical feeds — a different market than the price-feed competition.

### Valuation framing (qualitative)

UMA trades at a ~$38M market cap and a low MC/FDV (~0.70) with no aggressive emission schedule, so dilution is not the headline risk. The bull case is optionality on **prediction-market growth**: UMA is the de-facto resolution layer for [[polymarket]], and event-driven on-chain betting has structural tailwinds around elections and sports. The bear case is that the OO's relevance is **concentrated** in a single vertical, value accrual to the token is indirect (security/governance rather than fee capture), and the broad oracle market is dominated by [[chainlink]]. At -99% from ATH the token reflects deep skepticism; a re-rating likely requires demonstrable fee/usage growth or a major new OO integration, not just market beta.

---

## Notable History

- **2018-2020** — Founded by Hart Lambur and Allison Lu; backed by Blockchain Capital, Bain Capital Ventures, Placeholder, and others. Mainnet and the DVM launched in 2020.
- **2021** — UMA hit its ATH of $41.56 amid the DeFi "summer" expansion of synthetic-asset interest.
- **2021 onward** — Pivot from priceless synthetics toward the **Optimistic Oracle** as the flagship product, broadening UMA into a general-purpose data layer.
- **2022-2024** — UMA became the standard dispute-resolution oracle for [[polymarket]]; OO usage grew with the prediction-market boom around major elections.
- **Dispute incidents** — High-profile Polymarket resolution disputes (e.g., ambiguously worded markets) have periodically stress-tested the DVM and drawn debate over whether token-holder voting can be subverted on contentious questions.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — The optimistic model is only as safe as its economic bonds and the honesty of the DVM voter majority. A sufficiently large, motivated coalition could in theory vote a false outcome on a high-value market; ambiguous market wording amplifies this. See [[oracle-manipulation]] and [[oracle-disputes]].
- **Governance-capture risk** — Because resolution is token-vote-based, concentrated UMA holdings could sway outcomes; the security model assumes the cost to corrupt always exceeds the value at stake, which can fail for very large single disputes.
- **Concentration / dependency risk** — A large share of UMA's relevance is tied to [[polymarket]] and prediction-market volume; a downturn in that vertical would weigh on demand.
- **Liquidity risk** — ~$5.6M daily volume is thin; the [[hyperliquid]] perp can see outsized funding/price swings.
- **Macro / regime risk** — In an extreme-fear, established-bear backdrop ([[crypto-fear-and-greed-index|Fear & Greed]] 23), low-cap infrastructure tokens tend to underperform and suffer liquidity drought.

---

## Trading Profile

**Venues & liquidity.** UMA is tradable on **both** [[binance]] and [[hyperliquid]], a comparatively rare two-venue setup for a ~#584-rank token. Binance offers **spot** (UMA/USDT) and a **USD-margined perpetual**, while Hyperliquid lists **UMA-PERP** with leverage up to ~40-50x. This gives genuine cross-venue price discovery and a deeper, more contestable book than a single-venue microcap — but the underlying spot tape is still thin (~$2.5-5M/day on a ~$34-38M cap). The practical upshot: two liquid perp venues make funding/basis and cross-exchange plays feasible, yet absolute depth remains shallow, so size fills in slices, expect slippage beyond a few tens of thousands of dollars, and use limit orders rather than market sweeps.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — UMA-PERP on Hyperliquid vs the Binance USD-margined perp routinely price funding differently on a low-cap this size; harvest the spread between the two venues.
- [[funding-rate-harvest]] — thin OI makes UMA funding swing to persistent extremes, letting a delta-hedged position collect carry when the perp trades rich or cheap to spot.
- [[cash-and-carry]] — with Binance spot plus a Binance/Hyperliquid perp, long spot against short perp captures basis when the perp runs at a premium.
- [[cross-exchange-arbitrage]] — dual perp venues plus multiple spot listings (Binance, Kraken, KuCoin) create exploitable price gaps during the illiquid, fast-moving hours typical of a microcap.
- [[liquidation-cascade-fade]] — shallow depth means clustered stops and leverage flushes overshoot hard; fading the wick after a forced-liquidation spike is a recurring setup here.
- [[range-mean-reversion]] — outside of narrative catalysts UMA chops in wide, low-volume ranges, favoring reversion to a mean over directional trend-holding.

**Volatility & regime character.** UMA is a **low-cap DeFi / oracle-infrastructure token** (~#584) with high-beta-alt behavior: it is thin, reflexive, and prone to sharp squeezes on light volume, yet it is not a memecoin — moves are increasingly tied to a specific fundamental narrative (prediction-market resolution / [[polymarket]]). Broadly it carries positive [[bitcoin|BTC]]/[[ethereum|ETH]] beta and tends to underperform in risk-off regimes ([[crypto-fear-and-greed-index|Fear & Greed]] extremes), but idiosyncratic catalysts (a major OO integration, a high-profile Polymarket dispute) can fully decouple it from broad-market beta for days.

**Risk flags.**
- **Liquidity / depth concentration** — despite two perp venues, the real spot float is small; OI and funding are tiny and can swing violently, and perp price can dislocate from spot in volatility.
- **Narrative dependence** — a large share of UMA's demand thesis is tied to [[polymarket]] and prediction-market volume; a downturn in that vertical, or a contentious dispute outcome, moves the token sharply.
- **Perp funding dislocations** — low OI on both venues means funding can spike and stay pinned, and the Hyperliquid-vs-Binance funding gap can invert quickly; verify live before carrying.
- **Uncapped/governance-mintable supply** — the DVM can mint UMA; issuance is slow and governed, but it is a structural overhang rather than a fixed-cap token.
- **Microcap tail risk** — venue delisting, thin-book gap moves, and stop-cascade wicks are outsized relative to a large-cap; size accordingly.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=UMA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=UMA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=UMA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=UMA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=UMA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[chainlink]]
- [[pyth-network]]
- [[api3]]
- [[tellor]]
- [[oracle-disputes]]
- [[oracle-manipulation]]
- [[polymarket]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | UMA |
| **Market Cap Rank** | #584 |
| **Market Cap** | $33.83M |
| **Current Price** | $0.3689 |
| **Categories** | Decentralized Finance (DeFi), Oracle, Derivatives, Synthetic Issuer, Synthetic, Made in USA, Governance |
| **Website** | [https://uma.xyz/](https://uma.xyz/) |

---

## Overview

UMA is a decentralized financial contracts platform built to enable Universal Market Access.

UMA builds infrastructure for “priceless” financial contracts: DeFi contracts that minimize oracle usage, avoiding many of the security and scalability issues that have plagued decentralized finance. The first contracts built with UMA are priceless synthetic tokens: ERC20 tokens that can track anything while minimizing the need for on-chain price data.

The UMA project token powers the system in two ways:

Governance: UMA token holders govern what types of contracts can access the system, which asset types are supported, and key system parameters and upgrades.

Price requests: the priceless methodology minimizes on-chain price requests but doesn’t eliminate them — when contract interactions are disputed, UMA token holders fulfill price requests via the Data Verification Mechanism, or DVM.

UMA tokens enable the holder to participate in community governance and resolve contract disputes through the DVM. The tokens are not an investment opportunity.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 91.70M UMA |
| **Total Supply** | 129.14M UMA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $47.64M |
| **Market Cap / FDV Ratio** | 0.71 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $41.56 (2021-02-04) |
| **Current vs ATH** | -99.11% |
| **All-Time Low** | $0.3036 (2020-04-29) |
| **Current vs ATL** | +21.45% |
| **24h Change** | +0.07% |
| **7d Change** | -0.82% |
| **30d Change** | -14.96% |
| **1y Change** | -69.76% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x04fa0d235c4abf4bcf4787af4cf447de572ef828` |
| Avalanche | `0x3bd2b1c7ed8d396dbb98ded3aebb41350a5b2339` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | UMA/USDT | N/A |
| Kraken | UMA/USD | N/A |
| KuCoin | UMA/USDT | N/A |
| Crypto.com Exchange | UMA/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X04FA0D235C4ABF4BCF4787AF4CF447DE572EF828/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X04FA0D235C4ABF4BCF4787AF4CF447DE572EF828/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://uma.xyz/](https://uma.xyz/) |
| **Twitter** | [@UMAprotocol](https://twitter.com/UMAprotocol) |
| **Discord** | [https://discord.com/invite/jsb9XQJ](https://discord.com/invite/jsb9XQJ) |
| **GitHub** | [https://github.com/UMAprotocol/protocol](https://github.com/UMAprotocol/protocol) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 478 |
| **GitHub Forks** | 213 |
| **Pull Requests Merged** | 3,649 |
| **Contributors** | 53 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.49M |
| **Market Cap Rank** | #584 |
| **24h Range** | $0.3666 — $0.3734 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
