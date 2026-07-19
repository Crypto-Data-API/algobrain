---
title: "tastytrade Mechanics (Crypto)"
type: concept
created: 2026-05-07
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, volatility, methodology, premium-selling, education, bitcoin, ethereum]
aliases: ["tastytrade Playbook", "tastytrade Rules", "Sosnoff Mechanics", "45-DTE 50% 21-DTE", "tastytrade Methodology"]
domain: [volatility, options, risk-management]
difficulty: intermediate
markets: [crypto, options]
related: ["[[tom-sosnoff]]", "[[short-strangle]]", "[[iron-condor]]", "[[short-put]]", "[[options-premium-selling]]", "[[premium-selling-systematic]]", "[[crypto-options-volatility-selling]]", "[[options-selling]]", "[[variance-risk-premium]]", "[[probability-of-profit]]", "[[long-vol-vs-short-vol]]", "[[long-vol-overlay]]", "[[managing-winners]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[options-portfolio-construction]]"]
---

The tastytrade mechanics are the canonical retail short-volatility playbook popularized by [[tom-sosnoff|Tom Sosnoff]] and the tastytrade media network, **ported here to crypto**: sell 16-30 [[delta]] [[short-strangle|strangles]] (or defined-risk equivalents) at roughly 30-45 days to expiration on [[deribit]] BTC/ETH, manage winners by closing at 50% of credit received, manage losers/runners by closing or rolling in the gamma zone, gate entries on [[dvol|DVOL]] percentile, and trade *small and often* so the law of large numbers approximates the theoretical [[probability-of-profit|probability of profit]]. The mechanics are mechanical by design — the trader's job is to follow the rules, not to forecast direction. Ported to crypto, the rules survive but must be **tightened**: a shorter time stop, a tighter vega budget, and a hard DVOL kill switch, because crypto's tail is genuinely fatter and its 24/7 market has no session close to cap a gap. Proponents point to multi-year VRP-driven returns; critics point to negative-skew tail events — in crypto, 2020-03-12, the 2022 LUNA/FTX bear, and 2025-10-10 — that can erase months of theta in a day for unhedged practitioners.

## Origin and scope

The rule set is the tastytrade equity/index research lineage (SPX/SPY/large-cap options). This page keeps the *methodology* — the empirically-calibrated entry/management heuristics — and re-scopes the *application* to [[deribit]] BTC/ETH options, on-chain vaults, and BTC-ETF options. The equity origin is why the canonical numbers ("45-DTE, 50%, 21-DTE") are quoted; the crypto adaptations are flagged throughout.

## Edge Source

Per the wiki's [[edge-taxonomy|edge taxonomy]], tastytrade mechanics combine three edge sources:

- **Structural / risk-bearing** (primary). Implied volatility ([[dvol|DVOL]]) on liquid BTC/ETH options has historically priced *higher* than realized volatility — the [[variance-risk-premium]], which runs 2-4× the equity premium. The seller is paid this difference for absorbing tail risk that leveraged holders and lottery-ticket buyers will not hold.
- **Behavioral** (secondary). Long-option buyers systematically overpay for OTM convexity due to lottery-ticket bias and probability-distortion of low-probability events ([[behavioral-finance]]) — the crypto "100x call" is the purest expression.

The edge is *not* analytical — there is no informational asymmetry, no clever signal. The trader is simply willing to be the insurance writer in exchange for the empirical premium.

## Why This Edge Exists

The other side of the trade:

- **Leveraged holders and funds buying BTC/ETH puts** as crash insurance — price-insensitive on the wings because the alternative (an unhedged, liquidatable book) is unacceptable.
- **Retail call buyers** chasing OTM upside in majors and altcoins — overpaying for low-probability, high-payoff structures consistent with prospect-theory probability weighting.
- **Market makers** who bake a vol risk premium into option prices to cover hedging and gamma costs; dealer flow is the *channel* through which the premium reaches end investors, not its source.

The premium has compressed as systematic short-vol supply grew (on-chain covered-call vaults, BTC covered-call ETFs, Deribit auction flow), but it has not disappeared — empirical BTC/ETH VRP remains positive on average, and *wider* than equities'. The negative-skew tail events, however, are more impactful in crypto because the gaps are larger and continuous. See [[variance-risk-premium]] and [[volatility-regime-classification]].

