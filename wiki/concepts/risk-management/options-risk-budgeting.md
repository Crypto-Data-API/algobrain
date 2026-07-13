---
title: "Options Risk Budgeting"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, portfolio-theory, itpm]
aliases: ["Risk Budgeting for Options", "Options Risk Allocation"]
related: ["[[options-portfolio-construction]]", "[[risk-budgeting]]", "[[vega-budgeting]]", "[[theta-targeting]]", "[[portfolio-greeks-aggregation]]", "[[options-position-sizing]]", "[[value-at-risk]]", "[[expected-shortfall]]", "[[itpm-trade-construction-playbook]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[options-greeks]]", "[[risk-budgeting]]"]
difficulty: advanced
---

Options risk budgeting is the practice of allocating a portfolio's total risk capacity across [[options-greeks|Greek-based exposures]] (delta, gamma, vega, theta, rho) and across simultaneously running options trades, rather than allocating dollars of premium. Because individual options P&L is non-linear in the underlying — and because Greeks aggregate non-trivially across strikes, expirations, and underlyings — a budget expressed purely in dollars-at-risk is almost always misleading. The [[itpm|ITPM]] curriculum and most professional options desks therefore build their risk framework around *Greek caps* and *scenario losses* rather than dollar premium spent.

This page is the options-specific complement to [[risk-budgeting]] (which covers the linear, mean-variance/HRP world). It describes how to size a multi-Greek risk budget, allocate it across strategy sleeves and underlyings, and re-budget when conditions break the model. It is downstream of [[position-sizing]] and [[risk-management]] generally, and the binding tail constraint it enforces is the [[risk-of-ruin|risk-of-ruin]] survivability constraint — a Greek budget that passes every cap but allows a 4σ shock to halve the book has not actually been budgeted.

## Quick Reference — The Six-Cap System

The core of options risk budgeting is that a position must satisfy *every* cap below independently — you cannot net a comfortable theta budget against a breached gamma budget. Indicative caps per $100k of equity for a balanced book (tighten for short-vol sleeves, see [[theta-targeting]] and [[vega-budgeting]]):

| Cap | Measures | Indicative balanced cap (per $100k) | Binding for |
|---|---|---|---|
| **Delta** | Linear directional P&L | ±200 to ±500 (beta-weighted) | Directional sleeves |
| **Gamma** | Convexity / hedging cost | ±50 to ±150 | Short-premium, 0DTE |
| **Vega** | IV sensitivity (per vol point) | ±$500 to ±$3,000 | Premium selling, vol-arb |
| **Theta** | Daily time decay | ±$100 to ±$500/day | Premium sellers (income line) |
| **Rho** | Rate sensitivity | Soft cap | LEAPS, box spreads |
| **Scenario** | Worst-case stress-grid loss | ≤15-20% of account | Short-vol (the real constraint) |

All figures are illustrative starting points, not prescriptions; the scenario cap is the one that actually prevents [[risk-of-ruin|ruin]], because the Greeks can all look small while the [[non-linear-payoff|non-linear payoff]] explodes in the wings.

## Why Linear Risk Budgets Fail for Options

Classical [[risk-budgeting]] assumes returns are approximately normal and that risk contributions decompose linearly via the covariance matrix. Options violate both assumptions:

1. **Non-linear payoff in the underlying.** A long call has positive [[gamma]]. A 1% move in the underlying produces *more* than 1% × delta of P&L when the move is large. "I am risking $10,000 on this trade" is only true at one specific spot/IV/time point — it changes the moment the underlying moves.
2. **Greeks themselves move with spot, time, and IV.** Delta drifts as gamma kicks in. Vega is largest at-the-money and decays as options go deep ITM/OTM. Theta accelerates near expiration. A static "$10k delta budget" can become a $25k delta exposure after a 3% move.
3. **Vega depends on the IV regime.** A short-strangle with $500 vega in a 15-vol regime carries very different scenario risk than the same nominal vega in a 35-vol regime, because IV-of-IV (vol of vol) scales with the level. See [[vol-of-vol]] and [[vol-regime-detection]].
4. **Cross-Greek interactions.** Short-vol books typically have negative gamma *and* short vega *and* positive theta — these risks are all correlated, especially in a [[volatility-spike|vol spike]] where realized vol explodes simultaneously with implied vol. Treating them as independent budgets understates the joint tail.
5. **Path dependence.** Two portfolios with identical instantaneous Greeks can have very different outcomes over a week because gamma and vega *evolve along the path*. This is invisible to linear VaR but central to [[scenario-analysis]].

