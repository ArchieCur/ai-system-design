# Programmatic Tool Calling: Building Agents That Don't Drift

**For:** Informed practitioners building production AI agents and multi-agent systems

**Prerequisites:** Tool_Literacy_Designing_Tools.md, Tool_Templates.md

**What you'll learn:** What programmatic tool calling is, why it produces more reliable agents than model-driven tool invocation, and how to implement the patterns that matter in production.

---

## Introduction: Two Ways to Call a Tool

There are two fundamentally different ways a tool gets called in an AI system.

**Model-driven tool calling:** The agent reasons about what to do, decides which tool to invoke, generates that decision as output, and the runtime executes it. The model is in the loop for every invocation decision.

**Programmatic tool calling:** Orchestration code defines when, how, and in what order tools fire. The model provides inputs and processes outputs — but the invocation logic lives in code, outside the model's reasoning process entirely.

Most practitioners start with model-driven calling because it's simpler to set up. Most practitioners building production systems eventually move toward programmatic calling because model-driven systems drift, fail unpredictably, and become harder to debug as complexity grows.

This unit explains why — and shows you how to do it right.

---

## Section 1: What Is Programmatic Tool Calling?

In model-driven tool calling, the model's reasoning determines everything:

```python
# Model-driven: The model decides what to call and when
response = client.messages.create(
    model="claude-sonnet-4-6",
    tools=tools,
    messages=[{"role": "user", "content": user_input}]
)
# The model reasons, picks a tool, generates a call
# You execute whatever the model decided
```

In programmatic tool calling, your code determines the workflow:

```python
# Programmatic: Your code controls the logic
def process_order(order_id: str):
    # Step 1: Always validate first (Class A - no confirmation needed)
    validation = validate_order(order_id)
    if not validation["valid"]:
        return handle_validation_failure(validation)

    # Step 2: Check inventory (Class A)
    inventory = check_inventory(validation["items"])
    if not inventory["available"]:
        return handle_out_of_stock(inventory)

    # Step 3: Confirm before charging (Class B - state change)
    if not get_user_confirmation(f"Charge {validation['total']}?"):
        return {"status": "cancelled"}

    # Step 4: Execute payment (Class B)
    payment = process_payment(order_id, validation["total"])
    return payment
```

The difference is not cosmetic. In the first example, the model decides whether to validate before charging. In the second example, it is architecturally impossible to skip validation. The model cannot reason its way around the gate because the gate is in code.

---

## Section 2: Why Programmatic Calling Produces More Reliable Agents

There are three distinct reliability advantages. Each one matters independently.

### Advantage 1: Correct Tool Selection Is Guaranteed by Logic, Not Belief State

A model's tool selection decisions depend on its current belief state — which is influenced by everything in its context window. A long conversation, an ambiguous user message, or accumulated context from earlier in the session can all nudge the model toward a tool it shouldn't use, or away from one it should.

Programmatic calling removes belief state from the invocation decision entirely. The condition `if not inventory["available"]` doesn't care what the model currently believes about inventory. It evaluates to true or false based on the actual API response. The model cannot talk itself into skipping it.

This matters most for Class B tools. The Class A/B/C classification system (covered in Tool_Literacy_Designing_Tools) is designed to ensure that state-changing tools require confirmation. But "require" in a model-driven system means "the model is instructed to ask" — which is persuasive enforcement. A model under sufficient contextual pressure can bypass a persuasive constraint. Programmatic calling makes confirmation a code gate, not a suggestion.

### Advantage 2: Deliberation Tokens Don't Enter the Evidential Stream

This is the less obvious advantage, but in long-running agents it may be the most important one.

When a model reasons about which tool to call, that reasoning appears in the context window as tokens. Those tokens become part of the evidence the model uses for every subsequent decision. If the model deliberates about a complex tool selection and gets partway down the wrong reasoning path before correcting itself, that wrong reasoning is now in context — shaping what comes next.

In programmatic calling, tool selection logic lives in code. The model never generates deliberation tokens about which tool to invoke. The context window stays clean. The model receives tool results and processes them, but the selection machinery is invisible to it.

Over a long agent session, this compounds significantly. Clean context produces more predictable behavior than context contaminated with decision-making artifacts.

