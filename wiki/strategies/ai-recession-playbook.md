---
title: "AI Recession Playbook"
type: strategy
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [stocks, options, bonds, commodities, risk-management, ai-trading, volatility, derivatives, event-driven]
aliases: ["AI Job-Loss Recession Playbook", "AI Displacement Master Trade", "AI Labor Recession Trade Matrix"]
strategy_type: hybrid
timeframe: position
markets: [stocks, options, bonds, commodities]
complexity: advanced
backtest_status: untested
edge_source: [structural, behavioral, informational]
edge_mechanism: "Markets are pricing AI capex (Mag 7 + power infrastructure) as fully reflexive bullish, while pricing AI's labor-side costs — 11M displaced jobs (Goldman), 3-5x service-sector multiplier, 3-7% tech-hub fiscal contraction, and the [[ai-layoff-trap]] feedback loop — as either negligible or distant. The playbook combines several smaller edges (energy long, white-collar SaaS short, tech-hub muni short, VIX tail) that each express the same underlying mispricing of capital-vs-labor asymmetry."
data_required: [equity-prices, sector-etf-prices, hyperscaler-capex-guidance, vix-term-structure, muni-cds-pricing, bls-employment-revisions, regional-sales-tax-receipts, ibkr-forecast-trader-recession-probability, treasury-yields, hy-vs-ig-spreads, dxy]
min_capital_usd: 250000
capacity_usd: 2000000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.25
breakeven_cost_bps: 50
decay_evidence: "Edge concentrated in 2026-2028 window. Decays if (a) Pigouvian automation tax is enacted, (b) the productivity J-curve resolves and ex-Mag-7 margins reflate from 9%, or (c) AI capex disclosure shifts from infrastructure spend to revenue inflection — see [[ai-capex-vs-cash-flow-divergence]]."
related: ["[[ai-sector-rotation-energy-hedge]]", "[[white-collar-ai-displacement-short]]", "[[tech-hub-muni-bond-short]]", "[[crypto-ai-recession-shorts]]", "[[ai-layoff-trap]]", "[[citrini-2028-global-intelligence-crisis]]", "[[service-sector-multiplier]]", "[[capital-vs-labor-asymmetry]]", "[[skill-bifurcation]]", "[[wage-compression-vs-job-loss]]", "[[ai-driven-demand-destruction]]", "[[tech-hub-concentration-risk]]", "[[margin-expansion-disparity]]", "[[solow-paradox-2026]]", "[[skilled-trades-wage-boom]]", "[[ai-data-center-power-demand]]", "[[pigouvian-automation-tax]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[regime-matrix]]", "[[live-journal]]", "[[research-checklist]]", "[[hypothesis-to-backtest-workflow]]", "[[itpm-trade-construction-playbook]]", "[[crisis-alpha]]", "[[tail-risk]]", "[[barbell-strategy]]", "[[asymmetric-barbell]]", "[[hedging-strategies]]", "[[position-sizing]]", "[[risk-of-ruin]]", "[[vix-calls]]", "[[long-straddle]]", "[[volatility-trading]]", "[[2026-02-citrini-tech-selloff]]", "[[2026-03-bls-900k-jobs-revision]]", "[[2026-04-meta-ai-layoffs]]"]
---

The AI Recession Playbook is the meta-strategy a trader opens when they want to position a full book for an AI-driven labor recession. It is not a single trade — it is a coordinated set of legs across equities, credit, volatility, and rates that each express a different facet of the [[capital-vs-labor-asymmetry]] mispricing, sized so that the book makes money in any of three labor-recession scenarios (slow burn, Citrini base, 2028 GIC tail) without depending on a precise crash date. Reference event for the regime: the [[2026-02-citrini-tech-selloff]] and [[2026-03-bls-900k-jobs-revision]] (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]]).

