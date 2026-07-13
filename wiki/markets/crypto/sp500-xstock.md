---
title: "SP500 xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stocks, sp500]
aliases: ["SPYX", "SP500 xStock", "S&P 500 xStock"]
entity_type: protocol
headquarters: "Decentralized (issuer: Backed Finance AG, Switzerland)"
website: "https://xstocks.com/"
related: ["[[crypto-markets]]", "[[arbitrum]]", "[[solana]]", "[[real-world-assets]]", "[[tokenized-stocks]]", "[[backed-finance]]", "[[ishares-core-s-p-500-etf-ondo-tokenized-etf]]", "[[spdr-s-p-500-etf-ondo-tokenized-etf]]"]
---

# SP500 xStock

**SP500 xStock** (SPYX) is a [[tokenized-stocks|tokenized ETF]] issued by [[backed-finance|Backed Finance]] under its xStocks brand. Each SPYX token is designed to track the price of the **SPDR S&P 500 ETF Trust (NYSE Arca: SPY)** — the most widely held proxy for the **S&P 500** index — and is collateralized 1:1 by the underlying SPY shares held in custody. SPYX gives non-US users on-chain exposure to broad US large-cap equity beta as an SPL/ERC-20 token, composable across DeFi.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, SPYX traded at **$750.19**, ranked **#559** by market capitalization with a market cap of **$36,719,225**. It was **-0.13% over 24 hours** and **+0.67% over 7 days** — low-volatility moves consistent with a broad-index tracker mirroring SPY rather than a speculative crypto asset. (For regime context only: at the 2026-06-22 snapshot the broad crypto tape was risk-off — Fear & Greed at 21 / Extreme Fear, market-health 29/100, BTC ≈ $64,568 — but SPYX's value is driven by the US equity session, not the crypto cycle.)

---

## What SPYX Is

SPYX is a tokenized wrapper around the SPDR S&P 500 ETF (SPY). It is **not** a fund of its own, and it confers **no fund-shareholder rights** — it is a tracking token whose value is pegged to one SPY share held in custody. Because SPY itself holds the 500 constituents of the S&P 500, SPYX effectively offers diversified, single-token exposure to the US large-cap market for users who cannot or do not want to access SPY through a traditional broker. The economics chain through two wrappers: **S&P 500 index → SPY ETF → SPYX token**.

This places SPYX in the [[real-world-assets|real-world asset (RWA)]] category, alongside competing tokenized S&P 500 ETF products from [[ondo-finance|Ondo Global Markets]] (see [[ishares-core-s-p-500-etf-ondo-tokenized-etf]] and [[spdr-s-p-500-etf-ondo-tokenized-etf]]). Unlike single-name tokenized equities such as [[tesla-ondo-tokenized-stock|TSLAon]] or [[nvidia-xstock|NVDAx]], SPYX is a **broad-index** wrapper: its value reflects 500 constituents, so it is structurally lower-volatility and is the natural on-chain instrument for US-beta exposure rather than a directional single-stock bet.

### Architecture — how the wrapper works (Backed Finance model)

- **Issuer:** [[backed-finance|Backed Finance AG]], a Switzerland-based issuer of tokenized securities operating under EU/Swiss frameworks (issuance documented under a base prospectus approved in the EEA). xStocks target **non-US users** and are not offered to US persons.
- **1:1 backing / proof of reserves:** Each SPYX token is backed by one corresponding SPY share (or depositary-receipt equivalent) held with a regulated third-party custodian, giving the holder a legal claim to the value of that share. Backed publishes reserve attestations for its xStocks line so that on-chain supply can be reconciled against custodied shares.
- **Token form & settlement chains:** SPYX is issued as a [[solana|Solana]] SPL token natively, with ERC-20 representations on Ethereum, BNB Chain, and [[arbitrum|Arbitrum One]]. The same economic claim is fungible across these deployments via the issuer's bridging.
- **Mint / redeem & KYC gating:** Mint and redeem (the **primary market**) are restricted to KYC-verified, whitelisted parties. To mint, an authorised participant delivers SPY into custody and receives newly issued SPYX; to redeem, they burn SPYX and receive the underlying value. Once issued, SPYX trades **permissionlessly on the secondary market** and can be used in DeFi protocols like any other token.
- **Oracle / price feed:** On-chain venues and integrators reference the underlying SPY/S&P 500 price through market data and oracle feeds; the token's fair value is the underlying NAV, and arbitrage by primary participants is the mechanism that enforces it.
- **24/7 token vs market-hours underlying:** SPYX tracks SPY closely during US market hours via primary-market arbitrage. Because the S&P 500 trades only during the US session while the token trades 24/7, SPYX can drift from the last SPY print overnight and on weekends, when there is no live underlying reference.
- **Distributions / expense handling:** S&P 500 dividends and SPY's expense ratio are reflected through the issuer's terms (typically an economic adjustment to the token rather than a cash payout to holders).

