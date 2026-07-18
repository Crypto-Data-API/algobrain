---
title: "Unlock Short with Crowding Gate"
type: strategy
created: 2026-07-18
updated: 2026-07-18
status: good
tags: [combinations, meta-strategy, event-driven, funding-rate, perpetual-futures, derivatives, behavioral-finance, quantitative, crypto]
aliases: ["Gated Unlock Short", "Crowding-Filtered Token Unlock", "Unlock Supply-Event with Entry Discipline"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [structural, informational, behavioral]
edge_mechanism: "Token cliff unlocks create a predictable forced-supply overhang; the crowding gate (funding not deeply negative, OI not already spiked short) filters for the subset where the trade is non-consensus — entering before the short side is crowded avoids paying to be the last short in a position that is already squeezable, and captures the trade at its highest expected value."

data_required: [token-unlock-schedule, funding-rates, open-interest, perp-price, ohlcv-daily, circulating-supply, on-chain-vesting-contracts]
min_capital_usd: 5000
capacity_usd: 10000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 40

decay_evidence: "Token unlock front-running has become increasingly crowded since 2022 as dedicated unlock-tracking services (Token Unlocks, Coinglass unlock calendar, The Block) went mainstream. The trade's edge depends on entering before the short consensus forms; as crowding of unlock shorts increases, the gate becomes the primary source of remaining edge — it selects the subset of unlocks that are still non-consensus."

kill_criteria: |
  - strategy drawdown > 25% from high-water mark
  - rolling 3-month Sharpe < 0 on minimum 10 completed unlock trades
  - crowding gate rejects > 80% of all unlock candidates for 3 consecutive months (shorts are perpetually crowded = the setup no longer exists)
  - 3 consecutive unlock shorts produce negative net P&L after costs (edge priced in at entry)

related: ["[[token-unlock-supply-event]]", "[[token-unlock-arbitrage]]", "[[funding-rate-arbitrage]]", "[[crowded-long-funding-fade]]", "[[crowded-short-funding-fade]]", "[[funding-filtered-momentum]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[token-unlocks]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Unlock Short with Crowding Gate

An unlock short with crowding gate is a [[token-unlock-supply-event|token unlock supply event]] short on a perp — shorting a crypto asset ahead of a large, scheduled cliff unlock — filtered through a **crowding gate** that only permits entry when the short side is *not already crowded*. The primitive edge (supply shock from forced insider/VC selling) exists in the [[token-unlock-supply-event]] and [[token-unlock-arbitrage]] pages. This page is about the **entry discipline**: when the obvious trade is already in everyone's book (deep negative funding, spiked short OI), the risk-reward has flipped — the crowd is already short, squeeze risk is high, and the trade's expected value is marginal or negative.

**How this differs from related strategies:**

- **[[token-unlock-supply-event]]** (Hyperliquid basket) — describes the event-edge and execution mechanics. Does not gate on crowding; enters the trade regardless of positioning.
- **[[token-unlock-arbitrage]]** — describes the unlock supply overhang and when the edge is strongest. Notes crowding risk but does not implement it as a quantitative gate.
- **This page** — the *combination* of the unlock primitive *and* a quantitative crowding gate. The gate is the new contribution; the event-edge theory is inherited from the existing pages.

## Edge source

Per [[edge-taxonomy]]:

- **Structural** — cliff vesting schedules are hard-coded in smart contracts; the supply event is inelastic and non-deferrable by the issuer. The supply shock is a contractual fact, not a prediction.
- **Informational** — vesting schedules are publicly disclosed (on-chain) but most participants do not track them systematically. The edge is reading the public schedule before it is universally priced in — an increasingly slim window as unlock trackers proliferate.
- **Behavioral** — the crowding gate specifically exploits the behavioral tendency for momentum traders to all enter the same "obvious" short simultaneously once the unlock is widely publicised. That crowding creates the squeeze risk that the gate screens out.

The gate's specific value is **behavioral edge preservation**: by screening for non-consensus setups, it selects for the cases where the trade has not been front-run by the same crowd that knows about it.

## Why this edge exists

Three mechanism layers:

1. **Supply shock is inelastic.** A VC fund at end-of-life must sell; a team member selling to pay tax must sell. The locked tokens become liquid on a specific date regardless of price. This inelastic supply hits a market with no guaranteed demand increase.
2. **Sellers are price-insensitive.** Tokens acquired at seed price ($0.02) being sold at market price ($2.00) represent 100× returns regardless; the seller is indifferent to selling at $2.00 vs $1.90. This creates a natural buyer-vs-seller informational asymmetry.
3. **The crowd follows the calendar but crowds the exit.** When a large unlock is publicised on unlock trackers 30 days in advance, most shorts enter early. Funding rates go negative (shorts pay longs) and OI spikes. The "obvious" short is often already priced in by the time of the event. The crowding gate filters for the cases where this front-running has *not* yet occurred — the market has not fully digested the upcoming supply shock.

**Who is on the other side of the gated trade:** buyers who confuse "unlock done = bullish" with reality, dip-buyers who expect mean-reversion after price has already declined, and market makers absorbing the OTC block that early VCs sell before the cliff (they need to re-hedge their net short from the OTC block by buying the perp). These buyers lose because the supply shock is real and ongoing; the gated shorter enters before these dynamics are fully priced in.

## Null hypothesis

Under the null, the crowding gate has zero marginal value: unlock shorts taken when funding is negative and OI is already short should perform equally to unlock shorts taken when funding is neutral and OI is not yet crowded. If the null is true, the gate reduces the number of trades without improving the win rate or risk-adjusted return on the remaining trades.

The null is rejected (gate has value) if the conditional win rate and Sharpe are materially higher for non-crowded entries than for crowded entries on the same unlock events. Testable hypothesis: sort historical unlock events by funding level 5 days before the cliff; the bottom quartile of funding (most crowded shorts) should show significantly worse subsequent Sharpe than the top quartile (least crowded). This test has not been run in this wiki (strategy is `backtest_status: untested`).

## Rules

### Step 1: Identify eligible unlocks

A qualifying unlock event must meet **all** of:

1. **Size threshold.** Unlock volume ≥ 5% of circulating supply on the cliff date, OR ≥ $5M USD value at current price.
2. **Unlock type.** Team/founder or VC/seed-fund cliff vesting (first 1-3 events). Linear monthly emissions are lower edge (often already priced in).
3. **Timing window.** Enter 5-14 days *before* the cliff. Entering after the cliff reduces the short side of the trade to a rebound-fade (different and weaker setup).
4. **Perp availability.** A liquid perpetual exists for the token on Hyperliquid or a major CEX with adequate OI depth (at least 2× the intended short notional in open interest).

### Step 2: Apply crowding gate (must PASS all)

1. **Funding gate.** Current 8h funding rate on the perp is ≥ **−0.03%** per 8h (~−33% APY annualised). If funding is more negative than −0.03%, the short side is already crowded — skip the trade. Rationale: deep negative funding means shorts are paying longs; the crowd is already massively short and expecting a large drop. The squeeze risk and the entry cost make this an unfavourable risk-reward.
2. **OI gate.** 7-day OI change on the perp is NOT spiked: OI change over the past 7 days is ≤ +20%. A 7-day OI spike of > 20% indicates that a large number of short positions have been added recently — likely other unlock-trade participants front-running.
3. **Sentiment gate (optional but recommended).** Social volume / sentiment around the token's unlock is NOT yet at an extreme (i.e., the unlock is not the top trending topic on Crypto Twitter for the past 48h). Extreme pre-announcement social volume indicates the trade is consensus; the gate should lean toward rejection.
4. **Macro regime.** Global market regime (`/api/v1/regimes/current`) is not in `Established Bear` or `Structural Shock` — in outright bear markets, all alts decline regardless of unlock; the carry signal is diluted by macro beta.

### Entry

- **Instrument.** Short the token's perp (Hyperliquid preferred for hourly funding and clean liquidation engine).
- **Entry timing.** Enter on the 4h bar close after the crowding gate is confirmed, ideally 5-14 days before the cliff.
- **Size.** Risk ≤ 2% of sleeve capital per unlock trade. ATR(14) position sizing: notional = `(risk_pct × sleeve) / (ATR_4h / price)`. Hard cap: maximum 5% of sleeve per position.
- **Stop placement.** Set a hard stop 15% above entry (price rally of 15% invalidates the downside thesis). This is aggressive; a strong macro bid or short-squeeze can override unlock sell pressure entirely.

### Exit

1. **Take profit.** Close 50% of the position at −10% from entry (first leg of supply absorption); hold remaining 50% to −20% or the funding gate reversal (funding starts returning to neutral as short-side pressure fades).
2. **Stop loss.** Close 100% if price rallies > 15% above entry — short-squeeze or macro override in progress.
3. **Funding reversal.** If funding becomes deeply negative (< −0.05%/8h) *after* entry, the trade has now joined a crowded book — exit half the position as crowding risk has increased.
4. **Time stop.** If the unlock date passes and price has not declined by more than 5%, close remaining position within 3 days post-cliff. Post-cliff buying from "dip buyers" can reverse quickly if the supply was pre-absorbed via OTC.

### Position sizing summary

- Per-trade risk: 2% of sleeve (ATR-sized), cap 5%.
- Maximum concurrent unlock trades: 2 (different tokens; avoid correlated pairs).
- Total sleeve allocation: 10-15% of overall book to event-driven strategies.

## Implementation pseudocode

```python
# unlock_short_gated.py — unlock event screener + crowding gate + sizing

UNLOCK_SUPPLY_PCT_MIN  = 0.05     # 5% of circulating supply
UNLOCK_VALUE_USD_MIN   = 5e6      # $5M minimum USD value
ENTRY_WINDOW_DAYS      = (5, 14)  # 5-14 days before cliff
FUNDING_GATE_MIN       = -0.0003  # -0.03%/8h; more negative = skip
OI_SPIKE_7D_MAX        = 0.20     # OI increase over 7 days must be < 20%
STOP_PCT               = 0.15     # 15% rally = hard stop
TAKE_PROFIT_PCT_1      = -0.10    # close 50% at -10%
TAKE_PROFIT_PCT_2      = -0.20    # close 50% at -20%
FUNDING_CROWD_EXIT     = -0.0005  # -0.05%/8h: funding crowded post-entry = trim
RISK_PER_TRADE         = 0.02     # 2% of sleeve
CAP_PER_TRADE          = 0.05     # 5% of sleeve hard cap
MAX_CONCURRENT         = 2
TIME_STOP_POST_CLIFF   = 3        # days after cliff to exit if no move
DRAWDOWN_KILL          = 0.25

from dataclasses import dataclass

@dataclass
class UnlockSignal:
    token: str
    days_to_cliff: int
    unlock_supply_pct: float
    unlock_value_usd: float
    unlock_type: str           # "team_founder", "vc_seed", "ecosystem", etc.
    funding_8h: float
    oi_7d_change_pct: float
    price: float
    atr_4h: float
    regime: str
    days_post_cliff: int = 0   # 0 if not yet past cliff

def qualifies(u: UnlockSignal) -> bool:
    return (u.unlock_supply_pct >= UNLOCK_SUPPLY_PCT_MIN
            and u.unlock_value_usd >= UNLOCK_VALUE_USD_MIN
            and ENTRY_WINDOW_DAYS[0] <= u.days_to_cliff <= ENTRY_WINDOW_DAYS[1]
            and u.unlock_type in {"team_founder", "vc_seed"})

def crowding_gate_pass(u: UnlockSignal) -> bool:
    return (u.funding_8h >= FUNDING_GATE_MIN
            and u.oi_7d_change_pct <= OI_SPIKE_7D_MAX
            and u.regime not in {"Established Bear", "Structural Shock"})

def decide(u: UnlockSignal, book: dict) -> dict:
    if book["strategy_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    pos = book["positions"].get(u.token)

    if pos is not None:  # manage existing short
        entry_px = pos["entry_price"]
        pnl_pct = (entry_px - u.price) / entry_px  # positive = profit for short
        if u.price > entry_px * (1 + STOP_PCT):
            return {"action": "EXIT_STOP", "token": u.token, "reason": "stop loss rally"}
        if u.funding_8h < FUNDING_CROWD_EXIT and pos.get("size_pct", 1.0) == 1.0:
            return {"action": "TRIM_50PCT", "token": u.token, "reason": "post-entry crowding"}
        if pnl_pct <= TAKE_PROFIT_PCT_1 and pos.get("size_pct", 1.0) == 1.0:
            return {"action": "TAKE_PROFIT_50PCT", "token": u.token, "reason": "first TP hit"}
        if pnl_pct <= TAKE_PROFIT_PCT_2:
            return {"action": "EXIT_FULL", "token": u.token, "reason": "second TP hit"}
        if u.days_to_cliff <= 0 and u.days_post_cliff >= TIME_STOP_POST_CLIFF and pnl_pct < 0.05:
            return {"action": "EXIT_FULL", "token": u.token, "reason": "time stop post-cliff"}
        return {"action": "HOLD", "token": u.token}

    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent"}
    if not qualifies(u):
        return {"action": "WAIT", "reason": "unlock does not qualify"}
    if not crowding_gate_pass(u):
        return {"action": "SKIP", "reason": f"crowding gate fail: funding={u.funding_8h:.4%}, OI7d={u.oi_7d_change_pct:.0%}"}

    risk_usd = RISK_PER_TRADE * book["sleeve_capital"]
    raw_notional = risk_usd / (u.atr_4h / u.price)
    notional = min(raw_notional, CAP_PER_TRADE * book["sleeve_capital"])
    return {
        "action": "SHORT",
        "token": u.token,
        "notional": notional,
        "stop_px": u.price * (1 + STOP_PCT),
        "tp1_px": u.price * (1 + TAKE_PROFIT_PCT_1),
        "tp2_px": u.price * (1 + TAKE_PROFIT_PCT_2),
        "reason": f"unlock {u.unlock_supply_pct:.0%} in {u.days_to_cliff}d; funding={u.funding_8h:.4%}, OI7d={u.oi_7d_change_pct:.0%}",
    }
```

The production system adds: daily unlock calendar polling (Token Unlocks, on-chain vesting contract monitoring), Hyperliquid funding/OI feed, regime API polling, and a manual kill switch.

## Indicators / data used

- **Token unlock calendar** — primary signal trigger; verified against on-chain vesting contract addresses
- **[[funding-rate]] (8h)** — crowding gate denominator; also the cost of holding the short
- **[[open-interest]] (7d change)** — OI crowding gate
- **ATR(14) on 4h** — position sizing
- **Circulating supply / FDV data** — unlock size gate (% of circulating supply)
- **Regime classification** (`/api/v1/regimes/current`) — macro gate

## Example trade

**Setup (illustrative):**

- Token: ALTX-PERP on Hyperliquid.
- Cliff unlock in 9 days (in the entry window). Team + VC: 12% of circulating supply (~$18M at current price). Passes size gate.
- Funding (8h): +0.005%/8h. Gate: +0.005% ≥ −0.03% → **PASS** (shorts are not crowded; longs are marginally bullish — most unusual for an unlock setup).
- 7d OI change: +8%. Gate: 8% ≤ 20% → **PASS**.
- Regime: "BTC-Led Bull". Gate: not Bear → **PASS**.
- All gates clear. Sleeve = $40,000. ATR(4h) = $0.08 ($1.60 price). Risk = 2% = $800. Notional = $800 / (0.08/1.60) = $800 / 0.05 = **$16,000** (above 5% cap of $2,000; cap applies → **$2,000 notional**).

**Entry:** Short ALTX-PERP at $1.60, $2,000 notional = 1,250 contracts. Stop: $1.84 (+15%). TP1: $1.44 (−10%, 50% size). TP2: $1.28 (−20%, remainder).

**Hold (11 days):** ALTX declines steadily as the cliff approaches. Funding remains at +0.005%/8h (longs are still bullish, paying modestly). Day 9: cliff hits. ALTX falls from $1.52 to $1.38 on the cliff day as team wallets begin distributing. TP1 triggered at $1.44 → close 625 contracts.

**Remaining position (625 contracts):** held for 3 more days. Price settles at $1.31. Exit at $1.31 (TP2 approximately reached; also time stop approaches).

**Net P&L:**
- TP1 leg: ($1.60 − $1.44) / $1.60 × $1,000 = +$100, less fees ~$1.80 = +$98.20.
- TP2 leg: ($1.60 − $1.31) / $1.60 × $1,000 = +$181.25, less fees ~$1.18 = +$180.07.
- Funding cost (long side paying 0.005%/8h over 11 days × 33 periods × $2,000): ~$3.30 total drag.
- **Net: ~$275 on $2,000 deployed in 11 days = ~13.75% return on the position** (illustrative; exceptional relative to position size).

*(Illustrative only. Most unlock trades will be smaller moves. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Higher than ungated unlock short (~0.6-0.7) due to avoiding crowded setups |
| Win rate (per gated trade) | ~55-65% | Gated subset excludes worst entries |
| Win rate (ungated, for comparison) | ~45-55% | Includes crowded-short setups with squeeze risk |
| Expected max drawdown | ~25% | Single-name stop of 15% + correlation across tokens in similar sectors |
| Breakeven cost budget | 40 bps | High relative to position hold period; funding drag significant if funding negative |
| Signal frequency | 2-5 gated events per month | Low; the gate rejects ~30-60% of unlock candidates |

**What the gate adds (rough estimate):** The gate removes the cases where shorts are crowded (deeply negative funding, spiked OI). Those cases historically have higher squeeze frequency: when a token's perp is at −0.05%/8h with +40% OI increase in 7 days, the short is the consensus trade and the funding drag adds cost while the squeeze risk amplifies the downside. Removing these cases is estimated to improve win rate by ~10 percentage points and average win/loss ratio by ~0.3× — sufficient to raise Sharpe from ~0.6-0.7 to ~0.9.

## Capacity limits

- **Per token**: ~$500k-$2M notional before the short position becomes visible in Hyperliquid's transparent order book and invites copy-trading or front-running.
- **Cross-token**: a maximum of 2 concurrent positions limits total exposure to ~$2-4M.
- **Calendar-driven**: capacity is ultimately bounded by the number of qualifying, non-crowded unlocks per month (~2-5 per month realistically).

## What kills this strategy

1. **Pre-announcement crowding (#4).** The unlock calendar is public; as more participants act on it earlier, the crowding gate rejects nearly all setups (shorts are crowded by the time the entry window opens). The kill criterion "gate rejects > 80% of candidates" detects this.
2. **Macro override (#5).** In a strong bull market, macro buying absorbs the entire unlock supply in OTC blocks before the cliff hits. The "supply shock" never appears in the perp price. The macro regime gate partially addresses this but cannot predict OTC absorption.
3. **Short squeeze (#6).** Even a non-crowded short can be squeezed by a positive catalyst coinciding with the unlock (a partnership announcement, a new listing, a macro-positive event). The 15% stop contains but does not eliminate this.
4. **Funding decay (#5).** If funding on mid/small-cap perps compresses toward zero (as the Hyperliquid ecosystem deepens), funding drag for holding the short post-cliff becomes less significant but so does the crowding signal's information value.
5. **On-chain data reliability (#7).** Vesting contract addresses must be verified; some protocols use multiple contract addresses or off-chain OTC deals that are not captured in standard unlock calendars.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 25%** from high-water mark.
2. **Rolling 3-month Sharpe < 0** on minimum 10 completed trades.
3. **Gate rejects > 80% of candidates** for 3 consecutive months.
4. **3 consecutive unlock shorts negative net P&L** after all costs.

Re-deploy when gate acceptance rate normalises and rolling Sharpe is positive on paper-trade for 30 days. See [[when-to-retire-a-strategy]].

## Advantages

- **Converts a crowded event trade into a disciplined, selective one.** The gate removes the worst expected-value entries (late shorts in a crowded book) at the cost of reduced frequency.
- **Informs complementary trades.** When the gate rejects a setup because shorts are crowded, that is itself useful information: a [[crowded-short-funding-fade]] or a post-cliff rebound long may be the better trade.
- **Low correlation with other strategies.** Calendar-driven event timing means the strategy fires independently of trend or carry regimes, providing genuine diversification.
- **Transparent, verifiable signal.** Funding rates and OI are public in real time; the gate criteria are auditable.

## Disadvantages

- **Low signal frequency.** A gate that rejects 30-60% of unlocks produces 2-5 trades per month — too few for reliable Sharpe estimation in the short term.
- **Single-name risk.** Each unlock trade is a single-token bet with high idiosyncratic risk (protocol upgrade, listing, partnership) that cannot be diversified away.
- **Pre-cliff return decay.** As the unlock tracker ecosystem matures, the edge of entering 5-14 days before the cliff compresses. The gate may need to move the entry window earlier to stay ahead of the crowd.
- **Perp funding drag.** If positive (which passes the gate), funding drag on the short is a daily cost even when the trade is working. A 0.03%/8h rate over 14 days = 33% APY × 14/365 ≈ 1.3% drag on notional.

## Sources

- [[token-unlock-supply-event]] — the underlying event-edge page and Hyperliquid basket description.
- [[token-unlock-arbitrage]] — the broader unlock arbitrage framework with unlock typology.
- Coinglass unlock calendar; Token Unlocks (TokenUnlocks.app) — the public data sources for the unlock calendar signal.
- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (2023). The basis for using funding as a crowding signal.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding rate (crowding gate, generalise to token's coin param)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI level and trend (OI spike gate)
- `GET /api/v1/event/regime` — forward catalyst calendar including unlock events
- `GET /api/v1/event/calendar?type=unlock&days=14` — filterable unlock calendar with directional bias
- `GET /api/v1/regimes/current` — current market regime (macro gate)

**Historical data:**
- `GET /api/v1/derivatives/binance/history?days=90` — funding + OI history for gate calibration
- `GET /api/v1/backtesting/funding` — deep funding archive for multi-unlock backtest

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar?type=unlock"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]], [[cryptodataapi-derivatives]].

## Related

- [[token-unlock-supply-event]] — the event primitive (Hyperliquid basket)
- [[token-unlock-arbitrage]] — the broader unlock arbitrage framework
- [[funding-filtered-momentum]] — similar funding-gate architecture applied to momentum entries
- [[crowded-short-funding-fade]] — what to trade when the gate *rejects* an unlock short (shorts already crowded)
- [[crowded-long-funding-fade]] — the complement for crowded longs
- [[funding-rate]] — the crowding-gate signal mechanics
- [[open-interest]] — the OI spike gate
- [[perpetual-futures]] — the instrument used for the short
- [[token-unlocks]] — the concept page on vesting mechanics
- [[edge-taxonomy]] — structural + informational + behavioral classification
- [[failure-modes]] — crowding, macro override, and squeeze risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
