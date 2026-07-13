---
title: "Curve DAO (CRV)"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, arbitrage]
aliases: ["CRV", "Curve", "Curve Finance", "Curve-Finance", "Curve DAO Token"]
entity_type: protocol
founded: 2020
headquarters: "Decentralized"
website: "https://curve.finance"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoins]]", "[[curve-finance]]", "[[2023-07-curve-finance-exploit]]", "[[curve-gauge-wars-arbitrage]]", "[[hyperliquid]]"]
---

# Curve DAO (CRV)

**Curve DAO Token** (CRV) is the governance and incentive token of Curve Finance, the dominant stablecoin-focused [[automated-market-maker|automated market maker]] (AMM) and [[decentralized-exchange|decentralized exchange]] on [[ethereum|Ethereum]], launched by Michael Egorov in 2020. Curve is core DeFi plumbing — its pools anchor [[stablecoins|stablecoin]] liquidity and its veCRV "gauge wars" created an entire meta-game of bribe markets (Convex, Votium). For traders, CRV is a DeFi blue-chip beta with deep perp liquidity and a long history of governance- and founder-driven volatility events.

---

## Market Data

| Metric | Value |
|---|---|
| **Current Price** | $0.213759 |
| **Market Cap** | $326,506,555 (~$326.5M) |
| **Market Cap Rank** | #134 |
| **Fully Diluted Valuation (FDV)** | $511,636,100 (~$511.6M) |
| **24h Volume** | $30,594,503 (~$30.59M) |
| **24h Change** | -0.72% |
| **7d Change** | -8.54% |
| **Circulating Supply** | 1,526,582,368 CRV (~1.527B) |
| **Total Supply** | 2,392,156,103 CRV (~2.392B) |
| **Max Supply** | 3,030,303,031 CRV (~3.03B) |
| **MC / FDV Ratio** | ~0.64 |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: the snapshot lands in a risk-off tape — the crypto Fear & Greed Index reads **23 (extreme fear)** amid an **"Established Bear Market"** regime. CRV is roughly flat on the day (-0.72%) but down ~8.5% on the week, and it has just printed a **new on-chain all-time low of $0.171683 on 2026-06-06**, breaking the prior 2024 liquidation-era trough. As a high-beta mid-cap DeFi token, CRV typically amplifies broad [[crypto-markets|crypto-market]] drawdowns and lags on recoveries.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CRV |
| **Rank tier** | Mid-cap DeFi, #134 (~$326.5M cap) — as of 2026-06-20 |
| **Chain** | Ethereum native; deployed across 10+ chains (Arbitrum, Base, Optimism, Polygon, Fantom, etc.) |
| **Sector** | DeFi: stableswap AMM, stablecoin issuer (crvUSD), lending (Llamalend) |
| **Supply mechanics** | ~1.5-1.6B circulating of 3.03B max; ongoing emissions to liquidity gauges, ~45%+ of circulating locked as veCRV |
| **Protocol scale (2025)** | ~$126B annual trading volume; average TVL ~$3.05B (up from $119B / $2.86B in 2024) |
| **Founder** | Michael Egorov |
| **Website** | [https://curve.finance](https://curve.finance) |

---

## Overview

Curve Finance is an AMM-based decentralised exchange that, unlike Uniswap, focuses on swaps between assets meant to trade at par (stablecoins, wrapped/synthetic assets, liquid staking tokens). Its stableswap invariant delivers minimal slippage on like-for-like swaps, making pools like 3CRV (DAI/USDT/USDC) foundational DeFi liquidity. Pool imbalances create recurring **arbitrage** opportunities, and LPs stack swap fees, CRV emissions, and (for yield-bearing pools) underlying yield.

The **veCRV** model (vote-escrowed CRV, locked up to 4 years) directs CRV emissions via gauge votes — spawning the "Curve Wars" in which protocols (notably Convex) accumulate voting power and pay bribes for emissions, a tradable meta-game documented in [[curve-gauge-wars-arbitrage]].

### Key history and 2025-2026 developments

- **July 2023** — Vyper-compiler reentrancy exploit drained ~$70M from several pools (see [[2023-07-curve-finance-exploit]]); CRV crashed and nearly triggered liquidation of founder Michael Egorov's ~$100M CRV-collateralized loans.
- **August 2024** — CRV printed its all-time low ($0.18, 2024-08-05) amid the Egorov liquidation overhang unwind.
- **crvUSD** — Curve's overcollateralized stablecoin with the LLAMMA soft-liquidation mechanism remains central; a 2026 DAO proposal mints 5M crvUSD directly into the sreUSD Llamalend market to expand utility and DAO yield.
- **September 2025** — Egorov pitched **Yield Basis**, a ~$60M plan (funded by minting crvUSD) for leveraged Bitcoin LP pools claiming to eliminate impermanent loss; up to 65% of revenue would flow to veCRV holders and 25% of Yield Basis tokens to the Curve ecosystem.
- **2025 year in review** — volumes grew to ~$126B (from $119B in 2024), average TVL ~$3.05B; described by the team as a consolidation year ahead of 2026 expansion.
- **2026 roadmap** — **Llamalend V2** (early 2026): expanded lending framework with borrow-limit risk steering and removal of the strict crvUSD-only borrowable-asset dependency; plus on-chain FX markets. Egorov proposed a **17.45M CRV development grant** to fund a 25-person core team, and the DAO has voted on sharing protocol revenue directly with CRV holders — a potential value-accrual catalyst.
- **April 2026** — viral claims that Egorov "pulled $100M from CRV to buy mansions leaving bad debt" circulated and were fact-checked as misleading (conflating the 2023-24 loan episodes). Founder-leverage headlines remain a recurring CRV volatility source.

(Source: Curve News, CoinDesk, crypto.news; verified via web search 2026-06-10.)

---

## Protocol & Technology

Curve is a multi-product DeFi suite built around a family of specialized [[automated-market-maker|AMM]] invariants plus a stablecoin and a lending stack. The CRV token sits at the center as the emissions and governance unit.

### StableSwap invariant

Curve's original innovation is the **StableSwap invariant**, a hybrid of the constant-sum (`x + y = k`) and constant-product (`x · y = k`) curves. Near the balance point it behaves like constant-sum, delivering near-zero slippage for assets that should trade at par ([[stablecoins]], wrapped/synthetic assets, LSTs); as a pool drifts toward imbalance it smoothly transitions to constant-product to preserve a non-zero price floor and prevent the pool from being fully drained. An amplification coefficient `A` tunes how "flat" the curve is. This is what makes pools like **3CRV (DAI/USDT/USDC)** foundational [[ethereum|Ethereum]] liquidity and a recurring **arbitrage** venue when pools imbalance. Curve later added **CryptoSwap (V2)** — a separate invariant for volatile, uncorrelated pairs (e.g. tricrypto: USDT/WBTC/ETH) using internal price oracles and concentrated liquidity around an EMA price.

### crvUSD and LLAMMA soft-liquidation

**crvUSD** is Curve's overcollateralized [[stablecoins|stablecoin]]. Its defining feature is **LLAMMA** (Lending-Liquidating AMM Algorithm): instead of a single hard liquidation price, a borrower's collateral is spread across a band of price ranges and is *continuously* and *partially* converted between collateral and crvUSD as price moves through those bands — a "soft liquidation." This dampens the cliff-edge cascades typical of CDP systems. A **PegKeeper** mechanism and a market-driven borrow rate ([crvUSD borrow-rate dynamics](https://news.curve.finance/inside-crvusd-borrow-rate/)) defend the peg. crvUSD revenue (borrow interest) accrues to the DAO and, increasingly, toward veCRV/CRV value capture.

### veCRV vote-escrow and gauge emissions

CRV is emitted continuously on a decaying schedule to **liquidity gauges**. Holders lock CRV for up to **4 years** to receive **veCRV** (vote-escrowed CRV, non-transferable, decaying with time-to-unlock). veCRV confers: (1) **gauge voting** power that directs the next epoch's CRV emissions; (2) a **boost** of up to 2.5× on the voter's own LP rewards; and (3) a share of protocol/admin fees. Because controlling gauge votes lets a protocol cheaply direct emissions to its own liquidity, third parties (notably **Convex**) accumulate veCRV and run **bribe markets** (Votium) — the tradable "Curve Wars" meta-game documented in [[curve-gauge-wars-arbitrage]].

### Llamalend lending

**Llamalend** is Curve's isolated-market lending stack, also built on LLAMMA soft-liquidation, originally constrained to crvUSD as the borrowable asset. The **Llamalend V2** roadmap (early 2026) expands this into a general lending framework with borrow-limit risk steering and removes the crvUSD-only dependency, alongside planned on-chain **FX markets**.

### Multichain footprint

CRV is Ethereum-native but deployed across 10+ chains (Arbitrum, Base, Optimism, Polygon, Fantom and more), with pools and gauges bridged so that the gauge/emissions system spans L2s as well as mainnet.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 1,526,582,368 CRV (~1.527B) — 2026-06-20 |
| **Total Supply** | 2,392,156,103 CRV (~2.392B) |
| **Max Supply** | 3,030,303,031 CRV (~3.03B) |
| **MC / FDV Ratio** | ~0.64 |
| **Emissions** | Gradually decaying gauge emissions; large veCRV lock base dampens effective float |
| **Value accrual** | Admin/swap fees + crvUSD borrow revenue to veCRV; DAO votes on direct CRV revenue-sharing (2026) |

**Dilution read:** with circulating at ~1.527B and max at ~3.03B, **MC/FDV ≈ 0.64** — roughly a third of the eventual supply is still to be emitted via gauges, so CRV carries a persistent structural emissions overhang. The counterweight is the large **veCRV lock base** (a meaningful share of circulating supply is time-locked for up to four years), which removes tokens from liquid float and gives long-term holders a claim on fees and emission direction. The 2026 governance push to **share protocol revenue directly with CRV holders** (plus the proposed **17.45M CRV development grant**) is the key swing factor for whether net value accrual outpaces dilution.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $15.37 (2020-08-14, launch float squeeze) |
| **All-Time Low (current)** | $0.171683 (2026-06-06, on-chain ATL set in the 2026 bear) |
| **Prior low (historical)** | $0.1804 (2024-08-05, Egorov liquidation aftermath) — superseded by the June 2026 ATL |
| **Snapshot (2026-04-09)** | $0.2151, ~$322M mcap, rank #128 |
| **Snapshot (2026-06-20)** | $0.213759, ~$326.5M mcap, rank #134 |

Note: the **2026-06-06 print of $0.171683 is a fresh all-time low**, breaking the prior $0.1804 (Aug 2024) trough from the Egorov-liquidation episode. CRV has since reclaimed the ~$0.21 area but remains ~98.6% below its 2020 ATH.

---

## Ecosystem & Use Cases

- **Stablecoin / pegged-asset liquidity hub** — 3CRV and successor stable pools are reference liquidity for [[stablecoins]], LSTs, and wrapped assets across [[ethereum|Ethereum]] and L2s; other protocols route swaps and bootstrap pegs here.
- **crvUSD issuance** — borrowers mint crvUSD against blue-chip collateral with LLAMMA soft-liquidation, adding a Curve-native stablecoin to the DeFi stack.
- **Llamalend money market** — isolated lending markets (expanding under Llamalend V2) for leverage and yield.
- **veCRV governance & bribe economy** — protocols accumulate veCRV (directly or via Convex) to steer emissions; bribe markets (Votium) turn vote power into a yield instrument — see [[curve-gauge-wars-arbitrage]].
- **Yield Basis (proposed)** — leveraged BTC LP pools (funded by minting crvUSD) aiming to neutralize impermanent loss, routing up to 65% of revenue to veCRV holders.
- **Arbitrage venue** — pool imbalances and cross-venue spreads make Curve a standing target for [[arbitrage]] and MEV searchers.

---

## Market Structure & Derivatives

- **Spot venues**: Binance, Kraken, Bitget, KuCoin and other major CEXs; deep on-chain liquidity via Uniswap V3 and Curve's own pools. CRV is one of the more liquid mid-cap DeFi tokens (24h volume ~$30.6M on 2026-06-20).
- **Perpetuals**: CRV-PERP on [[hyperliquid|Hyperliquid]] plus CRV perps on all major CEX derivatives venues.
- **Metrics to watch (no fixed values — read live)**: perp **funding rate** (persistently negative funding flags crowded shorts and squeeze risk; positive funding flags crowded longs), **open interest** vs spot volume (OI spikes around founder-leverage headlines and governance votes), and CEX/DEX **basis**. Because CRV history is dominated by leveraged-liquidation events, OI and funding extremes are higher-signal here than for most mid-caps.

---

## Valuation Framework

CRV is best framed as a **cash-flow-bearing DeFi infrastructure token** whose value increasingly tracks protocol economics rather than pure emissions narrative. Metrics to monitor (describe and pull live — do not assume fixed numbers):

- **Protocol revenue / fees** — swap (admin) fees plus **crvUSD borrow interest**; the share routed to veCRV (and, pending governance, directly to CRV) is the core accrual lever.
- **TVL** — average TVL was reported ~$3.05B for 2025 (up from ~$2.86B in 2024); TVL and its stable-vs-volatile mix gauge fee-generating capacity.
- **Annual trading volume** — ~$126B in 2025 (vs ~$119B in 2024); volume × fee rate ≈ swap-fee revenue.
- **crvUSD outstanding & borrow rate** — supply and PegKeeper health drive interest revenue.
- **veCRV lock ratio & average lock duration** — measures float removed from market and conviction of long-term holders.
- **MC/FDV (~0.64)** — gauges remaining emission dilution against current cap.
- **P/F (price-to-fees) vs peers** — compare against [[uniswap]], [[balancer]] and other DEX tokens; CRV historically trades cheap on fees but carries higher emissions and key-man risk.

---

## Trading Relevance

- **Where it trades**: perps on [[hyperliquid|Hyperliquid]] (CRV-PERP) and all major CEX perp venues; spot on Binance, Kraken, Bitget, KuCoin; deep Uniswap V3 liquidity. One of the most liquid mid-cap DeFi tokens (~$55M/day at April snapshot).
- **Narrative basket**: **DeFi blue-chip basket** (AAVE, UNI, MKR/SKY, CRV) — CRV is typically the high-beta laggard of the group. Also a stablecoin-infrastructure proxy via crvUSD.
- **Recurring setups**: founder-leverage headline shocks (Egorov loans), gauge/bribe yield dislocations ([[curve-gauge-wars-arbitrage]]), pool-imbalance arbitrage, and governance catalysts (fee-share votes, Yield Basis rollout, Llamalend V2 launch).
- **Catalysts 2026**: revenue-sharing to CRV holders, Yield Basis launch and BTC pool traction, Llamalend V2, on-chain FX rollout, 17.45M CRV dev-grant vote outcome.
- **Risks**: persistent emissions, smart-contract/exploit history, Egorov key-man and leverage risk, and competition from Uniswap V4 hooks and Fluid/Ekubo-style next-gen AMMs.

### Trading Playbook

- **Regime context (2026-06-20)**: extreme fear (F&G 23) + Established Bear Market. CRV just set a new ATL ($0.171683, 2026-06-06) and bounced ~25% off it — treat strength into resistance skeptically until the broad regime turns.
- **High-beta basket trade**: long/short CRV as the lagging leg of the DeFi blue-chip basket (AAVE, UNI, MKR/SKY); CRV tends to under-rally and over-sell vs the group, so it suits mean-reversion pairs against a stronger blue-chip.
- **Event/headline trades**: founder-leverage and bad-debt headlines (Egorov loans) are the signature CRV shock. Watch perp funding/OI for crowded positioning into and out of these events.
- **Governance catalyst trades**: position around fee-share votes, the 17.45M CRV dev-grant outcome, Yield Basis rollout, and Llamalend V2 launch — value-accrual votes are the primary positive re-rating path.
- **Structural arb (not directional)**: gauge/bribe yield dislocations and pool-imbalance arbitrage ([[curve-gauge-wars-arbitrage]]) are separate, lower-beta edges available to on-chain participants.
- **Risk controls**: size for emissions-driven grind-down and gap risk on leverage headlines; CRV's liquidation history makes hard stops and modest leverage essential.

---

## Competitive Positioning

CRV competes in the [[decentralized-exchange|DEX]]/AMM token sector. Its moat is stable/pegged-asset depth plus the veCRV emissions-direction flywheel; the threats are next-gen AMM designs and value-accrual that favors fee-rich, emission-light competitors.

| Protocol | Focus | AMM model | TVL / scale tier | Token value accrual |
|---|---|---|---|---|
| **Curve (CRV)** | Stable/pegged-asset swaps + crvUSD + Llamalend | StableSwap + CryptoSwap; veCRV gauges | Multi-billion (~$3B avg TVL 2025) | Fees + crvUSD revenue to veCRV; direct CRV revenue-share (proposed) |
| **[[uniswap]] (UNI)** | General-purpose spot DEX; volatile pairs | Concentrated liquidity (V3); V4 hooks | Largest DEX by volume/TVL | Historically weak (fee switch contested); governance |
| **[[balancer]] (BAL)** | Weighted & stable pools, programmable AMM | Generalized weighted pools; veBAL gauges | Mid-tier | Fees + emissions direction via veBAL (Curve-style) |
| **Fluid / Ekubo** | Next-gen capital-efficient AMM/lending hybrids | Novel invariants, integrated lending | Smaller but fast-growing | Varies; pitched on efficiency over emissions |

CRV's edge vs Uniswap is purpose-built stable/pegged depth and a richer fee/emissions economy; its disadvantage is heavier ongoing emissions and the recurring key-man/leverage overhang that pure-DEX peers lack.

---

## Risks

- **Emissions dilution** — ~a third of max supply still to be emitted (MC/FDV ~0.64); persistent gauge emissions create structural sell pressure unless offset by locking and revenue-share.
- **Smart-contract / exploit history** — the July 2023 Vyper reentrancy exploit (~$70M, see [[2023-07-curve-finance-exploit]]) is a concrete precedent; LLAMMA, crvUSD, and Llamalend add surface area.
- **Founder key-man & leverage risk** — Michael Egorov's large CRV-collateralized borrowing has repeatedly threatened cascade liquidations; founder-leverage headlines are a recurring volatility source.
- **Competition** — Uniswap V4 hooks and Fluid/Ekubo-style next-gen AMMs erode Curve's slippage/efficiency edge over time.
- **crvUSD / peg risk** — PegKeeper failure, bad debt in Llamalend, or LLAMMA edge cases could impair the stablecoin and DAO revenue.
- **Governance / value-accrual uncertainty** — the bullish thesis depends on votes (revenue-share, dev grant) actually passing and executing.
- **Macro / regime beta** — as a high-beta mid-cap, CRV amplifies [[crypto-markets|crypto-market]] drawdowns; the 2026-06-20 extreme-fear, Established-Bear-Market backdrop and the fresh June 2026 ATL underscore current downside sensitivity.

> **Risk disclaimer:** Nothing here is financial advice. CRV has a documented history of exploit losses and leverage-driven liquidation cascades; position sizing and leverage discipline are essential.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd533a949740bb3306d119cc777fa900ba034cd52` |
| Arbitrum One | `0x11cdb42b0eb46d95f990bedd4695a6e3fa034978` |
| Base | `0x8ee73c484a26e0a5df2ee2a4960b789967dd0415` |
| Optimism | `0x0994206dfe8de6ec6920ff4d779b0d950605fb53` |
| Polygon PoS | `0x172370d5cd63279efa6d502dab29171933a610af` |
| Fantom | `0x1e4f97b9f9f913c46f1632781732927b9019c68b` |

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://curve.finance](https://curve.finance) |
| **News** | https://news.curve.finance/ |
| **Twitter** | [@curvefinance](https://twitter.com/curvefinance) |
| **Telegram** | [curvefi](https://t.me/curvefi) |
| **GitHub** | [https://github.com/curvefi](https://github.com/curvefi) |
| **Docs** | [https://docs.curve.finance/](https://docs.curve.finance/) |

---

## Related

- [[curve-finance]] — protocol entity page
- [[2023-07-curve-finance-exploit]]
- [[curve-gauge-wars-arbitrage]]
- [[ethereum]]
- [[stablecoins]]
- [[crypto-markets]]
- [[hyperliquid]]

---

## Sources

- CoinGecko snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Curve, "2025 Year in Review": https://news.curve.finance/curve-2025-year-in-review/
- CoinDesk, "Curve Finance Pitches Yield Basis, a $60M Plan..." (2025-09-17): https://www.coindesk.com/business/2025/09/17/curve-finance-pitches-usd60m-yield-basis-plan-aiming-to-turn-crv-into-income-asset
- crypto.news, "Curve Finance founder proposes 17M CRV grant to fund 2026 development roadmap": https://crypto.news/curve-finance-founder-proposes-17m-crv-grant-to-fund-2026-development-roadmap/
- The Crypto Times fact-check on Egorov claims (2026-04-27): https://www.cryptotimes.io/2026/04/27/fact-check-did-michael-egorov-pull-100m-from-crv-to-buy-mansions-and-leave-bad-debt/
- Curve, "Inside crvUSD Borrow Rate": https://news.curve.finance/inside-crvusd-borrow-rate/
- Web search verification, 2026-06-10
