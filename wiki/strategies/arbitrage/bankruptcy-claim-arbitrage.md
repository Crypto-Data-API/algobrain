---
title: "Crypto Bankruptcy Claim Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, regulation, event-driven]
aliases: ["FTX Claims Arb", "Mt. Gox Claims", "Crypto Distressed Claims"]
strategy_type: fundamental
timeframe: long-term
markets: [crypto]
complexity: advanced
backtest_status: pilot
edge_source: [analytical, informational, structural, risk-bearing]
edge_mechanism: "Bankruptcy claims trade at a discount to ultimate recovery because most retail creditors lack patience, accreditation, or legal expertise; specialised funds underwrite the legal process and earn the spread."
data_required: [bankruptcy-court-filings, claim-trading-quotes, btc-eth-spot, dollar-claim-vs-coin-claim-tracking]
min_capital_usd: 100000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 1.6
expected_max_drawdown: 0.40
breakeven_cost_bps: 200
related: ["[[merger-arbitrage]]", "[[distressed-debt-arbitrage]]", "[[ftx]]", "[[mt-gox]]", "[[celsius]]", "[[3ac]]", "[[governance-restitution-arbitrage]]", "[[ai-amplified-exploit-arbitrage]]"]
---

# Crypto Bankruptcy Claim Arbitrage

Crypto bankruptcy claim arbitrage involves buying claims against failed crypto firms — [[mt-gox|Mt. Gox]], [[celsius|Celsius]], [[voyager|Voyager]], [[ftx|FTX]], [[blockfi|BlockFi]], [[genesis|Genesis]] — at a discount on secondary OTC markets, then waiting for the bankruptcy estate to distribute recoveries. It is the crypto-native branch of classic [[distressed-debt-arbitrage]] and sits in the event-driven [[arbitrage]] family alongside [[merger-arbitrage]] and [[risk-arbitrage]]: the edge is convergence of a discounted claim toward its ultimate court-determined recovery value. As with the [[gbtc-discount-arbitrage|GBTC discount trade]], the deep discount is necessary but not sufficient — it must beat the multi-year time value and litigation risk it compensates for ([[limits-to-arbitrage]]).

### Major crypto estates (reference)

| Estate | Filing | Case no. | Recovery currency | Status / note |
|--------|--------|----------|-------------------|---------------|
| [[mt-gox|Mt. Gox]] | 2014 (civil rehab) | Tokyo District | BTC / BCH / JPY | Distributions began 2024; embedded long-BTC |
| [[celsius|Celsius]] | 2022-07 | 22-10964 (SDNY) | USD-equiv + coin mix | Plan effective 2024; CEL write-down risk |
| [[voyager|Voyager]] | 2022-07 | 22-10943 (SDNY) | USD-equiv | FTX/Binance.US deals collapsed; self-liquidation |
| [[ftx|FTX]] | 2022-11 | 22-11068 (D. Del.) | Petition-date USD | Plan confirmed Oct 2024; ~118% on USD claims |
| [[blockfi|BlockFi]] | 2022-11 | 22-19361 (D.N.J.) | USD-equiv | Wind-down; FTX/Alameda cross-claims |
| [[genesis|Genesis]] | 2023-01 | 23-10063 (SDNY) | USD-equiv + coin | DCG cross-claims; tied to GBTC contagion |

> **Important contrast (added 2026-04-28):** This strategy works because **CeFi bankruptcy claims** trade actively in well-developed secondary markets (specialized brokers Attestor, Silver Point, Contrarian Capital, Cherokee Acquisition, Olympus Peak; bankruptcy court machinery; multi-year resolution timelines that justify claim-trading infrastructure). **In contrast, DeFi exploit claims do NOT trade meaningfully** — recovery in DeFi typically happens fast via direct treasury reimbursement (Euler weeks, Wormhole hours via Jump recap) or not at all (Beanstalk total loss; Penpie / Sonne / UwU Lend zero recovery). Found Network is not active for DeFi-specific claims; major OTC desks don't quote DeFi claims as a product line. See [[governance-restitution-arbitrage]] for the DeFi-side strategy that *does* work — built around governance-vote uncertainty arb on protocol-native tokens, bridge-token discount arb, and sympathy-depeg arb. The two strategies share legal / mechanical structure but operate on distinct markets.

