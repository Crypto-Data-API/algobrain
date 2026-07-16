---
title: "Cygnus Finance Global USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["CGUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.cygnus.finance/"
related: ["[[base]]", "[[crypto-markets]]", "[[real-world-assets]]", "[[stablecoins]]"]
---

# Cygnus Finance Global USD

**Cygnus Finance Global USD** (ticker CGUSD) is an interest-bearing dollar stablecoin issued by the **Cygnus Finance** protocol on **[[base|Base]]**. It targets a peg of **1 CGUSD ≈ US$1** and is a **[[real-world-assets|real-world-asset (RWA)]]** stablecoin backed by **short-term U.S. Treasury debt**. Cygnus describes itself as the first native interest-bearing stablecoin and the first native RWA protocol on Base. As a yield-bearing tokenized-Treasury dollar, CGUSD competes with [[usdc]] (non-yielding fiat dollar) and the tokenized-Treasury cohort rather than with synthetic dollars like [[ethena-usde|USDe]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | CGUSD |
| **Price** | $0.99739 |
| **Peg target** | US$1.00 |
| **Market cap** | $75.70M |
| **Market-cap rank** | #330 |
| **24h volume** | $1.09 |
| **24h change** | +0.00% |
| **Circulating supply** | 75.90M CGUSD |
| **Total supply** | 75.90M CGUSD |
| **All-time high** | $1.089 (2025-06-06) |
| **All-time low** | $0.724325 (2025-09-29) |

CGUSD traded near peg at the snapshot (~$0.9974), but **24h volume was effectively nil (~$1)** — secondary trading is essentially dormant, so the quoted price is driven by primary mint/redeem rather than market activity. The ATL of ~$0.72 (2025-09-29) marks a severe historical de-peg.

---

## Architecture — peg, backing & yield mechanism

CGUSD is a **[[real-world-assets|real-world-asset (RWA)]]** stablecoin — a tokenized claim on a short-duration U.S. Treasury reserve rather than a crypto-collateralized or algorithmic dollar.

- **Backing / collateral model:** "pure, short-term U.S. debt assets" — i.e. short-dated **U.S. Treasury bills** and equivalents, a fiat-equivalent, low-duration reserve. This is the same backing family as the tokenized-Treasury cohort (BlackRock BUIDL, [[ondo-finance|Ondo]] USDY/OUSG, Mountain USDM, Hashnote USYC). Low duration matters: short T-bills carry minimal interest-rate (mark-to-market) risk, so NAV stays close to $1 even as rates move.
- **Peg / stability mechanism:** the peg is a **reserve-backed NAV peg**, not an over-collateralization or arbitrage-band peg. One CGUSD is meant to be redeemable for ~$1 of the underlying reserve; price holds near $1 to the extent mint/redeem against that reserve is open and reliable. There is no on-chain over-collateralization buffer the way [[dai]] has — the integrity of the peg rests on the off-chain reserve actually existing and being redeemable.
- **Where the yield comes from:** the **interest earned on the underlying short-term Treasuries**. As an "interest-bearing" stablecoin, CGUSD passes through T-bill yield to holders — a fundamentally different and generally lower-risk yield source than the funding-rate income behind synthetic dollars like [[ethena-usde|USDe]]. Yield accrual is typically reflected as a rising token value or via a wrapped/staked variant rather than a fiat dividend.
- **Mint / redeem & gating:** mint and redeem run **through the Cygnus protocol against the Treasury reserve**. RWA dollars usually gate primary mint/redeem behind **KYC/whitelisting and minimum sizes** (institutional onboarding), so retail holders frequently can only transact on secondary markets — which here are essentially dormant (see below). On [[base|Base]], holders can in principle exit via on-chain liquidity, but that liquidity is currently very thin.

This RWA / tokenized-Treasury model contrasts with the delta-neutral synthetic dollars (USDF, DUSD, USDm) elsewhere in this peer set: CGUSD's yield is **bank/Treasury interest**, not derivatives funding.

### Comparison vs peer dollars

| Token | Type | Backing | Yield source | Notable risk |
|---|---|---|---|---|
| **CGUSD** | RWA / interest-bearing | Short-term U.S. Treasuries | T-bill interest | Near-zero secondary liquidity; severe past de-peg (ATL ~$0.72) |
| **[[usdc]]** | Fiat-backed | Cash + short T-bills (Circle) | None passed to holders | Banking-partner / custody risk (cf. SVB 2023) |
| **[[ethena-usde\|USDe]]** | Synthetic / delta-neutral | Crypto collateral + short perps | Funding-rate carry | Negative-funding regimes; exchange counterparty |
| **[[dai]]** | Crypto-collateralized CDP | Over-collateralized crypto + RWA | Savings rate (sDAI) | Collateral volatility; governance |
| **Ondo USDY** | RWA / interest-bearing | Short T-bills + bank deposits | T-bill interest | KYC-gated; off-chain custody |

CGUSD's closest analogues are the **interest-bearing RWA dollars** (Ondo USDY, Mountain USDM): same Treasury-yield engine, same off-chain-custody dependency. Its distinguishing weakness in this peer set is its **liquidity profile** (essentially no live secondary market) and its **documented historical de-peg**.

---

## How and where it trades

CGUSD is a Base-native token; CoinGecko shows no major centralized-exchange listings. Reported 24h volume of ~$1 indicates there is essentially no active secondary market — CGUSD is held as a yield-bearing savings instrument and moves through mint/redeem rather than exchange trading. Any holder needing to exit at scale would depend on the protocol's redemption process rather than market liquidity.

Contract address:

| Chain | Address |
|---|---|
| Base | `0xca72827a3d211cfd8f6b00ac98824872b72cab49` |

---

## Tokenomics & supply

CGUSD supply is **demand-driven and reserve-matched**, like any redeemable tokenized-Treasury dollar: tokens are minted when dollars enter the reserve and burned on redemption, so supply expands and contracts with primary flows rather than a fixed schedule.

| Metric | Value |
|---|---|
| **Circulating supply** | 75.90M CGUSD |
| **Total supply** | 75.90M CGUSD |
| **Circulating / total** | ~1.00 (no large locked tranche) |
| **Market cap** | $75.70M |
| **Market-cap rank** | #330 |

Circulating equals total supply, consistent with a fully-issued reserve token (no vesting/lockup overhang to model). The ~$75.7M market cap is the reserve footprint; growth depends entirely on net new deposits into the Treasury reserve.

---

## Narrative / category & catalysts

CGUSD sits in the **tokenized-Treasury / RWA-yield** narrative — one of the most durable institutional crypto themes, anchored by BlackRock's BUIDL and [[ondo-finance|Ondo]]. The category pitch is "earn the risk-free rate on-chain," which is structurally attractive whenever short-term U.S. rates are elevated. Cygnus's specific angle is being a **Base-native** RWA dollar (proximity to Coinbase's ecosystem and Base DeFi).

- **Catalysts (upside):** Base ecosystem growth and DeFi integrations (lending markets, DEX pools) that give CGUSD real composability; new institutional deposits scaling the reserve; sustained high front-end Treasury yields keeping the product attractive.
- **Catalysts (downside):** a fall in short-term rates erodes the yield pitch; tightening RWA/securities regulation; any reserve-transparency concern.

---

## History / Timeline

| Date | Event |
|---|---|
| **2025-06-06** | All-time **high ~$1.089** — a brief above-peg print, likely thin-market / mint-redeem distortion rather than sustained premium. |
| **2025-09-29** | All-time **low ~$0.724325** — a **severe de-peg** (~28% below par), the defining risk event in CGUSD's record. |
| **2026-06-21/22** | Trades back near peg (~$0.9974) but with **~$1 of 24h volume** — i.e. a near-dormant secondary market; price is set by primary mint/redeem, not trading. |

> **De-peg flag:** the ATL of ~$0.72 (2025-09-29) is a documented, severe break from par. With essentially no live secondary liquidity, market price can dislocate sharply from NAV again under stress.

---

## Trading playbook

- **Treat as a yield instrument, not a trade.** With ~$1 of daily volume, CGUSD is held as a yield-bearing savings token; there is no meaningful spot market to trade in or out of at size. Entry/exit at par realistically runs through **protocol mint/redeem** (subject to any KYC gating), not an order book.
- **NAV-vs-price gap is the key signal.** Because the market is dormant, a quoted price meaningfully away from $1 reflects illiquidity, not a tradeable arbitrage — only an entity with primary redemption access can close the gap. The 2025-09-29 drop to ~$0.72 shows how wide that gap can get.
- **Macro framing (2026-06-23).** Broad crypto is in **Extreme Fear** (Fear & Greed 21; market-health 29/100). Bear-market liquidity stress is exactly when thin-liquidity RWA dollars are most prone to price dislocation from NAV — size and exit assumptions should account for that, not for the headline ~$0.997 print.

---

## Risks

- **De-peg risk:** CGUSD's ATL of ~$0.72 (2025-09-29) is a severe documented de-peg; combined with near-zero secondary liquidity, the market price can dislocate sharply from NAV. The current "Established Bear Market" (crypto Fear & Greed ~23) compounds liquidity stress.
- **Collateral / custody risk:** backing is off-chain short-term Treasuries; holders depend on the custodian, the protocol's reserve management, and accurate reporting of the reserve.
- **Issuer / regulatory risk:** tokenized-Treasury dollars sit squarely in the path of securities and money-transmission regulation; an interest-bearing token may be treated as a security in some jurisdictions.
- **Liquidity risk:** essentially no on-chain trading volume makes orderly market exit impossible; redemption depends on the protocol functioning.
- **Smart-contract risk:** reliance on Cygnus's Base contracts.

---

## Related

- [[real-world-assets]] — RWA / tokenized-Treasury context
- [[stablecoins]] — landscape overview
- [[ondo-finance]] — peer interest-bearing RWA dollar (USDY/OUSG)
- [[ethena-usde]], [[usde]] — synthetic-dollar peers (different yield source)
- [[usdc]], [[usdt]], [[dai]] — peer dollars
- [[base]] — host chain
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- Protocol description and whitepaper from Cygnus Finance ([https://wiki.cygnus.finance/whitepaper/](https://wiki.cygnus.finance/whitepaper/)). General market knowledge; no specific wiki source ingested yet beyond the CoinGecko snapshot.

## See Also

- [[crypto-markets]]
- [[base]]

---
