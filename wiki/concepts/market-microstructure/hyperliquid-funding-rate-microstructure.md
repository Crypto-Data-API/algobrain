---
title: "Hyperliquid Funding Rate Microstructure"
type: concept
created: 2026-05-05
updated: 2026-07-13
status: excellent
tags: [crypto, defi, derivatives, market-microstructure, volatility]
aliases: ["HL Funding Mechanics", "Hyperliquid Hourly Funding"]
related: ["[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[hyperliquid]]", "[[hyperliquid-oracle-mechanics]]", "[[hyperliquid-vault-architecture]]", "[[hl-vs-cex-funding-divergence]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[cryptodataapi]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[funding-rate]]", "[[perpetual-futures]]"]
difficulty: advanced
---

# Hyperliquid Funding Rate Microstructure

[[hyperliquid|Hyperliquid]] settles [[perpetual-futures|perp]] [[funding-rate|funding]] **every hour** — 24 settlement points per UTC day — versus the 8-hour cadence used by [[binance]], [[bybit]], and [[okx]] (3 settlements per day). The headline difference: a Hyperliquid arbitrageur can compound funding 24 times per day, capture transient funding spikes that a CEX 8h average completely smooths over, and exit a position within the same hour the funding regime turns. This page documents the formula, how mark-vs-oracle deviation drives the rate, how [[hyperliquid-hlp-basis-arbitrage|HLP]] sits inside the funding flow, why Hyperliquid funding diverges from CEXs in characteristic patterns, and the implications for delta-neutral and cross-venue arb.

This is the microstructure layer underneath [[funding-rate-arbitrage]] and [[hl-vs-cex-funding-divergence]] — read those for the strategy expression. Read this for the *mechanism* and the numerical artifacts it produces.

## TL;DR — Key Facts

| Property | Hyperliquid | Typical CEX (Binance/Bybit/OKX) |
|----------|-------------|---------------------------------|
| **Settlement cadence** | Hourly (24×/UTC day) | 8-hourly (3×/day) |
| **Rate basis** | Premium [[twap\|TWAP]] of mark vs oracle, sampled continuously | Premium index + interest, 8h window |
| **Predicted vs realized gap** | None — realized = integrated TWAP | Can drift (gameable on some venues) |
| **Annualization** | `hourly × 24 × 365` | `8h × 3 × 365` |
| **In-flight transparency** | `predictedFundings` endpoint exposes next-hour estimate | Mostly hidden |
| **Dominant passive LP** | [[hyperliquid-vault-architecture\|HLP]] vault (takes inventory) | Professional MMs (delta-neutral) |
| **Spike mean-reversion** | ~2-7 hours | ~12-24 hours |
| **Arb cadence** | Bot wakes 24×/day; smaller, faster, more numerous opportunities | Bot wakes 3×/day; fewer, larger, slower |
| **Per-settlement variance** | ~1/8 of an 8h settlement at equal APY → smoother P&L | Larger per-settlement bites |

The thread connecting every section below: Hyperliquid's hourly cadence is not a cosmetic units change — it restructures the *temporal microstructure* of funding, which changes who collects, how fast dislocations correct, and what arb cadence is optimal.

## The Funding Formula

Hyperliquid's funding rate is computed continuously from a [[twap|TWAP]] of the deviation between the perp **mark price** and the **oracle price** (a reference index assembled from external CEX spot venues), then settled hourly. The textbook implementation is:

```
hourly_funding_rate = clamp(
    premium_TWAP / 8 + interest_rate_component,
    -CAP, +CAP
)

where:
  premium_TWAP   = average of (mark_price - oracle_price) / oracle_price
                   sampled every few seconds across the prior hour
  interest_rate_component = ~0.00125% per 8h baseline, scaled to 1h
                          = ~0.00015625% per hour
  CAP            = per-hour cap (typically 0.04% to 0.4% depending on asset tier)
```

A few mechanical notes:

