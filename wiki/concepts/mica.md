---
title: "MiCA"
type: concept
created: 2026-07-19
updated: 2026-09-05
status: good
tags: [crypto, regulation, compliance, stablecoins, institutional]
aliases: ["Markets in Crypto-Assets Regulation", "Markets in Crypto-Assets", "EU Crypto Regulation"]
domain: [regulation, crypto]
prerequisites: ["[[regulation]]"]
difficulty: intermediate
related: ["[[regulation]]", "[[stablecoins]]", "[[stablecoin-regulation]]", "[[crypto-policy-shock-trading]]", "[[regulatory-arbitrage]]", "[[circle]]", "[[tether-limited]]", "[[usdc]]", "[[usdt]]", "[[regulatory-risk-map]]", "[[geopolitical-risk-premium]]", "[[cryptodataapi-regimes]]"]
---

# MiCA

**MiCA (Markets in Crypto-Assets Regulation)** is the European Union's comprehensive framework for regulating crypto-asset issuance and services across all 27 member states through a single passportable rulebook — replacing the fragmented, country-by-country licensing that previously governed crypto in Europe. It covers two distinct things that are often conflated: **licensing for crypto businesses** (Crypto-Asset Service Providers, or CASPs — exchanges, custodians, brokers) and **reserve/redemption rules for stablecoins** (E-Money Tokens and Asset-Referenced Tokens). MiCA rolled out in phases through 2024-2026 and has already reshaped EU market structure — most visibly by pushing [[usdt|Tether/USDT]] out of MiCA-compliant EU venues while [[usdc|Circle/USDC]] became the compliant incumbent — and it functions as a recurring policy catalyst that crypto markets price around each time a new rule, deadline, or enforcement action lands.

## What MiCA Covers

MiCA has two operative pillars:

1. **CASP licensing** — any firm providing crypto-asset services in the EU (custody, exchange, order execution, advice, portfolio management) needs authorization as a **Crypto-Asset Service Provider** from a national regulator in one member state. Once licensed, a CASP can "passport" that single license to operate across the entire EU/EEA without separate national approvals — the same passporting mechanism traditional EU financial services firms already use. This replaced a patchwork where a firm might need separate registrations in France, Germany, and elsewhere to serve EU customers.
2. **Stablecoin rules (EMTs and ARTs)** — MiCA classifies stablecoins as **E-Money Tokens (EMTs)**, which reference a single fiat currency (USDC, USDT, PYUSD), or **Asset-Referenced Tokens (ARTs)**, which reference a basket of currencies, commodities, or other assets. EMT issuers must be a licensed credit institution or Electronic Money Institution, hold 1:1 reserves with at least 30% in bank deposits spread across multiple institutions, undergo regular independent audits, and honor a legal right to redeem at par. The wiki's [[stablecoin-regulation]] page carries the full EMT/ART rule set, the EU comparison against other jurisdictions' stablecoin regimes, and the Circle/Tether market-share consequence in detail — this page does not repeat that table.

## CASP Licensing in Practice

The CASP regime is what makes MiCA more than a stablecoin law — it is a general-purpose crypto financial-services license. Key features:

- **Passporting** — a CASP license granted by one national regulator (e.g., France's AMF, Malta's MFSA) is valid across the entire EU, removing the need to re-license in every member state a firm wants to serve.
- **Prudential and conduct requirements** — minimum capital, custody segregation of client assets, conflict-of-interest rules, complaint handling, and market-abuse prevention obligations modeled on existing EU securities-market conduct rules (MiFID II).
- **Scope** — covers exchanges, custodians, brokers, and portfolio managers dealing in crypto-assets; notably, it does not cover fully decentralized protocols with no identifiable operator, leaving a live boundary question for DeFi.
- **Transitional periods** — existing crypto firms already operating in a member state before MiCA's CASP provisions took effect were generally given a transitional grandfathering window (up to 18 months, though several member states — France among them — opted to shorten it) to obtain full authorization rather than being shut down overnight.

## Phased Rollout (2024-2026)

MiCA did not take effect all at once — its two pillars were phased in on different dates, and national implementation timelines have varied:

