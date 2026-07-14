---
title: "Calendar Spread Arbitrage (Crypto)"
type: strategy
created: 2026-04-07
updated: 2026-07-14
status: good
tags: [arbitrage, crypto, futures, contango, backwardation, term-structure, roll-yield, basis, derivatives]
aliases: ["Calendar Arb", "Term Structure Arbitrage", "Crypto Futures Spread", "Inter-Expiry Basis"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: cost-corrected

# Edge characterization (see [[edge-taxonomy]])
edge_source: [structural, behavioral]
edge_mechanism: "Crypto dated-futures term structure is set by leverage demand and funding expectations, not storage cost. When the near-vs-far (or perp-vs-quarterly) annualised basis dislocates from fair carry, the arb sells the rich expiry and buys the cheap one and is paid by leveraged directional traders who bid one point of the curve without hedging the other — collecting the convergence with far less directional and margin risk than an outright."

# Data and infrastructure requirements
data_required: [dated-futures-curve, perp-funding-rate, spot-price, futures-open-interest, days-to-expiry]
min_capital_usd: 25000
capacity_usd: 50000000
crowding_risk: medium

# Performance expectations (net of both-leg fees, roll, and slippage)
expected_sharpe: 1.3
expected_max_drawdown: 0.12
breakeven_cost_bps: 15

# Decay history
decay_evidence: "BTC/ETH near-dated annualised basis compressed from routinely 20-40% in the 2020-2021 bull to mid-single digits by 2023-2025 as dedicated basis desks and (post-Jan-2024) spot-ETF-driven cash-and-carry flows arbed the curve. Deribit/CME term-structure dislocations that once persisted for days now close in hours on the majors; the wider, longer-lived calendar spreads remain in alt perps/quarterlies and around catalyst events (halvings, ETF flows, large liquidations)."

# Lifecycle
kill_criteria: |
  - annualised calendar spread inside round-trip cost on the monitored curve for 30 consecutive days
  - sleeve drawdown > 12% in any rolling 30-day window
  - a leg's venue enters withdrawal halt / solvency concern with the position open
  - realised spread widening beyond 2x entry edge without a convergence catalyst (thesis broken)

related: ["[[cash-and-carry]]", "[[fork-futures-spot-basis]]", "[[funding-rate-arbitrage]]", "[[basis-trade]]", "[[crypto-spot-perp-futures-triangle]]", "[[contango]]", "[[backwardation]]", "[[basis]]", "[[futures]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Calendar Spread Arbitrage (Crypto)

Calendar spread arbitrage trades the price relationship between two different expiries of the *same* crypto futures — near quarterly vs far quarterly, or the [[perpetual-futures|perpetual]] vs a dated quarterly — on venues like [[deribit|Deribit]], [[cme|CME]], [[binance|Binance]], and OKX. Because crypto has no storage or convenience yield, the term structure is driven almost entirely by **leverage demand and funding expectations**: in bullish regimes the curve is in [[contango]] (far expiries richer), in stress it flattens or inverts into [[backwardation]]. When the inter-expiry annualised basis deviates from fair carry, the arb sells the rich leg and buys the cheap leg, capturing the convergence with a fraction of the directional risk and margin of an outright position. It is a close cousin of [[cash-and-carry]] (spot vs one future) generalised to *two futures*, and it shares the [[funding-rate-arbitrage|funding]] data rails when one leg is a perp.

## Edge source

Mapping to [[edge-taxonomy]], crypto calendar spread arbitrage is **structural + behavioural**:

- **Structural.** Two contracts on the same underlying that both converge to the same spot at their respective expiries *must* have a term structure consistent with no-arbitrage carry (here: the interest/funding cost of holding, since there is no storage). When the observed near-far basis departs from that carry relationship, a mechanical mispricing exists that convergence will close. The relationship is contractual, not opinion.
- **Behavioural.** The *reason* the curve dislocates is leverage demand: directional traders express a view by lifting one part of the curve (usually the near perp/quarterly in a momentum burst, or dumping the near in a liquidation flush) without simultaneously trading the other expiry. That one-sided flow bends the term structure away from fair carry, and the calendar arb is paid to straighten it. It is the same leverage-preference bias that powers [[funding-rate-arbitrage]], viewed on the expiry axis instead of the perp-vs-spot axis.

It is **not** informational or analytical — the full curve is public on every venue. The edge is the operational capability to hold both legs, model fair carry, and warehouse the spread through convergence.

## Why this edge exists

- **No storage anchor, so the curve is pure sentiment carry.** Unlike oil or grain, crypto carry is just the cost of funding a levered position. That makes the term structure unusually *responsive to leverage flows* and prone to dislocation when those flows are one-sided.
- **Leveraged directional demand is lumpy.** ETF-approval manias, halving narratives, and liquidation cascades push leverage into one expiry at a time. Contango steepens when longs pile into the front perp; the curve inverts when a cascade dumps the near. Either way, the *relative* pricing of two expiries decouples from fair carry.
- **Dated-futures liquidity is uneven.** The near perp/quarterly is deep; far quarterlies are thin. Market makers do not always keep the far leg tightly arbed to the near, so a dislocation can persist longer on the back of the curve.
- **Why it does not fully close.** Warehousing a calendar spread through convergence ties up margin, bears mark-to-market path risk (the spread can widen before it narrows), and requires two-venue or two-contract execution. Dedicated basis desks and (since Jan 2024) spot-ETF cash-and-carry flows have arbed the *majors'* curves thin, but the alt curves and catalyst-driven dislocations still pay.

## Null hypothesis

Under a frictionless market with a competitive basis desk on every expiry, the term structure sits exactly on fair carry and the calendar spread earns nothing after costs. Concretely, under the null:

- `annualised_basis(near→far) = funding/carry rate` at every instant; any deviation is inside round-trip cost.
- The near-far spread is a fair reflection of the funding path; it does not mean-revert because it is never dislocated.
- A buy-cheap/sell-rich calendar trade earns zero net after both-leg fees and roll.

The empirical record confirms the null on liquid majors post-2023 (basis desks + ETF flows keep BTC/ETH curves on carry) and fails it on alt curves and around catalysts (dislocations of hundreds of bps annualised that mean-revert over days). **If the monitored curve's annualised spread stays inside round-trip cost for 30+ days, that curve has been arbed into the null and the sleeve should rotate to thinner alt expiries or wait for a catalyst-driven dislocation.**

## Rules

### Entry conditions

1. **Dislocation signal.** The observed annualised inter-expiry basis deviates from modelled fair carry (funding-implied) by **≥ 300 bps annualised** (majors) or **≥ 600 bps** (alts, to cover wider slippage on the thin far leg). Fair carry is anchored to the [[funding-rate|funding]]-implied rate, not a storage model.
2. **Direction.**
   - Curve too steep (far too rich vs carry): **sell far, buy near** (short the rich back, long the cheap front).
   - Curve inverted / near too rich (backwardation beyond carry, e.g. a liquidation flush): **buy far, sell near**.
3. **Persistence.** The dislocation has held beyond the fair-carry band for at least one funding interval — filters single-print noise from a fat-fingered far quote.
4. **Liquidity gate.** Both legs show ≥ 3× intended notional at the target band; the far/thin leg is the binding constraint on size.
5. **Convergence horizon.** Time-to-near-expiry is long enough for the spread to normalise but short enough to bound warehousing cost; avoid entering a leg inside its final delivery/settlement window.

### Exit conditions

1. **Mean reversion.** Spread returns to the fair-carry band — the primary profit mechanism; close both legs.
2. **Convergence at expiry.** Hold the near leg to expiry (it converges to spot/index by settlement mechanics) and roll or close the far leg; captures the full modelled basis.
3. **Roll before delivery/settlement.** Close or roll the near leg *before* it enters its settlement window; carry the thesis into the next expiry only if the dislocation persists.
4. **Stop / thesis-break.** Spread widens against you beyond **2× the entry edge** with no convergence catalyst — the term-structure regime has shifted (e.g. a leverage-driven contango blowout); exit rather than average down.
5. **Venue health.** Withdrawal halt, solvency concern, or margin-parameter change on either leg's venue → flatten.

### Position sizing

- Size to the **thinner (far) leg's 3×-depth**; the near leg is rarely the constraint.
- Exploit **cross-margin relief**: a calendar spread on one venue often receives a large margin offset (the legs hedge each other), improving capital efficiency vs two outrights — but only when both legs are on the same clearing venue.
- Per-venue cap ≤ 20-25% of book for counterparty risk; cap total spread notional to bound the widen-before-converge path risk.

## Implementation pseudocode

```python
# crypto_calendar_arb.py — inter-expiry basis mean-reversion (near vs far / perp vs quarterly)
ENTRY_EDGE_BPS_MAJOR = 300.0     # annualised deviation from fair carry, majors
ENTRY_EDGE_BPS_ALT   = 600.0     # alts (thin far leg)
EXIT_BAND_BPS        = 75.0      # inside this annualised band = converged
STOP_MULT            = 2.0       # exit if spread widens to 2x entry edge (thesis broken)
DEPTH_MULT           = 3.0       # 3x notional at band on the thin leg
PER_VENUE_CAP        = 0.25

def fair_carry_bps(funding_apy: float) -> float:
    # crypto carry = funding-implied rate (no storage/convenience yield)
    return funding_apy * 1e4

def annualised_basis_bps(near_px, far_px, days_between) -> float:
    return (far_px - near_px) / near_px * (365.0 / days_between) * 1e4

def decide(mkt, pos, book, is_alt=False) -> dict:
    edge_floor = ENTRY_EDGE_BPS_ALT if is_alt else ENTRY_EDGE_BPS_MAJOR
    basis = annualised_basis_bps(mkt.near_px, mkt.far_px, mkt.days_between)
    carry = fair_carry_bps(mkt.funding_apy)
    dev = basis - carry                              # + => curve too steep (far rich)

    if pos is not None:
        if abs(dev) <= EXIT_BAND_BPS:
            return {"action": "EXIT", "reason": "converged to fair carry"}
        if abs(dev) >= STOP_MULT * pos["entry_dev"]:
            return {"action": "EXIT", "reason": "thesis broken (2x widen)"}
        if mkt.near_in_settlement_window:
            return {"action": "ROLL_NEAR", "reason": "avoid delivery"}
        return {"action": "HOLD"}

    if abs(dev) < edge_floor:
        return {"action": "WAIT", "reason": f"dev {dev:.0f}bps inside floor"}
    if min(mkt.near_depth, mkt.far_depth) < DEPTH_MULT * book["ticket"]:
        return {"action": "WAIT", "reason": "insufficient far-leg depth"}
    if book["venue_exposure"] + book["ticket"] > PER_VENUE_CAP * book["capital"]:
        return {"action": "WAIT", "reason": "per-venue cap"}

    if dev > 0:   # far too rich -> sell far, buy near
        return {"action": "OPEN", "sell": "FAR", "buy": "NEAR",
                "entry_dev": dev, "reason": f"curve {dev:.0f}bps over carry"}
    else:         # near too rich / inverted -> buy far, sell near
        return {"action": "OPEN", "sell": "NEAR", "buy": "FAR",
                "entry_dev": dev, "reason": f"curve {dev:.0f}bps under carry"}
```

The production version wraps this with: a live dated-futures curve builder (Deribit/CME/Binance dated-futures feeds — *not* served by CryptoDataAPI; assemble natively), a funding-implied fair-carry model, cross-margin optimisation on the clearing venue, a roll scheduler that steps the near leg forward before settlement, and a manual kill switch.

## Indicators / data used

- **Dated-futures curve (multiple expiries)** — the raw term structure; built from native Deribit/CME/Binance dated-futures feeds.
- **Perp [[funding-rate]]** — the anchor for fair carry (crypto's carry is funding, not storage) and the near leg when trading perp-vs-quarterly.
- **Spot/index price** — the convergence target both legs settle toward.
- **[[open-interest]] per expiry** — liquidity/crowding on each leg; thin far OI = wider slippage and longer-lived dislocations.
- **Days-to-expiry** — sets the convergence horizon and the annualisation of the basis.
- **Cross-margin schedule** — the calendar offset that determines capital efficiency.
- **Sources** — Deribit/CME/Binance dated-futures APIs and [[coinglass]] for the curve; cryptodataapi.com for funding, OI, spot, and backtesting.

## Example trade

**Setup (illustrative, BTC perp-vs-quarterly on a single venue, 2026-06):**

- BTC spot/index: $71,000. Perp (near leg) trades at index. September quarterly (far, 82 DTE) trades at **$74,900**.
- Annualised basis (perp→Sep): (74,900 − 71,000)/71,000 × (365/82) = **24.4% annualised**.
- Funding-implied fair carry: ~**9% annualised**. Deviation: **~1,540 bps over carry** — the September contract is richly bid by leveraged longs positioning for a Q3 rally.
- Sleeve: $100k; ticket $50k notional per leg; venue cross-margin offset gives ~4:1 relief on the spread.

**Trade: sell the rich far, buy the cheap near (short Sep quarterly, long perp), delta-neutral by construction:**

**Cost overlay (realistic, never naive):**

| Leg | Amount | bps on $50k |
|---|---|---|
| Perp taker (0.04%) entry | −$20 | 4.0 |
| Sep quarterly taker (0.05%, thinner) entry | −$25 | 5.0 |
| Slippage, far leg ($50k into thin book) | −$30 | 6.0 |
| Perp funding paid on the long-perp leg over hold (net small, ~9% APY × 40d × 50k) | −$493 | — |
| Exit fees + slippage (both legs) | −$75 | 15.0 |
| **Total friction** | **~$643** | — |

**Result:** the September contract's premium normalises from 24.4% toward ~11% annualised over ~40 days as the leveraged-long positioning unwinds. Spread capture: the ~13.4-point annualised richness on $50k over 40 days ≈ (0.134 × 40/365 × $50,000) ≈ **$734 gross**, minus ~$643 friction (dominated by the perp funding you *pay* on the long-perp leg while short the rich quarterly) → **~$91 net** — modest, and highly sensitive to the funding cost of carrying the near leg. Had this been an *inverted* alt curve after a liquidation flush (buy the cheap far, short the rich near, and *collect* funding on the short-perp leg), the funding term flips in your favour and the net is materially larger. The honest cost-corrected lesson: **the funding you pay/collect on the perp leg often dominates the calendar P&L — model it explicitly, never as an afterthought.**

## Performance characteristics

Cost-corrected picture (2024-2026):

| Metric | Value | Note |
|---|---|---|
| Net edge, BTC/ETH majors | thin (single-digit % annualised) | Basis desks + ETF cash-and-carry keep the curve on carry. |
| Net edge, alt curves / post-catalyst | 10-40%+ annualised on the window | Where the durable money is; wider, longer-lived dislocations. |
| Sharpe (target) | 1.3 | Carry-plus-mean-reversion body; fat tail from contango blowouts. |
| Max drawdown (sleeve) | 8-12% | Driven by spread widening (leverage-driven curve steepening), not spot direction. |
| Win rate (per spread) | 75-90% | Most dislocations mean-revert; losses are the thesis-break widenings. |
| Breakeven cost budget | ~15 bps round-trip | Both-leg taker + far-leg slippage + roll. |
| Capital efficiency | good | Cross-margin offset on same-venue calendar spreads. |

**Costs the naive version ignores:** (1) the **perp-leg funding term** — carrying a perp leg means paying or collecting funding continuously, which frequently dominates the calendar P&L; (2) **far-leg slippage** — the back of the curve is thin, so entry/exit on the far leg costs multiples of the near; (3) **roll cost** — holding through multiple expiries means repeatedly crossing the spread; (4) **margin-parameter risk** — a venue raising spread margin during stress can force a de-lever at the worst spread; (5) **path risk** — the spread can widen well before it converges, and the mark-to-market pain can breach a stop.

## Capacity limits

- **BTC/ETH dated futures (Deribit/CME):** OI is large but the *dislocations* are small and short-lived — economic capacity before you compete the spread to carry is low-tens of $M per event.
- **Alt quarterlies / perp-vs-quarterly:** wider spreads but thin far OI — ~$1-10M per event, gated by the far leg.
- **Catalyst windows** (ETF-flow days, halving, liquidation cascades): temporarily deeper and wider, but crowded by the same basis desks.

Aggregate is bounded by dated-futures OI (far smaller than perp OI). Working capacity for an individual operator: **$25k-$5M**, above which far-leg slippage and the operator's own flow close the dislocation being harvested.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Crowding by basis desks + ETF flows (Failure Mode #4).** Post-Jan-2024 spot-ETF cash-and-carry and dedicated basis desks arbed the BTC/ETH curve thin; the majors now sit near carry most of the time.
2. **Contango blowout / leverage-driven steepening (Failure Mode #6, the signature tail).** A momentum burst can steepen the curve far beyond your entry edge before it reverts — the crypto analogue of a "the spread went against me violently" event. If the stop is loose, this is where the year's carry is lost.
3. **Curve inversion in a crash.** A liquidation cascade dumps the near contract, inverting the curve against a long-near/short-far position; the "safe" convergence trade takes a one-sided mark loss.
4. **Perp-funding drift.** When a perp leg is used, funding can move against the carry assumption, quietly turning a modelled-profitable spread into a loss.
5. **Venue/counterparty and margin risk (Failure Mode #7).** A withdrawal halt, solvency scare, or spread-margin hike on the clearing venue forces a de-lever mid-thesis.
6. **Roll/settlement mishandling.** Missing the near-leg roll into its settlement window can force delivery/settlement mechanics at an unfavourable mark.

## Kill criteria

Pause the sleeve on any of:

1. **Annualised calendar spread inside round-trip cost on the monitored curve for 30 consecutive days** — that curve is in the null; rotate to alts/catalysts.
2. **Sleeve drawdown > 12%** in any rolling 30-day window.
3. **A leg's venue enters withdrawal halt / solvency concern** with the position open — flatten immediately.
4. **Spread widens beyond 2× entry edge without a convergence catalyst** — thesis broken; exit, do not average down.
5. **Venue spread-margin parameter change** that invalidates the capital-efficiency assumption — re-model before re-entering.

Re-deploy: a fresh dislocation ≥ the entry floor on a curve with a functioning roll path, plus venue health confirmed for 24h. See [[when-to-retire-a-strategy]] — the *mechanism* (leverage-driven term-structure dislocation) recurs every cycle, so this is pause-able; the majors trend to null between catalysts while alts and event windows keep paying.

## Advantages

- **Lower risk than an outright.** The spread dampens directional moves; both legs share the same underlying and converge together.
- **Capital-efficient via cross-margin.** Same-venue calendar spreads receive large margin offsets vs two outright positions.
- **Structural convergence.** Both legs settle to the same spot/index by expiry mechanics, giving the trade a hard anchor.
- **Recurring, catalyst-driven supply.** Every leverage cycle (ETF flows, halving, liquidations) regenerates term-structure dislocations.
- **Shares rails with [[funding-rate-arbitrage]] and [[cash-and-carry]].** Marginal infrastructure cost to add it to a basis sleeve is low.

## Disadvantages

- **Perp-leg funding can dominate P&L.** The continuous funding on a perp leg frequently swamps the calendar edge and must be modelled explicitly.
- **Convergence is not guaranteed on your timeline.** The spread can widen (violently, in a contango blowout) before it reverts.
- **Thin far leg.** Back-of-curve slippage and wider spreads erode the edge and cap size.
- **Two-leg execution + roll complexity.** Both legs must be managed and rolled before settlement; leg risk if not filled together.
- **Venue/margin risk.** A spread-margin hike or venue failure forces de-lever at the worst moment.
- **Edge decay on majors.** Basis desks and ETF cash-and-carry have compressed BTC/ETH curves toward carry.

## Sources

- Crypto basis / cash-and-carry literature and exchange data — BTC/ETH annualised basis of 20-40% in the 2020-2021 bull compressing to mid-single digits by 2023-2025 as basis desks and spot-ETF cash-and-carry (post-Jan-2024) arbed the curve; establishes the decay and the funding-anchored fair-carry model.
- Deribit / CME / Binance dated-futures mechanics — quarterly/monthly expiry, index settlement, and the cross-margin offsets that make calendar spreads capital-efficient; the source of the live curve.
- [[funding-rate-arbitrage]] — the perp-vs-spot expression of the same leverage-demand carry; the funding rail this strategy shares and the reason the perp leg's funding dominates calendar P&L.
- [[cash-and-carry]] — the spot-vs-one-future special case this generalises to two futures.
- Volatility-term-structure blow-ups (e.g. equity "Volmageddon", Feb 2018) — out-of-crypto-scope context for how a one-sided leverage flush can violently steepen/invert a term structure; the mechanism the crypto contango-blowout tail mirrors.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does **not** serve the full dated-quarterly-futures curve — assemble that from native Deribit/CME/Binance dated-futures feeds. Use CryptoDataAPI for the **funding anchor** (fair carry), **OI/liquidity per expiry proxy**, **spot/index reference**, and **backtesting**.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange perp funding (fair-carry anchor + perp leg)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange OI (crowding/liquidity proxy)
- `GET /api/v1/derivatives/summary?coin=BTC` — combined derivatives overview (markdown format available)
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — spot/index reference (convergence target)

**Historical / research:**
- `GET /api/v1/backtesting/funding` — funding archive (fair-carry backtest)
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI)
- `GET /api/v1/backtesting/klines` — OHLCV archive for basis/term-structure studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=BTC"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

## Related

- [[cash-and-carry]] — spot-vs-one-future basis; the special case this generalises.
- [[fork-futures-spot-basis]] — event-driven basis variant.
- [[funding-rate-arbitrage]] — perp-vs-spot carry; shares the funding rail and dominates the perp-leg P&L.
- [[basis-trade]] — the broader basis-trade family.
- [[crypto-spot-perp-futures-triangle]] — the three-instrument extension (spot + perp + quarterly).
- [[contango]] / [[backwardation]] — the term-structure states that create and destroy the trade.
- [[basis]] — the spot-future spread that defines fair carry.
- [[futures]] / [[perpetual-futures]] — the instruments used on each leg.
- [[edge-taxonomy]] — structural + behavioural edge categories.
- [[failure-modes]] — the kill-criteria source taxonomy.
- [[when-to-retire-a-strategy]] — pause-vs-retire framework.