- **Settled hourly, accrued continuously.** Even though cash transfer happens on the hour mark, the rate that gets paid is the average of conditions across the *prior* hour. There is no single 30-second window that determines the payment.
- **Premium component dominates.** Above ~0.005%/h, the interest component is rounding error; the rate is essentially "how far above the oracle did the perp trade, on average, this hour."
- **Clamped.** Each asset has a per-hour cap. Majors (BTC, ETH, SOL) typically cap around 0.04%/h (annualized ~350%). Listed memecoins and thin pairs can cap higher. The cap exists to bound the worst-case payment and prevent oracle-glitch wipeouts.
- **The 8 in `premium_TWAP / 8`** is *not* the 8h CEX cadence — it is the canonical Hyperliquid scaling constant chosen to keep the per-hour rate roughly comparable in magnitude to how a 8h-cadence CEX would express the same premium. (Hyperliquid documentation has historically used variations of this; the practical takeaway is that an annualized rate of `hourly_funding × 24 × 365` is the correct annualization, not `× 3 × 365`.)
- **Prediction is endpoint-exposed.** The Hyperliquid info API exposes a `predictedFundings` endpoint that returns the expected funding for the *next* settlement, computed from the current premium TWAP-in-progress. This is unusual — most CEXs hide the in-flight calculation. The transparency means a fast operator can position 30+ minutes ahead of the actual settlement when the predicted rate diverges meaningfully from the trailing average.
- **No "predicted vs realized" gap.** Unlike Binance, where the displayed predicted funding can drift from the realized funding due to the way the premium is sampled, Hyperliquid's realized funding equals the integrated TWAP — what you see in flight is what you pay. This eliminates a class of micro-arb that exists on CEX (gaming the predicted-vs-realized gap).

The deployed numbers from the [[hyperliquid-market-snapshot-2026-04-06|2026-04-06 snapshot]] make the scale concrete:

- BTC: 0.000655%/h → 24 × 365 × 0.000655% = **5.74% APY**
- ETH/SOL/HYPE: 0.00125%/h → **10.95% APY** (right at the interest baseline)
- FARTCOIN: 0.00738%/h → **64.6% APY**

These numbers are not "tiny" because they are hourly — multiply by 24 × 365 to get the annualized equivalent.

## Hourly vs 8-Hour Cadence: What Changes

A naive observer might say "8h funding paid 3×/day vs 1h funding paid 24×/day, same total — just different units." This is wrong in three important ways.

### 1. Compounding granularity for arb capital

A funding-arb position on a CEX collects funding in 3 discrete chunks. On Hyperliquid it collects in 24 chunks. If funding is constant, the totals are equivalent. But funding is not constant — it spikes and reverts intra-day. The 24-chunk operator can:

- Enter at hour 2 of a spike, exit at hour 7, and capture exactly the spike portion.
- Re-enter at hour 14 when the rate spikes again, exit at hour 18.
- Avoid paying funding during hours 8-13 when the rate was negative.

The 8h CEX operator sees only the average across each 8h window and cannot enter/exit inside the window.

### 2. Faster mean-reversion of funding spikes

When Hyperliquid's mark blows above oracle (e.g., a memecoin face-rip), the *next hour's funding* immediately reflects the prior hour's TWAP. Within 1-2 hours the elevated funding is being paid and the trade flow incentive to short the perp / long spot pulls the perp back toward oracle. On an 8h-cadence venue, the mark can stay disconnected for a much longer wall-clock window because the next funding payment is potentially 7+ hours away — there is no near-term cash-flow incentive to compress the basis.

Empirically, Hyperliquid's funding spikes mean-revert in ~2-7 hours. The same flow on Binance can persist for 12-24 hours before the next 8h funding settlement forces a reckoning.

### 3. Different optimal arb cadence

Operationally, an HL funding-arb bot wakes up 24×/day to evaluate entry/exit. A CEX bot wakes up 3×/day. This means:

- **More signals.** Entry triggers fire 8× more frequently.
- **Tighter rebalance windows.** Delta drift on the spot leg is checked hourly, not every 8 hours.
- **Higher operational cost.** More API calls, more rate-limit pressure, more execution surfaces.
- **Lower per-signal capital cost.** Because funding is paid sooner, the time-value-of-money cost of holding a position to the *next* funding event is 1/8 of the CEX equivalent.

This is why Hyperliquid is structurally a better venue for tactical funding arb on top of a CEX-side hedge — see [[hl-vs-cex-funding-divergence]] for the cross-venue strategy.

### 4. Lower variance per settlement

Each individual hourly settlement carries 1/8 the cash-flow magnitude of an 8h settlement at equivalent annualized funding. This has two consequences:

