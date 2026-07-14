---
title: "Cash-Secured Put"
type: strategy
created: 2026-04-07
updated: 2026-07-14
status: good
tags: [options, crypto, premium-selling, derivatives]
aliases: ["Cash Secured Put", "Crypto Cash-Secured Put"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[cash-secured-puts]]", "[[covered-call]]", "[[wheel-strategy]]", "[[crypto-options-volatility-selling]]", "[[put-option]]", "[[deribit]]"]
---

# Cash-Secured Put

> **This page has been merged into the canonical [[cash-secured-puts]].**
> The two pages ("cash-secured-put" and "cash-secured-puts") described the same structure; the content has been consolidated and re-scoped to crypto ([[deribit]] BTC/ETH puts, USDC-secured) on **[[cash-secured-puts]]**. Existing `[[cash-secured-put]]` links continue to resolve here and this note points onward.

A **cash-secured put** sells a [[put-option]] on [[bitcoin]] or [[ethereum]] while reserving USDC collateral to acquire the coin at the strike if the option settles in-the-money — "getting paid to place a limit buy order" on the coin. It is the single-leg, fully-collateralised end of [[crypto-options-volatility-selling|crypto vol selling]] and the entry leg of the crypto [[wheel-strategy|wheel]].

For the full treatment — construction, payoff and breakevens, Greeks profile, when to use, adjustments, **crypto specifics** (Deribit cash settlement with no automatic coin assignment, USDC-secured vs coin-margined collateral, [[dvol|DVOL]]/put skew, 24/7 & weekend gap risk, no [[section-1256-contracts|§1256]], perp-funding skew, DeFi put-selling vaults), the worked crypto example, and the CryptoDataAPI endpoints — see:

## → [[cash-secured-puts]]

## Related

- [[cash-secured-puts]] — the canonical page (full crypto structure treatment)
- [[covered-call]] — the wheel's second leg (sell calls against acquired coin)
- [[wheel-strategy]] — the full crypto put-call income cycle
- [[crypto-options-volatility-selling]] — the systematic short-vol book this structure sits inside
- [[deribit]] — the venue
