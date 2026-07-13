---
title: "Resolution Risk Hedging"
type: concept
created: 2026-05-03
updated: 2026-06-11
status: good
tags: [prediction-markets, risk-management, hedging, derivatives]
aliases: ["Resolution Risk Hedging", "Pre-Resolution Hedging"]
domain: [risk-management]
prerequisites: ["[[prediction-markets]]", "[[oracle-disputes]]", "[[hedging]]"]
difficulty: advanced
related: ["[[polymarket]]", "[[oracle-disputes]]", "[[prediction-market-strategies]]", "[[hedging]]", "[[risk-management]]"]
---

Resolution risk hedging is the practice of offsetting prediction-market exposure with correlated instruments before a market settles, in order to lock in profit and neutralise the residual chance that resolution itself goes wrong. It is most relevant to traders running large or concentrated positions on platforms like [[polymarket]] and [[kalshi]], where the price has converged to near-certainty (95%+ implied probability) but the path from "market consensus" to "paid out" still passes through an [[uma]] optimistic oracle, a CFTC-regulated settlement process, or a smart contract — any of which can fail, dispute, or stall.

## Sources of Resolution Risk

Even when a prediction market position is "obviously winning" by economic substance, several distinct risks remain between the current price and final payout:

- **Oracle dispute risk** — Polymarket settles via the UMA optimistic oracle with a standard 2-hour challenge window after the initial proposal. Any UMA token holder can dispute a proposed outcome, which escalates to a Data Verification Mechanism (DVM) vote and can extend resolution by days. See [[oracle-disputes]] and [[uma]] for mechanics.
- **Resolution delay** — Even without a dispute, edge cases (ambiguous wording, missing data source, weekend/holiday timing) can stretch resolution. Capital is locked at $1.00 implied value while it could be redeployed elsewhere.
- **Ambiguous resolution criteria** — The market question may not map cleanly onto reality (e.g., what counts as a "ceasefire", which data print resolves "Fed cuts in March", does a delisted ticker count as "above $X"). Ambiguity is where disputes live.
- **Platform / settlement risk** — Smart contract bugs, exchange insolvency, frozen withdrawals, or regulatory action against the venue. This is generic [[counterparty-risk]] applied to prediction-market venues.
- **Correlation breakdown** — The traded asset that *should* determine the outcome diverges from the resolution source (e.g., spot BTC closes above $80K on Coinbase but the resolution source is a different exchange or index that prints below).

## When to Hedge

Hedging is not free — it caps upside and consumes capital. It is justified when:

- Implied probability is high (typically 90%+) and the marginal EV from holding to resolution is small relative to position size.
- The underlying event has a **liquid, correlated tradable instrument** (perp, option, or another prediction market).
- Capital efficiency matters — you would rather redeploy locked capital than wait for settlement.
- Position size is large enough that even a 1-2% dispute/delay tail risk represents meaningful dollars.
- You are exposed to a single platform whose [[counterparty-risk]] you cannot ignore.

## Hedging Methods

### 1. Cross-platform hedge

If the same outcome is tradable on a second venue with **independent** resolution (e.g., [[polymarket]] vs [[kalshi]]), sell the same outcome on the cheaper venue once your primary leg is profitable. Because Polymarket uses UMA and Kalshi uses CFTC-regulated internal resolution, dispute risk on one does not propagate to the other. Note that resolution criteria are not always identical — read the rules carefully or you create [[basis-risk]].

### 2. Correlated instrument hedge (perps)

For price-based markets ("BTC above $80K by EOY", "ETH above $4K by date"), short the underlying perp on [[hyperliquid]], [[drift-protocol]], or dYdX in size proportional to the remaining gap. If you hold a winning YES position, a short perp leg locks in profit if the price drops back below the threshold before resolution. Funding rates and basis between perp and spot must be tracked — see [[basis-risk]].

### 3. Options collar

For positions where you want to keep some upside but floor downside, buy puts on the underlying (e.g., spot ETH puts on [[deribit]]) so that a sharp adverse move before settlement is bounded. More capital-efficient than a full perp hedge when the position is far in the money but not certain.

### 4. Conditional / correlated prediction-market spread

Hold offsetting positions across correlated questions on the same or different platforms — e.g., "Fed cuts in June" YES vs "CPI prints above 3.0%" YES, or two phrasings of the same event with different resolution sources. This neutralises the directional macro view while retaining edge from mispricing between phrasings.

### 5. Early exit (sell into market liquidity)

The simplest hedge: sell the position into the order book before resolution rather than waiting. Trade a few cents of expected value for full certainty and immediate capital release. Often optimal when the order book is deep enough to absorb size and dispute/delay risk × position size exceeds the spread cost.

## Worked Example

Assumptions: round numbers, illustrative only.

