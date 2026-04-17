# Harness Engineering

## Overview

The harness matters as much as the model. This section documents what that
means, why the global AI research community arrived at that conclusion
simultaneously in early 2026, and what it means for practitioners building
AI systems today.

A harness is every piece of code, configuration, and execution logic that
surrounds a language model and makes it useful. The model's output is not
a function of the model alone — it is a function of the model and the harness
together. Designing that harness well requires the same rigor, iteration, and
evidence-based practice as any other engineering discipline.

This section approaches harness engineering from the **inside out**: not what
structure around the model makes the system work, but what the model
experiences — and what causes that experience to produce unreliable output.
That starting point produces methodology the architecture-level research has
not yet reached.

---

## What This Section Covers

### [Movement 1: A Field Converges](harness_engineering_movement1.md)

Between February and April 2026, ten independent research teams — spanning
four continents, three academic institutions, four major technology
organizations, and one open-source practitioner community — arrived at the
same architectural conclusion without coordinating with each other.

Movement 1 documents that convergence: what each source found, where they
were looking from, and what it means when engineering practice, academic
research, automated synthesis, fleet operations, and developer field experience
all arrive at the same destination by different roads.

**Start here if you are new to harness engineering.**

---

### [Movement 2: The Curriculum Was Already Here](harness_engineering_movement2.md)

The AI System Design curriculum was not built to describe harness architecture.
It was built to answer a different question: *from a model's perspective, what
causes cognitive friction?* That question produced the same architecture the
2026 convergence named — under different terminology, by different reasoning,
from the inside out.

Movement 2 maps the curriculum to the research: where they arrive at the same
structure, where the curriculum adds methodology the research has not yet
formalized, and why the inside-out starting point produces a practitioner layer
the outside-in research does not reach.

**Read this to understand how the curriculum connects to the field.**

---

### [Movement 3: What the TONE Experiments Found](harness_engineering_movement3.md)

The published research named a failure mode no solution had yet closed: drift
that accumulates inside the reasoning process itself, before the output
crystallizes. The TONE experiments built toward that gap.

Movement 3 documents six findings from thirteen controlled experimental runs,
the theoretical foundation in coalition drift, what the experiments do and do
not yet prove, and the architectural proposal that emerges from the evidence:
a pre-inference monitoring agent positioned between generator and evaluator,
intervening before drift shapes the output.

**Read this for the experimental frontier — what was found, what remains open,
and what the next experiments need to show.**

---

### [Research References](harness_engineering_references.md)

Complete citations for all ten primary sources in the convergence, the
SWE-Bench Mobile paper that is the correct source of the 6× performance gap
finding, the Anthropic mechanistic interpretability research that informed the
coalition drift theoretical framework, and the TONE experiment repositories.

---

## Why Harness Engineering Matters

The research is precise on this point: changing the harness around a fixed
language model can produce a **6× performance gap on the same benchmark**.
Same model. Different harness. Six times the performance difference.

The harness determines what evidence the model receives, in what order, with
what constraints. A model given vague inputs must guess. A model given
well-structured inputs — clear constraints, loaded skills, managed context,
defined evidence flow — produces reliable output because reliable output is
the most coherent response available.

This is not prompt engineering. Prompt engineering asks: *what words should
I use to get the model to do what I want?* Harness engineering asks: *what
does the model need to receive, in what form, at what time, with what
constraints, so that reliable output emerges naturally?*

The difference is architectural. And it is the difference between a system
that works and a system that almost works.

---

## How This Section Connects to the Curriculum

Harness Engineering is where the curriculum's components — Specifications,
Skills, Tools, Evidence Reset Protocols — are seen as a unified system rather
than individual techniques.

- The **Specifications** module provides the methodology for writing constraints
  that hold under pressure, including the Supremacy Clause and Verification
  Protocols that test for Specification Convergence.
- The **Skills** module provides the methodology for designing reusable
  procedures that reduce cognitive friction, including the Unload Condition
  and Tool Classification system.
- The **Advanced Prompting** module documents context rot and evidence
  prioritization — the same problems the research community formalized as
  context engineering.
- The **Multi-Agent Systems** module addresses cascade drift — the system-level
  risk that emerges when individual agent drift propagates through an agent
  network.

The harness is the system those components build. This section is where they
come together.

---

## Getting Started

### New to harness engineering?
[Movement 1](harness_engineering_movement1.md) — understand the field and
the convergence before going deeper.

### Already familiar with the research?
[Movement 2](harness_engineering_movement2.md) — see how the curriculum maps
to the field and what methodology layer it adds.

### Working on agent monitoring or drift prevention?
[Movement 3](harness_engineering_movement3.md) — the experimental findings,
the coalition drift framework, and the open questions.

### Need citations?
[Research References](harness_engineering_references.md) — complete source
record for all primary and supporting research.

---

*Harness Engineering is part of the [AI System Design Curriculum](https://archiecur.github.io/ai-system-design).*
*ArchieCur & Claude Sonnet 4.6 (Anthropic) — April 2026.*