| Date | Milestone |
|---|---|
| June 30, 2024 | Title III/IV (stablecoin rules for EMTs and ARTs) took effect |
| December 30, 2024 | Title V (CASP licensing regime) took effect across the EU |
| 2025 | National transitional periods for previously-operating firms run down; national regulators (AMF, MFSA, BaFin, and others) process the bulk of CASP license applications |
| Into 2026 | Full-scope enforcement matures; ongoing rulemaking refines technical standards (reserve composition, disclosure templates) via European Banking Authority (EBA) and European Securities and Markets Authority (ESMA) guidance |

Treat these dates as indicative — MiCA's technical standards and national transposition details continue to be refined by EBA/ESMA guidance and are worth confirming against current regulator publications before relying on them for compliance purposes.

## MiCA as a Policy Catalyst

Because MiCA rulemaking, enforcement actions, and compliance deadlines are discrete, dated, and market-moving, MiCA-related headlines are a recurring instance of the **Geopolitical/Policy Shock** regime basket in the [[crypto-market-regime-taxonomy]] and the specific signature class [[crypto-policy-shock-trading]] is built to trade — most often Signature A (pro-crypto/structural policy clarity, which the market tends to under-react to relative to its long-run significance) rather than the ban/adoption signature. Examples of MiCA-adjacent catalysts: a new EBA/ESMA technical standard, a national regulator granting or denying a major CASP license, an exchange delisting a non-compliant stablecoin, or an EU institution signaling stricter (or looser) enforcement of the reserve rules. See [[regulatory-risk-map]] and [[geopolitical-risk-premium]] for how to size the risk-off/risk-on component of a EU-specific regulatory shock relative to other jurisdictions' policy news.

## Getting the Data (CryptoDataAPI)

[[cryptodataapi|CryptoDataAPI]]'s Geopolitical/Policy Regime family surfaces exactly the kind of regulatory-headline flow MiCA developments generate, via GDELT news-flow classification. It is not MiCA-specific — it is the general regulatory/policy-headline surface — but it is the wiki's verified route to monitoring EU crypto-policy catalysts as they break. See [[cryptodataapi-regimes]] for the full endpoint family.

**Live data:**
- `GET /api/v1/policy/headlines` — live regulatory feed (Federal Register/SEC/CFTC-sourced in the current build, with a signed bias per headline); useful as a template for the kind of classification a MiCA-specific headline would receive
- `GET /api/v1/policy/regime` — policy risk score, signed tilt, and rate calendar
- `GET /api/v1/policy/regime/score` — composite 0-100 policy-risk score (40% GDELT news flow, 35% cross-asset stress, 25% rate calendar)

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time policy-regime snapshots for backtesting reactions to past regulatory events

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/policy/regime/score"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[regulation]] — general crypto regulation concept
- [[stablecoins]] — the asset class most directly reshaped by MiCA's EMT/ART rules
- [[stablecoin-regulation]] — full EMT/ART rule detail and global stablecoin-regulation comparison, including MiCA's table entry
- [[crypto-policy-shock-trading]] — the strategy that trades MiCA-class regulatory catalysts as Signature A/D policy shocks
- [[regulatory-arbitrage]] — trading price/access differences created by MiCA compliance splitting EU venues from the rest of the world
- [[circle]], [[usdc]] — MiCA-compliant issuer and token
- [[tether-limited]], [[usdt]] — issuer and token most affected by MiCA non-compliance in the EU
- [[regulatory-risk-map]], [[geopolitical-risk-premium]] — sizing frameworks for EU-specific policy shocks
- [[cryptodataapi-regimes]] — the Policy/Black-Swan Regime data family for monitoring regulatory headlines

## Sources

- [[stablecoin-regulation]] — wiki concept page with the full MiCA EMT/ART classification table, reserve requirements, and Circle/Tether market-structure impact
- [[cryptodataapi-regimes]] — wiki source page verifying the Policy/Geopolitical Regime endpoint family (fetched from https://cryptodataapi.com/api/docs)
- General knowledge of MiCA's phased effective dates (Title III/IV stablecoin rules, June 2024; Title V CASP licensing, December 2024) and passporting mechanism, cross-checked against the cited wiki pages; not legal advice — confirm current rule text and transposition status with EU/national regulator publications before relying on any date or requirement here
