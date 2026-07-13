---
title: "Capital Structure Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, quantitative, volatility, derivatives, stocks, bonds]
aliases: ["Cap Structure Arb", "CSA", "Debt-Equity Arbitrage"]
strategy_type: quantitative
timeframe: position
markets: [stocks, bonds, options]
complexity: advanced
backtest_status: untested
edge_source: [analytical, structural]
edge_mechanism: "Different classes of investors (credit funds, equity funds, quant equity, CDS dealers) price the same firm's cash flows inconsistently; the Merton model links them but market segmentation keeps spreads, vols, and equity prices out of sync."
data_required: [equity-prices, options-chain, cds-quotes, bond-quotes, fundamentals-pit, capital-structure-data]
min_capital_usd: 5000000
capacity_usd: 2000000000
crowding_risk: medium
expected_sharpe: 0.9
expected_max_drawdown: 0.35
breakeven_cost_bps: 40
related: ["[[cds-bond-basis-arbitrage]]", "[[convertible-arbitrage]]", "[[merton-model]]", "[[credit-default-swap]]", "[[volatility-arbitrage]]", "[[merger-arbitrage]]", "[[archegos]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[arbitrage]]"]
---

# Capital Structure Arbitrage

Capital structure arbitrage trades different securities issued by the **same company** -- common equity, preferred stock, senior debt, subordinated debt, [[convertible-bond|convertibles]], and [[credit-default-swap|CDS]] -- against each other when their prices imply inconsistent views of firm value or default probability. The theoretical anchor is the [[merton-model|Merton (1974) structural model]]: equity is a [[call-option]] on the firm's assets struck at the face value of debt, so equity volatility, equity price, leverage, and credit spreads are linked by a single set of firm-value dynamics. It is a flagship [[relative-value-arbitrage]] strategy — a single-name sibling of [[cds-bond-basis-arbitrage]] and [[convertible-arbitrage]] — and, like all [[convergence-arbitrage]], it is exposed to the [[limits-to-arbitrage]] that turn "convergence" into "blowup" when the model breaks or funding seizes.

At a glance:

| Attribute | Value |
|---|---|
| Style | [[relative-value-arbitrage]] across one issuer's capital stack |
| Model anchor | [[merton-model\|Merton (1974)]] / [[creditgrades\|CreditGrades]] structural credit |
| Core trade | CDS leg vs equity leg in Merton-delta ratio |
| Edge sources | [[edge-taxonomy\|Analytical + structural]] |
| Canonical blowups | GM/Ford May 2005, Deutsche Bank/Weinstein 2008 (~$1.8B) |
| Key failure mode | [[merton-model\|Diffusion]] assumption breaks — jump-to-default, recap, vol squeeze |
| Capacity constraint | Single-name [[credit-default-swap\|CDS]] liquidity (down ~70% post-Dodd-Frank) |

### The capital stack and what it implies

Every claim is a different slice of the same firm-value distribution; mispricing one against another is the trade:

| Claim | Merton interpretation | Sensitivity |
|---|---|---|
| Common equity | Call option on firm assets struck at debt face value | Long firm value + long asset vol |
| Preferred stock | Hybrid; senior to common, junior to debt | Dividend asymmetry, partial vol exposure |
| Senior / sub debt | Risk-free bond − put on firm assets | Short firm value tail, short credit |
| [[convertible-bond\|Convertible]] | Bond + equity call | Long vol; core of [[convertible-arbitrage]] |
| [[credit-default-swap\|CDS]] | Pure default-probability instrument | Short firm value tail |

## Edge Source

**Analytical** and **structural** (see [[edge-taxonomy]]).

| Edge | Where it comes from | Why it persists |
|---|---|---|
| **Analytical** | Practitioners who run structural credit models compute a "fair" CDS spread from equity price and [[implied-volatility]] (via [[creditgrades\|CreditGrades]] or a Merton variant) and take the other side when market spreads deviate materially. | The modeling, data plumbing, and cross-asset approvals are scarce |
| **Structural** | [[market-segmentation]]: equity-derivatives desks, HY bond PMs, CDS market-makers, and long-only equity managers price the same capital stack but rarely coordinate. | Mandate silos prevent the natural arbitrageurs from acting |

## Why This Edge Exists

- **Segmented investor bases.** Index-driven equity flows, mandate-constrained IG/HY bond funds, and banks hedging loan books each transact without reference to the other legs of the capital stack.
- **Model dispersion.** Credit desks use spread-based models; equity-vol desks use Black-Scholes on stock; a Merton view reconciles them but requires unusual data plumbing and approval to trade across silos.
- **Balance-sheet intermediation.** Dealers warehousing CDS inventory sometimes push spreads wider than equity vol justifies simply to offload risk before quarter-end; a hedge fund with patient capital earns the mean-reversion.
- **Who is on the other side?** Usually a dealer under [[regulatory-capital]] pressure, an ETF rebalancing into the equity, or a loan-portfolio hedger who is price-insensitive about CDS cost.

