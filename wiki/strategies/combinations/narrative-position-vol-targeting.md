---
title: "Narrative Position Vol Targeting"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, momentum, volatility, risk-management, behavioral-finance, memecoins, event-driven, quantitative, crypto, altcoins]
aliases: ["Narrative Book Vol Sizing", "Vol-Scaled Narrative Trading", "Risk-Contribution Narrative Sizing", "Meme-Vol Risk Budget"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, informational, analytical]
edge_mechanism: "Narrative and memecoin trading harvests capital-rotation and attention-driven price momentum; hot high-vol names dominate portfolio risk in a fixed-notional book because their realized vol is 3-10x that of BTC/ETH — vol targeting equalises each position's risk contribution so no single narrative can disproportionately blow up the book even if the narrative call is right, and the portfolio heat cap prevents concurrent narrative overload from creating correlated blow-up risk."

data_required: [ohlcv-daily, ohlcv-4h, realized-vol-calc, funding-rates, market-cap, sector-flows]
min_capital_usd: 10000
capacity_usd: 25000000
crowding_risk: high

expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 40

decay_evidence: "Narrative/memecoin momentum is documented as highly crowded; alpha decays rapidly as copy-trade flows follow the same signals. The vol-targeting overlay does not address the narrative signal quality — it addresses the sizing problem. The sizing improvement (higher Sharpe from better risk allocation) is structural and should persist as long as cross-narrative vol dispersion persists. The narrative edge itself is the primary decay concern: see [[narrative-trading]] and [[meme-coin-cycle]]."

kill_criteria: |
  - book drawdown > 25% from high-water mark
  - 3 consecutive narrative trades where vol-targeted size is filled but the position blows through 2× the target-risk budget before the exit signal fires (realized vol is consistently underestimated; recalibrate vol lookback window)
  - average realized vol at position close is > 3× the entry estimated vol for 5+ consecutive positions (hot narratives are arriving with vol already elevated; vol estimate is stale by the time position is opened)
  - portfolio heat cap (concurrent narrative exposure) is maxed > 50% of trading days in a rolling 90-day window (the strategy is over-deployed; reduce heat cap threshold)
  - vol-targeted position sizing produces sizes below minimum viable trade (< 0.1% of portfolio) for > 60% of narrative candidates screened (book is too large relative to available liquid narrative plays)

