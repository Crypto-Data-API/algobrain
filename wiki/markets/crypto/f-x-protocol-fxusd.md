---
title: "f(x) Protocol fxUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["FXUSD", "fxUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://fx.aladdin.club"
related: ["[[crvusd]]", "[[crypto-markets]]", "[[ethereum]]", "[[fx-usd-saving]]", "[[stablecoins]]"]
---

# f(x) Protocol fxUSD

**f(x) Protocol fxUSD (fxUSD)** is a decentralized, crypto-collateralized **USD [[stablecoins|stablecoin]]** from f(x) Protocol (part of the AladdinDAO ecosystem), deployed on [[ethereum|Ethereum]] and [[base|Base]]. fxUSD is minted as a byproduct of f(x)'s leverage product: the protocol lets users take leveraged long/short exposure on ETH and BTC, and the stablecoin is backed by the resulting collateral (wstETH and WBTC). As of the latest snapshot it ranks **#407** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | FXUSD |
| **Peg target** | US Dollar (~$1.00) |
| **Issuer / chain** | f(x) Protocol (AladdinDAO) — Ethereum & Base |
| **Current price** | $0.996764 |
| **Market cap** | $57.45M |
| **Market cap rank** | #407 |
| **24h volume** | $388,393 |
| **Circulating supply** | 57.63M FXUSD |
| **Total supply** | 57.63M FXUSD |
| **24h change** | +0.18% |
| **7d change** | -0.05% |
| **All-time high** | $1.071 (2026-04-28) |
| **All-time low** | $0.953062 (2024-12-05) |

The token is trading at $0.9968 — a slight (~0.3%) discount to $1, within normal range for a decentralized stablecoin and well inside its historical $0.95–$1.07 band. This is a minor soft-peg deviation, not a broken peg.

---

## Peg & backing mechanism

fxUSD's design is materially different from a fiat-backed stablecoin — it is a **crypto-backed stablecoin tied to f(x) Protocol's leverage engine**:

- **Collateral**: fxUSD is backed by yield-bearing crypto collateral, primarily **wstETH** (wrapped staked ETH) and **WBTC**. The protocol uses these reserves to fund leveraged positions.
- **Leverage product (f(x) V2)**: f(x) is an on-chain trading platform offering up to ~7x long or short exposure on ETH and WBTC with minimized liquidation and funding costs. Minting fxUSD is part of how the protocol funds and balances those positions.
- **Stability pool**: f(x) uses a stability-pool mechanism where fxUSD depositors backstop the system and absorb liquidations, earning yield in return — analogous to the stability-pool model used by other CDP stablecoins. This pool is the primary peg-defense and liquidation buffer.
- **Peg defense**: the peg is held by mint/redeem arbitrage against the collateral, the stability pool, and (in V1) zero-slippage swapping designed to keep fxUSD near $1.
- **Yield**: because the collateral is yield-bearing (staked ETH) and the stability pool earns liquidation/fee income, fxUSD carries native yield, surfaced to savers via the staked variant (see [[fx-usd-saving|f(x) USD Saving (fxSAVE)]]).

### Architecture deep-dive — the leverage-engine model

fxUSD is unusual among stablecoins because it is a **byproduct of a leverage product** rather than the protocol's primary objective:

- **Two-sided split.** f(x) Protocol's core idea is to split volatile collateral (wstETH, WBTC) into a *stable* leg and a *leveraged* leg. The stable leg backs fxUSD; the leveraged leg is sold to traders who want amplified long exposure ("xPOSITIONs" / leverage tokens). The leverage traders effectively absorb the volatility that would otherwise destabilize the stable leg — they are the counterparty that lets fxUSD stay near $1.
- **f(x) V2.** The current generation offers up to ~7x long/short exposure on ETH and WBTC with reduced liquidation and funding costs. Minting fxUSD is part of how the protocol funds and balances those positions; the collateral pool is shared between the stablecoin and the leverage book.
- **Stability pool.** fxUSD depositors backstop the system: in a liquidation, pooled fxUSD is burned against the seized collateral, so depositors absorb liquidations and earn the resulting yield/fees. This is the primary peg-defense and liquidation buffer — analogous to Liquity/[[felix-feusd|Felix]]/[[crvusd]] stability pools.
- **Peg defense & redemption.** Mint/redeem arbitrage against collateral, the stability pool, and (in V1) near-zero-slippage swapping keep fxUSD pinned near $1. When fxUSD is below par, redeeming for a full dollar of collateral is profitable, removing supply.

