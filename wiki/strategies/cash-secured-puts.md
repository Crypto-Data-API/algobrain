---
title: "Cash-Secured Puts"
type: strategy
created: 2026-04-15
updated: 2026-10-17
status: good
tags: [options, crypto, derivatives, premium-selling, volatility]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
aliases: ["Cash-Secured Puts", "Cash Secured Puts", "CSP", "Crypto Cash-Secured Put", "USDC-Secured Put", "BTC Cash-Secured Put"]
related: ["[[cash-secured-put]]", "[[covered-call]]", "[[wheel-strategy]]", "[[crypto-options-volatility-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[put-option]]", "[[theta]]", "[[vega]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[iv-crush]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
gates:
  - id: deribit_btc_eth
    role: universe
    rule: "Sell puts on Deribit BTC and ETH options, ideally the USDC-margined (linear) contracts"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "The options-side data served (DVOL, the expiry list with ATM IV) covers BTC and ETH. SOL and other alt options are named by the page as thin; nothing is served for them."
  - id: want_to_own_coin
    role: filter
    rule: "Only sell puts on a coin you genuinely want to accumulate at the strike"
    runnable: false
    note: "The page's load-bearing rule is the trader's own conviction about holding the coin; no market data answers it."
  - id: dvol_rich
    role: entry
    rule: "Enter when DVOL (put-side IV) is rich: in the upper part of its trailing-year range"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "items[].dvol is Deribit's live 30-day DVOL; history holds about 180 daily values, half the page's trailing year. The page gives no cutoff for the upper part (a percentile above 70 is one reading), so the level is the desk's call. DVOL is the whole surface, not put-side IV."
  - id: iv_over_rv
    role: entry
    rule: "Confirm premium richness: DVOL above realized vol computed from the last 90 daily closes"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].vrp
    note: "vrp = dvol - realized_30, a 30-day realized window. For the page's 90-bar version, compute annualized close-to-close vol from /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90 and compare with items[].dvol. The page sets no minimum gap, so how rich is rich enough is the desk's call."
  - id: put_skew_bid
    role: entry
    rule: "Prefer entries when 25-delta put skew is elevated (puts bid), often just after a selloff"
    runnable: false
    note: "No skew or per-strike IV is served; 25-delta put skew needs the Deribit option surface (Deribit or a surface vendor)."
  - id: vol_regime_gate
    role: filter
    rule: "Sell puts while the coin's vol regime is expanding or normal; stand aside on vol_shock"
    runnable: true
    endpoint: /api/v1/volatility/regime/{symbol}
    field: regime
    note: "From the page's AI-agent workflow. compressed and mean_reverting are not named by the page."
  - id: trend_regime_halt
    role: filter
    rule: "Trade in a range-bound-to-rising regime; halt new put sales while strong_trend_bear or vol_spike is the market regime or its probability is elevated"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "Halt on regime.label strong_trend_bear or vol_spike. The page gives no cutoff for an elevated probability; probabilities.regime_transitions.to_vol_spike is the served transition odds, and how high counts is the desk's call."
  - id: dte_21_45
    role: entry
    rule: "Sell the expiry 21-45 days out"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "Pick the row with expiry_days between 21 and 45; expiry is Deribit's code (27NOV26). The list holds the nearest 12 expiries, so there is usually one or two in range. term_structure is Pro Plus and is empty on lower tiers."
  - id: strike_delta_20_35
    role: entry
    rule: "Short strike out of the money at about 20-35 delta"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].atm_iv
    note: "No per-strike Greeks or IV are served. Approximate with Black-Scholes using spot, the chosen expiry's atm_iv and expiry_days; that ignores put skew, so it understates an OTM put's delta and places the strike a little too far out. Exact delta needs the Deribit chain."
  - id: strike_below_support
    role: entry
    rule: "Place the short strike below visible support, at a price you would happily own the coin"
    runnable: partial
    endpoint: /api/v1/indicators/technical/{symbol}
    field: sr.support[].price
    note: "Served support levels are computed on daily bars, each with a strength count and its distance from price. Which level counts as visible support is the desk's call."
  - id: collateral_secured
    role: sizing
    rule: "Reserve collateral equal to the strike notional, K x 1 USDC per contract (one BTC or one ETH per option), on USDC-margined linear contracts rather than coin-margined inverse ones"
    runnable: true
    input: position
  - id: profit_target_50
    role: exit
    rule: "Buy the put back at about 50% of the maximum credit"
    runnable: false
    note: "No option prices are served, so the put's current mark against the credit needs the Deribit order book or mark."
  - id: roll_trigger_near_strike
    role: exit
    rule: "Roll down-and-out when spot drops toward the short strike and the thesis still holds"
    runnable: partial
    input: position
    endpoint: /api/v1/market-data/ticker/price?symbol={symbol}USDT
    field: price
    note: "Spot against the position's strike. The page does not say how close counts as toward the strike, and whether the thesis holds is the trader's judgement."
  - id: roll_for_credit
    role: exit
    rule: "Only roll for a net credit (buy back, sell a lower and later put); if the thesis is broken, take the loss instead"
    runnable: false
    note: "Needs option prices for both legs, which are not served."
  - id: liq_cluster_below_strike
    role: exit
    rule: "A liquidation cluster below the short strike, as spot approaches it, is the early warning to roll before gamma dominates"
    runnable: partial
    endpoint: /api/v1/quant/positioning/ladder?symbol={coin}
    field: bins[].long_usd
    note: "long_usd is long-liquidation notional per 0.5% price bin (downside fuel) from Hyperliquid accounts of $100k and up, not Deribit or the whole market. levels[] lists the nearest clusters around mark. The page gives no size for a cluster, so the cut is the desk's call."
  - id: settle_buy_spot
    role: exit
    rule: "If the put settles below the strike and you wanted the coin, buy spot at settlement for an effective basis of K - C, then sell covered calls"
    runnable: partial
    input: position
    endpoint: /api/v1/market-data/klines?symbol={symbol}USDT&interval=1m&limit=60
    field: klines[].close
    note: "Deribit settles to its own index at 08:00 UTC (a 30-minute average of the index), which is not served. The nearest proxy is the mean of Binance spot 1-minute closes from 07:30 to 08:00 UTC on expiry day."
  - id: bull_put_tail_cap
    role: stop
    rule: "Cap the tail by buying a further-OTM put below the short strike, turning the trade into a bull put spread"
    runnable: false
    note: "Needs option prices and strikes for the protective put, which are not served."
  - id: time_stop_final_week
    role: exit
    rule: "Manage or roll the put before its final week to expiry, when gamma dominates"
    runnable: true
    input: position
    note: "The page says roughly the final week; 7 calendar days to expiry is the reading used here."
  - id: funding_not_crowded_long
    role: filter
    rule: "The best put-selling windows come when perp funding is negative or neutral; richly positive funding firms call skew and cheapens puts"
    runnable: partial
    endpoint: /api/v1/derivatives/binance/funding-rates?symbol={symbol}USDT
    field: current_rate
    note: "Binance 8-hour funding, whose neutral baseline is 0.0001 (0.01% per 8h). The page sets no cutoff for richly positive, so the line is the desk's call. Hyperliquid's hourly rate is on /api/v1/hyperliquid/funding-rates."
  - id: avoid_short_gamma_zone
    role: entry
    rule: "Do not park the short strike inside a short-gamma dealer zone that would amplify the selloff that tests it"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.gamma_profile[].long_usd
    note: "/quant/gex is a perp analog built from Hyperliquid market-maker liquidation density by price, not Deribit options dealer gamma. A bin with heavy long_usd around the strike is the analog of an amplifying zone; how heavy is the desk's call. regime.state amplify is the coin-level read."
