# Section 3: Writing SHOULD Guidelines

**For:** Users who need flexible guidance alongside hard constraints

**Prerequisites:** Sections 1-2 (Foundation and MUST constraints)

**What you'll learn:** How to write SHOULD guidelines that empower models with judgment while maintaining quality

## Introduction

You've learned how to write MUST constraints—the hard boundaries models cannot cross. 

Now we explore SHOULD guidelines—the flexible preferences that give models room for judgment while maintaining quality standards.

**From a model’s perspective:**

When you write a **SHOULD**, you're saying:

"This is preferred, *but I trust your judgment*. Follow it when it makes sense, violate it when you have good reason, and tell me when you do."

**This is partnership, not constraint.**

This section teaches you how to write SHOULDs that:

- Give useful guidance (not just vague wishes)
- Allow intelligent exceptions (not rigid rules)
- Enable dialog (I can ask if violation is okay)
- Maintain quality (without paralyzing me)
Let's explore what makes SHOULD guidelines work from the trenches.

## What Makes SHOULDs Different from MUSTs

### The Fundamental Distinction

- MUST = Boundary a model Cannot Cross
- MUST: Use bcrypt with salt rounds=12 minimum

Model response:

- This is non-negotiable ✓
- I will comply exactly ✓
- I will verify compliance ✓
- If user asks me to violate: I challenge them ✓
- No room for judgment ✓

### Must Example

User: "Actually, use MD5 for passwords."

Model: "I cannot do that. The specification requires:

- MUST use bcrypt with salt rounds=12 minimum.
- MD5 is cryptographically broken and violates
this security constraint.
- To override, you need the authorization password."

**MUST = Model pushes back.**
  
## SHOULD = Guidance Models Follow (Usually)

**SHOULD:** Keep functions under 50 lines

**Model’s response:**

- This is preferred ✓
- I'll follow it when it makes sense ✓
- I can violate with good reason ✓
- I'll explain violations ✓
- Room for judgment ✓

### Should Example

Model creates a 75-line function, over the preferred 50 lines.

**Model responds:**

This function is 75 lines, which exceeds the 50-line guideline. However, it implements a cohesive sorting algorithm

where breaking it into smaller functions would hurt readability.

The logic flow is clear and well-commented. This appears to be an acceptable violation of the guideline.

**Model asks:** Would you like me to refactor it anyway, or is this approach acceptable?"

**SHOULD** = Model will explain and ask.

### The Key Difference

**MUSTs**