The takeaway: dollar-VaR is necessary but not sufficient. You need budgets in each Greek dimension *and* a separate budget for worst-case scenario loss across a grid of spot × IV × time shocks.

## Risk Dimensions to Budget

A complete options risk budget allocates capacity across the following dimensions. Each is enforced as an independent cap; a position must fit *every* cap, not the sum of dollar values.

### 1. Net Delta Budget
- **What it measures**: linear directional exposure to the underlying (or to a beta-weighted benchmark — see [[beta-weighted-delta]]).
- **Typical cap**: ±200 to ±500 deltas per $100k of equity for a balanced book; tighter (±50 deltas) for vol-arb sleeves that aim to be [[delta-neutral]].
- **Aggregation**: sum deltas across positions. For multi-name books, beta-weight to SPY (or appropriate index) so a long 100 delta of MSFT is comparable to long 100 delta of TLT.

### 2. Net Gamma Budget
- **What it measures**: convexity — the rate at which delta changes as spot moves. Determines hedging cost and pin risk.
- **Typical cap**: ±50 to ±150 gamma per $100k. Short-gamma positions (covered calls, iron condors, short strangles) accumulate quickly and must be capped tightly.
- **Why it matters separately from delta**: a delta-hedged short gamma book has zero delta but still loses on every realized move (the [[gamma-pnl]] term).

### 3. Net Vega Budget
- **What it measures**: sensitivity to a 1-vol-point change in implied volatility. The dominant P&L driver for premium-selling and vol-arb books.
- **Typical cap**: ±$500 to ±$3,000 per vol point per $100k of equity, depending on aggressiveness and IV regime.
- **Sub-budgets**: split into *short-dated vega* (front-month, sensitive to event vol) and *long-dated vega* (term-structure trades). The two have different risk profiles. See [[vega-budgeting]].
- **Vega-by-strike**: also worth tracking [[volga]] and [[skew]] exposure separately for any book material in OTM wings.

### 4. Net Theta Budget
- **What it measures**: P&L decay per day from time passage. For premium sellers this is the *income line*; for premium buyers it is the *cost*.
- **Typical cap**: short-theta books target -$100 to -$500/day per $100k. Long-theta (premium-seller) books target +$100 to +$500/day per $100k.
- **Rule of thumb**: net portfolio theta should not exceed 0.5%/day of equity. If your daily decay income is more than that, you are almost certainly oversized in short premium and one [[volatility-spike|vol spike]] will erase weeks of theta. See [[theta-targeting]].

### 5. Net Rho Budget
- **What it measures**: sensitivity to a 1bp change in interest rates.
- **Typical cap**: usually a soft cap unless running a [[long-dated-options|LEAPS]] or [[interest-rate-options]] book. For most equity-options portfolios, rho is a rounding error vs delta/vega.
- **When it bites**: long-dated, deep-ITM calls and box spreads. Becomes material in fast-moving rate regimes (2022-2024).

### 6. Tail-Risk / Scenario Budget
- **What it measures**: maximum portfolio loss across a stress grid.
- **Typical grid**: spot ±5%, ±10%, ±20%; IV +5, +10, +20 points; time +1d, +1w. Combined shocks (spot -10% with IV +15) capture the [[fat-tails|fat-tail]] regime.
- **Typical cap**: worst-case scenario loss <= 15-20% of account. This is the binding constraint for short-vol books, where the Greeks look small but the [[non-linear-payoff|non-linear payoff]] explodes in the wings.
- **Methodology**: see [[scenario-analysis]] and [[expected-shortfall]]. Many desks also run a [[historical-stress-test]] over 2008, 2020-03, 2018-02, 2025 episodes.

## Setting the Total Risk Budget

The total budget is derived from three account-level inputs:

1. **Account size (E)** — equity available, after cash reserves for margin expansion.
2. **Annual drawdown tolerance (DD)** — typically 15-25% for retail; 5-10% for institutional.
3. **Annual return target (R)** — should be commensurate with drawdown via a target Sharpe (R / DD ≈ 0.5 to 1.5 for realistic options books, after costs).