## Null Hypothesis

If the strategy had no edge: (1) on a multi-cycle, cost-adjusted basis the average P&L would be near zero or negative, (2) the calm-regime Sharpe would tell you nothing about the out-of-sample Sharpe through a cycle, and (3) the negative-skew tail events would erase running income in proportion to accumulated theta.

A no-edge book would still *look* profitable in calm regimes (theta is collected daily regardless of edge) and would *blow up* during shocks at a rate set by realized vs implied vol. To distinguish edge from no-edge, the trader must run long enough through enough regime variation that the cycle-average return is statistically distinguishable from zero — harder in crypto, where the venue history is short and the shocks are large.

## Rules

The published tastytrade rules, restated for crypto execution. The full playbook fits on an index card; the **crypto-adapted** column is the operative one:

| Parameter | Equity-origin rule | Crypto adaptation | Why |
|-----------|--------------------|-------------------|-----|
| Entry DTE | ~45 days | **21-45 days** (avoid weeklies) | Balance theta vs gamma; crypto gamma hotter into expiry |
| Strike delta | 16-30 delta short | 15-16 delta (tighter) | ~1 SD OTM, ~84% [[probability-of-profit\|POP]]; crypto tail favors further OTM |
| IV filter | IV rank > 30-50% | **[[dvol\|DVOL]] percentile 40-90** + VRP > 5 vol pts | VRP fattest when DVOL is high vs its own history; skip active vol-shocks |
| Winner exit | Close at 50% of credit | 50% of credit | Captures most expected P&L per unit time-at-risk |
| Loser/runner | Close or roll at 21 DTE | **Close at 10-14 DTE** | Crypto gamma accelerates faster (24/7, unbounded gaps) |
| Roll discipline | Roll for credit only | Roll for credit only | Avoids leveraging a losing trade |
| Per-trade size | 1-5% of account | 1-3%; **vega ≤ ~1% NAV per DVOL point** | "Trade small, trade often"; DVOL moves 20-40 pts in a session |
| Tail control | (implicit) | **Hard DVOL kill switch + [[long-vol-overlay]]** | Crypto's fatter, continuous tail makes this mandatory |
| Venue | many liquid chains | **Deribit BTC/ETH** (deep); altcoins tiny | Deribit is effectively the market |

### Entry

- **Underlying selection**: Deribit BTC and ETH (deep, penny-tight relative to altcoins). Altcoin chains only in small size. Avoid known-catalyst windows (large unlocks, protocol events) unless explicitly trading the IV crush.
- **DTE**: Open at **21-45 DTE** — the theta-rich zone; avoid weeklies (crypto gamma too hot).
- **Strike selection**: **15-16 delta** short strikes (~1 SD OTM). Strangles use symmetric put/call; iron condors add long wings 8-10 delta further OTM (the preferred crypto expression). **Skew-aware**: read [[funding-rate|perp funding]] and lean the short toward the overbid wing.
- **DVOL filter**: open when **DVOL percentile is 40-90** and **DVOL − 30-day realized vol > 5 vol points**. The filter exists because the VRP is fattest when DVOL is rich relative to its own history, so credits are larger and breakevens wider — but selling *above* the 90th percentile is selling into an active shock.
- **Position size**: **1-3% of account per trade**, with aggregate short vega capped at ~1% of NAV per DVOL point. "Trade small, trade often."

### Exit

- **Manage winners at 50% of credit**: close when running P&L is half the original credit. Holding to expiration captures the last 50% at the cost of disproportionate gamma risk; closing at 50% locks in most of the expected P&L per unit of time-at-risk. See [[managing-winners]].
- **Manage losers/runners in the gamma zone**: at **10-14 DTE**, close or roll regardless of P&L. Crypto gamma inside two weeks accelerates sharply — a steady winner can give back its entire credit on a single 24/7 gap.
- **Roll for credit, not for hope**: roll a challenged position to a further expiration *for a credit* only — never for a debit.
- **Take the loss when challenged**: when a strike is breached and the position is materially negative, close. Do not "manage" by adding contracts.
- **Vol-shock kill**: flatten short vega if **DVOL rises > 50% in a session** — the crypto-critical control the equity playbook lacks.

### Position Sizing

