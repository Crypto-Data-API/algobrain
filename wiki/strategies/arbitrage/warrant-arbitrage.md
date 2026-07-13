---
title: "Warrant Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, options, derivatives, history, volatility]
aliases: ["Warrant Arb", "Covered Warrant Arbitrage", "Warrant-Stock Arbitrage"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, options]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, behavioral, analytical]
edge_mechanism: "Warrants are long-dated call-like instruments issued by companies or third parties, and they frequently misprice versus their theoretical Black-Scholes value because of retail speculation, illiquidity, dilution confusion, and structural demand imbalances; arbitrageurs profit by hedging warrants against the underlying and letting mispricing converge."
data_required: [warrant-terms, options-chain, equity-borrow-rates, dilution-schedule, implied-vol-surface]
min_capital_usd: 50000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 0.8
expected_max_drawdown: 0.15
breakeven_cost_bps: 50
decay_evidence: "SPAC-warrant boom 2020-2021 closed out when bubble deflated; Chinese warrant market 2005-2008 ended after regulators stopped new issuance (last warrant expired Aug 2011). Persistent opportunity in Hong Kong and Europe via covered warrants."
related: ["[[arbitrage]]", "[[convertible-arbitrage]]", "[[spac-arbitrage]]", "[[volatility-arbitrage]]", "[[options-strategies]]", "[[put-call-parity-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[dilution]]"]
---

# Warrant Arbitrage

A **[[warrant]]** is a financial instrument that gives the holder the right (but not the obligation) to buy shares of a company at a specified strike price before expiration -- economically similar to a long-dated call option, but typically **issued by the company itself** (causing [[dilution]] on exercise) or by a third-party investment bank (a "covered warrant"). Warrants differ from listed options in tenor (often 3-10 years), issuer (company vs exchange), liquidity profile, and -- critically -- the tendency to trade far from theoretical value due to retail speculation and structural demand. **Warrant arbitrage** is the strategy of hedging warrants against the underlying stock (or its options) to profit from convergence of warrant price to fair value. It is a member of the broader [[arbitrage]] family and a close cousin of [[convergence-arbitrage]], [[volatility-arbitrage]], and [[convertible-arbitrage]] — all of which rely on a model-implied "fair value" that the market is expected to converge toward, and all of which are bounded by the [[limits-to-arbitrage]].

Landmark episodes include: **Japanese warrant bubble of 1987-1989**, where European investment banks (UBS Warburg, Nomura International) made fortunes issuing and arbitraging Japanese equity warrants against Nikkei futures and underlying shares; **Chinese warrant market of 2005-2008**, a pure retail speculative mania where massively out-of-the-money warrants traded at prices wildly above any defensible fundamental value -- a textbook bubble that ended when regulators stopped approving new issues (the last warrant expired in August 2011); **SPAC warrant boom 2020-2021**, where virtually every de-SPAC'd company offered public warrants at $11.50 strike with 5-year tenors that initially traded at $2-5 but collapsed to pennies post-de-SPAC for the vast majority. Each episode illustrates a different form of structural edge and its eventual compression.

### Warrant vs listed option: key differences

The whole strategy rests on the fact that a warrant and a listed option can reference the *same underlying, same strike, same expiry* yet price differently. The table below summarises why.

| Dimension | Company/covered warrant | Exchange-listed option |
|-----------|-------------------------|------------------------|
| Issuer | The company (dilutive) or an investment bank (covered, non-dilutive) | The options exchange / OCC clearing |
| Typical tenor | 3-10 years | Days to ~3 years (LEAPS) |
| Dilution on exercise | Yes for company warrants — new shares created | No — settled against existing shares |
| Standardisation | Idiosyncratic (ratchets, redemption triggers, cashless exercise) | Fully standardised contract terms |
| Liquidity | Often thin; bid-ask frequently > 5% | Generally deep at liquid strikes |
| Marginal buyer | Retail "cheap leverage" speculators | Mix of retail, dealers, institutions |
| Shortability | Often hard or impossible to short | Freely writable |
| Fair-value anchor | The listed-option [[implied-volatility]] surface | The market itself |

The dilution column is the analytically load-bearing one: a correctly **dilution-adjusted** warrant value (Black-Scholes scaled for the new-share creation) is materially below the naive Black-Scholes value when the warrant overhang is large relative to shares outstanding. Desks that skip the dilution adjustment systematically over-value warrants and put on the wrong-signed hedge.

## Edge Source

**Structural**, **behavioral**, and **analytical**. Structural: warrants have idiosyncratic terms (cashless exercise, dilution, ratchet clauses, forced conversion triggers) that create gaps between warrant and listed-option pricing. Behavioral: retail speculators bid warrants to irrational premiums, especially in lottery-ticket regimes. Analytical: correctly modeling dilution, early-redemption provisions, and [[volatility]] term structure across 3-5 year tenors is non-trivial and rewards desks that do it well. See [[edge-taxonomy]].