### Yield source & distribution

fxUSD's yield is **dual-sourced**: (1) the staking yield of the wstETH collateral, and (2) protocol fee + liquidation income captured by the stability pool. Neither is RWA carry — both are crypto-native and procyclical. Yield is surfaced to savers via the staked wrapper [[fx-usd-saving|fxSAVE]]; holding raw fxUSD is non-yield-bearing unless deposited into the stability pool or fxSAVE.

---

## Comparison vs. peer crypto-collateralized dollars

| Dimension | **fxUSD** | [[crvusd]] | [[felix-feusd\|feUSD]] | [[ethena-usde\|USDe]] |
|---|---|---|---|---|
| **Model** | Leverage-engine split (stable + leveraged legs) | CDP, LLAMMA soft-liquidation | Liquity-style CDP + stability pool | Delta-neutral basis (perps short + spot) |
| **Collateral** | wstETH, WBTC | ETH, wBTC, LSTs | HYPE + whitelisted | Staked ETH + perp shorts |
| **Yield source** | wstETH staking + stability-pool fees | scrvUSD (fee distribution) | Liquidation gains + fees | Funding-rate carry + staking |
| **Saver wrapper** | [[fx-usd-saving\|fxSAVE]] | scrvUSD | Stability pool | sUSDe |
| **Peg defense** | Stability pool + redemption arb | Continuous soft-liquidation | Redemption arb + stability pool | Hedge rebalancing + redemption |
| **Home ecosystem** | Ethereum / Base (AladdinDAO) | Ethereum (Curve) | Hyperliquid | Ethereum |
| **Scale / cap** | ~$57M | Hundreds of M | ~$75M | Multi-billion |

fxUSD's distinctive trait versus plain CDPs (crvUSD, feUSD) is that its stability is *funded by leverage demand*: it needs a healthy population of leverage traders willing to take the volatile leg. That dependency is both its yield engine and a structural risk — if leverage demand dries up, the volatility-absorption that protects the peg weakens.

---

## Narrative, category & catalysts

fxUSD belongs to the **decentralized crypto-collateralized stablecoin** category, with a leverage-product flavour, inside the **AladdinDAO** ecosystem.

- **LST yield + leverage demand:** fxUSD scales with appetite for on-chain leveraged ETH/BTC exposure and with wstETH staking yield. Strong leverage demand both grows supply and funds peg stability.
- **Risk regime:** as of 2026-06-23 crypto is in **Extreme Fear** (Fear & Greed 21, market-health 29/100, bottoming/accumulation), with [[ethereum|ETH]] ≈ $1,737 and [[bitcoin|BTC]] ≈ $64,568. Sharp ETH/BTC drawdowns are precisely what stresses fxUSD's leverage engine — liquidations spike and the stable leg's buffer is tested.
- **Competition:** a crowded field of decentralized dollars (crvUSD, DAI, GHO, plus delta-neutral USDe) caps fxUSD's share; differentiation rests on the LST-collateral + leverage design and fxSAVE yield.

---

## How / where it trades