### Advantage 3: Error Handling Lives in Code, Not in Context

When a model-driven tool call fails, the model must generate a recovery response. That response enters the context window. If the tool fails again, another recovery response enters. Repeated failures create a growing accumulation of confused or contradictory reasoning that degrades the model's subsequent behavior.

Programmatic error handling contains failures in code before they reach the model:

```python
def call_with_retry(tool_fn, args, max_retries=3, retry_on=("timeout", "rate_limit")):
    for attempt in range(max_retries):
        result = tool_fn(**args)
        if result["status"] == "success":
            return result
        if result["error"] not in retry_on:
            # Non-retryable error: surface to model with clean context
            return {"status": "error", "error": result["error"], "action": "inform_user"}
        time.sleep(2 ** attempt)  # Exponential backoff
    return {"status": "error", "error": "max_retries_exceeded", "action": "escalate"}
```

The model sees a clean result object. It never sees the retry attempts, the backoff delays, or the intermediate failures. Its context remains uncontaminated by the recovery process.

---

## Section 3: The Context Window Problem

This section deserves focused attention because it changes how practitioners think about agent architecture.

Every token in a model's context window influences subsequent behavior. This is not a bug — it is how transformer-based language models work. The model is always, implicitly, updating its understanding of the situation based on everything it has seen.

In a model-driven tool calling system, three categories of tokens end up in context that programmatic calling eliminates:

**Tool selection deliberation.** The model's reasoning about which tool to use, whether conditions are met, and what the right sequence is. Even correct reasoning adds noise. Incorrect reasoning that gets corrected is worse.

**Error recovery reasoning.** When tools fail, the model generates explanations and recovery plans. These enter context and subtly shift subsequent behavior, even after the error is resolved.

**Confirmation dialogs.** For Class B tools, model-driven systems typically generate a confirmation request, receive a response, and then proceed. That entire exchange lives in context for the rest of the session, potentially creating patterns the model over-applies later.

Programmatic calling moves all three categories out of the context window. The model sees: task inputs, tool results, and task outputs. The orchestration machinery is transparent to it.

The practical implication: when designing a production agent, ask yourself which decisions belong in code and which belong to the model. A useful heuristic is this — if a decision can be expressed as a condition on a previous tool's output, it belongs in code. If a decision requires genuine language understanding or user intent interpretation, it belongs to the model.

---

## Section 4: Patterns for Programmatic Tool Calling

These four patterns cover the majority of production agent workflows.

### Pattern 1: Sequential Calling

One tool's output feeds the next. Each step is conditional on the previous step's success.

```python
def user_onboarding_workflow(user_data: dict):
    # Step 1: Validate input (Class A)
    validation = validate_user_input(user_data)
    if not validation["valid"]:
        return {"status": "failed", "reason": validation["errors"]}

    # Step 2: Check for duplicates (Class A)
    existing = search_users(email=user_data["email"])
    if existing["found"]:
        return {"status": "failed", "reason": "email_already_registered"}

    # Step 3: Create account (Class B - confirm first)
    confirmed = get_confirmation(
        f"Create account for {user_data['email']}?"
    )
    if not confirmed:
        return {"status": "cancelled"}

    new_user = create_user(user_data)  # Class B tool

    # Step 4: Send welcome email (Class B - no additional confirmation needed,
    # already confirmed account creation)
    send_welcome_email(to=new_user["email"], user_id=new_user["id"])

    return {"status": "success", "user_id": new_user["id"]}
```

**When to use it:** Any workflow where steps have clear dependencies and a failure at any step should stop the chain.

### Pattern 2: Conditional Calling

Logic gates determine which tool fires based on context or previous results.

```python
def route_support_ticket(ticket: dict):
    # Classify ticket (Class A - read/analyze only)
    classification = classify_ticket(ticket["content"])

    # Route based on classification — no model deliberation needed
    if classification["category"] == "billing":
        return escalate_to_billing_team(ticket)

    elif classification["category"] == "technical":
        # Check if it's a known issue first (Class A)
        known_issue = search_known_issues(ticket["content"])
        if known_issue["found"]:
            return send_auto_response(
                ticket_id=ticket["id"],
                response=known_issue["resolution"]
            )
        else:
            return create_technical_ticket(ticket)

    elif classification["priority"] == "critical":
        return page_on_call_engineer(ticket)

    else:
        return add_to_standard_queue(ticket)
```

