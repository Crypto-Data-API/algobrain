---
title: "Miner Capitulation Bottom"
type: strategy
created: 2026-06-03
updated: 2026-07-13
status: excellent
tags: [crypto, bitcoin, market-regime, position-trading, quantitative, regime-detection]
aliases: ["Miner Capitulation Bottom", "Hash Ribbon Strategy", "Miner Capitulation Trade"]
strategy_type: quantitative
timeframe: position
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [structural, behavioral]
edge_mechanism: "In deep bear markets, high-cost miners are forced to sell BTC to cover energy costs and eventually capitulate (turn off rigs); that forced, price-insensitive selling exhausts near cycle lows, and its end historically marks a bottoming zone — a structural supply event, not a forecast."
data_required: [hash-rate, miner-reserves, puell-multiple, difficulty, ohlcv-daily]
min_capital_usd: 1000
capacity_usd: 100000000
crowding_risk: low
expected_sharpe: null        # deliberately unestimated — sample too small (see Performance Characteristics)
expected_max_drawdown: null  # mid-accumulation MTM drawdowns of 30-50% must be survivable (see Sizing)
breakeven_cost_bps: null     # spot BTC, multi-month hold — costs are negligible relative to signal noise
decay_evidence: "The signal rests on a SMALL sample (a handful of BTC cycles since 2012), and spot-ETF demand (2024+) plus industrial/public miners with balance-sheet buffers may dampen the classic forced-capitulation dynamic. Treat historical hit rate as low-n."
related: ["[[on-chain-regime]]", "[[bitcoin-cycle-regime]]", "[[crypto-market-regime-taxonomy]]", "[[bitcoin-halving]]", "[[on-chain-analysis]]", "[[institutional-flow-regime]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Miner Capitulation Bottom

The **miner capitulation bottom** is a long-only, position-trading accumulation signal for **Bitcoin** that uses miner-stress metrics — Hash Ribbons (a 30-day vs 60-day hashrate moving-average cross), the Puell Multiple, and on-chain miner reserves — to time the late-bear-market bottoming *zone*. The thesis is structural, not predictive: when BTC trades below the marginal cost of production, high-cost miners are forced to liquidate reserves and eventually power off their rigs, and the *end* of that forced, price-insensitive selling has historically coincided with cycle-low accumulation regions. It is a scale-in, multi-month-hold trade — a way to express the "Miner Capitulation = late-bear bottoming signal" sub-state of basket 7 (On-Chain Intelligence) in the [[crypto-market-regime-taxonomy|14-basket crypto regime taxonomy]] — and emphatically **not** a precise bottom-caller.

> **Note:** This page describes a *zone* signal with a very small historical sample. Read the [[#Null Hypothesis|Null Hypothesis]] and [[#Performance Characteristics|Performance Characteristics]] sections before trusting any backtested hit rate. The classic forced-capitulation dynamic may be structurally weaker in the [[institutional-flow-regime|spot-ETF era]].

## At a Glance

| Attribute | Value |
|---|---|
| **Type** | Long-only [[position-trading|position-trade]] accumulation signal (BTC) |
| **Timeframe** | Multi-month hold (full cycle phase) |
| **Edge source** | Structural (forced miner selling) + behavioral (panic climax) |
| **Core indicators** | Hash Ribbons (30d/60d hashrate MA), Puell Multiple, miner reserves |
| **Signal type** | Confluence **zone**, not a precise bottom-caller |
| **Direction** | Long / accumulate only |
| **Sample size** | Very small (~3-4 BTC cycles) — low confidence |
| **Capacity** | High (~$100M) — deep spot BTC market |
| **Crowding risk** | Low — few will hold through the drawdown |
| **Biggest risk** | Overfitting to a handful of cycles; ETF-era structural change |

## Edge Source

Per [[edge-taxonomy]], the miner-capitulation bottom draws on two of the five edge categories:

- **Structural (primary).** Bitcoin miners are *non-economic, forced sellers* in deep bear markets. Their revenue (block subsidy + transaction fees, denominated in BTC) is fixed by protocol, while their costs (electricity, hosting, debt service) are denominated in fiat and are largely fixed. When the BTC price falls below an individual miner's all-in production cost, that miner must sell BTC — first from reserves, then everything mined — simply to stay solvent. The *least efficient* miners eventually capitulate entirely and switch off, which mechanically reduces network hashrate and, with a lag, difficulty. This is a supply event driven by survival, not by a price forecast — the same family of structural edge as index-rebalance flow or forced fund redemptions, transposed onto a mining cost curve.
- **Behavioral (secondary).** Miner capitulation tends to cluster with *peak fear* in the broader market. The macro tape that pushes BTC below production cost is the same tape that triggers retail panic selling, leverage flushes, and "Bitcoin is dead" narratives. So the structural supply exhaustion and the behavioral selling climax tend to bottom together, and the accumulator is taking the other side of both. See [[behavioral-finance]].

The combination is the point: even if mining economics change (cheaper energy, more efficient ASICs) and dampen the *structural* signal, the *behavioral* selling climax can still produce a low; and even if the market is numb to "Bitcoin is dead" headlines, the *forced* miner supply still has to exhaust. But neither edge is guaranteed to fire on any given cycle, which is why the small-sample caveat dominates everything below.

## Why This Edge Exists

Miner economics are unusually legible, which is what makes this signal tradeable in principle.

1. **Revenue is protocol-fixed and falls in steps.** A miner earns the **block subsidy** plus **transaction fees**. The subsidy halves roughly every four years at the [[bitcoin-halving]] — from 50 → 25 → 12.5 → 6.25 → 3.125 BTC per block. Each halving instantly cuts the BTC revenue of every miner in half (absent a fee surge), tightening the cost squeeze without any price move.
2. **Costs are fiat-fixed and sticky.** Electricity contracts, hosting fees, ASIC depreciation, and debt service are denominated in fiat and do not fall when BTC falls. The marginal miner has an all-in cost per BTC; when market price drops below it, that miner mines at a loss.
3. **Forced selling, then shutdown.** A loss-making miner first sells **reserves** to cover the fiat bill — visible as falling on-chain [[on-chain-analysis|miner reserves]]. When reserves and credit run out, the miner **powers off**: hashrate falls. Because [[bitcoin-halving|the protocol]] retargets **difficulty** roughly every two weeks, a wave of shutdowns shows up as a hashrate decline that the slower difficulty adjustment lags — exactly the divergence the **Hash Ribbons** indicator was designed to catch.
4. **Exhaustion marks a zone.** The forced-selling pressure is finite. Once the highest-cost miners have capitulated, the surviving miners have lower costs (they bought the capitulators' machines cheaply, or run cheaper power), difficulty has dropped to make their economics easier, and the marginal non-economic seller is gone. Historically, the *recovery* of hashrate after a capitulation has roughly coincided with the start of the next accumulation regime.

> **Who is on the other side?** Two groups, both selling for reasons unrelated to fair value: the **forced miner-seller** (an operator dumping BTC to pay an electricity bill, with no view on price) and the **panic seller** (retail and over-leveraged holders capitulating at peak fear). The accumulator is buying the supply both are forced to release.

## Null Hypothesis

This is the section that matters most. **Bitcoin has had only on the order of three to four full price cycles since 2012**, and "miner capitulation" events that were genuine cycle lows are an even smaller subset. With a sample that small, a rule like "buy when the Hash Ribbon recovers" can look spectacular in-sample purely by **curve-fitting to a handful of points**. A naive strategy of "buy a random week within 25% of each cycle low" would also appear to "work" on the same three or four cycles, because cycle lows are, tautologically, followed by recoveries.

Under the null — that the Hash Ribbon and Puell signals carry **no genuine information** about bottoms beyond "price already fell a lot" — we would expect:

- The signal to add nothing over a simple drawdown filter ("BTC is down >70% from its high"); the miner metrics would just be a noisy proxy for "price already crashed."
- No out-of-sample edge: a rule fit on cycles 1–3 would fail on cycle 4, or the parameters that worked would shift cycle to cycle.
- False signals during *mid-bear* hashrate dips (energy crackdowns, regional bans, weather/seasonality in mining) that capitulate hashrate without marking a price bottom — e.g., the 2021 China mining ban dropped global hashrate ~50% with no relation to a cycle low.

The honest position: this strategy should be treated as a **low-confidence, low-n confluence signal**, not a validated edge. It is included in the wiki because it is a *named, mechanistic regime sub-state* that practitioners watch — not because the backtest is statistically significant. Any deployment must size for the real possibility that the historical hit rate is an artifact of three or four lucky draws.

## Rules

The signal is a **confluence** of three miner-stress conditions plus a price-momentum confirmation. None alone is sufficient.

### Conditions (the "capitulation regime is bottoming" state)

1. **Hash Ribbons recovery.** Compute the 30-day and 60-day moving averages of network hashrate.
   - *Capitulation* is flagged when the **30-day MA crosses below the 60-day MA** (hashrate falling — miners going offline).
   - The **buy trigger** fires when, after a capitulation flag, the **30-day MA recovers and crosses back above** the 60-day MA (hashrate stabilizing/rebuilding), **and** a price-momentum confirmation is present (price 10-day MA turning up, or price closing above its own 30-day MA). The price confirmation is what filters out hashrate recoveries that are not yet matched by demand.
2. **Puell Multiple in the low band.** The [[on-chain-analysis|Puell Multiple]] (daily miner USD revenue ÷ its 365-day MA) sits in its historically low band (roughly **< 0.5**, "deep miner stress / undervaluation"). This confirms miner revenue is depressed relative to its own trailing norm.
3. **Miner reserves stabilizing.** On-chain miner reserves have stopped their bear-market draw-down and are **flat-to-rising** over a multi-week window — i.e., forced reserve liquidation has exhausted.

#### Confluence summary

| Signal | "Capitulation bottoming" reading | Why it matters |
|---|---|---|
| **Hash Ribbons** | 30d hashrate MA recovers back above 60d (after a cross-below) | Highest-cost miners have switched off, then the network stabilizes |
| **Puell Multiple** | In the low band (≈ < 0.5) | Miner USD revenue is depressed vs. its own trailing norm |
| **Miner reserves** | Flat-to-rising over weeks | Forced reserve liquidation has exhausted |
| **Price momentum** | Price reclaims its 30d MA / stops making new lows | Filters hashrate recoveries not yet matched by demand |

All four must align — any single metric alone is a known source of false positives (see [[#Null Hypothesis|Null Hypothesis]]).

### Entry — scale-in accumulation

- Treat the signal as a **zone, not a tick.** Begin a **laddered accumulation** when conditions 1–3 align: e.g., deploy the long allocation in 3–5 tranches over several weeks rather than a single market buy, because the true low may print before *or* after the Hash Ribbon recovery.
- Spot BTC only (or low-leverage long perp/futures for capital efficiency, but this is a *spot accumulation* strategy at heart — leverage defeats the multi-month hold).

### Exit — multi-month hold

- **Primary hold:** carry the position into the next cycle's expansion phase. The signal targets the *transition out of late-bear*, so the natural exit is the *return of euphoria* — e.g., Puell Multiple climbing into its high band (roughly **> 3–4**, historically a miner-profit/cycle-top region), not a fixed time stop.
- **Take-profit laddering:** scale out in tranches as price re-rates, mirroring the scale-in. Do not try to sell the exact top.
- **Invalidation stop:** see [[#Kill Criteria|Kill Criteria]] — the signal is invalidated if hashrate rolls back over and reserves resume a sustained decline while price makes new lows.

### Sizing

- Position-trade sizing: a **core allocation** (e.g., a fixed % of the crypto book earmarked for cycle-bottom accumulation), deployed across the laddered tranches. Because the entry zone can be wide and can keep falling, **size so a further 30–50% drawdown from the first tranche is survivable** without forced selling.

## Implementation Pseudocode

```python
# Miner Capitulation Bottom — accumulation-signal sketch
# Spot BTC, position timeframe. Emits ACCUMULATE / HOLD / INVALIDATE states.

import numpy as np

def sma(x, n):
    return np.convolve(x, np.ones(n) / n, mode="valid")

class MinerCapitulationSignal:
    PUELL_LOW   = 0.5    # deep miner-stress band
    PUELL_HIGH  = 3.0    # euphoria / take-profit band

    def __init__(self):
        self.capitulation_flagged = False  # latched once 30d < 60d hashrate

    def state(self, hashrate, price, puell, miner_reserves):
        """
        hashrate, price: daily series (>= 60 samples)
        puell:           latest Puell Multiple value
        miner_reserves:  recent daily series (>= ~30 samples)
        """
        hr30 = sma(hashrate, 30)[-1]
        hr60 = sma(hashrate, 60)[-1]

        # Latch capitulation when 30d hashrate MA dips below 60d MA
        if hr30 < hr60:
            self.capitulation_flagged = True

        # Hash Ribbon "recovery" = ribbon was flagged, now 30d back above 60d
        ribbon_recovery = self.capitulation_flagged and hr30 > hr60

        # Price-momentum confirmation: price above its own 30d MA
        px30 = sma(price, 30)[-1]
        price_confirm = price[-1] > px30

        # Miner reserves: forced liquidation exhausted (flat-to-rising 4 weeks)
        res_slope = np.polyfit(np.arange(len(miner_reserves[-28:])),
                               miner_reserves[-28:], 1)[0]
        reserves_stable = res_slope >= 0

        puell_low = puell < self.PUELL_LOW

        accumulate = (ribbon_recovery and price_confirm
                      and puell_low and reserves_stable)

        # Invalidation: ribbon rolls back over while price makes new lows
        invalidate = (self.capitulation_flagged and hr30 < hr60
                      and price[-1] < min(price[:-1]))

        if invalidate:
            self.capitulation_flagged = False  # reset; wait for next cycle
            return "INVALIDATE"
        if accumulate:
            return "ACCUMULATE"      # begin / continue laddered scale-in
        if puell > self.PUELL_HIGH:
            return "TAKE_PROFIT"     # euphoria band — scale out
        return "HOLD"
```

The pseudocode emits a *state*, not a single buy order — execution is the laddered scale-in described in [[#Rules|Rules]]. Thresholds (`PUELL_LOW`, `PUELL_HIGH`, the 30/60 ribbon windows) are the canonical popular values; they are themselves a source of overfitting risk and should be stress-tested, not trusted.

## Indicators / Data Used

- **Network hashrate moving averages (30-day, 60-day).** The Hash Ribbons core. See [[on-chain-analysis]].
- **Puell Multiple.** Daily miner USD revenue ÷ its 365-day moving average — a measure of miner profitability relative to its own history.
- **Miner reserves.** On-chain BTC held in miner-tagged wallets; the draw-down/stabilization signal for forced reserve selling.
- **Mining difficulty.** Confirms the hashrate story — sustained difficulty drops corroborate genuine miner exit (vs short-term hashrate noise).
- **Daily OHLCV.** For the price-momentum confirmation and the multi-month hold/exit logic.

Data vendors that publish these series (forward-links — pages may not yet exist): [[glassnode]], [[cryptoquant]], [[coinmetrics]], and the original Hash Ribbons work by [[charles-edwards]] / Capriole.

## Example Trade

*Illustrative — describes the general historical pattern, not a precise fill.* In a typical late-bear capitulation, BTC has already fallen 70–80% from its prior cycle high and is trading near or below estimated aggregate production cost. Over a multi-week window, network hashrate rolls over (the 30-day MA dips below the 60-day MA — the Hash Ribbon "capitulation" flag), the Puell Multiple sits deep in its low band, and miner reserves drain as stressed operators sell to cover costs. Then the picture turns: the highest-cost miners have switched off, difficulty has adjusted downward, reserves flatten, and the 30-day hashrate MA recovers back above the 60-day. Around the same time price stops making new lows and reclaims its 30-day MA.

A position trader running this signal would **begin laddering into spot BTC** as the Hash Ribbon recovery and price confirmation align, accept that the exact low may have already passed (or may still be a tranche away), and **hold for months** into the subsequent expansion phase, scaling out only as the Puell Multiple climbs back into its euphoria band. This general "deep-bear miner capitulation → hashrate recovery → multi-month re-rating" shape has appeared around prior BTC cycle bottoms; the wiki deliberately does **not** assert exact dated prices here, because the precise entries/exits are sample-specific and easy to over-fit in hindsight.

## Performance Characteristics

Honest framing, because the numbers are weak:

- **Very small sample.** The signal has only a handful of clean historical instances. Any reported win rate is **low-n** and should not be read as a stable probability.
- **It is a zone, not a bottom.** The Hash Ribbon recovery typically lags the absolute price low or leads it by weeks — expect to accumulate *through* drawdown, not buy the exact tick.
- **Long holding period.** Capital is committed for months to a full cycle phase. This is a patience trade; mark-to-market drawdowns mid-accumulation can be large and uncomfortable.
- **ETF-era dampening.** Since 2024, persistent spot-ETF demand and the rise of well-capitalized public/industrial miners with balance-sheet buffers and hedging may **mute the classic forced-capitulation dynamic** — miners that historically would have dumped reserves can now borrow against them or sell forward. The historical mechanism may simply be weaker going forward. See [[institutional-flow-regime]].
- **No `expected_sharpe` is claimed.** Frontmatter leaves performance fields null on purpose — there is not enough independent data to estimate them credibly.

## Capacity Limits

Capacity is **high**. The trade is in spot BTC (the deepest, most liquid crypto market) and any low-leverage BTC perp/future, on a **multi-month** accumulation horizon. Laddering tens of millions of dollars into BTC spot over several weeks at a cycle low is well within normal market depth, especially when miner *and* panic selling is supplying the market. The `capacity_usd` of $100M reflects this; even larger allocators can express the signal, though very large size would ladder over longer windows to limit impact. Crowding risk is **low** — the metrics are public but the strategy demands a multi-month hold through drawdown that most participants will not sit through.

## What Kills This Strategy

In rough order of importance (see [[failure-modes]]):

- **Small sample / overfitting.** The dominant risk. Three or four cycles is not enough to validate the rule; the thresholds may be curve-fit, and the next cycle may not rhyme.
- **Structural change — ETFs and industrial miners.** Spot-ETF demand absorbing supply, and large public miners with balance-sheet buffers, hedging, and capital-markets access, can blunt the *forced* part of forced selling. If miners stop capitulating, the signal stops firing meaningfully. See [[institutional-flow-regime]].
- **No stop discipline — the bottom keeps going lower.** A late-bear can extend far below "obvious" capitulation. Without survivable sizing and an invalidation rule, a trader who deploys the whole allocation on the first Hash Ribbon flag and then averages down with no limit can be ruined before the real low. This is the single most common way the trade goes wrong in practice.
- **Non-price hashrate shocks (false signals).** Energy crackdowns, regional mining bans, ASIC supply shocks, or weather can capitulate hashrate **without** a corresponding price bottom (e.g., the 2021 China ban halved hashrate mid-cycle). The price-momentum confirmation filters some of this, but not all.
- **Regime change.** A genuine secular shift (Bitcoin demand structurally impaired, or a four-year-cycle that simply stops repeating) breaks the entire premise. See [[bitcoin-cycle-regime]].

## Kill Criteria

Retire or pause the signal (see [[when-to-retire-a-strategy]]) when **any** trigger fires:

- **Two consecutive cycles** in which the Hash Ribbon "recovery + confirmation" signal fails to precede a multi-month positive return (i.e., the next cycle invalidates the prior one) → the edge is presumed curve-fit; stop trading it as a standalone signal.
- **Invalidation during a live position:** the 30-day hashrate MA crosses back *below* the 60-day MA **and** price makes a new cycle low **and** miner reserves resume a sustained decline → treat as INVALIDATE; halt further accumulation and reassess (this is the hard stop the strategy otherwise lacks).
- **Drawdown from first tranche > 50%** with no Hash Ribbon recovery in sight → sizing was wrong; do not add. Survival of the book takes priority over the thesis.
- **Documented structural break:** if, over a cycle, public-miner + ETF balance-sheet behavior demonstrably absorbs what would historically have been capitulation supply (hashrate falls but reserves do *not* drain into the market), downgrade the signal to "context only" and stop sizing trades on it.

These are intentionally conservative because the underlying sample is too small to justify confidence.

## Advantages

- **Mechanistic and legible.** Unlike most "buy the bottom" heuristics, the edge has a concrete supply mechanism (forced miner selling) tied to observable on-chain data.
- **High capacity, low crowding.** Spot BTC, multi-month horizon — large size fits, and few participants will hold through the drawdown.
- **Low minimum capital.** Works from $1k; it is fundamentally a patient spot-accumulation trade.
- **Confluence reduces single-metric noise.** Requiring Hash Ribbon recovery *and* a low Puell *and* stabilizing reserves *and* price confirmation filters out many lone-metric false positives.
- **Asymmetric cycle payoff.** When it does catch a cycle low, the multi-month re-rating is large relative to the drawdown risked (given disciplined sizing).

## Disadvantages

- **Tiny sample — possibly not a real edge.** The defining weakness; everything else is downstream of this.
- **Zone, not a bottom.** Guaranteed to feel "wrong" mid-accumulation; demands holding through further drawdown.
- **Long, illiquid commitment.** Capital is locked for months; opportunity cost and psychological strain are high.
- **Structurally fragile post-2024.** The ETF/industrial-miner era may have already weakened the forced-capitulation mechanism the signal depends on.
- **No clean stop.** Because it is a long-horizon accumulation, there is no tight stop; risk control comes from sizing and the (slow) invalidation rule, not a tight price stop.
- **False signals from policy/energy shocks.** Hashrate can capitulate for non-price reasons.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the source that defines basket 7 (On-Chain Intelligence) and the "Miner Capitulation = late-bear bottoming signal" sub-state this page fills. The specific strategy construction (rules, pseudocode, kill criteria) is the wiki's own synthesis, framed against the regime taxonomy.
- The Hash Ribbons indicator originates with Charles Edwards / Capriole Investments; the Puell Multiple with David Puell. These are referenced here as well-known public on-chain constructs — no specific external URL or backtest is asserted, in keeping with the small-sample caveat above.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — CEX inflow/outflow (1h/6h/24h/7d, per-exchange breakdown)
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — stablecoin dry-powder z-score signal
- `GET /api/v1/on-chain/miners/reserves` — BTC miner pool reserves + flows
- `GET /api/v1/on-chain/miners/hash-ribbon` — Hash Ribbon state (capitulation/recovery/normal)
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + supply-shock zone classification
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100)

**Historical data:**
- `GET /api/v1/on-chain/whale-score/{symbol}` — whale accumulation score timeseries
- `GET /api/v1/market-intelligence/stablecoin-history` — stablecoin market-cap timeseries

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]].

## Related

- [[miner-capitulation]] — the underlying market phenomenon this signal trades
- [[on-chain-regime]] — parent regime basket (basket 7, On-Chain Intelligence)
- [[bitcoin-cycle-regime]] — the four-year cycle context this signal sits inside
- [[crypto-market-regime-taxonomy]] — the 14-basket framework
- [[bitcoin-halving]] — the protocol event that periodically halves miner revenue
- [[on-chain-analysis]] — the metric family (hashrate, Puell, reserves, difficulty)
- [[on-chain-analytics]] — the broader on-chain data discipline
- [[on-chain-flow-trading]] — the aggregate-flow directional cousin of this signal
- [[institutional-flow-regime]] — ETF / industrial-miner forces that may dampen the signal
- [[behavioral-finance]] — the panic-selling-climax side of the edge
- [[edge-taxonomy]] — structural + behavioral edge framing
- [[failure-modes]] — what breaks it
- [[when-to-retire-a-strategy]] — kill-criteria methodology
