---
title: "Stargate Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["STG"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://stargate.finance/"
related: ["[[cross-chain-bridge]]", "[[crypto-markets]]", "[[ethereum]]", "[[layerzero]]", "[[smart-contract-risk]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[token-unlock-supply-event]]"]
---

# Stargate Finance

**Stargate Finance** (STG) is a [[cross-chain-bridge]] for native assets built on top of [[layerzero]], the omnichain messaging protocol. Its signature feature is **unified liquidity**: a single pool of an asset (e.g., USDC) can serve transfers to many chains at once, with instant guaranteed finality on the destination — solving the fragmented-liquidity problem that plagues route-by-route bridges. STG is the protocol's governance and incentive token.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, STG trades at **$0.20855**, ranked **#659** by market capitalization with a market cap of **~$29,065,000** (24h -1.26%). The standout figure is a sharp **-17.07% over 7 days** — by far the worst weekly performance in this cohort — underscoring acute weakness in the bridge-token sector amid the bear regime (BTC ~$64,390; Fear & Greed Index 21 — "Extreme Fear"). The token sits ~95% below its 2022 all-time high.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | STG |
| **Market Cap Rank** | #659 |
| **Market Cap** | ~$29,065,000 |
| **Current Price** | $0.20855 |
| **24h / 7d Change** | -1.26% / **-17.07%** |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, BNB Chain Ecosystem, Avalanche Ecosystem, Polygon Ecosystem, Fantom Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Optimism Ecosystem, Mantle Ecosystem, Linea Ecosystem, Bridge Governance Tokens, Base Ecosystem, FTX Holdings, Scroll Ecosystem, Berachain Ecosystem, Kava Ecosystem, Base Native |
| **Website** | [https://stargate.finance/](https://stargate.finance/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Stargate is a composable native-asset [[cross-chain-bridge]] offering unified liquidity and instant guaranteed finality, built on the [[layerzero]] omnichain messaging stack. Where many bridges fragment liquidity across each origin→destination route, Stargate pools liquidity per asset so a transfer can be settled instantly from a shared, capital-efficient reserve. It was one of the first high-profile applications of LayerZero and helped popularise the "omnichain fungible token" (OFT) model.

Stargate moved to a v2 architecture introducing a credit/path-based system and a Hydra design for issuing native assets across chains, but the core promise is unchanged: native (not user-facing wrapped) assets, deep pooled liquidity, and fast finality across the many chains LayerZero supports.

---

## How Stargate Works

**Unified-liquidity bridging over LayerZero:**

1. A user swaps an asset (e.g., USDC) on the origin chain into Stargate's pool for that asset.
2. Stargate sends a cross-chain message via [[layerzero]] — which relies on a configurable security stack of Decentralized Verifier Networks (DVNs) and executors — to the destination chain.
3. The user receives the **native** destination asset out of Stargate's unified pool on that chain, with guaranteed finality (no long optimistic wait).
4. **Liquidity providers** deposit single-sided liquidity into the asset pools and earn a share of bridge fees (and historically STG incentives).

**What the STG token does:**

- **Governance** — STG governs the protocol; holders can lock STG into **veSTG** (vote-escrowed) to gain governance weight and direct emissions/fee parameters, in the Curve-style ve model.
- **Incentives / fee accrual** — STG has been used to reward LPs and to align long-term participants via veSTG; protocol fees can be directed toward stakers/governance per DAO decisions.

**How LP yield is generated:** Stargate LPs earn the transfer fees paid by users moving assets across chains, plus any STG incentive emissions. Yield therefore tracks real bridging volume — which is cyclical and, as the -17% weekly token move suggests, currently under pressure.

---

## Architecture Deep Dive

Stargate sits one layer above [[layerzero]]: LayerZero provides the generic cross-chain *messaging* primitive, and Stargate is the *liquidity* application that uses it to move native value. The key innovations:

- **Unified liquidity ("Delta algorithm" / credit system).** Rather than maintaining a separate pool for each origin→destination *pair*, Stargate maintains one pool per *asset per chain* and tracks inter-pool "credits" so a single reserve can service transfers to many destinations. This is what lets the protocol promise **instant guaranteed finality**: the destination payout is committed at source time, not contingent on a slow optimistic challenge window as in [[across-protocol]].
- **Guaranteed finality.** A transfer either fully completes or is not committed — Stargate's design avoids the "in-flight" wrapped-asset limbo that plagues lock/mint bridges. The cost is that pool balances and the credit system must be carefully managed to avoid a destination pool running dry.
- **LayerZero messaging + DVNs.** Each transfer is carried by a LayerZero message. In LayerZero v2 the security of that message is enforced by a configurable set of **Decentralized Verifier Networks (DVNs)** plus an executor; Stargate (and integrators) choose the DVN stack, which directly determines the trust assumptions. This is the central, and most debated, trust dependency (see Risks and oracle).
- **Stargate v2 & Hydra.** v2 reworked the architecture around a credit/path-based model and a **Hydra** design that lets new chains issue native assets (rather than canonical-wrapped ones) and plug into the unified liquidity network, reducing fragmentation as the chain count grows. Stargate also popularised the **omnichain fungible token (OFT)** standard, where a token's total supply is tracked coherently across chains.

**Where Stargate sits in the stack:** [[layerzero]] (messaging) → Stargate (liquidity / native-asset transfer + OFT) → integrators (wallets, aggregators, dApps embedding cross-chain UX). Many aggregators route through Stargate for stablecoin transfers specifically because of its deep unified pools.

---

## Comparison vs Competing Bridges

| Dimension | **Stargate** | [[across-protocol\|Across]] | [[chainflip\|Chainflip]] | Wormhole / Portal | Synapse |
|---|---|---|---|---|---|
| Trust model | [[layerzero\|LayerZero]] DVN messaging | Optimistic ([[uma\|UMA]]) + relayers | TSS validator vaults | Guardian multisig + messaging | Optimistic / messaging |
| Liquidity model | **Unified per-asset pools** | Single shared HubPool | JIT market-maker quotes | Lock/mint + liquidity | Per-route AMM + nUSD |
| Finality | **Instant, guaranteed** | Optimistic (challenge window for relayers) | Source-chain confirmations | Guardian-attested | Optimistic |
| User receives | Native asset | Native/canonical | Native | Wrapped (Portal) or native | nUSD / native |
| Chain breadth | **Very broad (LayerZero set)** | EVM-focused | BTC, SOL + EVM | Very broad | Broad EVM |
| Headline strength | Stablecoin depth, OFT standard | Capital efficiency, no wrapped assets | Native non-EVM swaps | Generic messaging breadth | AMM-style routing |
| Key trust assumption | Honest DVN set | ≥1 honest disputer | Honest validator supermajority | Honest guardian quorum | Router/relayer honesty |

Stargate's edge is the combination of **deep unified stablecoin liquidity, instant finality, and the OFT standard**, making it a default rail for stablecoin movement and token omnichain deployment. Its dependency on the LayerZero/DVN verification layer is the main thing that distinguishes its risk profile from oracle-optimistic (Across) or validator-vault (Chainflip) designs.

---

## Governance & Value Accrual

- **Stargate DAO & veSTG.** STG holders can lock STG into **veSTG** (vote-escrowed STG) in the Curve-style ve model. Longer locks grant more voting power, which is used to direct emissions/incentives across pools and to govern fee parameters and supported assets — a "gauge"-style competition for liquidity incentives.
- **Fee accrual.** Bridge fees accrue to LPs and, per DAO decisions, can be directed to veSTG lockers/stakers — giving STG a closer link to protocol revenue than many pure governance tokens, contingent on governance choosing to route fees that way.
- **Supply overhang.** Circulating supply (~116M) is well below the 1B max; the gap is the most important tokenomics fact for STG holders, since future emissions/unlocks are a structural source of sell pressure (relevant context for the -17% weekly drop).
- **LayerZero relationship.** Stargate was the flagship LayerZero application and shares deep ties with the LayerZero Labs ecosystem; this is both a distribution advantage and a concentration of dependency on a single messaging provider.

---

## Notable History

- **2022 launch & "Curve War"-style bootstrap.** Stargate launched in March 2022 as LayerZero's flagship app with an aggressive, heavily-incentivised bonding/IDO and rapidly accumulated stablecoin liquidity. The STG ATH of ~$4.14 dates to that launch period.
- **OFT standard adoption.** Stargate's OFT model became a widely-used pattern for deploying a single coherent token across many chains, adopted well beyond Stargate itself.
- **v2 migration.** The move to a credit/path-based v2 with the Hydra native-asset design modernised the architecture for a multi-rollup world.
- **Bridge-sector scrutiny.** Like all bridges, Stargate operates under the shadow of the 2022 bridge-hack wave (Ronin, Wormhole, Nomad), which permanently raised scrutiny on the messaging/verification layer it inherits from [[layerzero]].

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 116.28M STG |
| **Total Supply** | 116.28M STG |
| **Max Supply** | 1.00B STG |
| **Fully Diluted Valuation** | $24.84M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.14 (2022-04-02) |
| **Current vs ATH** | -94.86% |
| **All-Time Low** | $0.1045 (2025-12-31) |
| **Current vs ATL** | +103.73% |
| **24h Change** | +1.31% |
| **7d Change** | -22.46% |
| **30d Change** | +19.57% |
| **1y Change** | +26.40% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xaf5191b0de278c7286d6c7cc6ab6bb8a73ba2cd6` |
| Berachain | `0x9895d81bb462a195b4922ed7de0e3acd007c32cb` |
| Mantle | `0x8731d54e9d02c286767d56ac03e8037c07e01e98` |
| Kava | `0x83c30eb8bc9ad7c56532895840039e62659896ea` |
| Linea | `0x808d7c71ad2ba3fa531b068a2417c63106bc0949` |
| Fantom | `0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590` |
| Scroll | `0x8731d54e9d02c286767d56ac03e8037c07e01e98` |
| Base | `0xe3b53af74a4bf62ae5511055290838050bf764df` |
| Polygon Pos | `0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590` |
| Binance Smart Chain | `0xb0d502e938ed5f4df2e681fe6e419ff29631d62b` |
| Arbitrum One | `0x6694340fc020c5e6b96567843da2df01b2ce1eb6` |
| Optimistic Ethereum | `0x296f55f8fb28e498b858d0bcda06d955b2cb3f97` |
| Avalanche | `0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | STG/USDT | N/A |
| Kraken | STG/USD | N/A |
| Bitget | STG/USDT | N/A |
| KuCoin | STG/USDT | N/A |
| Crypto.com Exchange | STG/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | STG-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://stargate.finance/](https://stargate.finance/) |
| **Twitter** | [@StargateFinance](https://twitter.com/StargateFinance) |
| **Discord** | [https://stargate.finance/discord](https://stargate.finance/discord) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $12.91M |
| **Market Cap Rank** | #328 |
| **24h Range** | $0.2054 — $0.2193 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Risks

Bridges are a top exploit vector in crypto (Ronin, Wormhole, Nomad and others lost hundreds of millions in 2022 alone). Stargate's risk profile:

- **[[layerzero]] dependency & verifier trust** — Stargate's security inherits from LayerZero's messaging stack. The integrity of cross-chain messages depends on the configured DVNs/oracle-relayer set; a compromise, collusion, or misconfiguration in that verification layer is the central trust assumption and a recognised systemic concern for LayerZero-based bridges.
- **Pooled-liquidity exposure & [[smart-contract-risk]]** — Unified pools concentrate large amounts of capital in a small set of contracts. A bug or exploit in the pool/router contracts could drain LP funds across chains simultaneously.
- **Liquidity imbalance risk** — Heavy one-directional flow can deplete a destination-chain pool, causing fees to spike or transfers to be rationed; LPs can be left holding the less-demanded side.
- **Governance / admin & upgrade risk** — Upgradeable contracts and DAO/admin controls are an attack surface; a malicious upgrade or compromised key is a classic bridge failure mode.
- **Supply / emissions overhang** — Circulating supply is far below max supply; future emissions and unlocks are a persistent structural source of sell pressure independent of protocol performance.
- **Sector & price risk** — The -17% weekly drop highlights that bridge governance tokens are highly volatile and sensitive to volume cycles and security sentiment.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed. The token's sharp -17.07% weekly drawdown as of 2026-06-22 is noted under market data.*

---

## Trading Profile

**Venues & liquidity.** STG is a genuine two-venue market: it trades on **Binance** (STG/USDT spot plus a **USD-margined perpetual**) and on **Hyperliquid** as **STG-PERP** (leverage up to roughly **40-50x**). Having both a deep CEX order book and an on-chain perp gives the asset real, liquid depth for a sub-$30M-cap token and makes two-legged execution (spot-vs-perp, or CEX-perp-vs-HL-perp) practical rather than theoretical. Because STG is still a small-cap, the Hyperliquid book thins out quickly on size and funding can swing hard when directional flow crowds in — so position sizing should respect L2 depth on both venues, and large clips are best worked across both books rather than swept on one. The dual availability is the main structural advantage: it lets funding and basis dislocations between Binance and Hyperliquid be arbitraged, and lets you route/net exposure to the venue with better depth at any moment.

**Applicable strategies:**
- [[funding-rate-harvest]] — a liquid two-venue STG-PERP lets you collect funding when the perp trades at a persistent premium/discount to spot, delta-hedged against the Binance spot leg.
- [[hl-vs-cex-funding-divergence]] — STG runs perps on both Hyperliquid and Binance, so funding rates on the two venues can diverge and be captured directly (long the cheaper-funded leg, short the richer one).
- [[cash-and-carry]] — with Binance spot plus a USD-margined perp, STG supports a clean carry trade: hold spot, short the perp, and harvest the basis/funding on a small-cap where the spread can run wide.
- [[crowded-long-funding-fade]] — STG's low float and narrative-driven pumps produce crowded longs and richly positive funding; fading that crowding is a repeatable setup on this token.
- [[token-unlock-supply-event]] — circulating supply sits far below the 1B max, so emissions/unlock events are a recurring, tradable supply-shock catalyst for STG.
- [[liquidation-cascade-fade]] — thin small-cap depth plus up-to-50x leverage on STG-PERP makes liquidation cascades sharp and self-reversing, a classic fade opportunity.

**Volatility & regime character.** STG is a **small-cap DeFi / cross-chain-bridge infrastructure token** with high-beta-alt behavior: it amplifies BTC/ETH moves on the downside (note the -17% weekly drawdown during the bear regime) and is additionally driven by its own idiosyncratic factors — bridge-sector sentiment, LayerZero-ecosystem news, and real bridging volume. Directional beta to BTC/ETH is high in risk-off tape, but the low float and DeFi-narrative sensitivity give it a large idiosyncratic, reflexive component that can decouple from majors on protocol-specific catalysts.

**Risk flags:**
- **Liquidity / venue concentration** — most tradable depth sits on Binance and Hyperliquid; on a sub-$30M-cap token, thin books mean slippage and gap risk on size, and a single-venue outage or delisting would materially impair exits.
- **Token unlocks / emissions** — circulating supply is far below max supply; scheduled emissions and unlocks are a structural, recurring source of sell pressure independent of protocol performance.
- **Narrative dependence** — price is tightly coupled to bridge-sector sentiment and the LayerZero ecosystem; a hack elsewhere in bridges or negative LayerZero news can hit STG regardless of fundamentals.
- **Perp funding dislocations** — low float plus high leverage on STG-PERP make funding volatile; crowded positioning can drive extreme funding and force liquidation cascades that whipsaw both venues.
- **Protocol / bridge tail risk** — as a bridge governance token, STG carries the sector's smart-contract and verifier-trust exploit risk, which can produce sudden, gap-down repricing that no funding or basis hedge fully protects.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=STG` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=STG` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=STG&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=STG&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=STG"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[cross-chain-bridge]]
- [[layerzero]]
- [[smart-contract-risk]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical market-data snapshot
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear)
- General market knowledge; no specific narrative wiki source ingested yet for protocol mechanism.
