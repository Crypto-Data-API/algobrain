---
title: "Volatility Swap"
type: strategy
created: 2026-06-22
updated: 2026-07-14
status: good
tags: [volatility, derivatives, quantitative, options, risk-management, crypto, bitcoin, ethereum]
aliases: ["Vol Swap", "Realized Volatility Swap", "Crypto Vol Swap"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, structural]
edge_mechanism: "An OTC forward on realized volatility paying (realized vol − strike) × notional; on BTC/ETH the sellers harvest the crypto variance/volatility risk premium because the strike (anchored to DVOL implied vol) systematically exceeds subsequent realized vol, in exchange for bearing crypto's fat crash convexity."
data_required: [realized-volatility, implied-volatility-surface, dvol-history, otc-quotes]
min_capital_usd: 100000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 50
related: ["[[variance-swap]]", "[[realized-volatility]]", "[[implied-volatility]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[volatility-trading]]", "[[delta-hedged-options]]", "[[gamma-scalping]]", "[[variance-risk-premium]]", "[[liquidation-cascade-fade]]", "[[edge-taxonomy]]"]
---

# Volatility Swap

A volatility swap is an over-the-counter (OTC) forward contract that pays the difference between the **[[realized-volatility]]** of an underlying over the contract life and a fixed **volatility strike** (set at inception near prevailing [[implied-volatility]]), multiplied by a vega notional. It lets a trader take a *direct, pure* position on realized volatility without holding and continuously [[delta-hedged-options|delta-hedging]] an options book. On crypto the reference underlyings are [[bitcoin|BTC]] and [[ethereum|ETH]], the strike is anchored to [[dvol|DVOL]] (Deribit's 30-day implied-vol index), and the market is thin and dealer-quoted — a very different liquidity picture from the equity-index vol-swap market. Its close cousin, the **[[variance-swap]]**, pays on realized *variance* (vol squared) rather than vol; the difference — linear in vol vs. linear in variance — produces a **convexity** distinction that is the central nuance of the instrument.

## Edge source

Per [[edge-taxonomy]], the (typical short) crypto volatility swap is a **risk-bearing** edge with a **structural** basis:

- **Risk-bearing** — selling a vol swap (receiving fixed strike, paying realized) earns the **[[variance-risk-premium]]**: implied vol set at strike has, on average and especially for BTC/ETH, exceeded subsequent realized vol — a spread wider than the equity-index VRP because crypto's tail is fatter. The seller is paid for bearing the risk that realized vol explodes.
- **Structural** — persistent hedging demand from leveraged perp longs, spot holders, and treasuries keeps implied vol (and hence achievable strikes) elevated relative to realized. The vol-swap seller monetizes that demand directly, without the path-dependent slippage of running a delta-hedged Deribit options book — but takes on OTC counterparty and single-desk risk instead.

## Why this edge exists

- **Who is on the other side**: crypto hedgers and long-vol/tail funds that *buy* volatility as insurance (against the next cascade) and are willing to overpay for it; dealers/market makers on the Deribit block / Paradigm network who warehouse and recycle the exposure.
- **Why they keep paying**: like all insurance, long-vol buyers accept a negative expected carry in exchange for protection that pays in crashes. Crypto buyers, trained by repeated 80% drawdowns, overpay more. The vol-swap seller collects that premium.
- **Why it isn't free money**: the seller has a short-convexity, fat-left-tail payoff. A single volatility explosion (2020-03, LUNA, FTX, 2025-10-10) can repay years of collected premium. Because a vol swap is *less* convex than a variance swap, the seller of a vol swap is exposed differently in the tail — see below.

## Vol swap vs. variance swap (the convexity point)

- A **variance swap** pays `(σ²_realized − K_var) × variance_notional`. Because the payoff is in variance, it is **convex in volatility**: gains accelerate as realized vol rises. This convexity makes variance swaps easier for dealers to replicate (via a static portfolio of options across strikes) and is why, in equities, variance swaps are far more liquid than vol swaps. In crypto, [[dvol|DVOL]] itself is computed variance-swap-style from the whole Deribit strike surface — so the replication logic exists, but the standalone crypto variance-swap market is still thin.
- A **volatility swap** pays `(σ_realized − K_vol) × vega_notional` — **linear in volatility**, hence *no* convexity. It cannot be statically replicated; dealers must dynamically hedge the "convexity adjustment" between the two, and the vol-swap strike trades slightly below the square root of the variance-swap strike to reflect that (a consequence of Jensen's inequality).
- Practical upshot: a volatility swap gives a cleaner, more intuitive bet on *vol* (no squaring to distort the payoff), but the variance swap's convexity makes it the dealer's preferred, more replicable product, and the long variance position benefits more in extreme moves — which matters a lot given crypto's tail.

## Crypto specifics

- **DVOL is the strike anchor.** Quoted vol-swap strikes track [[dvol|DVOL]] (BTC/ETH), minus the convexity adjustment. DVOL and the surface come from [[deribit|Deribit]] / [[greeks-live|Greeks.live]].
- **Thin, OTC, majors-only.** Crypto vol/variance swaps are bilateral, dealer-quoted (Deribit block / Paradigm / OTC desks), and effectively limited to BTC and ETH. There is no listed vol-swap; **Deribit's DVOL futures are the nearest exchange-traded proxy** for a clean vol view.
- **24/7 realized-vol measurement.** The realized-vol estimator runs on a continuous, no-close tape — weekend and holiday sessions count, and a single 24/7 gap (2025-10-10: BTC −12% in ~60 seconds) can dominate the realized-vol print.
- **Counterparty risk is acute.** Crypto OTC counterparties have a worse solvency track record than equity dealers (3AC, FTX, lenders in 2022). A short vol swap that "wins" is worthless if the long side that owes you cannot pay after a cascade.
- **Replication lives on one venue.** A dealer hedging the convexity adjustment does so with Deribit options — the same venue whose stress is the event being priced (single-venue concentration).
- **Fatter, wider premium.** The IV-RV spread is larger than equities' but so are bid-ask and hedging costs; the breakeven cost budget is materially higher than an equity vol swap's.

## Null hypothesis

If the volatility strike equals expected future realized volatility, a vol swap has **zero** expected payoff — selling it earns nothing beyond compensation embedded in the strike. Under this null any apparent profit to the seller is simply the [[variance-risk-premium]], i.e., fair payment for the crash tail, and a short-vol-swap book has an expected return near zero once a major crypto volatility event is included in the sample. A backtest that omits a vol explosion (2020-03, LUNA, FTX, 2025-10-10) will badly overstate the seller's edge, because the true crypto distribution is heavily left-skewed and its tail is fatter than the equity analogue.

## Rules

### Entry
1. **Form a realized-vol view.** Compare the dealer's quoted vol-swap strike (≈ DVOL, minus a convexity adjustment) against your forecast of realized vol.
2. **Sell vol** (receive fixed strike) when you expect realized < strike — the systematic carry case. **Buy vol** when you expect a vol expansion (catalyst, regime shift, cascade risk) the market is underpricing.
3. **Choose tenor and underlying** consistent with the view (BTC or ETH; 1-3 month vol swaps are most common).
4. **Negotiate terms** OTC: vega notional, observation frequency, annualization convention, realized-vol estimator, and any vol cap (caps limit the seller's tail loss). **Vet the counterparty's solvency** — non-negotiable in crypto.

### Exit
1. **Hold to maturity** — payoff settles on realized vol over the window.
2. **Unwind early** via an offsetting swap or a replicating Deribit options / DVOL-futures position if the view changes.
3. **Tail stop** — for short positions, exit or hedge (buy Deribit convexity / DVOL futures) if realized vol breaks decisively above strike.

### Position sizing
- Size vega notional to a stressed realized-vol scenario (e.g., realized vol tripling in a cascade — well within crypto precedent), not to the expected carry.
- Prefer **capped** vol swaps for short positions to bound the left tail; the cap costs carry but converts an unbounded loss into a known maximum.
- Reserve for counterparty failure — assume the winning leg may not fully pay after a systemic event.

## Implementation pseudocode

```python
def short_vol_swap(underlying, tenor, strike_vol, vega_notional, cap=None):
    # short: receive strike, pay realized (BTC or ETH, 24/7 realized-vol path)
    realized = annualized_realized_vol(price_path(underlying, tenor))
    payoff_to_long = (realized - strike_vol) * vega_notional
    if cap is not None:
        payoff_to_long = min(payoff_to_long, (cap - strike_vol) * vega_notional)
    seller_pnl = -payoff_to_long            # we are short the swap
    return seller_pnl

def decide(strike_vol, forecast_vol, hurdle):
    # strike_vol anchored to DVOL minus convexity adjustment
    if strike_vol - forecast_vol > hurdle:  # carry rich enough (wider hurdle than equities)
        return "SELL_VOL"
    if forecast_vol - strike_vol > hurdle:  # cheap vol into a catalyst / cascade risk
        return "BUY_VOL"
    return "PASS"
```

## Indicators / data used
- **Vol-swap / [[variance-swap]] strikes** (dealer quotes) vs. your **[[realized-volatility]]** forecast.
- **[[dvol|DVOL]] and the [[implied-volatility]] surface** — strikes are anchored to DVOL; the convexity adjustment links vol- and variance-swap strikes. From [[deribit]] / [[greeks-live]].
- **[[variance-risk-premium]]** estimates — the historical DVOL-minus-realized gap on BTC/ETH.
- **Realized-vol estimators** (close-to-close, Parkinson, Garman-Klass) computed on the 24/7 tape, and the contract's specified estimator.
- **Liquidation / cascade feed** — an early-warning tape for the vol explosion that hits a short (see [[liquidation-cascade-fade]]).

## Example trade

*Illustrative, round numbers — not a backtest.*

A trader sells a 1-month BTC volatility swap struck at 50% (near BTC DVOL) with a vega notional of $50,000 per vol point.
- **Calm scenario**: realized vol comes in at 40%. Payoff to the long = (40 − 50) × $50,000 = −$500,000, so the *seller* earns **+$500,000**.
- **Shock scenario**: a cascade (2025-10-10-style) pushes realized vol to 95%. Payoff to the long = (95 − 50) × $50,000 = +$2,250,000, so the seller *loses* **$2,250,000** — many times the calm-case gain. A vol cap (say at 85%) would have bounded that loss to $1,750,000. This asymmetry — sharper in crypto than in equities — is the whole risk story of short vol.

## Performance characteristics
- **Return profile (short)**: steady positive carry from the crypto variance premium, with rare, severe losses on vol spikes — short-convexity, negatively skewed, and fatter-tailed than the equity version.
- **Vs. delta-hedged options**: a vol swap delivers a *cleaner* realized-vol exposure with no path-dependent hedging error, but as an OTC crypto product it carries acute counterparty risk and wide spreads.
- **Best conditions (short)**: persistently elevated DVOL with subdued realized vol (calm-but-fearful regimes).
- **Worst conditions (short)**: regime shifts and cascades where realized vol explodes on the 24/7 tape.

## Capacity limits
Crypto vol swaps are OTC and thinner than [[variance-swap]]s, which are themselves thin in crypto; capacity is constrained by dealer balance sheet and willingness to warehouse the convexity-adjustment risk on Deribit. BTC supports larger notional than ETH; alts effectively none (frontmatter `capacity_usd: 100000000` reflects a small, single-desk-limited market). Crowding among short-vol sellers raises systemic fragility — a crowded short-vol complex can amplify a volatility spike as dealers and sellers hedge in the same direction into a [[liquidation-cascade-fade|cascade]].

## What kills this strategy
- **A volatility explosion** that overwhelms accumulated carry on the short side (2020-03, LUNA, FTX, 2025-10-10; see [[failure-modes]]).
- **Counterparty default** on the OTC contract — a live, repeatedly-realized risk in crypto (3AC, FTX, lender insolvencies).
- **Liquidity evaporation** preventing early unwind or replication during stress.
- **Crowded short-vol positioning** that turns a vol spike into a cascade.
- **Single-venue (Deribit) disruption** breaking the dealer's replication hedge.

## Kill criteria
- Realized vol breaches the strike by more than a preset multiple → exit / hedge the short (buy Deribit convexity or DVOL futures).
- Mark-to-market loss exceeds ~2-3× the contract's expected carry → unwind.
- Counterparty credit deterioration → novate or close immediately (do not wait in crypto).
- For uncapped short positions, any disorderly vol spike → cover immediately.

## Advantages
- **Pure, direct** exposure to realized volatility — no delta-hedging path dependence.
- Clean expression of the crypto [[variance-risk-premium]] for sellers, which is fatter than the equity version.
- Linear (intuitive) payoff in vol units; caps can bound seller risk.
- Customizable OTC terms (tenor, estimator, observation frequency).

## Disadvantages
- **Acute OTC counterparty risk** and wide spreads vs. listed products — worse in crypto than equities.
- **Short-convexity tail** — large losses in vol spikes (sellers), and crypto's tail is fatter.
- **Thin and majors-only** — less liquid than even crypto variance swaps; hard to unwind in stress; BTC/ETH only.
- **No static replication** — the linear-vol payoff is harder for dealers to hedge, embedded in pricing.
- **Single-venue replication risk** — dealer hedges live on Deribit, the venue whose stress is the priced event.

## Getting the Data (CryptoDataAPI)

Vol-swap strikes, DVOL, and the raw IV surface come from **Deribit** / [[greeks-live|Greeks.live]] and OTC dealer quotes — CryptoDataAPI does not serve OTC swap marks. [[cryptodataapi|CryptoDataAPI]] supplies the realized-vol inputs and the vol-regime / liquidation context around the trade.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-explosion early warning for a short)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV to compute the realized vol the swap pays on
- `GET /api/v1/backtesting/klines` — deep kline archive to backtest realized-vol vs strike across 2020-03/LUNA/FTX/2025-10-10

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90"
```

Auth: `X-API-Key` header. For the DVOL index/history that anchors the strike, and the full surface, use the Deribit API or [[greeks-live]]. Full catalog on [[cryptodataapi]].

## Sources
- General market knowledge; Deribit / [[greeks-live]] DVOL and surface documentation; no specific wiki source ingested yet.
- Crypto vol-shock record: 2020-03-12 Black Thursday, 2022-05 LUNA, 2022-11 FTX, 2025-10-10 cascade (see [[liquidation-cascade-fade]]).

## Related
- [[variance-swap]] — the convex sibling instrument
- [[dvol]] — the implied-vol benchmark that anchors the strike
- [[deribit]] / [[greeks-live]] — venue, surface, and DVOL-futures proxy
- [[realized-volatility]], [[implied-volatility]] — the payoff reference and strike anchor
- [[variance-risk-premium]] — the harvested premium
- [[delta-hedged-options]], [[gamma-scalping]] — the listed-options way to trade realized vol
- [[volatility-trading]] — broader context
- [[liquidation-cascade-fade]] — the crypto vol-shock case pages
- [[edge-taxonomy]] — classification