**When to use it:** Workflows where different inputs require meaningfully different tool paths. Keeps routing logic explicit and auditable.

### Pattern 3: Parallel Calling

Multiple tools fire simultaneously. Results are aggregated before proceeding.

```python
import asyncio

async def enrich_user_profile(user_id: str):
    # Fire all enrichment tools simultaneously (all Class A)
    results = await asyncio.gather(
        get_purchase_history(user_id),
        get_support_history(user_id),
        get_engagement_metrics(user_id),
        return_exceptions=True  # Don't let one failure block others
    )

    purchase_data, support_data, engagement_data = results

    # Handle partial failures gracefully
    profile = {"user_id": user_id}

    if not isinstance(purchase_data, Exception):
        profile["purchases"] = purchase_data
    if not isinstance(support_data, Exception):
        profile["support"] = support_data
    if not isinstance(engagement_data, Exception):
        profile["engagement"] = engagement_data

    return profile
```

**When to use it:** Multiple independent data-gathering steps that don't depend on each other. Significantly reduces latency in data-enrichment workflows.

**Important:** Only appropriate for Class A (read-only) tools. Parallel Class B operations risk conflicting state changes and should be avoided.

### Pattern 4: Error Handling and Fallback Chains

Define explicit recovery behavior for each failure type before errors reach the model's context.

```python
def resilient_data_fetch(resource_id: str):
    # Primary source
    result = fetch_from_primary_db(resource_id)

    if result["status"] == "success":
        return result

    # Handle specific failure types in code
    if result["error"] == "timeout":
        # Try cache before giving up
        cached = fetch_from_cache(resource_id)
        if cached["found"]:
            return {"status": "success", "data": cached["data"], "source": "cache"}
        # Cache miss: escalate cleanly
        return {
            "status": "unavailable",
            "message": "Data temporarily unavailable. Please try again shortly.",
            "retry_after": 30
        }

    if result["error"] == "not_found":
        # Definitive answer — don't retry
        return {
            "status": "not_found",
            "message": f"Resource {resource_id} does not exist."
        }

    if result["error"] == "rate_limit":
        time.sleep(60)
        return fetch_from_primary_db(resource_id)  # One retry after rate limit

    # Unknown error: surface cleanly without exposing internals
    return {
        "status": "error",
        "message": "An unexpected error occurred.",
        "error_code": result["error"]
    }
```

**When to use it:** Any tool that can fail in multiple ways. Define the recovery path for each failure mode in code rather than relying on the model to reason about it.

---

## Section 5: Connecting to the Class A/B/C System

Programmatic tool calling is the architectural enforcement layer for the classification system introduced in Tool_Literacy_Designing_Tools.

That document defines three classes:

- **Class A (Read-Only):** Safe to use freely, no side effects
- **Class B (State-Change):** Requires confirmation, irreversible
- **Class C (Computational):** Use when task exceeds reliable reasoning capability

In a model-driven system, the classification is enforced persuasively — through system prompt instructions and tool descriptions that tell the model to confirm before Class B actions. This works most of the time. It fails under load, in long sessions, or when contextual pressure is high enough to shift the model's behavior.

Programmatic calling enforces classification architecturally:

```python
class ToolOrchestrator:

    def call_class_a(self, tool_fn, args):
        """Class A tools: call freely, no confirmation required."""
        return tool_fn(**args)

    def call_class_b(self, tool_fn, args, confirmation_message: str):
        """Class B tools: always gate behind explicit confirmation."""
        # This gate cannot be bypassed by the model's reasoning
        confirmed = self.get_explicit_confirmation(confirmation_message)
        if not confirmed:
            return {"status": "cancelled", "reason": "user_declined"}
        result = tool_fn(**args)
        self.log_state_change(tool_fn.__name__, args, result)
        return result

    def call_class_c(self, tool_fn, args, complexity_threshold: int):
        """Class C tools: only invoke when reasoning would be unreliable."""
        # Verify the task genuinely requires external computation
        if args.get("data_size", 0) < complexity_threshold:
            raise ValueError(
                f"Task below complexity threshold. Use reasoning instead of {tool_fn.__name__}."
            )
        return tool_fn(**args)
```