A trader holds **10,000 YES shares** on a Polymarket question "BTC above $80,000 on Dec 31" trading at **$0.95** with BTC currently at $85,000 and 3 days to resolution. Position cost basis: $9,500. If it resolves YES at $1.00, profit = $500.

**Risks remaining:**
- BTC could drop below $80K in the next 3 days (market risk).
- UMA dispute could push resolution out by 2-7 days (oracle risk).
- Settlement source ambiguity (which BTC print at what timestamp).

**Hedge:** Short ~$10,000 notional BTC perp on [[hyperliquid]] (delta-equivalent to the directional risk on the position). If BTC stays above $80K and the market resolves YES, the trader earns the $500 prediction-market profit minus any perp PnL from BTC drift, minus funding costs over 3 days. If BTC crashes back below $80K, the perp short profits enough to substantially offset the loss on the YES leg.

**Result:** Approximately $400 of the $500 max profit is locked in regardless of price path, with a residual ~$100 at risk to dispute/delay outcomes (which no price hedge can cover). For that residual, the trader could additionally lay off a portion on [[kalshi]] if a similar market exists, or simply sell into the Polymarket order book to exit entirely.

## Cost-Benefit Analysis

Hedging trades expected value for variance reduction. The decision rule is roughly:

> Hedge when: (P(adverse resolution event) x position size) > (hedging cost + foregone EV).

Hedging costs include perp funding, options premium, gas/fees on both venues, slippage on the hedge leg, and the EV given up by exiting the prediction market early. Dispute/delay tail risk on Polymarket is small per-market but non-zero and fat-tailed; for 5-figure positions and above it usually clears the bar.

## When NOT to Hedge

- **Small positions** — fees and slippage on the hedge leg exceed any plausible risk reduction.
- **No correlated tradable instrument** — election, sports, or geopolitical markets often have no clean hedge.
- **Binary outcome with no continuous proxy** — correlation hedging assumes a continuous underlying; it breaks down when the event is purely categorical.
- **Already short-dated and deep ITM** — the position will resolve before any hedge could meaningfully matter, and the order book exit is the cleaner alternative.
- **The hedge introduces worse risk** — e.g., shorting a thinly-traded perp on a venue with worse [[counterparty-risk]] than the prediction-market platform itself.

## Practical Considerations

- **Capital efficiency across venues** — Hedging requires posting margin on a second venue. Check that hedge capital is not levered against the same wallet/custodian as the primary position.
- **Settlement timing mismatch** — Perps settle continuously; prediction markets settle at a discrete point. Plan when to unwind the hedge so you do not hold uncovered exposure during the resolution window.
- **Basis risk** — The hedge instrument is rarely a perfect correlate. Spot vs perp vs index, different exchanges, funding-rate divergence — see [[basis-risk]].
- **Gas / fee costs** — On-chain hedges (perps on [[hyperliquid]], [[drift-protocol]]) involve transaction costs each leg. Bundle entry and exit; do not over-rebalance.
- **Dispute window awareness** — On Polymarket, the 2-hour UMA challenge window starts after the initial proposal. Maintain the hedge through the entire window plus a buffer for potential DVM escalation.
- **Tax treatment** — Hedges may be treated as separate transactions for tax purposes in some jurisdictions, which can offset the cleanliness of the locked-in PnL.

## See Also

- [[prediction-markets]]
- [[polymarket]]
- [[kalshi]]
- [[oracle-disputes]]
- [[uma]]
- [[prediction-market-strategies]]
- [[hedging]]
- [[basis-risk]]
- [[counterparty-risk]]
- [[arbitrage-opportunity-map]]

## Sources

- UMA Protocol documentation — Optimistic Oracle mechanics, the proposal/dispute liveness window, and Data Verification Mechanism (DVM) escalation (`docs.uma.xyz`). Confirms that disputed Polymarket outcomes escalate to a token-holder DVM vote; the fast-resolution liveness window is commonly cited at ~2 hours.
- Polymarket documentation / resolution rules — describes UMA-based settlement, the role of the resolution source per market, and the dispute/redemption flow (`docs.polymarket.com`).
- Kalshi rulebook and CFTC designated-contract-market filings — internal, CFTC-regulated settlement process, independent of any on-chain oracle, which is what makes a Kalshi/Polymarket cross-platform hedge a genuine [[counterparty-risk|counterparty-risk]] diversifier.
- Deribit, Hyperliquid, and dYdX/Drift product documentation — perp funding mechanics and options margining used in the correlated-instrument and collar hedges ([[deribit]], [[hyperliquid]], [[drift-protocol]]).
- General derivatives-hedging theory — the EV-for-variance trade and the [[basis-risk]] of an imperfect hedge are standard results in any options/futures hedging text (e.g., Hull, *Options, Futures, and Other Derivatives*, ch. on hedging strategies).
