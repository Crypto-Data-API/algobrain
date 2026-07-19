---
title: "Triangular Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags: [arbitrage, forex, crypto, triangular, currency-pairs, algorithmic, market-neutral, cross-rate]
aliases: ["Tri Arb", "Three-Way Arbitrage", "Cross-Rate Arbitrage"]
strategy_type: algorithmic
timeframe: scalp
markets: [forex, crypto]
complexity: advanced
backtest_status: untested
edge_source: [latency, structural]
edge_mechanism: "Three currency/asset pairs on a single venue must satisfy a no-arbitrage cross-rate identity; when one quote is momentarily stale relative to the other two, a near-risk-free three-leg cycle returns to the starting asset with a small surplus. The edge is overwhelmingly a speed (latency) race to consume the stale quote before competitors."
data_required: [order-book-l2, exchange-fee-tiers, execution-latency, cross-rate-feed]
min_capital_usd: 25000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 1.5
expected_max_drawdown: 0.1
breakeven_cost_bps: 12
related: ["[[arbitrage]]", "[[cross-exchange-arbitrage]]", "[[mev-strategies]]", "[[forex]]", "[[order-book]]", "[[slippage]]", "[[latency-arbitrage]]", "[[limits-to-arbitrage]]", "[[market-efficiency]]", "[[restaking-token-arbitrage]]", "[[crisis-currency-triangular-arbitrage]]", "[[medieval-bill-of-exchange-arbitrage]]", "[[historical-cable-arbitrage]]", "[[eurodollar-triangular-arbitrage]]", "[[yen-carry-triangular-arbitrage]]", "[[crypto-spot-perp-futures-triangle]]", "[[dex-pool-triangular-arbitrage]]"]
---

# Triangular Arbitrage

## Overview

Triangular arbitrage exploits pricing inconsistencies among three related currency pairs on a single exchange. In an efficient market, the cross-rate between any three currencies should be mathematically consistent -- for example, if you know EUR/USD and USD/JPY, the implied EUR/JPY rate is determined. When the actual quoted EUR/JPY rate deviates from this implied rate, a triangular arbitrage opportunity exists. The trader executes three simultaneous trades to capture the discrepancy, ending up with more of the starting currency than they began with.

In [[forex]] markets, triangular arb opportunities are vanishingly small and last milliseconds, as banks and HFT firms enforce consistency. In [[crypto]] markets, the fragmentation of pairs and variable liquidity across tokens creates more frequent and larger opportunities -- for example, cycling through BTC/USDT -> ETH/BTC -> ETH/USDT. The strategy is almost exclusively algorithmic today, as human execution speed cannot capture these fleeting dislocations. It is the textbook example of a [[latency-arbitrage|latency-bound]] strategy and a member of the broader [[arbitrage]] family.

## Edge Source

**Latency** (dominant) with a **structural** underpinning. The structural fact is the no-arbitrage cross-rate identity: on a single venue, `mid(A/C)` must equal `mid(A/B) × mid(B/C)` net of spreads, or a riskless cycle exists. That identity is enforced *by the strategy itself*, so the residual edge is almost entirely a **speed race** — whoever consumes the stale quote first captures the surplus and erases the opportunity for everyone else. See [[edge-taxonomy]] for the framework.

## Why This Edge Exists

- **Quote staleness.** Three order books update asynchronously. When one leg re-prices a few milliseconds before another, the implied cross momentarily diverges from the quoted cross.
- **Heterogeneous participants.** Market makers on each pair optimize that pair in isolation; they do not always re-quote the third pair instantly when the other two move.
- **Fee-tier dispersion.** A maker-rebate or VIP-tier participant has a lower breakeven than a retail taker, so an opportunity that is unprofitable for one trader is profitable for another — the low-cost participant has the structural edge.
- **Listing and congestion events.** New pair listings, API congestion, and exchange outages create stale-quote windows far wider than steady-state.
- **Who is on the other side?** The market maker (or slow bot) whose quote went stale; in crypto, often a passive LP on a thin pair. They lose the few bps the fast arber extracts, and in aggregate they pay for the price-consistency the arber enforces.

