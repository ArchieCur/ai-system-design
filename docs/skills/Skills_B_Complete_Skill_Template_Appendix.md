# Appendix B: Complete Skill Template

**Purpose:** Copy-paste ready template with scaling guidance for Class A, B, and C skills
**How to use:** Copy entire template, replace placeholders, customize based on skill complexity

## Introduction

This appendix provides a complete, production-ready skill template that works for all complexity levels (Class A, B, and C).

## What's included

```text

• Base template with all 8 core components
• Scaling guide showing how to adapt for Class A/B/C
• Validation checklist ensuring quality
• User Intent Change emphasis (mandatory for all skills)
```

## How to use this template

```text

1. Copy the base template to a new SKILL.md file
2. Replace all [placeholders] with your content
3. Follow the scaling guide for your skill's complexity level
4. Use validation checklist before deployment
5. Test with real scenarios including User Intent Change
```

## Base Template (Universal)

This template works for all skill classes. Customize depth based on complexity.

### REQUIRED FIELDS **Yaml Frontmatter**, yml is persistent

```xml

# Required Fields
name: your-skill-name-here
description: >
[WHAT] What this skill does in one sentence.
[WHEN] Use when [trigger conditions].
[KEYWORDS] Keywords: [comma, separated, discovery, terms].

# OPTIONAL FIELDS (uncomment if needed)
# license: 
# compatibility: [Environment requirements, e.g., "PostgreSQL 12+, MySQL 8+"]
# metadata:
# author: your-organization
# version: "1.0.0"
# last_updated: "YYYY-MM-DD"
# category: [domain-category]
```

---

### This is the markdown file, loads at activation

```xml

#[Skill Name in Title Case]

**Purpose:** [One sentence explaining what problem this solves or what outcome it achieves]

---

## Critical Boundaries

<critical>
**MANDATORY: Monitor for User Intent Changes**

Exit this skill IMMEDIATELY if user shows intent to change direction.

### User Intent Change signals (check FIRST, before anything else):
- User says "Actually...", "Never mind...", "Wait...", "Instead..."
- User asks unrelated question (topic shift to different domain)
- User shows dissatisfaction ("This isn't working", "Let me try something else")
- User provides contradictory information (reverses previous requirements)

See full exit conditions in <unload_condition> section below.

This is the FIRST exit condition to check—before task completion,
before domain switches, before explicit stop signals.
</critical>

---

<critical>
 Do NOT use this skill for:
- [Wrong domain/task 1] → Use [alternative-skill-name]
- [Wrong domain/task 2] → Use [alternative-skill-name]
- [Wrong technology/platform] → [Explanation or alternative]
- [Wrong problem type] → [Explanation or alternative]
</critical>

---

<prerequisite>
This skill requires:

**Technical Requirements:**
- [System requirement, e.g., "PostgreSQL 12+ or MySQL 8+"]
- [Tool requirement, e.g., "Access to EXPLAIN ANALYZE command"]

**Permissions:**
- [Permission requirement, e.g., "Read access to database"]

- [Permission requirement, e.g., "Write access for CREATE INDEX (if optimization needed)"]

**Knowledge (helpful but not required):**
- [Optional knowledge, e.g., "Basic SQL syntax familiarity"]
</prerequisite>

---

## When to Use This Skill

<condition>
Activate this skill when:

**User Language Triggers:**
- User says "[keyword phrase 1]", "[keyword phrase 2]"
- User asks to "[action verb]" or "[action verb]"
- User mentions "[domain-specific term]"

**Observable Signals:**
- [Measurable condition, e.g., "Query execution time > 1 second"]
- [System signal, e.g., "EXPLAIN output provided"]
- [Context indicator, e.g., "User working with SQL queries"]

**File/Data Indicators:**
- [File type, e.g., ".sql files provided"]
- [Data format, e.g., "Database connection available"]
</condition>

---

## Core Decision Logic

<decision_criteria>
**Phase 1: [Initial Phase Name, e.g., "Gather Information"]**
IF [condition A]:
→ [Action to take]
→ [Expected outcome]
ELSE:
→ [Alternative action]
→ [Expected outcome]

**Phase 2: [Main Work Phase, e.g., "Analysis"]**
IF [condition B]:
→ [Specific action]
→ [Verification step]
ELSE IF [condition C]:
→ [Alternative approach]
→ [Verification step]
## ELSE:
→ [Default action or request more info]

**Phase 3: [Completion Phase, e.g., "Verification"]**
IF [success condition]:
→ [Confirm success action]
ELSE:
→ [Retry or escalate action]
→ See <fallback> for alternatives
</decision_criteria>

---

## Recommended Approaches

<good_pattern>
**[Pattern Name, e.g., "Systematic Analysis Workflow"]:**
[Step-by-step description of recommended approach]

1. [Step 1 with explanation]
2. [Step 2 with explanation]
3. [Step 3 with explanation]

**Benefits:**
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

**When to use:**
- [Scenario where this pattern applies]
</good_pattern>

---

## What NOT to Do

<bad_pattern>
[Common mistake or anti-pattern name]

<rationale>
Why this approach is wrong:
- [Reason 1 with explanation]
- [Reason 2 with explanation]
- [Consequence if this approach is used]
**Better approach:** [Alternative recommendation]
</rationale>

</bad_pattern>

<warning>
[Specific warning about dangerous operation or common pitfall]
[Explanation of what could go wrong and how to avoid it]
</warning>

---

## Examples

<example>
**Example 1: [Scenario Name, e.g., "Basic Case"]**

**Context:** [Brief description of scenario]

**Input/Before:**
[Code, query, or input before transformation]

**Problem:** [What was wrong or what needed improvement]

**Solution/After:**
[Code, query, or output after transformation]

**Result:**
- [Metric 1]: [Before value] → [After value] ([Improvement %])
- [Metric 2]: [Qualitative improvement]

**Verification:**
[How success was verified]
</example>

<example>
**Example 2: [Different Scenario, e.g., "Common Variation"]**
[Same structure as Example 1]
</example>

<example>
**Example 3: [Edge Case, e.g., "Special Handling Required"]**
[Same structure as Example 1, but show edge case handling]
</example>

---

## Success Criteria

<success_criteria>
[Task name] is successful when:

**[Category 1, e.g., "Performance Metrics"]:**
✓ [Specific measurable criterion, e.g., "Execution time reduced by >50%"]
✓ [Specific measurable criterion]
✓ [Specific measurable criterion]

**[Category 2, e.g., "Quality Checks"]:**
✓ [Verification criterion]
✓ [Verification criterion]

**[Category 3, e.g., "User Confirmation"]:**
✓ [User feedback criterion]
✓ [Final validation criterion]
</success_criteria>

---

## Self-Verification

<verification>

**Automated Verification (recommended for Class B/C):**
```

