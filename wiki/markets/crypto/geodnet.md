---
title: "Geodnet"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["GEOD", "GEODNET"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://geodnet.com/"
related: ["[[crypto-markets]]", "[[depin]]", "[[helium]]", "[[polygon]]", "[[solana]]", "[[xyo-network]]"]
---

# Geodnet

**Geodnet** (GEOD) is the token of the Global Earth Observation Decentralized Network (GEODNET), a [[depin|DePIN]] (Decentralized Physical Infrastructure Network) that crowdsources a global, satellite-grade GNSS/RTK correction service. The network's "miners" are GPS reference stations (and Space Weather stations) installed by operators worldwide that stream raw GNSS observations; in exchange they earn GEOD rewards. The token lives primarily on [[polygon]] PoS with a bridged version on [[solana]].

The core product is high-precision positioning: aggregating data from thousands of ground stations lets GEODNET correct raw GNSS (GPS, Galileo, BeiDou, GLONASS) signals down to centimeter-level accuracy and improve timing to the nanosecond. This RTK (Real-Time Kinematic) correction stream is sold to customers in surveying, agriculture, drones, autonomous vehicles, and robotics — the demand side that gives the token a real revenue underpinning.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | GEOD |
| **Price** | $0.199679 |
| **Market Cap** | $89.78M |
| **Market Cap Rank** | #285 |
| **24h Volume** | $168,452 |
| **24h Change** | -3.00% |
| **7d Change** | -11.53% |
| **Fully Diluted Valuation** | ~$199.68M (at 1.00B max supply) |
| **Market Cap / FDV** | ~0.45 |
| **All-Time High** | $0.374342 |
| **All-Time Low** | $0.03417228 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Backdrop: this snapshot lands during an **Established Bear Market** with the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] at **23 (Extreme Fear)**. GEOD was a relative laggard this week (**-11.5% over 7 days**). The 24h volume of ~$168K is extremely thin relative to the ~$89.8M market cap (~0.2% turnover), implying low liquidity and wide effective spreads — small orders can move the price.

---

## Technology & Protocol

GEODNET is a **physical-sensor [[depin|DePIN]]** built around RTK GNSS correction:

- **Miners (reference stations)** — operators buy and install GEODNET "Satellite Mining Stations" (multi-constellation GNSS receivers) that continuously stream raw observations to the network and earn GEOD.
- **Space Weather stations** — a secondary sensor class capturing ionospheric/atmospheric data that improves correction quality and feeds space-weather products.
- **RTK correction network** — by triangulating raw signals from thousands of geographically distributed stations, GEODNET computes **centimeter-level positioning** corrections (and nanosecond-grade timing) far cheaper than building proprietary base-station networks the way incumbents (Trimble, Hexagon) do.
- **Service delivery** — the correction stream is sold to enterprise customers in **surveying, precision agriculture, drones/UAVs, autonomous vehicles, and robotics**; service fees are the real-world revenue that is meant to flow back to the token.

This is the classic DePIN model: token emissions bootstrap a physical network whose output is a sellable, real-economy data service.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~449.63M GEOD |
| **Total Supply** | ~964.66M GEOD |
| **Max Supply** | 1.00B GEOD |
| **Circulating / Max** | ~45.0% |
| **Market Cap / FDV** | ~0.45 |

About 45% of the maximum supply is in circulation, so roughly 55% remains to be emitted — predominantly as ongoing **mining rewards paid to station operators** plus team/ecosystem allocations. This is the canonical DePIN economic loop: token emissions subsidize hardware deployment, growing network coverage; coverage attracts paying RTK customers; customer revenue (and, where implemented, token buy/burn from service fees) is meant to offset emission-driven dilution. The MC/FDV ratio of ~0.45 quantifies the forward-dilution overhang the market is pricing in.

---

## Market Structure & Derivatives

