---
title: "Box Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, box-spread, arbitrage, financing, crypto, derivatives, interest-rates]
aliases: ["Long Box", "Box Arbitrage", "Synthetic Loan", "Deribit Box"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[iron-condor]]", "[[risk-reversal]]", "[[implied-volatility]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[arbitrage]]", "[[deribit]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Box Spread

## Overview

The box spread is a four-leg options structure that combines a **bull call spread** and a **bear put spread** at the same two strikes and the same expiry. Its value at expiration is exactly the difference between the strikes, regardless of where the underlying settles. Because that payoff is fixed, the box functions as a **synthetic loan** — buy the box below the strike width to *lend*, sell it above to *borrow* — at an implied interest rate embedded in the options prices.

Box spreads are **not a directional or volatility trade**; they are a [[arbitrage|financing / arbitrage]] instrument. A correctly priced box costs the present value of the strike-width discounted at the prevailing funding rate. In crypto this is a natural fit: [[deribit]] BTC and ETH options are **European-style and cash-settled**, which is the exact prerequisite the box needs — there is no early-assignment risk of the kind that makes American equity boxes dangerous. The catch is that the box is only "risk-free" if the venue stays solvent: a Deribit box embeds **exchange credit risk** in place of the OCC-clearing guarantee that backstops an SPX box.

## Construction

Two strikes, `K_low` and `K_high`, same expiry, on the same underlying (BTC or ETH on [[deribit]]):

| Leg | Action | Strike |
|---|---|---|
| Bull call spread | Long call | `K_low` |
| | Short call | `K_high` |
| Bear put spread | Long put | `K_high` |
| | Short put | `K_low` |

- **Box width** = `K_high − K_low` (per unit of the underlying; on Deribit contracts are 1 BTC / 1 ETH per option).
- **Net debit** ≈ present value of the width. A *long box* (the layout above) is a net debit slightly below the width; the discount is the interest you earn to expiry. Reverse all four legs for a *short box* (net credit → you are borrowing).
- **Implied rate** = `(width / box price − 1) × (365 / DTE)`.

## Payoff & Breakevens

- **At expiration, any price:** the box is worth exactly the strike width. Above both strikes, below both, or in between — the two spreads always net to `K_high − K_low` in the settlement currency.
- **Long-box profit:** `width − debit paid` = interest earned over the holding period.
- **Short-box "profit":** the credit received is the borrowed principal; you repay the full width at expiry, an implied borrow cost.
- **Breakeven:** the trade clears if the box's implied rate beats your alternative — lend if implied rate > your cash yield; borrow if implied rate < your funding cost. There is no price breakeven: the payoff is path-independent.

## Greeks Profile

A correctly assembled box is **Greek-neutral by construction**: net [[delta]] ≈ 0, [[gamma]] ≈ 0, [[vega]] ≈ 0, and [[theta]] ≈ 0 in any meaningful sense (the only "decay" is the deterministic pull of the discount toward par). The single live exposure is **rho — interest-rate risk**. In crypto that rho maps to the **crypto USD funding/lending rate** (stablecoin borrow yields and the perp/futures basis), which is far higher and more volatile than a T-bill rate, so the box's implied rate reprices more than an equity box's would.

## Market View / When to Use

You hold **no view on price or volatility**. Use a box when:

- You want to **lend USDC** at a rate better than centralised-lending desks or on-chain money markets, by buying a linear (USDC-margined) box below fair value.
- You want to **borrow** against collateral cheaply by selling a box, as an alternative to Deribit portfolio-margin loans or perp-basis financing.
- A **mispricing** appears — the box's implied rate diverges from the stablecoin lending curve or the [[funding-rate-arbitrage|cash-and-carry basis]] — and you can capture the spread as near-arbitrage.

## Adjustments & Management

- **Hold to expiry.** The payoff is fixed, so there are no rolls, stops, or delta adjustments. The box settles to Deribit's expiry index at the strike width.
- **Early unwind** only if the implied rate mean-reverts and you can capture the gain before the four-leg round-trip cost eats it — usually you just hold.
- **Margin:** Deribit's **portfolio margin** recognises the offsetting legs and charges the box very little; entering the legs under isolated/standard margin instead can tie up far more capital.

## Crypto Specifics

- **Venue.** [[deribit]] is effectively the only venue with enough BTC/ETH four-leg depth to box reliably. Its options are **European-style, cash-settled to the Deribit index** — no early exercise, no physical delivery — which is precisely what a clean box requires.
- **Inverse vs linear settlement — this changes the currency of the loan.** BTC/ETH **coin-margined (inverse)** options settle in the coin, so a box on inverse contracts locks in a fixed *amount of BTC/ETH* — a **crypto-denominated** loan whose USD value floats with spot. **USDC-margined (linear)** options settle in USDC, giving a clean **USD-denominated** box. Match the collateral type to the currency you actually want to lend or borrow; mismatching them re-introduces price risk into a trade whose whole point is to have none.
- **The implied rate is the crypto USD rate.** Unlike an SPX box that prices off T-bills, a Deribit box prices off stablecoin lending yields and the [[funding-rate|perp funding]] / futures basis. When funding runs hot, box-implied financing rates run hot with it — the box and the [[funding-rate-arbitrage|cash-and-carry]] trade are two views on the same crypto USD curve.
- **24/7.** Rates quote continuously; there is no settlement-day auction or market close, so the box can be assembled or unwound at any hour, and expiry settlement happens on the schedule of Deribit's index rather than a session close.
- **No [[section-1256-contracts|§1256]].** Crypto options get **no** 60/40 blended-rate treatment. The interest captured by a box is ordinary income (short-term in the US at full marginal rates; ordinary/CGT in AU depending on trader status) — materially worse after-tax than an equivalent SPX box.
- **Alt-option liquidity limits.** Only BTC and ETH have the depth to fill four simultaneous legs at prices tight enough to leave a rate edge. Deribit's SOL and other alt options — and anything on smaller venues — are too thin; the bid-ask across four legs swamps the interest differential.

## Risks

- **Venue / counterparty risk (the dominant one).** A crypto box is only risk-free while Deribit is solvent and online. There is no OCC-style central clearing. A venue outage, hack, or insolvency at or before expiry turns the "risk-free loan" into an unsecured claim. This is the single most important difference from an equity box and caps sensible size.
- **Coin-margined quanto risk.** Boxing inverse options while thinking in USD gives you a coin-denominated payoff whose dollar value moves with spot — a silent directional exposure.
- **Execution risk.** Four legs must fill near-simultaneously; crypto's wider bid-ask can erase a thin rate edge in a single bad fill. Use combo/RFQ execution ([[greeks-live]] / Paradigm) rather than legging in.
- **Tiny edge, large scale needed.** The rate differential is a handful of basis points; the strategy only pays after fees at size, which collides with the venue-risk ceiling above.
- **Rate repricing before expiry.** If you must exit early, a jump in crypto funding rates moves the box mark against a lender (helps a borrower) — the rho exposure is real intraday even though it nets to the fixed payoff at expiry.

## Worked Crypto Example

**Underlying:** ETH, **USDC-margined (linear)** options on [[deribit]], 90 DTE. Prevailing stablecoin lending yield ≈ 8% annualised.

- Strikes: `K_low = $3,000`, `K_high = $3,500` → **box width = $500** (per 1 ETH).
- Fair box today = `$500 / (1 + 0.08 × 90/365)` = `$500 / 1.0197` = **$490.34**.
- Suppose the box is offered at **$488.00**. Implied rate = `(500/488 − 1) × (365/90)` = **≈ 9.98%** — richer than the 8% cash yield.
- **Buy the box at $488.** At expiry you receive exactly $500 in USDC regardless of where ETH trades. **Profit = $12 per 1-ETH box ≈ 10% annualised** — you have lent USDC through the options market above the lending-desk rate.
- **Mirror:** if the box instead traded at **$493** (implied ≈ 5.8%), you would *sell* the box to **borrow** USDC at 5.8% — cheaper than a margin loan — repaying $500 at expiry.

The trade's realised return is the rate edge *minus* four-leg execution cost, and it is contingent on Deribit honouring settlement.

## Getting the Data (CryptoDataAPI)

Box pricing is a Deribit order-book task ([[greeks-live]] / Deribit API for the four leg quotes and the implied rate). [[cryptodataapi]] supplies the **crypto USD rate context** you benchmark the box's implied rate against, plus options-market depth to judge fillability.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — perp funding, the near-term crypto USD rate the box competes with
- `GET /api/v1/derivatives/open-interest?coin=BTC` — futures/perp basis context for cash-and-carry comparison
- `GET /api/v1/market-intelligence/options` — BTC options OI / volume, a liquidity read for four-leg fillability
- `GET /api/v1/sentiment/stablecoins` — stablecoin market-cap and flows, a proxy for USDC lending supply/demand
- `GET /api/v1/market-intelligence/borrow-interest` — BTC margin borrow rate (Binance, 4h), a comparable financing benchmark

**Historical data:**
- `GET /api/v1/backtesting/funding` — historical funding to reconstruct the crypto USD rate curve over a box's life
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — spot path (confirms the box's price-independence)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-derivatives]] and [[cryptodataapi-market-intelligence]]. IV/DVOL are Deribit / [[greeks-live]] products, not CDA.

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — benchmark the box's implied rate against `GET /api/v1/derivatives/funding-rates?coin=ETH` (annualised perp carry) and `GET /api/v1/market-intelligence/borrow-interest`; trade only when the locked rate beats both after four-leg fees
- **Execution** — check `GET /api/v1/market-intelligence/options` OI/volume before quoting: on a thin chain, four-leg fill quality *is* the trade
- **Backtest** — reconstruct the crypto USD rate curve the box competed with using `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30)
- **Tips** — a box is rate arbitrage, not a market bet, so skip the directional regime gate; instead watch `/api/v1/sentiment/stablecoins` for USDC supply squeezes that move the whole crypto rate curve, and fold rate checks into an hourly cached `GET /api/v1/daily` poll rather than per-tick polling.

## Related

- [[funding-rate-arbitrage]] — the cash-and-carry trade the box competes with on the crypto USD curve
- [[funding-rate]] — the perp rate that anchors box-implied financing
- [[arbitrage]] — box spreads are a textbook options-arbitrage / financing structure
- [[deribit]] — the venue; European cash-settled options make the box clean
- [[section-1256-contracts]] — the tax shelter crypto boxes do **not** get
- [[iron-condor]] — a credit structure with real market exposure, contrasting the box's neutrality
- [[risk-reversal]] — a directional two-strike structure (opposite intent)
- [[greeks-live]] — combo/RFQ execution and implied-rate analytics
