---
title: "Threshold Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, defi]
aliases: ["T", "Threshold"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://threshold.network/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[wrapped-bitcoin]]"]
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

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | T |
| **Market Cap Rank** | #478 |
| **Market Cap** | $43.79M |
| **Current Price** | $0.00392469 |
| **Categories** | Decentralized Finance (DeFi), Cross-chain Communication, BTCfi Protocol |
| **Website** | [https://threshold.network/](https://threshold.network/) |

---

## Overview

Threshold is a project merged from the NuCypher and Keep networks, which strives to provide different threshold cryptography solutions in a fully decentralized manner to the web3 community. Threshold cryptography is a technology that uses cryptography to unlock greater utility and usability for digital assets without needing to trust a centralized party. Threshold cryptography distributes sensitive operations across multiple independent entities – like nodes in a network – and requires a threshold, or minimum number of those entities to cooperate for the operation to be successful.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 11.15B T |
| **Total Supply** | 11.15B T |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $43.79M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2269 (2022-03-02) |
| **Current vs ATH** | -98.26% |
| **All-Time Low** | $0.00316726 (2026-06-25) |
| **Current vs ATL** | +24.59% |
| **24h Change** | -5.23% |
| **7d Change** | +15.58% |
| **30d Change** | +1.34% |
| **1y Change** | -77.14% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xcdf7028ceab81fa0c6971208e83fa7872994bee5` |
| Base | `0x26f3901ac8a79c50fb0d8289c74f0d09adc42e29` |
| Optimistic Ethereum | `0x747e42eb0591547a0ab429b3627816208c734ea7` |
| Solana | `4Njvi3928U3figEF5tf8xvjLC5GqUN33oe4XTJNe7xXC` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | T/USDT | N/A |
| Kraken | T/USD | N/A |
| Upbit | T/KRW | N/A |
| Bitget | T/USDT | N/A |
| KuCoin | T/USDT | N/A |
| Crypto.com Exchange | T/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://threshold.network/](https://threshold.network/) |
| **Twitter** | [@TheTNetwork](https://twitter.com/TheTNetwork) |
| **Discord** | [https://discord.com/invite/threshold](https://discord.com/invite/threshold) |
| **GitHub** | [https://github.com/threshold-network](https://github.com/threshold-network) |
| **Whitepaper** | [https://docs.threshold.network/](https://docs.threshold.network/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $16.27M |
| **Market Cap Rank** | #478 |
| **24h Range** | $0.00389322 — $0.00418654 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
