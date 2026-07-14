---
title: "Cross-Exchange Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [arbitrage, crypto, cross-exchange, latency, market-neutral, dex, cex, market-microstructure]
aliases: ["Exchange Arb", "Spatial Arbitrage", "Inter-Exchange Arbitrage", "CEX-DEX Arb"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: cost-corrected

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, latency]
edge_mechanism: "Fragmented crypto liquidity across 100+ CEXs and thousands of DEX pools means the same token prints different prices for tens of milliseconds to minutes. The arbitrageur with pre-positioned inventory on both venues closes the gap and is paid the spread by whoever lifted/hit the stale quote — usually a slower taker or a retail market order on the thinner venue."

# Data and infrastructure requirements
data_required: [multi-venue-spot-price, order-book-depth, dex-pool-reserves, taker-fee-schedule, withdrawal-fee-schedule, gas-price]
min_capital_usd: 25000
capacity_usd: 20000000
crowding_risk: high

# Performance expectations (net of fees, gas, and rebalancing)
expected_sharpe: 1.6
expected_max_drawdown: 0.10
breakeven_cost_bps: 20

# Decay history
decay_evidence: "BTC/ETH cross-CEX spreads on top-10 venues compressed from persistent 20-100 bps gaps in 2016-2018 to routinely <5 bps by 2023 as pro market makers and inventory-based arbs saturated the majors. The Kimchi premium (Korea vs global) — once 30-50% in Jan 2018 — collapsed to low single digits by 2020-2022 as capital-control frictions eased. Edge now lives almost entirely in the long tail: new listings, low-cap tokens, CEX-vs-DEX gaps during volatility, and stablecoin/regional dislocations."

# Lifecycle
kill_criteria: |
  - median net spread on the monitored pair universe < breakeven for 30 consecutive days
  - sleeve drawdown > 10% in any rolling 30-day window
  - single-venue counterparty flag (withdrawal halt, solvency concern) on a venue holding > 20% of inventory
  - leg-fill success rate < 80% over any rolling 500 attempts

related: ["[[triangular-arbitrage]]", "[[cross-chain-arbitrage]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]", "[[flash-loan-arbitrage]]", "[[latency-arbitrage]]", "[[stablecoin-pair-arbitrage]]", "[[hl-vs-cex-funding-divergence]]", "[[multi-venue-capital-management]]", "[[slippage]]", "[[order-book]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[book-statistical-arbitrage-pole]]", "[[cryptodataapi]]"]
---

# Cross-Exchange Arbitrage

Cross-exchange arbitrage captures the price gap for the *same* crypto asset trading simultaneously on two different venues — CEX↔CEX (e.g. [[binance|Binance]] vs [[coinbase|Coinbase]]), or CEX↔DEX (e.g. Binance vs a [[uniswap|Uniswap]] pool). The arbitrageur buys where the token is cheaper and sells where it is dearer, locking the spread as a market-neutral profit. The single most important structural fact — and the one the naive "buy here, sell there, transfer the coins" description gets wrong — is that on-chain and cross-CEX transfers are far too slow (minutes to hours) to complete an arb before the gap closes. In practice this is an **inventory arbitrage**: the operator pre-positions capital on *both* venues, trades against the momentary dislocation using existing balances, and rebalances the inventory slowly and asynchronously. It is conceptually the simplest arb in crypto and, on the majors, one of the most competitive (Source: [[book-statistical-arbitrage-pole]]).

## Edge source

Mapping to the six categories in [[edge-taxonomy]], cross-exchange arbitrage is **structural + latency**:

- **Structural.** Crypto has no consolidated tape and no [[market-efficiency|NBBO]]. Liquidity is split across 100+ CEXs and thousands of AMM pools that each run an independent price. There is no mechanism forcing them to agree instant-to-instant. As long as venues remain fragmented and settlement between them is slow, the same asset can print different prices. The flow is a genuine, observable market imperfection, not an opinion.
- **Latency.** When a large market order lifts the offer on Venue A, that venue's book updates first; Venue B's quote is momentarily stale. Whoever detects the move and hits the stale quote on B fastest captures the gap. On majors this is a microsecond-to-millisecond race dominated by professional market makers; in the tail (new listings, thin alts, CEX-vs-DEX during volatility) the window stretches to seconds or minutes, which is where a well-engineered but non-colocated operator can still compete.