This page is a meta-strategy: it composes three deployable sub-strategies — [[ai-sector-rotation-energy-hedge]], [[white-collar-ai-displacement-short]], and [[tech-hub-muni-bond-short]] — into one position book with explicit weights, hedge ratios, triggers, and kill criteria. Read those pages first if you have not already.

### Sub-strategy map

| Sub-strategy | Express via | Edge facet | Tier | Stand-alone page |
|--------------|-------------|------------|------|------------------|
| AI sector rotation + energy hedge | Long XLE / utilities / nuclear / skilled-trades | Structural (durable capex → power demand) | 1 | [[ai-sector-rotation-energy-hedge]] |
| White-collar AI displacement short | Short legacy SaaS / legal / accounting / junior-IT basket | Behavioral + analytical (margin-disparity) | 1 | [[white-collar-ai-displacement-short]] |
| Tech-hub muni / regional credit short | Short munis / KRE; long Treasury duration | Informational (slow fiscal repricing) | 2 | [[tech-hub-muni-bond-short]] |
| Tail / volatility overlay | VIX call ladder + SPX put spreads + Mag-7 puts | Risk-bearing (crisis-alpha convexity) | 3 | [[vix-calls]], [[long-straddle]] |

The book is regime-aware by construction; map current conditions against the [[regime-matrix]] before sizing, and log every rebalance to the [[live-journal]].

## Edge Source

Three categories in the [[edge-taxonomy]]:

1. **Structural** — AI capex commitments are physically durable (PPAs, transformer backlogs, nuclear fuel contracts) while AI software margins are revisable on a single earnings call. The capex-vs-cash-flow asymmetry is real and slow to reprice.
2. **Behavioral** — allocators are anchored to "AI = long tech" framing. Most institutional mandates cannot easily express the bifurcation between AI-disrupted and AI-enabled equity, leaving the cross-sectional spread under-arbitraged.
3. **Informational** — lagging indicators ([[bls-benchmark-revisions]], [[randstad-job-postings]], regional sales-tax receipts) repeatedly surprise to the downside. The [[ai-layoff-trap]] paper, the ESRB systemic-risk channels, and Citrini's [[citrini-2028-global-intelligence-crisis]] scenario each describe the same cascade and each are non-consensus.

## Why This Edge Exists

1. **Asymmetric speed.** Capital captures AI productivity gains immediately (margin expansion books in the current quarter); labor absorbs job losses on a 2-4 quarter delayed schedule via [[service-sector-multiplier]] dynamics. Markets that mark to capital first, labor second, are structurally late.
2. **Mandate constraints.** Long-only equity managers cannot easily short legal SaaS or tech-hub munis. Long-short equity pods focus on intra-sector pairs, not cross-asset structural themes. The playbook's edge partially exists *because it is hard to express* inside conventional fund structures.
3. **Recency bias on tail risk.** [[citrini-2028-global-intelligence-crisis]] (10%+ unemployment, ~40% stock decline) was published in February 2026 and triggered a tech selloff, but volatility surface re-priced within weeks. VIX at 18.37 (4 May 2026) does not price the tail.
4. **Solow paradox window.** [[solow-paradox-2026]]: 90% of firms report zero measurable productivity gains from AI capex despite massive spending. Until the J-curve resolves, capex *destroys* labor income without creating offsetting consumption.

## Null Hypothesis

Under a no-edge null: AI is a normal productivity cycle, the displacement metrics in the source are noise inside a tight 4.5-4.8% unemployment band, the [[ai-layoff-trap]] is a non-falsifiable theoretical model, and the energy / tech-hub / SaaS spreads are fully priced. In that world the playbook earns roughly the cost of its hedges (negative carry on VIX calls, financing on shorts) and the long-energy beta — call it a -2% to +3% range with low realised vol.

A clean test requires decomposing each leg's return against (a) equity factor benchmarks (value, low-vol, momentum), (b) sector beta to XLE / XLK, (c) Treasury duration, and (d) realised vs implied vol on the option overlays. Only residual returns are "AI labor recession alpha."

