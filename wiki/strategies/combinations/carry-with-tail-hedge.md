---
title: "Carry with Tail Hedge"
type: strategy
created: 2026-07-18
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, funding-rate, arbitrage, derivatives, risk-management, tail-risk, market-neutral, quantitative, crypto]
aliases: ["Hedged Carry", "Tail-Hedged Funding Carry", "Carry Book with Convexity", "Funded Tail Protection"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, behavioral, risk-bearing]
edge_mechanism: "The carry book earns contractual funding income by being the hedge that leveraged perp longs need; the tail-hedge overlay — sized as a fixed fraction (10-25%) of expected carry income — reprices the negative-skew tail explicitly rather than leaving it as an uncompensated risk, so the combined book earns carry net of the tail-insurance cost and survives the occasional crash that would otherwise wipe the carry profits."

data_required: [funding-rates, perp-price, spot-price, open-interest, options-iv, implied-vol-surface, mark-price, funding-history-7d]
min_capital_usd: 25000
capacity_usd: 20000000
crowding_risk: high

expected_sharpe: 1.2
expected_max_drawdown: 0.10
breakeven_cost_bps: 20

decay_evidence: "Funding carry has compressed from ~40%+ APY (2021) to ~5-15% APY (2025) as Ethena/Resolv/Pendle industrialised the trade. This directly compresses the hedge budget: at 10% carry, a 25% hedge budget = 2.5% APY spent on protection, leaving 7.5% net — tighter than the 2021 economics but still potentially viable if options are cheap relative to realised tail frequency."

kill_criteria: |
  - carry book drawdown > 10% (net of hedge P&L) in rolling 30 days
  - expected carry (7d average funding) falls below hedge budget cost: annualised 7d funding × capital < hedge premium paid per year → negative carry net of hedge
  - options IV on chosen instruments > 3× 30-day realized vol (hedge is too expensive relative to actual tail risk)
  - 7-day funding average turns negative on > 50% of held carry positions
  - exchange insurance-fund socialised loss event on any carry venue

related: ["[[funding-rate-arbitrage]]", "[[delta-neutral-yield-farming]]", "[[convex-tail-hedge-arbitrage]]", "[[trend-plus-tail-hedge]]", "[[tail-risk-hedging]]", "[[5-percent-otm-put-overlay]]", "[[cash-and-carry]]", "[[basis-trading]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[delta-neutral]]", "[[options]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Carry with Tail Hedge

Carry with tail hedge is a [[funding-rate-arbitrage|carry book]] (short perp / long spot, collecting positive funding) combined with a budgeted **out-of-the-money convex overlay** — typically OTM puts on BTC/ETH or long positions in crypto volatility instruments — where the hedge premium is sized as a fixed percentage (10-25%) of the *expected annual carry income* from the book. The core carry book earns the contractual funding transfer paid by leveraged longs; the tail overlay reprices the book's negative-skew tail (funding inversion, basis blowup, exchange failure, cascading liquidation) at a known annual cost rather than leaving those tails as uncompensated exposures.

**How this differs from related strategies:**

- **[[funding-rate-arbitrage]]** — the plain carry trade, no tail overlay. This page adds the hedge and the budget discipline for sizing it.
- **[[trend-plus-tail-hedge]]** — trend-following CTA (diversified futures, long biased) plus tail options. This page is a *carry book* (delta-neutral), not a trend book; the tail hedge is carry-income-financed rather than separate.
- **[[convex-tail-hedge-arbitrage]]** — pure tail-buying during cheap-vol regimes; no carry book. This page uses carry income to *fund* the tail-buying, making the combination self-financing.
- **[[delta-neutral-yield-farming]]** — carry on a staking yield base. This page uses plain spot (no staking yield); the carry funding rate is the sole yield leg.

## Edge source

Per [[edge-taxonomy]], this is a **structural + behavioral + risk-bearing** triple:

- **Structural** — the funding mechanism contractually transfers cash from perp longs to shorts when the perp trades above index. As long as leveraged retail bids perps above spot, the carry book collects. This is the same hard-coded cash-flow as [[funding-rate-arbitrage]].
- **Behavioral** — the tail is paid for by the same retail participants who create the funding premium: their overconfidence and leverage preference fund both the carry (positive funding) *and* the deep crashes (liquidation cascades, exchange failures) that make tail protection valuable. In a sense, the longs are funding their own potential crash insurance.
- **Risk-bearing** — the carry book is paid to bear risks others will not: exchange counterparty risk, oracle divergence, basis blowup. The tail overlay reprices part of that compensation from an uncompensated bear-tail bet into a *financed* protection position. The combined book earns *structured* risk-bearing income: carry minus insurance cost.

## Why this edge exists

**The fundamental inefficiency:** Carry books earn a positive expected value *and* have negative skew — small reliable gains offset by infrequent large losses. The negative-skew component is the premium-in-disguise: the carry book is implicitly selling crash insurance (by staying deployed in periods of high crash risk) and collecting the insurance premium as funding income. The problem is that most carry operators either (a) do not recognize this insurance sale or (b) recognize it but are forced to close at the worst time (during a crash) because they have no explicit hedge.

The tail overlay makes the implicit insurance sale *explicit*: the operator spends a portion of the insurance premium (carry income) to buy *formal* insurance (OTM puts or long vol). The net position earns carry minus hedge cost, with the tail risk bounded and quantified.

**Who finances the hedge:** the same leveraged longs who pay funding also, in aggregate, create the demand for the underlying crypto's volatility — their leverage and momentum-chasing behavior increases realized volatility, which is precisely what makes OTM puts valuable. There is a structural coherence to using carry income (from longs) to pay for crash protection (against the same longs' leveraged behavior).

