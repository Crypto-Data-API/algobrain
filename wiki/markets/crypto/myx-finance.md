---
title: "MYX Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives]
aliases: ["MYX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.myx.finance/en"
related: ["[[bnb]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[defi]]", "[[dydx]]", "[[funding-rate]]", "[[gmx]]", "[[hyperliquid]]", "[[perpetual-futures]]"]
---

# MYX Finance

**MYX Finance** (MYX) is a [[decentralized-exchange|decentralized exchange]] focused on [[perpetual-futures|perpetual futures]] trading, primarily deployed in the [[bnb|BNB Chain]] ecosystem. It lets traders open leveraged long and short positions on crypto assets non-custodially, with all positions and collateral settled on-chain rather than through a centralized intermediary. MYX is the protocol's native [[governance-token|governance]] and incentive token.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, MYX traded at **$0.113885**, ranked **#783** by market capitalization with a market cap of roughly **$21.83M**. The token has been under heavy pressure: **-12.72% over 24 hours** and **-36.86% over the trailing 7 days**, a sharp drawdown that comes amid broadly fearful market conditions (Fear & Greed Index at 22, "Extreme Fear", with [[bitcoin]] near $64,180). This continues a steep decline from the token's all-time high of roughly $19 set in September 2025 — current levels sit more than 98% below that peak. Readers should treat MYX as a high-volatility, deeply drawn-down micro-cap.

---

## What MYX Finance Does

MYX Finance is a [[derivatives]] venue in the on-chain [[perpetual-futures]] category — the same broad space occupied by protocols such as GMX, dYdX, and [[fulcrom|Fulcrom]]. Perpetual futures ("perps") are leveraged contracts with no expiry date; a [[funding-rate|funding rate]] mechanism periodically transfers payments between longs and shorts to keep the contract price tethered to the underlying spot price. MYX aims to deliver this experience on-chain so traders retain custody of their collateral and can verify positions transparently.

The protocol gained early visibility through a Binance Wallet IDO (initial DEX offering) and a listing within the broader BNB Chain DeFi ecosystem.

---

## Mechanism and Architecture

On-chain perpetual DEXs typically use one of two designs, and MYX sits in the pool/oracle-priced family rather than a pure central-limit-order-book model:

- **Pooled liquidity / oracle pricing** — liquidity providers deposit assets into a shared pool that acts as the counterparty to traders. Trade prices are sourced from external oracles rather than from an internal order book, which reduces price impact for the trader (the protocol advertises low-slippage execution) but transfers directional risk to the liquidity pool.
- **Leverage and liquidations** — traders post collateral and select leverage; positions that breach maintenance-margin thresholds are liquidated, with the pool and liquidators absorbing the mechanics. This is closely related to how an [[automated-market-maker|AMM]]-style or pool-backed perp venue manages risk.

Because the pool is the counterparty, the health of a pooled-liquidity perp DEX depends on balanced long/short open interest and an effective funding mechanism; persistent one-sided positioning is a structural risk to liquidity providers.

### Architecture deep-dive: MPM and execution

MYX markets a proprietary **MPM (Matching Pool Mechanism)** design intended to combine pooled-liquidity depth with order-book-like pricing. The salient features of an oracle/pool-priced perp DEX in this family:

- **Zero/low price-impact execution** — because fills are priced off external oracle feeds rather than walking an internal order book, a trader's slippage is minimal regardless of size (up to pool limits). This is the headline UX advantage versus thin on-chain CLOBs.
- **Pool as counterparty** — the liquidity pool takes the other side of aggregate trader positioning. The pool profits from fees and from trader losses but bears the directional risk when traders are net-correctly-positioned; this is the same global-LP risk model as [[gmx|GMX]]'s GLP.
- **[[funding-rate|Funding]] + dynamic fees** — funding payments and dynamic open/close fees are the levers that nudge open interest back toward balance and compensate the pool for skew, since there is no natural maker on the other side to absorb imbalance.
- **Cross-chain reach** — MYX is associated primarily with the [[bnb|BNB Chain]] ecosystem (and has pursued multi-chain deployment), targeting the high-retail-traffic BNB user base seeded via its Binance Wallet IDO.

The key structural tension of this design: **oracle-priced, low-slippage execution is great for traders but transfers adverse selection and skew risk onto the pool/LPs.** Sustainable economics require funding/fees to fully price that risk; otherwise informed flow extracts value from passive LPs.

---

## Token Role: MYX

MYX is the protocol's [[governance-token|governance token]]. Across on-chain perp DEXs, native tokens commonly serve three overlapping purposes, and MYX is positioned in this mold:

- **Governance** — voting on protocol parameters, supported markets, and treasury use.
- **Incentives / liquidity mining** — rewarding liquidity providers and active traders to bootstrap volume.
- **Fee and revenue alignment** — capturing a share of trading-fee revenue, often via staking, to align long-term holders with protocol usage.

Supply is capped at 1.00B MYX, with a circulating supply that is a fraction of the maximum, meaning future emissions and unlocks are a material consideration for valuation. (Exact circulating-supply and FDV figures shift with each market snapshot and should be re-verified at source.)

---

## Competitive Position

The on-chain perpetuals niche is crowded and competitive. MYX competes for the same leveraged-trading flow as established venues like [[gmx|GMX]] and [[dydx|dYdX]], alongside other BNB Chain and multi-chain perp DEXs. Its differentiation pitch centers on low-fee, low-price-impact execution within the high-traffic BNB Chain ecosystem and a retail-friendly onboarding path (the Binance Wallet IDO). However, perpetual-DEX market share is highly concentrated among a few leaders, and smaller venues face an ongoing battle for liquidity depth and trader retention.

### Comparison vs Perp-DEX Peers

| Venue | Chain(s) | Model | Token | Notes |
|---|---|---|---|---|
| **MYX Finance** | [[bnb\|BNB Chain]] (+ multi-chain) | Pool/oracle-priced (MPM) | MYX | Low price-impact pitch; Binance Wallet IDO; deep drawdown |
| **[[hyperliquid\|Hyperliquid]]** | Own L1 (HyperEVM) | On-chain CLOB | HYPE | **Leading on-chain perp venue** as of mid-2026 |
| **[[gmx\|GMX]]** | [[arbitrum\|Arbitrum]] / [[avalanche\|Avalanche]] | Pool (GLP) + oracle | GMX | Reference pool-backed perp model |
| **[[dydx\|dYdX]]** | dYdX Chain ([[cosmos\|Cosmos]]) | Off-chain CLOB / on-chain settlement | DYDX | Appchain order-book perps |

The competitive reality in 2026 is that **[[hyperliquid|Hyperliquid]] has consolidated the on-chain perp narrative** (it is the leading on-chain perp venue per the current market snapshot), raising the bar for every challenger. MYX's pool/oracle model resembles GMX's more than the CLOB leaders', and its edge is narrowest precisely where liquidity and trader trust matter most.

### Value Accrual & Governance

MYX is the protocol's [[governance-token|governance token]], with the three standard perp-DEX roles: **governance** (parameters, listed markets, treasury), **incentives/liquidity mining** (rewarding LPs and traders to bootstrap volume), and **fee/revenue alignment** (capturing a share of trading-fee revenue, typically via staking, to tie holders to usage). The value question is whether real trading-fee revenue — net of the emissions used to attract that volume — actually accrues to stakers. With circulating supply a fraction of the 1.00B max, the unlock schedule is a material overhang on any fee-based value accrual.

---

## Risks

- **Severe recent drawdown / momentum risk** — MYX fell **~36.9% in the trailing 7 days** and **~12.7% in 24 hours** to 2026-06-21, and trades more than 98% below its 2025 all-time high. This signals weak demand, potential unlock/sell pressure, and elevated volatility.
- **Micro-cap liquidity** — at a ~$21.8M market cap (rank #783), the token is thinly capitalized; large orders can move price sharply and exit liquidity can evaporate in stress.
- **Smart-contract and oracle risk** — as with any [[defi]] derivatives protocol, bugs, exploits, or oracle manipulation can cause losses; verify audit status independently.
- **Counterparty/pool risk** — in pooled-liquidity perp designs, liquidity providers bear directional and funding risk; imbalanced open interest can impair the pool.
- **Leverage risk for users** — perpetual trading with leverage can result in rapid liquidation and total loss of collateral.
- **Emissions / unlock overhang** — a large gap between circulating and max supply implies future dilution.

> **Data disclaimer:** Figures above are point-in-time market snapshots (2026-06-21) and qualitative descriptions of mechanism. TVL, trading volume, APY, and audit details are not independently verified here and should be confirmed against official documentation and on-chain analytics before any decision.

---

## Platform & Chain Information

**Native Chain:** [[bnb|BNB Chain]] (Binance Smart Chain)

### Contract Addresses

| Chain | Address |
|---|---|
| BNB Chain | `0xd82544bf0dfe8385ef8fa34d67e6e4940cc63e16` |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Max Supply** | 1.00B MYX |
| **Total Supply** | 1.00B MYX |

*Note: circulating supply and FDV change with each snapshot; re-verify at source.*

---

## How & Where It Trades

- **The MYX token** trades as a small-cap on centralized exchanges (the Binance Wallet IDO seeded early distribution and BNB-ecosystem listings). At a ~$21.8M cap (rank #783) it is a thinly capitalized micro-cap — exit liquidity is fragile and large orders move price sharply.
- **The MYX protocol** offers leveraged perpetual trading on-chain via its [[bnb|BNB Chain]] deployment; traders deposit collateral and open positions against the liquidity pool.
- **Low float / unlock overhang** — circulating supply is well below the 1.00B max, so scheduled unlocks are a recurring catalyst for drawdowns. The ~37% weekly fall into 2026-06-21 is consistent with a token under distribution/unlock pressure.
- **No leverage on the token itself recommended** given micro-cap liquidity; the protocol's *product* (perps) is leveraged but distinct from the token.

---

## Narrative, Category & Catalysts

MYX sits in the **on-chain perpetuals / DeFi derivatives** narrative within the [[bnb|BNB Chain]] ecosystem. **Catalysts:** rising protocol trading volume and fee revenue, new market listings, additional chain deployments, a staking/fee-share activation, and any broad rotation back into perp-DEX tokens. **Headwinds (dominant as of mid-2026):** [[hyperliquid|Hyperliquid]]'s consolidation of the on-chain-perp narrative, the token's severe drawdown and weak momentum, unlock-driven dilution, and the Extreme-Fear macro regime.

---

## History / Timeline

- **2025-09 (approx.)** — MYX reached an all-time high near **~$19**; current levels sit more than 98% below that peak.
- **2026-04-09** — MYX appears in the CoinGecko top-1000 snapshot used to seed this page ([[bnb|BNB Chain]] perp DEX).
- **2026-06-21** — Market snapshot: ~$21.83M cap, price $0.113885, **-12.72% over 24h** and **-36.86% over 7 days** — a sharp drawdown amid Extreme Fear.
- **2026-06-23** — Macro regime read: Extreme Fear (F&G 21), long-horizon Bottoming/Accumulation.

> Only dated events confirmed in ingested snapshots/sources are listed (the ATH timing is approximate per the existing page note). Project milestones (audits, IDO date, listings) are not independently verified here.

---

## Trading Playbook (Bear / Extreme-Fear, Bottoming Regime)

Context: 2026-06-23 — **Extreme Fear** (F&G 21), long-horizon **Bottoming / Accumulation**; Hyperliquid leads on-chain perps.

- **This is a falling knife, not a value dip.** Down ~37% in a week and >98% from ATH with an unlock overhang — momentum and supply both point down. In a bottoming regime, deeply impaired micro-caps in active distribution are among the riskiest holds; wait for a confirmed trend reversal (price stabilization + rising volume) rather than averaging into the decline.
- **Distinguish token from protocol.** Strong protocol usage (volume, fees) can exist even while the token bleeds from unlocks — track real fee revenue as the fundamental signal, separate from price.
- **Liquidity / sizing:** at ~$21.8M cap, assume you cannot exit at quoted price under stress; size for total-loss tolerance and avoid leverage on the token.
- **Competitive invalidation:** Hyperliquid (and GMX/dYdX) hold the liquidity and trust; if MYX cannot show growing, differentiated volume, there is no fundamental case regardless of price.
- **Watch the unlock calendar** before any allocation — cliffs are the most predictable near-term downside catalyst.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.myx.finance/en](https://www.myx.finance/en) |
| **Twitter** | [@MYX_Finance](https://twitter.com/MYX_Finance) |
| **Telegram** | [MYX_Finance](https://t.me/MYX_Finance) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[perpetual-futures]]
- [[decentralized-exchange]]
- [[fulcrom]]
- [[defi]]
- [[hyperliquid]]
- [[gmx]]
- [[dydx]]
- [[funding-rate]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge; no additional specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MYX |
| **Market Cap Rank** | #972 |
| **Market Cap** | $14.48M |
| **Current Price** | $0.0759 |
| **Categories** | Decentralized Finance (DeFi), Derivatives, Perpetuals, Binance Wallet IDO |
| **Website** | [https://www.myx.finance/en](https://www.myx.finance/en) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $19.03 (2025-09-11) |
| **Current vs ATH** | -99.60% |
| **All-Time Low** | $0.0470 (2025-06-19) |
| **Current vs ATL** | +62.76% |
| **24h Change** | +8.28% |
| **7d Change** | +6.56% |
| **30d Change** | -53.30% |
| **1y Change** | +6.52% |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | MYX/USD | N/A |
| Bitget | MYX/USDT | N/A |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $10.65M |
| **Market Cap Rank** | #972 |
| **24h Range** | $0.0692 — $0.0767 |
| **CoinGecko Sentiment** | 33% positive |
| **Last Updated** | 2026-07-16 |

---
