---
title: "Coinbase Prime"
type: entity
created: 2026-05-16
updated: 2026-06-10
status: good
tags: [company, crypto, exchange, regulation]
aliases: ["Coinbase Prime", "Coinbase Institutional", "Prime Brokerage (Coinbase)"]
entity_type: company
founded: 2021
headquarters: "San Francisco, California, USA"
website: "https://prime.coinbase.com"
related: ["[[coinbase]]", "[[crypto-weekday-weekend-etf-era]]", "[[crypto-trading-sessions]]", "[[cme-bitcoin-futures]]", "[[whale-alert]]", "[[arkham-intelligence]]", "[[bitcoin-etfs]]"]
---

Coinbase Prime is the institutional prime brokerage and custody arm of [[coinbase|Coinbase]], offering integrated custody, execution, financing, and OTC services to large crypto holders. It is the primary custodian for the majority of US spot Bitcoin ETFs, which puts it at the center of the ETF-era restructuring of intraday crypto liquidity (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## What It Does

Coinbase Prime bundles the services a large institutional crypto holder needs into a single platform:

- **Custody** — qualified custodian holding spot crypto for funds, ETF issuers, corporate treasuries, and other institutions
- **Prime brokerage** — unified margin and credit across cash, spot, and (where available) derivatives
- **Execution** — smart order routing across exchanges, with algos for VWAP/TWAP-style execution
- **OTC desk** — block trading away from exchange order books to minimize market impact
- **Financing** — borrowing/lending against crypto collateral

The platform is targeted at hedge funds, asset managers, corporate treasuries, and other institutions that need bank-grade controls, qualified-custodian status, and a single counterparty for both holding and trading crypto (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## Role in ETF-Era Liquidity

Coinbase Prime is the custodian of choice for most US spot Bitcoin ETFs. The Perplexity-sourced gap-analysis describes Coinbase Prime as holding custody for a "double-digit share of global crypto market cap," with the precise number not stated — interpret the language as load-bearing rather than the implied magnitude (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

Because ETF creation and redemption flows route through Prime, those flows are concentrated in US trading hours when the underlying ETFs are open for primary-market activity. This is one of the major mechanical drivers of the weekday/US-session liquidity skew documented in [[crypto-weekday-weekend-etf-era]]:

- ETF creations require Authorized Participants to deliver cash (or coin) into the custodian during US business hours
- Redemptions reverse the flow, again gated to US hours
- Market makers hedge primary-market activity on exchanges, pulling exchange volume into the same window

The net effect is that Coinbase Prime's operating hours partially define when global crypto liquidity is deepest, even though spot exchanges themselves trade 24/7.

## 2025–2026 Developments

- **Custody scale quantified**: Coinbase reported roughly **$300 billion in assets under custody**, with spot Bitcoin and Ethereum ETFs the main growth driver. As of Q3 2025 reporting, Coinbase served as primary custodian for **over 80% of US Bitcoin and Ethereum ETF assets** (~84% of spot Bitcoin ETF assets per market analyses), including BlackRock's IBIT and ARK 21Shares' ARKB — confirming and sharpening the earlier "double-digit share" language below.
- **Deribit acquisition closed (2025-08-14)**: parent [[coinbase|Coinbase]] completed its **$2.9B acquisition of Deribit** (~$700M cash + 11M shares), the dominant offshore crypto options venue (July 2025 volumes >$185B, ~$60B open interest). This folds the deepest crypto options liquidity pool into the same institutional stack as Prime, extending Coinbase's reach from custody/spot execution into global derivatives.
- **Concentration debate**: the >80% ETF custody share has drawn explicit "choke point" / single-custodian systemic-risk commentary from analysts and ETF issuers, reinforcing the custody-concentration risk noted below; some issuers have begun adding or naming backup custodians.

## Why It Matters for Intraday Traders

For traders watching intraday flow, Coinbase Prime wallets are a high-signal flow source:

- **ETF flow leading indicator** — large transfers tagged to known Coinbase Prime wallets (visible via [[arkham-intelligence]] or [[whale-alert]]) can presage US-session ETF creation/redemption activity
- **Custody concentration risk** — because so much institutional spot BTC is custodied at Prime, operational or regulatory events affecting Coinbase have outsized systemic implications for the spot market
- **Session anchoring** — Prime's US-hours operational rhythm reinforces the [[crypto-trading-sessions|Asia/London/NY session]] structure even in a 24/7 market

For traders running [[session-overlap-momentum]] or other US-session strategies, on-chain Prime flows are part of the broader weekday/US-hours setup, alongside [[cme-bitcoin-futures]] basis and stablecoin issuance.

## Related

- [[coinbase]] — parent exchange and retail-facing platform
- [[crypto-weekday-weekend-etf-era]] — the structural shift Prime helps anchor
- [[crypto-trading-sessions]] — Asia/London/NY hub
- [[cme-bitcoin-futures]] — the regulated US derivatives anchor that hedges ETF flow
- [[whale-alert]] — real-time alerts on large on-chain transfers including Prime wallets
- [[arkham-intelligence]] — entity-labeled wallet attribution
- [[bitcoin-etfs]] — the products Prime custodies

## Sources

- [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]
- https://www.theblock.co/post/366957/coinbase-completes-2-9-billion-cash-and-stock-acquisition-of-deribit — Deribit deal close, 2025-08-14
- https://investor.coinbase.com/news/news-details/2025/Deribit-Joins-Coinbase-Unlocking-the-Future-of-Global-Crypto-Derivatives/default.aspx
- https://cryptorank.io/news/feed/7fecc-over-80-of-bitcoin-etf-assets-hit-coinbase-custody-choke-point-with-74b-at-risk — ETF custody concentration
- Verified via web search, 2026-06-10
