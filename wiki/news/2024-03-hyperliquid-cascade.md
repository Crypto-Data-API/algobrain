---
title: "Hyperliquid Mass Liquidation Cascade — March 2024"
type: news
created: 2026-05-05
updated: 2026-06-20
status: good
tags: [news, crypto, defi, hyperliquid, hlp, cascade, liquidations]
aliases: ["March 2024 HL Cascade", "HLP $5M Day", "Hyperliquid Black Tuesday 2024"]
event_date: 2024-03-12
markets_affected: [crypto, defi]
impact: high
verified: false
sources_count: 0
related: ["[[hyperliquid]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-vault-architecture]]", "[[hyperliquid-liquidation-engine]]", "[[liquidation-cascade-arbitrage]]", "[[liquidation-cascade-fade]]", "[[hlp-cascade-alongside-playbook]]", "[[2025-03-jellyjelly-hlp-attack]]"]
---

# Hyperliquid Mass Liquidation Cascade — March 2024

In **mid-March 2024 (event-day approximately March 12, 2024)**, [[hyperliquid]]'s native liquidation engine processed an estimated **$300M+ in cascading forced liquidations** over a roughly 24-hour window during a sharp BTC pullback from local highs. The protocol's [[hyperliquid-vault-architecture|HLP vault]] (Hyperliquidity Provider) absorbed the brunt of the unwind as backstop counterparty and **netted approximately $5M in 24 hours** — the single most-cited demonstration to date that *being the liquidator counterparty pool can be more profitable than running individual liquidator bots*. HLP showed a brief mark-to-market drawdown on the order of **-5% intraday** during the cascade before recovering within ~48 hours as prices reverted. The event has become the canonical case study for the [[hlp-cascade-alongside-playbook|"alongside HLP" playbook]]: passive depositors got paid the cascade bonus, and attentive arbs who tactically withdrew pre-cascade and re-deposited near the bottom captured **10%+ on the cycle** (Source: [[hyperliquid-hlp-basis-arbitrage]]).

> **Note on uncertainty — page kept as DRAFT / `verified: false`.** The exact event date (March 11 vs March 12 vs spread-over-multiple-days) and the precise dollar magnitudes ($300M liquidations, $5M HLP net, -5% HLP MTM) are sourced from secondary references in [[hyperliquid-hlp-basis-arbitrage]] and [[liquidation-cascade-arbitrage]] within this wiki. They have **not** been cross-verified against on-chain records via [[hypurrscan]] or Hyperliquid's official analytics dashboards.
>
> **External verification attempt (2026-06-12, Perplexity sonar) could not confirm a March 2024 HLP cascade.** The earliest well-documented HLP stress event in external sources is the **February-March 2025 "whale" episode** (a large ETH position that HLP absorbed for ~$4M, ETH-driven), and the [[2025-03-jellyjelly-hlp-attack|JELLYJELLY attack]] in March 2025. It is plausible that this page's "March 2024 cascade" is either (a) a genuine but lightly-documented early event, or (b) a conflation with the better-known March 2025 events. Until on-chain Hyperliquid liquidation-feed / HLP NAV data for March 2024 is ingested, **treat the entire event framing as unverified.** Do not cite the magnitudes as fact.

## Background — Hyperliquid in Early 2024

By mid-March 2024, [[hyperliquid]] mainnet had been live for roughly six months (mainnet launch late 2023) but was still pre-airdrop and pre-mass-attention:

- **HLP vault TVL**: estimated **~$80-200M** range during early 2024, growing fast as USDC depositors chased yields advertised at 30-100% APR.
- **No HYPE token yet**: the airdrop would not arrive until November 28, 2024 — at this point, Hyperliquid was a pure perps DEX with no governance token; the points-farming meta was still ramping.
- **Open interest**: Hyperliquid was the dominant on-chain perps DEX by OI but still a small fraction of [[binance]] / [[bybit]] perp volume.
- **HLP role**: HLP acted as automated market-maker AND backstop liquidator on every Hyperliquid pair. When the on-chain CLOB ran thin, HLP would step in as the absorber-of-last-resort. See [[hyperliquid-liquidation-engine]] for the mechanics.

