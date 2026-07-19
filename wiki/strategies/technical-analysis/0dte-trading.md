---
title: "0DTE Options Trading"
type: strategy
created: 2026-04-13
updated: 2026-07-19
status: review
tags: [options, crypto, day-trading, scalping, gamma, 0dte, derivatives]
aliases: ["Crypto 0DTE", "Same-Day Crypto Options", "BTC 0DTE", "Daily-Expiry Options Trading"]
strategy_type: technical
timeframe: intraday
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[zero-dte-options]]", "[[options]]", "[[gamma]]", "[[theta]]", "[[iron-condor]]", "[[iron-fly]]", "[[short-strangle]]", "[[straddle-strangle]]", "[[gamma-scalping]]", "[[gamma-exposure]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]

# Edge characterization
edge_source: [structural, behavioral]
edge_mechanism: "Front-end Deribit implied daily move exceeds realized intraday range on catalyst-free days; the short-credit seller collects the full-day theta in hours. Behavioral component: GEX-informed directional trades exploit the mechanical hedging flows of short-gamma dealers that systematically amplify or dampen moves. Crypto 0DTE edge is distinct from equities — no competing retail-bid compression, perp-funded intraday path, and 08:00 UTC settlement mechanics favor the disciplined seller in calm regimes."

# Data and infrastructure requirements
data_required: [options-chain, funding-rates, volatility-regime, open-interest, liquidations]
min_capital_usd: 5000
capacity_usd: 10000000
crowding_risk: low

# Performance expectations
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 100

# Kill criteria
kill_criteria: |
  - rolling 30-day win rate on short condors < 55% → regime break; pause selling
  - any single position exceeds 2× credit loss → exit immediately
  - vol-shock regime score > 70 → no new 0DTE shorts; flatten short-gamma before 08:00 UTC
  - DVOL intraday spike > 30% from open → flatten all short-gamma immediately
---

# 0DTE Options Trading

## Edge source

The 0DTE trading edge has two components:

**Structural (short-credit bias):** Deribit's front-end daily implied move — derived from same-day IV — systematically overstates the intraday realized range on catalyst-free days. The seller collects that discrepancy as theta in hours, not weeks. Unlike SPX 0DTE (where a mass of retail buyers has bid up the front-end surface), crypto 0DTE has no equivalent retail 0DTE demand; the implied move is not inflated by speculative call/put buying, so the structural premium is real and persistent.

**Behavioral / GEX-driven (directional variant):** When dealers are **short gamma** (net short the near-term strikes), their delta hedges are procyclical — they must sell into declines and buy into rallies, mechanically amplifying moves toward the next gamma level. This creates predictable, non-random momentum bursts that a GEX-aware directional 0DTE trade can exploit. See [[gamma-exposure]].

The behavioral risk on the *sell* side is also here: the high hit rate of short condors breeds over-confidence, causing position over-sizing exactly before shock days — a behavioral pattern that periodically concentrates losses.

## Null hypothesis

Under the null (no front-end premium and no GEX signal), a 0DTE short condor is a zero-expectancy bet less transaction costs: the credit received would, on average, equal the realized range minus fees, leaving the seller with a small negative carry. The argument against this null: the Deribit daily-expiry surface is not continuously arb'd by sophisticated vol desks — the front-end is less efficiently priced than SPX — so a persistent implied-realized discrepancy can survive. If a large on-chain vault or market maker begins systematically selling same-day IV to offset the premium, this discrepancy would compress and the null would hold.

0DTE ("zero days to expiration") options are contracts that expire on the **same day** they are traded. In crypto this means [[deribit]] BTC and ETH options on their nearest daily expiry, which settles at **08:00 UTC** to the Deribit index. Deribit lists daily expiries (plus weeklies, monthlies and quarterlies), so on any given day there is a same-day-expiry chain to trade. Crypto 0DTE is far younger and smaller than the equity 0DTE complex — where same-day SPX options are ~40–50% of volume — but short-dated BTC/ETH options are a growing, distinctly-behaved corner of the Deribit tape. This page is the **how-to-trade playbook**; the instrument and market-structure overview lives on [[zero-dte-options]].

0DTE is not "options with less time" — it is a qualitatively different instrument. With [[time-to-expiration]] measured in hours, [[gamma]] is at its absolute maximum and [[theta]] evaporates by the hour, while [[vega]] is nearly irrelevant (no time for [[dvol|DVOL]] to matter). It offers extreme leverage and defined-risk lottery payoffs, and it is genuinely dangerous: a small move produces outsized P&L swings, and crypto's 24/7 tape gives no session break to hide behind.

## Construction

The tradeable 0DTE structures on Deribit BTC/ETH are the short-dated versions of the standard menu:

- **Short-premium (the structural bet):** a 0DTE [[iron-condor]] (sell an OTM call spread + an OTM put spread) or [[iron-fly]] (ATM short straddle with bought wings). Defined risk via the long wings — essential at 0DTE gamma. Sell short strikes ~0.5–1.5% OTM, wings a few hundred dollars (BTC) wide.
- **Long-premium (the convexity bet):** a 0DTE ATM [[straddle-strangle|straddle]] bought immediately before a scheduled catalyst (US CPI/[[fomc]], a major unlock or listing, a large on-chain event) for a fast, direction-agnostic gamma play.
- **Directional:** a single 0DTE call or put, sized as a defined-risk lottery ticket, often placed in the direction of anticipated dealer hedging flow (see [[gamma-exposure|GEX]]).

Each BTC option represents 1 BTC, each ETH option 1 ETH; both are **cash-settled to the Deribit index** at the 08:00 UTC expiry — **no assignment, no physical delivery**. Premium is quoted in the coin (inverse) or USDC (linear); use linear for clean USD P&L.

## Payoff & breakevens

Same-day expiry does not change the payoff *shape* — a 0DTE short condor is the familiar flat-topped tent capped by its wings; a 0DTE long straddle is the "V". What changes is the *path*: every Greek is compressed into the hours before 08:00 UTC, so the diagram is realized violently.

```
 P/L (0DTE short condor at 08:00 UTC settle)
  │        ┌──────────────────┐   ← max profit = net credit (full theta in hours)
  │       /                    \
 0│──────/──────────────────────\──── spot →
  │     /                        \
  │____/                          \___ ← max loss = wing width − credit (realized in MINUTES)
       LP SP                  SC LC
   profit zone ≈ ±1× the day's expected move
```

- Short condor: max profit = net credit; max loss = wing width − credit; breakevens = short strike ± credit.
- Long straddle: max loss = debit (both legs expire worthless if spot pins the strike); breakevens = strike ± debit; upside unbounded.

## Greeks profile

0DTE trades the [[gamma]]/[[theta]] axis almost exclusively — [[vega]] is negligible because there is no time for DVOL to play out. It is a *realized-vol* game, not an *implied-vol* game.

| Greek | 0DTE behavior | Practical consequence |
|---|---|---|
| [[theta]] | Decays fast, near-total by the 08:00 UTC settle | A seller's edge is collected in hours; a buyer bleeds by the minute |
| [[gamma]] | At its absolute maximum, exploding near ATM in the final hours | A ~0.5–1% BTC move can take a strike from near-worthless to multiples; deltas flip violently |
| [[delta]] | Increasingly binary as expiry nears (→ 0 or 1) | The position behaves like a digital/binary bet in the final hours |
| [[vega]] | Tiny (little time for DVOL to matter) | Budget 0DTE against a **gamma** cap, not a vega budget |
| charm | Extreme — delta drifts fast purely from time passing | Hedges must be re-struck constantly; "set and forget" is impossible |

A 0DTE short condor is the most concave bet on the surface (maximum negative gamma per dollar of premium); a 0DTE long straddle is the most convex. This is [[gamma]]/convexity at its sharpest — the linear delta term is almost irrelevant by the final hour.

## Market view / when to use

- **0DTE short condor:** when short-dated realized vol is likely to come in *below* the day's implied move — a quiet, catalyst-free session with rich short-dated premium. Open after the immediate post-08:00-UTC-settle repositioning has settled; avoid days with a scheduled macro print inside the window.
- **0DTE long straddle:** immediately before a *known* catalyst with uncertain direction (CPI/FOMC, a major listing or unlock). The bet is that the realized intraday move beats the (already-elevated) implied move — a high bar, so size it as a lottery ticket.
- **GEX-informed directional:** use dealer [[gamma-exposure|gamma exposure]] to identify levels — when dealers are **short gamma** their hedging *amplifies* the move (momentum), when **long gamma** it *dampens* it (mean-reversion/pinning). Trade with the anticipated hedging flow toward the next gamma level.

## Adjustments & management

- **Short condor:** take profit at **50% of max credit**; hard stop at **~2× credit**; close immediately if spot breaches a short strike. Because crypto has no market close, the "singularity zone" is the final hours before the 08:00 UTC settle — flatten before it if the position is tested.
- **Long straddle:** take profit at 50–100% gain (gamma cuts both ways); close if spot has not moved within 1–2 hours (theta is destroying value); never nurse a losing 0DTE long hoping for a move.
- **Directional:** target the next gamma level; tight stop at ~50% of premium paid; close within 1–2 hours regardless.
- **Delta-hedge on the perp:** flatten residual delta with the Deribit **perpetual**; the hedge leg pays/collects [[funding-rate|funding]] and lets a long-gamma 0DTE straddle be [[gamma-scalping|gamma-scalped]] intraday.
- **Sizing:** max ~1–2% of book at risk per 0DTE position; budget against a *gamma* cap, not a vega cap.