## Rules

### Conviction Tiers

| Tier | Conviction | Sizing | Instruments |
|------|-----------|--------|-------------|
| **Tier 1** | High — direct, durable, multiple confirming data sources | 5-15% of book per leg | Long XLE / utilities / nuclear; long skilled-trades infrastructure ([[quanta-services]], [[caterpillar]], [[eaton]], [[emerson-electric]], [[ge-vernova]]); short legacy white-collar SaaS basket |
| **Tier 2** | Medium — directionally correct but timing-dependent | 2-7% of book per leg | Short KRE / regional banks; short tech-hub munis (limited liquidity); long [[constellation-energy]] / [[vistra]] / [[nextera-energy]] / [[oklo]] / [[bloom-energy]] single names |
| **Tier 3** | Tail / asymmetric only — defined-loss option structures | 0.5-2% premium per leg | VIX call ladder; SPX put-spread collars; long-dated put options on [[microsoft]] / [[meta-platforms]] / [[alphabet]] / [[amazon]] stock as funding-cost bearing tail bets |

### Position Book Template (Base Case — Citrini Slow Burn)

For a $1M discretionary book, indicative allocations:

| Leg | Weight | Rationale | Tier |
|-----|--------|-----------|------|
| Long energy / utilities / nuclear (XLE core + names) | 30% | Tier-1 long, see [[ai-sector-rotation-energy-hedge]] | 1 |
| Long skilled-trades infrastructure basket | 15% | Tier-1 long, [[skilled-trades-wage-boom]] inverse trade | 1 |
| Short white-collar SaaS basket (legal, accounting, junior-analyst IT services) | 15% | Tier-1 short, see [[white-collar-ai-displacement-short]] | 1 |
| Short tech-hub munis OR short KRE (regional banks) | 10% | Tier-2 short, see [[tech-hub-muni-bond-short]] | 2 |
| VIX call ladder (3-6 month, 22-30 strikes) | 5% premium | Tier-3 tail hedge for [[citrini-2028-global-intelligence-crisis]] | 3 |
| Long-dated SPX put spreads (12-month, -10%/-20%) | 5% premium | Defined-loss tail | 3 |
| Cash / T-bills | 20% | Dry powder for re-up after first 10% drawdown | — |

Total gross exposure ~120% (long + short legs), defined-loss option premium ~10% of book, cash ~20%.

### Hedge Ratios (Dollar Neutralisation)

Long-short pairs are dollar-neutralised, not beta-neutralised, on entry. Beta drift is monitored monthly; rebalance when net beta exceeds +/- 0.20 vs SPX.

- **Long skilled-trades vs short white-collar SaaS**: 1:1 dollar weight. Both are mid-cap-skewed; net sector beta near zero; net AI-thesis exposure positive (long the disruption-resistant side, short the disrupted side).
- **Long XLE vs short legacy enterprise software basket**: 1.5:1 dollar (XLE has lower beta, so size up). Captures the cross-sector AI rotation.
- **Long Treasury duration (TLT or IEF) vs short tech-hub munis**: duration-neutral (match modified duration, not dollar amount). The trade isolates credit-spread widening on the muni side.
- **VIX calls vs SPX put-spreads**: complementary, not hedged against each other. VIX captures vol-of-vol; SPX put-spread captures directional drawdown.

### Trigger Map (Lagging Indicators → Sizing Decisions)

The playbook is sized off a small set of lagging indicators that each map to a specific sub-leg.