It is **not** an informational or analytical edge — every quote is public. The edge is the operational capability to hold inventory on both sides, monitor cross-venue spreads at low latency, and fire paired legs before the gap closes.

## Why this edge exists

Four persistent frictions keep the gap open long enough to harvest:

1. **Slow inter-venue settlement.** Moving BTC between two CEXs takes 3-6 confirmations (~30-60 min); an ERC-20 takes a block plus withdrawal-processing delay; a fiat rail can take days. Because you cannot arbitrage-and-transfer inside the window, the *effective* competition is limited to operators who have already parked inventory on both venues — a much smaller set than "everyone who can see the spread."
2. **Capital fragmentation and counterparty aversion.** Pre-positioning inventory on many venues means accepting concentrated [[ftx|exchange-insolvency]] risk on each one. Many capable players refuse to hold size on second-tier venues, so dislocations on those venues persist longer.
3. **Fee and withdrawal-cost heterogeneity.** Taker fees range from ~1 bp (VIP CEX maker/taker tiers) to ~40-60 bps (base-tier or small venues); withdrawal fees and DEX gas are fixed-dollar costs that dominate on small tickets. A spread that clears for a tier-VIP arb does not clear for a base-tier retail account, narrowing the effective competitor pool.
4. **Regional and regulatory segmentation.** KYC, fiat on/off-ramp access, and capital controls wall off pools of demand (the Korean "Kimchi premium" being the canonical case). These frictions are the structural reason regional venues trade at persistent premia/discounts to the global mid.

The tail persists precisely because the frictions that professionals arb away on BTC/ETH are strongest on new, thin, or geographically walled markets. He/Manela-style microstructure work and [[book-statistical-arbitrage-pole|Pole (2007)]] both frame this as the general law: arbitrage compresses the liquid core and survives in the illiquid periphery.

## Null hypothesis

Under a frictionless, fully integrated market, every venue quotes the same price to within trading costs and the strategy earns nothing after fees. Concretely, under the null:

- The cross-venue spread distribution is centred on zero with a width no greater than the sum of round-trip taker fees (~2-6 bps on majors).
- Any gap wider than costs closes within one quote-update latency and is uncapturable by a non-colocated operator.
- Net-of-cost realised spreads over a month are statistically indistinguishable from zero.
- CEX↔DEX gaps equal exactly the gas + swap-fee cost of closing them, no more.

The empirical record falsifies the null in the tail but largely confirms it on the core. BTC/ETH cross-CEX gaps now sit inside costs the vast majority of the time (null holds); new-listing and low-cap gaps of 30-300 bps that persist for seconds-to-minutes are routinely observed (null fails). **If a monitored-pair sleeve produces net spreads indistinguishable from zero for 30+ days, the pair set has been arbed into the null regime and should be rotated to thinner venues/pairs or the sleeve paused.**

## Rules

### Entry conditions

1. **Net-spread signal.** `net_spread_bps = gross_spread_bps − taker_fee_A − taker_fee_B − expected_slippage − (gas_or_withdrawal_amortised)` must exceed an entry floor of **≥ 15 bps** (majors) or **≥ 30 bps** (thin/new pairs, to cover wider slippage and adverse selection).
2. **Depth gate.** Both venues must show ≥ 3× intended notional within the target price band on the [[order-book]] (CEX) or in pool reserves (DEX). Prevents slippage from eating the gross spread.
3. **Persistence / freshness.** Quote timestamps on both venues are < 500 ms stale; the gross gap has been observed on at least two consecutive snapshots (filters single-tick noise and crossed-book artefacts).
4. **Inventory availability.** Buy-side venue has quote-currency balance and sell-side venue has base-asset balance sufficient for the ticket. No arb fires that would require an in-flight transfer to settle.
5. **Venue health.** No withdrawal halt, no oracle/mark anomaly, and (CEX↔DEX) no pending honeypot/blacklist flag on the token contract.

### Exit conditions

Cross-exchange arb has **no holding period** — the position is flat the instant both legs fill. "Exit" management is really *leg-risk* and *inventory* management:

1. **Immediate completion.** Trade is done when both legs confirm. Profit is realised at fill.
2. **Leg-risk unwind.** If one leg fills and the other rejects/misses (partial or no fill within a 2-second window), immediately market-flatten the filled leg — never carry unhedged directional exposure. Booked as a small controlled loss.
3. **Inventory rebalance (asynchronous).** When cumulative one-directional flow depletes base asset on one venue and quote on the other past a band (e.g. > 40% inventory skew), schedule a withdrawal/transfer to rebalance. This is a slow background process, decoupled from the arb loop.

### Position sizing

- Size each ticket to the **min of the two venues' 3×-depth capacity** — never more than the thinner book supports.
- Per-venue inventory cap: **≤ 20-25% of sleeve** on any single exchange to bound [[ftx]]-style counterparty loss.
- Keep a working cash buffer for leg-risk flattening and withdrawal fees.

## Implementation pseudocode

```python
# cross_exchange_arb.py — inventory-based paired-leg harvester (non-colocated)
from dataclasses import dataclass

ENTRY_FLOOR_BPS_MAJOR = 15.0     # net spread floor on majors
ENTRY_FLOOR_BPS_TAIL  = 30.0     # net spread floor on thin/new pairs
DEPTH_MULTIPLE        = 3.0      # need 3x notional at target band on both venues
MAX_STALE_MS          = 500      # skip if either quote older than this
PER_VENUE_INV_CAP     = 0.25     # 25% of sleeve per venue
LEG_RISK_TIMEOUT_S    = 2.0      # flatten filled leg if partner misses within this

@dataclass
class Quote:
    venue: str
    is_dex: bool
    bid: float
    ask: float
    depth_at_band: float         # notional available within target band
    ts_ms: int
    taker_fee_bps: float
    gas_or_wd_usd: float         # fixed cost to close (DEX gas / CEX withdrawal amortised)

def net_spread_bps(buy: Quote, sell: Quote, notional_usd: float) -> float:
    gross = (sell.bid - buy.ask) / buy.ask * 1e4
    fixed_bps = (buy.gas_or_wd_usd + sell.gas_or_wd_usd) / notional_usd * 1e4
    slip = expected_slippage_bps(buy, sell, notional_usd)   # from depth curves
    return gross - buy.taker_fee_bps - sell.taker_fee_bps - fixed_bps - slip

def decide(a: Quote, b: Quote, notional: float, book: dict, is_tail: bool) -> dict:
    floor = ENTRY_FLOOR_BPS_TAIL if is_tail else ENTRY_FLOOR_BPS_MAJOR
    now = max(a.ts_ms, b.ts_ms)
    if now - min(a.ts_ms, b.ts_ms) > MAX_STALE_MS:
        return {"action": "SKIP", "reason": "stale quote"}

    # orient: buy on the venue with the lower ask, sell on the higher bid
    buy, sell = (a, b) if a.ask < b.ask else (b, a)
    if min(buy.depth_at_band, sell.depth_at_band) < DEPTH_MULTIPLE * notional:
        return {"action": "SKIP", "reason": "insufficient depth"}

    ns = net_spread_bps(buy, sell, notional)
    if ns < floor:
        return {"action": "WAIT", "reason": f"net spread {ns:.1f}bps < floor {floor}"}

    # inventory checks — arb only against pre-positioned balances, never in-flight transfers
    if book["quote_bal"][buy.venue] < notional:
        return {"action": "WAIT", "reason": f"no quote inventory on {buy.venue}"}
    if book["base_bal"][sell.venue] * sell.bid < notional:
        return {"action": "WAIT", "reason": f"no base inventory on {sell.venue}"}
    if book["inv_usd"][buy.venue] + notional > PER_VENUE_INV_CAP * book["sleeve"]:
        return {"action": "WAIT", "reason": "per-venue inventory cap"}

    return {
        "action": "FIRE_PAIR",
        "buy_venue": buy.venue, "sell_venue": sell.venue,
        "notional": notional, "expected_net_bps": ns,
        "leg_risk_timeout_s": LEG_RISK_TIMEOUT_S,
    }
```

The production loop wraps this with: per-venue WebSocket books (native feeds for execution latency), an async rebalancer that batches withdrawals when inventory skew exceeds the band, a leg-risk watchdog that flattens on partner-miss, and a manual kill switch. Colocation is *not* required for the tail — the edge there persists for seconds — but a private low-latency path to each venue's matching engine materially improves fill rates on the majors.

