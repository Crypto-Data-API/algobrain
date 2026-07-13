---
title: "NVIDIA xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stocks]
aliases: ["NVDAX", "NVIDIA xStock", "Nvidia xStock"]
entity_type: protocol
headquarters: "Decentralized (issuer: Backed Finance AG, Switzerland)"
website: "https://xstocks.com/"
related: ["[[crypto-markets]]", "[[arbitrum]]", "[[solana]]", "[[real-world-assets]]", "[[tokenized-stocks]]", "[[backed-finance]]", "[[nvidia-ondo-tokenized-stock]]", "[[nvidia]]", "[[tokenization]]"]
---

# NVIDIA xStock

**NVIDIA xStock** (ticker **NVDAX**) is a [[tokenized-stocks|tokenized equity]] issued by [[backed-finance|Backed Finance AG]] under its **xStocks** brand. Each NVDAX token is engineered to track the price of one share of **NVIDIA Corporation (NASDAQ: NVDA)** — the dominant AI/GPU semiconductor company — and is collateralized 1:1 by the underlying share held in custody. NVDAX is issued natively on [[solana]] as an SPL token, with bridged ERC-20 deployments across several EVM chains, giving non-US users on-chain, DeFi-composable price exposure to NVIDIA without a traditional brokerage account. It is a [[real-world-assets|real-world asset (RWA)]] wrapper, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, NVDAX traded at **$208.95**, ranked **#577** by market capitalization with a market cap of **$35,076,331**. It was **+0.03% over 24 hours** and **+1.83% over 7 days** — moves that track the underlying NVDA share rather than independent token dynamics.

---

## What NVDAX Is

NVDAX is **not** issued by NVIDIA and grants **no equity ownership, voting rights, or shareholder status**. It is a tracking token: a bearer-style instrument pegged to one NVDA share held in custody, giving the holder a legal claim (against the issuer) to the value of that share. It lets users gain NVIDIA price exposure 24/7 on-chain.

NVDAX sits alongside the competing Ondo-issued tokenization of the same name (see [[nvidia-ondo-tokenized-stock]]), differentiated by Backed Finance's issuance, custody, and access framework. Two prices coexist for any tokenized stock:

- **The reference price** — what NVDA trades at on the Nasdaq during US market hours.
- **The token price** — what NVDAX trades at on crypto venues 24/7, which can drift from the reference when the US market is closed or on-chain liquidity is thin.

---

## Architecture: How the Wrapper Works

### Issuer, custody and collateral

- **Issuer:** [[backed-finance|Backed Finance AG]], a Switzerland-based issuer of tokenized securities operating under EU/Swiss frameworks (Backed publishes its tokens under an EU base prospectus regime). xStocks target **non-US users** and are not offered to US persons.
- **1:1 backing:** Each NVDAX token is backed by one corresponding NVDA share (or depositary-receipt equivalent) held with a regulated third-party custodian, segregated from Backed's own balance sheet. Backed publishes proof-of-reserves / collateral attestations for its xStocks line.
- **Bankruptcy-remoteness:** Backed's structure is designed so that holders have a claim on the underlying collateral even in an issuer-default scenario — but this is a contractual/legal claim, not the brokerage-account ownership and SIPC-style protection a US investor would have holding NVDA directly.

### Mint / redeem and KYC gating

- **Permissioned primary market:** Mint and redeem are limited to KYC-verified, whitelisted authorized participants (typically institutions/market-makers). To mint, an AP delivers the underlying NVDA share into custody and receives a token; to redeem, the AP burns a token and receives the underlying value. This is the mechanism that keeps supply collateralized 1:1.
- **Permissionless secondary market:** Once minted, NVDAX trades **permissionlessly** — any wallet can buy, sell, transfer, or use it in DeFi without KYC. Whitelisting is required only to mint or redeem, not to hold or trade.
- **Jurisdiction gating:** Access is geofenced to non-US/eligible jurisdictions; US persons are excluded by the issuer's terms.

### Oracle / price feed, trading hours, corporate actions

