---
title: "Crypto Perp Backtesting Pitfalls"
type: concept
created: 2026-05-05
updated: 2026-06-14
status: excellent
tags: [backtesting, crypto, derivatives, risk-management, methodology, leverage]
aliases: ["Perpetual Futures Backtesting Pitfalls", "Crypto Perps Backtest Hazards"]
domain: [backtesting]
difficulty: advanced
related: ["[[auto-deleveraging]]", "[[liquidation-cascade-modeling]]", "[[point-in-time-data]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[slippage-modeling]]", "[[lookahead-bias]]", "[[walk-forward-analysis]]", "[[purged-kfold-cv]]", "[[hyperliquid-backtesting]]", "[[backtesting-overview]]", "[[perpetual-futures]]", "[[hyperliquid]]", "[[bybit]]", "[[binance]]", "[[2025-10-crypto-liquidation-cascade]]", "[[oracle-manipulation]]", "[[depeg-risk]]", "[[book-advances-in-financial-machine-learning]]", "[[in-sample-vs-out-of-sample]]", "[[deflated-sharpe-ratio]]"]
---

# Crypto Perp Backtesting Pitfalls

Crypto perpetual-futures backtests are systematically more fragile than tradfi backtests, and the failure modes are different in kind, not just degree. Perps trade 24/7 with no settlement, accrue funding payments every few hours, liquidate on intraday vol that would never threaten a margined equity book, and clear across a fragmented venue map whose dominance shifts violently — one decentralized venue (Hyperliquid) swung from ~80% to 38% of DEX perp share inside a single quarter of 2025. This page is the umbrella catalogue of what breaks; each pitfall links to a deeper page where one exists.

## Why Crypto Perps Are Different

Tradfi futures backtests can usually assume continuous liquidity within session, well-defined settlement at expiry, regulator-supervised counterparties, and stable contract specs. Perps violate all four:

- **24/7 trading.** No session breaks, no overnight gap to absorb stale orders, no daily settlement window. Strategies that implicitly batch by trading day on equities have no analog. Bar-boundary assumptions silently inherit a tradfi calendar — see [[bar-resolution-selection]] and [[microstructure-noise-low-timeframe]].
- **No settlement.** Perpetuals never expire. Convergence to spot is enforced by [[funding-rate|funding payments]] paid every 1, 4, or 8 hours, not by physical/cash settlement at maturity.
- **Funding payments.** Long-short positions accrue or pay funding every cycle. Backtests that ignore funding can be off by 10-20% APY on a directional book and far more on a delta-neutral book where funding *is* the strategy.
- **Liquidations.** Cross-margin, isolated-margin, and partial-liquidation rules vary by venue. A 5% adverse move at 20x leverage liquidates; the resulting forced flow moves price further.
- **Auto-Deleveraging (ADL).** When the insurance fund is exhausted, profitable positions on the *winning* side are force-closed to cover losses on the losing side. This breaks "neutral hedge" assumptions catastrophically.
- **Fragmented, fast-rotating venues.** Binance, Bybit, OKX, Hyperliquid, dYdX, plus regulated venues (CME). Liquidity, funding, and slippage differ; a single-venue backtest is not a strategy backtest. Worse, the dominance ranking is non-stationary (see pitfall 7).

## The Core Pitfalls

### 1. Auto-Deleveraging not modeled

[[auto-deleveraging|ADL]] is the mechanism exchanges use when the insurance fund cannot cover liquidation losses: they force-close *profitable* positions on the opposite side, ranked by leverage and unrealized PnL%, at the bankruptcy price of the liquidated position. This is documented behaviour on both Bybit and OKX (Source: Bybit Learn — ADL; OKX Help — ADL). During the October 10-11, 2025 cascade ($20B+ in liquidations across Binance, Bybit, OKX and Hyperliquid), ADL fired across venues, and supposedly delta-neutral basis traders saw their winning legs unilaterally closed at exchange-determined prices while their losing legs liquidated normally. A backtest that models liquidations only on the position-being-liquidated is not modeling perps — it is modeling a margin-call instrument that does not exist.

