---
title: "TempleDAO"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["TEMPLE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.templedao.link/rituals"
related: ["[[crypto-markets]]", "[[decentralized-finance]]", "[[ethereum]]", "[[real-world-assets]]"]
---

# TempleDAO

**TempleDAO** (TEMPLE) is an [[ethereum|Ethereum]]-based DeFi protocol and DAO whose token is backed by a managed **treasury**. It was built around mechanics aimed at "stable wealth creation" — an intrinsic-value floor, treasury-backed rewards, price-defence incentives, and an exit queue — positioning TEMPLE as a treasury-/yield-backed token rather than a pure governance coin.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | TEMPLE |
| **Chain** | Ethereum |
| **Current Price** | $3.00 |
| **Market Cap** | $71,143,582 |
| **Market Cap Rank** | #352 |
| **24h Volume** | $1,836 |
| **7d Change** | 0.00% |
| **Fully Diluted Valuation** | $71,285,381 |
| **All-Time High** | $4.11 (2025-11-21) |
| **All-Time Low** | $0.186329 (2023-03-19) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Trading context: the market is in **extreme fear** (Fear & Greed = 22) within an **established bear market** as of 2026-06-20. TEMPLE shows extremely thin turnover (~$1.8K/24h) and a flat 7-day move, consistent with a low-float, treasury-backed token whose price hugs its intrinsic backing rather than trading actively. (A 24h percentage change was not reported in the source snapshot and is therefore omitted.)

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~23.72M TEMPLE |
| **Total Supply** | ~23.77M TEMPLE |
| **Max Supply** | Uncapped (treasury-mechanics driven) |
| **Market Cap / FDV** | 1.00 |

Circulating ≈ total supply (MC/FDV = 1.00), so there is effectively no unvested overhang. The token's distinguishing feature is **treasury backing**: a managed protocol treasury underpins an intrinsic value (IV) floor, and historic mechanics ("safe mint," IV-backed rewards, "safe harvest," price-defence incentives, and an exit queue) were designed to keep the market price anchored to — and defend it near — treasury value. Because price tracks backing, MC and FDV converge.

**Why MC/FDV = 1.00 matters.** Most tokens in this set carry severe low-float / high-FDV unlock overhangs (see [[wefi]], [[lab]], [[token-unlocks]]). TEMPLE is the structural opposite: supply is effectively fully circulating, so there is no hidden dilution waiting to dump on holders. The trade-off is that the upside is capped by treasury growth rather than by reflexive speculative re-rating — this is a "floor asset," not a moonshot.

---

## Value Accrual & Governance

- **Value accrual = treasury growth, not emissions.** Unlike inflationary reward tokens, TEMPLE's holder value is meant to come from the **protocol treasury compounding** — protocol-owned assets are deployed into yield strategies and DeFi positions, and the per-token intrinsic-value (IV) floor rises as backing grows. "Rituals" (staking/reward flows) distribute treasury-sourced yield rather than printing new supply.
- **Floor mechanics.** The IV floor, price-defence incentives, and exit queue together aim to keep market price anchored to backing — a deliberate contrast to free-floating governance tokens whose price is set purely by speculation.
- **Governance.** TEMPLE is a **DAO** token: holders govern treasury strategy, mechanic parameters, and product direction. Because the entire thesis rests on treasury management, governance quality (who controls the treasury, how it is deployed, multisig/contract security) is the load-bearing variable — more so than for a typical app token.

---

## How & Where It Trades

### Protocol mechanics (the venue itself)
TempleDAO's economics revolve around its **treasury** rather than an order book:

- **Treasury backing / intrinsic value** — protocol-owned assets back the token at a per-token IV floor; the treasury is actively managed (deployed into yield strategies and DeFi positions) to grow backing over time.
- **Price-defence incentives** — mechanisms designed to support the market price toward IV, discouraging trading far below backing.
- **Exit queue** — redemptions/exits are throttled through a queue rather than instant dumps, smoothing treasury outflows and protecting remaining holders.
- **Treasury-backed rewards / "rituals"** — staking and reward flows ("rituals") distribute treasury-sourced yield to participants rather than relying solely on inflationary emissions.

### Spot venues for the TEMPLE token
- **Decentralized:** Uniswap V3 on Ethereum (TEMPLE/DAI pool — `0x470e…cf1b7` paired with DAI `0x6b17…1d0f`).

TEMPLE is a low-float, low-volume DeFi token; there is no material derivatives market (no meaningful perp OI or funding) for it at this snapshot. Liquidity is concentrated in its primary Uniswap V3 pool.

### Contract address
| Chain | Address |
|---|---|
| Ethereum | `0x470ebf5f030ed85fc1ed4c2d36b9dd02e77cf1b7` |

---

## Use Case / Narrative / Category

TempleDAO belongs to the **treasury-/crypto-backed token** category — a lineage of "protocol-owned value" experiments (kin to the OlympusDAO-era IV/backing model) that aim to give a token a hard floor from real assets. Its narrative is downside protection plus treasury-generated yield: holders are buying exposure to a managed on-chain treasury with mechanics intended to dampen volatility. Over its life the protocol has evolved its product surface around treasury management and yield distribution rather than chasing pure governance utility.

### Comparison Table

| Protocol | Model | Backing | vs TempleDAO |
|---|---|---|---|
| **TempleDAO (TEMPLE)** | Treasury-backed token + IV floor, exit queue | Managed protocol treasury | Floor-anchored, low-float, MC/FDV = 1.00; price hugs backing |
| **OlympusDAO (OHM)** | (3,3) bonding + protocol-owned liquidity / RFV | Treasury (DAI/stables + LP) | The category progenitor; far higher inflation historically — TEMPLE is the more conservative, defence-oriented descendant |
| **Frax / FXS-style** | Algorithmic-then-collateralised stable + governance | Collateral + AMOs | Frax targets a stable peg; TEMPLE targets a rising IV floor, not a $1 peg |
| **[[real-world-assets\|RWA]] yield tokens** | Tokenised T-bill / credit yield | Off-chain assets | RWA delivers exogenous yield with regulatory/custody dependence; TEMPLE's yield is endogenous DeFi treasury strategy |

The honest framing: the "protocol-owned value / IV floor" design is the **same family that produced the OlympusDAO boom-and-bust**. TEMPLE survived where many forks didn't, but the category's reputation is a headwind, and the floor is only as credible as the treasury behind it.

---

## Notable History

| Date | Event |
|---|---|
| **2023-03-19** | All-time low **$0.186** set during the deep bear market — the trough from which treasury value and confidence rebuilt. |
| **2025-11-21** | All-time high **$4.11**. |
| **2026-06-20** | Trades ~$3.00 (rank ~#352), ~27% below ATH, MC ≈ FDV ≈ $71M, ~$1.8K/24h volume — price hugging backing with near-zero active turnover. |

*All anchors above are from market-data snapshots; no fabricated editorial events are added.*

---

## Risks

- **Treasury / smart-contract risk** — the IV floor is only as good as the treasury's assets and the contracts holding them; a treasury exploit, bad strategy, or de-peg of backing assets would erode the floor.
- **Liquidity risk** — ~$1.8K/24h volume is extremely thin; any sizeable order would cause large slippage, and the exit queue throttles redemptions.
- **Backing-vs-market divergence** — if confidence breaks, market price can trade below IV despite defence mechanisms; price-defence is not guaranteed.
- **Mechanism complexity** — safe-mint/exit-queue/IV mechanics are intricate and can behave unexpectedly under stress or governance changes.
- **Regime risk** — treasury yields and token demand fall in bear markets, slowing backing growth.
- **Category-reputation risk** — the IV/backing model is associated with the OlympusDAO-era boom-and-bust; renewed skepticism toward "protocol-owned value" tokens can suppress demand regardless of TEMPLE's own treasury health.

---

## Trading Playbook (bear / Extreme-Fear, bottoming regime)

Framing only — not advice. Against the 2026-06-23 macro backdrop (Fear & Greed 21, market-health 29/100, *Bottoming / Accumulation* long-horizon regime):

- **Defensive profile, but illiquid.** TEMPLE's design is countercyclical-friendly — a treasury-backed floor is exactly the kind of "downside-protected" exposure that appeals in Extreme Fear. But ~$1.8K/24h volume makes it a *position*, not a *trade*: you cannot move size, and the exit queue throttles redemptions.
- **The edge is the discount-to-backing.** The cleanest setup is buying when market price trades **below** verified intrinsic value (a measurable floor), not when it trades at a premium on narrative. Verify current treasury IV from protocol data before assuming the floor.
- **Not a momentum vehicle.** Flat 7-day moves and near-zero turnover mean there is no trend to ride; this is a value/floor hold, sized for the possibility that confidence breaks and price trades *through* IV despite defence mechanics.
- **Invalidation.** A treasury exploit, a strategy blow-up, or a sustained market-below-IV regime (defence mechanics failing) breaks the entire thesis — those are the events to monitor, not the chart.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-finance]]
- [[real-world-assets]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko top-1000).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TEMPLE |
| **Market Cap Rank** | #343 |
| **Market Cap** | $69.64M |
| **Current Price** | $2.94 |
| **Categories** | Crypto-Backed Tokens |
| **Website** | [https://www.templedao.link/rituals](https://www.templedao.link/rituals) |

---

## Overview

TempleDAO is designed on strong principles: building the Temple for the long-term, community first and fairly in all aspects, and prioritising stable wealth creation. Our innovative mechanics including safe minting, intrinsic value backed rewards, safe harvest, price defence incentives, and exit queue.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 23.72M TEMPLE |
| **Total Supply** | 23.77M TEMPLE |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $69.78M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.11 (2025-11-21) |
| **Current vs ATH** | -28.62% |
| **All-Time Low** | $0.1863 (2023-03-19) |
| **Current vs ATL** | +1475.57% |
| **24h Change** | -0.02% |
| **7d Change** | -1.73% |
| **30d Change** | -2.11% |
| **1y Change** | -16.83% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x470ebf5f030ed85fc1ed4c2d36b9dd02e77cf1b7` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X470EBF5F030ED85FC1ED4C2D36B9DD02E77CF1B7/0X6B175474E89094C44DA98B954EEDEAC495271D0F | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.templedao.link/rituals](https://www.templedao.link/rituals) |
| **Twitter** | [@templedao](https://twitter.com/templedao) |
| **Telegram** | [TempleDAOcommunity](https://t.me/TempleDAOcommunity) (832 members) |
| **GitHub** | [https://github.com/TempleDAO/TempleDAO](https://github.com/TempleDAO/TempleDAO) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.61 |
| **Market Cap Rank** | #343 |
| **24h Range** | $2.92 — $2.94 |
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
