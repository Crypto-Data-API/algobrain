---
title: "Hyperlane"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives]
aliases: ["HYPER", "Hyperlane"]
entity_type: protocol
founded: 2022
headquarters: "Decentralized"
website: "https://hyperlane.xyz/"
related: ["[[arbitrum]]", "[[cross-chain]]", "[[crypto-markets]]", "[[ethereum]]", "[[interoperability]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# Hyperlane

**Hyperlane** (HYPER) is an open-source, **permissionless [[interoperability]] / cross-chain messaging** framework. It lets any blockchain — including new or app-specific chains — connect to the broader multi-chain ecosystem without needing approval from a central authority, powering [[cross-chain]] applications such as asset bridges, cross-chain governance, and interchain DeFi. The network reports connectivity across 170+ blockchains and multiple virtual-machine families. It ranks **#686** by market capitalization.

> **Disambiguation:** This page covers **Hyperlane** the interoperability protocol (ticker **HYPER**, hyperlane.xyz). Do not confuse it with Hyperliquid (HYPE), a separate perpetuals exchange. The "Hyperliquid HYPER-PERP" entry in the listings table below is a *perpetual futures market on Hyperlane's HYPER token traded on Hyperliquid*, not the Hyperliquid token.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* HYPER trades around **$0.07998**, market cap **~$27.0M** (rank #686), **+1.13% over 24h** and **+9.83% over 7d** — relative strength versus an Extreme-Fear market (Fear & Greed 22, BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HYPER |
| **Market Cap Rank** | #686 |
| **Market Cap** | $27,047,644 |
| **Current Price** | $0.079977 |
| **Categories** | Infrastructure, BNB Chain Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Optimism Ecosystem, Interoperability, Base Ecosystem, Cross-chain Communication, Binance HODLer Airdrops, Binance Wallet IDO, Base Native |
| **Website** | [https://hyperlane.xyz/](https://hyperlane.xyz/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Hyperlane is an open-source, permissionless framework for blockchain [[interoperability]]. Its defining property is **permissionless deployment**: unlike bridges that must be individually authorized and integrated, any developer can deploy Hyperlane to a new chain themselves, instantly connecting it to the network. This makes it especially relevant for the proliferation of L2s, app-chains, and rollups, which need interoperability "out of the box."

At its core, Hyperlane provides generalized **interchain messaging** — arbitrary data and contract calls passed between chains — on top of which it offers **Warp Routes** (a framework for permissionless cross-chain token bridges). A distinctive design element is **Interchain Security Modules (ISMs)**: modular, application-configurable security. Rather than forcing every app to accept one trust model, developers choose how messages are verified — multisig, optimistic, or external verification (e.g., reusing the security of [[cross-chain]] proof systems) — trading off cost, latency, and security per use case. The longer-term ambition stated by the team is to evolve from interchain messaging into broader value-transfer infrastructure for a multi-chain economy.

### How a cross-chain message actually flows

Unlike the ZK-proof networks elsewhere in this cohort, Hyperlane is an **interoperability / message-passing** protocol — its security comes from a configurable verification layer, not from succinct proofs. The lifecycle of a message:

1. **Dispatch.** A contract on the origin chain calls Hyperlane's `Mailbox`, emitting the message (recipient chain + address + payload). The Mailbox is the single canonical contract deployed on every connected chain.
2. **Observe & sign (validators).** Off-chain **validators** watch the origin Mailbox and sign attestations (checkpoints) over the messages it has committed to.
3. **Relay.** A permissionless **relayer** picks up the message plus the validators' signatures and delivers them to the destination chain's Mailbox.
4. **Verify (ISM).** Before delivery, the destination Mailbox calls the recipient's chosen **Interchain Security Module**. The ISM decides whether to accept the message — checking, for example, that enough validators in a configured multisig signed it, or running an optimistic challenge window, or deferring to an external proof system. Only if the ISM approves is the message executed on the recipient contract.

The crucial design point is that **security is set by the application, not the protocol**: two apps on the same Hyperlane deployment can demand entirely different trust assumptions. That modularity is the differentiator — and the double edge, because a poorly configured ISM is the application's responsibility, not Hyperlane's. **Warp Routes** are simply token contracts wired to this messaging layer: locking/burning on the origin and minting/releasing on the destination, with the chosen ISM gating each transfer.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 241.36M HYPER |
| **Total Supply** | 807.33M HYPER |
| **Max Supply** | 1.00B HYPER |
| **Fully Diluted Valuation** | $70.77M |
| **Market Cap / FDV Ratio** | 0.30 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.6641 (2025-07-11) |
| **Current vs ATH** | -86.84% |
| **All-Time Low** | $0.0782 (2026-03-29) |
| **Current vs ATL** | +11.78% |
| **24h Change** | +1.13% |
| **7d Change** | +9.83% |
| **1y Change** | +0.00% |

> HYPER is a recent token (ATH $0.6641 in July 2025, ~87% below peak). Only ~30% of max supply circulates (MCap/FDV ≈ 0.30), so future unlocks are a material dilution overhang despite the +9.8% weekly bounce.

---

## Token Role

The **HYPER token** was distributed in 2025 (including via a Binance HODLer airdrop and IDO) and underpins the protocol's economic security and coordination:

- **Staking / security** — HYPER is staked to secure the network and its validators/relayers; staked capital backs the default and economic-security ISMs that verify interchain messages.
- **Incentives** — relayers and validators that transport and attest to messages are rewarded, aligning infrastructure operators with usage.
- **Governance** — HYPER governs protocol parameters and treasury.

The core demand thesis is that as more chains deploy Hyperlane and route messages/token transfers through it, fees and security demand should accrue to the staked-HYPER economy. The risk, common to interoperability tokens, is that message-passing fees are competed toward zero and that the token's economic-security role is small relative to circulating/diluted supply.

## Competitive Position

Hyperlane competes in a crowded interoperability field against LayerZero, Wormhole, Axelar, Chainlink CCIP, and Cosmos IBC. Its differentiation is permissionless deployment plus modular security (ISMs); the trade-off is that "permissionless" can shift more security responsibility onto application developers.

| Project | Deployment model | Security model | Differentiator vs. Hyperlane |
|---|---|---|---|
| **Hyperlane (HYPER)** | Permissionless — anyone deploys to a new chain | Modular, app-chosen ISMs (multisig / optimistic / external) | Self-serve interop + per-app trust configuration |
| **LayerZero (ZRO)** | Partner/integration-led | Configurable DVNs (decentralized verifier networks) | Large incumbent footprint; conceptually similar modular verification |
| **Wormhole (W)** | Integration-led | Guardian validator set | Broad ecosystem reach; guardian trust model |
| **Axelar (AXL)** | Integration-led | Proof-of-stake validator network (own chain) | Full app-chain securing the network |
| **Chainlink CCIP** | Permissioned/curated rollout | Oracle + Risk Management Network | Enterprise focus; conservative, curated onboarding |
| **Cosmos IBC** | Native to IBC-enabled chains | Light-client verification | Trust-minimized but limited to compatible chains |

The cleanest contrast is permissionless self-serve deployment (Hyperlane) versus the curated/integration-led onboarding of most rivals — a fit for the long tail of new L2s and app-chains.

## Narrative & Catalysts

Hyperlane rides the **interoperability / modular-blockchain** narrative — the thesis that an explosion of L2s, rollups, and app-chains needs out-of-the-box connectivity. Distribution carries a **Binance-ecosystem** angle (Binance HODLer Airdrops, Binance Wallet IDO category tags) and a **Base-native** positioning. Catalysts: new-chain deployments and Warp Route token bridges that grow message volume, staking participation that deepens the economic-security layer, and any move "up the stack" from messaging into value-transfer infrastructure. The principal counterweight is fee compression (interop messaging tends toward commoditization) plus the unlock schedule.

## History & Timeline

- **founded: 2022** (per frontmatter) — Hyperlane originates as a permissionless interoperability framework.
- **2025** — HYPER token distributed (including via a Binance HODLer airdrop and IDO).
- **2025-07-11** — HYPER all-time high of **$0.6641** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-03-29** — All-time low of **$0.0782** (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-22** — Trades ~$0.0800, ~87% below ATH; rank #686, market cap ~$27M; relative strength (+1.13% 24h, +9.83% 7d) against an Extreme-Fear market (cryptodataapi.com / CoinGecko).

> The network reports connectivity across 170+ blockchains. Exact dated deployment milestones beyond the price events above are not asserted because no specific dated source has been ingested.

## Risks

- **Bridge/security risk** — cross-chain messaging is historically the most-exploited surface in crypto; a flaw in a widely-used ISM or Warp Route could be catastrophic for connected apps. The permissionless, app-configurable security model means misconfiguration risk lands on the application.
- **Intense competition** — well-capitalized rivals (LayerZero, Wormhole, CCIP) with strong distribution.
- **Fee compression** — interop messaging may commoditize, limiting fee accrual to the token.
- **Dilution** — low circulating-to-FDV ratio (~0.30) means significant scheduled unlocks.
- **Liquidity / size** — ~$27M cap small-cap with elevated volatility.

## Trading Playbook (bear / Extreme-Fear regime)

> *Not investment advice. Context only, for the 2026-06-22 Established-Bear-Market regime (Fear & Greed 21).*

- **Regime read.** HYPER showed relative strength (+9.83% on the week) while the broad market sits in Extreme Fear — notable for a ~$27M interop small-cap, but low-float strength can reverse hard. It is trading just above its all-time low (+11.78% from ATL), a level worth watching as support.
- **Dilution-aware.** MC/FDV ≈ 0.30 means ~70% of fully diluted value is unrealized supply; unlock windows are the dominant medium-term overhang.
- **Security-event tail risk.** Interop tokens carry idiosyncratic exploit risk; a bridge/ISM incident anywhere in the ecosystem can reprice the token sharply regardless of macro.
- **Sizing.** Small-cap depth — use limits and size for the volatility.

---

## Platform & Chain Information

**Native Chain:** Arbitrum One

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0xc9d23ed2adb0f551369946bd377f8644ce1ca5c4` |
| Ethereum | `0x93a2db22b7c736b341c32ff666307f4a9ed910f5` |
| Binance Smart Chain | `0xc9d23ed2adb0f551369946bd377f8644ce1ca5c4` |
| Base | `0xc9d23ed2adb0f551369946bd377f8644ce1ca5c4` |
| Optimistic Ethereum | `0x9923db8d7fbacc2e69e87fad19b886c81cd74979` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HYPER/USDT | N/A |
| Upbit | HYPER/KRW | N/A |
| Bitget | HYPER/USDT | N/A |
| KuCoin | HYPER/USDT | N/A |
| Crypto.com Exchange | HYPER/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | HYPER-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://hyperlane.xyz/](https://hyperlane.xyz/) |
| **Twitter** | [@hyperlane](https://twitter.com/hyperlane) |
| **Discord** | [https://discord.com/invite/VK9ZUy3aTV](https://discord.com/invite/VK9ZUy3aTV) |
| **GitHub** | [https://github.com/hyperlane-xyz](https://github.com/hyperlane-xyz) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.35M (Apr-2026 snapshot) |
| **Market Cap Rank** | #686 |
| **Current Price** | $0.079977 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

HYPER is a **two-venue derivatives market**, tradable on both **Binance** (HYPER/USDT spot plus a **USD-margined perpetual**) and **Hyperliquid** (**HYPER-PERP**, offering up to roughly **40-50x** leverage). This dual listing gives the token unusually deep, liquid order books for a ~$27M small-cap, with Binance supplying centralized spot/perp depth and Hyperliquid providing an on-chain perp with its own funding and order flow. The parallel venues mean execution can be split or routed to the tighter book, and — critically — the **spot leg on Binance plus perps on both venues** make cash-and-carry and cross-venue funding trades mechanically feasible rather than theoretical. Still, this is a low-float infra token: even with two liquid venues, absolute depth is thin versus large-caps, so scale in with limit orders and size for slippage on larger clips.

### Applicable strategies

- [[cash-and-carry]] — Binance spot HYPER can be held against a short on either the Binance or Hyperliquid perp to lock the basis/funding when the low-float token trades at a premium.
- [[funding-rate-harvest]] — collect perp funding on HYPER-PERP; low-float infra alts with airdrop-driven positioning often carry persistent, harvestable funding.
- [[hl-vs-cex-funding-divergence]] — HYPER runs perps on **both** Hyperliquid and Binance, so funding can diverge between the on-chain and CEX books, creating a delta-neutral spread to capture.
- [[crowded-long-funding-fade]] — post-airdrop/narrative pops in a thin infra name frequently over-extend longs; fade the crowd when perp funding spikes richly positive.
- [[liquidation-cascade-fade]] — 40-50x leverage on a ~$27M-cap token makes stop-run cascades violent and often over-shoot, offering mean-reversion entries into forced flow.
- [[breakout-and-retest]] — trading just above its all-time low, HYPER offers a defined support/ATL level for breakout-retest structure with a clean invalidation.

### Volatility & regime character

HYPER is a **high-beta interoperability / infra altcoin** — a recent, low-float token (MC/FDV ≈ 0.30) with elevated realized volatility and reflexive, narrative-driven moves tied to the modular-blockchain/interop theme and its Binance-ecosystem distribution. It trades with **high positive beta to BTC/ETH**: it amplifies broad-market risk-on/risk-off swings, though its thin float lets it decouple sharply on token-specific catalysts (as seen in its +9.8% weekly relative strength against an Extreme-Fear tape). Expect large-alt drawdowns in risk-off regimes and outsized rallies in risk-on.

### Risk flags

- **Dilution / unlocks** — only ~30% of max supply circulates (MC/FDV ≈ 0.30); scheduled unlocks are the dominant medium-term supply overhang and can cap or reverse rallies.
- **Liquidity / small-cap depth** — a ~$27M cap means real slippage on size despite two liquid venues; venue-concentration in Binance + Hyperliquid is a single-point dependency.
- **Narrative dependence** — price leans heavily on the interoperability/modular narrative and Binance-ecosystem flows; sentiment shifts hit hard.
- **Security-event tail risk** — as an interop/bridge token, an ISM or Warp Route exploit anywhere in the ecosystem can reprice it violently regardless of macro or funding.
- **Perp funding dislocations** — 40-50x leverage and low float make funding swings and liquidation cascades frequent; funding can flip and gap around unlocks and narrative events.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=HYPER` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=HYPER` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=HYPER&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=HYPER&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=HYPER"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[arbitrum]]
- [[ethereum]]
- [[cross-chain]]
- [[interoperability]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.