## Indicators / data used

- **Multi-venue best bid/ask** — the primary signal; the cross-venue gap itself.
- **[[order-book]] depth (CEX) / pool reserves (DEX)** — the slippage/depth gate; caps ticket size.
- **Taker-fee tier per venue** — the dominant *variable* cost; the arb is a fee-tier game.
- **Withdrawal fees + on-chain gas** — the dominant *fixed* cost; determines the minimum viable ticket.
- **Quote timestamps / feed latency** — freshness gate; measures round-trip to each venue.
- **Token security flags (CEX↔DEX)** — honeypot/blacklist/transfer-tax detection before touching a DEX token.
- **Aggregators** — cryptodataapi.com (Binance-spot price/depth, DEX pool state), [[coinglass]], and native exchange WebSockets for execution-grade latency.

## Example trade

**Setup (illustrative, CEX↔DEX during a volatility spike, 2026-05-11):**

- A mid-cap token, ARB-USDC, prints **$1.184 ask** in a [[uniswap|Uniswap v3]] pool on Arbitrum (deep enough for $20k) while **$1.192 bid** on a CEX ([[binance|Binance]]) after a burst of CEX buying that the DEX pool has not yet followed.
- Gross gap: (1.192 − 1.184) / 1.184 = **67.6 bps**.
- Sleeve: $200k, split across venues. Ticket: $20,000.

**Cost overlay (realistic, never naive):**

| Cost leg | Amount | bps on $20k |
|---|---|---|
| DEX swap fee (0.05% pool) | $10.00 | 5.0 |
| DEX gas (Arbitrum, ~$0.30) | $0.30 | 0.15 |
| CEX taker fee (0.04%) | $8.00 | 4.0 |
| Slippage, DEX side ($20k in pool) | ~$14 | 7.0 |
| Slippage, CEX side | ~$4 | 2.0 |
| **Total cost** | **~$36.30** | **~18.2 bps** |

**Execution:**

1. Buy $20,000 ARB in the Uniswap pool at ~$1.184 (already-held USDC inventory on Arbitrum; no bridge in the loop).
2. Simultaneously sell the equivalent ARB on Binance at ~$1.192 against pre-positioned ARB inventory there (the DEX-bought coins backfill inventory later, asynchronously).
3. Net delta ≈ 0 at fill.

**Result:** gross 67.6 bps − 18.2 bps costs = **~49.4 bps ≈ $98.80 net** on a $20k ticket, realised in the ~2-3 seconds it took both legs to confirm. The DEX-side coins are transferred to Binance later in a batched rebalance (one $0.30 gas + no urgency). Had this been a BTC/ETH major pair, the gross gap would almost certainly have been < 5 bps and the trade would not have cleared the floor at all.

## Performance characteristics

Realistic, cost-corrected picture (2024-2026 regime):

| Metric | Value | Note |
|---|---|---|
| Net edge, majors (BTC/ETH cross-CEX) | ~0 bps | Arbed out; gaps sit inside costs almost always. |
| Net edge, tail (new listings, thin alts, CEX↔DEX) | 20-80 bps/trade | Where essentially all the money is now. |
| Sharpe (target, tail-focused sleeve) | 1.6 | High per-trade hit rate; capped by opportunity frequency, not per-trade risk. |
| Max drawdown (sleeve) | 5-10% | Driven by leg-risk misfills and single-venue counterparty scares, not directional moves. |
| Win rate (per completed pair) | 85-95% | Losses are leg-risk flattens, not adverse spread. |
| Breakeven cost budget | ~20 bps round-trip | Taker×2 + slippage + amortised gas/withdrawal. |
| Capital efficiency | Low | Inventory pinned idle across N venues to be *ready*; only a fraction works at any instant. |

**Costs that the naive version ignores and that dominate reality:**
- **Idle-inventory drag.** To be ready on both sides you park capital that earns nothing (or must be separately yield-farmed), across venues you would rather not hold counterparty risk on. This is the real capital cost of the strategy and it is invisible in a per-trade P&L.
- **Rebalancing/withdrawal fees.** Every net-directional run of arbs eventually requires a withdrawal to re-centre inventory. On BTC that is a fixed ~$1-5 + confirmation delay; on ERC-20s, gas.
- **Leg-risk losses.** The 5-15% of attempts where the partner leg misses cost a small market-flatten each — a real, recurring tax.
- **Adverse selection in the tail.** A quote that is *still* stale when you hit it is sometimes stale because the other side has information you do not (an impending listing halt, a depeg). Wider floors on thin pairs price this in.

