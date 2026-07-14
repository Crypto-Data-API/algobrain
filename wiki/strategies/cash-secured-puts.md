---
title: "Cash-Secured Puts"
type: strategy
created: 2026-04-15
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, premium-selling, volatility]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
aliases: ["Cash-Secured Puts", "Cash Secured Puts", "CSP", "Crypto Cash-Secured Put", "USDC-Secured Put", "BTC Cash-Secured Put"]
related: ["[[cash-secured-put]]", "[[covered-call]]", "[[wheel-strategy]]", "[[crypto-options-volatility-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[put-option]]", "[[theta]]", "[[vega]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[iv-crush]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
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
- `GET /api/v1/backtesting/klines` — deep kline archive for RV/put-write backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

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
