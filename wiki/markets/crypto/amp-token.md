---
title: "Amp"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["AMP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.amp.xyz"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-finance]]", "[[collateral]]", "[[stablecoins]]", "[[flexa]]"]
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
