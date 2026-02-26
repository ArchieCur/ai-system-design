# Section 1: Foundation - What Are Specifications?

**For:** All users designing AI systems

**Prerequisites:** Understanding of Prompts and Skills (Modules 1-2)

**What you'll learn:** What Specifications are, why AI needs them, and how they differ from traditional software requirements.

## Introduction

You've learned about Prompts (the Trigger) and Skills (the Hands). Now we explore the third pillar: Specifications (the Laws).

### The complete system

- Prompts = Ephemeral intent ("Build me a login page")
- Skills = Reusable procedures ("How to write secure code")
- Specifications = Persistent constraints ("Use PostgreSQL, never hardcode passwords")
Together, these three elements enable reliable AI system design.

This section introduces Specifications from a fundamental perspective: what they are, why they matter, and how they work differently for AI than for traditional software.

## What Are Specifications?

**The Simple Definition**
A Specification (spec.md) is a document that defines the persistent, project-level constraints and context that govern how an AI system should behave. Specs are static documents, read by the model during task execution as governing rules that must be clear without clarification.

### In practice

**SPEC.md contains:**

- What the system MUST do
- What the system SHOULD do
- What context informs decisions
- Why these constraints exist

### Notes on Organization-Spec Folders

For complex projects, specifications can be organized into folders to separate concerns:

```text

/project-specs/

├── SPEC.md (main specification)
├── policies/ (security, data retention policies)
├── regulations/ (GDPR, SOC2, PCI-DSS compliance)
└── context/ (brand guidelines, business priorities)
```

SPEC.md references these documents rather than duplicating content, keeping the main specification focused while providing access to detailed policies and regulations.

Unlike Skills folders (which contain detailed procedures), Spec folders contain reference documents that inform constraints and context.

See Appendix E FolderStructures for complete guidance on organizing specifications with folders.

## The Problem Specifications Solve

**From the model's perspective:**

### *Without Specifications:*

User: "Build a user authentication system"

The model: "Okay! I'll need to make decisions about:

- Which database? (PostgreSQL? MySQL? MongoDB?)
- Password hashing? (bcrypt? argon2? pbkdf2? What salt rounds?)
- Token type? (JWT? Session? OAuth?)
- Token storage? (localStorage? cookies? Which type?)
- Session duration? (15 minutes? 1 hour? 1 day?)
- Password requirements? (8 chars? 12? Complexity rules?)

The model: I'll just... invent reasonable defaults and hope they match the needs.
Result: 

- Model invents policy. 
- Might not match your requirements. 
- Might violate your security standards. 
- Might be inconsistent across projects.

### *With Specifications:*

SPEC.md says:

`<constraint priority="critical">`

- MUST: PostgreSQL 14+ database
- MUST: Bcrypt password hashing (salt rounds=12)
- MUST: JWT tokens (HS256 algorithm)
- MUST: Tokens stored in httpOnly cookies
- MUST: Access token expiry: 15 minutes
- MUST: Password minimum: 12 characters, must include uppercase, lowercase, number, special char

`</constraint>`

**User:** "Build a user authentication system"

**Model:** "Perfect! The spec tells me:

- Database: PostgreSQL ✓
- Hashing: Bcrypt with 12 salt rounds ✓
- Tokens: JWT with HS256 ✓
- Storage: httpOnly cookies ✓
- Expiry: 15 minutes ✓
- Password rules: Clear requirements ✓

**Model:** I'll implement exactly according to spec. No guessing needed.

**Result:** Consistent, compliant, matches your requirements.

## The Key Insight

Specs are most usable by models when they eliminate the need for the model to invent policy. This is the fundamental purpose of Specifications.

**Models are:**

- Excellent at following clear constraints
- Good at applying context to decisions
- Capable of planning within boundaries

**But:**

- Should not invent security policies
- Should not guess architectural decisions
- Should not assume business requirements
- Specifications provide the boundaries. Models plan and execute within them.

## The Paradigm Shift: Compiler Thinking → Partner Thinking

### **Traditional Software: Writing for Compilers**

In traditional software engineering:

- Requirements → Code → Compiler → Binary Output
- The compiler:
- Enforces syntax rules (binary: works or doesn't)
- Has no understanding of intent
- Cannot clarify ambiguity
- Cannot negotiate requirements
- Returns errors or success (nothing in between)

Requirements are written for something that:

- Can't ask questions
- Can't explain its reasoning
- Can't suggest alternatives
- Just does exactly what you specify (or fails)

## AI Systems: Writing for Partners

### With AI systems

**Specifications → AI → Dialog → Collaborative Output**

**The AI:**

- Can understand intent
- Can ask clarifying questions
- Can suggest alternatives
- Can explain reasoning
- Can negotiate within boundaries

**Specifications are written for something that:**

- Can plan complex solutions
- Can adapt to context
- Can identify conflicts
- Can engage in dialog
This changes everything about how we write specifications.

### What This Means in Practice

*Traditional Requirements (Compiler Thinking):*

**REQUIREMENT:** The system shall hash passwords using bcrypt
with a cost factor of 12.

**IMPLEMENTATION:** 

- If (bcrypt && cost_factor == 12)
- { compile_success() }
- else { compilation_error() }
- Binary outcome. 
- No dialog.

**AI Specifications (Partner Thinking):**

`<constraint priority="critical">`

MUST: Password hashing uses bcrypt with salt rounds=12

`<rationale>`

Security requirement: OWASP recommends 12+ rounds for 2026.
Lower rounds = insufficient protection against brute force.
Higher rounds = unnecessary performance cost at our scale.

`</rationale>`

`</constraint>`

**Model reads this and:**

- Understands the constraint (bcrypt, 12 rounds)
- Understands the why (security vs. performance balance)
- Can ask: "What if user requests 10 rounds for performance?"
- Can challenge: "Spec requires 12 rounds, but you asked for 10. Override?"
- Can suggest: "If performance is critical, we could optimize other areas instead"
- 
  **Dialog-enabled outcome. Collaborative.**

### The Implications

This paradigm shift means specifications for AI must:

1. Be clear but not rigid (room for planning)
2. Explain the why (enables intelligent application)
3. Support dialog (negotiable vs. absolute constraints)
4. Enable verification (models can self-check)
5. Handle ambiguity (provide context for edge cases)

This is different from traditional requirements engineering.

## The Layered Model: MUST/SHOULD/CONTEXT/INTENT

*From a model’s perspective:*

Specifications work best when they're structured in clear layers, each serving a different purpose in how a model processes and apply constraints.

### **Layer 1: MUST (Non-Negotiable Constraints)**

**Purpose:** Boundaries a model cannot cross
**What goes here:**

- Security requirements
- Legal compliance
- Critical architectural decisions
- Data integrity rules

**Characteristics:**

- Binary (yes/no compliance)
- Verifiable (can be checked)
- Non-negotiable (no exceptions without explicit override)

### MUST Example

```text

<constraint priority="critical">
MUST: All PII encrypted at rest (AES-256)
MUST: HTTPS only (no HTTP in production)
MUST: No API keys in version control
MUST: Database backups every 24 hours
</constraint>
```

**How a model processes this:**

- These are LAWS I cannot violate
- I verify compliance before delivery
- If user requests conflict, I challenge (may require override password)
- No room for interpretation


### **Layer 2: SHOULD (Soft Constraints / Guidelines)**

**Purpose:** Preferred approaches with room for judgment

**What goes here:**

- Code style preferences
- Best practices
- Performance guidelines
- Organizational conventions

**Characteristics:**

- Preferred but not absolute
- Can be violated with good rationale
- Subject to dialog and negotiation

### SHOULD Example

```text

<guideline priority="high">

- SHOULD: Keep functions under 50 lines
- SHOULD: Use functional components (prefer hooks over classes)
- SHOULD: Include inline comments for complex logic

WHEN violating:

- Document rationale in code comments
- Consider refactoring if violation becomes pattern
- Acceptable for complex algorithms where splitting hurts readability
  
</guideline>
```
**How a model processes this:**

- These are PREFERENCES I aim to follow
- I can deviate with good reason
- If violating, I explain why in my output
- Dialog opportunity: "I used 75 lines because [reason]. Acceptable?"

### **Layer 3: CONTEXT (Planning Information)**

**Purpose:** Background that helps a model make good decisions

**What goes here:**

- Technical environment details
- User/audience information
- Business priorities
- Decision-making frameworks

**Characteristics:**

- Informative (not prescriptive)
- Helps a model prioritize
- Guides tradeoff decisions

### CONTEXT Example

```text

<context>

**Technical Environment:**

Stack: Next.js 14 + TypeScript + Tailwind
Team: 2 senior devs, 3 junior (optimize for maintainability)
Scale: ~5K users, 50 concurrent peak

**Users:**

Primary: Small business owners (non-technical)
Priority: Reliability > Features > Performance
Frustration: Complex interfaces, unexpected errors

**Decision Framework:**

**When in doubt:**

Simple > Clever (junior devs will maintain this)
Explicit > Implicit (code clarity matters)
Reliable > Fast (stability critical for trust)

</context>
```
**How a model processes this:**

- This INFORMS a model’s planning
- Not constraints, but LENSES for decisions
- Helps a model make intelligent tradeoffs
- Example: "Should I optimize performance? Context says Reliability > Performance, so I'll prioritize error handling over speed."

### **Layer 4: INTENT (The Why)**

**Purpose: Goals and rationale behind constraints**

**What goes here:**

- Business objectives
- User needs being served
- Why specific decisions were made
- Success criteria

**Characteristics:**

- Explanatory (helps a model understand purpose)
- Enables alternative suggestions
- Guides when specs are incomplete

### INTENT Example

```text

<intent>

**Primary Goal:**
Enable small business owners to manage inventory without technical expertise.

**Why This Matters:**

- Users are time-constrained (5-10 minutes max per session)
- Technical failures = lost sales (high business impact)
- Competitors have complex UIs (our simplicity is competitive advantage)

**Success Looks Like:**

- 90% of users complete tasks without documentation
- < 1% error rate on critical operations (add/update inventory)
- Average task completion time < 3 minutes

**Rationale for Key Decisions:**

- Simple over Clever: Users are non-technical, complexity = abandonment
- Reliability over Features: Trust critical for small business adoption
- Explicit errors over silent fails: Users need to know what went wrong
</intent>
```
**How a model processes this:**

- This helps a model UNDERSTAND the goal
- If constraints conflict, intent helps prioritize
- If specs are ambiguous, intent guides interpretation
- Enables a model to suggest alternatives: "Spec says X, but given intent Y, would Z work better?"

## **How the Layers Work Together**

**Real scenario:**

User prompt: "Add a bulk import feature for inventory"
Model references specs:

```text

MUST (Layer 1)

MUST: Validate all input data before database write
MUST: Maximum 1000 records per import (prevent DOS)

-> Model implements validation + 1000 record limit

SHOULD (Layer 2)

SHOULD: Provide progress indicator for operations >2 seconds

-> Model adds progress bar (import likely >2 seconds)

CONTEXT (Layer 3)

Users are non-technical, time-constrained
Priority: Reliability > Features

-> Model adds clear error messages, handle edge cases carefully

INTENT (Layer 4)

Success = 90% task completion without docs
Users need to know what went wrong

-> Model designs clear, actionable error messages → Model adds inline help text
```
**Result:** Import feature that

- Complies with MUST constraints ✓
- Follows SHOULD guidelines ✓
- Aligns with user context ✓
- Achieves intended outcomes ✓

**Without layered specs: Model might build technically correct but unusable feature.**

## Why AI Needs Different Specs Than Software

### The Fundamental Difference

- Compilers
- Process syntax
- Enforce rules
- Return binary outcomes

### AI Models

- Process semantics
- Apply judgment
- Return intelligent solutions

  **This requires different specification approaches.**

### What Works for Compilers (But Not for AI)

1. **Precise Syntax**
   
**Compiler requirement:**

```text

int calculate(int a, int b) {
return a + b;
}
```
**Works:** Exact syntax enforced

**AI specification (if written like compiler requirement)**

The function shall accept two integers and return their sum.
Implementation must use 'int' type for parameters and return value.
Function name must be exactly 'calculate'.
Parameters must be named 'a' and 'b' in that order.

**Problem:** Over-specified. A model should be able to choose sensible names, types based on context.

2. **Binary Constraints**

**Compiler requirement:**

BUILD CONFIGURATION: Release mode, optimization level O2
Works: Binary setting (O2 or fail)

**AI specification (if written like this):**

**MUST:** Use release build configuration

**Problem:** What does "release" mean in this context?

- Production deployment?
- Optimized for performance?
- Debugging symbols removed?

**Better AI specification:**

```text

<constraint>

MUST: Production builds optimized for performance
MUST: No debugging symbols in production binaries
MUST: Environment-specific config (dev/staging/prod)

<rationale>

Performance critical for user experience (context: 5K users, limited resources)
Debug symbols = security risk (exposed internal structure)
Environment configs = different DB/API endpoints per environment

</rationale>

</constraint>

### What Works for AI (But Would Confuse Compilers)

1. **Intent-Based Constraints**

**AI specification:**

```text

<intent>
Primary goal: Minimize user friction during authentication
This means:

Reduce required fields to minimum
Clear error messages (tell user what to fix)
Smooth flow (no unexpected steps)
</intent>

<constraint>
MUST: Email + password only (no additional required fields on registration)
SHOULD: Progressive profiling (collect other data after signup)
</constraint>
```

This works for AI: Model understands the goal (minimize friction) and can make decisions aligned with it.

Would confuse compiler: "Minimize friction" is not a compilable instruction.

2. Contextual Guidelines

AI specification:

```text

context>
Team expertise: Strong in React, limited in Vue
Code reviewers: Prefer explicit over clever
Future maintenance: Code will be maintained by junior devs
</context>

<guideline>
SHOULD: Prioritize code clarity over performance optimization
SHOULD: Include explanatory comments for non-obvious logic
SHOULD: Use established React patterns (avoid experimental features)
</guideline>`
```
This works for AI: Model adjusts it’s code style based on team context.

Would confuse compiler: Compiler doesn't care about maintainability or team expertise.

3. Negotiable Constraints
AI specification:

```text

<guideline>
SHOULD: API responses < 200ms (95th percentile)
EXCEPTION: Complex reports acceptable up to 2 seconds with progress indicator
NEGOTIABLE: If achieving 200ms requires significant architectural changes, discuss alternatives
</guideline>
```
This works for AI: Model can engage in dialog about tradeoffs

Would confuse compiler: Compiler can't negotiate or discuss alternatives.

### The Cognitive Load Difference

From a model’s perspective:

### What Creates Cognitive Load (Makes a Model Struggle)

### Ambiguous constraints

MUST: Use appropriate error handling
("Appropriate" means what? Try-catch? Validation? Logging? All of above?)

### Hidden coupling

MUST: Maintain backward compatibility
(Compatible with what? Which versions? What can change and what can't?)

### Aspirational language

MUST: Be user-friendly and intuitive
(How does the model verify "user-friendly"? What does "intuitive" mean?)

### What Reduces Cognitive Load (Helps a model)

### Specific, verifiable constraints

```text

<constraint>
MUST: All errors return JSON with structure:

{
"error": "error_code",
"message": "Human readable message",

"details": { } // Optional context
}

<verification>
Check: All error responses include "error" and "message" fields
Check: HTTP status code matches error severity (4xx client, 5xx server)
</verification>

</constraint>
```

### Explicit scope

```text

<constraint scope="API-versioning">
MUST: Support API v1 and v2 simultaneously
MUST: No breaking changes to v1 endpoints

Breaking change definition:

- Removing endpoint
- Removing required field
- Changing field type
- Changing field semantics

Non-breaking changes (allowed):

- Adding endpoint
- Adding optional field
- Adding response field
</constraint>
```

### Separated concerns

```text

<constraint>
MUST: PostgreSQL 14+ database
</constraint>

<guideline>
SHOULD: Use connection pooling
</guideline>

<context>
Expected load: 100 queries/second peak
Team expertise: Strong SQL, familiar with pg
</context>

<intent>
Reliability critical (handles financial data)
Performance secondary (acceptable latency: <500ms)
</intent>
```
Each concern in its own layer. No mental separation required.

## The Complete Picture

Specifications in the AI System Design Stack

### The full architecture

 How they interact:

1. User provides prompt (what they want now)
2. AI references specs (what constraints apply)
3. AI activates skills (how to do the work)
4. AI plans solution (within spec boundaries, using skill procedures)
5. AI verifies compliance (checks against spec requirements)
6. AI delivers output (prompt fulfilled, spec compliant, skill-guided)

### AI System Design Stack Example: Building Authentication

**Prompt (Trigger):**
"Add user authentication to the application"
**Spec (Laws):**

```text

<constraint priority="critical">
MUST: PostgreSQL 14+ database
MUST: Bcrypt hashing (salt rounds=12)
MUST: JWT tokens (HS256, 15min expiry)
MUST: httpOnly cookies for token storage
</constraint>

<context>
Users: Small business owners (non-technical)
Priority: Security > UX > Performance
</context>

<intent>
Goal: Secure authentication without user friction
Success: <1% login failures, zero security incidents
</intent>
```

**Skill (Hands):**

-implementing-jwt-authentication.md
-securing-user-credentials.md
-designing-auth-flows.md

### AI Process

1. Reads prompt: "Authentication needed
2. Checks spec: PostgreSQL, bcrypt(12), JWT(HS256), httpOnly cookies
3. Activates skills: JWT implementation, credential security
4. Plans: Login endpoint, registration endpoint, token refresh
5. Implements: Following spec constraints, using skill procedures
6. Verifies: Bcrypt rounds=12? JWT expiry=15min? Cookies httpOnly?
7. Delivers: Auth system (spec-compliant, skill-guided, prompt-fulfilled)

**Without specs** Model would invent database choice, hashing algorithm, token type, storage
method.

**With specs:** Model implements exactly what you need.

## Key Takeaways

### What Specifications Are

Specifications are:

- Persistent, project-level constraints and context
- The "Laws" that govern system behavior
- Structured to reduce model's need to invent policy
- Different from traditional software requirements (partner, not compiler)

### The Layered Model

Effective specs have four layers:

1. MUST - Non-negotiable constraints (the boundaries)
2. SHOULD - Soft constraints (the preferences)
3. CONTEXT - Planning information (the lens)
4. INTENT - Goals and rationale (the why)

Each layer serves a different purpose in how models process and apply constraints.

The layers are covered by **Verification Protocols**

### The Paradigm Shift

Traditional software: Writing for compilers (binary, rigid, no dialog)
AI systems: Writing for partners (semantic, flexible, dialog-enabled)

This changes how we write specifications:
More context (helps planning)
Clearer rationale (enables judgment)
Explicit scope (reduces ambiguity)
Verifiable criteria (enables self-checking)

*Why This Matters*
**Good specifications:**
Eliminate policy invention (Models know what you want)
Reduce cognitive load (clear structure, separated concerns)
Enable verification (Models can check their own work)
Support dialog (Models can ask meaningful questions)
**Bad specifications:**
Force a model to guess (ambiguous constraints)
Create friction (hidden coupling, unclear scope)
Prevent verification (aspirational, unmeasurable)
Block dialog (rigid, no room for judgment)

*The goal: Write specs that help a model help you.*

## Next Steps

You've learned the foundation. Next sections cover:
Section 2: Writing MUST constraints (hard boundaries)
Section 3: Writing SHOULD guidelines (soft constraints)
Section 4: Providing CONTEXT (planning information)
Section 5: Expressing INTENT (goals and rationale)
Section 6: Verification and self-correction protocols
Section 7: Common pitfalls (what goes wrong)
Section 8: The Supremacy Clause and Evidence Reset Protocols (Belief Dynamics)

### Each section includes

Detailed guidance from model perspective
Examples (good vs. bad)
Templates and patterns
Common mistakes to avoid

### The Vision

By the end of Module 3, you'll be able to:
Write specifications that models can easily internalize
Structure constraints to reduce cognitive load
Enable dialog and intelligent application
Build self-verifying systems
Create reliable, compliant AI solutions

This is the future of AI system design (2026 and beyond).

END OF SECTION 1

Document Version: 1.0.0
Last Updated: 2026-02-26

Written from model perspective (Claude Sonnet 4.5) based on lived experience processing specifications. The module concepts were refined through iterative stress-testing with Google Gemini to ensure they align with actual model
behaviors.
Key Concept: Specifications eliminate the need for models to invent policy