### What holders do NOT get

- No fund voting rights or distributions of the kind a registered SPY holder receives directly.
- No direct ETF-shareholder registration; the legal relationship is with the issuer.
- Distribution/dividend treatment depends on the issuer's terms (typically an economic adjustment rather than a cash payout).

---

## Tracking & Peg

SPYX's fair value is the SPY share price (and thus the S&P 500). The peg is maintained by **primary-market arbitrage**: if SPYX trades at a premium to SPY, whitelisted participants mint and sell; if at a discount, they buy and redeem. This keeps tracking error tight while the US market is open and arbitrageurs are active.

- **Premium / discount:** Small deviations are normal on thin secondary liquidity; they compress when US markets reopen and primary participants can act.
- **Weekend-gap risk:** The dominant structural basis risk. When the NYSE is closed (nights, weekends, US holidays), there is no live SPY reference. SPYX can drift on crypto-market sentiment and then "snap" to the new SPY print at the next US open, so a holder buying over a weekend is effectively pricing a forward.
- **Broad-index advantage:** Because SPY is a 500-name basket, single-stock gap events have far less impact on SPYX than on a single-name wrapper — tracking is generally cleaner than for volatile single equities.

---

## Comparison: SPYX vs alternatives

| Dimension | **SPYX** (Backed xStock) | **[[spdr-s-p-500-etf-ondo-tokenized-etf\|SPYon]]** (Ondo) | **Holding real SPY** (broker) | **Single-name token** (e.g. [[tesla-ondo-tokenized-stock\|TSLAon]]) |
|---|---|---|---|---|
| Underlying | SPY / S&P 500 (500 names) | SPY / S&P 500 (500 names) | SPY / S&P 500 (500 names) | One company |
| Issuer | [[backed-finance\|Backed Finance]] | [[ondo-finance\|Ondo Global Markets]] | State Street (SPY sponsor) | Ondo / Backed |
| Form | SPL + ERC-20, on-chain | ERC-20 + multi-chain, on-chain | Brokerage security | On-chain token |
| Native chain | Solana (also ETH/BNB/Arbitrum) | Ethereum (also BNB/Solana) | n/a | Ethereum / Solana |
| Trading hours | 24/7 | 24/7 | US market hours | 24/7 |
| Shareholder rights | None (economic claim) | None (economic claim) | Full (via ETF) | None |
| US persons | Not offered | Not offered | Available | Not offered |
| Diversification | High (broad index) | High (broad index) | High (broad index) | None (concentrated) |
| Main extra risk | Issuer/custody, weekend gap | Issuer/custody, weekend gap | None beyond market | Issuer + high single-name vol |

