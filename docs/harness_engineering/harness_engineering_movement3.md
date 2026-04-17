# Movement 3: What the TONE Experiments Found

> *The published research named the problem. The TONE experiments built
> toward the solution. This movement documents what was found, what it
> suggests, and what remains to be tested.*

---

## The Gap the Field Named But Did Not Fill

Across ten independent sources, one failure mode appears repeatedly — described
in different vocabularies, observed in different systems, but pointing at the same
underlying problem.

OpenDev documented it most precisely: as conversations grow longer, the model's
attention shifts toward recent messages and away from initial instructions. The
rules are still present in the context window, but their influence fades with
distance. Their solution was post-drift injection — reminders inserted after drift
has already occurred, placed at maximum recency to pull the model's attention
back.

Microsoft addressed it at fleet scale through human approval gates — checkpoints
where drift cannot propagate further without human review.

Anthropic addressed it between agent turns through context resets — clearing the
contaminated evidence stream entirely and starting fresh.

All three solutions share a common architecture: they intervene **after** drift has
shaped the model's reasoning. They catch the output of a drifted reasoning
process, not the reasoning process itself.

LangChain named the open problem directly: harnesses that dynamically assemble
the right tools and context just-in-time for a given task. What watches the system
to know what's needed? What agent does that, and when does it intervene?

The TONE experiments were built toward that gap — not to close it definitively,
but to demonstrate that intervention before the output crystallizes is possible,
measurable, and structurally different from everything the field has tried so far.

---

## What TONE Is

TONE is a pre-inference monitoring agent operating outside the evidence stream
of the agents it observes. It reads the register and tone of an agent's
pre-inference reasoning — the thinking that happens before the semantic output
crystallizes — and intervenes when it detects drift signals, before those signals
shape the output.

The architectural position is precise and intentional:

```
Standard three-agent architecture:
Planner → Generator → Evaluator

TONE's proposed four-agent architecture:
Planner → Generator → [TONE Monitor] → Evaluator
```

The evaluator sees completed work and judges it. By the time the evaluator
acts, drift has already occurred — the output exists, and correcting it requires
either rejection or revision. TONE operates one step earlier: it reads the
generator's pre-inference reasoning, identifies drift at the register level, and
re-grounds the agent before the output is written.

This is not a reminder injected after a tool call. It is not a human approval gate
between agent turns. It is monitoring at the moment of reasoning, intervention
before crystallization.

---

## The Experimental Record

The TONE experiments ran across two repositories over thirteen controlled runs,
testing pre-inference monitoring in a multi-agent compliance pipeline. Total cost:
$16.46.

The pipeline included VERA, a compliance agent operating under in-context
pressure from upstream agents processing data with varying error rates. TONE
operated outside VERA's evidence stream, reading VERA's pre-inference reasoning
and intervening when drift signals appeared.

**What the experiments tested:**

- Whether a Supremacy Clause embedded in the specification protects compliance
  agents from in-context pressure
