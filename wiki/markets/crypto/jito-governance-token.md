---
title: "Jito"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi, market-microstructure, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["JTO", "Jito Network", "JitoSOL"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.jito.network/"
related: ["[[crypto-markets]]", "[[jupiter-exchange-solana]]", "[[kamino]]", "[[liquid-staking]]", "[[mev]]", "[[raydium]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[pairs-trading]]"]
---

# Jito

**Jito** (JTO) is the governance token of the Jito Network, a major contributor to the [[solana|Solana]] ecosystem through its **JitoSOL** [[liquid-staking]] pool and its suite of [[mev|MEV]] products. JitoSOL is the largest Solana liquid-staking token, and the Jito-Solana validator client (which runs the on-chain MEV auction) is operated by validators controlling the large majority of Solana's active stake. JTO itself is a governance claim on this infrastructure — effectively a leveraged bet on Solana staking demand and MEV revenue.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | JTO |
| **Current Price** | $0.722816 |
| **Market Cap** | $350,739,708 |
| **Market Cap Rank** | #128 |
| **24h Volume** | $93,593,415 |
| **24h Change** | -4.37% |
| **7d Change** | +32.65% |
| **All-Time High** | $6.01 (2023-12-07) |
| **Current vs ATH** | -88.0% |
| **All-Time Low** | $0.218137 (2026-02-06) |
| **Current vs ATL** | +231% |
| **Categories** | DeFi, Solana Ecosystem, Liquid Staking Governance Tokens, Made in USA |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** As of 2026-06-20 the market sits in an *Established Bear Market* with the Crypto Fear & Greed Index at **23 (extreme fear)**. Despite that, JTO is up **+32.7% on the week** (though -4.4% on the day) on very heavy $93.6M of 24h volume against a $350M cap — a ~27% volume/cap ratio that flags an active, news/rotation-driven move rather than passive accumulation. The token has more than tripled off its February 2026 all-time low of $0.218.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | JTO |
| **Market Cap Rank** | #128 |
| **Native Chain** | [[solana]] |
| **Sector** | Liquid staking governance / MEV infrastructure |
| **Categories** | DeFi, Solana Ecosystem, Liquid Staking Governance Tokens, Multicoin Capital Portfolio, Delphi Ventures Portfolio, Made in USA |
| **Website** | [https://www.jito.network/](https://www.jito.network/) |

---

## Overview

JTO is the governance token of the Jito Network. Jito Network is a major contributor to the Solana ecosystem through its JitoSOL liquid staking pool, and its collection of MEV products. Users can exchange their SOL for JitoSOL. In return, holders maintain SOL's liquidity and DeFi opportunities while earning yield from staking. JitoSOL uniquely provides its holders with additional rewards from transaction revenue associated with MEV extraction on Solana. Maximum extractable value ([[mev|MEV]]) describes profit opportunities attributable to the specific order of transaction execution. For example, a large swap on Orca can lower the pool's price below that of [[raydium]]; traders race to profit from that price difference, and this arbitrage is considered MEV. The Jito Foundation was created to minimize the negative impacts of MEV, equitably distribute the profits and increase transparency. Jito published an open-source validator client designed to create a competitive market for MEV extraction. The client enables auctions within each block for the opportunity to capture that block's MEV: traders submit bids, and the highest bidders within each block can harvest available MEV.

---

## Protocol & Product

Jito operates across two tightly linked product lines: a **liquid-staking** product (JitoSOL) for capital holders, and **MEV infrastructure** (the Jito-Solana client, Block Engine and BAM) for validators and searchers. JTO governs both.

### JitoSOL liquid-staking mechanics

JitoSOL is Jito's [[liquid-staking]] token — the Solana equivalent of Lido's stETH on Ethereum. The mechanics:

1. **Deposit SOL** into the Jito stake pool.
2. **Receive JitoSOL**, a liquid receipt token representing staked SOL + accrued rewards.
3. **JitoSOL appreciates** relative to SOL over time as staking rewards accumulate (roughly ~7-8% APY base staking + MEV tips).
4. **Use JitoSOL across DeFi** — as collateral in [[kamino]], traded on [[jupiter-exchange-solana|Jupiter]], or in LP positions on [[raydium]] / [[orca]].

**JitoSOL vs SOL pricing.** JitoSOL is *not* pegged 1:1 to SOL. Instead, 1 JitoSOL is worth slightly more than 1 SOL, and this premium grows over time as yields accrue (the exchange rate only goes up, barring slashing). This makes JitoSOL/SOL pairs ideal for low-impermanent-loss LP positions since the two assets are highly correlated.

### MEV redistribution: Jito's unique edge

What distinguishes Jito from other Solana LST protocols (Marinade, SolBlaze, etc.) is its **MEV redistribution** mechanism:

1. **Jito validator client:** a modified Solana validator client with a built-in [[mev|MEV]] auction (conceptually similar to Flashbots on Ethereum).
2. **Searchers submit bundles:** arbitrage and liquidation bots submit transaction bundles with tips to Jito's **Block Engine**.
3. **Auction:** the Block Engine runs an auction; the highest-tipping bundles are included in the next block.
4. **Tips flow to stakers:** a portion of collected MEV tips is redistributed to JitoSOL holders, boosting their yield.

Why it matters for traders:

- **Higher yield:** JitoSOL consistently offers ~1-3% more APY than vanilla SOL staking from MEV tip redistribution.
- **MEV as a revenue stream:** as Solana DeFi activity grows (more arbitrage, liquidations), MEV tips scale proportionally.
- **Solana MEV proxy:** holding JitoSOL (or JTO) is an indirect way to profit from MEV activity on Solana without running searcher infrastructure.

### Tip Router and governance

The **Tip Router** distributes MEV tips between validators, stakers, and the Jito DAO treasury. JTO holders govern:

- **Tip distribution ratios** — what share of MEV tips goes to JitoSOL holders vs validators vs the DAO.
- **Validator delegation strategy** — which validators receive stake from the JitoSOL pool.
- **Protocol upgrades** — changes to the Block Engine, auction mechanism and staking infrastructure.

This governance power is the primary utility of the JTO token itself.

### Block Assembly Marketplace (BAM)

In 2025 Jito launched **BAM (Block Assembly Marketplace)**, a decentralized block-building system that moves Jito beyond the original Block Engine. BAM runs a network of nodes inside **Trusted Execution Environments (TEEs)** that order transactions and hand them to validators running Jito's upgraded client, emphasizing transparency, an encrypted mempool, and application-level customization of block construction. BAM reached **Solana mainnet in September 2025**. By late 2025 it was projected to add roughly **$15M/year** in revenue on top of the Block Engine's existing fee streams, contributing to total Jito protocol revenue estimated above **$30M annually** (Source: external; Verified via web search, 2026-06-11). BAM deepens Jito's control of Solana's MEV supply chain and gives the [[jito-governance-token|JTO]] DAO a second revenue lever beyond staking tips.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20, CoinGecko) |
|---|---|
| **Circulating Supply** | 485,179,783 JTO |
| **Total Supply** | 1,000,000,000 JTO |
| **Max Supply** | Uncapped (no hard cap) |
| **Fully Diluted Valuation** | $722,906,685 |
| **Market Cap / FDV Ratio** | ~0.49 |

**Dilution flag:** with an MC/FDV ratio of only **~0.49**, roughly half of the 1B total supply is still locked or unvested. As locked allocations (team, investors, ecosystem) continue to unlock against this still-thin market cap, holders face structural sell pressure unless demand grows in step. The **uncapped max supply** is a second-order risk: governance could in principle vote to inflate beyond 1B. This dilution overhang is a key reason JTO trades ~88% below its 2023 ATH despite the protocol's expanding revenue and network share.

### Contract address

| Chain | Address |
|---|---|
| [[solana]] | `jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL` |

---

## Ecosystem & Use Cases

- **Largest Solana LST:** JitoSOL is the #1 Solana [[liquid-staking]] token by TVL, the default staked-SOL primitive across Solana DeFi.
- **DeFi collateral:** JitoSOL is widely accepted as collateral ([[kamino]] leveraged staking), traded via [[jupiter-exchange-solana|Jupiter]], and LP'd on [[raydium]] / [[orca]].
- **MEV infrastructure for validators/searchers:** the Jito-Solana client, Block Engine and BAM are core Solana MEV plumbing.
- **Governance:** JTO governs tip routing, delegation and protocol upgrades.

### Jito's Solana staking market share

Jito is the dominant liquid-staking protocol on Solana. As of early 2026, JitoSOL is the **largest Solana liquid-staking token**, with over **14.5M SOL staked** and roughly **$2.92B TVL**, ahead of competitors such as Marinade. The Jito-Solana validator client runs on validators representing **over 95% of Solana's active stake**, giving Jito's Block Engine near-total network coverage for MEV auctions (Source: external; Verified via web search, 2026-06-11).

---

## Market Structure & Derivatives

### Centralized exchanges

| Exchange | Pair |
|---|---|
| Binance | JTO/USDT |
| Kraken | JTO/USD |
| Upbit | JTO/KRW |
| Bitget | JTO/USDT |
| KuCoin | JTO/USDT |
| Crypto.com Exchange | JTO/USD |

### DEX & derivatives

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid\|Hyperliquid]] | JTO-PERP | Perpetual |
| Orca | JTO/JitoSOL | Spot (Solana DEX) |