## Null hypothesis

Under the null, the tail overlay has zero NPV: the options premium paid equals the expected payout exactly (options are fairly priced), so the hedge neither adds nor subtracts value in expectation. The combined strategy earns exactly the carry yield net of the fair-value hedge cost. If this is true, the hedge is still useful as a *variance-reduction* tool — it converts a high-Sharpe, negative-skew, occasionally blown-up strategy into a lower-variance, lower-max-drawdown profile — but there is no *additional* return from the hedge itself.

The null is rejected (hedge is *underpriced*) when: options implied volatility is systematically below realized volatility in the tails; or when carry-induced crashes are correlated with option-payoff-positive events in a way the options market has not priced. The null is *accepted* or *exceeded* (hedge is overpriced) when: options IV is high relative to realized vol, and tail events are infrequent.

Practical implication: the hedge budget (10-25% of carry) is the *maximum* justifiable spend. If options IV is depressed (post-crash complacency), increase the hedge budget toward 25%. If IV is elevated, cut toward 10% or skip hedging until IV normalises.

## Rules

### Carry book construction

Follow [[funding-rate-arbitrage]] rules exactly:
1. Entry: 8h funding ≥ 0.03% (~33% APY), 7d average positive, OI healthy.
2. Exit: funding < 0.01%, 7d average negative, or oracle divergence > 100 bps.
3. Sizing: 1× leverage on perp short (isolated), per-asset cap 25% of sleeve.
4. Concurrent: maximum 3 positions.

### Tail hedge construction

1. **Annual hedge budget.** Compute expected annual carry income: `expected_carry = avg_7d_funding × 3 × 365 × deployed_capital`. Set hedge budget = **15%** of expected carry as the base case; range 10-25% depending on current options IV vs realized vol.
2. **Instrument selection.** Preferred: OTM puts on BTC or ETH on Deribit with **delta ≤ −0.15** (deep OTM). Strike: approximately **20-30% below current spot**. Tenor: **1-3 months**; roll before expiry. Alternatively, if options are unavailable or illiquid, use a small long position in DVOL (Deribit Volatility Index) perpetuals or BTC/ETH long-vol instruments.
3. **Sizing the hedge.** Spend no more than the budget: notional of puts = `hedge_budget_usd`. For example, at $50,000 deployed in carry earning 10% APY = $5,000/year, hedge budget = $750/year (15%). Buy puts costing $750/year premium.
4. **Hedge allocation logic.** Allocate hedge positions to BTC and ETH in proportion to the carry book's underlying exposure. If 60% of carry is in BTC assets, 60% of hedge budget goes to BTC puts.
5. **IV gate.** Only purchase hedge if 30-day ATM implied vol < **1.5× 30-day realized vol**. If options are priced above 1.5× realized vol, the hedge is expensive relative to actual crash frequency; skip or reduce budget to 10%.
6. **Roll policy.** Roll 1 week before expiry to avoid theta-cliff and liquidity collapse near expiry.

### Combined portfolio exit / adjustment conditions

1. **Carry exit conditions** as per [[funding-rate-arbitrage]] (funding compression, regime flip).
2. **Hedge exercise**: if a put strikes in-the-money (crypto price falls 20%+ from entry), the put payoff partially or fully offsets carry-book losses. The carry-book positions themselves are closed on their own exit rules, not on hedge exercise.
3. **Hedge budget recalculation**: re-compute every 30 days based on the trailing 7d funding average.

### Position sizing

