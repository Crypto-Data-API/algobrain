---
title: "Calendar Spread"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: good
tags: [options, crypto, derivatives, volatility, swing-trading, bitcoin, ethereum]
aliases: ["Calendar Spread", "Time Spread", "Horizontal Spread", "Crypto Calendar Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[diagonal-spread]]", "[[ratio-calendar-spread]]", "[[iron-condor]]", "[[double-diagonal]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[max-pain]]", "[[gamma-exposure]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_deribit_only
    role: universe
    rule: "BTC and ETH Deribit options only; alt options rarely list usable strikes in two expiries"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "These are the two coins with Deribit implied vol served. Option quotes come from Deribit itself."
  - id: front_leg_7_21_dte
    role: entry
    rule: "Sell the front option about 7-21 days out"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "term_structure lists the nearest 12 Deribit expiries. It is Pro Plus and empty on lower tiers."
  - id: back_leg_30_60_dte
    role: entry
    rule: "Buy the back option, same strike and type, about 30-60 days out, roughly 3-4x the front leg's DTE"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
  - id: strike_atm
    role: entry
    rule: "Strike ATM (nearest listed strike to spot) for a neutral view; slightly OTM for a directional lean"
    runnable: partial
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "Spot is served (oracle_price is a CEX spot composite close to Deribit's index); the listed strike grid is not, so the nearest strike comes from Deribit."
  - id: debit_30_50_pct
    role: entry
    rule: "Net debit typically 30-50% of the back leg's price; the debit is the whole max loss"
    runnable: false
    note: "Needs the two legs' quotes; no option prices are served."
  - id: front_vol_at_or_above_back
    role: filter
    rule: "Enter when front-month implied vol is at or above the back-month's (flat-to-backwardated near term); contango is expensive to enter"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].atm_iv
    note: "Compare atm_iv of the two expiries you trade. Pro Plus. No term-structure history is served, so this cannot be replayed."
  - id: dvol_bottom_third
    role: filter
    rule: "DVOL low and expected to rise: roughly the bottom third of its trailing-year range"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    replay: /api/v1/volatility/implied
    replay_field: items[].history[].dvol
    note: "Place the latest dvol in its range over history. Only about 180 daily closes are served (Pro Plus), so the range is six months, not a year; the expected rise is a forecast."
  - id: vol_regime_compressed
    role: filter
    rule: "Enter when the coin's vol regime reads compressed (cheap back-month vega)"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "From the page's AI-agent workflow. Its tip: the 60-day history on this route shows the typical compressed-to-expanding cycle length; match the front expiry to it."
  - id: max_pain_near_strike
    role: filter
    rule: "Max pain pins near the chosen strike"
    runnable: partial
    endpoint: /api/v1/market-intelligence/options
    field: data[].max_pain
    replay: /api/v1/backtesting/snapshots?data_type=coinglass_options&start={start}
    replay_field: snapshots[].data[].max_pain
    note: "BTC only (no ETH max pain), computed on the Deribit expiry with the largest open interest. The page gives no distance for 'near'."
  - id: range_now_spike_later
    role: filter
    rule: "Ideal sequence: range_low_vol now with vol_spike or squeeze probability building later; skip an in-progress vol shock"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "The 'now' half is mechanical (label range_low_vol, not vol_spike). 'Building later' is a forecast; probabilities.regime_transitions gives the 24h odds of moving to vol_spike or squeeze."
  - id: catalyst_between_expiries
    role: entry
    rule: "Optionally place a known catalyst (major unlock, ETF decision, FOMC/CPI) between the two expiries"
    runnable: partial
    endpoint: /api/v1/event/calendar?window_days=30&symbol={coin}
    field: items[].days_until
    note: "Compare days_until with the two expiries' expiry_days. Unlocks and macro prints are on the calendar (30 days out); ETF decisions are not."
  - id: profit_target_25_50
    role: exit
    rule: "Close at 25-50% of the debit in added spread value"
    runnable: true
    input: position
    note: "The spread's mark comes from Deribit; no option prices are served."
  - id: roll_front_leg
    role: exit
    rule: "At front expiry, if spot is still near the strike, sell a new front month against the surviving back leg"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "'Near the strike' has no distance on the page."
  - id: stop_half_debit_or_1_sigma
    role: stop
    rule: "Close if the spread falls to about 50% of the debit, or spot moves more than about 1 sigma from the strike"
    runnable: partial
    input: position
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].atm_iv
    note: "The debit test is mechanical from the position. The page does not define sigma; one reading is spot x atm_iv/100 x sqrt(DTE/365) for the front expiry."
  - id: no_front_leg_into_expiry
    role: exit
    rule: "Never carry the near leg into its final days near the money"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "Neither 'final days' nor 'near the money' is quantified."
  - id: dvol_crush_exit
    role: exit
    rule: "Cut early if back-month implied vol collapses in a market-wide vol crush"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol_change_24h
    note: "dvol_change_24h is in vol points; the back expiry's own atm_iv is in term_structure. The page gives no size for a collapse."
  - id: funding_spike_warning
    role: filter
    rule: "Funding spikes warn of the term-structure inversion that hurts a long calendar"
    runnable: partial
    endpoint: /api/v1/derivatives/funding-rates?coin={coin}
    field: binance.current_rate
    note: "From the page's AI tips; no threshold or action is given."
