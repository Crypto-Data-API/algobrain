---
title: "CryptoDataAPI"
type: source
created: 2026-07-13
updated: 2026-09-28
status: excellent
tags: [data-provider, crypto, api, derivatives, on-chain, market-regime, hyperliquid, backtesting, sentiment]
aliases: ["CryptoDataApi", "Crypto Data API", "cryptodataapi.com", "CDA"]
source_type: data
source_url: "https://cryptodataapi.com"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi-mcp]]", "[[cryptodataapi-market-data]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-hyperliquid-traders]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-indicators]]", "[[cryptodataapi-dex]]", "[[cryptodataapi-coins]]", "[[cryptodataapi-strategy-baskets]]", "[[cryptodataapi-strategy-library]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-nft]]", "[[cryptodataapi-news]]", "[[cryptodataapi-supply]]", "[[cryptodataapi-exchanges]]", "[[coinglass]]", "[[glassnode]]", "[[hyperliquid-api-and-sdk]]", "[[data-sources-overview]]"]
---

CryptoDataAPI ([cryptodataapi.com](https://cryptodataapi.com), Australia) is the **canonical data layer for this wiki**: a single REST API with 200+ endpoints spanning live crypto market data, derivatives positioning, Hyperliquid perp and trader intelligence, multi-family market-regime classification, on-chain flows, sentiment, news and catalyst detection, DEX/memecoin screening, NFTs, and a point-in-time backtesting archive going back to 2020. Where a wiki page describes data an endpoint serves, the page carries a **"Getting the Data (CryptoDataAPI)"** section with the live and historical access patterns.

## Access

- **Base URL**: `https://cryptodataapi.com`
- **Auth**: `X-API-Key` header on every request (create a key via `POST /api/v1/auth/keys`; rotate via `POST /api/v1/auth/keys/rotate`; delete via `DELETE /api/v1/auth/keys`). **Changed 2026-09-26:** rotate and delete now return `403` `oauth_token_cannot_manage_keys` when called with an **OAuth access token** (the short-lived delegated token an MCP client gets from browser login) — only the account's own `cdk_live_` key can manage keys. To end an OAuth connection use `POST /oauth/revoke` or Connected apps on the dashboard; OAuth token lifetime and redirect-URI rules are on [[cryptodataapi-mcp#OAuth connections]]
- **Effective limits**: `GET /api/v1/auth/keys/me` reports the calling key's *effective* limits (not the tier headline numbers) — fields include `per_minute_limit`, `email_verified`, and `verified_daily_limit`
- **Docs**: https://cryptodataapi.com/api/docs · OpenAPI JSON: https://cryptodataapi.com/api · changelog: https://cryptodataapi.com/changelog — same JSON as the public, key-free `GET /api/v1/changelog` (CalVer releases newest-first with a `breaking` flag; last 10 only) · status: https://cryptodataapi.com/status
- **MCP server**: hosted at `https://cryptodataapi.com/mcp` — AI agents connect via [[cryptodataapi-mcp]] (setup, free keys, agent loop, prompt library, live dashboards, backtest data availability)
- **Site surfaces**: live dashboards for every major data family (funding, OI, liquidations, whales, GEX, order books, regimes, market health, ETF flows, cycle indicators), a [50 meta-strategy catalog](https://cryptodataapi.com/trading-strategies), and a [14-prompt AI library](https://cryptodataapi.com/prompts) — wiki data sections deep-link the relevant views per page

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

### Plans & rate limits

| Tier | Requests | Burst | Unlocks |
|------|----------|-------|---------|
| Free | 1,000/day | 10/min | Core live endpoints |
| Pro | 10,000/day | 30/min | Per-coin quant matrices, trader profiles, copy signals, DEX promoted feed |
| Pro Plus | 50,000/day | 120/min | Point-in-time quant history, Parquet regime archive (2020+), whale history, refresh triggers |

Free was raised from 50/day + 5/min on 2026-08-20; Pro Plus burst was raised from 60/min to 120/min on 2026-08-22 — its daily cap is **50,000**, not unlimited, despite it being the top tier.

**Email verification unlocks the full free allowance.** A freshly created, unverified free key sits on a smaller starter allowance below the 1,000/day headline. Confirming the key's email address unlocks the full 1,000/day free tier **and** grants 24 hours of Pro-tier access as a trial. `POST /api/v1/auth/resend-verify` re-sends the confirmation link for the calling key's own address (10-minute cooldown between sends). The daily-quota `429` response for an unverified free key over its starter cap carries `upgrade_available: "verify_email"`, `upgrade_message`, and `verified_daily_limit` so an agent can detect and act on the gate programmatically. **Once per mailbox (changed 2026-09-26):** the 24h Pro trial and the `WELCOME` discount code are granted once per inbox — plus-addressed (`you+x@`) and Gmail dot variants of one address share the same grant, so minting extra keys on address variants does not re-trigger them.

**Consistent error envelope.** Every `401`/`403`/`429` on an `/api/*` path returns the same JSON shape — `{"detail": {"error": "<code>", "message": "<text>", ...}}` — never HTML or a bare string, so an agent can branch on `detail.error` instead of parsing prose. `403` tier refusals additionally carry `required_tier` (`"pro"`/`"pro_plus"`) and `pricing_url` as machine-readable fields (confirmed live: `{"detail":{"error":"pro_required","message":"...","required_tier":"pro","pricing_url":"https://cryptodataapi.com/pricing"}}`); `429`s carry a `scope` field (`"api_key"`) and, per CryptoDataAPI's own rate-limit documentation, a `Retry-After` header plus the full `X-RateLimit-*` set for backoff. Both `403` and `429` bodies also nest a machine-readable `upgrade` object (live-confirmed on both) whose fields now include `passes` (the six x402 time-boxed plans), `pay_per_request` (the six keyless-402 endpoints), and `pricing_api` (`https://cryptodataapi.com/api/v1/pricing`) alongside the existing subscription pricing — see [[cryptodataapi-mcp]]'s x402 section for the full three-rail payment detail.

### Billing & wallet payments

Subscriptions can be bought by card (`POST /api/v1/payments/stripe/checkout`), over x402 (see [[cryptodataapi-mcp#x402 gasless payments: three rails]]), or by a direct USDC transfer from a connected wallet (`/api/v1/wallet/*`). Changes in the 2026-09-26 release:

- **Card billing** — a card subscription is granted only once payment has **settled** (delayed payment methods activate when they clear, not at checkout). A chargeback or **full** refund cancels the subscription and ends paid access immediately; partial refunds do not change access. Checkout sessions that use a discount code expire after 60 minutes, and a limited-use code cannot be held by more open checkouts than it has uses left.
- **Wallet sign-in is SIWE (breaking).** `POST /api/v1/wallet/challenge` (request: `wallet_address`, optional new `chain_id` — `1` Ethereum or `8453` Base) now returns a Sign-In with Ethereum ([EIP-4361](https://eips.ethereum.org/EIPS/eip-4361)) `message` bound to cryptodataapi.com, the `nonce`, and a new `expires_at` (5-minute expiry). Sign `message` **exactly as returned**. `POST /api/v1/wallet/verify` (`wallet_address`, `signature`, `nonce`, optional `message` — which must match exactly if sent) checks the signature against the challenge the server issued; expired, reused, or altered messages are rejected.
- **Solana/Tron payments need the exact amount (breaking).** `POST /api/v1/wallet/create-solana-tx` and `POST /api/v1/wallet/create-tron-intent` (request: `sender`, `plan`, optional `discount_code`) now return `amount` / `amount_raw` — the plan price plus a unique sub-cent tag — and `expires_in`. Send **exactly** that amount: claims require an exact match, so a rounded or larger transfer no longer matches automatically (contact support with the transaction hash; funds are not lost). Limits: one open request per sending wallet across all accounts (`409`), at most 3 open requests per key (`429`), and the plan and discount code at settlement must match the request.

## Category map

| Category | Page | What it covers |
|----------|------|----------------|
| Coins | [[cryptodataapi-coins]] | 500+ aggregated asset profiles, search, categories, top-N |
| Market Data | [[cryptodataapi-market-data]] | Binance spot klines/tickers, BTC price history + 200D MA, volume, daily bulk snapshots |
| Derivatives | [[cryptodataapi-derivatives]] | Funding rates, open interest, long/short ratio — Binance + cross-exchange |
| Hyperliquid | [[cryptodataapi-hyperliquid]] | Perp prices, funding, OI, OHLCV candles, L2 order book |
| Hyperliquid Traders | [[cryptodataapi-hyperliquid-traders]] | Leaderboard, wallet positions/signals, trader profiles, copy-trading signals, watchlists |
| Market & Quant Regimes | [[cryptodataapi-regimes]] | 10-state market regimes, HMM quant probabilities (6 regimes), volatility/liquidity/meme/event/security/policy regimes |
| Market Intelligence | [[cryptodataapi-market-intelligence]] | BTC cycle indicators, ETF flows, liquidations, options max-pain, exchange balance, Coinbase premium, taker buy/sell, squeeze alerts |
| News & Catalysts | [[cryptodataapi-news]] | Per-coin news pressure/tilt, filtered market-moving catalyst tape, crypto-native and policy/macro categories, feed health, backtestable catalyst archive |
| On-Chain | [[cryptodataapi-on-chain]] | Stablecoin reserves & dry powder, exchange flows, miner reserves, hash ribbon, MVRV dormancy, whale scores |
| Sentiment & Macro | [[cryptodataapi-sentiment]] | Fear & Greed, stablecoin supply/flows, macro (EUR/USD, gold, yields) |
| Market Health | [[cryptodataapi-market-health]] | Dual-score market health (11 components), altcoin breadth |
| Indicators | [[cryptodataapi-indicators]] | Signum RGG (ADX/DMI), technical price-structure state (SMA/BB/RSI) |
| Supply | [[cryptodataapi-supply]] | Circulating float, dilution overhang, forward token-unlock cliff calendar |
| Exchanges | [[cryptodataapi-exchanges]] | Public venue directory (CEX/DEX/Broker profiles, specs, referral sign-up links) |
| DEX & Memecoins | [[cryptodataapi-dex]] | Trending pools, new launches, token security/rug reports, promotion-spend signal |
| Strategy Baskets | [[cryptodataapi-strategy-baskets]] | 50 meta-baskets across 6 thematic groups |
| Strategy Library | [[cryptodataapi-strategy-library]] | 317-strategy library in 22 groups (`/strategies`), 187-indicator catalogue in 12 groups (`/indicators/catalog`), hosted AlgoBrain wiki search (`/algobrain/search`, `/page`, `/stats`) — all tiers incl. Free |
| Backtesting | [[cryptodataapi-backtesting]] | Historical klines/funding/liquidations, point-in-time daily snapshots, Parquet archives since 2020 |
| NFTs | [[cryptodataapi-nft]] | Market overview, collections, volume, correlations |
| MCP / AI Agents | [[cryptodataapi-mcp]] | Hosted MCP server, agent workflow loop, x402 payments, backtest data availability |

## Why it is the wiki's canonical layer

- **Live + historical in one surface** — most signal families expose both a current endpoint and a history/backtesting endpoint, so strategy pages can cite one provider for research and production
- **Regime-native** — the regime endpoints map directly onto this wiki's [[crypto-market-regime-taxonomy|14-basket regime taxonomy]] and [[regime-strategy-playbook]]
- **Point-in-time discipline** — the [[cryptodataapi-backtesting|backtesting archive]] provides dated snapshots and Parquet downloads, addressing [[lookahead-bias]] and [[point-in-time-data]] requirements
- **Webhooks** — `GET/POST /api/v1/webhooks` (plus `PATCH`/`DELETE /api/v1/webhooks/{label}`) for push-based alerting into trading systems. **Limits (changed 2026-09-26):** each API key may own at most **2** webhook endpoints on Free and **10** on Pro / Pro Plus; creating one past that returns `403` `webhook_limit_reached` with `limit`, `current`, and `tier` (existing endpoints are unaffected). Fields are length-limited — `label` 1-100 chars, `secret` 1-255, up to 200 `addresses` of at most 128 chars each, up to 10 `events` of at most 32 chars each — and over-limit values return `422`

## Related

- [[coinglass]] — browser-first derivatives aggregator; CryptoDataAPI is the API-first counterpart
- [[glassnode]], [[cryptoquant]] — on-chain analytics alternatives
- [[hyperliquid-api-and-sdk]] — trading (order placement) on Hyperliquid; CryptoDataAPI covers the intelligence layer
- [[data-sources-overview]]

## Sources

- CryptoDataAPI changelog release 2026-09-26 (breaking; via `GET /api/v1/changelog`, fetched 2026-09-28) and the live OpenAPI spec (`ChallengeRequest`/`ChallengeResponse`/`VerifyRequest`, `SolanaTxRequest`/`TronIntentRequest`, `WebhookCreate` length limits, `/strategies`, `/indicators/catalog`, `/algobrain/*`; fetched 2026-09-28) — OAuth key-management refusal, wallet SIWE, exact-amount Solana/Tron payments, webhook limits, billing and trial changes
- https://cryptodataapi.com/api (live OpenAPI JSON) and live curl tests of 403/429 `upgrade` object fields (fetched 2026-09-08)
- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
