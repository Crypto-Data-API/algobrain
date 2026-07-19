---
title: "Stablecoin Depeg Sentiment Entry"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, stablecoins, arbitrage, behavioral-finance, mean-reversion, sentiment, crypto, defi]
aliases: ["Stablecoin Panic Entry", "Depeg Sentiment Filter", "Fear-Driven Depeg Buy", "Stablecoin Sentiment-Extreme Gate"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural]
edge_mechanism: "Major stablecoin depegs divide into two types: panic-driven depegs (temporary, driven by fear contagion regardless of redemption mechanism health — e.g., USDC/SVB 2023 where the stablecoin depegged to $0.87 before recovering fully as the peg mechanism was intact) and structural depegs (permanent or semi-permanent collapse driven by actual mechanism failure — e.g., UST/LUNA 2022 where the algorithmic peg broke). A Fear & Greed extreme (≤ 15 for 48h+) combined with a healthy redemption-channel status separates panic-driven depegs from structural failures: the sentiment extreme identifies when market participants are in full panic mode, which is precisely when panic-driven depegs occur at maximum discount. Entering a depeg buy at a Fear & Greed extreme with a confirmed-healthy redemption channel produces a near-arbitrage: the buyer is extracting value from sellers who are fleeing irrationally. The counterparty is the panicked stablecoin holder who sells USDC at $0.87 because they fear a bank run that the mechanism can handle."

data_required: [fear-greed-index, stablecoin-prices-by-venue, redemption-channel-status, curve-pool-composition, depeg-amount, psm-utilization, protocol-reserves, usdc-backing-data]
min_capital_usd: 20000
capacity_usd: 50000000
crowding_risk: low

expected_sharpe: 1.8
expected_max_drawdown: 0.15
breakeven_cost_bps: 20

decay_evidence: "The depeg panic-entry strategy is situational (not continuously deployed) and durable because human panic behavior in financial crises is persistent across decades. The March 2023 USDC/SVB depeg ($0.87 low, full recovery within 72 hours) is the canonical recent example; the 2018 USDT banking concern (USDT to $0.85), and USDT-2020 concerns all show the same pattern: major overcollateralised or fiat-backed stablecoins depeg on panic to well below their actual risk-adjusted fair value. Strategy capacity is limited by depeg event frequency (2–4 per year) and liquidity available at the discount level."

kill_criteria: |
  - 3 consecutive panic-entry trades where the stablecoin continued declining below the entry level by > 5% (the sentiment filter is not correctly separating panic depegs from structural depegs)
  - redemption channel status check false-positive: stablecoin entered as "healthy" subsequently freezes redemptions within 24h of entry (data source reliability failure)
  - maximum per-trade loss exceeds 10% of the capital deployed (structural depeg occurred despite sentiment extreme + healthy mechanism gate)
  - strategy draws down > 15% of dedicated stablecoin-arb sleeve in any 12-month period