## Null Hypothesis

In a perfectly synchronized, zero-latency, zero-fee market, the cross-rate identity holds exactly at every instant and triangular arbitrage returns exactly zero. The strategy's existence is therefore *evidence of microstructure friction* (asynchronous updates + latency + fees), not of mispricing in any economic sense. Under the null, observed "opportunities" net of three legs of fees and realistic fill probability average ≤ 0 — i.e., the apparent gross edge is exactly consumed by taker fees and adverse selection on partial fills. The strategy only beats the null for participants whose *latency and fee structure* sit at the top of the distribution.

## Rules

### Entry
1. **Identify three related pairs:** Choose three assets (A, B, C) where all three pairs are liquid. Example: USDT, BTC, ETH on Binance -- pairs BTC/USDT, ETH/BTC, ETH/USDT.
2. **Calculate the implied cross-rate:** Multiply the two direct rates and compare to the quoted third rate. If (BTC/USDT price) x (ETH/BTC price) != (ETH/USDT price), an arbitrage exists.
3. **Determine the profitable direction:** There are two possible paths (clockwise and counterclockwise). Calculate both:
   - **Path 1:** USDT -> BTC -> ETH -> USDT
   - **Path 2:** USDT -> ETH -> BTC -> USDT
4. **Account for fees:** Subtract the trading fee for each of the three legs (3x maker/taker fees). Only execute if the net profit after all three fees is positive.
5. **Execute all three legs simultaneously** (or as close to simultaneously as possible via API). Any delay between legs introduces risk that the prices change.

### Exit
1. **Immediate completion:** The trade is a single atomic event. Once all three legs fill, the profit (or loss) is realized.
2. **Partial fill management:** If one or two legs fill but the third does not, you have unintended exposure. Close the open position immediately at market.
3. **Continuous monitoring:** After one arb completes, continue scanning for the next opportunity. The algo runs 24/7.

### Position Sizing
Size each leg based on the minimum liquidity available across all three pairs. The bottleneck is always the least-liquid pair. Do not size larger than what the thinnest order book can absorb without significant [[slippage]].

## Indicators Used
- **Cross-rate deviation** -- the mathematical inconsistency between three pairs. This is the sole signal.
- [[order-book]] depth on all three pairs -- determines maximum executable size.
- **Fee tiers** -- exchange-specific maker/taker fees per trade. VIP tiers with lower fees make more arbs profitable.
- **Execution latency** -- round-trip API time determines whether you can capture the opportunity before it disappears.
- [[slippage]] model -- estimate fill quality at the target size for each leg.
- **Currency correlation matrix** -- identify which triplets historically produce the most frequent dislocations.

## Implementation Pseudocode

```python
# Single-venue triangular cycle scanner (latency-critical hot path)
FEE = exchange.taker_fee          # per leg, e.g. 0.0004 (4 bps)
HURDLE = 3 * FEE + safety_buffer  # must clear 3 legs of fees + slippage

def on_book_update(book):
    for (a, b, c) in candidate_triplets:        # e.g. (USDT, BTC, ETH)
        # Path 1: A -> B -> C -> A  (use executable bid/ask, not mid)
        out1 = 1.0
        out1 *= fill(book, a, b, side="buy")    # A buys B at ask
        out1 *= fill(book, b, c, side="buy")    # B buys C at ask
        out1 *= fill(book, c, a, side="sell")   # C sells to A at bid
        gross1 = out1 - 1.0

        # Path 2: reverse cycle A -> C -> B -> A
        gross2 = reverse_cycle_gross(book, a, b, c)

        gross, path = max((gross1, "P1"), (gross2, "P2"))
        if gross > HURDLE:
            size = min_depth_across_legs(book, path)   # thinnest leg caps size
            send_atomic_or_ioc(path, size)             # IOC; cancel-on-partial
            # If only 1-2 legs fill -> immediately flatten residual at market
```