**Validation:** inject a synthetic ADL on the strategy's most profitable open position during each stress window (see playbook) and confirm the strategy survives the forced close at bankruptcy price, not at mark price.

### 2. Funding-rate regime shifts

Perp funding rates are not a stationary series. They were historically anchored near the 0.01% per 8-hour baseline (~11% APY), trended elevated through the 2024 spot-ETF basis-trade boom, then compressed below 4% APY by mid-2025 as crowding unwound and the October 2025 ADL crisis drove out leveraged longs (Source: BitMEX — State of Crypto Perps 2025). A concrete validation window is **August 2024**, when Ethena's delta-neutral sUSDe basis trade saw its yield collapse from ~19% to ~4% in roughly 11 days as funding inverted (Source: Ethena docs) — any carry strategy should be re-tested across exactly this kind of compression event. A naive [[funding-rate-arbitrage|cash-and-carry]] backtest sampled only on 2024 highs overstates the post-2025 strategy by several-fold.

> Note on magnitudes: the often-quoted "2023 averaged ~11% APY, peaked ~19% APY in early 2024" figures are not cleanly corroborated by primary sources at that precision; treat them as illustrative of the *direction* (elevated 2024 → sub-4% mid-2025), which BitMEX's 2025 report confirms, rather than as exact statistics.

Regime-aware backtests must segment by funding regime, model the term structure, or use rolling-window training that captures the compression event. See [[funding-rate]] and [[hyperliquid-funding-rate-microstructure]].

### 3. Liquidation cascades treated as independent events

Liquidations are widely argued to be **self-exciting rather than i.i.d.**: a single forced sell pushes price toward the next cluster of stop/liquidation levels, which fires, which pushes price further. (The precise "clustering = ≥30% of liquidation volume within 2% of a range boundary" definition is one analyst framing, not a settled standard — Source: AmberData; treat as a heuristic, not a constant.) The October 2025 event saw well over a billion dollars liquidated within the first hour of the initial trigger, with the cascade propagating across Binance → Bybit → OKX → Hyperliquid in minutes (Source: CoinDesk postmortem). Backtests that draw liquidation losses from an independent distribution underestimate tail risk by an order of magnitude. Realistic modeling requires liquidation-cluster awareness ([[coinglass]] historical/heatmap data and API) and a cascade-propagation model. See [[liquidation-cascade-modeling]] and [[hyperliquid-liquidation-engine]].

### 4. Slippage modeled as fixed % rather than depth-aware

Crypto perp slippage ranges from ~0.05% on top-of-book BTC at low size to several percent on alt perps in stress regimes; fixed-percentage assumptions break precisely when they matter because large orders sweep multiple book levels (Source: LuxAlgo). A fixed 0.2% slippage assumption applied to a large order during the October 2025 crash underestimates the realized fill cost by an order of magnitude or more. A practical depth-aware model is:

```
slippage_% ≈ (order_size / top_N_book_depth) × regime_multiplier
```

where `regime_multiplier` is ~1 in calm regimes and rises sharply (often 5-50×) in high-vol windows. **Empirically validate** the model by comparing three methodologies against archived data: (a) **fixed %** (cheap, wrong in tails), (b) **VWAP-based** (fills against realized volume over the fill horizon), and (c) **depth-aware / tick-by-tick replay** against archived order-book snapshots. Where the three diverge sharply is exactly where the strategy's tail risk lives. Source order-book archives: [Tardis.dev](https://tardis.dev/) (tick-level book/trades/OI/funding/liquidations for BitMEX, Deribit, Binance Perpetuals, OKX) and Kaiko. See [[slippage-modeling]], [[intrabar-fill-modeling]], [[transaction-cost-modeling]], and [[execution-model-differences]].

### 5. Survivorship bias

