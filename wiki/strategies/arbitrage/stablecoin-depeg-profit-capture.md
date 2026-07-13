---
title: "Stablecoin Depeg Profit Capture Playbook"
type: strategy
created: 2026-04-28
updated: 2026-06-20
status: excellent
tags: [arbitrage, crypto, defi, mean-reversion, leverage, risk-management]
aliases: ["Depeg Profit Tactics", "Stable Depeg Money-Making", "Maximizing Depeg P&L"]
related: ["[[stablecoin-pair-arbitrage]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[lst-depeg-arbitrage]]", "[[depeg-risk]]", "[[ai-amplified-exploit-arbitrage]]", "[[cross-chain-contagion-hedge]]", "[[curve-finance]]", "[[makerdao]]", "[[ethena]]", "[[aave]]", "[[funding-rate-arbitrage]]", "[[2023-03-usdc-svb-depeg]]", "[[2022-06-steth-depeg]]", "[[2022-05-terra-luna-depeg-arb]]", "[[2017-2020-tether-banking-premium]]", "[[2020-03-dai-black-thursday]]", "[[2023-02-busd-wind-down]]", "[[2026-04-kelp-stable-sympathy-depeg]]", "[[stablecoin-depeg-history]]"]
strategy_type: hybrid
timeframe: swing
markets: [crypto, defi]
complexity: advanced
backtest_status: paper-traded
edge_source: [structural, behavioral, analytical]
edge_mechanism: "Stablecoin depegs create temporary price dislocations from $1.00. Multiple distinct profit-capture methods extract value at different risk/reward profiles: spot mean-reversion buy, redemption-channel arb (near risk-free), pair-trade on cross-stable spreads, leveraged borrow-and-redeem, AMM-band capture, post-event short of overshoot, options skew capture. The trade is matching the right capture method to the depeg's specific mechanics, then sizing aggressively when the redemption channel is open."
data_required: [stable-prices-by-venue, redemption-channel-status, lending-protocol-borrow-rates, curve-pool-composition, psm-utilization, perp-funding-rates, options-iv-by-strike]
min_capital_usd: 50000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 2.0
expected_max_drawdown: 0.20
breakeven_cost_bps: 25
decay_evidence: "Strategy-class is durable — depegs have happened reliably 2-5x per year since 2018. Per-event Sharpe extremely high (3.0+) for the redemption-arb path; lower for the speculative paths. Edge persists because most participants use only one capture method (typically the simplest spot buy); sophisticated layering of methods produces 2-5x the per-event return."
---

# Stablecoin Depeg Profit Capture Playbook

A tactical companion to [[stablecoin-pair-arbitrage]] and [[synthetic-stablecoin-depeg-arbitrage]]. Those pages answer *"when does a depeg create a tradable opportunity?"* — this page answers ***"once it does, how do we extract the most profit?"***. Different question, different toolkit. Most participants in depeg events only execute the simplest capture method: spot-buy the cheap stable, wait for peg restoration, sell at par. **That captures roughly 20-40% of the available P&L on a typical event.** The remaining 60-80% sits in less-obvious methods: redemption arb, leveraged borrow-and-redeem, cross-venue dislocation, post-event short of overshoot, AMM-fee capture during the volatility window, and options skew. This page documents all of them.

## Edge source

Per [[edge-taxonomy]], this strategy combines three edge categories:

- **Structural** (primary) — access barriers segment the market. Issuer redemption at $1.00 face (Circle, Tether) requires institutional KYB accounts most participants don't have; on-chain PSMs are permissionless but per-block capacity-limited. Participants who pre-built redemption access capture a discount others physically cannot close.
- **Behavioral** — panic sellers dump a fully-backed stable at $0.88 because headlines (bank failure, regulatory action) trigger indiscriminate flight; the overshoot below fair recovery value is fear-driven, and the post-event premium on the "safe" stable is the mirror image.
- **Analytical** — correctly classifying the depeg mechanism (banking scare vs. death spiral vs. bridge compromise) under time pressure is genuine analysis; the 2022 UST collapse punished anyone who pattern-matched it to a recoverable depeg.

## Why this edge exists

The other side of the trade is, in sequence:

1. **Forced and panicked sellers** during the event — DeFi treasuries de-risking, funds with mandates forbidding depegged collateral, retail extrapolating $0.95 → $0.50. They sell *because* the price is falling, not despite it; they keep losing because the decision is driven by mandate or fear, not by the redemption math.
2. **Structurally excluded buyers** — most market participants cannot redeem at face with the issuer (KYB minimums, no pre-existing relationship), so the discount-to-par persists longer than fundamentals justify. The few desks with redemption access face limited competition.
3. **Single-method arbitrageurs** — even sophisticated buyers usually deploy only the spot mean-reversion buy. The leveraged, LP-fee, pair-trade, and overshoot legs are under-trafficked, so layered execution earns 2-5x the single-method return on the same event.

The edge recurs because depegs are episodic and stressful: maintaining redemption relationships, pre-funded venue accounts, and rehearsed playbooks through 350 idle days a year is an organizational cost most won't pay.

## Null hypothesis

Under a no-edge null, a stablecoin trading at $0.88 is fairly priced: the discount exactly reflects the probability-weighted shortfall in reserves (e.g., 12% chance of a 100% loss, or certainty of an 88-cent recovery). Buying depegged stables would then earn zero expected excess return — wins on USDC-2023-type events exactly offset by UST-2022-type wipeouts. The strategy's claim is that this null fails for *mechanism-verifiable* depegs: when reserves are observably intact and a $1.00 redemption channel is observably open, the discount is panic pricing, not fair pricing. The null is correct, however, for depegs where the mechanism cannot be verified — which is why mechanism classification gates every entry, and why [[2022-05-terra-luna-depeg-arb]] is a counter-example, not a missed trade.

## Depeg mechanism taxonomy (gate before any size)