## Null Hypothesis

Under [[modigliani-miller]] with a single risk source, every claim on firm value moves deterministically with the asset value and its volatility. A random-no-edge world would show CDS-implied and equity-implied default probabilities cointegrated with zero mean reversion profit -- trades break even before costs. Any systematic P&L therefore reflects either a real risk premium (being paid to warehouse segmentation risk) or a temporary dislocation.

## Rules

**Entry.**
1. Screen the S&P 500 and HY universe daily. Compute Merton-implied CDS spread `s_merton` from equity price, equity vol surface, debt face value, and risk-free rate.
2. Identify names where `|s_market - s_merton| > 2 sigma` of the trailing 6-month residual, with absolute spread > 100 bps to make costs worthwhile.
3. Check that the dislocation is not explained by a known catalyst (pending [[merger-arbitrage|merger]], litigation, covenant event).

**Positioning.**
- **CDS rich vs equity**: sell CDS protection, short equity (or buy equity puts) in Merton-delta ratio.
- **CDS cheap vs equity**: buy CDS protection, buy equity or sell puts in Merton-delta ratio.
- **Preferred-vs-common dislocation**: long the cheap leg, short the rich leg, hedge dividend asymmetry with swaps.

**Exit.** Close when residual returns to within 0.5 sigma, at earnings if thesis is pre-earnings, or on stop-loss (below).

## Implementation Pseudocode

```python
for ticker in universe:
    S = equity_price(ticker)
    sigma_E = implied_vol_1y(ticker, strike=S)
    D = face_value_debt(ticker)  # from 10-Q, short-term + 0.5 * long-term
    r = risk_free_1y()
    # Solve Merton for asset value V and asset vol sigma_V
    V, sigma_V = merton_solve(S, sigma_E, D, r, T=1.0)
    pd_merton = merton_default_prob(V, sigma_V, D, r, T=5)
    s_merton = spread_from_pd(pd_merton, recovery=0.4)
    s_market = cds_5y_mid(ticker)
    residual = s_market - s_merton
    z = (residual - mean_6m(residual)) / std_6m(residual)
    if z > 2 and s_market > 100:
        short_cds(ticker, notional=N)
        short_equity(ticker, shares = N * merton_delta(V, D, sigma_V) / S)
    elif z < -2 and s_market > 100:
        long_cds(ticker, notional=N)
        long_equity(ticker, shares = N * merton_delta(V, D, sigma_V) / S)
```

## Indicators / Data Used

- [[merton-model]] / [[creditgrades]] structural models
- Daily CDS quotes (5Y senior unsecured) from Markit / IHS
- Equity [[implied-volatility]] surface (1Y ATM + skew)
- Capital structure from 10-Q: short-term debt, long-term debt, preferred, common
- Recovery assumption (typically 40% for senior unsecured)

## Example Trade

**Boaz Weinstein at Deutsche Bank, 2005-2007.** Weinstein's Credit Trading Group ran one of Wall Street's largest capital-structure books, reportedly generating >$1 bn of annual P&L by selling CDS protection on investment-grade names while shorting equity as a Merton hedge. The strategy was a core input into Deutsche Bank's 2008 losses: when equity vol spiked and CDS spreads blew out together, the short-equity hedge failed to keep pace with CDS losses because equity could not fall below zero while spreads could widen to the thousands. DB disclosed roughly **$1.8 bn of losses** attributed to Weinstein's desk in late 2008; he left in 2009 to found [[saba-capital]], which continued a version of the strategy with lower leverage.

**GM / Ford, May 2005.** After S&P cut GM and Ford to junk on 5 May 2005, CDS spreads widened sharply while Kirk Kerkorian's bid pushed GM equity up. Cap-structure funds that were short GM equity / long GM CDS (the "textbook" Merton trade) lost on both legs simultaneously, causing the first major industry-wide [[convertible-arbitrage]] and cap-structure unwind. Several funds including [[bailey-coates]] closed.

Worked episodes — why the Merton hedge failed:

| Episode | Position | What broke the model | Result |
|---|---|---|---|
| GM/Ford (May 2005) | Short equity / long CDS | Takeover bid lifted equity while downgrade widened CDS — legs moved *together* | Both legs lost; industry-wide unwind |
| Deutsche Bank / Weinstein (2008) | Sell CDS / short equity | Equity floored at zero while CDS widened to thousands | ~$1.8B disclosed loss |
| Parmalat (2003), Wirecard (2020) | Any Merton hedge | Jump-to-default / fraud — no diffusion warning | Hedge ratio meaningless |