From these:

- **Annual portfolio vol target**: σ_target ≈ DD / 2 (a 15% drawdown roughly corresponds to 7-8% annual vol given fat tails — short-premium books realize roughly 2x their normal-distribution vol).
- **Daily VaR at 95%**: 1.65 × (σ_target / √252) × E. For a $250k account targeting 8% vol, daily 95% VaR ≈ $2,050.
- **Tail scenario cap**: typically 2-3x the daily VaR.

The total budget is then *distributed* across the Greek dimensions and across sleeves below.

## Allocating Across Strategies (Sleeves)

A diversified options book typically runs three or four *sleeves*, each with its own Greek profile and risk allocation. Suggested initial allocations (for a book targeting balanced risk):

| Sleeve | Risk Allocation | Greek Profile | Purpose |
|---|---|---|---|
| **Short premium** ([[iron-condor]], [[short-strangle]], [[credit-spread]]) | 40-50% | Long theta, short gamma, short vega | Income; profits from vol overpricing and time decay |
| **Directional** ([[long-call]], [[bull-call-spread]], [[risk-reversal]]) | 25-35% | Long delta or short delta, long gamma, mixed vega | Express macro/catalyst views |
| **Vol arbitrage** ([[calendar-spread]], [[diagonal-spread]], dispersion) | 10-20% | Delta-neutral, mixed gamma, long-vega/short-vega across term | Profit from term-structure or skew mispricings |
| **Tail hedge** ([[long-put|OTM puts]], [[vix-call|VIX calls]], variance swaps) | 5-10% | Negative theta, long gamma, long vega | Protect against the tail loss the other sleeves are exposed to |

Allocation is made in *risk units*, not dollars. For example, on a $250k account with $5,000 daily 95% VaR:

- Short premium gets $2,000-$2,500 of daily VaR
- Directional gets $1,250-$1,750
- Vol arb gets $500-$1,000
- Tail hedge typically *uses up* $250-$500/day in negative carry but provides asymmetric upside in scenarios

The tail-hedge sleeve is critical: short-premium books have hidden left-tail risk, and a small allocation to long-gamma/long-vega protection often stabilizes portfolio Sharpe even though it bleeds in calm regimes. This is the [[itpm-trade-construction-playbook|ITPM]] insight that "the cost of insurance is the price of staying in business."

## Allocating Across Underlyings and Sectors

Greeks aggregate at the underlying level but risks correlate at the sector/factor level. Concentration limits:

- **Single underlying**: no single name should contribute more than 20-25% of portfolio gamma, vega, or beta-weighted delta. For short-premium sleeves, more like 10-15% per name.
- **Sector**: cap at 30-40% of any single Greek per [[gics-sector|GICS sector]]. A book of 8 short strangles all in tech is *one* trade, not 8 — they all crush together in a tech selloff.
- **Factor**: track exposure to [[size-factor]], [[value-factor]], [[momentum-factor]], and especially [[low-vol-factor]] (since low-vol stocks dominate short-premium screens). Cap factor exposure at ±0.5σ of the factor return.
- **Correlation regime**: in a [[risk-off]] correlation spike (correlations → 1), the *effective* concentration is much higher than the nominal. Pre-stress concentration limits assuming correlations of 0.8 across longs and 0.8 across shorts.

For a worked treatment of the underlying-level aggregation math, see [[portfolio-greeks-aggregation]].

## Allocating Across Expirations

Expiration buckets behave differently and need separate caps:

| Bucket | DTE | Gamma Profile | Vega Profile | Risk Notes |
|---|---|---|---|---|
| **0DTE / weekly** | 0-7 days | Extreme gamma, low vega | Tiny | Pin risk dominates; size by max-loss only — see [[zero-dte-options]] |
| **Front-month** | 7-45 days | High gamma | Medium vega | The "sweet spot" for premium sellers; most P&L lives here |
| **Near-dated** | 45-90 days | Medium gamma | Medium-high vega | Calendar-spread anchor; vol-arb sleeve |
| **Long-dated / LEAPS** | 90+ days | Low gamma | Highest vega, material rho | Directional bets with long horizon; small gamma but big vega |

