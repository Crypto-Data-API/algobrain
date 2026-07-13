---
title: "White-Collar AI Displacement Long-Short"
type: strategy
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [stocks, ai-trading, risk-management, event-driven, pairs-trading]
aliases: ["AI Displacement Pair Trade", "Bifurcation Long-Short", "AI-Disrupted vs AI-Enabled Basket"]
strategy_type: hybrid
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: untested
edge_source: [structural, behavioral]
edge_mechanism: "Mag 7 + AI infrastructure capture margin gains; legacy white-collar SaaS faces revenue compression as customers automate the workflow the SaaS was selling. The market still prices both halves as 'tech' with similar multiples, leaving a long-short spread that compensates for the 4pp tech / non-tech margin gap and the 9% ex-Mag-7 S&P 500 margin reality."
data_required: [equity-prices, fundamentals-pit, short-borrow-rates, hyperscaler-capex-guidance, vertical-ai-ma-data, anthropic-openai-revenue-disclosures]
min_capital_usd: 100000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.20
breakeven_cost_bps: 60
decay_evidence: "Edge concentrated in 2026-2028 window. Decays when (a) ex-Mag-7 S&P 500 margins reflate from 9% (sign that AI productivity is bottom-line-visible across the index), (b) Anthropic / OpenAI vertical AI revenue accelerates beyond consensus (capex justified), or (c) post-Anthropic April 2026 legal-tool launch initial repricing exhausts. See [[margin-expansion-disparity]] and [[ai-capex-vs-cash-flow-divergence]]."
related: ["[[ai-recession-playbook]]", "[[tech-hub-muni-bond-short]]", "[[ai-sector-rotation-energy-hedge]]", "[[ai-layoff-trap]]", "[[skill-bifurcation]]", "[[wage-compression-vs-job-loss]]", "[[capital-vs-labor-asymmetry]]", "[[margin-expansion-disparity]]", "[[ai-driven-demand-destruction]]", "[[skilled-trades-wage-boom]]", "[[ai-data-center-power-demand]]", "[[solow-paradox-2026]]", "[[anthropic]]", "[[microsoft]]", "[[meta-platforms]]", "[[alphabet]]", "[[amazon]]", "[[nvidia]]", "[[apple]]", "[[quanta-services]]", "[[caterpillar]]", "[[eaton]]", "[[emerson-electric]]", "[[ge-vernova]]", "[[constellation-energy]]", "[[vistra]]", "[[oklo]]", "[[bloom-energy]]", "[[equity-long-short]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[regime-matrix]]", "[[live-journal]]", "[[research-checklist]]", "[[itpm-trade-construction-playbook]]", "[[2026-02-citrini-tech-selloff]]", "[[2026-04-meta-ai-layoffs]]"]
---

A long-short equity basket strategy that goes long companies enabled by AI infrastructure (skilled-trades, power, defense / regulated SaaS) and short legacy white-collar SaaS whose customers are now automating the workflow that SaaS used to sell. The thesis is that the market under-prices the bifurcation between AI-disrupted and AI-enabled equity within "tech" — see [[margin-expansion-disparity]]: tech net margins of ~13.2% mask the fact that ex-[[microsoft]] / [[meta-platforms]] / [[alphabet]] / [[amazon]] / [[nvidia]] / [[apple]], the broader S&P 500 margin is closer to 9% (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]]).

This strategy is one leg of the broader [[ai-recession-playbook]]; deploy stand-alone or as part of the playbook book.

## Edge Source

Two categories from [[edge-taxonomy]]:

1. **Structural edge** — there is a real cash-flow asymmetry between Mag 7 plus AI infrastructure (capturing margin gains, including the ~4pp tech / non-tech margin gap) and legacy white-collar SaaS whose customers are deploying AI to automate the workflow the SaaS was selling. The 90% YoY growth in vertical AI M&A (266 deals in Q1 2026) is the structural confirmation that incumbents are being replaced, not augmented.
2. **Behavioral edge** — most equity allocators bucket "tech" as one factor. Sector mandates and benchmark-aware long-only managers are constrained from expressing the bifurcation. Long-short pods focus on intra-sector pairs (e.g., one accounting SaaS vs another) rather than the cross-sectional AI-disrupted / AI-enabled spread.

## Why This Edge Exists

