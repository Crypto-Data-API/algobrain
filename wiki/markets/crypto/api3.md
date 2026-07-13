---
title: "Api3"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi, oracle]
aliases: ["API3"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://api3.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[oracle]]", "[[chainlink]]", "[[oracle-manipulation]]"]
---

# Api3

**Api3** (ticker **API3**) is the governance token of the API3 DAO, an [[ethereum|Ethereum]]-based [[oracle]] protocol built around **first-party oracles** — data feeds operated directly by the API providers themselves rather than by third-party node middlemen. API3 is best known for **dAPIs** (decentralized APIs) and for pioneering **Oracle Extractable Value (OEV)**, a mechanism that recaptures the [[mev|MEV]] normally lost to searchers during oracle updates and returns it to the dApps consuming the data.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | API3 |
| **Chain** | [[ethereum\|Ethereum]] |
| **Current Price** | $0.269453 |
| **Market Cap** | $38.58M |
| **Market Cap Rank** | #542 |
| **24h Volume** | $9.74M |
| **24h Change** | +1.54% |
| **7d Change** | +4.56% |
| **Circulating Supply** | ~142.96M API3 |
| **Total Supply** | ~172.67M API3 |
| **Max Supply** | Uncapped |
| **All-Time High** | $10.30 (2021-04-07) |
| **All-Time Low** | $0.2364 (2026-06-10) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

API3 is up modestly on the day (+1.5%) and ~+4.6% over the week, showing relative resilience while the broad **Crypto [[fear-and-greed-index|Fear & Greed Index]] reads 23 (extreme fear)** in what analysts call an **Established Bear Market**. The token printed a fresh all-time low of **$0.2364 on 2026-06-10** — it now trades just above that level and roughly **-97% below its 2021 ATH** of $10.30. Daily turnover (~$9.7M on a ~$38.6M cap, ~25%) is unusually high for a token this size, signaling active rotation around the OEV narrative rather than dormant holding.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~142.96M API3 |
| **Total Supply** | ~172.67M API3 |
| **Max Supply** | Uncapped (inflationary staking rewards) |
| **Fully Diluted Valuation** | $46.01M |
| **Market Cap / FDV** | ~0.83 |
| **All-Time High** | $10.30 (2021-04-07) |
| **All-Time Low** | $0.2364 (2026-06-10) |

API3 uses an **inflationary staking model**: stakers lock API3 into a collateral/insurance pool that backstops feed accuracy, and they earn newly minted tokens for doing so. This pool is the protocol's security and accountability layer — if a first-party feed delivers bad data, staked API3 can be used to compensate harmed dApps. Token holders also govern the API3 DAO. Because supply is **uncapped** (staking rewards mint new API3 indefinitely), the MC/FDV near **0.83** understates the open-ended emission schedule — demand must continually outpace inflation to avoid sell pressure.

---

## Technology & Protocol

API3's design departs from the [[chainlink|Chainlink]] third-party-node [[oracle|oracle]] model:

- **First-party oracles** — Data providers run their own oracle nodes (using API3's **Airnode**), signing data directly. This removes the middleman node layer, improves transparency about data provenance, and lets providers be held accountable via the staking pool.
- **dAPIs (decentralized APIs)** — Aggregated, managed price feeds that dApps subscribe to, available across many EVM chains via the API3 Market.
- **OEV (Oracle Extractable Value)** — API3 auctions the right to trigger oracle updates (e.g., liquidation-triggering price pushes). The value searchers would otherwise extract as [[mev|MEV]] is instead captured and rebated to the dApp, turning the oracle from a cost center into a **revenue source** for [[lending-protocols|lending protocols]] and perp [[dex|DEXs]]. The **OEV Network** is the dedicated chain/auction layer that runs these update-right auctions.

These products make API3 a competitor to [[chainlink|Chainlink]], [[pyth-network]], and [[redstone-oracles]] in [[defi|DeFi]] price feeds, with **OEV** as its strongest differentiator.

## Market Structure & Derivatives

**Spot venues.** API3 lists on Binance (API3/USDT), Kraken (API3/USD), Upbit (API3/KRW), Bitget, KuCoin, and Crypto.com. On-chain liquidity is on [[uniswap]] V2/V3 and SushiSwap against WETH.

**Liquidity & depth.** ~$9.7M daily volume on a ~$38.6M cap is high turnover, but absolute depth remains modest — large orders move price. Spot CEX/DEX flow dominates; API3 is not a flagship perpetual market on [[hyperliquid|Hyperliquid]] or other major perp venues, so leveraged-derivatives exposure is limited and price is driven by spot supply/demand around oracle catalysts.

---

## Peer Comparison

| Oracle | Model | Mcap Rank | Market Cap | Edge |
|---|---|---|---|---|
| [[chainlink\|Chainlink (LINK)]] | Third-party node network | top-20 | multi-$B | Dominant integrations, CCIP, market standard |
| [[pyth-network\|Pyth (PYTH)]] | First-party, pull/low-latency | top-100 | larger | High-frequency feeds from trading firms |
| **Api3 (API3)** | First-party (Airnode) + OEV | #542 | ~$38.6M | OEV revenue recapture; provider accountability |
| [[redstone-oracles\|RedStone]] | Modular pull oracle | — | smaller/private | Cheap on-demand feeds, EVM + non-EVM |

API3 is a **small-cap challenger** to far larger incumbents. Its bet is not to out-integrate Chainlink but to differentiate on **first-party provenance** and **OEV economics** — letting integrators monetize their own liquidations instead of leaking that value to searchers.

---

## Valuation Framing

API3's fundamental value tracks **OEV revenue capture** and **feed adoption**. With an uncapped supply and inflationary staking, the bull case requires OEV fees and dApp subscriptions to grow faster than emissions; the bear case is that adoption stays niche while Chainlink/Pyth dominate distribution. Trading near its all-time low at ~$38M cap, API3 screens as a deep-value / high-optionality oracle bet — qualitative only, not a price target.

---

## Use Case, Narrative & Category

API3 sits in the **oracle / DeFi-infrastructure** category. Its narrative rests on two pillars: (1) **first-party data** as a more transparent, accountable alternative to node-operator oracles, and (2) **OEV** as a way for lending markets and derivatives venues to reclaim value that currently leaks to MEV searchers. As DeFi liquidations and perp funding generate large extractable value, OEV is positioned as a meaningful new revenue primitive — the core of API3's bullish thesis and the source of its "oracles that pay you" tagline.

---

## Notable History

- **2020** — API3 founded out of the CLC Group / Honeycomb API ecosystem; built the **Airnode** first-party oracle to let API providers serve data without intermediaries.
- **2021** — Token launch; API3 reached its ATH of $10.30 in April 2021.
- **2022-2023** — Rollout of **dAPIs** and the API3 Market across EVM chains; expansion of the staking/insurance model.
- **2024** — Launch and promotion of **OEV** as a flagship feature, with the OEV Network designed to auction update rights and rebate value to integrators.
- **2026** — Token set a new all-time low ($0.2364, 2026-06-10) during the broad crypto downturn.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — First-party feeds shift trust to the API providers themselves; a compromised or malicious provider could push bad data, with the staking pool as the only economic backstop. See [[oracle-manipulation]].
- **Coverage adequacy risk** — The insurance/collateral pool must remain large enough to credibly compensate harmed dApps; a sharp API3 price drop shrinks the real-dollar value of that backstop just when it may be needed.
- **Competitive risk** — API3 competes directly with the far larger [[chainlink]] and the high-frequency [[pyth-network]]; OEV adoption is still maturing and faces alternative MEV-redistribution designs.
- **Emission / dilution risk** — Inflationary staking rewards continually mint new supply; demand must outpace emissions to avoid sell pressure.
- **Liquidity & macro risk** — ~$9.7M daily volume is modest in absolute terms, and in an extreme-fear, Established Bear Market regime (Fear & Greed 23) low-cap infra tokens are prone to liquidity drought and underperformance.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[oracle]]
- [[mev]]
- [[defi]]
- [[chainlink]]
- [[pyth-network]]
- [[redstone-oracles]]
- [[uma]]
- [[tellor]]
- [[oracle-manipulation]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