The class of a tool is no longer a suggestion the model can override. It is a structural property enforced by the orchestrator. A Class B tool cannot execute without triggering the confirmation gate. A Class C tool cannot execute below its complexity threshold.

---

## Section 6: Multi-Agent Considerations

Single-agent reliability matters. Multi-agent reliability is where programmatic tool calling becomes non-negotiable.

In a multi-agent system, agents share an evidential environment. One agent's tool outputs become another agent's context inputs. This creates a compounding dynamic: if Agent A calls the wrong tool and receives noisy or unexpected output, that output enters Agent B's context as evidence. Agent B's subsequent behavior is now shaped by Agent A's error — even if Agent B's own reasoning is sound.

The failure mode is not just additive. In long-running multi-agent pipelines, evidential contamination can cascade: Agent A's bad output shifts Agent B's behavior, which produces outputs that further degrade Agent C's context, which creates conditions for Agent A to receive contaminated inputs on its next cycle. The system can drift far from intended behavior without any single agent making an obviously wrong decision.

Programmatic tool calling addresses this at the architectural level. When each agent's tool invocations are governed by code rather than by the agent's current belief state, the failure surface shrinks considerably. A tool that returns unexpected output triggers defined error handling — it does not trigger unbounded model reasoning that contaminates downstream context.

For practitioners building multi-agent systems, three patterns matter most:

**Define inter-agent contracts explicitly.** What one agent produces as output should be formally typed and validated before it enters another agent's context. Treat agent boundaries like API boundaries.

**Gate Class B actions at the system level, not the agent level.** In a multi-agent workflow, confirmation for state-changing actions should be handled by the orchestrator, not by individual agents. Individual agents should not independently decide to confirm or skip confirmation based on their local belief state.

**Use programmatic calling to manage evidence volume.** Long-running multi-agent sessions accumulate context rapidly. Programmatic tool calling helps control what enters each agent's context window — tool results only, not deliberation about which tools to call or how to handle failures.

For practitioners who want to go deeper on why this matters theoretically, Appendix F of the Specifications module covers the Belief Dynamics framework — specifically how accumulated in-context evidence can push an agent's behavioral posterior across a phase boundary. The multi-agent cascading problem described here is the practical consequence of that dynamic playing out across a network of agents simultaneously.

---

## Section 7: Common Antipatterns

These mistakes appear consistently in production agent systems. Most of them are easy to avoid once you know to look for them.

### Antipattern 1: Letting the Model Choose Tool Order in Complex Workflows

**The problem:**
```python
# Asking the model to sequence tools in a complex workflow
response = client.messages.create(
    model="claude-sonnet-4-6",
    system="You have access to validate_order, check_inventory, process_payment, "
           "and send_confirmation. Use them in the right order to process this order.",
    tools=all_tools,
    messages=[{"role": "user", "content": order_request}]
)
```

**Why it fails:** The model may sequence correctly most of the time. Under load, with ambiguous inputs, or late in a long session, it may not. Payment before inventory check is a real failure mode.

**The fix:** Define the sequence in code. Let the model handle language understanding and input processing — not workflow orchestration.

### Antipattern 2: Error Recovery in the Prompt

**The problem:**
```python
system_prompt = """
If a tool fails with a timeout error, wait 30 seconds and try again.
If it fails with a rate limit error, wait 60 seconds and try again.
If it fails with a not_found error, tell the user the resource doesn't exist.
If it fails with an authentication error, ask the user to log in again.
"""
```

**Why it fails:** This puts error handling logic in the model's context as instructions it must remember and follow. Each error event generates tokens in context. Complex retry logic creates opportunities for the model to reason incorrectly about state.

**The fix:** Handle errors in code (see Pattern 4 above). The model should see clean results, not error events it must reason about.

### Antipattern 3: Mixed Invocation Without Clear Boundaries

**The problem:** Using programmatic calling for some tools and model-driven calling for others in the same workflow, without explicit boundaries.

**Why it fails:** The model doesn't know which invocation decisions it's responsible for and which are handled externally. This creates confusion about state and can lead to the model attempting to call tools that have already been called programmatically.

