---
title: "Unlock Pair Hedge"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, pairs-trading, event-driven, perpetual-futures, derivatives, arbitrage, quantitative, crypto, altcoins]
aliases: ["Beta-Hedged Unlock Short", "Pair-Expressed Unlock Short", "Unlock Supply Pairs Trade", "Market-Neutral Unlock Short"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [informational, structural, analytical]
edge_mechanism: "Token cliff unlocks create a predictable idiosyncratic supply shock; expressing the short as a long-short pair — short the unlocking token, long a beta-matched sector peer — strips out broad crypto market exposure and isolates the supply-shock premium, leaving the trade to profit from the idiosyncratic price impact of the unlock while remaining neutral to BTC/ETH price direction."

data_required: [token-unlock-schedule, ohlcv-daily, funding-rates, open-interest, perp-price, circulating-supply, sector-classification]
min_capital_usd: 15000
capacity_usd: 10000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.20
breakeven_cost_bps: 40

decay_evidence: "Token unlock front-running has become increasingly crowded since 2022 as dedicated unlock-tracking services (Token Unlocks, Coinglass unlock calendar) went mainstream. This page's beta-hedged expression differs from the outright short (unlock-short-with-crowding-gate): the pair structure reduces crowding exposure by focusing on the idiosyncratic component. However, the pairs approach requires a liquid sector peer to hedge against, which is not always available for illiquid or idiosyncratic tokens — limiting the applicable universe."

kill_criteria: |
  - strategy drawdown > 20% from high-water mark
  - rolling 3-month Sharpe < 0 on minimum 8 completed pair-unlock trades
  - beta mismatch (rolling 20-day realised beta of unlocking token to sector peer deviates > 0.4 from estimated entry beta) for > 50% of trades in a 3-month period — pairs are consistently mis-matched
  - 4 consecutive unlock pair shorts produce negative net P&L after costs (the beta-hedge is not isolating the supply shock; the edge has decayed or was never present)
  - sector peer universe shrinks to < 2 qualifying beta-match candidates per unlock event (pairs approach is operationally infeasible; revert to outright short with crowding gate)

related: ["[[unlock-short-with-crowding-gate]]", "[[pairs-trading]]", "[[pairs-with-funding-differential]]", "[[token-unlock-supply-event]]", "[[correlation-regime-pairs]]", "[[cross-sectional-relative-value]]", "[[unlock-aware-momentum]]", "[[event-driven-trading]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[statistical-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Unlock Pair Hedge

Unlock pair hedge is a **beta-matched long-short pairs trade** constructed around a scheduled token cliff unlock: short the unlocking token's perp, long a beta-matched sector peer perp, in a ratio that makes the pair roughly neutral to broad crypto market direction. The primitive edge is the idiosyncratic supply shock from the unlock (same source as [[token-unlock-supply-event]] and [[unlock-short-with-crowding-gate]]); the overlay is the **pairs / sector-relative-value structure** that hedges out BTC beta and sector beta, leaving the P&L exposed primarily to the unlock's idiosyncratic supply-pressure impact rather than to broad market direction.

**This is explicitly differentiated from [[unlock-short-with-crowding-gate]]** — that page is an outright perp short on the unlocking token, filtered through a crowding gate (funding not deeply negative, OI not already spiked short). It retains full market-direction exposure and hedges only the crowding dimension. This page adds **beta hedging via a long in a sector peer**, removing the market/sector directional component and converting the trade from a directional unlock short into a market-neutral relative-value expression. An outright short in a bull market suffers BTC-beta losses that overwhelm the supply-shock return; the pair hedge explicitly addresses this.

**This is differentiated from [[pairs-with-funding-differential]]** — that page runs a pairs trade where the spread z-score AND the inter-leg funding differential must agree. Both legs are chosen for their cointegration properties, and the trade is entered based on z-score deviation with funding confirmation. This page constructs the pair specifically around an event (the unlock), uses beta-matching rather than cointegration as the pairing criterion, and has a predetermined exit schedule tied to the unlock digestion window rather than z-score mean-reversion.

**This is differentiated from [[cross-sectional-relative-value]]** — that page runs a cross-sectional ranking model (momentum + funding + OI rank) within sectors and goes long/short on the top/bottom quintile. The ranking is continuous and not tied to events. This page is event-driven: the short leg is selected by the unlock calendar, the long leg is selected by beta-matching, and the exit is tied to supply-digestion completion.

## Edge source

Per [[edge-taxonomy]], **informational + structural + analytical**:

- **Informational (primary)** — unlock schedules are public knowledge (on-chain vesting contracts, Token Unlocks, Coinglass). The supply shock date, magnitude (tokens released as a fraction of circulating supply), and likely sellers (VC investors, team, protocol treasury) are all knowable in advance. The edge is informational in the sense that systematic monitoring of the unlock calendar provides a structured entry signal that discretionary market participants miss or underweight.
- **Structural** — cliff unlocks represent a sudden discrete increase in floating supply from holders whose cost basis is far below market price. The structural overhang depresses the unlocking token's price in the 7–30 day window around the event; this is the same structural forcing as documented in [[token-unlock-supply-event]].
- **Analytical** — the beta-hedging step is an analytical improvement over the outright short: correctly estimating the unlocking token's rolling beta to a liquid sector peer and sizing the hedge ratio reduces the main noise source (broad market direction) and increases the signal-to-noise ratio of the supply-shock component.

## Why this edge exists

**Three mechanisms create the supply-shock premium on the idiosyncratic leg:**

1. **Insiders and VCs have near-zero cost basis and will sell at any price above cost.** Large early investors holding tokens at seed-round prices (typically 90–99% below current market) have a strong incentive to sell any portion of their allocation as soon as it unlocks. This is not rational-market selling — it is a mechanical supply event driven by vesting schedules, not by views on fair value. The selling pressure is predictable, large relative to daily trading volume, and does not depend on market direction.

2. **Market makers and informed traders are already positioned (but do not fully absorb the supply).** The unlock is public; some market participants short the token in anticipation. However, the pair structure in this strategy allows a cleaner expression than the outright short that most participants use: by isolating the idiosyncratic component, the pair trade avoids the crowding that accumulates on the outright short side (the [[unlock-short-with-crowding-gate]] crowding gate directly measures this).

3. **Sector beta hedging turns a directional bet into a relative-value trade.** The unlocking token moves with BTC/ETH beta approximately 60–80% of the time (industry-standard crypto beta). If BTC rises 5% during the unlock window, an outright short loses 5% × beta before the supply-shock return is captured. The long sector peer captures approximately 5% × sector beta, largely cancelling the directional noise and leaving the trade exposed to the idiosyncratic supply-shock component.

**Who is on the other side:** the early investor/team member selling unlocked tokens into the market regardless of price; and the discretionary trader who does not hedge BTC beta and therefore cannot hold the position through a broad market upswing.

## Null hypothesis

Under the null, the unlock event carries **no incremental idiosyncratic return** after beta-adjustment to a sector peer:
- The beta-adjusted return of the unlocking token (long = sector peer, short = unlocking token) in the 5-30 day window around the unlock should not differ from the beta-adjusted return in matched non-unlock windows at the same sector-relative-value ranking.
- The supply-shock component (fraction of circulating supply unlocked) should not be negatively correlated with beta-adjusted returns around the event.
- Funding on the unlocking token should not be more negative around unlock dates than on a matched non-unlock control sample (the crowding has already taken the supply pressure out of prices pre-event).

Currently not rejected (`backtest_status: untested`). Testable prediction: construct a database of BTC cliff unlocks (≥ 3% of circulating supply) over 2020–2025; compute beta-adjusted excess return of the unlocking token vs sector peer in the [−5d, +30d] window; compare to distribution of matched non-unlock windows. Predict significantly negative beta-adjusted excess returns in the unlock window.

## Rules

### Event selection criteria

1. **Cliff unlock magnitude ≥ 3% of circulating supply** at the unlock date — smaller unlocks lack sufficient supply pressure to overcome typical sector-level tracking noise.
2. **Unlock date known ≥ 7 days in advance** — sufficient lead time for pair construction and beta estimation.
3. **Token has a liquid perp available** on Hyperliquid or Binance — minimum $2M daily OI; minimum average daily volume $5M.
4. **At least one sector peer available** with liquid perp, OI ≥ $5M, 20-day beta to the unlocking token between 0.6 and 1.4 — if no suitable pair exists, skip the trade.
5. **Exclude unlock events in the 5 days following a BTC ≥ 10% move** — post-crash or post-pump windows produce unstable betas; the hedge ratio is unreliable.

### Pair construction and beta estimation

**Step 1: Select sector peer.**
- Identify the token's sector (L1, DeFi, AI, Gaming, etc.) from [[sector-classification]] or equivalent.
- Within the sector, find 2–3 liquid peers with the highest 20-day rolling correlation to the unlocking token (Pearson correlation ≥ 0.60).
- Among qualifying peers, select the one whose 20-day rolling beta to the unlocking token is closest to 1.0 (ideal beta-matched hedge).

**Step 2: Estimate hedge ratio.**
- Use rolling 20-day OLS regression of the unlocking token's daily log-returns on the sector peer's daily log-returns.
- `beta_estimate = cov(R_unlock, R_peer) / var(R_peer)` over 20 days.
- Hedge ratio: for every $1 short in the unlocking token perp, go long `$1 / beta_estimate` in the sector peer perp.
- Example: if beta = 1.25, the pair is: short $1 of unlocking token, long $0.80 of sector peer (to be beta-neutral to the sector).

**Step 3: Check funding alignment.**
- Preferred: funding on the unlocking token is not deeply negative (funding > −0.02%/8h) — avoids the overcrowded short scenario flagged in [[unlock-short-with-crowding-gate]].
- Preferred: funding on the sector peer is not deeply negative either (if the peer is also in a crowded short regime, the pair has a funding headwind on both legs).

### Entry

- **Entry timing:** enter the pair 5–7 days before the unlock date.
- **Size:** short unlocking token perp at 1× notional; long sector peer perp at (1 / beta) × notional. Total pair notional = (1 + 1/beta) × base position size.
- **Capital required:** the net beta-neutral pair uses margin on both legs; at 1:1 notional, the capital requirement = 2× the position notional at 1× leverage, or 1× notional at 2× leverage (one leg offsets the other's delta).

### Exit

1. **Primary exit (supply digestion):** close both legs **10 days after the unlock date**. The supply overhang typically resolves within 7–14 days; 10 days is the standard digestion window.
2. **Early exit (supply absorbed faster):** if the unlocking token recovers to within **2% of its pre-entry spread level** vs the sector peer (beta-adjusted) before day 10 — the supply shock has been absorbed; close early and reset.
3. **Stop:** if the beta-adjusted spread (short unlocking token − long sector peer, beta-adjusted) widens by **15% adverse** from entry — the pair is moving against the supply-shock thesis; close both legs and reassess.
4. **Forced exit on sector structural break:** if the sector peer's daily correlation to the unlocking token drops below 0.50 during the hold (beta hedge breaking down), close both legs and do not reopen.

## Implementation pseudocode

```python
# unlock_pair_hedge.py

from dataclasses import dataclass
from typing import Optional
import numpy as np

# ---- event selection ----
MIN_UNLOCK_PCT_CIRC_SUPPLY  = 0.03     # >= 3% of circulating supply
MIN_DAYS_ADVANCE_NOTICE     = 7
MIN_OI_UNLOCKING_TOKEN      = 2e6      # >= $2M OI
MIN_PEER_OI                 = 5e6      # >= $5M OI for sector peer
MIN_PEER_CORRELATION        = 0.60     # 20d correlation >= 0.60
BETA_RANGE                  = (0.6, 1.4)  # acceptable beta range for peer selection

# ---- funding check ----
FUNDING_MIN_UNLOCK_TOKEN    = -0.0002  # funding not more negative than -0.02%/8h
FUNDING_MIN_PEER            = -0.0002

# ---- pair entry ----
ENTRY_DAYS_BEFORE_UNLOCK    = 6        # enter 5-7 days before unlock
BETA_WINDOW_DAYS            = 20       # OLS window for beta estimation

# ---- exits ----
DIGESTION_DAYS_POST_UNLOCK  = 10
EARLY_EXIT_SPREAD_PCT       = 0.02     # close early if spread within 2%
STOP_SPREAD_ADVERSE_PCT     = 0.15     # stop at 15% adverse spread move
MIN_CORRELATION_HOLD        = 0.50     # close if correlation drops below 0.50

@dataclass
class PairSetup:
    unlocking_token:      str
    sector_peer:          str
    beta_estimate:        float    # rolling 20d beta
    hedge_ratio:          float    # 1 / beta_estimate (peer units per token unit)
    entry_spread:         float    # (price_unlock - beta * price_peer) at entry
    unlock_date_offset:   int      # days until unlock at entry (should be 5-7)

def estimate_beta(returns_unlock: list[float], returns_peer: list[float]) -> float:
    """20-day OLS beta of unlocking token on sector peer."""
    x = np.array(returns_peer)
    y = np.array(returns_unlock)
    beta = np.cov(y, x)[0, 1] / np.var(x) if np.var(x) > 0 else 1.0
    return float(beta)

def select_pair(candidates: list[dict], unlock_returns: list[float]) -> Optional[dict]:
    """Select best sector peer: highest correlation within beta range."""
    best = None
    best_corr = MIN_PEER_CORRELATION - 0.01
    for c in candidates:
        if c["oi"] < MIN_PEER_OI:
            continue
        beta = estimate_beta(unlock_returns, c["returns"])
        corr = float(np.corrcoef(unlock_returns, c["returns"])[0, 1])
        if corr < MIN_PEER_CORRELATION:
            continue
        if not (BETA_RANGE[0] <= beta <= BETA_RANGE[1]):
            continue
        if corr > best_corr:
            best = {**c, "beta": beta, "hedge_ratio": 1.0 / beta, "corr": corr}
            best_corr = corr
    return best

def entry_decision(event: dict, pair: PairSetup, funding_unlock: float,
                   funding_peer: float, base_notional: float) -> dict:
    if funding_unlock < FUNDING_MIN_UNLOCK_TOKEN:
        return {"action": "SKIP", "reason": f"funding on unlock token too negative: {funding_unlock:.4f}"}
    if funding_peer < FUNDING_MIN_PEER:
        return {"action": "SKIP", "reason": f"funding on sector peer too negative: {funding_peer:.4f}"}
    short_notional = base_notional
    long_notional = base_notional * pair.hedge_ratio
    return {
        "action":           "ENTER_PAIR",
        "short_leg":        {"token": pair.unlocking_token, "notional": short_notional, "side": "SHORT"},
        "long_leg":         {"token": pair.sector_peer, "notional": long_notional, "side": "LONG"},
        "beta":             pair.beta_estimate,
        "hedge_ratio":      pair.hedge_ratio,
        "entry_spread":     pair.entry_spread,
        "days_to_unlock":   pair.unlock_date_offset,
        "note": (f"beta-neutral pair: short {pair.unlocking_token} ({short_notional:.0f}), "
                 f"long {pair.sector_peer} ({long_notional:.0f}), beta={pair.beta_estimate:.2f}"),
    }

def exit_decision(pair: PairSetup, days_since_unlock: int,
                  current_spread: float, current_corr: float) -> Optional[dict]:
    # primary: digestion window complete
    if days_since_unlock >= DIGESTION_DAYS_POST_UNLOCK:
        return {"action": "CLOSE_BOTH", "reason": f"{DIGESTION_DAYS_POST_UNLOCK}d post-unlock digestion window complete"}
    # early exit: spread recovered
    spread_change = (current_spread - pair.entry_spread) / abs(pair.entry_spread) if pair.entry_spread != 0 else 0
    if abs(spread_change) <= EARLY_EXIT_SPREAD_PCT:
        return {"action": "CLOSE_BOTH", "reason": f"spread within {EARLY_EXIT_SPREAD_PCT:.0%} of entry — supply digested"}
    # stop: adverse spread move
    if spread_change > STOP_SPREAD_ADVERSE_PCT:
        return {"action": "CLOSE_BOTH", "reason": f"adverse spread move {spread_change:.1%} > {STOP_SPREAD_ADVERSE_PCT:.0%} — stop"}
    # correlation breakdown
    if current_corr < MIN_CORRELATION_HOLD:
        return {"action": "CLOSE_BOTH", "reason": f"correlation {current_corr:.2f} < {MIN_CORRELATION_HOLD} — beta hedge unreliable"}
    return None
```

The production system adds: an unlock calendar feed (Token Unlocks API or on-chain vesting contract monitoring); a rolling 20-day OLS beta calculator; a daily spread-monitor computing `(price_unlock − beta × price_peer)` in normalised units; and a funding dashboard for both legs.

## Indicators / data used

- **Token unlock schedule** — external sources: Token Unlocks (tokenunlocks.app), Coinglass unlock calendar, on-chain vesting contract events. No CryptoDataAPI endpoint for token unlock schedules; maintain an external feed.
- **Daily OHLCV (unlocking token and sector peer)** — `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=30`; compute 20-day rolling beta and correlation.
- **Funding rates (both legs)** — `GET /api/v1/derivatives/funding-rates?coin={TOKEN}`; funding check on both the unlocking token and sector peer before entry.
- **Open interest (unlocking token and peer)** — `GET /api/v1/derivatives/open-interest?coin={TOKEN}`; OI threshold check for qualifying both legs.
- **Sector classification** — from [[cross-sectional-relative-value]] sector definitions, [[token-unlock-supply-event]] context, and community resources (CoinGecko categories, Messari sector tags). No dedicated CryptoDataAPI endpoint; maintained manually or from external classification APIs.
- **Regime context** — `GET /api/v1/regimes/current`; avoid entry during `Structural_Shock` (betas become unstable in systemic events).

## Example trade

**Setup (illustrative):**

- Upcoming cliff unlock: EXAMPLE_TOKEN releases 8.5% of its circulating supply in 7 days. Unlock magnitude ≥ 3% — qualifies.
- EXAMPLE_TOKEN has a Hyperliquid perp with $4.2M OI and $8M average daily volume — qualifies.
- **Sector:** L1 blockchain. Sector peers with ≥ 0.60 correlation to EXAMPLE_TOKEN over the trailing 20 days:
  - PEER_A: correlation = 0.73, estimated beta = 1.15. Hedge ratio = 1/1.15 = 0.87.
  - PEER_B: correlation = 0.68, estimated beta = 0.82. Hedge ratio = 1.22.
  - Select PEER_A (higher correlation, beta closer to 1.0).
- **Funding check:** EXAMPLE_TOKEN funding = −0.008%/8h (slightly negative but above −0.02% threshold). PEER_A funding = +0.015%/8h. Both acceptable.
- **Entry (6 days before unlock):** short $20,000 of EXAMPLE_TOKEN perp; long $17,400 of PEER_A perp (0.87 × $20,000). Total position notional: $37,400. Capital deployed (at 1× leverage on each leg): ~$37,400 in margin.

**During the hold:**
- BTC rallies +5.8% in the 3 days after entry. EXAMPLE_TOKEN rises +4.3% (below BTC beta — supply overhang dampening its move). PEER_A rises +5.5% (full beta).
- **Beta-adjusted pair return:** short EXAMPLE_TOKEN +4.3% loss, long PEER_A +5.5% gain. Beta-adjusted net = −(−4.3%) + 1.15 × (+5.5%) / 1.15 ≈ +4.3% offset by +4.785% ≈ pair is nearly flat despite BTC rally. The beta hedge worked.

**At unlock (day 7):** EXAMPLE_TOKEN drops −9.2% on the unlock day (supply hits market). PEER_A drops −1.5% (sympathetic sector move). Beta-adjusted pair return on unlock day: −(−9.2%) + 0.87 × (−1.5%) = +9.2% − 1.3% = **+7.9% spread gain** on the pair.

**Day 10 post-unlock:** EXAMPLE_TOKEN has stabilised; pair spread has normalised to near-zero. Close both legs.
- Total pair P&L: approximately +7.9% on the $20,000 short-leg notional, partially offset by path-dependent P&L from the BTC-rally period (approximately net +5.5% on base).
- Round-trip P&L: assume +$1,100 on $20,000 notional (5.5%) = **+$1,100 gross** less two-way Hyperliquid fees (0.045% per side × 4 fills ≈ $67) = **+$1,033 net** / +2.8% of $37,400 total notional deployed.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Higher than outright unlock short due to beta hedge reducing directional noise; lower than funding-differential pairs due to event-calendar limitation |
| Expected max drawdown | ~20% | Stop at 15% adverse spread move; consecutive failed pair events possible |
| Win rate (per pair trade) | ~60–70% (estimated) | Supply shock from ≥ 3% unlocks historically depresses prices; beta hedge reduces loss frequency from market direction |
| Average holding period | ~15–17 days | 6 days pre-unlock + 10 days post-unlock digestion = 16 days typical |
| Breakeven cost budget | 40 bps | Two-leg perp pair at ~0.045% per fill × 4 fills (entry + exit both legs) = ~18 bps fees; 40 bps budget absorbs spread slippage |
| Signal frequency | Moderate | Qualifying cliff unlocks (≥ 3% of circulating supply, liquid perp available, suitable peer) occur approximately 8–20 times per year across the liquid altcoin universe |

## Capacity limits

- **Binding constraint:** the liquidity of the unlocking token's perp, not the sector peer.
- At $10M AUM: position notional per trade = $30K–$100K; well within typical Hyperliquid perp OI of $2–15M for mid-cap tokens.
- Above $10M per trade: for smaller tokens, a $1M+ short could move the funding rate and alert other participants. The `capacity_usd: 10000000` reflects the aggregate strategy AUM, not per-trade notional.
- **Crowding sensitivity:** if many operators run the same pairs approach, the beta hedge itself becomes crowded (the sector peer goes bid while the unlocking token is shorted, distorting the hedge). Monitor peer funding as a crowding indicator.

## What kills this strategy

1. **Beta instability during unlock event (#4: Crowding).** In volatile sector-wide moves (e.g., all L1s drop 15% on a macro news shock during the hold period), the 20-day OLS beta becomes a poor real-time hedge. The short-unlocking-token / long-peer pair loses its neutrality; both legs lose money simultaneously if the pair is mis-sized.
2. **No suitable peer available (#7: Operational).** For tokens with unusual sector positioning or insufficient liquid peers, the beta-matching step is infeasible. The applicable universe is limited to tokens with ≥ 2 liquid sector peers.
3. **Unlock already crowded before entry (#4: Crowding).** Even with the beta hedge, if the short side on the unlocking token is already deeply negative in funding, the pair inherits a funding headwind on the short leg. The funding check at entry addresses this but does not eliminate it.
4. **Supply digestion is faster or slower than expected (#5: Regime change).** Some large unlocks (especially from protocols with strong buy pressure from new product launches) are digested within 2–3 days; the 6-day pre-unlock entry is too early, and the position gives up P&L on a rebound before the digestion window closes. Other unlocks produce multi-week supply pressure; the 10-day digestion exit may be premature.
5. **OTC or dark-pool insider selling (#3: Market-structure).** Large VC holders sometimes arrange OTC block sales that do not hit the spot/perp market directly, reducing the on-chain supply impact. The supply shock is smaller than the on-chain unlock suggests; the pair underperforms.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 20% from high-water mark** — pair structure is not protecting against adverse moves.
2. **Rolling 3-month Sharpe < 0 on minimum 8 completed trades** — supply-shock alpha has decayed; pairs structure is adding cost without edge.
3. **Beta mismatch (rolling 20-day realised beta deviates > 0.4 from entry estimate) for > 50% of trades** — OLS beta estimation is unreliable for the current market environment; recalibrate the beta-estimation window or method.
4. **4 consecutive pair unlock shorts produce negative net P&L** — the idiosyncratic supply shock is not materialising post-digestion; either crowding has front-run the trade to zero or unlock impact has structurally changed.
5. **Sector peer universe < 2 qualifying candidates per unlock** — the beta-hedge approach is operationally infeasible; revert to [[unlock-short-with-crowding-gate]] (outright short with crowding gate).

See [[when-to-retire-a-strategy]] for the broader framework.

## Instrument Structures

Unlock pair hedge deploys on the **pair** structure, expressing the unlock short as a hedged spread rather than an outright directional short.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Pair** | The defining structure. Short the unlocking token (the idiosyncratic supply-shock bet), long a beta-matched sector peer (the BTC-beta hedge). The two legs are sized to be beta-neutral: `long_notional = short_notional × (beta_A / beta_B)`, where beta is each token's rolling 30-day BTC-beta. |
| Single-asset | The base unlock short without the hedge is [[unlock-short-with-crowding-gate]]. This strategy explicitly replaces that single-leg expression with a pair to strip out market-direction risk. |
| Basket | An extension is possible: instead of one sector peer as the long leg, long a basket of sector peers (e.g., the [[l1-blockchains-basket]] as the hedge when shorting a single L1 unlock). This reduces idiosyncratic peer risk but adds construction complexity. |
| Cross-venue | Not directly deployed. If the unlocking token's HL perp is illiquid, the short can be expressed on a CEX perp instead, but the long hedge remains an HL perp of the sector peer. |

Mechanical difference from naked unlock shorting: the pair structure means the trade profits only from the *idiosyncratic* component of the unlock price impact. If the entire crypto market drops 5% during the unlock window, both legs decline roughly equally and P&L is approximately flat — the market direction is hedged. The edge (and risk) is concentrated in the *relative* underperformance of the unlocking token vs. its sector peer.

## Advantages

- **Beta hedge removes the largest noise source** — broad market direction accounts for 60–80% of a typical altcoin's short-term return variance; removing it isolates the supply-shock signal.
- **Wider holding window than outright short** — because market direction is hedged, the position can be held through a BTC rally without triggering a stop on the short leg alone.
- **Lower crowding sensitivity** — the beta-matched long leg is less obvious to crowded short operators who target only the unlocking token; the pair structure is less crowded than the outright unlock short.
- **Self-documenting beta estimate** — the OLS beta from the 20-day rolling window provides a real-time measure of how well the hedge is functioning; degrading beta (large deviation from entry estimate) is an explicit exit trigger.

## Disadvantages

- **Requires a suitable sector peer** — the strategy is operationally infeasible for tokens without ≥ 1 liquid, beta-matched sector peer. Unlocking tokens in niche or illiquid sectors (e.g., RWA, SocialFi) may have no suitable peer.
- **Two-leg transaction costs** — opening and closing four perp positions (entry + exit on both legs) at ~0.045% per fill = ~18 bps round-trip in fees; higher than the outright short's two fills.
- **Beta instability in volatile regimes** — the 20-day OLS beta becomes a poor real-time hedge during extreme market moves. The hedge works best in moderate-volatility regimes; in crisis periods, cross-asset correlations converge to 1.0 and the pair provides no protection.
- **Capital efficiency** — running two legs instead of one requires approximately 2× the margin capital for the same notional exposure on the short leg.

## Sources

- [[token-unlock-supply-event]] — the primitive supply-shock edge; the idiosyncratic supply pressure that both this page and [[unlock-short-with-crowding-gate]] exploit.
- [[unlock-short-with-crowding-gate]] — the outright short variant; the baseline to which this page adds beta hedging; both pages exploit the same supply-event primitive.
- [[pairs-trading]] — the general pairs/stat-arb framework; the beta-hedging methodology and spread-based exit logic are rooted in pairs-trading methodology.
- [[correlation-regime-pairs]] — the cointegration-based pairs variant; the rolling-correlation and beta-estimation methodology is consistent with the approach described there.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=30` — daily OHLCV for unlocking token and sector peer; 20-day rolling beta and correlation estimation
- `GET /api/v1/derivatives/funding-rates?coin={TOKEN}` — funding rate on unlocking token and sector peer; entry gate check
- `GET /api/v1/derivatives/open-interest?coin={TOKEN}` — OI qualification check for both legs
- `GET /api/v1/regimes/current` — regime context; block entry in `Structural_Shock`

**Historical data:**
- `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=200` — long daily OHLCV for beta-estimation backtest and unlock-event performance analysis

*Note: token unlock schedules are NOT currently available as a CryptoDataAPI endpoint. Source from external services (Token Unlocks, Coinglass, on-chain vesting contract event feeds). Perp funding and OI data for major tokens is available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=SOL"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

## Related

- [[unlock-short-with-crowding-gate]] — the outright short expression of the same unlock-supply edge; this page is the beta-hedged pairs expression — more capital-intensive, lower crowding sensitivity, market-neutral
- [[pairs-trading]] — the general long-short pairs methodology; the beta-matching and spread-exit logic
- [[pairs-with-funding-differential]] — cointegration-based pairs with funding confirmation; contrasts with this page's event-driven, beta-matched approach
- [[token-unlock-supply-event]] — the supply-shock primitive; the full unlock playbook including post-unlock relief long
- [[correlation-regime-pairs]] — rolling-correlation pairs gated on cointegration; the regime-gate methodology for pairs
- [[cross-sectional-relative-value]] — cross-sectional ranking within sectors; this page's sector-peer selection uses similar sector classification
- [[unlock-aware-momentum]] — momentum book that avoids unlock supply headwinds; the momentum-layer complement to this page's pairs structure
- [[event-driven-trading]] — the broader event-driven category
- [[funding-rate]] — funding check on both legs at entry
- [[open-interest]] — OI qualification for liquidity of both legs
- [[perpetual-futures]] — the instrument for both legs
- [[statistical-arbitrage]] — the broader stat-arb category
- [[edge-taxonomy]] — informational + structural + analytical classification
- [[failure-modes]] — beta instability, no suitable peer, crowding
- [[when-to-retire-a-strategy]] — kill vs pause framework