related: ["[[stablecoin-depeg-profit-capture]]", "[[stablecoin-pair-arbitrage]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[contrarian-extremes]]", "[[sentiment-positioning-divergence]]", "[[onchain-capitulation-confluence]]", "[[post-panic-vol-selling]]", "[[crowded-short-funding-fade]]", "[[stablecoin-depeg-history]]", "[[stablecoins]]", "[[algorithmic-stablecoin]]", "[[curve-finance]]", "[[makerdao]]", "[[ethena]]", "[[depeg-risk]]", "[[behavioral-finance]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Stablecoin Depeg Sentiment Entry

Stablecoin depeg sentiment entry is a **panic-driven mean-reversion** strategy that buys a major overcollateralised or fiat-backed stablecoin at a discount to its $1.00 peg specifically when two simultaneous conditions are confirmed: (1) crypto-wide Fear & Greed is at a panic extreme (≤ 15 for 48+ hours), confirming that the depeg is driven by contagion fear rather than mechanism failure, AND (2) the stablecoin's redemption channel is confirmed operational (not frozen, not capacity-constrained above the entry discount level). The combination separates the high-expected-value panic depeg (where the discount is a product of irrational fear, not genuine credit risk) from the structural depeg (where the discount accurately reflects broken mechanics). The counterparty is the panicking stablecoin holder who exits USDC at $0.87 because they fear a bank run that the mint/redemption mechanism can contain.

**This is differentiated from [[stablecoin-depeg-profit-capture]]** — that page is a multi-method tactical playbook for extracting maximum P&L from any depeg event regardless of cause (spot buy, redemption arb, leveraged borrow-and-redeem, cross-venue dislocation, post-event short of overshoot, options skew capture). This page answers a different question: WHEN to enter a depeg buy. The sentiment-extreme filter is the entry selection gate; the depeg-profit-capture playbook is the execution toolkit to use once this gate triggers the entry. The two pages are composable: this page selects the events; that page maximises P&L per event.

**This is differentiated from [[stablecoin-pair-arbitrage]]** — that page trades the relative price spread between two different stablecoins (USDC vs USDT, DAI vs USDC) as a continuous cross-stable mean-reversion trade, without requiring a panic extreme or a single-stable depeg event. This page requires a single stablecoin to depeg materially (≥ 2% discount) in the context of a broader panic sentiment extreme.

**This is differentiated from [[contrarian-extremes]]** — that page fades whole-market directional sentiment extremes (buy BTC/ETH at Fear & Greed ≤ 15; sell at ≥ 85) for the underlying price trend reversals. This page uses the same Fear & Greed gate but applies it to a structurally different instrument (stablecoin peg restoration) with a hard $1.00 recovery target instead of a probabilistic price reversion target. The mechanism is more mechanical: a healthy stablecoin's peg must restore to $1.00 (mechanically guaranteed by redemption); a BTC/ETH reversion is probabilistic.

**This is differentiated from [[sentiment-positioning-divergence]]** — that page uses the sentiment extreme as a gate for a leveraged BTC/ETH long entry confirmed by funding/positioning divergence. This page uses the sentiment extreme as a gate for a stablecoin peg-restoration trade, where the instrument is structurally uncorrelated to BTC/ETH positioning.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural**:

- **Behavioral (primary)** — Financial panics cause correlated selling across all assets perceived as "risky" in the current regime, including stablecoins whose backing is not actually impaired. In March 2023, USDC sold off to $0.87 because market participants feared the SVB bank run would impair Circle's reserves — despite the reserves being primarily short-term US Treasuries and cash at other institutions. The fear was real; the credit risk was not. Behavioral overcorrection in financial panics creates the entry opportunity.
- **Structural** — Overcollateralised and fiat-backed stablecoins have a mechanical peg-restoration guarantee: the issuer (Circle, Tether, MakerDAO) maintains redemption channels at $1.00 par. When the spot price trades at a discount and the redemption channel is open, a structural arbitrage exists: buy the stablecoin cheap, redeem at par. The sentiment extreme identifies WHEN the discount is largest (panic phase = maximum irrational selling); the redemption channel confirms the structural floor.

## Why this edge exists

**The two-type depeg taxonomy:**

| Type | Example | Redemption channel | Expected recovery | Entry decision |
|---|---|---|---|---|
| Panic depeg | USDC/SVB 2023 ($0.87 low) | Open — Circle operations normal | Full recovery to $1.00 within 72h | ENTER at sentiment extreme |
| Structural depeg | UST/LUNA 2022 ($0 → death spiral) | Broken — algorithm unable to mint/burn | No recovery | DO NOT ENTER |
| Partial structural | BUSD 2023 (Paxos wind-down) | Technically open but confidence zero | Slow recovery over weeks/months | Borderline — smaller position, longer hold |

**The sentiment-extreme filter selects for panic depegs, not structural ones,** because:
1. Genuine structural depegs are triggered by MECHANISM failure, not by generalised fear. They generate a market-specific negative signal (smart money exiting), NOT a market-wide panic sentiment extreme. UST collapse in May 2022 coincided with BTC declining but the Fear & Greed did not reach ≤ 15 at the exact moment of the initial UST break — the contagion spread later.
2. Panic depegs correlate with market-wide Fear & Greed extremes because they are driven by general risk-off sentiment (bank run fears, "crypto is dead" narratives, contagion from a different failure). They infect healthy stablecoins by association.

**The redemption-channel health check is the structural safeguard:** even in a panic, if the redemption channel is operationally open and Circle/Tether confirms reserves are sufficient, the structural floor at $1.00 (via redemption) prevents the stablecoin from approaching zero. The entry discount is thus bounded: the buyer is purchasing a $1.00 instrument at $0.87–0.95 with a clear mechanical path back to $1.00.

**Who is on the other side:** the panicking stablecoin holder who has lost trust in the mechanism and is selling at any bid available to get "safety" into BTC or another stablecoin they perceive as safer. They are the supply side of the depeg discount; their fear-driven selling creates the maximum entry opportunity at the lowest price.

## Null hypothesis

Under the null, sentiment extremes add **no incremental predictive power** for stablecoin depeg recovery:

- The expected recovery time and probability for a stablecoin depeg are the same whether the depeg occurs at Fear & Greed ≤ 15 vs Fear & Greed 20–50 (moderate fear), controlling for depeg depth and redemption channel status.
- Entries during panic extremes (Fear & Greed ≤ 15) should not produce statistically higher average returns than entries at moderate fear levels, after controlling for depeg discount magnitude.

Testable using historical depeg data ([[stablecoin-depeg-history]]): for each depeg event, record the Fear & Greed at the maximum discount date and the subsequent recovery to $0.995+ in days. Compare recovery speed and probability across Fear & Greed deciles. Prediction: depegs occurring at Fear & Greed ≤ 15 show faster recovery and lower non-recovery probability than depegs at Fear & Greed 20–40, controlling for depeg depth.

Currently untested (not rejected). The 2023 USDC/SVB example supports the hypothesis: Fear & Greed was ≤ 15 at the $0.87 low on March 10–11, 2023; recovery was complete by March 13 (72 hours).

## Rules

### Entry gate (all four conditions must be simultaneously confirmed)

**Gate 1: Fear & Greed panic extreme**
- Fear & Greed Index ≤ **15** (extreme fear) for ≥ **48 consecutive hours**.
- Source: `GET /api/v1/sentiment/fear-greed`.
- *Rationale:* 48-hour persistence filters out a single-day spike; sustained extreme fear indicates a genuine panic contagion environment, not a one-day correction.

**Gate 2: Target stablecoin at material discount**
- Spot price of the target stablecoin on at least 2 major venues ≤ **$0.97** (≥ 3% discount to par).
- Source: multiple venues (Binance, Coinbase, Kraken spot prices for USDC/USDT/DAI).
- *Rationale:* a discount of ≥ 3% provides a margin above round-trip costs (CEX fee + withdrawal/deposit friction); shallow depegs (< 3% discount) do not offer enough spread after costs.

**Gate 3: Redemption channel confirmed operational**
- Issuer has NOT announced a redemption freeze or capacity suspension within the last 24 hours.
- Circle (for USDC) / Tether (for USDT) reserves report is ≤ 30 days old with no new adverse disclosure.
- PSM utilization (for DAI PSM) is < 95% (redemption capacity available).
- *Sources:* issuer's official communications (Circle blog, Tether attestations), DeFi protocol PSM dashboards.
- *Rationale:* this is the structural floor check. Without a functional redemption channel, the $1.00 par floor is theoretical. Gate 3 confirms the floor is physically accessible.

**Gate 4: No new systemic failure announcement in last 12 hours**
- No announcement from the issuer, major custodian, or regulator indicating mechanism impairment (reserve shortfall, regulatory seizure, smart contract hack).
- Source: manual monitoring of issuer Twitter/blog, Rekt.news, crypto news feeds.
- *Rationale:* the redemption channel can be open but a new impairment announcement (not yet reflected in the operational status) can render it non-functional within hours. Recent negative news is a disqualifier regardless of current operational status.

### Instrument and execution

- **Primary instrument:** spot buy of the depegged stablecoin at the discount (e.g., USDC at $0.87 on Coinbase or Binance).
- **Secondary (if spot not available at sufficient discount):** Curve pool imbalance — buy the depegged stablecoin from the Curve 3pool or specific depeg pool where it is offered at the maximum discount.
- **Redemption path:** as soon as the discount exceeds the redemption cost, route to the issuer's redemption portal directly (Circle: native USDC redemption; MakerDAO: PSM) for near-arbitrage rather than waiting for market recovery.

### Position sizing

- **Base position:** 10–20% of stablecoin-arb sleeve per depeg event (this is a higher-conviction setup than continuous cross-stable arb).
- **Maximum per event:** 40% of sleeve (the redemption-channel health check still carries tail risk of rapid status change).
- **Tiered entry:** deploy 50% at first signal, add 50% if the discount widens a further 1% (average down into the panic bottom).

### Exit rules

1. **Primary exit:** sell at ≥ **$0.997** (3 bps below par — accounts for spread and venue friction). If redemption channel is open, redeem directly at $1.00 instead.
2. **Time exit:** close at market price after **7 days** if $0.997 not reached (structural depeg in progress; cap the loss).
3. **Stop loss:** close at **$0.82** (entry at $0.87: stop at 5.7% below entry). Gate 3 failed after entry or mechanism impairment materialised.

## Implementation pseudocode

```python
# stablecoin_sentiment_depeg_entry.py

from dataclasses import dataclass
from typing import Optional

FEAR_GREED_MAX        = 15      # extreme fear threshold
FEAR_GREED_MIN_HOURS  = 48     # minimum sustained hours at threshold
DEPEG_DISCOUNT_MIN    = 0.03   # minimum discount to par (3%) for viable entry
ENTRY_TIER1_FRAC      = 0.50   # deploy 50% on first signal
ENTRY_TIER2_EXTRA_DIP = 0.01   # add remaining 50% if discount widens 1% further
EXIT_TARGET           = 0.997  # sell at near-par
STOP_LOSS_PRICE       = 0.82   # hard stop below structural worst-case
MAX_HOLD_DAYS         = 7

@dataclass
class DepegState:
    stablecoin:              str       # "USDC", "USDT", "DAI"
    fear_greed_current:      float     # current F&G index (0–100)
    fear_greed_hours_below:  float     # hours F&G has been ≤ 15
    spot_price_venue1:       float     # e.g. Binance USDC/USD
    spot_price_venue2:       float     # e.g. Coinbase USDC/USD
    redemption_channel_open: bool      # operational status (manual flag)
    adverse_news_12h:        bool      # any new impairment announcement
    psm_utilization:         float     # DAI PSM or equivalent (0–1)

@dataclass
class OpenPosition:
    entry_price:      float
    entry_date:       str
    days_held:        int
    max_discount_seen: float   # for averaging down logic

def gates_pass(s: DepegState) -> tuple[bool, list[str]]:
    fails = []
    if s.fear_greed_current > FEAR_GREED_MAX:
        fails.append(f"F&G {s.fear_greed_current} > {FEAR_GREED_MAX}")
    if s.fear_greed_hours_below < FEAR_GREED_MIN_HOURS:
        fails.append(f"F&G only below threshold for {s.fear_greed_hours_below:.0f}h < {FEAR_GREED_MIN_HOURS}h")
    best_price = min(s.spot_price_venue1, s.spot_price_venue2)
    discount = 1.0 - best_price
    if discount < DEPEG_DISCOUNT_MIN:
        fails.append(f"discount {discount:.1%} < {DEPEG_DISCOUNT_MIN:.1%}")
    if not s.redemption_channel_open:
        fails.append("redemption channel NOT confirmed open")
    if s.adverse_news_12h:
        fails.append("adverse issuer/custodian news in last 12h")
    if s.psm_utilization > 0.95:
        fails.append(f"PSM utilization {s.psm_utilization:.0%} > 95% — capacity constrained")
    return len(fails) == 0, fails

def entry_decision(s: DepegState, sleeve_usd: float,
                   existing_position: Optional[OpenPosition]) -> dict:
    ok, fails = gates_pass(s)
    if not ok:
        return {"action": "WAIT", "reason": "; ".join(fails)}
    best_price = min(s.spot_price_venue1, s.spot_price_venue2)
    discount = 1.0 - best_price
    if existing_position is None:
        # first entry: deploy Tier 1 (50% of 20% sleeve = 10% of sleeve total)
        notional = sleeve_usd * 0.20 * ENTRY_TIER1_FRAC
        return {"action": "BUY_TIER1", "notional_usd": notional, "entry_price": best_price,
                "note": f"discount={discount:.1%}, F&G={s.fear_greed_current}"}
    if discount >= existing_position.max_discount_seen + ENTRY_TIER2_EXTRA_DIP:
        # average down: add Tier 2 (remaining 10% of sleeve)
        notional = sleeve_usd * 0.20 * (1 - ENTRY_TIER1_FRAC)
        return {"action": "BUY_TIER2_AVGDOWN", "notional_usd": notional, "entry_price": best_price}
    return {"action": "HOLD", "reason": "waiting for further discount or recovery"}

def exit_decision(pos: OpenPosition, current_price: float) -> Optional[dict]:
    if current_price >= EXIT_TARGET:
        return {"action": "SELL_TARGET", "reason": f"price {current_price:.4f} >= {EXIT_TARGET}"}
    if current_price <= STOP_LOSS_PRICE:
        return {"action": "SELL_STOP", "reason": f"price {current_price:.4f} <= {STOP_LOSS_PRICE} (structural depeg)"}
    if pos.days_held >= MAX_HOLD_DAYS:
        return {"action": "SELL_TIME", "reason": f"{MAX_HOLD_DAYS}d time exit"}
    return None
```

## Indicators / data used

- **Fear & Greed Index** — `GET /api/v1/sentiment/fear-greed`; current value and historical readings; Gate 1: ≤ 15 for ≥ 48h.
- **Stablecoin spot prices** — multi-venue (Binance, Coinbase, Kraken APIs; stablecoin price data is not in CryptoDataAPI but is available from exchange APIs directly); Gate 2: ≤ $0.97 on at least 2 venues.
- **Stablecoin flow anomalies** — `GET /api/v1/sentiment/stablecoin-flows` or `GET /api/v1/on-chain/exchange-flows/USDC`; large exchange inflows of USDC signal redemption pressure; large outflows signal distribution.
- **Regime** — `GET /api/v1/regimes/current`; `Structural_Shock` or `Crash` regimes confirm the macro context that justifies panic entry; `Bear_Trend` without panic context is insufficient.
- **DVOL** — `GET /api/v1/volatility/dvol?coin=BTC`; elevated DVOL (> 80) in conjunction with Fear & Greed ≤ 15 confirms systemic risk-off environment (not just a normal correction).
- **Issuer redemption status** — manual: Circle blog (`circle.com/blog`), Tether attestations, MakerDAO governance forum. CryptoDataAPI does not cover issuer communication.
- **Curve pool composition** — manual: Curve Finance UI or DefiLlama for pool imbalance data (high USDC fraction in 3pool = USDC is cheap; pool is imbalanced toward USDC).

## Example trade

**Setup: USDC/SVB analog depeg (illustrative, based on March 2023 pattern)**

- March 10, 2023: USDC spot price on Coinbase = $0.872. Binance USDC = $0.881. Best price = $0.872. Discount = 12.8%.
- Fear & Greed: 8 (extreme fear). Hours below 15: 52 hours. Gate 1 PASSES.
- Discount = 12.8% > 3%. Gate 2 PASSES.
- Circle blog post: "USDC reserves are unaffected by SVB. $3.3B of reserves ($40B total) were at SVB; Circle is actively managing the situation. Redemptions remain open." Gate 3 PASSES.
- No issuer-announced freeze in last 12 hours. Gate 4 PASSES.
- All gates pass. Sleeve: $100,000. Tier 1 entry: $100,000 × 20% × 50% = **$10,000 at $0.872**.

*March 10, 2023 (6 hours later): USDC drops to $0.857 (discount = 14.3%). Tier 2 average-down trigger: discount widened 1.5% from $0.872 entry (≥ 1% trigger). Deploy Tier 2: $10,000 × (50% remaining) = **$5,000 at $0.857**. Total position: $15,000 at blended entry $0.867.*

*March 13, 2023 (72 hours after entry):* USDC recovers to $0.999 as US government guarantees SVB deposits. Circle confirms full reserves.
- Exit: sell $15,000 position at $0.999.
- P&L: ($0.999 − $0.867) / $0.867 × $15,000 = **+$2,284** (+15.2% on the depeg position, +2.28% of total $100K sleeve). Net of 20 bps costs: **+$2,254**.

*(Illustrative. Based on publicly reported USDC price action March 10–13, 2023. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.8 | High selectivity (2–4 events/year); near-mechanical recovery when gates pass |
| Expected max drawdown | ~15% | From a gate-3 false positive (redemption channel opens then freezes) |
| Win rate (per event) | ~75–85% (estimated) | Historical panic depegs on major overcollateralised stables recover almost universally when redemption channel is intact |
| Average hold duration | 24–72 hours | Panic depegs recover rapidly once fear subsides; structural depegs do not |
| Breakeven cost | 20 bps | CEX taker fee ~5–10 bps per side; redemption channel processing 0–5 bps; total well within typical 3–12% entry discount |
| Events per year | 2–4 | Depeg panic events with Fear & Greed ≤ 15 AND ≥ 3% discount; uncommon but recurring |

**Cost overlay:** the breakeven cost (20 bps) is trivially low relative to the typical entry discount (3–15%). The dominant risk is not cost — it is the Gate 3 false positive (entering when the redemption channel appears open but is about to freeze). Sized at 10–20% of sleeve per event, even a complete loss (→ $0) on one event loses 10–20% of the sleeve, within the 15% max drawdown budget.

## Capacity limits

- **Per event:** `capacity_usd: 50000000` — constrained by spot liquidity at the discount price level. USDC at $0.87 had genuine depth on Coinbase/Binance/Kraken; $50M of buying could be executed with 3–5% market impact over 12 hours. Curve pool imbalance execution does not have the same depth constraint.
- **Per operator:** above $5–10M, the operator's buying itself starts to recover the peg, reducing the entry advantage. The strategy is not self-defeating at smaller sizes.
- **Strategy-level:** frequency (2–4 events/year) limits annual capacity; cannot be the sole P&L source for a large book.

## What kills this strategy

1. **Gate-3 false positive — redemption channel freezes after entry (#7: Operational).** The most dangerous scenario: a stablecoin appears healthy at entry (Circle says redemptions are open) but a new adverse development (regulatory seizure, custodian failure) freezes redemptions 6–12 hours later. Gate 4 (no adverse news in last 12h) partially mitigates this but cannot prevent a sudden freeze. The stop loss at $0.82 limits the loss but structural depegs can fall below $0.82.
2. **Panic depeg becomes structural during hold (#4: Crowding / regime).** The gate correctly identifies a panic depeg entry, but subsequent news (Circle loses second banking partner, revealing inadequate diversification) converts the panic depeg into a structural one during the 7-day hold. The 7-day time exit forces realisation of whatever discount remains at expiry.
3. **Sentiment extreme without stablecoin depeg (#7: Operational).** Fear & Greed can reach ≤ 15 during BTC crashes that do not impair stablecoin pegs (the discount remains < 3%). In this case, no entry is triggered — the strategy sits idle. This is correct behavior but may frustrate operators looking for activity during panic windows.
4. **Redemption channel process risk (#7: Operational).** Circle's USDC redemption requires KYB/KYC and minimum redemption amounts ($100K). For smaller operators, the spot-market recovery path (not the redemption arb path) is the only available exit. This adds hold time and price risk that the pure redemption arb operator does not face.

## Kill criteria

Pause or retire on any of:

1. **3 consecutive panic-entry trades where price continued declining ≥ 5% below entry** — sentiment filter is not correctly separating panic depegs from structural ones; reassess Gate 3/4 criteria.
2. **Redemption channel false-positive causes > 10% loss on a single trade** — Gate 3 source reliability failure; upgrade the monitoring approach.
3. **Maximum drawdown of stablecoin-arb sleeve exceeds 15%** — strategy sizing or gate calibration is incorrect for current market conditions.
4. **No qualifying events in 18 months** — strategy may be appropriate to maintain as standby capital; consider allocating sleeve to AAVE stablecoin yield until next qualifying event.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **High win rate when gates pass** — major fiat-backed / overcollateralised stablecoins have a mechanical floor at $1.00 via redemption; gate-passing depegs have near-mechanical recovery.
- **Low crowding** — the strategy requires manual monitoring of issuer communications (Gate 3/4) that cannot be fully automated; this limits the number of systematic competitors executing the same entry.
- **Composable with the full depeg-profit-capture toolkit** — [[stablecoin-depeg-profit-capture]]'s redemption arb, cross-venue capture, leveraged borrow-and-redeem, and post-event overshoot short methods can all be layered on top of this gate once the sentiment-extreme entry is triggered.
- **Clear stop-loss mechanics** — the strategy has a well-defined failure mode (Gate 3 false positive) and a hard price-based stop, making position sizing and risk management explicit.

## Disadvantages

- **Manual monitoring required** — Gate 3 (redemption channel status) and Gate 4 (no adverse news) cannot be fully automated from a single API. The operator must monitor issuer communications; automation gap creates operational risk.
- **Rare signal frequency** — 2–4 qualifying events per year. Capital deployed in this strategy sleeve must earn alternative yield (AAVE stablecoin rates) in the interim.
- **Tail risk from complete mechanism failure** — the strategy explicitly avoids structural depegs, but the line between panic and structural is not always clear in real time (UST/LUNA 2022 looked like a panic depeg initially). Gate 3/4 are designed to catch this but are not infallible.
- **Redemption access inequality** — large operators (with Circle KYB redemption access) can execute the near-arbitrage directly at $1.00; smaller operators must wait for market recovery, which takes longer and carries more hold risk.

## Sources

- [[stablecoin-depeg-history]] — documented depeg events with Fear & Greed context; primary empirical reference for this strategy
- [[stablecoin-depeg-profit-capture]] — the multi-method execution toolkit composable with this entry gate
- [[contrarian-extremes]] — the general sentiment-extreme contrarian entry; this page is the stablecoin-specific analog
- [[2023-03-usdc-svb-depeg]] — the canonical panic-depeg event (if this page exists); USDC to $0.87, recovery to $1.00 in 72h

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — Gate 1: Fear & Greed Index value and history; ≤ 15 for 48h = entry trigger
- `GET /api/v1/regimes/current` — macro regime context; Structural_Shock or Crash confirms panic environment
- `GET /api/v1/volatility/dvol?coin=BTC` — secondary panic confirmation; DVOL > 80 in conjunction with low F&G
- `GET /api/v1/on-chain/exchange-flows/USDC` — stablecoin exchange flow context; large USDC exchange inflows signal redemption pressure

**Historical data:**
- `GET /api/v1/sentiment/fear-greed?historical=true&days=730` — 2-year Fear & Greed history for backtesting; align with stablecoin-depeg-history events to calibrate the ≤ 15 threshold

*Note: stablecoin spot prices (USDC/USD, USDT/USD on multiple venues) are NOT in CryptoDataAPI. Use exchange REST APIs directly: Binance `GET /api/v3/ticker/price?symbol=USDCUSDT`, Coinbase `GET /api/v3/brokerage/products/USDC-USD/ticker`. Curve pool composition: Curve Finance subgraph or DefiLlama. Issuer redemption status: Circle blog (`circle.com/blog`), Tether transparency (`tether.to/transparency`), MakerDAO governance forum.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/sentiment/fear-greed"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]], [[cryptodataapi-regimes]].

**Live dashboards:** [fear & greed](https://cryptodataapi.com/fear-greed) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can arm this trade end-to-end (execution needs external venue feeds):

- **Gate** — `GET /api/v1/sentiment/fear-greed` at or below 15 for 48h plus `GET /api/v1/regimes/current` in a shock label are the panic pre-conditions
- **Filter** — `GET /api/v1/volatility/dvol?coin=BTC` above 80 corroborates systemic panic; `GET /api/v1/on-chain/exchange-flows/USDC` flags redemption pressure building
- **Signal** — the depeg price itself comes from venue tickers (Binance/Coinbase REST, no CDA endpoint); the agent arms on CDA panic gates and executes on external price feeds
- **Backtest** — `GET /api/v1/market-intelligence/fear-greed-history` aligned with known depeg events (see [[stablecoin-depeg-history]]) calibrates the threshold; `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) preserves point-in-time sentiment for future events
- **Tips** — depegs resolve in hours; pre-authorize order routes before the event, because a depeg hitting during rate-limit exhaustion is an unrecoverable miss

## Related

- [[stablecoin-depeg-profit-capture]] — the full multi-method depeg execution toolkit; composable with this sentiment-entry gate
- [[stablecoin-pair-arbitrage]] — continuous cross-stable spread arb; differentiated as a continuous strategy vs this page's event-triggered entry
- [[synthetic-stablecoin-depeg-arbitrage]] — synthetic stablecoin depeg arb via on-chain mechanisms; different execution path for the same entry
- [[contrarian-extremes]] — market-wide sentiment extreme fade for BTC/ETH; differentiated as directional vs stablecoin peg-restoration
- [[sentiment-positioning-divergence]] — sentiment extreme + derivative positioning confirmation for BTC/ETH long; different asset, different instrument
- [[onchain-capitulation-confluence]] — on-chain + sentiment for cycle-bottom BTC entries; stablecoin-focused analog
- [[post-panic-vol-selling]] — post-panic stabilisation vol trade; thematically adjacent (both are post-panic mean-reversion plays)
- [[stablecoin-depeg-history]] — historical depeg events; primary empirical basis
- [[stablecoins]] — stablecoin concept overview
- [[algorithmic-stablecoin]] — algorithmic stablecoin design; key context for distinguishing structural vs panic depegs
- [[depeg-risk]] — depeg risk concept; theoretical basis for Gate 3/4 design
- [[behavioral-finance]] — panic and contagion behavior; theoretical basis for Gate 1
- [[edge-taxonomy]] — behavioral + structural edge classification
- [[failure-modes]] — gate false-positive, structural depeg conversion failure modes
- [[when-to-retire-a-strategy]] — kill vs pause framework