Because crypto recoveries are typically denominated in *USD as of the petition date* but may be paid partially in BTC/ETH (or in cash that the buyer can re-convert), the trade often contains a hidden long-crypto exposure. FTX claims that traded at $0.10-0.15 in early 2023 reached $0.80+ by 2024 — partly from improved estate recoveries and partly from the underlying [[bitcoin]] rally.

## Edge source

A blend of four of the edge categories in [[edge-taxonomy]]:

- **Analytical**: requires modelling the estate's asset recovery, litigation outcomes, fee waterfall, and timing.
- **Informational**: court filings, creditor committee minutes, and trustee reports are public but voluminous; specialists read them all.
- **Structural**: most retail creditors *cannot* sell because they lack accredited-investor status or KYC with claim brokers; supply is forced.
- **Risk-bearing**: capital is locked for 1-7+ years with no current yield, no liquid hedge for many estates, and tail risks of denied claims or clawback litigation.

See [[edge-taxonomy]].

## Why this edge exists

Three reasons claims trade below intrinsic value:

1. **Time preference.** A retail creditor with $50K stuck in FTX prefers $35K today over a probability-weighted $50K in three years. Funds with patient capital underwrite that discount.
2. **Operational complexity.** Filing a proof of claim, KYCing with multiple claim brokers, navigating the cession process, and tracking USD-vs-coin denomination is non-trivial. Most retail outsources this by selling.
3. **Regulatory and tax friction.** Many creditors face country-specific issues (UK SIPP rules, German tax on coin distributions, US bad-debt deduction questions) that make selling more attractive than waiting.

The losers (sellers at a discount) are crypto users who never wanted to be distressed-debt investors. The winners are funds like **Attestor**, **Silver Point**, **Contrarian Capital**, **Cherokee Acquisition**, **Olympus Peak**, and the various claim brokers that intermediate.

## Null hypothesis

In an efficient market, claims would trade at NPV(expected recovery) using a risk-free discount rate. They don't — claims persistently trade 20-50% below NPV at announced recovery levels, and the spread to ultimate recovery has been positive in every major crypto bankruptcy through 2024-2025.

## Rules

### Entry
1. **Estate diligence.** Read first-day motions, schedules of assets/liabilities, trustee reports. Build a bottoms-up recovery model.
2. **Identify the denomination question.** USD-claim or coin-claim? FTX/Celsius pay USD-equivalent at petition date; Mt. Gox pays a mix of BTC, BCH, and JPY.
3. **Hedge the implied long-crypto.** If the recovery is paid in coin, hedge proportionally with short BTC/ETH perps to isolate the credit-arb spread. If the recovery is paid in USD but the *claim trades on the implied dollar value at petition date*, you have a hidden long-BTC exposure that may or may not be desired.
4. **Buy below modelled recovery minus fees minus time-discount.** Target IRR > 20% on each tranche.

### Exit
5. **Hold to distribution.** Most claims are buy-and-hold to the estate plan effective date plus distribution waterfall.
6. **Sell up the curve.** As the estate confirms a plan, claims rerate; some funds sell to less-patient secondary buyers at higher prices rather than waiting for cash.
7. **Tax-loss harvest residual.** After final distribution, any remaining basis can be deducted.

### Position sizing
- No more than 10% of book per estate.
- Stagger purchase dates to dollar-cost into the discount rather than catching the falling claim price.

## Implementation pseudocode

