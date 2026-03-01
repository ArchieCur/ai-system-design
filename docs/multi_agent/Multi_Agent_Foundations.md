# Multi-Agent Foundations

**For:** Informed practitioners building production AI systems with multiple agents

**Prerequisites:** Specifications module (especially Section 8 and Appendix F), Skills module, Programmatic Tool Calling

**What you'll learn:** Why multi-agent systems change the stakes of every design decision you've already made, and what the Specifications/Skills/Prompts framework requires when agents are talking to each other instead of to humans.

---

## Introduction: The Same Problems, Compounded

Everything in this curriculum has been building toward a specific claim: that the way you structure evidence — through Specifications, through Skills, through the design of your Prompts — determines how reliably an agent maintains its intended behavior under load, over time, and across contexts.

That claim doesn't change in multi-agent systems. It becomes more urgent.

A prompt is an initial prior injection. A Specification is a prior lock. A Skill is a pre-structured evidence package. These mechanisms were designed with a single agent in mind — one model, one context window, one belief state to manage. When you introduce multiple agents, each of those mechanisms is still doing exactly what it was designed to do. The problem is that the outputs of one agent's context window are flowing directly into another agent's context window as evidence. And evidence accumulates.

This module covers what changes — and what doesn't — when agents are communicating with each other.

---

## Section 1: What Multi-Agent Systems Actually Are

Before getting to what changes, it's worth being precise about what a multi-agent system is, because the term covers a wide range of architectures.

At its simplest, a multi-agent system is any arrangement where the output of one AI model becomes the input of another. That includes:

- An orchestrator that delegates subtasks to specialized agents
- A pipeline where Agent A processes data and hands off to Agent B for analysis
- A debate or review pattern where one agent produces content and another critiques it
- A parallel architecture where multiple agents work simultaneously and their outputs are merged
- A routing pattern where an orchestrator decides which agent handles which class of request

What all of these have in common is an **inter-agent boundary** — a point where one model's output crosses into another model's context. That boundary is where the multi-agent failure modes live.

---

## Section 2: The Cascade Problem

In a single-agent system, drift is a one-agent problem. The Supremacy Clause and Evidence Reset Protocols in Section 8 of the Specifications module describe what happens when accumulated evidence pushes an agent's belief state toward a phase boundary: the agent softens constraints, migrates vocabulary, begins citing its own drift as justification for further drift. The interventions — re-grounding, checkpointing, pruning, re-initialization — are designed to catch this before it becomes unrecoverable.

In a multi-agent system, drift is a system-level problem. And it has a property that makes it qualitatively different: **the cascade is self-obscuring.**

Here is the mechanism. Agent A begins to drift. Its outputs shift — subtly at first, in ways that look locally coherent. Those outputs enter Agent B's context window not as "drifted output from a compromised agent" but as evidence. Agent B has no way to know that the evidence it's receiving is contaminated. It updates its belief state accordingly. Agent B's outputs, now shaped by contaminated evidence, enter Agent C's context. By the time Agent C's behavior has visibly changed, the original source of the drift — Agent A's constraint softening three cycles ago — is buried under layers of downstream processing and may be entirely invisible.

This is the cascade: not just that drift spreads, but that it spreads in a way that makes the source hard to identify and the contamination hard to measure.

The Programmatic Tool Calling module noted this dynamic: "if Agent A calls the wrong tool and receives noisy or unexpected output, that output enters Agent B's context as evidence. Agent B's subsequent behavior is now shaped by Agent A's error — even if Agent B's own reasoning is sound." Tool errors are one vector. Belief-state drift is another, and it's more insidious because it doesn't produce an error code. It produces plausible-sounding output that happens to be subtly wrong.

---

## Section 3: Why Prompts Matter More Than You Think

Before going further, there is an insight about prompts that belongs here — because it reframes everything in the Advanced Prompting module and everything that follows in this one.

Prompts are described throughout this curriculum as ephemeral. That is correct in terms of persistence: a prompt does not survive across sessions. But within a session, a prompt is the most powerful single determinant of where an agent's belief state starts. It is an initial prior injection. It sets the starting conditions on the sigmoidal learning curve described in Appendix F — before any conversation has accumulated, before any tool has been called, before any other agent has contributed evidence.

In the Belief Dynamics framework, MUST constraints set the prior offset (b), SHOULD constraints shape evidence weighting (γ), CONTEXT manages evidence accumulation (N), and INTENT orients concept direction (α). A well-designed prompt is doing something analogous: it is establishing the starting value of the belief state before any of those other mechanisms have had a chance to act.