- Carry book: per [[funding-rate-arbitrage]]. Sleeve = total capital allocated to this combination strategy.
- Tail hedge: sized in USD premium, not notional. Premium ≤ 15% of expected carry income.
- Never use leverage on the options (long vol position is bounded by premium paid; cannot exceed loss of premium).

## Implementation pseudocode

```python
# carry_with_tail_hedge.py — budget manager for the combined position
from dataclasses import dataclass

# ---- carry parameters (from funding_arb.py) ----
ENTRY_8H_THRESHOLD = 0.0003     # 0.03% / 8h
EXIT_8H_THRESHOLD  = 0.0001     # 0.01% / 8h
MAX_PER_ASSET      = 0.25
DRAWDOWN_KILL      = 0.10

# ---- hedge parameters ----
HEDGE_BUDGET_BASE  = 0.15       # 15% of expected carry income
HEDGE_BUDGET_MIN   = 0.10
HEDGE_BUDGET_MAX   = 0.25
IV_TO_RV_MAX       = 1.5        # skip hedge if IV/RV > 1.5
DELTA_TARGET       = -0.15      # OTM puts, delta ~ -0.15
PUT_TENOR_DAYS     = 60         # approx 2-month expiry target

@dataclass
class HedgeState:
    current_puts_notional: float    # total puts notional held
    current_puts_cost_ytd: float    # USD premium spent this year
    expected_carry_annual: float    # projected annual carry income
    atm_iv_30d: float
    realized_vol_30d: float

def hedge_budget(h: HedgeState) -> float:
    iv_rv_ratio = h.atm_iv_30d / max(h.realized_vol_30d, 0.001)
    if iv_rv_ratio > IV_TO_RV_MAX:
        return HEDGE_BUDGET_MIN
    # scale budget inversely with IV/RV: cheap vol = max budget
    budget_pct = HEDGE_BUDGET_MAX - (HEDGE_BUDGET_MAX - HEDGE_BUDGET_MIN) * (iv_rv_ratio - 1.0) / (IV_TO_RV_MAX - 1.0)
    return max(HEDGE_BUDGET_MIN, min(HEDGE_BUDGET_MAX, budget_pct))

def hedge_action(h: HedgeState, carry_book_capital: float) -> dict:
    budget = hedge_budget(h)
    target_premium = h.expected_carry_annual * budget
    remaining = target_premium - h.current_puts_cost_ytd
    if remaining <= 0:
        return {"action": "NO_HEDGE", "reason": "annual budget exhausted"}
    return {
        "action": "BUY_PUTS",
        "target_delta": DELTA_TARGET,
        "tenor_days": PUT_TENOR_DAYS,
        "max_premium_usd": remaining,
        "note": f"budget={budget:.0%} of ${h.expected_carry_annual:.0f} carry; IV/RV={h.atm_iv_30d/h.realized_vol_30d:.2f}",
    }
```

The production system adds: Deribit options data feed for IV surface; daily budget recalculation; put-roll scheduler; and the carry-book loop from [[funding-rate-arbitrage]].

## Indicators / data used

- **[[funding-rate]] (8h)** — primary carry signal and budget-calculation input
- **OTM options IV (30d)** — hedge cost and IV-gate check
- **30-day realized volatility** — denominator for the IV/RV hedge-sizing gate
- **[[open-interest]]** — carry-book OI gate
- **Mark price / index price** — oracle-divergence guard on carry book
- **Options max pain / expiry OI** — roll timing for puts (optional; avoids expiry-pinning periods)

## Example trade

**Setup (illustrative):**

- Carry book: $50,000 deployed, 3 positions (BTC, ETH, SOL perp shorts + spot longs).
- 7d average funding: +0.025%/8h = ~27% APY.
- Expected annual carry income: 27% × $50,000 = **$13,500**.
- Hedge budget (15%): $13,500 × 0.15 = **$2,025/year** = $169/month.
- Current BTC 30d ATM IV = 55%; 30d realized vol = 42%. IV/RV = 1.31 < 1.5 → hedge eligible.
- Buy BTC 2-month OTM put (delta −0.13, strike ~$70,000 vs spot $85,000). Premium = $1,200 for position covering $50,000 notional. Monthly cost = $600.
- Remaining budget for ETH put: $169 − $600... budget is being consumed fast; in practice the hedge budget scales with the actual carry income and covers a smaller fraction of downside rather than full-book coverage. For a 2-month put at $1,200 on one leg, the first 1.2 months' hedge budget is consumed; the residual is cash.

