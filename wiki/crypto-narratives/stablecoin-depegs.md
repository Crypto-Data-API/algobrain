---
title: "Stablecoin Depegs & Contagion — Narrative Impact"
type: concept
created: 2026-06-04
updated: 2026-07-13
status: good
tags: [crypto, defi, event-driven, market-regime, liquidity, market-microstructure, behavioral-finance, narrative-impact]
aliases: ["Depeg", "Stablecoin Depeg", "Depeg Contagion", "Stablecoin Run", "USDe Depeg", "Algorithmic Stablecoin Collapse"]
related: ["[[crypto-narratives-overview]]", "[[stablecoin-supply]]", "[[stablecoin-depeg-history]]", "[[cryptodataapi]]"]
domain: [market-microstructure, behavioral-finance]
difficulty: intermediate
---

Stablecoins are crypto tokens engineered to hold a steady $1 value. When one "depegs" (trades meaningfully below $1) it signals that holders no longer trust the backing and rush to redeem or sell, and depending on the design that rush either self-corrects or spirals to zero. Depegs are reliably bearish for the affected coin and frequently contagious — the canonical case (Terra, May 2022) cascaded into lending desks and exchanges and helped erase hundreds of billions across the market.

> **2026 regime context — the risk moved from algo pegs to yield-bearing DeFi and exploits.** With the algorithmic-stablecoin model discredited after Terra, the live 2025-26 depeg risk concentrated in two newer vectors: (1) **yield-bearing "synthetic" stablecoins** (Ethena's USDe, Stream's xUSD, Elixir's deUSD), where the Nov-2025 Stream/Elixir contagion took deUSD to ~$0.015 and exposed how opaque off-chain yield strategies can vaporise backing; and (2) **infrastructure exploits** rather than reserve doubt — the Mar-2026 Resolv USR collapse (-80%) came from an AWS-KMS key compromise minting $80M of unbacked tokens, not a bank run. The cleanest tradable distinction remains intact: *fiat-backed reserve shocks recover* (USDC repegged in ~3 days after SVB) and *venue flash-wicks are arbitrage gifts* (USDe printed $0.65 on Binance in Oct-2025 while staying at par on-chain), whereas *algo death-spirals and destroyed-backing exploits are terminal*. The aggregate stablecoin float (~$322B by May 2026) means a major-issuer depeg is now a systemic, not niche, event.

## How it moves price

A depeg is a confidence event expressed as a price discount. The discount equals the market's probability-weighted haircut on the reserves (or, for algorithmic coins, on the entire mechanism). Three repeatable shapes drive the price action, and they have opposite payoffs for the trader on the other side:

- **Algorithmic death spirals** have no hard reserves; once the peg cracks, the redemption mechanism hyperinflates a sister token and the whole thing goes terminal. The other side is late yield-farmers who hold into the spiral and lose ~100%.
- **Reserve-shock depegs** hit collateralized coins when the market doubts the reserves are redeemable. The other side is arbitrageurs buying the discount betting 1:1 redemption resumes — they win when backing is real (USDC recovered in ~3 days) and lose when it is genuinely gone (USDR ~half permanent). A key read-across: when the trigger is TradFi banking stress (SVB), BTC *rallies* as a banking-system hedge.
- **Venue-liquidity flash wicks** are mechanical dislocations on a single exchange or imbalanced AMM pool while the coin stays at par everywhere else. The other side is fast arbitrageurs who buy the wick and redeem elsewhere — they almost always win, because the discount is not fundamental.

## Algorithmic / reflexive death-spiral depeg

**Mechanism.** An uncollateralized or under-collateralized stablecoin maintains its peg via an arbitrage loop that mints/burns a sister governance/seigniorage token (LUNA for UST, TITAN for IRON, xUSD/deUSD backing). When the peg breaks, arbitrageurs redeem the stablecoin for newly-minted sister tokens and dump them, crashing the sister token, which forces even more minting to absorb redemptions — a reflexive doom loop. The other side is late holders and yield farmers (e.g. Anchor's ~20% APY depositors) who keep holding into the spiral; they lose ~100% because there are no real reserves and supply hyperinflates. There is no natural floor, so these go terminal rather than recover.

- **Directional bias:** bearish
- **Typical magnitude:** -50% to -100% on the stablecoin; -95% to -100% on the sister token
- **Typical lag:** immediate to hours once the peg cracks; full collapse over 1-7 days
- **Typical duration:** terminal — days to a week to reach near-zero; no recovery
- **Recurrence:** recurring; ~once every 6-18 months a notable algo design fails (2021 IRON, 2022 UST/USDD, 2025 xUSD/deUSD)
- **Affected scope:** the named stablecoin, its sister/governance token, DeFi lending, large-cap alts, BTC, total-market-cap
- **Leading signals:** unsustainably high fixed yield (Anchor 19.5%, IRON farms hundreds of percent); large single-address withdrawals from the anchor pool/farm; Curve/AMM pool tilting heavily to the stablecoin side; stablecoin trading 0.98-0.99 persistently before the break; concentration of backing in one risky counterparty (Stream Finance); sister-token price rolling over while the stablecoin is still ~pegged

| Date | Event | Asset | Impact | Window | Confidence | Source |
|------|-------|-------|--------|--------|------------|--------|
| 2022-05-09 | Terra UST/LUNA collapse | UST | -98% | 7d, low ~$0.02 by May 13 | high | [Harvard CorpGov](https://corpgov.law.harvard.edu/2023/05/22/anatomy-of-a-run-the-terra-luna-crash/) |
| 2022-05-09 | Terra UST/LUNA collapse | LUNA | -99.99% | 7d, to ~$0 by May 13 | high | [Wikipedia](https://en.wikipedia.org/wiki/Terra_(blockchain)) |
| 2022-05-09 | Terra UST/LUNA collapse | BTC | -33% | May 5 ~$38k to May 12 low ~$25.4k-26.7k | high | [Riksbank](https://www.riksbank.se/globalassets/media/konferenser/2023/session-1-liu_makarov_schoar-anatomy_of_a_run-_the_terra_luna_crash.pdf) |
| 2022-05-09 | Terra UST/LUNA collapse | ETH | -35% | to May 12 low ~$1,700 | high | [Harvard CorpGov](https://corpgov.law.harvard.edu/2023/05/22/anatomy-of-a-run-the-terra-luna-crash/) |
| 2021-06-16 | IRON Finance / TITAN collapse | TITAN | -100% | 24h, ~$60-65 to ~$0 | high | [Fed Reserve note](https://www.federalreserve.gov/econres/notes/feds-notes/runs-on-algorithmic-stablecoins-evidence-from-iron-titan-and-steel-20220602.html) |
| 2021-06-16 | IRON Finance / TITAN collapse | IRON | -25% | intraday low below $0.75 | high | [CoinDesk](https://www.coindesk.com/markets/2021/06/17/in-token-crash-postmortem-iron-finance-says-it-suffered-cryptos-first-large-scale-bank-run) |
| 2022-06-13 | USDD (Tron) algo depeg | USDD | -9% | intraday low ~$0.91 | medium | [Fortune](https://fortune.com/2022/06/13/algorithmic-stablecoin-usdd-loses-peg-justin-sun-tron-decentralized-usd/) |
| 2022-06-13 | USDD (Tron) algo depeg | TRX | -16% | during depeg | medium | [U.Today](https://u.today/tron-dao-attacked-usdd-depeg-causes-16-trx-collapse-justin-sun-ready-to-cash-in-2-billion-to-fight) |
| 2025-11-04 | Stream xUSD / Elixir deUSD contagion | deUSD | -98% | Nov 4-6, $1.00 to ~$0.015 | medium | [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/elixir-deusd-stablecoin-collapse-stream-finance-loss-2025-202511071458) |
| 2025-11-04 | Stream xUSD / Elixir deUSD contagion | xUSD | -74% | to ~$0.26 by early-mid Nov | medium | [BlockEden](https://blockeden.xyz/blog/2025/11/08/m-defi-contagion/) |

## Fiat/asset-backed reserve-shock depeg

**Mechanism.** A collateralized stablecoin (USDC, USDR, FDUSD) loses peg because the market doubts the reserves are fully redeemable — a real impairment (USDC's $3.3B stuck at failed SVB; USDR's treasury drained of liquid DAI) or a credible accusation (Justin Sun calling FDUSD's custodian insolvent). Redemptions queue while secondary-market sellers dump below $1 to exit immediately; the discount equals the market's probability-weighted haircut on the reserve. The other side is arbitrageurs/redeemers who buy the discounted coin betting reserves are good and 1:1 redemption resumes — they win when backing is real (USDC recovered to $1 in ~3 days) and lose when it is genuinely gone (USDR ~half permanent). Key read-across: when the trigger is TradFi banking stress (SVB), BTC *rallies* as a banking-system hedge.

- **Directional bias:** mixed
- **Typical magnitude:** -9% to -25% for credible fiat-backed (recovers); ~-49% for impaired RWA-backed (permanent)
- **Typical lag:** immediate (minutes-hours of disclosure); worst during banking off-hours / weekends
- **Typical duration:** hours to days; full recovery if reserves are real, permanent partial loss if not
- **Recurrence:** recurring; clustered around banking/custodian stress events
- **Affected scope:** the named stablecoin, stablecoins sharing its collateral (DAI, FRAX held USDC), issuer governance token (MKR, FXS), BTC, ETH
- **Leading signals:** disclosure of reserve held at a stressed bank/custodian; issuer pausing or slowing redemptions; prominent insolvency accusation against the issuer; collateral concentration in illiquid/RWA assets vs cash; downstream protocols (Maker, Frax) carrying large balances of the coin

| Date | Event | Asset | Impact | Window | Confidence | Source |
|------|-------|-------|--------|--------|------------|--------|
| 2023-03-11 | USDC SVB depeg | USDC | -12% | low ~$0.877 Mar 11 | high | [CoinDesk](https://www.coindesk.com/markets/2023/03/11/usdc-stablecoin-depegs-from-1-circle-says-operations-are-normal) |
| 2023-03-11 | USDC SVB depeg | DAI | -15% | low ~$0.85 | high | [Chainalysis](https://www.chainalysis.com/blog/crypto-market-usdc-silicon-valley-bank/) |
| 2023-03-11 | USDC SVB depeg | FRAX | -12% | low ~$0.877 | high | [CoinMarketCap](https://coinmarketcap.com/academy/article/explaining-the-silicon-valley-bank-fallout-and-usdc-de-peg) |
| 2023-03-11 | USDC SVB depeg (banking hedge) | BTC | +32% | Mar 10 low ~$19,670 to Mar 14 ~$26,000 | high | [Chainalysis](https://www.chainalysis.com/blog/crypto-market-usdc-silicon-valley-bank/) |
| 2023-03-11 | USDC SVB depeg | ETH | +6.8% | ~$1,660 to ~$1,773 by Mar 14 | high | [CoinDesk](https://www.coindesk.com/markets/2023/03/11/usdc-stablecoin-depegs-from-1-circle-says-operations-are-normal) |
| 2023-10-11 | USDR real-estate-backed collapse | USDR | -49% | hours, low ~$0.50-0.51 | high | [CoinDesk](https://www.coindesk.com/markets/2023/10/11/real-estate-backed-stablecoin-usdr-de-pegs-after-treasury-was-drained-of-liquid-assets) |
| 2025-04-02 | FDUSD insolvency-accusation depeg | FDUSD | -13% to -24% | intraday low ~$0.76-0.87 | medium | [The Daily Hodl](https://dailyhodl.com/2025/04/02/first-digital-usd-fdusd-depegs-after-justin-sun-alleges-firm-is-insolvent-and-not-fulfilling-redemptions/) |
| 2026-03-22 | Resolv USR — AWS-KMS key compromise mints $80M unbacked USR (backing destroyed) | USR | −79.8% ($1→$0.20; low ~$0.025, ~$25M extracted) | hours (Mar 22) | high | [coindesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr) |

## Venue-specific liquidity-cascade flash depeg

**Mechanism.** A well-collateralized stablecoin briefly prints a sharp discount on ONE venue (a single exchange order book or an imbalanced AMM pool) because of a localized liquidity vacuum — forced liquidations dump collateral into thin books, or an oracle/pricing quirk triggers a cascade, while the coin stays at ~$1 everywhere else and remains fully redeemable. The other side is fast arbitrageurs who buy the venue wick and redeem/sell elsewhere at par; they win because the discount is mechanical, not fundamental. These revert within minutes-to-hours and are NOT true insolvency events, but the wick itself can auto-liquidate over-collateralized borrowers who used the coin as collateral, propagating real losses.

- **Directional bias:** neutral
- **Typical magnitude:** -1% to -35% on the affected venue only; ~0% on aggregate/redeemable price
- **Typical lag:** instantaneous wick; reverts in minutes to a few hours
- **Typical duration:** minutes to hours; usually fully recovered same day
- **Recurrence:** frequent; minor venue wicks happen several times a year, severe ones during big liquidation cascades
- **Affected scope:** the named stablecoin (on one venue), its governance token (ENA), leveraged positions collateralized by it, broad market during liquidation cascades
- **Leading signals:** market-wide forced-liquidation cascade in progress (Oct 10-11 2025); single-venue order-book depth collapsing; AMM stable-pool weight skewing past ~70/30; high leverage / open interest using the stablecoin as margin; thin weekend/off-hours liquidity

| Date | Event | Asset | Impact | Window | Confidence | Source |
|------|-------|-------|--------|--------|------------|--------|
| 2025-10-10 | USDe (Ethena) Oct flash depeg | USDe (Binance venue) | -35% | flash low ~$0.65 on Binance | high | [CoinDesk](https://www.coindesk.com/markets/2025/10/13/no-ethena-s-usde-didn-t-de-peg) |
| 2025-10-10 | USDe (Ethena) Oct flash depeg | USDe (aggregate) | -0.88% | max drawdown Oct 8-15 | high | [21Shares](https://www.21shares.com/en-eu/insights/why-did-ethenas-stablecoin-remain-stable-onchain-but-depegged-on-binance) |
| 2025-10-10 | USDe (Ethena) Oct flash depeg | ENA | -40% | during crash | high | [99Bitcoins](https://99bitcoins.com/news/altcoins/ethena-usde-8b-outflows/) |
| 2025-10-10 | USDe (Ethena) Oct flash depeg | BTC | -8.96% | Oct 10-15 | high | [CoinDesk](https://www.coindesk.com/markets/2025/10/13/no-ethena-s-usde-didn-t-de-peg) |
| 2022-05-12 | USDT Terra-contagion flash wick | USDT | -8% | flash low ~$0.92 on Kraken | medium | [Protos](https://protos.com/history-of-tethers-peg-every-time-usdt-traded-above-or-below-one-dollar/) |
| 2023-06-15 | USDT Curve 3pool imbalance | USDT | -0.3% | low ~$0.997 | medium | [The Block](https://www.theblock.co/post/234822/tether-depeg-curve-3pool) |

## Backtest features

Aggregated across all three archetypes — the quant-consumable feature and analog-mechanism list:

**Features:**

- stablecoin_price_deviation_from_1usd
- sister_token_supply_growth_rate
- anchor_or_pool_TVL_outflow_24h
- deposit_apy_vs_market_apy_spread
- collateralization_ratio_below_1
- dex_pool_imbalance_pct (e.g. Curve 4pool UST weight)
- redemption_queue_size
- circulating_supply_zscore_of_sister_token
- exchange_netflow_zscore_of_sister_token
- share_of_supply_in_single_yield_venue
- secondary_vs_primary_market_discount
- reserve_exposure_to_impaired_counterparty_pct
- redemption_window_open_closed_flag
- downstream_stablecoin_collateral_overlap_pct (DAI/FRAX USDC weight)
- issuer_gov_token_drawdown
- btc_return_during_window (sign flip vs banking-stress trigger)
- stablecoin_market_cap_outflow_72h
- weekend_or_after_hours_flag (banking closed amplifies)
- per_venue_price_vs_aggregate_price_spread
- amm_pool_imbalance_pct (Curve/Uniswap stable pool weights)
- exchange_orderbook_depth_within_50bps
- liquidation_volume_zscore_market_wide
- time_to_revert_to_peg_minutes
- share_of_stablecoin_used_as_exchange_collateral
- oracle_vs_market_price_divergence
- open_interest_zscore_at_event

**Analog mechanisms:**

- reflexive-deleveraging
- sell-pressure
- forced-liquidation
- sentiment-shock
- supply-restriction
- dry-powder-injection

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/security/events` — recent hacks/depegs (10d lookback, filterable)
- `GET /api/v1/security/regime/score` — security-stress composite (45% hack, 30% flow, 25% depeg)
- `GET /api/v1/security/regime/{symbol}` — per-symbol security overlay

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time snapshots

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/security/events"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[crypto-narratives-overview]]
- [[bitcoin]]
- [[ethereum]]
- [[stablecoins]]
- [[terra-luna-collapse]]
- [[usdc]]
- [[usdt]]
- [[defi-lending]]
- [[curve-finance]]
- [[ethena]]
- [[risk-management]]
- [[liquidity]]

## Sources

- https://corpgov.law.harvard.edu/2023/05/22/anatomy-of-a-run-the-terra-luna-crash/
- https://en.wikipedia.org/wiki/Terra_(blockchain)
- https://www.riksbank.se/globalassets/media/konferenser/2023/session-1-liu_makarov_schoar-anatomy_of_a_run-_the_terra_luna_crash.pdf
- https://www.federalreserve.gov/econres/notes/feds-notes/runs-on-algorithmic-stablecoins-evidence-from-iron-titan-and-steel-20220602.html
- https://www.coindesk.com/markets/2021/06/17/in-token-crash-postmortem-iron-finance-says-it-suffered-cryptos-first-large-scale-bank-run
- https://en.wikipedia.org/wiki/Iron_Finance
- https://fortune.com/2022/06/13/algorithmic-stablecoin-usdd-loses-peg-justin-sun-tron-decentralized-usd/
- https://u.today/tron-dao-attacked-usdd-depeg-causes-16-trx-collapse-justin-sun-ready-to-cash-in-2-billion-to-fight
- https://blockeden.xyz/blog/2025/11/08/m-defi-contagion/
- https://www.fxstreet.com/cryptocurrencies/news/elixir-deusd-stablecoin-collapse-stream-finance-loss-2025-202511071458
- https://www.ainvest.com/news/systemic-risks-yield-bearing-stablecoins-lessons-deusd-xusd-usdx-collapses-2511/
- https://www.coindesk.com/markets/2023/03/11/usdc-stablecoin-depegs-from-1-circle-says-operations-are-normal
- https://www.chainalysis.com/blog/crypto-market-usdc-silicon-valley-bank/
- https://coinmarketcap.com/academy/article/explaining-the-silicon-valley-bank-fallout-and-usdc-de-peg
- https://www.coindesk.com/markets/2023/10/11/real-estate-backed-stablecoin-usdr-de-pegs-after-treasury-was-drained-of-liquid-assets
- https://www.dlnews.com/articles/defi/usdr-stablecoin-backed-by-real-estate-collapses/
- https://thedefiant.io/news/defi/tangible-s-usdr-stablecoin-depegs-to-50-cents
- https://dailyhodl.com/2025/04/02/first-digital-usd-fdusd-depegs-after-justin-sun-alleges-firm-is-insolvent-and-not-fulfilling-redemptions/
- https://www.tradingview.com/news/cointelegraph:090a27f4a094b:0-fdusd-stablecoin-depegs-following-insolvency-claims-by-justin-sun/
- https://www.altcoinbuzz.io/cryptocurrency-news/everything-about-the-fdusd-depeg/
- https://www.coindesk.com/markets/2025/10/13/no-ethena-s-usde-didn-t-de-peg
- https://www.21shares.com/en-eu/insights/why-did-ethenas-stablecoin-remain-stable-onchain-but-depegged-on-binance
- https://99bitcoins.com/news/altcoins/ethena-usde-8b-outflows/
- https://protos.com/history-of-tethers-peg-every-time-usdt-traded-above-or-below-one-dollar/
- https://www.theblock.co/post/234822/tether-depeg-curve-3pool