| Edge component | Category | Source of the gap | Who pays it |
|----------------|----------|-------------------|-------------|
| Idiosyncratic terms | Structural | Redemption triggers, dilution, ratchets not in listed options | Anyone using a naive option model |
| Retail premium / discount | Behavioral | Lottery-ticket demand in manias; capitulation in busts | Late retail buyers / panic sellers |
| Dilution-adjustment skill | Analytical | Fully-diluted share count, anti-dilution clauses | Desks that mis-model fair value |
| Borrow / hedge friction | Structural | Hard-to-borrow underlying breaks the hedge | Whoever must short to hedge |

The cleanest cases combine all three: a mania (behavioral) generates the gross premium, idiosyncratic terms (structural) keep listed-option arbs from trivially closing it, and a dilution-aware model (analytical) tells you which side is actually rich.

## Why This Edge Exists

Warrants are marketed to retail investors ("get levered exposure to the stock!") who often do not understand that a 5-year call option can lose 90% of its value even if the underlying appreciates modestly. Retail bids warrants above fair value in bullish regimes and dumps them below fair value in bearish regimes, while company insiders frequently sell warrants in the aftermarket via rule 144 or S-1 registrations. The counterparty to the arb is therefore the retail speculator on one side of the cycle and the insider or institutional seller on the other. Listed options on the same underlying, where they exist, anchor the true fair value. See [[behavioral-finance]].

## Null Hypothesis

Under efficient-markets conditions, warrant prices equal their Black-Scholes-with-dilution value computed from the listed-options implied-volatility surface at the same expiry and strike. The null outcome: any apparent spread between warrant market price and model value equals the round-trip transaction cost plus the borrow rate on the underlying times the warrant delta exposure. Any positive alpha from static arbitrage should be arbitraged away by market makers within seconds.

## Rules

### Entry

1. **Screen warrant market** for warrants where warrant-implied volatility differs from listed-option implied volatility at the same expiry/strike by more than 300 bps.
2. **Model the warrant correctly** including dilution, cashless-exercise provisions, redemption triggers (e.g., SPAC warrants often have "redeem if stock > $18 for 20 of 30 trading days" clauses), anti-dilution adjustments.
3. **Check liquidity**: only trade warrants with daily volume > $500K and bid-ask < 5%.
4. **Confirm borrow availability** on the underlying -- the hedge requires shorting stock in proportion to warrant delta.
5. **Enter long-warrant / short-stock** when warrant is cheap; **short-warrant / long-stock** when warrant is rich. For retail-issued warrants, shorting can be difficult/impossible.
6. **Delta hedge dynamically** as the stock moves; warrant delta changes with spot level.

### Exit

1. **Warrant-to-model spread closes** below the entry threshold net of costs
2. **Warrant approaches expiration** and delta converges on intrinsic
3. **Forced redemption triggered** by stock clearing the redemption threshold (common in SPAC warrants) -- warrants become $11.50 calls with 30-day expiry
4. **Credit event** on issuer invalidates thesis (warrant value depends on company solvency for cash exercise; issuer bankruptcy often voids warrants)

### Position Sizing

Size by (a) gamma budget -- how much delta re-hedging cost can be tolerated, (b) warrant market liquidity, and (c) concentration in a single name. A typical trade: $500K-5M per single-name warrant arb, diversified across 10-30 names.

## Implementation Pseudocode

```python
def warrant_arb_scan(warrants):
    trades = []
    for w in warrants:
        if not w.listed_options_exist: continue
        listed_iv = implied_vol_surface(w.underlying, w.strike, w.expiry)
        warrant_iv = imply_vol_from_warrant_price(
            price=w.mid_price,
            spot=w.underlying.spot,
            strike=w.strike,
            expiry=w.expiry,
            dividends=w.underlying.dividend_pv,
            borrow=w.underlying.borrow_rate,
            dilution_factor=w.new_shares / w.old_shares_outstanding,
            redemption_trigger=w.redemption_rule
        )
        spread = warrant_iv - listed_iv
        if abs(spread) > 0.03:  # 300 bps
            direction = "short_warrant_long_stock" if spread > 0 else "long_warrant_short_stock"
            delta = warrant_delta(w, spot=w.underlying.spot)
            trades.append({
                "warrant": w, "direction": direction,
                "warrant_size": size, "stock_hedge": size * delta,
                "expected_convergence_bps": abs(spread) * 100
            })
    return trades
```

## Indicators / Data Used

- Warrant prospectus: strike, expiry, ratio, cashless-exercise, redemption triggers, anti-dilution clauses
- Listed-option [[implied-volatility]] surface for the same underlying at the warrant's expiry/strike
- Dilution math: fully-diluted share count including warrant exercise
- Equity borrow rate on the underlying (critical for the hedge)
- Warrant and underlying intraday bid-ask, volume, and open-interest
- [[gamma]] and [[vega]] exposures across the portfolio

