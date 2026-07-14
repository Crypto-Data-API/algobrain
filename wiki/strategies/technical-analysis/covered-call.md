---
title: "Covered Call (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, income, premium-selling, covered-call, derivatives, bitcoin, ethereum]
aliases: ["Buy-Write", "Covered Call Writing", "Crypto Covered Call", "BTC Covered Call", "ETH Covered Call", "covered-calls", "covered-call-strategy"]
strategy_type: hybrid
timeframe: swing|position
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[wheel-strategy]]", "[[cash-secured-put]]", "[[collar]]", "[[protective-put]]", "[[options-selling]]", "[[crypto-options-volatility-selling]]", "[[iron-condor]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[staking]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[max-pain]]", "[[cryptodataapi]]"]
---

# Covered Call (Crypto)

## Overview

The covered call is the most common [[options]] income structure, re-scoped here for crypto. The trader holds spot [[bitcoin|BTC]] or [[ethereum|ETH]] (or a BTC ETF position) and sells one [[call-option|call]] against those coins on [[deribit]], collecting the option [[premium]] as immediate income. The premium lowers the effective cost basis and provides a small downside buffer, while capping the upside at the chosen [[strike-price]]. The structure is **bullish-to-neutral** — it performs best when spot drifts sideways or rises modestly, so the short call expires worthless and the writer keeps both the coins and the full premium.