The single most important decision is classifying *why* the [[stablecoins|stablecoin]] is below par. The mechanism determines whether the discount is panic (tradeable) or fair (a trap). This table is the master gate referenced throughout the playbook; it maps each scenario to its verifiable signals and the methods that apply.

| Scenario | Mechanism state | Verifiable signals | Tradeable? | Methods that apply | Canonical case |
|----------|-----------------|--------------------|-----------:|--------------------|----------------|
| **Banking scare** | Reserves observably intact; a banking partner failed but deposits likely backstopped | Issuer attestation; bank exposure disclosed and bounded; redemption channel still open | **Yes — aggressive** | 1, 2, 3, 4, 5, 6, 7 | [[2023-03-usdc-svb-depeg]] |
| **Contagion sympathy** | This stable's own mechanism is healthy; it drops because a *different* protocol blew up | No direct exposure to the exploited asset; [[oracle]] median unchanged; reserves unchanged | **Yes — moderate** | 1, 2, 3, 5, 6 | [[2026-04-kelp-stable-sympathy-depeg]] |
| **Redemption suspension / wind-down** | Issuer halts minting/redemption; slow drain, not recovery | Issuer announces pause; [[arbitrage|arb]] channel closed | **No** (hold only in-flight claims) | none new | [[2023-02-busd-wind-down]] |
| **Mechanism break** | Backing/hedge is depleting faster than it can recover (synthetic reserve burn, undercollateralization) | Reserve fund draining; collateral ratio falling; perp [[funding-rate]] inverted for days | **No** | none | (see [[synthetic-stablecoin-depeg-arbitrage]]) |
| **Death spiral** | Reflexive collapse, no floor (pure algorithmic) | Mint/burn feedback loop; backing token in freefall | **Never** | none | [[2022-05-terra-luna-depeg-arb]] |
| **Bridge compromise** | Wrapped stable orphaned from canonical until recap | Bridge exploited; canonical unaffected; recap probability uncertain | **Only on credible recap** | bounded long | [[2020-03-dai-black-thursday]] (oracle-stress analog) |

The asymmetry is brutal: a correctly-classified banking scare ([[2023-03-usdc-svb-depeg]]) returns 10-50% on equity in days; a misclassified death spiral ([[2022-05-terra-luna-depeg-arb]]) is a near-total loss. The gate is not optional. See [[synthetic-stablecoin-depeg-arbitrage]] for the synthetic-mechanism variants and [[stablecoin-pair-arbitrage]] for the fiat-backed variants.

## Method-selection matrix

Given a verified-tradeable depeg, which of the seven methods to deploy depends on three inputs: depeg depth, redemption-channel status, and mechanism confidence. This matrix maps the situation to the recommended method stack.

| Situation | Depeg depth | Redemption channel | Recommended stack | Notes |
|-----------|-------------|--------------------|--------------------|-------|
| Shallow sympathy depeg | 30-100 bp | n/a (not needed) | 1 + 5 | Cheap-to-carry; LP fee capture is the bonus |
| Deep banking scare, channel open | 100-1200 bp | open | 2 (anchor) + 1 + 3 + 4 | Redemption arb is the near-risk-free core |
| Deep depeg, channel gated (no KYB) | 100-1200 bp | closed to you | 1 + 3 + 5 + 7 | Retail/no-KYB path; lower Sharpe but still positive |
| Cross-stable dislocation | both stables off par | either | 3 (pair) + 6 (overshoot) | Capture discount AND premium |
| Anticipated stress (pre-position) | pre-event | n/a | 5 (Curve LP) | Seed before the event; collect fee surge |

## Rules

### Entry

1. **Trigger**: peg deviation > 30 bp on deep venues (Curve 3pool, major CEX spot).
2. **Mechanism gate** (mandatory before any size): classify the scenario — banking scare / mechanism break / contagion-sympathy / bridge compromise — per [[synthetic-stablecoin-depeg-arbitrage]] and [[stablecoin-pair-arbitrage]]. Only banking-scare and contagion-sympathy depegs with verifiably intact reserves qualify for aggressive sizing.
3. **Scale in across deviation tiers** — never full size at first deviation: 25% of position at -30 bp, 50% at -100 bp, final 25% reserved for capitulation lows (-300 bp+).
4. **Use limit orders, not market** — stress spreads are wide; market orders pay 50-200 bp extra.
5. **Activate the redemption-arb leg immediately** if the issuer channel is confirmed open — it is the near-risk-free anchor of the position.

### Exit

- Spot/pair/leveraged legs: exit at deviation < 10 bp from par, or at redemption clearing for the redemption leg.
- Close in reverse order of risk: options first (if profitable), leveraged legs, pair trade, then LP and spot last; capture the post-event overshoot short (Method 6) after resolution.
- **Time stop**: 30 days without resolution = close everything, don't wait.
- **Hard stop**: if the depeg deepens past entry by 2x AND the mechanism is impaired, close at any cost.

### Position sizing (hard rules)

1. **Max 25% of book in any single stablecoin** — diversify across USDC/USDT/DAI/FRAX even when only one is depegged
2. **Max 50% of book in stablecoin depeg trades total** — not all-in on a single thesis
3. **Max 5x leverage on any single position** — beyond that, liquidation risk dominates
4. **Reserve 25% of position size for capitulation lows** — never enter at full size at first deviation

```
target_size = (capital × 0.25)                # Max stable concentration
            × (1 - mechanism_risk_factor)     # 0=safe, 1=structural-break risk
            × scaling_in_factor               # 0.25 / 0.50 / 1.00 by deviation tier
            × (1 - cross_correlation_haircut) # If multiple stables depegging together
```

For USDC/SVB at $0.88 (deep depeg, mechanism solvable, second-tier scaling, low cross-correlation): $10M book × 0.25 × 0.95 × 0.50 × 0.95 = **~$1.13M base position size** — then layer methods 2-7 on top of that base.

