---
title: "Pax Dollar"
type: market
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoin, stablecoins, defi]
aliases: ["PAX", "Pax Dollar", "Paxos Standard", "USDP"]
entity_type: protocol
headquarters: "New York, USA"
website: "https://www.paxos.com/standard/"
related: ["[[base]]", "[[binance]]", "[[binance-usd]]", "[[crypto-markets]]", "[[ethereum]]", "[[gemini-dollar]]", "[[paxos]]", "[[paypal-usd]]", "[[stablecoin]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-pair-arbitrage]]", "[[tether]]", "[[usdc]]"]
---

# Pax Dollar

**Pax Dollar** (ticker **USDP**, ERC-20 on [[ethereum|Ethereum]]) is a fiat-collateralized [[stablecoin]] pegged 1:1 to the U.S. dollar and issued by [[paxos|Paxos Trust Company, LLC]]. Originally launched in September 2018 as **Paxos Standard (PAX)**, it was one of the first regulated dollar stablecoins — Paxos was an early holder of a limited-purpose trust charter from the New York State Department of Financial Services (NYDFS), and PAX/GUSD were greenlit by NYDFS in the same 2018 cohort. The token was rebranded from PAX to USDP in 2021. Backing is held in cash and short-dated U.S. Treasury instruments, with monthly third-party attestations.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, USDP trades at **$0.998971**, holds market-cap rank **#619**, and carries a market capitalization of **$31,920,864** (**24h −0.02%**, **7d −0.05%**) — peg-anchored as expected.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDP (formerly PAX) |
| **Price (2026-06-21)** | $0.998971 |
| **Market Cap Rank** | #619 |
| **Market Cap** | $31,920,864 |
| **24h Change** | −0.02% |
| **7d Change** | −0.05% |
| **Peg target** | 1 USDP = 1 USD |
| **Backing model** | Fiat reserves (USD cash + short-dated U.S. Treasuries) |
| **Issuer** | [[paxos\|Paxos Trust Company, LLC]] |
| **Regulator** | NYDFS (limited-purpose trust charter) |
| **Native chain** | [[ethereum\|Ethereum]] (ERC-20); bridged to Solana |
| **Website** | [https://www.paxos.com/standard/](https://www.paxos.com/standard/) |

---

## Architecture: How USDP Works

USDP is a **fiat-reserve (custodial) stablecoin** — the simplest and most conservative stablecoin design. There is no algorithmic mechanism and no crypto collateral; each token is a digital claim on a dollar held in reserve by a regulated trust company. Contrast this with debt-backed designs like [[dola-usd|DOLA]] or over-collateralized [[dai|DAI]].

### Reserve model and attestation
Reserves backing circulating USDP are held in **U.S. dollar deposits and short-dated U.S. Treasury bills / overnight reverse repo** collateralized by Treasuries, segregated for the benefit of token holders under New York trust law. Because Paxos operates as a limited-purpose trust company (not a fractional-reserve bank), reserves are held 1:1 and are not lent out. Paxos publishes **monthly reserve attestation reports** prepared by an independent accounting firm, listing reserve composition and confirming that reserves meet or exceed tokens outstanding. This is a higher transparency bar than [[tether|USDT]] historically met, and comparable to [[usdc|USDC]] and [[gemini-dollar|GUSD]].

### Regulatory wrapper
Paxos holds a **NYDFS limited-purpose trust charter**, which subjects it to state-level reserve standards, capital requirements, custody rules, AML/KYC obligations, and periodic examination. This is the same regulatory framework under which Paxos issued [[binance-usd|BUSD]] and the white-label [[paypal-usd|PayPal USD (PYUSD)]]. The charter is a state trust charter, not a federal bank charter — an important distinction as the U.S. moves toward a federal stablecoin framework.

### Peg-maintenance / mint-redeem
The peg is held by **primary-market mint/redeem at par**:

- **Mint** — Vetted, KYC'd institutional customers wire USD to Paxos and receive USDP 1:1.
- **Redeem** — USDP returned to Paxos is burned and USD released 1:1.

This guaranteed convertibility lets arbitrageurs profit from any secondary-market deviation (buy USDP below $1, redeem for $1), pulling the secondary price back to peg. Mint/redeem is **gated to onboarded institutions**; retail users typically obtain USDP on exchanges rather than directly. The 2026-06-21 price of $0.998971 is ordinary micro-deviation, not a [[depeg]].

---

## Tokenomics & Supply

USDP supply is **fully reserve-backed and elastic** — it expands when institutions mint and contracts when they redeem, so circulating supply tracks net dollar inflows. There is no fixed max supply and no token-emission or seigniorage model; Paxos earns yield on the reserve assets (the float), the standard fiat-stablecoin business model. At ~$32M market cap, USDP is a small-cap stablecoin, well below its multi-billion-dollar peak as PAX in 2021. Supply has structurally declined as institutional demand migrated to [[usdc|USDC]], [[tether|USDT]], and Paxos's own [[paypal-usd|PYUSD]] / [[usdg|Global Dollar]] products.

---

## Comparison vs Competitor Stablecoins

| Stablecoin | Issuer | Peg | Backing | Regulatory wrapper | Attestation |
|---|---|---|---|---|---|
| **USDP** (Pax Dollar) | [[paxos\|Paxos]] | USD | Cash + T-bills | NYDFS trust charter | Monthly |
| [[usdc\|USDC]] | Circle | USD | Cash + T-bills | US state MTLs + EU MiCA EMT | Monthly |
| [[tether\|USDT]] | Tether | USD | Cash, T-bills, other | Offshore (El Salvador) | Quarterly |
| [[gemini-dollar\|GUSD]] | Gemini | USD | Cash + short instruments | NYDFS trust charter | Monthly |
| [[paypal-usd\|PYUSD]] | Paxos (for PayPal) | USD | Cash + T-bills | NYDFS trust charter | Monthly |

USDP and GUSD are the two original NYDFS-regulated dollar stablecoins. USDP's distinguishing trait today is its trust-charter regulatory wrapper and shared infrastructure with PYUSD — but it has lost scale to larger peers.

---

## How & Where It Trades / Is Used

USDP has historically been listed on major exchanges (Binance, KuCoin, Gate.io and others) as a regulated alternative to [[tether|USDT]], and trades in [[ethereum|Ethereum]] DEX pools (e.g. Uniswap USDP/[[usdc|USDC]] and USDP/[[tether|USDT]]). It is also bridged to Solana. Composability is standard ERC-20: it can be supplied to lending markets and stable pools, though its small float means depth is thin. With a ~$32M market cap it is a small-cap stablecoin; liquidity is real but far below [[usdc|USDC]] and [[tether|USDT]]. Primary use cases are regulated dollar settlement and as a stablecoin pair on venues that prefer NYDFS-overseen assets.

---

## Narrative, Category & Catalysts

USDP sits in the **regulated fiat-backed dollar stablecoin** category. Its forward catalysts are primarily regulatory: U.S. federal stablecoin legislation (which would advantage trust-chartered, fully-reserved issuers like Paxos), the growth of Paxos's broader stablecoin franchise ([[paypal-usd|PYUSD]], the Global Dollar Network / [[usdg|USDG]]), and institutional/payments adoption of regulated on-chain dollars. The counter-narrative is consolidation: capital concentrates in [[usdc|USDC]] and [[tether|USDT]], and Paxos's own newer products may cannibalize standalone USDP demand. In the current **Extreme Fear / bottoming-accumulation** macro regime (Fear & Greed 21), aggregate stablecoin supply is the key proxy for capital entering or leaving crypto; small regulated coins like USDP are a minor share of that flow.

---

## History / Timeline

- **September 2018** — Launched as **Paxos Standard (PAX)**; approved by NYDFS alongside [[gemini-dollar|Gemini Dollar (GUSD)]] in the first state-regulated dollar-stablecoin cohort.
- **2019–2021** — PAX grows as a regulated alternative to USDT; Paxos also issues white-label stablecoins including [[binance-usd|BUSD]].
- **2021** — Rebranded from **PAX to USDP** (Pax Dollar).
- **February 2023** — NYDFS orders Paxos to **stop minting [[binance-usd|BUSD]]**; this affected BUSD specifically, while USDP continued to be issued. A direct demonstration of NYDFS's authority over Paxos-issued tokens.
- **2023–2026** — USDP supply declines as demand migrates to larger and newer stablecoins; Paxos expands into [[paypal-usd|PYUSD]] and the Global Dollar Network.

---

## Risks

- **Issuer/counterparty risk** — Reliance on Paxos solvency and full reserve backing; holders have a claim on reserves but assume issuer continuity.
- **Reserve / counterparty risk** — Quality, custody, and liquidity of reserve assets and banking partners; a banking-partner failure could transiently stress redemptions.
- **Regulatory risk** — As [[binance-usd|BUSD]] demonstrated in February 2023, NYDFS can compel material changes to (or halt) a Paxos-issued stablecoin program.
- **Redemption-gating risk** — Direct mint/redeem is restricted to onboarded institutions; retail holders depend on secondary-market liquidity to exit at par.
- **Liquidity risk** — Small supply and modest volume can widen spreads and slippage, especially on-chain.
- **Smart-contract risk** — Standard audited ERC-20 exposure.

See [[stablecoin]] and [[depeg]] for the general failure-mode taxonomy.

---

## Trading Playbook

- **As a parking asset** — A regulated, fully-reserved dollar suitable for risk-off positioning; in the current bottoming regime, treat stablecoin balances as dry powder.
- **Mind the float** — At ~$32M, USDP is far thinner than [[usdc|USDC]]/[[tether|USDT]]; size on-chain trades to pool depth to avoid slippage.
- **Peg reads** — Treat $0.997–$1.001 as normal; only a sustained, widening discount with redemption friction signals a genuine [[depeg]].
- **Regulatory headline sensitivity** — Watch NYDFS / U.S. federal stablecoin news, which moves regulated issuers like Paxos more than offshore peers.

---

## Related

- [[stablecoin]]
- [[paxos]]
- [[binance-usd]]
- [[gemini-dollar]]
- [[paypal-usd]]
- [[usdc]]
- [[tether]]
- [[depeg]]
- [[collateralization]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for issuer/mechanism details.

## Trading Profile

### Venues & liquidity

USDP is a USD-pegged [[stablecoin]] traded on [[binance]] and other centralized venues, and it is a **PEG / cash-management instrument, NOT a directional asset** — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. Because it is fully fiat-reserved and pegged 1:1, there is no directional thesis and no meaningful use for leverage; it functions as quote-side or parking liquidity rather than a position to be long or short. With a small float, secondary-market depth is thin relative to [[usdc|USDC]] and [[tether|USDT]], so venue availability directly shapes execution: on Binance and deep CEX order books, tight spreads permit larger arbitrage clips at par, while on-chain pools and minor venues force smaller sizing to avoid slippage. Primary-market mint/redeem is gated to onboarded institutions, so retail execution and sizing are constrained to whatever secondary liquidity a given venue offers.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — Buy USDP below par during a depeg episode when the trust-charter backing and institutional redemption support a snap-back to $1.
- [[stablecoin-pair-arbitrage]] — Arb USDP against [[usdc|USDC]]/[[tether|USDT]] across CEX pairs and DEX pools, capturing spreads between regulated dollar tokens.
- [[mint-parity-arbitrage]] — For onboarded institutions, mint/redeem USDP at par with Paxos to close any secondary-market deviation against $1.
- [[stablecoin-yield]] — Deploy idle USDP into lending markets and stable pools to earn yield on a fully-reserved, NYDFS-regulated dollar.
- [[carry-trade]] — Hold USDP as the funding/parking leg while harvesting yield differentials, given its conservative fiat-reserve backing.

### Volatility & regime character

USDP is a fiat-reserve (custodial) stablecoin with monthly independent attestations and 1:1 par mint/redeem, so under normal conditions the peg is tight and volatility is near-zero — treat micro-deviations around $0.997–$1.001 as ordinary noise. Redemption mechanics are par-based but gated to onboarded institutions, so retail peg-recovery relies on secondary-market arbitrage. Its thin float means episodic wicks can appear on low-liquidity venues without reflecting genuine reserve stress; a real regime shift would be a sustained, widening discount accompanied by redemption friction rather than a transient tick.

### Risk flags

- **Depeg risk** — Thin liquidity and small supply can produce transient secondary-market deviations; only a sustained, widening discount signals a genuine [[depeg]].
- **Reserve / backing transparency** — Backing is cash plus short-dated Treasuries with monthly attestations; reserve-asset quality, custody, and banking-partner health remain the key trust assumptions.
- **Redemption gating** — Direct par redemption is restricted to onboarded institutions, so retail holders depend on venue liquidity to exit at $1.
- **Regulatory** — As the February 2023 [[binance-usd|BUSD]] halt showed, NYDFS can compel material changes to a Paxos-issued program; U.S. federal stablecoin policy is the dominant headline risk.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=USDPUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=USDPUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=USDPUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=USDPUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---