The recurring lesson: the Merton delta assumes smooth diffusion. In recaps, fraud, and squeezes the two legs decouple or co-move adversely, which is the strategy's defining tail risk.

## Performance Characteristics

> **Data disclaimer:** the figures below are from peer-reviewed academic studies (Yu 2006; Duarte-Longstaff-Yu 2007) and realistic order-of-magnitude estimates, not a reproducible in-house backtest. Crucially, Yu (2006) showed the Merton-based strategy is profitable *on average* but carries severe negative skew — most names converge, a few blow up — so headline Sharpe understates the tail. Treat all numbers as illustrative.

| Metric | Range | Note |
|---|---|---|
| Gross residual spread | 50-300 bps stressed; 10-50 bps IG | The raw mispricing to harvest |
| Net Sharpe (2000-2020, Merton rules) | 0.5-1.2 pre-crisis; negative in 2008 | Yu 2006; Duarte-Longstaff-Yu 2007 |
| Drawdown (2008) | 30-50% peak-to-trough | 2020 COVID similar but shorter |
| Skew | Strongly negative | Convergence wins are small; blowups are large |

**Realistic cost overlay:** CDS bid-ask 5-15 bps for IG, 25-75 bps HY; equity financing 40-200 bps; [[slippage]] on delta rebalancing. The `breakeven_cost_bps: 40` in frontmatter reflects an IG-name round trip; HY and stressed names cost materially more, and rebalancing frequency compounds the drag.

## Capacity Limits

Strategy can absorb several billion dollars for a well-established desk (Saba, Citadel Credit, Blackrock Credit). Beyond that, single-name CDS liquidity -- which fell ~70% post-Dodd-Frank -- becomes binding. Index-vs-single-name variants (trading CDX vs components) extend capacity but reduce edge.

## What Kills This Strategy

- **Jump-to-default** without a corresponding equity move (fraud cases: Parmalat 2003, Wirecard 2020). The Merton hedge assumes diffusion dynamics; jumps break the delta.
- **Recapitalizations and LBOs** that change `D` abruptly -- CDS spreads blow out while equity rallies on takeout premium.
- **Dealer balance-sheet retreat**: during 2008 and again in March 2020, CDS bid-ask doubled and delta-hedging became prohibitively expensive.
- **Equity vol regime change** (e.g. the October 2008 Volkswagen squeeze; 2021 meme-stock squeezes on distressed names): the short-equity leg explodes. See [[failure-modes]].

## Kill Criteria

- Drawdown > 25% from high-water mark.
- 6-month rolling Sharpe < 0.
- Average bid-ask on CDS book > 2x historical (signals liquidity regime break).
- More than 3 jump-to-default events in trailing 12 months hitting positions on the wrong side.

## Advantages

| Advantage | Why it matters |
|---|---|
| Multiple profit sources | Carry, convergence, and gamma on the equity hedge |
| Lower directional exposure | Less net equity beta than long/short equity |
| Proprietary-model edge | Structural-credit modeling is a sustainable, defensible edge |
| Desk synergies | Natural complement to [[convertible-arbitrage]] and [[volatility-arbitrage]] books |

## Disadvantages

| Disadvantage | Why it matters |
|---|---|
| Extreme tail risk | Jump-to-default, recaps, and funding squeezes break the Merton hedge |
| Thinned CDS market | Single-name liquidity down ~70% post-Dodd-Frank; less capacity, wider costs |
| Heavy infrastructure | ISDA/CSA docs, clearing relationships, regulatory-capital allocation |
| Attribution ambiguity | Hard to separate model error from genuine mispricing |
| Negative skew | Many small wins, occasional large losses — psychologically and operationally taxing |

## Sources

- Yu, F. (2006). "How Profitable Is Capital Structure Arbitrage?" *Financial Analysts Journal*.
- Duarte, J., Longstaff, F., Yu, F. (2007). "Risk and Return in Fixed Income Arbitrage." *Review of Financial Studies*.
- Merton, R. (1974). "On the Pricing of Corporate Debt." *Journal of Finance*.
- Scott Patterson, *The Quants* (2010) -- Weinstein and Deutsche Bank chapters.
- Lisa Abramowicz, *Bloomberg*, "Saba's Weinstein on JPM Whale Trade" (2012).

## Related

- [[cds-bond-basis-arbitrage]]
- [[convertible-arbitrage]]
- [[convergence-arbitrage]]
- [[relative-value-arbitrage]]
- [[merton-model]]
- [[creditgrades]]
- [[credit-default-swap]]
- [[volatility-arbitrage]]
- [[merger-arbitrage]]
- [[saba-capital]]
- [[archegos]]
- [[limits-to-arbitrage]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[arbitrage]]