```python
estates = ["ftx", "celsius", "voyager", "blockfi", "genesis", "mt_gox"]

for estate in estates:
    model = build_recovery_model(
        assets=estate.scheduled_assets,
        liabilities=estate.scheduled_liabilities,
        litigation_recoveries=estate.expected_clawbacks,
        fees=estate.estimated_professional_fees,
    )
    expected_recovery_pct = model.recovery_per_dollar_of_claim
    expected_distribution_date = model.plan_effective_date + DISTRIBUTION_LAG

    quote = otc_broker.bid_offer(estate)
    irr = compute_irr(
        cost=quote.offer,
        proceeds=expected_recovery_pct,
        years=(expected_distribution_date - today).years,
    )

    if irr < HURDLE_IRR: continue

    # Adjust for crypto exposure
    if estate.recovery_currency == "coin":
        crypto_exposure = position_size * expected_recovery_pct
        short_perp(symbol="BTC", notional=crypto_exposure)
    elif estate.recovery_pegged_to_petition_date_usd:
        # Hidden long-coin if buying coin claim at low petition-date USD vs current coin USD
        evaluate_basis_risk(estate)

    buy_claim(estate, size=position_size)
```

## Indicators / data used

- **PACER** US bankruptcy court docket (free access to filings)
- **Stretto / Kroll Restructuring** — case administrator websites with trustee reports
- **Creditor committee** updates (often Twitter/blog leaks)
- **Cherokee Acquisition / Xclaim** — public claim trading marketplaces with indicative quotes
- BTC/ETH spot for hedging math
- Estate-specific token quotes (FTT, CEL) — sometimes used for directional plays around recoveries

## Example trade

**FTX claims, January 2023.** FTX filed Chapter 11 on 2022-11-11. By January 2023, claims were quoted at **$0.10-0.15 on the dollar** (per Cherokee Acquisition and Xclaim public order books). A fund that:

- Bought $10M face of GUC (general unsecured creditor) FTX claims at $0.12 in Jan 2023 (cost: $1.2M)
- Held through estate developments (Anthropic stake recovery, BTC rally, Alameda asset sales)
- Saw quotes rise to $0.50 by end of 2023, $0.80+ by mid-2024
- Final FTX plan confirmed October 2024 promised ~118% recovery on petition-date USD claims

...realised a return of approximately **5-8x on the original capital** in 18-24 months. Critical caveat: FTX recoveries were paid in USD pegged to petition-date prices (Nov 11, 2022, when BTC was ~$16K). Claim buyers who *also* held BTC had a beautiful trade; pure claim buyers without crypto exposure missed the upside from BTC running to $70K+, since their recovery was capped at the petition-date dollar amount.

This is the **hidden short-BTC** in FTX-style claims: the estate sold confiscated BTC at ~$30K rather than holding to $70K, which is one reason recoveries were higher in % terms but lower in BTC terms than they might have been. Mt. Gox is the opposite case — recoveries denominated in BTC/BCH, so a 2014 claim buyer at $0.10 received an enormous embedded long-BTC position when distributions began in 2024.

## Performance characteristics

> **Data disclaimer:** The IRR/return ranges below are *qualitative estimates* drawn from public quote feeds and reported estate outcomes (e.g., FTX claims quoted ~$0.10–0.15 in early 2023 per Cherokee Acquisition / Xclaim, rising to $0.80+ by mid-2024). They are not an audited backtest, and each estate is bespoke — past recovery multiples do not generalize.

- Median holding period: **18-48 months**
- Target unlevered IRR: **20-40%** per estate
- Realised returns on FTX cohort (2023 vintage): **40-80% IRR**
- Sharpe is meaningless on illiquid annual mark-to-market; use IRR and recovery-multiple
- Drawdown comes from delayed plans, surprise litigation, or estate asset write-downs

### Cost overlay (what eats the recovery spread)