1. **Solow Paradox is still binding.** [[solow-paradox-2026]]: 90% of firms report zero measurable productivity gains from AI capex. Until that resolves, AI capex is destroying labor income (and SaaS seat revenue) without creating offsetting consumption. The income side of legacy SaaS customers is shrinking; the disruption side is also shrinking. Both ends of the legacy SaaS P&L are stressed.
2. **Anthropic April 2026 inflection.** [[anthropic]]'s April 2026 release of an explicit legal-automation tool (document review, contract analysis) made disruption tangible, not theoretical. Yet 68% of corporate legal departments don't know whether outside counsel uses AI — creating a visibility crisis for the SaaS providers selling the legacy workflow.
3. **Mag 7 cash flows are real.** Capital expenditure on AI is being booked, billed, and paid — to Nvidia, to power providers, to Quanta-style contractors. The capex is not speculative; the *return on* capex is the question. While that question is open, the providers of capex inputs are being paid.
4. **Crowding hasn't equalised the spread.** Despite the [[2026-02-citrini-tech-selloff]] focusing market attention on the bifurcation, sector ETFs have not reweighted; index funds still own AI-disrupted SaaS at the same weight as AI-enabled infrastructure.
5. **Seat compression on the revenue side.** [[2026-04-09-saas-agent-selloff|April 9 2026 SaaSpocalypse Day]] (NET -12%, SNOW -9%, NOW -7%, CRM -4%) confirmed the market is now actively pricing AI-agent orchestration as a permanent revenue-side headwind for seat-license SaaS. If 10 agents do the work of 100 reps, seat counts compress in the disrupted workflows — a structural revenue erosion incumbents cannot offset by adding AI features.
6. **AI COGS creep on the cost side.** [[ai-cogs-creep]]: adding AI features to SaaS routes ~$15 of inference / model / vector-DB cost per $100 of revenue, taking gross margin from 80% toward 65% (and AI-first products toward ~52% per ICONIQ 2026). Crucially this sits in *cost of revenue*, so headcount cuts (which sit in opex) cannot offset it. The [[2026-05-08-cloudflare-ai-layoff-selloff|Cloudflare May 8 2026 print]] is the firm-level confirmation: -24% on a 230 bps gross-margin miss in the same quarter as the ~20% AI-attributed workforce cut.
7. **Klarna-class reversal risk on the short side's bull case.** The [[klarna]] reversal (CEO admitted "we went too far," rehired humans, Q1 2025 net loss doubled) is the public failure of the "AI replaces N humans" claim in customer service. Investors now demand evidence rather than narrative for any AI-substitution announcement — the "show-me" stance behind ServiceNow Q1 2026 (beat earnings, stock fell 11% intraday) and Salesforce 2026 YTD (-30%). This creates persistent multiple compression on legacy SaaS even when prints are clean.

## Null Hypothesis

Under a no-edge null: the long-short basket earns approximately the value-vs-growth factor differential plus a small size premium. The 4pp tech / non-tech margin gap is a steady-state of the new economy that the market has already correctly priced; the ex-Mag-7 9% margin level is a one-time non-tech composition effect that mean-reverts; and the [[ai-driven-demand-destruction]] thesis is overweighted by the [[ai-layoff-trap]] paper.

A clean test decomposes returns against (a) the Russell 1000 Growth-vs-Value factor, (b) sector betas to XLK, (c) a "high-quality minus low-quality" factor (return on capital, leverage), and (d) the borrow rate on the short basket. Only the residual is "AI bifurcation alpha."

## The Two Legs Side by Side

The strategy is a *thematic basket pair*, and the two legs have very different risk and capacity profiles. Treating them as one undifferentiated "trade" is a common error:

| Dimension | Long leg (AI-enabled infra) | Short leg (legacy white-collar SaaS) |
|---|---|---|
| **Thesis** | Capex is booked and paid regardless of ROI | Revenue and margin compressed by AI substitution |
| **Edge category** | Structural (real cash flows) | Structural + behavioral (mis-bucketed as "tech") |
| **Names** | Industrials, utilities, power, grid, regulated SaaS | Legal / accounting / consulting / BPO SaaS |
| **Liquidity / capacity** | High (~$500M+) | Low (~$50M, borrow-constrained) |
| **Beta to SPX** | High, positive (cyclical drift) | Lower, can be negative in selloffs |
| **Carry** | Long carry (positive drift) | Negative carry (borrow cost 50–150 bps/yr) |
| **Dominant risk** | Beta drift toward "long cyclicals"; Klarna-class AI reversal | Short squeeze, take-private bid, borrow spike |
| **Survives if thesis fails?** | Yes (capex story stands) | No (the disruption *is* the thesis) |