- **Smoother realized P&L.** A funding-arb sleeve on HL produces a much smoother equity curve at the daily level. The Sharpe-ratio-of-funding-income alone (before any directional P&L) is materially higher on HL than on a CEX — typically 1.3-1.5× on the same realized annualized rate.
- **Tighter kill criteria are tractable.** Because each hourly settlement is a small bite, an operator can run intraday kill criteria (e.g., "if 3 consecutive hourly fundings are negative, exit") without those criteria firing on noise. The same logic on an 8h venue would require *days* of bad funding to confirm a regime shift.

### 5. Better intraday news handling

Funding spikes on HL respond within the next hour to news events (CPI prints, FOMC, large unlocks). On a CEX, a CPI surprise at 8:30am UTC may not show up in funding until the 16:00 UTC settlement — 7.5 hours of accumulated dislocation before the cash-flow signal arrives. HL's hourly cadence makes the venue more responsive to intraday catalysts and therefore a faster-acting basis-correction mechanism.

## How Mark-Oracle Deviation Drives Funding

The mechanical chain is direct:

1. **Perp trades above oracle** (longs are aggressive bidders, shorts are reluctant). Mark > oracle by, say, 12 bps.
2. **TWAP samples the deviation** across the next ~3,600 seconds. If the deviation persists, the TWAP centers on +12 bps.
3. **End of hour: funding is computed.** With the canonical /8 scaling, +12 bps premium produces ~0.00015 (1.5 bp) per-hour funding. Longs pay shorts.
4. **Shorts collect, longs pay.** Cash transfer at the hour mark. Aggregated across 24 hours: longs paid ~36 bps for chasing the perp.
5. **Incentive feedback.** That 36 bps/day cost (~13% APY) eventually deters new long entries. New shorts are *paid* to enter. Mark drifts back toward oracle. Funding compresses.

The magnitude is *proportional* to the persistent deviation, not to the price level. This means:

- A 5 bp persistent deviation produces ~0.6 bp/h funding (~5% APY).
- A 50 bp persistent deviation produces ~6 bp/h funding (~52% APY).
- A 200 bp persistent deviation hits the per-hour cap and is clamped.

The clamp is a feature: it bounds losses for the side that is wrong, but it also means that during *very* strong directional regimes, the perp can stay disconnected from oracle longer than the funding mechanism alone could correct. In those regimes, oracle convergence happens via spot price moving up to meet perp, not perp coming down to meet oracle. See [[hyperliquid-oracle-mechanics]] for how the oracle itself is constructed and what its lag characteristics are.

### What "the oracle" actually is

Hyperliquid's oracle is constructed as a weighted median of CEX spot prices for the underlying asset. The composition typically draws from Binance, OKX, Bybit, Coinbase, and Kraken (with weights reflecting depth and liquidity). For TradFi `xyz:` perps, the oracle is sourced from third-party price providers (Pyth and similar) covering the underlying instrument's reference exchange.

This construction has implications for funding behavior:

- **The oracle lags spot by sub-second windows.** During fast moves, the perp price (live order book) leads the oracle by a few hundred milliseconds. The premium-TWAP captures this lead, and funding accumulates accordingly.
- **CEX-spot moves drive HL funding.** If the underlying CEX spot for BTC suddenly drops 0.5%, the HL oracle drops with it. If the HL perp does not drop at the same speed (because order book queue dynamics differ), the perp briefly trades at a positive premium to oracle and funding spikes positive — even though directionally the market is selling off.
- **Manipulating the oracle directly is hard but not impossible.** If a malicious actor can move CEX spot for a thinly-traded HL pair, they can move the HL oracle, which moves the funding direction. This is a known attack vector for smaller pairs and is why HL applies clamps and uses median-of-multiple-sources.

## HLP's Role in Funding

[[hyperliquid-vault-architecture|HLP]] is the protocol's own market-maker / liquidator vault. Its role in funding flow is structural and worth understanding carefully because **HLP's residual book delta is the single largest determinant of whether HLP collects or pays funding on a given asset.**

### Steady-state: HLP is structurally short-funding-payer

Most retail flow on Hyperliquid is *long-biased*. Retail wants leveraged upside. When retail aggressively buys the perp, HLP is the natural counterparty (passive market-maker on the offer). HLP ends up *short* the perp, accumulating a delta-negative book.

Because most retail is long, the perp persistently trades at a small positive premium to oracle. Funding is positive. **The shorts collect funding. HLP is short. Therefore HLP collects funding.**

