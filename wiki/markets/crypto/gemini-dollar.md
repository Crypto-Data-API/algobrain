---
title: "Gemini Dollar"
type: market
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["GUSD", "Gemini USD"]
entity_type: protocol
headquarters: "New York, USA"
website: "https://gemini.com/dollar/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[gemini]]", "[[paxos-standard]]", "[[paypal-usd]]", "[[stablecoin]]", "[[tether]]", "[[usdc]]"]
---

# Gemini Dollar

**Gemini Dollar** (ticker **GUSD**, ERC-20 on [[ethereum|Ethereum]]) is a fiat-collateralized [[stablecoin]] pegged 1:1 to the U.S. dollar, issued by [[gemini|Gemini Trust Company, LLC]], a New York trust company regulated by the New York State Department of Financial Services (NYDFS). Launched on **10 September 2018** alongside [[paxos-standard|Pax Dollar (then PAX)]], GUSD was one of the first regulated, fiat-backed dollar stablecoins to receive explicit approval from a U.S. state regulator. Reserves are held at a U.S. bank with monthly independent attestations, and the contract was audited by Trail of Bits at launch.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, GUSD trades at **$0.998303**, holds market-cap rank **#531**, and carries a market capitalization of **$39,379,670**. It was essentially flat over the trailing window (**24h −0.09%**, **7d −0.08%**), behaving as a peg-anchored asset should.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GUSD |
| **Price (2026-06-21)** | $0.998303 |
| **Market Cap Rank** | #531 |
| **Market Cap** | $39,379,670 |
| **24h Change** | −0.09% |
| **7d Change** | −0.08% |
| **Peg target** | 1 GUSD = 1 USD |
| **Backing model** | Fiat reserves (USD at U.S. bank + short-dated instruments) |
| **Issuer** | Gemini Trust Company, LLC |
| **Regulator** | NYDFS (New York limited-purpose trust charter) |
| **Native chain** | [[ethereum\|Ethereum]] (ERC-20) |
| **Website** | [https://gemini.com/dollar/](https://gemini.com/dollar/) |

---

## Architecture: How GUSD Works

GUSD is a **fiat-reserve (custodial) stablecoin**: each token is intended to be redeemable for one U.S. dollar held in reserve, in contrast to crypto-collateralized designs like [[dola-usd|DOLA]] or over-collateralized [[dai|DAI]]. There is no algorithmic component.

### Reserve model and attestation
Reserves backing circulating GUSD are held in **U.S. dollar deposits at a U.S. bank** (historically supplemented by money-market funds / short-dated instruments), structured under New York trust law so that they back tokens 1:1 rather than being lent out. Gemini has historically published **monthly attestation reports** from an independent accounting firm confirming that the dollar value of reserves equals or exceeds GUSD outstanding. The GUSD ERC-20 contract was **audited by Trail of Bits** at launch and uses an upgradeable, custodian-controlled design that allows the issuer to pause or upgrade the token — a feature that aids compliance but adds issuer trust assumptions.

### Regulatory wrapper
Gemini operates as a **New York limited-purpose trust company under NYDFS supervision**, the same regulatory category as [[paxos-standard|Paxos]]. NYDFS approval covers the issuance framework, reserve requirements, and custody — but it is a state trust charter, not a federal bank charter. This regulatory posture historically distinguished GUSD (and [[paxos-standard|USDP]]) from offshore, less-transparent issuers such as [[tether|Tether (USDT)]].

### Peg-maintenance / mint-redeem
The peg is maintained through a **mint/redeem arbitrage loop** anchored at par:

- **Mint** — A user deposits USD with Gemini and receives newly issued GUSD 1:1, withdrawable to any Ethereum address.
- **Redeem** — GUSD returned to Gemini is burned and the corresponding USD credited back to the user's account 1:1.

Because users can create or destroy GUSD at par, secondary-market deviations create arbitrage incentives that pull GUSD back toward $1. Mint/redeem flows through the Gemini exchange account (KYC-gated), so retail typically obtains GUSD on venues rather than minting directly. The current price of $0.998303 reflects ordinary secondary-market micro-deviation (spread, thin liquidity), not a meaningful [[depeg]].

---

## Tokenomics & Supply

GUSD supply is **fully reserve-backed and elastic**, expanding and contracting with net dollar deposits and redemptions. There is no fixed max supply, no emissions, and no seigniorage; the issuer earns yield on the reserve float, the standard fiat-stablecoin business model. At ~$39M market cap, GUSD is a small-cap stablecoin, well below its earlier scale. Supply has structurally declined as institutional and retail dollar demand consolidated into [[usdc|USDC]] and [[tether|USDT]].

---

## Comparison vs Competitor Stablecoins

| Stablecoin | Issuer | Peg | Backing | Regulatory wrapper | Notable |
|---|---|---|---|---|---|
| **GUSD** | [[gemini\|Gemini Trust]] | USD | Cash at U.S. bank + short instruments | NYDFS trust charter | Trail of Bits–audited; pausable contract |
| [[paxos-standard\|USDP]] | Paxos | USD | Cash + T-bills | NYDFS trust charter | Sibling 2018 NYDFS coin |
| [[usdc\|USDC]] | Circle | USD | Cash + T-bills | US MTLs + EU MiCA EMT | Largest regulated USD coin |
| [[tether\|USDT]] | Tether | USD | Cash, T-bills, other | Offshore | Largest stablecoin; less transparent |
| [[paypal-usd\|PYUSD]] | Paxos (PayPal) | USD | Cash + T-bills | NYDFS trust charter | Payments-distribution focus |

GUSD and USDP are the two original NYDFS-regulated dollar stablecoins (both approved in 2018). GUSD's differentiators are its exchange-native distribution (Gemini) and its audited, custodian-controlled contract; its weakness is small scale and thin liquidity.

---

## How & Where It Trades / Is Used

GUSD historically traded on the [[gemini|Gemini]] exchange and several centralized venues, with on-chain liquidity concentrated in [[ethereum|Ethereum]] DEX pools (e.g. Uniswap V3 GUSD/[[usdc|USDC]]). As a standard ERC-20 it can be supplied to lending markets and stable pools, but its ~$39M cap and modest daily volume make it a small-cap stablecoin relative to [[usdc|USDC]] and [[tether|USDT]]; thinner liquidity can amplify intraday ticks away from $1.00. Primary use cases are settlement on/around the Gemini ecosystem and as a regulated dollar pair.

---

## Narrative, Category & Catalysts

GUSD sits in the **regulated fiat-backed dollar stablecoin** category. Catalysts are largely regulatory and franchise-driven: U.S. federal stablecoin legislation would advantage trust-chartered issuers; growth in Gemini's regulated dollar rails and any payments/institutional adoption would lift demand. The dominant counter-trend is consolidation into [[usdc|USDC]] and [[tether|USDT]] plus newer entrants like [[paypal-usd|PYUSD]]. In the current **Extreme Fear / bottoming-accumulation** regime (Fear & Greed 21), aggregate stablecoin supply proxies capital entering or leaving crypto; small regulated coins like GUSD are a minor share of that flow.

---

## History / Timeline

- **10 September 2018** — GUSD launched and **approved by NYDFS** alongside [[paxos-standard|Pax Dollar (PAX)]]; contract audited by Trail of Bits.
- **2019–2022** — GUSD circulates as a regulated, exchange-native dollar stablecoin; supply scales with Gemini's growth.
- **November 2022** — The collapse of FTX and the failure of the **Gemini Earn** program (run with lender Genesis) damaged Gemini's reputation and contributed to GUSD supply decline (the Earn dispute concerned a separate lending product, not GUSD reserves).
- **February 2023** — NYDFS halts [[binance-usd|BUSD]] minting at [[paxos-standard|Paxos]], underscoring state-regulator authority over NYDFS-chartered stablecoin issuers (a comparable framework to Gemini's).
- **2023–2026** — GUSD supply declines as dollar demand consolidates into larger stablecoins.

---

## Risks

- **Issuer/counterparty risk** — Holders rely on Gemini Trust solvency and on reserves being fully backed and accessible; the custodian-controlled, pausable contract adds issuer trust assumptions.
- **Reserve / counterparty risk** — Quality and custody of reserve assets; banking-partner exposure (a banking failure can transiently stress redemptions, as USDC experienced in March 2023).
- **Regulatory risk** — NYDFS can constrain or order changes to a regulated stablecoin program (as it did with [[binance-usd|BUSD]] in 2023).
- **Redemption-gating risk** — Direct mint/redeem is KYC-gated through Gemini accounts; retail exit at par depends on secondary liquidity.
- **Liquidity risk** — Low circulating supply and volume can widen spreads and increase slippage versus larger stablecoins.
- **Smart-contract risk** — Audited ERC-20 contract, but upgradeable/pausable design concentrates control with the issuer.

See [[stablecoin]] and [[depeg]] for the general failure-mode taxonomy.

---

## Trading Playbook

- **As a parking asset** — A regulated, fully-reserved dollar; in the current bottoming regime, treat stablecoin balances as dry powder.
- **Venue choice** — GUSD is most liquid on/around Gemini; on-chain depth is limited, so size DEX trades to pool depth.
- **Peg reads** — Treat $0.997–$1.001 as normal micro-deviation; only a sustained, widening discount with redemption friction signals a genuine [[depeg]].
- **Headline sensitivity** — Watch NYDFS / U.S. stablecoin policy and Gemini corporate news, which move regulated issuers more than offshore peers.

---

## Related

- [[stablecoin]]
- [[gemini]]
- [[usdc]]
- [[tether]]
- [[paxos-standard]]
- [[paypal-usd]]
- [[depeg]]
- [[collateralization]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for issuer/mechanism details.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