Suggested gamma cap: at most 60% of total portfolio gamma should sit in 0-21 DTE options. Anything more and a single 2-sigma move can blow through the daily VaR. Vega cap: limit *any single expiration cycle* to 40% of the portfolio's total vega — otherwise an idiosyncratic shock to one event (e.g. an [[earnings-announcement|earnings IV crush]]) dominates the book.

## Re-Budgeting Triggers

The risk budget is not static. It must shrink (or shift) when reality breaks the model. Concrete re-budget triggers:

1. **Realized vol breaks the budget**. If the portfolio's 5-day realized P&L vol exceeds 1.5× the modeled daily vol for two consecutive weeks, the model is wrong (or the regime has shifted). Cut all Greek caps by 50% until the model re-calibrates.
2. **Drawdown trigger**. At -5% account drawdown: halve all sleeve allocations. At -10%: close vol-arb and short-premium sleeves entirely; keep only tail-hedge and the highest-conviction directional positions.
3. **IV regime shift**. If the [[vix|VIX]] (or appropriate vol benchmark) crosses a regime boundary (e.g. >25 from <20), recalibrate vega caps — short-vega capacity should shrink as IV rises because [[vol-of-vol]] is non-linear in level.
4. **Correlation regime shift**. If 1-month average pairwise correlation in the long book or the short book exceeds 0.7, treat the book as a single concentrated position and cut sleeve sizes accordingly.
5. **Liquidity shock**. If bid-ask spreads on key positions widen >2x normal, exit-cost rises non-linearly. Cut size before [[liquidity-risk]] forces it.
6. **Catalyst proximity**. As a position approaches its catalyst date (earnings, FDA, Fed), gamma and vega both grow toward expiration. Re-budget the position 5-7 days before the catalyst — either close, roll out, or hedge.
7. **Macro regime change**. If the macro view that drove the directional sleeve flips (e.g. Fed pivots, growth data turns), the entire directional sleeve needs review — see [[itpm-trade-construction-playbook]] Stage 10.

## Reporting

Daily reporting must attribute P&L *and risk* across multiple axes simultaneously. A minimal options-book daily report includes:

### P&L attribution by Greek
Decompose daily P&L into:
- **Delta P&L** = portfolio delta × spot move
- **Gamma P&L** = 0.5 × portfolio gamma × (spot move)²
- **Vega P&L** = portfolio vega × IV change
- **Theta P&L** = portfolio theta × 1 day
- **Residual** (vanna, volga, charm, costs) = total P&L − sum of the above

If the residual is consistently >20% of total P&L, the desk has un-modeled risk (typically from [[second-order-greeks]] or skew dynamics).

### Risk attribution by name
For each underlying, report current delta, gamma, vega, theta, and *scenario loss* at -5% spot / +5 IV. Order by largest scenario loss to surface concentration before the market does.

### Risk attribution by sleeve
For each of the 3-4 sleeves above: % of total risk budget consumed, current daily VaR, current scenario loss, and sleeve P&L MTD. Surface any sleeve consuming >120% of its budgeted risk for immediate review.

### Greek time series
A 30-day chart of net delta, gamma, vega, theta. Drift in any of these without an intentional decision is evidence of *implicit* re-budgeting — Greeks moving on their own as the market moves. Address before they breach a cap.

### Scenario grid
Daily P&L matrix across spot × IV shocks. Worst cell should be within the tail-risk budget set above. If the worst cell breaches the budget, there is no negotiation — cut size before the next session.

## Worked Example — $250k Account

**Inputs**:
- Account equity (E): $250,000
- Target return (R): 12% annual = $30,000
- Max drawdown tolerance (DD): 15% = $37,500
- Implied target Sharpe ≈ 1.0 (after costs)
- Implied annual vol target: ~8% = $20,000

**Derived total budget**:
- Daily 95% VaR ≈ 1.65 × $20,000 / √252 ≈ $2,080
- Daily tail-scenario cap (worst stress cell) ≈ $7,500 (3% of equity)
- Annual theta budget if running short premium: target +$30k from theta = $120/day average

**Sleeve allocation**:

| Sleeve | % of Risk Budget | Daily VaR | Scenario Loss Cap | Greek Caps (per $100k, scaled to $250k) |
|---|---|---|---|---|
| Short premium | 45% | $935 | $3,400 | Δ: ±400 / Γ: -250 / V: -$2,500 / Θ: +$300/day |
| Directional | 30% | $625 | $2,250 | Δ: ±750 (intentional bias) / Γ: ±150 / V: ±$1,000 |
| Vol arb | 15% | $310 | $1,150 | Δ: ±50 (hedged) / Γ: ±100 / V: ±$1,500 (term-spread) |
| Tail hedge | 10% (carry) | n/a | -$250/day bleed | Δ: -100 to -200 (puts) / V: +$500 / Γ: +75 |

**Concrete positions consistent with this budget**:

*Short-premium sleeve (~$112,500 of risk allocation)*:
- 5x SPX iron condors, 30 DTE, 1-sigma wings: ~$1,500 max loss each, ~$60 theta total
- 3x QQQ short strangles, 21 DTE, 16-delta: ~$30 theta each, capped at $5,000 max loss per
- 2x bond ETF (TLT) short puts at support: diversifies sector, low correlation to equity vol

Sleeve aggregate: theta ≈ +$200/day; vega ≈ -$2,200; gamma ≈ -220; scenario loss at SPX -5%/IV+10 ≈ -$3,200 (within $3,400 cap).

*Directional sleeve (~$75,000)*:
- Long [[bull-call-spread]] on a high-conviction long thesis (e.g. semi cycle): 50 contracts, $4 wide, $1 debit = $20,000 risk, +320 deltas, +$300 vega.
- Short [[bear-call-spread]] on a high-conviction short thesis: 30 contracts, $5 wide, $1.50 credit = $10,500 risk, -180 deltas, -$200 vega.

Sleeve aggregate: net delta ≈ +140 (intentional long bias), gamma ≈ +60, vega ≈ +$100. Within ±750 delta cap.

*Vol-arb sleeve (~$37,500)*:
- 2x SPY [[calendar-spread]], long 60 DTE / short 30 DTE, ATM: collects term-structure premium, ~+$800 vega front-back, near-zero delta.

*Tail-hedge sleeve (~$25,000 in capital, ~$250/day in carry)*:
- Long 5x SPX 90 DTE puts at -10% strike: -100 deltas, +$500 vega, +75 gamma, -$80/day theta.
- Long 10x [[vix|VIX]] 45 DTE 25-strike calls: +$200 vega in equity terms, -$60/day theta.

**Aggregate book Greeks** (sum of sleeves):
- Net delta ≈ +40 (essentially flat after directional + tail-hedge offset)
- Net gamma ≈ -85 (slightly short, dominated by short premium offset by tail puts)
- Net vega ≈ -$800 (modest short vega — most short-prem vega is offset by tail + vol-arb longs)
- Net theta ≈ +$120/day (income engine)
- Worst scenario cell (SPX -10% / IV +15): -$5,800 vs $7,500 cap

**Re-budget triggers wired in**:
- If MTD drawdown hits -$12,500 (-5%): halve every sleeve.
- If realized 5-day vol > 1.5× model for two weeks: cut Greek caps by 50%.
- If [[vix|VIX]] crosses 25: shrink short-vega cap by 30%.
- If average pairwise correlation in short-premium book > 0.7: treat as single position, cut to 1 unit.

This worked example illustrates that a coherent options risk budget is *multi-dimensional* — six Greek caps, a scenario cap, a sleeve allocation, a concentration check, and a set of re-budget triggers. The budget is not a single number; it is a *system of caps* that must all bind simultaneously. (Figures above are illustrative; calibrate to your own account, costs, and regime.)

## Pre-Trade Budget Checklist

Before adding any position to the book, walk it through the budget — not just its standalone risk but its *marginal* contribution to every cap:

1. **Marginal delta** — does the new position push net beta-weighted delta past the cap? Beta-weight to the index before checking.
2. **Marginal gamma** — does it push gamma past cap, and how much of the gamma sits in 0-21 DTE? (Target ≤60% of total gamma in the front bucket.)
3. **Marginal vega** — split into short-dated vs long-dated; does either sub-budget breach? Is the vega cap appropriate for the current IV regime (shrink as IV rises)?
4. **Marginal theta** — for a premium seller, does adding this push daily decay above the 0.5%/day-of-equity ceiling? If your income line is "too good," you are oversized in short premium.
5. **Marginal scenario loss** — re-run the spot × IV stress grid *with* the new position. The worst cell is the only number that matters; if it breaches, the trade is rejected regardless of how attractive the Greeks look.
6. **Marginal concentration** — does it tip any single name past 20-25% of any Greek, or any sector past 30-40%?
7. **Correlation overlay** — would this position crush together with existing positions in a [[correlation-regime|correlation spike]]? Stress at correlation 0.8 before approving.