## Capacity limits

Bounded by depth on the *thinner* of the two venues, in roughly this order:

- **BTC/ETH cross-CEX:** effectively zero economic capacity for a non-colocated operator — the gaps are already inside costs.
- **Top alts (SOL, and CEX-listed L1/L2 tokens):** ~$0.5-5M/event before the arb itself moves the thinner book; aggregate low tens of $M/year.
- **CEX↔DEX on mid-caps:** ~$20k-500k/event, gated by pool depth; aggregate $10-30M/year, but per-dollar returns are the highest here.
- **Regional/stablecoin dislocations:** episodic, capacity set by fiat-rail and on/off-ramp throughput, not order-book depth.

For an individual operator a realistic working ceiling is **$25k-$5M** of *deployed* inventory (multiples of that pinned idle across venues). Above that, on anything but the deepest majors, the operator's own flow closes the gaps it is trying to harvest.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Crowding on the core (Failure Mode #4).** The dominant secular story: BTC/ETH cross-CEX gaps compressed from tens of bps (2016-2018) to inside-costs by 2023. The Kimchi premium collapse is the textbook regional example. The trade is not dead but has retreated entirely into the tail.
2. **Leg risk / operational collapse (Failure Mode #7).** One leg fills, the other misses (venue lag, rate limit, rejected order), leaving unhedged exposure. At scale this is the primary loss generator; a slow or buggy flatten path turns a market-neutral book into a directional one.
3. **Counterparty failure (Failure Mode #7).** Inventory pinned on a second-tier venue to *enable* the arb is exactly the capital most exposed to an [[ftx]]-style insolvency or withdrawal halt. The strategy structurally forces you to hold size on venues you would otherwise avoid.
4. **Adverse selection / tail realised (Failure Mode #6).** The stale quote you hit was stale for a reason — an impending delisting, halt, or depeg. In CEX↔DEX, buying a token that turns out to have a transfer tax, honeypot, or freeze function is a total-loss trap.
5. **Fee-tier disadvantage.** A base-tier account simply cannot clear spreads that a VIP-tier maker can. If your competitors have a structurally lower cost base, the net edge accrues to them.
6. **Gas/congestion spikes (CEX↔DEX).** On Ethereum L1 a fee spike can turn a modelled-profitable arb into a loss between simulation and inclusion.

## Kill criteria

Pause (not retire) the sleeve on any of:

1. **Median net spread on the monitored pair universe < breakeven for 30 consecutive days** — the pair set has been arbed into the null; rotate venues/pairs.
2. **Sleeve drawdown > 10%** in any rolling 30-day window.
3. **Leg-fill success rate < 80%** over any rolling 500 attempts — execution infrastructure is losing the race; stop feeding it.
4. **Counterparty flag** (withdrawal halt, solvency concern, unscheduled maintenance > 4h) on any venue holding > 20% of inventory — flatten and withdraw.
5. **Repeated honeypot/adverse-token losses** in the CEX↔DEX book — tighten the security gate before re-enabling.

Re-deploy: all clear, plus a fresh scan showing ≥ 3 monitored pairs with 14-day median net spread back above the entry floor. See [[when-to-retire-a-strategy]] — this is a *pause-able* strategy: fragmentation never fully disappears, only the exploitable gap on a given pair set does.

## Advantages

- **Market-neutral, instant realisation.** No directional view, no holding period; P&L locked at fill.
- **Exploits a genuine, observable imperfection.** Fragmentation is real and structural, not a modelled anomaly.
- **Scales with infrastructure.** Better feeds, lower latency, and higher fee tiers translate directly into more captured gaps.
- **Deep tail.** Thousands of thin pairs and new listings continuously regenerate exploitable gaps even as the core is arbed out.
- **Performs a public good.** Synchronises prices across venues, improving [[market-efficiency]].

## Disadvantages

- **Capital-inefficient by design.** Inventory must sit idle on multiple venues to be *ready*; the working fraction is small and the counterparty risk is concentrated on exactly that idle capital.
- **Speed arms race on the majors.** Colocated pro market makers own the BTC/ETH core; retail earns nothing there.
- **Leg risk is a permanent tax.** Misfills are unavoidable and each one is a small controlled loss.
- **Multi-venue counterparty risk.** [[ftx]], Mt. Gox, and dozens of smaller failures — the strategy forces exposure to the weakest venues.
- **Fixed costs dominate small tickets.** Withdrawal fees and gas make sub-$5k tickets uneconomic on most pairs.
- **CEX↔DEX token risk.** Honeypots, transfer taxes, and freeze functions can convert a "risk-free" arb into a total loss.
- **Edge decay is documented and ongoing.** Every liquid pair trends toward the null over time.

## Sources

- [[book-statistical-arbitrage-pole]] — Pole (2007): theoretical foundation for cross-market price-discrepancy exploitation, the competitive dynamics that compress arbitrage margins, and the statistical framework for identifying profitable spreads.
- Kimchi-premium literature and public exchange data — the canonical regional-segmentation case: Korean BTC premia of 30-50% (Jan 2018) collapsing to low single digits by 2020-2022 as capital-control frictions eased. Documents the structural (KYC/fiat-rail) source of persistent cross-venue gaps.
- Crypto market-microstructure work on price discovery and lead-lag across venues (CEXs lead, DEXs follow) — motivates the latency component of the edge and the CEX→DEX direction of most exploitable gaps.
- [[funding-rate-arbitrage]], [[cash-and-carry]] — adjacent market-neutral crypto strategies sharing the counterparty-risk and inventory-management problems.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI is **Binance-spot-centric** for CEX quotes; it does not stream every CEX book. Use it for one side of the pair, for DEX pool state, and for depth/backtesting — pair it with native venue WebSockets for the second CEX side at execution latency.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — Binance spot price (one CEX leg)
- `GET /api/v1/market-data/ticker/24hr?symbol=ETHUSDT` — 24h stats for liquidity screening
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps (the slippage/depth gate)
- `GET /api/v1/liquidity/depth/{coin}` — per-coin 24h rolling depth history (BTC free; full universe Pro+)
- `GET /api/v1/dex/token/{chain}/{address}` — DEX token info + top pools (the DEX leg)
- `GET /api/v1/dex/trending` — trending DEX pools across Solana/Ethereum/Base/BSC/Arbitrum
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection) before touching a DEX token
- `GET /api/v1/market-data/exchange-info?symbol=BTCUSDT` — pair specs (tick size, filters)

**Historical / research:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1m&limit=1000` — Binance OHLCV for spread backtests
- `GET /api/v1/backtesting/klines` — deep OHLCV archive
- `GET /api/v1/backtesting/symbols` — backtest-available symbols

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/depth"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/token/arbitrum/0x912CE59144191C1204E64559FE8253a0e49E6548"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-dex]], [[cryptodataapi-backtesting]].

## Related

- [[triangular-arbitrage]] — single-venue three-pair variant (no cross-venue latency risk).
- [[cross-chain-arbitrage]] — the multi-blockchain extension; adds bridge time/risk to the transfer problem.
- [[flash-loan-arbitrage]] — the atomic on-chain cousin that removes inventory/leg risk within one transaction.
- [[latency-arbitrage]] — the speed-first extreme of the same idea on crypto venues.
- [[stablecoin-pair-arbitrage]] — a peg-anchored special case with a known convergence target.
- [[hl-vs-cex-funding-divergence]] — cross-venue arb on the *funding* dimension rather than price.
- [[funding-rate-arbitrage]] / [[cash-and-carry]] — carry-based market-neutral crypto strategies.
- [[multi-venue-capital-management]] — how to run inventory and counterparty limits across venues.
- [[order-book]] / [[slippage]] — the depth and cost mechanics that gate every ticket.
- [[edge-taxonomy]] — where this sits among the six edge categories.
- [[failure-modes]] — the catalog the kill criteria draw from.
- [[when-to-retire-a-strategy]] — pause-vs-retire framework.
- [[market-efficiency]] — the principle arbitrage enforces.
- [[ftx]] — the counterparty-risk cautionary tale for pinned inventory.
