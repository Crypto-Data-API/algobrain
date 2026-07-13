---
title: "AI & Intellectual Property"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, regulation, education]
aliases: ["AI IP", "AI Copyright", "AI Intellectual Property"]
domain: [risk-management]
difficulty: intermediate
related: ["[[ethics-safety-overview]]", "[[ai-regulation-global]]", "[[ai-creative]]", "[[image-generation-ai]]", "[[foundation-models]]", "[[openai]]", "[[artificial-intelligence]]"]
---

# AI & Intellectual Property

AI intellectual property law is being shaped in real-time through landmark lawsuits, regulatory actions, and legislative proposals. Two core questions dominate: **Can AI models be trained on copyrighted data?** and **Who owns AI-generated content?** The answers will determine the economics of every [[foundation-models|foundation model]] company and the creative industries they disrupt.

## The Key Lawsuits

> Litigation status moves quickly; entries below reflect the broad posture as of mid-2026. Several cases have produced partial rulings on individual claims (e.g. fair-use and DMCA questions) while the core copyright-infringement claims continue. Always check the current docket before relying on an outcome.

| Case | Parties | Issue | Status | Market Impact |
|------|---------|-------|--------|---------------|
| **NYT v OpenAI/Microsoft** | New York Times vs [[openai|OpenAI]] | NYT claims GPT-4 memorises and reproduces articles | Ongoing | Existential for training-on-web-data model |
| **Getty v Stability AI** | Getty Images vs Stability AI | [[image-generation-ai|Stable Diffusion]] trained on Getty images without licence | Ongoing | Defines visual AI training rights |
| **Authors Guild v OpenAI** | 17+ authors vs OpenAI | Books used for training without consent | Ongoing | Scope of fair use for AI training |
| **UMG v Anthropic** | Universal Music vs [[anthropic|Anthropic]] | Claude generates copyrighted song lyrics | Settled/ongoing | Music IP boundaries |
| **Thelen v OpenAI** | Class action vs OpenAI | Generates defamatory statements about real people | Ongoing | [[hallucinations-ai|Hallucination]] liability |

## The Two Core Questions

### 1. Can AI Train on Copyrighted Data?

| Position | Argument | Supporters |
|----------|---------|-----------|
| **Yes (fair use)** | Training transforms the data; model learns patterns, doesn't copy | AI companies, tech industry |
| **No (licence required)** | Training is reproduction; creators deserve compensation | Publishers, artists, music labels |
| **Compromise** | Training is fair use, but output that reproduces protected works is infringement | Some legal scholars |

The US "fair use" doctrine is the key legal battleground. Outcomes will differ by jurisdiction (US, EU, UK, Japan all have different copyright frameworks).

### 2. Who Owns AI-Generated Content?

| Position | Current Status |
|----------|---------------|
| **The user who prompted** | Not settled; US Copyright Office says "pure AI output" can't be copyrighted |
| **The AI company** | Most terms of service assign output rights to the user |
| **Nobody** | US Copyright Office: works must have human authorship; pure AI output is public domain |
| **Hybrid** | Human-directed AI output with sufficient human creativity may be copyrightable |

## Investment Implications

### Risk: AI Companies

- If courts rule that training on copyrighted data requires licences, training costs could increase **10-100x**
- [[openai|OpenAI]], Stability AI, and others face potential damages in the billions
- Companies with licensed training data (Adobe Firefly, Shutterstock) gain competitive advantage

### Risk: Content Companies

- If AI training is fair use, media companies lose a revenue stream they've been counting on
- Music labels (UMG, WMG), publishers (NYT, WSJ), and image libraries (Getty) face disruption
- But: licensing deals are already being struck (OpenAI + AP, Google + Reddit) — creating new revenue streams

### Opportunity: Data Licensing

Companies with valuable, unique data can licence it for AI training:
- Reddit (RDDT): $60M/year deal with Google for training data
- Shutterstock: Licences image data to AI companies + contributor fund
- News publishers: Increasingly licensing content to AI companies

The value of proprietary data for AI training is a **new asset class** that traders should factor into valuations.

## See Also

- [[ethics-safety-overview]] — Ethics hub
- [[ai-regulation-global]] — Regulatory context
- [[ai-creative]] — The creative industries being disrupted
- [[image-generation-ai]] — Visual AI IP disputes
- [[foundation-models]] — Models at the centre of IP debates
- [[openai]] — Primary defendant in training data lawsuits
- [[artificial-intelligence]] — AI section hub

## Sources

- Court filings: NYT v OpenAI/Microsoft; Getty Images v Stability AI; Authors Guild v OpenAI; UMG v Anthropic
- US Copyright Office guidance on AI-generated works (human-authorship requirement)
- US fair-use doctrine, 17 U.S.C. § 107
- Public reporting on AI training-data licensing deals (Reddit-Google, OpenAI-AP, Shutterstock contributor fund)