- **Spot venues:** GEOD trades on a mix of centralized and decentralized markets. On-chain liquidity is concentrated in DEX pools on [[solana]] (e.g. Orca) and [[polygon]] PoS, with centralized listings on tier-2 exchanges. Given the ~$168K daily volume in this snapshot, depth is shallow.
- **Derivatives / perps:** GEOD is **not** a major perpetual-futures listing — there is no liquid [[hyperliquid|Hyperliquid]] or top-CEX perp market for it, so funding-rate and open-interest data are not meaningfully available. Traders are effectively limited to spot exposure.
- **Liquidity caveat:** with rank #285 and very thin volume, GEOD behaves like a small-cap altcoin — execution risk and slippage are material.

---

## Use Case, Narrative & Category

GEODNET sits in the **[[depin|DePIN]]** sector, specifically the "physical/sensor network" subcategory alongside peers like [[xyo-network]] and [[helium]]. CoinGecko categorizes it under DePIN, Robotics, and Solana/Polygon ecosystems, and it is associated with the **Pantera Capital** portfolio.

The investment thesis rests on **hardware-network economics**: rather than the capital-intensive model of incumbent RTK providers (Trimble, Hexagon) building their own base-station networks, GEODNET pushes deployment costs onto independent operators who are compensated in GEOD. If real-world RTK demand (precision agriculture, drone delivery, autonomous machinery, surveying) scales, service fees can flow back to the token, decoupling price from pure speculation. The bear case is that emissions outrun paying-customer revenue, leaving the token reliant on subsidy.

---

## Valuation Framing

- **Revenue-vs-emissions** — the central GEOD question is whether annualized RTK service revenue is growing faster than token emissions; a DePIN that "sells" more correction service than it pays out in rewards is on a path to sustainability.
- **Coverage / station-count proxy** — value scales with the number and geographic density of active stations (more coverage = more sellable, higher-quality corrections); network growth is a leading indicator.
- **Incumbent-displacement TAM** — framed against the multi-billion-dollar commercial GNSS-correction market (Trimble/Hexagon), GEODNET's ~$90M cap is a small bet on capturing a slice via a cheaper crowd-sourced supply side.

---

## Peer Comparison

| Token | DePIN subcategory | Mkt Cap | Rank | MC/FDV | 7d | Note |
|---|---|---|---|---|---|---|
| **GEOD** | RTK / GNSS positioning | $90M | #285 | 0.45 | -11.5% | Real RTK revenue; very thin liquidity |
| [[helium]] (HNT) | Wireless / IoT + 5G | — | — | — | — | Largest sensor-DePIN precedent |
| [[xyo-network]] (XYO) | Location / geospatial | — | — | — | — | Geospatial data network |

---

## Notable History

- **All-Time High:** $0.374342 — current price is ~47% below ATH.
- **All-Time Low:** $0.03417228 — current price is ~5.8x above ATL.
- GEOD has held up better than much of the broader DePIN cohort over its lifetime: its drawdown from ATH (~-47%) is shallower than peers that fell ~90%+ from their highs, reflecting a comparatively healthier revenue narrative and a later/lower ATH — though the most recent week (-11.5%) shows it is not immune to risk-off pressure.

---

## Risks

- **Liquidity risk:** extremely thin 24h volume (~$168K) for an ~$89.8M-cap token; entering or exiting size is difficult without slippage.
- **Emission/dilution risk:** ~55% of max supply still to be released, much of it as mining rewards — sustained sell pressure from operators monetizing rewards.
- **Demand-side execution risk:** the thesis requires real RTK revenue to outgrow emissions; competition from entrenched commercial GNSS-correction providers (Trimble, Hexagon) is significant.
- **Hardware/operational dependence:** network value is tied to physical station deployment, geographic coverage, and operator retention.
- **Macro/sentiment risk:** snapshot taken during an Established Bear Market with Extreme Fear (F&G 23); small-cap DePIN tokens are high-beta to risk-off conditions.
- **Multi-chain/bridge risk:** token exists on both [[polygon]] and [[solana]], introducing bridge and contract-surface considerations.

---

## Related

- [[depin]] — GEODNET's core category
- [[crypto-markets]]
- [[polygon]] — primary token chain
- [[solana]] — bridged deployment
- [[xyo-network]] — geospatial DePIN peer
- [[helium]] — sensor-DePIN precedent

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## See Also

- [[crypto-markets]]
- [[polygon]]

---