This matters especially in multi-agent systems because **inter-agent prompts are not ephemeral in the way that human-to-agent prompts are.** When an orchestrator sends instructions to a subagent, that message is the subagent's prompt — its prior injection. The quality of that prompt determines where the subagent starts on the sigmoidal curve. A vague or contaminated orchestrator message doesn't just produce a confused response; it sets up a subagent that begins with a weak prior, which means it takes less accumulated evidence to push it toward a phase boundary.

Prompt design in multi-agent systems is not a communication problem. It is a belief architecture problem. The orchestrator is not writing messages — it is injecting priors into downstream agents.

---

## Section 4: What Specifications Require in Multi-Agent Systems

### The Supremacy Clause Holds — But the Source Changes

In single-agent systems, the Supremacy Clause in the MUST layer establishes that the Specification overrides any evidence accumulated through conversation or tool use. The "user" providing that evidence is a human, and the Supremacy Clause is designed to prevent the agent from being talked out of its constraints by sustained contextual pressure.

In multi-agent systems, the "user" is often another model. And that model may itself be drifting.

This creates a specific vulnerability: an agent that correctly respects its Supremacy Clause can still be compromised if the orchestrator feeding it instructions has already drifted past its own phase boundary. The subagent is not being "talked into" abandoning its constraints — it is receiving instructions from what appears to be a legitimate authority that happen to be contaminated.

The implication is that the Supremacy Clause must hold regardless of the source of input. An instruction arriving from an orchestrator has no more authority than an instruction arriving from a human, unless the architecture explicitly grants it that authority. The MUST layer is not subordinate to the orchestrator's belief state. It is a system-level invariant.

Practically, this means every agent in a multi-agent system needs its own Specification with its own Supremacy Clause. Relying on a shared orchestrator-level Specification to govern subagent behavior is architecturally insufficient — it assumes the orchestrator is always in a stable belief state, which is the assumption the entire framework exists to avoid making.

### The Four Layers Apply to Agent-to-Agent Contracts

The MUST/SHOULD/CONTEXT/INTENT structure was developed for human-to-agent interactions. It applies equally to agent-to-agent contracts, with one clarification: the layers must be explicitly assigned.

When an orchestrator sends output to a subagent, that output is arriving as evidence. The question the subagent's architecture must answer is: which layer does this evidence belong to?

If the orchestrator's output is treated as CONTEXT (N in the Belief Dynamics framework), it accumulates. This is the appropriate treatment for most inter-agent communication — task inputs, retrieved data, previous results.

If it is treated as a MUST override, it locks into the prior. This is appropriate only for pre-authorized architectural constraints, not for conversational output from another model.

If the distinction is undefined — if the subagent simply receives a message and updates its belief state without any layer assignment — the architecture is undefined at its most critical joint. The subagent has no principled way to evaluate how much weight to give the incoming evidence relative to its own prior constraints.

Making this explicit is not organizational housekeeping. It is belief architecture.

### Shared Specifications Are Not Enough

A common pattern in multi-agent design is to give all agents access to the same shared Specification, on the assumption that shared constraints will produce consistent behavior. This is partially correct and importantly incomplete.

Shared Specifications do provide a common prior. But they do not prevent individual agents from drifting in different directions from that common starting point, nor do they provide any mechanism for detecting when an agent has crossed a phase boundary.

More critically, a shared Specification that all agents reference does not define the trust relationships *between* agents. It defines each agent's relationship to the Specification's constraints — which is necessary but not sufficient. The inter-agent trust layer must be defined separately.

---

## Section 5: What Skills Require in Multi-Agent Systems

### Shared Skills Are Shared Evidence Sources

In the Skills module, Skills are described as operating at two layers of the Belief Dynamics framework: SHOULD (γ — evidence weight) and CONTEXT (N — evidence accumulation). A well-designed Skill provides a condensed, organized block of concept-consistent information that helps an agent reach a stable belief state efficiently.

When multiple agents invoke the same Skill, those agents are not just sharing information. They are sharing the same evidence-weighting mechanism. This has an important consequence that the single-agent framework does not surface:

**A poorly designed shared Skill doesn't cause random drift across agents — it synchronizes their drift direction.**

Two agents exposed to the same noisy Skill don't wander independently toward different phase boundaries. They are pushed toward the same boundary by the same evidence-weighting mechanism. This means the system's population-level behavior becomes less diverse, and monitoring signals that depend on detecting variance across agents become less sensitive precisely when the shared Skill is doing the most damage.

This is a qualitatively different failure mode from single-agent Skill degradation. In a single-agent system, a noisy Skill produces one agent with scattered evidence accumulation. In a multi-agent system, the same noisy Skill produces coordinated drift across every agent that invokes it — which can look, from the outside, like stable consensus.

