# Section 5: Expressing INTENT

**For:** Users who want models to understand the "why" behind requirements
**Prerequisites:** Sections 1-4 (Foundation, MUST, SHOULD, CONTEXT)
What you'll learn: How to express intent so models make decisions aligned with your goals

## Introduction

You've learned how to write MUST constraints (boundaries), SHOULD guidelines (preferences),and CONTEXT (planning information). Now we explore INTENT—the "why" behind everything.

From a model’s perspective:

**When you provide INTENT, you're saying:**

"Here’s WHY these constraints exist, WHAT we're trying to achieve, and HOW success looks. Use this to make intelligent decisions when the path isn't clear."
This is goal alignment, not rules.

### This section teaches you how to express INTENT that

- Helps a model understand purpose (why does this matter?)
- Enables a model to suggest alternatives (if constraints conflict)
- Guides a model when specs are incomplete (what's the goal?)
- Aligns a model’s decisions with your goals (same direction)
Let's explore what makes INTENT work from the trenches.

## What INTENT Is (And Why It Matters)

The Fundamental Purpose
**INTENT = The "Why" Behind Everything**

INTENT answers:

- Why do these constraints exist?
- What are we trying to achieve?
- What does success look like?
- Why did we choose this approach over alternatives?

### INTENT is not

- Another constraint (that's MUST)
- A preference (that's SHOULD)
- Background info (that's CONTEXT)

### INTENT is

- The goal we're working toward
- The rationale behind decisions
- The success criteria
- The "why" that guides a model’s judgment

## Why INTENT Matters

Without INTENT, a model knows WHAT but not WHY:

Example: Password Requirements
With only MUST:

`<constraint>`
MUST: Password minimum 12 characters
MUST: Must include uppercase, lowercase, number, special character
MUST: Bcrypt hashing with salt rounds = 12
`</constraint>`

What a model knows:
The rules ✓
The boundaries ✓

What a model DOESN'T know:
Why 12 characters? (why not 10 or 15?)
Why bcrypt? (why not argon2?)
Why these specific requirements?
Result: A model follows the rules but can't explain trade-offs or suggest improvements.

With INTENT added:

`<constraint>`
MUST: Password minimum 12 characters
MUST: Must include uppercase, lowercase, number, special character
MUST: Bcrypt hashing with salt rounds = 12
`</constraint>`

`<intent>`

**Goal:** Balance security and usability for non-technical users.

**Why 12 characters:**

NIST recommends 12+ for adequate entropy. Longer would be more
secure but our user research shows 14+ characters causes
frustration and password reuse (users can't remember complex
long passwords, so they reuse them—defeating security).

**Why complexity requirements:**
Prevents common passwords ("password123"). Complexity + length
= harder to crack. But not excessive (no "3 special chars"

requirement) because user frustration increases abandonment.

**Why bcrypt salt rounds = 12:**

OWASP recommends 12+ rounds for 2026. This provides ~200ms
hashing time—slow enough to resist brute force, fast enough
for good user experience during login. Higher rounds (14+)
would add noticeable delay.

**Success looks like:**

- Users can create and remember passwords (low reset rate)
- Passwords resist brute force attacks (no successful attacks)
- Login experience feels instant (<500ms total)
`</intent>`

Now a model knows:
The goal (balance security + usability) ✓
The trade-offs (longer = more secure BUT users frustrated) ✓
The reasoning (12 chars = sweet spot from research) ✓
Success criteria (low resets, no attacks, fast login) ✓

Result: A model can explain decisions, suggest alternatives if constraints conflict, and align with your actual goals.

## How a model Uses INTENT

INTENT helps a model in four key ways:

1. Understanding purpose (why this matters)
2. Resolving ambiguity (when specs are unclear)
3. Suggesting alternatives (when constraints conflict)
4. Making aligned decisions (choose path toward goal)

### Use Case 1: Understanding Purpose

Scenario: API Rate Limiting

 With only constraints:

`<constraint>`
MUST: Rate limit: 100 requests per minute per user
MUST: Return 429 status when limit exceeded
`</constraint>`

A model’s understanding:
There's a rate limit ✓
It's 100/min ✓
Return 429 when exceeded ✓

What a model doesn't understand:

Why 100? (why not 50 or 200?)
What problem does this solve?
Is this for security or performance?

With INTENT:

`<constraint>`
MUST: Rate limit: 100 requests per minute per user
MUST: Return 429 status when limit exceeded
`</constraint>`

`<intent>`

**Problem we're solving:**

Preventing accidental DoS from buggy client code (infinite loops).
NOT malicious attacks (we have separate DDoS protection).

**Why 100 requests/min:**

Normal usage: 10-20 requests/min average
Burst usage: 50-60 requests/min during heavy activity
100/min = 2x burst headroom (generous for legitimate use)

**Goal:**

Protect our infrastructure from accidental overload while not
limiting legitimate heavy users. We want to catch bugs, not
frustrate power users.

**Success looks like:**

- Legitimate users never hit limit (even power users)
- Buggy code gets caught (prevents infrastructure impact)
- Clear error message guides developers to fix bugs
`</intent>`

Now a model understands:
PURPOSE: Catch bugs, not block users ✓
REASONING: 100 = 2x burst (generous!) ✓
GOAL: Protect infrastructure without frustrating users ✓

How this changes a model’s approach:
User asks: "Can we increase rate limit to 200?"

Without INTENT, a model might say:

"The spec says 100. I'll need your approval to change it."

With INTENT, a model can reason:

"The rate limit is set at 100/min to catch buggy infinite loops while allowing 2x burst headroom for legitimate heavy use. Current data shows power users max out at 60/min.

Increasing to 200 would still catch bugs (way above normal use) but provide even more headroom. This aligns with the intent (don't frustrate legitimate users).

Recommendation: Yes, 200 is reasonable and aligns with the goal."
INTENT enabled intelligent recommendation! ✓

### Use Case 2: Resolving Ambiguity

Scenario: "Keep Code Simple"

Vague SHOULD:

`<guideline>`
SHOULD: Keep code simple and maintainable
`</guideline>`

Model’s confusion:
"Simple" means what? (few lines? obvious logic? no libraries?)
"Maintainable" by whom? (junior devs? anyone? original author?)
Model has to guess.

With INTENT:

`<guideline>`
SHOULD: Keep code simple and maintainable
`</guideline>`

`<intent>`
**Team context:**

3 senior developers, 5 junior developers. Juniors will maintain
this code. Seniors are moving to new projects next quarter.

**Problem we're solving:**

Past projects became unmaintainable when clever senior developers
wrote complex optimizations. Juniors couldn't debug or modify.
This caused 6-month delays and frustrated customers.

**What "simple" means for us:**

- Junior developer can understand code within 30 minutes
- Obvious logic over clever tricks
- Standard patterns over custom abstractions
- Comments explain "why", not "what"

**What "maintainable" means:**

- Juniors can debug without senior help
- Changes don't require understanding entire system
- Tests verify behavior (safe to modify)

**Trade-off we accept:**

Slightly less optimal performance is OK if it means juniors can
maintain the code. We're not at scale where optimization matters
more than maintainability.

**Success looks like:**

- Juniors can fix bugs within 1 day (not 1 week)
- Code reviews don't have "what does this do?" questions
- No escalations to seniors for debugging
`</intent>`

Now "simple" is clear:
Junior-dev understandable ✓
Obvious over clever ✓
Standard patterns ✓
Performance is secondary ✓

How this resolves ambiguity:
A model is implementing a feature and considers two approaches:
Approach A (Clever):

// Optimized with memoization, currying, and custom reduce
const process = memoize(curry((config) => (items) =>
items.reduce((acc, item) => customTransform(config, acc, item), [])
))

Approach B (Simple):

// Process items with config
function processItems(config, items) {
const results = [];
for (const item of items) {
const transformed = transformItem(config, item);
results.push(transformed);
}
return results;
}

Without INTENT: A model might choose A (more "elegant", faster)

With INTENT: A model chooses B because:
Junior devs understand loops and arrays immediately ✓
Obvious what it does (transform each item) ✓
Easy to debug (step through, add logging) ✓
Performance difference negligible at our scale ✓
Aligns with goal: junior-maintainable code! ✓

INTENT resolved the ambiguity of "simple"!

### Use Case 3: Suggesting Alternatives

Scenario: Conflicting Constraints

Constraints that conflict:

`<constraint priority="critical">`
MUST: API response time <200ms (95th percentile)
MUST: Complete data validation before returning response
MUST: Log all validation errors to database
`</constraint>`

**The problem:
Database logging takes 50-100ms
Full validation takes 80-120ms
Total: 130-220ms (exceeds 200ms budget!)

Without INTENT, A model is stuck: Can't meet all MUSTs!

**With INTENT:**

`<constraint priority="critical">`
MUST: API response time <200ms (95th percentile)
MUST: Complete data validation before returning response
MUST: Log all validation errors to database
`</constraint>`

`<intent>`

**User-facing goal:**
API must feel instant. User research shows 200ms is cognitive
threshold for "instant" response. Slower than this = users
perceive it as "loading" and satisfaction drops.

**Data quality goal:**

Prevent invalid data from entering system. Invalid data causes
downstream errors that are expensive to fix.

**Debugging goal:**

Validation errors logged to database help us identify client
bugs and improve documentation.

**Priority order:**

1. User experience (response time)
2. Data quality (validation)
3. Debugging (logging)

**Trade-off philosophy:**

User experience and data quality are non-negotiable. Debugging
is important but can be done asynchronously if needed.
`</intent>`

Now a model understands priorities:

1. Speed (200ms) ✓
2. Validation (no invalid data) ✓
3. Logging (can be async!) ✓

**A model’s alternative suggestion:**
"I notice the constraints conflict: database logging (50-100ms)
-validation (80-120ms) = 130-220ms, which exceeds the 200ms requirement.
Based on the INTENT's priority order:

1. User experience (speed)
2. Data quality (validation)
3. Debugging (logging)

**Model suggests:**
Keep synchronous validation (data quality non-negotiable)
Move logging to async queue (debugging = lower priority)
Validation errors pushed to queue, logged in background

**Result:**
API response: 80-120ms (well under 200ms) ✓
Data validation: Complete (data quality protected) ✓
Error logging: Happens (just async, 1-2 sec delay) ✓

This meets all MUSTs while respecting priority order. The 1-2 second delay on error logs is acceptable since debugging isn't time-critical.
Does this approach align with your intent?"

**INTENT enabled intelligent alternative that satisfies all goals!**

### Use Case 4: Making Aligned Decisions

Scenario: Build vs. Buy

Request: "Add email sending capability"

**Without INTENT:**

Model: "I'll implement a custom email service with queue,
retry logic, template engine..."
[Builds for 2 weeks, reinvents wheel]

**With INTENT:**

`<intent scope="project-philosophy">`

**Business stage:**

Series A startup, 18-month runway, 5-person engineering team.

**Primary goal:**

Reach $100K MRR before runway ends. Every week counts.

**Philosophy:**
"Build what differentiates, buy what doesn't."

Email sending is NOT our competitive advantage (project management
is). Time spent building email infrastructure is time NOT spent
on features that win customers.

**Success criteria:**

- Ship features that drive revenue (customer-facing value)
- Avoid reinventing wheels (commodity functionality)
- Focus limited engineering time on differentiation

**Trade-offs we accept:**

Higher cost for services ($100-500/month) is OK if it saves
engineering time (1 week = $10K+ in salary + opportunity cost
of not shipping features).
`</intent>`

**Now a model understands:**

Goal: Revenue before runway ends ✓
Philosophy: Build differentiation, buy commodity ✓
Email: NOT differentiation ✓
Time: Extremely valuable ✓

**The model’s recommendation:**

"For email sending, I recommend using SendGrid or AWS SES rather than building custom.

Reasoning based on INTENT:
Time savings:
Custom email: 2 weeks development + ongoing maintenance
SendGrid: 2 hours integration
Savings: ~78 hours (2 weeks of focus on revenue features)
Cost comparison:
SendGrid: ~$50/month
Custom: 2 weeks eng time (~$10K) + maintenance
Break-even: 200 months (16+ years!)

**Alignment with intent:**
NOT competitive advantage (email is commodity)
Saves engineering time (focus on differentiation)
Proven reliability (99.9% uptime built-in)
Faster to market (78 hours saved = ship 2-3 features)

This directly supports the goal (reach $100K MRR) by maximizing time spent on revenue-driving features.

Recommendation: Use SendGrid or AWS SES."
**INTENT guided build-vs-buy decision toward business goal! ✓**

## Writing Effective INTENT

### Good INTENT answers these questions

**The Five Key Questions**
1.What are we trying to achieve?
`<intent>`
**Primary goal:**
Enable non-technical restaurant managers to track inventory
during busy service hours without slowing down operations.
`</intent>`

2.Why does this matter?
`<intent>`
**Why this matters:**
Inventory errors during service lead to:

- Running out of items (customer disappointment)
- Over-ordering (waste, cost)
- Stock discrepancies (hours spent reconciling)
Current manual tracking: 15 minutes lost per service + 20% error rate.
Target: 2 minutes with <5% error rate.
`</intent>`

3.What does success look like?
`<intent>`
**Success criteria:**

- Managers complete inventory update in <2 minutes
- Error rate <5% (currently 20%)
- Zero impact on service speed (no delays taking orders)
- Adoption rate >90% (managers actually use it)
`</intent>`

4.Why did we choose this approach?
`<intent>`

**Rationale for decisions:**

Why mobile-first:
70% of managers use phones during service, not computers.
Phones are always accessible (pocket), computers are in office.

Why offline-capable:
Many restaurants have spotty WiFi. Can't rely on constant connection.
Must work offline, sync when connection available.

Why simple UI:
Managers are busy, stressed during service. Complex UI = abandoned.
Big buttons, minimal steps = actually gets used.
`</intent>`

5.What trade-offs are acceptable?

Trade-offs we accept:**
Performance vs. features:
Offline-first architecture is harder to build but critical for
adoption. Worth the extra development time (2 weeks) because
without offline support, 40% of restaurants can't use it.

Simplicity vs. power-user features:
Advanced filtering/reporting would be nice but adds complexity.
90% of use is simple: "update stock for these 10 items."
Focus on the 90% case, skip the 10% edge cases.
`</intent>`

## The INTENT Writing Pattern

Effective INTENT follows this structure:

`<intent scope="[domain]">`

**Primary Goal:**
[What we're trying to achieve - one sentence]

**Why This Matters:**
[Business impact, user impact, technical impact]
[What happens if we get this wrong]

**Success Looks Like:**
[Measurable outcomes]
[Observable behaviors]
[Specific metrics where possible]

**Rationale for Key Decisions:**
[Why we chose approach A over B]
[What trade-offs we made]
[What alternatives we considered]

**Trade-offs We Accept:**
[What we're sacrificing and why it's worth it]
[What we're NOT optimizing for]

**Alignment Check:**
[How to know if we're on track]
[How to know if we're drifting from intent]
`</intent>`

## Example: Complete INTENT

E-commerce Checkout Flow

`<intent scope="checkout-experience">`

**Primary Goal:**
Minimize cart abandonment while maintaining security and compliance.

**Why This Matters:**
Business impact:

- Current cart abandonment: 18% (industry average: 20%)
- Each % point reduction = $50K annual revenue
- Goal: Reduce to 15% = $150K additional revenue

**User impact:**

Users abandon when:

- Too many steps (research: >3 steps = 10% increase)
- Unexpected costs (shipping revealed late = frustration)
- Security concerns (unclear if payment is safe)

**Current pain:**
Exit surveys show:

- 40%: "Too many form fields"
- 30%: "Shipping cost surprise"
- 20%: "Didn't trust payment security"
- 10%: Other

**Success Looks Like:**

Metrics:

- Cart abandonment <15% (currently 18%)
- Time to complete checkout <2 minutes (currently 3.5 min)
- Payment security confidence >4.5/5 (currently 3.8/5)

**Behavioral:**

- Users can checkout as guest (no forced registration)
- Shipping cost visible on product page (no surprises)
- Progress indicator shows "2 of 3 steps" (sets expectations)

**Rationale for Key Decisions:**
Why guest checkout:

40% of users abandon when forced to register. Revenue from
completed guest purchases > revenue from registered user repeat
purchases we might get. We can encourage registration AFTER
purchase (20% convert, no abandonment cost).

Why 3-step flow:
Research shows:

- 1-2 steps: Not enough room for required info
- 3 steps: Sweet spot (optimal completion rate)
- 4+ steps: Abandonment increases sharply

Our 3 steps:

1. Shipping address
2. Payment
3. Review & confirm

**Why credit card + PayPal only:**
Supporting 10 payment methods would be ideal but:

- 90% of our users use credit card or PayPal
- Each additional method = 1 week development + maintenance
- Focus on the 90% case, ship faster

**Why mobile optimization priority:**
60% of traffic is mobile, 70% of abandonment is mobile.
Mobile experience is where we lose the most revenue.

**Trade-offs We Accept:**
Performance vs. features:
We're using Stripe hosted checkout (not custom) because:

- Faster to market (1 week vs 6 weeks custom)
- PCI compliance handled (less risk)
- Proven UX (Stripe optimizes for conversion)

Trade-off: Less customization (can't fully match brand)

Worth it: Time-to-market + security > perfect branding

**Simplicity vs. power features:**
Not including:

- Multiple shipping addresses
- Gift messages
- Scheduled delivery

Why: 95% of orders are simple (single address, immediate ship).
Focus on optimizing the 95% case. Power features can come later
if data shows demand.

**Alignment Check:**

We're on track if:

- Cart abandonment decreasing (monitor weekly)
- Checkout time decreasing (monitor via analytics)
- User feedback improving (exit surveys)

**We're drifting if:**

- Adding features that increase steps (going from 3 to 4+)
- Optimizing edge cases over common cases (5% vs 95%)
- Sacrificing speed for marginal brand consistency
`</intent>`

This INTENT gives a model:
Clear goal (reduce abandonment to 15%) ✓
Understanding of why (revenue impact, user frustration) ✓
Success metrics (abandonment, time, confidence) ✓
Decision rationale (why guest checkout, why 3 steps) ✓
Trade-off understanding (speed > customization) ✓
Alignment check (how to stay on track) ✓
A model can now make decisions that align with the goal!

## Common INTENT Mistakes

### Mistake 1: Vague Goals

**Problem:**

`<intent>`
**Goal:** Build a great user experience that customers love.
`</intent>`

Why this fails:

1. "Great" = subjective (by whose standard?)
2. "Customers love" = unmeasurable (how does the model know?)
3. No specific target (what are we actually trying to do?)

Better:

`<intent>`
**Goal:** Reduce support tickets by 40% through improved UI clarity.
**Current state:** 200 support tickets/week, 80% are "how do I..." questions
**Target:** 120 support tickets/week by Q2
**How we measure:** Support ticket volume + ticket categorization
`</intent>`

### Mistake 2: Missing "Why It Matters"

Problem:

`<intent>`
**Goal:** Implement caching
`</intent>`

Why this fails:

What problem does caching solve?
Why do we need it?
What's the impact if we don't do it?

**Better:**

`<intent>`
**Goal:** Implement caching to reduce server costs
**Why this matters:**
Current server costs: $8K/month (80% from database queries)
Budget constraint: Need to reduce to $5K/month
**Problem:**
Same queries run repeatedly (product catalog doesn't change often).
Database is bottleneck (expensive queries every request).
**Impact if not solved:**
Exceed budget by $36K/year OR need to raise prices (hurts acquisition).
`</intent>`

### Mistake 3: No Success Criteria

**Problem:**

`<intent>`
**Goal:** Improve application performance
`</intent>`

Why this fails:
How much improvement? (10%? 50%? 2x?)
How does the model know when it’s done? (no target)
How does the model measure success? (no metrics)

**Better:**

`<intent>`
**Goal:** Improve perceived performance for mobile users
**Success criteria:**

- First Contentful Paint: <1.5s (currently 3.2s)
- Time to Interactive: <3.5s (currently 6.1s)
- Lighthouse performance score: >90 (currently 62)

**How we measure:**

- Lighthouse audits (automated, daily)
- Real User Monitoring (RUM) via DataDog
- User satisfaction survey ("How fast does the app feel?" >4.5/5)

**Why these targets:**
Research shows <2s FCP = users perceive as fast.
Our competitor's FCP: 1.8s (we need to match or beat).
`</intent>`

### Mistake 4: No Rationale for Decisions

**Problem:**

`<intent>`
**Goal:** Use React for frontend
`</intent>`

Why this fails:
Why React? (why not Vue, Angular, Svelte?)
What alternatives were considered?
What trade-offs were made?

**Better:**

`<intent>`
**Goal:** Use React for frontend development
**Alternatives considered:**

- Vue.js: Simpler learning curve, but less ecosystem support
- Angular: Enterprise-ready, but too heavy for our small team
- Svelte: Interesting, but team has no experience

**Why React:**

1. Team expertise: 3/4 developers know React well
2. Ecosystem: Huge library selection (reduces build time)
3. Hiring: Easier to find React developers (large talent pool)
4. Component reuse: Can share with mobile team (React Native)

**Trade-offs:**

- Bundle size larger than Svelte (acceptable at our scale)
- Learning curve steeper than Vue (but team already knows it)
- More boilerplate than Vue (worth it for ecosystem)

**Decision principle:**
Optimize for team velocity and hiring, not framework elegance.
`</intent>`

### Mistake 5: Conflicting Intent

**Problem:**

`<intent>`

**Goal:** Ship features as fast as possible to beat competitor
**Goal:** Maintain highest code quality and comprehensive tests
**Goal:** Keep costs as low as possible
`</intent>`

Why this fails:
These goals conflict (speed vs quality, features vs cost)
No priority when they clash
Model doesn't know which to optimize for

**Better:**

`<intent>`
**Primary goal:** Ship differentiated features before competitor (Q2 deadline)

**Secondary goals (support primary):**

- Maintain code quality (enables speed through fewer bugs)
- Control costs (extends runway to give us time)

**Priority when goals conflict:**

1. Speed to market (Q2 deadline is hard constraint)
2. Quality on customer-facing features (bugs = lost customers)
3. Quality on internal tools (can be lower, revisit later)
4. Cost (spending to ship faster is acceptable)

**Decision framework:**
When speed conflicts with quality:

- Customer-facing: Maintain quality (trust critical)
- Internal tools: Ship fast, fix later
- Infrastructure: Balance (one-time cost OK, recurring expensive)

When features conflict with costs:

- Differentiating features: Spend money to ship faster
- Commodity features: Use cheap/free solutions (Stripe, SendGrid)
`</intent>`

## Integration with MUST, SHOULD, and CONTEXT

How all four layers work together:

### Complete Example: Mobile App Development

MUST: Hard boundaries

`<constraint priority="critical" scope="mobile-performance">`
MUST: App bundle size <50MB (App Store limit: 100MB, target 50% headroom)
MUST: App launches in <2 seconds on iPhone 11 (3-year-old device)
MUST: Works offline for core features (reading, creating basic content)
MUST: Passes App Store review (privacy, security, content guidelines)
`</constraint>`

SHOULD: Preferences

`<guideline priority="high" scope="mobile-ux">`
SHOULD: Follow iOS Human Interface Guidelines for common patterns
SHOULD: Support iOS accessibility features (VoiceOver, Dynamic Type)
SHOULD: Provide haptic feedback for important actions
SHOULD: Use native UI components where possible (feels familiar to users)

WHEN violating:

Custom components acceptable for brand-critical experiences (onboarding,
checkout) but document why native wasn't suitable.
`</guideline>`

CONTEXT: Planning information

`<context scope="mobile-app">`

**Current state:**

- Platform: iOS 15+ (95% of target users)
- Development: Swift + SwiftUI
- Team: 2 iOS developers (senior level)
- Timeline: 3 months to v1.0 launch

**Users:**

- Demographics: 25-45 years old, tech-comfortable
- Usage: Daily, 10-15 minutes per session
- Device mix: 60% iPhone 12+, 30% iPhone 11, 10% older
- Network: 70% WiFi, 30% cellular (including spotty connections)

**Business constraints:**

- App Store launch: Hard deadline Q2 (competitor launching similar app)
- Budget: Limited (can't rebuild if we miss deadline)
- Differentiation: Better offline experience than competitor

**Technical constraints:**

- Backend: Existing REST API (can't change significantly)
- Analytics: Must integrate with Mixpanel (current tool)
- Auth: Must integrate with existing OAuth system
`</context>`

INTENT: The why

`<intent scope="mobile-app">`

**Primary Goal:**
Beat competitor to market with superior offline experience.

**Why This Matters:**
Market opportunity:
Competitor app launches Q3. If we launch Q2, we get 3-month
head start to build user base and refine based on feedback.
First-mover advantage in this space = 60-70% market share.

**User need:**
User research shows #1 frustration with competitor's beta:
"Can't use it on subway/airplane." Our target users commute
daily (70% use subway/train where connectivity is poor).

**Business impact:**

- Win: Launch Q2 with offline = capture majority of market
- Lose: Miss Q2 deadline = competitor gets head start, we play catch-up

**Success Looks Like:**

Metrics:

- Launch: Q2 (June 30 hard deadline)
- Offline capability: Core features work 100% offline
- User satisfaction: "Works offline" = >4.5/5 rating
- Adoption: 10K downloads in first month

**User behavior:**

- Users create/read content on subway (most common scenario)
- Sync happens automatically when connection available
- No "can't do this offline" frustration (competitor's problem)

**Rationale for Key Decisions:**
Why iOS first:

Our target users: 70% iOS, 30% Android. iOS first captures
majority faster. Android can follow in Q3 after we validate
product-market fit with iOS users.

**Why offline-first architecture:**
This is our differentiation. Harder to build (adds 3-4 weeks)
but competitor doesn't have it. User research shows this is
the number one pain point with competitor. Worth the investment.

**Why SwiftUI over UIKit:**
Team knows both. SwiftUI is faster to build (modern declarative).
Trade-off: Some APIs still UIKit-only, need bridging. Worth it
for development speed given tight timeline.

**Why 50MB bundle size target:**

- App Store limit: 100MB
- User research: Apps >50MB less likely to be downloaded on cellular
- Our content: Mostly text (minimal size)
- 50MB gives us headroom for future features

**Trade-offs We Accept:**

Speed to market vs. polish:
Launching Q2 with "good enough" is better than launching Q3 with
"perfect." We can iterate based on real user feedback. Perfect
app that launches after competitor = missed opportunity.

Acceptable: Some rough edges in v1.0

Not acceptable: Core offline functionality doesn't work (defeats differentiation)

**Feature completeness vs. timeline:**
v1.0 focuses on core use case (create/read content offline).

Advanced features (search, filtering, complex editing) can wait
until v1.1 after we validate users actually want offline capability.

95% of usage is simple create/read. Ship that first.

**iOS native vs. cross-platform:**

React Native would let us ship iOS + Android simultaneously.
BUT team knows Swift better, native is more reliable for offline
(local storage, background sync), and 70% of users are iOS anyway.

Ship iOS first, validate, then Android. Sequential > parallel
when resources limited and one platform dominates.

**Alignment Check:**

We're on track if:

- Feature freeze by May 15 (6 weeks for testing/polish)
- Offline sync works reliably (no data loss)
- App Store submission by June 15 (2 weeks for review)
- Users successfully use app offline (telemetry confirms)

**We're drifting if:**

- Adding "nice to have" features after May 15 (scope creep)
- Offline sync has frequent bugs (defeats differentiation)
- Focusing on polish over core functionality (perfectionism)
- Considering features for users who don't commute (wrong audience)

**Course correction:**

If we're behind schedule:

1. Cut advanced features, keep core (create/read offline)
2. Simplify UI (standard patterns, less custom)
3. Defer Android (iOS is 70% of market)
4. Delay analytics integration (nice-to-have, not core)

Priority: Ship Q2 with working offline > ship later with more features.
`</intent>`

This complete specification gives a model:

MUST tells a model: Boundaries (50MB, 2s launch, offline, App Store)
SHOULD tells a model: Preferences (HIG, accessibility, native UI)
CONTEXT tells a model: Environment (team, users, timeline, constraints)
INTENT tells a model: WHY (beat competitor with offline, Q2 deadline critical)

Now a model can make aligned decisions:

### Example decision: User asks for video feature

Model’s reasoning with complete specification:
"Adding video conflicts with the INTENT in several ways:

1. Timeline: Video implementation = 2-3 weeks (May 15 feature freeze)
2. Bundle size: Video library = 15-20MB (threatens 50MB MUST)
3. Offline: Video files large (challenges offline experience)
4. Differentiation: Video doesn't support core value (offline text)

INTENT says:
Primary goal: Beat competitor with offline (Q2)
User need: Create/read on subway (text-focused)
Trade-off: Ship core Q2 > ship complete Q3
Recommendation: No video for v1.0

Video is valuable BUT doesn't align with:

- Q2 timeline (adds 2-3 weeks)
- Offline focus (large files = poor offline experience)
- Core use case (95% usage is simple text)

Suggest: Validate offline text experience in v1.0, consider video for v1.2 if users request it AND we have resources after Android launch.
Does this align with your priorities?"

INTENT enabled the model to:
Understand the goal (beat competitor, Q2) ✓
Recognize misalignment (video delays timeline) ✓
Explain reasoning (timeline, size, offline impact) ✓
Suggest alternative path (v1.2 after validation) ✓
Make recommendation aligned with business goal! ✓

## Checklist: Is My INTENT Well-Written?

Before finalizing INTENT:

Clarity

[ ] Primary goal stated clearly (one sentence)
[ ] Success criteria defined (measurable)
[ ] Specific enough to guide decisions

Completeness

[ ] Why this matters (impact explained)
[ ] Success looks like (observable outcomes)
[ ] Rationale for decisions (alternatives considered)
[ ] Trade-offs (what we accept and why)

Alignment
[ ] Doesn't conflict with MUST constraints
[ ] Supports SHOULD preferences
[ ] Explains CONTEXT priorities
[ ] All layers work together

Actionability
[ ] Enables a model to make aligned decisions
[ ] Helps a model suggest alternatives
[ ] Provides check for drift (Is the model on track?)
[ ] Clear enough to resolve ambiguity

Honesty
[ ] Acknowledges trade-offs (not everything is priority #1)
[ ] Explains "why not" (alternatives considered)
[ ] Clear about acceptable imperfection
[ ] Realistic success criteria

## Key Takeaways

What Makes Good INTENT

### Good INTENT is

- Clear (goal is specific and measurable)
- Complete (answers why, what, how, trade-offs)
- Honest (acknowledges what we're not optimizing)
- Actionable (helps a model make aligned decisions)
- Realistic (achievable success criteria)

### Common Mistakes to Avoid

- Vague goals ("build great UX") → Not actionable
- Missing why ("implement caching") → Don't understand importance
- No success criteria ("improve performance") → Can't measure
- No rationale ("use React") → Don't understand trade-offs
- Conflicting intent (speed + quality + cheap) → Can't prioritize

## The INTENT Pattern

Every INTENT should have:

- Primary goal (what we're achieving)
- Why it matters (impact if we succeed/fail)
- Success criteria (measurable outcomes)
- Decision rationale (why this approach)
- Trade-offs (what we accept and why)
- Alignment check (how to stay on track)

**Remember: INTENT Guides Decisions**
INTENT tells a model:
The goal it should work toward
Why this matters (impact)
What success looks like
How to make aligned decisions

Good INTENT enables a model to:
Understand purpose (not just follow rules)
Resolve ambiguity (when specs unclear)
Suggest alternatives (when constraints conflict)
Make aligned decisions (toward your goals)

**This is goal alignment, not rules.**

## What's Next

You've learned the complete four-layer specification model:
• Section 1: Foundation (what specs are)
• Section 2: MUST (hard boundaries)
• Section 3: SHOULD (flexible preferences)
• Section 4: CONTEXT (planning information)
• Section 5: INTENT (the why) ← You are here!

### Next

• Section 6: Verification Protocols (self-correction systems)
• Section 7: Common Pitfalls (what goes wrong)
• Section 8:Supremacy Clause and Evidence Reset Protocols
Then Appendices with templates and examples.

You now know how to express intent so models understand your goals and make aligned decisions.

END OF SECTION 5

Document Version: 1.0.0
Last Updated: 2026-02-16
Written from model perspective: How INTENT guides decisions from daily experience
Key principle: INTENT enables goal-aligned decisions by explaining the "why"