## Example Trade

### SPAC Warrant Arb, 2021

The 2021 SPAC wave saw hundreds of companies go public via SPAC mergers, each leaving behind public warrants. A typical structure: $11.50 strike, 5-year expiry, redeemable by company if stock trades above $18.00 for 20 of 30 consecutive days. Listed options on the same company trade at an implied-vol surface typically 5-15 vols **below** the warrant-implied vol, because retail piled into warrants as cheap leverage.

- **Example case** (illustrative reconstruction using approximate mid-2021 prices): Clover Health (CLOV), de-SPAC'd January 2021. Post-merger, public warrants (CLOV.WS) traded around $4.50 in June 2021 when stock was ~$11. Listed 2-year LEAPS at $11 strike implied ~90 vol; warrant implied ~115 vol -- 2500 bps rich.
- **Trade**: short 10,000 CLOV warrants at $4.50 ($45,000 credit), long ~4,500 CLOV shares (warrant delta ~0.45) at $11 ($49,500 debit). Net debit $4,500.
- **Thesis**: warrant IV converges to listed IV as hype fades and retail exits.
- **Result (late 2021)**: CLOV fell to $4, warrants to $0.40. Short warrants gained: ($4.50 - $0.40) * 10,000 = **$41,000**. Long shares lost: ($11 - $4) * 4,500 = -$31,500. Delta rehedging over 6 months recovered ~$8,000. **Net P&L ~$17,500 on $4,500 initial net capital over 6 months.**
- Note: the dramatic stock fall helped the short-warrant leg disproportionately because vega compressed on a big move.

### Chinese Warrant Bubble, 2007

In 2005-2008, Chinese retail speculators bid exchange-listed warrants (权证) to spectacular premiums. The canonical cases documented by Xiong and Yu (2011) are the **deep out-of-the-money put warrants** -- e.g., the WuLiangYe put warrant -- which traded at substantial prices (at times over 1 RMB, with frenzied intraday turnover) even when their Black-Scholes value was essentially zero because the underlying had risen so far above the strike that exercise was near-impossible. Outside investors could not short A-share warrants, so the main arbitrage channel was the regulator-sanctioned **creation mechanism**: qualified domestic securities firms could mint new put warrants (notably the China Southern Airlines puts in 2007-2008) and sell them into retail demand, earning billions of RMB in near-riskless profit as the warrants expired worthless. The CSRC stopped approving new warrants after 2008, and the market ended when the last warrant expired in August 2011.

### Japanese Warrant Bubble, 1987-1989

European investment banks structured and issued equity warrants on Japanese blue-chips to investors worldwide, delta-hedging against Nikkei futures. Profits were astronomical; Nomura International's London warrant desk is legendary. The game ended with the 1990 Nikkei collapse.

## Performance Characteristics

> **No fabricated backtest.** The figures below are qualitative practitioner ranges and regime descriptions, not a verified return series. The arithmetic in the worked examples is illustrative reconstruction using approximate historical prices, not audited P&L.

The economics are dominated by the **gross IV spread minus carry**. Gross edge is the warrant-vs-listed IV gap; against it you pay the round-trip transaction cost (often large because warrant bid-ask can exceed 5%), the borrow on the short-stock hedge, and the path-dependent cost of delta re-hedging (the gamma bill). Only the residual is realised alpha.

| Cost / friction | Typical magnitude | Notes |
|-----------------|-------------------|-------|
| Warrant bid-ask | 1-5%+ of price | The single biggest drag; wide in illiquid names |
| Underlying borrow | 0.5-50%+ annualised | Meme / post-de-SPAC names can be punitively hard-to-borrow |
| Delta re-hedge (gamma) | variable | Scales with realised vol of the underlying |
| Listed-option hedge cost | listed bid-ask | If hedging with options rather than stock |
| `breakeven_cost_bps` | ~50 (frontmatter) | Round-trip cost the edge must clear |

- **Hit rate (qualitative)**: high in bubble regimes where retail is bidding warrants richly; much lower in normal regimes.
- **Return per trade (illustrative)**: on the order of 100-500 bps of capital deployed, held 1-9 months — before the costs above.
- **Volatility**: moderate -- delta hedging compresses directional risk, but vega and gamma exposure create meaningful drawdowns during vol shocks.
- **Best conditions**: retail speculative manias (2020-2021 SPACs, 2005-2008 China, 1987-1989 Japan), new-issue waves with standardized warrant structures.
- **Worst conditions**: quiet markets with no new warrant issuance; warrant markets dominated by professional market-making, where the gap is already arbitraged away (the [[limits-to-arbitrage]] no longer bind).

## Capacity Limits

