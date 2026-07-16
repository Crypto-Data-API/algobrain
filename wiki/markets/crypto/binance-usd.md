---
title: "Binance USD"
type: market
created: 2026-04-09
updated: 2026-07-16
status: good
tags: [crypto, stablecoin]
aliases: ["BUSD", "Binance USD"]
entity_type: protocol
headquarters: "New York, USA (issuer Paxos)"
website: "https://www.paxos.com/busd/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[paxos-standard]]", "[[paxos]]", "[[stablecoin]]", "[[tether]]", "[[usdc]]"]
---

# Binance USD

**Binance USD** (BUSD) is a fiat-collateralized [[stablecoin]] formerly pegged 1:1 to the U.S. dollar, **issued by [[paxos|Paxos Trust Company]]** under license to Binance and originally approved by the New York State Department of Financial Services (NYDFS). BUSD is **no longer being minted**: in February 2023 NYDFS ordered Paxos to stop issuing new BUSD, and the token has been in long-term wind-down ever since. The figures below describe a contracting, legacy stablecoin, not an actively growing one.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, BUSD trades at **$0.999427**, holds market-cap rank **#545**, and carries a market capitalization of **$37,820,798** (**24h +0.07%**, **7d +0.18%**). The peg has held close to $1, but the residual market cap is a small fraction of BUSD's ~$16B+ peak before the 2023 wind-down.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BUSD |
| **Price (2026-06-21)** | $0.999427 |
| **Market Cap Rank** | #545 |
| **Market Cap** | $37,820,798 |
| **24h Change** | +0.07% |
| **7d Change** | +0.18% |
| **Peg target** | 1 BUSD = 1 USD (legacy) |
| **Backing model** | Fiat reserves (during active issuance) |
| **Issuer** | [[paxos\|Paxos Trust Company]] (NOT Binance directly) |
| **Status** | Minting halted Feb 2023; wind-down |
| **Native chain** | [[ethereum\|Ethereum]] (ERC-20) |

---

## History and Regulatory Wind-Down

BUSD launched in 2019 as a partnership: **Paxos** was the regulated issuer and reserve custodian, while **Binance** branded and distributed the token. At its peak in late 2022, BUSD was among the largest stablecoins by market cap.

On **13 February 2023**, NYDFS directed Paxos to **cease minting new BUSD**, citing unresolved issues in the Paxos–Binance relationship and oversight of the token. Around the same time the U.S. SEC issued Paxos a Wells notice alleging BUSD was an unregistered security (a claim Paxos disputed). Paxos committed to:

- Stopping all new BUSD issuance.
- Continuing to **honor redemptions** of existing BUSD 1:1 for USD through a defined wind-down period, supported by reserves.

Because no new tokens can be created and holders steadily redeem, BUSD's supply and market cap have declined monotonically toward the ~$38M residual seen on 2026-06-21. Binance itself has migrated users toward other stablecoins (including its own branded alternatives and [[tether]]/[[usdc]]).

This history is the defining fact about BUSD: it is a **regulator-ordered sunset of a fiat-backed stablecoin**, and a case study in how stablecoins carry issuer and regulatory risk even when reserves are sound.

---

## Backing and Peg-Maintenance Mechanism

During active issuance, BUSD was a **fiat-reserve stablecoin**: Paxos held U.S. dollars and short-dated cash-equivalent reserves against circulating BUSD and published attestations. The peg was maintained through Paxos's **mint/redeem at par** loop. With minting now closed, peg stability is anchored almost entirely by the **ongoing 1:1 redemption guarantee** — holders can still redeem residual BUSD with Paxos, which keeps the secondary-market price (currently $0.999427) pinned near $1.

---

## Trading and Liquidity

Major exchanges have delisted or de-emphasized BUSD spot pairs since the wind-down, and on-chain liquidity has thinned. Remaining activity is largely redemption-driven plus residual DEX pools on [[ethereum|Ethereum]]. Holders are generally advised to redeem or convert to an actively maintained stablecoin rather than rely on long-term BUSD liquidity.

---

## Risks

- **Wind-down / discontinuation risk** — BUSD is being retired; supply only shrinks and venue support continues to erode.
- **Redemption-window risk** — Peg integrity depends on Paxos continuing to honor redemptions; holders should not assume indefinite redeemability.
- **Liquidity risk** — Falling volume and delistings widen spreads and increase slippage.
- **Regulatory risk (realized)** — BUSD is itself the example: NYDFS ordered minting to stop and the SEC alleged it was a security.
- **Smart-contract risk** — Standard ERC-20 exposure.

See [[stablecoin]] and [[depeg]] for the general framework, and [[paxos-standard|USDP/Pax Dollar]] for the issuer's still-active dollar stablecoin.

---

## Related

- [[stablecoin]]
- [[paxos]]
- [[paxos-standard]]
- [[tether]]
- [[usdc]]
- [[depeg]]
- [[collateralization]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge (Paxos/Binance issuance, Feb 2023 NYDFS wind-down order); no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