## Crypto specifics

- **Venue & instrument.** [[deribit]] daily-expiry BTC/ETH options, settling **08:00 UTC** to the Deribit index. [[greeks-live]] is the workbench for the short-dated surface and per-leg Greeks. Liquidity thins fast off BTC/ETH and off the nearest expiry.
- **Inverse vs linear settlement.** Inverse (coin-margined) options denominate premium/P&L in the coin (collateral moves with spot); USDC-margined (linear) options give clean USD P&L — preferred for a pure gamma/theta 0DTE bet.
- **[[dvol|DVOL]] context.** DVOL is a *30-day* index, so it is background context, not the 0DTE signal — the 0DTE game is short-dated *realized* vol vs the day's implied move. **DVOL and the IV surface come from Deribit / [[greeks-live]], not [[cryptodataapi|CryptoDataAPI]]**.
- **24/7 and weekend gamma.** There is **no market close** to cap a move — the equity 0DTE "close by 15:30" rule has no crypto analogue; the reference point is the 08:00 UTC settle. Weekend daily expiries exist and trade against thin liquidity, so a 0DTE short-gamma position can be run over by a weekend air-pocket.
- **No [[section-1256-contracts|§1256]].** Offshore Deribit options get **no §1256 60/40 treatment** — US ordinary short-term rates; AU CGT/income by trader status. High-frequency 0DTE turnover makes the record-keeping heavy.
- **Perp-funding & flow.** [[funding-rate|Funding]] and liquidation cascades drive the intraday path more than option flow does — crypto 0DTE is dominated by the perp/spot tape, unlike SPX 0DTE where option hedging *is* a large share of flow.
- **Alt-option liquidity.** Daily-expiry options barely exist off BTC/ETH; 0DTE on alts is not a viable structure.

## Risks

- **Intraday gap / liquidation cascade:** a news event or forced-liquidation spiral can move BTC 2–5% in minutes, blowing through condor wings before any exit.
- **Extreme gamma into the settle:** a position that is safe hours before 08:00 UTC can be in crisis near it; short gamma turns a small move into a max loss fast.
- **Bid-ask erosion:** short-dated crypto option spreads are wide and widen further in stress; taker fees (0.03% of underlying, capped at 12.5% of premium) hit cheap 0DTE options hard.
- **Weekend & 24/7 exposure:** no session break to halt a move.
- **Behavioral ruin:** the high win rate of 0DTE selling breeds over-sizing and skipped stops — one session then destroys the account.
- **Thin/nascent market:** off BTC/ETH and off the front expiry, liquidity is too thin to trade or exit reliably.

## Worked crypto example

*Illustrative round numbers — not a recommendation or backtest.*

**0DTE iron condor on BTC.** BTC spot **$60,000** at 22:00 UTC, expiry at 08:00 UTC (~10 hours). Day's implied move ≈ $900. No scheduled macro.
- Sell 60,750 call / buy 61,250 call (call spread credit ≈ $110).
- Sell 59,250 put / buy 58,750 put (put spread credit ≈ $100).
- Total credit ≈ **$210** per condor; wings $500 wide → max loss ≈ $500 − $210 = **$290**.
- *Win:* BTC chops $59.6k–$60.4k into the settle; both spreads expire worthless → keep **$210** (full credit) — a 72% return on the $290 at risk in ~10 hours.
- *Loss:* a liquidation cascade at 03:00 UTC gaps BTC to $61,400; the call spread goes max — loss ≈ **−$290** realized in minutes, with no session break to react. The defined wings are the only reason the loss is bounded.

## Capacity limits

0DTE capacity is tight — same-day Deribit liquidity is the binding constraint.

- **BTC front-expiry ATM/near-ATM options**: most liquid; $200–500K notional condor/fly works without material slippage. Above $500K, spreads widen and edge narrows.
- **BTC deep-OTM wings**: thinner market; $50–150K notional per leg before noticeable slippage.
- **ETH 0DTE**: roughly 2–3× less liquid than BTC; practical per-position max ~$100–200K notional.
- **Total book**: a systematic 0DTE program should cap at $500K–$2M total notional; larger accounts should extend expiry to weekly/monthly and leave 0DTE as a small high-frequency sleeve only.
- **Crowding risk**: low — the crypto 0DTE market is not retail-crowded. Risk is capacity exhaustion, not crowding compression.

## What kills this strategy

