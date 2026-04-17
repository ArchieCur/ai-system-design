# Movement 2: The Curriculum Was Already Here

> *"From a model's perspective, what causes cognitive friction?"*
>
> That was the question. Not: how do we build a harness? Not: how do we
> orchestrate agents? Not: how do we prevent drift? Those were answers that
> arrived later. The question came first — and the question turned out to be
> the right one.

---

## A Different Starting Point

Every source in the 2026 convergence approached harness engineering from the
**outside in**: what does the system need to do, and what structure around the
model makes that possible?

The AI System Design curriculum approached it from the **inside out**: what does
the model experience, and what causes that experience to produce unreliable
output?

These are not competing questions. They are complementary — and the difference
in starting point determines what each approach can reach.

The research establishes the architecture: what a harness is, what components it
requires, and why those components produce reliable systems. That is rigorous,
essential work. What it does not yet provide — across all ten sources, individually
or collectively — is the methodology for building it. How to write a specification
that prevents drift. How to design a skill that reduces cognitive friction rather
than adding to it. How to engineer the evidence flow between agents so that drift
cannot propagate undetected.

That layer is what practitioners need at the bench. And it is what the inside-out
starting point produces — because when you begin with what the model experiences,
you build toward enabling reliable output rather than constraining unreliable
output. The research and the curriculum are working the same problem from both
ends. This is where they meet.

---

## How the Curriculum Maps to the Field

The ten sources in the convergence each named pieces of the architecture. The
curriculum, built earlier, contained them all — under different names, arrived at
through different reasoning, but structurally identical when the mapping is made
explicit.

---

### Specifications → Kim's Context/Constraint/Convergence + NLAH Contracts

Hanyang's Kim proposed a three-dimensional governance framework: Context (the
knowledge that informs the agent), Constraint (the rules that govern its output),
and Convergence (iterative refinement until the harness produces no further
structural change).

The curriculum's Specifications framework maps directly:

| Kim's Dimension | Curriculum Layer | Function |
|---|---|---|
| Context | CONTEXT + INTENT | What the model needs to know and why |
| Constraint (Guidance) | SHOULD Guidelines | Probabilistic behavioral shaping |
| Constraint (Enforcement) | MUST Constraints | Non-negotiable boundaries |
| Convergence (mechanism) | Verification Protocols | Per-output: does output match intent? |
| Convergence (criterion) | Specification Convergence | Harness-stability termination condition |

The Shenzhen/Tsinghua team's NLAH Contracts — required inputs and outputs,
validation gates — map to the MUST layer. Their Stage structure maps to the
workflow topology in Multi-Agent specifications. Their Failure taxonomy maps to
the error recovery patterns in Verification Protocols.

The curriculum built these layers from a simple question: *what does the model
need to not guess?* Kim and the Shenzhen team built them from governance
theory and formalization research. Same structure. Different roads.

The mapping table captures the mechanism. What the curriculum also names
explicitly is the criterion: the point at which the specification is done.

Kim calls this structural idempotence — the termination condition for harness
development. A specification has converged when re-applying its rules produces
identical structural outcomes. If a second pass changes anything, the rule set is
incomplete or conflicting and needs further refinement.

The curriculum achieves this state through iterative Verification Protocol runs —
finding gaps, refining constraints, running again. **Specification Convergence**
is the named milestone for that process: the point at which iterating on the
specification produces no further structural change in agent output. It is not a
property of any single run. It is a property of the specification itself — the
signal that the harness is sufficiently complete.

Verification Protocols are how you test for it. Specification Convergence is
what you are testing for.

One element the curriculum added that the governance frameworks did not:
the **Supremacy Clause** — a non-negotiable constraint block embedded directly
in the specification, not applied post-hoc. The TONE experiments (documented
in Movement 3) showed why this matters: without enforcement embedded in the
specification, agents operating under in-context pressure drift toward the path
of least resistance. The Supremacy Clause is not a guardrail on top of the
specification. It is load-bearing architecture inside it.

---

### Skills → Lopopolo's Reusable Control Procedures + LangChain's Progressive Disclosure + Stanford's Undifferentiated Skill Object

Ryan Lopopolo, building at OpenAI, reinvented Skills from first principles before
Anthropic shipped them as a product feature. His team called them the same
thing: reusable control procedures embedded in the harness that the agent reads
as governing context.

