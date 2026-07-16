---
title: "Amp"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, altcoins]
aliases: ["AMP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.amp.xyz"
related: ["[[collateral]]", "[[crypto-markets]]", "[[decentralized-finance]]", "[[ethereum]]", "[[flexa]]", "[[stablecoins]]", "[[binance]]", "[[dca-strategy]]", "[[range-mean-reversion]]"]
---

# Amp

**Amp** (ticker **AMP**) is an ERC-20 "digital collateral" token on [[ethereum|Ethereum]], designed to provide instant, verifiable collateralization for any kind of value transfer. Its flagship use case is the [[flexa]] payments network, where AMP is staked as [[collateral]] to instantly and irreversibly guarantee point-of-sale and merchant transactions while the underlying settlement clears. AMP is a small-cap infrastructure token (market cap rank **#479**) and one of the original DeFi-era collateral primitives, issued by Flexa and backed by [[pantera-capital|Pantera Capital]].

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | AMP |
| **Current Price** | $0.00051997 |
| **Market Cap** | $46.68M |
| **Market Cap Rank** | #479 |
| **24h Volume** | $4.15M |
| **24h Change** | -1.63% |
| **7d Change** | -3.57% |
| **Fully Diluted Valuation** | $51.85M |
| **Circulating Supply** | ~89.78B AMP |
| **Total / Max Supply** | ~99.72B / 100.00B AMP |
| **All-Time High** | $0.120813 (2021-06-16), -99.57% from ATH |
| **All-Time Low** | $0.00050073 (2026-06-10) |

Trading backdrop: the broad crypto market sits in **extreme fear** (Crypto [[fear-and-greed-index|Fear & Greed Index]] ≈ 23) amid an **Established Bear Market** as of 2026-06-21. AMP is down ~99.6% from its 2021 cycle high and is trading within a hair of its all-time low ($0.00050073, set 2026-06-10) — i.e. at the weakest valuation in its history, far below peak collateral-network usage.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~89.78B AMP |
| **Total Supply** | ~99.72B AMP |
| **Max Supply** | 100.00B AMP |
| **Market Cap** | $46.68M |
| **Fully Diluted Valuation** | $51.85M |
| **MC / FDV Ratio** | ~0.90 |

The MC/FDV ratio of ~0.90 means roughly 90% of the maximum supply already circulates, so future dilution from token unlocks is limited — most of the 100B hard cap is already in the market. AMP migrated from the earlier FLX/Flexacoin token; the fixed 100B cap was set at launch.

---

## How & Where It Trades

**Spot venues.** AMP trades primarily as **AMP/USDT** and **AMP/USD** pairs on centralized exchanges including [[binance]], Bitget, [[kucoin]], and Crypto.com, plus on-chain via [[uniswap]] (V2/V3) and SushiSwap pools against WETH and DAI on [[ethereum]]. As a low-priced (~$0.0005), large-supply token, AMP is liquid in dollar terms relative to its cap (~$5.7M daily volume) but is a sub-$50M micro-cap with correspondingly thin order books outside the top venues.

**Collateralization mechanics (the actual utility).** Unlike a yield or governance token, AMP's design is built around *staking-as-collateral*:

- **Collateral partitions** — balances of AMP earmarked to back a specific account, application, or even an individual transaction, verifiable directly on the Ethereum blockchain.
- **Collateral managers** — smart contracts that can lock, release, and redirect AMP within partitions to support a value transfer.
- **Predefined partition strategies** — let tokens be staked as collateral *without leaving the holder's original address*, so stakers retain custody while earning Flexa network rewards.

In the [[flexa]] network, merchants receive instant payment assurance because staked AMP is held as collateral against the transaction; if a payment fails to settle, the collateral is liquidated to make the merchant whole. This makes AMP a "spendable-value insurance" layer rather than a speculative DeFi yield asset.

**Derivatives.** AMP has no significant perpetual-futures / [[hyperliquid]] presence; no meaningful funding or open-interest data is available for it. It should be treated as a spot-only micro-cap for trading purposes.

---

## Use Case, Narrative & Category

AMP sits in the **digital-collateral / payments-infrastructure** category (CoinGecko tags it under Decentralized Finance (DeFi), Payment Solutions, Ethereum Ecosystem, and Near Protocol Ecosystem). Its narrative is enabling *instant, irreversible* crypto payments by collateralizing the settlement window — solving the problem that base-layer crypto settlement is too slow for retail point-of-sale. AMP is closely tied to the fortunes of [[flexa]]; its value accrual depends on collateral demand from the payments network rather than on transaction fees or staking inflation.

---

## Custody, Staking & Regulatory

- **Custody / staking model** — AMP's "predefined partition strategies" let holders stake as collateral *without transferring tokens out of their own address*, retaining custody while earning Flexa network rewards. This is non-custodial collateralization, distinct from depositing into a centralized staking pool.
- **Redemption / settlement** — AMP is not a redeemable claim on an off-chain asset (unlike [[kinesis-silver|KAG]] or [[ripple-usd|RLUSD]]); it is a crypto-native collateral buffer. If a Flexa-guaranteed payment fails to settle, the earmarked AMP is liquidated to make the merchant whole — the collateral *is* the backstop, not a reserve held elsewhere.
- **Regulatory status** — AMP appears among tokens named in **SEC enforcement actions** as an "alleged security" (CoinGecko tags it "Alleged SEC Securities"), creating US delisting/legal overhang. It is a permissionless ERC-20 with no KYC at the token level.

---

## Peer Comparison — Collateral / Payments-Infrastructure Tokens

| Token | Role | Backing / model | Cap status |
|---|---|---|---|
| **AMP** (this page) | Payments collateral (Flexa) | Crypto-native staked collateral buffer | Fixed 100B; ~90% circulating |
| [[ripple-usd|RLUSD]] | Payment stablecoin | Fiat + T-bill reserves (redeemable) | Uncapped mint/redeem |
| [[usdtb]] | Payment/collateral stablecoin | BUIDL T-bill reserves | Uncapped mint/redeem |
| [[kinesis-silver|KAG]] | Spendable hard-asset money | 1 oz physical silver (redeemable) | Minted vs vaulted metal |

AMP is the odd one out: a *collateral primitive* rather than a price-stable instrument. Its peers in function are payment rails, but unlike them AMP carries full price volatility (it is not pegged), which is why over-collateralization is required in the Flexa design.

---

## Notable History

- Launched in 2020 as a rebrand/upgrade of **Flexacoin (FLX)**, with a fixed 100B supply.
- Backed by **Pantera Capital** (CoinGecko lists AMP in the Pantera Capital portfolio).
- AMP appears among the tokens named in **SEC enforcement actions** as an "alleged security" (CoinGecko tags it "Alleged SEC Securities"), reflecting US regulatory scrutiny of exchange-listed tokens.
- Bridged to **Near Protocol** and **Energi** in addition to its native Ethereum deployment.

---

## Risks

- **Single-use-case dependency** — AMP's utility is concentrated in the Flexa collateral network; weak payments adoption directly caps demand.
- **Regulatory risk** — inclusion in SEC "alleged securities" lists creates delisting and legal overhang in the US.
- **Deep drawdown / bear market** — down ~99.6% from ATH and trading in an extreme-fear, established-bear-market environment.
- **Micro-cap liquidity** — sub-$50M market cap; thin books outside major exchanges amplify slippage.
- **Smart-contract risk** — collateral-manager contracts that lock/redirect staked AMP are an attack surface.

---

## Trading Profile

### Venues & liquidity

AMP is tradable on **Binance SPOT only** among tier-1 CEXs (with secondary spot listings on KuCoin and Crypto.com, plus on-chain Uniswap/SushiSwap pools) — **there is no liquid perpetual venue**, so leverage and short access are limited and AMP is a **spot-primary asset**. Perp funding/basis/liquidation strategies do NOT apply. As a sub-$50M micro-cap with a very low unit price (~$0.0005) and thin books outside Binance, execution should lean on limit orders, staggered entries, and small clip sizes; large market orders will move price and incur meaningful slippage. Position sizing must assume no easy hedge — exposure is directional long unless routed through borrow/margin where available, and exit liquidity concentrates on Binance AMP/USDT.

### Applicable strategies

- [[dca-strategy]] — for a spot-only micro-cap trading near its all-time low, mechanical dollar-cost averaging removes timing risk and fits the no-leverage, accumulation-oriented profile.
- [[range-mean-reversion]] — AMP has spent long stretches pinned in tight bands near ATL; fading extremes within an established range suits its low-volatility, sub-$50M chop.
- [[rsi-mean-reversion]] — deeply oversold RSI readings during established-bear drift offer bounce entries on a token with no perp overhang to force liquidations.
- [[breakout-and-retest]] — with thin books, clean breakouts from multi-week bases are tradable long-only, using a retest to confirm before sizing up on spot.
- [[volatility-targeting]] — scaling spot size to realized volatility caps drawdown on an illiquid micro-cap where slippage, not funding, is the main cost.
- [[grid-trading]] — a range-bound, spot-only token near ATL is a natural fit for grid orders that harvest AMP/USDT oscillation without leverage.

### Volatility & regime character

Small-cap infrastructure / DeFi collateral token (rank ~#524), high-beta to BTC/ETH with amplified downside in risk-off regimes. Not a memecoin — value is tied to Flexa collateral-network demand rather than reflexive hype — but it behaves like a deep-drawdown micro-cap: illiquid, prone to long sideways bases punctuated by sharp beta-driven moves. Correlation to majors is high on the downside; independent upside requires a Flexa/payments narrative catalyst. Currently trading within a hair of its all-time low, so realized volatility can compress for extended periods then spike.

### Risk flags

- **Venue/liquidity concentration** — spot-only, with real depth concentrated on Binance; delisting from that venue would sharply impair tradability, and thin secondary books amplify slippage.
- **Regulatory overhang** — AMP is tagged among "Alleged SEC Securities," creating US delisting/legal risk that can trigger sudden liquidity withdrawal.
- **Narrative dependence** — demand hinges almost entirely on Flexa collateral usage; weak payments adoption caps upside and invites structural downtrend.
- **No hedge / no perp** — absence of a liquid perpetual venue means exposure cannot be cheaply shorted or hedged; risk must be managed via sizing and spot exits.
- **Micro-cap drawdown risk** — down ~99.6% from ATH and near all-time lows; further capitulation is possible in continued bear regimes.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=AMPUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=AMPUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=AMPUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=AMPUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[flexa]]
- [[decentralized-finance]]
- [[collateral]]
- [[stablecoins]] / [[stablecoin]]
- [[ripple-usd]]
- [[pantera-capital]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- CoinGecko / cryptodataapi.com top-1000 snapshot, 2026-06-21 — live market data (price, market cap, supply, ATH/ATL)
- CoinGecko — Amp (AMP) category tags and project metadata (Pantera Capital portfolio, Alleged SEC Securities, Flexa network)

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AMP |
| **Market Cap Rank** | #525 |
| **Market Cap** | $38.62M |
| **Current Price** | $0.00043026 |
| **Categories** | Decentralized Finance (DeFi), Payment Solutions, Alleged SEC Securities, Made in USA |
| **Website** | [https://www.amp.xyz](https://www.amp.xyz) |

---

## Overview

What is Amp?

Amp is described as the new digital collateral token offering instant, verifiable assurances for any kind of value transfer. Using Amp, networks like Flexa can quickly and irreversibly secure transactions for a wide variety of asset-related use cases.

How does Amp work?

Amp claims to offer a straightforward but versatile interface for verifiable collateralization through a system of collateral partitions and collateral managers. Where collateral partitions can be designated to collateralize any account, application, or even transaction, and carry balances which are directly verifiable on the Ethereum blockchain, collateral managers are smart contracts that can lock, release, and redirect collateral in these partitions as needed in order to support value transfer activities. Amp supports a wide variety of use cases for collateralization, and also introduces the concept of predefined partition strategies, which can enable special capabilities such as collateral models through which tokens can be staked without ever leaving their original address.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 89.78B AMP |
| **Total Supply** | 99.72B AMP |
| **Max Supply** | 100.00B AMP |
| **Fully Diluted Valuation** | $42.90M |
| **Market Cap / FDV Ratio** | 0.90 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1208 (2021-06-16) |
| **Current vs ATH** | -99.64% |
| **All-Time Low** | $0.00042608 (2026-07-13) |
| **Current vs ATL** | +1.18% |
| **24h Change** | -0.04% |
| **7d Change** | -3.00% |
| **30d Change** | -20.94% |
| **1y Change** | -88.79% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xff20817765cb7f73d4bde2e66e067e58d11095c2` |
| Near Protocol | `ff20817765cb7f73d4bde2e66e067e58d11095c2.factory.bridge.near` |
| Energi | `0xad7abe6f12f1059bdf48ae67bff92b00438ced95` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | AMP/USDT | N/A |
| KuCoin | AMP/USDT | N/A |
| Crypto.com Exchange | AMP/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XFF20817765CB7F73D4BDE2E66E067E58D11095C2/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Sushiswap | 0XFF20817765CB7F73D4BDE2E66E067E58D11095C2/0X6B175474E89094C44DA98B954EEDEAC495271D0F | Spot |
| Uniswap V3 (Ethereum) | 0XFF20817765CB7F73D4BDE2E66E067E58D11095C2/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.amp.xyz](https://www.amp.xyz) |
| **Twitter** | [@ampdotxyz](https://twitter.com/ampdotxyz) |
| **Reddit** | [https://www.reddit.com/r/amptoken/](https://www.reddit.com/r/amptoken/) |
| **Telegram** | [ampchat](https://t.me/ampchat) (2,810 members) |
| **Discord** | [https://discord.gg/T4EY6yx](https://discord.gg/T4EY6yx) |
| **GitHub** | [https://github.com/amptoken](https://github.com/amptoken) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.36M |
| **Market Cap Rank** | #525 |
| **24h Range** | $0.00042713 — $0.00043363 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