- **Price tracking:** NVDAX tracks NVDA closely during US market hours through primary-market arbitrage (see below). DeFi venues that consume NVDAX may rely on a price oracle, which can itself be a source of staleness or manipulation risk when the underlying market is closed.
- **24/7 vs market hours:** NVDAX trades 24/7 while NVDA trades only in the US session (plus pre/post-market). The token can therefore drift from the last NASDAQ print overnight, on weekends, and during US holidays, then re-converge at the next US open.
- **Dividends / corporate actions:** NVIDIA pays only a small dividend. Dividend treatment and corporate actions (splits, etc.) are handled by the issuer and typically reflected as an economic adjustment to the token rather than a cash payout or direct shareholder entitlement.
- **Settlement chains:** Native SPL on [[solana]]; bridged ERC-20 across [[arbitrum|Arbitrum One]], Ethereum, BNB Chain, Mantle, Ink, TON, and Tron.

### What holders do NOT get

- No voting rights or proxy participation at NVIDIA.
- No direct shareholder registration; the legal relationship is with the issuer, not the company.
- No US investor-protection coverage (no SIPC).

---

## Tracking & Peg

NVDAX stays near the NVDA reference price through **arbitrage by primary participants**: when the token trades at a premium, APs mint (delivering shares) and sell tokens; when it trades at a discount, they buy tokens and redeem for shares. This keeps the peg honest *while* the underlying market is open and APs are active.

**Sources of premium/discount and depeg risk:**

- **Weekend / after-hours gap risk:** With NVDA closed, NVDAX can move on sentiment or on a thin order book, opening a basis to the (stale) last print. This is structural, not a malfunction.
- **Thin liquidity:** Small on-chain depth means large orders can push the token away from fair value and widen spreads.
- **Redemption friction:** If primary redemption windows are slow or APs step back (stress, custody issues), discounts can persist longer.
- **Oracle staleness:** DeFi protocols pricing NVDAX off an oracle can misprice it during closures.

---

## Comparison: Ways to Get NVIDIA Exposure

| Dimension | **NVDAX (Backed xStock)** | **NVDAON ([[nvidia-ondo-tokenized-stock|Ondo]])** | **Real NVDA share (broker)** | **NVDA CFD** |
|---|---|---|---|---|
| **Issuer / venue** | Backed Finance AG | Ondo Global Markets | Exchange + broker | CFD broker |
| **Backing** | 1:1 NVDA share in custody | 1:1 NVDA share off-chain | Direct ownership | None (synthetic) |
| **Native chain** | Solana (SPL), multi-chain | Ethereum, multi-chain | n/a | n/a |
| **Secondary trading** | Permissionless on-chain | KYC / whitelist-restricted | Brokerage account | Broker platform |
| **Hours** | 24/7 | 24/7 mint/redeem (5d/wk) | US market hours | Broker hours |
| **Dividends** | Issuer economic adjustment | Reinvested into token | Paid to holder | Adjustment |
| **Shareholder rights** | None | None | Full (voting) | None |
| **US persons** | Excluded | Excluded | Allowed | Often restricted |
| **Key risk** | Issuer/custody, peg | Issuer/custody, transfer limits | Counterparty minimal | Broker counterparty, leverage |

---

## How & Where It Trades

