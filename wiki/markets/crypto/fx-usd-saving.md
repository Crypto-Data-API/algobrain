---
title: "f(x) USD Saving"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins, defi]
aliases: ["FXSAVE", "fxSAVE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://fx.aladdin.club/"
related: ["[[crypto-markets]]", "[[stablecoins]]", "[[f-x-protocol-fxusd]]", "[[ethereum]]"]
---

# f(x) USD Saving

**f(x) USD Saving (fxSAVE)** is the **yield-bearing savings wrapper for [[f-x-protocol-fxusd|fxUSD]]**, f(x) Protocol's USD stablecoin (AladdinDAO ecosystem), on [[ethereum|Ethereum]]. Holders deposit fxUSD to receive fxSAVE, which accrues yield from the protocol's stability-pool income and collateral yield. As such it is a **yield-accruing token, not a $1-pegged stablecoin itself** — its price drifts above $1 as yield compounds. As of the latest snapshot it ranks **#408** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). Note: fxSAVE is a savings/staked wrapper, so a price above $1 reflects accrued yield over the underlying fxUSD — it is not a de-peg or premium.*

| Field | Detail |
|---|---|
| **Ticker** | FXSAVE |
| **Underlying peg** | US Dollar via [[f-x-protocol-fxusd|fxUSD]] (fxSAVE itself accrues yield above $1) |
| **Issuer / chain** | f(x) Protocol (AladdinDAO) — Ethereum |
| **Current price** | $1.11 (reflects accrued yield on fxUSD) |
| **Market cap** | $57.23M |
| **Market cap rank** | #408 |
| **24h volume** | $5.77 |
| **Circulating supply** | 51.62M FXSAVE |
| **Total supply** | 51.62M FXSAVE |
| **24h change** | -0.02% |
| **7d change** | -0.17% |
| **All-time high** | $4.68 (2026-02-21) |
| **All-time low** | $0.972207 (2026-03-19) |

The $1.11 price is **the value of accrued savings on the underlying fxUSD**, behaving like a price-per-share that rises as yield compounds — comparable to how staked-stablecoin wrappers (e.g. sDAI, sUSDe) trade above their underlying. The $4.68 ATH and $0.97 ATL are early/thin-market data artifacts, not the current operating range.

---

## Architecture & how it works

fxSAVE does **not maintain its own peg**; it represents a claim on a growing pool of [[f-x-protocol-fxusd|fxUSD]]. The design is an **accumulating savings vault** (price-per-share rises) rather than a rebasing one (balance grows).

- **Collateral / reserve model:** Each fxSAVE is backed by **deposited fxUSD plus accumulated yield.** fxUSD in turn is backed by f(x) Protocol's crypto collateral — principally **wstETH** (staked ETH) and **WBTC** — under the protocol's f(x) 2.0 stability design. So fxSAVE's ultimate backing is volatile crypto collateral, one layer removed.
- **Peg / stability mechanism:** fxSAVE inherits **fxUSD's** peg and stability mechanism; it does not defend $1 itself. The redemption value of fxSAVE *in fxUSD* increases over time as yield accrues — an accumulating per-share value, like sDAI relative to DAI.
- **Mint / redeem & gating:** Acquired by **depositing fxUSD** into the f(x) savings contract (receiving fxSAVE) and exited by **unwrapping fxSAVE back into fxUSD** (which is itself redeemable against the protocol's wstETH/WBTC collateral). There is effectively **no order-book market**; entry/exit is via the protocol contract.
- **Yield source & distribution:** Income from f(x) Protocol's **stability pool** (liquidation fees, protocol fees) plus the **staking yield on the underlying crypto collateral** (wstETH staking yield) flows to fxSAVE depositors. Yield is **accrued into the per-share value** rather than distributed, so the fxSAVE/fxUSD ratio compounds upward.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 51.62M FXSAVE |
| **Total Supply** | 51.62M FXSAVE |
| **Max Supply** | Unlimited |

Supply is elastic to fxUSD deposits; there is no fixed cap. Because yield accrues into price-per-share, supply does not inflate with yield — the *value* of each fxSAVE rises instead. Market cap (~$57.23M, rank #408) reflects deposited fxUSD plus accrued yield.

---

## Comparison vs peers

| Token | Underlying dollar | Yield source | Yield mechanic | Liquid market? |
|---|---|---|---|---|
| **fxSAVE** | [[f-x-protocol-fxusd\|fxUSD]] | Stability-pool fees + wstETH staking | Accruing per-share | **No — contract-only** |
| sDAI | [[dai\|DAI]] | DAI Savings Rate (RWA/T-bills) | Accruing per-share | Yes (deep) |
| sUSDe | [[usde\|USDe]] | Delta-neutral funding/basis | Accruing per-share | Yes |
| savUSD | Avant USD | Strategy yield | Accruing per-share | Limited |

fxSAVE follows the same **accruing-savings-wrapper** pattern as sDAI and sUSDe, but its yield is tied to f(x) Protocol's CDP-style stability pool and ETH/BTC collateral, and — unlike sDAI/sUSDe — it has **effectively no secondary liquidity** (24h volume ~$5.77), so it must be entered/exited through the protocol rather than on an exchange.

---

## How / where it trades & is used

fxSAVE is essentially **not traded on secondary markets** — at snapshot time reported 24h volume is **$5.77**, i.e. effectively nil. It is acquired and exited by depositing/withdrawing fxUSD through the f(x) Protocol savings contract, not by buying on an exchange.

- **Treat as non-tradable on order books**; price is a contract-derived per-share value, and any quoted "market" is illiquid.
- **Composability** is within the f(x)/AladdinDAO ecosystem (as savings collateral); it is not a cross-venue trading instrument.
- For the underlying liquid token, see [[f-x-protocol-fxusd|fxUSD]].

---

## Narrative, category & catalysts

fxSAVE sits in the **savings-wrapper / yield-bearing-stablecoin** category alongside sDAI and sUSDe — a way to earn protocol yield on a stablecoin balance without a separate staking UI. Catalysts: (1) growth of fxUSD adoption and the f(x) stability pool, which drives fee income; (2) high ETH staking yields, which lift the collateral-yield leg; (3) integrations that accept fxSAVE as collateral. Narrative/demand risk is tied to f(x) Protocol's health and to the level of ETH staking yield and liquidation-fee income.

---

## History / timeline

- **2026-02-21** — All-time high of **$4.68** recorded — an early thin-market data artifact, not a meaningful operating price.
- **2026-03-19** — All-time low of **$0.972207** — likewise an early/thin-market artifact.
- **2026-06-21** — Snapshot: **$1.11** per-share value (accrued yield over fxUSD), $57.23M cap, rank #408, near-zero 24h volume ($5.77).

The ATH/ATL extremes pre-date a stable operating regime and reflect illiquid early pricing rather than any de-peg of the underlying fxUSD.

---

## Risks

- **Inherited fxUSD risk**: fxSAVE is only as safe as fxUSD; any de-peg, undercollateralization, or mechanism failure of fxUSD flows through to fxSAVE.
- **Collateral / volatility risk**: ultimate backing is volatile crypto (wstETH, WBTC); a sharp drawdown can impair the underlying collateral and yield.
- **Yield / mechanism risk**: yield depends on stability-pool income and staking returns, which can fall or turn negative (stability-pool depositors can absorb liquidation losses), reducing or eroding the savings value.
- **Yield-source / counterparty risk**: the stability-pool fee stream depends on liquidation activity and protocol usage; in quiet markets fee income shrinks, and stability-pool depositors bear liquidation losses.
- **Redemption-gating risk**: exit is **contract-only** (unwrap to fxUSD, then redeem fxUSD against collateral); there is no order book to sell into if the protocol path is congested or paused.
- **Smart-contract risk**: an additional wrapper contract on top of the already-complex f(x) system increases attack surface.
- **Liquidity risk**: near-zero secondary volume — exits must go through the protocol's withdraw path; there is no deep market to sell into.
- **Regulatory risk**: yield-bearing stablecoin products face heightened regulatory scrutiny (potential "security" treatment in some jurisdictions).
- **Macro backdrop**: the broader market is in **Extreme Fear** (Fear & Greed Index 21; BTC ≈ $64,568, ETH ≈ $1,737), which pressures both the ETH collateral and the yield underpinning savings products.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x7743e50f534a7f9f1791dde7dcd89f7783eefc39` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://fx.aladdin.club/](https://fx.aladdin.club/) |
| **Twitter** | [@protocol_fx](https://twitter.com/protocol_fx) |
| **Whitepaper** | [f(x) 2.0 whitepaper](https://github.com/AladdinDAO/aladdin-v3-contracts/blob/main/whitepapers/f(x)_2.0_whitepaper.pdf) |

---

## Trading / usage playbook

- **Price-per-share, not peg.** A price above $1 is accrued yield, not a premium — value fxSAVE by its fxUSD redemption ratio, not against $1.
- **Enter/exit through the contract.** With ~$5.77 daily volume there is no order book; deposit/withdraw fxUSD via the f(x) savings contract.
- **Watch the underlying.** fxSAVE health = fxUSD health = wstETH/WBTC collateral health plus stability-pool fee income; monitor those, not the fxSAVE "market price."
- **Yield is variable.** ETH staking yield and liquidation-fee income drive returns and can compress in quiet or falling markets.

---

## Related

- [[stablecoins]]
- [[f-x-protocol-fxusd]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.