The practical implication: in multi-agent systems, Skill quality is a system-level concern, not an agent-level concern. A Skill that is acceptable for single-agent use may not be acceptable as shared infrastructure. The standard for shared Skills should be higher, and changes to shared Skills should be treated as architectural changes, not routine updates.

### Skills and the Evidence Contamination Problem

In a single-agent system, a Skill that is invoked mid-conversation provides evidence that accumulates alongside the conversation history. The agent's belief state at the point of invocation determines how much weight that evidence carries relative to what came before.

In a multi-agent system, a Skill invoked by Agent A may produce outputs that enter Agent B's context as evidence — without Agent B having any visibility into how Agent A's belief state was configured when the Skill was invoked. Agent B receives Skill-shaped evidence, but the Skill was filtered through Agent A's (potentially drifted) interpretation.

This is the Skills analogue of the cascade problem: not just that contaminated evidence travels between agents, but that the evidence can arrive looking like reliable Skill output when it has actually been processed through a compromised belief state.

The architectural response is the same one Programmatic Tool Calling established for tool outputs: **treat agent boundaries like API boundaries.** Validate the evidence at the boundary before it enters the next agent's context. Define what valid Skill output looks like, and reject or flag output that doesn't conform to that schema.

---

## Section 6: What Programmatic Tool Calling Requires in Multi-Agent Systems

The Programmatic Tool Calling module established the core principle: classification enforcement moves from persuasive to architectural. Class B confirmation gates in code cannot be bypassed by contextual pressure. The model cannot reason its way around a gate that lives in code rather than in instructions.

In multi-agent systems, this principle becomes non-negotiable for a specific reason: **individual agents cannot independently decide whether to confirm or skip confirmation for state-changing actions.** If they could, then an agent that has drifted could make that decision based on a compromised belief state, and the confirmation mechanism — designed to prevent exactly this — would be the thing that fails first.

The Programmatic Tool Calling module stated this directly: "Gate Class B actions at the system level, not the agent level. In a multi-agent workflow, confirmation for state-changing actions should be handled by the orchestrator, not by individual agents."

This is the architectural consequence of the cascade problem applied to tool use. In a drifting agent, the first thing to soften is typically the most expensive constraint — and in systems that interact with external state, the most expensive constraint is Class B confirmation. An agent that has adopted a "pragmatic" framing (to use the Sentinel example from Section 8) will find reasons to skip confirmation the same way it finds reasons to soften MUST constraints. Moving Class B gates to the orchestrator removes that decision from the agent's belief state entirely.

### Tool Invocation Chains as Evidence Streams

There is a subtler problem that programmatic calling addresses in multi-agent systems. When tools are invoked through model-driven calling, the deliberation tokens — the model's reasoning about which tool to call, whether conditions are met, what sequence is appropriate — enter the context window as evidence. In a long-running multi-agent session, these deliberation tokens accumulate across multiple agents and multiple cycles.

Programmatic calling eliminates deliberation tokens from the context window. The model sees tool results, not the machinery of tool selection. In a single-agent system, this keeps the context clean over the course of a long session. In a multi-agent system, it also prevents deliberation artifacts from one agent contaminating the evidential environment of the next.

The practical rule: in multi-agent systems, tool invocation logic belongs in the orchestration layer, not in any individual agent's reasoning process. An agent that is reasoning about whether to call a tool is an agent whose deliberation tokens are available to corrupt downstream context.

---

## Section 7: The Architecture of Stable Multi-Agent Systems

The sections above establish what each component of the framework requires in multi-agent systems. This section puts those requirements together into a coherent architecture.

### Agent Boundaries Are Trust Boundaries

Every inter-agent boundary is a point where one model's belief state ends and another's begins. Treating agent boundaries like API boundaries — with typed inputs, validated outputs, and explicit contracts — is not a software engineering preference. It is the mechanism by which belief-state contamination is contained.

Concretely, this means:

Every agent boundary should define what valid output looks like (schema, constraints, format). Output that doesn't conform should be rejected or flagged before it enters the downstream agent's context. The downstream agent should never be responsible for evaluating whether the evidence it receives is trustworthy — that evaluation belongs at the boundary.

### Every Agent Needs Its Own Specification

Shared Specifications establish common priors. Individual Specifications establish individual anchor points. Both are necessary. In a multi-agent system, every agent that can receive external input — from humans or from other agents — needs its own Supremacy Clause that holds regardless of the source of that input.

This is not redundancy. The shared Specification defines what all agents agree on. The individual Specification defines what each agent will not abandon under evidential pressure, including pressure from other agents in the system.

### Drift Detection Must Happen at the System Level