related: ["[[vol-targeted-trend-following]]", "[[narrative-trading]]", "[[narrative-with-trend-confirmation]]", "[[meme-coin-cycle]]", "[[risk-budgeting]]", "[[volatility-targeting]]", "[[unlock-aware-momentum]]", "[[funding-filtered-momentum]]", "[[behavioral-finance]]", "[[perpetual-futures]]", "[[altcoins]]", "[[memecoins]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Narrative Position Vol Targeting

Narrative position vol targeting applies **volatility-scaled position sizing** to a narrative/memecoin book so that each individual trade contributes an equal amount of realized-volatility risk to the portfolio, regardless of how hot (high-vol) the narrative name is. The primitive is [[narrative-trading]] — entering positions in tokens driven by a dominant current story (AI agent cycle, DePIN, restaking, meme supercycles) before the crowd fully prices the capital rotation. The overlay is a per-position vol-targeting rule: each position is sized to a fixed **risk contribution** (e.g., 1% of portfolio as 20-day realised vol × notional), plus a **portfolio heat cap** that limits the total concurrent narrative exposure across the whole book.

**This is explicitly differentiated from [[vol-targeted-trend-following]]** — that page applies vol targeting to a BTC/ETH/major-crypto trend book: the universe is large-cap perps, the signal is multi-week trend/momentum, and vol is used to equalise the risk of each trend entry across the major assets. This page applies vol targeting to the **narrative and memecoin book**: the universe is high-vol small/mid-cap tokens driven by rotating themes; vol dispersion within the book is 5–10× wider (a SOL-ecosystem memecoin might have 400% annualised realized vol while a BTC trend position has 60%); without sizing correction, a single hot narrative completely dominates portfolio risk.

**This is differentiated from [[narrative-with-trend-confirmation]]** — that page determines **when to enter** a narrative trade (requires breakout or higher-low confirmation before entry). This page determines **how much to put on** once the entry signal from any narrative strategy fires. The two pages are composable: narrative-with-trend-confirmation defines entry; this page defines sizing.

**This is differentiated from [[risk-budgeting]]** — that page applies risk-parity or HRP allocation to a diversified multi-asset portfolio at the portfolio-construction level (strategic weights, weekly rebalance). This page applies vol-targeting at the **individual trade level** within a single narrative sub-book, dynamically sizing each new position at entry time based on current realized vol of that specific token.

## Edge source

Per [[edge-taxonomy]], **behavioral + informational + analytical**:

- **Behavioral (primary)** — narrative and memecoin price action is driven by social attention, influencer amplification, and herd-capital rotation. The price momentum that follows narrative adoption is a behavioral overshoot funded by late retail. This is the [[narrative-trading]] primitive's edge.
- **Informational** — early identification of the prevailing narrative (before it becomes consensus, when social volume is just starting to surge) gives an entry advantage. This page does not improve the informational edge; it ensures that the informational edge is not wasted on a correctly-identified narrative that happens to be so volatile it blows the portfolio before the move completes.
- **Analytical (primary of the overlay)** — the vol-targeting arithmetic is a quantitative improvement over intuitive or fixed-notional sizing. The analytics of equal risk contribution — sizing so that each position's 20-day realized vol × notional equals the same dollar-risk target — is a well-documented Sharpe-improving technique in the CTA literature ([[vol-targeted-trend-following]]). Applying it to the narrative book is an analytical enhancement.

## Why this edge exists

**Two problems in a fixed-notional narrative book that vol targeting fixes:**

1. **Hot names dominate risk without dominating expected return.** A SOL-ecosystem memecoin with 300% annualised realized vol and the same $10,000 fixed-notional position as a Ethereum staking narrative token at 80% vol contributes 3.75× the risk to the portfolio. If the sizing logic is "same dollar amount in each narrative," the book's P&L is dominated by which meme happened to be the most volatile — not which narrative was most correctly identified. Vol targeting equalises the risk contribution so each narrative gets a fair chance to contribute to P&L.

2. **Concurrent narrative overload creates correlated crash risk.** Running 5–7 concurrent narrative trades in a bullish market can create a highly correlated book: when crypto risk-off hits, all narratives sell off simultaneously. The portfolio heat cap — a total-book vol cap across all concurrent positions — limits the correlated drawdown from a market-wide rotation out of high-beta narratives.

**Who is on the other side:** late retail capital chasing the same narratives after they have become consensus — the crowd provides the exit liquidity. The vol-targeting overlay does not change the counterparty; it ensures the trade is sized to survive long enough to reach the crowd-driven exit, rather than being stopped out early by vol noise.

## Null hypothesis

Under the null, the vol-targeting overlay produces **no incremental Sharpe improvement** over a fixed-notional narrative book:
- Equal-risk-contribution sizing across narrative positions should not produce a higher Sharpe than fixed-notional sizing, net of the rebalancing friction introduced by vol-scaling.
- The portfolio heat cap should not reduce drawdown without proportionally reducing expected return.
- The analytical sizing improvement should not overcome the noise in 20-day realized vol estimates for short-duration narrative positions.

Currently not rejected (`backtest_status: untested`). The null is plausible for short-duration meme trades (< 7 days) where the 20-day vol lookback is longer than the trade horizon. The overlay is more clearly beneficial for multi-week narrative trades where the vol estimate is stable and meaningful. Testable prediction: vol-targeted narrative book Sharpe ≥ 1.3× fixed-notional book Sharpe over a 12-month sample with ≥ 20 narrative trades.

## Rules

### Per-position sizing

**Step 1: Estimate current realized vol for the narrative name**
- Compute 20-day annualised realized vol (close-to-close log returns): `RV_20d = std(log_returns_20d) × √365`.
- If the token has fewer than 20 days of price history, use the sector-average RV or decline to size the position at all (insufficient vol estimate).

**Step 2: Calculate vol-targeted position size**
- Set the **daily dollar risk target** per position: `T = portfolio_capital × 0.01` (1% of portfolio as the daily vol risk budget per position).
- Vol-targeted notional: `N = T / (RV_20d / √365)` — equivalent to `N = T × √365 / RV_20d`.
- Example: portfolio = $100,000; T = $1,000; RV_20d for a DePIN narrative token = 180% annualised → daily vol = 180 / √365 = 9.4% → N = $1,000 / 0.094 = **$10,638 notional**.
- Example: portfolio = $100,000; T = $1,000; RV_20d for a memecoin = 400% annualised → daily vol = 400 / √365 = 20.9% → N = $1,000 / 0.209 = **$4,785 notional**.
- The high-vol memecoin gets a 55% smaller notional than the moderate-vol DePIN token for the same 1% daily risk budget.

**Step 3: Apply per-position caps**
- **Minimum position:** `N ≥ 0.1%` of portfolio (below this, the position is uneconomical; skip the narrative).
- **Maximum position:** `N ≤ 5%` of portfolio (single-position cap regardless of how low the vol estimate is; prevents concentration in anomalously low-vol narratives).

### Portfolio heat cap

**Step 4: Check concurrent narrative exposure**
- Before entering a new narrative position, compute **total book delta** = sum of current open narrative positions as a fraction of portfolio.
- **Heat cap:** total narrative book notional ≤ **25% of portfolio**.
- If entering the new position would exceed 25%, either reduce the size of the new entry proportionally or skip the entry until another position exits.
- **Portfolio-level vol cap:** sum of all narrative positions' (notional × daily RV) ≤ **2.5% of portfolio** (total portfolio-level daily risk from the narrative book).

### Entry and exit signals

This page is signal-agnostic — use any of the following narrative entry triggers:
- [[narrative-with-trend-confirmation]] entry rules (breakout/higher-low + trend confirmation)
- [[meme-coin-cycle]] entry signal (narrative phase identification)
- Social volume surge + early price-action confirmation (social arbitrage entry)

**Exit triggers (any fires, close the position):**
- Narrative fade signal fires (social volume declining, sector flows rotating out, major narrative catalyst resolved).
- Vol-targeted stop: position loses **2.5× the daily risk budget** (`2.5 × T`) from entry — this is a dynamic stop based on the same vol logic as the entry size.
- Time exit: close after **21 days** if neither profit target nor stop has been reached (narrative trades that don't resolve within 3 weeks are typically dead).
- Portfolio heat cap breach: if the overall book exceeds the heat cap due to correlated gains increasing notional, trim the largest positions.

## Implementation pseudocode

```python
# narrative_position_vol_targeting.py

from dataclasses import dataclass
from typing import Optional
import math

# ---- sizing parameters ----
RISK_BUDGET_PCT_PORTFOLIO    = 0.01    # 1% of portfolio as daily-vol risk per position
MIN_POSITION_PCT             = 0.001   # 0.1% minimum position
MAX_POSITION_PCT             = 0.05    # 5% maximum single position
PORTFOLIO_NOTIONAL_CAP       = 0.25    # 25% total narrative book notional cap
PORTFOLIO_DAILY_VOL_CAP      = 0.025   # 2.5% total daily vol risk across book
MIN_HISTORY_DAYS             = 14      # minimum price history for vol estimate

# ---- exit parameters ----
STOP_MULT_OF_DAILY_RISK      = 2.5     # stop loss = 2.5× daily risk budget
MAX_HOLD_DAYS                = 21      # time exit after 21 days

@dataclass
class NarrativeToken:
    symbol:              str
    price:               float
    log_returns_20d:     list[float]   # list of 20 daily log-returns
    history_days:        int

@dataclass
class BookState:
    portfolio_capital:   float
    open_positions:      list[dict]    # each: {symbol, notional, entry_price, days_held, daily_risk}

def estimate_rv_20d(log_returns: list[float]) -> Optional[float]:
    """Annualised realised vol from daily log returns."""
    if len(log_returns) < 14:
        return None
    n = len(log_returns)
    mean = sum(log_returns) / n
    variance = sum((r - mean) ** 2 for r in log_returns) / (n - 1)
    daily_vol = math.sqrt(variance)
    return daily_vol * math.sqrt(365)

def compute_vol_targeted_size(portfolio_capital: float, rv_20d_annual: float) -> dict:
    """Returns vol-targeted notional and the daily dollar risk this implies."""
    daily_vol = rv_20d_annual / math.sqrt(365)
    risk_budget = portfolio_capital * RISK_BUDGET_PCT_PORTFOLIO
    raw_notional = risk_budget / daily_vol if daily_vol > 0 else 0
    notional = max(
        portfolio_capital * MIN_POSITION_PCT,
        min(raw_notional, portfolio_capital * MAX_POSITION_PCT)
    )
    daily_risk = notional * daily_vol
    return {
        "notional":      notional,
        "daily_risk":    daily_risk,
        "rv_20d_annual": rv_20d_annual,
        "daily_vol_pct": daily_vol,
    }

def heat_cap_check(book: BookState, new_notional: float, new_daily_risk: float) -> tuple[bool, str]:
    current_notional = sum(p["notional"] for p in book.open_positions)
    current_daily_vol = sum(p["daily_risk"] for p in book.open_positions)
    if (current_notional + new_notional) / book.portfolio_capital > PORTFOLIO_NOTIONAL_CAP:
        return False, (f"heat cap: book notional {(current_notional + new_notional)/book.portfolio_capital:.1%} "
                       f"> {PORTFOLIO_NOTIONAL_CAP:.0%} cap")
    if (current_daily_vol + new_daily_risk) / book.portfolio_capital > PORTFOLIO_DAILY_VOL_CAP:
        return False, (f"vol cap: book daily vol {(current_daily_vol + new_daily_risk)/book.portfolio_capital:.2%} "
                       f"> {PORTFOLIO_DAILY_VOL_CAP:.1%} cap")
    return True, "heat cap OK"

def entry_decision(token: NarrativeToken, book: BookState, signal_confirmed: bool) -> Optional[dict]:
    if not signal_confirmed:
        return None
    rv = estimate_rv_20d(token.log_returns_20d)
    if rv is None:
        return {"action": "SKIP", "reason": f"insufficient history ({token.history_days}d < {MIN_HISTORY_DAYS}d)"}
    sizing = compute_vol_targeted_size(book.portfolio_capital, rv)
    ok, heat_reason = heat_cap_check(book, sizing["notional"], sizing["daily_risk"])
    if not ok:
        return {"action": "SKIP", "reason": heat_reason}
    stop_level = token.price * (1 - STOP_MULT_OF_DAILY_RISK * sizing["daily_vol_pct"])
    return {
        "action":        "ENTER",
        "symbol":        token.symbol,
        "notional":      sizing["notional"],
        "entry_price":   token.price,
        "stop_price":    stop_level,
        "daily_risk":    sizing["daily_risk"],
        "rv_20d":        rv,
        "note": (f"vol-targeted: notional={sizing['notional']:.0f}, "
                 f"RV={rv:.0%}/yr, daily_vol={sizing['daily_vol_pct']:.2%}, "
                 f"daily_risk={sizing['daily_risk']:.0f} ({sizing['daily_risk']/book.portfolio_capital:.2%} of portfolio)"),
    }

def exit_decision(position: dict, current_price: float) -> Optional[dict]:
    entry_price = position["entry_price"]
    notional    = position["notional"]
    daily_risk  = position["daily_risk"]
    days_held   = position["days_held"]
    stop_loss   = entry_price * (1 - STOP_MULT_OF_DAILY_RISK * (daily_risk / notional))
    if current_price <= stop_loss:
        pnl = (current_price - entry_price) / entry_price
        return {"action": "CLOSE_STOP",
                "reason": f"price {current_price:.4f} ≤ vol-stop {stop_loss:.4f}; loss = {pnl:.1%}"}
    if days_held >= MAX_HOLD_DAYS:
        return {"action": "CLOSE_TIME", "reason": f"{MAX_HOLD_DAYS}d time exit"}
    return None
```

The production system adds: a narrative signal aggregator that monitors social volume (CryptoDataAPI sentiment endpoints, Nansen narratives, sector-flow data) to generate the entry signal; a daily vol recalculation to adjust the stop level as the position ages; and a book-level dashboard showing per-position risk contribution and aggregate heat.

## Indicators / data used

- **Realized vol (20-day)** — computed from `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=30`; close-to-close log-return standard deviation × √365. The primary sizing input.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin={TOKEN}`; context check — if funding is negative (crowd is shorting), the narrative trade may be entering against positioning headwind.
- **Market cap / token price** — `GET /api/v1/coins/{symbol}` or market data endpoint; used to convert notional to token units and check minimum viable trade size.
- **Sentiment / social volume** — `GET /api/v1/sentiment/fear-greed-index` for macro context; narrative-specific social volume requires external tools (Santiment, Nansen narrative dashboard) — not a current CryptoDataAPI endpoint.
- **Sector flows / regime** — `GET /api/v1/regimes/current`; if `Risk_Off` or `Structural_Shock`, the heat cap should be reduced to 10% of portfolio (narrative trades are highly correlated to risk appetite).
- **DEX / token data** — for memecoin narratives: `GET /api/v1/dex/*` endpoints for on-chain liquidity context; minimum $2M daily DEX volume for a narrative name to be tradeable at meaningful size.

*Note: narrative-specific social volume and KOL-amplification signals are not currently available via CryptoDataAPI; supplement with Santiment or LunarCrush for social-volume confirmation of the entry signal.*

## Example trade

**Setup (illustrative — DePIN narrative cycle entry, two concurrent positions):**

- Portfolio: $50,000. Risk budget per position: 1% × $50,000 = $500/day.
- Portfolio heat cap: 25% × $50,000 = $12,500 max notional.

**Position 1: IOTX (DePIN narrative name)**
- 20-day RV = 160% annualised. Daily vol = 160 / √365 = 8.37%.
- Vol-targeted notional = $500 / 0.0837 = **$5,974**. Within 5% cap ($2,500 max — uses $2,500 cap check: 5% × $50,000 = $2,500... actually $5,974 < $2,500 is false; $5,974 > $2,500 so cap applies: **$2,500**).

*Wait — let me recalculate. The 5% cap is $2,500. The raw vol-targeted notional $5,974 exceeds it — use $2,500.*

- Entry: IOTX at $0.082. Notional $2,500 / $0.082 = **30,488 IOTX**. Daily risk = $2,500 × 0.0837 = **$209**.
- Vol-stop: $0.082 × (1 − 2.5 × 0.0837) = $0.082 × 0.791 = **$0.0649** stop.

**Position 2: RENDER (AI-GPU narrative name)**
- 20-day RV = 95% annualised. Daily vol = 95 / √365 = 4.97%.
- Vol-targeted notional = $500 / 0.0497 = **$10,060**. Above 5% cap ($2,500) → cap applies: **$2,500**.
- Entry: RENDER at $7.40. Notional $2,500 / $7.40 = **338 RENDER**. Daily risk = $2,500 × 0.0497 = **$124**.

Heat check: $2,500 + $2,500 = $5,000 / $50,000 = 10% < 25% heat cap. Book daily vol = $209 + $124 = $333 / $50,000 = 0.67% < 2.5% vol cap. Both positions entered.

**Scenario A — DePIN narrative runs:**
- After 9 days, IOTX has risen from $0.082 to $0.148 (+80.5%). RENDER has risen from $7.40 to $8.90 (+20.3%).
- Narrative fade signal fires for DePIN sector (social volume declining). Both positions closed.
- IOTX P&L: ($0.148 − $0.082) × 30,488 = +$2,012. RENDER P&L: ($8.90 − $7.40) × 338 = +$507.
- **Total: +$2,519** on $5,000 notional / +5.04% of portfolio.

**Scenario B — IOTX stopped out, RENDER runs:**
- IOTX drops to $0.0649 (stop hit) after 4 days. Loss: ($0.0649 − $0.082) × 30,488 = **−$521** (−1.04% portfolio).
- RENDER continues rising to $11.20 (+51.4%) over 15 days. Close on narrative fade.
- RENDER P&L: ($11.20 − $7.40) × 338 = +$1,284 (+2.57% portfolio).
- **Net: −$521 + $1,284 = +$763** / +1.53% of portfolio.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Vol targeting improves Sharpe vs fixed-notional; narrative alpha is the primary driver; highly variable by cycle |
| Expected max drawdown | ~25% | Correlated narrative sell-off in risk-off events; heat cap limits but does not eliminate concurrent losses |
| Win rate (per narrative) | ~40–55% (estimated) | Narrative trades have modest win rates; large wins on correct narratives must overcome frequent small losses |
| Average win / loss ratio | ~2.5–4× (estimated) | Narrative trades that work tend to produce large multiples; vol-targeted stops limit losses to ~2.5× daily risk |
| Breakeven cost budget | 40 bps | Altcoin/memecoin taker fees 8–15 bps; funding costs if perp-expressed; slippage in thin altcoin markets; 40 bps budget is achievable for liquid mid-cap narratives |
| Signal frequency | 10–25 trades per year | Active narrative cycles generate more trades; bear markets reduce signal frequency |

**Cost overlay:** the dominant costs are altcoin-specific: wide bid-ask spreads in low-cap names, funding on perp-expressed positions, and slippage on exit when narratives fade and liquidity thins. The vol-targeting overlay does not increase cost; it simply shifts notional from high-vol names (where spread costs are also highest) to lower-vol names (where spreads are relatively tighter).

## Capacity limits

- **Per narrative name:** liquid mid-cap altcoin perps (Hyperliquid) can support $500K–$2M per entry without significant slippage. Small-cap and memecoin names may support only $50K–$200K at acceptable slippage.
- **Aggregate:** `capacity_usd: 25000000` is constrained by the small-cap universe of narrative names. At $25M AUM, the 5% single-position cap = $1.25M per position — achievable only in the most liquid narrative perp markets.
- **Memecoin-specific:** spot-only memecoins (no perp available) have much lower capacity due to DEX liquidity. The strategy is best suited to mid-cap tokens with Hyperliquid or Binance perp listings.

## What kills this strategy

1. **Narrative alpha decay (#4: Crowding).** Narrative and memecoin alpha is the most fragile component. As copy-trade platforms and social-signal aggregators proliferate, early-narrative entries become more crowded and the alpha window narrows from days to hours. The vol targeting overlay does not help here — it improves the risk structure but cannot create alpha where none exists.
2. **Vol underestimation for new tokens (#1: Primitive degradation).** 20-day realized vol for a newly launched token may be far below the true forward vol (the token hasn't experienced a major regime yet). Using a sector-average vol as a floor mitigates this; but the stop level based on underestimated vol will be set too wide, allowing losses to exceed the risk budget before triggering.
3. **Correlated narrative crash (#3: Market-structure regime change).** In a sharp risk-off event, all narrative/memecoin positions sell off simultaneously and violently. Even with a 25% heat cap, a 15–20% single-day move in the altcoin complex can produce portfolio losses of 3–5% in one day. The portfolio daily vol cap (2.5%) is breached in these events.
4. **Illiquidity at exit (#7: Operational).** Narrative fade exits — when the narrative is visibly turning — often coincide with all narrative traders exiting simultaneously. Slippage on exits can be 3–8% in low-cap names, wiping out the volatility-targeting precision of the sizing.
5. **Vol targeting reduces position size in the best narratives (#2: Cost structure of sorts).** The highest-vol narrative names tend to be the ones with the most explosive potential. Reducing position size in the most volatile names (which vol targeting does) mechanically reduces exposure to the best opportunities. This is a deliberate tradeoff: lower variance at the cost of capped upside.

## Kill criteria

Pause on any of:

1. **Book drawdown > 25%** from high-water mark — narrative alpha is not being captured; the signal quality or execution is degraded.
2. **3 consecutive positions where realized loss > 2× the target daily risk budget** — the vol estimate is consistently underestimating actual volatility; extend the lookback window to 30 days or add a vol-of-vol multiplier.
3. **Average realized vol at close is > 3× entry estimated vol for 5+ consecutive positions** — hot narrative positions are being entered after vol has already spiked; add a vol-percentile gate (do not enter if current RV > 150% of 30-day average for that token).
4. **Portfolio heat cap maxed > 50% of trading days in rolling 90 days** — the strategy is being over-deployed; reduce the heat cap to 15% to enforce tighter selectivity.
5. **Vol-targeted size < 0.1% of portfolio for > 60% of narrative candidates** — the book is too large for the available liquid narrative universe; reduce portfolio capital allocated to this sleeve or lower the minimum position cap.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Prevents single-narrative domination of portfolio risk** — without vol targeting, a correctly-identified high-vol narrative (500% annualised RV) will produce a 5–10× larger impact on portfolio P&L than a correctly-identified moderate-vol narrative. Vol targeting ensures each narrative idea gets equal risk airtime.
- **Portfolio heat cap prevents correlated blow-up** — the cap on concurrent narrative exposure limits the damage from market-wide altcoin risk-off events that hit all narratives simultaneously.
- **Dynamic stop logic scales with the position's own vol** — the stop is set in vol-adjusted space, not as a fixed percentage. This means the stop for a 400% RV memecoin is set tighter in absolute dollar terms, preventing runaway losses.
- **Signal-agnostic sizing** — the vol-targeting arithmetic can be applied to any narrative entry signal (trend confirmation, social volume surge, on-chain flow). It is a sizing wrapper, not a signal generator.

## Disadvantages

- **Reduces size in the best (highest-vol) opportunities** — vol targeting mechanically cuts the largest positions in the most explosive narratives. In bull markets where the highest-vol names produce the largest multiples, the strategy underperforms a fixed-notional book that happened to be concentrated in those names.
- **20-day RV lookback is stale for short-duration narratives** — a narrative that launches, peaks, and fades within 7 days is poorly served by a 20-day vol estimate from the same token's quiet pre-launch period. The vol estimate is structurally behind for newly-launched tokens.
- **Heat cap is blunt** — the 25% notional cap is a simple constraint; it does not account for correlation between concurrent narratives (AI tokens and DePIN may be highly correlated). A correlation-adjusted heat cap would be more precise but significantly more complex.
- **Requires per-token RV computation** — the narrative universe may contain dozens of tokens; computing and maintaining 20-day RV for each active candidate requires a data pipeline that goes beyond a standard portfolio management system.

## Sources

- [[vol-targeted-trend-following]] — the canonical vol-targeting application to the trend/momentum book; this page is the direct adaptation of the same sizing methodology to the narrative sub-book.
- [[narrative-trading]] — the primitive; defines the behavioral mechanism (capital rotation into dominant stories) that this page's sizing overlay improves.
- [[risk-budgeting]] — the portfolio-theory foundation of risk-contribution sizing; this page applies the risk-budgeting insight (equal risk allocation) at the individual trade level rather than the portfolio-construction level.
- [[meme-coin-cycle]] — the memecoin-specific narrative cycle; provides the signal infrastructure that feeds entry triggers for this page's sizing rules.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=30` — daily OHLCV for 20-day realised vol calculation (the primary sizing input)
- `GET /api/v1/derivatives/funding-rates?coin={TOKEN}` — funding context check for perp-expressed narrative positions
- `GET /api/v1/regimes/current` — macro regime; reduce heat cap to 10% if `Risk_Off` or `Structural_Shock`
- `GET /api/v1/sentiment/fear-greed-index` — book-level risk-appetite context; Fear & Greed < 30 reduces heat cap
- `GET /api/v1/dex/tokens` or `GET /api/v1/coins/{symbol}` — token market cap and liquidity context; filter out tokens below minimum DEX volume threshold

**Historical data:**
- `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=90` — 90-day daily OHLCV for vol regime history and lookback calibration
- `GET /api/v1/derivatives/binance/history?days=90` — cross-asset derivatives context for calibrating sector-average vol floors

*Note: narrative-specific social volume and sector-capital-rotation data require external sources (Santiment, Nansen, LunarCrush). These are not currently available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=RENDERUSDT&interval=1d&limit=30"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], [[cryptodataapi-sentiment]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [long-term regimes](https://cryptodataapi.com/regimes) · [fear & greed](https://cryptodataapi.com/fear-greed) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this sizing overlay end-to-end:

- **Sizing** — `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=30` per token feeds the 20-day realised-vol input; position weight = target vol / realised vol, capped by the book heat limit
- **Regime gate** — `GET /api/v1/regimes/current` plus the Fear & Greed read cut the heat cap in risk-off states before any per-token sizing runs
- **Batch sizing** — `GET /api/v1/quant/coins/risk?horizon=24h` returns per-coin vol-target multipliers for 180+ coins in one call — a ready-made cross-check on locally computed vol weights
- **Backtest** — replay sizing decisions on `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) and pair them with point-in-time regime state from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid lookahead in the heat-cap rules
- **Tips** — respect `insufficient_history` flags: a narrative token with fewer than 30 daily bars gets the sector-average vol floor, not its own noisy estimate
- **Prompt library** — the "Volatility-Aware Position Sizer" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) handles the vol-targeting leg; layer the narrative filter on top

## Related

- [[vol-targeted-trend-following]] — the trend-book analog of this page's narrative-book vol targeting; same sizing mechanic, different universe
- [[narrative-trading]] — the primitive; narrative entry signal generation and cycle identification
- [[narrative-with-trend-confirmation]] — entry timing for narrative trades; composable with this page's sizing overlay
- [[meme-coin-cycle]] — memecoin narrative cycle; provides the high-vol entry candidates for this page's sizing logic
- [[risk-budgeting]] — portfolio-theory foundation of equal risk contribution at the portfolio level
- [[volatility-targeting]] — the general vol-targeting concept
- [[unlock-aware-momentum]] — momentum/narrative book that adjusts for unlock supply risk; adjacent risk-management overlay for the same universe
- [[funding-filtered-momentum]] — momentum entries gated by funding; applicable to perp-expressed narrative positions
- [[behavioral-finance]] — the psychological mechanisms driving narrative price momentum
- [[altcoins]] — the primary universe for narrative trading
- [[memecoins]] — the high-vol tail of the narrative universe
- [[perpetual-futures]] — the perp instrument for narrative positions where available
- [[edge-taxonomy]] — behavioral + informational + analytical classification
- [[failure-modes]] — narrative alpha decay, vol underestimation, correlated crash
- [[when-to-retire-a-strategy]] — kill vs pause framework
