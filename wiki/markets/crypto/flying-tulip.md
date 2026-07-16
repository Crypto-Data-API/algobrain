---
title: "Flying Tulip"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives]
aliases: ["FT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://flyingtulip.com/"
related: ["[[automated-market-maker]]", "[[crypto-markets]]", "[[decentralized-finance]]", "[[ethereum]]", "[[perpetual-futures]]"]
---

# Flying Tulip

**Flying Tulip** (FT) is an all-in-one decentralized finance (DeFi) protocol associated with developer **Andre Cronje** (founder of [[yearn-finance|Yearn Finance]] and a key figure behind [[sonic]] / the former Fantom ecosystem). It aims to combine spot trading, an [[automated-market-maker|automated market maker]] (AMM), lending, and [[perpetual-futures|perpetuals]] into a single capital-efficient venue, with an adaptive-curve AMM design intended to vary liquidity concentration with volatility. FT is a multi-chain ERC-20-style token deployed across Ethereum, Sonic, BNB Chain, Base, and Avalanche.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | FT |
| **Market Cap Rank** | #231 |
| **Market Cap** | ~$122.7M |
| **Current Price** | $0.1003 |
| **24h Change** | -0.43% |
| **7d Change** | +1.58% |
| **Circulating Supply** | 1.23B FT |
| **Total Supply** | 9.99B FT |
| **Max Supply** | 10.00B FT |
| **All-Time High** | $0.2999 (≈ -66.6% from current) |
| **All-Time Low** | $0.0679 (≈ +47.7% from current) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Dilution flag:** Only ~12.3% of the 10B max supply is circulating (MC ≈ $122.7M vs. **FDV ≈ $1.0B**, MC/FDV ≈ 0.12). The bulk of supply remains unissued — future unlocks/emissions are a material overhang and a key risk for spot holders.

---

## Technology / What It Does

Flying Tulip is positioned as a unified DeFi exchange rather than a single-purpose dApp. Its stated design pillars are:

- **Adaptive-curve AMM** — a liquidity curve whose shape adjusts to realized volatility, intended to keep spreads tight in calm markets while widening to protect liquidity providers (LPs) in volatile ones. This contrasts with static constant-product ([[automated-market-maker|x·y=k]]) or fixed concentrated-liquidity ranges.
- **Integrated lending + leverage** — collateral posted into the system can back borrowing and on-chain [[perpetual-futures|perpetual]]/leverage positions, sharing one capital base across spot, margin, and derivatives.
- **Multi-chain deployment** — the same token/contract is live on Ethereum, [[sonic|Sonic]], BNB Chain, Base, and Avalanche, reflecting Cronje's cross-chain footprint.

The project's "LTV" whitepaper (flyingtulip.com/ltv.html) frames the system around dynamic loan-to-value and risk-adjusted liquidity. As of this snapshot the protocol is early-stage; treat capability claims as design goals rather than proven, audited production behavior.

### Comparison vs other on-chain trading venues

Flying Tulip's pitch is **convergence**: spot AMM + lending + perps in one capital pool, with an adaptive curve. Most incumbents specialize in one or two of those legs. The table frames where FT claims to differ:

| Protocol | Core product(s) | AMM/liquidity model | Founder / origin | Maturity |
|---|---|---|---|---|
| **Flying Tulip** | Unified spot AMM + lending + perps | Adaptive-curve (volatility-aware) | Andre Cronje ([[yearn-finance|Yearn]], [[sonic|Sonic]]) | Early-stage / pre-proven |
| **[[hyperliquid\|Hyperliquid]]** | Perps + spot (own L1 order book) | Central limit order book, not AMM | Independent team | Live, high-volume leader in on-chain perps |
| **[[gmx\|GMX]]** | Perps + spot via shared liquidity pool | GLP/multi-asset pool, oracle-priced | Independent team | Established, multi-cycle track record |
| **[[uniswap\|Uniswap]]** | Spot AMM (no native lending/perps) | Constant-product / concentrated liquidity (v3/v4) | Hayden Adams | Most-integrated spot AMM |
| **[[aave\|Aave]]** | Lending/borrowing (no native spot/perps) | Pooled money market | Stani Kulechov | Blue-chip DeFi lending |

The differentiation is real **in design** — a single capital base across spot, margin, and derivatives plus a volatility-adaptive curve — but as of this snapshot it is unproven against battle-tested specialists like Hyperliquid (perps) and Uniswap (spot). The investment case rests on execution and the founder premium, not on demonstrated fee/volume dominance.

### Value accrual & governance

How the FT token captures value from protocol activity is **not established by hard, audited tokenomics in this snapshot**; the project is early-stage and the live fee-routing/governance design should be verified against current docs before relying on it. Concretely, holders should not assume a fee-share or buyback accrual mechanism exists in production yet. With ~88% of supply uncirculated (see tokenomics), governance weight and any future value capture will also be shaped heavily by how undistributed supply is allocated.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.23B FT |
| **Total Supply** | ~9.99B FT |
| **Max Supply** | 10.00B FT |
| **FDV** | ~$1.0B |
| **MC / FDV** | ~0.12 |

With ~88% of max supply not yet circulating, FT trades at a steep discount of market cap to fully diluted valuation. Holders should track the emission/unlock schedule closely: at full dilution the same price implies an order-of-magnitude larger valuation, so future supply growth is the dominant tokenomics risk.

---

## How / Where It Trades

- **Venues:** Trades primarily on decentralized exchanges. CoinGecko data lists a Uniswap V3 (Ethereum) FT pair; additional liquidity exists across its other deployment chains (Sonic, BNB, Base, Avalanche).
- **Liquidity — thin:** 24h volume is only ~$207K against a ~$122.7M market cap (volume/MC well under 1%). This is **very thin liquidity** for a top-250 asset — large orders will move price materially and slippage risk is high.
- **Perps:** No evidence in this snapshot of FT being listed as a perpetual on a major centralized venue; the "perpetuals" association refers to the protocol's own product category, not a CEX-listed FT-perp.

---

## Narrative / Category

FT sits at the intersection of several hot narratives: the **Andre Cronje builder premium**, the **all-in-one DeFi / unified exchange** thesis, the **Sonic ecosystem** revival, and on-chain **derivatives/perps**. Its valuation is heavily reputation- and roadmap-driven rather than fee-/revenue-driven at this stage. In the current macro backdrop (Fear & Greed 22, "Established Bear Market", BTC ~$62.6K and ~18% below its 200-day MA as of 2026-06-24), speculative founder-narrative tokens like FT are especially sensitive to risk-off sentiment.

**Catalysts to watch:** mainnet/product milestones that move FT from "design goals" to live, audited volume; published audits; a transparent unlock/emissions schedule; and any sign of real fee revenue and TVL growth. The single biggest swing factor remains **Andre Cronje's continued involvement** — positive on engagement, sharply negative on any step-back, given his history.

## Trading Playbook (bear / Extreme-Fear regime)

Given the 2026-06-24 Extreme-Fear, established-bear backdrop, FT is a **high-beta, founder-narrative, dilution-heavy** small cap:

- **Dilution is the dominant risk, not direction.** With ~88% of max supply uncirculated (MC/FDV ≈ 0.12), the same price implies an ~$1.0B fully diluted valuation. Future unlocks/emissions can pressure price for years independent of fundamentals — track the emission schedule before sizing anything.
- **Thin liquidity punishes size.** ~$207K daily volume against a ~$122.7M cap (volume/MC well under 1%) means large orders move price materially; this is a token to trade small or not at all, with wide slippage assumptions.
- **Narrative beta in risk-off.** Founder-premium tokens are exactly what gets sold first in Extreme Fear. Expect FT to underperform majors in continued risk-off and to be whippy on any Cronje/roadmap headline.
- **Catalyst-driven, not carry.** There is no demonstrated fee/yield to hold for; the case is event-driven (product launches, audits, founder engagement). Treat it as a speculative roadmap bet, not an income or value position.

---

## Risks

- **Massive dilution overhang** — ~88% of supply uncirculated; emissions/unlocks could pressure price for years.
- **Thin liquidity** — ~$207K daily volume makes entry/exit costly and the token vulnerable to manipulation.
- **Execution/early-stage risk** — ambitious all-in-one scope (AMM + lending + perps) raises smart-contract and protocol-design risk; verify audits before depositing.
- **Founder/key-person risk** — value is tightly coupled to Andre Cronje; Cronje has historically stepped back from projects, which has caused sharp drawdowns elsewhere.
- **Bear-market beta** — a small-cap, high-narrative token will underperform in risk-off regimes (see macro backdrop above).

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[sonic]]
- [[decentralized-finance]]
- [[automated-market-maker]]
- [[perpetual-futures]]
- [[yearn-finance]]
- [[hyperliquid]] — leading on-chain perps venue (comparison)
- [[gmx]] · [[uniswap]] · [[aave]] — incumbents FT's unified design competes with

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Project site & whitepaper: flyingtulip.com, flyingtulip.com/ltv.html (project self-description).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FT |
| **Market Cap Rank** | #429 |
| **Market Cap** | $50.86M |
| **Current Price** | $0.0919 |
| **Categories** | Decentralized Finance (DeFi), Derivatives, Perpetuals |
| **Website** | [https://flyingtulip.com/](https://flyingtulip.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 553.19M FT |
| **Total Supply** | 9.99B FT |
| **Max Supply** | 10.00B FT |
| **Fully Diluted Valuation** | $918.15M |
| **Market Cap / FDV Ratio** | 0.06 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2999 (2026-02-23) |
| **Current vs ATH** | -69.34% |
| **All-Time Low** | $0.0679 (2026-04-22) |
| **Current vs ATL** | +35.41% |
| **24h Change** | -2.43% |
| **7d Change** | -3.39% |
| **30d Change** | -11.67% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x5dd1a7a369e8273371d2dbf9d83356057088082c` |
| Sonic | `0x5dd1a7a369e8273371d2dbf9d83356057088082c` |
| Binance Smart Chain | `0x5dd1a7a369e8273371d2dbf9d83356057088082c` |
| Base | `0x5dd1a7a369e8273371d2dbf9d83356057088082c` |
| Avalanche | `0x5dd1a7a369e8273371d2dbf9d83356057088082c` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X5DD1A7A369E8273371D2DBF9D83356057088082C/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://flyingtulip.com/](https://flyingtulip.com/) |
| **Twitter** | [@flyingtulip_](https://twitter.com/flyingtulip_) |
| **Whitepaper** | [https://flyingtulip.com/ltv.html](https://flyingtulip.com/ltv.html) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $218,632.00 |
| **Market Cap Rank** | #429 |
| **24h Range** | $0.0889 — $0.0943 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