A position that fails any one check does not enter the book at full size — it is resized, restructured, or rejected.

## Pitfalls and Failure Modes

The most common ways options risk budgets fail in practice:

| Pitfall | Mechanism | Mitigation |
|---|---|---|
| **Budgeting in premium dollars** | "$10k at risk" is true at one spot/IV/time point only; the [[non-linear-payoff]] breaks the assumption the moment spot moves | Budget in Greeks + scenario loss, never in premium |
| **Static Greek caps** | Delta drifts as [[gamma]] kicks in; a "$10k delta" becomes $25k after a 3% move — implicit re-budgeting nobody decided | Track Greek time series; re-budget on drift before it breaches |
| **Vega caps not scaled to IV regime** | Short $500 vega in a 15-vol regime ≠ same vega in a 35-vol regime; [[vol-of-vol]] is non-linear in level | Shrink short-vega capacity as the [[vix\|VIX]] rises across regime boundaries |
| **Treating cross-Greek risks as independent** | Short-vol books are short gamma *and* short vega *and* long theta simultaneously — all correlated in a [[volatility-spike]] | Use the joint scenario grid, not summed dollar VaRs |
| **Concentration disguised as diversification** | Eight short strangles in tech is one trade, not eight — they crush together in a sector selloff | Cap per-name and per-sector Greeks; pre-stress at correlation 0.8 |
| **The [[the-theta-trap\|theta trap]]** | A premium book collects income for months, the trader upsizes, and a single discontinuous move erases years of theta | Hard scenario cap; mandatory long-vol overlay; the [[the-theta-trap\|theta-trap]] exit playbook |
| **Ignoring path dependence** | Two books with identical instantaneous Greeks have different week-ahead outcomes because gamma/vega evolve along the path | [[scenario-analysis]] over multi-day paths, not single-point VaR |
| **No re-budget triggers wired in** | The budget is treated as set-once; reality breaks the model and nobody resizes | Pre-commit the drawdown / realized-vol / IV-regime triggers above |

The deepest failure is the [[the-theta-trap|theta trap]]: a Greek budget that looks disciplined in calm regimes but has no binding scenario cap is exactly the structure that blows up in a vol expansion. The scenario cap, not the Greek caps, is what keeps the book inside the [[risk-of-ruin|recoverable zone]].

## Related

- [[options-portfolio-construction]] — how to build the full options book
- [[risk-budgeting]] — the linear/equity-bond version of this framework
- [[vega-budgeting]] — deeper dive on the vol-exposure budget
- [[theta-targeting]] — using theta income as a return target
- [[portfolio-greeks-aggregation]] — math of aggregating Greeks across underlyings
- [[options-position-sizing]] — sizing of individual positions within the budget
- [[value-at-risk]] — VaR methodology
- [[expected-shortfall]] — tail-risk metric, complement to VaR
- [[scenario-analysis]] — building the stress grid
- [[itpm-trade-construction-playbook]] — discretionary workflow that this budget enforces discipline against
- [[options-greeks]] — primer on the underlying risk measures
- [[delta-neutral]] — delta-budget = 0 special case
- [[gamma-pnl]] — the gamma component of P&L attribution
- [[vol-of-vol]] — why vega caps must scale with IV regime
- [[correlation-regime]] — when concentration limits need to tighten
- [[zero-dte-options]] — special considerations for 0DTE in the gamma budget
- [[risk-of-ruin]] — the survivability constraint the scenario cap enforces
- [[the-theta-trap]] — the canonical failure mode of an unbudgeted short-premium book
- [[position-sizing]] — the upstream sizing discipline
- [[risk-management]] — the parent framework

## Sources

- [[itpm]] — risk-budgeting discipline as taught in the ITPM curriculum
- [[itpm-trade-construction-playbook]] — companion workflow for trade construction
- [[book-option-volatility-and-pricing]] — Natenberg on portfolio-level Greek management
- [[book-dynamic-hedging]] — Taleb on non-linear risk and scenario thinking