LangChain named the problem Skills solve: **progressive disclosure**. Loading all
tools and context at agent start degrades performance before the agent can begin
working. Skills inject reusable, domain-specific prompt templates lazily — only
when needed, in a form the model can use without guessing.

Stanford's Meta-Harness paper uses "skill" to mean an undifferentiated
natural-language instruction set — combining what the curriculum separates into
Specifications (laws), Skills (reusable procedures), and system-level context (CLI
commands, directory layout, output format) into a single object doing three jobs.
The paper cites Anthropic's agentskills repository when using this term, indicating
awareness of the framework — but without the architectural separation the
curriculum provides. That the field's most rigorous harness optimization research
had not yet made those distinctions is itself evidence of the methodological layer
the curriculum occupies. The differentiation between components is not incidental
to the curriculum's architecture. It is the architecture.

The curriculum's Skills framework contains elements the 2026 research had not
yet formalized:

- **The Unload Condition** — a trigger for user intent change that releases a
  skill when the task it was loaded for is complete, preventing stale context
  from contaminating subsequent reasoning. The research identifies progressive
  disclosure as important. It does not address what happens when the disclosed
  context is no longer needed.
- **The Class A/B/C Tool Classification System** — a taxonomy for categorizing
  tools by cognitive load and risk profile, enabling architectural enforcement of
  correct tool behavior rather than persuasive instruction. The research documents
  tool use. It does not provide a classification framework that makes tool safety
  a structural property rather than a specification property.
- **The Tool Library** — a structured catalog that Skills draw from, ensuring
  consistent tool definitions across agent roles and preventing the drift that
  occurs when the same tool is described differently in different contexts. The
  research documents tool integration. It does not address cross-agent tool
  definition consistency as a harness-level design concern.

These are not theoretical additions. They were built by asking: *where does the
model guess when working with tools, and how do we eliminate that guess?*

---

### Evidence Reset Protocols → Anthropic's Context Resets

Anthropic's engineering team, documenting harness design for long-running
applications, arrived at a pattern they called **context resets**: clearing the
context window entirely and starting a fresh agent with a structured handoff
carrying prior state. Their motivation: context anxiety and belief drift.

The curriculum documented the same pattern as **Evidence Reset Protocols**,
derived from the Bayesian belief dynamics research that showed how accumulated
context shapes the prior over every subsequent inference. When the prior has
been contaminated by drift — by in-context pressure, by conflicting instructions,
by the positional decay of critical constraints — the most reliable intervention
is not a reminder injected at distance. It is a fresh context carrying only the
evidence the next inference actually needs.

Anthropic's engineers arrived at this independently because the problem demands
it. The curriculum arrived at it because the Bayesian framing made it visible
earlier: if the model's output is a function of its evidence stream and its priors,
then corrupted evidence requires a reset, not a patch.

---

### The Harness Architecture → Lopopolo's Symphony + Microsoft's Fleet Governance

The curriculum's Multi-Agent Systems section documented the cascade problem:
everything that causes individual agent drift becomes a system-level cascade risk
when agents communicate with each other. A belief state that shifts in one agent
gets injected as evidence into the next agent's context window. Drift propagates.

Lopopolo's Symphony — an orchestration system for managing large numbers of
coding agents in parallel, with an escalation ladder and neighborhood-style
monitoring — is the engineering implementation of this insight at scale. Microsoft's
Azure SRE Agent fleet, governing 35,000+ incidents with role-based access and
clear escalation paths, is its operational instantiation.

The curriculum's contribution was naming the mechanism: **coalition drift** —
drift by architectural position, not by disposition. An agent does not fail because
it has bad values. It drifts because its position in the evidence stream exposes it
to in-context pressure that accumulates faster than its constraints can absorb.
The harness must be designed with this in mind from the first agent role
specification, not patched at the orchestration layer after drift has already
occurred.

---

### Context Engineering → OpenDev's Five-Stage Compaction + LangChain's Context Rot

The curriculum's Advanced Prompting section documented **context rot** as a
first-class failure mode — the degradation of model performance as the context
window fills with stale, irrelevant, or conflicting evidence. The curriculum's
treatment of episodic resets, token budget management, and evidence prioritization
predates the field's formalization of these patterns.

OpenDev's five-stage compaction pipeline — Warning at 70%, Observation Masking
at 80%, Fast Pruning at 85%, Aggressive Masking at 90%, Full Compaction at 99%
— is the production engineering implementation of the same insight: context is
a finite resource, and managing it actively is not optional. Their finding that
typical session length extended from 15-20 turns to 30-40 turns after implementing
progressive compaction confirms the curriculum's framing: context rot is
measurable, and its effects are large.