---

# Calendar Spread

## Overview

A calendar spread (also **time spread** or **horizontal spread**) sells a **near-dated** option and buys a **longer-dated** option at the **same strike**. It is the canonical **long-vega, positive-theta, defined-risk** structure: the front leg decays faster than the back leg, so the spread widens as time passes while the underlying sits near the strike. Maximum loss is the net debit paid. Unlike the short-vol credit structures in [[crypto-options-volatility-selling]] (short vega), the calendar is the one you reach for when implied vol is **low and expected to rise** — it is a bet on the *shape and level* of the volatility term structure, not on direction.

In crypto this is a [[deribit]] BTC/ETH trade on the **[[dvol|DVOL]] term structure**. You sell a rich or normal front-month [[implied-volatility|IV]] and own a cheaper or steady back-month, profiting if spot pins the strike while back-month DVOL holds up or rises. Because Deribit options are **European and cash-settled**, the front short leg cannot be assigned early — removing the pin/assignment headache that dogs American-style equity calendars. The main crypto constraints are Deribit's **~1-year tenor ceiling** (the "long" leg is months, not years) and the fact that crypto vol crushes are fast and deep, which can gut the long leg's vega even when spot cooperates.

## Construction

Two legs, same strike, two expiries, on BTC or ETH [[deribit]] options:

| Leg | Action | Tenor | Purpose |
|---|---|---|---|
| Front | Sell 1 option (call or put) | ~7-21 DTE | fast theta decay (income engine) |
| Back | Buy 1 option, same strike/type | ~30-60 DTE | slow-decaying long vega (anchor) |

- **Strike selection:** ATM (nearest listed strike to spot) for a neutral view; slightly OTM for a directional lean (a call calendar above spot is mildly bullish, a put calendar below spot mildly bearish).
- **Type:** calls and puts give near-identical calendars at the same strike (put-call parity), so pick whichever side is fractionally cheaper on Deribit's book.
- **Net debit** = back premium − front premium, typically **30-50%** of the back-leg price. The debit is the entire max loss.
- **Expiry gap:** the back leg should carry roughly **3-4×** the front's DTE so the decay differential is meaningful.
- **DVOL term structure:** prefer entering when the front-month DVOL is **at or above** the back-month (flat-to-backwardated near-term), so you sell relatively rich front vol and own relatively cheap back vol.

## Payoff & breakevens

Evaluated **at front-month expiration** (the only clean snapshot, because the legs expire at different times):

- **Max profit:** spot exactly at the strike `K` at front expiry — the front leg expires worthless while the back leg retains full extrinsic value. The exact peak depends on back-month DVOL at that moment and cannot be known precisely at entry.
- **Max loss:** the **net debit**, on a large move in either direction (both legs collapse toward the same intrinsic value and the time-value differential vanishes).
- **Breakevens:** two, straddling `K`, whose width depends on back-month IV at front expiry — wider when back-month DVOL is higher. They cannot be pinned exactly at entry.

```
Calendar spread P&L at FRONT-month expiration

  +max  ┤            ╱▔▔╲              ← peak at strike K
        │          ╱      ╲
    0 ──┼────────╱──────────╲────────────
        │       ╱            ╲
 −debit ┤━━━━━━╱              ╲━━━━━━━━━━  ← capped loss = net debit (large move either way)
        └──────────────────────────────────
              BE_lo      K     BE_hi
```

The payoff is a smooth, rounded tent peaking at `K` — the profit zone is widest at the strike and both breakevens migrate with IV.

## Greeks profile