Delisted tokens, dead exchanges, and bankrupt venues are routinely excluded from "historical perp datasets," and the inflation is large: survivorship bias can inflate backtested crypto returns by roughly **200-400%**. A worked "buy the top-20 altcoins" example shows +2,800% with the bias versus +680% once corrected (Source: StratBase.ai, via CoinAPI discussion). The academic baseline: Ammann, Burdorf, Liebi & Stöckl, studying 3,904 cryptocurrencies over 2014-2021, estimate a survivorship-and-delisting bias of ~0.93% annualized on a value-weighted basis, ballooning to 62.19% on an equal-weighted basis (Source: SSRN 4287573).

FTX's November 2022 collapse took a complete contract history with it; perpetuals on now-shuttered DEXes disappear from snapshot pulls — including **Mango Markets**, the Solana perp DEX that shut down in January 2025 following an SEC settlement ($700,000 civil penalty) and a CFTC settlement ($500,000), after the October 2022 Avraham Eisenberg oracle-manipulation exploit drained ~$110M (of which ~$67M was returned). Bybit archives from early 2025 are patchy in some datasets, but that appears to be archival/labeling gaps rather than confirmed wholesale data loss; treat venue-incident periods as suspect rather than authoritative. The fix: use survivorship-free archives ([CoinAPI](https://www.coinapi.io/blog/how-to-eliminate-survivorship-bias-in-crypto-backtesting) flat files with point-in-time universe construction, Kaiko) and explicitly include the dead set. See [[selection-bias-research]].

### 6. Look-ahead bias from revised on-chain data

On-chain features look immutable because the blockchain is, but the *interpretation layer* (entity labels, exchange clusters, contract tags) is revised continuously. A feature like `exchange_net_inflow` for January 2024 reads differently in May 2026 than it did when it was current. The discipline is point-in-time (PIT): every feature carries a **vintage stamp** and joins use **as-of semantics**, not latest-labels (Source: PIT backtesting practice). See [[point-in-time-data]] and [[lookahead-bias]].

### 7. Single-venue assumption when liquidity is fragmented — and rotating

Venue dominance in crypto perps is not just uneven, it is **non-stationary on a quarterly timescale**. Hyperliquid dominated decentralized perps through August 2025 at roughly 75-80% of DEX perp share (processing ~$30B/day), then **fell to about 38% by late September 2025** as Aster and Lighter took share (Sources: CoinDesk, Aug & Sept 2025; The Block). A backtest run on a single venue's order book assumes that venue's liquidity for all fills; a strategy that actually trades cross-venue must model venue-specific funding, depth, latency, and counterparty risk. Single-venue backtests are upper bounds. The cross-venue check: if `Sharpe(venue_1) − Sharpe(venue_2) > 0.5`, the result is venue-specific, not strategy-specific. See [[hyperliquid-perp-trading-map]].

### 8. Stablecoin / collateral assumed always at par

USDT, USDC, DAI, and FDUSD are margin collateral on most perp venues, and backtests typically assume `1 USDC = $1` always. This breaks during stress: **USDC depegged to roughly $0.877 on March 11, 2023** after Circle disclosed $3.3B of reserves at the failing Silicon Valley Bank, recovering to ~$1.00 within a few days (Source: CNBC; Bitget market data for the low). A position collateralized in USDC during such a depeg loses on the collateral and the trade simultaneously. See [[depeg-risk]].

### 9. Oracle manipulation and DeFi-collateral risk

Strategies that trade DeFi-listed perps or use DeFi-collateralized positions inherit oracle and bridge risk. The **April 2026 Aave / KelpDAO incident** is the canonical recent case: ~116,500 rsETH (~$292M) was drained via a LayerZero bridge, the attacker supplied the stolen rsETH as Aave collateral and borrowed ~126,000 WETH, leaving roughly $177M in bad debt (some analyses put the impaired total higher). Aave's TVL fell from ~$48.5B to ~$30.7B (a ~$15.1B outflow) in about 3.5 days, and total DeFi TVL dropped ~$13.2B (Sources: KuCoin; Yahoo Finance). Backtests of DeFi-integrated strategies must model oracle staleness, single-verifier bridge assumptions, manipulation windows, and bridge-dependency failures. See [[oracle-manipulation]].