| Indicator | Source | Trigger | Action |
|-----------|--------|---------|--------|
| BLS benchmark revision direction | [[bls-benchmark-revisions]] | Monthly revision more negative than -200K | Increase long-energy weight by 2-5pp; the [[2026-03-bls-900k-jobs-revision]] confirmed the regime |
| Tech-hub sales tax revenue YoY | Bay Area, Austin, Seattle, Boston quarterly municipal filings | Quarterly print < -3% YoY | Increase tech-hub muni short / KRE short weight by 2-5pp |
| VIX term structure (front-month vs 6-month) | Cboe | Backwardation OR vol-of-vol spike | Roll VIX call ladder up the strike; do not increase notional |
| IBKR Forecast Trader recession probability | [[ibkr-forecast-trader]] | Recession probability > 50% (41% as of 2026-05) | Take Tier-3 hedges off the table — the tail is no longer cheap; rotate premium into Tier-1 shorts |
| Hyperscaler capex guidance | [[microsoft]] / [[meta-platforms]] / [[alphabet]] / [[amazon]] earnings | Two consecutive quarters of guide-down | Reduce long-energy weight by 5-10pp; the structural thesis is breaking — see [[ai-sector-rotation-energy-hedge]] |
| Randstad skilled-trades demand | [[randstad-job-postings]] | Robotics / HVAC / electrician demand growth flattens | Reduce long skilled-trades weight by 2-5pp; the inverse trade is exhausting |
| Anthropic / OpenAI revenue inflection | Quarterly disclosures | Vertical AI booking accelerates beyond consensus | Reduce white-collar short weight; thesis converging into price |

### Scenario Trade Matrix

The playbook is sized for three labour-recession scenarios. Trade legs are weighted differently in each.

| Leg | Slow burn (most likely) | Citrini base case | 2028 GIC tail |
|-----|-------------------------|-------------------|----------------|
| Long energy / nuclear / utilities | 30% | 25% | 15% (capex itself stalls) |
| Long skilled-trades infrastructure | 15% | 20% | 15% |
| Short white-collar SaaS | 15% | 25% | 25% |
| Short tech-hub munis / KRE | 10% | 15% | 15% |
| VIX call ladder (premium) | 3% | 5% | 8% |
| SPX put spreads (premium) | 3% | 5% | 7% |
| Long-dated single-name puts on Mag 7 | 0% | 2% | 5% |
| Cash / T-bills | 24% | 3% | 10% |

The slow-burn allocation is the **starting allocation**. Migration toward the base / tail allocations happens on triggers (above), not on view changes. This is intentional — it forces evidence-based, not vibes-based, sizing.

### Time-Horizon Overlay

| Window | Event | Position |
|--------|-------|----------|
| Q1 2026 (already happened) | [[2026-02-citrini-tech-selloff]], [[2026-03-bls-900k-jobs-revision]], [[2026-04-meta-ai-layoffs]] | Entry window — initial sizing in slow-burn allocation |
| Q2-Q3 2026 | [[service-sector-multiplier]] cascades 2-4 quarters after Q1 tech cuts | Watch BLS revisions; expect confirmation of multiplier; add to white-collar short and tech-hub muni short |
| Q4 2026 | Tech-hub fiscal stress (3-7% sales tax revenue contraction) materialises | Largest single move expected in tech-hub muni / regional bank legs; have option roll plan ready |
| 2027+ | Political response — Pigouvian tax debate, UBI proposals, retraining bills | Begin migrating playbook out; see Kill Criteria |

## Implementation Pseudocode