This is why HLP's headline yield in bull regimes (50-100% APR documented in 2024) is dominated by funding income, not spread capture or liquidation fees.

### Stress-state: HLP can briefly become a funding payer

When a memecoin pumps violently and HLP is long (because too many shorts were bidding the perp down past oracle, HLP filled them on the bid and is now long), or when HLP gets stuck on the wrong side of a thin-pair manipulation (the [[jellyjelly-incident-march-2025|JELLYJELLY incident]] in March 2025 is the canonical example), funding can flip negative against HLP's positioning. In those windows, HLP pays funding, eats the basis blowup, and depositors take a paper drawdown.

### Implication for HLP depositors

HLP yield is *structurally tied* to retail's leverage demand. The key signal:

- High aggregate funding across HL pairs → HLP collecting → high HLP APR.
- Low or negative funding → HLP paying → low or negative HLP APR.

If you are a passive HLP depositor, monitor the aggregate funding across the top HL pairs. When the aggregate compresses below the interest baseline (~10.95% APY equivalent) for >7 days, expect HLP yield to compress with it. See [[hyperliquid-hlp-basis-arbitrage]] for the active strategies built on this dynamic.

## Why Hyperliquid Funding Diverges From CEX Funding

If [[binance]], [[bybit]], [[okx]], and Hyperliquid all priced the same BTC, you might expect identical funding. They don't. The divergence has structural sources:

### Different liquidity provider mix

CEXs are dominated by professional [[market-maker|market-makers]] (Wintermute, GSR, Cumberland, Jump) running tight, mostly delta-neutral books. They quote both sides aggressively and rarely accumulate large directional inventory. HL has a much smaller pro-MM presence relative to its volume; HLP is the dominant passive provider, and HLP's job description includes *taking inventory*. This means HL marks can drift further from oracle before pro-MMs arbitrage them back.

### Different retail base

HL retail skews younger, more degen, more leverage-hungry. Memecoin perps (FARTCOIN, MON, kPEPE) attract speculators who would not have been on Bybit five years ago. This shifts the leveraged-long bias upward on HL relative to CEX equivalents.

### Different listed pairs

HL lists assets that no major CEX will list — the long tail of HIP-3 listed memecoins, plus the `xyz:` prefix TradFi assets (xyz:CL, xyz:GOLD, xyz:SP500, xyz:TSLA). For these assets there is no CEX funding to compare against; the HL funding is the only funding. Funding behavior on these pairs is its own microstructure subject:

- **TradFi `xyz:` perps** trade 24/7 but the underlying spot trades only during market hours. Over a weekend, HL's xyz:SP500 perp can drift several percent from the Friday close based on crypto-native sentiment. When NYSE reopens Monday, the perp must converge to spot — funding does part of this work, but the hour-of-Monday-open price move does most of it. Funding on xyz: pairs is therefore noisier and less informative than crypto funding.
- **Memecoin-only pairs** have no spot leg of equivalent depth on a CEX, so the funding rate cannot be easily arb'd. Funding on these pairs can persist at extreme levels (FARTCOIN at 0.00738%/h = 64.6% APY) for days because there is no professional desk willing to short the perp into a 30%-overnight-rip risk profile.

### Different fee and listing economics

HL's 0.015% maker fee (vs Binance 0.02%, GMX 0.05-0.07%) makes passive provisioning cheaper. Pro market-makers can quote tighter, in theory pulling funding down. In practice the effect is dominated by the retail-flow asymmetry above.

## Cross-Venue Divergence Patterns

Three patterns recur across thousands of observed hours:

### Pattern 1 — Memecoin pump: HL > CEX

When a memecoin or HL-favored asset pumps, HL retail piles in via leverage. HL funding spikes 5-10× the CEX equivalent. Example: in 2024 memecoin episodes, HL funding on similar-sector tokens often ran 50-150% APY-equivalent while Bybit funding on the same sector ran 20-40%. Arb opportunity: short HL perp / long CEX perp (where listed) or long spot.

### Pattern 2 — Big-cap mean-reversion: HL < CEX

In neutral or mildly mean-reverting BTC/ETH regimes, professional MMs on Binance keep CEX funding pinned just above the interest baseline. HL funding often compresses *below* CEX because HLP's passive provisioning absorbs imbalances rather than pushing premium back to oracle. Observed: BTC funding on HL frequently runs 10-30% lower (in absolute APY-equivalent) than on Binance during quiet periods.

