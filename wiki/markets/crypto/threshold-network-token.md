---
title: "Threshold Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["T", "Threshold"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://threshold.network/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[wrapped-bitcoin]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Threshold Network

**Threshold Network** (ticker **T**) is the [[ethereum|Ethereum]]-based token of the Threshold protocol, formed by the on-chain merger of the **NuCypher** and **Keep** networks. Threshold provides **threshold cryptography** services — distributing sensitive operations (like signing or decryption) across many independent nodes so that a minimum threshold must cooperate, with no single trusted party. Its flagship product is **tBTC**, a decentralized, redeemable bridge that mints [[bitcoin|Bitcoin]] onto Ethereum and other chains as an ERC-20.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | T |
| **Chain** | [[ethereum\|Ethereum]] (also [[base\|Base]], Optimism, Solana) |
| **Current Price** | $0.00359736 |
| **Market Cap** | $40.16M |
| **Market Cap Rank** | #522 |
| **24h Volume** | $4.64M |
| **24h Change** | +1.86% |
| **7d Change** | -6.44% |
| **Circulating Supply** | ~11.16B T |
| **Total Supply** | ~11.16B T |
| **Max Supply** | Uncapped (governance-controlled) |
| **All-Time High** | $0.2269 (2022-03-02) |
| **All-Time Low** | $0.003499 (2026-06-19) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

T is up ~+1.9% on the day but down ~-6.4% over the week, underperforming as the **Crypto [[fear-and-greed-index|Fear & Greed Index]] sits at 23 (extreme fear)** in an **Established Bear Market**. The token printed a fresh all-time low of **$0.003499 on 2026-06-19** — essentially where it trades now — about **-98% below its 2022 ATH** of $0.2269. The very low unit price is a function of the ~11.16B token supply, not a valuation signal in itself.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~11.16B T |
| **Total Supply** | ~11.16B T |
| **Max Supply** | Uncapped (governance-controlled) |
| **Fully Diluted Valuation** | $39.41M |
| **Market Cap / FDV** | 1.00 |
| **All-Time High** | $0.2269 (2022-03-02) |
| **All-Time Low** | $0.003499 (2026-06-19) |

T's supply is effectively **fully circulating (MC/FDV = 1.00)** — there is no large unlock overhang, since the entire ~11.16B supply was distributed at the NuCypher/Keep merger and via the DAO. The token is used for **governance** of the Threshold DAO and for **staking**: node operators stake T to run the [[threshold-cryptography|threshold-cryptography]] "stake-and-go" infrastructure that backs tBTC and other services, earning rewards and bearing slashing exposure for misbehavior. Because supply is **governance-mintable in principle** (no hard cap), future emissions depend on DAO decisions — the main forward dilution risk.

---

## Technology & Protocol

Threshold's core mechanic is the **tBTC** decentralized [[bitcoin|BTC]] bridge, built on [[threshold-cryptography|threshold cryptography]]:

- A user sends [[bitcoin|BTC]] to a wallet controlled by a randomly selected group of staked Threshold node operators.
- Custody of that BTC is split via **threshold signatures (ECDSA)** across the group — no single operator holds the keys, and a threshold (e.g., 51-of-100) must cooperate to move funds.
- Once the BTC deposit is confirmed, an equivalent amount of **tBTC** (ERC-20) is minted on Ethereum/L2s, usable across [[defi|DeFi]].
- Redemption reverses the process: burn tBTC, and the operator group releases the native BTC.

This makes **tBTC a trust-minimized alternative to custodial [[wrapped-bitcoin|wrapped Bitcoin]]** like WBTC, where a single custodian holds the BTC. T staking secures the operator set; misbehaving operators can be slashed. Threshold also inherits NuCypher's **proxy re-encryption / threshold access control** for managing data and digital-asset permissions without a trusted intermediary.

## Market Structure & Derivatives

**Spot venues.** T lists on Binance (T/USDT), Kraken (T/USD), Upbit (T/KRW), Bitget, KuCoin, and Crypto.com. The token is deployed across [[ethereum|Ethereum]], [[base|Base]], Optimism, and Solana.

**Liquidity & depth.** ~$4.6M daily volume on a ~$40M cap (~12% turnover) is thin; the very large supply means tight unit-price granularity but shallow book depth, so sizable orders face slippage.

**Derivatives.** T does not have a prominent perp listing on [[hyperliquid|Hyperliquid]]; spot is the primary venue. (Verify current perp availability before assuming derivatives access.) Trading is therefore spot-driven, with limited leverage-fueled volatility.

---

## Peer Comparison (BTC-on-chain / BTCfi)

| Asset | Custody model | Mcap Rank (T) | Decentralization | Note |
|---|---|---|---|---|
| **tBTC / Threshold (T)** | Threshold-signature operator set | #522 (T) | High (permissionless operators) | Trust-minimized, slashing-secured |
| [[wrapped-bitcoin\|WBTC]] | Single/federated custodian (BitGo) | — | Low | Deepest liquidity, custodial trust |
| cbBTC (Coinbase) | Single custodian (Coinbase) | — | Low | Exchange-backed, fast adoption |
| LBTC (Lombard) | Consortium / staking | — | Medium | BTC-staking yield angle |

T's differentiator is **decentralized custody** versus the convenience and depth of custodial wrappers. The trade-off: deeper liquidity sits with WBTC/cbBTC, so tBTC must win on trust-minimization to grow share.

---

## Valuation Framing

