---
title: "Quantum Computing in Finance"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [ai-trading, machine-learning, portfolio-theory, risk-management]
domain: [artificial-intelligence, portfolio-theory, risk-management]
prerequisites: ["[[portfolio-optimization]]", "[[monte-carlo]]"]
difficulty: advanced
aliases: ["Quantum", "Quantum Computing", "Quantum Finance", "Quantum Computing in Trading"]
related: ["[[artificial-intelligence]]", "[[portfolio-theory]]", "[[risk-management]]", "[[monte-carlo]]", "[[portfolio-optimization]]", "[[machine-learning]]"]
---

Quantum computing is an emerging computational paradigm that uses quantum mechanical phenomena — superposition, entanglement, and interference — to process information in ways fundamentally different from classical computers. In finance, quantum computing has been proposed as a potential tool for [[portfolio-optimization|portfolio optimization]], [[risk-management|risk assessment]], derivatives pricing, and cryptographic applications. As of 2025, practical quantum advantage in finance remains largely theoretical, with most useful applications still years away.

## Quantum Computing Basics

### Qubits
Classical computers use bits that exist in one of two states: 0 or 1. Quantum computers use **qubits**, which can exist in a superposition of both states simultaneously. When multiple qubits are entangled, the system can represent and process an exponentially large number of states in parallel — 50 qubits can represent 2^50 (approximately 1 quadrillion) states simultaneously.

### Key Quantum Properties
- **Superposition** — A qubit can be in a combination of 0 and 1 states until measured, allowing parallel exploration of solution spaces.
- **Entanglement** — Qubits can be correlated so that the state of one instantly determines the state of another, regardless of distance. This enables certain computations that have no classical equivalent.
- **Interference** — Quantum algorithms manipulate probability amplitudes so that correct answers are amplified and incorrect answers cancel out, guiding the computation toward useful results.

### Types of Quantum Computers
- **Gate-based (universal)** — Perform quantum logic operations on qubits using quantum gates, analogous to classical logic gates. This is the approach pursued by IBM, Google, IonQ, and most academic labs.
- **Quantum annealers** — Specialized devices designed to find the lowest-energy state of a problem, naturally suited to optimization tasks. D-Wave is the primary vendor.
- **Photonic quantum computers** — Use photons as qubits. PsiQuantum and Xanadu are notable players.

## Potential Financial Applications

### Portfolio Optimization
Classical [[portfolio-optimization|portfolio optimization]] (Markowitz mean-variance and its extensions) becomes computationally intractable as the number of assets grows and constraints multiply. A portfolio of 1,000 assets with cardinality constraints, transaction costs, and sector limits is an NP-hard combinatorial problem. Quantum annealers and variational quantum algorithms (like QAOA — Quantum Approximate Optimization Algorithm) have shown promise in solving simplified versions of these problems, though current hardware can only handle toy-scale portfolios of dozens of assets.

### Monte Carlo Simulation
[[monte-carlo|Monte Carlo methods]] are used extensively in derivatives pricing, Value at Risk (VaR) calculations, and stress testing. Classical Monte Carlo converges at a rate of 1/sqrt(N) — to halve the error, you need 4x the samples. Quantum Monte Carlo (using quantum amplitude estimation) theoretically achieves a quadratic speedup, converging at 1/N. For risk calculations that currently require millions of simulations, this could dramatically reduce computation time. Goldman Sachs and QC Ware have published research on quantum Monte Carlo for derivatives pricing.

### Cryptography and Security
Shor's algorithm, if run on a sufficiently powerful quantum computer, could factor large numbers exponentially faster than classical computers, breaking RSA and ECC encryption that secures all financial communications and transactions. This "crypto-apocalypse" scenario has driven investment in:
- **Post-quantum cryptography** — New encryption algorithms resistant to quantum attacks (NIST finalized its first post-quantum standards in 2024)
- **Quantum key distribution** — Using quantum mechanics to create theoretically unbreakable encryption
Financial institutions are beginning to inventory cryptographic dependencies and plan migration timelines, though a quantum computer capable of breaking current encryption is estimated to require millions of stable qubits — far beyond current capabilities.

### Machine Learning
Quantum machine learning algorithms (quantum kernel methods, quantum neural networks, quantum Boltzmann machines) have been proposed for tasks like fraud detection, credit scoring, and [[artificial-intelligence|AI-driven trading]] signal generation. However, rigorous evidence of quantum advantage for practical ML tasks remains scarce, and many early claims have not survived scrutiny.

### Option Pricing
Exotic [[derivatives]] with path-dependent payoffs (barrier options, Asian options, lookback options) often require Monte Carlo simulation because closed-form solutions do not exist. Quantum speedups to Monte Carlo could make complex derivatives pricing significantly faster.

## Current State: The NISQ Era

