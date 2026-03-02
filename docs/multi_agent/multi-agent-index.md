# Multi-Agent Systems

## Overview

Multi-agent systems extend every principle in this curriculum to architectures where agents communicate with each other, share evidence streams, and can influence each other's belief states. This module teaches you why that changes the stakes of every design decision you've already made — and how to build systems that remain stable, detectable, and recoverable when they come under pressure.

This is where the two major threads of the curriculum converge: the belief architecture work in Specifications and the practical implementation work in Skills, Tools, and Prompts — applied to systems where the "user" sending evidence to an agent may itself be a drifting model.

---

## What You'll Learn

### Foundations

**[Multi-Agent Foundations](Multi_Agent_Foundations.md)** - Why multi-agent systems change the stakes, the cascade problem, how Specifications, Skills, and Prompts extend to agent-to-agent interactions, and what stays the same

### Patterns

**[Multi-Agent Patterns](Multi_Agent_Patterns.md)** - Concrete implementation patterns for stable multi-agent architectures: boundary design, Specification architecture, evidence flow control, exposure mapping, and the Harness Architecture

### Monitoring

**[Multi-Agent Monitoring](Multi_Agent_Monitoring.md)** - Observing belief states across agent networks, population-level drift detection, and the intervention hierarchy for multi-agent-specific failure modes

---

## Why Multi-Agent Systems Require Their Own Module

Everything that causes individual agent drift becomes a system-level cascade risk when agents are communicating with each other.

A belief state that drifts in a single agent is a single-agent problem. The Evidence Reset Protocols in Section 8 of the Specifications module are designed to catch it. But in a multi-agent system, a drifted agent's outputs don't just affect that agent — they enter downstream agents' context windows as evidence. Those agents update their belief states accordingly. Their outputs, now shaped by contaminated evidence, travel further downstream.

The cascade is self-obscuring: by the time behavior has visibly changed, the source of contamination may be several cycles back and invisible. No individual agent appears to have made an obviously wrong decision. The system has drifted, and the drift looks like consensus.

This module teaches practitioners how to design systems where that cascade is contained, the drift is detectable, and recovery is possible.

---

## Core Concepts

### The Cascade Problem

In multi-agent systems, drift propagates through evidence. One agent's softened constraint becomes another agent's evidence. The contamination travels faster than it can be observed at the individual agent level — and it arrives in downstream agents looking like legitimate input, not like the compromised output it actually is.

### Prompts as Prior Injections

Within a session, a prompt is the most powerful single determinant of where an agent's belief state starts. In multi-agent systems, inter-agent prompts are not messages — they are prior injections into downstream agents. The quality of an orchestrator's output to a subagent determines where that subagent starts on the sigmoidal learning curve.

### Agent Boundaries as Trust Boundaries

Every inter-agent boundary is a point where one model's belief state ends and another's begins. Treating those boundaries like API boundaries — typed inputs, validated outputs, explicit contracts — is the mechanism by which belief-state contamination is contained rather than propagated.

### Exposure Mapping

Not all agents carry equal contamination risk. Evidence volume, evidence quality, and fan-out to downstream agents determine which agents can do the most damage to the system if they drift. Identifying high-exposure agents before deployment allows monitoring and intervention resources to be allocated where they matter most.

---

## Prerequisites

This module assumes familiarity with:

- **Specifications module** — especially Section 8 (Supremacy Clause and Evidence Reset Protocols) and Appendix F (Belief Dynamics framework). The multi-agent module extends these concepts directly; it does not re-teach them.
- **Skills module** — the Class A/B/C classification, progressive disclosure, and how Skills operate at the SHOULD and CONTEXT layers of the Belief Dynamics framework.
- **Programmatic Tool Calling** — the Class A/B/C tool classification, architectural enforcement of confirmation gates, and the context window problem. The multi-agent module's enforcement arguments build directly on this foundation.

If any of these are unfamiliar, return to those modules before proceeding here.

---

## How This Module Fits the Curriculum

The Specifications module established the theoretical foundation: how models accumulate evidence, how belief states drift, and how to architect priors that resist contamination. The Skills and Tools modules established the practical infrastructure: reusable knowledge packages, tool classification, and programmatic enforcement.

This module applies both to the hardest version of the problem: systems where the evidence sources are other models, the contamination paths are invisible, and the failure modes scale with the number of agents.

Each existing module in the curriculum has a cross-reference to this one in its "What's Next" section. The connection runs in both directions — understanding multi-agent systems deepens the understanding of why single-agent design decisions matter, and mastering single-agent design is the prerequisite for building multi-agent systems that work.

---

## Getting Started

### New to multi-agent systems?

**Recommended path:**  
[Multi-Agent Foundations](Multi_Agent_Foundations.md) → [Multi-Agent Patterns](Multi_Agent_Patterns.md) → [Multi-Agent Monitoring](Multi_Agent_Monitoring.md)

Read in order. Foundations establishes the argument. Patterns gives you the implementation tools. Monitoring gives you the observability layer.

### Building something now?

- **Designing agent boundaries?** → [Multi-Agent Patterns: Pattern 1 — Boundary Design](Multi_Agent_Patterns.md)
- **Structuring Specifications across agents?** → [Multi-Agent Patterns: Pattern 2 — Specification Architecture](Multi_Agent_Patterns.md)
- **Managing what enters each agent's context?** → [Multi-Agent Patterns: Pattern 3 — Evidence Flow Control](Multi_Agent_Patterns.md)
- **Identifying your highest-risk agents?** → [Multi-Agent Patterns: Pattern 4 — Exposure Mapping](Multi_Agent_Patterns.md)
- **Setting up persistent state management?** → [Multi-Agent Patterns: Pattern 5 — The Harness Architecture](Multi_Agent_Patterns.md)

---

## Key Principle

**The framework extends, not changes.** Everything that produces reliable single-agent systems produces reliable multi-agent systems — with higher stakes at every decision point, and with contamination risks that require explicit architectural responses at the boundaries between agents.

---

*Ready to begin? Start with [Multi-Agent Foundations](Multi_Agent_Foundations.md) →*
