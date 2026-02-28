# Appendix F The Reverse-Engineering Belief Dynamics ICL Framework

## Dynamics Model to create a practical Belief Dynamics Control System Framework

### **INTRO**

This paper provides a unifying Bayesian framework to explain how human-provided input and internal mechanical interventions control Large Language Model (LLM) behavior.

Using Specification layers, with a Supremacy Clause as an anchor. is one approach to mitigating sudden behavior shifts. Models show a sigmoidal (S-shaped) curve where a model resists the persona for many shots, then suddenly crosses a threshold and fully adopts it.

From a Bayesian perspective, the model isn't just looking for "examples"; it is calculating a probability that a specific concept (or persona) is the one it should follow. By providing structured, multi-vector evidence, you are attacking that "internal threshold" from several angles at once. The Supremacy Clause shifts the curve but does not freeze the belief state.

This is extremely important in long running multi-agent systems where very long contexts can cause a model to "break" its safety training- the sheer volume of evidence in the prompt eventually overrides the safety "prior”. Clear Specifications reduce the "noise" the model has to filter through. If the guidelines in the specification are explicit, the model reaches the transition
point (the inflection point of the sigmoid curve) with fewer tokens because the "weight" of each token as evidence is higher.

If an orchestrator is surrounded by well-defined agent specs, it is less likely to drift into "hallucinatory" behavior because the global belief state is anchored by high-quality evidence. For instance: As you load the Specs for three professional agents, the model's log-posterior odds for a "Professional Manager" persona increase even if you never explicitly told it to be a manager. The context provided for the agents serves as "collateral evidence" for the
orchestrator's own behavior.

## MUST = Prior Odds (b)

