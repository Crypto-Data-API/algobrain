---
title: "GUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: good
tags: [crypto, stablecoins]
aliases: ["GUSD", "Gate USD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.gate.com/"
related: ["[[crypto-markets]]", "[[dai]]", "[[stablecoin]]", "[[stablecoins]]", "[[usdc]]", "[[usdt]]"]
---

# GUSD

**GUSD** is a yield-bearing USD stablecoin / principal-protected investment product issued within the **Gate** exchange ecosystem, pegged to the US dollar (1 USD target). Holders mint GUSD by depositing [[usdt]] or [[usdc]], and the token accrues a daily, dynamically-adjusted yield sourced from Gate ecosystem revenue, tokenized treasuries / real-world assets (RWA), and stablecoin-backed yield strategies. It is redeemable 1:1 back into USDT/USDC (subject to redemption fees).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | GUSD |
| **Price** | $0.998283 |
| **Market cap** | $149.6M |
| **Market-cap rank** | #211 |
| **24h volume** | $0.71M |
| **24h change** | -0.03% |
| **Circulating supply** | 149.79M GUSD |
| **Total supply** | 320.00M GUSD |
| **All-time high** | $1.022 |
| **All-time low** | $0.979237 |

---

## Peg & backing mechanism

GUSD is best described as a **yield-bearing stablecoin** rather than a pure fiat-collateralized one. The peg target is 1 USD, but the economic model is closer to a tokenized yield certificate:

- **Minting** — users stake USDT or USDC into the Gate product and receive GUSD as a yield-bearing certificate representing the value of their deposit. GUSD does not confer direct ownership of the underlying reserve assets.
- **Backing** — returns (and notionally the backing) are sourced from a blend of Gate ecosystem revenue, tokenized US Treasury bills / other RWA, and stablecoin-backed yield assets. The APR is adjusted dynamically with the performance of those revenue streams.
- **Redemption** — GUSD is converted back to USDT/USDC at a 1:1 ratio on redemption, with redemption fees applied.

Because backing and yield are managed by the Gate ecosystem rather than disclosed on-chain reserves, holders carry **counterparty / custodial exposure** to the issuer in a way they would not with an independently attested reserve. No public third-party reserve attestation is referenced in the source data. This places GUSD in the same broad category as exchange-issued yield products and centralized stablecoins, distinct from crypto-overcollateralized designs like [[dai]] and [[helio-protocol-hay|Lista USD]].

---

## How & where it trades

GUSD trades primarily inside the **Gate** ecosystem, where it functions both as a yield-earning deposit certificate and as collateral / a tradable asset. 24h reported volume is modest (~$0.71M) relative to its ~$149.6M market cap, consistent with a product whose primary use case is *holding for yield* rather than active spot trading. Liquidity outside the issuer's venue is limited, so large redemptions or transfers may be concentrated through the Gate platform.

---

## Risks

- **De-peg risk** — the token has historically traded in a tight ~$0.98–$1.02 band (ATH $1.022, ATL $0.979237), but yield-bearing models can drift below peg if redemption demand outpaces liquid reserves or if underlying yield assets impair.
- **Issuer / custodial risk** — backing and redemption depend entirely on the Gate ecosystem; there is no independent on-chain proof of reserves in the source data. A failure, freeze, or insolvency at the issuer is the dominant tail risk.
- **Yield-source risk** — returns depend on RWA / Treasury yields and ecosystem revenue, which can compress or turn negative, and tokenized-RWA strategies carry their own credit and operational risk.
- **Regulatory risk** — yield-bearing stablecoins distributed by exchanges face evolving scrutiny (e.g. securities classification of yield products) across jurisdictions.
- **Liquidity / concentration risk** — thin secondary-market depth means exit may be effectively gated through the issuer.

In a macro backdrop of Fear & Greed 23 ("Established Bear Market"), demand for exchange-based USD yield products can be sticky, but redemption pressure tends to rise during risk-off episodes.

---

## Related

- [[stablecoin]] / [[stablecoins]] — category overview
- [[usdc]], [[usdt]] — the assets used to mint and redeem GUSD
- [[dai]] — decentralized, crypto-overcollateralized peer
- [[frax-usd|Frax USD]], [[agora-dollar|AUSD]] — other USD stablecoin peers
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]

---