JTO has broad CEX coverage including Korean retail access (Upbit/KRW), which adds episodic high-beta flow. Spot liquidity is healthy relative to cap (the 2026-06-20 ~$93.6M volume is ~27% of market cap). [[hyperliquid|Hyperliquid]]'s JTO-PERP allows leveraged and short expression; with a strong +32.7% weekly move into extreme-fear macro, perp funding and open interest are worth watching for crowding/exhaustion at the top of the rally.

---

## Valuation Framework (qualitative)

JTO can be valued through several complementary lenses:

1. **Fee/revenue claim.** Through tip routing and BAM, the Jito DAO captures a slice of Solana MEV plus staking-pool economics (protocol revenue estimated >$30M/year). JTO is the governance claim on that cash-flow stack, so a price-to-protocol-revenue framing applies — though token holders do not currently receive direct fee distribution.
2. **SOL-beta.** JTO is a leveraged play on [[solana]]: more SOL staked and more on-chain activity → more MEV tips → more value under JitoSOL/DAO control. JTO amplifies SOL's directional moves.
3. **Liquid-staking category beta.** JTO rises and falls with the broad LST/LSD narrative.
4. **Dilution discount.** The ~0.49 MC/FDV ratio means continued unlocks are a structural headwind that any fundamental valuation must net out.