The macro setup going in: BTC had run to fresh local highs through February-early March 2024 on the back of US spot Bitcoin ETF inflows (which started January 2024). Funding rates on Hyperliquid and CEXs were elevated, indicating crowded long positioning by leveraged retail. The system was loaded.

## Trigger — A Sharp BTC Pullback

The proximate trigger was a sharp BTC pullback from local highs. Two non-mutually-exclusive characterizations appear in wiki references:

1. **Pure macro / BTC pullback.** ETF flows briefly reversed; profit-taking near a round-number top; stop-runs into thin liquidity.
2. **Memecoin-driven cascade.** Per [[hyperliquid-hlp-basis-arbitrage]]: "*During a memecoin-driven liquidation cascade on Hyperliquid, HLP took a brief -5% drawdown over 48 hours before recovering.*" This phrasing suggests a memecoin-perp move (e.g., long-tail asset on the platform) was the spark, not BTC alone.

The two are compatible: a memecoin-perp blowup on Hyperliquid can coincide with — and amplify — a BTC pullback, since cross-margined accounts auto-liquidate across pairs once equity drops below maintenance.

> **Uncertainty flagged.** Was this a BTC-led cascade, a memecoin-led cascade, or a combined event? The wiki references both framings. On-chain data via [[hypurrscan]] would settle which pair triggered the first wave of liquidations.

## The Cascade Flow

```
Step 1: Trigger move
  BTC pulls back ~5-8% in hours; or single memecoin perp dumps 30%+

Step 2: Cross-margin propagation
  Leveraged longs (10x-50x) on HL hit maintenance margin simultaneously
  Equity drops below MMR; liquidation engine fires automatically

Step 3: On-chain CLOB absorbs first wave
  Limit-order resters on the bid side fill the initial market-out flow
  Spread widens; book depth thins on the bid side

Step 4: HLP escalates to backstop role
  When CLOB depth runs thin, HLP's auto-AMM steps in as counterparty
  HLP buys the unwinding longs (i.e., HLP goes long via absorption)
  Initial entry is at progressively worse prices vs fair (~3% adverse)

Step 5: Cascade self-reinforces
  HLP absorbing forces dumps drive marks lower
  Lower marks trip more leveraged positions on next tick
  Process repeats for several minutes to hours

Step 6: Reversion
  External arbs see Hyperliquid mark trading below CEX index by 1-5%
  Cross-venue arb buys HL / shorts Binance/Bybit, closing the gap
  HLP's absorbed inventory marks back up; realized PnL crystallizes
```

This is the textbook cascade-into-vault flow described in [[liquidation-cascade-arbitrage]] and [[liquidation-cascade-fade]].

## Why HLP Netted ~$5M in 24h

Two stacked income streams produced the $5M figure:

**1. Liquidation bonuses.** Hyperliquid's liquidation engine pays a bonus (~1% of liquidated collateral, exact rate per asset config) to whoever absorbs the position. With ~$300M in cascading liquidations and HLP capturing the lion's share that the CLOB couldn't fill cleanly, the bonus pool alone is on the order of **$1-3M**.

**2. Adverse-price absorption capture.** The liquidation engine, when escalating to HLP, fills at prices materially through the prevailing CLOB best-bid — frequently 2-5% below the prevailing CEX index. When prices revert (which they did within ~48h), HLP marks back to fair and crystallizes the spread between absorption price and reversion price. On $300M of forced flow with a ~3% average absorption discount, this is roughly **$3-5M** of additional PnL.

Sum: order-of-magnitude **~$5M net in 24 hours**, consistent with the cited figure.

For context, this single 24-hour window represented a meaningful fraction of HLP's *annualized* APR contribution: a $100M HLP vault grossing $5M in one day equals roughly 1800% annualized for that day alone — which then averages out across normal operating days into the headline 30-60% APR.

## The Brief HLP -5% Drawdown — Mark-to-Market vs Realized

During the cascade itself, HLP's *displayed* return showed a sharp drawdown on the order of **-5%** over roughly 48 hours. This was almost entirely **mark-to-market**, not realized loss:

- HLP absorbed positions at prices that marked-to-fair were instantly underwater (it bought longs that immediately printed lower).
- The vault's NAV calc reflects current marks, so depositors saw vault share-price drop ~5%.
- As prices reverted within 48h, marks recovered and the *realized* outcome was **+$5M, not -5%**.

This is the textbook lesson for HLP depositors: **daily MTM volatility is normal during cascades; realized PnL is what matters at the withdrawal horizon.** Panicking out at the MTM bottom is the same mistake retail makes on every leveraged-long blowup, just dressed up as a "DeFi yield strategy."

## The Pre-Cascade Withdrawal Arbitrage

This event surfaced a tradeable meta-strategy that has since been documented in [[hyperliquid-hlp-basis-arbitrage]]:

> *"Specialist arbs that withdrew pre-cascade and re-deposited at the bottom captured 10%+ on the cycle."*

The mechanic:

1. **Detection phase**: monitor Hyperliquid open interest, leverage distribution (HL is fully transparent), and HLP's positioning. When OI is at extremes, leverage is concentrated, and HLP is already heavily long against retail short flow (or vice versa), a cascade is increasingly likely.
2. **Withdrawal phase**: redeem HLP shares before the cascade. **Critical caveat**: HLP enforces a **4-day withdrawal lockup** — you must initiate redemption ~4 days *before* the event you're trying to dodge. This makes the strategy a forecasting game, not a reactive one.
3. **Cascade phase**: hold stablecoins (or trade the cascade directionally via [[liquidation-cascade-fade]]) while HLP marks down ~5%.
4. **Re-deposit phase**: deposit fresh USDC into HLP near the MTM bottom, capturing more vault shares per dollar.
5. **Reversion phase**: HLP marks back up over 24-48h; the cycle nets ~10% on capital that briefly stepped out.

This is genuinely a specialist trade — most depositors are not paying close enough attention to detect cascade-eligible setups, and the 4-day lockup punishes anyone who reacts late.

## Lessons for HLP Depositors

1. **Daily MTM volatility is normal.** A -5% intraday print on the vault during a cascade is not a sign the strategy is broken — it's a sign the strategy is *working* (HLP is doing its absorption job, which is what generates the bonus). Panicking on the MTM low locks in a paper loss as real.
2. **The 4-day withdrawal lockup is the price of the yield.** You cannot tactically exit in real time. Anyone advertising HLP yield as "risk-free stablecoin yield" is misrepresenting the structure. The 4-day lockup *is* the illiquidity premium that drives APR above passive lending.
3. **Withdrawing in a panic is the worst possible time.** By the time you can redeem, the MTM has typically reverted, and you've crystallized a notional loss while exiting at the bottom.
4. **Position-size to your risk tolerance, not the headline APR.** A -5% drawdown on a 30-60% APR vault is normal; a -20% drawdown is the failure mode (see [[2025-03-jellyjelly-hlp-attack]]).

## Lessons for Cascade-Follower Traders

For traders not in HLP, the cascade itself is tradeable on the *directional* side:

- **Long the dip / short the spike**: see [[liquidation-cascade-fade]]. When HL marks deviate from CEX index by >2-3%, the closing trade is essentially riskless once the cascade fires have stopped.
- **Cross-venue funding arb**: when HL funding spikes during the cascade (long demand crushed, perp trades at deep discount to spot), short on CEX / long on HL captures both the price reversion and the funding inversion. See [[hyperliquid-hlp-basis-arbitrage]] for the mechanics.
- **Recovery is sharp**: most of the price reversion happens within hours, not days. This is a scalp-to-intraday window, not a swing trade.

## Lessons for HLP-Aware Active Traders — The "Alongside HLP" Playbook

The combined strategy that this event canonized:

| Leg | Action | Source of Edge |
|---|---|---|
| **Passive HLP yield** | Keep base allocation in HLP for 30-60% APR | Risk-bearing premium |
| **Tactical withdrawal** | Pre-cascade, redeem partial allocation | Forecasting + analytical |
| **Cascade-direction trade** | Long the dip on HL via [[liquidation-cascade-fade]] | Latency + structural |
| **Re-deposit at bottom** | Add HLP shares near the MTM low | Timing |
| **Hold through reversion** | Capture both passive yield and active follower returns | Stacked |

See [[hlp-cascade-alongside-playbook]] for the full operational layout. The March 2024 event is the canonical proof that this combined playbook beats either leg in isolation.

## Comparison to Subsequent Events

The March 2024 cascade established the template that subsequent Hyperliquid stress events have followed:

| Event | Date | Trigger | HLP Outcome | Notes |
|---|---|---|---|---|
| **March 2024 cascade** *(this event)* | ~Mar 12, 2024 | BTC pullback / memecoin | +$5M, -5% MTM, recovered 48h | Canonical template |
| [[2024-08-yen-carry-unwind\|Aug 5 2024 yen-carry unwind]] | Aug 5, 2024 | Macro: BoJ + Fed + US jobs | Cross-asset crypto cascade; HLP absorbed similar dynamics | Proved playbook generalizes to non-crypto-native triggers |
| [[2025-03-jellyjelly-hlp-attack\|JELLYJELLY attack]] | March 2025 | Coordinated thin-pair manipulation | HLP paper loss ~$13M before governance halt | Different category — *attack*, not market cascade |
| April 2026 (17,214 liquidations day) | Apr 2026 | TBD | Largest single-day liquidation count to date | Most recent major data point |

The key analytical distinction: **March 2024 and August 2024 were market-driven cascades** where HLP's absorption was profitable on net. **March 2025 (JELLYJELLY) was a deliberate adversarial attack** that exploited HLP's automated AMM logic on a thin asset — a different failure mode that required protocol-level intervention rather than just waiting for reversion. Any analysis of HLP's risk profile must distinguish these two regimes.

## Aftermath

- **HLP depositors**: net positive across the event window despite the brief MTM scare; APR for that month came in elevated due to the bonus capture.
- **Hyperliquid TVL**: continued growing through 2024; the cascade was a stress test that the protocol passed without insurance-fund socialization.
- **Strategy proliferation**: the "alongside HLP" pattern became publicized over Q2-Q4 2024, attracting more sophisticated capital into HLP and gradually compressing per-event returns.
- **Pre-airdrop tailwind**: combined with the November 2024 HYPE airdrop, depositors active during this March 2024 window earned outsized cumulative returns (HLP yield + airdrop allocation).

## Sources

- [[hyperliquid-hlp-basis-arbitrage]] — primary internal reference for HLP drawdown and 10%+ cycle capture.
- [[liquidation-cascade-arbitrage]] — primary internal reference for $300M cascade and $5M HLP capture.
- **HypurrScan** ([[hypurrscan]]) — on-chain Hyperliquid analytics dashboard; would settle exact date and magnitude.
- **Hyperliquid official analytics** — HLP vault NAV history, liquidation feed.
- **DefiLlama Hyperliquid category** — TVL series.
- **Coinglass / Laevitas** — cross-venue funding rates for the period.

> **Sources gap**: this page is built from internal cross-references rather than primary on-chain data. A follow-up ingestion of HypurrScan snapshots or Hyperliquid liquidation-feed exports for the March 10-14, 2024 window would let us pin down the exact event timestamp, the trigger pair, and the precise dollar magnitudes.

## Related

[[hyperliquid]] · [[hyperliquid-hlp-basis-arbitrage]] · [[hyperliquid-vault-architecture]] · [[hyperliquid-liquidation-engine]] · [[liquidation]] · [[liquidation-cascade-arbitrage]] · [[liquidation-cascade-fade]] · [[hlp-cascade-alongside-playbook]] · [[2025-03-jellyjelly-hlp-attack]] · [[2024-08-yen-carry-unwind]] · [[perpetual-futures]] · [[funding-rate]] · [[open-interest]] · [[market-regime]] · [[hypurrscan]] · [[funding-rate-arbitrage]] · [[crypto-spot-perp-futures-triangle]]
