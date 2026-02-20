# Skills_1.2_Basic_Template_ClassA

**For:** Inexperienced users creating their first skill
**Goal:** Create a working Class A skill in 15 minutes
What you'll build: Simple formatting rule, style guide, or organizational constraint

## Who This Section Is For

**You're in the right place if:**
• You're new to skills and want to start simple
• You're creating formatting rules or style guides
• Your skill is under 100 lines
• You don't need automated verification
• You use reasoning only OR 1-2 read-only tools

### Examples of Class A skills

• "Always use Oxford commas in documentation"
• "Format dates as YYYY-MM-DD"
• "Use company disclaimer in client emails"
• "Follow PEP8 style for Python code"

If your skill is more complex, see Section 1.3 (Advanced Skills).

## How to Use This Template

### Three approaches—choose what works for you

**Approach 1: Quick Worksheet (Fastest)**
Answer the questions below, then copy-paste the completed template at the end.

**Approach 2: Form with Guidance (Recommended)**
Fill in each element with explanations right beneath to guide you.

**Approach 3: See Example First (If you learn by example)**
Jump to the "Complete Example" section, study it, then come back and build yours.

Whichever you choose, you'll have a working skill by the end!

## Part 1: Quick Worksheet (Answer These Questions)

If you prefer detailed guidance, skip to Part 2 (Form with Explanations)

### Basic Information

1. What should your skill be called?
Skill name: ____________________________
(lowercase, hyphens only, 1-64 characters)

2. What does your skill do? (One sentence)
Description: ____________________________
(Describe what it does AND when to use it. Include keywords.)

3. What's the main purpose?
Purpose: ____________________________
(Single sentence: "This skill ensures..." or "This skill helps...")

**When to Use This Skill**
4. The AI should use this skill when:
(List when AI should use the Skill)
•
•
•
5. The AI should NOT use this skill when:
(List when AI should not use this Skill)
•
•
•

**The Rules**
6. What's the correct way to do this? (Good pattern)
7. What's the wrong way? (What to avoid)

**Completion**
8. How does the AI know the task is done?
(List when AI should know the task is done)
•
•
9. When should the AI stop using this skill?
(List when AI should know stop using the Skill)
•
•


**Done with worksheet?** → Jump to "Your Completed Template" section below to assemble your skill!

## Part 2: Form with Embedded Explanations

If you prefer the quick worksheet, you can skip this section

### Element 1: Skill Name

**Your skill name**
Explanation:
The skill name is used for:

• Directory name (your-skill-name/)
• File discovery
• References in other skills

Rules:
• 1-64 characters
• Lowercase letters, numbers, hyphens only
• No spaces, no underscores, no uppercase
• Must match your directory name exactly

### Skill Name Examples

Good
• oxford-comma-rule
• date-format-iso8601
• company-email-disclaimer
Bad
X Oxford_Comma (uppercase, underscore)
X my skill (spaces)

## Element 2: Description

**Your description:**

Explanation:
The description field is how the AI decides when to activate your skill.

Must include:

1. What the skill does
2. When to use it
3. Keywords for discovery

Rules:

• 1-1024 characters
• Be specific (not "helps with writing" but "ensures Oxford commas in lists")
• Include trigger words the user might say

### Skill Description Examples

**Good:**

"Apply Oxford comma rule to lists. Use when writing documentation, emails, or any formal text
with three or more items. Keywords: lists, commas, and, serial comma."

**Too vague:**

"Helps with punctuation"

### Element 3: Purpose Statement

**Your purpose (one sentence):**

Explanation:

This is the first thing in your skill body. It tells the AI why this skill exists.
Format: Start with "This skill ensures..." or "This skill helps..."

### Purpose Satement Examples

• "This skill ensures consistent date formatting across all documentation."
• "This skill helps maintain brand voice in client communications."
• "This skill applies company email disclaimer to external messages."

Keep it to ONE sentence. If you need more, you might be building a Class B skill (see Section
1.3).