### 10. Walk-forward windows that span regime breaks

Crypto regimes shift on identifiable events: **January 11, 2024** (10 spot Bitcoin ETFs launched after SEC approval of 11; ~$2.1B average daily volume, with a documented 3-4pm NYC volume spike around NAV fixing — Source: Grayscale, Kaiko), July 23, 2024 (ETH spot ETF launch), the October 10-11, 2025 ADL crisis, and the subsequent funding-rate compression. A [[walk-forward-analysis]] window that straddles one of these breaks fits a model on a regime that no longer exists, then validates on a regime that did not yet exist at fit time.

The fix is regime-aware windowing. To set anchors algorithmically rather than by hand: (a) seed known event dates as candidate breakpoints; (b) run a structural-break / changepoint test (e.g., on rolling realized vol, funding level, or open-interest growth) to detect unlabeled breaks; (c) ensure no single train or test window crosses a detected breakpoint, embargoing a buffer around it. For the time-series leakage problem more generally, the academic standard is **López de Prado's Purged K-Fold and Combinatorial Purged Cross-Validation**, which purge training observations whose label horizons overlap the test set and embargo a gap afterward (Source: *Advances in Financial Machine Learning*, Wiley 2018). See [[purged-kfold-cv]], [[cross-validation]], [[in-sample-vs-out-of-sample]], and [[book-advances-in-financial-machine-learning]].

## Recommended Validation Playbook

A defensible perp backtest must include:

- **Stressed regime windows.** At a minimum, replay performance through:
  - **March 12, 2020** ("COVID Thursday") — BTC fell from ~$7,200 to $5,678; ~$702M liquidated on BitMEX; BitMEX insurance fund lost 1,627 BTC (Source: CoinDesk). (The often-cited funding swing from +0.01% to -0.375% is unverified — do not rely on it.)
  - **May 2021** — China mining ban; BTC fell ~55% from ~$65,000 to ~$28,000; global hash rate roughly halved; combined with the Tesla payment suspension and heavy leverage this drove cascading liquidations (Source: Decrypt).
  - **May 2022** — LUNA / UST collapse; UST depegged below $1 on May 7 and bottomed near **$0.06**; LUNA supply hyperinflated from ~343M to ~6.53 trillion tokens; >90% of market cap lost within a week (Source: ECOS; Richmond Fed post-mortem). Note: this was a far larger supply blowup than the sometimes-quoted "80x."
  - **November 2022** — FTX collapse; ~$3.5B+ in forced position closures, ~$8B hole in customer accounts across ~1M creditors (Source: Wikipedia — Bankruptcy of FTX).
  - **October 10-11, 2025** — ADL crisis; $20B+ liquidations; cross-venue cascade (Source: CoinDesk). See [[2025-10-crypto-liquidation-cascade]].
  - **April 2026** — Aave / KelpDAO bridge-and-oracle exploit; ~$177M bad debt; ~$15B Aave TVL outflow.
- **Depth-aware slippage.** Slippage as `(order_size / top-N book depth) × regime_multiplier`, replayed against archived order-book snapshots (Tardis.dev, Kaiko) and cross-checked against fixed-% and VWAP baselines.
- **Funding APY zeroed (or inverted) in stressed regimes.** Strategies relying on positive carry should be re-run with funding = 0 (and once with funding inverted, à la August 2024) across all stress windows. If the strategy is not viable without carry, label it "carry-dependent" and size accordingly.
- **ADL events forced.** Inject a synthetic ADL on the strategy's most profitable position during each stress window; verify survival at bankruptcy price.
- **Cross-venue replay.** Replay on at least three venue datasets (e.g., Binance, Bybit, Hyperliquid) and report Sharpe variance. If venue choice changes Sharpe by >0.5, the result is venue-specific.
- **PiT discipline.** Every on-chain or off-chain feature carries a vintage; joins use as-of semantics. See [[point-in-time-data]].
- **Survivorship-corrected universe.** Include delisted tokens, dead exchanges (FTX, Mango), and rebranded tickers explicitly. See [[selection-bias-research]].
- **Leakage-safe validation.** Use purged/embargoed cross-validation, and deflate the headline Sharpe for the number of configurations tried. See [[purged-kfold-cv]], [[deflated-sharpe-ratio]], and [[data-snooping-and-p-hacking]].