- **[[delta]]:** ≈ 0 near `K`; grows directional as spot drifts away (long-ish above `K` for a call calendar, short-ish below).
- **[[gamma]]:** **negative** — the front short leg's gamma dominates near its expiry, which is exactly why the front leg must be closed or rolled before it expires (crypto gaps make this acute).
- **[[theta]]:** **positive** — the front leg decays faster than the back leg; the core profit driver while spot stays near `K`.
- **[[vega]]:** **positive** — the defining sign. The back-month leg carries more vega than the front, so the position *gains* when [[dvol|DVOL]] rises and *loses* in a vol crush. This positive-theta / **positive-vega** pairing is rare and valuable: a defined-risk way to be long vol and still collect decay.

## Market view / when to use

- You expect BTC/ETH to **pin or hover near the strike** through the front-month expiry — no big trend, no violent gap.
- **[[dvol|DVOL]] is low and you expect it to rise** (roughly the bottom third of its trailing-year range): the opposite regime to selling an [[iron-condor]] or [[short-strangle]]. You want to *buy* vol cheap via the net-long-vega back leg.
- **Term structure is favourable:** front-month DVOL flat-to-rich versus back-month (contango is expensive to enter; steep backwardation compresses profit).
- You want a **defined-risk long-vol expression** — max loss is the debit, unlike a naked long straddle's full premium bleed, and far tamer than short-vol tail risk.
- Optionally, place the calendar so a **known catalyst** (major unlock, ETF decision, FOMC/CPI) falls *between* the two expiries — the front expires before the event while the back leg is long the event's IV inflation.

## Adjustments & management

- **Profit target:** close at **25-50% of the debit** in additional spread value (calendar upside is modest and lumpy — bank it).
- **Roll the front leg:** at front expiry, if spot is still near `K`, buy back / let the front expire and **sell a new front-month** against the surviving back leg, rolling into a fresh calendar and lowering effective cost basis.
- **Convert to a [[diagonal-spread]]:** if spot has drifted, re-strike the new front leg toward the current price — turning the calendar into a diagonal with a directional lean.
- **Stop:** close if the spread value falls to **~50% of the debit**, or if spot moves more than ~1σ from `K` (both legs heading to parity).
- **Front-leg gamma trap:** never carry the near leg into its final days near the money — crypto's 24/7 gaps can jump the front strike overnight with no session close to cap the move.
- **DVOL-crush exit:** if back-month DVOL collapses (a market-wide vol crush), the long leg bleeds even at the right price — cut early rather than hope.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the dominant share of BTC/ETH options open interest and is effectively "the market." **Alt options (SOL and below) rarely list usable dated strikes in two expiries** at the same strike, so calendars are a BTC/ETH-only structure — the second-expiry liquidity requirement is stricter than for a single-expiry vertical.
- **[[dvol|DVOL]] term structure is the trade:** the calendar is long back-month vega and short front-month vega, so the *slope* of the DVOL curve drives entry economics. A steep front-rich (backwardated) curve is the ideal cheap entry; a contango curve (back richer than front) is expensive and starts you with no edge.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options for a clean USD debit, breakevens, and P&L. **Inverse (coin-margined)** options are BTC/ETH-settled and embed a quanto-like curvature — the collateral's USD value moves with spot, distorting the textbook tent. Use inverse only if you *want* the embedded coin exposure.
- **European cash settlement — no pin/assignment risk:** Deribit options are European, cash-settled to the ~30-minute index TWAP at **08:00 UTC**. The front short leg **cannot be assigned early**, eliminating the pin-risk and early-exercise hazards that make American-style equity calendars fiddly. You still manage front-leg gamma, but there is no assignment surprise.
- **24/7 & weekend gaps:** continuous trading means rolls can be timed to any hour, but the front strike can be breached overnight with no close — favour rolling the front leg early rather than holding into a thin weekend book.
- **[[funding-rate|Perp-funding]] interaction:** crypto skew and the vol term structure are shaped by the [[perpetual-futures|perp]] book. Rich positive funding (leveraged longs paying) firms call skew and steepens near-term call vol; a post-selloff funding flip fattens put vol. This tilts whether a call- or put-side calendar is the cheaper build.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit options get **no 60/40 blended US tax treatment** — the rolled front-leg income and any spread gain are ordinary/short-term (US) or trader-status-dependent (AU). After-tax net is below an SPX calendar's.
- **Tenor ceiling:** Deribit lists tenors out to roughly **a year** (quarterly expiries), with thinner far-dated strikes than US equity LEAPS. The "long" leg is a *months*-long anchor, not a multi-year one.

## Risks