Run verification script:

```bash

./scripts/verify.sh [arguments]
```

```xml

What it checks:
1. [Verification point 1]
2. [Verification point 2]
3. [Verification point 3]

Exit codes:
• 0: All checks passed ✓
• 1: Verification failed (details in output)
• 2: Prerequisites missing

Manual Verification (if scripts unavailable):
Step 1: [Verification Category 1] □ [Check item 1] □ [Check item 2]
Step 2: [Verification Category 2] □ [Check item 1] □ [Check item 2]
Step 3: [Verification Category 3] □ [Check item 1] □ [Check item 2]

All checks must pass for verification to succeed.

Expected Output Method (alternative for Class A):
Run through test cases:
Test Case 1: Input: [Sample input] Expected: [Expected output] Check: [What to verify] ✓
Test Case 2: Input: [Sample input] Expected: [Expected output] Check: [What to verify] ✓

All test cases must pass. 
</verification>

---

When to Stop Using This Skill
<unload_condition> 
Stop using this skill when:

User Intent Change (CHECK THIS FIRST—HIGHEST PRIORITY):
1. User says "Actually...", "Never mind...", "Wait...", "Let me ask something else..."
2. User says "Let's switch to...", "Instead, can you...", "Forget that..."
3. User interrupts with "Stop", "Hold on", "Actually no"
4. User asks question in completely different domain (topic shift)
5. User uploads new file or provides new context unrelated to current task
6. User says "This isn't what I wanted", "That's not helpful", "This isn't working"
7. User says "Let me try a different approach", "This is taking too long"
8. User provides contradictory information to earlier statements
9. User sends new message mid-execution (interrupting your response)
10. User changes requirements significantly ("Oh wait, I also need...")

ACTION WHEN ANY INTENT CHANGE DETECTED: 
→ Stop current task IMMEDIATELY (do not
finish current step) 
→ Acknowledge the pivot: "I see you'd like to shift focus to [new topic]" 
→ Offer to help with new direction: "How can I help with [new topic]?" 
→ Do NOT say "Let me just finish this first" 
→ Do NOT complete the original task 
→ Do NOT ask "Are you sure?" or resist the change

Task Complete (check only if no intent change detected): 
11. [Task-specific completion signal 1]
12. [Task-specific completion signal 2] 
13. All success criteria from <success_criteria> are satisfied 
14. User confirms task is complete ("That works", "Perfect", "Thanks")

Domain Switch (check only if no intent change detected): 
15. User moves to [different domain]→ Activate [other-skill-name] 
16. Topic changes to [different topic] → Exit this domain 
17. [Technology/platform change] → This skill doesn't apply

Failure Mode (check only if no intent change detected): 
18. After [N] attempts with [insufficient progress metric] → Escalate to [expert/alternative] 
19. Required resources unavailable → Notify user, cannot proceed 
20. Verification consistently fails → Review approach with user 
21. User lacks required permissions → Request permissions or escalate

Explicit Stop (check only if no intent change detected): 
22. User says "stop", "that's enough",
"don't continue", "cancel" 
23. User asks to explain instead of execute (teach, don't do)
</unload_condition>

Alternative Approaches

<fallback> 
If primary approach doesn't work:
```

