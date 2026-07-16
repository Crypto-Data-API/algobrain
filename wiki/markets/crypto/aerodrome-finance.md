---
title: "Aerodrome Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["AERO", "Aerodrome"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://aerodrome.finance/"
related: ["[[base]]", "[[crypto-markets]]", "[[ethereum]]", "[[velodrome-finance]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[oi-confirmed-trend]]"]
---

# Aerodrome Finance

**Aerodrome Finance** (AERO) is the dominant [[decentralized-exchange|decentralized exchange]] and central liquidity hub of the [[base|Base]] L2, built as the sister deployment of [[velodrome-finance|Velodrome]] (Optimism) using the ve(3,3) vote-escrow [[automated-market-maker|AMM]] model. For traders it is the primary venue for Base-native spot liquidity and the benchmark "Base ecosystem beta" token — and in 2026 it is mid-way through its most consequential event: a planned merger with Velodrome into a unified cross-chain liquidity layer called "Aero."

---

## Market Data

| Metric | Value |
|---|---|
| **Current Price** | $0.486512 |
| **Market Cap** | $465,470,069 (~$465.5M) |
| **Market Cap Rank** | #108 |
| **Fully Diluted Valuation** | $934,881,054 (~$934.9M) |
| **24h Volume** | $51,196,338 (~$51.20M) |
| **24h Change** | +8.00% |
| **7d Change** | +35.10% |
| **Circulating Supply** | 956,809,667 AERO (~956.8M) |
| **Total Supply** | 1,921,720,191 AERO (~1.922B) |
| **Max Supply** | None (uncapped — ongoing emissions) |
| **MC / FDV Ratio** | ~0.50 |
| **All-Time High** | $2.32 (2024-12-07) |
| **All-Time Low** | $0.00001861 (2023-10-17) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Tape divergence:** with the broad market in **extreme fear** (Fear & Greed = 23) and an **Established Bear Market** regime as of 2026-06-20, AERO is conspicuously *bucking the tape* — up ~8% over 24h and ~35% over the week while most altcoins bleed. The most likely driver is anticipation of the **July 2026 Aero cross-chain launch / Velodrome merger** (see [[#2025–2026 Developments]]), an event-driven re-rating rather than a beta move with [[crypto-markets]]. At ~$465M market cap vs ~$935M FDV (MC/FDV ~0.50), roughly half the eventual supply is still unissued via emissions — the structural counterweight to the rally.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AERO |
| **Asset class** | DEX / ve(3,3) AMM governance token |
| **Native Chain** | [[base|Base]] (Coinbase-incubated Ethereum L2) |
| **Market Cap** | $465.5M, rank #108 — as of 2026-06-20 |
| **Price** | $0.486512 — as of 2026-06-20 |
| **Categories** | Decentralized Exchange (DEX), DeFi, AMM, Base Ecosystem, Base Native |
| **Website** | [https://aerodrome.finance/](https://aerodrome.finance/) |

---

## Overview

Aerodrome Finance is a next-generation AMM designed to serve as Base's central liquidity hub, combining a powerful liquidity incentive engine, vote-lock governance model, and friendly user experience. Aerodrome inherits the latest features from Velodrome V2.

Mechanics that matter: AERO emissions are directed weekly by veAERO lockers, who vote on which pools receive incentives and in exchange capture that pool's trading fees plus third-party "bribes" (voting incentives). This makes AERO partly a cash-flow asset — veAERO yield tracks Base DEX volumes — and partly a governance asset that protocols must accumulate to bootstrap liquidity on Base.

---

## Protocol & Technology

Aerodrome is a **ve(3,3) vote-escrow AMM** — the design lineage Andre Cronje pioneered with Solidly, refined by [[velodrome-finance|Velodrome]], and deployed on [[base|Base]] as Aerodrome. It fuses an [[automated-market-maker|AMM]] [[decentralized-exchange|DEX]] with a vote-escrow governance economy so that *the protocol's own emissions are auctioned to whoever brings the most liquidity demand*.

### Core mechanism (the flywheel)

1. **AMM trading layer.** Aerodrome runs two pool types:
   - **Stable / volatile pools** (Velodrome V2-style) — a constant-product curve for volatile pairs and a low-slippage stable curve for pegged assets ([[stablecoins]], LSTs).
   - **Slipstream concentrated-liquidity pools** — Uniswap-V3-style tick-based concentrated liquidity, letting LPs target capital around the active price for far higher capital efficiency on correlated pairs.
2. **AERO emissions.** New AERO is minted each weekly epoch and distributed to liquidity pools as incentives. Emissions follow a decaying schedule but the supply remains **uncapped**.
3. **veAERO vote-escrow.** Holders lock AERO (up to ~4 years) to mint **veAERO**, a non-transferable, time-decaying voting NFT. Longer locks → more voting weight.
4. **Gauge voting.** Each weekly epoch, veAERO holders vote on **gauges** (per-pool emission allocators). Whichever pools attract the most votes receive that week's AERO emissions.
5. **Fee + bribe capture.** Crucially — and unlike Curve-style models — veAERO voters earn **100% of the trading fees** of the pools they vote for, *plus* third-party **bribes / voting incentives** that protocols pay to attract emissions to their pool. This is the "real yield" that makes veAERO a cash-flow asset tracking Base DEX volume.

### Why this matters

The design creates a market for emissions: a protocol that wants deep liquidity on [[base|Base]] either locks AERO itself (becoming a veAERO voter) or bribes existing voters. veAERO yield therefore scales with Base on-chain activity, while AERO the liquid token is the levered, dilution-exposed claim on that flywheel. The model is a direct descendant of the [[ethereum|Ethereum]]-mainnet "Curve Wars" gauge-bribe meta, ported to Base.

---

## 2025–2026 Developments

- **Velodrome merger / "Aero" unification (announced, executing through 2026)** — official docs state Aerodrome will merge with Velodrome in 2026 to form **Aero**, a unified liquidity layer extending beyond Base to [[ethereum|Ethereum]] mainnet and Circle's Arc chain, with liquidity migration and new pools rolling out ahead of a **July 2026 cross-chain launch**. This is the dominant catalyst and re-rating thesis for the token — and the most plausible explanation for the +35% week into 2026-06-20.
- **Supply overhang remains live** — circulating supply ~957M vs ~1.92B total; ongoing weekly emissions and scheduled unlocks (e.g. an unlock flagged for 11 June 2026 on CoinGecko) keep structural sell pressure on the token. MC/FDV is ~0.50 at the 2026-06-20 snapshot.
- **Price round-trip** — ATH $2.32 (7 Dec 2024) in the Base-season rally, then an ~85% drawdown through the 2025 alt bear; recovered to ~$0.49 by 2026-06-20 on merger anticipation.

---

## Tokenomics & Supply

As of the 2026-06-20 snapshot (CoinGecko):

| Metric | Value |
|---|---|
| **Circulating Supply** | 956,809,667 AERO (~956.8M) |
| **Total Supply** | 1,921,720,191 AERO (~1.922B) |
| **Max Supply** | None — uncapped, ongoing weekly emissions on a decaying schedule |
| **MC / FDV Ratio** | ~0.50 |

**Emissions & ve-locking.** AERO has *no hard cap*: new tokens are minted every epoch and routed to gauges by veAERO vote. The mitigating force is **vote-escrow lockup** — a large share of supply is locked as veAERO (removed from float) to chase fees and bribes, which structurally absorbs some of the emission. The bull case is that lock demand + fee/bribe yield outpaces sell pressure from emissions; the bear case is the reverse.

**Dilution flag.** With MC/FDV ~0.50, roughly **half of the eventual fully-diluted supply has not yet been issued**. Combined with an *uncapped* schedule, AERO carries persistent, ongoing dilution — distinct from fixed-cap tokens where unlocks eventually end. Any valuation must net emissions against fee/bribe accrual rather than treat current circulating supply as terminal.

---

## Ecosystem & Use Cases

- **Base's central liquidity hub.** Aerodrome is the default AMM for [[base|Base]]-native projects bootstrapping liquidity — new tokens route emissions/bribes through Aerodrome gauges to attract depth, making it structurally central to the Base DeFi stack.
- **Stable / pegged-asset routing.** Stable pools anchor [[stablecoins]] and LST liquidity on Base; deep stable depth makes Aerodrome a core swap router for the chain.
- **veAERO as protocol-owned liquidity tooling.** Protocols accumulate veAERO to self-direct emissions, or bribe voters — a recurring on-chain market for liquidity.
- **Coinbase-ecosystem proxy.** As the dominant DEX on Coinbase's L2, AERO is the cleanest liquid proxy for on-chain Base activity and Coinbase's on-chain initiatives.
- **Cross-chain expansion (pending).** Post-merger "Aero" extends the model to [[ethereum|Ethereum]] mainnet and Circle's Arc, broadening the addressable liquidity surface beyond Base.

---

## Market Structure & Derivatives

- **Spot venues** — Kraken, Upbit, Bitget, KuCoin, Crypto.com (CEX listings); the **deepest spot liquidity is native, on Aerodrome itself on [[base|Base]]**.
- **Perpetuals** — **AERO-PERP on [[hyperliquid|Hyperliquid]]** is the primary liquid derivatives venue; some CEX perp listings exist.
- **Metrics to monitor (no invented values):**
  - **Perp funding rate** — persistently positive funding into the +35% week would flag crowded longs / squeeze risk; negative funding on strength can signal a short squeeze.
  - **Open interest (OI)** — rising OI with rising price confirms fresh positioning; rising OI into resistance warns of leverage build-up.
  - **Spot vs perp basis** and **CEX↔on-chain liquidity split** — most real AERO depth is on-chain, so CEX order books can be thin relative to size.

---

## Valuation Framework

AERO is best valued as a **claim on Base DEX cash flows**, discounted by emissions. Key metrics to track (describe, don't invent):

- **Protocol trading volume** — weekly/annual DEX volume routed through Aerodrome pools; the top-line driver of fees.
- **Trading fees → veAERO** — fees flow to voters, so fee growth is the real-yield numerator.
- **Bribe / voting-incentive revenue** — third-party payments to veAERO voters; a second yield stream and a demand signal for emissions.
- **TVL** — liquidity depth on Base; supports volume capacity.
- **veAERO lock ratio** — share of supply locked vs liquid; high lock ratio reduces effective float and signals conviction.
- **Emissions vs fee/bribe accrual** — the central tension: is real yield outpacing dilution?
- **MC/FDV (~0.50)** — discount embeds future emissions; useful as a dilution-adjusted relative-value gauge vs peers.

A common framing is **fee + bribe yield to veAERO** vs a comparable ve(3,3) peer ([[velodrome-finance|Velodrome]]) or vs the dilution rate — if real yield exceeds emission dilution, the flywheel is value-accretive.

---

## Trading Playbook

- **Proxy logic** — AERO ≈ levered exposure to Base DEX volume the way [[velodrome-finance|Velodrome]] is to Optimism. Long AERO to express a "Base activity accelerates" thesis.
- **Event-driven (current)** — the **July 2026 Aero cross-chain launch / Velodrome merger** is the dominant catalyst; the +35% week into 2026-06-20 is most likely front-running it. Watch **token-conversion terms** (Velodrome→Aero) closely — botched ve(3,3) migrations have historically punished tokens hard. Classic "buy the rumor, watch the news" risk around the launch date.
- **Narrative baskets** — Base ecosystem / Coinbase beta, "real yield" DeFi (fee-sharing ve tokens), DEX tokens. Standard long when Base activity or Coinbase on-chain initiatives accelerate.
- **Yield/structural** — lock AERO → veAERO to harvest fees + bribes; the trade is whether real yield beats emission dilution.
- **Risk management** — uncapped emissions and recurring unlocks (e.g. June 11 2026) mean structural supply hits; size for merger-execution headline risk and thinner-than-CEX-implied liquidity.

---

## History

| Date | Event |
|---|---|
| **2023** | Aerodrome launches on [[base|Base]] as the ve(3,3) sister deployment of [[velodrome-finance|Velodrome]]. |
| **2023-10-17** | All-time low $0.00001861 (early float / launch pricing). |
| **2024** | Becomes the dominant DEX and central liquidity hub on Base; "Base season" inflows. |
| **2024-12-07** | All-time high $2.32 during the Base-season rally. |
| **2025** | ~85% drawdown through the alt bear market; emissions/unlocks weigh on price. |
| **2026** | Velodrome merger / "Aero" unification announced — cross-chain layer to [[ethereum|Ethereum]] mainnet and Circle's Arc. |
| **2026-06-11** | Scheduled unlock flagged on CoinGecko. |
| **2026-06-20** | Price ~$0.49, mcap ~$465.5M, rank #108; +35% on the week bucking the bear tape on merger anticipation. |
| **July 2026 (planned)** | Aero cross-chain launch — the dominant catalyst. |

---

## Competitive Positioning

| DEX | Chain | Model | TVL tier | Token |
|---|---|---|---|---|
| **Aerodrome** | [[base\|Base]] | ve(3,3) vote-escrow AMM (stable/volatile + Slipstream CL) | Largest on Base | AERO |
| [[velodrome-finance\|Velodrome]] | Optimism | ve(3,3) vote-escrow AMM (Aerodrome's sister; merging into "Aero") | Largest on Optimism | VELO |
| [[uniswap\|Uniswap]] (v4 on Base) | Base + multichain | Concentrated liquidity + v4 hooks; no emission flywheel | Largest DEX overall | UNI |
| BaseSwap | Base | Forked AMM / yield farm | Small | BSWAP |
| SushiSwap (on Base) | Base + multichain | Multichain AMM | Small on Base | SUSHI |

**Positioning read:** Aerodrome's moat on Base is the ve(3,3) **emission flywheel** — it can rent liquidity in via bribes/votes in a way pure-CL DEXs cannot, which is why it dominates Base TVL despite [[uniswap|Uniswap]]'s deployment there. The biggest competitive threat is **[[uniswap|Uniswap v4]] hooks on Base** (programmable liquidity that could replicate incentive logic) and any erosion of Base's overall activity. The Velodrome merger is an offensive move to extend the flywheel cross-chain rather than defend Base alone.

---

## Contract Addresses

| Chain | Address |
|---|---|
| Base | `0x940181a94a35a4569e4529a3cdfb74e38fd98631` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://aerodrome.finance/](https://aerodrome.finance/) |
| **Twitter** | [@aerodromefi](https://twitter.com/aerodromefi) |
| **Discord** | [https://discord.gg/aerodrome](https://discord.gg/aerodrome) |
| **GitHub** | [https://github.com/aerodrome-finance](https://github.com/aerodrome-finance) |
| **Docs** | [https://aerodrome.finance/docs](https://aerodrome.finance/docs) |

---

## Risks

- **Emission-driven dilution** — uncapped supply with ongoing weekly emissions; MC/FDV ~0.50 means ~half of eventual supply is still unissued. Real yield must outpace dilution for the token to accrue value.
- **Scheduled unlocks** — recurring unlocks (e.g. 11 June 2026) add structural sell pressure.
- **Merger / migration execution risk** — the Velodrome→Aero unification involves liquidity migration and token-conversion mechanics; botched ve(3,3) migrations have historically punished tokens hard. The +35% week prices in success.
- **Base-DEX competition** — [[uniswap|Uniswap v4]] (hooks) on Base, plus BaseSwap/SushiSwap, compete for the same volume and liquidity.
- **Single-chain concentration** — pre-merger, AERO's fortunes are tightly coupled to [[base|Base]] activity and Coinbase's on-chain strategy.
- **Liquidity / venue risk** — deepest depth is on-chain on Base; CEX order books can be thin relative to size, and AERO-PERP on [[hyperliquid|Hyperliquid]] carries the usual leverage/funding risk.
- **Macro / regime risk** — despite the current divergence, AERO remains a high-beta altcoin exposed to the prevailing **Established Bear Market** and extreme-fear conditions; an event-driven rally can unwind sharply if the catalyst disappoints.

---

## Related

- [[base]]
- [[velodrome-finance]]
- [[ethereum]]
- [[uniswap]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[stablecoins]]
- [[crypto-markets]]
- [[hyperliquid]]
- [[stablecoin-yields]]

---

## Sources

- CoinGecko 2026-06-20 snapshot — current market data (cryptodataapi.com / CoinGecko)
- CoinGecko April 2026 snapshot (Source: [[coingecko-top-1000-2026-04-09]])
- Aerodrome docs — Velodrome merger / Aero unification: https://aerodrome.finance/docs
- CoinMarketCap AI updates, 7 June 2026 (July 2026 cross-chain launch): https://coinmarketcap.com/cmc-ai/aerodrome-finance/latest-updates/
- CoinStats AERO valuation page, June 2026 (~$387M mcap): https://coinstats.app/ai/a/price-potential-aerodrome-finance
- CoinGecko AERO live page (June 11 unlock): https://www.coingecko.com/en/coins/aerodrome-finance
- Verified via Perplexity (sonar) + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 969.59M AERO |
| **Total Supply** | 1.94B AERO |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $956.04M |
| **Market Cap / FDV Ratio** | 0.50 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.32 (2024-12-07) |
| **Current vs ATH** | -78.73% |
| **All-Time Low** | $0.00001861 (2023-10-17) |
| **Current vs ATL** | +2647968.07% |
| **24h Change** | -4.87% |
| **7d Change** | -7.79% |
| **30d Change** | +9.42% |
| **1y Change** | -43.09% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0x940181a94a35a4569e4529a3cdfb74e38fd98631` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | AERO/USD | N/A |
| Upbit | AERO/KRW | N/A |
| Bitget | AERO/USDT | N/A |
| KuCoin | AERO/USDT | N/A |
| Crypto.com Exchange | AERO/USD | N/A |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $21.90M |
| **Market Cap Rank** | #106 |
| **24h Range** | $0.4896 — $0.5240 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

AERO is a **PERP-FIRST** asset for leveraged traders: **AERO-PERP on [[hyperliquid|Hyperliquid]]** (up to ~40-50x) is the primary liquid derivatives venue, while it is **NOT listed on Binance** and CEX spot access is limited/offshore (Kraken, Upbit, Bitget, KuCoin, Crypto.com). The deepest *spot* depth is actually on-chain on Aerodrome itself on [[base|Base]], so directional flow and price discovery for size concentrate on the HL perp. Practical consequence: sizing should key off HL order-book depth (`l2-book`) rather than headline CEX volumes — CEX books can be thin relative to size, on-chain spot has slippage/gas friction for fast execution, and the perp is where funding, OI and liquidations form. Use limit/scaled entries; assume shallower depth than a Binance-listed alt of comparable market cap.

### Applicable strategies

- [[funding-rate-harvest]] — a PERP-FIRST alt with no Binance venue tends to carry a persistent funding premium on HL; collect it while delta-hedging against on-chain spot.
- [[hl-vs-cex-funding-divergence]] — because AERO trades on HL and offshore CEX perps but not Binance, funding can dislocate meaningfully between venues, creating a spread to harvest.
- [[crowded-long-funding-fade]] — event-driven anticipation of the July 2026 Aero merger crowds longs; fade richly positive funding into resistance on the HL perp.
- [[liquidation-cascade-fade]] — thin cross-venue depth plus ~40-50x leverage makes AERO prone to sharp liquidation flushes; fade forced-seller wicks back toward the mean.
- [[oi-confirmed-trend]] — rising OI confirming a merger-driven breakout signals fresh positioning worth following; rising OI into resistance warns of leverage build-up.
- [[event-driven-trading]] — the token-conversion / cross-chain launch and recurring unlocks are discrete, scheduled catalysts that drive AERO more than beta does.

### Volatility & regime character

AERO is a **high-beta DeFi / DEX governance token** (ve(3,3) infra token, "Base ecosystem beta" and Coinbase-on-chain proxy). It generally carries high correlation to broad alt risk and BTC/ETH beta, but its defining trait in 2026 is **event-driven reflexivity** — it can decouple hard from the tape around the Velodrome merger and cross-chain launch (e.g. bucking a bear tape on merger anticipation). Expect elevated realized volatility, uncapped-emissions dilution as a structural drag, and sharp two-way moves around discrete catalysts rather than a steady beta profile.

### Risk flags

- **Venue concentration** — leveraged flow depends on the single HL perp; no Binance backstop and thin/offshore CEX spot means gappy liquidity and outsized slippage on size.
- **Uncapped emissions + scheduled unlocks** — ongoing weekly emissions (MC/FDV ~0.50, ~half of supply unissued) and recurring unlocks create persistent structural sell pressure.
- **Narrative / event dependence** — price leans heavily on the merger/cross-chain launch thesis; botched ve(3,3) migrations have historically punished tokens, and a "buy the rumor" unwind can be violent.
- **Perp funding dislocations** — PERP-FIRST status means funding can run rich (crowded longs) or dislocate vs offshore CEX perps; funding shocks and cascade risk are amplified by high leverage.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=AERO` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=AERO` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=AERO&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=AERO&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=AERO"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---