- **No more than 25-50% of NAV** committed to short-premium at any time; keep Deribit portfolio-margin utilisation low so a spike does not force liquidation.
- **Diversify across genuinely uncorrelated risk**: BTC, ETH, and non-crypto sleeves. Beware the "five altcoins = one beta bet" trap — in crypto almost everything is one beta to BTC (see [[options-portfolio-construction]]).
- **Track margin/BPR, not just credit**, as the binding constraint.

## Implementation Pseudocode

```python
def tastytrade_crypto_book(account, underlyings, market, today):
    if market.dvol_session_change >= 0.50:
        return flatten_short_vega(account)          # vol-shock kill first

    book = account.open_positions

    # ENTRY LOOP
    for u in underlyings:                            # ["BTC", "ETH"] primarily
        if not (0.40 <= market.dvol_pctl(u) <= 0.90):
            continue                                 # DVOL filter
        if (market.dvol(u) - market.rv30(u)) < 5.0:
            continue                                 # VRP too thin
        if account.margin_used > 0.5:
            continue
        if u in [pos.underlying for pos in book]:
            continue                                 # one position per name

        chain = u.deribit_chain(dte_target=35)
        short_call = chain.find_call(delta=0.16)
        short_put  = chain.find_put(delta=-0.16)
        tilt = "call" if market.funding_8h(u) > 0.0003 else "balanced"
        size = position_size(account, target_vega_per_volpt=0.01)
        place_order(iron_condor(short_call, short_put, wings_delta=0.09,
                                skew_tilt=tilt, size=size))

    # MANAGEMENT LOOP
    for pos in book:
        running_pnl_pct = (pos.credit - pos.current_value) / pos.credit
        dte = (pos.expiry - today).days
        if running_pnl_pct >= 0.5:                   # 50% winners rule
            close(pos)
        elif dte <= 12:                              # crypto gamma-zone exit
            close(pos)                               # or roll for credit if thesis intact
        elif pos.is_challenged():                    # short strike breached
            close(pos)                               # mechanical loss-take
```

The pseudocode is deliberately mechanical — the trader's role is execution and bookkeeping, not forecasting.

## Indicators / Data Used

