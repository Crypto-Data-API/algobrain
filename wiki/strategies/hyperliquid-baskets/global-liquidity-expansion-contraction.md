---
title: "Global Liquidity Expansion / Contraction (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, quantitative, market-regime, regime-detection, risk-management, macro-events]
aliases: ["Global Liquidity Basket", "M2 Expansion Basket", "Macro Liquidity Signal", "DXY Liquidity Regime Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[crypto-macro-correlation-regime]]", "[[institutional-flow-regime]]", "[[macro-trend-regime]]", "[[policy-shock-regime]]", "[[dxy]]", "[[macro-relative-value]]", "[[regime-strategy-playbook]]", "[[crypto-market-regime-taxonomy]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[etf-and-institutional-flow]]", "[[macro-event-pump]]", "[[breadth-and-momentum-divergence]]", "[[defensive-majors]]", "[[full-bear-short-book]]", "[[trend-following]]", "[[trend-following-cta]]", "[[multi-strategy-portfolio]]", "[[when-to-retire-a-strategy]]"]
strategy_type: quantitative
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [analytical, informational]
edge_mechanism: "Central banks and institutional allocators shift liquidity conditions over months; crypto acts as a high-beta lever on global risk appetite, so leading indicators of liquidity expansion or contraction provide a directional bias weeks before price fully adjusts."
data_required: [dxy, global-m2-proxy, central-bank-balance-sheet-data, treasury-general-account, reverse-repo-balance, ohlcv-weekly, bitcoin-dominance]
min_capital_usd: 25000
capacity_usd: 200000000
crowding_risk: low
expected_sharpe: 0.6
expected_max_drawdown: 0.30
breakeven_cost_bps: 20
kill_criteria: |
  - drawdown > 30% over rolling 12 months
  - rolling 12-month Sharpe < 0 after 2 full liquidity cycles
  - correlation between liquidity signal and BTC 90-day forward return falls below 0.15 for 6 consecutive months
---

# Global Liquidity Expansion / Contraction (Hyperliquid Basket)

> **Not investment advice.** This is a design-doc draft for a systematic strategy sleeve. Performance figures are illustrative estimates only. Macro data levels (M2, balance sheets, reverse repo) are framed as heuristics, not verified current data — the direction of travel matters more than any specific level.

A macro-driven position [[trading-strategy-baskets|basket]] of [[hyperliquid|Hyperliquid]] [[perpetual-futures|perp]] positions that tracks the [[global-liquidity|global monetary liquidity cycle]] — central bank balance sheets, dollar liquidity conditions, and the broad [[dxy|DXY]] trend — and tilts long risk-crypto during expansion phases, reduces or flips short during contraction. This is the **slowest basket in the basket library**: the signal operates on a weeks-to-months timeframe, making it a structural backdrop for all other baskets rather than a source of frequent trading opportunities. Unlike the intraday and swing baskets, this sleeve may hold a position for 4–12 weeks between meaningful changes. It corresponds to the [[crypto-macro-correlation-regime]] within the [[market-regime]] framework.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Analytical** + **informational** (see [[edge-taxonomy]]).

- **Analytical** — the relationship between global liquidity and crypto price is widely discussed but rarely operationalized as a systematic signal with defined rules. Most market participants observe the correlation qualitatively; translating it into a rules-based position with explicit entry/exit triggers captures the gap between acknowledged correlation and disciplined implementation.
- **Informational** — central bank balance sheet data, TGA flows, and reverse repo balances are public but low-frequency; many crypto participants discount or ignore them entirely. Tracking these signals provides a directional view that is informed by macro inputs orthogonal to the on-chain and derivatives data the majority of crypto traders watch.

