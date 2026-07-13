---
title: "MicroStrategy xStock"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, stocks, nasdaq, tokenization]
aliases: ["MSTRX", "Strategy xStock", "MicroStrategy Tokenized Stock"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://xstocks.com/"
related: ["[[real-world-assets]]", "[[tokenized-stocks]]", "[[backed-finance]]", "[[microstrategy]]", "[[bitcoin]]", "[[crypto-markets]]", "[[arbitrum]]", "[[solana]]", "[[tokenization]]"]
---

# MicroStrategy xStock

**MicroStrategy xStock** (ticker **MSTRX**) is a tokenized equity ("xStock") issued by [[backed-finance|Backed Finance]] that tracks the share price of **MicroStrategy** — the company that rebranded to **Strategy** in 2025 — listed on the Nasdaq as **NASDAQ: MSTR**. MSTRX is **not** the underlying stock itself: it is an on-chain wrapper whose value is designed to follow the off-chain MSTR share, backed 1:1 by real shares held in custody by the issuer. Issued as an SPL token on [[solana]] with bridged ERC-20 deployments (Arbitrum, Ethereum, BNB Chain), it is a [[real-world-assets|real-world asset (RWA)]] token, not an independent cryptocurrency.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, MSTRX trades at **$117.75**, ranks **#695** by market capitalization with a market cap of **$26,516,501**, and is **+2.43%** over 24 hours and **-7.47%** over the trailing 7 days. The broader market context is risk-off: BTC sits near $64,180 and the Crypto Fear & Greed Index reads 22 (Extreme Fear).

---

## What MSTRX Actually Is

MSTRX is a **[[tokenization|tokenized]] stock** — a blockchain token engineered to mirror the economics of a single underlying equity. It belongs to the **xStock** product line operated by [[backed-finance|Backed Finance]], a Switzerland-based issuer of tokenized securities. For every MSTRX token in circulation, Backed (via its custodial arrangements) holds a corresponding MSTR share off-chain. The token's price therefore *tracks* the share price; it does not set it.

Because the subject is a wrapper, two distinct prices exist:

- **The reference price** — what MSTR trades at on the Nasdaq during US market hours.
- **The token price** — what MSTRX trades at on crypto venues 24/7, which can drift from the reference price when traditional markets are closed (nights, weekends, holidays) or when secondary-market liquidity is thin.

### A leveraged-Bitcoin proxy, wrapped on-chain

The underlying company deserves special note. [[microstrategy|MicroStrategy / Strategy]] is itself a **leveraged [[bitcoin|Bitcoin]] proxy equity**: it has financed large Bitcoin purchases with equity and convertible debt, so MSTR shares behave like a geared bet on BTC rather than a software business. MSTRX therefore stacks two layers of exposure — the tokenized-wrapper layer (Backed, custody, chain) on top of an already-volatile, Bitcoin-correlated equity. Holders are exposed to BTC price moves *amplified* by Strategy's balance-sheet leverage, plus the tracking and issuer risks of the wrapper. This makes MSTRX one of the highest-beta names in the xStocks lineup.

---

## Key Facts

| Field | Detail |
|---|---|
| **Token ticker** | MSTRX |
| **Underlying** | MicroStrategy / Strategy (NASDAQ: MSTR) |
| **Issuer** | [[backed-finance|Backed Finance]] (xStocks) |
| **Backing** | 1:1 real MSTR shares held in custody |
| **Standard** | SPL (Solana) / ERC-20 (EVM chains) |
| **Market cap rank** | #695 |
| **Market cap** | $26,516,501 |
| **Current price** | $117.75 |
| **24h change** | +2.43% |
| **7d change** | -7.47% |
| **Website** | [https://xstocks.com/](https://xstocks.com/) |

---

## Architecture: How the Wrapper Works

### Issuer, custody and collateral

- **Issuer:** [[backed-finance|Backed Finance AG]], Switzerland-based, operating under EU/Swiss frameworks. xStocks target **non-US users** and are not offered to US persons.
- **1:1 backing:** For every MSTRX token, Backed holds one corresponding MSTR share with a regulated third-party custodian, segregated from its own balance sheet, with published proof-of-reserves / collateral attestations.
- **Bankruptcy-remoteness:** The structure is designed to give holders a claim on the collateral even in issuer default — a contractual/legal claim, not the SIPC-protected brokerage ownership a US investor holding MSTR would have.

### Mint / redeem and access gating

- **Primary market (permissioned):** Only KYC'd, whitelisted institutional participants can **mint** new MSTRX (by delivering MSTR shares into custody) or **redeem** MSTRX (burning tokens to receive the underlying value). This gatekeeping keeps the token supply collateralized 1:1.
- **Secondary market (permissionless):** Once minted, MSTRX trades freely on centralized exchanges (e.g., Kraken) and DeFi venues (e.g., Orca on Solana). Any wallet can buy or sell; you do not need to be whitelisted to *hold or trade* the token, only to mint or redeem it.
- **Jurisdiction gating:** Geofenced to non-US/eligible jurisdictions; US persons excluded.

This permissioned-primary / permissionless-secondary structure is the defining mechanic of Backed's xStocks and the main thing that distinguishes them from simply owning MSTR through a broker.

### Oracle, trading hours, corporate actions, settlement

- **Tracking & oracle:** MSTRX tracks MSTR through primary-participant arbitrage. DeFi protocols consuming an oracle price face staleness risk when the Nasdaq is closed.
- **24/7 vs market hours:** MSTRX trades 24/7; MSTR trades only in US session hours. The token can drift while MSTR is closed and snap back at the next US open — and because the underlying is BTC-geared, BTC's own 24/7 moves over a weekend can drag MSTRX even though MSTR itself is shut.
- **Dividends / corporate actions:** Strategy/MSTR pays no common dividend, so dividend pass-through is not a live consideration. Splits and other corporate actions are reflected by the issuer via token adjustment rather than direct shareholder entitlement.
- **Settlement chains:** Native SPL on Solana; bridged ERC-20 on Arbitrum, Ethereum, and BNB Chain.

### No shareholder rights

Holding MSTRX confers **economic exposure only**. Token holders do **not** receive voting rights and are not registered shareholders of Strategy.

---

## Tracking & Peg

MSTRX stays close to MSTR through **arbitrage by primary participants**. If the token trades at a premium to the underlying, whitelisted parties mint cheaply (delivering shares) and sell tokens; if it trades at a discount, they buy tokens and redeem for shares. This keeps the peg honest *during* hours when the underlying market is open and primary participants are active. Sources of premium/discount and depeg risk:

- **Weekend / after-hours gap risk** — amplified here because BTC trades 24/7. MSTRX can move sharply on weekend BTC action while MSTR is closed, opening a wide basis to the stale MSTR print.
- **Liquidity** — with a ~$26.5M cap and modest on-chain volume, spreads widen and size moves price.
- **Redemption friction** — if the AP channel slows under stress, discounts can persist.
- **Oracle staleness** — DeFi venues pricing MSTRX off an oracle may misprice it during closures.

---

## Comparison: Ways to Get a Leveraged-BTC / MSTR Exposure

| Dimension | **MSTRX (Backed xStock)** | **Real MSTR share (broker)** | **Hold BTC directly** | **MSTR CFD / leveraged ETF** |
|---|---|---|---|---|
| **Exposure** | MSTR (geared BTC proxy) | MSTR (geared BTC proxy) | Spot BTC (1x) | Geared MSTR |
| **Backing** | 1:1 MSTR share in custody | Direct ownership | Self-custody / exchange | None (synthetic / fund) |
| **Native chain** | Solana (SPL), multi-chain | n/a | Bitcoin | n/a |
| **Secondary trading** | Permissionless on-chain | Brokerage account | Crypto exchange | Broker / exchange |
| **Hours** | 24/7 | US market hours | 24/7 | Broker hours |
| **Leverage** | Indirect (via MSTR's balance sheet) | Indirect | None | Built-in |
| **US persons** | Excluded | Allowed | Allowed | Often restricted |
| **Key risk** | Issuer/custody, peg, BTC-gearing | BTC-gearing, equity | Custody, BTC vol | Decay, leverage |

For a crypto trader, MSTRX is a way to express a *leveraged-BTC* view on-chain in dollars, without using a derivatives account — but with wrapper risk on top of MSTR's own balance-sheet gearing.

---

## How & Where It Trades

| Venue | Type | Pair |
|---|---|---|
| Kraken | CEX | MSTRX/USD |
| Orca (Solana) | DEX | MSTRX / USDC |

Solana is the deepest venue. Liquidity concentrates during US trading hours when arbitrageurs are active; off-hours depth is shallow.

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0xae2f842ef90c0d5213259ab82639d5bbf649b08e` |
| Binance Smart Chain | `0xae2f842ef90c0d5213259ab82639d5bbf649b08e` |
| Ethereum | `0xae2f842ef90c0d5213259ab82639d5bbf649b08e` |
| Solana | `XsP7xzNPvEHS1m6qfanPUGjNmdnmsLKEoNAnHjdxxyZ` |

---

## Narrative, Category & Catalysts

MSTRX sits in the **tokenized stocks / RWA** narrative, with a twist: it is the on-chain way to hold the market's best-known **leveraged-Bitcoin equity**. The xStocks lineup spans 50+ US stocks and ETFs; MSTR/Strategy is uniquely relevant to crypto users because its price is dominated by BTC and its balance-sheet leverage.

**Catalysts:** BTC's own price action (the primary driver), Strategy's capital-raising/BTC-purchase announcements, broader on-chain-equities adoption, DeFi integrations accepting tokenized stocks as collateral, and regulatory clarity on tokenized securities.

**Macro context (2026-06):** crypto is risk-off — Fear & Greed at 21-22 (Extreme Fear), composite market-health 29/100 — though the long-horizon regime model has shifted toward **Bottoming / Accumulation**, with BTC ~$64.6k (~16% below its 200-day MA). Because MSTRX is a geared BTC proxy, it is especially sensitive to which way this transitional tape resolves.

### History / timeline

- MicroStrategy rebranded to **Strategy** in 2025. MSTRX is published by Backed Finance under the xStocks brand. The earliest market snapshot for this page in the wiki is the [[coingecko-top-1000-2026-04-09|CoinGecko listing snapshot of 2026-04-09]].

*(Only verified dated events are asserted; additional history should be added via the ingestion workflow.)*

---

## Risks

- **Off-chain dependency.** MSTRX is only as good as the off-chain MSTR shares backing it and the systems that price and custody them. If the underlying feed or custody breaks, the peg breaks.
- **Issuer & custody risk.** Holders rely entirely on [[backed-finance|Backed Finance]] and its custodians to hold real shares 1:1 and honor redemptions — a counterparty/centralization risk absent from holding MSTR in a brokerage account, without US investor-protection coverage.
- **Redemption-gating risk.** Only whitelisted APs can mint/redeem; if that channel slows under stress, peg arbitrage weakens and discounts can persist.
- **Stacked volatility.** Because [[microstrategy|Strategy]] is a leveraged [[bitcoin|Bitcoin]] proxy, MSTRX inherits amplified BTC volatility *plus* wrapper risk — a notably high-beta instrument.
- **Weekend / after-hours tracking gaps.** Crypto trades 24/7 but the Nasdaq does not. With BTC moving over weekends while MSTR is closed, MSTRX can open a wide basis and snap back at the next US open.
- **Regulatory / securities-law risk.** xStocks are marketed to **non-US** users and positioned around EU rules; availability and legality vary by jurisdiction.
- **Liquidity risk.** With a market cap around $26.5M and modest on-chain volume, spreads can widen and large orders can move the token price.
- **No shareholder rights / no recourse.** No voting, and token holders are not the registered owners of the underlying shares.

---

## Trading Playbook (for a crypto trader)

- **Use case:** Express a **leveraged-long-BTC** view on-chain, in dollars, without a derivatives account — MSTRX rises faster than spot BTC in a rally and falls faster in a drawdown, courtesy of Strategy's balance-sheet gearing.
- **Character of the underlying:** Highest-beta name in this set. Expect amplified BTC swings; treat MSTRX as a geared crypto position, not a sleepy equity.
- **Mind the (double) basis:** Two gaps to watch — (1) MSTRX vs the stale MSTR print over closures, and (2) MSTR's own premium/discount to its BTC net asset value. Weekend BTC moves can dislocate MSTRX well before the US open re-anchors it.
- **Execution:** Prefer US market hours for tightest spreads and active AP arbitrage; size to shallow on-chain depth; consider hedging the BTC leg if you only want the MSTR-specific spread.
- **Alternatives:** Want clean 1x BTC? Hold spot. Want leverage with daily-rebalance decay risk? A leveraged MSTR ETF or perp behaves differently. MSTRX is the "geared BTC equity, wrapped on-chain" option.

---

## See Also

- [[microstrategy]] — the underlying company (Strategy, NASDAQ: MSTR)
- [[backed-finance]] — the xStock issuer
- [[tokenized-stocks]] · [[real-world-assets]] · [[tokenization]]
- [[bitcoin]] — the asset Strategy's equity is geared to
- [[crypto-markets]] · [[arbitrum]] · [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet for the xStocks product mechanics.