The asymmetry matters for construction: the long leg has a standalone reason to exist (the [[ai-data-center-power-demand|power/grid buildout]]), while the short leg is purely a thesis expression. This is why the book runs **net long** (+5% to +15%) rather than market-neutral — the long leg carries positive drift the short leg cannot match, and over-shorting to force neutrality just adds borrow drag.

## Regime Fit

Per the [[regime-matrix]], this is a thematic long-short with a mild long bias, so its regime behavior blends value/growth dynamics with a structural-disruption overlay:

| Regime | Fit | Reason |
|---|---|---|
| **Trending up (low vol)** | Mixed | Long leg participates, but a *broad* risk-on rally lifts the short basket too (beta squeeze) |
| **Trending down** | Good for short leg | Legacy SaaS multiple compression accelerates; but watch take-private bids on washouts |
| **Sideways / chop** | Best | The bifurcation spread can grind in without index beta dominating either leg |
| **High vol / risk-off** | Dangerous both ways | Short squeezes on illiquid SaaS names *and* cyclical long leg sells off; correlations → 1 |
| **Rate / inflation regime** | Tailwind | A value-over-growth rotation reinforces the structural spread (the null-case factor tilt) |

The trade is **most vulnerable to a melt-up risk-on regime** where everything-tech rallies and the short leg squeezes faster than the long leg gains. It is **most comfortable in a discriminating, fundamentals-led tape** where the market actually re-prices margins — which is the [[#Why This Edge Exists|"show-me" stance]] the strategy depends on.

## Rules

### Universe

**Long basket (skilled-trades and AI-enabled infrastructure)**
- Specialty contractors and grid: [[quanta-services]], [[ge-vernova]]
- Industrial / electrical OEMs: [[caterpillar]], [[eaton]], [[emerson-electric]]
- Power producers serving data centers: [[constellation-energy]], [[vistra]], [[nextera-energy]]
- Defense and regulated-vertical SaaS (Anthropic-resistant): companies whose moats include compliance certifications, classified clearances, FDA / FedRAMP gates
- Healthcare regulated workflow (resistant to general-purpose LLM displacement)
- Data center power infrastructure (turbines, transformers, switchgear)
- Optionality / small caps: [[oklo]], [[bloom-energy]]

**Short basket (legacy white-collar SaaS facing AI disruption)**
- Legal SaaS — document review, contract management, e-discovery — most exposed post-Anthropic April 2026 launch ([[legal-services-ai-disruption]])
- Accounting SaaS and BPO — junior-analyst-heavy workflow (54% of financial sector jobs flagged by Citigroup as high-automation potential)
- Consulting and IT services with junior-analyst-heavy delivery models ([[junior-analyst-stranding]])
- Customer-support BPO and helpdesk / call-center SaaS
- Junior-analyst-heavy SMB software whose customers' headcount is shrinking via AI

The strategy is implemented as a *basket*, not a single-name pair. This avoids idiosyncratic blowups (e.g., a take-private bid on one short name) and reduces the variance of the long-short spread.

### Entry

- **Confirmation gate**: at least one of the following has printed within the trailing 90 days
  - BLS benchmark revision more negative than -200K (cf. [[2026-03-bls-900k-jobs-revision]])
  - Anthropic, OpenAI, or a Mag-7 lab releases a vertical-AI tool targeting a specific white-collar workflow (cf. Anthropic April 2026 legal tool)
  - At least one Mag-7 announces an AI-attributed workforce reduction (cf. [[2026-04-meta-ai-layoffs]])
  - Vertical AI M&A exceeds 50 deals in a quarter (Q1 2026 was 266 deals)
- **Margin-gap check**: trailing 4-quarter S&P 500 ex-Mag-7 net margin remains below 11% (currently ~9% per [[margin-expansion-disparity]])
- **Borrow rate check**: borrow rates on the short basket below 200 bps annualized; otherwise reduce notional or substitute with put options

### Position Sizing

- Long basket: 50-60% of strategy capital, equal-weighted within each sub-bucket (skilled-trades 25-30%, regulated SaaS 15-20%, power infra 10-15%)
- Short basket: 40-50% of strategy capital, equal-weighted across legal / accounting / consulting / BPO sub-buckets to avoid single-vertical concentration
- Net dollar exposure: target +5% to +15% net long. The strategy is *not* a market-neutral hedge fund vehicle — the long side has a positive structural drift the short side does not need to neutralize fully.
- Net beta to SPX: target +0.10 to +0.30 (mildly long-biased)
- Position cap per single name: 5% of strategy

### Exits

Reduce or close when:

- Ex-Mag-7 S&P 500 net margin reflates above 11% on a trailing 4-quarter basis
- A short-name's borrow rate exceeds 500 bps — replace with put options or drop from basket
- The bifurcation thesis is mainstream — when sell-side strategy notes from at least three top-10 banks recommend the trade, scale down by 30%
- See **Kill Criteria** for hard exits

## Implementation Pseudocode

```python
# Pseudocode — illustrative.

LONG_BASKET = {
    # Specialty contractors and grid
    "QUANTA_SERVICES": 0.10, "GE_VERNOVA": 0.06, "EATON": 0.05,
    "EMERSON_ELECTRIC": 0.04, "CATERPILLAR": 0.05,
    # Power producers
    "CONSTELLATION_ENERGY": 0.06, "VISTRA": 0.05, "NEXTERA": 0.04,
    # Optionality
    "OKLO": 0.02, "BLOOM_ENERGY": 0.02,
    # Regulated SaaS (defense / healthcare workflow) - filled by screen
    "REGULATED_SAAS_BUCKET": 0.07,
}  # weights sum to ~0.56

SHORT_BASKET = {
    "LEGAL_SAAS_BUCKET": 0.12,        # doc review / contract / e-discovery
    "ACCOUNTING_SAAS_BUCKET": 0.10,   # junior-analyst-heavy
    "CONSULTING_IT_BUCKET": 0.10,     # IT services with junior-heavy delivery
    "BPO_HELPDESK_BUCKET": 0.08,      # call-center / helpdesk
}  # weights sum to ~0.40, net long ~+0.16

def signal_active(macro):
    """Confirmation gate: at least one trigger in last 90 days."""
    return (
        macro["bls_revision"] < -200_000
        or macro["new_vertical_ai_tools_90d"] >= 1
        or macro["mag7_ai_layoff_announcement_90d"] >= 1
        or macro["vertical_ai_ma_deals_quarter"] >= 50
    )

def can_enter(macro, borrow):
    return (
        signal_active(macro)
        and macro["sp500_ex_mag7_net_margin_ttm"] < 0.11
        and max(borrow.values()) < 0.02   # 200 bps borrow cap
    )

def rebalance(book_value, macro, borrow):
    if not can_enter(macro, borrow):
        return {"cash": book_value}
    longs  = {k: v * book_value for k, v in LONG_BASKET.items()}
    shorts = {k: -v * book_value for k, v in SHORT_BASKET.items()}
    return {**longs, **shorts}

def kill(macro):
    return (
        macro["sp500_ex_mag7_net_margin_ttm"] > 0.11
        or macro["anthropic_openai_revenue_yoy"] > 5
        or macro["pigouvian_tax_passed"]
    )
```

## Indicators / Data Used

- **Equity prices and fundamentals**: rolling 4-quarter net margin per name and per sub-bucket; revenue YoY growth on legacy SaaS short names (the leading indicator of disruption hitting the income statement)
- **Hyperscaler capex guidance**: [[microsoft]], [[meta-platforms]], [[alphabet]], [[amazon]] quarterly — confirms the long basket's revenue source
- **Borrow rates**: daily monitoring of short-basket borrow availability and cost
- **Vertical AI M&A activity**: deal count and median valuation multiples — the structural confirmation of disruption
- **Anthropic / OpenAI product launches**: each new vertical-AI tool is a discrete trigger
- **BLS benchmark revisions**: [[bls-benchmark-revisions]]
- **Margin disparity tracking**: [[margin-expansion-disparity]] — quarterly update of ex-Mag-7 S&P 500 margins

## Example Trade

**Scenario**: Mid-Q2 2026. The April 2026 Anthropic legal-tool launch is two months old. Q1 2026 vertical AI M&A printed 266 deals (90% YoY). [[2026-04-meta-ai-layoffs]] (8,000 roles, AI-attributed) confirmed the trend. Borrow on the legal-SaaS basket is 80-180 bps; on the accounting basket 60-100 bps.

Trader deploys $1M into the strategy:

- Long $560K across the long basket weighted as above
- Short $400K notional across the short basket
- Net long ~$160K, net beta to SPX ~+0.18
- 30-day implied vol on the short basket ~28%; on the long basket ~22%

After three months, the legal-SaaS short basket draws down 14% (vertical-AI competitor announces design-wins inside Fortune 500 corporate legal departments); the long basket is flat-to-up 4% (energy / utilities range-bound, skilled-trades up). Short basket P&L: +$56K; long basket P&L: +$22K. Total P&L on $1M: +$78K (+7.8%) over three months. Net beta drift: from +0.18 to +0.06 as the short basket beta dropped — trader rebalances back to original weights, taking some short profit.

This example is *illustrative* and not a backtest. `backtest_status: untested`.

## Performance Characteristics

Realistic estimates with conservative cost overlay:

- **Best plausible Sharpe (net of costs)**: 0.6-0.9 if the bifurcation thesis plays out within 12-24 months
- **Realistic null-case Sharpe**: 0.0 to +0.4 — strategy still earns the value-vs-growth differential and a small size premium even without the AI thesis
- **Cost overlay (round-trip per rebalance)**:
  - Long basket: 8-15 bps
  - Short basket: 25-40 bps (borrow + slippage on smaller-cap names)
  - Quarterly rebalance: 30-60 bps total cost drag annually
  - Borrow drag: 50-150 bps per year on the short basket
- **Expected max drawdown**: -20% if the productivity J-curve resolves and short squeezes hit simultaneously
- **Realised correlation to SPX**: target +0.30 to +0.50 (mildly long-biased basket)
- **Realised correlation to value-vs-growth factor**: meaningful — the strategy will look like value over growth in the null case

## Capacity Limits

- **Long basket**: scales to 500M+; large-cap industrials and utilities have ample liquidity
- **Short basket**: ~50M before borrow availability and squeeze risk on individual SaaS names compresses edge. The accounting SaaS sub-bucket is the binding constraint (mid-cap names with thinner float)
- **Strategy total capacity**: ~50M per fund mandate. Beyond that, replace short-basket exposure with put-spread overlays on legacy-SaaS sector ETFs, accepting weaker edge.
- **Crowding risk**: medium and rising. Watch for sell-side replication.

## What Kills This Strategy

From [[failure-modes]]:

1. **Productivity J-curve resolves.** Ex-Mag-7 margins reflate from 9% to 11%+; legacy SaaS revenue stabilises as the AI capex cycle creates offsetting consumption; short basket gets squeezed. **Highest-probability kill.** See [[solow-paradox-2026]].
2. **Vertical AI revenue stalls.** Anthropic / OpenAI fail to monetise vertical applications quickly enough; legacy SaaS retains its embedded distribution moat; the disruption narrative loses urgency. The long basket may still work (capex is still being spent), but the short basket bleeds.
3. **Take-private wave.** Private equity acquires distressed legacy SaaS companies at premium multiples, taking out the short basket via M&A premia. Mitigation: diversify within each sub-bucket; cap single-name exposure at 5%.
4. **Regulatory backstop.** [[pigouvian-automation-tax]] enacted; AI capex slows; both sides of the trade compress. Long basket hurts more than short basket initially; book becomes a net loss.
5. **Mag 7 antitrust action.** [[microsoft]] / [[meta-platforms]] / [[alphabet]] / [[amazon]] face structural break-up risk; capex slows; long basket loses its revenue source.
6. **Borrow squeeze.** Specific short names see borrow rates spike to 5-10%+; basket has to be scaled down or replaced with options.
7. **Klarna-class reversal in the long basket.** A frontier AI deployer (Mag 7 or hyperscaler-aligned) publicly reverses an AI workforce substitution because customer-experience quality degrades — the [[klarna]] pattern at megacap scale. The long basket's AI-narrative premium compresses; AI capex guidance is cut; the long-side revenue source thins. Mitigation: monitor customer-satisfaction proxies (NPS, churn, support-ticket volumes) at long-basket names alongside margin and revenue; if any long-basket name signals quality degradation, rotate within the long basket toward energy / power infrastructure (lower exposure to the customer-experience channel).
8. **Inference cost collapse.** A 10×+ drop in foundation-model inference costs in 12 months largely neutralizes [[ai-cogs-creep]] for the short basket, removing one of the three legs supporting the trade. The seat-compression and Klarna-class-reversal legs would still apply, but conviction and time-to-resolution weaken. Watch token-cost trajectories from Anthropic, OpenAI, Google, and open-weight competition.

## Kill Criteria

Hard exits (close all legs):

- Ex-Mag-7 S&P 500 net margin reflates above 11% on a trailing 4-quarter basis
- Anthropic and OpenAI combined trailing-12M revenue exceeds 5x prior-year
- Pigouvian automation tax passes a federal legislature
- Drawdown on the strategy exceeds -20% peak-to-trough
- Average borrow rate across short basket exceeds 500 bps for 30 consecutive sessions

Soft exits (reduce by 50%):

- Vertical AI M&A deal count falls below 50 per quarter for two consecutive quarters
- Sell-side strategy desks at three top-10 banks recommend the same long-short spread
- Long basket beta to SPX exceeds +1.2 (the trade has become a momentum chase)

Re-review window: every 60 days, log to [[live-journal]].

## Advantages

- Self-funding short side reduces capital requirement
- Multiple discrete confirmation triggers (BLS revisions, vertical AI launches, Mag-7 layoffs) reduce reliance on a single signal
- Long basket has a real cash-flow story even if the short thesis fails
- Compatible with long-short equity mandates as a thematic sleeve
- Edge survives modest J-curve resolution (~10.5% ex-Mag-7 margin) — only fully kills above 11%

## Disadvantages

- Borrow costs and short-squeeze risk are real and persistent
- Operationally heavy — basket rebalance, borrow monitoring, quarterly margin tracking
- Crowding risk medium and rising
- Untested as a composite — `backtest_status: untested`
- Capacity limited to ~50M per mandate
- Requires legal / accounting / IT-services sub-sector knowledge to construct the short basket safely
- Long basket beta drift toward +1 in benign markets — trade can become indistinguishable from "long industrial cyclicals"

## Sources

- [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]] — primary source for all data points (4pp tech / non-tech margin gap, 9% ex-Mag-7 margins, 266 vertical AI M&A deals Q1 2026 [+90% YoY], Anthropic April 2026 legal-tool launch, [[2026-04-meta-ai-layoffs]] 8,000 roles, 54% Citigroup high-automation finance jobs, 68% corporate legal AI usage visibility gap). Raw file: `raw/articles/2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces.md` (Perplexity deep research via `gap_finder.py`, logged in [[log|wiki log]] 2026-04-22; source-summary page pending).
- News anchors used as triggers and confirmations: [[2026-02-citrini-tech-selloff]], [[2026-04-09-saas-agent-selloff]], [[2026-05-08-cloudflare-ai-layoff-selloff]], [[2026-04-meta-ai-layoffs]], [[2026-03-bls-900k-jobs-revision]].

## Related

- Sub-strategies / parent: [[ai-recession-playbook]] (parent), [[tech-hub-muni-bond-short]] (sibling), [[ai-sector-rotation-energy-hedge]] (sibling)
- Concepts: [[ai-layoff-trap]], [[skill-bifurcation]], [[wage-compression-vs-job-loss]], [[capital-vs-labor-asymmetry]], [[margin-expansion-disparity]], [[ai-driven-demand-destruction]], [[skilled-trades-wage-boom]], [[ai-data-center-power-demand]], [[solow-paradox-2026]]
- Frameworks: [[edge-taxonomy]], [[failure-modes]], [[regime-matrix]], [[live-journal]], [[research-checklist]], [[itpm-trade-construction-playbook]], [[equity-long-short]]
- Entities: [[anthropic]], [[microsoft]], [[meta-platforms]], [[alphabet]], [[amazon]], [[nvidia]], [[apple]], [[quanta-services]], [[caterpillar]], [[eaton]], [[emerson-electric]], [[ge-vernova]], [[constellation-energy]], [[vistra]], [[oklo]], [[bloom-energy]]
- News anchors: [[2026-02-citrini-tech-selloff]], [[2026-04-meta-ai-layoffs]]
- Forward links: [[legal-services-ai-disruption]], [[junior-analyst-stranding]], [[ai-capex-vs-cash-flow-divergence]], [[productivity-j-curve]], [[stranded-office-real-estate]], [[openai]]
