---
title: "Rocket Pool"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, indicators, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["RPL", "Rocket Pool ETH", "rETH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.rocketpool.net"
related: ["[[crypto-markets]]", "[[defi]]", "[[depeg]]", "[[ethereum]]", "[[governance-token]]", "[[lido]]", "[[liquid-staking]]", "[[slashing]]", "[[smart-contract-risk]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[oi-confirmed-trend]]"]
---

# Rocket Pool

**Rocket Pool** (RPL) is Ethereum's leading decentralised [[liquid-staking]] protocol. Liquid stakers deposit as little as 0.01 ETH and receive **rETH**, a reward-bearing liquid staking token whose exchange rate appreciates against ETH as staking rewards accrue. Rocket Pool is fully non-custodial, and its permissionless node operators run validators ("minipools") that require only a fraction of the standard 32 ETH plus an RPL collateral bond — aligning operators economically with the stakers whose ETH they validate.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, RPL trades at **$1.35**, ranked **#639** by market capitalization with a market cap of **$30,456,495** (24h -1.20%, 7d -4.45%) — a recovery is not in evidence; the token sits roughly 98% below its 2023 all-time high, consistent with the broader bear regime (BTC ~$64,508; Fear & Greed Index 21, "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RPL |
| **Market Cap Rank** | #639 |
| **Market Cap** | $30,456,495 |
| **Current Price** | $1.35 |
| **24h / 7d Change** | -1.20% / -4.45% |
| **Categories** | Infrastructure, Smart Contract Platform, Decentralized Finance (DeFi), Polygon Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Liquid Staking Governance Tokens, Coinbase Ventures Portfolio, Proof of Stake (PoS), Index Coop Defi Index, Consensys Portfolio, Liquid Staking, Governance |
| **Website** | [https://www.rocketpool.net](https://www.rocketpool.net) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Rocket Pool is one of the most decentralised [[liquid-staking]] protocols on [[ethereum]], launched in 2021 after years of development dating back to 2016. It solves the core tension of Ethereum proof-of-stake: solo staking requires a full 32 ETH and the technical skill to run a validator 24/7, while centralized staking services concentrate trust. Rocket Pool splits the role into two participant types and bonds them together with the RPL token.

The Rocket Pool team has been in the staking space since its inception, giving it a long track record. Unlike its larger rival Lido, Rocket Pool emphasises a **permissionless** node-operator set — anyone can run a minipool — which is widely cited as a decentralization advantage for Ethereum's validator distribution. See also [[liquid-staking]] for the general mechanism and [[ethereum]] for the underlying proof-of-stake context.

---

## How Rocket Pool Works

**Two sides of the market:**

1. **Liquid stakers** deposit ETH (from 0.01 ETH upward) into the deposit pool and immediately receive **rETH**. rETH is a *reward-bearing* token: instead of rebasing the balance, its ETH-denominated exchange rate rises over time as validator rewards accumulate. Stakers can hold, trade, or use rETH across DeFi while their underlying stake keeps earning.
2. **Node operators** run validators called **minipools**. Rather than supplying the full 32 ETH, an operator bonds a reduced amount of ETH (8 or 16 ETH under current minipool designs) plus a minimum value of **RPL** as collateral; the remaining ETH is matched from staker deposits. Operators earn the base validator yield on their own ETH plus a commission on the staker-supplied ETH, plus RPL rewards.

**Role of the RPL token:**

- **Security collateral / insurance** — Node operators must bond RPL alongside their ETH. If a minipool is penalised or [[slashing|slashed]], the RPL bond can be liquidated to compensate affected stakers. This makes RPL the protocol's economic backstop, not merely a governance token.
- **Governance** — RPL holders (via the protocol DAO and the Oracle DAO / pDAO structure) vote on protocol parameters, commission rates, and treasury matters.
- **Incentive emissions** — RPL inflation is distributed to node operators (rewarding collateralization), the Oracle DAO, and the protocol DAO treasury.

**How yield is generated:** rETH yield comes entirely from real Ethereum [[liquid-staking]] rewards — consensus-layer issuance plus execution-layer priority fees and MEV — net of the node-operator commission. There is no Ponzi-style or emissions-funded "yield"; the appreciation of rETH reflects genuine validator income.

### Minipool designs (LEB8 / "Saturn")

Rocket Pool's capital-efficiency story is driven by progressively shrinking the node operator's ETH bond:

- **16-ETH minipool** (original) — operator supplies 16 ETH, stakers match 16 ETH. Operator earns base yield on its half plus a commission on the staker half.
- **8-ETH minipool (LEB8)** — introduced with the *Atlas* upgrade (2023). The operator bonds only 8 ETH (a "Lower-ETH-Bonded" minipool), and 24 ETH is matched from the deposit pool. This roughly triples the leverage on operator capital and lets the protocol absorb far more rETH demand per unit of operator ETH, at the cost of requiring a higher RPL collateral floor (because each minipool now carries more staker ETH per operator-ETH).
- **Saturn upgrade roadmap** — a multi-phase upgrade (Saturn 1/2) aimed at further reducing bond size (toward a future where operators may run validators with even smaller ETH bonds), introducing a "megapool" architecture that consolidates many validators under one contract, and reworking RPL utility/value accrual (including protocol-level revenue sharing and a forced-RPL-stake design). The direction is to make node operation cheaper and to give RPL a clearer cash-flow claim than pure inflation rewards.

### rETH exchange-rate mechanics (worked example)

rETH is a **reward-bearing** (non-rebasing) token. Suppose the rETH:ETH rate is 1.10 — i.e., 1 rETH redeems for 1.10 ETH. A user who deposits 10 ETH receives ~9.09 rETH (10 / 1.10). If Ethereum staking yields ~3.2% net over a year, the rate climbs to ~1.135, so the same 9.09 rETH is now worth ~10.32 ETH. The holder's *rETH balance never changes*; only the exchange rate rises. This non-rebasing design is gas-efficient and DeFi-friendly (it does not break LP accounting the way rebasing stETH can), and it is why rETH is widely used as collateral in lending markets (see [[lending]], [[defi]]).

---

## Competitive Position

Rocket Pool is the second- or third-largest Ethereum liquid-staking provider by staked ETH, behind the dominant [[lido|Lido]] (stETH) and competing with centralized-exchange staking (Coinbase's cbETH, Binance's wBETH) and with [[frax-share|Frax]]'s frxETH/sfrxETH. Its differentiation is **decentralization of the validator set**: anyone can become a node operator permissionlessly, whereas Lido's operator set is curated/whitelisted. This makes Rocket Pool a frequently cited mitigant to the systemic concern that a single provider controls too large a share of Ethereum's validators.

| Provider | LST | Operator set | Min stake to run a node | Non-rebasing token | Notable trait |
|---|---|---|---|---|---|
| **Rocket Pool** | rETH | **Permissionless** (anyone can run a minipool) | 8 ETH + RPL bond | Yes (rate-based) | Most decentralized operator set; RPL insurance bond |
| [[lido\|Lido]] | stETH (wstETH) | Curated/whitelisted | N/A (can't self-operate) | stETH rebases; wstETH is non-rebasing | Largest TVL/market share; DAO-governed |
| Coinbase | cbETH | Centralized (Coinbase) | N/A | Yes | Custodial, regulated US entity |
| Binance | wBETH | Centralized (Binance) | N/A | Yes | Custodial exchange product |
| [[frax-share\|Frax]] | sfrxETH | Frax-operated | N/A | Yes | Integrated into the Frax DeFi stack |

Rocket Pool's disadvantages are smaller scale (and thus less deep secondary liquidity for rETH than stETH) and a more demanding setup for node operators. Its advantage — credible decentralization plus a real economic-alignment mechanism (the RPL bond) — is what keeps it central to Ethereum's "neutrality" narrative.

---

## Governance

Rocket Pool governance is split across two bodies:

- **Protocol DAO (pDAO)** — RPL holders who vote on protocol-economic parameters (inflation split, minimum/maximum RPL collateral, commission rates, treasury spend). The pDAO uses on-chain, snapshot-anchored voting with a delegation system, and a **Security Council** can act on time-sensitive issues within bounded powers.
- **Oracle DAO (oDAO)** — a smaller permissioned set of trusted node operators responsible for reporting off-chain data on-chain: the rETH:ETH exchange rate, validator balances, network penalties, and reward Merkle trees. The oDAO is a trust-minimized oracle layer (it cannot steal funds) but it is a point of relative centralization that the protocol is working to reduce over time.

RPL inflation (historically ~5%/yr) is split among node operators (rewarding RPL collateralization), the oDAO, and the pDAO treasury. The *Saturn* roadmap proposes redirecting some protocol revenue to RPL and altering the inflation model, which is one of the most consequential live governance debates for token holders.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 22.28M RPL |
| **Total Supply** | 22.28M RPL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $38.21M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $61.90 (2023-04-16) |
| **Current vs ATH** | -97.23% |
| **All-Time Low** | $0.00884718 (2018-08-28) |
| **Current vs ATL** | +19285.00% |
| **24h Change** | -3.26% |
| **7d Change** | -2.95% |
| **30d Change** | -9.57% |
| **1y Change** | -49.69% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd33526068d116ce69f19a9ee46f0bd304f21a51f` |
| Polygon Pos | `0x7205705771547cf79201111b4bd8aaf29467b9ec` |
| Arbitrum One | `0xb766039cc6db368759c1e56b79affe831d0cc507` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RPL/USDT | N/A |
| Kraken | RPL/USD | N/A |
| Bitget | RPL/USDT | N/A |
| KuCoin | RPL/USDT | N/A |
| Crypto.com Exchange | RPL/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XD33526068D116CE69F19A9EE46F0BD304F21A51F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0XAE78736CD615F374D3085123A210448E74FC6393/0XD33526068D116CE69F19A9EE46F0BD304F21A51F | Spot |
| Uniswap V2 (Ethereum) | 0XB4EFD85C19999D84251304BDA99E90B92300BD93/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.rocketpool.net](https://www.rocketpool.net) |
| **Twitter** | [@Rocket_Pool](https://twitter.com/Rocket_Pool) |
| **Reddit** | [https://www.reddit.com/r/rocketpool](https://www.reddit.com/r/rocketpool) |
| **Discord** | [https://discordapp.com/invite/tCRG54c](https://discordapp.com/invite/tCRG54c) |
| **GitHub** | [https://github.com/rocket-pool/rocketpool](https://github.com/rocket-pool/rocketpool) |
| **Whitepaper** | [https://www.rocketpool.net/files/RocketPoolWhitePaper.pdf](https://www.rocketpool.net/files/RocketPoolWhitePaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 988 |
| **GitHub Forks** | 248 |
| **Pull Requests Merged** | 142 |
| **Contributors** | 15 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.45M |
| **Market Cap Rank** | #630 |
| **24h Range** | $1.71 — $1.79 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Risks

- **rETH [[depeg]] risk** — rETH should track its growing ETH redemption value, but in secondary markets it can trade at a discount during stress (forced selling, thin liquidity, or doubt about redeemability). A persistent discount can cascade for leveraged holders, even though protocol redemptions remain backed by real staked ETH.
- **[[slashing]] and validator penalties** — If node operators are slashed or go offline, penalties are absorbed first by the operator's ETH and RPL bond; the design is intended to insulate rETH holders, but a correlated slashing event (e.g., a client bug across many minipools) is a tail risk.
- **[[smart-contract-risk]]** — Rocket Pool's deposit pool, minipool, and reward contracts are complex and immutable in parts; a bug could put staked ETH at risk. The protocol is heavily audited but not risk-free.
- **RPL collateral volatility** — Because RPL is itself a volatile asset used as operator collateral, a sharp RPL drawdown (RPL is ~97% below its 2023 ATH) can push operators below minimum collateral thresholds, stressing the insurance model.
- **Centralization comparison** — While more decentralized than custodial stakers, Ethereum liquid staking as a whole concentrates validator power; Rocket Pool is a partial mitigant, not a complete one.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Notable Events

- **2016–2017** — Rocket Pool conceived by David Rugendyke; among the earliest projects to attempt decentralized, pooled Ethereum staking before the Beacon Chain even existed.
- **November 2021** — Rocket Pool **mainnet launch**, going live shortly after Ethereum's staking infrastructure matured, with rETH and the original 16-ETH minipool design.
- **2022** — Steady TVL growth through the bear market; rETH establishes itself as the primary *decentralized* alternative to Lido's stETH.
- **April 2023 — Atlas upgrade.** Introduced the **8-ETH (LEB8) minipool**, dramatically improving operator capital efficiency and unlocking far greater rETH issuance per unit of operator ETH. Coincided with RPL's all-time high near $61.90.
- **2023–2024** — RPL price declines sharply (~97–98% off ATH) as the broad governance-token drawdown and questions about RPL's value-accrual model weigh on the token, even while rETH (the product) continues functioning normally.
- **2024–2026 — Saturn roadmap.** Multi-phase upgrade work (megapools, smaller bonds, RPL value-accrual reform) becomes the central governance theme, aiming to revitalize both node-operator economics and the RPL token thesis.

> *Additional events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

RPL is tradable on [[binance]] — both **spot** (RPL/USDT) and a **USD-margined perpetual** with the full derivatives toolkit ([[funding-rate|funding]], [[open-interest]], [[liquidations]]). It is **not** listed on Hyperliquid, so Binance is the **primary leveraged venue** — there is no deep on-chain perp order book to diversify execution across. With RPL a small-cap (~#504–639 by market cap) and thin 24h spot volume, the perp is where most price discovery and leverage concentrate. Practical implications: leveraged flow, funding, and liquidation data all key off the single Binance perp, so slippage on larger clips is meaningful, order-book depth thins fast in stress, and position **sizing should assume shallow liquidity** and wide effective spreads. Cross-venue arbitrage is limited to routing spot fills across Binance/Kraken/Bitget/KuCoin against the one Binance perp, which shapes how basis and funding trades must be executed.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on the single Binance RPL-USDT contract when the funding sign is persistent; the sole-venue structure keeps the carry clean but caps size.
- [[cash-and-carry]] — pair long RPL spot against a short Binance perp to lock the basis, harvesting positive funding on a small-cap where perp demand periodically outruns spot.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when Binance funding spikes sharply positive after a rally in a thin, reflexive small-cap like RPL.
- [[liquidation-cascade-fade]] — RPL's shallow perp book makes cascade wicks violent; fade the overshoot after a forced-liquidation flush once [[open-interest]] resets.
- [[oi-confirmed-trend]] — use Binance open-interest confirmation to separate genuine trend legs from thin, low-conviction moves in a low-liquidity name.
- [[range-mean-reversion]] — RPL spends long stretches range-bound ~98% below its ATH; mean-revert the extremes when there is no active catalyst.

### Volatility & regime character

RPL is a **small-cap DeFi / liquid-staking infrastructure governance token** with high beta to ETH and BTC, amplified by thin liquidity — moves are reflexive and can overshoot in both directions. Because RPL is used as **operator collateral** in the Rocket Pool protocol, its price carries an extra reflexive loop (falling RPL stresses the insurance model, which can feed sentiment). It trades as a high-beta altcoin: it tends to underperform in risk-off ETH regimes and can spike on staking-narrative or Saturn-roadmap catalysts. Correlation to ETH is structurally elevated given the protocol's ETH-staking dependence.

### Risk flags

- **Venue concentration** — Binance is effectively the only meaningful leveraged venue (not on Hyperliquid); a single-exchange outage, delisting, or funding dislocation dominates risk with no on-chain perp fallback.
- **Liquidity** — thin spot and perp depth make slippage, gap risk, and liquidation-driven wicks severe relative to large-caps; size conservatively.
- **Emissions / tokenomics** — ongoing RPL inflation and the Saturn value-accrual reform are live governance debates that can re-rate the token; unlimited max supply and inflation split are structural overhangs.
- **Narrative dependence** — price is tied to the liquid-staking / decentralization narrative and Ethereum-staking economics; loss of narrative or shift toward rivals (Lido, exchange LSTs) weighs on RPL independently of protocol health.
- **Reflexive collateral loop** — sharp RPL drawdowns can push node operators below minimum collateral, a protocol-specific stress vector that can compound selling.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=RPLUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=RPLUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=RPL` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=RPL` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=RPLUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=RPLUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=RPL"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[liquid-staking]]
- [[lido]]
- [[frax-share]]
- [[slashing]]
- [[smart-contract-risk]]
- [[governance-token]]
- [[defi]]
- [[depeg]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical market-data snapshot
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko)
- General market knowledge (publicly documented Rocket Pool mechanism, Atlas/LEB8 and Saturn roadmap); no specific narrative wiki source ingested yet for protocol mechanism.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