## When Backtests Are Most Likely to Mislead

The danger is highest when the strategy combines:

- **High leverage** (≥10x) — small adverse moves trigger liquidation, and ADL becomes structurally relevant
- **Short time windows** (<2 years) — insufficient regime coverage; no LUNA, no FTX, no October 2025
- **Narrow basket** (single asset or ≤5 alts) — idiosyncratic survivorship dominates
- **Single venue** — venue-specific liquidity and funding baked in as if universal, on a dominance ranking that rotates quarterly
- **Carry-dependent edge** — PnL *is* funding, and funding compressed several-fold between the 2024 peak and mid-2025

Any strategy meeting three or more of these criteria with a backtest Sharpe > 2 should be treated as suspect until the validation playbook above is run end-to-end. See [[overfitting]] and [[hypothesis-to-backtest-workflow]].

## Sources

- [BitMEX — State of Crypto Perps 2025](https://www.bitmex.com/blog/state-of-crypto-perps-2025) — funding-rate compression timeline and ADL impact through 2025
- [BitMEX — Q2 2025 Derivatives / XBTUSD Funding Report](https://www.bitmex.com/blog/2025q2-derivatives-report) — long-run funding-rate history
- [CoinDesk — Friday's $20B crypto meltdown: a Bitwise PM's postmortem (Oct 12, 2025)](https://www.coindesk.com/markets/2025/10/12/friday-s-usd20b-crypto-market-meltdown-a-bitwise-portfolio-manager-s-postmortem-analysis) — October 2025 cascade size and cross-venue propagation
- [CoinDesk — Hyperliquid now dominates DeFi derivatives, $30B/day (Aug 21, 2025)](https://www.coindesk.com/business/2025/08/21/hyperliquid-now-dominates-defi-derivatives-processing-usd30b-a-day) — Hyperliquid peak DEX perp share
- [Bybit Learn — What Is Auto-Deleveraging (ADL)](https://learn.bybit.com/en/trading/what-is-auto-deleveraging-adl) — ADL ranking and bankruptcy-price close
- [OKX Help — Introduction to Auto-Deleveraging (ADL)](https://www.okx.com/en-us/help/iv-introduction-to-auto-deleveraging-adl) — ADL mechanism
- [LuxAlgo — Backtesting Limitations: Slippage and Liquidity](https://www.luxalgo.com/blog/backtesting-limitations-slippage-and-liquidity-explained/) — slippage modeling taxonomy and stress-regime fill failure
- [Tardis.dev — Granular crypto market data](https://tardis.dev/) — tick-level order-book / funding / liquidation archives
- [CoinGlass — Liquidation history API & heatmaps](https://docs.coinglass.com/reference/liquidation-history) — aggregated liquidation data across venues
- [CoinAPI — Eliminating Survivorship Bias in Crypto Backtesting](https://www.coinapi.io/blog/how-to-eliminate-survivorship-bias-in-crypto-backtesting) — survivorship-free universe construction
- [Ammann, Burdorf, Liebi & Stöckl — Survivorship and Delisting Bias in Cryptocurrency Markets (SSRN 4287573)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4287573) — quantified bias on 3,904 cryptos, 2014-2021
- [López de Prado — Advances in Financial Machine Learning (Wiley 2018)](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086) — purged & combinatorial cross-validation
- [Ethena — USDe / sUSDe delta-neutral yield](https://eco.com/support/en/articles/15254002-ethena-usde-and-susde-2026-delta-neutral-yield) — August 2024 funding compression (19%→4% in ~11 days)
- [Gate Learn — Perpetual Contract Funding Rate Arbitrage](https://www.gate.com/learn/articles/perpetual-contract-funding-rate-arbitrage/2166) — carry mechanics
- [CNBC — USDC breaks dollar peg after $3.3B SVB exposure (Mar 11, 2023)](https://www.cnbc.com/2023/03/11/stablecoin-usdc-breaks-dollar-peg-after-firm-reveals-it-has-3point3-billion-in-svb-exposure.html) — USDC depeg
- [KuCoin — KelpDAO rsETH exploit: $292M LayerZero bridge attack, $177M Aave bad debt](https://www.kucoin.com/blog/vn-kelpdao-rseth-exploit-how-292m-layerzero-bridge-attack-created-177m-bad-debt-on-aave) — April 2026 incident mechanism
- [Yahoo Finance — Where did Aave's $15B go? KelpDAO aftermath](https://finance.yahoo.com/markets/crypto/articles/where-did-aave-15b-kelpdao-105215197.html) — Aave TVL impact
- [CoinDesk — Bitcoin's crash triggers $700M+ in liquidations on BitMEX (Mar 12, 2020)](https://www.coindesk.com/markets/2020/03/12/bitcoins-crash-triggers-over-700m-in-liquidations-on-bitmex) — COVID Thursday figures
- [Decrypt — China's 2021 Bitcoin crackdown](https://decrypt.co/74187/chinas-2021-bitcoin-crackdown-what-you-need-know) — May 2021 mining ban cascade
- [ECOS — Terra Luna crash complete breakdown](https://ecos.am/en/blog/terra-luna-crash-complete-breakdown-of-the-luna-and-ust-algorithmic-stablecoin-implosion) — May 2022 LUNA/UST collapse
- [Richmond Fed — Why Stablecoins Fail: Terra post-mortem](https://www.richmondfed.org/publications/research/economic_brief/2022/eb_22-24) — UST economics
- [Wikipedia — Bankruptcy of FTX](https://en.wikipedia.org/wiki/Bankruptcy_of_FTX) — November 2022 collapse
- [The Defiant — Mango Markets to shut down after SEC settlement](https://thedefiant.io/news/defi/mango-markets-to-shut-down-after-sec-settlement) — Mango shutdown / exploit history
- [Grayscale — January 2024: the debut of spot Bitcoin ETFs](https://research.grayscale.com/market-commentary/january-2024-the-debut-of-spot-bitcoin-etfs) — ETF launch volumes
- [Kaiko — BTC ETFs' impact on spot market structure](https://research.kaiko.com/insights/btc-etfs-impact-on-spot-market-structure) — NAV-fixing volume spike
- [AmberData — Liquidations in crypto: anticipating volatile moves](https://blog.amberdata.io/liquidations-in-crypto-how-to-anticipate-volatile-market-moves) — liquidation clustering (heuristic framing)

## Related

- [[hyperliquid-backtesting]] — the Hyperliquid-specific anti-overfit playbook that specializes this page
- [[hyperliquid-funding-rate-microstructure]]
- [[hyperliquid-liquidation-engine]]
- [[hyperliquid-perp-trading-map]]
- [[auto-deleveraging]]
- [[liquidation-cascade-modeling]]
- [[point-in-time-data]]
- [[funding-rate]]
- [[funding-rate-arbitrage]]
- [[slippage-modeling]]
- [[intrabar-fill-modeling]]
- [[transaction-cost-modeling]]
- [[execution-model-differences]]
- [[lookahead-bias]]
- [[walk-forward-analysis]]
- [[purged-kfold-cv]]
- [[cross-validation]]
- [[in-sample-vs-out-of-sample]]
- [[deflated-sharpe-ratio]]
- [[selection-bias-research]]
- [[data-snooping-and-p-hacking]]
- [[overfitting]]
- [[hypothesis-to-backtest-workflow]]
- [[backtesting-overview]]
- [[perpetual-futures]]
- [[hyperliquid]]
- [[bybit]]
- [[binance]]
- [[2025-10-crypto-liquidation-cascade]]
- [[oracle-manipulation]]
- [[depeg-risk]]
- [[book-advances-in-financial-machine-learning]]