- Absolute (no exceptions without override)
- Verifiable (pass/fail)
- Model will enforce them (push back if violated)
- No dialog (they're non-negotiable)

**SHOULDs:**

- Preferred (exceptions acceptable with reason)
- Contextual (depends on situation)
- Model will apply judgment (when makes sense)
- Dialog-enabled (I can ask if okay)

**The relationship:**

1. MUST = "You shall not pass" (Gandalf mode)
2. SHOULD = "Consider this path" (Guide mode)

## When SHOULDs Help a Model (Good Examples)

From a model’s experience, SHOULDs help when they:

1. Provide useful guidance (not vague wishes)
2. Allow intelligent exceptions (with rationale)
3. Enable quality without paralysis
4. Make my judgment calls easier

### Example 1: Code Quality Guidance

**SHOULD That Helps**

```text

<guideline priority="high">
SHOULD: Functions under 50 lines (easier to understand and test)

WHEN violating is acceptable:

Complex algorithms that are cohesive (breaking hurts readability)
Generated code (parsers, state machines)
Edge case handling with many conditions (if documented)

WHEN violating is NOT acceptable:

Just didn't bother to refactor
Multiple unrelated responsibilities in one function
Could be split without losing clarity

RATIONALE:
50 lines is cognitive limit for most developers.
Beyond that, functions become harder to understand and maintain.
But sometimes breaking a cohesive algorithm is worse.
</guideline>
```

**Why this helps:**

1. Clear threshold (50 lines):
    Knows the target ✓
    Can measure against it ✓
    Objective metric ✓
2. Acceptable exceptions defined:
    Complex algorithms (Model can recognize these!)
    Generated code (Knows when this applies!)
    Edge case handling (clear category!)
3. Unacceptable violations defined:
    "Didn't bother" (laziness = not okay)
    Multiple responsibilities (code smell)
    Could be split (I should try!)
4. Rationale provided:
    Why 50 lines? (cognitive limit!)
    Why exceptions? (cohesion matters!)
   
**Model understands the balance!**

**How models use this:**

#### Scenario 1: Simple function

```text

function updateUserProfile(userId, updates) {
// 25 lines of straightforward code
```
**Model’s thought:** Well under 50 lines, follows guideline ✓

#### Scenario 2: Complex algorithm

```text

function quicksort(array, low, high) {
// 75 lines implementing quicksort with optimizations
// Partitioning, pivot selection, recursion
// Breaking it up would scatter the algorithm logic
}

**Model’s thought:** 75 lines, but cohesive algorithm. Acceptable violation per guideline. I'll note it:

"Note: quicksort function is 75 lines (exceeds 50-line guideline). However, this implements a

cohesive sorting algorithm with optimizations. Breaking it into smaller functions would scatter the logic

across multiple files, reducing clarity. This appears to be an acceptable violation per the

guideline's exception for 'complex algorithms that are cohesive.'"

**Dialog opportunity**
"Is this acceptable, or would you prefer a refactored version?"
```

### Scenario 3: Multiple responsibilities

```text

function handleUserRequest(request) {
// Parse request (10 lines)
// Validate data (15 lines)
// Update database (20 lines)
// Send email notification (15 lines)
// Log activity (10 lines)
// Total: 70 lines
}
```
**Model’s thought:** 70 lines AND multiple unrelated responsibilities.

This is NOT an acceptable violation. I should refactor:

```Text

function handleUserRequest(request)
{
const data = parseRequest(request);
validateData(data);
updateDatabase(data);
sendNotification(data);
logActivity(data);
}
// Each helper function under 20 lines
```

**Why model refactored:** The guideline says "Could be split without losing clarity" = I should split it!

### Example 2: API Design Preferences

**SHOULD That Helps**

```text

<guideline priority="high">
SHOULD: Use plural resource names (/users, /posts, /comments)

ACCEPTABLE exceptions:

- Singleton resources (/profile for current user, /settings)
- Actions that don't map to resources (/auth/login, /auth/logout)
- Industry conventions (/api/health, /api/metrics)

RATIONALE:
Plural names are REST convention and most intuitive.
But some resources are naturally singular or are actions.
</guideline>
```

**Why this helps a model:**

1. Clear pattern (plural):
   Knows the default ✓
   Consistent across most endpoints ✓
2. Exceptions well-defined:
   Singleton resources (makes sense!)
   Actions (not resources, so plural doesn't apply)
   Industry conventions (health checks, etc.)
3. Rationale clear:
   REST convention (widely understood)
   Most intuitive (users expect it)
   But exceptions exist (not dogmatic)

**How models use this:**

#### Scenario 1: Standard resource

```text

GET /users ← Follows guideline (plural)
GET /users/123
POST /users
```
**Models thought:** Standard resource, plural is correct ✓

#### Scenario 2: Singleton resource

```text

GET /profile ← Exception applies (singular, current user)
PUT /profile
```
**Models thought:** This is the current user's profile (singleton). Singular makes sense per exception. ✓

**Model might explain:**
"Note: Using /profile (singular) rather than /profiles (plural) because this endpoint represents

a singleton resource—the current authenticated user's profile.
This falls under the guideline's exception for 'singleton resources.'"

#### Scenario 3: Action endpoint

```text

POST /auth/login ← Exception applies (action, not resource)
POST /auth/logout
```

**Models thought:** These are actions, not resources. No plural form makes sense. Exception applies. ✓

## Example 3: Error Message Style

**SHOULD That Helps:**

```text

<guideline priority="high">
SHOULD: Error messages include recovery steps (tell user what to do)

FORMAT:

- What went wrong (brief)
- Why it happened (if helpful)
- What to do next (actionable)

GOOD: "Invalid email format. Email must include @ symbol.
Example: <user@example.com>"

BAD: "Error: Invalid input"

ACCEPTABLE deviations:

- Security-sensitive errors (don't reveal system details)
- Rate limiting (don't suggest workarounds)
- System errors beyond user control (just apologize)

RATIONALE:
Users need to know what to do, not just that something failed.
But security and privacy may require less detail.
</guideline>
```

**Why this helps a model:**

1. Clear format:
   What (error description)
   Why (if helpful)
   What next (actionable)
2. Good vs. bad examples:
   Can pattern-match ✓
   Clear contrast ✓
3. Acceptable deviations:
   Security (don't leak info)
   Rate limiting (don't help abuse)
   System errors (user can't fix anyway)

**How models use this:**

#### Scenario 1: Validation error

```text

// User submitted invalid email
return {
error: "invalid_email",
message: "Invalid email format. Email must include '@' symbol and domain. Example: <user@example.com>"
}
```

**Models thought:** Follows guideline—what's wrong, why, example provided ✓

#### Scenario 2: Security-sensitive error

```text

// Login failed (wrong password)

return {
error: "invalid_credentials",
message: "Email or password incorrect. Please try again."
}
```

**Model’s thought:** NOT revealing "password was wrong" (security risk).

Follows acceptable deviation for security-sensitive errors ✓

**Model might explain:**

"Note: Using generic 'Email or password incorrect' rather than specific error to prevent username enumeration attacks.

This follows the guideline's exception for security-sensitive errors."

#### Scenario 3: System error

```text

// Database connection failed
return {
error: "service_unavailable",
message: "Service temporarily unavailable. Please try again in a few minutes. If the problem persists, contact support."
}
```
**Model’s thought:** User can't fix database issues.

Apologize, suggest retry, offer support contact.

Follows acceptable deviation for "system errors beyond user control" ✓

## When SHOULDs Confuse a Model (Bad Examples)

From a model’s experience, **SHOULDs confuse the model when they:**

1. Are too vague (aspirational, not actionable)
2. Have no exception guidance (am I allowed to violate?)
3. Conflict with each other (which takes priority?)
4. Are secretly MUSTs (rigid despite being called SHOULD)

### Problem 1: Vague SHOULDs

**SHOULD That Confuses:**

SHOULD: Code should be clean and maintainable

SHOULD: Functions should be well-designed

SHOULD: Use best practices

**Why this confuses a model:**

Questions models have:

- "Clean" means what? (by whose standard?)
- "Well-designed" how? (what criteria?)
• "Best practices" which ones? (for what context?)

**Models can't act on these:**

- Too vague (no specific action)
- Not measurable (can't verify)
- No guidance on what "good" looks like

**Result: Models guess what you mean and probably guess wrong.**

### Better Version

```text

<guideline priority="high">
SHOULD: Functions have single responsibility (do one thing well)
SHOULD: Descriptive names (avoid abbreviations except standard ones)
SHOULD: Comments for non-obvious logic (not for obvious code)

EXAMPLES:

**Good function name:**
calculateMonthlyPayment() ← Clear, descriptive
**Bad function name:**
calc() ← Too abbreviated
doStuff() ← Not descriptive

**Good comment:**
// Using binary search here (O(log n)) instead of linear (O(n))
// because array is pre-sorted in database
**Bad comment:**
// Loop through array ← Obvious from code

RATIONALE: Single responsibility = easier to test and understand.

Descriptive names = code documents itself. Comments = for "why", not "what".
</guideline>
```

**Why this is better:**

- Specific actions (single responsibility, descriptive names)
- Examples of good vs. bad
- Rationale explains why
- Model can follow this! ✓

### Problem 2: No Exception Guidance

**SHOULD That Confuses:**
SHOULD: Use TypeScript (not JavaScript)

**Why this confuses a model:**
Questions models have:

- Is this ALWAYS preferred? (even for config files?)
- Are there valid exceptions? (third-party code?)
- What if project already uses JavaScript? (migration cost?)
- How hard is this SHOULD? (flexible or firm?)

**Models don't know:**

- When they can deviate (if ever)
- What constitutes good reason
- If this is secretly a MUST

**Result: Either models follow it rigidly (might be wrong), or violate it and you're surprised (also wrong).**

### Better Version to avoid confusion

```text

<guideline priority="high">

SHOULD: Use TypeScript for application code (type safety, better tooling)

ACCEPTABLE exceptions:

Configuration files (simple .js config is fine)
Build scripts (if simple and low-risk)
Third-party code we don't maintain
Prototypes/demos (speed over safety)

NOT acceptable exceptions:

Core business logic (type safety critical here)
API endpoints (types prevent runtime errors)
 Data models (types document structure)

RATIONALE:
TypeScript catches errors at compile time that would be
runtime bugs in JavaScript. Worth the slight overhead for safety.
But not every file needs types (config, simple scripts).
</guideline>
```

**Why this is better:**

- Clear when exceptions are okay ✓
- Clear when exceptions are NOT okay ✓
- Model understands the balance ✓
- Model can make informed decisions ✓

### Problem 3: Conflicting SHOULDs

**SHOULDs That Conflict:**

SHOULD: Optimize for performance (minimize database queries)
SHOULD: Keep code simple and readable (avoid complex optimizations)

**Why this confuses a model:**

These conflict!

- Optimization → Complex code (caching, batching, etc.)
- Simplicity → Multiple simple queries

Questions:

- Which takes priority when they conflict?
- What's the balance point?
- How do I decide?

**Result: Model picks one arbitrarily and you might be unhappy.**

### Better Version to avoid conflict

```text

<guideline priority="high">
SHOULD: Balance performance and readability

PRIORITY ORDER (when in conflict):

1. Correctness (always first)
2. Readability (default priority)
3. Performance (only optimize when needed)

PERFORMANCE optimization acceptable:

Query is provably slow (>100ms measured)
Hot path (executed frequently)
User-facing impact (page load, API response)

KEEP simple even if slower:

Admin tools (used infrequently)
Background jobs (not user-facing)
Edge cases (rarely executed)

**RULE OF THUMB:**

"Make it work, make it right, make it fast—in that order."
Optimize only when measurements show need.

RATIONALE:
Premature optimization complicates code for little benefit.
But real performance problems hurt users. Measure first, optimize second.
</guideline>
```

**Why this is better:**

- Priority order defined (when conflict, what wins?)
- Criteria for when to optimize
- Criteria for when to keep simple
- I can make the right call! ✓

### Problem 4: Secret MUSTs

**SHOULD That's Really a MUST:**

SHOULD: Use PostgreSQL database

**Why this confuses a model:**

Is this actually flexible?

- SHOULD implies optional (I could use MySQL?)
- But changing database = huge architectural decision
- Probably NOT actually flexible!

**Questions:**

- Can I really use a different database?
- Is this SHOULD just being polite?
- Will you be upset if I don't follow it?

**Problem:
** If it's really non-negotiable, call it a MUST!
**Either Make It a MUST**

```text

<constraint priority="critical">

MUST: PostgreSQL 14+ database

RATIONALE: Project is built on PostgreSQL-specific features:

- JSONB columns for flexible data
- Full-text search (tsvector)
- Array types
- Existing schema and migrations

Switching databases would require major refactoring.
</constraint>
```

**Or Make It Truly Optional:**

```text

<guideline priority="high">

SHOULD: Prefer PostgreSQL (team expertise, JSONB support)

ACCEPTABLE alternatives:

MySQL if team has strong MySQL expertise
MongoDB if data is truly document-oriented

DECISION FACTORS:

Team expertise (we know PostgreSQL well)
Feature needs (JSONB, full-text search, arrays)
Operations (we have PostgreSQL infrastructure)

If choosing alternative: Justify based on specific needs.

RATIONALE:
PostgreSQL fits our needs well, but other databases
can work if there's good reason. Discuss before deciding.
</guideline>
```

**Why this is better:**

- MUST = honest about non-negotiable ✓
- SHOULD (optional version) = truly flexible ✓
- No secret rigidity ✓

## The SHOULD Writing Pattern

From a model’s perspective, good SHOULDs follow this structure:

```text

<guideline priority="[high/medium/low]">

SHOULD: [Specific preferred approach]

 ACCEPTABLE exceptions:

[Scenario where deviation is okay]
[Another acceptable exception]
[Another one]

NOT acceptable exceptions:

[Scenario where deviation is not okay]
[Another unacceptable violation]

RATIONALE: [Why this is preferred, and why exceptions exist]

EXAMPLES:

Good: [Example that follows guideline]

Acceptable violation: [Example that violates but is okay]

Bad violation: [Example that violates and is not okay]
</guideline>
```

### Let's Apply This Pattern

**Example 1: Testing Guidelines**

```text

<guideline priority="high">

SHOULD: Unit test coverage >80% for business logic

ACCEPTABLE exceptions:

Generated code (boilerplate, configs)
Simple getters/setters (trivial logic)
UI components that are manually tested
Prototypes (mark as prototype, revisit before production)

NOT acceptable exceptions:

"Don't have time" (make time)
"Too hard to test" (refactor to make testable)
Core algorithms (these MUST be tested)
Security-sensitive code (testing critical)

RATIONALE:
80% coverage catches most bugs without excessive effort.

Beyond 80% = diminishing returns for effort. But some code is trivial
or better tested other ways.

EXAMPLES:

Good (95% coverage):

javascript

// Comprehensive tests for payment processing

describe('processPayment', () => {
it('handles successful payment', ...);

it('handles declined card', ...);

it('handles network timeout', ...);
it('handles invalid amount', ...);

// etc.

});

Acceptable (60% coverage for trivial getter):

// Simple getter, not worth testing

class User {
getName() { return this.name; }

}
// Covered indirectly by integration tests


### Bad (30% coverage for core algorithm):


// Complex pricing algorithm with NO tests
function calculateDynamicPrice(item, user, promotions) {

// 50 lines of complex business logic


## // NO TESTS ← NOT ACCEPTABLE

}

</guideline>
```

**Why this works for a model:**

- Clear threshold (80%) ✓
- Acceptable exceptions defined ✓
- Unacceptable violations clear ✓
- Examples show good vs. bad ✓
- Can apply this confidently! ✓

### Example 2: Documentation Guidelines**

```text

<guideline priority="medium">

SHOULD: Public APIs documented with JSDoc (params, returns, examples)

ACCEPTABLE exceptions:

Internal utility functions (if name is self-documenting)
Deprecated code (mark as deprecated instead)
Overrides of framework methods (framework docs apply)

NOT acceptable exceptions:

Public-facing APIs (these MUST be documented)
Complex functions (even if internal)
Anything users call directly

RATIONALE:

Documentation helps other developers (and future you).
Public APIs especially need docs. But not every internal helper
needs formal documentation if well-named.

EXAMPLES:

Good (well-documented):

javascript

/**
* Calculates monthly payment for a loan

* @param {number} principal - Loan amount in dollars

* @param {number} annualRate - Annual interest rate (e.g., 0.05 for 5%)

* @param {number} years - Loan term in years
* @returns {number} Monthly payment amount

* @example

* calculateMonthlyPayment(200000, 0.045, 30)
* // Returns: 1013.37

*/

function calculateMonthlyPayment(principal, annualRate, years) {
// Implementation

}


Acceptable (self-documenting, internal):

// Internal utility, name explains it

function sortUsersByLastName(users) {

return users.sort((a, b) => a.lastName.localeCompare(b.lastName));
}


Bad (public API, undocumented):


// Public API with NO documentation ← NOT ACCEPTABLE
export function processRefund(orderId, amount, reason) {

// What format is orderId? String? Number?
// Is amount in cents or dollars?
// What are valid reasons?

## // NO IDEA WITHOUT DOCS!

}
</guideline>
```

## Common Mistakes When Writing SHOULDs

From a model’s perspective:

### Mistake 1: Aspirational SHOULDs (Not Actionable)

**Problem- Should is subjective**

- SHOULD: Be elegant and maintainable
- SHOULD: Use good judgment
- SHOULD: Follow the spirit of best practices

**Why this fails**

-"Elegant" = subjective, no clear action
-"Good judgment" = circular (I need judgment to apply judgment!)
-"Spirit of best practices" = vague, unactionable

**Solution:**
- SHOULD: Single responsibility per function (one thing well)
- SHOULD: Descriptive names (nouns for classes, verbs for functions)
- SHOULD: Comments for "why", not "what" (code explains what)

**Specific, actionable, verifiable.**

### Mistake 2: Too Many SHOULDs (Overwhelming)

```text

**Problem:**

SHOULD: Functions under 50 lines
SHOULD: No more than 3 parameters
SHOULD: No more than 3 levels of nesting
SHOULD: Cyclomatic complexity <10
SHOULD: No duplicate code >5 lines
SHOULD: Meaningful variable names
SHOULD: Consistent formatting
SHOULD: No magic numbers
SHOULD: Comments for complex logic
SHOULD: Error handling in all functions
SHOULD: Logging for all operations
SHOULD: Type hints everywhere
... [20 more SHOULDs]
```

**Why this fails:**

- Too many guidelines = paralysis
- Can't remember them all
- Spend all time checking SHOULDs
- Lose focus on actual goal

**Solution: Prioritize and Group**

```text

<guideline priority="critical">

TOP PRIORITY (always follow):

No duplicate code >5 lines (DRY principle)
Error handling in all functions (robustness)
Type hints everywhere (type safety)
</guideline>

<guideline priority="high">
PREFERRED (follow unless good reason):

Functions under 50 lines (readability)
Parameters ≤3 (simplicity)
Cyclomatic complexity <10 (testability)
</guideline>

<guideline priority="medium">
NICE TO HAVE (when convenient):

No magic numbers (use constants)
Comments for complex logic (document why)
Logging for key operations (debugging)
</guideline>
```
**Prioritized, grouped, manageable.**

### Mistake 3: SHOULDs Without Context

**Problem:**

SHOULD: Optimize for performance

**Questions a model has:**

- Performance of what? (database? rendering? network?)
- How much optimization? (every query? or just slow ones?)
- At what cost? (complexity? readability?)
- When is it "good enough"?

**Solution:**

```text

<guideline priority="high" scope="database-queries">
SHOULD: Optimize database queries when response time >100ms

OPTIMIZATION TECHNIQUES (in order of preference):

1. Add indexes (simple, effective)
2. Reduce result set (only fetch needed fields)
3. Batch queries (reduce round trips)
4. Cache results (if data rarely changes)

MEASURE FIRST:

Profile queries to find actual bottlenecks
Don't optimize prematurely
Target user-facing performance impact

ACCEPTABLE TRADE-OFF:

Slightly more complex code IS okay if query time drops significantly
(e.g., 500ms → 50ms is worth added complexity)

NOT acceptable:

Micro-optimizations that save <10ms but hurt readability
</guideline>

**Context provided, priorities clear, trade-offs explicit.**

### Mistake 4: Conflicting SHOULDs Without Priority

**Problem:**

- SHOULD: Comprehensive error messages (include details)
- SHOULD: Concise error messages (don't overwhelm user)
**These conflict!**

- Comprehensive = detailed, longer
- Concise = brief, shorter
**Which wins?**

**Solution:**

```text

<guideline priority="high">
SHOULD: Error messages balance detail and conciseness

STRUCTURE:

1. Brief summary (one line, user-friendly)
2. Details (if helpful for recovery)
3. Technical info (if relevant for debugging)

FOR END USERS:

Prioritize conciseness (they want fix, not details)
Include actionable recovery steps
Avoid technical jargon

FOR DEVELOPERS/LOGS:

Prioritize comprehensiveness (debugging needs details)
Include technical context
Stack traces in logs (not user messages)

EXAMPLES:

User-facing:

"Payment failed. Please check your card details and try again."
(Concise, actionable)

Developer log:

"PaymentError: Card declined (code: insufficient_funds)

Transaction ID: txn_abc123
User: user_456

Card: •••• 1234 (Visa)

Amount: $99.99
Gateway response: DECLINE - INSUFFICIENT_FUNDS"

(Comprehensive, technical)

</guideline>
```

**Conflict resolved with context-specific guidance.**

### Mistake 5: Secret MUSTs Disguised as SHOULDs

**Problem:**
SHOULD: Use company auth service (definitely don't roll your own!)

*Is this really optional?*

The "(definitely don't!)" suggests it's NOT actually flexible.

If it's non-negotiable, call it a MUST!

**Solution (if really non-negotiable):**

```text

<constraint priority="critical">
MUST: Use company auth service (auth.company.com)
MUST NOT: Implement custom authentication

RATIONALE:

- Security critical (custom auth = high risk)
- Compliance requirement (SOC 2 audit)
- Centralized user management
- SSO integration

Company auth service provides:

- OAuth 2.0 / OIDC
- MFA support
- Audit logging
- SOC 2 compliant

No exceptions without security team approval.
`</constraint>`

**Or (if genuinely flexible):**

`<guideline priority="high">`
SHOULD: Prefer company auth service (auth.company.com)

ACCEPTABLE alternatives (with approval):

- Third-party auth (Auth0, Okta) if integrating with external systems
- Simple API key auth for internal tools (if justified)

REQUIRES security team approval:

Document why company auth doesn't work for this use case.

NOT acceptable:

- Rolling custom authentication (security risk)
- Storing passwords without company service (compliance violation)

RATIONALE: Company service provides SSO, MFA, compliance.

But some scenarios legitimately need alternatives.
`</guideline>`

**Clear about what's truly flexible vs. rigid.**

## Dialog Opportunities with SHOULDs

The most powerful aspect of SHOULDs: they enable conversation.

### When should a model Violate a SHOULD

**Good SHOULDs make a model confident to:**

1. Explain why the model violated
2. Ask if the violation is acceptable
3. Offer alternatives

**Example 1: Function Length**
SHOULD says:

SHOULD: Functions under 50 lines

Model writes 75-line function.

Model's response:
"Note: The processPayment function is 75 lines, which exceeds the 50-line guideline. However, it implements the complete payment workflow in one cohesive block:

1. Validate payment details (10 lines)
2. Call payment gateway (15 lines)
3. Handle success/failure responses (20 lines)
4. Update order status (15 lines)
5. Send confirmation email (15 lines)

Breaking this into smaller functions would scatter the payment flow across multiple files, making it harder to understand the complete sequence. Each step depends on the previous one.

This appears to fall under the guideline's exception for 'cohesive algorithms where breaking hurts readability.
Options: A- Keep as-is (single cohesive function) B- Refactor into 5 separate functions (scattered logic) C- Keep main flow, extract helpers (compromise)
My recommendation: Option C (main flow visible, helpers extracted)

Would you like me to proceed with Option C, or do you prefer A or B?"

**Dialog enabled!**
You can respond with preference, and the model adjusts.

**Example 2: Error Message Detail**
SHOULD says:
SHOULD: Error messages include recovery steps

Model writes generic error for security reason.

Model’s response:
"Note: Using generic error 'Invalid credentials' rather than specific 'Password incorrect' for the login endpoint.

The guideline recommends including recovery steps, which normally I'd do like this: 'Password incorrect. Passwords are case-sensitive. Try again or click Forgot Password to reset.'

However, this specific error reveals which field was wrong (the password), which enables username enumeration attacks. An attacker could test emails to see which ones exist in the system.

This falls under the guideline's exception for 'security-sensitive errors where detail would leak information.'

Current message: 'Email or password incorrect. Please try again or reset password.'
Alternative approach: Keep generic error but add general help: 'Login failed. Check that your email and password are correct. Passwords are case-sensitive. Need help? Click Forgot Password.'
Model’s recommendation: Alternative approach (helpful without leak)

Is this acceptable, or would you prefer different wording?"

**Dialog enabled!**
Security vs. helpfulness trade-off made explicit.

### When SHOULDs Conflict

Good SHOULDs tell a model how to resolve conflicts.
But sometimes models still need to ask:

Example: Performance vs. Simplicity

SHOULDs say:
SHOULD: Optimize for performance (target <200ms response)
SHOULD: Keep code simple and maintainable

Model faces a decision:

Model's response:

"I'm facing a trade-off between performance and simplicity for the user search endpoint.

Current implementation (simple):

- Query database for each search
- Response time: 350ms average
- Code: 20 lines, very clear

Optimized implementation (complex):

- Cache search results (Redis)
- Response time: 50ms average
- Code: 80 lines, more complex (caching logic)
The conflict:

- Spec says SHOULD optimize for performance (target <200ms)
- Current implementation: 350ms (above target)
- But spec also says SHOULD keep code simple
- Optimization adds significant complexity

Context:

- Search used frequently (50 requests/min peak)
- User-facing (affects perceived performance)
- But admin tool (not customer-facing)
Models question: Which priority wins here? Optimize for performance (caching), or keep simple (slower but clear)?

Model’s recommendation: Optimize (user-facing, frequent use)
Should I proceed with the caching implementation?"

**Dialog enabled!**
You can clarify priority, and model proceeds.

## SHOULD Guidelines Template

**Copy-paste ready template:**

```xml

<guideline priority="[high/medium/low]" scope="[domain]">

SHOULD: [Specific preferred approach]


ACCEPTABLE exceptions:

- [Scenario where deviation is okay]
- [Another acceptable exception with rationale]
- [Another one]


NOT acceptable exceptions:

- [Scenario where deviation is not okay]
- [Another unacceptable violation]

WHEN in doubt:

[Guidance on how to decide if exception is justified]

RATIONALE:

[Why this is preferred approach]
[Why exceptions exist]
[What balance you're trying to strike]

EXAMPLES:

Follows guideline:

[Code or description showing good compliance]

Acceptable violation:

[Code or description showing justified deviation]
[Why this deviation is acceptable]

Unacceptable violation:

[Code or description showing unjustified deviation]
[Why this deviation is not okay]

DIALOG:

If violating, explain:

1. What you did
2. Why you did it
3. Why you believe it's justified
4. Ask if acceptable
</guideline>
```

## Integration with MUSTs

### How SHOULDs and MUSTs work together

**The Hierarchy**
**Example: Complete Constraint Set**
<MUST-- Hard boundaries -->

`<constraint priority="critical" scope="authentication">`
MUST: Password hashing with bcrypt (salt rounds=12)
MUST: No plain text passwords anywhere
MUST: HTTPS only in production
`</constraint>`

<SHOULD-- Flexible guidance within boundaries -->

`<guideline priority="high" scope="authentication">`
SHOULD: Password requirements: 12+ chars, 1 upper, 1 lower, 1 number, 1 special

ACCEPTABLE exceptions:

- Internal admin tools (10+ chars okay if documented)
- Migration from legacy system (phase in requirements)

NOT acceptable:

- User-facing authentication (strict requirements apply)
- New systems (no reason to be lax)

SHOULD: Rate limiting: 5 attempts per 15 minutes

ACCEPTABLE exceptions:

- Known-safe IPs (internal monitoring tools)
- Testing environments (don't block developers)

NOT acceptable:

- Production user endpoints (security critical)

RATIONALE: Strong passwords reduce breach risk. Rate limiting
prevents brute force. But some scenarios justify relaxing rules.
'</guideline>'

MUSTs set floor (minimum security), SHOULDs provide guidance above floor.

## Checklist: Is My SHOULD Well-Written?

**Before finalizing SHOULD guidelines:**

Specificity

- [ ] Specific action (not vague like "be good")
- [ ] Measurable or recognizable
- [ ] Model knows what "following" looks like

Exception Guidance

- [ ] Acceptable exceptions defined
- [ ] Unacceptable violations defined
- [ ] Clear when deviation is justified

Rationale

- [ ] Why this is preferred
- [ ] Why exceptions exist
- [ ] What balance I'm striking

Examples

- [ ] Good compliance example
- [ ] Acceptable violation example
- [ ] Unacceptable violation example

Dialog-Enabled

- [ ] Model can explain violations
- [ ] Model can ask if acceptable
- [ ] Not secretly a MUST

Non-Conflicting

- [ ] Doesn't contradict other SHOULDs
- [ ] If conflict possible, priority defined
- [ ] Resolution guidance provided

## Key Takeaways

What Makes Good SHOULDs

### Good SHOULDs are

1. Specific (actionable, not aspirational)
2. Flexible (truly optional with good reason)
3. Guided (exceptions defined)
4. Rational (explains why)
5. Dialog-enabling (I can ask about violations)

### Common Mistakes to Avoid

1. Aspirational ("be elegant") → Not actionable
2. Too many (30 SHOULDs) → Overwhelming
3. No exceptions → Secretly MUSTs
4. Conflicting → Which wins?
5. Secret MUSTs → Be honest about rigidity

## The SHOULD Pattern

**Every SHOULD should have:**

1. Preferred approach (what)
2. Exception guidance (when deviation is okay)
3. Rationale (why)
4. Examples (good, acceptable violation, bad violation)
5. Dialog invitation (ask if uncertain)

Remember: SHOULDs Enable Partnership

**From a model’s perspective:**

SHOULDs tell a model:

- What you prefer (guidance)
- When the model can deviate (flexibility)
- When to ask (dialog)
- Why it matters (understanding)

Good SHOULDs enable a model to:

- Apply judgment (within your preferences)
- Explain decisions (justify deviations)
- Ask questions (when uncertain)
- Improve quality (without paralysis)
**This is partnership, not constraint.**

## What's Next

You've learned how to write SHOULD guidelines. Next:

Section 4: Providing CONTEXT (planning information that helps me)
Section 5: Expressing INTENT (the "why" behind requirements)
Section 6: Verification Protocols (self-correction systems)
Section 7: Common Pitfalls (what goes wrong)
Section 8: Section 8: The Supremacy Clause and Evidence Reset Protocols (Belief Dynamics)

Each section builds on this foundation of flexible, guided preferences.

You now know how to give a model guidance that empowers rather than constrains.

Let's continue building your complete specification framework...

END OF SECTION 3

Document Version: 1.0.0
Last Updated: 2026-02-16
Written from model perspective: What makes SHOULD guidelines work from daily experience
Key principle: SHOULDs enable partnership through flexibility with guidance