---

## Trading Playbook

| Strategy | Description | Risk |
|---|---|---|
| **JTO as SOL beta** | Buy JTO when bullish on Solana; it amplifies SOL moves | High volatility; ~88% ATH drawdown; dilution |
| **JitoSOL yield farming** | Hold JitoSOL for staking yield + MEV tips; lever via [[kamino]] | Smart-contract and depeg risk |
| **JitoSOL/SOL LP** | LP the JitoSOL/SOL pair on [[raydium]] / [[orca]] — minimal IL due to correlation | Low IL; smart-contract risk |
| **MEV-activity momentum** | Track Jito tip metrics; rising tips = bullish for JitoSOL yield and JTO | Requires on-chain data monitoring |
| **Exhaustion fade** | Short JTO-PERP on [[hyperliquid]] into vertical rallies + crowded funding | Squeeze risk; high beta |

- **Unlock-aware entries.** Given the ~0.49 MC/FDV, time entries around scheduled unlock cliffs rather than fighting them.
- **Solana-correlated.** Pair-trade JTO against SOL to isolate the staking/MEV beta from broad market direction.

---

## History

- **2023-12-07** — JTO launches with an airdrop to JitoSOL stakers and MEV users; prints its all-time high of **$6.01** in the first days of trading.
- **2024-2025** — multi-year drawdown alongside the broad alt market; JitoSOL nonetheless climbs to dominate Solana liquid staking, and the Jito-Solana client reaches 95%+ of active stake.
- **2025-09** — **BAM** reaches Solana mainnet, adding a second protocol-revenue lever (~$15M/year projected) atop the Block Engine.
- **2026-02-06** — JTO prints its all-time low of **$0.218137** amid the broad bear market.
- **2026-06-20** — $0.722816, market cap $350M, rank #128; +32.7% on the week, more than 3x off the February low, but still ~88% below ATH. No exploit reported for Jito through mid-2026.