### Pattern 3 — Capitulation: HL flips negative first

In a fast risk-off (BTC drops 5%+ in an hour), HL funding can flip negative within 1-2 hourly settlements as longs deleverage and the perp briefly trades below oracle. CEX funding takes longer to reflect the same flow because the next 8h settlement is hours away. Cross-venue arb: long HL perp (collect negative funding flowing the other way) / short CEX perp.

### Pattern 4 — Listing premium decay

Newly-listed pairs on HL routinely open with extreme positive funding (50-200% APY-equivalent) as the pair attracts speculative long flow before professional desks ramp up to provide passive offer. The decay path is roughly: hour 0 funding at the per-hour cap; hour 24 still 3-5× the eventual mean; hour 168 (one week) compressed near the new equilibrium. Pro arb desks specifically watch new HL listings as a recurring source of capturable funding income — *if* a hedge venue is available.

### Pattern 5 — Funding-rate convergence after CEX settlement

Within ~30-60 minutes after each CEX 8h funding settlement, the cross-venue spread tends to compress as CEX funding-arb operators rebalance and pro MMs re-quote. HL operators who entered a divergence position can target exit during these windows for cleaner execution. Conversely, the period *just before* a CEX settlement (where the upcoming 8h rate is locked in) tends to see widening cross-venue spreads as positioning tilts.

These are tendencies, not laws. The active arb strategy is documented at [[hl-vs-cex-funding-divergence]].

## The 2026-04-06 Snapshot — Concrete Examples

From [[hyperliquid-market-snapshot-2026-04-06]]:

| Asset | Funding (per hour) | Annualized | Interpretation |
|---|---|---|---|
| BTC | 0.000655% | **5.74% APY** | *Below* the interest baseline (~10.95%). Mildly bearish positioning; longs are not aggressively bidding. No funding-arb entry signal. |
| ETH | 0.00125% | **10.95% APY** | At the interest baseline. Funding is essentially the carrying cost of capital — neutral. No edge. |
| SOL | 0.00125% | 10.95% APY | Same as ETH. Neutral. |
| HYPE | 0.00125% | 10.95% APY | Neutral. Despite HYPE's volatility, current positioning is balanced. |
| ZEC | 0.00125% | 10.95% APY | Neutral. |
| XRP | 0.000873% | 7.65% APY | Mildly below baseline. |
| FARTCOIN | 0.00738% | **64.6% APY** | **6× the baseline.** Strongly long-biased crowded positioning. Classic [[funding-rate-arbitrage]] entry signal — short FARTCOIN perp on HL, hedge with spot if available, collect ~5%/month while it lasts. Caveat: thin liquidity, high liquidation tail risk, and capacity is bounded by FARTCOIN's $8M daily volume. |
| PAXG | 0.00125% | 10.95% APY | Neutral. Gold's slight pullback (-0.30%) is not yet reflected in funding. |

The snapshot shows the typical regime fingerprint:

- **Majors compressed.** Funding on BTC/ETH/SOL is at or below the interest baseline. This is consistent with the post-2024 regime where [[ethena-usde]], Resolv, and Pendle have industrialized the trade and compressed major-pair funding.
- **Long-tail elevated.** FARTCOIN at 64.6% APY is doing all the heavy lifting for funding-arb yield. The trade-off: it is small-capacity, high-vol, and one bad-day liquidation can wipe a quarter's collected funding.
- **Cross-venue divergence latent.** With BTC at 5.74% APY on HL, the same window on Binance (8h funding) was likely showing higher funding because Binance's larger leveraged-long base typically keeps majors slightly above the baseline. This is exactly the Pattern 2 setup — go long HL perp, short Binance perp, collect the spread.

## Funding Spikes and Dislocations

A "funding spike" on Hyperliquid is defined operationally as: hourly funding > 5× the trailing 7-day mean of that hourly rate, sustained for at least 2 consecutive hours.

Empirical lifecycle of a typical spike:

1. **Hour 0-2: Trigger.** A narrative event, listing, or whale long ramps the perp 30-100 bps above oracle.
2. **Hour 2-4: Peak.** Funding hits the per-hour cap or close to it. Aggregate funding APY-equivalent ranges from 100% to 600%.
3. **Hour 4-12: Arb in.** Sophisticated operators short the perp / long spot. Pro MMs widen quotes. Premium compresses to 20-50 bps.
4. **Hour 12-72: Decay.** Funding decays exponentially toward the trailing mean. Most of the convergence happens in the first 24 hours.
5. **Hour 72-168: Tail.** Funding sits modestly elevated (1.5-3× mean) for several days as residual long bias bleeds out.

The full window from spike onset to full normalization is typically **2-7 days**. During that window, an arb sleeve can collect 5-15% on deployed capital before the trade closes.

The dangerous failure mode: a spike that does *not* mean-revert because the underlying narrative continues to attract new leveraged longs. In that case, funding stays elevated, but spot price keeps rising, and the short-perp leg of the arb takes mark-to-market pain that can liquidate the position before the funding income compounds. This is why [[funding-rate-arbitrage]] strategies on HL run with isolated margin and a hard kill switch on the perp leg's mark-to-market drawdown.

### Anatomy of a representative spike

A representative HL funding spike (memecoin face-rip, March 2025 era):

| Hour (UTC) | Asset price | Funding (per hour) | Annualized | Notes |
|---|---|---|---|---|
| 14:00 | $0.10 | 0.0010% | 8.8% | Pre-spike baseline |
| 15:00 | $0.13 | 0.0042% | 36.8% | Long flow ramping |
| 16:00 | $0.18 | 0.0220% | 192.7% | Spike onset |
| 17:00 | $0.22 | 0.0400% | 350.4% | At the per-hour cap |
| 18:00 | $0.21 | 0.0380% | 332.9% | Cap held |
| 19:00 | $0.21 | 0.0250% | 219.0% | Pro arb in |
| 20:00 | $0.20 | 0.0140% | 122.6% | Spread compressing |
| 22:00 | $0.20 | 0.0080% | 70.1% | |
| 06:00 (next day) | $0.20 | 0.0035% | 30.7% | Tail |
| 14:00 (24h later) | $0.20 | 0.0018% | 15.8% | Near baseline |

A pro arb that entered at hour 16:00 and held until hour 22:00 collected ~13 bps of cumulative funding (~5%/month annualized just on this single trade) while bearing ~6 hours of mark-to-market exposure. The trade off: had the spike continued past hour 18:00 (i.e., asset moved to $0.30), the short-perp leg would have been deeply underwater, requiring margin top-up or accepting liquidation.

### Why some spikes don't compress

Three conditions where an apparently-arbable funding spike fails to revert:

1. **No spot leg available.** HL-listed memecoins often have no deep spot venue. Without a hedge, the trade is just a short-the-pump bet, which is not arb.
2. **Continuing narrative inflow.** A narrative that keeps minting new long-biased speculators (memecoin season tops, AI-agent token launches) can sustain elevated funding for weeks.
3. **HLP positioning amplification.** If HLP is already heavily long going into the spike, HLP's own delta-management may force it to short more aggressively *after* the spike, which paradoxically deepens its negative carry exposure and slows convergence.

### Funding regime vs volatility regime

Funding is a positioning signal, and positioning interacts with the broader [[market-regime]]. The cross-product matters for both arb operators and HLP depositors:

- **Low [[volatility]] + compressed funding** — the quiet, industrialized regime. Major-pair funding pinned near the interest baseline; HLP yield dominated by spread capture; arb edge thin. This is the funding analogue of a *Calm* [[volatility-regime-classification|vol regime]].
- **High volatility + spiking funding (one-sided)** — crowded directional positioning. Funding-arb edge is richest here, but so is liquidation tail risk on the unhedged perp leg. The reward and the danger rise together.
- **High volatility + funding flipping sign** — capitulation/deleveraging. Funding can invert within 1-2 hourly settlements (see [[#Pattern 3 — Capitulation: HL flips negative first]]); HLP can be caught long into a collapse, paying funding *and* taking mark-to-market drawdown.

The practical takeaway: read aggregate funding *together with* the volatility regime, not in isolation. A funding spike in a calm regime is a clean arb; the same spike during a fast risk-off is a trap.

## Implications for HLP Depositors

For passive depositors in [[hyperliquid-vault-architecture|HLP]], funding flow is the single most important yield driver:

| Regime | Aggregate HL funding (APY-eq) | HLP APR (typical) | What's happening |
|---|---|---|---|
| Strong bull, leveraged retail piling in | 30-80% | **50-100%+** | HLP short the long-biased flow, collecting funding + spreads. Liquidation fees secondary. |
| Calm bull / sideways | 10-20% | **15-30%** | Funding contributes ~50-70% of yield; spreads and liquidation fees fill the rest. |
| Chop / low vol | 5-12% | **10-20%** | Funding is barely above interest baseline. HLP yield is dominated by spread capture; depositors should expect lower headline numbers. |
| Capitulation / negative funding | 0% to -20% | **negative or ~0%** | HLP can be stuck long during a collapse, paying funding *and* taking mark-to-market drawdown. Historical examples: October 2025 funding crash, March 2025 JELLYJELLY incident. |

Practical heuristic for depositors: **track aggregate hourly funding across the top 10 HL pairs by OI.** When the median across that basket falls below 0.0006%/h (5.25% APY) for more than 7 consecutive days, expect HLP APR to compress materially over the following 30 days. This is your early warning to consider rotating to alternative yield sources or to expect a yield drawdown.

The corollary: a sudden spike in aggregate funding is bullish for HLP yield but can also signal a spike in adverse-selection cost (the same flow that drives funding up also creates the conditions for HLP to take inventory in the wrong direction). Headline yield up *and* tail risk up simultaneously.

## Implications for Cross-Venue Arb

The full strategy is documented at [[hl-vs-cex-funding-divergence]]; the microstructure-level summary:

1. **Use HL hourly granularity to detect divergence sooner.** A CEX 8h funding settlement that ends in 6 hours has not yet "happened" — a divergence can be observed and traded for the 6 hours before the CEX rate even prints.
2. **Hedge on the slower-cadence venue.** Open the HL leg, then hedge on the CEX leg. The CEX leg's funding is locked in only at the 8h settlement, which gives you ~7 hours of "free" basis carry if you time entry just after a CEX settlement.
3. **Exit when the spread compresses past breakeven costs.** Round-trip costs across HL (0.015% maker / 0.045% taker) and a CEX (0.02% maker / 0.05% taker) come to ~10-15 bps. The spread must justify that plus a margin buffer.
4. **Watch for HL-specific risks.** Oracle staleness, [[hyperliquid-oracle-mechanics|oracle attacks]], chain outages, and HLP-positioning dislocations can all break the assumed convergence.

The general principle: **HL's hourly cadence creates more, smaller, faster-converging arb opportunities; the CEX 8h cadence creates fewer, larger, slower-converging ones.** A cross-venue operator can run both cadences in parallel.

### Worked example: BTC HL vs Binance divergence

Concrete numbers from a representative window:

- HL BTC funding (current hour): 0.0008%/h → ~7% APY-equivalent.
- Binance BTC funding (current 8h): 0.012%/8h → ~13.1% APY-equivalent.
- Cross-venue funding spread: ~6% APY-equivalent.

Trade construction:

1. Long 5 BTC perp on Hyperliquid at $69,200 (collect or pay HL funding; here paying ~7% APY).
2. Short 5 BTC perp on Binance at $69,205 (receive Binance funding; here ~13% APY).
3. Net carry: ~6% APY-equivalent on $345k notional, with delta hedged across the two venues.

Daily funding income: 5 × $69,200 × 6% / 365 = ~$56.84/day. Round-trip costs (open + close, both legs, taker mix): ~30 bps of notional = ~$1,038. Breakeven hold: ~18 days. If the spread compresses within 18 days, the trade is unprofitable; if it persists for 30+ days, the trade earns ~$1,700-$2,000 net.

The strategy shines when HL's hourly granularity surfaces a divergence within 1-2 hours of onset — versus a CEX-only operator who would need to wait until the next 8h settlement to observe the same gap.

### Failure modes specific to HL-CEX arb

- **Oracle-vs-spot divergence on HL.** If HL's oracle gets stale during a chain congestion event, the funding rate may not reflect the true cross-venue spread, and the arb position can mark wildly off until the oracle catches up.
- **CEX withdrawal limits.** Daily withdrawal caps on Binance/Bybit/OKX limit how quickly you can rebalance the hedge leg. A locked hedge during a fast move can produce significant slippage on close.
- **HL bridge risk.** Capital must be bridged to HyperBVM. Any bridge incident isolates the HL leg and breaks the hedge.
- **HLP-driven micro-divergence.** If HLP gets stuck on the wrong side, HL funding can briefly diverge from "fair" funding in a direction that fights you. This is rare but can wipe a quarter of carry in one window.

## Tools

The following tools are commonly used to monitor and act on HL funding microstructure:

- **[[coinglass|Coinglass]]** — cross-venue funding aggregation; useful for spotting HL vs CEX divergences in real time. Limitation: Coinglass typically displays HL funding annualized on a 1h basis, while CEX is shown on 8h basis — verify the units before computing spreads.
- **[[hyperliquidscan]]** — Hyperliquid block explorer with funding history, HLP positioning, and per-pair OI charts.
- **[[hypurrscan]]** — community analytics dashboard with HLP vault-level returns, funding-rate heatmaps, and trader leaderboards.
- **Hyperliquid native API** — `https://api.hyperliquid.xyz/info` endpoints for `metaAndAssetCtxs` (funding rates per asset), `fundingHistory`, and `predictedFundings`. The `predictedFundings` endpoint is particularly valuable: it returns the expected funding rate for the *next* hour based on the current premium TWAP, allowing arb positioning ~30 minutes ahead of the actual settlement.
- **Custom infrastructure** — production funding-arb bots typically subscribe to Hyperliquid's WebSocket `bbo` and `trades` channels to compute their own real-time premium TWAP and front-run the official funding calculation.
- **[[velo-data]] / Amberdata / Laevitas** — paid data providers that aggregate funding history across HL + CEXs with consistent units; useful for backtesting cross-venue strategies.

Production-grade tooling typically combines the native API for HL data, a CEX SDK (Binance / Bybit / OKX) for the hedge leg, and a custom premium-TWAP estimator that updates faster than the 1-hour settlement cadence. See [[funding-rate-arbitrage]] for the canonical implementation pattern.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

- [[funding-rate]] — the underlying mechanism across all perp venues.
- [[funding-rate-arbitrage]] — the canonical delta-neutral expression of this microstructure.
- [[hl-vs-cex-funding-divergence]] — the cross-venue arb strategy built on the cadence asymmetry.
- [[hyperliquid]] — the venue.
- [[hyperliquid-oracle-mechanics]] — how the oracle that funding is computed against is constructed.
- [[hyperliquid-vault-architecture]] — HLP's structural role.
- [[hyperliquid-hlp-basis-arbitrage]] — strategies built on HLP's funding-flow exposure.
- [[hyperliquid-perp-trading-map]] — the broader strategy map for HL.
- [[perpetual-futures]] — instrument-level mechanics.
- [[twap]] — the averaging method that smooths the premium computation.
- [[basis]] / [[basis-trading]] — broader basis-trade family.
- [[market-regime]] — funding-regime reading sits inside the broader regime context.
- [[volatility]] — funding spikes and volatility regimes interact (see above).
- [[market-microstructure-overview]] — parent concept area.

## Sources

- Hyperliquid funding-rate documentation: hourly settlement; premium-TWAP-based computation; per-asset clamps. (Public docs.)
- [[hyperliquid-market-snapshot-2026-04-06]] — the source of the BTC/ETH/SOL/HYPE/FARTCOIN funding numbers cited above.
- [[funding-rate-arbitrage]] — canonical strategy page with cost overlay and execution mechanics.
- [[hyperliquid-perp-trading-map]] — strategy-level synthesis covering HL's full surface.
- [[hyperliquid-hlp-basis-arbitrage]] — HLP-vault-specific strategy stack.
- BIS Working Paper No 1087, *Crypto carry* (Schmeling, Schrimpf, Todorov, 2023). https://www.bis.org/publ/work1087.pdf — empirical foundation for crypto funding-rate persistence.
- He, Manela, Xu, Yan, *Fundamentals of Perpetual Futures* (2022/2024), Wharton/WashU. arxiv.org/abs/2212.06888 — perp-vs-index deviation magnitudes and Sharpe estimates.
- Ackerer, Hugonnier, Jermann, *Perpetual Futures Pricing*, Mathematical Finance (2024). doi.org/10.1111/mafi.70018 — theoretical pricing model under funding mechanism.
- "The Two-Tiered Structure of Cryptocurrency Funding Rate Markets," *Mathematics* MDPI (2025). mdpi.com/2227-7390/14/2/346 — CEX-vs-DEX information flow analysis.