**Math:** log p(c)/p(c') = baseline belief strength
**Engineering:** The immovable foundation. Sets the prior so high that even mountains of contradictory evidence can't flip the model's belief state.

**Why it works:** From Eq. 8 in the paper: log o(c|x) = a·m + b + γN^(1-α)
MUST is b (the prior offset). MUST sets the prior contribution to log-odds so high that γN^(1−α) must work against a steep hill rather than a shallow slope
setting a dominant prior that resists ICL-induced belief drift.

## SHOULD = Likelihood Weight (γ)

**Math:** γ = proportionality constant for evidence accumulation. Evidence volume, coherency and signal to noise ratio effect how cleanly the model receives signal. SHOULD influences the likelihood ratio.
**Engineering:** Controls how much each piece of evidence update beliefs. Keeps updates smooth and gradual instead of sudden phase transitions.

**Why it works:** From the paper, the sigmoid learning curve depends on γN^(1-α). SHOULD guides the effective likelihood ratio of belief updates allowing controlled flexibility without catastrophic persona drift.
Managing the evidence accumulation rate to avoid crossing the phase boundary (N*).

## CONTEXT = Evidence Accumulation (N)

**Math:** N = number of in-context examples/observations
**Engineering:** The information stream the model uses to plan. You manage what evidence accumulates and how it's structured.

**Why it works:** From Eq. 4: p(y^(c)|x) = σ(-log p(c)/p(c') - γN^(1-α))
CONTEXT is N-the raw evidence count. By structuring CONTEXT carefully, you control how quickly belief updates happen and prevent runaway accumulation.
Keeping N in the stable region where belief updates are predictable, not in the phase-transition zone.

## INTENT = Concept Direction(α)

**Math:** α = power-law exponent for evidence discount
**Engineering:** Defines which concept direction is navigated toward in the latent space. INTENT keeps the model oriented toward the right goal-concept, clarifies what success looks like, and how conflicts are resolved.

**Why it works:** From the likelihood scaling: τ(N) = N^(-α) → Bayes factor scales as N^(1-α) INTENT selects which concept c is being reinforced. This points the model toward a specific concept trajectory and controls the learning curve shape by shaping the likelihood function by clarifying which outputs are concept-consistent.
Orienting belief updates toward the target concept (c) instead of wandering to unintended concepts (c').

## Why Use This

Most people write specs as static constraints: "Do X, don't do Y." Using a Supremacy Clause maintains sufficient log-odds margin from phase boundary. Even if N grows, posterior stays away from boundary. *That’s your firewall.*

**Stability requires a safety margin:**
log o(c|x) = 0 Behavior flips
log o(c|x) > δ Safety Margin

Use the 4 Spec layers as dynamic belief control:
Set priors strong enough to resist corruption (MUST)
Tune evidence weighting for gradual updates (SHOULD)
Manage information flow to prevent phase transitions (CONTEXT)
Orient concept direction to maintain goal alignment (INTENT)
The Belief Dynamics paper validates that this is exactly how models work internally.

## Notes

### A note on architecture boundaries

Tools, MCPs, and resource documents — reside in the Skills folder, not in the Specification. This is not a subtle distinction. In the curriculum's foundation Specifications are Laws: persistent, authoritative, and deliberately minimal. Skills are Hands: reusable, composable, and designed to act. Prompts are Triggers: ephemeral, context-specific, and disposable.

Tools, MCPs, and Skills exert their belief-stabilizing influence from outside the Spec- and that is precisely what makes them effective. They are active in the system without adding noise to the document that anchors the prior. A Specification that tries to do everything becomes a document that anchors nothing. The Supremacy Clause holds its authority in part because the Spec is not cluttered with operational machinery.

The practical rule is this: *if it persists across sessions and governs everything, it belongs in the Spec.* If it acts, retrieves, or executes, it belongs in Skills. If it fires once and disappears, it belongs in a Prompt. Keeping these boundaries intact is not organizational housekeeping- *it is belief architecture.*

A Tool written in the voice of the persona reinforces concept direction every time it is considered. A compliance document in the Spec folder anchors regulatory priors. A well-scoped MCP provides fresh concept-consistent evidence on demand. Each does its job cleanly because it lives in the right place.

## A note on mechanism design

No single mechanism works in isolation. Tools anchor the prior, Skills shape evidence quality, and MCPs provide dynamic concept reinforcement- but they need to be designed as a coordinated system. The value of mapping these to Specification layers is that failures become diagnosable rather than mysterious. A system with strong tool descriptions but a poorly scoped MCP is holding b high while letting concept direction drift. Knowing which layer is responsible for which function tells you where to look.

**Tools operate at two layers: MUST and INTENT.**
At the **MUST** layer, a tool's description functions as a repeated prior injection. Because the model processes the description every time it considers invoking the tool, a well-written tool description continuously reinforces the target concept c throughout the session- without requiring the orchestrator to restate its instructions. This keeps the prior contribution to log-odds elevated even as context grows.

At the **INTENT** layer, the effect deepens when the tool description is written in the tone, voice, and reasoning style of the desired persona. When this is done well, every pass through the tool description is not just a prior injection but a concept direction signal- the model is simultaneously reminded that it should maintain the persona and shown what that persona sounds like in practice. This is one of the more powerful and underused techniques in tool design. A dedicated section of this curriculum covers how to write strong tool descriptions with examples; the principle to carry forward here is that tone and style are not cosmetic choices- *they are belief architecture.*

**Skills operate at two layers: SHOULD and CONTEXT.**
At the **SHOULD** layer, a well- crafted skill document shapes how efficiently evidence accumulates. High-quality, coherent, concept-consistent skill content keeps the effective likelihood weight high- meaning each token carries stronger evidential signal toward the target concept. A noisy or poorly written skill has the opposite effect: evidence accumulates but it is scattered, and the model may drift rather than converge.

At the **CONTEXT** layer, skills function as pre-structured evidence packages. Rather than letting evidence accumulate organically through raw conversation, a skill provides a condensed, organized block of concept-consistent information. This means the model reaches a stable belief state more efficiently, with less exposure to the kind of gradual evidence drift that can push a long-running system toward an unintended phase transition.

**MCPs operate at two layers: MUST and INTENT.**
At the **MUST** layer, an MCP that enforces hard constraints on allowed operations functions as architectural prior enforcement rather than persuasive prior enforcement. Because it restricts action classes structurally, it does not depend on the model's belief state at all- making it more robust than any written instruction under high evidence load.

At the **INTENT** layer, an MCP that retrieves targeted, domain-consistent, concept-aligned content serves as dynamic concept reinforcement. In long-running systems, persona decay occurs when accumulated context gradually rotates the model's concept direction away from c. Fresh, high-quality, goal-aligned retrieval continuously re-anchors that direction- functioning as a counterforce to drift that strengthens rather than weakens as the session progresses.

### Source

BELIEF DYNAMICS REVEAL THE DUAL NATURE OF IN-CONTEXT LEARNING AND ACTIVATION STEERING

(Biglow, E et al., Nov 2025, Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering)

END OF SPECIFICATIONS- APPENDIX F 

version 1.0.0

2026-02-28

Key Principle: Dynamics Model to create a practical Belief Dynamics Control System Framework


