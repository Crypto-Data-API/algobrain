---
title: "Circle xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stocks]
aliases: ["CRCLX", "Circle xStock", "Circle Internet Group xStock"]
entity_type: protocol
headquarters: "Decentralized (issuer: Backed Finance AG, Switzerland)"
website: "https://xstocks.com/"
related: ["[[crypto-markets]]", "[[solana]]", "[[real-world-assets]]", "[[tokenized-stocks]]", "[[backed-finance]]", "[[circle]]", "[[circle-internet-group-ondo-tokenized-stock]]", "[[usdc]]", "[[tokenization]]"]
---

# Circle xStock

**Circle xStock** (ticker **CRCLX**) is a [[tokenized-stocks|tokenized equity]] issued by [[backed-finance|Backed Finance]] under its xStocks brand. Each CRCLX token is designed to track the price of one share of **Circle Internet Group (NYSE: CRCL)** — the company behind the [[usdc|USDC]] stablecoin (see [[circle]]) — and is collateralized 1:1 by the underlying share held in custody by a regulated third party. CRCLX is one of ~57 [[real-world-assets|real-world asset]] tokens in the Backed xStocks lineup and trades primarily on the [[solana]] network as an SPL token, with bridged ERC-20 deployments on other chains. It is a tokenized wrapper, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, CRCLX traded at **$80.63**, ranked **#492** by market capitalization with a market cap of **$44,976,277**. It was up **+1.01% over 24 hours** and **+1.18% over 7 days** — movements that mirror the underlying CRCL share price rather than independent crypto-market dynamics.

---

## What CRCLX Is

CRCLX is **not** Circle's own token and confers **no equity ownership, voting rights, or shareholder status**. It is a tracking instrument: a bearer-style token whose economic value is pegged to a single CRCL share held in custody. Holders gain price exposure to Circle Internet Group — and, where the issuer passes them through, economic equivalents of dividends — without holding the share through a traditional broker.

This makes CRCLX a [[real-world-assets|real-world asset (RWA)]] product: a blockchain wrapper around an off-chain security. It competes in the same category as Ondo Finance's tokenized equities (see [[circle-internet-group-ondo-tokenized-stock]]) but uses Backed Finance's issuance and custody framework. Two prices coexist:

- **The reference price** — what CRCL trades at on the NYSE during US market hours.
- **The token price** — what CRCLX trades at on crypto venues 24/7, which can drift when traditional markets are closed or on-chain liquidity is thin.