```python
# Pseudocode — not production. Illustrative only.

def ai_recession_playbook(book_value, regime, signals):
    """
    regime: one of "slow_burn", "citrini_base", "gic_tail"
    signals: dict of latest readings on trigger map indicators
    returns: dict of leg -> dollar allocation
    """
    # 1. Scenario base weights
    base = {
        "slow_burn":    {"long_energy": 0.30, "long_trades": 0.15, "short_saas": 0.15,
                         "short_munis": 0.10, "vix_calls": 0.03, "spx_puts": 0.03,
                         "mag7_puts": 0.00, "cash": 0.24},
        "citrini_base": {"long_energy": 0.25, "long_trades": 0.20, "short_saas": 0.25,
                         "short_munis": 0.15, "vix_calls": 0.05, "spx_puts": 0.05,
                         "mag7_puts": 0.02, "cash": 0.03},
        "gic_tail":     {"long_energy": 0.15, "long_trades": 0.15, "short_saas": 0.25,
                         "short_munis": 0.15, "vix_calls": 0.08, "spx_puts": 0.07,
                         "mag7_puts": 0.05, "cash": 0.10},
    }
    weights = dict(base[regime])

    # 2. Trigger adjustments (caps in [-0.10, +0.10] per leg)
    if signals["bls_revision"] < -200_000:
        weights["long_energy"]  += 0.03
        weights["short_saas"]   += 0.02
    if signals["tech_hub_sales_tax_yoy"] < -0.03:
        weights["short_munis"]  += 0.03
    if signals["recession_prob"] > 0.50:
        weights["vix_calls"]    -= 0.02
        weights["spx_puts"]     -= 0.02
        weights["short_saas"]   += 0.02
        weights["short_munis"]  += 0.02
    if signals["hyperscaler_capex_qoq"] < 0 and signals["hyperscaler_capex_qoq_prev"] < 0:
        weights["long_energy"]  -= 0.07
        weights["cash"]         += 0.07
    if signals["skilled_trades_demand_yoy"] < 0:
        weights["long_trades"]  -= 0.03
        weights["cash"]         += 0.03

    # 3. Hedge ratios (dollar-neutral within long-short pairs)
    weights["short_saas"]  = -abs(weights["short_saas"])
    weights["short_munis"] = -abs(weights["short_munis"])

    # 4. Renormalise so absolute non-cash legs sum to ~1.0 (gross 100%)
    return {k: round(v * book_value, 0) for k, v in weights.items()}

def kill_book(signals):
    """Hard exit: flatten everything except cash."""
    return (
        signals["pigouvian_tax_passed"]
        or signals["ex_mag7_margin_pct"] > 0.105   # productivity J-curve resolves
        or signals["anthropic_revenue_yoy"] > 5    # AI capex justified by revenue
        or signals["bls_unemployment_rate"] < 0.04 # labor market re-tightening
    )
```

## Indicators / Data Used

- **Equity prices**: XLE, XLK, XLF, KRE, QQQ, plus single-name overweights ([[constellation-energy]], [[vistra]], [[nextera-energy]], [[oklo]], [[bloom-energy]], [[ge-vernova]], [[quanta-services]], [[caterpillar]], [[eaton]], [[emerson-electric]])
- **Hyperscaler capex guidance**: [[microsoft]], [[meta-platforms]], [[alphabet]], [[amazon]], [[nvidia]], [[apple]] — quarterly earnings
- **Volatility surface**: VIX spot, VIX term structure (Cboe), individual-name implied vol
- **Recession probability**: [[ibkr-forecast-trader]] — 41% as of 2026-05
- **Labour market lagging indicators**: [[bls-benchmark-revisions]], [[randstad-job-postings]], [[skillit-construction-wages]], NCCI quarterly
- **Regional fiscal data**: tech-hub city / county sales tax filings (Bay Area, Austin, Seattle, Boston)
- **Credit spreads**: HY OAS vs IG OAS, KRE option skew, muni / Treasury yield ratios
- **Macro**: DXY (USD index — flight-to-quality on confirmation), 10y Treasury yield

## Cross-Asset Coverage