- **Centralized:** Listed on Kraken (NVDAX/USD) among the venues that support xStocks.
- **Decentralized:** Trades on Solana DEXs (e.g., Orca); Solana is the deepest venue and the primary liquidity hub.
- **Liquidity profile:** Thin relative to the underlying equity. Liquidity concentrates during US trading hours when arbitrageurs are active; off-hours depth is shallow, so size trades incur slippage.

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0xc845b2894dbddd03858fd2d643b4ef725fe0849d` |
| Ethereum | `0xc845b2894dbddd03858fd2d643b4ef725fe0849d` |
| Binance Smart Chain | `0xc845b2894dbddd03858fd2d643b4ef725fe0849d` |
| Tron | `TNMR6r9Z4cL7eWNrNQ4e4sm2XPhhifexZU` |
| Ink | `0xc845b2894dbddd03858fd2d643b4ef725fe0849d` |
| The Open Network | `EQCva-Of7acQdU_piADdlcbzsFtA-xJwZoctz8ZOXBdBoaB8` |
| Solana | `Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh` |
| Mantle | `0xc845b2894dbddd03858fd2d643b4ef725fe0849d` |

### Exchange Listings

| Exchange | Type | Pair |
|---|---|---|
| Kraken | CEX | NVDAX/USD |
| Orca (Solana) | DEX | NVDAX / USDC |

---

## Narrative, Category & Catalysts

NVDAX sits in the **tokenized stocks / RWA** narrative — bringing US equities on-chain for non-US users who want 24/7 access, DeFi composability (using tokenized equity as collateral), and fractional, borderless exposure. The xStocks lineup spans 50+ US stocks and ETFs, and "on-chain equities" was one of the most actively built corners of [[real-world-assets|RWA]] through 2025-2026. NVIDIA is a marquee name in the lineup given its role as the bellwether AI/semiconductor stock.

**Catalysts** for the tokenized-NVDA category: growth of the broader on-chain-equities trend, additional issuer entrants (Ondo, others) competing on the same names, DeFi integrations that accept tokenized stocks as collateral, and any regulatory clarity (positive or negative) on tokenized securities. Idiosyncratic catalysts for the *price* are simply NVDA's own drivers — AI-datacenter demand, GPU supply, earnings, and semiconductor-cycle dynamics.

**Macro context (2026-06):** the broad crypto tape is risk-off — Fear & Greed at 21 (Extreme Fear) and composite market-health 29/100 (bearish), though the long-horizon regime model has shifted toward **Bottoming / Accumulation**. NVDAX's price is driven mainly by NVDA, not crypto beta, but muted crypto risk appetite can thin on-chain RWA liquidity at the margin.

### History / timeline

- xStocks (Backed Finance) is the issuer brand under which NVDAX is published as part of the broader tokenized-US-equities lineup. This page's earliest market snapshot in the wiki is the [[coingecko-top-1000-2026-04-09|CoinGecko listing snapshot of 2026-04-09]].

*(No additional dated launch events are asserted here — only verified events should be added via the ingestion workflow.)*

---

## Risks

- **Issuer / custody risk:** Value depends on Backed Finance and its custodian actually holding the backing NVDA share — the dominant risk versus holding NVDA through a regulated broker with investor-protection schemes.
- **Redemption-gating risk:** Only whitelisted APs can mint/redeem; if that channel slows or closes under stress, peg arbitrage weakens and discounts can persist.
- **Overnight / weekend tracking gap:** NVDAX trades 24/7 while NVDA does not, so the token can diverge from the last NASDAQ print when the US market is closed; thin token liquidity can widen spreads.
- **Liquidity risk:** Market cap around $35M with modest on-chain depth — size orders move price.
- **Regulatory / securities-law risk:** Tokenized equities are an evolving regulatory category; access is geofenced to non-US users and could change.
- **Smart-contract / bridge risk:** NVDAX spans many chains, increasing exposure to smart-contract and cross-chain bridge vulnerabilities.
- **No shareholder rights:** Buyers seeking governance influence or formal shareholder protections will not get them via NVDAX.

> *On-chain holder distribution data requires blockchain analytics integration and is not yet ingested.*

---

## Trading Playbook (for a crypto trader)

- **Use case:** On-chain, dollar-denominated exposure to the AI/semiconductor bellwether without a US brokerage account; usable as DeFi collateral or as a high-beta growth sleeve inside an on-chain portfolio.
- **Character of the underlying:** NVDA is a **high-beta, high-momentum** mega-cap — large gaps around earnings and AI-demand headlines. Expect equity-style volatility, not stablecoin-style flatness.
- **Mind the basis:** Treat weekend/holiday quotes with caution — NVDAX can carry a premium/discount to the stale NVDA print that mean-reverts at the next US open. Avoid taking large positions into a long market closure unless you intend to hold the basis.
- **Execution:** Prefer trading during US market hours when AP arbitrage is active and spreads are tightest; size to the shallow on-chain depth and check the premium/discount to the underlying before sending size.
- **Alternatives:** If KYC and direct ownership are acceptable, the real NVDA share avoids wrapper/issuer risk; if leverage is the goal, an NVDA CFD or options may suit better than a spot wrapper.

---

## See Also

- [[nvidia]] — the underlying company (NASDAQ: NVDA)
- [[nvidia-ondo-tokenized-stock]] — alternative NVDA tokenization via Ondo
- [[backed-finance]] — the xStock issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- [[crypto-markets]] · [[solana]] · [[arbitrum]]
- [[circle-xstock]] · [[sp500-xstock]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge of Backed Finance's xStocks issuance model; no dedicated wiki source ingested yet.