**Reflexive note:** CRCLX is unusual in this lineup — it is a *tokenized equity of a stablecoin issuer*, traded on the very rails (and often paired against USDC, Circle's own product) whose growth drives CRCL's fundamentals. A crypto trader using CRCLX is effectively taking an on-chain equity view on the health of the stablecoin/on-chain-dollar business itself.

---

## Architecture: How the Wrapper Works

### Issuer, custody and collateral

- **Issuer:** [[backed-finance|Backed Finance AG]], a Switzerland-based issuer of tokenized securities operating under EU/Swiss frameworks. xStocks are marketed to **non-US users** and are not offered to US persons.
- **1:1 backing:** For every CRCLX token minted, Backed holds one corresponding CRCL share (or a depositary-receipt equivalent) with a regulated third-party custodian, segregated from its own balance sheet, with published proof-of-reserves / collateral attestations. The token represents a legal claim to the value of that share.
- **Bankruptcy-remoteness:** The structure is designed to give holders a claim on the collateral even in issuer default — a contractual/legal claim, not the SIPC-protected brokerage ownership a US investor holding CRCL would have.

### Mint / redeem and access gating

- **Permissioned primary market:** Minting and redemption are restricted to KYC-verified, whitelisted parties who deposit or redeem the underlying. To mint, an AP delivers a CRCL share into custody; to redeem, the AP burns a token for the underlying value.
- **Permissionless secondary market:** Once minted, the token trades **permissionlessly** — any wallet can buy, sell, transfer, or use it in DeFi without KYC. Whitelisting is required only to mint or redeem.
- **Jurisdiction gating:** Geofenced to non-US/eligible jurisdictions; US persons excluded.

### Oracle, trading hours, corporate actions, settlement

- **Price tracking & oracle:** Secondary-market price closely tracks CRCL during US market hours; arbitrageurs in the primary market keep the token near the share's value. DeFi protocols consuming an oracle price for CRCLX face staleness risk when the NYSE is closed.
- **24/7 vs market hours:** CRCLX trades 24/7; CRCL trades only in US session hours. Outside US trading hours the token can trade on thinner liquidity, so spreads can widen and price can drift from the last NYSE print, then re-converge at the next US open.
- **Dividends / corporate actions:** Dividend treatment depends on the issuer's terms (typically reflected as an economic adjustment rather than a cash payout). The legal relationship is with the issuer, not the company.

### What holders do NOT get

- No voting rights or proxy participation at Circle.
- No direct shareholder registration; the legal relationship is with the issuer.
- No US investor-protection coverage (no SIPC).

---

## Tracking & Peg

CRCLX stays near the CRCL reference price through **primary-market arbitrage**: APs mint-and-sell at a premium, buy-and-redeem at a discount. Peg integrity holds best while the US market is open and APs are active. Sources of premium/discount and depeg risk:

- **Weekend / after-hours gap risk.** With CRCL closed, the token can trade away from the stale last print on sentiment or thin depth, opening a basis that reverts at the next US open.
- **Liquidity.** Off-hours on-chain depth is shallow; large orders move price and widen spreads.
- **Redemption friction.** If the AP/redemption channel slows under stress, discounts can persist.
- **Oracle staleness.** DeFi venues pricing CRCLX off an oracle may misprice it during closures.

---

## Comparison: Ways to Get Circle (CRCL) Exposure

| Dimension | **CRCLX (Backed xStock)** | **[[circle-internet-group-ondo-tokenized-stock\|CRCL (Ondo)]]** | **Real CRCL share (broker)** | **CRCL CFD** |
|---|---|---|---|---|
| **Issuer** | [[backed-finance\|Backed Finance]] | Ondo Global Markets | Exchange + broker | CFD broker |
| **Backing** | 1:1 CRCL share in custody | 1:1 CRCL share off-chain | Direct ownership | None (synthetic) |
| **Native chain** | Solana (SPL), multi-chain | Multi-chain | n/a | n/a |
| **Secondary trading** | Permissionless on-chain | KYC / transfer-restricted | Brokerage account | Broker platform |
| **Hours** | 24/7 | 24/7 mint/redeem (5d/wk) | US market hours | Broker hours |
| **Rights** | Economic only, no voting | Economic only, no voting | Full (voting) | None |
| **US persons** | Excluded | Excluded | Allowed | Often restricted |
| **Key risk** | Issuer/custody, peg | Issuer/custody, transfer limits | Counterparty minimal | Broker counterparty, leverage |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CRCLX |
| **Underlying** | Circle Internet Group (NYSE: CRCL) |
| **Issuer** | [[backed-finance|Backed Finance AG]] |
| **Market Cap Rank** | #492 |
| **Market Cap** | $44,976,277 |
| **Current Price** | $80.63 |
| **24h Change** | +1.01% |
| **7d Change** | +1.18% |
| **Native Chain** | [[solana]] (SPL); bridged ERC-20 |
| **Categories** | Tokenized Assets, Tokenized Stock, Real World Assets (RWA), BackedFi xStocks Ecosystem |
| **Website** | [https://xstocks.com/](https://xstocks.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## How & Where It Trades

**Native Chain:** Solana. Solana is the deepest venue; liquidity concentrates during US trading hours when arbitrageurs are active.

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `XsueG8BtpquVJX9LVLLEGuViXUungE6WmK5YZ3p3bd1` |
| Ethereum | `0xfebded1b0986a8ee107f5ab1a1c5a813491deceb` |
| Binance Smart Chain | `0xfebded1b0986a8ee107f5ab1a1c5a813491deceb` |
| Arbitrum One | `0xfebded1b0986a8ee107f5ab1a1c5a813491deceb` |

### Exchange Listings

| Exchange | Type | Pair |
|---|---|---|
| Kraken | CEX | CRCLX/USD |
| Orca (Solana) | DEX | CRCLX / USDC |

---

## Narrative, Category & Catalysts

CRCLX sits in the **tokenized stocks / RWA** narrative — bringing US equities on-chain for non-US users who want 24/7 access, DeFi composability, and fractional, borderless exposure. The xStocks lineup spans 50+ US stocks and ETFs. CRCLX is distinctive because the underlying, Circle, *is* a crypto-infrastructure company (the USDC issuer), so its equity fundamentals are tied to stablecoin adoption, on-chain dollar volumes, and interest income on reserves.

**Catalysts:** stablecoin/USDC growth and regulation (e.g., US stablecoin legislation), interest-rate moves that change reserve income, broader on-chain-equities adoption, issuer competition (Backed vs Ondo on the same name), and DeFi integrations accepting tokenized stocks as collateral.

**Macro context (2026-06):** the broad crypto tape is risk-off — Fear & Greed at 21-22 (Extreme Fear) — though the long-horizon regime model has shifted toward **Bottoming / Accumulation**. CRCLX's price is driven mainly by CRCL, not crypto beta, though Circle's fundamentals are themselves crypto-linked.

### History / timeline

- CRCLX is published by Backed Finance under the xStocks brand. The earliest market snapshot for this page in the wiki is the [[coingecko-top-1000-2026-04-09|CoinGecko listing snapshot of 2026-04-09]].

*(Only verified dated events are asserted; additional history should be added via the ingestion workflow.)*

---

## Risks and Considerations

- **Issuer / custody risk:** Holders depend on Backed Finance and its custodian to actually hold and segregate the backing shares. A failure, insolvency, or fraud at the issuer/custodian level is the dominant risk — unlike holding the share directly through a broker with investor-protection schemes.
- **Redemption-gating risk:** Only whitelisted APs can mint/redeem; if that channel slows under stress, peg arbitrage weakens and discounts can persist.
- **Tracking / liquidity risk:** Price tracks CRCL but is not guaranteed to equal it. Thin secondary liquidity, especially outside US market hours, can produce premiums/discounts to the underlying share price.
- **Regulatory / securities-law risk:** Tokenized equities sit in an evolving legal area. Availability is geofenced (non-US) and could be curtailed by regulators in any jurisdiction.
- **Smart-contract / bridge risk:** As an on-chain token spanning multiple chains, CRCLX is exposed to smart-contract and cross-chain bridge vulnerabilities.
- **No shareholder rights:** Buyers seeking governance influence or formal shareholder protections will not get them via CRCLX.

> *On-chain holder distribution data requires blockchain analytics integration and is not yet ingested.*

---

## Trading Playbook (for a crypto trader)

- **Use case:** Take an on-chain *equity* view on the stablecoin business — long CRCLX as a leveraged-to-USDC-adoption play, or hedge a stablecoin-heavy book against Circle-specific risk.
- **Character of the underlying:** CRCL is a financial/crypto-infrastructure equity whose value is sensitive to stablecoin regulation, USDC float, and interest rates on reserves. Expect event-driven moves around stablecoin legislation and rate decisions.
- **Mind the basis:** Weekend/holiday quotes can carry a premium/discount to the stale CRCL print that reverts at the next US open.
- **Execution:** Prefer US market hours for tightest spreads and active AP arbitrage; the natural pairing is CRCLX/USDC on Solana — note the reflexivity of pricing Circle's equity against Circle's own stablecoin. Size to shallow on-chain depth.
- **Alternatives:** Want direct ownership without wrapper risk? Hold the real share (KYC + US hours). Want the same on-chain exposure with a different access model? Compare the Ondo version.

---

## See Also

- [[circle]] — the underlying company (NYSE: CRCL), USDC issuer
- [[circle-internet-group-ondo-tokenized-stock]] — alternative CRCL tokenization via Ondo
- [[backed-finance]] — the xStock issuer
- [[usdc]] · [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- [[crypto-markets]] · [[solana]]
- [[nvidia-xstock]] · [[sp500-xstock]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge of Backed Finance's xStocks issuance model; no dedicated wiki source ingested yet.
