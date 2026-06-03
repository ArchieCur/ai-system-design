# Security Architecture for Agentic Systems

## Overview

Security in agentic AI systems is not a layer you add after the system works. It is a property of how the system reasons — and it can only be guaranteed by controlling what evidence reaches the inference step, before it gets there.

This module applies the Belief Dynamics framework from the Specifications curriculum to a security threat model drawn from Anthropic's Zero Trust for AI Agents (2026). The result is a practical architecture built on three tools you already have: the Supremacy Clause, the Tool Security Contract, and Evidence Reset Protocols — each shown here in its security deployment.

---

## What You'll Learn

### Security Architecture for Agentic Systems

**[Security Architecture for Agentic Systems](Security_Architecture_Agentic_Systems.md)** — The full threat taxonomy, architectural defenses, and deployment maturity model for practitioners building or reviewing agentic systems

Covers:

- **Section 1: The Threat Landscape Through an Evidence Lens** — A unified taxonomy of prompt injection, tool poisoning, memory poisoning, and persuasive pressure as evidence attacks on different layers of the reasoning chain
- **Section 2: The Supremacy Clause as a Zero Trust Primitive** — The security deployment template, the Stability Protocol's intervention ladder, and the mid-session Supremacy Clause injection pattern enabled by the mid-conversation system messages API
- **Section 3: The Tool Return Contract Security Layer** — The incorporation gate, the Security Contract template, and mid-chain security anomaly handling
- **Section 4: Pre-Inference Monitoring — The Open Problem** — What true pre-inference monitoring would require and what the current architecture provides as practical approximations
- **Section 5: Mapping to Deployment Maturity** — Minimum viable, Advanced, and Optimized security architectures calibrated to system scale and risk level

---

## Why Security Architecture Requires Its Own Module

Every tool in this curriculum can be used correctly and still produce an insecure system if the security deployment of that tool is not explicitly designed.

The Supremacy Clause is in the Specifications module because it was introduced as a mechanism for preventing persona drift. Its security function — as a static prior lock that keeps the model's belief state far enough from the phase boundary that adversarial evidence accumulation cannot produce a flip — is the same mechanism, applied to a threat model. The security module makes that application explicit.

The Tool Definition Standard is in the Tools module. Its Security Contract extension — which intercepts tool returns before they become evidence and halts the chain on anomaly detection — is a security primitive that the Tools module does not cover. Without it, a tool that functions correctly from an operational standpoint can still deliver a poisoned evidence stream into the model's context window.

Evidence Reset Protocols are in the Specifications module as a drift management tool. Their security interpretation — as an operational system for monitoring drift signals and intervening before the sigmoid transition makes late correction qualitatively different from early correction — is what turns them from a recovery mechanism into a monitoring and prevention infrastructure.

The security module synthesizes these tools. It does not reintroduce them. The prerequisites are real: without the Specifications and Tools modules, the security architecture described here will not be implementable.

---

## Core Concepts

### Evidence Architecture

Every security threat to an agentic system is, at its root, an evidence attack — an attempt to corrupt, contaminate, or gradually shift the evidence the model reasons from. The threat taxonomy follows from this: prompt injection attacks Layer 1 (input evidence), tool poisoning attacks Layer 2 (retrieval evidence), and memory poisoning attacks Layer 3 (persistence evidence). Persuasive pressure is not a corruption attack — it is an accumulation attack, and it requires a different defense.

### The Three Pillars

**Supremacy Clause — Static Prior Lock:** Sets the prior. Defines invariants. Establishes the dominance of MUST constraints regardless of what evidence accumulates afterward. The mathematical firewall that keeps adversarial arguments accumulating as noise rather than as evidence that can shift the belief state past the phase boundary.

**Tool Security Contract — Evidence Validation Gate:** Intercepts tool returns before they become evidence. A tool return that passes schema validation and contains no operational error can still carry malicious instructions or contaminated data. The incorporation gate is the mechanism that catches this before it enters the context as trusted evidence for the next inference step.

**Evidence Reset Protocols — Dynamic Belief Hygiene:** Manages evidence accumulation over time. The Supremacy Clause alone cannot stop drift if evidence volume grows unbounded. The Stability Protocol provides graded interventions — from a short re-grounding prompt to a full prior re-initialization — calibrated to drift severity and to the timing constraint imposed by the sigmoid transition.

### The Timing Constraint

The sigmoid transition in belief dynamics means that late intervention is qualitatively different from early intervention. At Level 1 drift, a short re-grounding prompt is sufficient to return the agent to its stable zone. At Level 4 drift, re-grounding will not work — the contaminated evidence has accumulated past the point where a reminder can shift the posterior. Continuous monitoring is not optional. It is the mechanism by which the system stays in the range where intervention is still effective.

---

## Prerequisites

This module assumes familiarity with:

- **Specifications module** — especially Section 1 (Foundations), Section 8 (Supremacy Clause and Evidence Reset Protocols), and Appendix F (Belief Dynamics framework). The security module applies these concepts to a threat model rather than re-teaching them.
- **Tools module** — especially Tool Literacy: Designing Tools the Model Can Actually Use (v1.2.0), Sections 1–3 (Tool Definition Standard, Classification, Return Contract). The Security Contract is an optional fourth component of the Tool Definition Standard; it assumes the first three are already in place.

If either of these is unfamiliar, return to those modules before proceeding here.

---

## How This Module Fits the Curriculum

The Specifications module established how belief states form, drift, and can be anchored. The Skills module established reusable implementation patterns. The Tools module established what tools are and how they fail. The Multi-Agent Systems module extended all of this to architectures where agents communicate with each other and contamination propagates across agent boundaries.

This module takes those foundations and asks: given everything you have built, what are the specific ways it can be attacked — and what does a complete defensive architecture look like?

The answer is not a new framework. It is the existing framework, read through a security lens, with the specific deployment patterns that make each component resistant to the threat classes it is designed to address.

---

## Getting Started

### New to agentic security?

**Recommended path:**
[Security Architecture for Agentic Systems — Section 1](Security_Architecture_Agentic_Systems.md) → Section 2 → Section 3 → Section 4 → Section 5

Read in order. Section 1 establishes the threat model. Sections 2 and 3 give you the defensive tools. Section 4 is honest about what the current architecture cannot do. Section 5 tells you what to deploy at your scale.

### Building something now?

- **Single agent, need prompt injection resistance?** → [Section 2: Supremacy Clause Template](Security_Architecture_Agentic_Systems.md)
- **Tools that retrieve external content?** → [Section 3: Tool Security Contract](Security_Architecture_Agentic_Systems.md)
- **Long-running or multi-agent system?** → [Section 2: Stability Protocol and Intervention Ladder](Security_Architecture_Agentic_Systems.md)
- **Opus 4.8 deployment, need mid-session re-grounding?** → [Section 2: Mid-Session Supremacy Clause Injection](Security_Architecture_Agentic_Systems.md)
- **Not sure what security architecture your system needs?** → [Section 5: Deployment Maturity Model](Security_Architecture_Agentic_Systems.md)

---

## Key Principle

**Agentic security is evidence architecture.**

The practitioner who controls what evidence reaches inference controls what the agent does. Every defensive tool in this module — the Supremacy Clause, the Tool Security Contract, the Evidence Reset Protocols — is a mechanism for controlling the evidence chain at a different point: at session start, at the retrieval layer, and across the lifetime of the session.

---

*Ready to begin? Start with [Security Architecture for Agentic Systems](Security_Architecture_Agentic_Systems.md) →*