The current period is called the NISQ (Noisy Intermediate-Scale Quantum) era, a term coined by John Preskill in 2018. NISQ devices have:
- **50-1,000+ qubits** — enough to do some useful computations in theory
- **High error rates** — qubits are extremely fragile, losing their quantum state due to environmental noise (decoherence) in microseconds to milliseconds
- **Limited coherence time** — computations must complete before qubits decohere
- **No fault tolerance** — true quantum error correction requires thousands of physical qubits per logical qubit, and is not yet practical at scale

As of 2025, no quantum computer has demonstrated a clear, practical advantage over classical computers for any financial computation. Google's "quantum supremacy" demonstration (2019) and subsequent experiments solved artificial problems with no direct commercial application.

## Key Players

| Company | Approach | Finance Relevance |
|---|---|---|
| **IBM** | Superconducting qubits (gate-based) | IBM Quantum Network includes JPMorgan, Goldman Sachs; 1,000+ qubit processors deployed |
| **Google (Alphabet)** | Superconducting qubits | Quantum supremacy claim (2019); research on quantum Monte Carlo |
| **IonQ** | Trapped ion qubits | High-fidelity qubits; partnership with Goldman Sachs on portfolio optimization |
| **D-Wave** | Quantum annealing | Optimization focus; used in early financial experiments by BBVA, Volkswagen |
| **Quantinuum (Honeywell)** | Trapped ion | High-quality qubits; financial services partnerships |
| **PsiQuantum** | Photonic | Aiming for fault-tolerant quantum computing; less near-term finance work |
| **Rigetti** | Superconducting | Cloud quantum computing; finance-focused hybrid algorithms |

Major banks and asset managers actively exploring quantum computing include JPMorgan Chase (QC research lab), Goldman Sachs (Monte Carlo and optimization research), HSBC, Barclays, and several hedge funds.

## Timeline Reality Check

Despite significant hype, the honest assessment as of 2025 is:

- **Now (2025)** — Quantum computers can solve toy problems faster than classical computers on artificially constructed tasks. No practical financial advantage exists. Useful for building expertise and algorithms that will scale when hardware improves.
- **Near-term (2026-2030)** — Incremental improvements in qubit count and error rates. Hybrid quantum-classical algorithms may show modest advantages for specific optimization and simulation problems. Unlikely to displace classical approaches for production workloads.
- **Medium-term (2030-2035)** — If fault-tolerant quantum computing becomes practical (requiring millions of physical qubits), quadratic speedups for Monte Carlo and combinatorial optimization could become real. Cryptographic migration will need to be complete.
- **Long-term (2035+)** — Potential for transformative impact on risk management, portfolio optimization, and cryptography. Timeline is highly uncertain and depends on fundamental engineering breakthroughs.

The most immediate practical concern for finance is not quantum computing for trading but quantum computing breaking encryption — the migration to post-quantum cryptography is an urgent, ongoing process.

## Trading Relevance

For a working trader, the practical takeaway is sober: as of 2026 there is no quantum computer that improves any production trading, pricing, or risk workload over classical hardware, and claims of "quantum trading" products should be treated as marketing. The one near-term concern that is *not* hype is **harvest-now-decrypt-later** risk to cryptography — adversaries can store encrypted financial data today and decrypt it once a large fault-tolerant machine exists — which is why exchanges, custodians, and crypto protocols ([[quantum-resistant-ledger|quantum-resistant chains]]) are beginning migration to NIST post-quantum standards. The speculative upside (quadratic Monte Carlo speedups for [[risk-management|VaR]] and exotic [[derivatives]] pricing, faster combinatorial [[portfolio-optimization]]) is real in theory but gated on fault-tolerant hardware that remains years to decades away. Treat quantum as a watch-list R&D item, not an edge.

## Related

- [[artificial-intelligence]] — the broader field of AI/ML in trading
- [[portfolio-theory]] — portfolio optimization is a key proposed use case
- [[risk-management]] — Monte Carlo speedups could transform risk calculations
- [[monte-carlo]] — the simulation method most likely to benefit from quantum speedup
- [[machine-learning]] — quantum ML is a speculative but active research area

## Sources

- Preskill, J., "Quantum Computing in the NISQ era and beyond" (Quantum, 2018) — origin of the NISQ framing.
- Orús, R., Mugel, S. & Lizaso, E., "Quantum computing for finance: Overview and prospects" (Reviews in Physics, 2019).
- Egger, D. J. et al. (IBM), "Quantum Computing for Finance: State-of-the-Art and Future Prospects" (IEEE Transactions on Quantum Engineering, 2020).
- Stamatopoulos et al. (Goldman Sachs / QC Ware), "Option Pricing using Quantum Computers" (Quantum, 2020) — quantum amplitude estimation for derivatives.
- NIST, Post-Quantum Cryptography Standardization — finalized FIPS 203/204/205 standards (2024).