### Element 4: Critical Information (Exclusions)

**What should the AI NOT do with this skill?** (List what AI should not do with this Skill)

•
•

Explanation:

```xml

Use the <critical> tag to prevent misuse.
```

***Think about:***

• Wrong domains (don't use for X, use for Y)
• Wrong file types (don't apply to code, only prose)
• Wrong contexts (don't use in informal chat)

### Critical Informatio9n (Exclusion) Example

```xml
<critical>
Do NOT use this skill for:
- Code comments (different formatting rules)
- Informal messages (Slack, text)
- User-facing error messages (brevity required)
</critical>
```

## Element 5: When to Use

**The AI should use this skill when:** (List when the AI should use this Skill)

•
•
•

Explanation:

List 2-4 specific scenarios where this skill should activate.

**Be concrete:**

• "User asks to write a formal email"
• "Drafting documentation with lists"
X "User needs help writing" (too vague)

**Trigger phrases: Include actual words users might say:**

• "Can you write..."
• "Format this..."
• "Create a..."

## Element 6: Good Pattern

**The correct way to do this:**
Explanation:

```xml
Use the <good_pattern> tag to show the right approach.

### Example:

<good_pattern>


Lists with three or more items:

"We need apples, oranges, and bananas."
The comma before "and" is the Oxford comma.
Always include it for clarity.
</good_pattern>
```

**Include:**

• Concrete examples
• Why this is the right way
• Expected format

### Element 7: Bad Pattern

What NOT to do:

Explanation:

```xml
Use the <bad_pattern> tag to show common mistakes.


### Example:

<bad_pattern>

Missing Oxford comma:
"We need apples, oranges and bananas."
This is ambiguous—"oranges and bananas" could be one item.
</bad_pattern>
```

Why this matters: AI learns from contrast. Showing both good AND bad examples improves
accuracy.

### Element 8: Success Criteria

**How to verify the task is complete:** (List ways for AI to verify the task is complete)

•
•

Explanation:

What does success look like?

**Keep it simple for Class A:**

• ✓ Rule is applied
• ✓ Format matches examples
• ✓ User confirms it looks right

### Success Criteria Example

Success Criteria is met when:

✓ All lists with 3+ items have Oxford commas
✓ Format matches good_pattern examples
✓ User confirms text is correct

### Element 9: Unload Conditions

When should the AI stop using this skill?

•
•

Explanation:

Tell the AI when to deactivate.

### Common unload triggers-

1. Task is complete (formatting applied)

2. User changes topic (from writing to coding)

3. User says "stop" or "that's enough"

4. User asks about the rule (explain, don't apply)

### Unload Trigger Example

```xml
<unload_condition>

Stop using this skill when:

1. Formatting is complete and user confirms

2. User switches to different task (coding, analysis)

3. User asks to explain the rule (don't apply it)

4. User says "stop" or "never mind"

</unload_condition>
```

**Include User Intent Change signals (from Section 1.1):**

• "Actually..." / "Never mind..." / "Wait..."
• Topic shift to unrelated domain
• User provides contradictory information

## Part 3: Complete Example (Study This)

Here's a fully-completed Class A skill you can use as a reference:

name: oxford-comma-rule
description: >
Apply Oxford comma (serial comma) to lists with three or more items.
Use when writing documentation, emails, or formal text.
Keywords: lists, commas, serial comma, and, punctuation.

---

Oxford Comma Rule

**Purpose:** This skill ensures consistent use of Oxford commas in lists for clarity and
readability.

---

Critical Information

```xml

<critical>

Do NOT use this skill for:

- Code syntax (different grammar rules)

- Informal messages (Slack, text messages)

- Direct quotes (preserve original punctuation)
- Non-English languages (different conventions)

</critical>

```

---

When to Use This Skill

Use this skill when:

- User asks to write or edit formal text

- Drafting documentation with lists

- Writing emails, reports, or articles

- Any text with lists of three or more items

---

The Rule

```xml

<good_pattern>

**Correct - With Oxford comma:**

"We offer training in Python, JavaScript, and SQL."

The comma before "and" (the Oxford comma) eliminates ambiguity.

**More examples:**

- "The flag is red, white, and blue."

- "Bring a notebook, pen, and laptop."
- "She studied math, physics, and chemistry."

</good_pattern>

<bad_pattern>

**Incorrect - Missing Oxford comma:**
"We offer training in Python, JavaScript and SQL."

Without the Oxford comma, "JavaScript and SQL" might be read as a single item.

**Ambiguous examples:**

- "I love my parents, Taylor Swift and Beyoncé."

(Are your parents Taylor Swift and Beyoncé?!)


- "The book is dedicated to my mother, Oprah Winfrey and God."

(Is your mother Oprah Winfrey?!)
</bad_pattern>

```

---

Success Criteria

Task is successful when:

✓ All lists with 3+ items include Oxford comma

✓ Format matches good_pattern examples

✓ Text is clear and unambiguous

✓ User confirms formatting is correct

---

When to Stop Using This Skill

```xml
<unload_condition>


Stop using this skill when:


**User Intent Change (check FIRST):**

1. User says "Actually...", "Never mind...", or "Wait..."

2. User asks unrelated question (topic shift)

3. User shows dissatisfaction with approach

**Task Complete:**

4. Formatting applied successfully

5. User confirms text is correct

**Domain Switch:**

6. User switches to coding (different punctuation)

7. User switches to informal writing (chat, text)

**Explicit Stop:**

8. User asks to explain the rule (don't apply)

9. User says "stop" or "that's enough"

</unload_condition>

```

---

Notes

```xml

<note>

The Oxford comma is standard in American English but optional in British English.

If user specifies British English, ask for their preference.


### For two-item lists, no comma before "and":

✓ "Python and JavaScript" (no comma needed)

</note>

```

## Part 4: Your Completed Template

Copy this template, replace the [BLANKS] with your answers from Part 1 or Part 2, and save as SKILL.md:

---

````markdown

name: [your-skill-name]
description: >
[What your skill does]. Use when [trigger condition].
Keywords: [discovery keywords].
---

#[Your Skill Title]

**Purpose:** [Single sentence explaining what problem this solves]

---

##Critical Information

<critical>

Do NOT use this skill for:

- [Exclusion 1]
- [Exclusion 2]
- [Exclusion 3]

</critical>

---

## When to Use This Skill

Use this skill when:
- [Trigger scenario 1]
- [Trigger scenario 2]
- [Trigger scenario 3]

---

## The Rule

<good_pattern>
**Correct approach:**

[Show the right way with examples]

[Explain why this is correct]

</good_pattern>

<bad_pattern>

**What to avoid:**

[Show the wrong way with examples]

[Explain why this is wrong]

</bad_pattern>

---

## Success Criteria


Task is successful when:

✓ [Measurable criterion 1]

✓ [Measurable criterion 2]

✓ [Measurable criterion 3]

---

## When to Stop Using This Skill

<unload_condition>

Stop using this skill when:


**User Intent Change (check FIRST):**

1. User says "Actually...", "Never mind...", or "Wait..."
2. User asks unrelated question (topic shift)
3. User shows dissatisfaction with approach


**Task Complete:**

4. [Task completion signal]
5. User confirms success

**Domain Switch:**

6. [Different domain that doesn't apply]

**Explicit Stop:**

## 7. User says "stop" or "that's enough"

</unload_condition>

---

## Notes

<note>

[Any additional context, edge cases, or helpful information]
</note>

````

## Validation Checklist

### Before using your skill, verify

**Frontmatter:**

• [ ] Name is lowercase, hyphens only, 1-64 characters
• [ ] Name matches your directory name
• [ ] Description includes WHAT, WHEN, and KEYWORDS

**Body:**

```xml
• [ ] Purpose is one clear sentence
• [ ] <critical> tag lists exclusions (what NOT to do)
• [ ] 2-4 "When to Use" scenarios are specific
• [ ] <good_pattern> shows correct approach with examples
• [ ] <bad_pattern> shows mistakes to avoid
• [ ] Success criteria are observable
• [ ] Unload conditions include User Intent Change (FIRST!)

```

**Quality:**

• [ ] Total length under 100 lines (Class A guideline)
• [ ] Examples are concrete, not abstract
• [ ] Language is clear and specific
• [ ] No ambiguous terms ("best practices", "usually", "sometimes")

## Testing Your Skill

### Step 1: Ask AI to Review

I created a skill called [your-skill-name]. Can you review it and tell me:

1. Is the description clear about when to use it?
2. Are the good/bad patterns helpful?
3. Are the exclusions specific enough?
4. Is anything confusing or ambiguous?

### Step 2: Test Activation Try a query that should trigger your skill

[Give a task that matches your "When to Use" scenarios]

Verify the AI

• ✓ Activates the skill
• ✓ Follows the good_pattern
• ✓ Avoids the bad_pattern
• ✓ Unloads when task complete

### Step 3: Test Exclusions Try a query that matches your exclusions

```xml

[Give a task that's in your <critical> "Do NOT use" list]

Verify the AI:

• ✓ Does NOT activate your skill
• ✓ Uses different approach or different skill
```

## Common Beginner Mistakes

### Mistake 1: Vague Description

Bad: "Helps with writing"
Good: "Apply Oxford comma to lists with 3+ items in formal writing"

Why: AI can't activate if it doesn't know WHEN to activate.

### Mistake 2: No Concrete Examples

Bad: "Use good punctuation"
Good: "apples, oranges, and bananas" (shows exact format)

Why: AI learns from specific examples, not abstract rules.

### Mistake 3: Missing Exclusions

Bad: Only says what TO do
Good: Says what to do AND what NOT to do

Why: Without boundaries, skill activates inappropriately.

### Mistake 4: Forgetting User Intent Change

Bad: Only "task complete" in unload conditions

Good: User Intent Change checked FIRST

Why: AI should stop immediately when user pivots, not finish task.

Mistake 5: Too Much Complexity

Bad: 300-line Class A skill with 10 examples

Good: 60-line skill with 2-3 examples
Why: Class A should be simple. If you need more, it's Class B (see Section 1.3).

## Next Steps

You've created your first skill!

### Implementing Your Skill

### On Anthropic Claude

1. Create directory: your-skill-name/
2. Save as: your-skill-name/SKILL.md
3. Upload to Claude.ai (Settings → Features → Upload Skill)

### On Other Platforms: See Appendix D: Cross-Platform Implementation for OpenAI/Gemini instructions

## Want to Learn More

### Improve your skill

• Section 1.4: Learn all 18 semantic tags (you used 3 basic ones)
• Section 1.5: Deep dive into each component
• Section 1.6: Common pitfalls and how to avoid them

### Build more complex skills

• Section 1.3: Advanced Skills (Class B/C)
    o Multi-file architecture
    o References/ and scripts/
    o Complex tool orchestration
    o Automated verification

### Understand the ecosystem

• Tool Literacy module: How skills and tools work together

## Quick Reference

### Three basic tags for Class A

```xml

• <critical> - Must-follow instructions, exclusions
• <good_pattern> - Show the right way
• <bad_pattern> - Show mistakes to avoid
```

### File structure

your-skill-name/
└── SKILL.md
Target length: 50-100 lines (Class A)

Key principle: Be specific, not vague. Use concrete examples, not abstract rules.

Congratulations! You've mastered Class A skills. When you're ready for more complexity, see Section 1.3 (Advanced Skills).

## END OF SECTION 1.2

Document Version: 1.0.0
Last Updated: 2026-02-08
Target Audience: Inexperienced users, first skill

Skill Class: Class A (Simple)