**Scenario A: calm month.** Funding averages 0.025%/8h. Carry income: $13,500/12 = $1,125. Put expires worthless (BTC did not fall 17%+). Net: $1,125 − $600 put cost = **+$525**. Annualised net yield: ~12.6% on $50,000. The hedge cost $600 = 5.3% of monthly gross carry. Max drawdown the hedge prevented: in theory a 40% BTC crash would have blown the carry book; puts would have offset $5-10k of that.

**Scenario B: crash month.** Funding spikes to −0.05%/8h (carry book exit triggered on 7d avg negative); carry positions closed. BTC falls 35%. OTM put (delta −0.13 at $70k strike) is now deep ITM ($55k spot vs $70k strike): payout ≈ ($70k − $55k) × notional/price × contract size ≈ **$8,750 gross payout**. Net: carry loss ≈ −$1,500 (positions closed 2 days into the crash on 7d avg trigger) + put payout $8,750 − put cost $600 = **+$6,650 in crash month** — the combined book profits from the tail event instead of suffering it.

*(Illustrative. Actual put payouts depend on exercise mechanics, liquidity at expiry, and timing.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Net APY (carry − hedge cost) | 6-18% | Was 30%+ in 2021; current regime 8-15% carry with 15% hedge budget leaves ~7-13% net |
| Expected Sharpe | ~1.2 | Higher than unhedged carry (~1.4) for some regimes due to drawdown reduction |
| Max drawdown (combined) | ~10% | Carry book tail risk explicitly bounded; residual from basis/oracle events |
| Breakeven cost budget | 20 bps | Tighter than unhedged carry (12 bps) because hedge cost adds to breakeven |
| Annual hedge budget | 10-25% of carry | Adjusts with IV/RV ratio |
| Put payoff probability | ~5-15% per year | Deep OTM put; most years pay nothing, 1 in 5-10 years pay multi-bagger |

**The expected Sharpe trade-off:** in a carry-only world with no tail events, hedge costs drag Sharpe from ~1.4 to ~1.2 (for 15% hedge budget). Over long periods with occasional crashes (2022, 2025-10-10 style events), the hedge improves risk-adjusted returns because it prevents the event that would otherwise eliminate the strategy entirely. The value is in the *left-tail truncation*, not in expected return improvement.

## Capacity limits

Bounded by:
1. **Carry book capacity**: ~$5M per asset per venue (see [[funding-rate-arbitrage]]).
2. **Options liquidity**: deep OTM crypto puts with >$10M notional face wide bid-ask spreads on Deribit. The hedge becomes expensive at scale, compressing net carry. Practical hedge capacity: ~$5-20M notional before liquidity-premium costs exceed the budget benefit.
3. **Aggregate**: the combined strategy's capacity is set by the smaller of carry capacity and options liquidity, approximately **$5-20M** at reasonable hedge costs.

## What kills this strategy

1. **Carry compression without IV compression (#4).** If funding falls toward zero (as post-Ethena trend), the hedge budget shrinks but options may remain expensive. Net carry can go negative (hedge cost > carry income). The kill criterion "expected carry < hedge premium" directly addresses this.
2. **Options market too expensive (#5).** If the IV/RV ratio stays above 1.5 persistently (post-crisis, elevated fear), the hedge gate blocks purchasing. The strategy runs as pure carry (no hedge) until IV/RV normalises.
3. **Correlated failure (#7).** In a systemic exchange failure or stablecoin depeg, both the carry positions *and* the options clearing infrastructure may fail simultaneously. This is the tail-within-the-tail that no options overlay can fully hedge.
4. **Counterparty risk on options (#7).** Deribit or a comparable options venue could fail (counterparty risk), leaving the long-put position worthless at exactly the wrong time. Diversify across options venues if scale warrants.
5. **Hedge miscalibration (#5).** If the put strike is too far OTM (delta < −0.05), the payout in a typical crash (~30% drawdown) is minimal. If too close to ATM (delta > −0.30), the premium cost is high relative to expected funding carry.

## Kill criteria

Pause on any of:

1. **Carry book drawdown > 10%** (net of hedge P&L) in any rolling 30-day window.
2. **Expected carry < hedge budget**: 7d average funding, annualised, falls below the hedge premium rate.
3. **Options IV > 3× realized vol** on target instruments — hedge is far too expensive.
4. **7d funding average negative on > 50% of held positions** — regime flip.
5. **Exchange insurance-fund socialised loss** on any carry venue.

Re-deploy when funding recovers above 0.015%/8h average, hedge IV/RV drops below 1.5, and no exchange risk events are active. See [[when-to-retire-a-strategy]].

## Advantages

- **Converts implicit insurance-selling into explicit, budgeted protection.** The carry book was always implicitly short the tail; this construction acknowledges it and prices it.
- **Self-financing hedge.** The hedge premium comes from the same cash-flow (carry income) that the tail event threatens — structurally coherent and capital-efficient.
- **Bounded max drawdown.** With a properly sized put overlay, the carry book's left tail is explicitly capped, improving institutional suitability and reducing the probability of forced closure at the worst moment.
- **Carry income survives the hedge.** In calm regimes (the majority of time), carry income net of hedge cost remains positive — unlike pure tail-buying strategies (e.g. [[convex-tail-hedge-arbitrage]]) which bleed premium continuously.
- **IV/RV adaptive sizing.** The hedge budget scales with the relative attractiveness of options, avoiding purchases when vol is overpriced.

## Disadvantages

- **Reduced net carry.** 10-25% of carry income goes to hedge premiums; net yield is structurally lower than an unhedged carry book.
- **Complexity.** Two-instrument book (perp shorts + puts) across multiple venues (perp DEX + options exchange) with different settlement mechanics, collateral requirements, and roll schedules.
- **Options liquidity at scale.** Deep OTM crypto puts are illiquid above ~$5-10M notional; wide bid-ask spreads at size eat the hedge budget faster than the budget allows.
- **Hedge timing mismatch.** Options expire on fixed dates; carry positions close on continuous signals. A put expiring 1 week before a crash that triggers the carry exit provides zero protection.
- **Tax complexity.** Options premiums paid, options gains/losses, perp funding, and perp mark-to-market are often subject to different tax treatment in every jurisdiction.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (2023). The funding-carry baseline and its behavioral explanation. https://www.bis.org/publ/work1087.pdf
- He, Manela, Xu, Yan (2022/2024), *Fundamentals of Perpetual Futures*. Carry Sharpe ratios at retail and MM cost levels.
- [[book-a-man-for-all-markets]] — Thorp's treatment of delta-neutral arbitrage and Kelly sizing; the philosophical basis for carry-plus-hedge thinking.
- Ackman (2020) pandemic CDS trade — the canonical example of using income-bearing positions to finance tail-hedge premium. See [[2020-03-ackman-pandemic-cds-trade]] and [[convex-tail-hedge-arbitrage]].
- Haghani, V. and White, J. (2023), *The Missing Billionaires* (Wiley). Framework for sizing finite-variance positions with explicit tail recognition — relevant to the hedge budget calculation.
- AMBCrypto / DLNews coverage of the 2025-10-10 funding crash — the canonical tail event the hedge is designed to survive. See [[funding-rate-arbitrage#The 2021-2024 funding rate compression]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding (carry book signal + budget input)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI gate for carry positions
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — crowding check
- `GET /api/v1/derivatives/summary?coin=BTC` — combined carry book snapshot

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for budget projection
- `GET /api/v1/backtesting/funding` — deep funding archive for hedge-budget calibration backtests
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, max pain (complement to Deribit data for hedge sizing)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Carry leg** — `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding drives both carry entries and the rolling hedge budget
- **Crowding filter** — `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` + `GET /api/v1/derivatives/open-interest?coin=BTC` — skip carry entries into crowded, OI-stretched books
- **Hedge leg** — `GET /api/v1/market-intelligence/options` — BTC options OI / max-pain context for put-strike selection (strike-level pricing itself comes from Deribit)
- **Backtest** — `GET /api/v1/backtesting/funding` — Hyperliquid hourly funding since 2023-05, Binance daily since 2026-03-30; older Binance funding via `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` paging
- **Tips** — replay the hedge-budget rules against point-in-time states from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) so "when the hedge was cheap" is judged without lookahead

## Related

- [[funding-rate-arbitrage]] — the carry book primitive this page extends
- [[delta-neutral-yield-farming]] — the staking-enhanced cousin with a similar hedge structure
- [[convex-tail-hedge-arbitrage]] — pure tail-buying without carry; the complement
- [[trend-plus-tail-hedge]] — trend book + tail hedge (different primitive; not carry-specific)
- [[5-percent-otm-put-overlay]] — a simpler OTM put overlay at fixed-percentage size
- [[tail-risk-hedging]] — the general tail-hedge methodology
- [[cash-and-carry]] — the traditional basis-trade analog
- [[perpetual-futures]] — the instrument carrying the funding mechanism
- [[funding-rate]] — the underlying signal and cash-flow source
- [[options]] — the hedge instrument mechanics
- [[edge-taxonomy]] — structural + behavioral + risk-bearing classification
- [[failure-modes]] — crowding and counterparty risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
