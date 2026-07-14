---
title: "Options Selection Framework"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, derivatives, crypto, risk-management, position-sizing, methodology]
markets: [crypto, options]
aliases: ["How to Pick Options", "Options Selection Methodology", "Options Filter Funnel", "Strike Picking Process"]
domain: [options, risk-management]
prerequisites: ["[[options]]", "[[delta]]", "[[implied-volatility]]", "[[iv-rank-and-iv-percentile]]", "[[dvol]]"]
difficulty: intermediate
related:
  - "[[crypto-options-volatility-selling]]"
  - "[[deribit]]"
  - "[[dvol]]"
  - "[[funding-rate]]"
  - "[[options-liquidity-screening]]"
  - "[[strike-selection]]"
  - "[[expiration-selection]]"
  - "[[moneyness-selection]]"
  - "[[iv-rank-and-iv-percentile]]"
  - "[[spread-width-selection]]"
  - "[[delta]]"
  - "[[theta]]"
  - "[[gamma]]"
  - "[[vega]]"
  - "[[probability-of-profit]]"
  - "[[credit-spread]]"
  - "[[long-call]]"
  - "[[covered-calls]]"
  - "[[cash-secured-puts]]"
  - "[[iron-condors]]"
  - "[[debit-spread]]"
  - "[[leaps]]"
  - "[[skew]]"
  - "[[vix-calls]]"
  - "[[options-position-management]]"
---

The **Options Selection Framework** is a five-filter funnel that walks the trader from the universe of all listed contracts down to a single tradeable structure. Every option chain on a liquid crypto underlying — [[deribit|Deribit]] BTC or ETH, where the overwhelming majority of crypto options open interest lives — exposes hundreds of strike-by-expiration combinations; the job of the framework is to systematically discard the unsuitable ones before the trader ever looks at price. Skipping the funnel — picking a strike "by gut" because the premium looks juicy — is the single most common failure mode for retail options traders. The funnel logic is instrument-agnostic; every concrete threshold below is stated in its crypto form, and the **Crypto specifics** section collects what changes versus the equity-index version this framework was first written for.

## The 5-Filter Funnel

The funnel is ordered: each filter removes contracts so the next filter operates on a smaller, cleaner set. Reordering wastes time and can hide problems (e.g., a 16-delta strike that looks attractive on paper but is functionally untradeable because of bid-ask).

| # | Filter | Question it answers | Primary metric | Detail page |
|---|---|---|---|---|
| 1 | Liquidity | Can I get in and out at fair prices? | Bid-ask, OI, volume | [[options-liquidity-screening]] |
| 2 | IV regime | Should I be a buyer or a seller of premium? | [[iv-rank-and-iv-percentile\|IV rank]] | [[iv-rank-and-iv-percentile]] |
| 3 | Expiration / DTE | How long for the thesis to play out? | DTE, [[theta]] curve | [[expiration-selection]] |
| 4 | Moneyness | ATM, OTM, or ITM? | [[delta]], standard deviations | [[moneyness-selection]] |
| 5 | Strike-by-Greeks | Exactly which strike? | [[delta]] then [[theta]]/[[gamma]]/[[vega]] | [[strike-selection]] |

Each filter is a hard gate: a contract that fails any one is discarded before the next is considered.

### 1. Liquidity Screen

Before anything else, drop contracts that cannot be entered and exited at fair prices. See [[options-liquidity-screening]] for full thresholds. Quick filter:

- **Bid-ask spread** — quote it in **vol points** (Deribit prices in IV), not dollars: ≤ ~3-5 vol points round-trip on 15-25Δ BTC/ETH wings; ≤ 5% of mid-premium as a universal cap.
- **Open interest** ≥ ~1,000 contracts on the BTC/ETH strike for retail entry; block size (≥ 25 BTC / 200 ETH) routes through the [[deribit|Deribit]] block / Paradigm RFQ network rather than the screen.
- **Volume** — the strike should print daily. Monthly (last-Friday) expiries carry the volume; weeklies and dailies far less.
- **Underlying** must have a genuinely active options market. On crypto that means **BTC and ETH**; SOL and a couple of alts are thin, and everything else is phantom liquidity — a listed chain that almost never trades.