Key engineering points: quote prices off the *executable* side of the book (not mid), size to the thinnest leg, use immediate-or-cancel orders, and have a deterministic unwind path for partial fills. In production the loop is co-located and the decision-to-order latency is sub-millisecond.

## Example trade

> Illustrative, round numbers — not a backtest.

**Exchange:** Binance. **Triplet:** USDT → BTC → ETH → USDT. Starting capital: $68,000 USDT.

**Quoted prices at signal:**

| Pair | Best executable price |
|------|-----------------------|
| BTC/USDT ask | $68,000 |
| ETH/BTC ask | 0.04750 |
| ETH/USDT bid | $3,240 |

**Implied cross-check:**
$68,000 × 0.04750 = $3,230 implied ETH/USDT, but the market quotes ETH/USDT bid at $3,240 — ETH is overpriced in the USDT leg by $10. Path 1 (USDT → BTC → ETH → USDT) is the profitable direction.

**Execution (three IOC orders sent in ~50ms):**

| Leg | Order | Fill | Running balance |
|-----|-------|------|----------------|
| 1. Buy BTC | Buy 1 BTC at $68,000 | Filled | 1.000 BTC |
| 2. Buy ETH with BTC | Buy 21.053 ETH at 0.04750 BTC/ETH | Filled | 21.053 ETH |
| 3. Sell ETH for USDT | Sell 21.053 ETH at $3,240 bid | Filled | $68,211.58 USDT |

**P&L breakdown:**

| Item | Amount |
|------|--------|
| Gross surplus (ending − starting) | +$211.58 |
| Taker fee leg 1 (0.04% × $68,000) | −$27.20 |
| Taker fee leg 2 (0.04% × 1 BTC × $68,000) | −$27.20 |
| Taker fee leg 3 (0.04% × $68,212) | −$27.28 |
| **Net P&L** | **+$129.90** |
| Round-trip time | ~100-300 ms |

Net $129.90 on $68,000 capital = **0.19%** per cycle. At this size, the bot could theoretically recycle the same capital 10-30 times per day across multiple triplets, but in practice the opportunity reappears only when market makers fail to re-quote the third leg promptly — frequency drops sharply as ETH/BTC or BTC/USDT spreads tighten.

**Partial-fill scenario (the main risk):** If Leg 2 only partially fills (say, 10 ETH instead of 21.053), the bot holds 10 ETH with no corresponding USDT obligation. It must immediately close the residual at market price — if ETH/USDT has already repriced back to $3,230, the unwind cost on the 11 ETH residual is ~$11, turning the net P&L negative. This is why the pseudocode above uses IOC orders and an immediate-flatten path for partial fills.

## Worked Example

Illustrative arithmetic with round numbers to show the mechanics; not a recorded trade or backtest.

**Exchange:** Binance. **Triplet:** USDT, BTC, ETH.
1. **Quoted prices:** BTC/USDT = $68,000. ETH/BTC = 0.04750. ETH/USDT = $3,240.
2. **Implied ETH/USDT via BTC:** $68,000 x 0.04750 = $3,230. But the market quotes ETH/USDT at $3,240.
3. **Discrepancy:** ETH is overpriced in USDT terms relative to the BTC cross-rate by $10 (0.31%).
4. **Profitable path:** USDT -> BTC -> ETH -> USDT.
   - **Leg 1:** Buy BTC with $68,000 USDT. Receive 1 BTC.
   - **Leg 2:** Buy ETH with 1 BTC. Receive 1/0.04750 = 21.053 ETH.
   - **Leg 3:** Sell 21.053 ETH for USDT at $3,240. Receive $68,211.58.
5. **Gross profit:** $68,211.58 - $68,000 = **$211.58 (0.31%)**.
6. **Fees:** 3 legs x 0.04% taker = 0.12% total. On $68,000 = $81.60.
7. **Net profit:** $211.58 - $81.60 = **$129.98** in approximately 100-500 milliseconds.

## Performance Characteristics