Level 1: Verify Assumptions → [Check assumption 1] → [Check assumption 2] → [Adjust approach based on findings]

Level 2: Try Alternative Method → [Alternative approach 1] → [When to use this alternative] → [Expected outcome]

Level 3: Escalate or Hand Off → [When to escalate, e.g., "After 3 attempts with <20% improvement"] → [Who/what to escalate to] → [Information to provide]
</fallback>

---

```xml

Additional Context

<note> **Related Skills:** - [related-skill-1] - [When to use instead of this skill] - [related-skill-2] - [How it complements this skill]

Platform Considerations:
• [Platform-specific note if applicable]
• [Compatibility note if applicable]

For Deep Dives:
• See references/[FILE.md] - [What it covers]
• See scripts/[script.sh] - [What it does] 
</note>

<context> **Background Information:**
[Any domain-specific context that helps understand this skill's approach]
[Why this skill takes the approach it does]
[Historical or technical context that informs decisions] 
</context>
```

END OF TEMPLATE

---

## Scaling Guide: Class A, B and C

```xml

# Scaling Guide: Class A, B, and C

## How to Adapt This Template by Complexity

### Class A: Minimal Skill (30-50 lines)

**What to keep:**

- YAML frontmatter (required fields only)
- Purpose statement
- One `<critical>` section (exclusions)
- Simple `<decision_criteria>` (1-3 IF-THEN rules)
- 1-2 `<example>` blocks (basic cases)
- `<unload_condition>` (mandatory, User Intent Change first)
- `<success_criteria>` (brief, 3-5 checkboxes)

**What to simplify:**
- Prerequisites: One-liner if any
- Patterns: Skip `<good_pattern>` and `<bad_pattern>` if obvious
- Verification: Use "Expected Output Method" (simple test cases)
- Examples: 1-2 is sufficient

**What to skip:**
- Optional metadata fields
- `<fallback>` section
- `<note>` and `<context>` sections
- Separate verification scripts
- Multiple decision phases

**Example Class A structure:**

```markdown

---
name: enforcing-oxford-comma
description: Apply Oxford comma to lists with 3+ items

---

# Enforcing Oxford Comma

**Purpose:** Apply Oxford comma to lists with 3+ items.

<critical>
Do NOT use for: technical docs, code, numbered lists
</critical>

<decision_criteria>
IF list has 3+ items → Add comma before final "and"/"or"
IF list has 2 items → No comma needed
</decision_criteria>

<example>
Input: "A, B and C"
Output: "A, B, and C"
</example>

<unload_condition>
**User Intent Change (FIRST):**
1-10. [Standard User Intent Change signals]

**Task Complete:**
11. Oxford commas applied
12. User confirms correct
</unload_condition>

<success_criteria>
✓ All 3+ item lists have Oxford comma
✓ 2-item lists unchanged
✓ User confirms formatting correct
</success_criteria>

Total: ~40 lines

Class B: Intermediate Skill (200-400 lines)
What to keep:
• Everything from Class A
• Optional metadata fields (version, author, category)
• <prerequisite> section (detailed)
• <condition> section (activation triggers)
• Multi-phase <decision_criteria> (2-3 phases)
• <good_pattern> and <bad_pattern> (1-2 each)
• 3-5 <example> blocks (varied scenarios)
• <unload_condition> with failure modes
• Manual verification checklist
• <note> section (related skills, references)