| Asset class | Long | Short | Tail / option |
|-------------|------|-------|----------------|
| **Equities — large cap** | XLE, utilities, nuclear | Legacy enterprise SaaS basket | Long-dated puts on [[microsoft]], [[meta-platforms]], [[alphabet]], [[amazon]] |
| **Equities — mid / small** | Skilled-trades infra, [[oklo]], [[bloom-energy]] | KRE (regional banks), tech-hub-exposed REITs | — |
| **Credit** | IG corporates, Treasury duration | Tech-hub munis, HY (off-the-run regional bank issuers) | KRE put options |
| **Rates / FX** | TLT or IEF (duration) | — | DXY long as flight-to-quality (small Tier-3) |
| **Commodities** | Copper (data center proxy), uranium, natural gas (turbine fuel) | — | Energy call options on tariff-shock tail |
| **Volatility** | — | — | VIX call ladder, SPX put spreads |

## Example Trade

**Scenario**: It is mid Q3 2026. Q2 BLS revision came in at -340K. Bay Area sales tax revenue printed -4.1% YoY. Recession probability on [[ibkr-forecast-trader]] climbed from 41% to 48%. Hyperscaler capex guidance held flat-to-up. Trader has a $1M discretionary equity sleeve.

Starting from the slow-burn allocation, applying the trigger map:

- BLS revision < -200K → long-energy +3pp, short-SaaS +2pp
- Tech-hub sales tax < -3% → short-munis +3pp
- Recession prob still < 50% → no Tier-3 reduction yet
- Hyperscaler capex flat → no long-energy reduction

Adjusted allocation: long energy 33%, long trades 15%, short SaaS 17%, short munis 13%, VIX calls 3%, SPX puts 3%, cash 16%.

Trader rolls VIX calls (had 22-strike Sep, rolls to 24-strike Dec on Cboe ATM), tops up XLE long by ~$30K, adds ~$20K notional short on a basket of legal SaaS names, and takes ~$30K notional short on KRE (cheaper to express than direct muni shorts). Net beta to SPX checked: was +0.05, now -0.10 — within tolerance.

## Performance Characteristics

This is an untested composite playbook (`backtest_status: untested`). Realistic estimates with conservative cost overlay:

- **Best plausible Sharpe (net of costs)**: 0.7-1.0 if the slow-burn or Citrini base case plays out
- **Realistic null-case Sharpe**: -0.2 to +0.3 if AI productivity J-curve resolves and the playbook just bleeds option premium
- **Cost overlay** (per leg, round-trip):
  - XLE / single-name equity legs: 5-10 bps
  - White-collar SaaS short basket: 15-25 bps (rebalancing + borrow cost on illiquid names)
  - KRE / muni short: 30-80 bps depending on instrument (muni market is the binding constraint)
  - VIX call ladder: 20-40% of premium per roll — the dominant drag
  - SPX put spreads: 1-2% of notional per 12 months
- **Expected max drawdown** (excluding option premium spend): -25% in the null case (productivity J-curve resolves and shorts get squeezed simultaneously)
- **Realised correlation to SPX**: target -0.20 to +0.10. The playbook is *not* a net short — it is sector-rotational with tail overlay.

### Inter-leg correlation and concentration monitoring

Because the legs all express the same underlying [[capital-vs-labor-asymmetry]] thesis, the dominant *hidden* risk is that they stop being diversifying and start moving together (all the "short" legs are short-equity-vol in a crash; all the "long" legs are pro-cyclical energy beta in a tariff shock). Monitor the cross-leg correlation matrix monthly:

| Leg pair | Intended relationship | Watch for |
|----------|----------------------|-----------|
| Long energy ↔ short SaaS | Low / mildly negative (rotation) | Both falling together in a broad de-risking |
| Short SaaS ↔ short munis/KRE | Positive (both AI-displacement shorts) | Squeeze on both simultaneously on a relief rally |
| VIX calls ↔ SPX put spreads | Both long-convexity, complementary | Premium decay if the tail never fires |
| Long Treasury ↔ short munis | Spread-isolation (duration matched) | Muni-Treasury basis breaking in a muni dislocation |

When realised pairwise correlation among the short legs exceeds ~0.7 for 30 days, the diversification assumption has failed — treat the book as a single net-short bet and cut gross accordingly.

### Operational cadence