---

# Cash-Secured Puts

A cash-secured put is an [[options]] income structure: sell a [[put-option]] on [[bitcoin]] or [[ethereum]] while reserving enough collateral to buy the coin at the strike if the option settles in-the-money. In crypto it is traded on [[deribit]] BTC/ETH options, most cleanly with **USDC-margined (linear)** contracts secured by USDC collateral. It is often described as "getting paid to place a limit buy order" — you collect premium today in exchange for the obligation (economic, since Deribit is cash-settled) to acquire the coin at the strike if it falls there. Maximum profit is the premium; the loss profile below the strike is the same as owning the coin (cushioned by the premium).

The cash-secured put harvests the put-side [[variance-risk-premium]] — implied vol prices above subsequently realized vol, and crypto's fat left tail keeps that premium fatter than equities'. It is the single-leg, conservative end of the [[crypto-options-volatility-selling|crypto vol-selling]] spectrum: fully collateralised, it removes the leverage that turns a naked short put into an account-destroyer in a crash. It is also the entry leg of the crypto [[wheel-strategy|wheel]] (sell puts to accumulate the coin, then sell [[covered-call|covered calls]] on it).

## Construction

Sell one OTM put at the strike you would happily accumulate the coin at, same-expiry, and reserve the cash to cover it:

- Sell 1 OTM put (strike `K < S`, typically ~20–35 delta) on Deribit BTC/ETH.
- Reserve collateral equal to the strike notional — for USDC-margined contracts, `K × 1` USDC per contract (each BTC option = 1 BTC, each ETH option = 1 ETH). This is what makes it *cash-secured* rather than a leveraged naked put.
- Credit = the put premium.

On Deribit the option is **cash-settled to the Deribit index** at expiry — there is **no automatic coin assignment**. If the put settles ITM you are debited the intrinsic value in cash; to actually *acquire the coin at a discount* (the wheel's intent) you separately buy spot or perp at settlement. This is the key crypto difference from equity CSPs and is covered in *Crypto specifics*.

## Payoff & breakevens

Capped gain (the premium), coin-like downside below the strike. Payoff at expiry, credit `C`, strike `K`:

- Max profit = `C` (put expires OTM; keep the premium)
- Breakeven = `K − C`
- Max loss = `(K − C)` if the coin goes to zero (economically identical to owning the coin from the breakeven)

```
   P&L
    |        ___________________________   <- max gain = premium (C)
    |       /
    |      /
  0 +-----B---------K------- spot at expiry
    |    /   B = K - C (breakeven)
    |   /
    |  /   (settles ITM: cash loss ≈ owning the coin below K)
    | /
    |/   <- max loss = (K - C) as coin -> 0
```

## Greeks profile

A cash-secured put is a single short put:

| Greek | Sign | Behaviour |
|---|---|---|
| [[delta]] | **Positive** (≈ +0.20 to +0.35 at entry) | Bullish-to-neutral; rises toward +1.0 (full long-coin equivalent) as the put goes deeper ITM |
| Gamma | **Negative** | The "gamma trap" — spikes into the final weeks; the reason to roll/close early |
| [[vega]] | **Negative** | A [[dvol|DVOL]]/IV spike marks the short put against you — losses cluster exactly when IV explodes in a selloff |
| [[theta]] | **Positive** | The primary profit driver — the put decays each calm day, accruing to the seller |

The seller is **long delta, short gamma, short vega, long theta**: a directional-bullish, short-vol position. The reserved USDC removes the leverage; what remains is a paid-for commitment to buy the coin lower. See [[iv-crush]] for the DVOL contraction that helps the seller.

## Market view / when to use

- **On a coin you genuinely want to accumulate** at the strike. This is the load-bearing rule — selling puts on a coin you would not hold turns income into unwanted, forced exposure.
- **When [[dvol|DVOL]] / put-side IV is rich** (upper part of the trailing-year range) so the premium is fat relative to the expected move — often *after* a selloff, when put skew is bid and you are paid richly to underwrite the fear.
- **At a strike below visible support**, ~20–35 delta, 21–45 DTE for the steepest [[theta]] with room to manage.
- **In a range-bound-to-rising regime.** The worst regime is a fast, deep selloff that pushes the whole book ITM at once while DVOL spikes — the signature clustered loss.

## Adjustments & management

- **Profit target:** buy back at ~**50% of max credit**, freeing collateral and shedding late-cycle gamma.
- **Roll down-and-out for a credit:** if spot drops toward the strike and the thesis holds, buy back and sell a lower, later put for net credit — lowering the effective entry. Only roll for a *credit*; if the thesis is broken, take the loss.
- **Take the "assignment":** when spot settles below the strike and you wanted the coin there, let it settle and **buy spot at settlement** at an effective basis of `K − C`, then pivot to selling [[covered-call|covered calls]] — the crypto [[wheel-strategy|wheel]].
- **Cap the tail:** convert to a **bull put spread** by buying a further-OTM put below the short strike, bounding the loss if the coin keeps falling.
- **Time stop:** manage or roll before the final ~week, when gamma dominates.

## Crypto specifics

- **Cash settlement — no auto-assignment.** [[deribit]] BTC/ETH options are **cash-settled to the Deribit index**; an ITM short put is settled in cash, not by delivering the coin. To run the wheel you must **manually buy spot/perp at settlement** to acquire the coin at the strike. This is the single biggest departure from equity CSPs, where assignment hands you the shares automatically.
- **USDC-secured (linear) vs coin-margined (inverse).** Secure the put with **USDC** on the linear line for clean, coin-independent collateral and USD P&L — the true "cash-secured" analogue. Coin-margined (inverse) puts denominate premium/P&L in the coin and let collateral move with spot, which reintroduces exactly the leverage a CSP is meant to remove.
- **[[dvol|DVOL]] & put skew.** DVOL is Deribit's 30-day forward IV index — the crypto VIX; put-side richness is best entered when DVOL and 25-delta put skew are elevated. **DVOL, put skew and the raw IV surface come from Deribit / [[greeks-live]], not [[cryptodataapi|CryptoDataAPI]]** (CDA gives the complementary OI/regime/funding context — see below).
- **24/7 and weekend gap.** No session break: a thin **weekend** air-pocket can push a put deep ITM with nothing to halt the move — crypto CSPs carry more overnight/weekend gap risk than equity CSPs, which only gap at the open.
- **No [[section-1256-contracts|§1256]].** Offshore Deribit options get **no §1256 60/40 treatment** — US ordinary short-term rates; AU CGT/income by trader status. Coin-margined record-keeping is onerous.
- **Perp-funding interaction.** [[funding-rate|Funding]] shapes the skew — richly positive funding (crowded longs) firms call skew and *cheapens* puts, so the best-paid put-selling windows often come when funding is negative/neutral and puts are bid.
- **Alt & DeFi analogues.** SOL and other alt options exist (Deribit; thinner OKX/Bybit) but are wide and shallow. The on-chain systematic analogue is the **put-selling vault** (Ribbon/Aevo, Thetanuts and similar) — USDC-collateralised BTC/ETH put-writing run mechanically; the same VRP harvest, packaged.

## Risks

- **Crash / gap below the strike** on a coin that keeps falling — the put seller owns the full move below breakeven; a fast selloff pushes the whole book ITM at once while DVOL spikes.
- **Selling puts on coins you do not actually want** — turns settlement from a plan into a forced bad position.
- **Broken-thesis rolling** — serially rolling a put on a deteriorating asset converts a small loss into a large concentrated one.
- **Cash drag** — collateral tied up at low premium yield (low DVOL) is poor return on capital; offset partly by USDC yield.
- **Coin-margin leverage creep** — securing with coin instead of USDC reintroduces non-linear collateral risk.
- **Single-venue** Deribit dependency; margin expansion into a spike.

## Worked crypto example

*Illustrative round numbers — not a recommendation or backtest.*

**Setup.** BTC spot **$60,000**. You want to accumulate at **$54,000** (10% lower). [[dvol|DVOL]] **50**, put skew firm. Sell the 30-DTE $54,000 put (≈ 20 delta), USDC-margined.

| Item | Value |
|---|---|
| Strike | $54,000 |
| Premium received | **$1,650** |
| USDC secured | $54,000 |
| Effective basis if it settles ITM | $52,350 |
| Breakeven | $52,350 |
| Max gain | $1,650 (put expires OTM) |
| Max loss | $52,350 (BTC → $0) |

- **BTC above $54,000 at expiry:** put expires worthless → keep **$1,650** (≈ 3.1% on the $54k collateral in ~30 days, before USDC yield); sell the next put.
- **BTC at $52,350:** put settles ITM by $1,650, offset exactly by the premium — roughly breakeven; buy spot at settlement to begin the wheel at a $52,350 basis.
- **BTC gaps to $48,000 on a weekend:** put settles ITM by $6,000; net loss ≈ **−$4,350** (cushioned $1,650 by the premium). You either buy spot at an effective $52,350 basis and start selling covered calls (wheel), roll down-and-out to a lower put near even, or had you bought a $50,000 put you would have capped the loss as a bull put spread.

## Getting the Data (CryptoDataAPI)

**DVOL, put skew, and the raw IV surface come from Deribit / [[greeks-live]]** (Deribit products; CDA does not serve them). [[cryptodataapi|CryptoDataAPI]] supplies the complementary options-flow, regime, and funding context for timing put-selling entries.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (sell rich put premium into "expanding/normal", stand aside on "vol_shock")
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (positioning/pin context)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding; negative/neutral funding often coincides with bid put skew (richer put premium)
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory; short-gamma dealers amplify a selloff that tests your put)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (downside-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (compare RV to DVOL to judge put-premium richness)
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history for RV/put-write backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Entry gate** — `GET /api/v1/volatility/regime`: sell puts in `expanding`/`normal`, stand aside on `vol_shock`; confirm premium richness by comparing Deribit DVOL to realized vol computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90`.
- **Strike context** — `GET /api/v1/market-intelligence/options` (max pain / OI) + `GET /api/v1/quant/gex`: avoid parking the short strike inside a short-gamma dealer zone that would amplify the very selloff that tests it.
- **Regime gate** — `GET /api/v1/quant/market`: elevated `strong_trend_bear`/`vol_spike` probabilities describe the clustered-loss regime where the whole put book goes ITM at once — halt new sales.
- **Roll trigger** — watch `GET /api/v1/market-intelligence/liquidations` intraday when spot approaches the short strike; a liquidation cluster below it is the early warning to roll down-and-out (for a credit) before gamma dominates.
- **Backtest** — replay put-write proxies against `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09), pairing entries with point-in-time regime states from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid lookahead. CDA has no options-chain archive — premium series come from Deribit.
- **Tips** — append `?format=markdown` for cleaner context; poll the cached `GET /api/v1/daily` bundle hourly instead of per-endpoint loops between management checks.

## Related

- [[cash-secured-put]] — redirects here (merged singular page)
- [[covered-call]] — the mirror strategy (sell calls against long coin); the wheel's second leg
- [[wheel-strategy]] — the full crypto put-call income cycle (CSP → acquire coin → covered call → repeat)
- [[crypto-options-volatility-selling]] — the systematic short-vol book this single-leg structure sits inside
- [[short-strangle]], [[iron-condor]] — multi-leg premium-selling relatives
- [[put-option]] — put mechanics
- [[dvol]], [[implied-volatility]], [[realized-volatility]] — the vol inputs and put-skew driver
- [[iv-crush]] — the DVOL contraction the seller wants
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL, skew, and surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[funding-rate]] — the perp linkage that shapes crypto skew

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — cash-secured put mechanics, rolling, and defense (equity framework; ported to crypto here).
- [[deribit]] / [[greeks-live]] documentation — cash settlement to the Deribit index (no coin assignment), USDC-margined vs inverse collateral, put skew and the DVOL index.
- Bakshi & Kapadia (2003) and the variance-risk-premium literature — the put-side premium the structure harvests (see [[variance-risk-premium]]); crypto IV−RV spreads run wider than equities'.