If a strike fails liquidity, the rest of the funnel is moot: a 70%-PoP credit spread on an illiquid contract loses more to slippage than it ever earns in theta.

### 2. IV Regime Check

Before choosing direction or structure, check the volatility environment. On equities this filter uses [[iv-rank-and-iv-percentile|IV rank]] (IVR); on crypto the direct analog is the **[[dvol|DVOL]] percentile** — where Deribit's 30-day forward-vol index sits in its trailing-1-year distribution — cross-checked against the [[realized-volatility|realized-vol]] spread:

- **High DVOL percentile (≈ 50-90th) and DVOL − 30d realized > ~5 vol points** → premium-selling environment. Favor [[credit-spread|credit spreads]], [[iron-condors]], short strangles. Theta and vega both work *for* the seller. Above the ~90th percentile you are usually selling into an active vol shock — stand aside.
- **Mid percentile (≈ 30-50th)** → neutral. Either side works; emphasize directional conviction and structure efficiency.
- **Low DVOL percentile (< ~30th)** → premium-buying environment. Favor long calls/puts, debit spreads, calendars, diagonals. Vega and gamma both work *for* the buyer if the move materializes.

Match the structure to the regime before choosing strikes. Selling 16-delta puts at DVOL's 10th percentile is the same structure as at its 80th, but the expected value is dramatically different because the credit collected is a fraction as large. See [[crypto-options-volatility-selling]] for the full DVOL-gated carry book, and note crypto's [[variance-risk-premium|variance risk premium]] runs structurally fatter than SPX's (but so does the tail).

### 3. Expiration / DTE Selection

See [[expiration-selection]] for the full mechanics. Quick map:

- **Credit spreads, iron condors, short strangles**: 30-45 DTE — sweet spot of theta-curve acceleration, manageable gamma, deep enough to roll if needed.
- **Long premium (long calls, long puts, debit spreads)**: 60-90 DTE — gives the thesis time to play out, minimizes daily theta bleed.
- **Weekly income**: 7-14 DTE — extreme theta but extreme gamma, made sharper by 24/7 gap risk (no close to cap the move); only on BTC/ETH where liquidity supports it.
- **0DTE / daily**: Deribit lists daily expiries on BTC/ETH — intraday gamma scalps, hedges, or lottery tickets, never a steady income stream.
- **Long-dated** (up to ~12 months on Deribit): the long end of the crypto curve for coin-replacement or multi-quarter thesis trades. There is no formal LEAPS in crypto — see [[long-dated-options]].

### 4. Moneyness Selection

See [[moneyness-selection]] for full coverage. The choice between ATM, OTM, and ITM is a function of strategy:

- **Short premium**: OTM by 1-2 standard deviations (~16-30 delta). ATM short straddles only when explicitly targeting a catalyst's IV crush (FOMC, unlock, ETF-decision date).
- **Long premium directional**: ATM (~50 delta) for balanced gamma/vega exposure; slightly ITM (~70 delta) when conviction is high; OTM (~30 delta or less) only for lottery-ticket sizing.
- **Coin replacement**: deep ITM (~80 delta) so the option behaves nearly like the underlying, at the longest liquid [[long-dated-options|long-dated]] expiry.
- **Income overwrites (covered calls on spot BTC/ETH, or via on-chain vaults)**: 20-30 delta OTM — collect premium without high assignment probability.

### 5. Strike-by-Greeks

The final filter is the precise strike pick using [[delta]] as the dominant input. See [[strike-selection]] for the full table. Common conventions:

- **16 delta** ≈ 1 standard deviation OTM ≈ ~84% probability of expiring OTM ≈ ~68% PoP on a credit spread (after debit-cushion arithmetic) — the "tastytrade default" for short premium.
- **30 delta** — tighter, larger credit, lower PoP (~70% on the strike alone, ~60-65% PoP on a spread). Used when IVR is moderate and the trader wants meaningful credit.
- **50 delta** = ATM — used for ATM straddles, ATM debit spreads, gamma-scalping setups.
- **70 delta** ITM — used as the long leg in deep-ITM debit spreads or as coin replacement.

Once the strike is picked by delta, sanity-check theta (decay velocity), vega (IV exposure), and gamma (delta sensitivity) to confirm the trade has the Greeks profile the strategy demands.

#### Delta → probability reference

[[delta|Delta]] doubles as a rough probability that the option finishes ITM. The complement (1 − delta) approximates the probability of expiring OTM — the headline for short-premium sellers.

| Delta | ≈ SD from ATM | ≈ P(expire OTM) | Typical use |
|---|---|---|---|
| 50 | 0.0 (ATM) | ~50% | ATM straddles, ATM debit spreads, gamma scalps |
| 30 | ~0.5 SD | ~70% | Aggressive short premium, larger credit |
| 16 | ~1.0 SD | ~84% | "tastytrade default" short strike |
| 10 | ~1.3 SD | ~90% | Conservative wings, far-OTM hedges |
| 5 | ~1.6 SD | ~95% | Deep tail; often illiquid (see [[options-liquidity-screening]]) |
| 70-80 | ITM | ~25-30% OTM | Stock replacement / long leg of deep-ITM [[debit-spread\|debit spreads]] |

Caveat: delta-as-probability is a risk-neutral approximation under the option's own IV; it is not the real-world probability and it diverges under heavy [[skew]]. For a spread, the strike-level OTM probability is **not** the [[probability-of-profit]] — see the worked example below for the breakeven-win-rate arithmetic.

## Strategy-Driven Selection

The funnel is universal but the parameter values change by strategy. The table below summarizes the parameter choices for common structures; the three canonical examples that follow walk the funnel end-to-end.

| Strategy | Vol regime (DVOL %ile) | DTE | Moneyness | Strike (delta) |
|---|---|---|---|---|
| [[credit-spread\|Credit spread]] | > 40th (ideally > 50th) | 21-45 | OTM both legs | short 16-30Δ |
| [[iron-condors\|Iron condor]] | > 50th | 21-45 | OTM both wings | 16Δ each side |
| [[long-call\|Long call]] (directional) | < 30th | 45-90 | ATM / slightly ITM | 50-70Δ |
| [[covered-calls\|Covered call]] (on spot BTC/ETH) | any (adjust by DVOL) | 21-45 | OTM | 20-30Δ |
| [[cash-secured-puts\|Cash-secured put]] | > 40th | 21-45 | OTM | 16-30Δ |
| Coin replacement | any | longest liquid ([[long-dated-options]]) | deep ITM | ~80Δ |
| Long-[[dvol\|DVOL]] / protective BTC put (tail hedge) | low DVOL (regime, not %ile) | 30-90 | OTM | 10-25Δ |

Three canonical examples:

### Credit Spreads (e.g., BTC put credit spread on Deribit)

1. Liquidity: BTC monthlies — deep; weeklies thinner, check before trading.
2. Vol regime: only enter when DVOL is above its ~40th percentile; ideally > 50th, with DVOL − realized > ~5 vol points.
3. DTE: 21-45.
4. Moneyness: OTM both legs.
5. Strike: short leg at 16-30 delta; long leg per [[spread-width-selection]] (crypto widths are set in dollars proportional to the far-larger BTC notional).

### Long Call (directional bullish thesis)