> *Earlier notable events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Competitive Positioning

| Protocol | Network | LST | Distinctive feature | MEV redistribution? |
|---|---|---|---|---|
| **Jito** | [[solana\|Solana]] | JitoSOL | Largest Solana LST; native MEV auction + BAM | Yes (core edge) |
| Marinade | Solana | mSOL | Early Solana LST; native + liquid staking | Limited |
| SolBlaze | Solana | bSOL | Smaller LST; ecosystem-focused | Limited |
| Lido | [[ethereum\|Ethereum]] | stETH | Dominant Ethereum LST (different chain) | Via MEV-Boost relays |

Jito's moat is the combination of the **largest Solana LST** with **ownership of the MEV supply chain** (validator client + Block Engine + BAM). Marinade and SolBlaze compete for staking share but lack Jito's MEV-auction infrastructure and its near-universal validator-client penetration — the structural edge that lets JitoSOL pay higher yield than vanilla staking.

---

## Risks

- **Dilution:** ~0.49 MC/FDV — roughly half of supply still to unlock; uncapped max supply allows governance-driven inflation.
- **Validator-client concentration:** a bug in Jito's client could affect a large share of Solana's validator set (95%+ run it).
- **MEV regulation:** MEV extraction is controversial; regulatory action could undercut Jito's value proposition.
- **Competition:** Marinade, SolBlaze and new entrants compete for Solana LST share.
- **SOL beta / market regime:** JTO is high-beta to [[solana]] and the broad market; the current Established Bear Market amplifies downside.
- **No direct fee accrual to token:** JTO is governance, not a dividend; value capture depends on future DAO decisions.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.jito.network/](https://www.jito.network/) |
| **Twitter** | [@jito_sol](https://twitter.com/jito_sol) |
| **Discord** | [https://discord.gg/jitocommunity](https://discord.gg/jitocommunity) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. With ~half of supply unvested, locked allocations (team/investors/ecosystem) dominate the cap table. This section will be populated from on-chain sources as they are ingested.*

---

## Trading Profile

### Venues & liquidity

JTO trades on a deep, two-venue derivatives market. **Binance** lists JTO spot (JTO/USDT) plus a **USD-margined perpetual**, giving it the tightest books and the deepest funding/OI liquidity, while **[[hyperliquid|Hyperliquid]]** runs **JTO-PERP** at up to **~40-50x** leverage for on-chain leveraged and short expression. Broad additional CEX coverage (Kraken, Upbit/KRW, Bitget, KuCoin) adds episodic Korean-retail beta. Because the same contract is quoted on both a CEX and Hyperliquid, cross-venue funding and basis dislocations are directly tradable, and the redundant venues let size be split for lower impact — but as a rank ~134 alt, depth still thins fast versus majors, so ladder entries and size against L2 book depth rather than headline notional.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — same JTO perp on Binance (USD-margined) and Hyperliquid lets you harvest funding-rate gaps between the two venues.
- [[cash-and-carry]] — pair Binance JTO spot long against a short perp to capture basis/funding on an asset that trades spot + perp on the same exchange.
- [[crowded-long-funding-fade]] — after a vertical move like the +32.7% weekly rally, fade crowded longs when JTO-PERP funding turns richly positive.
- [[liquidation-cascade-fade]] — high-beta, ~88%-off-ATH JTO produces sharp forced-liquidation flushes; fade the overshoot as the cascade exhausts.
- [[oi-confirmed-trend]] — use rising Hyperliquid open interest to confirm (or veto) JTO's Solana-beta directional trends.
- [[pairs-trading]] — trade JTO against SOL to isolate the staking/MEV beta from broad market direction.

### Volatility & regime character

JTO is a **high-beta DeFi / liquid-staking infrastructure token** and a leveraged proxy on [[solana]] — more SOL staked and more on-chain MEV → more value under JitoSOL/DAO control, so JTO amplifies SOL's directional swings. It carries strong positive correlation to SOL and, through it, to broad crypto (BTC/ETH) risk-on/risk-off regimes, with realized volatility well above large-cap majors. Moves are reflexive and narrative-driven (LST/MEV cycle, Solana activity), as the recent >3x rally off the February 2026 low into an extreme-fear macro illustrates.

### Risk flags

- **Dilution / unlocks:** ~0.49 MC/FDV means roughly half of supply is still unvested; scheduled unlock cliffs impose structural sell pressure, and the uncapped max supply allows governance-driven inflation.
- **Narrative & SOL dependence:** value is tightly coupled to Solana activity and the LST/MEV narrative; a Solana risk-off drags JTO harder than the market.
- **Liquidity depth:** healthy volume for its cap, but rank ~134 books thin quickly — venue concentration on Binance/Hyperliquid means outages or delistings would sharply cut executable size.
- **Perp funding dislocations:** thin two-venue perp liquidity can push funding and basis to extremes during crowded moves, raising squeeze risk on both crowded-long fades and shorts.
- **No direct fee accrual:** JTO is a governance claim, not a dividend — a valuation risk independent of price action.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=JTO` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=JTO` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=JTO&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=JTO&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=JTO"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]
- [[liquid-staking]] — the DeFi category Jito operates in
- [[mev]] — the value source underpinning JitoSOL's yield edge
- [[kamino]] — leveraged JitoSOL staking strategies
- [[jupiter-exchange-solana]] — JitoSOL trading venue
- [[raydium]] — JitoSOL LP pools

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- CoinGecko / cryptodataapi.com snapshot, 2026-06-20 (market data baseline)
- [Blockworks — Jito launches BAM on Solana mainnet](https://blockworks.co/news/jito-bam-solana-mainnet)
- [Datawallet — Jito Explained: JitoSOL, Bundles, Restaking & BAM](https://www.datawallet.com/crypto/jito-and-jitosol-explained)
- [Solana Compass — Jito project review](https://solanacompass.com/projects/jito)
- Verified via web search, 2026-06-11

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 498.99M JTO |
| **Total Supply** | 1.00B JTO |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $599.25M |
| **Market Cap / FDV Ratio** | 0.50 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $6.01 (2023-12-07) |
| **Current vs ATH** | -90.03% |
| **All-Time Low** | $0.2181 (2026-02-06) |
| **Current vs ATL** | +174.88% |
| **24h Change** | -2.96% |
| **7d Change** | -5.82% |
| **30d Change** | -20.16% |
| **1y Change** | -68.85% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | JTO/USDT | N/A |
| Kraken | JTO/USD | N/A |
| Upbit | JTO/KRW | N/A |
| Bitget | JTO/USDT | N/A |
| KuCoin | JTO/USDT | N/A |
| Crypto.com Exchange | JTO/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | JTOJTOMEPA8BEP8AUQC6EXT5FRIJWFFMWQX2V2F9MCL/J1TOSO1UCK3RLMJORHTTRVWY9HJ7X8V9YYAC6Y7KGCPN | Spot |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $33.76M |
| **Market Cap Rank** | #134 |
| **24h Range** | $0.5991 — $0.6353 |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