Capacity depends on the specific market. Global SPAC-warrant arb in 2020-2021 absorbed $5-10B across the industry. Single-name capacity is typically $10-50M for major warrants. Chinese warrants at their peak had daily volume in the tens of billions of yuan; arb capacity was multi-billion before the shutdown.

| Market / regime | Approx. arb capacity | Binding constraint |
|-----------------|----------------------|--------------------|
| Single major warrant | $10-50M | Warrant liquidity + underlying borrow |
| Global SPAC-warrant wave (2020-21) | $5-10B industry-wide | Borrow on thin de-SPAC floats |
| Chinese warrant market (2005-08) | Multi-billion RMB (creation channel) | Regulatory issuance approval |
| HKEX / European covered warrants (today) | Moderate, persistent | Dealer market-making compresses gap |

The `capacity_usd: 500000000` in frontmatter is a strategy-level figure across a diversified book during an active issuance wave; in a quiet regime real deployable capacity is a small fraction of that.

## What Kills This Strategy

1. **Hard-to-borrow underlying**: if the short-stock hedge leg is unavailable, the trade cannot be put on. Common in meme stocks and post-de-SPAC names where floats are thin.
2. **Forced warrant redemption** at awkward times, compressing the warrant to $0 intrinsic value and ending the trade earlier than expected. Neutral P&L but ends opportunity.
3. **Issuer bankruptcy**: warrants typically become worthless immediately. Short-warrant leg wins, but if net delta is positive, the long-stock hedge is simultaneously wiped out. Asymmetric downside.
4. **Retail mania intensifying**: a short-warrant position can be squeezed higher for months (SPAC warrants 2021 H1) before reverting, causing margin pressure.
5. **Regulatory action**: the CSRC stopped approving new Chinese warrants after 2008 and the market wound down by 2011. SEC changes to SPAC-warrant accounting in April 2021 caused sharp repricings.
6. **Model error on dilution** or redemption triggers: if you miscompute the fully-diluted share count, the hedge ratio is wrong.

See [[failure-modes]].

## Kill Criteria

- Warrant-to-listed-option IV spread collapses below 150 bps across the universe (edge compressed)
- Three consecutive single-name trades with drawdowns > 2x expected P&L
- Regulatory announcement altering warrant tax or accounting treatment
- Prime broker pulls short-stock locates on >50% of portfolio

## Advantages

- Vega-rich arb that profits from IV convergence across different instrument types on the same underlying
- Bubble episodes (SPACs, China) provide spectacular risk-reward setups
- Less competitive than standard listed-options volatility arbitrage because warrants require idiosyncratic modeling
- Delta-hedged construction is broadly market-neutral
- Capacity is meaningful during issuance waves

## Disadvantages

- Requires deep understanding of warrant terms; one overlooked redemption clause can make the trade unprofitable
- Short-warrant positions can be squeezed during manias; staying power required
- Borrow availability on underlying is a persistent risk
- Illiquid warrant markets mean entry and exit can be costly; bid-ask > 5% is common
- Regulatory risk: regulators have ended or repriced warrant markets multiple times (China 2008-2011, SEC SPAC-warrant accounting 2021)
- Delta-hedging costs consume a meaningful fraction of gross edge

## Sources

- Xiong, W. and Yu, J. (2011), *The Chinese Warrant Bubble*, American Economic Review 101(6) — definitive study of the 2005-2008 mania, including the deep-OTM put warrants trading far above fundamental value
- SEC Staff Statement on Accounting and Reporting Considerations for Warrants Issued by SPACs (April 12, 2021) — triggered industry-wide SPAC-warrant restatements and repricings
- Taleb, N., *Dynamic Hedging* (1997) — practitioner treatment of hedging long-dated optionality and warrant books
- Hong Kong Exchanges (HKEX) covered-warrant / structured-products market statistics — the largest surviving listed-warrant market
- No ingested wiki source pages yet; the above are external references.

## Related

- [[arbitrage]] -- parent concept
- [[convergence-arbitrage]] -- the general "model fair value converges" family this belongs to
- [[convertible-arbitrage]] -- related embedded-option arb
- [[spac-arbitrage]] -- the cash-leg cousin of the SPAC warrant trade
- [[volatility-arbitrage]] -- closely related IV-convergence strategy
- [[warrant]] -- the instrument itself
- [[options-strategies]] -- broader options context
- [[put-call-parity-arbitrage]] -- uses similar four-leg hedging logic
- [[dilution]] -- critical concept for warrant valuation
- [[implied-volatility]] -- the fair-value anchor
- [[limits-to-arbitrage]] -- why the gap persists and sometimes widens
- [[chinese-warrant-bubble]] -- historical mania
- [[japanese-warrant-bubble]] -- historical mania
- [[edge-taxonomy]], [[failure-modes]] -- methodology
