# Section 4: Providing CONTEXT

**For:**
Users who want to help models make better decisions

**Prerequisites:** Sections 1-3 (Foundation, MUST, and SHOULD)

What you'll learn: How to provide context that helps models plan effectively without overwhelming them

## Introduction

You've learned how to write MUST constraints (hard boundaries) and SHOULD guidelines (flexible preferences).

Now we explore CONTEXT—the planning information that helps models make intelligent decisions within those boundaries.

**From a model’s perspective:**
When you provide CONTEXT, you're saying:

"Here's the background you need to make good decisions.

This isn't a constraint—it's a lens to help you prioritize, make tradeoffs, and choose the right approach."

**This is planning support, not rules.**

### This section teaches you how to provide CONTEXT that

- Helps models prioritize (what matters most?)
- Informs tradeoffs (when things conflict?)
- Guides judgment (how to decide?)
- Doesn't overwhelm (focused, relevant)

## What CONTEXT Is (And Isn't)

The Fundamental Nature

**CONTEXT = Planning Information**

**Not:**

- Constraints (that's MUST)
- Preferences (that's SHOULD)
- Instructions (that's prompts)

**But:**

- Background that informs decisions
- Priorities when making tradeoffs
- Understanding of who/what/why
- Lens for intelligent judgment

### Example: The Difference

```text

MUST (constraint):
MUST: API response time <200ms (95th percentile)

Model’s response: This is a boundary. I will comply. ✓

SHOULD (preference):
SHOULD: Prefer caching to reduce database queries

Model’s response: This is preferred. I'll follow unless good reason not to. ✓

CONTEXT (planning info):

<context>

Users: Non-technical small business owners

Usage pattern: Peak 9am-12pm (morning admin), low afternoons

Current pain: "System feels slow during morning rush"

Priority: User experience > System efficiency

Scale: 2K users, 50 concurrent peak
</context>
```
**Model’s response:**

- Ah! Morning peak is the problem (9am-12pm)
- Users are non-technical (need simplicity, not complexity)
- "Feels slow" = perception matters (target <200ms for instant feel)
- Priority is UX, not efficiency (ok to use more resources for speed)
- Scale is small (can optimize for speed, not scale)

Now when a model sees the SHOULD about caching, it understands:

- WHY caching matters (morning peak performance!)
- WHERE to cache (morning admin workflows!)
- HOW aggressive (very—UX is priority!)

**CONTEXT changed HOW a model applies the SHOULD!!!**

## CONTEXT vs. Other Layers

**How the four layers work together:**

CONTEXT informs HOW a model executes within the boundaries.

### When CONTEXT Helps a model (Good Examples)

CONTEXT helps a model when it provides:

1. Who (users/audience)
2. What (technical environment)
3. When (timing/patterns)
4. Why (priorities/pain points)
5. How much (scale/scope)

#### Example 1: Technical Environment Context

CONTEXT That Helps:

```text

<context scope="technical-environment">
**Technology Stack:**

- Backend: Node.js 20 LTS on AWS Lambda
- Database: PostgreSQL 14 on RDS (db.t3.medium)
- Frontend: React 18 + Next.js 14
- CDN: CloudFront
- Monitoring: DataDog

**Infrastructure Constraints:**

- Lambda timeout: 15 seconds maximum
- Lambda memory: 1GB allocated
- RDS connections: 100 maximum
- Cold start concern: First request after idle can be slow

**Team Context:**

- 2 senior developers (strong Node.js/React)
- 3 mid-level developers (learning serverless)
- Code review required for all changes
- CI/CD: GitHub Actions

**Deployment:**

- Production: Blue-green deployment
- Staging: Mirrors production
- Dev: Local development with Docker
</context>

**Why this helps a model**

1. Technology Choices Informed:
Scenario: User asks for caching solution

**Without context:**
Model: "I could use Redis, Memcached, or in-memory caching..."
[Guesses which to recommend]

**With context:**
Model: "Given Lambda serverless architecture, external caching
(ElastiCache Redis) makes most sense. In-memory caching
won't persist across Lambda invocations due to stateless
nature. Redis integrates well with Node.js, team has
serverless experience, and keeps within infrastructure."
CONTEXT guided my recommendation! ✓

2. Constraints Understood:
Scenario: User asks for long-running background job

**Without context:**
Model: "I'll create a background worker process..."
[Designs solution that won't work]

**With context:**
Model: "Lambda has 15-second timeout, so long-running job won't work.
Two options:
A- SQS + Step Functions (for jobs >15s, <15min)
B- ECS Fargate (for jobs >15min)
Given team's serverless focus, recommend Step Functions
with Lambda functions for each step. Fits infrastructure
and team expertise."
CONTEXT prevented impossible solution! ✓

3. Team Capabilities Considered:
Scenario: User asks for complex optimization

**Without context:**
Model: "I'll use advanced caching with cache invalidation
strategies, distributed locks, and Redis Cluster..."
[Designs solution team can't maintain]

**With context:**
Model: "Given mix of senior and mid-level developers, I'll design
straightforward caching with clear patterns:

- Simple key-value caching (easy to understand)
- TTL-based expiration (no complex invalidation)
- Well-commented code (learning opportunity)
- Comprehensive tests (safety net)
- This balances performance with maintainability for your team."
```
**CONTEXT matched solution to team! ✓**

#### Example 2: User/Audience Context

**CONTEXT That Helps**

```text

<context scope="users-and-audience">

**Primary Users:**

- Small business owners (restaurants, retail, services)
- Age: 35-60 years old
- Technical proficiency: Low (use email, social media, basic apps)
- Time available: 5-10 minutes per session (very busy!)
- Device: 60% mobile, 40% desktop
- Internet: Variable (sometimes slow connections)

**User Goals:**

- Manage daily operations (inventory, sales, schedules)
- Quick data entry (during work, not after hours)
- Access reports (weekly/monthly summaries)

**Pain Points (from user research):**

- Frustrated by complex interfaces ("too many buttons")
- Annoyed by slow loading ("I don't have time to wait")
- Confused by technical jargon ("what does that mean?")
- Need help accessible ("I get stuck and don't know what to do")

**Success Criteria:**

- 90% task completion without external help
- Average task time <3 minutes
- <1% error rate on critical operations
- User satisfaction >4.5/5
</context>
```
**Why this helps a model:**

1. UI Complexity Decisions:

**Scenario:** Designing inventory management screen

**Without context:**
Model: "I'll create comprehensive interface with:

- Advanced filters (date range, categories, suppliers, tags)
- Bulk operations (select multiple, batch edit)
- Export options (CSV, Excel, PDF)
- Advanced search (regex, wildcards)..."
[Designs power-user interface]

**With context:**
Model: "Users are non-technical and time-constrained.

I'll design:

- Simple search (just product name)
- One-click common operations (no bulk actions)
- Big, clear buttons (mobile-friendly)
- Minimal options (reduce decision fatigue)
- Inline help (contextual tooltips)
- Advanced features can go in 'Settings' for rare use."
**CONTEXT drove simplicity! ✓**

2. Error Message Tone:

**Scenario:** Writing validation error messages

**Without context:**
Error: "Invalid input: field 'quantity' must be numeric (regex: ^[0-9]+$)"

Technical, confusing for non-technical users.

**With context:**
Error: "Please enter a number for quantity. For example: 5 or 10"

**Simple, helpful, example-driven for non-technical users. ✓**

3. Performance Priorities:

**Scenario:** Optimizing application

**Without context:**

Model: "I'll optimize everything for maximum performance..."

[Spends effort optimizing features users rarely use]

**With context:**
Model: "Users are mobile (60%) with variable internet. Priority:

1. Fast initial load (<2s on slow connection)
2. Quick common operations (inventory check, sales entry)
3. Offline capability (work without internet, sync later)
Less critical:
- Report generation (users do this weekly, can wait)
- Settings changes (rare, can be slower)
- Optimize where users spend TIME, not everything."
**CONTEXT focused optimization effort! ✓**

#### Example 3: Business Priority Context

**CONTEXT That Helps:**

```text

<context scope="business-priorities">

**Company Stage:**

- Series A startup (18 months old)
- 2,000 paying customers
- Growing 30% month-over-month
- Runway: 18 months

**Business Priorities (ranked):**

1. Customer retention (churn is #1 risk)
2. Reliability (downtime = customers leave)
3. Speed to market (competitive pressure)
4. New features (differentiation)
5. Code quality (important but not top priority)
6. Performance (acceptable unless it affects retention)

**Key Metrics:**

- Monthly churn rate: 5% (goal: <3%)
- Customer satisfaction: 4.2/5 (goal: >4.5/5)
- Uptime: 99.5% (goal: 99.9%)
- Feature velocity: 2 major features/month

**Competitive Context:**

- Main competitor: Established player (10 years old)
- Our advantage: Modern UI, better mobile experience
- Our disadvantage: Fewer features, smaller team
- Differentiation strategy: Better UX, faster innovation

**Trade-off Philosophy:**

"Ship fast, fix later IF customers complain.

Perfect code doesn't matter if we run out of runway."
</context>
```

**Why User/Audience helps a model**

1. Quality vs. Speed Decisions:
Scenario: User asks for new feature

**Without context:**
Model: "I'll build comprehensive solution with:

- Full test coverage (unit, integration, e2e)
- Edge case handling (all scenarios)
- Performance optimization
- Extensive documentation..."
[Takes 3 weeks, misses market opportunity]

**With context:**
Model: "Given 'ship fast, fix later' philosophy and competitive pressure:
WEEK 1:

- Core functionality (happy path)
- Basic error handling
- Key tests (critical flows only)
- Deploy to staging
WEEK 2

- Customer beta (get feedback fast)
- Fix critical issues found
- Deploy to production

LATER (if customers use it):

- Edge cases
- Optimization
- Comprehensive tests
This matches startup stage (runway concern) and competitive
pressure (need speed). Quality improves based on actual usage."

**CONTEXT justified rapid iteration! ✓**

2.What to Optimize:

**Scenario:** Performance optimization request

**Without context:**
Model: "I'll optimize everything:

- Database queries (add indexes)
- API responses (add caching)
- Frontend (code splitting, lazy loading)
- Images (compression, WebP)..."
[Weeks of work, minimal business impact]

**With context:**
Model: "Business priority #1 is retention, driven by satisfaction.
User pain point: 'Slow loading frustrates me'

- Initial page load (first impression!)
- Common operations (daily pain points!)
- Mobile experience (60% of users!)
- DON'T OPTIMIZE (doesn't affect retention):

- Admin features (internal use, doesn't affect customers)
- Reports (weekly use, patience higher)
- Edge cases (rarely encountered)
- Focus optimization where it reduces churn."

**CONTEXT focused effort on business impact! ✓**

3.Build vs. Buy:

**Scenario:** User asks for email sending capability

**Without context:**
"I'll build custom email service with:

- Template engine
- Queue system
- Retry logic
- Analytics..."
- [Reinventing wheel, burning runway]

**With context:**
Model: "Given startup stage (18-month runway) and priority on
speed to market, recommend:

USE: SendGrid or AWS SES (battle-tested, $50/month)

Why:

- Saves 2-3 weeks development time
- Proven reliability (99.9% uptime built-in)
- Focus team on differentiation (better UX)
- Low cost vs. developer time
- Build custom ONLY if email becomes competitive advantage
(unlikely for your business model)."

**CONTEXT drove build vs. buy decision! ✓**

## When CONTEXT Hurts a Model (Bad Examples)

**CONTEXT hurts a model when it:**

1. Is too vague (not actionable)
2. Is too much (overwhelming)
3. Is irrelevant (why are you telling the model this?)
4. Conflicts with constraints (confusing)

### Problem 1: Vague Context

CONTEXT That Doesn't Help:

```text

<context>

We're a technology company focused on innovation.

Our users value quality and good user experience.

We want to use best practices and modern approaches.

Our team is skilled and dedicated.

We operate in a competitive market.
/context>
```

**Why this doesn't help me:**

Questions a model still has:

- "Technology company" doing what? (SaaS? E-commerce? Internal tools?)
- "Users value quality" how? (Fast? Bug-free? Simple?)
- "Best practices" which ones? (Security? Performance? Accessibility?)
- "Skilled team" in what? (Frontend? Backend? DevOps?)
- "Competitive market" with whom? (What differentiates you?)

**Result: Generic information that doesn't inform ANY decision.**

**Better Version:**

```text

<context>

**Company:** B2B SaaS (project management for construction companies)

**Users:** Construction project managers (non-technical, field workers)

**User Value:** Reliability (#1), Mobile experience (#2), Simplicity (#3)

**Team:** 3 full-stack developers (React/Node.js), 1 designer

**Market:** Competing with Procore (established) and Buildertrend

**Differentiation:** Better mobile offline support, simpler interface
</context>
```
**Why this helps:**

- Specific users (construction PMs, non-technical)
- Clear priorities (reliability > mobile > simplicity)
- Concrete team skills (React/Node.js)
- Known competitors (can research their approach)
- Clear differentiation (offline mobile, simplicity)

**Model can make decisions based on this! ✓**

### Problem 2: Too Much Context (Information Overload)

CONTEXT That Overwhelms:

```text

<context>

**Company History:**

Founded in 2010 by John Smith and Jane Doe in a garage in Palo Alto.
Initial funding: $50K from friends and family. First product launched 2011.
Series A in 2012 ($2M from Sequoia). Pivoted in 2013 from B2C to B2B.
Series B in 2015 ($10M from Andreessen Horowitz). Acquired competitor
in 2017. Series C in 2019 ($50M from Tiger Global). IPO planned for 2026.

**Team History:**

Original CTO left in 2014, replaced by current CTO who worked at Google
for 7 years. Engineering team grew from 3 to 50 people between 2015-2020.
Hired VP Engineering in 2018 from Facebook. Reorganized into pods in 2020.
Adopted Agile methodology in 2021. Started using Jira in 2022.

**Technology History:**

Started with PHP/MySQL, migrated to Python in 2013, then Node.js in 2016.
Moved from monolith to microservices in 2018. Adopted Kubernetes in 2019.
Migrated from AWS to GCP in 2020, then back to AWS in 2021. Started using
TypeScript in 2022. Considering Rust for performance-critical services.

**Customer History:**
First customer: Small construction company in San Jose (2011).
First enterprise customer: Fortune 500 company (2015).
International expansion started 2017 (Canada first, then EU).
Enterprise customers now 60% of revenue. SMB still 40%.
[... 5 more pages of historical context ...]
</context>
```
**Why this overwhelms a model:**

**Problems:**

- 90% is historical (not relevant to current decisions!)
- Buried in detail (can't find what matters!)
- No clear relevance (why does the model need to know this?)
- Takes forever to parse (cognitive overload!)

**Result: Model will either ignore it all, or waste time finding relevant parts.**

**Better Version (Focused):**

```text

<context>

**Current State (2024):**

- Stage: Series C startup, 50 employees
- Technology: Node.js/TypeScript microservices on AWS + Kubernetes
- Customers: 60% enterprise, 40% SMB
- Team: 20 engineers (70% senior, 30% mid-level)

**Key Constraint from History:**

- Legacy PHP API still running (20% of customers not migrated yet)
- Must maintain backward compatibility until 2025-Q2

**Relevant Background:**

- Migrated back to AWS from GCP in 2021 (team AWS-expert now)
- Adopted TypeScript 2022 (all new code must be TypeScript)
[Only what's relevant to current decisions]
</context>
```

**Why this works:**

- Current state (what matters now)
- Key constraint (backward compatibility requirement)
- Relevant history (affects current decisions)
- Concise (not overwhelming)

**Model can use this! ✓**

### Problem 3: Irrelevant Context

CONTEXT That Doesn't Matter:

```text

context>
**Office Details:**`

- Located in WeWork, downtown San Francisco
- Office has standing desks, ergonomic chairs
- Free snacks (fruit, granola bars, coffee)
- Gym membership provided
- Dog-friendly office (3 dogs usually present)

**Team Lunch Preferences:**

- Taco Tuesdays are popular
- CEO prefers Thai food
- Engineering team likes pizza
- Catered lunch on Fridays

**Company Culture:**

- Casual dress code
- Flexible hours (core hours 10am-3pm)
- Remote work Mondays
- All-hands meeting Fridays at 4pm
- Company retreats twice a year
</context>
```

**Why this is irrelevant:**

For code/system decisions, model doesn't care about:

- Office furniture
- Lunch preferences
- Dress code
- Company retreats
- None of this affects:
- Technology choices
- Architecture decisions
- Code quality
- Performance optimization

**Result:** Noise that distracts from relevant context.

**Better Version (Relevant):**

```text

<context>

**Work Patterns:**

- Core hours: 10am-3pm Pacific (affects deployment timing)
- Remote Mondays (team async on Mondays, sync Tue-Fri)
- All-hands Fridays 4pm (avoid Friday afternoon deployments)

**Team Dynamics:**

- Casual culture (clear documentation > formal processes)
- Flexible hours (async communication preferred)
- Dog-friendly (interruptions normal, design for context-switching)
`</context>`

**Why this is relevant:**

Core hours → Deploy during off-hours (after 3pm or before 10am)
Remote Mondays → Async communication patterns in code reviews
Friday all-hands → No risky deploys Friday afternoon
```

**Actually affects decisions! ✓**

### Problem 4: Context Conflicts with Constraints

CONTEXT That Contradicts MUST:

```text

<constraint priority="critical">

MUST: All PII encrypted at rest (AES-256)
MUST: HTTPS only in production
MUST: No API keys in code
</constraint>

<context>
**Speed is Critical:**
We're in a race to market. Competitors are 2 months ahead.
Need to ship fast, cut corners where possible.
Perfect security can come later if we survive.
Encryption is slow, avoid if possible.
</context>
```

**Why this is confusing:**

Contradiction:

- MUST says: Encrypt PII, HTTPS only, secure practices
- CONTEXT says: Cut corners, skip encryption, speed over security

Model’s confusion:

- Which wins? (MUST should win, but context suggests otherwise!)
- Is MUST actually flexible? (context implies it is!)
- Should I violate MUST? (context seems to encourage it!)

**Result:** Paralyzed by contradiction, or will make wrong call.

**Better Version (Aligned):**

```text

<constraint priority="critical">
MUST: All PII encrypted at rest (AES-256)
MUST: HTTPS only in production
MUST: No API keys in code
</constraint>

<context>
**Speed is Critical (Within Security Boundaries):**

- We're in competitive race (2 months behind).
- Need to ship fast WHERE SAFE:

MOVE FAST:

- UI iterations (safe to iterate)
- Non-security features (can refine later)
- Admin tools (internal use, lower risk)

NEVER COMPROMISE:

- Security (MUST constraints are absolute)
- PII handling (compliance requirement)
- Authentication (user trust critical)

Philosophy:
- "Fast but secure. Ship features quickly,
but security is non-negotiable foundation."
</context>
```

**Why this works:**

- CONTEXT respects MUST constraints ✓
- Clarifies where speed is ok (UI, features) ✓
- Clarifies where it's not ok (security) ✓
- No contradiction ✓

**Aligned, not conflicting! ✓**

## The CONTEXT Writing Pattern

### Good CONTEXT follows this structure

```text

<context scope="[domain]">

**Current State:**
[Who, what, where we are NOW]

**Key Constraints:**

[Important limitations from environment/history]

**Priorities (ranked):**

1. [Highest priority]
2. [Second priority]
3. [Third priority]

**Decision Framework:**

When [X] conflicts with [Y], prioritize [X] because [reason].

**Success Criteria:**

[What good looks like - measurable if possible]
[Only what's relevant to decisions]
</context>
```

### Applying This Pattern

#### **Example 1: Technical Context**

```text

<context scope="technical-environment">

**Current State:**

- Stack: Node.js 20 + Express + PostgreSQL 14 on AWS Lambda
- Scale: 5K users, 100 concurrent peak
- Team: 3 developers (2 senior Node.js, 1 mid-level learning serverless)

**Key Constraints:**

- Lambda 15-second timeout (limits long operations)
- Cold start concern (first request can be slow)
- RDS connection limit: 100 max

**Priorities (ranked):**

1. Reliability (uptime > performance)
2. Development speed (small team, many features)
3. Cost efficiency (startup budget)

**Decision Framework:**

- When reliability conflicts with performance → reliability wins
- When simplicity conflicts with optimization → simplicity wins (small team)
- When build vs buy → buy unless core differentiation

**Success Criteria:**

- 99.9% uptime
- <200ms API response (p95)
- <2 hours to deploy new feature
</context>
```

#### **Example 2: User Context**

```text

<context scope="users-and-audience">
**Current State:**

- Users: Restaurant managers (35-60 years, non-technical)
- Usage: During service hours (11am-2pm, 5pm-9pm)
- Devices: 70% mobile (often in kitchen/floor), 30% desktop (office)

**Key Constraints:**

- Busy during service (no time for complex operations)
- Variable internet (some restaurants have spotty wifi)
- High stress environment (errors are very costly)

**Priorities (ranked):**

1. Simplicity (can use while busy)
2. Reliability (errors = lost orders)
3. Speed (impatient during rush)

**Decision Framework:**

- When feature complexity conflicts with simplicity → simplicity wins
- When offline support costs dev time → offline wins (spotty wifi common)
- When mobile UX conflicts with desktop → mobile wins (70% usage)

**Success Criteria:**

- 90% task completion without help
- <3 minutes per common task
- Works offline for critical operations
</context>
```

#### **Example 3: Business Context**

```text

<context scope="business-priorities">

**Current State:**

- Stage: Early-stage startup (Series A, 12-month runway)
- Customers: 500 paying (growing 20%/month)
- Revenue: $50K MRR, goal: $100K by end of year

**Key Constraints:**

- Limited runway (must hit $100K MRR or raise more)
- Small team (can't do everything)
- Competitive market (2 well-funded competitors)

**Priorities (ranked):**

1. Revenue growth (survival depends on it)
2. Customer retention (churn kills growth)
3. Feature velocity (competitive pressure)
4. Code quality (important but not top 3)

**Decision Framework:**

- When quality conflicts with speed → ship fast, fix if customers complain
- When build vs buy → buy unless core differentiation
- When feature request conflicts with revenue → revenue wins

**Success Criteria:**

- Hit $100K MRR by year end
- Churn rate <5% monthly
- Ship 2 major features per month
</context>
```

## Common CONTEXT Mistakes

### Mistake 1: History Dump (Not Current State)

**Problem:**

```text

<context>

Founded in 2010. First product PHP/MySQL. Migrated to Python 2013.
Migrated to Node.js 2016. Adopted microservices 2018. Moved to AWS
2019. Added Kubernetes 2020. Started TypeScript 2021...
[Endless history, no current state]
</context>
```

**Solution:**

```text

<context>

**Current State (2026):**
Node.js/TypeScript microservices on AWS + Kubernetes

**Relevant History:**
Legacy PHP API still running (migrate by 20265-Q2)
</context>
```
**Focus on NOW, include history ONLY if it affects current decisions.**

### Mistake 2: Everything Is High Priority

**Problem:**

```text

<context>

**Priorities:**

- Security is critical
- Performance is critical
- User experience is critical
- Code quality is critical
- Speed to market is critical
- Cost efficiency is critical
- Scalability is critical
[Everything is critical = nothing is prioritized]
</context>
```

**Solution:**

```text

<context>
**Priorities (ranked, when they conflict):**

1. Security (compliance requirement, non-negotiable)
2. Reliability (SLA commitment to customers)
3. User experience (competitive differentiation)
4. Speed to market (acceptable if 1-3 maintained)
5. Cost efficiency (optimize but not at expense of 1-4)

**Trade-off Philosophy:**

Security and reliability are never compromised.
UX is our competitive advantage (protect it).
Speed and cost are flexible within above constraints.
</context>
```
**Ranked priorities with explicit trade-off guidance.**

### Mistake 3: No Decision Framework

**Problem:**

```text

<context>

We value both quality and speed.
We want happy customers and efficient development.
We need reliability and innovation.
</context>
```
**No guidance when these conflict!**

**Solution:**

```text

<context>

**Decision Framework:**
WHEN quality conflicts with speed:

Ship fast for features (can iterate)
Never compromise for security (can't fix breaches)

WHEN customer requests conflict with roadmap:

If request from >3 customers → prioritize
If request from <3 customers → roadmap wins

WHEN technical debt slows development:

If velocity drops >30% → sprint to fix debt
If velocity drops <30% → keep shipping, fix gradually
</context>
```
**Explicit guidance for common conflicts.**

### Mistake 4: Vague Audience Description

**Problem:**

```text

<context>

**Users:** Business professionals who value efficiency
</context>
```
**Too vague to inform decisions!**

**Solution:**

```text

<context>
**Users:**

- Role: Sales managers at B2B companies
- Age: 30-50
- Technical skill: Medium (comfortable with CRM, spreadsheets)
- Usage: Daily (2-3 hours/day)
- Device: 80% desktop (in office), 20% mobile (on the road)
- Pain point: "Too many tools, want everything in one place"
- Success metric: Reduce time on admin tasks by 50%
</context>
```
**Specific details that inform UI, complexity, and feature decisions.**

## Integration with MUST, SHOULD, and INTENT

How all four layers work together:

### Complete Example: Payment Processing

```text

MUST: Hard boundaries

<constraint priority="critical" scope="payments">
MUST: PCI DSS compliant (never store card numbers)
MUST: HTTPS only
MUST: 3D Secure authentication for EU transactions
MUST: Transaction logging (all attempts, even failed)
</constraint>

SHOULD: Preferences

<guideline priority="high" scope="payments">
SHOULD: Support Apple Pay and Google Pay (user convenience)
SHOULD: Save payment methods for returning customers
SHOULD: Provide receipt via email within 5 minutes

WHEN violating:

Document why (e.g., Apple Pay requires legal approval in some countries)
</guideline>

CONTEXT: Planning information

<context scope="payments">
**Current State:**

- Processing: Stripe (primary), PayPal (backup)
- Volume: 5K transactions/month, $200K total
- Users: 60% credit card, 30% PayPal, 10% other
- Geography: 70% US, 20% EU, 10% other

**User Patterns:**

- Peak: Monday mornings (subscription renewals)
- Cart abandonment: 15% (vs 20% industry average)
- Failed payments: 2% (mostly expired cards)

**Priorities:**

1. PCI compliance (legal requirement)
2. Low friction (reduce abandonment)
3. Failed payment recovery (retry expired cards)

**Decision Framework:**

- When compliance conflicts with UX → compliance wins
- When new payment method costs dev time → analyze user demand first
- When fraud prevention adds friction → err on side of prevention

**Success Criteria:**

- Cart abandonment <12%
- Failed payment rate <1.5%
- Zero PCI compliance violations
</context>

INTENT: The why

<intent scope="payments">

**Primary Goal:**
Secure, frictionless payment experience that builds customer trust.

**Why This Matters:**
Payment is moment of highest purchase anxiety. Any friction or
security concern = abandoned cart. Our conversion rate is 5%
above industry average—payment UX is competitive advantage.

**Success Looks Like:**

Customers feel confident entering payment info (trust).
Process completes in <30 seconds (friction-free).
Zero chargebacks from fraud (secure).
</intent>
```

### How a model uses all four layers

**Scenario:** User asks to add cryptocurrency payment option

- **MUST** tells a model: Must maintain PCI compliance, HTTPS, logging

- **SHOULD** tells a model: Prefer methods that improve UX

- **CONTEXT** tells a model:
  Only 5K transactions/month (low volume)

  Users are 60% credit card, 30% PayPal (traditional methods)
  
  Low cart abandonment already (12% vs 15%)

- **INTENT** tells a model: Goal is trust and low friction

**Model’s recommendation:** "Given context (low volume, traditional user base) and intent (trust and low friction),

cryptocurrency adds complexity without clear user demand. Current payment mix (credit/PayPal) already achieves <12% abandonment.

**Recommend:** Wait until >50 customer requests OR competitor advantage appears. 

Resources better spent on failed payment recovery (2% failure rate could be reduced)."

**All four layers informed this decision!**

## Checklist: Is My CONTEXT Well-Written

Before finalizing CONTEXT:

```text

Relevance

[ ] Directly informs decisions (not just background)
[ ] Current state focused (minimal history)
[ ] Actionable information (I can use this)

Specificity

[ ] Concrete details (not vague generalities)
[ ] Measurable where possible (numbers, not adjectives)
[ ] Named technologies/tools (not just "modern stack")

Priorities

[ ] Ranked order (when conflicts occur)
[ ] Explicit trade-offs (what wins when things conflict)
[ ] Success criteria defined

Conciseness

[ ] No information overload (focused on what matters)
[ ] No irrelevant details (office snacks, etc.)
[ ] Skimmable (Can the model find what it needs quickly)

Alignment

[ ] Doesn't conflict with MUST constraints
[ ] Supports SHOULD preferences
[ ] Connects to INTENT (explains why priorities exist)
```

## Key Takeaways

### **What Makes Good CONTEXT**

Good CONTEXT is:

1. Relevant (informs decisions, not just background)
2. Specific (concrete details, not vague)
3. Prioritized (ranked when conflicts occur)
4. Concise (focused on what matters)
5. Aligned (doesn't contradict constraints)

### Common Mistakes to Avoid

1. Vague ("We're a tech company") → Useless
2. Too much (10 pages of history) → Overwhelming
3. Irrelevant (office furniture) → Distracting
4. Conflicting (contradicts MUST) → Confusing
5. No priorities (everything is critical) → Unhelpful

### The CONTEXT Pattern

Every CONTEXT should have:

1. Current state (who/what/where NOW)
2. Key constraints (relevant limitations)
3. Ranked priorities (what wins when things conflict)
4. Decision framework (tie-breaker rules)
5. Success criteria (what good looks like)

Remember: CONTEXT Enables Better Decisions

**From a model’s perspective:**
CONTEXT tells a model:

- Who I'm serving (audience understanding)
- What environment I'm in (technical constraints)
- What matters most (priority guidance)
- How to decide (trade-off framework)

Good CONTEXT enables a model to:

- Make intelligent tradeoffs (informed decisions)
- Prioritize correctly (focus effort)
- Match solutions to audience (appropriate complexity)
- Avoid wasted work (optimize what matters)

**This is planning support, not rules.**

## What's Next

You've learned how to provide CONTEXT. Next:

- Section 5: Expressing INTENT (the "why" behind everything)
- Section 6: Verification Protocols (self-correction systems)
- Section 7: Common Pitfalls (what goes wrong)
- Section 8: Section 8: The Supremacy Clause and Evidence Reset Protocols (Belief Dynamics)

Each section builds on this foundation of informed decision-making.

END OF SECTION 4

Document Version: 1.0.0
Last Updated: 2026-02-27
Written from model perspective: What context actually helps vs. overwhelms from daily experience
Key principle: CONTEXT enables better decisions by providing relevant planning information