1. Liquidity: BTC/ETH monthly, tight in vol-point terms on the chosen strike.
2. Vol regime: prefer DVOL below its ~30th percentile (don't pay up for vega).
3. DTE: 45-90.
4. Moneyness: ATM (50d) for balanced exposure; 70d if conviction is high and you want coin-like behavior with capped downside.
5. Strike: pick by delta first, then check that vega exposure is consistent with your DVOL view.

### Covered Call (yield overlay on long spot BTC/ETH)

1. Liquidity: monthly on BTC or ETH (or run it through an on-chain covered-call vault).
2. Vol regime: don't gate — covered calls are always running. Just adjust strike by DVOL percentile (see below).
3. DTE: 21-45 (monthly).
4. Moneyness: OTM.
5. Strike: 20-30 delta in normal DVOL; tighter (30-40 delta) when DVOL is high and credit is fat; wider (10-15 delta) when DVOL is low and you don't want to risk being called away.

## Common Selection Mistakes

The mistakes are predictable. The framework exists because every one of these failures has been documented thousands of times in retail-trader case studies.

### Chasing High Premium on Illiquid Options

A 25-delta put on a thin alt option (or an off-cycle BTC weekly) might quote wide — a mid that implies a fat credit but a bid-ask of several vol points. The "credit" is fictional — fills happen near the bid on entry and near the ask on exit, eating a large chunk of the theoretical premium per round-trip. On Deribit this is worst on anything outside BTC/ETH monthlies. Filter 1 (liquidity) prevents this entirely.

### Ignoring the DVOL Regime

Selling premium at DVOL's 5th percentile looks identical mechanically to selling at its 80th, but the risk-adjusted edge is gone. The trader collects a fraction of the credit for the same gamma exposure. Conversely, buying long premium at DVOL's 90th percentile means paying for vega that almost certainly mean-reverts against you (a DVOL/IV crush after the event passes). Filter 2 catches both.

### Picking Strikes by Gut

"This level looks like good support" is not a strike-selection method. Discretionary chart-based strike picks systematically deviate from delta-based picks in the worst direction (selecting closer-to-ATM strikes that *feel* like they "won't get hit," while collecting too little credit for the gamma assumed). Filter 5 (strike-by-Greeks) imposes statistical discipline.

### Mismatched DTE

A 7-DTE iron condor is structurally a different trade from a 45-DTE iron condor on the same strikes — the former is a gamma trade, the latter a theta trade. Traders who treat DTE as a free parameter ("I'll just go shorter for more theta") quickly discover they've taken a position they cannot manage. Filter 3 forces an explicit DTE choice.

### Skipping the Greek Sanity Check

Picking a 16-delta short put at 5 DTE into a scheduled catalyst (FOMC, a large [[token-unlocks|token unlock]], an ETF-decision date) looks like a normal credit spread but has a gamma-to-theta ratio 10× a 45-DTE position on the same strike. Filter 5's "Greek sanity check" prevents this — short premium near a catalyst or near expiry without explicit awareness of gamma is a recipe for tail blowups, and crypto's 24/7 gap risk makes it sharper than the equity version.

### Pitfalls quick reference

| Mistake | Filter that catches it | Symptom |
|---|---|---|
| Chasing premium on illiquid strikes | 1 — [[options-liquidity-screening\|Liquidity]] | Fills far from mid; "credit" never realized |
| Ignoring [[iv-rank-and-iv-percentile\|IV rank]] | 2 — IV regime | Half the credit for the same [[gamma]] |
| Picking strikes by gut / "support" | 5 — [[strike-selection\|Strike-by-Greeks]] | Too little credit for the risk assumed |
| Mismatched DTE | 3 — [[expiration-selection\|DTE]] | Gamma trade managed as a theta trade |
| Skipping the Greek sanity check | 5 — Greek check | Hidden gamma blowup near a catalyst/expiry |

## Worked Example: 16-Delta ETH Put Credit Spread (Deribit)

Walk the funnel end-to-end on a Deribit ETH chain (USDC-margined / linear, so P&L is clean USD).

**Setup**: ETH at $3,000 on 2026-07-14. Looking for a bullish-to-neutral premium-selling trade. Account size $100K, risk budget 1% per trade ($1,000).

**Filter 1 — Liquidity**: ETH monthly (last-Friday) expiries are the deep ones — bid-ask on 15-25Δ wings ~4 vol points, OI in the thousands of contracts. Pass. (Weeklies are thinner; check before trading.)

**Filter 2 — vol regime**: ETH DVOL = 55, ~55th percentile of the trailing year; DVOL − 30d realized = 8 vol points. Premium-selling viable but not rich. Proceed but accept smaller credit.

**Filter 3 — DTE**: target 21-45 DTE. The next monthly is 40 DTE. Pick it.

**Filter 4 — Moneyness**: OTM both legs.

**Filter 5 — Strike-by-Greeks**: scan the put side for the 16-delta strike.

| Strike | Delta | Mid | Bid-ask (vol pts) |
|---|---|---|---|
| 2,750 | -0.22 | $40 | ±4 |
| 2,700 | -0.16 | $28 | ±4 |
| 2,650 | -0.11 | $22 | ±5 |
| 2,600 | -0.08 | $18 | ±5 |

Short the **2,700 put** (16 delta). For the long leg, pick a width per [[spread-width-selection]] — say 100-wide on ETH. Long the **2,600 put** for $18.

**Spread**: short 2,700p / long 2,600p, 40 DTE.

- Credit: $28 − $18 = **$10**/contract
- Width: $100, max loss $100 − $10 = **$90**/contract
- R:R: 1 : 9 — ouch. Below the 1/3-of-width rule (would need credit ≥ $33.30).

**Verdict**: filter 5 reveals that the 16-delta strike at DVOL's ~55th percentile doesn't pay enough to clear the 1/3 rule. Two fixes:

1. **Move closer in**: short the 22-delta 2,750 put for $40 (short 2,750 / long 2,700, 50-wide). Spread credit: $40 − $28 = $12 on a $50 width — still below 1/3. Move closer again.
2. **Skip the trade**: the framework correctly identified that this underlying/structure/regime combination doesn't have edge today. Wait for DVOL higher in its range.

A trader without the funnel might still take the 16-delta trade at $10 because "70% PoP feels good" — and lose money over a year because the breakeven win-rate (max-loss / (max-loss + max-profit) = 90 / 100 = **90%**) requires winning 90% of trades to break even. The model PoP is ~84%. The trade is structurally edge-negative even before Deribit's wider costs.

This is exactly the failure mode the framework catches. The filters worked.

## When to Skip the Funnel

The funnel applies to *new* trade entries. It doesn't apply to:

- **Position management** (rolling, adjusting, closing) — different rule sets, see [[options-position-management]].
- **Hedges** chosen for portfolio-Greek reasons rather than expected value (e.g., a 5-10% OTM BTC put bought for tail protection regardless of DVOL — see [[tail-risk-hedging]]).
- **Event binary plays** (FOMC, a [[token-unlocks|token unlock]], an ETF-decision date) where the trader is explicitly buying gamma, not pricing a regime — though the vol-regime check still applies in reverse (DVOL usually inflates ahead of a scheduled catalyst).

## Crypto Specifics

The five-filter funnel is instrument-agnostic — the logic of screening liquidity, matching structure to the vol regime, then choosing tenor, moneyness, and strike survives intact on crypto. What changes is every concrete input, because crypto options live on [[deribit|Deribit]] (~80-90% of BTC/ETH options open interest), trade **24/7 with no close**, cash-settle to a Deribit index, and price off a [[perpetual-futures|perp]]-driven forward rather than a dividend-and-rates forward.

- **Filter 1 (liquidity) — one venue, two deep names.** No penny-pilot list, no NBBO. Deribit BTC and ETH are the only genuinely deep chains; SOL and the odd alt are thin, everything else untradeable. Screen bid-ask in **vol points** (3-8 on 15-25Δ wings is normal), OI in contracts, and route blocks through the Deribit block / Paradigm RFQ network. See [[options-liquidity-screening]].
- **Filter 2 (vol regime) — [[dvol|DVOL]] percentile replaces IV rank.** Deribit's DVOL index (the "VIX of crypto") is the crypto IVR analog. Sell premium when DVOL sits ≈ 40-90th trailing-year percentile with DVOL − realized > ~5 vol points; stand aside below (premium too thin) or above (selling into an active vol shock). The [[variance-risk-premium|VRP]] is structurally fatter than SPX's, but so is the tail (2020-03-12, LUNA, FTX, 2025-10-10). See [[crypto-options-volatility-selling]].
- **Filter 3 (DTE) — continuous gap risk, no LEAPS.** Because crypto never closes, overnight gap risk is continuous and gamma into expiry is hotter than on equities; short-premium sweet spot is 21-45 DTE, and Deribit's long end tops out near ~12 months (there is no LEAPS equivalent — see [[long-dated-options]]).
- **Filter 4/5 (moneyness & strike) — the perp book sets the skew.** Equity put skew is near-static; the crypto 25-delta [[risk-reversal|risk reversal]] oscillates with [[funding-rate|funding]]. Richly positive funding firms call skew (lean short calls); post-crash put bids firm put skew. Read funding and perp OI before picking the wing. See [[moneyness-selection]] and [[skew-trading]].
- **Settlement & tax.** Deribit options are cash-settled to index — no physical assignment, minimal pin risk (an advantage). But **inverse (coin-margined) contracts** carry a quanto-like wrong-way risk (collateral falls in USD as a short put goes against you); use USDC-margined (linear) options for clean USD P&L. And there is **no [[section-1256-contracts|§1256]] shelter** — offshore Deribit contracts are ordinary capital-gains events, so the after-tax edge is below an SPX equivalent (AU traders: ordinary CGT / trading-income treatment).

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from Deribit / [[greeks-live|Greeks.live]]. [[cryptodataapi|CryptoDataAPI]] supplies the options-flow, volatility-regime, and funding context that feed the funnel's liquidity, vol-regime, and skew filters.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (Filter 1 liquidity/positioning context)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal) (Filter 2)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite 0-100 (Filter 2)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the crypto skew driver (Filters 4-5)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for the realized-vol leg of the DVOL−RV spread

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

## Related

- [[crypto-options-volatility-selling]] — the DVOL-gated short-vol book this funnel feeds
- [[deribit]] — the venue where crypto option selection happens
- [[dvol]] — the crypto IV-regime gauge (Filter 2)
- [[funding-rate]] — the perp linkage that shapes crypto skew (Filters 4-5)
- [[options-liquidity-screening]] — Filter 1 in detail
- [[iv-rank-and-iv-percentile]] — Filter 2 in detail
- [[expiration-selection]] — Filter 3 in detail
- [[moneyness-selection]] — Filter 4 in detail
- [[strike-selection]] — Filter 5 in detail
- [[spread-width-selection]] — pairs with strike selection for spreads
- [[delta]] — primary strike-selection metric
- [[theta]] — decay budget
- [[gamma]] — risk concentration metric
- [[probability-of-profit]] — the headline number every filter feeds into
- [[credit-spread]], [[iron-condors]], [[covered-calls]], [[cash-secured-puts]], [[long-call]] — strategy pages

## Sources

- tastytrade research archive — IV-rank-gated structure selection, 16-delta short-premium convention, 30-45 DTE entry studies
- Euan Sinclair, *Positional Option Trading* — systematic strike/expiration selection and cost-aware filtering
- Lawrence McMillan, *Options as a Strategic Investment* — strategy-to-regime matching
- CBOE Options Institute — probability-of-profit and delta-as-probability educational materials
