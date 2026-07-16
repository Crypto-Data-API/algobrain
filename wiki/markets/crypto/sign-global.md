---
title: "Sign"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, ethereum, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi]
aliases: ["EthSign", "SIGN", "Sign Global", "Sign Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://sign.global/"
related: ["[[attestation]]", "[[base]]", "[[crypto-markets]]", "[[ethereum]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# Sign

**Sign** (SIGN), formerly known as **EthSign**, is an on-chain **[[attestation]]** and token-distribution project. Its product suite spans **Sign Protocol** — an omni-chain attestation layer for making and verifying verifiable claims on-chain — and **TokenTable**, a widely used platform for token-distribution events such as airdrops and vesting. SIGN is the native token of the Sign ecosystem.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, SIGN trades at **$0.00932647**, ranking **#774** by market capitalization with a market cap of **$22,250,101**. It is down **-1.19% over 24h** but up **+3.83% over 7 days** — modestly outperforming on the week despite the broader "Extreme Fear" backdrop (Bitcoin ~$64,508; Fear & Greed Index 21).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SIGN |
| **Market Cap Rank** | #774 |
| **Market Cap** | $22,250,101 |
| **Current Price** | $0.00932647 |
| **24h / 7d Change** | -1.19% / +3.83% |
| **Former Name** | EthSign |
| **Core Products** | Sign Protocol (attestation), TokenTable (token distribution) |
| **Categories** | Analytics, BNB Chain Ecosystem, Ethereum Ecosystem, Zero Knowledge (ZK), Base Ecosystem, Binance HODLer Airdrops |
| **Website** | [https://sign.global/](https://sign.global/) |

> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot); price/rank/cap above updated 2026-06-22.*

---

## Overview

Sign began as **EthSign**, a decentralized e-signature / agreement tool, and grew into a broader infrastructure brand for **verifiable claims and token distribution** across multiple chains.

### Sign Protocol (attestation)

Sign Protocol is an **omni-chain [[attestation]] protocol**: a standardized way to create, store, and verify "attestations" — signed, structured statements that something is true (e.g. "this wallet completed KYC," "this address is on an allowlist," "this user holds credential X"). Attestations are a foundational primitive for on-chain identity, reputation, credentials, allowlisting, and compliance. By being omni-chain, Sign Protocol aims to let an attestation made on one network be referenced or verified on others, rather than being siloed per chain.

**How attestations work.** An attestation is built from three pieces: a **schema** (the structure of the claim — what fields it contains), the **attestation data** (the actual values, signed by an issuer), and a **verification path** (how a consumer checks the claim is valid and unrevoked). Attestations can be **revocable** (so a credential can be withdrawn) and can be made **off-chain or on-chain** depending on cost/privacy needs, with **Zero-Knowledge ([[zero-knowledge-proofs|ZK]])** options to prove a claim is true without revealing the underlying data (e.g. prove "over 18" without exposing a birthdate). This makes the protocol a building block for [[decentralized-identity|decentralized identity]], reputation, Sybil-resistance, allowlists, and on-chain compliance.

Sign Protocol competes most directly with **[[ethereum-attestation-service|Ethereum Attestation Service (EAS)]]**, the best-known attestation standard. Sign's pitch is **omni-chain reach plus a productized distribution layer (TokenTable)** rather than a bare standard, aiming to bundle the primitive with real demand.

### TokenTable (token distribution)

TokenTable is Sign's token-distribution engine, used by projects to run **airdrops, vesting schedules, and other token-unlock events** at scale. Because claims, vesting cliffs, and linear unlocks are enforced by audited smart contracts, projects use TokenTable to distribute large volumes of tokens trustlessly rather than building bespoke claim portals. This is the source of much of Sign's real-world traction and visibility within the airdrop/distribution niche, and it pairs naturally with attestations (e.g. gating an airdrop claim on an on-chain attestation that the wallet is eligible / not a Sybil).

### Token role, value accrual & governance

The **SIGN** token is the native asset of the Sign ecosystem. It is associated with ecosystem participation and incentives (including Binance HODLer Airdrops, per its category tags) and is listed on major venues including Binance, Upbit, Bitget, and KuCoin. With circulating supply far below total/max supply (per the tokenomics table below), future unlocks are a material consideration — the low market-cap-to-FDV ratio signals significant supply still to enter circulation.

**Value-accrual caveat:** Sign's two products are genuinely used, but — as with most infrastructure tokens — **product usage does not automatically require the SIGN token**. Attestations can be created and TokenTable distributions can run without holders necessarily spending SIGN, so the durable accrual question is whether fees, staking, or access mechanics are wired to force SIGN demand, versus the token being primarily an incentive/governance asset riding the brand. **Governance** is the clearest role today: SIGN coordinates ecosystem incentives and protocol direction. The split between **strong product traction** and **uncertain token capture** is the central investment tension.

### Competitive comparison

| Project | Token | Category | Differentiator | Risk |
|---|---|---|---|---|
| **Sign (Sign Protocol + TokenTable)** | SIGN | Omni-chain attestations **+ token distribution** | Bundles the primitive with a high-usage distribution product; ZK + omni-chain | Token-vs-product value capture; unlock overhang |
| [[ethereum-attestation-service\|EAS]] | — (no token) | Attestation standard | First-mover, neutral standard, broad adoption | Tokenless — competes on being the default, not on a token |
| **Gitcoin Passport / Human Passport** | — | Sybil-resistance / identity scoring | Aggregated identity "stamps" | Narrower (Sybil-scoring) vs. general attestations |
| **Galxe (credential graph)** | GAL | On-chain credentials + campaigns | Large campaign/quest distribution | Overlaps on distribution; different credential model |

Sign's edge is **bundling** — pairing a general attestation layer with TokenTable's real distribution demand — in a field where the incumbent standard (EAS) has no token and identity competitors (Passport, Galxe) attack adjacent slices.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.64B SIGN |
| **Total Supply** | 10.00B SIGN |
| **Max Supply** | 10.00B SIGN |
| **Fully Diluted Valuation** | $318.94M |
| **Market Cap / FDV Ratio** | 0.16 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1311 (2025-09-24) |
| **Current vs ATH** | -75.57% |
| **All-Time Low** | $0.0207 (2026-02-27) |
| **Current vs ATL** | +54.54% |
| **24h Change** | +1.90% |
| **7d Change** | +0.55% |
| **30d Change** | -40.34% |
| **1y Change** | +0.00% |

> *Note: the 24h/7d figures in this table are from a retained earlier snapshot; the current 2026-06-22 values in [[#Key Facts]] (24h -1.19%; 7d +3.83%) supersede them. The ATH/ATL dates and the -40% 30-day drop are the durable takeaways: SIGN is a 2025-vintage, high-beta token trading ~76% below its Sept-2025 ATH.*

---

## History & Timeline

> Only well-established dates are listed; uncertain dates are kept qualitative.

- **EthSign era** — the project launches as **EthSign**, a decentralized e-signature / on-chain agreement tool, before broadening into attestations and token distribution.
- **Rebrand to Sign** — EthSign expands into **Sign Protocol** (omni-chain attestations) and **TokenTable** (token distribution), consolidating under the "Sign" brand at `sign.global`.
- **2025** — SIGN is distributed via **Binance HODLer Airdrops** and lists on major venues (Binance, Upbit, Bitget, KuCoin).
- **2025-09** — SIGN reaches its **all-time high of ~$0.1311 (2025-09-24)**.
- **2026-02** — SIGN prints its **all-time low of ~$0.0207 (2026-02-27)** amid the broad market downturn.

---

## Narrative, Category & Catalysts

SIGN sits across **on-chain identity/attestation** and **airdrop/distribution infrastructure**, with [[zero-knowledge-proofs|ZK]] and multi-chain ([[ethereum|Ethereum]], [[base|Base]], [[bnb|BNB Chain]]) tags:

- **Decentralized identity / [[attestation]]** — exposure to the DID, reputation, and Sybil-resistance themes; re-rates when on-chain-identity narratives are in favor.
- **Airdrop / token-distribution tooling** — TokenTable benefits structurally from active airdrop seasons; more launches → more usage and visibility.
- **Binance ecosystem** — the HODLer-airdrop origin and Binance listing give it CEX distribution and retail reach.

**Catalysts:** a high-profile airdrop run through TokenTable; major-protocol adoption of Sign attestations; ZK-attestation/identity narrative revival; favorable token-unlock schedule or buyback/utility upgrades. **Anti-catalysts:** large scheduled unlocks (low MC/FDV), airdrop-season lulls, and competition from the tokenless EAS standard.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x868fced65edbf0056c4163515dd840e9f287a4c3` |
| Base | `0x868fced65edbf0056c4163515dd840e9f287a4c3` |
| Binance Smart Chain | `0x868fced65edbf0056c4163515dd840e9f287a4c3` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SIGN/USDT | N/A |
| Upbit | SIGN/KRW | N/A |
| Bitget | SIGN/USDT | N/A |
| KuCoin | SIGN/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://sign.global/](https://sign.global/) |
| **Twitter** | [@ethsign](https://twitter.com/ethsign) |
| **Whitepaper** | [https://docs.sign.global/](https://docs.sign.global/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $18.67M |
| **Market Cap Rank** | #827 |
| **24h Range** | $0.0311 — $0.0325 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

> *The rank, range, and volume in this table are from the retained earlier snapshot; current price/rank/cap are in [[#Key Facts]] (2026-06-22). Preserved for history.*

**How & where it trades:** SIGN's primary liquidity is on **Binance (SIGN/USDT)** — a major advantage versus most micro-caps — with strong Korean flow via **Upbit (SIGN/KRW)** and additional coverage on Bitget and KuCoin. The Binance + Upbit pairing gives it meaningful dollar and won depth for a ~$22M cap, but also exposes it to Korean-sentiment spikes and a basis between venues. With a **low MC/FDV (~0.16)**, scheduled unlocks are the dominant structural overhang on the order book, so liquidity needs to be read alongside the vesting calendar.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *See [[#History & Timeline]] for dated milestones. Further notable events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **Token-unlock / dilution risk:** A low circulating-to-total supply ratio means substantial future unlocks; new supply can pressure price as it enters circulation.
- **Adoption dependency:** Sign's value rests on continued usage of Sign Protocol attestations and TokenTable distributions; in a competitive infra market, attestation/airdrop tooling can be substituted.
- **Token-vs-product value capture:** As with many infrastructure tokens, it is not guaranteed that protocol/product usage translates into demand for the SIGN token.
- **Market and liquidity risk:** Small-cap (~$22.3M), high-beta altcoin; price is volatile and sensitive to broad crypto sentiment.

> *This is informational, not financial advice.*

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: as of 2026-06-22 the market is in an established **bear market**, Fear & Greed **21 (Extreme Fear)**, market-health 30/100; BTC ~$64.2k (~16% below its 200-day MA). SIGN is a 2025-vintage, low-float, high-beta token. Informational, not financial advice.

- **Unlock calendar over chart.** With MC/FDV ≈ 0.16, the single biggest driver is the **vesting/unlock schedule**: large cliffs in a bear tape reliably pressure price. Map upcoming unlocks before taking any swing position; treat pre-unlock strength with suspicion.
- **Liquidity is a genuine edge here.** Binance + Upbit depth means SIGN is more exitable than typical micro-caps — useful for defined-risk trades, but it also makes SIGN a momentum/perp playground prone to sharp squeezes.
- **Catalyst-gated longs.** Upside needs a real trigger — a marquee TokenTable airdrop, a major Sign-Protocol adoption, or an identity/ZK-narrative turn — confirmed by volume. Don't pre-empt the regime.
- **Respect the downtrend.** ~76% below ATH and -40% over 30 days signal an entrenched downtrend; favor small size, hard invalidation below recent range lows, and avoid leverage into unlock events.

---

## Trading Profile

### Venues & liquidity

SIGN is tradable on **[[binance]]** — both **spot (SIGN/USDT)** and a **USD-margined [[perpetual-futures|perpetual]]**, which exposes [[funding-rate|funding]], **[[open-interest]]**, and **[[liquidations]]** data. It is **not listed on Hyperliquid**, so **Binance is the primary leveraged venue**. Deep Korean flow via Upbit (SIGN/KRW) adds spot depth but no perp. Because leverage and derivatives data concentrate on a single venue, funding/OI/liquidation signals should be read as Binance-specific rather than aggregate; the single-venue perp means squeezes and liquidation cascades are more reflexive, so position sizing must respect that a low-float (~$22M cap, MC/FDV ~0.16) token can move violently on modest perp flow. Spot depth on Binance + Upbit makes SIGN more exitable than typical micro-caps, which favors defined-risk execution and staged entries/exits.

### Applicable strategies

- [[funding-rate-harvest]] — the single Binance perp can run persistently skewed funding on a low-float token, making periodic funding collection viable when spot-hedged.
- [[crowded-long-funding-fade]] — catalyst-driven retail crowding (airdrop/narrative pumps) into a thin float often overheats perp longs; fade extreme positive funding.
- [[liquidation-cascade-fade]] — single-venue leverage on a small-cap makes forced-liquidation flushes overshoot; fade the cascade once liquidation velocity peaks.
- [[cash-and-carry]] — with tradable spot and USD-M perp on the same venue, spot-long/perp-short captures basis and funding without directional risk.
- [[token-unlock-supply-event]] — MC/FDV ~0.16 means large scheduled unlocks are the dominant structural driver; trade the supply-event overhang around vesting cliffs.
- [[breakout-and-retest]] — SIGN trades in extended ranges below its ATH; volume-confirmed breakouts with retest entries suit its high-beta, catalyst-gated moves.

### Volatility & regime character

Small-cap (~$22M), 2025-vintage, high-beta altcoin trading ~76% below its Sept-2025 ATH. It behaves as a reflexive, low-float infra/DeFi token (on-chain identity/attestation + airdrop-distribution tooling) with strong directional beta to BTC/ETH and to broad risk sentiment. Moves are amplified by Korean (Upbit) sentiment spikes and by narrative rotations (ZK/identity, airdrop-season activity). Realized volatility is elevated and event-driven rather than steady.

### Risk flags

- **Venue/liquidity concentration:** perp leverage is Binance-only; a single leveraged venue concentrates funding/OI/liquidation risk and cross-venue basis vs Upbit spot.
- **Unlocks / emissions:** low MC/FDV (~0.16) means substantial future supply; unlock cliffs are the dominant order-book overhang, especially in a bear tape.
- **Narrative dependence:** upside is catalyst-gated (TokenTable airdrops, Sign-Protocol adoption, ZK/identity revival); airdrop-season lulls remove the bid.
- **Token-vs-product value capture:** product usage does not clearly force SIGN demand, a structural risk to durable valuation.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SIGNUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=SIGNUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=SIGN` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=SIGN` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SIGNUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SIGNUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SIGN"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[base]]
- [[bnb]]
- [[attestation]] — the core primitive Sign Protocol provides
- [[ethereum-attestation-service]] — the leading competing attestation standard
- [[decentralized-identity]]
- [[zero-knowledge-proofs]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; market figures as of 2026-06-22 (cryptodataapi.com / CoinGecko). Product descriptions (Sign Protocol, TokenTable, EthSign history) summarized from general knowledge; no specific wiki source ingested yet.
