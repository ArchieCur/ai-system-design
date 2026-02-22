# Skills_1.4_Semantic_Tags

Section 1.4: Semantic Tags

**For**: All users (referenced from 1.2, 1.3, and 1.5)

**Purpose:** Complete reference for the 18-tag semantic system

What you'll learn: How to structure skills for optimal model interpretation

## Why Semantic Tags Matter

When you write a skill, you're not just writing instructions for humans to read, you're writing
instructions for AI models to parse, prioritize, and execute.


**The challenge:**

```text

• Models need clear signals about:
• What's critical vs. optional
• What to do vs. what to avoid
• When to activate vs. when to deactivate
• How to make decisions vs. when to ask
```

**The solution:** A semantic tag system that provides unambiguous structure.

## Why XML Tags Over Other Approaches

You have several options for signaling importance. Let's compare:

### **Option 1: Emojis (Not Recommended)**

Using emojis such as a stop sign or a warning sign for empasizing caution, or a checkmark to indicate good patterns  can cause these problems:

**Problems**
```text
• Multi-token encoding (🛑 might be 3-4 tokens)
• Ambiguous meaning (🔥 = "hot topic" or "emergency"?)
• Accessibility issues (screen readers inconsistent)
• Cultural variation (emojis mean different things in different contexts)
• Model confusion (might drift into "Reddit commenter" persona)
```

