# Tools

## Overview

Tools are the **Achilles heel** of AI systems. Poorly designed tools—vague descriptions, unclear usage conditions, unpredictable failures-create massive cognitive friction and lead to unreliable behavior, especially in agentic workflows.

This section provides a complete engineering framework for tool design, not just "better descriptions." You'll learn the **Three-Part Tool Definition Standard** (Trigger Logic, Negative Constraints, Return Contract), **Risk Classification** (Read-Only, State-Change, Computational), and systematic approaches to testing, composition, and error handling.

Mastering tools transforms them from a source of confusion into a source of reliability.

---

## What You'll Learn

**[Tool Literacy: Designing Tools](Tool_Literacy_Designing_Tools.md)**  
The complete framework for engineering tools models can actually use reliably:

- **Three-Part Tool Definition Standard**
  - Trigger Logic (when to use this tool)
  - Negative Constraints (what NOT to do)
  - Return Contract (success states + failure modes with recovery actions)

- **Tool Classification System**
  - Class A: Read-Only (low risk, use freely)
  - Class B: State-Change (high risk, requires confirmation)
  - Class C: Computational (when reliability requires it)

- **Decision Trees** - When to use reasoning vs. tools
- **Standard Library Pattern** - Why fewer tools win
- **Testing Framework** - Validating tool comprehension
- **Common Antipatterns** - Mistakes to avoid

**[Tool Templates](Tool_Templates.md)**  
Ready-to-use templates implementing the three-part standard for common tool patterns.

**[Programmatic Tool Calling](Programmatic_Tool_Calling.md)**  
How to move from model-driven tool invocation to code-controlled orchestration for production-grade reliability:

- **Why Programmatic Calling Wins** - Three reliability advantages over model-driven invocation
- **The Context Window Problem** - Why model deliberation tokens contaminate the evidential stream
- **Four Orchestration Patterns**
  - Sequential calling (dependent steps)
  - Conditional calling (logic-gated routing)
  - Parallel calling (independent data gathering)
  - Error handling and fallback chains
- **Architectural Classification Enforcement** - Moving Class A/B/C from persuasive to structural
- **Multi-Agent Considerations** - Preventing cascading evidential contamination
- **Common Antipatterns** - Mistakes that cause drift and production failures

---

## Why Tools Are Critical

Tools multiply cognitive friction when poorly designed:

- **Vague descriptions** → Models guess wrong
- **No trigger logic** → Models use tools at wrong times
- **Missing failure modes** → Models hallucinate error recovery
- **Tool overload** → Decision paralysis
- **Unclear risk classification** → State-change accidents

**The cost:** Wasted context, unreliable behavior, agent confusion, production failures.

**Well-engineered tools eliminate guessing** by explicitly defining:

- When to use them (and when not to)
- What NOT to do (common mistakes, safety constraints)
- What to expect (success + every failure mode + recovery actions)

---

## The Three-Part Tool Definition Standard

Every tool should define:

### 1. Trigger Logic (When to Use This)

Explicit scenarios for when the model should (and shouldn't) use this tool.

**Example:**

use_when:

- User asks about a specific person's information
- Need to verify user exists before action

dont_use_when:

- Asking about multiple users (use search_users)
- General questions (explain from knowledge)

```text

### 2. Negative Constraints (What NOT to Do)
Common mistakes and safety rules.

**Example:**
```text
do_not:

- Execute queries on null input (validate first)
- Assume column names not in schema

safety:

- Never return password fields
- Limit results to 100 rows maximum

```

### 3. Return Contract (What to Expect)

Success schema + every failure mode with recovery actions.

**Example:**

```text

failure_modes:
  rate_limit:
    error: "Rate limit exceeded"
    recovery_action: "Wait 60 seconds, retry automatically"
    user_action: "Email will be sent in 60 seconds"
```

**This eliminates guessing.** The model knows exactly what to do for each failure—no loops, no hallucination.

---

## Tool Risk Classification

Every tool must be classified by risk:

**Class A: Read-Only (Low Risk)**  
No side effects, safe to retry, safe to use speculatively  
*Examples: get_user, search_documents, calculate_statistics*

**Class B: State-Change (High Risk)**  
Irreversible, has side effects, requires confirmation  
*Examples: delete_file, send_email, update_database*  
**Rule:** ALWAYS confirm with user before execution

**Class C: Computational (When Reliability Requires It)**  
Tasks where accumulated steps, scale, or precision requirements make in-context reasoning unreliable 

*Examples: 360-month mortgage calculations, large dataset analysis*
**NOT:** "tasks Claude finds hard" but "tasks where error accumulates faster than reasoning can correct"

## Beyond Basic Descriptions

This isn't about writing prettier tool descriptions. It's about:

- **Engineering for reliability** - Systematic error handling
- **Risk management** - Explicit classification and guardrails
- **Cognitive load reduction** - Decision trees, standard libraries
- **Testing discipline** - Validating tool comprehension
- **Production readiness** - Real failure modes, real recovery actions

---

## Getting Started

### New to Tool Design?

**Start here:**  
[Tool Literacy: Designing Tools](Tool_Literacy_Designing_Tools.md)

Work through:

1. Three-Part Tool Definition Standard
2. Tool Classification System
3. Decision Trees (reasoning vs. tools)
4. Standard Library Pattern
5. Testing Framework
6. Common Antipatterns

### Need Templates?

Jump to [Tool Templates](Tool_Templates.md) for ready-to-use patterns implementing the three-part standard.

### Building Production Systems?

Pay special attention to:

- **Return Contracts** (failure modes + recovery actions)
- **Risk Classification** (especially Class B confirmation patterns)
- **Testing Framework** (validate tool comprehension before deployment)
- **Programmatic Tool Calling** (architectural enforcement for multi-agent and long-running systems)

---

## Key Principle

**Tools are the Achilles heel of AI systems—but only when poorly engineered.**

Well-designed tools with explicit trigger logic, negative constraints, and return contracts transform uncertainty into reliability. In production systems and multi-agent architectures, programmatic orchestration elevates that reliability from persuasive to architectural.

---

*Ready to begin? Start with [Tool Literacy: Designing Tools](Tool_Literacy_Designing_Tools.md) →*