- **[[delta]]** — strike-selection metric (15-16 delta target).
- **[[dvol|DVOL]] percentile** — the entry filter (Deribit's 30-day forward IV vs its trailing-year range).
- **[[probability-of-profit]] (POP)** — derived from delta; ~70%+ POP setups.
- **[[theta]]** — daily decay; the income harvested.
- **[[vega]]** — exposure to DVOL changes; the risk absorbed and the budget constraint.
- **[[gamma]]** — the tail risk that accelerates into the gamma zone.
- **[[funding-rate]]** — the skew driver for wing selection.
- **DTE and Deribit portfolio margin** — the time-axis of the rules and the binding capital constraint.

No directional indicators (moving averages, RSI, MACD) are used in canonical tastytrade mechanics — the strategy is explicitly direction-agnostic.

## Payoff and Greeks

The canonical [[short-strangle]] is **short-vega, short-gamma, positive-theta, and direction-neutral at entry**. The payoff is a wide plateau of maximum profit (the credit) between the short strikes, with losses that grow as the underlying breaches either strike — unbounded for naked strangles, capped at the wing width for the defined-risk [[iron-condor]] variant (preferred in crypto).

| Greek | Sign at entry | Role in the mechanics |
|-------|---------------|------------------------|
| Theta | Long (positive) | The harvested income — collected daily; the reason the 50% / gamma-zone rules exist. |
| Vega | Short (negative) | The risk being paid for — a DVOL spike marks the position down hard; the [[variance-risk-premium]] source and the tail-event killer. |
| Gamma | Short (negative) | Accelerating loss as the underlying nears/breaches a short strike — the reason the 10-14 DTE exit exists (crypto gamma explodes faster). |
| Delta | ~0 at entry | Symmetric strikes start neutral; becomes one-sided fast on a directional gap, requiring management or the mechanical loss-take. |

The DTE, 50%-profit, and gamma-zone rules are best understood as **gamma-risk-management heuristics dressed as P&L rules**: they keep the book in the slow-theta / low-gamma zone and force exits before the convex tail of short gamma dominates. The defining failure (Path D below) is a simultaneous vega and gamma shock that the time-based rules cannot escape because liquidity vanishes.

## Example Trade

**Underlying**: BTC at $68,000 on Deribit (USDC-margined).
**DVOL**: 55 (63rd percentile, above the 40 threshold); RV30 = 40 → VRP ≈ 15 vol points.
**Setup**: 35-DTE short strangle (or iron condor for defined risk).
**Short strikes**: $60,000 put (~16 delta) and $76,000 call (~16 delta). Funding +0.03%/8h → tilt toward the call wing.
**Credit**: ≈ $1,400 per 1-BTC strangle.

Trader sells 3 contracts within the vega budget.

**Path A — winner**: BTC drifts in the $63k-$74k range over 20 days. Position decays to ~50% of credit. Trader closes mechanically at 50% — banks the profit minus Deribit fees, in 20 days.

**Path B — gamma-zone management**: BTC trades sideways slowly; at 12 DTE the position is at +25% of credit. Trader closes mechanically rather than holding into the crypto gamma zone.

**Path C — loser**: a macro headline gaps BTC −8% on day 10. The put short is tested; the position is at -120% of credit. Trader closes; the next several positive trades rebuild the credit.

**Path D — tail event** (2025-10-10-style): BTC gaps −12% in minutes and DVOL spikes from 55 to 120+. Vega and gamma compound; the position is deeply underwater and bid-ask widens sharply. **The DVOL kill switch fires**; a defined-risk condor caps the loss at the wings, a naked strangle does not. This path is the strategy's defining tail risk — and the reason crypto demands the kill switch, the tighter time stop, and defined-risk structures.

## Performance Characteristics

The realistic, cost-adjusted picture (crypto, paper/vault evidence):

- **Win rate**: ~70-80% per trade — high by design, because the strikes are far OTM.
- **Average winner**: ~50% of credit (closed early per the rule).
- **Average loser**: -100% to -200% of credit (when a strike is breached or the trade gaps).
- **Naive backtest Sharpe (calm regimes only)**: high and misleading.
- **Cycle-adjusted Sharpe (including 2020-03, 2022, 2025-10-10 shocks)**: ~0.3-0.7 unhedged; ~0.6-1.0 with a [[long-vol-overlay]].
- **Max drawdown**: 30-60% in a vol shock for unhedged practitioners; 10-20% with a properly-sized overlay and DVOL kill switch.
- **Skew**: strongly negative — "many small wins, occasional very large losses," and the losses are larger in crypto than in equities.

The honest summary: in a calm regime, crypto tastytrade mechanics deliver a pleasant carry with a high hit rate and a smooth equity curve. Across a full cycle including at least one crypto vol shock, the risk-adjusted return is *closer to mediocre than great*, and survival depends on the overlay + kill switch and extreme size discipline. See [[long-vol-vs-short-vol]].

## Capacity Limits

- **Retail capacity**: effectively unlimited at the individual level on BTC/ETH.
- **Account-level capacity**: a single trader can run the playbook well into the tens of millions of notional without market-impact issues, provided they stay in Deribit BTC/ETH; altcoin chains are far thinner.
- **Strategy-level capacity (across all participants)**: the crypto VRP persists despite growing vault/ETF short-vol supply, because the marginal insurance buyer and the marginal 100x-call retail buyer are price-insensitive on the wings — but call-side premium compresses as systematic writing scales.
- **Crowding risk**: medium and rising. A trader in this strategy is correlated with on-chain vaults, covered-call ETFs, and thousands of other retail sellers; cascade dynamics ([[liquidation-cascade]]) in shocks are partly endogenous to this crowding.

## What Kills This Strategy

The dominant failure modes (cross-reference [[failure-modes]]):

1. **Negative-skew tail event**. A crypto vol shock erases months of theta in a day — 2020-03-12 (BTC −50% in 24h), 2022 ([[terra-luna|LUNA]]/[[ftx-collapse|FTX]]), 2025-10-10 (BTC −12% in 60 seconds). Unhedged: 50-100% drawdowns; hedged: 10-20%.
2. **Margin reprice / Deribit auto-liquidation**. Even with cash to cover, portfolio margin can rise 5-10x intraday and the venue force-liquidates at the worst prices.
3. **Liquidity collapse on the wings**. Bid-ask on OTM options widens sharply in a panic; getting out costs more. *Liquidity-driven ruin*, not directional ruin.
4. **Behavioral failure: refusing to take losers**. The tail-risk profile makes loss-taking psychologically hard; letting challenged positions ride into the gamma zone produces the largest losses.
5. **Concentration creep**. Five "uncorrelated" altcoin strangles are one BTC-beta bet. Sector/factor concentration is the silent stack-up — even sharper in crypto's high all-asset correlation.
6. **Single-venue and coin-margin risks**. Deribit outage/insolvency during a shock is un-hedgeable; inverse-margined collateral falls in USD terms as the short goes against you.
7. **Edge decay**. Vault/ETF supply compresses the call-side VRP over time.

The proper hedge for failure modes 1-3 is a [[long-vol-overlay]] plus the DVOL kill switch — see [[long-vol-vs-short-vol]] and [[premium-selling-systematic]] for sizing.

## Kill Criteria

Numerical conditions for pausing (cross-reference [[when-to-retire-a-strategy]]):

- **DVOL rises > 50% in a session**: flatten short vega immediately.
- **Drawdown > 25%** on the short-vol sleeve: pause new entries; close to half-size; review sizing.
- **Drawdown > 40%**: full pause; no new short-premium trades; review whether the strategy fits the current DVOL regime.
- **Rolling 12-month Sharpe < 0**: review whether the VRP has compressed beyond profitability.
- **3 consecutive months of breached strikes**: behavioral red flag — strikes too aggressive, DVOL filter mistuned, or underlying selection poor.
- **Deribit liquidity/margin stress event**: immediately halve size regardless of P&L.

## Crypto specifics

- **Deribit is the market.** Execution is on [[deribit]] BTC/ETH (or on-chain vaults / BTC-ETF options); altcoin chains are thin.
- **DVOL, not VIX.** The entry gate is [[dvol|DVOL]] percentile, not VIX/IV-rank.
- **Tighter and hard-stopped.** The crypto adaptations — 10-14 DTE time stop, ~1%-NAV-per-DVOL-point vega cap, mandatory DVOL kill switch and [[long-vol-overlay]] — exist because the tail is fatter and the market never closes.
- **European, cash-settled.** No early [[assignment]], no delivery — a simplification versus American single-name options.
- **Perp-funding sets the skew.** Richly positive [[funding-rate|funding]] firms call skew; lean the short toward the overbid wing.
- **Inverse vs linear.** USDC-margined (linear) for clean USD P&L; coin-margined (inverse) carries quanto-like non-linearity.
- **No [[section-1256-contracts|§1256]].** Crypto/crypto-ETF options get no 60/40 shelter — premium is ordinary/short-term income.

## Advantages

- **Mechanical and learnable.** The rules fit on an index card; eliminates discretionary judgment errors.
- **Real running income.** Theta is genuinely collected daily in calm regimes.
- **Fatter premium than equities** — more room to absorb Deribit's wider costs.
- **Cash-settled, European** Deribit options — no assignment, minimal pin risk.
- **High hit rate.** 70-80% winners supports adherence.
- **Combines well with overlays.** A clean *core* for the [[long-vol-vs-short-vol|short-vol-core-plus-long-vol-overlay]] construction.

## Disadvantages

- **Negative skew is brutal — and fatter in crypto.** The tail event is not theoretical; a trader running the strategy long enough will experience one.
- **Survivor bias in published results.** Both the equity tastytrade record and crypto vault marketing over-represent survivors; the blow-ups disappear. The [[karen-the-supertrader]] case (equity) is the canonical cautionary tale of the roll-the-loser failure the playbook is prone to — a universal failure mode.
- **Sharpe ratio is misleading.** Short-vol violates the Gaussian assumption catastrophically. See [[sharpe-ratio-pitfalls]] and [[deflated-sharpe-ratio]].
- **Single-venue and coin-margin risks** absent from listed equity options.
- **No [[section-1256-contracts|§1256]] shelter** — after-tax net is materially below an equity index program.
- **Crowded.** On-chain vaults, covered-call ETFs, and retail run variations of the same mechanics; cascade dynamics in shocks are partly endogenous.
- **Behavioral pitfall: the dopamine loop.** Frequent small wins reinforce oversizing right before the shock arrives.
- **Naked vs defined-risk mismatch.** Much of the published research assumes naked strangles; crypto's tail makes defined-risk condors the responsible default, with different P&L dynamics.

### Proponents vs Critics

- **Proponents** (Sosnoff, tastytrade research, many practitioners): the rules-of-thumb are derived from extensive backtesting, the [[variance-risk-premium]] is real and persistent (and fatter in crypto), the mechanical discipline is the central virtue, and traders who follow the rules across many trades harvest the premium over time.
- **Critics** (academic researchers, hedged-overlay practitioners): the published backtests are calm-regime-biased, survivor bias inflates the perceived edge, the negative-skew tail is materially worse than published Sharpes suggest, and running the playbook unhedged is structurally selling tail insurance with no reserves — a critique that bites *harder* in crypto's fatter, 24/7 tail.

The most defensible synthesis: tastytrade mechanics are a *correct core* and an *insufficient stand-alone strategy* — they earn real income, but in crypto they need the [[long-vol-overlay]], the tightened stops, and the DVOL kill switch to become a survivable, full-cycle engine.

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
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

The index-card rule set is a natural agent policy — an AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can execute it without discretion:

- **Entry filter** — `GET /api/v1/volatility/regime` (skip `vol_shock`) + realized vol from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` for the DVOL−RV > 5 check; the DVOL percentile itself comes from Deribit
- **Wing tilt** — `GET /api/v1/derivatives/funding-rates?coin=BTC` drives the `skew_tilt` branch in the pseudocode (funding > 0.03%/8h → lean the short toward the call wing)
- **Kill switch** — poll `GET /api/v1/volatility/regime/score` + `GET /api/v1/market-intelligence/liquidations` each cycle; a joint spike is the automated stand-in for the "DVOL +50% in a session" flatten rule the equity playbook lacks
- **Backtest** — replay the 50%-winner / 10-14-DTE / 2x-credit rules on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d to 2017-08) with point-in-time regimes from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02); a sample that excludes 2020-03 or 2022 is calm-regime-biased by construction
- **Tips** — enforce "trade small, trade often" as hard per-trade caps in the agent's order layer; the playbook's known failure mode (rolling losers) is precisely what mechanical execution exists to prevent

## Sources

- [[tom-sosnoff]] — primary articulator of the rules (equity-origin).
- "Market Measures" — tastytrade's in-house research segment (45- vs 30-DTE, 50% vs hold-to-expiration, IV-rank filter variants).
- [[karen-the-supertrader]] — the Karen Bruton / KKMFA case, a cautionary example of the roll-the-loser failure the playbook is prone to (equity; the failure mode is universal).
- [[crypto-options-volatility-selling]] — the wiki's canonical crypto short-vol treatment and kill-switch framework.
- [[greeks-live]] / [[deribit]] documentation — DVOL, European cash settlement, coin-margined vs USDC-margined mechanics.
- Carr and Wu, "Variance Risk Premiums" (2009) — academic measurement of the premium being harvested.
- Crash record: 2020-03-12, 2022-05 [[terra-luna|LUNA]], 2022-11 [[ftx-collapse|FTX]], 2025-10-10 [[liquidation-cascade|liquidation cascade]].

## Related

- [[tom-sosnoff]] — primary articulator
- [[short-strangle]] — the canonical structure
- [[iron-condor]] — defined-risk variant (preferred in crypto)
- [[short-put]] — single-leg variant
- [[options-premium-selling]] / [[premium-selling-systematic]] — the broader crypto strategy class and its systematic implementation
- [[crypto-options-volatility-selling]] — the deep short-vol-book treatment
- [[options-selling]] — the crypto premium-selling family hub
- [[managing-winners]] — the 50% / time-stop management rule
- [[probability-of-profit]] — the metric tastytrade emphasizes
- [[variance-risk-premium]] — the underlying edge
- [[dvol]] — the crypto vol gauge that gates entries
- [[funding-rate]] — the perp linkage that shapes crypto skew
- [[long-vol-vs-short-vol]] — the synthesis context
- [[long-vol-overlay]] — the recommended hedge layer
- [[options-portfolio-construction]] — book-level treatment
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[karen-the-supertrader]] — cautionary case study
