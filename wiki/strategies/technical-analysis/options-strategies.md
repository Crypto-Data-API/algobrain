---
title: "Options Strategies (Crypto)"
type: strategy
created: 2026-04-13
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, swing-trading, bitcoin, ethereum]
aliases: ["Option Strategies", "Options Structures", "Option Spreads", "Crypto Options Strategies", "options-strategies-overview"]
strategy_type: hybrid
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[covered-call]]", "[[vertical-spread]]", "[[iron-condor]]", "[[straddle-strangle]]", "[[options-selling]]", "[[options-premium-selling]]", "[[crypto-options-volatility-selling]]", "[[call-option]]", "[[put-option]]", "[[options]]", "[[cash-secured-put]]", "[[credit-spread]]", "[[volatility-risk-premium]]", "[[variance-risk-premium]]", "[[greeks]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[edge-taxonomy]]"]
---

# Options Strategies (Crypto)

Options strategies combine one or more [[call-option|call]] and [[put-option|put]] options to create defined risk/reward profiles. By structuring positions across different strikes, expirations, and option types, traders can express views on direction, volatility, time decay, or any combination of these factors. In crypto they are traded on [[deribit]] (which holds the overwhelming majority of BTC/ETH options open interest), plus on-chain option vaults and BTC-ETF options. This page treats the family as a whole, with defined-risk premium selling — the one family with a documented persistent edge, the [[volatility-risk-premium]] — as the canonical implementation.

## Strategy Families

### Directional Strategies

Directional strategies profit from a move in the underlying's price. The simplest are outright [[call-option|call]] purchases (bullish) and [[put-option|put]] purchases (bearish), but these carry full premium risk and suffer from [[theta-decay|time decay]]. [[vertical-spread|Vertical spreads]] — bull call spreads and bear put spreads — reduce cost and cap risk by simultaneously buying and selling options at different strikes. Directional spreads are popular because they define maximum loss at entry, making [[position-sizing|position sizing]] straightforward. In crypto they compete directly with leveraged [[perpetual-futures|perp]] positions; the option version caps downside where a perp can be liquidated.

### Income Strategies

Income strategies collect premium by selling options, profiting when the underlying stays within a defined range. [[covered-call|Covered calls]] sell calls against long spot BTC/ETH, generating income in exchange for capping upside (the most common crypto income overlay, and the basis of on-chain covered-call vaults). [[cash-secured-put|Cash-secured puts]] sell puts with USDC reserved to buy the coin if assigned — getting paid to place a limit buy. [[iron-condor|Iron condors]] combine a bull put spread and a bear call spread, profiting when the underlying stays between the short strikes with capped risk both sides — the strongly-preferred two-sided structure in crypto given the gap profile. These strategies benefit from [[theta-decay|time decay]] and declining [[dvol|DVOL]].

### Volatility Strategies

Volatility strategies profit from large moves in either direction or from changes in implied volatility itself. [[straddle-strangle|Straddles]] (buying a call and put at the same strike) and [[straddle-strangle|strangles]] (buying a call and put at different strikes) profit when the underlying moves more than the combined premium paid. [[gamma-scalping]] involves buying options and dynamically [[delta-hedging|delta-hedging]] with the [[perpetual-futures|perp]], profiting when realised volatility exceeds implied. These are typically used around macro events, major protocol catalysts, or when [[dvol|DVOL]] is deemed cheap relative to expected [[realized-volatility|realised volatility]].

### Hedging Strategies

Hedging strategies use options to protect existing crypto positions. Protective puts provide downside insurance on long spot BTC/ETH — the cost of the put is the "insurance premium." [[collar|Collars]] combine a protective put with a covered call, financing the put by sacrificing some upside. Book-level hedging may use BTC/ETH index puts or long-DVOL convexity to protect against a broad crypto drawdown. The key tradeoff in all hedging strategies is protection cost versus coverage level.

## Risk Profiles

Every options strategy has a defined risk profile at expiration, characterised by maximum profit, maximum loss, and breakeven point(s). Single-leg strategies (buying calls or puts) have large profit potential but can lose 100% of premium. Multi-leg strategies (spreads, condors, butterflies) have both capped profit and capped loss. Understanding the [[greeks]] — [[delta]], [[gamma]], [[theta]], [[vega]], and [[rho]] — is essential for managing positions before expiration, as these sensitivities change continuously with price, time, and volatility. Deribit options are European-style and cash-settled, so there is no early assignment and no delivery — a genuine simplification versus American single-name equity options.

### Structure Reference Table