> These are *qualitative characteristics of the trade type*, not a backtest. The economics are entirely cost- and latency-determined: the gross edge per cycle is tiny and is consumed almost completely by three legs of fees plus partial-fill risk unless you sit near the top of the speed/fee distribution.

- **Win Rate:** high *when a true opportunity is correctly identified and all three legs fill before the discrepancy closes*. The dominant losses come from partial fills and stale quotes, not from a directional bet.
- **Per-cycle gross edge:** typically a few bps to tens of bps in crypto; sub-bp and fleeting in major-pair [[forex]].
- **Profit driver:** frequency × capital recycling, not size per trade. Each cycle returns to the base asset, so the same capital is reused many times per day.
- **Best Market Conditions:** High [[volatility]], rapid price changes, new pair listings, low-liquidity pairs, and exchange API congestion (creates stale quotes on some pairs).
- **Worst Market Conditions:** Calm, highly efficient markets where cross-rates are perfectly aligned. Competition from dozens of other bots compresses opportunities to zero.

### Cost / breakeven stack

| Component | Magnitude | Why it matters |
|-----------|-----------|----------------|
| Taker fee × 3 legs | e.g. 0.04% × 3 = 12 bps | The headline hurdle; VIP/maker tiers lower it sharply |
| Spread paid on each leg | leg-dependent | Thin pairs eat the edge |
| Partial-fill / unwind slippage | variable, can be large | One leg missing = unhedged exposure |
| Latency disadvantage | opportunity-cost | Slower bots see the spread vanish before they fill |

The breakeven is roughly `3 × fee + spreads + expected unwind slippage`; only opportunities exceeding that hurdle are real.

## Advantages
- **Zero directional risk:** Start and end with the same currency; no market exposure between arbs
- **Exploitable on a single exchange:** No need to transfer funds between venues, eliminating counterparty fragmentation
- **Mathematically verifiable:** The opportunity is a pure mathematical inconsistency, not a statistical bet
- **Fast capital recycling:** Each trade completes in under a second, allowing the same capital to be reused thousands of times per day
- **Self-correcting markets:** By executing arbs, the trader helps enforce price consistency (a positive externality)

## Disadvantages
- **Extremely competitive:** HFT firms and professional bots dominate. Retail traders without low-latency infrastructure cannot compete
- **Razor-thin margins:** Net profit per trade is often 0.01-0.10% after fees. Requires massive volume or frequency to be meaningful
- **Execution complexity:** Three legs must execute near-simultaneously. Partial fills create unwanted exposure
- **Fee sensitivity:** At 0.04% per leg, three legs cost 0.12%. Many apparent opportunities vanish after fees
- **Technology requirement:** Requires custom-built bots with direct API connections, real-time order book monitoring, and sub-second execution
- **Diminishing opportunities:** As crypto markets mature and market makers improve, triangular discrepancies shrink

## Capacity Limits

Single-cycle capacity is bounded by the **thinnest leg's** order-book depth at the moment of the opportunity — frequently only tens of thousands of dollars per cycle on minor crypto triplets, and far thinner in major-pair FX where banks instantly re-quote. Strategy-level capacity scales with *frequency* rather than per-trade size: a fast bot can recycle modest capital across thousands of cycles a day. Practical aggregate capacity for a dedicated low-latency crypto operation is on the order of tens of millions of dollars (frontmatter assumes ~$50M); beyond that the act of taking the stale quote moves the market and self-cannibalizes the edge.

## What Kills This Strategy