## Implementation pseudocode

```python
# Monitoring loop (always on)
for stable in [USDC, USDT, DAI, FRAX, sUSDe, GHO, crvUSD]:
    px = min_price_across_venues(stable)      # Curve, CEX spot, PSMs
    if abs(1.0 - px) > 0.003:                 # 30 bp trigger
        scenario = classify_mechanism(stable)  # banking|mechanism|contagion|bridge
        if scenario in (BANKING_SCARE, CONTAGION) and reserves_verifiable(stable):
            run_playbook(stable, px, scenario)

def run_playbook(stable, px, scenario):
    base = book * 0.25 * (1 - mech_risk(scenario)) * tier(px) * (1 - corr_haircut())

    # Leg 1: redemption arb (anchor) — only if channel confirmed open
    if redemption_channel_open(stable):        # API / status page / PSM probe
        buy(stable, size=redemption_capacity(), order=LIMIT)
        initiate_redemption(stable)            # T+1 fiat or instant PSM

    # Leg 2: spot mean-reversion, scaled in
    buy(stable, size=base * tier_fraction(px), order=LIMIT)

    # Leg 3: pair trade if cross-stable spread > 100 bp and both mechanisms intact
    rich = richest_major_stable()
    if price(rich) - px > 0.010:
        short(rich, size=base)

    # Leg 4: leverage only if scenario == BANKING_SCARE and depth < -200 bp
    if px < 0.98 and scenario == BANKING_SCARE:
        loop_borrow(stable, max_leverage=3)    # Aave/PSM loop, never >5x

    # Exits
    while position_open():
        if deviation() < 0.001: unwind_all(reverse_risk_order=True)
        if days_open() > 30: unwind_all()                       # time stop
        if deviation() > 2 * entry_deviation() and mechanism_impaired():
            unwind_all(at_any_cost=True)                        # hard stop
    short_overshoot(rich)                       # Method 6, post-resolution
```

## Indicators / data used

Each capture method consumes a specific feed set. The table maps the data input to a source and to the method(s) it gates. Peg, [[funding-rate]], and [[open-interest]] feeds are available through aggregators such as cryptodataapi.com (multi-venue REST/WS); on-chain feeds (PSM/GSM capacity, Curve composition, lending rates) require RPC reads or subgraphs.

| Data input | Source | Feeds method(s) | Why it matters |
|------------|--------|-----------------|----------------|
| **Peg prices by venue** | Curve pool quotes; CEX spot (Coinbase, Binance, Kraken, Bitfinex); DeFiLlama peg monitors; cryptodataapi.com multi-venue spot | 1, 2, 3, 6 | The trigger (>30 bp deviation) and the cheapest-venue entry decision |
| **Redemption-channel status** | Circle/Tether status pages + APIs; MakerDAO PSM + Aave GSM on-chain capacity | 2, 4 | Gates the near-risk-free redemption anchor; if closed, drop Method 2 |
| **Curve pool composition** | Curve subgraph; Curve frontend | 5 (input) + 1 (severity gauge) | 3pool imbalance is both depeg severity and the LP rebalance-capture input |
| **Lending-protocol borrow rates** | Aave/Compound/Morpho dashboards; on-chain reads | 4 | USDT borrow spiked >30% APR during SVB weekend — directly sets leverage-leg viability |
| **Lending-protocol oracle setup** | Per-protocol oracle config (Chainlink feed vs hardcoded $1.00) | 4 (risk gate) | A market-tracking [[oracle]] marks depegged collateral down, cutting borrow power |
| **Perp [[funding-rate]]s** | Exchange WS; [[coinglass]]; cryptodataapi.com | 6, 7 | Short-leg carry; sUSDe mechanism context (see [[synthetic-stablecoin-depeg-arbitrage]]) |
| **[[open-interest]]** | Exchange APIs; [[coinglass]]; cryptodataapi.com | 6, 7 | Confirms the overshoot/short is supported by real flow, not a print artifact |
| **Options IV by strike** | Deribit (BTC/ETH proxy); DeFi options venues (thin) | 7 | Where stablecoin-adjacent optionality exists; mostly proxy/OTC (see Method 7) |
| **News / regulatory feed** | Banking headlines; issuer attestations; regulatory actions | mechanism gate | Drives the depeg-mechanism classification above |

## Example trade

**The layered USDC/SVB playbook (March 2023).** USDC fell to ~$0.88 on Saturday 11 March 2023 after Circle disclosed $3.3B of reserves at Silicon Valley Bank; the peg restored by Monday 13 March after the FDIC backstop. A sample full-suite deployment:

| Method | Allocation | Expected return | Contribution |
|--------|-----------|-----------------|--------------|
| Spot buy (Method 1) | $5M @ $0.90 | +12% | +$600K |
| Redemption arb (Method 2) | $20M via Circle | +10% | +$2,000K |
| Pair trade (Method 3) | $5M long/short | +25% on $1M margin | +$250K |
| Leveraged borrow (Method 4) | 3x leverage on $5M = $15M position | +30% on $5M equity | +$1,500K |
| 3pool LP (Method 5) | $20M LP | +5% | +$1,000K |
| Post-event short (Method 6) | $10M USDT short | +0.7% | +$70K |
| Options (Method 7) | $1M premium | +200% | +$2,000K (if right) |

**Total deployed**: ~$56M (with some overlap on collateral). **Total P&L**: ~$7.42M (if all methods work). **Blended return on capital**: ~13.3% over 52 hours.

The blended return is similar to spot-buy alone, but **capital efficiency is dramatically higher**: methods 2-4 turn over capital faster (redemption clears in T+1; pair trade releases margin), and methods 5-7 don't require full notional commitment. **Effective capital deployed at any given moment** might be only $30M, producing **~25% effective return on actively-deployed capital** in 52 hours. For a sophisticated desk with full method-suite access, USDC/SVB returned 20-50% on equity, not the ~13% from the spot leg alone. (Single-leg worked examples appear under each method below.)