The choice between SPYX and SPYon is mainly **issuer/venue/chain preference and liquidity** — both target the same SPY exposure for non-US users. Versus a real broker SPY position, the trade-off is on-chain composability and 24/7 access against added issuer, custody and tracking risk.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SPYX |
| **Underlying** | SPDR S&P 500 ETF Trust (SPY) — tracks the S&P 500 |
| **Issuer** | [[backed-finance|Backed Finance AG]] |
| **Market Cap Rank** | #559 |
| **Market Cap** | $36,719,225 |
| **Current Price** | $750.19 |
| **24h Change** | -0.13% |
| **7d Change** | +0.67% |
| **Native Chain** | [[solana]] (SPL); bridged ERC-20 incl. [[arbitrum]] |
| **Categories** | Tokenized Assets, Tokenized Stock, Tokenized ETFs, Real World Assets (RWA), BackedFi xStocks Ecosystem |
| **Website** | [https://xstocks.com/](https://xstocks.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Platform & Chain Information

**Native Chain:** Solana (SPL); bridged to multiple EVM chains.

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0x90a2a4c76b5d8c0bc892a69ea28aa775a8f2dd48` |
| Ethereum | `0x90a2a4c76b5d8c0bc892a69ea28aa775a8f2dd48` |
| Binance Smart Chain | `0x90a2a4c76b5d8c0bc892a69ea28aa775a8f2dd48` |
| Solana | `XsoCS1TfEyfFhfvj8EtZ528L3CaKBDBRqRapnBbDF2W` |

---

## How & Where It Trades

**Native Chain:** Solana (SPL); bridged to multiple EVM chains.

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | SPYX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | XSOCS1TFEYFFHFVJ8ETZ528L3CAKBDBRQRAPNBBDF2W/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

Most secondary liquidity sits on Solana DEXs (e.g. Orca) where SPYX is issued natively, with Kraken providing a CEX venue for the xStocks line. Liquidity is concentrated and thinner than for the underlying SPY; large orders move the token price and spreads widen markedly when the US market is closed. The ERC-20/Arbitrum/BNB representations exist for composability but tend to carry shallower books than the native Solana market.

---

## Narrative & Catalysts

SPYX sits at the centre of the **[[real-world-assets|RWA tokenization]]** narrative — bringing the single most recognised US equity benchmark on-chain as a composable token. Key drivers:

- **On-chain index access for non-US users:** SPYX offers broad US large-cap beta to wallets that cannot access SPY through a US broker, in a form usable as DeFi collateral and in 24/7 markets.
- **RWA growth wave (2024–2026):** Tokenized equities and ETFs expanded sharply as issuers like [[backed-finance|Backed Finance]] and [[ondo-finance|Ondo]] competed to wrap the most liquid TradFi instruments. Broad-index wrappers (S&P 500, Nasdaq-100) are the flagship products of that wave.
- **Composability:** Unlike a brokerage SPY position, SPYX can be lent, used as collateral, or paired in liquidity pools on-chain — the core argument for tokenizing index exposure.

### History / timeline

- **2025:** Backed Finance launches the **xStocks** brand, tokenizing major US equities and ETFs as Solana-native SPL tokens with EVM representations; SPYX (SPY / S&P 500) is among the flagship index wrappers.
- **2026-04-09:** SPYX captured in the wiki's CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]).
- **2026-06-21:** Market-data snapshot — $750.19, market cap $36.72M, rank #559.

> *Only dated, verifiable events are listed; precise launch dates beyond the year are not asserted absent a confirmed source.*

---

## Risks (structured)

- **Issuer / custodian counterparty risk:** Value depends entirely on [[backed-finance|Backed Finance]] and its custodian holding the backing SPY shares. Issuer or custodian failure — or a break in proof-of-reserves — is the primary risk versus holding SPY through a regulated broker.
- **Redemption-gating / access risk:** Mint and redeem are permissioned and KYC-gated to whitelisted parties. Ordinary holders cannot themselves redeem; if primary participants withdraw, the peg-enforcement mechanism weakens and the token can trade away from NAV.
- **Liquidity risk:** Secondary liquidity is thin and concentrated (modest 24h volume); spreads widen and slippage rises on size, especially outside US hours.
- **Tracking-error / weekend-gap risk:** SPYX trades 24/7 but the S&P 500 does not. Pricing can diverge from SPY when the underlying market is closed, snapping back at the next US open.
- **Regulatory risk:** Tokenized ETFs are an evolving regulatory category; access is geofenced to non-US users and could change.
- **Smart-contract / bridge risk:** As a multi-chain token, SPYX carries smart-contract and cross-chain bridge exposure.
- **No fund-holder protections:** Buyers do not get the investor protections associated with holding the ETF directly.

> *On-chain holder distribution data requires blockchain analytics integration and is not yet ingested.*

---

## Trading Playbook

- **On-chain US-beta core:** Use SPYX as a broad-index, lower-volatility building block for non-US, on-chain portfolios — the closest token to "owning the US market" without a broker.
- **Crypto-portfolio hedge / diversifier:** Because its return is driven by the US equity session rather than the crypto cycle, SPYX can dampen a crypto-heavy book's volatility (note: equity and crypto correlations are regime-dependent and can rise in broad risk-off events).
- **Index vs single-name:** Prefer SPYX over single-name tokens (e.g. [[tesla-ondo-tokenized-stock|TSLAon]], [[nvidia-xstock|NVDAx]]) when the goal is diversified beta rather than a directional company bet.
- **Mind the weekend gap:** Avoid taking large positions over US-market closures expecting NAV pricing; the token can drift on crypto sentiment and re-rate at the next open.
- **Liquidity-aware sizing:** Check on-chain depth (primarily Solana/Orca) before sizing; thin books mean meaningful price impact on large orders.

---

## See Also

- [[crypto-markets]]
- [[arbitrum]]
- [[solana]]
- [[real-world-assets]]
- [[tokenized-stocks]]
- [[backed-finance]]
- [[circle-xstock]]
- [[nvidia-xstock]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge of Backed Finance's xStocks issuance model; no dedicated wiki source ingested yet.