1. **Intraday liquidation cascade** — BTC/ETH gaps 2–5% in minutes from a headline; the short condor hits max loss before exit is possible. No session break can stop it (crypto is 24/7). The most dangerous time is late Asian / early European session weekends with thin orderbooks.
2. **08:00 UTC gamma singularity** — positions that are "safe" at 04:00 UTC can be in crisis by 07:30 UTC; extreme gamma in the final hour creates sudden delta whips; bid-ask on tested positions widens dramatically, making clean exits expensive.
3. **Over-sizing on high hit rate** — the silent killer; the structural high win rate makes sellers habitually over-size, and one shock day destroys multi-month gains in minutes.
4. **Bid-ask and fee erosion** — wide short-dated spreads (3–8 vol points) plus taker fee (0.03% of underlying, capped at 12.5% of premium) can consume the entire alpha on small credits; the edge only survives at a minimum credit-to-cost ratio.
5. **Vol-shock regime entry** — selling 0DTE during a live vol-spike regime (DVOL spike > 30% intraday, active cascade) is a donation; the realized range will exceed any condor wing.
6. **Alt/off-expiry illiquidity** — daily-expiry options barely exist off BTC/ETH; attempting to run 0DTE on altcoins or off-tenor expiries is not viable.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Rolling 30-day win rate on short condors below 55% → regime break; suspend selling until win rate returns above 60% for 10 consecutive days.
- Any single-position loss exceeds 2× the credit received → exit immediately, no averaging.
- CryptoDataAPI vol-regime-score > 70 on entry day → no new 0DTE shorts; flatten existing short-gamma before the 08:00 UTC settle.
- DVOL intraday spike > 30% from session open → flatten all short-gamma immediately; this is a cascade signal.
- Net P&L from 0DTE is negative for 3 consecutive calendar months with proper regime filters applied → pause and re-examine whether the front-end implied-realized premium has structurally compressed.

## Getting the Data (CryptoDataAPI)

**DVOL and the raw IV surface come from Deribit / [[greeks-live]]** (Deribit products; CDA does not serve them). [[cryptodataapi|CryptoDataAPI]] supplies the intraday context — dealer gamma, funding, liquidations, options OI, and short-term momentum — that drives the 0DTE path.

**Live data:**
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory + liquidation profile); short-gamma dealers amplify the tape, long-gamma dampen it — the core GEX-directional input
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (pin context into the settle)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, an intraday flow driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (the cascade that gaps 0DTE positions)
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics for intraday direction
- `GET /api/v1/volatility/regime` — per-asset vol regime (a vol-shock reading vetoes 0DTE selling)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=5m&limit=1000` — intraday OHLCV for short-dated realized-vol vs the implied move
- `GET /api/v1/backtesting/klines` — deep archive for intraday backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — at session open, `GET /api/v1/quant/gex` + `GET /api/v1/market-intelligence/options` classify the day (pin vs cascade) and locate the max-pain magnet; `GET /api/v1/market-data/short-term-price` supplies the intraday directional read
- **Regime gate** — `GET /api/v1/volatility/regime`: a `vol_shock` reading vetoes short-gamma 0DTE outright; `GET /api/v1/quant/market` (15-min refresh) separates squeeze days from range days before structure selection
- **Backtest** — intraday replay needs `GET /api/v1/backtesting/klines` 1m bars, available only since 2026-03-30 (the 1h/4h/1d archive back to 2017-08 is too coarse for same-day expiry); tag cascade days with `/api/v1/backtesting/liquidations` (Hyperliquid, since 2026-03-30)
- **Tips** — poll `/api/v1/market-intelligence/liquidations` throughout the session: a cascade against a short-gamma book is the flatten-now trigger, consistent with the DVOL-spike kill rule above. Append `?format=markdown` to keep high-frequency polling light on context.

## Related

- [[zero-dte-options]] — the instrument and market-structure overview (read alongside this playbook)
- [[iron-condor]], [[iron-fly]] — the defined-risk structures used at 0DTE tenors
- [[short-strangle]] — the longer-dated short-premium equivalent
- [[straddle-strangle]] — 0DTE volatility buying (the long side)
- [[gamma]], [[theta]] — the dominant Greeks at same-day expiry
- [[gamma-scalping]] — dynamic hedging of a long-gamma 0DTE position
- [[gamma-exposure]] — dealer hedging flows and the GEX-directional read
- [[dvol]] — 30-day background vol context
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[funding-rate]] — the perp linkage that drives the intraday path

## Sources

- Natenberg, *Option Volatility and Pricing* (2nd ed.) — gamma acceleration near expiration.
- [[gamma-exposure]] — dealer-gamma framework for the directional variant.
- [[deribit]] / [[greeks-live]] documentation — daily-expiry listing, 08:00 UTC index settlement, cash settlement, inverse vs USDC-margined contracts, fee schedule.