- **Large directional move:** a gap through the profit zone sends both legs toward the same parity value and destroys the time-value differential — the single most common loss mode, and worse in crypto where gaps are unbounded.
- **Back-month DVOL crush:** a broad vol collapse deflates the long leg's vega even if spot sits at the strike — a real, often-misunderstood mid-trade drawdown.
- **Backwardation entry:** buying when the front is cheaper than the back (contango) means overpaying for the structure and starting with negative edge.
- **Front-leg gamma into expiry:** short-gamma near the strike, with no overnight close to cap a move.
- **Second-expiry liquidity:** the back-month strike can be wide, especially off the ATM line; two-expiry, same-strike depth exists only on BTC/ETH.
- **Wrong catalyst timing:** if the anticipated back-month IV expansion never materialises, the long leg just bleeds theta.

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$60,000**; BTC [[dvol|DVOL]] **48** and near the bottom third of its trailing-year range (you expect it to rise); front-month DVOL slightly rich to back-month (mild backwardation — favourable). No trend; expect BTC to hover.

**Trade (per 1-BTC contract, ATM call calendar at $60,000):**
- Sell 1 front call, 10 DTE, @ **$1,600**.
- Buy 1 back call, 38 DTE, @ **$3,100**.
- **Net debit = $3,100 − $1,600 = $1,500** — the entire max loss.

**Path A — base case (pin + vol rise).** Over 10 days BTC oscillates $58k-$62k and finishes near $60k at front expiry; DVOL drifts 48 → 54. The front expires ~worthless; the surviving 28-DTE back call is worth ~$2,700. Spread value $2,700 vs $1,500 debit → **+$1,200/contract**. Roll into a new front-month for another cycle, or bank it.

**Path B — big move.** A macro headline sends BTC +14% to ~$68,400 in three days. Both calls go deep ITM and converge toward intrinsic; the time-value differential collapses. Close for ~$900 → **−$600/contract** (loss capped by the debit, well short of the −$1,500 floor).

**Path C — vol crush.** BTC pins $60k but a market-wide DVOL crush takes 48 → 33. The back leg's vega deflates faster than the front decays; spread marks ~$1,050. Cut at the ~50%-of-debit stop → **−$450/contract** — the exact long-vega risk the structure carries.

## Sources

- [[greeks-live]] / [[deribit]] documentation — [[dvol|DVOL]] index and term structure, IV surface, USDC (linear) vs inverse settlement, European 08:00 UTC cash settlement, tenor ladder.
- [[book-option-volatility-and-pricing]] — Natenberg on time spreads, the differential theta decay between near- and far-dated options, and how the volatility term structure prices the calendar (mechanics port to crypto; the vol crush and gap tail are sharper).
- McMillan, *Options as a Strategic Investment* — calendar and diagonal construction and rolling (re-scoped to Deribit's European cash-settled BTC/ETH options).

## Getting the Data (CryptoDataAPI)

Strike/expiry selection, the [[dvol|DVOL]] level and its **term structure** come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the **volatility-regime, funding, and options-flow** context to time entries and read the tape.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal): calendars want *compressed* → *expanding*
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (pinning context for strike selection)
- `GET /api/v1/quant/gex` — dealer Gamma Exposure (whether spot is likely pinned near the strike or cascade-prone)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the crypto skew/term-structure driver

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation vs DVOL
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — OHLCV history for roll/backtest studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — enter when `GET /api/v1/volatility/regime` reads `compressed` (cheap back-month vega) and `GET /api/v1/market-intelligence/options` max pain pins near the chosen strike
- **Regime gate** — `GET /api/v1/quant/market`: the ideal sequence is `range_low_vol` now with `vol_spike`/`squeeze` probability building later; an in-progress vol shock means the vega is already repriced
- **Backtest** — replay strike-vs-path outcomes with `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09); the IV term structure itself is not archived by CDA, so validate the regime-timing leg against `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — the 60-day `/api/v1/volatility/regime/{symbol}` history reveals the typical compressed→expanding cycle length — match the front expiry to it; funding spikes on `/api/v1/derivatives/funding-rates?coin=BTC` warn of the term-structure inversion that hurts a long calendar.

## Related

- [[diagonal-spread]] — the same structure with a strike offset; a diagonal is a calendar with a directional lean
- [[ratio-calendar-spread]] — the unbalanced-ratio variant (income- or convexity-tilted)
- [[double-diagonal]] — two diagonals (call + put) for range-bound coverage
- [[iron-condor]] — the short-vega structure the calendar is the regime-opposite of
- [[crypto-options-volatility-selling]] — the short-vol book the long-vega calendar hedges against across the DVOL cycle
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and surface source
- [[dvol]], [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]] — the perp linkage that shapes crypto skew and term structure
- [[max-pain]], [[gamma-exposure]] — dealer-positioning / pinning context
- [[section-1256-contracts]] — the tax treatment crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position (long vega, positive theta)
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
