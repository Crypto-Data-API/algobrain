---
title: "AI Regulation in Trading"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, risk-management]
domain: [risk-management]
difficulty: intermediate
aliases: ["AI Trading Regulation", "Regulation of AI in Trading"]
related: ["[[regulation]]", "[[sec]]", "[[ai-safety-alignment]]", "[[ai-trading-agents]]", "[[foundation-models]]", "[[artificial-intelligence]]", "[[ai-portfolio-risk]]"]
---

# AI Regulation in Trading

The use of AI in trading faces a fast-moving regulatory landscape. Regulators worry about three things: market-stability risks from autonomous AI agents acting at machine speed, fairness and conflict-of-interest risks when AI optimizes against retail investors, and transparency/auditability of AI-driven investment decisions. As of mid-2026, the direction of travel is firmly toward **disclosure, documentation, and human oversight** rather than outright prohibition — with the EU furthest ahead on binding rules and the US relying on existing securities law plus enforcement.

## Why This Matters for Traders

For a systematic or AI-assisted trader, regulation is not abstract. It determines whether you must log every model decision, whether you can run a fully autonomous agent without a human in the loop, and what you must disclose to clients or counterparties. Getting this wrong is an operational and legal risk on top of market risk — see [[ai-portfolio-risk]] and [[ai-trading-risks]].

## United States

- **SEC — Predictive Data Analytics (PDA) proposal**: Proposed July 2023 under the Investment Advisers Act and the Exchange Act. It would require broker-dealers and investment advisers to eliminate or neutralize conflicts of interest arising when they use predictive analytics, AI, or similar technologies to optimize for the firm's interest over the investor's. The proposal drew heavy industry pushback for its broad definition of "covered technology" and **has not been finalized** as of mid-2026; the SEC's agenda under the post-2025 administration shifted, and any final rule is widely expected to be significantly narrower than the original proposal — if it advances at all. (Source: SEC PDA proposal, Federal Register 2023-16377)
- **SEC enforcement**: The Commission has stated it will continue to bring enforcement actions under existing securities laws for "AI-washing" (overstating AI capabilities) and for conduct involving PDA-like technologies — meaning AI use is already regulated in substance even without a dedicated final rule.
- **CFTC**: Monitors algorithmic trading, including AI-based systems, in derivatives markets; has issued AI-focused requests for comment.
- **FINRA**: Examines broker-dealer use of generative AI for supervision, communications, and compliance; reminds members that existing rules (supervision, recordkeeping, suitability) apply regardless of whether a human or model makes the decision.
- **Reg SCI / market access rules**: Existing rules on systems integrity and pre-trade risk controls already cover automated trading infrastructure.

## European Union

- **EU AI Act**: Entered into force 1 August 2024. AI systems used for **creditworthiness / credit scoring and certain financial decisioning** are classified as high-risk; many trading and financial-services AI uses fall under high-risk or transparency obligations. Prohibited-practice and AI-literacy provisions applied from **2 February 2025**. The bulk of high-risk obligations — risk management, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy, robustness, cybersecurity, conformity assessment, and post-market monitoring — become applicable from **2 August 2026**. (Source: European Commission, AI Act timeline)
  - A November 2025 **Digital Omnibus** proposal could push some high-risk enforcement deadlines to **2 December 2027** if harmonized standards and compliance tooling are not ready — so the 2026 date is the planned baseline but may slip for specific obligations.
- **MiFID II / RTS 6**: Existing algorithmic-trading rules (testing, kill switches, pre-trade controls, market-making obligations, record-keeping) apply to AI-based systems. ESMA reinforced this in a February 2026 supervisory briefing on algorithmic trading. (Source: ESMA Supervisory Briefing on Algorithmic Trading, Feb 2026)
- **Human oversight**: The Act requires "meaningful human oversight" of high-risk AI — relevant for fully autonomous trading agents.

## Other Jurisdictions

- **UK**: A "pro-innovation," principles-based approach delegated to existing regulators (FCA, PRA) rather than a single AI statute. The FCA emphasizes existing frameworks (SM&CR accountability, Consumer Duty) applying to AI use.
- **Singapore (MAS)**: FEAT principles (Fairness, Ethics, Accountability, Transparency) and the Veritas toolkit — guidance, not binding law.

## Key Requirements (Common Themes)

| Requirement | Implication for traders |
|-------------|-------------------------|
| **Explainability** | Be able to explain why a model produced a given decision; black-box models face scrutiny in high-risk contexts |
| **Human oversight** | Fully autonomous trading without human review may face restrictions in the EU; a kill switch and monitoring are expected everywhere |
| **Disclosure** | May need to disclose AI use to clients/counterparties; AI-washing is an enforcement target |
| **Testing & documentation** | High-risk AI systems require documented pre-deployment testing and a technical-documentation file |
| **Record-keeping** | Model decisions, versions, and training data must be logged and auditable |
| **Conflicts of interest** | (US PDA proposal) firms must not let AI optimize the firm's interest over the investor's |

## Implications by Trader Type

- **Retail traders** using off-the-shelf AI tools (e.g. an LLM for research, or a copilot like Claude Code) face minimal direct regulatory burden today — they are the end user, not a regulated adviser.
- **Registered advisers / broker-dealers** must document and be able to explain AI usage in their investment and client-interaction processes, and should assume PDA-style conflict rules are coming in some form.
- **Funds and prop firms in the EU** running high-risk AI must prepare for the August 2026 (or later) high-risk obligations: documentation, oversight, and conformity assessment.
- **AI agent tokens / on-chain agents** that manage pooled funds face the most uncertainty — depending on structure they may be treated as collective investment vehicles or unregistered advisers. See [[ai-trading-agents]].

## The Trading Lesson

Regulation lags technology, but enforcement uses existing law in the meantime. The prudent posture for any serious AI-driven operation is to build for the strict case now: log every decision, keep a human able to intervene, document your testing, and avoid overstating what your AI does. These are also simply good risk-management practices — see [[ai-portfolio-risk]] and [[ai-trading-risks]].

## Sources

- SEC, "Conflicts of Interest Associated With the Use of Predictive Data Analytics by Broker-Dealers and Investment Advisers" (proposed rule, Federal Register 2023-16377)
- European Commission, AI Act timeline and high-risk requirements (digital-strategy.ec.europa.eu)
- ESMA, "Supervisory Briefing on Algorithmic Trading in the EU" (February 2026)
- European Commission Digital Omnibus package (proposed November 2025)

## Related

- [[regulation]] — broader regulatory overview
- [[sec]] — US securities regulator
- [[ai-safety-alignment]] — technical safety measures
- [[ai-trading-agents]] — the autonomous systems being regulated
- [[ai-portfolio-risk]] — AI in risk management
- [[artificial-intelligence]] — AI section hub
