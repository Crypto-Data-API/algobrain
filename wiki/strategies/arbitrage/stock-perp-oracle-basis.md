---
title: "Stock Perp Oracle Basis"
type: strategy
created: 2026-04-27
updated: 2026-04-27
status: excellent
tags: [arbitrage, crypto, defi, stocks, perpetual-futures, basis-trade, oracle, market-microstructure, mean-reversion, quantitative]
aliases: ["Stock Perp Basis", "Off-Hours Perp Arb", "Pyth Oracle Drift Trade", "Stock-Perp Convergence", "NYSE-Closed Perp Fade"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto, stocks]
complexity: intermediate
backtest_status: live
edge_source: [structural, informational, behavioral]
edge_mechanism: "When the NYSE is closed, the cash side of the basis cannot trade, so the on-chain perp drifts on speculator flow with no arbitrage anchor. The drift mean-reverts at market open as cash-side arbitrage capital returns and pulls the perp back to oracle / cash price."
data_required: [pyth-oracle-feed, perp-mark-price, nyse-calendar, holiday-calendar, perp-funding-rate]
min_capital_usd: 5000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 1.5
expected_max_drawdown: 0.20
breakeven_cost_bps: 15
decay_evidence: "Strategy is new — Aster's 24/7 stock perpetuals launched July 2025; Hyperliquid HIP-3 equity perps launched October 2025. No long-term decay history exists yet. Expect compression as Pyth and competitor oracles add genuine after-hours equity feeds and as more arbitrage capital concentrates on the trade."
deploy_date: 2026-04-01
capital_allocation: "11.25% of book per stock x max 8 concurrent stocks (~90% notional, 2x leveraged)"
kill_criteria: |
  - 30-day rolling Sharpe < 0
  - 3 consecutive earnings-night blow-ups in a single quarter
  - Pyth (or upstream oracle) adds continuous after-hours equity pricing that matches perp mark
  - perp DEX changes funding / oracle anchor mechanism
  - sustained drawdown > 20% on book
related: ["[[basis-trading]]", "[[funding-rate-arbitrage]]", "[[pyth-network]]", "[[perpetual-futures]]", "[[mean-reversion]]", "[[after-hours-trading]]", "[[asterdex]]", "[[oracle-manipulation]]", "[[overnight-vs-intraday]]", "[[hyperliquid]]", "[[asterdex-perp-trading-map]]"]
---

# Stock Perp Oracle Basis

The **Stock Perp Oracle Basis** trade fades the price drift between an on-chain stock perpetual (e.g., AAPL-PERP, TSLA-PERP on [[asterdex|AsterDEX]]) and its [[pyth-network|Pyth oracle]] reference price during hours when the [[after-hours-trading|NYSE is closed]]. When the perp drifts more than 0.5% away from oracle, the bot takes the opposite side and waits for the perp to snap back to the cash equity price — typically by ~15 minutes after the next NYSE open, when real cash-side arbitrageurs return and pull the perp back to fair value. It is a calendar-driven, structurally motivated [[mean-reversion]] strategy that exists only because [[perpetual-futures|perpetual]] DEXes opened 24/7 markets in late 2025 on assets whose cash venues run only ~6.5 hours a day.

This page covers a specific, narrow trade — distinct from the generic [[basis-trading|cash-and-carry basis trade]]. There is no "carry" leg here. The trade is a short-horizon convergence bet against off-hours noise in a synthetic basis market, not a hold-to-expiry yield capture.

---

## Edge source

