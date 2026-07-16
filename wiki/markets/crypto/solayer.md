---
title: "Solayer"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, nft, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["LAYER", "sSOL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://solayer.org/network"
related: ["[[crypto-markets]]", "[[depeg]]", "[[eigenlayer]]", "[[ethereum]]", "[[liquid-restaking]]", "[[liquid-staking]]", "[[restaking]]", "[[slashing]]", "[[smart-contract-risk]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[token-unlock-supply-event]]"]
---

# Solayer

**Solayer** (LAYER) is a [[restaking]] protocol built on [[solana]]. It lets users restake SOL or Solana liquid-staking tokens to extend Solana's economic security to additional applications and infrastructure ("AVS"-style services), issuing the **sSOL** restaking token to depositors. Solayer is also developing **InfiniSVM**, a hardware-accelerated, RDMA-based execution environment aiming for very high throughput — but the protocol's core, token-relevant function today is Solana restaking and the yield/security it coordinates.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, LAYER trades at **$0.066789**, ranked **#989** by market capitalization with a market cap of **$14,031,378** (24h **+0.84%**, 7d **-0.72%**), in an "Extreme Fear" market regime (Fear & Greed Index **21**). LAYER is among the smallest-cap names in this cohort and sits roughly 98% below its 2025 all-time high, reflecting both the risk-off regime and a large unlocked-supply overhang (circulating is a small fraction of max supply).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LAYER |
| **Market Cap Rank** | #989 |
| **Market Cap** | $14,031,378 |
| **Current Price** | $0.066789 |
| **24h / 7d Change** | +0.84% / -0.72% |
| **Categories** | Decentralized Finance (DeFi), Solana Ecosystem, LSDFi, Restaking, Stablecoin Issuer, YZi Labs (Prev. Binance Labs) Portfolio, Binance HODLer Airdrops, Polychain Capital Portfolio, Buidlpad Launchpad |
| **Website** | [https://solayer.org/network](https://solayer.org/network) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Solayer brings the [[restaking]] model — pioneered on Ethereum by [[eigenlayer]] — to the [[solana]] ecosystem. Users stake or restake SOL (and Solana LSTs) to provide pooled economic security and earn layered rewards, receiving **sSOL** as the [[liquid-restaking]] representation of their position. This lets capital simultaneously earn Solana staking yield and additional restaking incentives while remaining liquid and composable across Solana DeFi.

Solayer is also building **InfiniSVM**, a next-generation, hardware-accelerated execution environment that leverages InfiniBand RDMA for near-microsecond inter-node communication and aggressive concurrency control, with stated targets of very high throughput (1M+ TPS) and large network bandwidth. InfiniSVM is the protocol's longer-term performance ambition; the restaking layer is what underpins the LAYER token economy today.

---

## How Solayer Works

**Restaking on Solana:**

1. A user deposits SOL or a Solana liquid-staking token. The underlying SOL earns base [[solana]] staking rewards.
2. The position is restaked through Solayer to extend Solana's stake-based security to additional services and applications, in the [[restaking]] tradition.
3. The user holds **sSOL**, a yield-bearing [[liquid-restaking]] token usable across Solana DeFi.

**What the LAYER token does:**

- **Governance** — LAYER governs protocol parameters, supported services, and treasury decisions.
- **Incentives / coordination** — LAYER is used to reward restakers and align participants in Solayer's restaking and InfiniSVM roadmap.
- LAYER is the protocol/governance token and is separate from sSOL (the yield-bearing restaking asset). LAYER does not itself accrue SOL staking yield.

**How yield is generated:** sSOL yield combines base Solana staking rewards with restaking incentives. As with all restaking, the *extra* yield depends on real demand for the security Solayer provides; emissions-funded incentives are not the same as sustainable fee-based yield, and should be assessed critically.

**Endogenous AVS / "delegated staking."** Solayer's restaking is designed to secure additional services (validators, oracles, bridges, app-specific infrastructure) by extending Solana's stake-weighted security to them — the Solana analogue of [[eigenlayer|EigenLayer]]'s Actively Validated Services (AVS) model. Where EigenLayer reuses Ethereum stake, Solayer reuses Solana stake, inheriting Solana's faster finality and lower fees but also its younger restaking tooling and shorter security track record.

---

## InfiniSVM: the high-performance execution roadmap

InfiniSVM is Solayer's longer-term, hardware-accelerated execution environment and the protocol's most ambitious bet:

- **Hardware acceleration / RDMA.** It targets near-microsecond inter-node communication over InfiniBand RDMA, with aggressive concurrency control, aiming at headline throughput figures (stated targets of 1M+ TPS and very high bandwidth).
- **SVM compatibility.** It is positioned as an SVM (Solana Virtual Machine) execution layer, so existing Solana programs and tooling can target it.
- **Relationship to the token economy.** InfiniSVM is the *narrative* and growth engine; the restaking layer and sSOL are what underpin LAYER's economics today. The high-performance claims are unproven at production scale and should be treated as roadmap, not delivered fact.

This pairing — a restaking security layer plus a high-throughput chain that could itself become a major consumer of that security — is the strategic logic behind Solayer combining the two products under one token.

---

## Comparison vs Other Restaking Protocols

[[restaking|Restaking]] is dominated on Ethereum by [[eigenlayer|EigenLayer]] and its liquid-restaking front-ends (Ether.fi, Renzo, Kelp). Solayer is the most prominent Solana-native entrant. The category's core question is whether *reused* security commands sustainable, fee-based demand or merely subsidized emissions.

| Protocol | Base chain | Restaking token | AVS / service model | Distinguishing feature |
|---|---|---|---|---|
| **Solayer** | [[solana\|Solana]] | sSOL | Solana-native delegated security | Pairs restaking with the InfiniSVM high-throughput chain |
| **EigenLayer** | [[ethereum\|Ethereum]] | (restaked ETH / LSTs) | AVS marketplace (the original model) | Largest restaking TVL; defined the category |
| **Ether.fi** | Ethereum | eETH / weETH | LRT on top of EigenLayer | Leading liquid-restaking token by adoption |
| **Renzo** | Ethereum | ezETH | LRT on top of EigenLayer | Suffered an ezETH [[depeg]] in April 2024 (cautionary case) |
| **Jito (restaking)** | Solana | (JitoSOL + restaking) | Solana restaking + MEV/liquid staking | Dominant Solana LST; MEV-tipped yield |

Solayer's edge versus other Solana restakers (e.g., Jito's restaking, Picasso) is its tight coupling to InfiniSVM; its disadvantage is that Solana restaking as a whole is younger and less battle-tested than Ethereum's, and Solayer competes for the same SOL deposits as the entrenched JitoSOL LST.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 210.00M LAYER |
| **Total Supply** | 1.00B LAYER |
| **Max Supply** | 1.00B LAYER |
| **Fully Diluted Valuation** | $80.67M |
| **Market Cap / FDV Ratio** | 0.21 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.39 (2025-05-05) |
| **Current vs ATH** | -97.63% |
| **All-Time Low** | $0.0729 (2026-02-06) |
| **Current vs ATL** | +10.46% |
| **24h Change** | -4.37% |
| **7d Change** | +0.80% |
| **30d Change** | +1.81% |
| **1y Change** | -94.10% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `LAYER4xPpTCb3QL8S9u41EAhAX7mhBn8Q6xMTwY2Yzc` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LAYER/USDT | N/A |
| Kraken | LAYER/USD | N/A |
| Upbit | LAYER/KRW | N/A |
| Bitget | LAYER/USDT | N/A |
| Crypto.com Exchange | LAYER/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | LAYER-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://solayer.org/network](https://solayer.org/network) |
| **Twitter** | [@solayer_labs](https://twitter.com/solayer_labs) |
| **Telegram** | [solayer_discussion](https://t.me/solayer_discussion) (9,027 members) |
| **Discord** | [https://discord.gg/solayerlabs](https://discord.gg/solayerlabs) |
| **GitHub** | [https://github.com/solayer-labs](https://github.com/solayer-labs) |
| **Whitepaper** | [https://whitepaper-101797961016.us-central1.run.app/variants/solayer_infinisvm_737.pdf](https://whitepaper-101797961016.us-central1.run.app/variants/solayer_infinisvm_737.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.60M |
| **Market Cap Rank** | #994 |
| **24h Range** | $0.0804 — $0.0847 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-04-09 |

---

## Risks

- **sSOL [[depeg]] risk** — Like any [[liquid-restaking]] token, sSOL can trade below its underlying redemption value in secondary markets during stress or thin liquidity, with knock-on liquidations for leveraged holders.
- **[[restaking]] / [[slashing]] risk** — Restaked SOL backs additional services; misbehavior or restaking-layer faults can lead to penalties on the underlying stake. The restaking-on-Solana security model is younger and less battle-tested than Ethereum's.
- **[[smart-contract-risk]]** — Solayer's restaking, sSOL, and InfiniSVM-related contracts/programs are complex and relatively new; a bug could endanger deposits.
- **Supply overhang / unlock pressure** — Circulating LAYER is a small fraction of the 1B max supply (Mcap/FDV ~0.2 in earlier snapshots). Future token unlocks are a structural headwind for price.
- **Roadmap execution risk** — InfiniSVM's high-performance claims (1M+ TPS) are ambitious and unproven at scale; failure to deliver could undercut the token's narrative.
- **Competitive / TVL risk** — Solayer competes for Solana stake against the entrenched JitoSOL [[liquid-staking]] token and other [[restaking]] entrants; restaking demand may concentrate with incumbents.
- **Reflexive-yield risk** — much of sSOL's *extra* yield is incentive-funded. If LAYER emissions value falls, restaking demand can unwind, similar in shape to other reflexive [[defi|DeFi]] flywheels.
- **Governance / dependence on Solana** — LAYER value depends on Solana network health, congestion, and uptime; Solana outages historically propagate to its DeFi ecosystem.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

**Venues & liquidity.** LAYER trades on **both** [[hyperliquid|Hyperliquid]] (LAYER-PERP, up to ~40-50x leverage) and [[binance|Binance]] (spot LAYER/USDT plus a USD-margined perpetual). This is a genuine two-venue market rather than a single-DEX listing, so there is centralized spot for basis/carry construction and derivatives depth on both a major CEX and the leading on-chain perp DEX. Practically, that dual availability tightens quotes and supports cross-venue and spot-vs-perp structures — but note LAYER is a very small-cap name (rank ~998), so aggregate depth is still thin: size positions to the order-book depth, expect slippage on larger clips, and treat headline max leverage as a hard ceiling, not a target.

**Applicable strategies.**
- [[funding-rate-harvest]] — collect perp funding on LAYER across two liquid venues; a small-cap alt perp often carries persistent funding to harvest while delta-hedged.
- [[hl-vs-cex-funding-divergence]] — LAYER runs on both Hyperliquid and Binance, so funding can diverge between the two perps and be captured with an offsetting position.
- [[cash-and-carry]] — buy Binance spot LAYER and short the perp to lock the basis, using centralized spot that pure-DEX listings lack.
- [[crypto-spot-perp-futures-triangle]] — combine Binance spot, the Binance perp, and the Hyperliquid perp into a three-legged relative-value structure across venues.
- [[token-unlock-supply-event]] — LAYER has a large locked-supply overhang (Mcap/FDV ~0.2), so scheduled unlocks are tradable, recurring supply catalysts.
- [[liquidation-cascade-fade]] — thin small-cap depth plus high perp leverage makes LAYER prone to sharp liquidation wicks that mean-revert, offering fade setups.

**Volatility & regime character.** LAYER is a small-cap, high-beta [[defi]]/infrastructure (Solana [[restaking]]) altcoin: it behaves reflexively, amplifying broad-market moves on the way up and down, and is highly sensitive to Solana-ecosystem risk appetite and its own emissions/unlock narrative. Correlation to BTC/ETH beta is high in direction but with a much larger amplitude — it tends to overshoot majors in both directions, and its dominant idiosyncratic driver is the restaking/InfiniSVM narrative rather than macro alone.

**Risk flags.**
- **Liquidity / venue concentration** — despite two venues, absolute depth is small (rank ~998); large orders move price and can gap through stops.
- **Token unlocks / emissions** — circulating LAYER is a small fraction of the 1B max supply; unlock schedules and incentive emissions are a persistent supply headwind and a funding/price catalyst.
- **Narrative dependence** — valuation leans on unproven InfiniSVM performance claims and Solana-restaking demand; narrative reversals hit price hard.
- **Perp funding dislocations** — a low-float, high-leverage small-cap can see funding spike and flip abruptly, punishing crowded carry positions.
- **Depeg-adjacent risk** — sSOL redemption stress or Solana-ecosystem shocks can feed back into LAYER sentiment and liquidity.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=LAYER` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=LAYER` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=LAYER&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=LAYER&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=LAYER"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]
- [[restaking]]
- [[liquid-restaking]]
- [[liquid-staking]]
- [[depeg]]
- [[smart-contract-risk]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical market-data snapshot
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear)
- General market knowledge; no specific narrative wiki source ingested yet for protocol mechanism.