The canonical structures, with terminal risk profile, directional bias, and dominant Greek exposure. "Net debit" structures pay premium (long convexity); "net credit" structures collect premium (short convexity — see [[non-linear-payoff]]).

| Structure | Bias | Premium | Max profit | Max loss | Net theta | Net vega | Net gamma |
|---|---|---|---|---|---|---|---|
| Long call | bullish | debit | large | premium paid | negative | positive | positive |
| Long put | bearish | debit | strike − premium | premium paid | negative | positive | positive |
| [[vertical-spread\|Bull call spread]] | bullish | debit | width − debit | debit | mixed | small + | small + |
| [[credit-spread\|Bull put spread]] | bullish | credit | credit | width − credit | positive | negative | negative |
| [[covered-call\|Covered call]] | neutral-bull | credit | strike − cost + premium | substantial (coin) | positive | negative | negative |
| [[cash-secured-put\|Cash-secured put]] | neutral-bull | credit | premium | strike − premium | positive | negative | negative |
| [[iron-condor\|Iron condor]] | neutral | credit | credit | width − credit | positive | negative | negative |
| [[straddle-strangle\|Long straddle]] | volatility ↑ | debit | large | premium paid | negative (large) | positive (large) | positive (large) |
| [[short-strangle\|Short strangle]] | volatility ↓ | credit | credit | unlimited (undefined) | positive | negative (large) | negative (large) |
| [[collar\|Collar]] | hedge | ~zero | capped (call strike) | capped (put strike) | small | small | small |

