---
title: "Cross-Venue Execution (Crypto)"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [crypto, market-microstructure, liquidity, slippage, algorithmic-trading, funding-rate, hyperliquid]
aliases: ["Cross-Venue Execution", "Crypto Venue Routing", "Multi-Venue Order Routing", "Cross-Exchange Execution"]
domain: [market-microstructure]
prerequisites: ["[[best-execution]]", "[[depth-of-market]]", "[[smart-order-routing]]"]
difficulty: advanced
related: ["[[smart-order-routing]]", "[[best-execution]]", "[[depth-of-market]]", "[[market-impact]]", "[[slippage]]", "[[thin-market-execution]]", "[[perp-dex-aggregation]]", "[[funding-rate]]", "[[funding-by-hour]]", "[[hyperliquid-fee-tiers-and-maker-rebates]]", "[[twap]]", "[[iceberg-orders]]", "[[market-fragmentation]]"]
---

# Cross-Venue Execution (Crypto)

**Cross-venue execution** is the practice of filling a single *directional* crypto order — a decision to be net long or net short a size — by splitting and routing it across multiple exchanges (Binance, Bybit, OKX, [[hyperliquid|Hyperliquid]]) chosen by live [[depth-of-market|book depth]], [[hyperliquid-fee-tiers-and-maker-rebates|fee tier]], and [[funding-rate|funding]]. It is the crypto-native form of [[smart-order-routing]]. Crucially, it is **not** [[arbitrage]] or a [[perp-dex-aggregation|hedged basis trade]]: the trader wants the *same net exposure* regardless of venue and is only minimizing the total cost of acquiring it. The output is an allocation — "45% Binance, 25% Bybit, 20% OKX, 10% Hyperliquid" — not a set of offsetting legs.

## Why Crypto Fragments the Order

Crypto liquidity for the same asset is split across dozens of independently-operated books with no consolidated tape and no Reg-NMS-style best-execution mandate. There is no NBBO, no protected-quote rule, and no obligation on any venue to route to another's better price. The consequences that shape execution:

- **Depth differs by venue and by asset.** BTC and ETH are deep everywhere; a mid-cap alt may have 5-10x more resting size on one venue than another, and that ranking shifts intraday.
- **Fees are personalized.** Each venue runs its own maker/taker tier ladder keyed to *your* rolling volume, so the cheapest venue depends on which trader is asking (see [[hyperliquid-fee-tiers-and-maker-rebates]]).
- **Funding is dispersed.** The same perp can carry meaningfully different [[funding-rate|funding]] across venues at the same moment, and on different clocks (see below).
- **Settlement and custody differ.** A CEX fill settles against that exchange's balance; a Hyperliquid fill settles on-chain. Moving inventory between them is slow and costs fees, so routing has to respect where collateral already sits.

## The Venue Set

Typical low-tier figures — every schedule is tiered and changes; treat as order-of-magnitude, verify live:

| Venue | Instrument | Perp funding clock | Taker (typical low tier) | Maker (typical low tier) | Depth profile |
|---|---|---|---|---|---|
| Binance | Spot + USDⓈ-M perps | 8h (3/day) | ~4.5 bps | ~2 bps | Deepest overall; tightest majors |
| Bybit | Perps + spot | 8h (3/day) | ~5.5 bps | ~2 bps | Deep majors, strong alt-perp depth |
| OKX | Perps + spot | 8h (3/day) | ~5 bps | ~2 bps | Deep majors, good alt coverage |
| Hyperliquid | On-chain perps ([[hypercore|HyperCore]] CLOB) | **1h (24/day)** | ~4.5 bps, maker rebate at tier | rebate-eligible | Transparent per-minute L2; strong majors, price-discovery venue |

The 8h-vs-1h funding cadence gap between the CEXes and Hyperliquid is the single biggest structural difference and drives the funding-timing logic below.

## Depth-Proportional Allocation

The core routing method is to split the order so that the **marginal fee-inclusive fill price is equalized across venues** — a water-filling problem on the consolidated book.

1. **Build a consolidated cost curve.** For each venue, walk its [[order-book]] and compute the average fill price for candidate child sizes, then add that venue's taker fee. This is the venue's fee-inclusive [[slippage]] curve (see [[depth-of-market]] for the walk-the-book calculation).
2. **Allocate to equalize the margin.** Send the next unit of size to whichever venue currently offers the cheapest *marginal* fee-inclusive price, and stop adding to a venue once its marginal price rises above the next-cheapest venue's. In the smooth case this reduces to allocating child size roughly in proportion to each venue's cumulative depth within an acceptable band δ:

```
q_i  ∝  D_i(δ)              # depth on venue i within δ bps of mid
subject to:  Σ q_i = target_size
             q_i ≤ participation_cap_i   # never exceed a set % of venue i's depth/volume
```

3. **Respect self-impact caps.** Depth-proportional sizing keeps each venue's realized impact similar, but a hard per-venue [[participation-rate|participation cap]] (e.g. each child ≤ 20-30% of resting depth within δ, or ≤ 10-15% of that venue's trailing 1-min volume) prevents any one book from being run over. This matters most for alts — see [[thin-market-execution]].
4. **Prefer the price-discovery venue for the aggressive slice.** On majors, Hyperliquid and Binance frequently lead price discovery; routing the most aggressive child there reduces the risk of trading into stale quotes on a lagging venue.

The intuition mirrors equities [[smart-order-routing]]: you are trying to consume the *cheapest liquidity first, everywhere at once*, rather than eating one book down its slippage curve.

## Venue Selection: Fee Tier and Rebates

Because tiers are personalized, the fee-inclusive ranking is trader-specific:

- **Net fees into the price, always.** A nominally better headline quote can be worse after a higher taker fee. Compare *fee-inclusive* marginal prices, not raw book prices.
- **Route passive size to rebate venues.** If part of the order can rest as a maker (you are not in a hurry), placing it where the maker rebate is richest — Hyperliquid's continuously-paid rebate at a high volume tier, for instance — can turn a cost into a credit.
- **Consolidate volume to climb tiers.** Splitting flow across five venues can keep you in the worst fee tier on all of them. There is a real tension between depth diversification and tier consolidation; high-volume desks often keep a "home" venue where they hold a good tier and only spill overflow elsewhere.

## Funding-Timing

For a position that will be *held* (not scalped), funding is a recurring carry that routing can optimize without changing net exposure:

- **Park the held leg where funding pays you (or costs least) for your side.** If you are long and one venue's funding for longs is least positive, hold size there; roll toward whichever venue's funding ranking is best as it shifts.
- **Mind the clock mismatch.** CEX funding settles every 8h at fixed snapshots; Hyperliquid settles hourly. Opening a fresh long moments before a large positive-funding snapshot means paying immediately; the 8h venues have predictable snapshot times (see [[funding-by-hour]]) that let you avoid or capture the print.
- **Do not chase funding into a thin book.** A long-tail venue can show enticing funding but a book too thin to exit; the funding pickup is dwarfed by exit [[slippage]]. Funding-timing is a second-order optimization applied *after* the depth/fee routing decides where the size can actually live.

## Worked Example

A desk wants to open a **$4M BTC-perp long**, to be held for several days. Consolidated snapshot within ±10 bps of mid: Binance $2.0M resting, Bybit $1.1M, OKX $0.9M, Hyperliquid $0.6M. Fee-inclusive marginal prices are near-equal after fees.

- Depth-proportional child sizes (capped at 30% of each venue's ±10 bps depth): Binance $1.8M, Bybit $1.0M, OKX $0.8M, Hyperliquid $0.4M — filling the bulk where the book is deepest and keeping each venue's impact below ~10 bps.
- The aggressive first tranche goes to Binance/Hyperliquid (price-discovery leads); the remainder rests as maker orders where possible to earn rebates.
- Funding check: Hyperliquid longs currently pay the least, so as fills complete the desk rolls a slice of the held size onto Hyperliquid to sit in the cheaper carry — net BTC exposure unchanged, funding bill reduced.

Result: one directional position, ~$4M long BTC, acquired at materially lower blended cost than dumping it into any single book.

## Not Arbitrage — the Distinction

| | Cross-venue execution | Cross-venue arbitrage / [[perp-dex-aggregation|basis]] |
|---|---|---|
| Goal | One net directional position, cheapest | Capture a price/funding *spread* |
| Legs | All same side | Offsetting long and short legs |
| Net exposure | The exposure you wanted | ~Delta-neutral |
| Edge harvested | Lower execution cost | Cross-venue dispersion |

Cross-venue execution is a *cost-minimization* discipline layered under any directional strategy; arbitrage is a standalone P&L source. This page is the former; see [[perp-dex-aggregation]] for the latter.

## Common Mistakes

1. **Equal-splitting across venues** regardless of depth — sends the same size into a thin book as a deep one, paying outsized impact on the thin leg.
2. **Ignoring the fee tier** — routing on raw quotes inverts the true cheapest-venue ranking.
3. **Over-fragmenting** — five child orders each too small to matter, but collectively keeping you in every venue's worst fee tier and leaking latency.
4. **Chasing funding into illiquid venues** — a carry pickup swamped by exit slippage.
5. **Treating displayed depth as real** — spoofed and fleeting quotes vanish on contact; time-average the depth snapshot before sizing (see [[depth-of-market]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps (the consolidated depth read that drives allocation)
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — raw Hyperliquid L2 order-book snapshot
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding (Binance + Hyperliquid) for the funding-timing decision
- `GET /api/v1/market-intelligence/funding-rates` — cross-exchange funding across top coins

**Historical data:**
- `GET /api/v1/liquidity/depth/{coin}` — 24h rolling depth history, 1-min samples (backtest the depth-proportional split)
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — Binance funding history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/depth"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-regimes]] (liquidity/depth), [[cryptodataapi-derivatives]] (funding), [[cryptodataapi-hyperliquid]] (L2 book).

> Note: the API exposes consolidated per-coin depth, the Hyperliquid on-chain L2 book, and cross-exchange (Binance + Hyperliquid) funding. Per-venue CEX order books for Bybit/OKX come from those venues' own market-data APIs.

## Related

- [[smart-order-routing]] — the general (equities-origin) routing discipline this specializes
- [[best-execution]] — the objective cross-venue routing serves
- [[depth-of-market]] — the depth measurement that drives the allocation
- [[market-impact]] / [[slippage]] — the costs being minimized
- [[thin-market-execution]] — the sibling problem when the book is too thin to split
- [[perp-dex-aggregation]] — the *arbitrage/basis* cousin (offsetting legs, not directional)
- [[funding-rate]] / [[funding-by-hour]] — the carry the held leg optimizes and the snapshot timing
- [[hyperliquid-fee-tiers-and-maker-rebates]] — the personalized fee tier that decides the cheapest venue
- [[twap]] / [[iceberg-orders]] — execution primitives used per-venue once size is allocated
- [[market-fragmentation]] — the structural condition that makes routing necessary

## Sources

- General crypto market-microstructure knowledge; venue fee/funding schedules per Binance, Bybit, OKX, and Hyperliquid public documentation (figures illustrative, tiers vary).
- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) — Hyperliquid depth, fee-tier, and funding mechanics underpinning the venue-set table.