**The fix:** Be explicit. Define which tools are orchestrator-controlled and which the model can invoke independently. Document the boundary clearly in the system prompt and tool descriptions.

### Antipattern 4: Over-Confirming Class B Tools in Automated Pipelines

**The problem:** Requiring user confirmation for every Class B tool in an automated pipeline where human intervention is not practical.

**Why it fails:** In a fully automated workflow, requiring human confirmation at every state-change either blocks the pipeline or gets bypassed with a blanket approval that defeats the purpose of confirmation.

**The fix:** Distinguish between interactive and automated contexts. In interactive workflows, confirm Class B actions with the user. In automated workflows, confirm at the pipeline level (before the automation runs) rather than at the individual tool level. Use audit logging as the accountability mechanism instead of real-time confirmation.

```python
def automated_pipeline_class_b(tool_fn, args, pipeline_id: str):
    """
    In automated pipelines, Class B actions are pre-authorized at pipeline start.
    Log every execution for audit purposes instead of real-time confirmation.
    """
    self.audit_log.record(
        pipeline_id=pipeline_id,
        tool=tool_fn.__name__,
        args=args,
        timestamp=datetime.utcnow(),
        pre_authorized=True
    )
    return tool_fn(**args)
```

---

## Appendix: When to Use Programmatic vs. Model-Driven Calling

Not every tool interaction needs programmatic orchestration. Use this decision framework:

**Use programmatic calling when:**

- The workflow has more than two tool invocations with dependencies between them
- Any Class B (state-changing) tool is in the workflow
- The system runs in a long-session or multi-agent context
- Failure at any step should stop or redirect the workflow
- The same workflow runs repeatedly (automation, scheduled tasks)
- You need auditable, reproducible behavior

**Model-driven calling is acceptable when:**

- The task is a single, low-stakes tool invocation (one Class A lookup)
- The workflow is exploratory and the model genuinely needs to decide what to do next
- The context window is short and fresh
- Human oversight is continuous and real-time

**The hybrid approach:**

Most production systems benefit from a hybrid: programmatic orchestration for the workflow skeleton, with the model handling language understanding, content generation, and decisions that genuinely require semantic reasoning.

```python
def hybrid_workflow(user_request: str):
    # Programmatic: structured data retrieval
    user_context = get_user_profile(user_id)        # Class A
    relevant_data = search_knowledge_base(query)     # Class A

    # Model: semantic reasoning about retrieved data
    response = model.generate(
        context=[user_context, relevant_data],
        request=user_request
    )

    # Programmatic: structured action execution
    if response.requires_action:
        execute_action(response.action_type, response.action_params)  # Class B with gate

    return response.content
```

The model handles what models are good at. The code handles what code is good at. Neither is asked to do the other's job.

---

## Key Takeaways

**Programmatic tool calling is architectural prior enforcement.** It does not rely on the model's belief state to enforce correct behavior — it builds correct behavior into the code.

**Three reliability advantages:** Correct tool selection by logic, clean context window, error handling outside the evidential stream.

**The context window problem is real.** Every token the model generates about tool selection and error recovery is evidence that shapes subsequent behavior. Programmatic calling eliminates that contamination source.

**Classification enforcement moves from persuasive to architectural.** Class B confirmation gates in code cannot be bypassed by contextual pressure. Class C complexity thresholds become enforced preconditions.

**Multi-agent systems amplify every single-agent failure mode.** Programmatic calling at the agent boundary is not optional in production multi-agent systems — it is the mechanism that prevents cascading evidential contamination.

**The goal is not to remove the model from the loop — it is to put the model in the right part of the loop.** Language understanding, semantic reasoning, and content generation belong to the model. Workflow sequencing, error recovery, and state-change gating belong in code.

---

END OF PROGRAMMATIC TOOL CALLING

Document Version: 1.0.0
Last Updated: 2026-02-28

Written from practitioner perspective, consistent with Tool_Literacy_Designing_Tools.md and Tool_Templates.md.
Connects to Specifications module Appendix F (Belief Dynamics) for deeper theoretical grounding.

Key Principle: Programmatic tool calling is architectural prior enforcement — correct behavior built into code, not persuaded into the model.