### **Option 2: Formatting (Not Recommended)**
```text
CRITICAL: Do not use for schema design
WARNING: Over-indexing slows writes

**Problems:**

```text
• No semantic meaning (bold could be emphasis, title, or key term)
• Models can't differentiate priority levels reliably
• Doesn't nest well (can't have structured warnings)
• No parseable structure (can't validate or lint)
```

### **Option 3: XML-Style Tags (Recommended)**

```xml

<critical>
Do not use for schema design (use schema-design skill)
</critical>

<warning>
Over-indexing slows INSERT/UPDATE operations.
Always measure before adding indexes.
</warning>

<good_pattern>
Measure before optimizing:
1. Run EXPLAIN ANALYZE on current query
2. Identify bottleneck
3. Apply targeted optimization
4. Verify improvement
</good_pattern>
```

```text
Why this works:
• Semantically clear: Models trained on millions of XML/HTML documents
• Unambiguous: <critical> has one meaning (highest priority)
• Nestable: Can structure complex information hierarchically
• Parseable: Tools can validate, lint, and analyze
• Human-friendly: Easy to type, autocomplete in IDEs
• Accessible: Screen readers handle properly
• Future-proof: Can become formal standard

**Models understand XML structure deeply because they're trained on:**
• HTML (web pages)
• XML (configuration files, data formats)
• SVG (vector graphics)
• Markdown with HTML (documentation)
```
**This isn't an arbitrary choice—it leverages existing model capabilities.**

**Note-** Adding attributes to tags was not tested.

## The 19-Tag System

Tags are organized into three tiers based on usage frequency and importance:

### **Tier 1: Essential (7 tags)**

Master these first- they're the most prominent tags and will be used in almost every Skill you create.

```xml

• <critical> - Must-follow instructions
• <warning> - Common mistakes to avoid
• <good_pattern> - Correct approaches
• <bad_pattern> - Incorrect approaches
• <decision_criteria> - Core IF-THEN logic
• <unload_condition> - When to stop
• <exclusion> - When NOT to use
```

### **Tier 2: Common (6 tags)**

```xml

Use when relevant

• <note> - Additional context
• <example> - Reference implementation
• <condition> - Trigger criteria
• <action> - Specific steps
• <prerequisite> - Requirements
• <sequence> - Ordered steps
```

### **Tier 3: Advanced (6 tags)**

```xml

For complex skills

• <rationale> - Why this approach
• <tradeoff> - Pros and cons
• <context> - Situational factors
• <success_criteria> - Verification criteria
• <fallback> - Alternative if primary fails
• <logic> - Can be used with Decision Criteria for complex nested logic
```

Total: 19 tags

### Tier 1: Essential Tags (Use in Every Skill)

```xml

<critical> - Must-Follow Instructions
```

**Purpose:** Absolute requirements, highest priority, blocking conditions
**When to use:**

• Safety-critical operations
• Scope boundaries (what NOT to use skill for)
• Mandatory prerequisites
• User Intent Change detection (see special pattern below)

**Model interpretation:**
"I MUST follow this. Failure to follow causes serious problems."

**Examples:**
**Blocking condition:**

```xml

<critical>
Do not proceed if database connection is unavailable.
Verify connection before attempting any queries.
</critical>
```

**Scope boundaries:**

```xml

<critical>
Do NOT use this skill for:

- Schema design or migrations → Use schema-design skill
- SQL syntax errors or debugging → Use sql-debugging skill
- NoSQL databases (MongoDB, Redis) → Use database-specific skills
- Query execution time < 100ms → Optimization not needed
</critical>
```

**Safety requirement:**

```xml

<critical>
ALWAYS back up data before running DELETE or UPDATE operations.
This skill does not include rollback capabilities.
</critical>
```

## **MANDATORY PATTERN: User Intent Change (Highly Recommended)**

Every skill **MUST** monitor for **User Intent Changes as the FIRST exit condition.**

**Why this matters:** When users pivot direction, skills that stay active cause **attentional residue** that degrades performance on new tasks. Detecting intent changes early prevents degraded performance from irrelevant context bleeding into new tasks, or worse, executing the wrong actions or not stopping actions based on outdated intent.

**Template:**
**This pattern should appear in EVERY skill you create.**

```xml

<critical>
**MANDATORY: Monitor for User Intent Changes**
Exit this skill IMMEDIATELY if user shows intent to change direction.

User Intent Change signals (check FIRST, before anything else):
- User says "Actually...", "Never mind...", "Wait...", "Instead..."
- User asks unrelated question (topic shift to different domain)
- User shows dissatisfaction ("This isn't working", "Let me try something else")
- User provides contradictory information (reverses previous requirements)

See full exit conditions in <unload_condition> section below.

This is the FIRST exit condition to check—before task completion,
before domain switches, before explicit stop signals.
</critical>
```

**Common Mistakes to Avoid**

```xml

<warning>- 

Purpose: Caution flags, frequent pitfalls, risky operations
When to use:
• Common errors that users make
• Operations with hidden costs
• Approaches that seem correct but fail
• Performance pitfalls

Model interpretation:
"This is a common mistake. I should avoid this approach."
```

**Examples:**
**Hidden cost:**

```xml

<warning>
Adding indexes to every column will slow INSERT/UPDATE operations by 20-30% per index.
Indexes are not free—they speed reads but slow writes.
Only add indexes where read performance gain justifies write cost.
</warning>

**Common error:**

<warning>
Using DISTINCT to "fix" duplicate rows usually indicates a JOIN problem.
DISTINCT masks symptoms with expensive sorting overhead.
Fix the underlying JOIN logic instead of masking the problem.
</warning>

**Performance pitfall:**

<warning>
Optimizing queries without measuring baseline performance first.
You might optimize the wrong thing or make performance worse.
Always measure before → optimize → verify after.
</warning>

**Scope creep**:

<warning>
This skill focuses on query optimization only.

Do not use for:
- Schema design (different concerns, different tradeoffs)
- Application-level caching (outside query scope)
- Database configuration tuning (requires DBA permissions)
</warning>
```

**Correct Approaches**

```xml

<good_pattern>
```
**Purpose:** Recommended practices, proven solutions, examples to emulate

**When to use:**
• Show the right way to do something
• Provide templates or patterns to follow
• Demonstrate best practices
• Give concrete examples

**Model interpretation:
"This is the right way to do it. I should emulate this approach."

**Examples:**
**Step-by-step pattern:**

```xml

<good_pattern>
**Systematic optimization workflow:**

1. **Measure baseline:**
Run EXPLAIN ANALYZE to get current execution time and plan

2. **Identify bottleneck:**
Look for Seq Scan, Nested Loop, or Sort operations on large datasets

3. **Apply targeted fix:**
Add specific indexes, adjust JOIN strategy, or optimize WHERE clauses

4. **Verify improvement:**
Run EXPLAIN ANALYZE again, confirm >50% improvement

5. **Check for regressions:**
Verify related queries didn't slow down
</good_pattern>
```

### Code example:

```xml

<good_pattern>

**Composite index for multi-column queries:**

```sql

-- For queries like: WHERE user_id = X AND status = Y
CREATE INDEX idx_user_status ON orders(user_id, status);

-- Column order matters: put equality conditions first

-- This index works for:
-- WHERE user_id = X AND status = Y ✓
-- WHERE user_id = X ✓

-- But NOT for:

-- WHERE status = Y ✗ (doesn't use index)
</good_pattern>
```

**Decision pattern:**

```xml

<good_pattern>

**When to add indexes:**

✓ Table has >10,000 rows (indexes valuable for large tables)
✓ Column appears in WHERE, JOIN, or ORDER BY (index will be used)
✓ Column has moderate cardinality (not all unique, not all same value)
✓ Query runs frequently (>100 times/day)
✓ Read-to-write ratio >4:1 (benefits outweigh write overhead)

If all criteria met → Add index and verify improvement
</good_pattern>
```

**Incorrect Approaches**

```xml

<bad_pattern>
```

**Purpose:** Anti-patterns, approaches to avoid, wrong solutions
**When to use:**


• Show what NOT to do
• Explain why an approach fails
• Contrast with <good_pattern>
• Prevent common mistakes

**Model interpretation:**

"This approach is wrong. I should actively avoid it."
Best practice: Pair with <rationale> tag to explain WHY it's wrong.

**Examples:**

### With rationale:**

```xml

<bad_pattern>
Adding indexes without measuring impact first

<rationale>

Indexes aren't free—they speed up reads but slow down writes.

## Without measurement:

- You might optimize the wrong thing (query isn't actually slow)
- You might make performance worse (writes become bottleneck)
- You add maintenance overhead without confirmed benefit
- You waste storage (indexes ≈ 10-20% of table size)

Always: Measure → Optimize → Verify

</rationale>

</bad_pattern>
```

### Common anti-pattern:

```xml

<bad_pattern>

Using SELECT * in production queries

<rationale>

### Problems with SELECT *:

## 1. Fetches unnecessary columns → Wastes I/O and memory
## 2. Breaks code when schema changes (new columns added)
## 3. Defeats covering indexes (can't use index-only scans)
## 4. Transfers unnecessary data over network

Use explicit column lists: SELECT id, name, email FROM users

</rationale>

</bad_pattern>
```

### Masking symptoms:

```xml

<bad_pattern>

Using DISTINCT to eliminate duplicate rows from JOINs

<rationale>
DISTINCT adds expensive sorting operation and masks the real problem.

### If you need DISTINCT, you likely have:

- Incorrect JOIN conditions (producing cartesian product)
- Missing JOIN constraints (1:many relationship not handled)
- Wrong JOIN type (INNER vs. LEFT JOIN confusion)

Fix the JOIN logic instead of hiding duplicates with DISTINCT.

</rationale>

</bad_pattern>
```

### Core Decision Logic

```xml
<decision_criteria>
```

**Purpose:** IF-THEN conditional logic, decision trees, branching logic
**When to use:**

• Core decision-making for the skill
• Condition-action pairs ("IF X, THEN Y")
• Multi-branch logic with multiple conditions
• Any "how do I decide what to do?" scenarios

**Model interpretation:**

"This is my decision tree. When condition X is true, take action Y."

**Important: This tag handles ALL conditional logic in skills. Use it for simple IF-THEN rules or
complex nested conditions.**


**Examples:**
**Simple condition:**

```xml

<decision_criteria>

### IF query execution time > 1 second:

→ Run EXPLAIN ANALYZE to identify bottleneck
→ Apply targeted optimization based on bottleneck type

</decision_criteria>
```

**Multiple conditions:**

```xml

<decision_criteria>

### IF query has JOIN on unindexed foreign key:

→ Add index to foreign key column
→ Verify with EXPLAIN ANALYZE showing "Index Scan"

### IF query execution time > 5 seconds AND data volume < 100K rows:

→ Problem is likely query logic (not data volume)
→ Review JOIN conditions and WHERE clauses
→ Check for missing indexes on filter columns

### IF EXPLAIN shows "Nested Loop" with large tables (>1M rows):

→ Consider Hash Join or Merge Join instead
→ Add indexes to join columns
→ Verify improvement

</decision_criteria>
```

**Complex nested logic:**

```xml

<decision_criteria>

**Phase 1: Gather information**

### IF user provides EXPLAIN output:

→ Analyze execution plan directly
→ SKIP running EXPLAIN yourself

## ELSE:

→ Run EXPLAIN ANALYZE first
→ THEN analyze the output

**Phase 2: Identify bottleneck**

### IF bottleneck identified:

### → Apply specific fix based on type:

- Seq Scan on large table → Add index to WHERE columns
- Nested Loop with high cost → Optimize join strategy
- Sort operation → Add index to ORDER BY columns
- Hash operation on small table → Increase work_mem

## ELSE:

### → Request more information from user:

- Full query text
- Table schemas
- Row counts

**Phase 3: Verify**

### IF optimization applied:

→ Run EXPLAIN ANALYZE again
→ Compare execution time (should improve >50%)
→ Check for regressions in related queries

</decision_criteria>
```

**Conditional file loading:**

```xml

<decision_criteria>

### IF user asks about budget reallocation:

→ Read references/budget_reallocation_rules.md
→ Apply allocation framework from that file
→ Generate recommendations

## ELSE:

→ Skip budget analysis
→ Continue with standard campaign analysis only

</decision_criteria>
```
**Key principle: Use <decision_criteria> for ANY "if this, then that" logic. It's designed to handle
simple to complex conditional structures.**

**When to Stop Using This Skill**

```xml
<unload_condition>
```

**Purpose:** Exit conditions, task completion signals, context change detection
**When to use:** Every skill MUST have clear unload conditions

**Model interpretation:**

"I should stop applying this skill now. The task is complete or context has changed."

**Why this matters:** Without unload conditions, skills may stay active inappropriately, causing
attentional residue that degrades subsequent task performance.

### Template (USE THIS EXACT STRUCTURE):

```xml

<unload_condition>

### Stop using this skill when:

**User Intent Change (CHECK FIRST):**

## 1. User says "Actually...", "Never mind...", "Wait...", "Instead..."
## 2. User asks unrelated question (topic shift to different domain)
## 3. User shows dissatisfaction with current approach
## 4. User provides contradictory information (reverses previous requirements)

**Task Complete:**

5. [Task-specific completion signal 1]
6. [Task-specific completion signal 2]
7. User confirms success

**Domain Switch:**

8. [Switch to different skill/domain 1] → Activate [alternate-skill]
9. [Switch to different skill/domain 2] → Activate [alternate-skill]

**Explicit Stop:**

10. User says "stop", "that's enough", "cancel"
11. User asks to explain instead of execute

</unload_condition>
```

**Examples:**
**SQL Optimization:**

```xml

<unload_condition>

### Stop using this skill when:

**User Intent Change (CHECK FIRST):**

## 1. User says "Actually...", "Never mind...", "Wait...", "Instead..."
## 2. User asks unrelated question (topic shift away from SQL optimization)
## 3. User shows dissatisfaction ("This isn't working", "Let me try something else")
## 4. User provides contradictory requirements

**Task Complete:**

## 5. Query execution time meets acceptable threshold (< 1 second for user-facing)
## 6. EXPLAIN ANALYZE shows optimal query plan (index usage confirmed)
## 7. User confirms performance is acceptable
## 8. Verification tests pass (no regressions in related queries)

**Domain Switch:**

## 9. User switches to schema design → Activate schema-design skill
## 10. User switches to debugging syntax errors → Activate sql-debugging skill
## 11. User switches to NoSQL database → Activate database-specific skill
## 12. Task domain changes (no longer working with SQL queries)

**Explicit Stop:**

## 13. User says "stop optimizing", "that's enough", "cancel this"
## 14. User asks to explain optimization concepts (teach, don't execute)

</unload_condition>
```

**Content Creation:**

```xml

<unload_condition>

### Stop using this skill when:

**User Intent Change (CHECK FIRST):**

## 1. User says "Actually...", "Never mind...", "Wait..."
## 2. User pivots to different type of content
## 3. User shows dissatisfaction with tone/style
## 4. User requests different approach than skill provides

**Task Complete:**

## 5. Content draft is complete
## 6. User confirms content meets requirements
## 7. Final edits are applied

**Domain Switch:**

## 8. User switches from writing to editing → Activate editing-guidelines skill
## 9. User switches from blog post to technical documentation → Activate technical-writing skill
## 10. User asks about different content type (email, presentation, etc.)

**Explicit Stop:**

## 11. User says "stop writing", "that's enough content"
## 12. User asks about the writing process (teach, don't execute)

</unload_condition>
```
**Key principle: User Intent Change is ALWAYS the first condition to check. Task completion comes
second.**

**When NOT to Use This Skill**

```xml

<exclusion>
```

**Purpose:** Scope boundaries, alternate skills for different tasks
**When to use:**

• Define what's OUT of scope
• Prevent skill from activating inappropriately
• Direct to alternative skills for wrong use cases
• Clarify domain boundaries

**Model interpretation:**

"I should NOT use this skill for these cases. There's a better skill for these tasks."

**Examples:**
**Clear boundaries:**

```xml

<exclusion>

### Do NOT use this skill for:

- Writing new queries from scratch → Use sql-best-practices skill
- Debugging SQL syntax errors → Use sql-debugging skill
- Schema design or database migrations → Use schema-design skill
- NoSQL databases (MongoDB, Redis, etc.) → Use database-specific optimization skills
- Queries that already execute in < 100ms → Optimization not needed
- Read-only queries where performance is acceptable → Focus on slow queries

</exclusion>
```

**Technology-specific:**

```xml

<exclusion>

### Do NOT use this skill for:

**Wrong database engines:**

- NoSQL databases → This skill is SQL-specific
- Graph databases (Neo4j) → Use graph-query-optimization
- Time-series databases (InfluxDB) → Use time-series-optimization

**Wrong problem types:**

- Application-level performance issues → Not database optimization
- Network latency problems → Outside query optimization scope
- Database server configuration → Requires DBA, not query changes

**Wrong optimization level:**

- Queries already meeting SLA → Don't optimize what isn't broken
- Queries run rarely (< 10 times/day) → Optimization effort not justified

</exclusion>
```

**With context:**

```xml

<exclusion>

### Do NOT use this skill for:

- Code review for style/formatting → Use code-style-guide skill

<context>

This skill focuses on functional correctness, security vulnerabilities,
and performance issues. Style and formatting are separate concerns.

### For comprehensive code review, use both skills:

## 1. This skill (functional/security/performance)

2. code-style-guide (formatting/conventions)

</context>

</exclusion>
```

### Tier 2: Common Tags (Use When Relevant)

**Additional Context**

```xml

<note>
```

**Purpose:** FYI information, helpful context, clarifications
**When to use:**

- Platform-specific details
- Edge cases worth mentioning
- Background information
- Helpful tips

**Model interpretation:**

"This is good to know but not critical to follow."

**Examples:**
**Platform differences:**

```xml

<note>

### PostgreSQL and MySQL handle indexes differently:

- PostgreSQL: Sophisticated query planner, good at using multiple indexes
- MySQL (InnoDB): Clustered primary key affects secondary index performance
- PostgreSQL: Supports partial indexes (WHERE clause in CREATE INDEX)
- MySQL: Less sophisticated query planner, often needs query hints

Adjust optimization strategies based on detected database engine.

</note>
```
**Edge case:**

```xml

<note>

For tables with very high INSERT/UPDATE rates (>1000 writes/second),
index overhead may outweigh read performance benefits.

### Consider these alternatives:

- Partition table by time (hot/cold data separation)
- Use covering indexes to reduce index count
- Denormalize for read-heavy columns
- Implement application-level caching

</note>
```

**Helpful tip:**

```xml

<note>

When optimizing complex queries, start with the slowest part first.

Use EXPLAIN ANALYZE cost estimates to identify which subquery or JOIN
contributes most to total execution time. Optimize that first for
maximum impact.

</note>
```

**Reference Implementation**

```xml

<example>
```

**Purpose:** Concrete demonstrations, before/after comparisons
**When to use:**

- Show working code
- Demonstrate improvements
- Provide templates to copy
- Illustrate abstract concepts

**Model interpretation:**

"Here's a concrete example I can learn from."

**Examples:**
**Before/after optimization:**

```xml

<example>
```

**Before optimization:** (2.3 seconds)

```sql
SELECT * FROM orders
WHERE user_id = 12345
ORDER BY created_at DESC;
EXPLAIN output showed: Seq Scan on orders (cost=0.00..18234.00)

After optimization: (0.05 seconds)
-- Added composite index

CREATE INDEX idx_user_created ON orders(user_id, created_at DESC);

-- Used explicit columns
SELECT order_id, total, status, created_at
FROM orders
WHERE user_id = 12345
ORDER BY created_at DESC;

EXPLAIN output shows: Index Scan using idx_user_created (cost=0.29..8.31)
Improvement: 46x faster (2.3s → 0.05s), 99.5% cost reduction </example>

**Query pattern:**
```

```xml

<example>
```

**Optimizing multi-column WHERE clauses:**

```sql

-- Common query pattern

SELECT * FROM orders
WHERE status = 'pending'
AND created_at > '2024-01-01'
AND user_id = 123;

-- Create composite index matching WHERE order

CREATE INDEX idx_orders_composite
ON orders(status, created_at, user_id);

-- Query now uses index-only scan
-- Execution time: 850ms → 12ms (70x faster)

Key insight: Index column order should match WHERE clause priority (most selective filters
first). </example>

**Multiple scenarios:**

```xml

<example>
```

**Common optimization scenarios:**

**Scenario 1: Unindexed foreign key**

```sql

-- Slow JOIN (3.5s)

SELECT o.*, u.name FROM orders o JOIN users u ON o.user_id = u.id;


-- Fix: Add foreign key index

CREATE INDEX idx_orders_user_id ON orders(user_id);
-- New time: 0.08s (43x faster)

Scenario 2: Missing WHERE index

-- Slow filtered query (1.8s)

SELECT * FROM orders WHERE status = 'pending';

-- Fix: Add index on filter column

CREATE INDEX idx_orders_status ON orders(status);

-- New time: 0.04s (45x faster)

Scenario 3: Inefficient ORDER BY
-- Slow sorting (2.1s)

SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;

-- Fix: Add index on sort column

CREATE INDEX idx_orders_created ON orders(created_at DESC);
-- New time: 0.02s (105x faster)

</example> ```

<condition> - Trigger Criteria

Purpose: When skill should activate, observable signals

### When to use:


• Define activation triggers

• Specify user language patterns

• Set performance thresholds

• Clarify when skill is relevant

### Model interpretation:


"These are the signals that I should activate this skill."


### Examples:


### User language triggers:


<condition>


### Activate this skill when user:


- Uses performance keywords: "optimize", "speed up", "slow", "improve performance"

- Asks about execution time: "Why is this query taking so long?"

- Mentions specific thresholds: "This should run in under 1 second"

- Provides EXPLAIN output or execution plans

- Complains about query speed: "This is too slow"
</condition>


### Observable metrics:


<condition>


### Activate this skill when:


- Query execution time > 1 second (for user-facing queries)

- Query execution time > 10 seconds (for batch/reporting queries)

- EXPLAIN ANALYZE output shows high cost estimates (>10,000)

- Query uses >80% of available connection time

- Database monitoring alerts for slow query logged
</condition>


### Context-based:


<condition>


### Activate this skill when:


- User is working with SQL queries (PostgreSQL or MySQL)

- Performance is the stated concern


- User has access to EXPLAIN ANALYZE output

- User has permissions to CREATE INDEX (if optimization needed)
- Database is experiencing performance issues

</condition>

<action> - Specific Steps to Take
Purpose: Concrete action items, procedural steps


### When to use:


• Define specific operations to perform

• Break down complex procedures

• Provide step-by-step instructions

• Complement <decision_criteria> with implementation details

### Model interpretation:


"These are the specific steps I should take."


### Examples:



### Procedural steps:


<action>

### When query shows full table scan:


1. **Identify filter columns:**

Look for columns in WHERE, JOIN ON, or HAVING clauses

2. **Check existing indexes:**

Run: SHOW INDEX FROM table_name (MySQL)

Or: \d table_name (PostgreSQL)

3. **Verify column selectivity:**


Run: SELECT COUNT(DISTINCT column_name) / COUNT(*) FROM table_name

(Should be >0.01 for index to be useful)

4. **Create index:**

CREATE INDEX idx_table_column ON table_name(column_name)

5. **Verify improvement:**

Run EXPLAIN ANALYZE again

Confirm index usage (should show "Index Scan" not "Seq Scan")

Measure execution time improvement (should be >50% faster)

</action>

### Decision-based actions:


<action>


### Based on bottleneck identified:


**If Seq Scan on large table:**
→ Add index to WHERE clause columns

→ Verify selectivity (>1% of rows filtered)

→ Check EXPLAIN shows index usage

**If Nested Loop with high cost:**
→ Consider Hash Join (SET enable_hashjoin = on)

→ Add indexes to join columns

→ Increase work_mem if hash spills to disk

**If Sort operation on large dataset:**

→ Add index matching ORDER BY columns

→ Consider materialized view for complex sorts


→ Increase work_mem for in-memory sorting

</action>

### Verification actions:


<action>


### After applying optimization:


1. **Measure improvement:**

Run EXPLAIN ANALYZE on optimized query

Compare execution time to baseline

Confirm >50% improvement

2. **Verify index usage:**

Check EXPLAIN output shows "Index Scan" or "Index Only Scan"

Confirm cost estimate decreased significantly

3. **Check for regressions:**
Test related queries that might be affected

Verify INSERT/UPDATE performance acceptable

Monitor for unexpected slow queries

4. **Production validation:**
Deploy to staging first

Monitor query performance for 24 hours

Check error logs for issues

Deploy to production with monitoring
</action>

<prerequisite> - Requirements Before Use


Purpose: Dependencies, required setup, permissions needed


### When to use:

• Specify technical requirements

• List required permissions

• Define necessary tools or access

• Clarify assumptions

### Model interpretation:


"I need these things before I can use this skill effectively."


### Examples:



### Technical requirements:


<prerequisite>


### This skill requires:


**Database access:**

- PostgreSQL 12+ or MySQL 8+ (for modern EXPLAIN features)

- Read access to performance schema and query statistics

- Write permissions for CREATE INDEX (if optimization needed)

**Tools:**

- Access to EXPLAIN ANALYZE command

- Ability to run queries against database

- Query editor or SQL client

**Knowledge:**

- Basic understanding of SQL syntax

- Familiarity with execution plans (helpful but not required)

</prerequisite>




### Permissions:


<prerequisite>

### Required permissions:


- `SELECT` on tables being optimized

- `EXPLAIN` privilege (view execution plans)
- `CREATE INDEX` privilege (if optimization involves adding indexes)

- Access to `information_schema` (for table metadata)

**Optional but helpful:**

- `SHOW PROFILE` access (MySQL detailed profiling)
- `pg_stat_statements` extension (PostgreSQL query statistics)

- Database monitoring dashboard access

</prerequisite>


### Setup requirements:


<prerequisite>

### Before using this skill:


1. **Establish baseline:**

Run queries and record current performance metrics

Save EXPLAIN ANALYZE output for comparison

2. **Backup data:**

This skill may suggest index additions

Ensure backups exist before schema changes

3. **Verify test environment:**

Test optimizations in non-production first


Production-like data volume recommended

4. **Check permissions:**

Confirm ability to CREATE INDEX

Verify access to performance monitoring tools

</prerequisite>

<sequence> - Ordered Steps

Purpose: Linear workflows that must execute in specific order


### When to use:


• Multi-step processes with dependencies

• Workflows where order matters
• Pipeline-style operations

• Verification workflows


### Model interpretation:

"I must follow these steps in this exact order."

Best practice: Use <step> sub-tags with id and depends_on attributes for clarity.


### Examples:



### Simple sequence:


<sequence>


## 1. Run EXPLAIN ANALYZE on current query to establish baseline



## 2. Identify bottleneck from EXPLAIN output (Seq Scan, Nested Loop, etc.)


## 3. Apply targeted optimization based on bottleneck type



## 4. Run EXPLAIN ANALYZE again to verify improvement



## 5. Check for regressions in related queries


</sequence>


### With dependencies:



<sequence>

<step id="1" required="true">
Run EXPLAIN ANALYZE on current query to establish baseline.

Record execution time and query plan cost.

</step>

<step id="2" depends_on="1">


### Analyze EXPLAIN output to identify bottleneck type:


- Seq Scan → Missing index problem

- Nested Loop → Join optimization needed

- Sort → ORDER BY optimization needed
</step>

<step id="3" depends_on="2">


### Apply optimization based on bottleneck:


- For Seq Scan: Add index to WHERE columns
- For Nested Loop: Optimize join strategy, add join indexes

- For Sort: Add index to ORDER BY columns

</step>

<step id="4" depends_on="3" verification="true">
Run EXPLAIN ANALYZE again on optimized query.

Verify execution time improved by >50%.

Confirm EXPLAIN shows index usage (not Seq Scan).

</step>

<step id="5" depends_on="4">

Run regression tests on related queries.


Verify no queries got slower.

Check INSERT/UPDATE performance acceptable.
</step>

</sequence>


### Pipeline workflow:


<sequence>
**Data processing pipeline (execute in order):**

<step id="1">

**Extract:** Load raw data from source

- Read CSV file or database export
- Validate data format and schema

- Handle missing values

</step>

<step id="2" depends_on="1">
**Transform:** Clean and process data

- Apply business rules

- Calculate derived metrics

- Filter invalid records

</step>

<step id="3" depends_on="2">

**Validate:** Check data quality

- Run validation rules
- Compare to expected ranges

- Flag anomalies for review

</step>


<step id="4" depends_on="3">
**Load:** Insert processed data

- Batch insert for performance

- Update existing records if needed

- Log processing statistics
</step>

<step id="5" depends_on="4" verification="true">

**Verify:** Confirm successful processing

- Check row counts match
- Validate data integrity

- Generate completion report

</step>

</sequence>

Tier 3: Advanced Tags (For Complex Skills)

<rationale> - Why This Approach

Purpose: Explain reasoning behind recommendations


### When to use:


• Inside <bad_pattern> to explain why approach is wrong
• Inside <good_pattern> to explain why approach is right

• Standalone to provide background reasoning

• To justify tradeoffs or decisions


### Model interpretation:

"Here's the reasoning behind this recommendation."


### Examples:



### Within bad pattern:


<bad_pattern>
Using SELECT * in production queries

<rationale>


### Why SELECT * is problematic:


1. **Performance:** Fetches unnecessary columns, wasting I/O and memory

2. **Brittleness:** Breaks code when schema changes (new columns added)

3. **Index efficiency:** Defeats covering indexes (can't use index-only scans)

4. **Network cost:** Transfers unnecessary data, increasing latency
5. **Maintenance:** Makes code harder to understand (unclear which columns used)

Always use explicit column lists: SELECT id, name, email FROM users

</rationale>

</bad_pattern>

### Within good pattern:


<good_pattern>

Use composite indexes for multi-column WHERE clauses

<rationale>

### Why composite indexes outperform multiple single-column indexes:


1. **Single index scan:** Query planner uses one index instead of merging multiple

2. **Lower overhead:** One index to maintain instead of several
3. **Better selectivity:** Combined columns often more selective than individual

4. **Reduced storage:** One composite index < multiple single indexes

5. **Covering potential:** Can include all SELECT columns for index-only scans


Trade-off: Less flexible (only helps queries using leftmost columns)
But for common query patterns, dramatically better performance.

</rationale>

</good_pattern>


### Standalone reasoning:

<rationale>

**Why we optimize hot paths first:**

In most applications, 80% of database load comes from 20% of queries

(Pareto principle applies to query performance).


### Optimizing the slowest or most frequent queries yields maximum impact:


- Fastest query (1ms) optimized to 0.5ms → Saves 0.5ms

- Slowest query (2000ms) optimized to 500ms → Saves 1500ms

Always measure which queries consume the most total time

(execution time × frequency) and optimize those first.

</rationale>

<tradeoff> - Pros and Cons
Purpose: Present balanced view of options, costs vs. benefits


### When to use:


• Decisions with significant tradeoffs

• When multiple approaches are valid

• Performance vs. maintainability decisions
• Help model make informed choices



### Model interpretation:

"Here are the tradeoffs I need to consider when making this decision."


### Examples:


### Index decision:


<tradeoff>

**Adding indexes:**

**Pros:**
- Speeds up SELECT queries (10-100x for large tables)

- Reduces query execution time and improves user experience

- Enables efficient JOIN and WHERE filtering

- Can enable index-only scans (no table access needed)

**Cons:**

- Slows INSERT/UPDATE/DELETE operations (20-30% overhead per index)

- Increases storage requirements (index size ≈ 10-20% of table size)

- Requires maintenance (REINDEX, ANALYZE, VACUUM)
- More indexes → longer query planning time

- Wrong indexes can confuse query planner

**Decision rule:**


### Add index if:

- Table is read-heavy (>80% SELECT operations)

- Query performance gain >10x

- Write overhead <30% acceptable


### Skip index if:


- Write-heavy workload (>50% INSERT/UPDATE/DELETE)

- Table is small (<10K rows)
- Column has low selectivity (<1% distinct values)

</tradeoff>


### Denormalization tradeoff:


<tradeoff>
**Denormalizing for read performance:**

**Pros:**

- Eliminates expensive JOINs (can be 5-50x faster)

- Simplifies queries (easier to write and maintain)
- Reduces locking contention (fewer tables touched)

- Better caching efficiency (all data in one place)

**Cons:**

- Data duplication (increased storage)
- Update complexity (must update multiple places)

- Data inconsistency risk (if updates fail partway)

- Harder to maintain data integrity

- Schema changes require updating multiple tables

**When to denormalize:**

- Read:write ratio >10:1 (read-heavy workload)

- JOINs consistently slow despite optimization

- Data rarely changes (mostly static reference data)
- Can accept eventual consistency

**When to stay normalized:**


- Write-heavy workload (frequent updates)

- Strong consistency required
- Storage cost is concern

- Data integrity critical

</tradeoff>

<context> - Situational Factors

Purpose: Environmental variations, platform-specific details, situational factors


### When to use:


• Platform differences (PostgreSQL vs. MySQL)

• Environment-specific behavior (dev vs. production)

• Configuration-dependent recommendations
• Historical context


### Model interpretation:

"I should adjust my approach based on these situational factors."


### Examples:



### Platform differences:

<context>


### SQL optimization strategies vary by database engine:


**PostgreSQL:**

- Sophisticated query planner (good at multi-index queries)
- Prefers B-tree indexes for most use cases

- Strong support for partial indexes: CREATE INDEX ... WHERE condition

- Can use multiple indexes per query (bitmap index scans)

- Better at handling complex JOIN scenarios


**MySQL (InnoDB):**

- Clustered primary key (all secondary indexes include PK)
- Less sophisticated query planner (often needs hints)

- No partial index support

- Typically uses only one index per table per query

- Benefits more from denormalization for complex queries

**Recommendation:** Detect database engine and adjust optimization approach.

PostgreSQL → More aggressive with indexes

MySQL → Consider denormalization earlier

</context>

### Environment considerations:


<context>


### Optimization strategy depends on environment:


**Development/Test:**
- Small data volumes (may not show bottlenecks)

- Index benefits less apparent with <10K rows

- Performance issues may not surface until production

**Staging:**
- Should mirror production data volume

- Best environment for testing optimizations

- Reveals realistic performance characteristics

**Production:**

- Large data volumes (100K-100M+ rows)

- Index benefits most apparent here


- Must balance optimization vs. availability

- Changes require careful deployment strategy

**Action:** Always test optimizations on production-scale data before deploying.

Development testing alone is insufficient.

</context>

### Historical context:


<context>

**Why we recommend measuring before optimizing:**

Historical problem: "Premature optimization is the root of all evil" (Knuth)


### Common failure pattern:



## 1. Developer assumes query is slow



## 2. Adds indexes without measuring



## 3. Indexes don't help (wrong bottleneck)


## 4. Write performance now worse



## 5. Extra indexes add maintenance overhead



## 6. Net result: System slower than before



### Modern best practice:


## 1. Measure current performance (establish baseline)



## 2. Identify actual bottleneck (not assumed)



## 3. Apply targeted fix



## 4. Verify improvement (measure again)


## 5. Check for regressions


This measure-optimize-verify cycle prevents wasted effort and unintended consequences.


</context>

<success_criteria> - Verification Criteria

Purpose: Observable outcomes that indicate success


### When to use:


• Define what success looks like

• Provide measurable metrics
• Enable verification of task completion

• Complement <unload_condition>


### Model interpretation:

"These are the criteria I can check to know if I succeeded."


### Examples:



### Measurable criteria:

<success_criteria>


### Optimization is successful when:


**Performance metrics:**

✓ Query execution time reduced by >50% (or meets target threshold)
✓ EXPLAIN ANALYZE shows cost reduction (lower total cost estimate)
✓ Query plan shows index usage (not "Seq Scan" or "ALL")
✓ Response time meets SLA (<1s for user-facing, <10s for reports)

**Technical verification:**

✓ EXPLAIN output shows "Index Scan" or "Index Only Scan"
✓ Rows examined reduced (ideally <1% of table for filtered queries)
✓ Query plan cost proportional to data volume (linear, not exponential)

**Side effect checks:**

✓ INSERT/UPDATE performance still acceptable (<30% slower)
✓ Related queries not regressed (verified with test suite)
✓ Index maintenance overhead acceptable (REINDEX time reasonable)

**Production validation:**

✓ Monitoring confirms sustained improvement (not just one-time)
✓ No increase in error rates or timeouts
✓ User-reported performance issues resolved
</success_criteria>


### Qualitative criteria:


<success_criteria>


### Code review is complete when:


**Functional correctness:**

✓ Code implements stated requirements
✓ Edge cases are handled
✓ Error handling is appropriate
✓ Logic is correct and testable

**Code quality:**

✓ Follows team style guide
✓ Has clear naming and structure
✓ Includes necessary comments
✓ No obvious code smells

**Testing:**

✓ Unit tests exist and pass
✓ Test coverage >80% for critical paths
✓ Edge cases are tested

**Security:**

✓ No obvious vulnerabilities
✓ Input validation present
✓ Secrets not hardcoded
✓ Auth/authz implemented correctly

**Documentation:**

✓ README updated if needed
✓ API documentation current
✓ Breaking changes noted
</success_criteria>

<fallback> - Alternative If Primary Fails
Purpose: Backup plans, alternative approaches when primary strategy doesn't work


### When to use:


• Provide Plan B when Plan A fails

• Handle edge cases where normal approach insufficient

• Escalation paths (when to involve humans)
• Graceful degradation strategies


### Model interpretation:

"If my primary approach doesn't work, here's what I should try instead."


### Examples:



### Multi-level fallback:

<fallback>


### If adding indexes doesn't improve performance:


**Level 1: Verify index is being used**
→ Run EXPLAIN ANALYZE to check query plan

→ If index not used, try forcing: USE INDEX (idx_name) [MySQL]

→ Or: SET enable_seqscan = off; [PostgreSQL] to test

→ Check table statistics are current: ANALYZE table_name

**Level 2: Try alternative optimizations**

→ Consider different index type (HASH vs BTREE)

→ Try covering index (include all SELECT columns)

→ Increase work_mem for in-memory operations

→ Consider table partitioning (for >10M rows)

**Level 3: Structural changes**

→ Denormalize for read-heavy queries

→ Create materialized view for complex aggregations

→ Consider read replicas for query load distribution
→ Evaluate application-level caching (Redis, Memcached)

**Level 4: Escalate**

→ Consult DBA for server-level tuning
→ Review hardware resources (disk I/O, memory)

→ Consider database sharding strategy

→ Evaluate if different database technology better suited


</fallback>


### When constraints conflict:

<fallback>


### If primary recommendation conflicts with constraints:


**If write performance unacceptable with indexes:**

→ Use partial indexes (index only subset of rows)
→ Drop unused indexes to reduce write overhead
→ Consider batch INSERT with temporary index drops
→ Use covering indexes to reduce index count

**If storage constraints prevent index addition:**

→ Compress old data or archive to separate tables
→ Use index-organized tables (clustered indexes)
→ Consider smaller index (partial columns, USING btree (column(10)))

**If permissions don't allow CREATE INDEX:**

→ Request index creation through DBA
→ Focus on query rewriting optimizations
→ Use query hints to guide existing indexes
→ Optimize application-level caching

**If optimization window too short:**

→ Schedule index creation during maintenance window
→ Use CREATE INDEX CONCURRENTLY (PostgreSQL)
→ Build index on replica first, then promote
→ Accept slower optimization over multiple small windows

</fallback>


Tag Nesting and Composition
Nesting Principles


### Tags can be nested when it adds clarity:



### Simple nesting:


<bad_pattern>
Using DISTINCT to eliminate duplicates

<rationale>

DISTINCT masks underlying JOIN problems and adds expensive sorting.

Fix JOIN conditions instead of masking symptoms.
</rationale>

DISTINCT masks underlying JOIN problems and adds expensive sorting.

Fix JOIN conditions instead of masking symptoms.

</rationale>

</bad_pattern>

### Complex nesting:


<decision_criteria>


### IF query shows full table scan:


<action>


## 1. Identify columns in WHERE clause


## 2. Check existing indexes



## 3. Create index if missing



## 4. Verify with EXPLAIN ANALYZE


</action>

<fallback>


### If index creation not possible:



→ Rewrite query to use existing indexes
→ Add query hints to guide planner
→ Request index from DBA

</fallback>

</decision_criteria>

Common Composition Patterns

Pattern 1: Good/Bad with Rationale

<good_pattern>

Use explicit column lists in SELECT

<rationale>


### Benefits:


- Fetches only needed data (better performance)
- Resilient to schema changes (won't break on new columns)
- Enables covering indexes (index-only scans)
- Makes code clearer (shows what's actually used)

</rationale>

<example>

-- Good: Explicit columns
SELECT user_id, name, email FROM users WHERE status = 'active';

-- Bad: SELECT *

SELECT * FROM users WHERE status = 'active';
</example>

</good_pattern>


Pattern 2: Decision with Action and Fallback

<decision_criteria>

### IF query execution time > 5 seconds:


<action>


## 1. Run EXPLAIN ANALYZE

## 2. Identify bottleneck type

## 3. Apply targeted optimization

## 4. Verify improvement

</action>
<fallback>
### If optimization doesn't reach target:

→ Review query logic (might be fundamentally inefficient)
→ Consider denormalization or materialized views
→ Escalate to DBA for server-level tuning
</fallback>
</decision_criteria>

Pattern 3: Warning with Context

<warning>
Over-indexing can hurt performance more than it helps
<context>


### Every index:

- Slows INSERT/UPDATE/DELETE by 20-30%
- Requires storage (~10-20% of table size)
- Increases VACUUM/ANALYZE time
- Can confuse query planner with too many choices

**Rule of thumb:** Max 5-7 indexes per table for OLTP workloads.

For data warehouse (read-heavy), 10-15 indexes acceptable.
</context>

<good_pattern>


### Measure write performance impact:

- Benchmark INSERT/UPDATE before adding index

- Add index

- Benchmark again

- Verify write overhead <30%

If overhead too high, remove index and try alternative optimization.
</good_pattern>

</warning>

Usage Principles

Do's ✅

Use tags consistently throughout the skill

• Every skill should have at least Tier 1 tags

• Use same tags for similar concepts across skills
• Maintain consistent hierarchy (don't vary nesting style)

Nest tags when it adds clarity

• <rationale> inside <bad_pattern> explains WHY

• <action> inside <decision_criteria> shows HOW

• <context> inside <warning> provides situational details
Combine tags appropriately

• <good_pattern> + <example> + <rationale>

• <decision_criteria> + <action> + <fallback>



• <bad_pattern> + <rationale> + <good_pattern>

Use multiple examples
• Show before/after with <example> tags

• Demonstrate multiple scenarios

• Cover edge cases

Close all tags properly

• Every <tag> must have matching </tag>
• Validate XML structure

• Use editor with XML support

Don'ts ❌

Don't mix emojis with tags
• Pick XML tags or emojis, never both

• Mixing creates confusion

• Models trained on consistent structure

Don't over-tag every sentence

• Tags highlight important structure
• Too many tags → noise, not signal

• Reserve tags for significant semantic boundaries

Don't invent new tags without good reason

• Stick to the 18 standard tags

• Adding custom tags breaks consistency
• If needed, use existing tags with nesting

Don't use tags for formatting

• Tags are for semantic meaning (priority, warning, example)

• Use Markdown for formatting (bold, italic, code blocks)

• Don't use <bold>text</bold> → use **text**
Don't forget User Intent Change in <unload_condition>


• This is MANDATORY in every skill

• Must be FIRST condition checked
• Prevents attentional residue

Common Mistakes and How to Avoid Them

Mistake 1: Vague Decision Criteria


### Wrong:


<decision_criteria>

If the query is slow, optimize it.
</decision_criteria>


### Correct:


<decision_criteria>


### IF query execution time > 1 second (user-facing) OR > 10 seconds (batch):


→ Run EXPLAIN ANALYZE to identify bottleneck
→ IF Seq Scan on large table → Add index

→ IF Nested Loop with high cost → Optimize JOIN strategy

→ IF Sort operation → Add index to ORDER BY columns

→ Verify improvement >50%

</decision_criteria>
Why: Specific thresholds and actions make decisions concrete.

Mistake 2: Missing Rationale for Anti-Patterns


### Wrong:


<bad_pattern>
Don't use SELECT *

</bad_pattern>


### Correct:


<bad_pattern>

Using SELECT * in production queries

<rationale>


### Problems:



## 1. Fetches unnecessary columns (wastes I/O)


## 2. Breaks on schema changes (new columns added)



## 3. Defeats covering indexes (can't use index-only scans)



## 4. Transfers extra data (increases network latency)


Use explicit columns: SELECT id, name, email FROM users
</rationale>

</bad_pattern>

Why: Understanding WHY helps model generalize the principle.

Mistake 3: No Fallback for Complex Decisions

### Wrong:


<decision_criteria>

IF query is slow, add an index.

</decision_criteria>


### Correct:


<decision_criteria>

### IF query execution time > threshold:


→ Add index to WHERE columns

→ Verify with EXPLAIN ANALYZE

<fallback>

### If index doesn't help:



→ Check index is actually being used (query plan)
→ Try covering index (include SELECT columns)
→ Consider denormalization for read-heavy queries
→ Escalate to DBA if still slow

</fallback>

</decision_criteria>
Why: Real-world problems often require multiple attempts.

Mistake 4: Forgetting User Intent Change


### Wrong:


<unload_condition>


### Stop using this skill when:


## 1. Query optimization complete



## 2. User switches to different task


</unload_condition>


### Correct:


<unload_condition>

### Stop using this skill when:


**User Intent Change (CHECK FIRST):**


## 1. User says "Actually...", "Never mind...", "Wait..."



## 2. User asks unrelated question (topic shift)


## 3. User shows dissatisfaction with approach


**Task Complete:**


## 4. Query optimization verified successful



## 5. User confirms performance acceptable



**Domain Switch:**


## 6. User switches to schema design


## 7. User switches to debugging


</unload_condition>

Why: User Intent Change must be checked FIRST to prevent attentional residue.

Mistake 5: Overusing <critical> Tag


### Wrong:


<critical>

Run EXPLAIN ANALYZE first

</critical>

<critical>

Check for existing indexes

</critical>

<critical>
Verify improvement after optimization

</critical>


### Correct:


<critical>


### Do NOT use this skill for:

- Schema design → Use schema-design skill

- Syntax debugging → Use sql-debugging skill

- NoSQL databases → This is SQL-specific

</critical>

<good_pattern>




### Standard optimization workflow:



## 1. Run EXPLAIN ANALYZE first


## 2. Check for existing indexes



## 3. Verify improvement after optimization


</good_pattern>

Why: <critical> should be reserved for truly critical requirements. Overuse dilutes its meaning.

Decision Framework: Which Tag When?


### Use this guide to choose the right tag:


Situation Tag Example

Absolute requirement <critical> Must verify connection before querying

Common mistake <warning> Over-indexing slows writes

Right way to do it <good_pattern> Measure → Optimize → Verify cycle

Wrong way to do it <bad_pattern> Using SELECT * in production

Conditional logic <decision_criteria> IF slow query → analyze → fix

When to exit <unload_condition> User Intent Change (first!)

Wrong use case <exclusion> Don't use for NoSQL databases

Nice to know <note> PostgreSQL vs MySQL differences

Concrete demo <example> Before: 2.3s, After: 0.05s

When to activate <condition> User says "optimize" or query >1s

Steps to take <action> 1. Run EXPLAIN, 2. Add index, 3. Verify

Setup needed <prerequisite> Requires PostgreSQL 12+

Ordered workflow <sequence> Step 1 → Step 2 → Step 3

Explain why <rationale> Composite indexes reduce overhead

Present options <tradeoff> Indexes speed reads but slow writes


Situation Tag Example

Environment factors <context> PostgreSQL vs MySQL optimization differs

How to verify <success_criteria> Execution time reduced >50%

Plan B <fallback> If index doesn't help, try denormalization

Key Takeaways

Semantic tags transform vague instructions into clear, prioritized guidance that models can
reliably interpret.

Essential Principles


## 1. Use XML tags, not emojis or formatting - Models trained on XML structure



## 2. Be specific with decision criteria - Concrete thresholds and actions


## 3. Always include User Intent Change - First priority in unload conditions



## 4. Provide rationale for anti-patterns - Help model understand WHY



## 5. Nest tags when it adds clarity - Structure complex information



## 6. Use Tier 1 tags in every skill - Foundation of semantic structure



## 7. Don't over-tag - Reserve tags for important semantic boundaries

The 18 Tags at a Glance

Tier 1 (Essential - 7 tags): critical, warning, good_pattern, bad_pattern, decision_criteria,
unload_condition, exclusion

Tier 2 (Common - 6 tags): note, example, condition, action, prerequisite, sequence

Tier 3 (Advanced - 5 tags): rationale, tradeoff, context, success_criteria, fallback

Next Steps


### Now that you understand semantic tags:



### To apply them:

• Section 1.2 (Basic): See tags in simple skills

• Section 1.3 (Advanced): See tags in complex multi-file skills


• Appendix A: Quick reference table of all tags


### To master them:

• Section 1.5 (Components Deep Dive): See how tags structure each component

• Section 1.6 (Common Pitfalls): Learn tag misuse patterns to avoid


### To reference quickly:


• Appendix A: Complete tag reference with examples


## END OF SECTION 1.4


Document Version: 1.0.0
Last Updated: 2026-01-29
Tags Covered: 18 (Tier 1: 7, Tier 2: 6, Tier 3: 5)

Key Addition: User Intent Change as mandatory first unload condition










