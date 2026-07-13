---
title: "Stub Trading"
type: strategy
created: 2026-04-26
updated: 2026-06-10
status: good
tags: [arbitrage, stocks, event-driven]
aliases: ["Stub Equity Arbitrage", "Stub Arb", "Sum-of-Parts Stub Trade"]
related: ["[[risk-arbitrage]]", "[[corporate-action-arbitrage]]", "[[merger-arbitrage]]", "[[capital-structure-arbitrage]]"]
strategy_type: hybrid
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: untested
edge_source: [analytical, structural, risk-bearing]
edge_mechanism: "After a partial acquisition, spin-off, or carve-out, the residual 'stub' equity often trades at a structural discount to its sum-of-parts value because (1) the holder base churns, (2) liquidity collapses, and (3) coverage drops. Patient capital captures the discount as the stub re-rates over months-quarters."
data_required: [parent-subsidiary-equity-prices, spin-off-prospectus, holder-tracking, index-membership-data]
min_capital_usd: 1000000
capacity_usd: 200000000
crowding_risk: low
expected_sharpe: 1
expected_max_drawdown: 0.35
breakeven_cost_bps: 300
decay_evidence: "Spin-off mechanics well understood; Greenblatt and the event-driven fund community institutionalized the trade from the 1990s. Spreads still exist but are narrower."
---

# Stub Trading

Strategy targeting the **residual equity ("stub")** that remains after a partial acquisition, leveraged buyout with rump equity, spin-off, or holding-company carve-out. The stub typically trades at a 20-50% discount to its sum-of-parts (SOTP) value in the weeks-to-months following the corporate event because of holder-base churn, liquidity dry-up, analyst coverage gap, and forced index-fund selling. Popularised by Joel Greenblatt in *You Can Be a Stock Market Genius* (1997) and institutionalized by event-driven funds (e.g. Pentwater, Sachem Head) since the 2000s.

## Edge Source

**Analytical** + **structural** + **risk-bearing**.

- **Analytical:** Sum-of-parts valuation requires understanding the stub's standalone economics, which the prospectus usually describes incompletely.
- **Structural:** Index-fund forced selling on spin-off effective date is mechanical and predictable.
- **Risk-bearing:** Capital sits in an illiquid name for months waiting for re-rating.

## Why This Edge Exists

Three flow mechanics drive systematic discount:

1. **Forced-seller mechanics.** When ParentCo spins off SubCo, S&P 500 funds receive SubCo shares but cannot hold them (SubCo is too small, not in their index). They sell mechanically on/after the spin-off effective date — often $100M-$1B of supply hitting a thin order book.
2. **Holder churn.** Long-time ParentCo holders (often value/dividend-focused) inherit SubCo shares with different fundamentals. They sell — they didn't pick SubCo.
3. **Analyst coverage gap.** Sell-side analysts initially don't cover SubCo. Coverage takes 30-90 days to bootstrap. The information vacuum suppresses fair price discovery.

Counterparty: passive funds (forced sellers), indifferent retail (sells small lots), legacy ParentCo holders (churning out).

## Null Hypothesis

In an efficient market, ParentCo trading should reflect ParentCo + (its stake in SubCo, marked at the spin-off prospectus's implied valuation). Empirically, stubs trade at 20-50% discount to fair SOTP for weeks, narrowing over 90-180 days.

## Rules

1. Pre-spin: model the stub's standalone P&L, balance sheet, and SOTP value.
2. Watch for the spin-off effective date.
3. T+0 to T+30: monitor forced-seller flow; identify the discount bottom.
4. Buy stub at discount > 25% of fair SOTP.
5. Hedge ParentCo beta if needed (often not — different business).
6. Hold 6-18 months for re-rating.
7. Exit when discount narrows to <10% or when management catalyst lands.

## Implementation Pseudocode

```python
on spin_off_announcement(parent, sub_ratio):
    sub_value = model_sub_sotp(parent.10K, prospectus.S-1)
    parent_post_value = parent_pre_value - sub_value
    spin_date = prospectus.distribution_date
    on spin_date + 1:
        observed_sub_price = market.observed(sub.ticker)
        discount = (sub_value - observed_sub_price) / sub_value
        if discount > 0.25:
            buy_sub(target_size)
            hedge_parent_optional()
    on spin_date + 90 to + 180:
        if discount < 0.10 or catalyst_landed:
            exit()
```

## Indicators / Data Used

- Form 10 (spin-off prospectus).
- Form 8-K (corporate action announcement).
- Index methodology docs (S&P 500, Russell 1000 inclusion criteria).
- Holder concentration (13F).
- Sell-side coverage initiations (post-spin analyst kickoff).
- Pre-spin "when-issued" trading prices.

## Example Trades

**Marriott International / Marriott Vacations Worldwide (2011)** — Marriott spun off its timeshare unit Nov 2011. VAC traded at $20 effective date; sum-of-parts implied $32. Re-rated to $30+ within 12 months. ~50% return.

**eBay / PayPal (2015)** — eBay spun off PayPal July 2015. PayPal initially ~$36; rapidly re-rated to $40+ as sell-side coverage launched and growth premium recognized. eBay (the stub-of-the-spin) traded at depressed multiples for 18 months while market digested it as a value name.

**Liberty Media spin-offs (multiple)** — John Malone's Liberty Media has spun off Liberty Broadband, Liberty TripAdvisor, Liberty Sirius XM, etc. Each generated 6-18 month re-rating opportunities; institutional arbs (Greenblatt's old fund Gotham Capital made part of its career on Malone spins).

**ConocoPhillips / Phillips 66 (2012)** — Refining/midstream spin from upstream parent. Phillips 66 traded at $34 initial; 12 months later $63. Pure stub re-rating.

## Performance Characteristics

Greenblatt's *You Can Be a Stock Market Genius* claimed 50%+ annualized on selected spin-off trades 1985-1995 (small-fund era). Institutional desks 2010-2024 report 8-15% annualized on the strategy as a sub-allocation within event-driven portfolios. Sharpe 0.8-1.5; drawdowns concentrated when broader market falls (forced selling from passive funds intensifies in down markets).

## Capacity Limits

Bound by stub float ($100M-$5B typical). Per-event $5-100M position size. Annual: 30-60 spin-offs globally with arb-able discounts.

## What Kills This Strategy

- Pre-spin "when-issued" trading already prices the discount efficiently.
- Activist crowding (Starboard, Land & Buildings, Engine No.1 chase same setups).
- Reduced spin-off frequency (deal market preferences shift).
- Index-inclusion changes (S&P now sometimes adds spin-offs immediately, removing forced-selling).

## Kill Criteria

- Median post-spin discount across the opportunity set narrows below 10% (edge structurally gone).
- Three consecutive events closed at a loss, or strategy-level drawdown > 35% (matches expected_max_drawdown).
- Rolling 24-month return below T-bills + 200 bps.

## Advantages

- Mechanical edge from passive-flow structure.
- Multi-month holding window — no scramble.
- Decoupled from market beta.

## Disadvantages

- Capital lock-up.
- Illiquidity in the stub.
- Re-rating can take longer than expected.

## Sources

- Joel Greenblatt, *You Can Be a Stock Market Genius* (1997).
- Pat Dorsey, *The Five Rules for Successful Stock Investing* (2003) — spin-off framework.
- Penn State Smeal "Spin-Off Performance" academic studies.
- Edge Consulting Group spin-off coverage.

## Related

[[risk-arbitrage]] · [[corporate-action-arbitrage]] · [[merger-arbitrage]] · [[capital-structure-arbitrage]] · [[index-arbitrage]] · [[structural-forced-selling]]