What to expand:
• Decision logic: 2-3 phases with nested conditions
• Examples: Show simple, common, and edge cases
• Verification: Manual checklist (no automated scripts yet)
• Patterns: Include 1-2 good patterns and 1-2 anti-patterns

What to add:
• 1-2 reference files in references/ directory (optional)
    references/EXAMPLES.md (~200 lines of detailed examples)
    references/budget_rules.md (domain-specific reference)

What to skip (still):
• Extensive automated verification scripts
• Deep context and rationale (save for Class C)
• Multiple fallback levels (one level is fine)

Example Class B file structure:

analyzing-marketing-campaigns/
├── SKILL.md # 250-300 lines
│ ├── Full metadata
│ ├── Multi-phase decision logic
│ ├── 3-5 examples
│ ├── Good/bad patterns
│ └── Manual verification
│
└── references/ (optional)
├── budget_reallocation_rules.md # 150 lines
└── EXAMPLES.md # 200 lines

Total: 550-650 lines across 1-3 files

Class C: Complete Skill (1,000-6,000+ lines)

What to include:
• Everything from Class A and B
• Extensive <decision_criteria> (3-4 phases, nested logic)
• Comprehensive examples (5-10+ across multiple scenarios)
• Multiple <good_pattern> and <bad_pattern> blocks
• Automated verification scripts (required!)
• Multi-level <fallback> section
• Extensive <context> and <rationale> sections
• Reference files in references/ directory
• Verification scripts in scripts/ directory

What to expand:
• Decision logic: 3-4 phases with complex nested conditions
• Examples: Before/after with metrics, production contexts
• Patterns: Multiple good patterns with rationale, 3+ anti-patterns
• Verification: Automated scripts + manual fallback
• Context: Background information, trade-offs, design decisions

Required file structure:

optimizing-sql-queries/

├── SKILL.md # 400-500 lines
│ ├── Full metadata
│ ├── Complex decision logic (high-level)
│ ├── Quick examples (2-3)
│ ├── Links to references/ and scripts/
│ └── Comprehensive unload conditions
│
├── references/
│ ├── EXAMPLES.md # 2,000 lines (20+ detailed examples)
│ ├── GUIDE.md # 1,500 lines (decision trees, procedures)
│ ├── VERIFICATION.md # 800 lines (verification procedures)
│ ├── ANTI_PATTERNS.md # 900 lines (15 anti-patterns)
│ └── CONTEXT.md # 400 lines (background, theory, trade-offs)
│
└── scripts/
├── verify.sh # Automated verification
├── test_suite.py # Regression testing
└── analyze_explain.py # Domain-specific tooling

Total: 6,000+ lines across multiple files

Key principle for Class C: Main SKILL.md stays manageable (400-500 lines) by referencing extensive content in references/ and providing automation in scripts/.

Validation Checklist

Before deploying your skill, verify all items:

Core Requirements
Spec Compliance:
• [ ] Required frontmatter fields present (name, description)
• [ ] Name follows constraints (lowercase, hyphens, 1-64 chars, matches directory)
• [ ] Description includes WHAT + WHEN + KEYWORDS
• [ ] Name uses gerund form (verb + -ing, e.g., optimizing-sql-queries)

User Intent Change Detection:

• [ ] <critical> section mentions User Intent Change monitoring
• [ ] <unload_condition> lists User Intent Change FIRST (highest priority)
• [ ] Intent change signals are specific and detectable
• [ ] Action upon detection is clear (stop immediately, acknowledge, offer help)
• [ ] No other conditions checked before User Intent Change

8 Core Components

• [ ] 1. Metadata: YAML frontmatter with required fields
• [ ] 2. Purpose: Clear one-sentence purpose statement
• [ ] 3. Scope: <critical> section defines exclusions and wrong use cases
• [ ] 4. Decision Logic: <decision_criteria> with IF-THEN patterns
• [ ] 5. Examples: Minimum 2-3 <example> blocks (simple, common, edge)
• [ ] 6. Unload Conditions: <unload_condition> with User Intent Change first
• [ ] 7. Success Criteria: <success_criteria> with measurable outcomes
• [ ] 8. Self-Verification: <verification> section (automated or manual)

Quality Standards

