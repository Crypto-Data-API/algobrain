---
title: "HL vs CEX Funding Divergence"
type: strategy
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [arbitrage, crypto, defi, derivatives]
aliases: ["HL-Binance Funding Arb", "Cross-Venue Funding Spread", "Hyperliquid Funding Arb"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: live
edge_source: [structural, latency]
edge_mechanism: "Hyperliquid's hourly funding and distinct retail base produces persistent funding-rate dislocations vs Binance/Bybit. Long the venue paying you funding, short the venue charging you funding, profit from the spread until convergence."
data_required: [hyperliquid-funding-rate, binance-funding-rate, bybit-funding-rate, cross-venue-mark-prices]
min_capital_usd: 25000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 2.5
expected_max_drawdown: 0.15
breakeven_cost_bps: 25
related: ["[[funding-rate-arbitrage]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[funding-rate]]", "[[hyperliquid]]", "[[cross-exchange-arbitrage]]", "[[hlp-cascade-alongside-playbook]]"]
---

# HL vs CEX Funding Divergence

A cross-venue funding-rate arbitrage that pairs a [[hyperliquid|Hyperliquid]] perp leg against a [[binance|Binance]], [[bybit|Bybit]], or OKX perp leg of equal notional and opposite direction. The trade fires when funding on one venue diverges from funding on the other by more than ~5 basis points per 8-hour-equivalent — large enough to comfortably clear round-trip costs. Wiki sources document captured returns of **100–300% APR for 2–7 day windows** during 2024, with an estimated **$50–200M extracted by sophisticated cross-CEX arbs in 2024** (Source: [[hyperliquid-hlp-basis-arbitrage]]). This page is the standalone strategy; the parent [[hyperliquid-hlp-basis-arbitrage]] lists it as a variant, and [[hyperliquid-perp-trading-map]] covers it as Strategy 4.

The trade is fully delta-neutral by construction: equal-notional long on one venue cancels equal-notional short on the other. P&L is driven by the *funding spread*, not by the price of the underlying.

**Where this sits in the basket.** Within the [[trading-strategy-baskets|crypto strategy basket]] this is the cross-venue node of the [[hyperliquid|Hyperliquid]] funding family: it is a variant of [[funding-rate-arbitrage]] (single-venue parent), a sibling of [[hyperliquid-hlp-basis-arbitrage]] (HLP-aware HL strategies) and [[hlp-cascade-alongside-playbook]] (stackable in the same sleeve), and it is Strategy 4 in the [[hyperliquid-perp-trading-map]]. It shares the [[funding-rate]]/[[open-interest]] data rails with all of them, so the marginal infrastructure cost of adding this trade to an existing HL sleeve is low.

## Edge source

Mapping to [[edge-taxonomy]], this is a **structural + latency** edge:

- **Structural.** [[hyperliquid|Hyperliquid]] and the major CEXs ([[binance]], [[bybit]], OKX) share a contract design (USDT-quoted perpetuals, periodic funding) but differ materially in their *flow composition* and *funding mechanics*. Hyperliquid's user base is heavier on memecoin retail, HYPE-airdrop farmers, and DeFi-native traders; Binance/Bybit/OKX skew toward global retail plus institutional and market-maker flow. These distinct flow bases generate persistently different funding rates for the *same underlying asset* at the *same instant*.
- **Latency.** Hyperliquid funds **hourly** (24 settlements/day); Binance, Bybit, and OKX fund **every 8 hours** (3 settlements/day). The cadence mismatch means Hyperliquid's funding rate can spike, decay, and renormalize *within a single CEX funding window*. A trader watching only the 8h CEX print sees a smoothed average; a trader who measures both venues at hourly resolution sees an exploitable dislocation. See [[hyperliquid-funding-rate-microstructure]] for the cadence detail.

The trade is **not** an informational edge (funding rates are public on every venue) and **not** an analytical edge (no hidden model required). It is the operational capability to be on both venues at scale, monitor sub-hour cross-venue spreads, and execute paired positions before the spread converges.

### Venue funding-mechanics comparison

The edge is born from the *mechanical differences* in how each venue computes and settles [[funding-rate|funding]]. The cadence mismatch (column 2) and the flow-base difference (column 5) are the two structural sources of the spread. See [[hyperliquid-oracle-mechanics]] for how HL derives funding from `(mark − oracle)` and [[hyperliquid-funding-rate-microstructure]] for the cadence detail.

| Venue | Funding interval | Settlements/day | Margin asset | Dominant flow base | Funding basis |
|-------|------------------|-----------------:|--------------|--------------------|---------------|
| [[hyperliquid]] | **1 hour** | 24 | USDC (mostly) | Memecoin retail, HYPE farmers, DeFi-native | `(mark − oracle)` premium index, hourly |
| [[binance]] | 8 hours | 3 | USDT | Global retail + institutional + MM | clamped premium + 0.01% interest baseline |
| [[bybit]] | 8 hours | 3 | USDT | Global retail + MM | venue premium formula, 8h |
| OKX | 8 hours | 3 | USDT | Global retail + MM | venue premium formula, 8h |

The single most important normalization: convert HL hourly to 8h-equivalent before comparing. `hl_8h_eq = hl_hourly × 8`. A trader who reads HL's hourly print against Binance's 8h print without normalizing will systematically misread the spread by 8x.

## Why this edge exists

Five structural reasons HL funding diverges from CEX funding, and why arbitrage capital does not instantly close the gap:

1. **Memecoin and high-beta retail concentration on HL.** A meaningful fraction of [[hyperliquid|Hyperliquid]]'s daily volume is in long-tail and memecoin perps. When a meme name pumps, retail piles into the HL listing aggressively (fast onboarding, no KYC, hourly funding visible) and bids the perp far above the index. Funding spikes to 0.05%+/hour on HL while the same name on Binance — if even listed — funds at 0.01–0.02%/8h because Binance liquidity providers are deeper and absorb the imbalance faster.
2. **HL's hourly funding cadence vs CEX 8h cadence.** The mechanical effect: Hyperliquid funding can travel from +0.01%/h to +0.05%/h to +0.005%/h in the span of a single Binance 8h window. Binance's print is the time-average; HL's print is the instantaneous. The *difference between an instantaneous reading and a smoothed reading* is the dislocation an arb captures. (Source: [[hyperliquid-funding-rate-microstructure]].)
3. **Lower market-maker density on HL for non-major pairs.** Binance has dozens of professional market makers quoting BTC and ETH perps with ms-tight spreads; their algorithms include funding-rate flatteners that bid the perp toward the index whenever funding spikes. Hyperliquid has [[hyperliquid-hlp-basis-arbitrage|HLP]] and a smaller set of MMs; on majors they are competitive, but on alts and meme pairs the depth is materially thinner. Less MM presence = funding can persist in dislocation longer.
4. **Different fee tiers and capital efficiency between venues.** Binance top-tier VIP takers pay roughly 0.017% (makers ~0%); HL base-tier takers pay 0.045%. A cross-venue arb that nets +0.04% per funding period only clears if the round-trip cost is below the captured spread. Many smaller arbs cannot clear HL's higher taker fees, so they stay out of trades that a tier-VIP maker on Binance can comfortably profit from. The pool of capable cross-venue arbs is therefore narrower than the pool of single-venue funding arbs.
5. **HYPE airdrop and points-program loyalty on HL.** Through 2024 and into 2025, a meaningful share of HL volume was tied to airdrop farming and points accumulation. Farmers run net long perps on HL to maximise volume metrics, *paying funding* as a cost of farming. This created a structural long-bias on HL distinct from Binance, where there is no equivalent loyalty incentive. Funding-arb capital sits opposite the farmers and collects.

The edge is therefore *real, structural, and bounded*. Bounded because as more capital learns to bridge the venues, the average dislocation compresses. By 2025, BTC/ETH cross-venue spreads on majors compressed sharply (often <2 bp/8h-equivalent); spreads on alts and memes remain wide.

## Null hypothesis

Under uniform funding across venues — i.e., a frictionless world where the same asset funds at the same rate on every exchange — the cross-venue spread is identically zero and the strategy returns nothing after costs. Specifically:

- Hyperliquid's hourly funding would equal the time-average of Binance's 8h funding within the same window, modulo a spread bounded by trading costs and execution latency (no more than ~2 bp/8h-equivalent).
- The 7-day rolling cross-venue spread would oscillate around zero with no persistence beyond a few hours.
- A long-HL/short-CEX (or reversed) trade would earn zero net carry after fees and would not generate excess Sharpe.

The empirical record falsifies this null: 2024 saw repeated 5–15 bp/8h-equivalent spreads on majors that persisted for 2–7 day windows, and far wider, longer spreads on memecoin pairs. If your live cross-venue sleeve produces returns indistinguishable from the null distribution for 30+ days on majors and 60+ days on alts, the regime has compressed and the trade should be paused or moved to thinner pairs (where the edge persists longer). See the *Performance* section below for regime-by-regime numbers.

## Rules

### Entry conditions

1. **Spread signal.** Cross-venue funding spread > **5 bp / 8h-equivalent**. Convert HL hourly to 8h-equivalent: `hl_8h_eq = hl_hourly * 8`. Compare directly to Binance/Bybit/OKX 8h prints.
2. **Spread direction.**
   - If HL funding > CEX funding by ≥5 bp/8h-eq: **short HL perp, long CEX perp** (collect HL funding, pay smaller CEX funding).
   - If CEX funding > HL funding by ≥5 bp/8h-eq: **long HL perp, short CEX perp** (collect CEX funding, pay smaller HL funding).
3. **Persistence filter.** Spread has held above the 5 bp threshold for at least the last 1 hour (one HL funding period) — filters out flash spikes that revert before you can collect.
4. **Liquidity check.** Both venues have ≥3x intended notional in top-of-book depth at the entry mark. Prevents entry-slippage from eating the spread.
5. **Mark-price sanity.** HL mark and CEX mark are within 50 bps of each other; a wider divergence signals an oracle anomaly, not a funding dislocation. Skip and re-evaluate.
6. **Asset filter.** Restrict to pairs with HL daily volume ≥$50M (BTC, ETH, SOL, top memes) for the size band $25k–$1M; tighten further for larger sizes.

### Exit conditions

1. **Convergence.** Spread compresses to < **2 bp / 8h-equivalent**. Close both legs.
2. **Spread inversion.** Spread crosses zero in the opposite direction — the regime has flipped; close immediately rather than wait for re-convergence.
3. **One-sided MTM stress.** Notional unrealised loss on either leg exceeds 5% of position margin (despite the hedge). This typically signals a basis-blowup event (mark divergence between venues); close before forced liquidation.
4. **Funding cap.** After 7 funding periods (HL: 7h; CEX: 56h-equivalent), reassess: if spread has not delivered the modelled carry, exit even if still positive — the regime is below model.
5. **Venue health.** Any unscheduled maintenance, withdrawal halt, oracle issue, or chain outage on either venue → flatten that leg first, then mirror on the other.

### Position sizing

- **1x leverage on each leg, equal-notional, isolated margin.** Higher leverage compresses capital outlay but introduces liquidation risk on either leg during sharp moves. The hedge does not protect against single-leg liquidation.
- **Per-pair cap.** No more than 25% of cross-venue sleeve in a single pair.
- **Per-venue cap.** No more than 50% of sleeve at risk on either venue, ever — counterparty risk dominates above this.
- **Sleeve cap.** Max-loss tolerance: 15% sleeve drawdown triggers the kill switch (see below).

### Latency requirement

Sub-second execution between legs is **not** required for this trade — the edge persists for hours to days, not milliseconds. But **both legs must fire within ~30 seconds**: a long delay leaves the first leg directionally exposed to whatever happens during the gap. Use venue WebSocket order-acknowledgement to confirm the first fill before sending the second.

## Implementation pseudocode

```python
# hl_cex_funding_div.py — paired-leg cross-venue funding-spread harvester
from dataclasses import dataclass
from typing import Optional

ENTRY_SPREAD_BP_8H = 5.0           # 5 bp/8h-equivalent minimum
EXIT_SPREAD_BP_8H  = 2.0           # close on convergence
MARK_DIV_BP_LIMIT  = 50.0          # skip if HL vs CEX mark > 50 bp
PER_PAIR_CAP       = 0.25          # 25% of sleeve per pair
PER_VENUE_CAP      = 0.50          # 50% of sleeve per venue
SLEEVE_DD_KILL     = 0.15          # 15% sleeve drawdown kill
MIN_PERSISTENCE_H  = 1             # spread must hold ≥1 hour pre-entry
MAX_HOLD_PERIODS   = 7             # HL funding periods (= 7 hours)

@dataclass
class CrossVenueSignal:
    asset: str
    hl_funding_hourly: float        # current HL hourly funding rate
    cex_funding_8h: float           # current CEX 8h funding rate
    cex_venue: str                  # "binance" | "bybit" | "okx"
    hl_mark: float
    cex_mark: float
    spread_persistence_h: int       # hours the spread has been > threshold
    hl_depth_3x_ok: bool            # ≥3x notional depth at top-of-book HL
    cex_depth_3x_ok: bool           # same for CEX

def spread_bp_8h(s: CrossVenueSignal) -> float:
    """Convert both rates to 8h-equivalent and return HL minus CEX in bp."""
    hl_8h_eq = s.hl_funding_hourly * 8
    return (hl_8h_eq - s.cex_funding_8h) * 1e4   # to bp

def mark_divergence_bp(s: CrossVenueSignal) -> float:
    return abs(s.hl_mark - s.cex_mark) / s.cex_mark * 1e4

def decide(s: CrossVenueSignal, book: dict) -> dict:
    # ---- kill switches ----
    if book["sleeve_drawdown"] > SLEEVE_DD_KILL:
        return {"action": "FLATTEN_ALL", "reason": "sleeve drawdown kill"}

    if mark_divergence_bp(s) > MARK_DIV_BP_LIMIT:
        return {"action": "SKIP", "asset": s.asset, "reason": "mark divergence > 50bp"}

    spread = spread_bp_8h(s)
    pos = book["positions"].get(s.asset)

    # ---- exit logic ----
    if pos is not None:
        # convergence
        if abs(spread) < EXIT_SPREAD_BP_8H:
            return {"action": "EXIT", "asset": s.asset, "reason": "spread converged"}
        # spread flipped sign vs entry
        if (pos["entry_spread_sign"] > 0 and spread < 0) or \
           (pos["entry_spread_sign"] < 0 and spread > 0):
            return {"action": "EXIT", "asset": s.asset, "reason": "spread flipped"}
        # held too long without convergence
        if pos["periods_held"] >= MAX_HOLD_PERIODS:
            return {"action": "EXIT", "asset": s.asset, "reason": "max hold reached"}
        # MTM stress on either leg
        if max(pos["hl_unreal_loss_pct"], pos["cex_unreal_loss_pct"]) > 0.05:
            return {"action": "EXIT", "asset": s.asset, "reason": "leg MTM stress"}
        return {"action": "HOLD", "asset": s.asset}

    # ---- entry logic ----
    if abs(spread) < ENTRY_SPREAD_BP_8H:
        return {"action": "WAIT", "reason": "spread below threshold"}
    if s.spread_persistence_h < MIN_PERSISTENCE_H:
        return {"action": "WAIT", "reason": "spread not persistent"}
    if not (s.hl_depth_3x_ok and s.cex_depth_3x_ok):
        return {"action": "WAIT", "reason": "insufficient depth"}
    if book["pair_exposure"].get(s.asset, 0) >= PER_PAIR_CAP * book["sleeve_capital"]:
        return {"action": "WAIT", "reason": "per-pair cap"}
    if book["hl_exposure"] >= PER_VENUE_CAP * book["sleeve_capital"]:
        return {"action": "WAIT", "reason": "HL venue cap"}
    if book["cex_exposure"] >= PER_VENUE_CAP * book["sleeve_capital"]:
        return {"action": "WAIT", "reason": "CEX venue cap"}

    notional = PER_PAIR_CAP * book["sleeve_capital"]

    # spread > 0 means HL funding > CEX funding → short HL, long CEX
    if spread > 0:
        return {
            "action": "OPEN",
            "asset": s.asset,
            "hl_side": "SHORT", "hl_notional": notional,
            "cex_side": "LONG", "cex_venue": s.cex_venue, "cex_notional": notional,
            "reason": f"HL pays {spread:.1f} bp/8h above {s.cex_venue}",
        }
    else:
        return {
            "action": "OPEN",
            "asset": s.asset,
            "hl_side": "LONG", "hl_notional": notional,
            "cex_side": "SHORT", "cex_venue": s.cex_venue, "cex_notional": notional,
            "reason": f"{s.cex_venue} pays {-spread:.1f} bp/8h above HL",
        }
```

The production version wraps this with: WebSocket feeds for HL and the chosen CEX (acknowledgement-gated leg-2 firing), per-asset 7-day spread history for persistence filtering, hourly delta-drift checks, withdrawal-velocity monitoring, and a manual kill switch.

## Indicators / data used

The strategy consumes four primary signal families: **[[funding-rate]]** (the spread itself), **mark price** (delta-neutrality sanity check), **depth** (entry-slippage gate), and **[[open-interest]]** (flow confirmation). Cross-venue funding/OI/mark are available through aggregators such as cryptodataapi.com and [[coinglass]]; for execution-grade latency, read the native HL and CEX websockets directly.

| Data input | Source | Role in the trade |
|------------|--------|-------------------|
| **HL hourly [[funding-rate]]** | Native HL API / WS; cryptodataapi.com | Primary signal — the HL leg of the spread |
| **Binance / Bybit / OKX 8h [[funding-rate]]** | Native CEX API / WS; cryptodataapi.com | Counterparty-leg rate; the CEX side of the spread |
| **Cross-venue funding table** | [[coinglass]]; cryptodataapi.com | Universe scan for which pairs have a live spread |
| **Historical funding distribution** | Velo Data, Amberdata, Laevitas; cryptodataapi.com history | Backtest the per-pair spread distribution; size `MAX_HOLD_PERIODS` |
| **HL + CEX mark prices** | Native WS | Divergence sanity check (skip if > 50 bp; see [[hyperliquid-oracle-mechanics]]) |
| **HL + CEX top-of-book depth** | Native WS | Liquidity gate — need 3x intended size at top or slippage eats the spread |
| **HL + CEX [[open-interest]]** | Native API; [[coinglass]]; cryptodataapi.com | Confirms the divergence is real flow, not an oracle/print artefact |
| **Spread persistence histogram (per pair)** | Derived from funding history | How long the spread holds > 5 bp before reverting; the persistence filter input |

## Example trade

**Setup (illustrative, 2024 regime — ETH on HL vs Binance):**

- ETH HL hourly funding: **+0.0125%/h** (8h-equivalent: +0.10% = 10 bp).
- ETH Binance 8h funding: **+0.04%/8h** (= 4 bp).
- Spread: HL pays 10 bp/8h-eq vs Binance 4 bp/8h-eq → **HL pays 6 bp/8h-equivalent more than Binance**, above the 5 bp entry threshold.
- The spread has held above 5 bp for the past 4 hours (persistence ✓).
- HL ETH-PERP top-of-book depth: $4M; Binance ETHUSDT-PERP: $40M (depth ✓).
- Mark divergence: HL $3,512.40 vs Binance $3,512.10 → 0.85 bp (well below 50 bp).
- Sleeve capital: $100,000. Per-pair cap: 25% → $25,000 notional per leg.

**Entry:**

1. **HL leg.** Submit market short of $25,000 notional ETH-PERP on HL with $25,000 USDC isolated margin (1x). HL base-tier taker: ~$11.25 fee.
2. **Binance leg.** On WebSocket ack of HL fill, submit market long of $25,000 notional ETHUSDT-PERP on Binance with $25,000 USDT isolated margin (1x). Binance taker (assume tier 1): ~$10.
3. Net delta: ~0. Net funding accrual rate: +0.10% × $25k = $25/8h-equivalent on HL leg, –0.04% × $25k = –$10/8h on Binance leg → **net +$15/8h-equivalent = ~$45/day net funding** (HL pays you 24 hours/day; Binance charges you 3 times/day).

   *Restated more cleanly:* HL pays you 0.0125% × $25,000 = **$3.13/hour** for 24 hours = **$75/day** in HL funding income. Binance charges you 0.04% × $25,000 = **$10 per 8h** × 3 = **$30/day** in Binance funding cost. **Net funding: ~$45/day** at the modelled rates. (During meme-driven HL spikes in 2024, sustained net carry on $25k notional ran materially higher still — consistent with the 100–300% APR windows cited at the top.)

**Hold (3.5 days, ~24 funding periods on HL, ~10 on Binance):**

- Funding stays elevated on HL (memecoin contagion bidding ETH on HL too); Binance funding climbs slightly.
- ETH price drifts +2.4% over the hold. HL short loses ~$600 unrealised; Binance long gains ~$600 unrealised. Net price-leg P&L: ≈ $0 (the hedge does its job).
- Cumulative net funding earned: ~$45/day average × 3.5 days = **~$157**.

**Exit (day 4 morning):**

- HL hourly funding compresses to +0.0015%/h (8h-eq: 1.2 bp). Binance 8h funding: +0.030%/8h (3 bp). Spread now: 1.2 – 3 = **–1.8 bp/8h-eq** — sign-flipped vs entry. Trigger: spread flipped → close.
- Close HL short (taker: $11.25). Close Binance long (taker: $10). Total exit fees: $21.25.

**Net P&L:**

- Funding earned: ~$157.
- Round-trip fees (entry + exit): ~$42.50.
- Slippage (assume 1 bp each leg, both ways): ~$10.
- **Net: ~$104 on $25,000 deployed × 2 = $50,000 capital at risk over 3.5 days.**
- Annualised on $50k: 0.21% over 3.5 days → ~22% APR for this trade alone.

During *peak* dislocation windows (memecoin pumps, HYPE airdrop period, late-2024 HL volume surges), wiki sources document captured returns of **100–300% APR for the duration of the window** (Source: [[hyperliquid-hlp-basis-arbitrage]], [[hyperliquid-perp-trading-map]]). The above example is a conservative steady-state trade; the high-APR windows show what's possible when the spread blows out and persists.

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Net APR (2024 best windows) | 100–300% | 2–7 day windows; multiple per quarter on alts and memes |
| Net APR (steady state, 2024) | 20–60% | Across a portfolio of 5–10 active pairs |
| Net APR (2025 BTC/ETH only) | 5–15% | Spreads on majors compressed as more arbs entered |
| Sharpe target | 2.5 | Higher in dislocation regimes; can collapse to <0 during venue-specific outages |
| Max drawdown (sleeve) | 10–15% | Driven by basis-blowup or venue-outage events, not directional moves |
| Win rate (per trade) | 75–90% | Most trades reach convergence cleanly |
| Profit factor | 3.0–6.0 in dislocation regimes; 1.2–1.8 in calm |  |
| Breakeven cost budget | ~25 bp round-trip | HL taker + Binance taker + slippage, both legs, both ways |
| Active windows per year | 5–10 that fire >7 days | On majors. Many more on alts and memes. |
| Capital efficiency | ~50% (1x each leg = 2x total deployment) | Same as all delta-neutral cross-venue trades |

The realistic expectation: on a $100k–$500k sleeve trading the universe of HL-listed perps with active monitoring, **20–60% net APR in 2024–2025 regimes**, punctuated by 2–7 day windows where the sleeve compounds at 100%+ annualised. As more capital learns to bridge HL and CEX, expect spreads on BTC/ETH to continue compressing through 2025–2026; the alt and meme tail remains exploitable.

## Capacity limits

The trade is bounded by HL liquidity per pair, in this approximate order:

- **BTC, ETH on HL**: capacity per spread event ~$10–50M before MM rebalancing on HL or arb capital from Binance closes the spread within minutes. Aggregate annual capacity: tens to low-hundreds of $M across BTC+ETH.
- **SOL, top-tier alts**: ~$2–10M per spread event; aggregate ~$50M/year.
- **Memes and long-tail**: ~$100k–$2M per event; aggregate ~$10–30M/year, but the *spreads* are wider (20–100 bp/8h-eq) so the per-dollar return is much higher.
- **Aggregate across all HL pairs**: estimated **$50–200M extracted in 2024 by sophisticated cross-CEX arbs** (Source: [[hyperliquid-hlp-basis-arbitrage]]). This is the wiki's documented number.

For an individual operator, working capacity is **$25k–$5M** before HL meme-pair execution becomes self-defeating; **$10–50M** if the operator restricts to BTC/ETH/SOL on HL, where depth is genuinely deep. Above that, you are competing with [[hyperliquid-hlp-basis-arbitrage|HLP]] and the largest cross-venue arb desks.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Spread compression as more arbs enter.** The dominant secular risk. Cross-venue spreads on BTC/ETH compressed materially from 2024 to 2025 as HL grew and more capital learned to bridge. Already noticeable on majors; alts and memes still have room. (Failure Mode #4: The Edge Got Crowded Out.)
2. **HL or CEX outage during the position.** Either venue going down with an open position leaves the other leg directionally exposed. HL chain outages (rare but documented) and Binance/Bybit/OKX maintenance windows are the canonical events. Mitigation: monitor venue status pages and pre-flatten before scheduled maintenance. (Failure Mode #7: Operational Collapse.)
3. **Mark-to-market pain forcing close at suboptimal time.** Even at 1x leverage, a violent move against either leg can pull margin below the maintenance buffer if the venues' marks diverge transiently. The "delta-neutral" position takes a one-sided loss when one leg liquidates. Mitigation: 1x isolated margin, MTM-stress kill at 5%, depth gate at entry. (Failure Mode #6: Tail Realised.)
4. **Funding-formula change on either venue.** HL has revised its funding mechanism multiple times since launch; CEXs occasionally adjust their interest-rate component or premium clamps. A change overnight invalidates the bot's spread calculation. Mitigation: funding-formula health check in the daily review.
5. **Counterparty failure on the CEX leg.** [[ftx]] is the canonical reminder. CEX capital sitting as margin for the long/short leg is at risk of insolvency, withdrawal halt, or rehypothecation. HL is decentralised but introduces its own chain/contract risks. The double-venue structure of this trade means **counterparty risk is doubled vs single-venue funding arb**.
6. **Stablecoin depeg.** USDT or USDC depeg events distort margin and funding-rate calculations on both venues simultaneously, but asymmetrically — HL is USDC-margined (mostly), Binance is USDT-margined; a depeg on either creates a disguised directional exposure.
7. **Regulatory action against HL.** US/Ontario already block HL; further geo-fence expansion would force a forced unwind for affected operators.
8. **Mark divergence between venues during stress.** When HL and CEX mark prices decouple by >100 bps for >10 minutes (oracle issue, flash crash), the supposedly delta-neutral position has real basis exposure. The 50 bp divergence skip in the entry rules and 100 bp emergency-flatten in production are designed for this.

## Kill criteria

The deployed sleeve is paused (not retired) on any of:

1. **Sleeve drawdown > 15%** in any rolling 30-day window.
2. **Cross-venue spread on monitored pairs averages < 3 bp/8h-eq for 30+ consecutive days** — regime confirmation that the trade has been arb'd out for that asset class.
3. **HL or CEX mark divergence > 100 bps sustained > 10 minutes** on a held position — emergency flatten.
4. **Either venue enters maintenance / withdrawal halt > 4 hours** with an open position — flatten, do not re-enter until full liveness restored for 24h.
5. **Funding-formula change announcement on either venue** — pause until the formula is re-modelled and the bot's threshold logic is updated.
6. **Insurance-fund socialised loss event on either venue** (any size) — pause and review counterparty exposure.

Re-deploy criteria: all the above clear, plus 14-day average cross-venue spread on at least 3 monitored pairs back above 5 bp/8h-eq.

See [[when-to-retire-a-strategy]] for the broader framework. Like [[funding-rate-arbitrage]], this is a *pause-able* strategy: the underlying mechanism (cadence mismatch + flow-base divergence) does not disappear, only the spread level does.

## Advantages

- **High Sharpe in active regimes.** 2.5 target Sharpe vs ~1.4 for single-venue funding arb — the cadence mismatch creates a richer signal than either venue's funding rate alone.
- **Fully delta-neutral by construction.** Equal-notional opposing legs cancel directional exposure exactly. Only carry, basis, and counterparty matter.
- **Multi-pair availability.** HL lists 200+ perps; the universe of cross-venue spreads to monitor is large. Diversification across pairs reduces idiosyncratic event risk.
- **Predictable cash-flow.** Like all funding strategies, income accrues continuously. HL pays hourly; CEX pays every 8h. Visibility is much better than directional crypto strategies.
- **Transparent inputs.** Funding rates, marks, depths, OI all publicly observable real-time.
- **Compatible with [[hyperliquid-hlp-basis-arbitrage|HLP]] and [[hlp-cascade-alongside-playbook|HLP-cascade-alongside]] strategies.** Can be stacked in the same sleeve.

## Disadvantages

- **Capital split across two venues = doubled counterparty risk.** Single-venue funding arb concentrates on one exchange; this trade requires *both* venues to be solvent and live throughout the hold. The probability of *either* failing is roughly the sum of the individual probabilities.
- **Execution timing is critical.** Both legs must fire within ~30 seconds of each other; a long inter-leg gap leaves the first leg directionally exposed. Requires WebSocket-grade infrastructure and pre-funded margin on both venues.
- **Capital-inefficient.** 2x capital outlay for 1x notional risk on each side. Higher leverage (3–5x) reduces this but introduces liquidation risk on either leg during stress.
- **Large-MTM events can force suboptimal closes.** Even though delta-neutral, a violent move can stress one leg's margin enough to force a flatten at a worse spread than the modelled exit.
- **Edge decays as more arbs enter.** Documented in the BTC/ETH compression from 2024 to 2025; expected to continue.
- **Operational complexity.** Two-venue WebSockets, two-venue API rate limits, two-venue withdrawal management, two-venue oracle health monitoring. A bug or rate-limit hit on either side is a live-fire risk.
- **Tax complexity across two jurisdictions.** Funding income from HL (DeFi protocol) vs Binance (offshore CEX) may be classified differently in many jurisdictions. After-tax APY can lag headline materially.
- **Subject to HL-specific risks.** Hyperliquid chain risk, [[hyperliquid-hlp-basis-arbitrage|HLP]] market-maker concentration, and HYPE-incentive policy changes all affect HL funding distinct from CEX funding — sometimes creating the spread, sometimes destroying it.

## Sources

**Wiki sources (primary):**
- [[hyperliquid-hlp-basis-arbitrage]] — parent page that lists this trade as a variant. Documents the *"100–300% APR for 2–7 day windows"* and the *"$50–200M extracted by sophisticated cross-CEX arbs in 2024"* numbers cited above.
- [[hyperliquid-perp-trading-map]] — covers this trade as Strategy 4 ("Cross-Venue Funding Rate Arbitrage"), including the worked numerical example.
- [[funding-rate-arbitrage]] — the single-venue parent strategy; this page is the cross-venue variant.
- [[hyperliquid-funding-rate-microstructure]] — the cadence-mismatch detail (HL hourly vs CEX 8h) that creates much of the edge.
- [[funding-rate]] — the underlying instrument-level mechanism.
- [[hyperliquid]] — venue overview and structural features.
- [[binance]], [[bybit]] — counterparty venues and benchmark for funding rates.
- [[cross-exchange-arbitrage]] — broader cross-venue arbitrage family.
- [[hlp-cascade-alongside-playbook]] — adjacent HL-specific strategy that can be stacked.

**Empirical / academic (inherited from [[funding-rate-arbitrage]]):**
- BIS Working Papers No 1087, *Crypto carry* (Schmeling, Schrimpf, Todorov, 2023). Cross-venue carry premia documented at >10% annualised on average, with cited spreads of 60–90% per year between perp and index.
- He, Manela, Xu, Yan, *Fundamentals of Perpetual Futures* (2022, updated 2024). Sharpe 1.8 retail / 3.5 MM-tier on funding-rate arbitrage; cross-venue spreads identified as a sub-strategy.
- "The Two-Tiered Structure of Cryptocurrency Funding Rate Markets", *Mathematics* MDPI (2025) — shows CEXes lead price discovery; one-way information flow CEX→DEX. Useful framing for *why* HL funding lags / leads CEX funding asymmetrically.

**Industry / mechanics:**
- Hyperliquid funding-rate documentation: 1-hour funding interval, predictive-mid premium calculation. (See [[hyperliquid]].)
- Binance funding documentation: 8h interval, 0.01% interest baseline, clamped premium component.
- Bybit, OKX funding-rate mechanics: similar 8h cadence with venue-specific premium formulas.
- Coinglass, Velo Data, Amberdata, Laevitas: cross-venue funding aggregators used in production.

**Regime/event evidence:**
- 2024 HYPE airdrop + memecoin period: peak HL-vs-CEX divergence; 100–300% APR windows widely reported by cross-venue arb desks.
- Late-2024 to 2025 compression: BTC/ETH spreads on majors compressed sharply as more capital deployed; alts and memes remain wide.
- HLP JELLYJELLY incident (March 2025) — coordinated thin-pair attack creating a transient HL-specific funding dislocation distinct from CEX. (See [[hyperliquid-hlp-basis-arbitrage]].)

## Related

- [[funding-rate-arbitrage]] — single-venue parent strategy.
- [[hyperliquid-funding-rate-microstructure]] — the hourly-vs-8h cadence detail.
- [[hyperliquid-hlp-basis-arbitrage]] — parent page; HLP-aware HL strategies.
- [[hlp-cascade-alongside-playbook]] — adjacent HL-cascade strategy (can be stacked).
- [[funding-rate]] — instrument-level mechanism.
- [[perpetual-futures]] — contract type.
- [[cross-exchange-arbitrage]] — broader cross-venue arb family.
- [[basis]] / [[basis-trading]] / [[cash-and-carry]] — broader basis-trade lineage.
- [[delta-neutral]] — hedging principle.
- [[edge-taxonomy]] — structural + latency edge categories.
- [[failure-modes]] — kill-criteria source taxonomy.
- [[when-to-retire-a-strategy]] — pause-vs-retire framework.
- [[hyperliquid]] — primary venue.
- [[binance]], [[bybit]] — counterparty venues.
- [[coinglass]] — primary cross-venue funding aggregator.
- [[liquidation]] — risk to either leg if margin breaks.
- [[ftx]] — canonical counterparty-failure reminder.
- [[hyperliquid-perp-trading-map]] — broader HL strategy map; this is Strategy 4 there.