| Frequency | Task |
|-----------|------|
| Daily | Net beta and net-delta check; option-overlay mark; VIX term-structure read |
| Weekly | Single-name borrow costs on short basket; KRE skew; rebalance any leg drifted > 2pp |
| Monthly | Inter-leg correlation matrix; net-beta rebalance if outside ±0.20; trigger-map review |
| Quarterly | Tech-hub sales-tax prints; hyperscaler capex guides; full scenario re-weight; [[live-journal]] entry |
| Per-event | BLS revisions, Mag-7 layoffs, prediction-market jumps → apply trigger map |

## Capacity Limits

- **Long-energy / skilled-trades / Mag 7 puts legs**: large — 1B+ across the equity book before market impact dominates.
- **White-collar SaaS short basket**: ~50M before borrow costs and short-squeeze risk on individual names compress edge.
- **Tech-hub muni short**: ~25M — muni illiquidity is the binding constraint. See [[tech-hub-muni-bond-short]].
- **Regional bank / KRE short**: 200M+ on KRE itself; single-name regional bank shorts are smaller (10-50M each).
- **VIX call ladder**: 50-100M premium notional before becoming a noticeable buyer in the surface.

Aggregate playbook capacity: roughly 2B before the muni and short-SaaS legs become the bottleneck. Beyond that, the playbook reduces to the long-energy + Mag 7 put-spread version with weaker edge.

## What Kills This Strategy

From [[failure-modes]]:

1. **Productivity J-curve resolves quickly.** [[solow-paradox-2026]] turns out to have been a measurement artifact; ex-Mag-7 margins reflate from 9% to 11%+ within a year. Short-SaaS basket gets squeezed; energy long under-performs broad equity. **Highest probability kill.**
2. **Pigouvian tax passes.** [[pigouvian-automation-tax]] enacted at federal level. Mag 7 capex slows, energy thesis weakens, but white-collar shorts may hold. Net: book becomes a tracking error to general equity bear move. **Tail-but-real probability.**
3. **AI capex disclosure shows revenue inflection.** [[ai-capex-vs-cash-flow-divergence]] resolves favourably — Anthropic / OpenAI / Mag 7 vertical AI revenue accelerates. Capex is no longer "burning cash with no offset." White-collar short loses its narrative anchor.
4. **Labour market re-tightens.** Wage compression reverses, displaced workers find jobs at non-discounted wages within 6 months. Tech-hub fiscal contraction never materialises. Muni shorts bleed; service-sector multiplier never triggers.
5. **Crowding into the rotation.** Other allocators replicate "long energy / short SaaS" at scale; spread compresses; entry-vol grows; carry deteriorates. Crowding-risk is `medium`, not `high`, today — but watch.
6. **Tariff / geopolitical shock that hits energy supply.** Long-energy leg rallies for the wrong reason; positioning gets confused; risk-management discipline breaks down.

## Kill Criteria

Hard exits (flatten everything except VIX residual):

- Pigouvian automation tax passes a national legislature (not state-level)
- Ex-Mag-7 S&P 500 net margin reflates above 10.5% on a trailing 4-quarter basis
- Anthropic and OpenAI combined trailing-12M revenue exceeds 5x prior-year (capex justified by revenue)
- BLS unemployment rate falls below 4.0% on three consecutive monthly prints
- Drawdown on the playbook exceeds -25% peak-to-trough at the book level

Soft exits (reduce by 50%):

- Hyperscaler capex guides down two consecutive quarters
- VIX trades above 35 for 30 consecutive sessions (tail-hedge has paid; rotate out, not in)
- Recession probability on [[ibkr-forecast-trader]] crosses 65% (consensus is now in the trade)

Re-review window: every 90 days, log to [[live-journal]].

## Counter-Scenarios — When To Flatten The Book