- **Latency loss.** A faster competitor co-located at the exchange consumes every real opportunity before you fill. This is the primary kill switch.
- **Fee-tier erosion.** Losing a VIP/maker tier (lower volume) raises the breakeven above the typical gross edge.
- **Market-maker improvement.** As MMs quote all three legs in lockstep, cross-rate dislocations vanish — the long-run direction of efficient markets ([[market-efficiency]]).
- **Partial-fill / leg risk.** A non-atomic cycle where one leg fails leaves an unhedged position; repeated, this turns a "risk-free" arb into a directional loss machine.
- **Venue / API risk.** Exchange downtime, withdrawal freezes, or quote-feed throttling mid-cycle. (On-chain DEX variants face MEV competition instead — see [[dex-pool-triangular-arbitrage]] and [[mev-strategies]].)
- **Crowding.** High `crowding_risk`: dozens of bots chase the same triplets, compressing opportunities to zero in calm markets.
- See [[failure-modes]] and [[limits-to-arbitrage]].

## Kill Criteria

- Rolling fill-success rate on identified cycles falls below the level where partial-fill unwinds erase net profit.
- Median realized edge per cycle drops below `3 × fee + spreads` for a sustained period (the breakeven hurdle is no longer cleared).
- Measured order-to-fill latency falls persistently behind the competitive frontier for the target venues.
- Cumulative partial-fill / leg-risk losses exceed a defined fraction of trailing arb P&L.

## Notable Historic Trades — Where Real Money Was Made

The textbook "tri-arb" mathematical inconsistency is one slice of the actual P&L space. Most of the largest historical triangular wins came from **crisis-driven cross-rate dislocations** — when one leg of the triangle becomes illiquid, mispriced, or pegged, sophisticated traders captured spreads orders of magnitude larger than the millisecond opportunities described above.

### Single-trader / single-trade legends

| Date | Trade | Trader / Firm | Reported P&L |
|------|-------|---------------|--------------|
| Oct 1987 | NZD short via FX options post-Black Monday | [[1987-andy-krieger-nzd-short\|Andy Krieger]] / Bankers Trust | ~$300M |
| Sep 1992 | GBP short during ERM exit; DEM/GBP/ITL triangulation | Soros / Druckenmiller / Quantum | ~$1B+ |
| Dec 1994 | Mexican peso short during Tequila Crisis | Tudor, Caxton, Soros | $200-500M each |
| Aug 1998 | Russian ruble + GKO short | Tudor, Caxton; LTCM lost | $200-500M (Tudor) |
| Jan 1999 | Brazilian real short | Tudor, Soros (recovered Russia loss), Caxton | $300-800M each |
| Dec 2001 | Argentine peso short + multi-decade hold-out bond trade | Macro funds 2001; Elliott (Singer) hold-out | $2.4B (Elliott on Argentina) |
| Jan 2015 | Long CHF via OTM calls before SNB un-peg | Hayman (Bass), Brevan Howard | $200-300M each |
| Aug 2018 | Short Turkish lira | Macro funds, vol funds | $100-500M cumulative |
| Sep 2022 | Short GBP + short Gilts during Truss mini-budget | Crispin Odey | £250M+ |
| Aug 2024 | Long JPY + long vol during carry unwind | Vol funds (Universa, Capstone), several macro funds | $300-800M (top funds) |

### Era-defining crises (broader macro events)

| Era | Page | Triangle Driver |
|-----|------|-----------------|
| 1992 | [[1992-black-wednesday-erm-crisis]] | ERM peg break |
| 1994 | [[1994-tequila-crisis]] | Tesobonos + peso |
| 1997 | [[asian-financial-crisis]] | Sequential EM peg breaks |
| 1998 | [[1998-08-russia-ruble-default]] | Sovereign default + FX moratorium |
| 1999 | [[1999-01-brazil-real-devaluation]] | Plano Real anchor break |
| 2001 | [[2001-12-argentina-convertibility-break]] | Currency-board collapse |
| 2015 | [[2015-01-snb-swiss-franc-unpeg]] | Floor abandoned |
| 2018 | [[2018-08-turkish-lira-crisis]] | Erdoğan-CB conflict |
| 2022 | [[2022-09-uk-mini-budget-crisis]] | Fiscal credibility shock |
| 2024 | [[2024-08-yen-carry-unwind]] | BoJ + Fed simultaneous reversal |

### Crypto-era triangular wins