Reading the table: **credit/short-premium structures are net-positive theta and net-negative vega/gamma** — they are short [[convexity]] and harvest the [[volatility-risk-premium]]; **debit/long-premium structures are the mirror** — they pay theta to own convexity. The choice of [[expiration-selection|DTE]] then sets *how much* of each Greek the structure carries: shorter DTE amplifies gamma (especially dangerous with crypto's 24/7 unbounded gaps); longer DTE amplifies vega (see [[expiration-selection]]).

## Edge source

Per [[edge-taxonomy]], the documented edge in options strategies is primarily **risk-bearing**, with a secondary **behavioral** component:

- **Risk-bearing**: net sellers of options act as insurers. They collect the [[volatility-risk-premium]] — the persistent gap between [[dvol|DVOL]] paid by option buyers and the [[realized-volatility|realized volatility]] that subsequently materialises. This is compensation for bearing tail risk and negative skew. In crypto the premium runs fatter than in equities because the tail is genuinely fatter.
- **Behavioral**: retail demand for cheap lottery-like payoffs (short-dated OTM "100x" calls) and leveraged-holder demand for crash protection (BTC/ETH puts) both systematically push implied volatility above fair value at the wings of the [[volatility-surface|surface]].

Directional and hedging structures, by contrast, carry no inherent edge — they are *expressions* of a separately-held view. A bull call spread is only as good as the directional forecast behind it.

## Why this edge exists

BTC/ETH implied volatility (DVOL) has exceeded subsequently realized volatility on average over the measured history, and the spread is materially wider than the equity VRP. The premium persists because:

- **Who is on the other side**: (1) leveraged spot holders and perp longs who *must* buy downside protection after drawdowns, largely price-insensitive; (2) retail speculators who overpay for convex lottery payoffs.
- **Why they keep losing/paying**: hedgers are not trying to win — they are buying insurance, which has a negative expected value by design. Lottery buyers exhibit well-documented probability-weighting biases ([[behavioral-finance]]): they overweight small probabilities of large gains.
- **Why it isn't arbitraged away**: harvesting the premium requires bearing crash risk with real crypto/USDC collateral on a single offshore venue. The short-vol P&L profile (steady gains, occasional violent losses — BTC −50% in 24h on 2020-03-12, −12% in 60 seconds on 2025-10-10) limits how much capital is willing to hold the position, so the premium compresses but does not vanish.

## Null hypothesis

If options were always fairly priced (no [[volatility-risk-premium]]), then:

- Systematically selling premium would earn **zero expected excess return** — collected theta would exactly pay for realized gamma losses over time, and the P&L would be pure short-volatility beta plus transaction costs (i.e., negative net of Deribit's wide costs).
- Any options structure would have the same expected return as its delta-equivalent position in the underlying (spot or perp), minus costs.
- The test: track average (DVOL at entry − subsequent realized vol). If that spread is not reliably positive, there is no edge — only repackaged market beta.

## Rules

Canonical implementation: defined-risk premium selling (short [[iron-condor]] on Deribit BTC or ETH). Other families adapt the entry/exit logic to their own structure.

**Entry**
- Underlying: Deribit BTC or ETH (deep, penny-tight relative to altcoins); altcoin chains only in small size.
- Enter only when [[dvol|DVOL]] percentile is in the upper-middle of its 1-year range (roughly 40th-90th) — sell premium when it is rich, not cheap, and not into an active vol-shock.
- Require DVOL − 30-day realized vol > 5 vol points (VRP confirmation).
- Tenor: 21-45 DTE, the theta-rich zone; avoid weeklies (crypto gamma too hot).
- Strikes: short strikes at ~16 [[delta]] (≈1 SD) on each side; long wings 8-10 delta to define risk.
- Skew-aware: read [[funding-rate|perp funding]] and lean the short toward the overbid wing.

**Exit**
- Take profit at **50% of maximum credit** received.
- Time exit at **10-14 DTE** regardless of P&L (avoids the crypto gamma-heavy final weeks).
- Stop loss when the structure trades at **2x the credit received** (loss = 1x credit).
- Vol-shock kill: flatten short vega if DVOL rises > 50% in a session.

**Position sizing**
- Maximum loss per structure ≤ **2% of account equity**.
- Aggregate short-premium exposure bounded; net portfolio [[vega]] kept short but capped (≈ ≤ 1% of NAV per DVOL vol point — tighter than an equity book because crypto DVOL can move 20-40 points in a session).
- No naked short options in size — every short leg wing-protected. This is the lesson of every blown-up premium seller and of crypto's fat tail.

## Implementation pseudocode

```python
# Defined-risk crypto premium selling (iron condor on Deribit BTC/ETH), run daily
def scan_and_trade(account, chain, underlying, market):
    if market.dvol_session_change >= 0.50:
        return flatten_short_vega(account)               # vol-shock kill first
    if not (0.40 <= market.dvol_pctl(underlying) <= 0.90):
        return                                            # premium not rich / too hot
    if (market.dvol(underlying) - market.rv30(underlying)) < 5.0:
        return                                            # VRP too thin

    exp = nearest_expiration(chain, target_dte=35)
    put_short  = strike_at_delta(exp.puts,  delta=-0.16)
    call_short = strike_at_delta(exp.calls, delta=+0.16)
    put_long   = strike_at_delta(exp.puts,  delta=-0.09)
    call_long  = strike_at_delta(exp.calls, delta=+0.09)

    credit = price_condor(put_long, put_short, call_short, call_long)
    max_loss = wing_width(put_long, put_short) - credit
    qty = floor(0.02 * account.equity / max_loss)         # ≤ 2% NAV at risk
    if qty >= 1 and aggregate_risk(account) + qty * max_loss <= 0.10 * account.equity:
        sell_condor(qty, put_long, put_short, call_short, call_long)

def manage(position, market):
    if position.pnl >= 0.50 * position.credit:            # 50% profit target
        close(position)
    elif position.mark >= 2.0 * position.credit:          # 2x credit stop
        close(position)
    elif position.dte <= 12:                              # crypto gamma-zone time exit
        close(position)
```

## Indicators / data used

- Full Deribit [[options-chain]] with bids/asks, [[greeks]], and open interest (via [[greeks-live]]).
- [[dvol|DVOL]]: level, percentile (1-year lookback), and the [[volatility-surface|IV surface]] for skew context.
- [[realized-volatility|Realized volatility]] (20/30-day) for the DVOL−RV spread that is the strategy's raison d'être.
- [[funding-rate]] and perp [[open-interest]] — the skew driver.
- [[max-pain]] / OI-by-strike and [[gamma-exposure|GEX]] for dealer-positioning context.
- Macro and crypto-catalyst calendars — avoid opening short premium through binary events unless that is the explicit trade.

## Example trade

(Illustrative.) BTC at $68,000, DVOL 55 (63rd percentile), 30-day RV 40 (VRP ≈ 15), 35 DTE, USDC-margined:

- Sell $60,000 put / buy $56,000 put; sell $76,000 call / buy $80,000 call (short strikes ≈16 delta, ~1 SD).
- Credit collected ≈ **$1,100** per 1-BTC condor. Max loss ≈ **$2,900** (wing width − credit).
- On a mid-size account, one condor sits within the 2% max-loss rule.
- Management: close at 50% profit (≈ +$550 less Deribit fees/slippage), or at 2x-credit stop, or at 12 DTE, whichever comes first. Flatten on a > 50% DVOL session spike.
- Probability profile at entry: ~65-70% chance of expiring between short strikes; the early-profit-take rule converts this into many small wins and contained losses.

## Performance characteristics

The best crypto evidence comes from on-chain option vaults and the DVOL−RV series (Deribit / [[greeks-live]]):

- **On-chain covered-call / put-selling vaults** (Ribbon/Aevo-style DOVs, Deribit auction flow) and BTC covered-call ETFs have delivered steady premium yields in calm regimes and sharp mark-downs in crypto crashes — the same distributional shape as equity put-write programs, on a fatter-tailed underlying.
- **DVOL − realized** has averaged positive and persistent, and materially wider than the equity VRP (which runs ~0.6-2 vol points on the S&P); crypto's spread routinely runs into the high single digits / low teens of vol points.
- Returns are strongly **negatively skewed**: many small gains, rare large losses. Sharpe overstates the experience; expect long grinds followed by give-backs in vol spikes (2020-03, 2022 LUNA/FTX, 2025-10-10).

**Cost overlay (Deribit, defined-risk spreads)**: four-legged condors cross the spread eight times round trip. Deribit's taker fee is 0.03% of underlying **capped at 12.5% of premium**, and bid-ask on 15-delta wings runs 3-8 vol points round-trip — far wider than SPX. This drags the realistic net Sharpe toward ~0.5. On thin altcoin chains, costs can exceed the entire edge; this strategy lives or dies on BTC/ETH liquidity. Breakeven cost tolerance is roughly double an equity book's.

Directional and long-volatility structures have **no standalone expectancy**: long premium bleeds roughly the VRP and is justified only by a forecast or a hedging need.

## Capacity limits

Deribit BTC/ETH options are the deepest crypto derivative-options market, but a fraction of listed equity index options. A systematic defined-risk premium program takes clean fills to roughly $5-25M vega-notional on front-month BTC (ETH thinner) before short-strike selection moves the surface at the wings; beyond that, use the [[greeks-live]]/Paradigm RFQ network. Whole-book capacity for an individual/small fund is roughly $50-300M notional. Altcoin options capacity is far smaller — often a small fraction, with far wider spreads. Crowding is a real constraint: covered-call ETF and on-chain vault supply compresses the call-side premium over time.

## What kills this strategy

- **Volatility regime shift / crash**: a 2020-03- or 2022-style event delivers months of accumulated premium back in days. Naked variants die outright.
- **VRP compression**: if DVOL−RV goes to zero or negative for a sustained period (vault/ETF crowding), the engine has no fuel and Deribit's costs dominate.
- **Cost creep / illiquidity**: spreads widen in stressed markets exactly when stops must execute — the 2x-credit stop can fill far worse than modeled, especially on altcoins.
- **Coin-margined wrong-way risk**: inverse collateral falls in USD terms as the short goes against you — use USDC-margined (linear) options for clean P&L.
- **Single-venue (Deribit) concentration**: an outage/insolvency during a vol event is un-hedgeable.
- **Discipline failure**: doubling down after losses, selling more premium into a DVOL spike, or removing the wings to boost credit. Most premium-selling blowups are sizing failures, not signal failures.

## Kill criteria

- Trailing 12-month average (entry DVOL − subsequent 30-day realized vol) **< 0 vol points** → the premium has vanished; stand down.
- **DVOL rises > 50% in a single session** → flatten short vega immediately.
- Strategy drawdown **> 35%** of allocated capital → stop, full post-mortem.
- Rolling 24-month net Sharpe **< 0** → retire or re-research.
- Average realized round-trip cost **> the crypto budget (≈ 60 bps)** of notional → the structure is no longer economic at this size/venue.
- Any Deribit auto-liquidation / socialised-loss / unscheduled-outage event → flatten and stand down.

## Advantages

- Backed by one of the most persistent documented premia in finance, running *fatter* in crypto than in equities.
- Defined-risk structures cap maximum loss at entry — position sizing is exact, not estimated.
- **Cash-settled, European** Deribit options — no early assignment, minimal pin risk.
- High win rate and smooth equity between vol events; mechanically simple to systematise.
- Flexible: the same toolkit expresses income, directional, volatility, and hedging views.
- **Readable skew** via the perp/funding link.

## Disadvantages

- Negatively skewed returns: losses cluster in crashes, exactly when the rest of a crypto book is also losing (positive crash-beta correlation). Crypto's tail is genuinely fatter than equities'.
- The edge is crowded on the call wing (vault/ETF supply) and Deribit's costs are wide — sloppy execution can consume it entirely.
- Multi-leg fees and slippage are material; premium-capped Deribit fees bite hardest on cheap OTM wings.
- Capped upside on every income structure; covered calls underperform badly in a melt-up.
- **No [[section-1256-contracts|§1256]] shelter** — premium is ordinary/short-term income.
- **Single-venue and coin-margined risks** absent from listed equity index options.
- Psychologically hard: long streaks of small wins breed the oversizing that the rare large loss then punishes.

## Regime Fit

Which family to deploy depends on the prevailing [[market-regime]]. Options structures are regime-sensitive in a way that single-leg directional bets are not, because they bundle a volatility view with a directional view.

| [[market-regime\|Regime]] | High DVOL percentile | Low DVOL percentile | Favored family |
|---|---|---|---|
| Range-bound, calm | sell condors/strangles | smaller credit, tighter wings | income (short premium) |
| Trending up | bull put spreads, covered calls | bull call spreads (debit) | directional + income blend |
| Trending down | bear call spreads | bear put spreads (debit) | directional / hedging |
| Pre-catalyst / vol expected | sell into the IV crush (7-21 DTE) | buy straddles before the move | volatility |
| Crash / DVOL spike | stand down; long convexity only | buy puts / long-DVOL convexity | hedging (long convexity) |

The cardinal rule: **sell premium when DVOL is rich relative to its own history, buy premium (or hold long convexity) when DVOL is cheap** — and never sell undefined-risk premium into a rising-vol regime, the failure mode behind every short-vol blowup. See [[non-linear-payoff]] for why short-vol books mark to market far worse than their stated max loss in exactly these regimes.

## Crypto specifics

- **Deribit is the market.** The vast majority of crypto options OI is on [[deribit]]; execution is there (or via on-chain vaults / BTC-ETF options).
- **European, cash-settled.** No early [[assignment]], no delivery — capped/assigned outcomes settle in cash and you keep any spot/staked coin. A genuine simplification versus American single-name options.
- **DVOL, not VIX.** The regime gauge is Deribit's [[dvol|DVOL]] index and its percentile — not VIX/IV-rank.
- **Inverse vs linear settlement.** Sell in **USDC (linear)** for clean USD P&L, or **coin-margined (inverse)** to keep collateral in coin (quanto-like non-linearity).
- **Perp-funding sets the skew.** Unlike equities' static put skew, crypto skew swings with [[funding-rate|funding]]: richly positive funding firms call skew, letting the seller lean into the overbid wing.
- **24/7 markets.** Continuous theta and continuous gap risk; weeklies are especially gamma-hot with no market close to cap a move.
- **No [[section-1256-contracts|§1256]].** Crypto (and crypto-ETF) options get no 60/40 shelter — premium is ordinary/short-term income.

## Getting the Data (CryptoDataAPI)

DVOL and the IV surface come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies the options-flow, vol-regime, dealer-gamma, funding, and liquidation context for gating entries and firing the kill switch.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (skew driver)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for VRP backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

## Sources

- [[greeks-live]] / [[deribit]] documentation — DVOL, IV surface, European cash settlement, coin-margined vs USDC-margined (linear) mechanics.
- Deribit Insights research on DVOL and the crypto variance risk premium.
- [[crypto-options-volatility-selling]] — the wiki's canonical crypto short-vol treatment.
- Sheldon Natenberg, *Option Volatility and Pricing* — structure mechanics and Greek behavior (instrument-agnostic).
- Crash record: 2020-03-12, 2022-05 [[terra-luna|LUNA]], 2022-11 [[ftx-collapse|FTX]], 2025-10-10 [[liquidation-cascade|liquidation cascade]].

## Related

- [[options]] — options market overview
- [[options-selling]] — the crypto premium-selling family hub
- [[options-premium-selling]] / [[crypto-options-volatility-selling]] — the short-vol core and its systematic book
- [[vertical-spread]] — bull/bear spreads
- [[iron-condor]] — range-bound income structure (preferred in crypto)
- [[straddle-strangle]] — volatility plays
- [[covered-call]] — income via call writing on spot BTC/ETH
- [[cash-secured-put]] — USDC-backed paid limit orders
- [[credit-spread]] — selling spreads for premium
- [[greeks]] — option price sensitivities
- [[volatility-risk-premium]] / [[variance-risk-premium]] — the underlying edge
- [[dvol]] — the crypto volatility regime gauge
- [[funding-rate]] — the perp linkage that shapes crypto skew
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[edge-taxonomy]] — edge classification framework
- [[non-linear-payoff]] — why "max loss" understates mid-trade risk
- [[convexity]] — long vs short curvature across structures
- [[expiration-selection]] — DTE choice sets the Greek mix
- [[market-regime]] — which structures fit trending vs range-bound regimes