1. **Productivity boom**: Mag 7 cash flows accelerate, ex-Mag 7 margins reflate, BLS revisions turn positive. Flatten. The trade was wrong.
2. **Geopolitical reset**: A hot conflict re-prices everything; the AI-labor thesis is dwarfed by macro vol. Flatten the labor-recession-specific legs (white-collar short, muni short); keep the energy long and convert VIX to a smaller defensive sleeve.
3. **Regulatory landing**: Pigouvian tax is enacted in form-of-compromise (limited scope, slow phase-in). Re-size — keep skilled-trades long, drop white-collar short to half size, drop muni short entirely.
4. **Anthropic / OpenAI revenue beat**: Vertical AI revenue inflects. Drop white-collar short to zero. Energy and skilled-trades legs survive.

## Advantages

- Diversified across asset classes — no single thesis failure flattens the book
- Multiple independent confirming data feeds (BLS, sales tax, capex, prediction market)
- Defined-loss tail hedges (option premium) cap the cost of being early
- Edge is multi-sourced (structural + behavioral + informational), not reliant on a single mispricing
- Deployable in $250K-$2B size
- Compatible with long-only mandates if the short legs are replaced with underweights vs benchmark

## Disadvantages

- Requires active management of 5-7 legs simultaneously — operationally heavy
- Muni short and white-collar SaaS short have liquidity constraints
- Option-premium drag on Tier-3 legs is real and persistent if the tail does not arrive
- Untested as a composite — see `backtest_status: untested`
- Edge depends on a 2026-2028 window; decays after that
- High coordination cost across desks if implemented across institutional silos

## Sources

- [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]] — primary source for all data points (Goldman 11M jobs, Citrini 2028 GIC, 4pp tech / non-tech margin gap, ex-Mag-7 9% margins, 41% recession probability, 3-7% tech-hub sales tax contraction, 123 GW data center demand by 2035)
- [[2026-02-citrini-tech-selloff]] — wiki news record of the regime-defining selloff (verified)
- [[2026-03-bls-900k-jobs-revision]] — wiki news record of the labour-data confirmation event
- [[2026-04-meta-ai-layoffs]] — wiki news record of the first explicit AI-attribution mega-cap layoff

## Related

- Sub-strategies: [[ai-sector-rotation-energy-hedge]], [[white-collar-ai-displacement-short]], [[tech-hub-muni-bond-short]]
- Concepts: [[ai-layoff-trap]], [[citrini-2028-global-intelligence-crisis]], [[service-sector-multiplier]], [[capital-vs-labor-asymmetry]], [[skill-bifurcation]], [[wage-compression-vs-job-loss]], [[ai-driven-demand-destruction]], [[tech-hub-concentration-risk]], [[margin-expansion-disparity]], [[solow-paradox-2026]], [[skilled-trades-wage-boom]], [[ai-data-center-power-demand]], [[pigouvian-automation-tax]]
- Frameworks: [[edge-taxonomy]], [[failure-modes]], [[regime-matrix]], [[live-journal]], [[research-checklist]], [[hypothesis-to-backtest-workflow]], [[itpm-trade-construction-playbook]]
- Risk concepts: [[crisis-alpha]], [[tail-risk]], [[hedging-strategies]], [[position-sizing]], [[risk-of-ruin]], [[barbell-strategy]], [[asymmetric-barbell]]
- Tail strategies: [[vix-calls]], [[long-straddle]], [[volatility-trading]]
- News anchors: [[2026-02-citrini-tech-selloff]], [[2026-03-bls-900k-jobs-revision]], [[2026-04-meta-ai-layoffs]]
- Forward links (created in parallel): [[esrb-ai-systemic-risk-channels]], [[esrb]], [[brett-hemenway-falk]], [[gerry-tsoukalas]], [[openai]], [[ai-capex-vs-cash-flow-divergence]], [[productivity-j-curve]], [[junior-analyst-stranding]], [[legal-services-ai-disruption]], [[stranded-office-real-estate]]
