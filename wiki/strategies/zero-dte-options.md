---
title: "Zero DTE Options"
type: strategy
created: 2026-05-07
updated: 2026-07-19
status: review
tags: [options, crypto, derivatives, volatility, scalping, market-microstructure]
aliases: ["Zero DTE", "Same-Day Crypto Options", "Daily-Expiry Options", "Crypto 0DTE Overview"]
strategy_type: quantitative
timeframe: scalp
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[0dte-trading]]", "[[crypto-options-volatility-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[iron-fly]]", "[[gamma]]", "[[theta]]", "[[gamma-exposure]]", "[[gamma-scalping]]", "[[dvol]]", "[[implied-volatility]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]

# Edge characterization
edge_source: [structural, behavioral]
edge_mechanism: "Short-dated crypto options are priced to embed a realized-vol premium at the front end of the surface (the front-end implied move typically exceeds the realized intraday move on non-cascade days); seller collects rich theta in hours and the edge persists because there is no competing retail-0DTE demand large enough to cheapen it, and because the market path is driven by the perp tape, not option-dealer hedging. Behavioral element: high hit rate of selling induces over-sizing right before shock days."

# Data and infrastructure requirements
data_required: [options-chain, funding-rates, volatility-regime, open-interest, liquidations]
min_capital_usd: 5000
capacity_usd: 20000000
crowding_risk: low

# Performance expectations
expected_sharpe: 0.5
expected_max_drawdown: 0.15
breakeven_cost_bps: 80

# Kill criteria
kill_criteria: |
  - rolling 30-day realized move exceeds 0DTE implied move on > 40% of days → regime break; pause selling
  - single position loss exceeds 2.5× credit received → exit immediately; no averaging
  - vol-shock regime score > 70 on CryptoDataAPI → pause all 0DTE selling until regime clears
  - liquidation cascade signal active (DVOL spike > 30% intraday) → flatten all short-gamma immediately
---

# Zero DTE Options

## Edge source

Short-dated crypto options carry a **structural** realized-vol premium at the front end of the Deribit surface: the daily implied move typically exceeds the intraday realized move in non-cascade conditions, making the short-credit seller structurally advantaged. Unlike equity 0DTE — where a mass of retail buyers has compressed premium — crypto 0DTE has no equivalent retail 0DTE bid, so the front-end theta remains rich relative to intraday realized vol. A secondary **behavioral** element: sellers over-size on the back of high hit rates, and that over-confidence is the mechanism that turns quiet-period success into shock-day blowups. The buyer side (long straddles/strangles before catalyst) has a pure informational edge only when the trader has an asymmetric view of the event outcome; without that, buying rich implied vol in 0DTE is a negative-EV donation.

## Null hypothesis

Under the null hypothesis (no edge in the front-end pricing), the 0DTE credit collected would on average equal the realized move less transaction costs, leaving the seller with zero expected return before fees. The argument against this null is that: (1) the crypto vol surface is not continuously arbitraged by sophisticated flow the way SPX is; (2) the Deribit structure (daily cash settlement at 08:00 UTC) creates a gap between equity-style microstructure and crypto's perp-driven price discovery; and (3) there is no reliable mass of retail demand bidding up the 0DTE surface from below. If over time a competitor segment (e.g., large on-chain vaults, structured-product desks) systematically bids same-day IV, this null would flip and the edge would shrink.

Zero-DTE (0DTE) options are options that expire **on the same day they are traded**. In crypto the 0DTE tenor is served by [[deribit]] daily-expiry BTC and ETH options, which settle at **08:00 UTC** to the Deribit index. Deribit lists a full expiry ladder — daily, weekly, monthly, quarterly — so on any day there is a same-day-expiry chain. This page is the **instrument and market-structure overview**; the trading playbook (structures, entries, management) lives on [[0dte-trading]].

Crypto 0DTE is a nascent, distinctly-behaved corner of the options market rather than the dominant force it has become in equities. In US index options, same-day SPX contracts grew to ~40–50% of volume after [[cboe|Cboe]] completed daily expirations in 2022; crypto has no equivalent single-venue concentration of retail 0DTE flow, and the 24/7 spot/perp tape — not option hedging — dominates the intraday path. What crypto 0DTE *does* share with equities is the Greek profile: the highest [[theta]]-per-dollar on the surface, paired with the highest [[gamma]] of any tradeable structure and negligible [[vega]]. Selling 0DTE premium is the front-end of the [[crypto-options-volatility-selling|crypto vol-selling]] world; buying it is the most convex short-horizon bet available.

## Construction

0DTE is a *tenor*, not a single structure; the tradeable expressions are the short-dated versions of the standard menu on Deribit BTC/ETH:

- **Short-premium (where the structural edge is hypothesised):** 0DTE [[iron-condor|condors]], [[iron-fly|flies]], and credit spreads — always defined-risk via long wings at this gamma.
- **Long-premium:** an ATM [[straddle-strangle|straddle]] bought before a scheduled catalyst.
- **Directional:** a single 0DTE call or put as a defined-risk lottery ticket.

Each BTC option = 1 BTC, each ETH option = 1 ETH; both are **cash-settled to the Deribit index** at the 08:00 UTC expiry — **no assignment, no physical delivery**. Premium is quoted in the coin (inverse) or USDC (linear).

## Payoff & breakevens

At the same-day settle the payoff shape is identical to the longer-dated structure — a short condor is a flat-topped tent capped by its wings; a long straddle is a "V" — but every Greek is compressed into the hours before 08:00 UTC, so the *path* is far more violent than the static diagram implies.

```
 P/L (0DTE short condor at 08:00 UTC settle)
  │        ┌──────────────────┐   ← max profit = net credit (full theta in hours)
  │       /                    \
 0│──────/──────────────────────\──── spot →
  │     /                        \
  │____/                          \___ ← max loss = wing width − credit (realized in MINUTES)
       LP SP                  SC LC
```

- Short condor/spread: max profit = credit; max loss = wing width − credit; breakevens = short strike ± credit.
- Long straddle: max loss = debit; breakevens = strike ± debit; upside unbounded.

## Greeks profile

0DTE is the purest **short-gamma / long-theta** expression on the surface (for the seller), with vega nearly irrelevant — it is a *realized-vol* game, not an *implied-vol* game.

| Greek | Sign / magnitude | Intraday behaviour | Implication |
|-------|------------------|--------------------|-------------|
| [[theta]] | Positive, **very high per dollar** | Bulk accrues in the hours to the 08:00 UTC settle | The reason to sell — highest theta velocity on the surface |
| [[gamma]] | Negative, **extreme** (largest near short strikes into the settle) | Explodes in the final hours | A small adverse move flips P&L violently |
| [[delta]] | ≈ 0 at entry | Whips to ±large as spot nears a short strike | Becomes a fast directional loser when tested |
| [[vega]] | Negative but **small** | Little time value to lose | Budgeted against a **gamma** cap, not a vega budget |

Because [[dvol|DVOL]] is a 30-day index and 0DTE has no time for implied vol to matter, the whole edge is the rich front-end theta collected against enormous gamma — the same [[theta]]-positive / [[gamma]]-negative signature as the longer-dated [[iron-condor]] and [[short-strangle]], compressed into a single day.

## Market view / when to use

- **Sell 0DTE premium** in quiet, catalyst-free sessions when the day's implied move looks rich relative to likely realized intraday movement, and the [[volatility-regime|vol regime]] is not a live shock.
- **Buy 0DTE premium** only into a scheduled catalyst with uncertain direction and a bet that realized beats the already-elevated implied move.
- **Stand aside** during vol-shock regimes, active liquidation cascades, and around major macro prints unless the event *is* the trade. Full entry/exit/sizing rules on [[0dte-trading]].

## Adjustments & management

- Take profit at ~**50% of max credit** on short spreads/condors; hard stop at ~**2× credit**; flatten a tested position before the final hours into the 08:00 UTC settle (crypto's analogue of the equity "close before the bell").
- **Delta-hedge on the perp** to neutralise residual delta; a long-gamma 0DTE straddle can be [[gamma-scalping|gamma-scalped]] against the hedge.
- Size against a **gamma** budget (≤ ~1–2% of book per position), not a vega budget.

## Crypto specifics

- **Venue & instrument.** [[deribit]] daily-expiry BTC/ETH options, **08:00 UTC** index settlement. [[greeks-live]] is the short-dated-surface workbench. Off BTC/ETH and off the front expiry, liquidity is too thin for a viable 0DTE market.
- **Inverse vs linear settlement.** Inverse (coin-margined) options denominate premium/P&L in the coin; USDC-margined (linear) options give clean USD P&L — preferred for a pure gamma/theta bet.
- **[[dvol|DVOL]] context, not signal.** DVOL is a 30-day index; the 0DTE game is short-dated *realized* vol vs the day's implied move. **DVOL and the IV surface come from Deribit / [[greeks-live]], not [[cryptodataapi|CryptoDataAPI]]**.
- **24/7 and no close.** There is **no market close** to cap a move; the reference point is the 08:00 UTC settle, and **weekend** daily expiries trade against thin liquidity — the defining structural difference from SPX 0DTE.
- **No [[section-1256-contracts|§1256]].** Offshore Deribit options get **no §1256 60/40 treatment** — US ordinary short-term rates; AU CGT/income by trader status; heavy record-keeping given high turnover.
- **Flow is perp-driven.** The intraday path is set by the [[funding-rate|perp]]/spot tape and liquidation cascades, not by option-dealer hedging as in equities — crypto 0DTE feedback loops run through the perp book.
- **Alt-option liquidity.** Daily-expiry options barely exist off BTC/ETH; there is no viable alt 0DTE market.

## Risks

- **Intraday vol shock / liquidation cascade** that gaps BTC/ETH 2–5% in minutes — the short condor's max loss realized before any exit.
- **Extreme gamma into the settle** — the position's whole risk concentrates in the final hours to 08:00 UTC.
- **Cost fragility** — wide short-dated spreads plus taker fees (0.03% of underlying, capped at 12.5% of premium) consume a large share of a small credit; 0DTE is the most cost-sensitive premium-selling tenor.
- **Weekend / 24/7 exposure** with no session break.
- **Crowding & nascency** — the crypto 0DTE market is thin off the front expiry, and edge can invert quickly in stress.
- **Behavioral** — the high hit rate of selling breeds over-sizing right before the shock day.

## Worked crypto example

*Illustrative round numbers — not a recommendation or backtest.*

**0DTE credit-spread pair on ETH.** ETH spot **$3,000** at 20:00 UTC, expiry 08:00 UTC (~12 hours), day's implied move ≈ $60, no scheduled macro.
- Sell 3,050 call / buy 3,090 call (credit ≈ $9).
- Sell 2,950 put / buy 2,910 put (credit ≈ $8).
- Total credit ≈ **$17** per structure; wings $40 wide → max loss ≈ $40 − $17 = **$23**.
- *Win:* ETH holds $2.97k–$3.03k into the settle; both spreads expire worthless → keep **$17** (≈ 74% return on the $23 at risk in ~12 hours).
- *Loss:* a cascade at 02:00 UTC pushes ETH to $3,075; the call spread goes max → loss ≈ **−$23**, realized in minutes. The long wings are the only reason the loss is bounded — the whole point of trading 0DTE defined-risk in crypto.

## Capacity limits

0DTE capacity is **much tighter** than longer-dated premium selling because same-day liquidity is thin.

- **BTC 0DTE at-the-money/near-the-money options**: best liquidity; a small operator can sell $200–500K notional credit spreads without material slippage. Beyond $500K the spreads widen noticeably.
- **ETH 0DTE**: similar but typically 2–3× less liquid than BTC equivalent strikes; practical cap ~$100–200K notional per position.
- **Defined-risk structures (condors/flies)**: the wing legs often have thin markets at same-day expiry; realistic working size $50–200K notional before impact becomes problematic.
- **Aggregate book**: a systematic 0DTE program can run $500K–$2M book without regularly moving the market; above that, the act of entering depresses the credit received, which narrows the edge. Larger accounts should extend to weekly/monthly structures rather than scaling 0DTE.
- **Crowding risk**: low — the crypto 0DTE market is not retail-crowded like SPX. But the market is small, so the risk is **capacity exhaustion**, not crowding-induced edge compression.

## What kills this strategy

1. **Intraday liquidation cascade** — a BTC/ETH gap of 2–5% in minutes defeats any short-condor before exit is possible; the wing limits the loss but the full max-loss is still 1–2× the credit received. LUNA (2022-05), FTX (2022-11), 2025-10-10 cascade all produced 0DTE-killing moves.
2. **Regime blindness** — selling 0DTE in a live vol-shock regime where realized daily range already exceeds the implied move; if the vol-regime score is elevated, selling is a negative-EV donation to the cascade.
3. **08:00 UTC pin risk** — an active gamma-squeeze into the Deribit settlement creates extreme delta whips in the final hour; positions that are "nearly safe" at 06:00 UTC can go max-loss by 08:00 UTC without a chance to exit at a reasonable spread.
4. **Overconfidence from high hit rate** — 0DTE short-credit has a high win rate (most days are quiet) that breeds over-sizing; the rare loss day can exceed many months of premium.
5. **Cost drag** — short-dated Deribit spreads (3–8 vol points round-trip) are a permanent friction; if the net edge is narrow, fees consume the entire alpha.
6. **Thinning liquidity on expiry** — as the 08:00 UTC settle approaches, bid-asks on tested positions widen dramatically; in a real adverse move, getting out cleanly is expensive or impossible.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Rolling 30-day ratio of "realized intraday range > 0DTE implied move" exceeds 40% of days → regime break; suspend selling until ratio falls below 25%.
- Any single-position loss exceeds 2.5× the credit received → exit immediately, regardless of time to settle; no averaging or holding hope.
- CryptoDataAPI vol-regime-score > 70 on a selling day → no new 0DTE shorts; clear existing to flat if any approach the short strike.
- DVOL intraday spike > 30% from the session open → flatten all short-gamma immediately; this is a liquidation-cascade signal.
- Net 30-day P&L from 0DTE is negative for 3 consecutive months despite disciplined regime filters → pause, review structural assumptions, verify the front-end theta premium still exists.

## Getting the Data (CryptoDataAPI)

**DVOL and the raw IV surface come from Deribit / [[greeks-live]]** (Deribit products; CDA does not serve them). [[cryptodataapi|CryptoDataAPI]] supplies the intraday structural context — dealer gamma, options OI, funding, liquidations, and short-term momentum — that governs the 0DTE tape.

**Live data:**
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory + liquidation profile); the short-vs-long-gamma read for the day
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (pin context into the settle)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, an intraday flow driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (the cascade that gaps 0DTE positions)
- `GET /api/v1/volatility/regime` — per-asset vol regime (a vol-shock reading vetoes 0DTE selling)
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=5m&limit=1000` — intraday OHLCV for short-dated realized-vol vs the implied move
- `GET /api/v1/backtesting/klines` — deep archive for intraday backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].
**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma)


## Related

- [[0dte-trading]] — the trading playbook (structures, entries, management) for this instrument
- [[crypto-options-volatility-selling]] — the broader short-vol / variance-risk-premium context
- [[short-strangle]] / [[strangle]] — the longer-dated equivalent on the same premium
- [[iron-condor]] / [[iron-fly]] — the defined-risk building blocks used at 0DTE tenors
- [[gamma]] / [[theta]] / [[vega]] / [[delta]] — the intraday Greek profile
- [[gamma-exposure]] — dealer-gamma and the intraday feedback context
- [[gamma-scalping]] — the long-gamma counterparty approach
- [[dvol]] / [[implied-volatility]] — the 30-day background vol context
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[funding-rate]] — the perp linkage that drives the intraday path

## Sources

- [[deribit]] / [[greeks-live]] documentation — daily-expiry listing, 08:00 UTC index settlement, cash settlement, inverse vs USDC-margined contracts, block minimums (25 BTC / 200 ETH), fee schedule.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — gamma/theta behaviour near expiration.
- [[gamma-exposure]] — dealer-gamma framework for the intraday feedback discussion.