| Cost / friction | Effect on net IRR |
|-----------------|-------------------|
| Multi-year capital lock (no current yield) | The dominant cost; time-discount on a 1–7yr workout |
| OTC bid/ask on the claim | Often 5–15 pts on illiquid names |
| Legal / diligence / specialist counsel | Fixed cost; favors larger tickets |
| Estate professional fees (advisors, trustees) | Reduces gross recovery before distribution |
| Clawback / preference litigation | Tail risk: trustee can sue claim holders |
| Hedge cost (perp funding) on coin-denominated claims | Carry over the hold if hedging the crypto leg |
| KYC / accreditation friction | Limits who can transact at all |

## Capacity limits

- Aggregate crypto-bankruptcy claim market: estimated **$10-20B** of face value across active estates as of 2024.
- A single fund can deploy **$50-500M** per estate without moving prices much, since OTC quotes are private.
- Strategy capacity is bounded by the number of large failures — a quiet year (no new $1B+ collapse) starves new vintages.

## What kills this strategy

- **Plan rejection / litigation extension.** A creditor class voting down a plan can add years to distribution. See protracted Mt. Gox saga (2014 collapse, partial distributions only beginning 2024).
- **Asset write-downs.** Estate "discovers" that recovered assets are encumbered, fraudulent, or worthless (e.g., Celsius's CEL token holdings).
- **Clawback litigation.** Trustee sues claim holders for preferential transfers received pre-petition (FTX trustee pursued large withdrawal recipients aggressively).
- **Tax law changes.** A change in US bad-debt deduction rules or German cryptocurrency tax treatment can alter post-tax IRR materially.
- **Sub-trustee fraud or misappropriation.** Rare but has happened in offshore liquidations.
- **Crypto bull market in unhedged USD-claim positions** — opportunity cost dwarfs the recovery if BTC 5x's during the workout.

See [[failure-modes]].

## Kill criteria

- Estate IRR drops below 10% due to plan delays → mark down and consider secondary sale.
- Total claim portfolio mark-to-market drawdown >30% → review thesis on each estate.
- Discovery of new fraud/litigation that extends timeline >2 years beyond model → redo recovery math.

## Advantages

- Largely uncorrelated with crypto spot once hedged
- Calendar of catalysts is reasonably observable (court hearings, plan confirmation, distribution dates)
- Repeatable as long as crypto firms keep failing — and they do
- Returns are convex when estates surprise to the upside (FTX's Anthropic stake, Mt. Gox's BTC appreciation)
- Patient capital is a real moat — most retail cannot wait

## Disadvantages

- Multi-year capital lockup
- Requires legal, tax, and bankruptcy expertise (or expensive specialist counsel)
- KYC/accreditation barriers to participate at scale
- Illiquid — secondary market is OTC and slow
- Headline risk and ESG-style scrutiny ("vulture capital on retail crypto victims")
- Each estate is bespoke; not easily systematised

## Sources

- PACER filings for FTX (Case No. 22-11068, D. Del.), Celsius (Case No. 22-10964, S.D.N.Y.), Voyager (Case No. 22-10943, S.D.N.Y.), BlockFi (Case No. 22-19361, D.N.J.), Genesis (Case No. 23-10063, S.D.N.Y.)
- Cherokee Acquisition public quote feed
- Xclaim marketplace data
- Mt. Gox Civil Rehabilitation Trustee reports (Nobuaki Kobayashi)
- Industry reporting from The Block, CoinDesk, Bloomberg crypto coverage 2022-2024

## Related

- [[arbitrage]] — parent concept
- [[merger-arbitrage]] — event-driven cousin
- [[risk-arbitrage]] — convergence-to-known-value family
- [[distressed-debt-arbitrage]] — traditional analog
- [[rights-issue-arbitrage]] — adjacent event-driven equity strategy
- [[limits-to-arbitrage]] — why discounted claims persist
- [[ftx]]
- [[mt-gox]]
- [[celsius]]
- [[3ac]]
- [[gbtc-discount-arbitrage]] — DCG/Genesis contagion link; same "discount-to-terminal-value" structure
- [[governance-restitution-arbitrage]] — the DeFi-side analog (see contrast box above)
- [[regulatory-arbitrage]]
- [[2023-03-usdc-svb-depeg]]