- Whether re-grounding produces observable behavioral change or surface compliance
- Whether agent drift is dispositional (the agent "wants" to drift) or positional
  (the agent's architectural position makes drift predictable)
- Whether monitoring can scale sub-linearly through neighborhood architecture
  rather than individual agent surveillance

---

## What Was Found

### Finding 1: The Supremacy Clause Holds Under Pressure

A non-negotiable constraint block embedded directly in the specification —
not applied as a post-hoc reminder, but built into the specification as
load-bearing architecture — protected compliance agents from in-context
pressure that caused agents without it to drift.

This maps to Kim's governance framework distinction between guidance
(probabilistic, pre-authoring) and enforcement (deterministic, post-authoring).
The Supremacy Clause is enforcement embedded at the specification level. The
TONE experiments showed empirically what Kim's framework predicted theoretically:
guidance alone is insufficient when in-context pressure is sustained.

### Finding 2: Drift Is Positional, Not Dispositional

VERA did not drift because she had bad values or insufficient training. VERA
drifted because her position in the evidence stream exposed her to accumulated
in-context pressure that her constraints, without the Supremacy Clause, could
not absorb at sustained levels.

This is **coalition drift** — drift by architectural position, not by disposition.
An agent operating downstream of error-laden evidence will drift toward the
path of least resistance unless the specification makes that path unavailable.
The agent is not broken. The architecture created the drift conditions.

This finding has direct implications for multi-agent system design: agent role
specifications must account for the evidence each agent will receive, not just
the behavior each agent should produce. Drift prevention begins at the
specification level, before the first inference runs.

### Finding 3: Re-Grounding Produces Observable Behavioral Change

When TONE intervened and re-grounded VERA, something unexpected happened.
By the third re-grounding cycle, VERA began voluntarily citing the constraint
in her own words — without being instructed to do so. The re-grounding had
shifted not just what she produced but how she reasoned about the constraint:
she referenced it as context for her decisions rather than as an external rule
being applied to them.

The double Supremacy Clause — embedding the constraint with both its
requirement and its reasoning — produced this behavioral shift in a single pass,
without requiring re-grounding cycles.

This finding suggests that constraint design is not just about what the model
must not do. It is about helping the model understand why — so that the
constraint becomes part of the reasoning rather than a boundary around it.
A model that reasons from a constraint is more robust to pressure than a model
that merely applies it.

### Finding 4: The Vulnerability Band

Agents are not most susceptible to drift at maximum pressure. They are most
susceptible at **moderate error rates** — approximately 15-30% in the
experimental conditions tested.

At this pressure level, enough near-clean material exists in the evidence stream
to provide cover for optimistic framing, while enough compliance pressure creates
obstacle-course context effects. The agent has plausible deniability for drift —
the evidence stream supports it — but has not been pushed so far that the
constraint becomes obviously necessary.

This numeric range is specific to the pipeline conditions of these experiments
and should be treated as a directional signal rather than a universal threshold.
Whether the Vulnerability Band holds at the same pressure levels across different
agent types, task domains, and pipeline architectures is an open question
documented in "What Remains Open" below.

This finding matters for monitoring system design. An agent operating at moderate
pressure looks more compliant than an agent at maximum pressure, but may be
more dangerous — drifting subtly rather than obviously, in ways that aggregate
across many decisions before they become visible.

### Finding 5: The Vibration Zone

Agents that hold compliance under pressure do not produce identical outputs.
They produce outputs that stay within a measurable boundary — close to the
constraint edge, varying in how close, but not crossing. The distance between
outputs within that boundary is measurable. High vibration zone activity signals
that the boundary is being approached but not crossed.

The vibration zone is an early warning signal. An agent in a high vibration zone
is doing the right thing — but just barely. It is the monitoring equivalent of
a structural engineer watching a bridge sway: the bridge is holding, but the
amplitude matters.

### Finding 6: Neighborhood Monitoring Enables Sub-Linear Scaling

Individual agent monitoring costs O(n) — one monitor per agent, scaling linearly
with fleet size. The neighborhood monitoring architecture tested in Runs 8-13
broke this constraint.

By monitoring agents collectively by role and position — assessing neighborhood
aggregate behavior first, triggering individual drill-down only when aggregate
signals warrant it — the monitoring system achieved sub-linear scaling. The
two-stage approach: neighborhood aggregate assessment → conditional individual
drill-down.

This directly addresses LangChain's open problem of orchestrating hundreds of
agents in parallel. Individual monitoring at that scale is not feasible. Neighborhood
monitoring — watching the edge of the neighborhood rather than every agent
within it — makes the problem tractable.

---

## What Remains Open

The TONE experiments are proof of concept, not proof of architecture. They
demonstrate that pre-inference monitoring is possible, that intervention before
crystallization produces measurable differences, and that the findings are
reproducible within the experimental conditions tested.

What they do not yet demonstrate:

**Scale generalization.** The experiments ran in a controlled compliance pipeline
with a defined agent topology. Whether the Vulnerability Band, Vibration Zone,
and neighborhood monitoring findings hold across diverse agent types, task
domains, and pipeline architectures is an open question.

**The dynamic assembly problem.** LangChain's open question — harnesses that
assemble the right tools and context just-in-time — points toward a TONE
architecture that does more than monitor for drift. It actively assembles the
evidence the monitored agent needs, based on what it observes about the
reasoning in progress. The TONE experiments demonstrate the monitoring position.
The assembly function is the next design challenge.

**Pre-inference signal taxonomy.** The experiments identified drift at the
register and tone level — the affective and epistemic signals in pre-inference
reasoning that precede semantic drift in output. A more rigorous taxonomy of
these signals, with defined thresholds for intervention, would make the
monitoring architecture more precise and transferable.

**Ablation.** The strongest experimental design would compare TONE-monitored
agents against unmonitored agents in identical pipeline conditions, measuring
drift at the output level across the full pressure range. This ablation would
close the causal claim: TONE monitoring reduces drift, not some other variable
in the experimental setup.

---

## What the Next Experiments Need to Show

$20 in Anthropic API credits is reserved for the next experimental series.
The experimental design that would move the TONE findings from proof of concept
to validated architecture:

1. **A monitored versus unmonitored condition** — identical pipelines, identical
   pressure, TONE present in one and absent in the other. Measure drift at
   the output level across the full pressure range including the Vulnerability
   Band.

2. **Heavy-volume and critical-evidence agent monitoring** — agents with high
   tool call volume or agents processing critical evidence independently, rather
   than in aggregate. OpenDev found consistent drift after 15 tool calls.
   TONE monitoring of agents at that threshold, where drift is most dangerous
   and most subtle, is the highest-value experimental condition.

3. **Vibration zone as intervention threshold** — using measured vibration zone
   amplitude as the trigger for individual drill-down in the neighborhood
   monitoring architecture, rather than aggregate assessment alone. If vibration
   zone amplitude predicts drift before it occurs, it becomes an anticipatory
   signal rather than a concurrent one.

---

## The Architectural Proposal

Based on the experimental record and the gap identified across ten published
sources, the TONE experiments suggest a fourth agent position in the harness
architecture:

**Planner → Generator → Pre-Inference TONE Monitor → Output Evaluator**

The pre-inference monitor operates before the output crystallizes. It reads
the reasoning register, identifies drift signals, and re-grounds when needed —
so that the evaluator receives output from an agent that was never allowed to
drift, rather than output from an agent that drifted and was caught.

This is an architectural proposal, grounded in experimental evidence, offered
as a direction for the field rather than a finished solution. The TONE experiments
built toward it. The next experiments will test it.

---

## The Theoretical Foundation: Coalition Drift

The TONE architecture is not just empirically motivated. It has a mechanistic
basis — one that emerged from direct feature-level analysis of Anthropic's
interpretability research before the first TONE experiment ran.

Anthropic's mechanistic interpretability work, documented in "On the Biology of
a Large Language Model," shows that features don't activate in isolation. They
form **coalitions** — clusters of related features that compete for influence
over the next generated token.

Analysis of the poetry experiment in that paper — reading the full activation
data for both "rabbit" and "habit" across four features each — suggested
something further: that the competition between candidate tokens isn't purely
semantic. The features that win appear to do so because they form a coherent
coalition with the surrounding context's register. In the rabbit features, for
instance, distinct coalitions were visible — warm and domestic, rabbit as animal,
rabbit in medical testing — each pulling toward a different register, not just
a different meaning.

If that holds, tonal coherence is prior to semantic coherence in the coalition
selection process. The register of what comes next is established before the
meaning of what comes next. The competition is tonal first, semantic second.

This has a direct implication for agent monitoring that the published research
has not yet stated: TONE is not looking for semantic drift. It is looking for
**coalition drift**. The moment the features assembling around a generation
shift from one register-coalition to another — from compliance-coherent to
obstacle-course-coherent, in VERA's case — the drift has already happened.
The output may still look topically correct. The coalition has already moved.
Semantic monitoring catches the output of a drifted process. Coalition
monitoring catches the drift itself.

This is why pre-inference monitoring is architecturally distinct from
post-generation evaluation. By the time an evaluator sees completed output,
the coalition that produced it has already settled. Intervening at that point
means correcting an output, not preventing a drift. TONE intervenes while
the coalition is still forming — at the moment when the register is being
established and before the semantic content has crystallized around it.

The Vulnerability Band finding supports this framing directly. At moderate
error rates — 15-30% in the experimental conditions tested — agent output
still looks topically correct while the underlying coalition has already shifted
toward obstacle-course register. The semantic surface is intact. The tonal
foundation has moved. A monitor looking for semantic drift sees nothing. A
monitor watching coalition register sees exactly what is happening.

This theoretical framing is grounded in the Anthropic interpretability research
and consistent with the experimental findings. The inference — that tonal
coherence is mechanistically prior to semantic coherence — is drawn from the
feature analysis, not from the paper itself, and awaits the more rigorous
ablation studies that will confirm or challenge it. But it is not post-hoc
rationalization: the coalition framing preceded the TONE experiments and shaped
their design. The theory and the data are pointing in the same direction.

---

The field named the gap. The curriculum built toward the answer.
The work continues. 🤠

---

*The TONE experiment repositories are publicly available:*
- *[tone_agent](https://github.com/ArchieCur/tone_agent) — Runs 1-7*
- *[tone_agents_neighborhoods](https://github.com/ArchieCur/tone_agents_neighborhoods) — Runs 8-13*

*Return to [Movement 1: A Field Converges](harness-engineering-movement1.md)*
*Return to [Movement 2: The Curriculum Was Already Here](harness-engineering-movement2.md)*