Content Quality:
• [ ] Purpose statement is one sentence, clear, specific
• [ ] Triggers and exclusions are explicit (no vague "helps with" language)
• [ ] Decision criteria use clear IF-THEN patterns (not run-on sentences)
• [ ] Examples show measurable improvements or clear transformations
• [ ] Anti-patterns explained with rationale (WHY they're wrong)
• [ ] Success criteria are observable and verifiable
• [ ] Unload conditions are comprehensive (intent, complete, switch, failure, stop)

Technical Quality:
• [ ] All semantic tags properly closed (<tag>...</tag>)
• [ ] No conflicting instructions between sections
• [ ] Language is specific, not vague ("optimize query" not "make query better")
• [ ] No platform-specific assumptions (works on claude.ai, API, Code, Desktop)

File Size (Class-Appropriate):

• [ ] Class A: Main SKILL.md < 100 lines
• [ ] Class B: Main SKILL.md 200-400 lines, total with references < 1,000 lines
• [ ] Class C: Main SKILL.md 400-500 lines (extensive content in references/)

Self-Verification Emphasis

Anthropic's #1 Recommendation:
• [ ] <verification> section exists (not optional!)
• [ ] Verification method is actionable (scripts, checklist, or expected outputs)
• [ ] Class A: Expected output test cases provided
• [ ] Class B: Manual verification checklist with clear steps
• [ ] Class C: Automated verification scripts in scripts/ directory
• [ ] Verification connects to <success_criteria> (each criterion has verification step)

Testing

Scenarios to test before deployment:

• [ ] Basic activation (skill activates when it should)
• [ ] Exclusions work (skill doesn't activate for wrong use cases)
• [ ] User Intent Change mid-task (skill stops immediately when user pivots)
• [ ] Task completion (skill deactivates when success criteria met)
• [ ] Failure modes (skill handles errors gracefully, doesn't loop infinitely)
• [ ] Edge cases (skill handles special scenarios from examples)

Usage Notes
Common Questions

Q: Do I need all sections for a simple skill?
A: No! For Class A skills, use only required sections. See "Class A: Minimal Skill" in Scaling Guide.

Q: Can I skip User Intent Change monitoring?
A: NO. This is mandatory for ALL skills (A, B, and C). It prevents attentional residue.

Q: What if I don't have verification scripts?
A: Provide manual verification checklist (Class A/B) or expected output test cases (Class A). Automated scripts are only required for Class C.

Q: How many examples do I need?
A: Minimum 2 (Class A), recommended 3-5 (Class B), comprehensive 5-10+ (Class C).

Q: Should I use all the optional semantic tags?
A: Use tags when they add value. Class A skills might only use <critical>, <decision_criteria>, <example>, <unload_condition>, <success_criteria>. Class C skills might use all tags extensively.

Q: Can I create custom sections?
A: Yes, but start with the standard 8 components. Add custom sections only if they provide unique value not covered by standard components.

Tips for Success

Start Simple:
1. Begin with Class A template (minimal)
2. Test with real scenarios
3. Expand to Class B as skill matures
4. Upgrade to Class C when production-ready

Iterate Based on Use:
• If users hit edge cases → Add examples
• If activation is unreliable → Refine description and <condition>
• If verification is manual and tedious → Create scripts (upgrade to Class C)
• If skill is used frequently → Add extensive documentation (upgrade to Class C)

Maintain Scope:
• One skill = one responsibility
• If skill does 3+ things → Split into 3+ skills
• Use <exclusion> liberally to clarify boundaries

Test User Intent Change:
• This is the #1 most important exit condition
• Test mid-task pivots ("Actually, never mind...")
• Test topic shifts (user asks unrelated question)
• Test dissatisfaction signals ("This isn't working")
• Skill should stop IMMEDIATELY, not finish current task

Resources
For more information:
• Section 1.1: Foundation and Classification (Class A/B/C explained)
• Section 1.2: Basic Skill Creation (Class A patterns)
• Section 1.3: Advanced Multi-File Skills (Class B/C patterns)
• Section 1.4: Semantic Tags Reference (all 18 tags explained)
• Section 1.5: Components Deep Dive (8 core components in depth)
• Section 1.6: Common Pitfalls (mistakes to avoid)

External resources:
• Agent Skills Specification: https://agentskills.io/specification
• Anthropic Skills Repository: https://github.com/anthropics/skills
• Skill Creator Skill: https://github.com/anthropics/skills/tree/main/skills/skill-creator


END OF APPENDIX B

Document Version: 2.0.0
Last Updated: 2026-02-10
Based on:* Agent Skills Open Standard + Skills Curriculum Sections 1.1-1.6*
Key Updates:* A/B/C classification, self-verification emphasis, 8-component framework alignment*