**Primary: structural.** The NYSE regular session runs 9:30 am – 4:00 pm ET, Mon–Fri. Outside those ~32.5 hours per week, the cash equity simply cannot trade with any meaningful liquidity (pre-market and after-hours ECN liquidity is real but extremely thin; weekends are completely dark). On-chain stock perps such as [[asterdex|Aster's]] AAPL-PERP, TSLA-PERP, NVDA-PERP and the [[hyperliquid|Hyperliquid HIP-3]] TSLA market trade 24/7. This creates a synthetic basis market where one side has trading and the other does not — a structural asymmetry that disappears at NYSE open.

**Secondary: informational.** The reference oracle ([[pyth-network|Pyth]], or RedStone/HyperStone for some Hyperliquid HIP-3 markets) effectively flatlines outside NYSE hours, because all of its institutional publishers price equities off the same stale last-trade or off the same thin ECN feed. Pyth does publish equity feeds during pre-market (4:00 – 9:30 ET), post-market (16:00 – 20:00 ET), and overnight (Sun–Thu 20:00 ET – 4:00 ET) windows, but the consensus price during those windows is much less informative than during the NYSE regular session. The perp mark, by contrast, is set by leveraged speculator flow that does not need to agree with the oracle — only to stay within funding-rate-tolerable distance. This information gap is the second-order driver of drift.

**Tertiary: behavioral.** Off-hours news (earnings hits the wire after 16:00 ET, M&A leaks on weekends, geopolitics during Asia hours) drives speculative perp moves that are often *over*-reactions. Retail leverage skews the perp; reflexive funding payments compound the move. Most of these spikes mean-revert at NYSE open as the price discovery process rebases the perp against the cash market.

The trade does not require the oracle to be wrong — only for the perp to deviate from the oracle by more than the threshold during a window where the cash side cannot vote.

---

## Why this edge exists

### The synthetic basis market

A normal [[basis-trading|cash-and-carry basis trade]] works because the futures contract converges to spot at expiry. Here, there is no expiry — perpetual futures use a [[funding-rate|funding rate]] to anchor mark price to oracle. Funding is paid hourly on AsterDEX Pro (per-block in Simple mode) and hourly on Hyperliquid. Funding is the *only* anchoring force during NYSE-closed hours, and an hourly funding payment of even 1% annualized is just ~0.0001% per hour — far too weak to discipline a 1% intraday spike on its own.

What pulls the perp back is not funding. It is the *threat* of cash-side arbitrage at NYSE open. Once the cash market reopens, arbitrageurs can short cash AAPL and long perp AAPL (or vice versa) without any structural barrier. The perp must converge to the cash market — and in practice, the snap is fast: most of the convergence happens in the first 5–30 minutes of regular session trading.

### NYSE regular session = the only "fair" window

The NYSE schedule that matters for this strategy:

- **Regular session:** 9:30 am – 4:00 pm ET, Mon–Fri
- **Pre-market (ECN):** 4:00 – 9:30 ET
- **Post-market (ECN):** 16:00 – 20:00 ET
- **Closed:** 20:00 ET – 4:00 ET overnight Mon–Thu, all of Friday 16:00 ET → Monday 4:00 ET (~60 hours), plus full holidays and early-close days (e.g., July 3rd close at 13:00 ET, day after Thanksgiving close at 13:00 ET)

Pyth's equity feeds [explicitly follow the NYSE calendar][pyth-mh] including pre-market, post-market, and an "overnight" window from Sun–Thu 20:00 ET to 4:00 ET. During NYSE holidays and Friday-night-to-Sunday-night, the equity price feed is effectively halted or stale — its `PriceStatus` enum (Trading / Halted / Auction / Unknown) reports `Halted` when the underlying market is not open.

### Why the perp drifts

Three forces push the perp away from oracle when NYSE is closed:

1. **Speculator flow.** A leveraged trader who wants to express an after-hours news view (Apple miss after earnings, Tesla delivery beat, an executive arrest, etc.) buys or sells the perp. With cash-side arb absent, their flow moves the mark price against thin off-hours order book depth.
2. **Forced flow.** If perp funding has been paying longs aggressively, mechanical arb desks may close hedges off-hours, removing one side of the book and amplifying any directional flow.
3. **Reflexive momentum.** Stop runs, liquidations of leveraged retail, and copy-trading bots produce momentum that decays once cash-side liquidity returns.

### Why the snap-back is reliable

The 9:30 am ET cash open is *the* re-anchoring event. Pyth's equity feed transitions from low-information aggregation to high-information aggregation. Cash-side arb desks (Citadel-style market makers, dedicated tokenized-equity arb shops, HFT books) reactivate their cash-vs-perp basis books. The perp mark price typically converges within 5–30 minutes of the open. This is the same dynamic studied in the academic literature on [[overnight-vs-intraday|overnight vs intraday returns]] — see [Boyarchenko, Larsen, and Whelan (2023)][nyfed-overnight] on the "overnight drift" and the way dealer inventory risk produces predictable patterns into and out of the open.

### What's different from generic basis trading

This is not [[basis-trading]]. There is:

- **No carry leg.** You are not earning the spread between cash and futures. You are betting on a short-horizon convergence event.
- **No expiry.** Convergence is not contractual; it is behavioral / structural and only happens because of the NYSE schedule.
- **No long-only or short-only bias.** The trade fades drift in both directions — long the perp when it's drifted below oracle, short when it's drifted above.
- **No two-leg hedge.** The trade is *naked perp* against the oracle reference. There is no cash hedge (you cannot trade cash AAPL on-chain — that is the whole point of the opportunity).

This last point matters: this is *not market-neutral in the sense of a cash-and-carry*. It is *directional in the perp* until the oracle convergence happens. The "market neutrality" comes from the structural mean-reversion, not from a hedged spread.

---

## Null hypothesis

If on-chain stock perps tracked their oracle reference perfectly 24/7, with deviations only inside the bid-ask spread, the drift would be pure microstructure noise and this trade would not exist. Under that null:

- 0.5% deviations would be vanishingly rare and would resolve in seconds
- Off-hours and on-hours behaviour would look identical
- The bot would generate near-zero signals; trade frequency would be < 1/day
- Win rate would not differ meaningfully from coin-flip after costs
- There would be no detectable bias toward NYSE-open as the convergence trigger

What the bot's logs actually show — ~17 signals in 24 hours, mostly clustered in NYSE-closed hours, with most exits triggered by oracle convergence within ~15 minutes of NYSE open — refutes the null. The cleanest empirical falsification test is the *time distribution of signals*: if signals are uniformly distributed across the 24-hour clock, the strategy is just noise-fading and will lose money to costs. If signals cluster in NYSE-closed windows and resolve at NYSE-open, the structural edge is real.

A secondary null: if drifts above 0.5% were always genuine repricings (every spike "means something"), then fading them would lose. The empirical question is the *base rate* — what fraction of >0.5% deviations during NYSE-closed hours mean-revert vs. continue? Anecdotally and from the bot's positive PnL, the base rate of mean-reversion is high enough to be tradeable, but earnings-night and weekend-news spikes are the principal-component failure cases.

---

## Rules

### Entry

1. **Universe:** Liquid stock perps on AsterDEX (currently AAPL, TSLA, NVDA, MSFT, AMZN, META, GOOG and similar blue-chip names — Aster confirmed this initial set on launch, July 2025) and HIP-3 equity perps on Hyperliquid (TSLA via Felix/HyperStone is the canonical example; more added since October 2025). Restrict to stocks with $1M+ daily perp volume to avoid pure-noise drifts on small caps.
2. **Eligibility window:** NYSE *closed*. Determined via [[python|pandas_market_calendars]] (`mcal.get_calendar('NYSE')` + `open_at_time()`) — handles regular hours, half-days, and holidays. Treat the trade as valid throughout extended hours (pre-market, post-market) as long as Pyth's equity feed is in `Trading` status; treat overnight (20:00 – 4:00 ET) and weekend windows as the highest-edge zone.
3. **Drift threshold:** `drift = (perp_mark - pyth_oracle) / pyth_oracle`. Open a trade when `|drift| > 0.5%`. Optionally tier the threshold up for high-volatility names (e.g., 0.75% on TSLA, NVDA) and down for low-vol names (0.4% on MSFT, AAPL).
4. **Direction:** *Fade the drift.*
   - If `drift > +0.5%` (perp above oracle) → **short** perp.
   - If `drift < -0.5%` (perp below oracle) → **long** perp.
5. **Funding sanity check:** If predicted funding for the next hour would *pay you* to hold the position you would open (e.g., perp is rich and funding is positive — shorts get paid), allocate normally. If funding is *paying against you* by more than ~50% annualized, reduce sizing or skip — the funding cost will eat the convergence profit on long holds.
6. **Concentration cap:** Maximum 8 concurrent stock-perp positions. No more than one position per ticker.
7. **News blackout:** Do not enter within 30 minutes before scheduled earnings releases or Fed announcements. Earnings are the single largest risk factor (see "What kills this strategy").

### Exit

1. **Primary exit — oracle convergence:** Close when `|drift| < 0.1%`. This captures the bulk of the move and avoids round-tripping at the open.
2. **Time-based exit — NYSE open + 15 min:** Force-close all positions at 9:45 am ET regardless of P&L. By 9:45 ET, cash-side arb has had 15 minutes to re-anchor the perp; further holding earns no edge and accumulates funding / delta risk.
3. **Stop-loss — drift extension:** Close if drift moves *further* from oracle by another 0.75% (i.e., a +0.5% short turns into a -1.25% loss). This is the earnings-night / news-driven kill switch.
4. **Time-based stop — 36-hour cap:** Close any position open longer than 36 hours regardless of state. Friday-night entries that survive the weekend are the worst-case path; this prevents Monday-morning gap-and-go disasters.
5. **Funding flip:** If funding flips against the position by more than 100% APR annualized, exit early — the convergence will not happen fast enough to overcome the funding bleed.

### Position sizing

- **Per-stock allocation:** 11.25% of book notional per stock.
- **Leverage:** 2x. So 11.25% notional means ~5.6% of book in margin per position.
- **Aggregate exposure:** With max 8 concurrent positions, total notional is 90% of book; total margin ~45%. Remaining ~55% sits as reserve for adverse mark-to-market and funding.
- **Per-trade dollar risk:** With a -1.25% drift stop on 11.25% notional at 2x, max loss per stop is ~0.28% of book. With 8 simultaneous adverse moves (highly correlated tail event — e.g., the entire S&P gapping up on macro news), max book loss in a single open is ~2.25%, before accounting for slippage at the stop.

### Special-case rules

- **Friday close → Monday open:** The 64.5-hour NYSE-closed weekend window is the highest-risk zone. Default policy: do not open new positions after 12:00 ET Friday unless drift exceeds 1.5% (a higher threshold reflecting genuine weekend-news flow), and reduce per-stock sizing to 5% of book.
- **Earnings windows:** Do not hold any position from 30 minutes before scheduled earnings through the next NYSE open. Earnings drift is signal, not noise.
- **Holidays / early closes:** Treat half-days as full-closed days for sizing. The Monday-after-Thanksgiving close at 13:00 ET extends the closed window by ~3 hours; size accordingly.

---

## Implementation pseudocode

```python
import pandas_market_calendars as mcal
from datetime import datetime, timezone

NYSE = mcal.get_calendar('NYSE')
DRIFT_OPEN = 0.005       # 0.5%
DRIFT_CLOSE = 0.001      # 0.1%
DRIFT_STOP = 0.0125      # +0.75% beyond entry
MAX_POSITIONS = 8
PER_STOCK_PCT = 0.1125   # 11.25% notional
LEVERAGE = 2

def is_nyse_closed(now_utc: datetime) -> bool:
    """True when NYSE regular session is closed."""
    # pandas_market_calendars expects tz-aware timestamps
    schedule = NYSE.schedule(
        start_date=now_utc.date(),
        end_date=now_utc.date(),
    )
    if schedule.empty:
        return True  # weekend or full holiday
    try:
        return not NYSE.open_at_time(schedule, now_utc)
    except ValueError:
        return True  # before first open / after last close of window

def get_pyth_oracle(symbol: str) -> tuple[float, str]:
    """Returns (price, status). status in {Trading, Halted, Auction, Unknown}."""
    feed = pyth_client.get_price_feed(equity_feed_id(symbol))
    return feed.price, feed.status

def get_perp_mark(symbol: str) -> float:
    return aster_client.get_mark_price(f"{symbol}-PERP")

def evaluate_signal(symbol: str, now_utc: datetime) -> dict | None:
    if not is_nyse_closed(now_utc):
        return None
    if is_within_earnings_blackout(symbol, now_utc):
        return None

    oracle_price, status = get_pyth_oracle(symbol)
    if status != "Trading":
        return None  # halted feed = no reference, do not trade

    perp_price = get_perp_mark(symbol)
    drift = (perp_price - oracle_price) / oracle_price

    if abs(drift) < DRIFT_OPEN:
        return None

    side = "short" if drift > 0 else "long"
    return {
        "symbol": symbol,
        "side": side,
        "entry_drift": drift,
        "oracle": oracle_price,
        "perp": perp_price,
        "ts": now_utc,
    }

def manage_open_position(pos, now_utc):
    """Run every 5–30 sec on each open position."""
    oracle_price, status = get_pyth_oracle(pos["symbol"])
    perp_price = get_perp_mark(pos["symbol"])
    drift = (perp_price - oracle_price) / oracle_price

    # 1. Convergence exit
    if abs(drift) < DRIFT_CLOSE:
        return close(pos, reason="oracle_convergence")

    # 2. NYSE open + 15 min hard exit
    if is_within_first_15min_of_open(now_utc):
        return close(pos, reason="open_plus_15")

    # 3. Drift-extension stop
    extension = (drift - pos["entry_drift"])
    adverse = (pos["side"] == "short" and extension > 0.0075) or \
              (pos["side"] == "long"  and extension < -0.0075)
    if adverse:
        return close(pos, reason="drift_stop")

    # 4. 36-hour cap
    if (now_utc - pos["ts"]).total_seconds() > 36 * 3600:
        return close(pos, reason="time_cap")

    # 5. Funding flip
    if predicted_funding_apr(pos) < -1.0:  # paying you >100% APR against
        return close(pos, reason="funding_bleed")
```

The actual production bot wraps this in a polling loop (typically 10–30s tick), routes orders through the AsterDEX Pro API with hidden orders to minimise market impact, and keeps a per-symbol cooldown to prevent immediate re-entry after a stop-out.

---

## Indicators / data used

- **[[pyth-network|Pyth oracle]] equity feed.** Primary reference. Update cadence is sub-second when markets are open; status field is the gating signal.
- **Perp mark price.** From AsterDEX or Hyperliquid REST/WebSocket API. Use mark price (not last trade) to avoid being whipsawed by isolated trades against thin order book layers.
- **NYSE market calendar.** `pandas_market_calendars` (`NYSE` calendar) is the standard. Handles holidays, half-days, and the post-2018 schedule changes correctly.
- **Holiday calendar.** Same source. Critical for Thanksgiving, Christmas Eve, July 3rd, and unscheduled closures (e.g., presidential funerals, weather closures — these have happened).
- **Per-symbol [[funding-rate|funding rate]].** Used as an entry sanity check and ongoing exit trigger.
- **Earnings calendar.** A scheduled-events feed (e.g., Earnings Whispers, AlphaVantage, or scraped from Nasdaq) to enforce the earnings blackout window.
- **Perp order book depth.** For pre-trade slippage estimation — necessary for the $5M capacity ceiling.

---

## Example trade

**Setup.** Tuesday 2026-03-17, 03:00 ET. NYSE has been closed since Monday 16:00 ET. TSLA closed at $215.40. Around 02:30 ET, a viral tweet from a prominent crypto-stock account claims "TSLA delivery numbers leaked, miss vs whisper." Speculative perp shorts pile in.

**State at 03:00 ET:**

- Pyth `TSLA/USD` oracle: `$214.92` (drifting only on thin overnight ECN; status = `Trading` because it falls inside Pyth's overnight 20:00–04:00 ET window)
- AsterDEX TSLA-PERP mark: `$212.30`
- `drift = (212.30 - 214.92) / 214.92 = -1.22%`

**Entry.** Drift exceeds the -0.5% threshold. NYSE is closed. No earnings in the next 24 hours (TSLA's next earnings is 6 weeks out). Bot opens a long: 11.25% of $100k book = $11,250 notional at 2x leverage = $5,625 margin posted. Funding: 8% APR positive (paying longs to shorts) — an annoying headwind but well within tolerance.

**Hold.** Perp drifts further to $211.50 by 04:30 ET (drift = -1.59%) — close to the -1.97% drift-stop level (-1.22% entry minus -0.75% extension), but not triggered. Bot holds. By 06:30 ET the perp has crawled back to $213.10 as the rumour circulates and gets debunked. By 09:30 ET (NYSE open), perp is at $214.50 (drift -0.20%), and the cash market opens at $214.85 — the leak rumour is essentially noise, and the cash market opens roughly flat to oracle.

**Exit.** At 09:33 ET the perp converges to $214.80 (drift -0.06%), inside the 0.1% close threshold. Bot closes long at $214.80. Round-trip P&L:

- Entry: long $11,250 notional at $212.30 → $11,250 / $212.30 = 53.0 TSLA-PERP units
- Exit: 53.0 × $214.80 = $11,384.40
- Gross P&L: +$134.40 (+1.18% on notional, +2.39% on margin)
- Funding cost: ~6.5h × 8% APR / 8760 × $11,250 ≈ -$0.67
- Fees: 0% on Aster's stock perps (promotional) — for non-promo venues budget ~3 bps round-trip ≈ -$3.40
- Net: ~+$130 → ~+2.3% on margin, ~+1.16% on notional, in 6.5 hours

This is a typical trade. Most live trades close inside the convergence band well before the 09:45 ET hard exit.

**Counter-example (the trade that fails).** Same setup, but the "leak" turns out to be real — TSLA pre-announces a 6% delivery miss at 06:00 ET. Cash markets open at 09:30 ET at $202 (-6%). Perp reprices to $202 well before that, blowing through the drift-stop at $209.18 around 06:15 ET. The bot closes the long at $209.18, realising a loss of ~$135 on the $11,250 notional position before fees — about -2.4% on margin. The drift-stop is the firewall that prevents earnings-style events from becoming book-killing losses.

---

## Performance characteristics

The trade has the classic signature of a high-frequency mean-reversion strategy with *fat left tails*:

- **Win rate:** 75–85% expected, based on the bot's 17-signals/24h cadence and the structural snap-back. Most signals close at oracle convergence with small positive P&L.
- **Average win:** ~0.5–1.5% on notional (1–3% on margin) — the band between entry and convergence.
- **Average loss:** ~2–4% on notional when the drift-stop trips (4–8% on margin) — and these are predominantly earnings-driven, news-driven, or weekend-gap events.
- **Sharpe (expected, net of costs):** 1.0–1.8. The bot's frequency (potentially hundreds of trades per quarter across 8 names) gives strong T-stat aggregation if the per-trade edge is real.
- **Max drawdown (expected):** 15–25%. The principal-component risk is correlated earnings nights and weekend gaps. A single Monday open after a major weekend event (election, geopolitical shock) could drawdown the full book by 5–10% in one open.
- **Equity curve shape:** Slow steady accumulation through normal weeks, occasional sharp drawdowns at quarterly earnings clusters (mid-Jan, mid-Apr, mid-Jul, mid-Oct). Operators should expect to give back 1–3 months of gains in a bad earnings week.
- **Cost sensitivity:** Per-trade gross edge is small (50–150 bps) so the strategy is sensitive to round-trip fees. Aster's 0% promotional fees on stock perps make the strategy substantially more profitable than it would be at 5–10 bps round-trip — when promo fees end, the strategy's expected Sharpe will fall by ~30%.

The realistic-cost overlay (vs naive backtest):

| Cost item | Per-trade impact |
|---|---|
| Maker fee (Aster promo) | 0 bps |
| Maker fee (post-promo, est) | 1–2 bps |
| Slippage (mark-to-fill on hidden orders) | 2–5 bps |
| Funding (avg, varies by symbol) | 1–4 bps over typical 6h hold |
| Total realistic round-trip cost | 4–11 bps in promo, 6–15 bps post-promo |

Breakeven cost is ~15 bps round-trip (50 bps gross edge × ~30% loss-rate weighted).

---

## Capacity limits

Capacity is set by perp DEX order book depth on individual stock symbols:

- **Top names (TSLA, NVDA, AAPL):** Aster reports daily volume in tens of millions on these names. Order book depth at <0.1% from mark is typically $200k–$500k. A single trade should be sized to <20% of that depth to keep slippage within the 5 bps budget — i.e., $40k–$100k per trade.
- **Mid names (MSFT, AMZN, META, GOOG):** Depth is materially thinner. Per-trade size should drop to $20k–$50k.
- **Long tail:** Aster has been adding more names; on these, depth at <0.1% can be $5k–$20k. Effectively un-tradeable for any meaningful book.

With per-stock allocation of 11.25% × 8 stocks at 2x leverage, the strategy can comfortably run a $1–5M book on the top names alone. Above $10M book size, market impact on entry and exit dominates the edge and the strategy decays. Hyperliquid HIP-3 equity perps and any future Drift / dYdX equity perps would expand capacity if and as they list.

The strategy *does not scale to institutional book size* — it is firmly in the prop-and-individual zone.

---

## What kills this strategy

In rough order of importance:

1. **Earnings releases during NYSE-closed hours.** Earnings beats and misses are *not* noise. The drift after-hours is real price discovery. Fading a real earnings move and getting stopped is the principal-component loss case. Mitigation: hard earnings blackout — never hold across earnings.
2. **Weekend news events.** Major M&A leaks (Saturday morning), geopolitical shocks (Sunday-night Asia open), unexpected Fed actions (rare but historic). The 65-hour Friday-close-to-Monday-open window is the longest unanchored period and the highest-risk zone.
3. **Pyth (or competitor oracle) adopting genuine after-hours feeds.** If Pyth or a competitor begins publishing institutional-grade equity prices that *do* track perp mark prices off-hours (e.g., by ingesting blockheight-aligned dark-pool prints, or by using a different consensus methodology that incorporates perp mark itself), the structural asymmetry collapses. Watch Pyth governance and roadmap announcements.
4. **Perp DEX changing oracle anchor or funding mechanism.** If AsterDEX switches the TSLA-PERP funding/mark anchor away from a Pyth-style equity oracle to e.g. a rolling perp-internal twap, the oracle-vs-mark divergence becomes an internal feedback loop and the basis dynamic disappears.
5. **Counterparty / venue risk.** AsterDEX, Hyperliquid, or the chains they settle on going down with positions open. The August 2025 outages, MEV-driven settlement failures, or full insolvency events are the tail. Mitigation: distribute positions across venues, keep margin buffer high, never run >50% margin utilisation on a single venue.
6. **Funding-rate compression.** If a large arb desk runs a similar strategy and continuously squeezes the basis, funding rates may flip violently and frequently, eating the per-trade edge. This is the [[failure-modes|crowding mode]].
7. **Regulatory action.** Tokenized stock perps exist in a grey zone. A sudden enforcement action against AsterDEX or Hyperliquid (or against US-domiciled users of these venues) could force liquidation at the worst possible time.
8. **Pyth feed halts / freezes.** If Pyth's equity feed reports `Halted` (its `PriceStatus` enum value 2) or `Unknown` (value 0) due to upstream publisher issues, the oracle reference is unreliable. The bot must check status on every tick and refuse to enter when status ≠ `Trading`.

See [[failure-modes]] for the general taxonomy.

---

## Kill criteria

Numerical conditions for retiring or pausing the strategy:

- **30-day rolling Sharpe < 0.** Two months of negative Sharpe → retire.
- **Three consecutive earnings-night blow-ups in a single quarter.** Indicates the earnings blackout logic is failing or a structural shift in earnings reactions has occurred.
- **Single-trade loss > 3× average win.** Investigate immediately. Likely indicates a stale Pyth status flag or a missed news event.
- **Cumulative drawdown > 20% of book.** Pause and review.
- **Pyth or perp DEX announces a structural change** (continuous after-hours equity pricing, anchor change). Pre-emptively pause and reassess.
- **Aster promo fees end** *and* the strategy's net Sharpe falls below 0.7 with new fees. Retire or reduce sizing.

See [[when-to-retire-a-strategy]] for the general framework.

---

## Advantages

- **Calendar-driven.** Entry and exit windows are deterministic — the NYSE schedule is published years in advance. Compare to [[funding-rate-arbitrage]] which depends on uncertain funding regimes.
- **Frequent signals.** ~17 signals/24h across 8 names produces high T-stat aggregation; results are not dominated by single trades.
- **Short hold times.** Median hold is hours, not days. Margin recycles fast.
- **Synthetic market-neutrality.** Although the trade is technically a directional perp, the structural mean-reversion gives it the *behaviour* of a market-neutral strategy in normal regimes — daily P&L is uncorrelated with the broad equity market, the [[bitcoin]] market, and macro.
- **No two-leg execution risk.** Unlike cash-and-carry [[basis-trading]], no spot leg to hedge — entry is a single perp order.
- **Aster's 0% stock-perp fees.** Promotional fee structure makes the small per-trade edge actually capturable.
- **Capacity is private-trader-friendly.** $1–5M is a sweet spot below institutional radar but above retail hobby-bot scale.
- **Edge is novel.** Stock perps on-chain only became reliably tradeable in late 2025. The edge has not been arbitraged out.

---

## Disadvantages

- **Earnings risk is the principal-component tail.** A single missed-blackout earnings night can give back a quarter of gains.
- **Weekend gap risk.** 65-hour windows expose the book to news events with no possibility of intra-period exit.
- **Depends on oracle being structurally lazy.** The whole edge collapses if oracle quality improves off-hours.
- **Counterparty risk on novel venues.** AsterDEX is a 2025-vintage merged DEX; Hyperliquid HIP-3 markets are new. Operational risk is non-trivial.
- **Capacity-limited.** Strategy does not scale to large books. Dilutes to nothing past ~$10M.
- **Funding-rate path dependency.** A long position held through a period of strongly positive funding bleeds; the realised edge is sensitive to funding regime.
- **Regulatory grey zone.** Tokenized stock perps occupy uncertain legal status; sudden regulatory action is a tail risk.
- **Requires high-availability infrastructure.** Bot must run 24/7 — overnight outages miss the highest-edge windows.
- **Pyth status field must be respected.** Trading on a `Halted` or `Unknown` status is asking to be wrong-footed when the feed catches up.

---

## Sources

- [Pyth Network — Market Hours documentation][pyth-mh] — Pyth's official documentation of equity-feed scheduling, including the 4:00 ET pre-market open, 9:30 ET regular open, 16:00 ET regular close, 20:00 ET post-market close, and overnight 20:00–04:00 ET window for Sun–Thu equity feeds.
- [Pyth `PriceStatus` enum (pyth-client crate)](https://docs.rs/pyth-client/latest/pyth_client/enum.PriceStatus.html) — definitive list of feed statuses (`Trading`, `Halted`, `Auction`, `Unknown`) and their semantics.
- [Aster Launches 24/7 Stock Perpetual Contracts (Daily Hodl, July 2025)](https://dailyhodl.com/2025/07/16/aster-launches-24-7-stock-perpetual-contracts-trading-with-exposure-to-u-s-equities/) — confirms launch date, initial set of stock perps (AMZN, AAPL, GOOG, META, MSFT, NVDA, TSLA), and 50x max leverage on equity perps.
- [Aster DEX eliminates trading fees on NVDA and TSLA stock perpetuals (Cryptopolitan)](https://www.cryptopolitan.com/aster-dex-eliminate-trading-fees-nvda-tsla/) — confirms 0% maker / 0% taker promotional fees on Aster stock perps.
- [HIP-3: Permissionless Perps on Hyperliquid (Hyperdash)](https://hyperdash.com/learn/hip-3-permissionless-perpetual-markets-on-hyperliquid) — describes the permissionless equity-perp framework launched October 13, 2025.
- [Felix launches its first Hyperliquid HIP-3 market with TSLA, powered by HyperStone (RedStone, Nov 2025)](https://blog.redstone.finance/2025/11/13/felix-launches-its-first-hyperliquid-hip-3-market-with-tsla-powered-by-hyperstone/) — first major HIP-3 equity market, Tesla, with a dedicated equity-oracle (HyperStone) — illustrates the alternative-oracle landscape.
- [The Overnight Drift in U.S. Equity Returns — Liberty Street Economics (NY Fed, 2021)][nyfed-overnight] — documents that nearly all equity gains since 1998 have been earned overnight, with peaks around 2–3 ET (European open). Provides academic basis for the off-hours mean-reversion phenomenon. Boyarchenko, Larsen, Whelan (NY Fed Staff Report 917).
- [Cooper, Cliff, and Gulen (2008) — Return Differences between Trading and Non-Trading Hours](https://www.researchgate.net/publication/228461243_Return_Differences_between_Trading_and_Non-Trading_Hours_Like_Night_and_Day) — foundational paper on overnight vs intraday return decomposition.
- [Lou, Polk, Skouras — A Tug of War: Overnight Versus Intraday Expected Returns](http://www.econ.yale.edu/~shiller/behfin/2015-04-11/lou_polk_skouras.pdf) — clientele model of overnight/intraday reversal.
- [Statistical Arbitrage with Mean-Reverting Overnight Price Gaps — MDPI (2019)](https://www.mdpi.com/1911-8074/12/2/51) — empirical evidence for overnight-gap mean reversion in S&P 500 names; the closest published analogue to this strategy in traditional markets.
- [Perpetual Futures: The Missing Link in Tokenized Equities — TD Securities](https://www.tdsecurities.com/ca/en/tokenized-equities-missing-link-perps) — institutional view of why on-chain stock perps emerged and how they connect to cash markets.
- [pandas_market_calendars documentation](https://pandas-market-calendars.readthedocs.io/en/latest/usage.html) — library used for NYSE schedule logic in the bot's implementation.

[pyth-mh]: https://docs.pyth.network/price-feeds/market-hours
[nyfed-overnight]: https://libertystreeteconomics.newyorkfed.org/2021/05/the-overnight-drift-in-us-equity-returns/

---

## Related

- [[basis-trading]] — generic cash-and-carry futures basis (distinct: this page covers a *behavioural / structural* convergence trade, not a carry trade)
- [[funding-rate-arbitrage]] — the other major perp-vs-spot convergence trade; uses funding payments instead of NYSE-open snap-back
- [[mean-reversion]] — the parent strategy family
- [[after-hours-trading]] — extended-hours equity microstructure and ECN dynamics
- [[overnight-vs-intraday]] — the academic literature on overnight vs intraday return decomposition that motivates the edge
- [[pyth-network]] — the oracle providing the reference price
- [[oracle-manipulation]] — adjacent risk topic; the strategy depends on the oracle being honest but lazy, not on it being manipulable
- [[asterdex]] — the principal venue
- [[hyperliquid]] — secondary venue (HIP-3 equity perps)
- [[asterdex-perp-trading-map]] — broader strategy map for the venue
- [[perpetual-futures]] — the instrument class
- [[failure-modes]] — taxonomy of strategy failure modes
- [[when-to-retire-a-strategy]] — kill-criteria framework
