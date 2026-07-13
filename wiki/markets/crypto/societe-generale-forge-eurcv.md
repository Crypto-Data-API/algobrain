---
title: "EUR CoinVertible"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins, real-world-assets]
aliases: ["EURCV", "EUR CoinVertible", "Societe Generale FORGE EURCV", "SG-FORGE EURCV"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.sgforge.com/product/coinvertible/"
related: ["[[stablecoins]]", "[[real-world-assets]]", "[[crypto-markets]]", "[[euro-coin]]", "[[eurite]]", "[[ethereum]]"]
---

# EUR CoinVertible

**EUR CoinVertible** (ticker **EURCV**, native on [[ethereum|Ethereum]]) is a **euro-denominated, fiat-backed [[stablecoins|stablecoin]]** issued by **Société Générale-FORGE (SG-FORGE)**, the regulated digital-asset subsidiary of French bank Société Générale. It holds a 1:1 peg to the euro (EUR), is **MiCA-compliant**, and is one of the most institutionally credible euro stablecoins given its bank issuer. It is issued on Ethereum and bridged to Solana, Stellar, and the XRP Ledger.

> **Price note:** The snapshot price of ~$1.15 is **not a de-peg** — EURCV is pegged to the **euro**, and ~$1.15 simply reflects the EUR/USD exchange rate. Against the euro, EURCV trades at ~1.00.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | EURCV |
| **Issuer** | Société Générale-FORGE (SG-FORGE) |
| **Peg** | 1:1 to the euro (EUR) |
| **Current price** | $1.15 (≈ €1.00; USD price = EUR/USD FX) |
| **Market cap** | $135.49M |
| **Market cap rank** | #221 |
| **24h volume** | $16.42M |
| **24h change** | -0.05% |
| **Circulating supply** | ~118.26M EURCV |
| **Total supply** | ~118.26M EURCV |
| **All-time high** | $1.22 (2026-01-27) |
| **All-time low** | $0.9885 (2025-02-04) |
| **Chains** | Ethereum (native), Solana, Stellar, XRP Ledger |

> The "ATH $1.22 / ATL $0.99" range is mostly EUR/USD FX movement, not peg instability; in euro terms the token has tracked ~€1.00.

---

## Architecture: Mechanism & Backing

EURCV is a **fully fiat-reserve-backed stablecoin**: each token in circulation is backed by euro-denominated reserves held by SG-FORGE under a regulated framework. The decisive feature is its issuer — a **licensed subsidiary of a systemically important EU bank** — which places EURCV at the most institutionally conservative end of the euro-stablecoin spectrum, ahead of independent issuers like [[eurite|Eurite (EURI)]] and on par with Circle's [[euro-coin|EURC]].

- **Backing asset:** Euro cash and high-quality, liquid euro-denominated reserve assets held in segregated accounts, structured for bankruptcy-remoteness from the issuer so reserves are ring-fenced from SG-FORGE's own balance-sheet claims.
- **Peg model:** 1:1 to the euro, maintained via full reserve backing plus authorized mint/redeem at par for eligible participants.
- **Custody & attestation:** Reserves are managed within Société Générale's regulated banking infrastructure, with reserve reporting/attestation under MiCA's stablecoin (e-money token / asset-referenced token) regime.
- **Mint / redeem & gating:** Eligible, KYC'd **institutional** participants can mint and redeem at par (€1.00) directly with SG-FORGE; this permissioned primary channel anchors the peg. Secondary on-chain transfers are open and broader; retail typically accesses EURCV on DEX/CEX venues rather than via direct redemption.
- **Regulatory wrapper:** **MiCA-compliant** euro stablecoin from a licensed EU bank subsidiary — a key differentiator versus offshore or lightly-regulated stablecoins, and the basis for European institutions to treat it as a compliant on-chain euro.

See [[stablecoins]] for the category and [[real-world-assets]] for the broader on-chain RWA landscape.

---

## Tokenomics & Supply

EURCV supply is **fully reserve-backed and elastic** — it expands when institutions mint against euro deposits and contracts on redemption, so circulating supply tracks net euro inflows (circulating ≈ total ≈ 118.26M, market-cap/FDV ≈ 1.00). There is no fixed max supply, no emissions, and no algorithmic component; SG-FORGE earns yield on the reserve float. At ~$135M cap it is one of the larger euro stablecoins, though euro-stablecoin supply overall is a small fraction of the USD-stablecoin universe (USDT ≈ $186B, USDC ≈ $74.8B for reference).

---

## Comparison vs Euro Stablecoins

| Stablecoin | Issuer | Backing | Regulatory wrapper | Distinguishing trait |
|---|---|---|---|---|
| **EURCV** | SG-FORGE (Société Générale) | Euro cash + HQLA, segregated | MiCA-compliant | Issued by a systemic EU bank subsidiary |
| [[euro-coin\|EURC]] | Circle | Euro cash + short instruments | MiCA EMT (licensed in France) | Largest EUR stablecoin; deep liquidity |
| [[eurite\|EURI]] | Eurite | Euro cash-equivalents | Marketed MiCA-compliant | BNB-Chain native; Binance-listed |
| EURS (Stasis) | Stasis | Euro reserves | EU-based, attested | One of the oldest euro stablecoins |
| agEUR (Angle) | Angle Protocol | Crypto/RWA-backed (DeFi) | Decentralized | DeFi-native, not fiat-custodial |

EURCV's edge is issuer credibility (a major bank) and a clean MiCA wrapper; its weakness versus [[euro-coin|EURC]] is liquidity depth and venue breadth.

---

## How & Where It Trades / Is Used

- **Tracking:** Designed to hold €1.00. USD-quoted price moves with EUR/USD; euro-relative deviations are small and arbitraged via mint/redeem at par.
- **Hours:** Trades and transfers 24/7 on-chain; primary mint/redeem follows SG-FORGE's institutional operating schedule.
- **Venues:** Real secondary liquidity exists (24h volume ~$16.4M, the highest of this RWA cohort), including a Uniswap V3 (Ethereum) pool and other DEX/CEX listings across its supported chains (Ethereum, Solana, Stellar, XRP Ledger).
- **DeFi composability:** As an ERC-20 (and bridged equivalents), EURCV can be used in euro stable pools and as on-chain euro settlement; depth is improving but remains below USD stablecoins and below [[euro-coin|EURC]].
- **Use cases:** Regulated on-chain euro settlement for European institutions, euro-denominated tokenized-asset/RWA settlement, and FX/treasury rails on public chains.

---

## Narrative, Category & Catalysts

EURCV sits at the intersection of **regulated euro stablecoins** and **bank-issued on-chain money / RWA**. Catalysts: MiCA-driven demand for compliant euro settlement, European institutional adoption of public-chain rails, tokenized-asset and repo/settlement pilots using a bank-issued euro, and any push by European policymakers for a non-USD digital settlement asset. The counter-trend is the overwhelming dominance of USD stablecoins and the thinness of euro-stablecoin liquidity. In the current **Extreme Fear / bottoming-accumulation** macro regime (Fear & Greed 21), stablecoins often see relative demand as traders de-risk into cash-equivalents, but euro-stablecoin volumes remain a fraction of USD-stablecoin activity.

---

## History / Timeline

- **2023** — SG-FORGE first issued the CoinVertible euro stablecoin on Ethereum, an early example of a major regulated bank deploying a stablecoin on a public chain.
- **2024** — EU **MiCA** stablecoin provisions take effect; EURCV is positioned as a MiCA-compliant euro token, reinforcing SG-FORGE's regulated-issuer narrative.
- **2025–2026** — EURCV expands to additional chains (Solana, Stellar, XRP Ledger) and grows secondary liquidity; ATL $0.9885 (2025-02-04) and ATH $1.22 (2026-01-27) on the USD chart reflect EUR/USD FX, not peg breaks.

*(Only FX-driven price extrema above are dated from the market-data block; specific issuance dates beyond the general 2023 launch are not independently sourced here.)*

---

## Risks

- **De-peg risk (vs EUR):** If reserves are impaired or redemption is impeded, the token could trade below €1.00; the institutional bank backing materially lowers but does not eliminate this risk.
- **FX confusion:** Users measuring against USD may misread normal EUR/USD moves as a de-peg.
- **Issuer / reserve-counterparty risk:** Holders rely on SG-FORGE's reserve management, segregation, and redemption commitment.
- **Redemption-gating risk:** Direct mint/redeem at par is restricted to onboarded institutions; retail must exit via secondary markets, which are thinner.
- **Liquidity risk:** Thinner euro-stablecoin markets can widen spreads and slippage in stress versus USD stablecoins.
- **Regulatory risk:** Although MiCA gives a clear EU framework, rules continue to evolve and could alter issuance, reserve, or distribution terms.
- **Smart-contract / bridge risk:** Multi-chain deployment (Ethereum, Solana, Stellar, XRP Ledger) adds contract and bridge attack surface.

---

## Trading Playbook

- **Read the peg in euros, not dollars** — quote EURCV against EUR (target €1.00); ignore USD-chart swings that are just EUR/USD.
- **FX exposure** — a USD-based holder of EURCV is implicitly long EUR/USD; size accordingly or hedge.
- **Venue/depth** — best secondary depth in this euro cohort, but still small; size on-chain trades to pool depth.
- **Institutional angle** — most relevant as a compliant euro settlement asset; watch MiCA and SG-FORGE product news as catalysts.

---

## See Also

- [[stablecoins]]
- [[euro-coin]]
- [[eurite]]
- [[real-world-assets]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko market snapshot, 2026-06-21
- General market knowledge; no specific wiki source ingested yet.