Because crypto [[implied-volatility|IV]] (measured by Deribit's [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]]) runs structurally far above equity IV, crypto covered-call premium yields are correspondingly richer — annualized premium on a monthly ~0.25-delta call routinely runs 15-40%+ versus 4-10% for large-cap equities. That yield is not free money: it is compensation for crypto's higher realized volatility and genuinely fatter tail. The strategy has been industrialized by on-chain option vaults (Ribbon/Aevo lineage) and by listed BTC covered-call ETFs.

## Construction

- **Underlying:** spot BTC/ETH held on the exchange or in custody, OR a BTC-ETF share position. On-chain, a covered-call vault deposits the coin and auto-writes calls.
- **Short leg:** sell 1 out-of-the-money (OTM) call per unit of coin, typically at a [[delta]] of 0.20-0.35 — a balance between premium and cap probability. Deribit contracts are 1 BTC / 1 ETH per contract.
- **Settlement choice:** sell a **USDC-margined (linear)** call for clean USD income, or a **coin-margined (inverse)** call to receive the premium in BTC/ETH and stack coin (accepting quanto-like non-linearity — see *Crypto specifics*).
- **Tenor:** 21-45 DTE captures the steepest [[theta]] decay. Weeklies pay more frequently but carry hotter gamma into crypto's continuous gap risk.
- **IV gate:** prefer writing when DVOL is in the upper half of its trailing range (rich premium); avoid selling calls into a suppressed-vol trough.

## Payoff & breakevens

At expiry the payoff is the classic bent line: long spot 1-for-1 below the strike (lifted by the premium), then flat above the strike.

| Point | Value |
|---|---|
| **Breakeven** | Spot cost − premium received |
| **Max profit** | (Strike − spot cost) + premium, reached at/above the strike |
| **Max loss** | Spot → 0 minus premium (same as holding the coin, premium-buffered) |

A covered call is **synthetically a short put**: identical economics to a [[cash-secured-put]], which is why both legs sit inside the [[wheel-strategy]]. On Deribit's cash-settled European options the "cap" is realized as a cash payment at expiry rather than by delivery of coin (see *Crypto specifics*), but the P&L shape is identical.

## Greeks profile

Dominated by the long spot (delta ≈ +1.0) with the short-call overlay subtracted on top:

| Greek | Sign | Driver |
|---|---|---|
| [[delta]] | Positive, < 1.0 (≈ +0.65-0.80 at a 0.25-delta call) | Long coin minus the short call's delta; upside progressively given up toward the strike |
| [[gamma]] | Negative (small) | From the short call; matters near expiry/ATM — the reason to manage before the last week |
| [[theta]] | Positive | The income engine; the short call decays in the writer's favor, fastest in the 21-45 DTE window |
| [[vega]] | Negative | A DVOL spike marks the short call up (paper loss) even with spot flat; rich IV at *entry* is what makes the write worthwhile |

Positive theta and negative vega are the short-premium signature: the writer is paid for time and is short volatility, harvesting the crypto [[variance-risk-premium|variance risk premium]].

## Market view / when to use

- **Sideways-to-mildly-bullish** on the coin over the next few weeks; you would be content to sell at the strike.
- You hold long-term BTC/ETH and want to **monetize the position's high IV** without selling the coins.
- DVOL is elevated (rich premium) but you do not expect a violent breakout above the strike.
- You want a yield overlay that stacks with [[staking|staking yield]] (ETH) or with the [[funding-rate|funding]] carry from a [[cash-and-carry]] leg.

Avoid in strong trending bull phases (the cap causes painful underperformance versus simply holding) and understand the premium is a thin cushion, not a hedge, in a crash.

## Adjustments & management

- **Take profit early:** buy the call back at 50-80% of max credit, then re-write — improves premium capture per unit of tail risk.
- **Roll up and out:** if spot rallies through the strike, buy back the call and sell a higher-strike, later-dated call, ideally for a net credit, to lift the cap. See [[trade-repair-and-rolling]].
- **Roll down after a drop:** if spot falls and the call is nearly worthless, roll to a lower strike for meaningful premium — only if you are comfortable capping at the new, lower level.
- **Manage before the last week:** unlike equities there is no market close, so an ATM call can swing across the strike on a weekend move; close or roll ~7-14 DTE to sidestep the hottest gamma.
- **Sizing:** one short call per unit of coin held — never more (that creates naked upside). Keep any single position to a sensible book weight; size the coin position as if the premium did not exist.

## Crypto specifics

- **Spot BTC/ETH or via Deribit.** The canonical construction is spot coin in custody + a Deribit short call. On-chain covered-call vaults and BTC covered-call ETFs (e.g., listed buy-write products) automate the same payoff.
- **No early assignment / cash settlement.** Deribit options are **European and cash-settled to the Deribit index** — there is no early [[assignment]] and no shares are "called away." If the call finishes ITM it settles in cash (index − strike), which offsets your spot appreciation above the strike; **you keep the coins** (and any staked position) and pay the cap in cash. This is a genuine simplification versus American-style US equity options. Note that **BTC-ETF options (e.g., IBIT) are American-style and physically settled** in ETF shares, so those behave like equity covered calls with real early-assignment mechanics.
- **Inverse vs linear settlement.** A **coin-margined (inverse)** call is quoted and settled in BTC/ETH — the premium arrives as coin, but payoff is non-linear in USD (a quanto-like effect: your collateral and the option both move with spot). A **USDC-margined (linear)** call gives a clean USD payoff at the cost of tying up stablecoin. Match the collateral to the exposure you actually want.
- **DVOL makes the premium rich — and the risk real.** High DVOL is why crypto buy-write yields dwarf equity yields; it also means the moves the cap gives up (and the drawdowns the buffer fails to cover) are larger.
- **24/7 markets.** Theta accrues over weekends and holidays; there is no session gap, but gap risk is continuous and weekend liquidity is thin. Weeklies are especially gamma-sensitive.
- **No [[section-1256-contracts|§1256]] treatment.** Crypto options (and crypto-ETF options) do not receive the 60/40 blended rate that broad-based US index options enjoy — premium and cap events are ordinary/short-term capital events (ordinary income or CGT in AU depending on trader status). After-tax yield is materially below the headline.
- **Perp-funding interaction.** In positive-[[funding-rate|funding]] (leveraged-long) regimes, call skew firms and buy-write premiums richen — a tailwind for the writer. The covered call competes with, and can be stacked on top of, [[cash-and-carry|cash-and-carry]] funding carry.
- **Staking-yield interaction.** On ETH you can write calls against staked/liquid-staked ETH to stack **staking yield + call premium** on the same coin; because Deribit settles in cash you never have to deliver the (possibly locked) staked ETH. Watch liquidity of the staked asset if you must post it as margin.

## Risks

- **Capped upside:** all gains above the strike are forgone — acute in crypto's explosive rallies.
- **Thin downside buffer:** the premium offsets only a few percent of a 30-50% crash.
- **Coin-margined non-linearity:** using inverse options couples collateral and payoff to spot.
- **Whipsaw / path dependency:** roll down after a drop, then a V-shaped recovery rips through the lower strike — locking the decline while forfeiting the rebound.
- **Vol compression:** systematic vault and ETF call-writing supply compresses call-side premium over time.
- **Venue concentration:** Deribit dominates crypto options; a venue outage during a vol event is hard to hedge.

## Worked crypto example

**Setup (illustrative).** Hold 10 ETH at spot $3,050. ETH DVOL 58 (rich). Sell 10 monthly (35 DTE) USDC-margined $3,450 calls (~0.22 delta) at ~$95 each → **$950 premium**.

- **Spot below $3,450 at expiry:** calls expire worthless. Keep $950 (~1.0% of the $30,500 position for the month, ≈ 12-13% annualized) plus any spot drift; re-write next cycle.
- **Spot rallies to $3,700:** calls settle ITM. You keep the 10 ETH (cash-settled, not called away) and pay ~$250 × 10 = $2,500 cap, offset by your $6,500 spot gain — net +$4,000 + $950 premium, but you "miss" the move above $3,450.
- **Spot drops to $2,700:** calls expire worthless (keep $950), but the 10 ETH lost $3,500. Net −$2,550 — the premium offset ~21% of the decline.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface are Deribit / [[greeks-live]] products. [[cryptodataapi]] supplies the complementary options-flow, volatility-regime, and funding context for strike selection and timing.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (dealer-positioning context for strike choice)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (call-skew driver; richer premium when positive)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for realized-vol and cost-basis tracking

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

## Related

- [[wheel-strategy]] — extends the covered call into a full income cycle with cash-secured puts
- [[cash-secured-put]] — the synthetic-short-put counterpart; the other half of the wheel
- [[collar]] — adds a protective put to a covered-call position
- [[protective-put]] — the opposite structure (buying puts for protection rather than selling calls for income)
- [[options-selling]] — the broader premium-selling family this belongs to
- [[crypto-options-volatility-selling]] — the systematic short-vol book on Deribit BTC/ETH
- [[iron-condor]] — defined-risk premium selling without holding the coin
- [[deribit]] — the venue; DVOL and surface source
- [[greeks-live]] — the analytics/RFQ workbench
- [[implied-volatility]] — the driver of premium richness
- [[funding-rate]] — the perp linkage that shapes crypto call skew
- [[staking]] — stackable yield on ETH covered calls
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]] — the income Greek; [[vega]] — the IV-spike risk

## Sources

- [[deribit]] / [[greeks-live]] documentation — DVOL, European cash settlement, coin-margined vs USDC-margined (linear) option mechanics
- [[crypto-options-volatility-selling]] — the wiki's canonical treatment of the crypto variance risk premium these premiums come from