T value tracks **tBTC supply/TVL** (which drives staking demand) and broader **BTCfi adoption**. With supply fully circulating, there is no unlock overhang, but the open-ended governance mint and a token that just printed a new all-time low make this a deep-value, high-risk infrastructure bet contingent on non-custodial BTC demand. Qualitative only — not a price target.

---

## Use Case, Narrative & Category

Threshold sits in two overlapping categories: **threshold cryptography / DeFi infrastructure** and **BTCfi** (Bitcoin-in-DeFi). Its central narrative is **tBTC as the decentralized way to bring Bitcoin liquidity into DeFi**, contrasting with custodial WBTC and competing with newer BTC bridges (e.g., Lombard's LBTC, Coinbase's cbBTC). Beyond tBTC, Threshold offers threshold-based access control and proxy re-encryption (inherited from NuCypher) for managing data and digital-asset permissions without a trusted intermediary. The thesis rises and falls with demand for non-custodial Bitcoin on Ethereum and L2s.

---

## Notable History

- **2017-2020** — **NuCypher** (proxy re-encryption / key management) and **Keep Network** (private data containers, original tBTC v1) launch independently.
- **2021-2022** — The two networks vote to merge into **Threshold Network**; KEEP and NU holders convert to the new **T** token. tBTC v2 launches with an open, permissionless operator set (vs. the bonded v1 model). T reached its ATH of $0.2269 in March 2022.
- **2022-2024** — Expansion of tBTC across L2s (Base, Optimism, Arbitrum) and to Solana via cross-chain deployments; growth of the BTCfi narrative.
- **2026** — T set a new all-time low ($0.003499, 2026-06-19) during the broad crypto bear market.

---

## Risks

- **Custody / bridge risk (tBTC)** — The single largest risk: tBTC's value depends on the staked operator set faithfully custodying native BTC via threshold signatures. A collusion of operators above the signing threshold, a key-generation flaw, or a smart-contract exploit could lead to loss of the backing BTC and de-pegging of tBTC. Cross-chain bridges have historically been among the most-exploited DeFi components.
- **Slashing / operator-set risk** — Node operators stake T and can be slashed; a thin or concentrated operator set weakens the decentralization guarantee, while heavy slashing events can stress operators and the token.
- **De-peg risk** — Any doubt about backing or redemption can push tBTC below 1:1 with BTC, with knock-on effects across DeFi pools that hold it.
- **Competitive risk** — tBTC competes with custodial [[wrapped-bitcoin|WBTC]], cbBTC, and other BTC-bridging designs; if liquidity consolidates elsewhere, demand for T staking falls.
- **Liquidity & macro risk** — ~$4.6M daily volume is thin, and in an extreme-fear, Established Bear Market regime (Fear & Greed 23) the token has been making new lows.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[bitcoin]]
- [[wrapped-bitcoin]]
- [[threshold-cryptography]]
- [[defi]]
- [[base]]
- [[uma]]
- [[ssv-network]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Trading Profile

### Venues & liquidity

T is tradable on [[binance|Binance]] — **spot (T/USDT)** plus a **USD-margined perpetual**, exposing [[funding-rate|funding]], [[open-interest|open interest]], and [[liquidations|liquidation]] data. It is **not** listed on [[hyperliquid|Hyperliquid]], so Binance is the **primary leveraged venue**. With a small-cap (~#474) profile, thin spot turnover, and an ~11.16B token supply, order-book depth is shallow; leverage amplifies moves and makes stops/liquidation clusters influential. Venue concentration on Binance means execution and sizing should assume slippage on larger orders — split entries, favor limit orders, and size positions to the perp's realistic liquidity rather than headline volume.

### Applicable strategies

- [[funding-rate-harvest]] — capture recurring Binance perp funding on T when it trends persistently positive or negative on a small-cap perp.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when T funding spikes positive into a bounce, a common small-cap perp setup.
- [[liquidation-cascade-fade]] — thin depth and leverage make T prone to liquidation flushes that overshoot and mean-revert.
- [[cash-and-carry]] — hold spot T against the short perp to harvest basis/funding while staying delta-neutral.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether a T breakout is backed by real positioning or is a fakeout.
- [[breakout-and-retest]] — deep-value token near all-time lows; range breaks with retests offer defined-risk entries on this volatile small cap.

### Volatility & regime character

T is a **small-cap DeFi / BTCfi infrastructure token** with high beta to [[bitcoin|BTC]] and broad altcoin risk sentiment. Price action reflects **tBTC / BTCfi demand** and staking flows rather than memecoin reflexivity. Volatility is elevated on a low absolute price and thin book; the token has been printing new all-time lows in the prevailing bear regime, so trends can be sharp and one-directional, with leverage-driven squeezes in both directions.

### Risk flags

- **Liquidity / venue concentration** — thin spot volume and leverage centered on Binance; large orders slip and a single-venue outage or delisting is a concentration risk.
- **Emissions / dilution** — supply is fully circulating (MC/FDV ~1.00) but **governance-mintable with no hard cap**, so DAO-driven emissions are the main forward dilution risk.
- **Narrative dependence** — value hinges on non-custodial BTC (tBTC) adoption versus WBTC/cbBTC/LBTC; fading BTCfi interest pressures demand.
- **Protocol / bridge risk** — tBTC custody, de-peg, and operator-slashing events can trigger abrupt repricing that overwhelms leveraged positions.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=TUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=TUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=T` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=T` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=TUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=TUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=T"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
