# Skills_A_Semantic_Tag_Reference_Appendix

*Converted from PDF: Skills_A_Semantic_Tag_Reference_Appendix.pdf*



---
**Page 1**

Appendix A: Semantic Tags Reference

Quick reference guide for all recommended semantic tags.

Master the Tier 1: Essential Tags first. Use the other 11 only when you need granular control.

Tier 1: Essential Tags (Use in Every Skill)
Tag Purpose Example

Must-follow instructions, <critical>Do not use for schema
<critical>
highest priority design</critical>
Common mistakes, <warning>Over-indexing slows
<warning>
caution flags writes</warning>
Recommended <good_pattern>Always measure before
<good_pattern>
approaches optimizing</good_pattern>

<bad_pattern>Adding indexes without
<bad_pattern> Approaches to avoid
measuring</bad_pattern>
<decision_criteria>IF slow query → analyze →
<decision_criteria> Core IF-THEN logic
fix</decision_criteria>
<unload_condition>Stop when performance
<unload_condition> When to stop using skill
meets SLA</unload_condition>

<exclusion>Do NOT use for schema
<exclusion> When NOT to use skill
design</exclusion>
Tier 2: Common Tags (Use When Relevant)

Tag Purpose Example

Additional <note>PostgreSQL and MySQL handle indexes
<note>
context, FYI differently</note>
Reference
<example> <example>Before: 2.3s, After: 0.05s (46x faster)</example>
implementation

<condition> Trigger criteria <condition>Activate when execution time > 1s</condition>

Specific steps to
<action> <action>Run EXPLAIN ANALYZE, then add index</action>
take


---
**Page 2**

Tag Purpose Example

Requirements
<prerequisite> <prerequisite>Requires PostgreSQL 12+</prerequisite>
before use
<sequence> <step id="1" required="true"> Run EXPLAIN

Linear execution ANALYZE on current query to establish baseline </step>
<sequence>
of steps <step id="2" depends_on="1"> Identify bottleneck from
EXPLAIN output </step></sequence>
Tier 3: Advanced Tags (For Complex Skills)

Tag Purpose Example

<rationale>Composite indexes reduce
<rationale> Why this approach
overhead</rationale>

<tradeoff>Indexes speed reads but slow
<tradeoff> Pros and cons
writes</tradeoff>
<context>Different databases have different
<context> Situational factors
optimizers</context>
<success_criteria>✓ Query time reduced
<success_criteria> Verification criteria
>50%</success_criteria>

Alternative if primary <fallback>If indexes don't help, try
<fallback>
fails denormalization</fallback>
Tag Nesting Examples

Good Pattern with Rationale

<bad_pattern>
Using DISTINCT to eliminate duplicates

<rationale>

DISTINCT masks underlying JOIN problems and adds expensive sorting.

Fix JOIN conditions instead of masking symptoms.
</rationale>

</bad_pattern>


---
**Page 3**

Decision Criteria with Actions

<decision_criteria>

### IF query shows full table scan:


<action>


## 1. Identify columns in WHERE clause



## 2. Check existing indexes


## 3. Create index if missing



## 4. Verify with EXPLAIN ANALYZE


</action>

</decision_criteria>

Exclusions with Context
<exclusion>

Do NOT use for NoSQL databases

<context>

This skill is specific to SQL databases (PostgreSQL, MySQL).

### For NoSQL optimization, use database-specific skills:


- MongoDB → mongodb-optimization

- Redis → redis-optimization

</context>

</exclusion>
Usage Principles


### Do:


Use tags for semantic meaning (priority, warning, example)
Nest tags when it adds clarity

Close all tags properly
Combine tags (e.g., <bad_pattern> + <rationale>)


### Don't:



---
**Page 4**

Mix emojis with tags (choose one system)
Over-tag every sentence

Invent new tags without good reason
Use tags for formatting (use Markdown for that)