fxUSD is a DeFi-native stablecoin and trades primarily on-chain (Curve-style pools and the protocol's own swap), not on major centralized exchanges.

- **24h volume (~$388K)** is modest; liquidity is concentrated in on-chain pools on Ethereum/Base. Treat external order books as thin.
- The closely related **[[fx-usd-saving|fxSAVE]]** token is the staked/savings wrapper that accrues yield on top of fxUSD.

## History & timeline

| Date | Event |
|---|---|
| 2024-12-05 | All-time low of $0.953062 (~4.7% soft-peg deviation) |
| 2026-04-09 | Captured in CoinGecko top-1000 listing snapshot (Source: [[coingecko-top-1000-2026-04-09]]) |
| 2026-04-28 | All-time high of $1.071 (above par) |
| 2026-06-21 | Market snapshot: $0.996764, ~$57.45M cap, rank #407, 24h volume ~$388K |

> fxUSD has held inside a ~$0.95–$1.07 band — wider than an RWA dollar but normal for a crypto-collateralized design. Only verifiable price/listing events are recorded; protocol milestones will be added as primary f(x) sources are ingested.

## Usage playbook

- **Saver angle:** to earn fxUSD's native yield, hold the staked [[fx-usd-saving|fxSAVE]] wrapper or deposit into the stability pool — raw fxUSD is idle. Stability-pool depositors earn liquidation/fee income but absorb seized (falling) collateral during stress.
- **Borrower / leverage angle:** use f(x) V2 for leveraged ETH/BTC exposure; fxUSD is the stable counter-leg. In the current Extreme-Fear regime, keep buffers wide — leverage-engine dollars are most fragile in sharp drawdowns.
- **Risk watch:** ETH/BTC collateral volatility, leverage-trader demand (the volatility sink that protects the peg), stability-pool depth, oracle integrity, and thin secondary liquidity (~$388K/day). Do not assume par exits for size during a drawdown.

---

## Risks

- **De-peg risk**: as a crypto-collateralized stablecoin, fxUSD can deviate from $1 (it has traded as low as $0.95). Sharp ETH/BTC drawdowns stress the leverage system and can pressure the peg.
- **Collateral / volatility risk**: backing is volatile crypto (wstETH, WBTC). A rapid collateral price drop can cause undercollateralization and forced liquidations.
- **Mechanism / liquidation risk**: the leverage and stability-pool design is complex; stability-pool depositors can suffer losses absorbing liquidations, and a pool drain weakens peg defense.
- **Smart-contract risk**: multiple interacting contracts (leverage, stability pool, swaps) increase the attack surface.
- **Liquidity risk**: thin secondary volume means large exits can move the price away from peg.
- **Regulatory risk**: USD-pegged DeFi stablecoins face evolving regulation.
- **Macro backdrop**: the broader market is in an "Established Bear Market" (Fear & Greed Index 23) — exactly the environment that most stresses leveraged, crypto-backed stablecoin designs.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 57.63M FXUSD |
| **Total Supply** | 57.63M FXUSD |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Platform & Chain Information

**Native Chain:** Ethereum (also Base)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x085780639cc2cacd35e474e71f4d000e2405d8f6` |
| Base | `0x55380fe7a1910dff29a47b622057ab4139da42c5` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://fx.aladdin.club](https://fx.aladdin.club) |
| **Twitter** | [@protocol_fx](https://twitter.com/protocol_fx) |
| **Telegram** | [AladdinDAO](https://t.me/AladdinDAO) |
| **Discord** | [https://discord.gg/D8znPnRqZ6](https://discord.gg/D8znPnRqZ6) |
| **GitHub** | [https://github.com/AladdinDAO/](https://github.com/AladdinDAO/) |
| **Whitepaper** | [https://fxprotocol.gitbook.io/fx-docs/overview/abstract](https://fxprotocol.gitbook.io/fx-docs/overview/abstract) |

---

## Related

- [[stablecoins]]
- [[fx-usd-saving]]
- [[crvusd]] — closest CDP peer
- [[felix-feusd]] — peer crypto-backed dollar (stability-pool model)
- [[collateralized-debt-position]]
- [[depeg]]
- [[ethereum]]
- [[base]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FXUSD |
| **Market Cap Rank** | #385 |
| **Market Cap** | $59.16M |
| **Current Price** | $1.00 |
| **Categories** | Stablecoins, USD Stablecoin, Crypto-backed Stablecoin, Fiat-backed Stablecoin |
| **Website** | [https://fx.aladdin.club](https://fx.aladdin.club) |

---

## Overview

On V1, fxUSD is unlike anything else in DeFi. It is the first truly decentralized stablecoin with the scalability to compete toe-to-toe with centralized offerings. Its combination of strong peg, built in yield and zero slippage swapping makes it extremely user friendly, while the ingenious economic design grows the available liquidity automatically as a byproduct of providing serious value to constituent LSDs.
For the f(x) V2, f(x) Protocol is a decentralized on-chain trading platform that enables stress-free leverage on ETH and WBTC while delivering the highest organic &amp; sustainable yield on stablecoins. By utilizing an innovative mechanism, we offer up to 7X long or short exposure with minimum liquidation risk &amp; funding costs. To fuel the leverage positions, the protocol mints fxUSD, a scalable &amp; decentralized stablecoin with a strong peg to the dollar and backed by wstETH and WBTC.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.07 (2026-04-28) |
| **Current vs ATH** | -6.52% |
| **All-Time Low** | $0.9531 (2024-12-05) |
| **Current vs ATL** | +5.03% |
| **24h Change** | -0.31% |
| **7d Change** | +0.01% |
| **30d Change** | -0.21% |
| **1y Change** | +0.17% |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $718,794.00 |
| **Market Cap Rank** | #385 |
| **24h Range** | $0.9939 — $1.01 |
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