**Honest framing:** the BTC↔global-liquidity correlation is widely cited (see e.g. [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) but is **unstable** — it can break down during idiosyncratic crypto cycles, during crypto-specific regulatory shocks, or when the liquidity signal is already consensus. The strategy is best characterized as a **macro backdrop tilt**, not a precise timing tool.

## Why This Edge Exists

Risk assets — equities, high-yield credit, commodities, and crypto — are all claims on future nominal cash flows. When the global supply of dollars expands (central bank balance sheets growing, TGA drawdowns adding reserves, reverse repo draining), the discount rate on future cash flows falls and asset prices are bid. Crypto, as the highest-beta and least-regulated liquid risk asset, historically amplifies these moves. The counterparty is twofold: (1) macro-agnostic crypto traders who price Bitcoin purely on on-chain metrics, narratives, or technicals, ignoring the monetary backdrop; (2) macro investors who observe the correlation but do not systematically position in crypto as a liquidity-beta instrument. Both groups create a persistent lag between liquidity shifts and crypto price adjustment, which a systematic tracker exploits.

The [[dxy|DXY]] (US Dollar Index) is the most liquid, real-time proxy for global dollar tightness: a rising DXY means dollars are scarce globally, a headwind for dollar-priced risk assets. A falling DXY is the single most consistent macro tailwind for crypto (Source: [[crypto-macro-correlation-regime]]).

## Null Hypothesis

Under "no edge," global liquidity is coincident, not leading — BTC moves first (due to crypto-native catalysts) and M2 / balance sheet data follows with a lag because economic activity drives central bank action. The apparent lead-lag is an artifact of the data frequency mismatch (monthly M2 vs daily crypto prices) and survivor bias in choosing which liquidity windows to study. The strategy earns no alpha because the signal is either already priced or consistently late in regimes driven by crypto-native catalysts.

**Disconfirming evidence to monitor:**

- Sustained liquidity contraction periods where BTC rallies on crypto-native demand (ETF flows, halvings) — the strategy bleeds short-side carry while the signal is "wrong."
- DXY strength that is crypto-irrelevant (EM currency crises, geopolitical flight to dollar) — falsely fires a bearish signal.
- Liquidity expansion that is captured by equities and real assets without flowing into crypto (e.g., risk-off liquidity expansion where cash flees to Treasuries, not crypto).

## Rules

**Signal construction.** Evaluate weekly (each Monday close):

1. **DXY trend** — 20-week SMA slope: rising = tightening bias (bearish crypto), falling = easing bias (bullish crypto). DXY > an approximate "risk-off threshold" (illustrative heuristic: ~104–106 range) adds an extra bearish weight. *This is a directional signal, not a precise level.*
2. **Central bank balance sheet proxy** — use the 13-week rate of change of a blended G4 balance sheet proxy (Fed + ECB + BoJ + PBoC, converted to USD). Positive = expanding = bullish; negative = contracting = bearish.
3. **Dollar liquidity drain/inject proxies** — US Treasury General Account (TGA) drawdown = liquidity inject (bullish); reverse repo drain = liquidity inject (bullish). The direction and rate of change matter; specific balances are heuristics and should be tracked as flows, not levels.
4. **BTC correlation confirmation** — BTC's 20-week rolling correlation with a broad equity risk-on index: if correlation > 0.5, the macro signal has greater predictive power; if correlation collapses (crypto-idiosyncratic phase), downweight the signal.

**Composite liquidity score** (−100 to +100):
- Each of the four inputs scores −25 to +25 based on direction and magnitude.
- Score > +40 → Expansion (bullish crypto).
- Score −40 to +40 → Neutral (reduce size, hold BTC/ETH only).
- Score < −40 → Contraction (reduce or hedge).

**Position sizing by signal state:**

| State | Score | Position |
|-------|-------|----------|
| Strong expansion | > +60 | 100% long: BTC 60%, ETH 30%, high-beta alt basket 10% |
| Mild expansion | +40 to +60 | 70% long: BTC 50%, ETH 20% |
| Neutral | −40 to +40 | 30% long BTC/ETH only; no alts |
| Mild contraction | −40 to −60 | 0–10% net; hedge with [[defensive-majors]] posture |
| Strong contraction | < −60 | 0% long; optional short BTC perp at 1–2x, coordinate with [[full-bear-short-book]] |

**Holding / rebalancing.** Signal evaluated weekly. Re-score monthly (unless a major macro catalyst fires — see [[macro-event-pump]] for the intra-week event layer). Minimum hold: 2 weeks per signal state to avoid excessive turnover on weekly noise.

## Implementation Pseudocode

```python
def liquidity_score(state) -> float:
    """Returns composite liquidity score in [-100, +100]."""
    # DXY signal: falling DXY is bullish for crypto
    dxy_slope = sma_slope("DXY", window=20)  # negative slope = easing
    dxy_score = clamp(-dxy_slope * 500, -25, 25)

    # G4 balance sheet proxy: positive 13w ROC = expansion
    g4_roc = balance_sheet_13w_roc()  # returns fraction, e.g. 0.02 = +2%
    bs_score = clamp(g4_roc * 1000, -25, 25)

    # Dollar liquidity flows: TGA drawdown + reverse repo drain = inject
    tga_flow  = tga_weekly_change()   # negative (shrinking TGA) = inject = bullish
    rrp_flow  = rrp_weekly_change()   # negative (draining RRP)  = inject = bullish
    flow_score = clamp((-tga_flow - rrp_flow) * scale, -25, 25)

    # BTC-risk correlation weight
    btc_corr = rolling_correlation("BTC", "SPY", window=20, freq="W")
    corr_weight = max(0.4, min(1.0, btc_corr * 2))

    raw = dxy_score + bs_score + flow_score
    return raw * corr_weight  # scale down in low-correlation regimes

def position_from_score(score: float) -> dict:
    if score > 60:
        return {"BTC": 0.60, "ETH": 0.30, "alts": 0.10, "leverage": 1.5}
    elif score > 40:
        return {"BTC": 0.50, "ETH": 0.20, "leverage": 1.2}
    elif score > -40:
        return {"BTC": 0.30, "ETH": 0.00, "leverage": 1.0}
    elif score > -60:
        return {"BTC": 0.00, "hedge": True, "leverage": 1.0}
    else:
        return {"BTC": -0.20, "ETH": 0.00, "leverage": 1.0, "note": "light short"}
```

## Indicators / Data Used

- **[[dxy|DXY]]** — US Dollar Index, weekly close; 20-week SMA and slope. Primary real-time liquidity proxy.
- **G4 central bank balance sheets** — Fed H.4.1 (weekly), ECB balance sheet (weekly), BoJ (weekly), PBoC (monthly); blended proxy in USD terms. Source: central bank websites; aggregated by macro data providers.
- **US TGA balance** — US Treasury General Account at the Fed; weekly changes. Source: US Treasury Daily Statement.
- **Federal Reserve reverse repo (RRP)** — overnight reverse repo outstanding; direction of flow matters. Source: New York Fed.
- **BTC-equity rolling correlation** — 20-week rolling correlation of BTC weekly returns against SPY or a global equity index; used as a weight on the macro signal.
- **[[bitcoin-dominance-rotation|BTC dominance]]** — secondary signal; rising dominance in a contraction phase confirms the bearish macro read.
- **[[macro-events]]** — FOMC meeting dates, CPI release calendar, ECB policy meetings. These create event-driven step-changes in the liquidity signal; see [[macro-event-pump]] for the intra-week overlay.

Data sourced via [[the-block]], [[coinglass]], and public central bank data APIs.

**Data-feed mapping (cryptodataapi.com).** The macro inputs (DXY, M2 proxy, G4 balance sheets, TGA, RRP) are exogenous to cryptodataapi — they come from central-bank and Treasury sources. cryptodataapi.com supplies the Hyperliquid execution context for the BTC/ETH perp legs: [[funding-rate]] (the multi-week carry that is material at 4–12 week holds), [[open-interest]], mark price, and the liquidation feed. The basket's signal is macro; cryptodataapi governs how cheaply and safely that macro tilt is expressed on Hyperliquid.

## Example Trade

**Illustrative scenario — not a backtest.** Setup: Q1 of a hypothetical expansion year. DXY trending lower (20w slope negative); Fed begins balance sheet expansion program; TGA drawdown in progress (adds ~$200B+ reserves over 8 weeks — illustrative magnitude); BTC-SPY correlation at 0.65.

| Week | Action | Liquidity score | Position |
|------|--------|-----------------|----------|
| Week 1 | Signal enters expansion zone | +52 | Long BTC 50%, ETH 20%; leverage 1.2x |
| Week 4 | Score rises as DXY continues lower | +68 | Expand to BTC 60%, ETH 30%, alts 10%; 1.5x |
| Week 10 | DXY reverses; TGA refilling | +20 (falling) | Trim to BTC 30% only; wait for confirmation |
| Week 12 | Score crosses into contraction | −42 | Flatten longs; activate defensive posture |

*BTC hypothetically moves +35% during the expansion window, +8% during the neutral phase, −20% from the contraction trigger. Illustrative estimates only.*

## Performance Characteristics

**Return shape:** slow, lumpy, and trend-following in character. Long stretches of low activity punctuated by large directional moves during clear expansion/contraction cycles. Very similar in style to [[trend-following-cta]] strategies.

**Expected Sharpe (illustrative):** ~0.5–0.7 net over a full liquidity cycle (12–24 months). Sharpe can be negative in crypto-idiosyncratic years where BTC's correlation to macro breaks down.

**Max drawdown (illustrative):** ~25–30%. The main loss scenario is a crypto-specific bull run (e.g., halving-driven, ETF-driven) that occurs during a liquidity contraction — the strategy sits flat or short while BTC rallies strongly on crypto-native demand.

**Cost efficiency:** excellent. This is a weekly-rebalance, low-turnover basket. At a 4–8 week average hold, round-trip costs of ~15–25 bps per rebalance are low relative to the multi-week directional moves the strategy targets.

## Capacity Limits

Expressed entirely through BTC and ETH perps on Hyperliquid — effectively uncapped at the strategy's scale ($200M+). Hyperliquid's BTC and ETH perps are the deepest in the venue; multi-million-dollar positions can be entered/exited over hours without material impact. The strategy has no liquidity constraint at the sizes a small systematic book is likely to run. The binding constraint is model risk (the strategy is untested systematically) rather than market impact.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **BTC-macro correlation breakdown.** The core mechanism — crypto as high-beta global liquidity — breaks when Bitcoin enters a crypto-idiosyncratic phase (halving narratives, spot ETF-driven demand, regulatory pivots). The strategy will sit on the wrong side for an extended period.
2. **Signal latency.** Monthly M2 and balance sheet data arrives weeks after the fact. By the time the composite score clearly signals expansion or contraction, the price move is already partially complete. The DXY (daily) partially solves this, but the lags remain significant.
3. **Regime where DXY is geopolitically driven.** If DXY strength reflects EM instability or geopolitical flight to safety rather than Fed tightening, the DXY signal misfires as a crypto-bearish read.
4. **[[policy-shock-regime|Policy shock]] override.** A sudden, unexpected central bank action (emergency rate cut or hike) can reverse the liquidity signal faster than the weekly-rebalance cycle updates. Coordinate with [[macro-event-pump]] for the intra-week event layer.
5. **Overfitting on any single liquidity cycle.** With limited historical data for crypto-specific macro cycles, threshold calibration is highly vulnerable to in-sample bias. See [[crypto-perp-backtesting-pitfalls]] and [[overfitting-detection]].

## Kill Criteria

Linked to [[when-to-retire-a-strategy]]:

- **Drawdown > 30%** over rolling 12 months → pause; full strategy review.
- **Rolling 12-month Sharpe < 0** after experiencing at least 2 identifiable full liquidity cycles → the macro-correlation premise is not translating into returns; retire or restructure.
- **90-day rolling BTC-macro correlation < 0.15 for 6 consecutive months** → crypto has decoupled from the macro backdrop; suspend the signal until correlation re-establishes.

## Advantages

- **Orthogonal signal** — macro liquidity data is almost entirely uncorrelated to the on-chain and derivatives signals that drive the other baskets. Genuine diversification within the portfolio.
- **Low turnover / low cost** — weekly evaluation; 4–12 week holding periods; minimal transaction cost drag.
- **Large moves** — liquidity cycle turns are associated with multi-month directional trends in crypto; when the signal is right, the reward-to-cost ratio is exceptional.
- **Complements [[etf-and-institutional-flow]]** — liquidity expansion provides the macro backdrop that supports ETF inflows; the two signals corroborate or flag divergence.

## Disadvantages

- **Untested systematically** — the relationship is widely observed but not rigorously validated with walk-forward testing; `backtest_status: untested` reflects genuine uncertainty.
- **Slow and infrequent** — may produce only 2–4 full signal-state changes per year; not suitable as a standalone alpha source; best as a portfolio overlay.
- **Data quality / lag** — balance sheet and TGA data is published with delays; some series are revised retroactively. Real-time tracking requires aggregation across multiple official sources.
- **Model risk** — the liquidity↔crypto relationship is structurally plausible but not stable; it can break for multi-year periods.

## Hyperliquid Execution Notes

This is a **position-timeframe basket** (hold durations 4–12 weeks). Hyperliquid-specific considerations:

- **Funding carry over multi-week holds** is a material cost or income. At a 4-week hold, even 0.01% per 8 hours (~11% annualized) becomes a significant drag on short legs or tailwind on long legs. Monitor funding closely; see [[hyperliquid-funding-rate-microstructure]]. Large positive funding during an expansion phase is a carry bonus for longs; large positive funding during a contraction phase may discourage shorting unless the macro signal is strong.
- **Isolated margin per leg** — especially important for the rare short leg during contraction. Single-mark-tick liquidation and ADL are not abstract risks at multi-week hold durations; see [[hyperliquid-liquidation-engine]]. Size BTC shorts to survive a 20% adverse move (unexpected macro policy reversal) without liquidation; leverage ≤ 2x on any held leg.
- **No thin perps** — this basket trades BTC and ETH only. No alt exposure on the long leg (beyond the 10% allocation in strong expansion), and no alt shorts. The macro signal's precision does not justify the squeeze risk of thinner perps at multi-week holding durations.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket framework; the [[institutional-flow-regime]] and [[macro-trend-regime]] baskets are the direct regime contexts for this strategy.
- [[crypto-macro-correlation-regime]] — detailed treatment of the DXY / cross-asset correlation regime.
- [[dxy]] — reference page for the primary real-time liquidity proxy.
- [[macro-relative-value]] — companion strategy using cross-asset macro signals.
- [[trend-following-cta]] — the closest stylistic analog in the strategy library.
- [[crypto-perp-backtesting-pitfalls]], [[overfitting-detection]] — calibration caveats especially relevant given the low-frequency, hard-to-backtest nature of this signal.

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[global-liquidity]] · [[market-regime]] · [[crypto-macro-correlation-regime]] · [[institutional-flow-regime]] · [[macro-trend-regime]] · [[policy-shock-regime]] · [[dxy]] · [[macro-relative-value]] · [[regime-strategy-playbook]] · [[crypto-market-regime-taxonomy]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[etf-and-institutional-flow]] · [[etf-flows]] · [[macro-event-pump]] · [[breadth-and-momentum-divergence]] · [[defensive-majors]] · [[full-bear-short-book]] · [[trend-following]] · [[trend-following-cta]] · [[multi-strategy-portfolio]] · [[hyperliquid]] · [[perpetual-futures]] · [[funding-rate]] · [[open-interest]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[the-block]] · [[coinglass]]