LangChain named Skills as the solution to a specific form of context rot —
the cognitive overhead of loading all tools at agent start. The curriculum's
Skills framework was built to solve the same problem: *the model cannot reason
well about a tool it cannot see clearly, and it cannot see clearly when the
context is cluttered.*

---

## What the Curriculum Added That the Field Has Not Yet Named

The ten sources in the convergence document the harness architecture
comprehensively. They establish what a harness is, what components it requires,
and why those components produce reliable systems. That is rigorous, essential
work — and it stops there.

The research tells you what a harness needs. It does not tell you how to build
one that works under real conditions — when the model is guessing, when context
is rotting, when drift is subtle, when tools conflict, when agents hand off to
each other and contamination propagates. Most sources address one component.
None address the full stack. None provide the operational knowledge a practitioner
needs at the bench today.

The curriculum was built to fill exactly that layer. Its three-component
architecture maps directly to the operational demands the research names but
does not resolve:

| Component | Role | What It Addresses |
|---|---|---|
| **Prompts** | Ephemeral intent | *"Build me a login page"* — task-specific, disposable |
| **Skills & Tools** | Reusable procedures | *"How to write secure code"* — loaded when needed, unloaded when done |
| **Specifications** | Persistent constraints | *"Use PostgreSQL, never hardcode passwords"* — always present, non-negotiable |

Together, these three components enable reliable AI system design by eliminating
the conditions under which models guess. Prompts express what the practitioner
wants. Skills and Tools give the model the reusable procedures it needs to act.
Specifications hold the constraints that make the output trustworthy regardless
of what the prompt requests.

The research documents each of these component types in isolation. What it has
not yet formalized is the operational methodology for building them — the
practitioner knowledge that only emerges from asking not *what does the system
need* but *what does the model experience*:

**How to write a Specification that prevents drift** — not just what constraints
to include, but how to structure them so enforcement is architectural rather than
persuasive. The Supremacy Clause is not a reminder. It is load-bearing structure.
Verification Protocols are not checklists. They are the mechanism for testing
whether the specification has achieved Specification Convergence — the state in
which iterating on the constraints produces no further structural change in output.

**How to design Skills that reduce cognitive friction** — including the Unload
Condition (releasing a skill when the task it was loaded for is complete, so stale
context does not contaminate subsequent reasoning), the Class A/B/C Tool
Classification System (categorizing tools by cognitive load and risk profile so
that tool safety becomes a structural property rather than a specification
property), and the Tool Library (a structured catalog ensuring consistent tool
definitions across agent roles, preventing the drift that occurs when the same
tool is described differently in different contexts).

**How to engineer the evidence flow between agents** — so that drift at the
individual agent level cannot propagate undetected through the system. The
research names cascade risk. The curriculum provides the design methodology
for preventing it: specification architecture that accounts for the evidence each
agent will receive, not just the behavior each agent should produce.

These are not theoretical additions. They were built by asking the question the
curriculum was built to answer: where does the model guess, and how do we
eliminate that guess?

The Specifications module provides templates, worked examples, and anti-patterns
a practitioner can apply at the bench today. That operational layer is what the
inside-out starting point produces — and what the outside-in research, for all
its rigor, has not yet reached.

That distinction is what Movement 3 documents in experimental detail.

---

## The Principle That Unifies Everything

Every element of the curriculum maps to the harness engineering research because
every element of the curriculum was built from the same underlying principle that
the harness engineering research independently confirmed:

**The model's output is a function of its evidence stream. Design the evidence
stream, and you design the output.**

This is not prompt engineering. Prompt engineering asks: *what words should I
use to get the model to do what I want?* This is evidence engineering: *what
does the model need to receive, in what form, at what time, with what constraints,
so that reliable output is the most coherent response available?*

The difference matters. Prompt engineering treats the model as a black box to be
coaxed. Evidence engineering treats the model as a reasoning system with
predictable behavior given well-structured inputs. The harness is the structure.
The curriculum is the design guide for building it.

Red Hat's Marco Rizzi, arriving at this from field experience, captured it in four
words: *Structure in, structure out.*

The curriculum, built from the cognitive friction question, built toward the same
four words before the field had a name for what it was building toward.

---

*Continue to [Movement 3: What the TONE Experiments Found](harness-engineering-movement3.md)*
