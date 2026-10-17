---
title: "CryptoDataAPI"
type: source
created: 2026-07-13
updated: 2026-10-17
status: excellent
tags: [data-provider, crypto, api, derivatives, on-chain, market-regime, hyperliquid, backtesting, sentiment]
aliases: ["CryptoDataApi", "Crypto Data API", "cryptodataapi.com", "CDA"]
source_type: data
source_url: "https://cryptodataapi.com"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi-mcp]]", "[[cryptodataapi-market-data]]", "[[cryptodataapi-derivatives]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-hyperliquid-traders]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-indicators]]", "[[cryptodataapi-dex]]", "[[cryptodataapi-coins]]", "[[cryptodataapi-strategy-baskets]]", "[[cryptodataapi-strategy-library]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-nft]]", "[[cryptodataapi-news]]", "[[cryptodataapi-supply]]", "[[cryptodataapi-exchanges]]", "[[coinglass]]", "[[glassnode]]", "[[hyperliquid-api-and-sdk]]", "[[data-sources-overview]]"]
---

CryptoDataAPI ([cryptodataapi.com](https://cryptodataapi.com), Australia) is the **canonical data layer for this wiki**: a single REST API with 220+ endpoints (226 paths in the live OpenAPI spec on 2026-10-17) spanning live crypto market data, derivatives positioning, Hyperliquid perp and trader intelligence, multi-family market-regime classification, on-chain flows, sentiment, news and catalyst detection, DEX/memecoin screening, NFTs, and a point-in-time backtesting archive going back to 2020. Where a wiki page describes data an endpoint serves, the page carries a **"Getting the Data (CryptoDataAPI)"** section with the live and historical access patterns.

## Access

- **Base URL**: `https://cryptodataapi.com`
- **Auth**: `X-API-Key` header on every request (create a key via `POST /api/v1/auth/keys`; rotate via `POST /api/v1/auth/keys/rotate`; delete via `DELETE /api/v1/auth/keys`). **Changed 2026-09-26:** rotate and delete now return `403` `oauth_token_cannot_manage_keys` when called with an **OAuth access token** (the short-lived delegated token an MCP client gets from browser login) — only the account's own `cdk_live_` key can manage keys. To end an OAuth connection use `POST /oauth/revoke` or Connected apps on the dashboard; OAuth token lifetime and redirect-URI rules are on [[cryptodataapi-mcp#OAuth connections]]
- **Effective limits**: `GET /api/v1/auth/keys/me` reports the calling key's *effective* limits (not the tier headline numbers) — fields include `per_minute_limit`, `email_verified`, and `verified_daily_limit`
- **Docs**: https://cryptodataapi.com/api/docs · OpenAPI JSON: https://cryptodataapi.com/api · changelog: https://cryptodataapi.com/changelog — same JSON as the public, key-free `GET /api/v1/changelog` (CalVer releases newest-first with a `breaking` flag; a bounded window, not the full history. It served the last 10 releases when first documented, and 36 releases back to 2026-06-27 on 2026-10-17) · status: https://cryptodataapi.com/status
- **OpenAPI spec for agents (2026-10-09, 2026-10-14)**: the spec at `/api/openapi.json` gives every required path and query parameter an `example` that answers 200 for a Pro Plus key, so a working call can be built for every operation from the spec alone. Date examples are relative (two days ago). A few optional parameters carry one too, where the bare call would 400 or is far heavier than needed: `coins` on `/hyperliquid/candles/batch`, `data_type=daily` on `/backtesting/archives` and `/archives/download`, and the daily-bundle fields on `/archives/purchase`. Operation extensions:
  - `x-timeout-seconds`: the longest the operation can take. It was on 19 operations on 2026-10-17, with values of 20-90 s. Operations without it answer within 10 s once warm.
  - `x-streaming`: on `/stream`, whose response never completes.

  **Live event stream: observed limits (2026-10-17).** `GET /api/v1/stream` (SSE, Pro and Pro Plus, up to 3 concurrent streams per key) pushes liquidations, whale transfers, whale positions, funding, OI and price moves. `/stream/recent` (JSON, any key, newest 1-500 events with `last_id`) and the keyless `/stream/delayed` preview serve the same events. Two measurements differ from the spec, which still says what is shown here:
  - **Replay buffer.** The spec says `since_id` replays a "~2h ring". A `since_id=1` replay at 06:13 UTC on 2026-10-17 began about 14 minutes back. Re-measured at 11:09-11:10 UTC the same day, `since_id=1`, a `since_id` 30 minutes back and one 120 minutes back each replayed about 450-500 events, starting 4.8-5.9 minutes back. The first replayed id equalled the first id of a 500-event `/stream/recent` pull, which spanned 3.9 minutes. The buffer behaved like a cap of about 500 events, not a 2-hour window, so its reach in time shrinks as the event rate rises (about 100 events a minute at the second test). After a disconnect longer than a few minutes, expect a gap.
  - **Delayed preview window.** The spec says `/stream/delayed` serves "a 5-minute window that ended 30 minutes ago". Live on 2026-10-17 `window_end - window_start` was 180 s (3 minutes), with 229 events at 76.3 per minute, and the window ended 30.0 minutes before `server_now`. The 2026-09-28 changelog narrowed it from a 5-minute window of at most 300 events to a 3-minute window of at most 900; the spec text was not updated. (The same release note still describes the replay buffer as "~2h".)
  - `x-account-scoped`: the resource belongs to one caller. The changelog says the invoice and payment-signature routes carry it; on 2026-10-17 the spec put it on `/payments/invoices/{number}` and `/wallet/invoices/{number}` only.

  Since 2026-10-14 the spec is served with `Cache-Control: public, max-age=300` (previously `private, max-age=60`), so shared caches may hold it for up to 5 minutes. A fetch on 2026-10-17 came back `public, max-age=150`. Every other `/api/` response stays `private`.
- **Strict query parameters (2026-10-10, breaking for some callers)**: these routes now return `400 unknown_parameter` for a query parameter they do not read, instead of silently ignoring it:
  - `/indicators/technical`, `/indicators/signum-rgg` ([[cryptodataapi-indicators]])
  - `/algobrain/search`, `/algobrain/page` ([[cryptodataapi-strategy-library]])
  - `/backtesting/klines` ([[cryptodataapi-backtesting]])
  - `/quant/gex`, `/quant/gex/history`, `/quant/positioning`, `/quant/positioning/ladder` ([[cryptodataapi-regimes]])
  - `/supply/unlocks` ([[cryptodataapi-supply]])

  The body is `{"detail": {"error": "unknown_parameter", "message", "unknown": [...], "accepted": [...]}}`. Some messages point to the right parameter or route: `interval` on `/indicators/technical` points to `/indicators/adx`, and `days` on `/quant/gex/history` points to `from` / `to`. The silent-ignore behaviour had been returning wrong data. For example, `/indicators/technical?coin=BTC&interval=4h` returned the whole daily universe, and `/quant/gex?coin=X` returned every coin. A 404 on a guessed indicator path such as `/indicators/rsi` now carries a `hint` naming the route and field that serve it.
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

**Email verification unlocks the full free allowance.** A freshly created, unverified free key sits on a smaller starter allowance below the 1,000/day headline. Confirming the key's email address unlocks the full 1,000/day free tier **and** grants 24 hours of Pro-tier access as a trial. `POST /api/v1/auth/resend-verify` re-sends the confirmation link for the calling key's own address (10-minute cooldown between sends). The daily-quota `429` response for an unverified free key over its starter cap carries `upgrade_available: "verify_email"`, `upgrade_message`, and `verified_daily_limit` so an agent can detect and act on the gate programmatically. **Once per mailbox (changed 2026-09-26):** the 24h Pro trial and the `WELCOME` discount code (see the 2026-10-02 note below on discount codes) are granted once per inbox — plus-addressed (`you+x@`) and Gmail dot variants of one address share the same grant, so minting extra keys on address variants does not re-trigger them.

**Key minting is limited (breaking, 2026-10-02).** `POST /api/v1/auth/keys` mints **one key per network per day** (it was 3). A second attempt returns `429 ip_rate_limit` with `Retry-After: 86400`. It also allows **one active key per mailbox**: `name+tag@` aliases and Gmail dot variants of an address that already holds a key get `409 mailbox_already_registered` instead of a new key. **Keys never expire.** Reuse your key, or sign in to rotate it. This breaks any client that minted a fresh key per run.

**No discount code in `upgrade` blocks (breaking, 2026-10-02).** `upgrade.discount` was removed from every tier `403` and per-key `429` body. It was also removed from the edge-served 403s on `/quant/gex`, `/quant/positioning` and `/hyperliquid/*`, from the key-mint `limits.upgrade` block, and from the MCP server's tier copy. The field is absent now, not null, and the API no longer quotes any discount code. The rest of `upgrade` is unchanged: `pricing_url`, `why_subscribe`, `pro`, `pro_plus`, and `agent_subscribe` when the x402 rail is live. Codes you already hold still redeem at card or crypto checkout on the dashboard, and are still never accepted over x402. (`discount_code` is still an optional field on the Solana/Tron payment requests below, per the 2026-10-17 spec.) The changelog does not say whether email verification still grants the `WELCOME` code mentioned above.

**Consistent error envelope.** Every `401`/`403`/`429` on an `/api/*` path returns the same JSON shape — `{"detail": {"error": "<code>", "message": "<text>", ...}}` — never HTML or a bare string, so an agent can branch on `detail.error` instead of parsing prose. `403` tier refusals additionally carry `required_tier` (`"pro"`/`"pro_plus"`) and `pricing_url` as machine-readable fields (confirmed live: `{"detail":{"error":"pro_required","message":"...","required_tier":"pro","pricing_url":"https://cryptodataapi.com/pricing"}}`); `429`s carry a `scope` field (`"api_key"`) and, per CryptoDataAPI's own rate-limit documentation, a `Retry-After` header plus the full `X-RateLimit-*` set for backoff. Both `403` and `429` bodies also nest a machine-readable `upgrade` object (live-confirmed on both) whose fields now include `passes` (the six x402 time-boxed plans), `pay_per_request` (the six keyless-402 endpoints), and `pricing_api` (`https://cryptodataapi.com/api/v1/pricing`) alongside the existing subscription pricing — see [[cryptodataapi-mcp]]'s x402 section for the full three-rail payment detail.

### Billing & wallet payments

Subscriptions can be bought by card (`POST /api/v1/payments/stripe/checkout`), over x402 (see [[cryptodataapi-mcp#x402 gasless payments: three rails]]), or by a direct USDC transfer from a connected wallet (`/api/v1/wallet/*`). Changes in the 2026-09-26 release:

- **Card billing** — a card subscription is granted only once payment has **settled** (delayed payment methods activate when they clear, not at checkout). A chargeback or **full** refund cancels the subscription and ends paid access immediately; partial refunds do not change access. Checkout sessions that use a discount code expire after 60 minutes, and a limited-use code cannot be held by more open checkouts than it has uses left.
- **Wallet sign-in is SIWE (breaking).** `POST /api/v1/wallet/challenge` (request: `wallet_address`, optional new `chain_id` — `1` Ethereum or `8453` Base) now returns a Sign-In with Ethereum ([EIP-4361](https://eips.ethereum.org/EIPS/eip-4361)) `message` bound to cryptodataapi.com, the `nonce`, and a new `expires_at` (5-minute expiry). Sign `message` **exactly as returned**. `POST /api/v1/wallet/verify` (`wallet_address`, `signature`, `nonce`, optional `message` — which must match exactly if sent) checks the signature against the challenge the server issued; expired, reused, or altered messages are rejected.
- **Solana/Tron payments need the exact amount (breaking).** `POST /api/v1/wallet/create-solana-tx` and `POST /api/v1/wallet/create-tron-intent` (request: `sender`, `plan`, optional `discount_code`) now return `amount` / `amount_raw` — the plan price plus a unique sub-cent tag — and `expires_in`. Send **exactly** that amount: claims require an exact match, so a rounded or larger transfer no longer matches automatically (contact support with the transaction hash; funds are not lost). Limits: one open request per sending wallet across all accounts (`409`), at most 3 open requests per key (`429`), and the plan and discount code at settlement must match the request.

**Solana payment changes (2026-10-14).**
- **Removed (breaking):** ~~`GET /api/v1/wallet/solana-blockhash`~~ and ~~`GET /api/v1/wallet/solana-confirm/{signature}`~~ now return 404 (confirmed live 2026-10-17). Both were keyless passthroughs to a public Solana node, and the checkout never used them. To pay in Solana USDC, `POST /wallet/create-solana-tx` returns the transaction with a fresh blockhash already in it, and `POST /wallet/upgrade` with `network: "solana"` verifies the transfer.
- **`POST /wallet/upgrade` on Solana** now falls back to a second node when the first fails or does not have the transaction. When no Solana node can be reached it returns **`503` with `Retry-After: 30`** (it was 502). A rate-limited node no longer produces a `400 "Transaction not found"` for a payment that landed. A 400 now means no reachable node has the transaction. Base and Ethereum already worked this way. Treat a 503 as "retry after 30 s", not as a failed payment.

**Partner gateways (2026-10-09).** A key registered as a reseller gateway, on a request carrying that gateway's marker header, is limited by a gateway profile: 600/min and no daily cap. No other key's limits or 429 bodies change.

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

- Live `/stream` replays with `since_id` (06:13 UTC and 11:09-11:10 UTC), a 500-event `/stream/recent` pull, a `/stream/delayed` call, the `/stream*` spec descriptions, and the 2026-09-28 changelog release (all 2026-10-17)
- CryptoDataAPI changelog releases 2026-10-02, 2026-10-09, 2026-10-10 and 2026-10-14 (via `GET /api/v1/changelog`, fetched 2026-10-17; the feed then held 36 releases back to 2026-06-27), the live OpenAPI spec (226 paths; `x-timeout-seconds`/`x-streaming`/`x-account-scoped` extensions, 60 parameter `example`s, `SolanaTxRequest`/`TronIntentRequest` still carrying `discount_code`; fetched 2026-10-17), the `/api/openapi.json` response headers, and live 404s on `/wallet/solana-blockhash` and `/wallet/solana-confirm/{signature}` (2026-10-17)
- CryptoDataAPI changelog release 2026-09-26 (breaking; via `GET /api/v1/changelog`, fetched 2026-09-28) and the live OpenAPI spec (`ChallengeRequest`/`ChallengeResponse`/`VerifyRequest`, `SolanaTxRequest`/`TronIntentRequest`, `WebhookCreate` length limits, `/strategies`, `/indicators/catalog`, `/algobrain/*`; fetched 2026-09-28) — OAuth key-management refusal, wallet SIWE, exact-amount Solana/Tron payments, webhook limits, billing and trial changes
- https://cryptodataapi.com/api (live OpenAPI JSON) and live curl tests of 403/429 `upgrade` object fields (fetched 2026-09-08)
- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