| Date | Page | Setup |
|------|------|-------|
| Mar-Apr 2013 | [[2013-04-cyprus-banking-crisis-btc-pump]] | First macro-driven BTC pump; FX-BTC triangulation via flight currency |
| 2013-2014 | [[2013-2014-mtgox-premium-arbitrage]] | Mt. Gox premium / discount triangulation |
| 2017-2021 | [[2017-2021-kimchi-premium]] | Korea capital-controls premium |
| Aug 2017 | [[2017-08-bitcoin-cash-fork-arbitrage]] | BCH fork; cross-exchange credit arbitrage; $50-200M extracted by top desks |
| Dec 2017 | [[2017-12-cme-bitcoin-futures-launch]] | CME futures launch enabled institutional shorts; basis-trade era begins |
| Mar 2020 | [[2020-03-12-black-thursday-crypto]] | $0 MakerDAO CDP bug ($8.3M free ETH); BitMEX-Coinbase $600 spread |
| Jun 2022 | [[2022-06-three-arrows-blowup]] | 3AC liquidation cascade; stETH convergence trade; GBTC-discount widening |
| Nov 2022 | [[2022-11-ftx-collapse-arbitrage]] | FTT death spiral; SOL ecosystem -65%; $5-10x return on FTX claim trading |

### Crypto triangular-arb strategy pages

**Core / structural:**

| Strategy | Description |
|----------|-------------|
| [[crypto-spot-perp-futures-triangle]] | Three-wrapper basis trades across spot/perp/dated futures |
| [[dex-pool-triangular-arbitrage]] | Atomic on-chain MEV cycles via Uniswap/Curve/Balancer |
| [[multi-leg-arbitrage]] | 4+ leg generalization across fragmented liquidity |
| [[cross-l2-arbitrage]] | Same asset across Arbitrum/Optimism/Base/zkSync |
| [[wrapped-asset-triangular-arbitrage]] | WBTC/renBTC/tBTC, stETH/cbETH/rETH variants |
| [[fork-airdrop-triangulation]] | BCH-style hard forks + UNI-style protocol airdrops |
| [[lst-depeg-arbitrage]] | stETH-ETH convergence post-Shapella |
| [[stablecoin-pair-arbitrage]] | USDC/USDT/DAI basket during depegs |

**Modern / exotic (2024-2025):**

| Strategy | Description |
|----------|-------------|
| [[restaking-token-arbitrage]] | EigenLayer LRT-LST stack (eETH/ezETH/rsETH/pufETH) |
| [[babylon-bitcoin-staking-arbitrage]] | Bitcoin staking via Babylon; LBTC/SolvBTC/pumpBTC ecosystem |
| [[pendle-pt-yt-arbitrage]] | Yield-decomposition arb via Pendle PT/YT splits |
| [[velodrome-aerodrome-bribe-arbitrage]] | ve(3,3) bribe-market trading on Optimism / Base |
| [[polymarket-prediction-market-arbitrage]] | Polymarket / Kalshi cross-venue + reality-vs-market arb |
| [[pump-fun-bonding-curve-sniping]] | Solana memecoin bonding-curve sniping |
| [[bitcoin-runes-brc20-arbitrage]] | Bitcoin Runes / BRC-20 cross-marketplace arb |
| [[uniswap-v4-hooks-arbitrage]] | V4 hook-enabled custom AMM arbs |
| [[jito-solana-mev-arbitrage]] | Solana MEV via Jito Block Engine + ShredStream |
| [[intent-based-arbitrage]] | Solver-side fills on CoW / UniswapX / 1inch Fusion |
| [[private-mempool-arbitrage]] | Flashbots Protect / MEV-Share backruns |
| [[zkml-predictive-mev]] | ML predictions verified on-chain via ZK proofs |

### Pattern recognition for traders

Across all the above, the same structural setup recurs:

1. **A "stable" leg becomes brittle** (currency peg, central-bank floor, fiscal anchor, exchange withdrawal mechanics).
2. **One or more public signals leak** (central-bank statement, political announcement, deteriorating reserves data).
3. **Cross-rates diverge before the spot crash** because liquidity withdraws from the brittle leg first.
4. **Options pricing systematically lags spot** — vol is "too cheap" going in.
5. **Forced unwind of the dominant carry trade** amplifies the move 3-10x beyond fundamentals.

The math of "(BTC/USDT) × (ETH/BTC) ≠ (ETH/USDT)" is the textbook framing. The money is made when **the entire FX or asset triangle dislocates because the structural assumption holding it together cracks.**

## Sources

The crisis case studies above are documented on their own linked event pages (e.g. [[1992-black-wednesday-erm-crisis]], [[2015-01-snb-swiss-franc-unpeg]], [[2024-08-yen-carry-unwind]]); reported single-trade P&L figures are widely cited but trader-attributed and should be treated as approximate. The mechanical/no-arbitrage portion of this page is general market knowledge; no specific wiki source ingested yet.

## Getting the Data (CryptoDataAPI)

Execution is a sub-millisecond latency race that needs native exchange WebSocket feeds; [[cryptodataapi|CryptoDataAPI]] serves the research layer — triplet discovery, cross-rate deviation screening, and dislocation-frequency studies.

**Live data:**
- `GET /api/v1/daily/prices` — ~2,500 Binance spot pairs in one call (screen every candidate triplet for cross-rate inconsistency at snapshot cadence)
- `GET /api/v1/market-data/ticker/price?symbol=<SYM>` — per-pair spot price spot-checks
- `GET /api/v1/market-data/exchange-info?symbol=<SYM>` — pair specs (tick size, filters) that set the executable-size and rounding constraints per leg

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=<SYM>&interval=1m&limit=1000` — recent bars for deviation-frequency studies per triplet
- `GET /api/v1/backtesting/klines` — deep OHLCV archive (Binance spot 1h/4h/1d to 2017-08; 1m only since 2026-03-30)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/daily/prices"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] cannot win the execution race (REST polling is orders of magnitude too slow) but can run the research loop that decides where a low-latency bot should point:

- **Universe** — sweep `GET /api/v1/daily/prices` for triplets whose implied cross deviates from the quoted third leg; rank triplets by deviation frequency and magnitude to pick where a real-time bot earns its infrastructure cost.
- **Constraint check** — `GET /api/v1/market-data/exchange-info` per candidate pair for tick sizes and lot filters; a triplet whose thinnest leg cannot absorb the minimum viable size is dead regardless of deviation stats.
- **Regime gate** — `GET /api/v1/quant/market`: stale-quote windows widen in `vol_spike`/`choppy_high_vol` states and around listings; deviation frequency measured per regime state estimates how often the bot will actually fire.
- **Backtest** — 1m bars from `GET /api/v1/backtesting/klines` exist only since 2026-03-30 (Binance USDT-perps + HL); bar-level cross-rate studies are an upper bound on opportunity frequency, not P&L evidence — sub-second fills and fees decide the real economics.
- **Tips** — respect `Cache-Control`/`X-Cache` headers when sampling for deviation studies (cached prices fake dislocations); benchmark every apparent gross edge against the `3 × fee + spreads` hurdle before counting it as an opportunity.

## See Also
- [[arbitrage]] -- the umbrella concept
- [[latency-arbitrage]] -- the speed-race edge that dominates tri-arb economics
- [[cross-exchange-arbitrage]] -- arbitraging price differences across different exchanges rather than across pairs
- [[mev-strategies]] -- on-chain arbitrage in DeFi that exploits similar pricing inconsistencies on DEXs
- [[forex]] -- the traditional market where triangular arbitrage originated
- [[order-book]] -- understanding depth is critical for sizing and execution
- [[limits-to-arbitrage]] -- why the residual edge accrues only to the fastest, lowest-cost participants
- [[market-efficiency]] -- the economic force that makes these opportunities scarce and short-lived
- [[edge-taxonomy]] -- classification of edge sources
- [[failure-modes]] -- catalogue of how the strategy breaks