## Performance characteristics

All figures net of realistic costs (limit-order fills, 1-4 bp AMM fees, gas, borrow interest, redemption wire costs) — round-trip costs on the core legs run well under the 25 bp `breakeven_cost_bps`; only the post-event overshoot leg (10-30 bp capture) is cost-marginal.

| Strategy | Per-event Sharpe | Frequency | Capacity | Setup complexity |
|----------|------------------|-----------|----------|------------------|
| **Stablecoin depeg (combined methods)** | **3.0+ per event** | 2-5x/year | $200M | Moderate |
| Funding-rate arbitrage | 0.5-1.5 | Continuous | $500M+ | Low |
| Cash-and-carry basis | 0.8-1.5 | Continuous | $1B+ | Low |
| Cross-exchange arb | 1.0-2.0 | Continuous | $50-200M | High (latency) |
| Merger arbitrage | 1.0-2.0 | 5-10x/year | $200M+ | High (legal) |
| Bankruptcy claim arb | 1.5-2.0 | 1-3x/year | $500M | High (relationships) |

**Stablecoin depeg has the highest per-event Sharpe** because the clear $1.00 target eliminates directional risk, multiple capture methods provide redundant exit paths, redemption-channel arb is near risk-free when the channel is open, and layered execution amplifies returns 2-5x vs a single-method play.

The catch: **opportunities are intermittent**. A typical year has 2-3 major events; capital is idle the other ~350 days unless deployed in adjacent strategies ([[funding-rate-arbitrage]], [[cash-and-carry]]). The frontmatter `expected_sharpe: 2.0` is the *annualized blended* figure after idle-capital drag and the occasional small loss on speculative legs; per-event Sharpe on the redemption-anchored stack is 3.0+. `expected_max_drawdown: 0.20` reflects a mechanism-misclassification loss on a maximum-size (25% of book) position cut at the hard stop, not the benign base case.

## Capacity limits

Strategy-level capacity is approximately **$200M per event** before impact dominates, decomposed by method: spot buys $5-50M (venue depth — Curve held >$50M of depth at $0.88-0.92 during SVB weekend); redemption arb $5-100M (issuer redemption caps and T+1 settlement throughput — Circle/Tether capacity is very deep, 8-9 figures); pair trade $10-50M (short-side borrow availability); leveraged loops $5-30M (lending-pool depth and borrow-rate spikes); Curve LP $50-200M (highest capacity — 3pool TVL $500M+, a $50-100M LP position is feasible without significantly diluting per-LP returns); overshoot short $5-20M; options $1-10M (thin markets). Beyond ~$200M, the buyer becomes the market: bids restore the peg themselves and compress the capture. Annualized capacity is event-frequency-bound (2-5 events/year), not size-bound.

## What kills this strategy

Tail risks that have wiped out depeg trades:

1. **Death spiral mechanisms** (UST May 2022 — went $1 → effectively $0; long-only positions zeroed)
2. **Redemption channel suspension** (BUSD Feb 2023 — Paxos halted new minting and wound down; slow drain rather than recovery)
3. **Lending-protocol oracle behavior** — during the March 2023 depeg, Chainlink's USDC/USD feed used by [[aave]] tracked the depegged market price, while Compound v2 had hardcoded USDC at $1.00 and had to disable USDC supply. A market-tracking oracle marks depegged collateral down, cutting borrowing power and threatening liquidation cascades on leveraged legs — verify each protocol's oracle setup before looping.
4. **Smart contract exploit during stress** (Curve July 2023 — Vyper reentrancy hit several pools during depeg-adjacent stress)
5. **Regulatory action mid-trade** (BUSD wind-down; potential future actions against an issuer)
6. **Banking partner permanent failure** (if SVB depositors had not been backstopped, USDC's recovery to par was not guaranteed)

Risk-management musts: never long a stable whose mechanism is breaking; never max-leverage on speculative depegs; diversify across mechanisms (if all depeg exposure is fiat-backed, regulatory action correlates them); time stops are essential.

## Kill criteria

Per-trade:

- Deviation deepens to **2x entry deviation with mechanism impaired** → close at any cost
- **30 days** without peg resolution → close all legs
- Leveraged-leg health factor < **1.15** → deleverage immediately regardless of view
- Issuer announces redemption suspension or wind-down → exit spot/leveraged legs same day, keep only redemption claims already in flight

Strategy-level retirement:

- Two consecutive events with realized loss > **10% of deployed capital** each → mechanism-classification process is broken; halt until rebuilt
- Redemption-access advantage gone (e.g., instant permissionless redemption becomes universal) **and** average event depth < 50 bp for 2 years → structural edge decayed; retire
- Cumulative strategy drawdown > **20%** of allocated book → stop, full post-mortem before re-allocation

## Advantages

- Clear $1.00 anchor removes open-ended directional risk present in most mean-reversion trades
- Redemption-arb leg is near risk-free when the channel is verified open — a rare genuine structural edge
- Seven semi-independent capture methods give redundancy: if one leg is inaccessible (no KYB, thin options), others still work
- High per-event returns (10-50% on equity in 2-3 days for major events) with definable, gateable tail risk
- Durable: depegs have recurred 2-5x/year since 2018 across fiat-backed, crypto-backed, and synthetic designs

## Disadvantages

- Episodic — capital and infrastructure sit idle ~95% of the time; demands a complementary baseline strategy
- The best leg (issuer redemption) is gated behind institutional KYB and pre-built relationships; retail accesses only the lower-Sharpe legs
- Tail risk is binary and severe: misclassifying a death spiral as a banking scare converts a 12% expected gain into a near-total loss
- Operationally intense at the worst times — weekend events, congested chains, spiking gas, halted venues
- Leverage legs depend on protocol oracle and parameter behavior that differs by venue and can change between events

---

## The Seven Profit-Capture Methods

| # | Method | Risk profile | Typical return per event | Capacity |
|---|--------|--------------|--------------------------|----------|
| 1 | **Spot mean-reversion buy** | Low (if mechanism solvable) | 2-15% (depends on depth of depeg) | $5-50M |
| 2 | **Redemption-channel arb** | Near-zero risk if channel functional | 2-15% (matches depeg depth, but near risk-free) | $5-100M (subject to issuer redemption caps) |
| 3 | **Cross-stable pair trade** | Low-moderate (cross-margin risk) | 3-20% (captures both stables' deviation) | $10-50M |
| 4 | **Leveraged borrow-and-redeem** | Moderate (borrow rate + liquidation) | 5-50% on equity (3-10x leverage typical) | $5-30M |
| 5 | **AMM band capture (Curve LP)** | Low (impermanent loss bounded) | 0.5-3% per event from fee capture | $50-200M (highest capacity) |
| 6 | **Post-event short of overshoot** | Moderate (timing risk) | 1-5% on the rich-stable leg | $5-20M |
| 7 | **Options skew capture** | High (theta decay) | Variable, can be very high in tails | $1-10M |

**Combined deployment**: layering 3-5 of these methods on a single event can produce 15-50% blended return on capital deployed for an event like USDC/SVB (March 2023), vs. the textbook ~13.5% from spot-buy alone. The methods complement each other.

### Method 1: Spot Mean-Reversion Buy

**The default play.** Buy the cheap stable on a venue where it trades, hold to peg restoration, sell.

#### Best venues by stable

| Stable | Best venue for entry | Notes |
|--------|---------------------|-------|
| **USDC** | Curve 3pool (cheapest during stress); Coinbase (institutional access) | During SVB weekend, Curve had >$50M depth at $0.88-0.92 |
| **USDT** | Bitfinex historically (banking issues 2018-2020); Binance (deepest spot) | Tether premium has flipped both directions historically |
| **DAI** | Curve 3pool; MakerDAO PSM (bidirectional) | PSM is the official redemption-equivalent |
| **FRAX** | Curve FRAXBP / 3pool; FRAX governance redemption | FRAX historically follows USDC due to USDC backing |
| **sUSDe** | Curve sUSDe/USDC pool | Watch funding rate context |
| **GHO** | Balancer GHO/USDC; Aave GSM (GHO Stability Module) | GSM bidirectional but capacity-limited |
| **crvUSD** | Curve native pools | LLAMMA mechanism complications during stress |

#### Tactical rules

1. **Scale in across deviation tiers** — never go full size at first deviation: 25% at -30 bp, 50% at -100 bp, final 25% reserved for capitulation lows (-300 bp+)
2. **Use limit orders, not market** — stress periods have wide spreads; market orders pay 50-200 bp extra
3. **Verify mechanism** before entry per [[synthetic-stablecoin-depeg-arbitrage]] (don't catch falling knives in death spirals)
4. **Don't add below kill-criteria** — if redemption channel is impaired, adding to a losing position doubles the structural risk

#### P&L worked example: USDC March 2023

- T0 (Sat Mar 11, 12:00 UTC): USDC at ~$0.88 on Curve, 3pool composition heavily skewed toward USDC
- Buy 1,000,000 USDC at $0.88 (good limit fill at the bid); capital outlay: $880,000
- T+52h (Mon Mar 13, 16:00): USDC at $0.999; sell at $0.999
- P&L: $1,000,000 × ($0.999 - $0.88) = $119,000 = **13.5% in 52h**

This is the textbook capture. Methods 2-7 layer additional return on top of this base.

### Method 2: Redemption-Channel Arb (near risk-free if channel open)

**The hidden gem.** When a stable depegs but the issuer's redemption channel is functional, you can buy the discount stable on-market and redeem it via the official channel at $1.00. This is mechanically near risk-free in the period between purchase and redemption clearing (residual risks: issuer suspends redemption mid-flight, or banking rails fail).

#### Channels by stable

| Stable | Channel | Speed | Min size | KYC requirement |
|--------|---------|-------|----------|----------------|
| **USDC** | Circle direct redemption | T+1 (next business day) | $100K | Yes (KYB for institutions) |
| **USDT** | Tether direct redemption | T+0 to T+3 | $100K | Yes; Tether banking partner restrictions apply |
| **DAI** | MakerDAO PSM (instant) | Instant on-chain | None | None (permissionless) |
| **GHO** | Aave GSM (instant) | Instant on-chain | None | None |
| **FRAX** | FRAX governance / AMO | Variable | Varies | Permissionless on AMM; gated for direct redemption |
| **BUSD** | Paxos direct | T+1 (when active) | $100K | Yes |
| **sUSDe** | Ethena direct mint/redeem | Instant on-chain (unstaking cooldown applies, ~7 days) | None | None |

#### Tactical pattern

1. **Verify channel is actually open** — call the issuer's API or check status page. Issuers occasionally pause redemptions during stress (Tether 2017, BUSD wind-down 2023).
2. **Buy on cheapest venue** — Curve typically wins during DeFi stress; Coinbase wins for institutional access.
3. **Initiate redemption immediately** — don't wait for further depeg; the time-decay risk exceeds the marginal capture.
4. **Hold cash until redemption clears** — typically T+1 to T+3 for fiat-backed; instant for on-chain PSM.
5. **Repeat until depeg closes** — Circle / Tether redemption capacity is very deep; you can typically size into 8-9 figures.

#### P&L worked example: USDC March 2023 (redemption arb path)

- T0 (Sat Mar 11): USDC at $0.88; Circle confirms redemption status: open via Coinbase Custody (T+1).
- Buy 5,000,000 USDC at $0.89 ($4,450,000 capital).
- T0 + 1 hour: initiate redemption to Circle.
- T+~50 hours (Mon Mar 13 morning): redemption clears at $1.00 face.
- P&L: 5,000,000 × ($1.00 - $0.89) = **$550,000 in ~50 hours = 12.4%**.
- **Crucially, this trade had ~zero market risk** — once the redemption was initiated, the only failure mode was Circle suspending redemptions retroactively (which they didn't).

#### Why this is undertraded

- Most retail can't access Circle / Tether direct redemption (institutional minimum + KYB requirements).
- Many funds don't have pre-existing relationships with stablecoin issuers.
- The on-chain PSM equivalent (MakerDAO PSM, Aave GSM) is permissionless but capacity-limited per block.
- Result: the discount-to-par persists longer than fundamentals would suggest, leaving alpha for the few participants with redemption access.

#### How to set this up in advance

1. **Open accounts at Circle, Coinbase Prime, Kraken Institutional** with KYB completed before any depeg event.
2. **Pre-fund relationships with USDT redemption agents** (Cumberland, Wintermute, OTC desks).
3. **Pre-test on-chain PSM transactions** with small amounts so you know the mechanics under stress.

### Method 3: Cross-Stable Pair Trade

**Captures both legs of the dislocation.** When USDC trades at $0.88 and USDT trades at $1.02+, you can long USDC + short USDT and capture *both* the discount on USDC and the premium on USDT.

#### Mechanics

- Long discount stable on Curve / spot CEX
- Short rich stable via: margin short on Coinbase / Kraken (where supported); Curve swap (sell rich stable for cheap stable); Aave borrow rich stable + sell (use long stable as collateral)

#### P&L worked example: USDC/USDT March 2023

- T0 (Sat Mar 11, 12:00): USDC at ~$0.88, USDT trading at a premium (~$1.02) on cross-stable pairs
- Long 1,000,000 USDC at $0.88 = $880,000 cost
- Short 1,000,000 USDT at $1.02 = $1,020,000 proceeds (held as collateral)
- Net capital required: ~$200K margin (assuming 1:1 cross-margin)
- T+52h: USDC at $0.999, USDT at $1.001
- P&L: Long USDC +$119,000 (0.88 → 0.999); Short USDT +$19,000 (1.02 → 1.001); **Total: $138,000 on $200K margin = 69% return in 52h**

The pair trade captures **~5x the return on capital** vs. spot-buy alone (~13.5%) because you're not tying up full notional on the long side.

#### Margin / cross-stable risks

- If both stables move adversely (rare but possible — e.g., systemic stable scare), margin call risk
- Funding rate on the short (varies by venue; often positive during stress)
- Liquidity risk if exchange halts trading (USDT was halted on some venues during stress)
- Counterparty risk on the venue providing the short

#### When to size up

- Cross-stable spread > 100 bp
- Both stables have functional redemption channels
- No systemic stable concern (entire stablecoin sector questioned)

### Method 4: Leveraged Borrow-and-Redeem

**The capital-efficiency play.** Borrow against your existing stables to size up the trade by 3-10x.

#### Pattern A: Aave borrow-against-cheap-stable

1. Buy $10M USDC at $0.88 = $8.8M capital outlay.
2. Deposit $10M USDC as collateral on Aave at 80% LTV (your basis is $8.8M).
3. Borrow $8M USDT (or USDC if you want even more discount stable) at par.
4. Use $8M USDT to buy more discount USDC: $8M / $0.88 = $9.09M USDC.
5. Repeat: deposit $9.09M USDC, borrow ~$7.27M USDT, buy ~$8.26M USDC.
6. Convergence: ~5x leverage achievable in theory before borrow rates and slippage compound — **but note**: if the protocol's oracle marks USDC at the depegged market price (as Aave's Chainlink feed did in March 2023), borrowing power against the depegged collateral is cut proportionally, reducing achievable leverage and raising liquidation risk. Verify oracle behavior first.

#### Pattern B: Maker / PSM-amplified

1. Buy $10M USDC at $0.90 = $9M outlay.
2. Swap USDC → DAI via MakerDAO PSM at 1:1 (instant, no slippage, subject to remaining PSM capacity).
3. Borrow more USDC against DAI on Aave, or use DAI in reverse at the PSM.
4. Buy more discount USDC.
5. When peg restores, unwind in reverse.

#### P&L worked example: 3x leveraged USDC March 2023

- Initial buy: $1M USDC at $0.88 ($880K outlay).
- Leverage to 3x via Aave: $3M USDC position with $880K equity.
- Borrowing cost: ~5% APR × 2 days ≈ 0.027% = $810 cost (in practice USDT borrow rates spiked above 30% APR that weekend, which would raise this to ~$5K — still small relative to the capture).
- T+52h: USDC at $0.999; unwind.
- P&L: $3M × ($0.999 - $0.88) = $357K gross, less borrow cost → **~$352-356K on $880K equity = ~40% return in 52h**

vs. unleveraged spot-buy at 13.5%, leverage produces ~3x the return.

#### Risks

- **Liquidation if depeg deepens** — Aave will liquidate at -20-40% adverse move depending on collateral parameters
- **Borrow rate spikes** during stress (USDT borrow on Aave exceeded 30% APR during SVB weekend; eats into return)
- **Oracle risk** on the lending protocol — see correction in ## Contradictions: Aave's Chainlink USDC/USD feed tracked the depegged market price in March 2023 (it did *not* hold $1.00), while Compound v2's hardcoded $1.00 price forced it to pause USDC supply. Oracle behavior differs by protocol and can change between events.
- **Smart contract risk** on the lending protocol

#### When NOT to use

- Death spirals (UST 2022) — leverage amplifies the loss
- Mechanism breaks (e.g., a synthetic's reserve/hedge depleting) — same
- Bridge-wrapped stables on compromised bridges — recap probability is too uncertain

### Method 5: AMM Band Capture (Curve LP)

**The slow-but-steady play.** During stress, Curve 3pool composition becomes severely imbalanced (e.g., 80% USDC / 10% USDT / 10% DAI when USDC is depegged). This generates massive trading fees.

#### Mechanics

1. Pre-position as 3pool LP holder *before* major depeg events (or seed during the early stages).
2. During the depeg, traders pay 1-4 bps per swap × 1000s of swaps × deep liquidity = significant fees accrue.
3. As composition rebalances, your LP position naturally swaps from rich stable into cheap stable.
4. Exit LP after peg restores; collect aggregated fees.

#### P&L mechanics (USDC March 2023, estimates)

- Curve 3pool TVL during stress: ~$500M.
- Total trading volume across 48h: ~$2-4B (estimate).
- Fee tier: 1 bp on stable swaps → total fees generated: $200K-$400K accrued to LPs.
- LP share of $1M (0.2% of pool): $400-$800 in fees over 48 hours.
- **Plus** the rebalancing effect: your $1M LP position ends up holding more discount stable than rich stable, naturally capturing ~3-8% of price reversion.
- **Total: ~3-8% over the event** (fee yield ~0.04-0.08% plus rebalance capture), and the LP position recovers as the peg restores.

#### Why this is high-capacity

The 3pool TVL is $500M+. A $50-100M LP position is feasible without significantly diluting per-LP returns.

#### Risks

- **Impermanent loss on systemic break** — if USDC had truly failed, 3pool LPs would absorb the loss as the pool drained into the failed asset
- **Smart contract risk** on Curve (the July 2023 Vyper reentrancy is the cautionary example)
- **Front-running risk** during entry

#### When to use

- Anticipated stress event (banking news, regulatory FUD) — pre-position
- During slow-moving depegs where you want passive exposure
- As complement to active strategies (Methods 1-4)

### Method 6: Post-Event Short of Overshoot

**The contrarian post-resolution play.** After a depeg resolves, the formerly rich stable typically bleeds its panic premium and can briefly undershoot parity as panic-buyers unwind. Capture the overshoot.

#### Mechanics

- During depeg: USDC at $0.88, USDT rich at $1.02+
- After resolution: USDC recovers to ~$1.00; USDT typically falls back toward $0.998-1.000 as the flight-to-USDT unwinds
- The capture is small but reliable (10-30 bp typical) and short-duration (4-12 hours)

#### P&L worked example: USDT post-USDC-SVB

- T0+50h: USDT at $1.005 (close to par, panic resolved)
- Short 5,000,000 USDT at $1.005
- T+60h: USDT at $0.998 (brief undershoot as panic-USDT-longs unwind); cover at $0.998
- P&L: 5,000,000 × ($1.005 - $0.998) = **$35,000 in 10 hours**

Modest absolute return, but high Sharpe (low risk, short duration). Note this leg is the most cost-sensitive: at 10-30 bp capture, it only clears costs on cheap venues.

#### Risks

- Overshoot doesn't materialize — small loss on the short
- Funding rate on perp short
- Hard to size up without affecting price

### Method 7: Options Skew Capture

**The convex play.** Direct options on stablecoins are scarce — no major venue listed standardized USDC options in 2023 (see ## Contradictions) — so this method mostly works through proxies and OTC structures.

#### Mechanics

- During a depeg, implied volatility on crypto options spikes broadly; any stablecoin-linked optionality (DeFi options venues, OTC variance structures) reprices dramatically
- Sell expensive optionality to monetize the IV crush as the peg restores, OR buy convex downside on the rich stable speculating on overshoot

#### Implementation

- Most accessible: Deribit BTC/ETH options as a proxy for stable-stress events (ETH options are relevant context for sUSDe, whose backing is an ETH-derivative hedge)
- Direct stablecoin options: limited venues (some DeFi option protocols), thin liquidity
- Variance-swap structures: OTC; only large desks

#### P&L characteristics

- High variance — single events can return 100%+ on premium
- Low capacity — options markets touching stables are thin
- Requires options-pricing expertise (Greeks, IV surface)

#### When to use

- You have an options trading background
- IV is genuinely elevated (verify, don't assume)
- Position size is small (<5% of book)

---

## Capital Amplification Stack (Detailed)

For sizing up beyond your base capital:

### Pre-event preparation

1. **Open accounts at all major venues**: Coinbase Prime, Kraken Institutional, Binance, OKX, Bybit, Bitfinex (USDT-specific), Hyperliquid, AsterDEX
2. **Pre-fund cross-margin accounts**: keep ~10% of capital ready as margin on each venue
3. **Establish redemption-agent relationships**: Circle (direct or via Coinbase Custody), Tether (Cumberland/Wintermute as redemption proxies), MakerDAO PSM (permissionless), Aave GSM (permissionless)
4. **Pre-deposit collateral on lending protocols**: Aave, Compound, Morpho, Spark — keep modest balances even when not trading, ready to size up
5. **Maintain USD bank wires ready**: for fiat redemption, your bank wire should be tested in advance

### During-event amplification

| Method | Amplification factor |
|--------|---------------------|
| Direct spot buy | 1x (base) |
| Cross-margin pair trade | 5-10x (capital-efficient) |
| Aave borrow-and-redeem | 3-5x (with margin buffer; less if oracle marks collateral down) |
| MakerDAO PSM cycle | 2-3x (atomic on-chain) |
| Curve LP fee capture | 0.5-1x (passive complement) |
| Options leverage | Variable (10-50x on premium) |

**Realistic combined amplification**: 8-15x your base capital effectively deployed, with the redemption-arb leg providing the near-risk-free anchor.

## Historical depeg reference (calibration set)

The recurrence of depegs is the durability case for this strategy. The table is the calibration set for mechanism classification — each row is a worked example of the taxonomy above. Full write-ups live in [[stablecoin-depeg-history]] and the per-event pages.

| Event | Stable | Low | Mechanism | Outcome | Playbook lesson |
|-------|--------|-----|-----------|---------|-----------------|
| [[2017-2020-tether-banking-premium]] | USDT | premium/discount both ways | Banking-partner uncertainty | Recovered | Premium *and* discount are tradeable; pair-trade (Method 3) |
| [[2020-03-dai-black-thursday]] | DAI | ~$1.10 (above par) | [[oracle]] stress + liquidation cascade | Recovered after MKR auctions | Oracle behavior under stress is the real risk to Method 4 |
| [[2022-05-terra-luna-depeg-arb]] | UST | →$0 | Death spiral (algorithmic) | Total loss | The counter-example: never long a structural break |
| [[2022-06-steth-depeg]] | stETH | ~$0.93 | Liquidity discount (redemption queued) | Recovered post-Merge | LST depeg ≠ stablecoin depeg; see [[lst-depeg-arbitrage]] |
| [[2023-02-busd-wind-down]] | BUSD | mild | Redemption suspension / wind-down | Slow drain | Hold only in-flight claims; don't add |
| [[2023-03-usdc-svb-depeg]] | USDC | ~$0.88 | Banking scare (reserves intact) | Restored in 52h | The canonical full-suite capture |
| [[2026-04-kelp-stable-sympathy-depeg]] | GHO/crvUSD | 30-100 bp | Contagion sympathy | Recovered 24-72h | Sympathy ≠ direct exposure; cheap-to-carry basket |

Depegs have recurred 2-5x per year since 2018 across fiat-backed, crypto-collateralized, synthetic, and bridge-wrapped designs. The mechanism changes; the panic-pricing pattern does not.

## Pragmatic Workflow

**Quiet markets (95% of the time)**:
- Maintain redemption-agent relationships, pre-funded venue accounts, baseline lending-protocol deposits
- Run [[funding-rate-arbitrage]] or [[cash-and-carry]] on idle capital
- Monitor stablecoin peg dashboards (DeFiLlama, Curve frontend, custom Discord bot per [[exploit-arb-implementation-guide]])

**Stress detected (peg deviation > 30 bp)**:
- Verify mechanism (per [[synthetic-stablecoin-depeg-arbitrage]] for synthetics, [[stablecoin-pair-arbitrage]] for fiat-backed)
- Classify scenario (banking, mechanism, contagion, bridge)
- Activate appropriate method-suite from this page; deploy capital in scaled-in tiers
- Initiate redemption arb for the near-risk-free leg ASAP
- Layer pair trade + leveraged borrow + LP + options as available

**Resolution phase**:
- Close in reverse order of risk (options first if profitable; redemption-arb settles automatically; LP and spot last)
- Capture post-event overshoot on the formerly-rich stable (Method 6)
- Document P&L attribution by method for next-event calibration

## Contradictions

> **Claim A** (earlier draft of this page, confidence: LOW): "Aave uses Chainlink which kept USDC at fair $1.00 during the depeg, allowing positions to remain solvent."
> **Claim B** (Galaxy Research coverage of the March 2023 depeg, verified via Perplexity sonar 2026-06-10, confidence: HIGH): Chainlink's USDC/USD feed used by Aave **tracked the depegged market price**; it was **Compound v2** that hardcoded USDC at $1.00 and consequently paused USDC supply transactions.
> **Resolution**: Claim B supersedes. The page body has been corrected; the practical implication for Method 4 is *reduced* achievable leverage and *higher* liquidation risk than the original draft implied.

> **Claim** (earlier draft, confidence: LOW): "Deribit USDC IV during SVB weekend reportedly hit 200%+."
> **Resolution**: Could not be verified — no evidence found that Deribit listed direct USDC options in 2023. The claim has been removed from Method 7, which now treats direct stablecoin options as scarce and proxy/OTC-based.

## Sources

- [[stablecoin-pair-arbitrage]] — fiat-backed stable companion strategy
- [[synthetic-stablecoin-depeg-arbitrage]] — mechanism-aware companion strategy
- [[2023-03-usdc-svb-depeg]] — primary case study source
- [[2022-06-steth-depeg]] — adjacent LST depeg case
- [[2022-05-terra-luna-depeg-arb]] — counter-example (death spiral, NOT an arb)
- Circle public documentation on USDC redemption mechanics
- MakerDAO PSM documentation
- Aave GHO Stability Module (GSM) documentation
- Curve Finance 3pool composition history
- Galaxy Research, "USDC's Fall Below $1 Sends Ripples Across DeFi" (oracle behavior, Compound v2 hardcoded price, ~$0.88 low)
- Verified via Perplexity (sonar), 2026-06-10: Chainlink USDC/USD feed tracked the depeg (did not pin at $1.00); Compound v2 hardcoded $1.00; USDC low ~$0.88 over the Mar 11-13 weekend; no evidence of direct Deribit USDC options in 2023. Citation: https://www.galaxy.com/insights/research/usdcs-fall-below-usd1-sends-ripples-across-defi

## Related

[[stablecoin-pair-arbitrage]] · [[synthetic-stablecoin-depeg-arbitrage]] · [[lst-depeg-arbitrage]] · [[depeg-risk]] · [[ai-amplified-exploit-arbitrage]] · [[cross-chain-contagion-hedge]] · [[curve-finance]] · [[makerdao]] · [[ethena]] · [[aave]] · [[funding-rate-arbitrage]] · [[2023-03-usdc-svb-depeg]] · [[2022-06-steth-depeg]] · [[2022-05-terra-luna-depeg-arb]] · [[exploit-arb-implementation-guide]] · [[multi-venue-capital-management]] · [[bankruptcy-claim-arbitrage]] · [[edge-taxonomy]]