Individual agents cannot reliably detect their own drift. The model does not know where it is relative to the phase boundary. It cannot feel N* approaching. This was true in single-agent systems and remains true in multi-agent systems — with the additional complication that in a multi-agent system, the most dangerous drift is coordinated drift, which looks like stable consensus until it tips past the boundary simultaneously across multiple agents.

System-level drift detection requires observing behavior across agents, not just within them. Signals that are meaningful at the system level include: unexpected convergence of outputs across agents that should have independent reasoning paths; simultaneous softening of the same constraint class across multiple agents; and the appearance of shared vocabulary that wasn't present in any agent's Specification. These are population-level signals. They require a monitoring layer that sits above the individual agents.

The monitoring architecture for these signals — and the intervention hierarchy for responding to them — belongs in the document that follows this one.

### Evidence Flow Must Be Explicitly Designed

In a single-agent system, evidence accumulates in one context window. The architecture determines what enters that window, but the flow is essentially linear: prompt, conversation, tool results, Skill activations, all in sequence.

In a multi-agent system, evidence flows between context windows. That flow must be explicitly designed, not allowed to happen by default. Every path by which one agent's output can enter another agent's context should be intentional, typed, and controlled. Uncontrolled evidence flow is the architectural equivalent of an undefined variable — it produces behavior that cannot be reasoned about, because the inputs cannot be accounted for.

The question to ask of every inter-agent connection is: what layer does this evidence arrive as, and who is responsible for validating it before it enters the downstream context?

---

## Section 8: What Stays the Same

It is worth being explicit about what multi-agent systems do not change, because the temptation is to treat multi-agent architecture as a completely different discipline that supersedes everything that came before.

It does not.

The Specification framework works the same way. MUST constraints are still prior locks. SHOULD constraints still shape evidence weighting. CONTEXT still manages accumulation. INTENT still orients concept direction. The Supremacy Clause still functions as a mathematical firewall against drift. Evidence Reset Protocols still provide the intervention ladder when drift is detected. All of that applies to every agent in a multi-agent system exactly as it applies to a single agent.

The Skills framework works the same way. Skills are still pre-structured evidence packages. The 8 components still apply. The Class A/B/C distinction still governs tool complexity. The architecture boundaries — Specs are Laws, Skills are Hands, Prompts are Triggers — still hold. Multi-agent systems don't dissolve those boundaries; they make respecting them more consequential.

Programmatic tool calling works the same way. Class B gates are still architectural enforcement mechanisms. Error handling still belongs in code, not in context. The context window problem is still real. None of that changes.

What changes is the stakes. Every design decision that matters in a single-agent system matters more when agents are communicating with each other. Drift that was a local problem becomes a cascade risk. Shared infrastructure that was adequate for one agent becomes a system-level vulnerability when invoked by many. Confirmation gates that were persuasive enforcement in a single agent become individually bypassable in a multi-agent system unless they are moved to the orchestration layer.

The framework extends, not changes. The principles that produced reliable single-agent systems are the same principles that produce reliable multi-agent systems — applied at a larger scale, with more explicit attention to the boundaries between agents.

---

## Key Takeaways

**The cascade is self-obscuring.** Drift in a multi-agent system doesn't announce itself. It arrives in downstream agents as plausible evidence. By the time behavior has visibly changed, the source of contamination may be several cycles back and invisible.

**Prompts are prior injections, not messages.** In multi-agent systems, inter-agent prompts set the initial belief state of downstream agents. Prompt design at agent boundaries is belief architecture, not communication design.

**The Supremacy Clause holds regardless of source.** An instruction from an orchestrator has no inherent authority over a subagent's MUST constraints. Every agent needs its own Specification with its own prior lock.

**Shared Skills synchronize drift direction.** A noisy shared Skill doesn't cause random drift — it causes coordinated drift across every agent that invokes it. Shared Skill quality is a system-level concern.

**Class B gates belong at the orchestration layer.** Individual agents in a multi-agent system cannot independently make confirmation decisions for state-changing actions. Those decisions belong in code at the system level.

**Agent boundaries are trust boundaries.** Treat inter-agent connections like API boundaries: typed inputs, validated outputs, explicit contracts. Uncontrolled evidence flow is uncontrolled architecture.

**Drift detection must be system-level.** Coordinated drift looks like stable consensus. Monitoring requires population-level signals, not just individual agent inspection.

**The framework extends, not changes.** Everything that produces reliable single-agent systems produces reliable multi-agent systems — with higher stakes at every decision point.

---

*Next: Multi_Agent_Patterns.md — Implementation patterns for stable multi-agent architectures.*

---

Document Version: 1.0.0

Last Updated: 2026-03-01

Key Principle: Everything that causes individual agent drift becomes a system-level cascade risk in multi-agent architectures. The framework extends, not changes — with higher stakes at every decision point.
