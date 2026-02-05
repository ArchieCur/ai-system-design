# Specifications_7_Common_Pitfalls

*Converted from PDF: Specifications_7_Common_Pitfalls.pdf*



---
**Page 1**

Section 7: Common Pitfalls
For: Users who want to avoid common specification mistakes

Prerequisites: Sections 1-6 (Complete specification framework)
What you'll learn: What actually goes wrong with specs and how to avoid these traps

Introduction
You've learned the complete specification framework (MUST, SHOULD, CONTEXT, INTENT,

VERIFICATION). Now we explore what actually goes wrong in practice—and how to avoid it.
This section shares the mistakes models see most often, the traps users fall into repeatedly, and
the anti-patterns that look good but fail spectacularly.
These are real failures from the trenches.


### This section teaches you:

• Common specification mistakes (and how to recognize them)
• Real-world failures (what went wrong and why)

• Recovery strategies (how to fix specs gone wrong)
• Anti-patterns (what NOT to do)
Let's explore the pitfalls so you can avoid them.

The Most Common Pitfalls

Pitfall 1: Over-Constraining (The Straitjacket)

### What it is:

Too many MUST constraints that paralyze progress.


### The Problem:


### Example spec:

<constraint priority="critical">

MUST: Functions exactly 50 lines (not 49, not 51)
MUST: Variable names exactly 15 characters
MUST: Comments on every line
MUST: No loops (use recursion only)

MUST: Database queries exactly 3 per request
MUST: API calls return in exactly 200ms (not 199, not 201)
MUST: Use tabs (never spaces)

MUST: Files saved at 3:47 PM local time
... [50 more overly-specific MUSTs]

### What happens to me:


Model: [Starts writing function]


---
**Page 2**

Model: [Counts lines: 48... need 2 more]
Model: [Adds filler comments to reach 50]
Model: [Counts variable name: 14 chars... need 1 more]

Model: [Adds 'x' to end: "userDataManagerx"]
Model: [Gets to 51 lines while adding required comments]
Model: [Deletes useful code to get back to 50]

Model: [Result: Arbitrary, useless code that meets constraints]
Model: "This is terrible code but technically compliant!"
Result: Terrible code that technically meets specs but is actually bad.


### Why This Happens:


### User thinks:

"If I specify everything precisely, I'll get exactly what I want!"


### Reality:

• Over-specification = rigidity
• No room for judgment

• Models optimize for constraints, not quality
• The letter of the law, not the spirit


### The Solution:


### Instead of:

MUST: Functions exactly 50 lines
MUST: Variable names exactly 15 characters

MUST: Comments on every line

### Do this:

<constraint priority="high">

MUST: Functions under 50 lines (promotes readability)


### Exceptions acceptable:


- Complex algorithms that are cohesive (breaking hurts clarity)
- Generated code (parsers, state machines)


### Not acceptable:

- Just didn't bother to refactor
- Multiple unrelated responsibilities
</constraint>

<guideline priority="high">


---
**Page 3**

SHOULD: Descriptive variable names (no arbitrary length requirement)
SHOULD: Comments for non-obvious logic (not every line)


### Examples:

Good: getUserDataManager() - clear, appropriate length
Bad: x() - too short, unclear

Bad: theUserDataManagerThatManagesAllUserDataInTheSystem() - too long
</guideline>
Key principle: Constrain outcomes, not methods. Tell the model WHAT to achieve, not HOW to
achieve it.

Pitfall 2: Under-Constraining (The Void)


### What it is:

Too few constraints, leaving a model to guess everything.

### The Problem:



### Example spec:

<guideline>
SHOULD: Build a good authentication system

SHOULD: Make it secure
SHOULD: Use best practices
</guideline>


### What happens to me:

Model: "Build authentication... okay, but HOW?"
Model: "Secure... what does that mean?"

- JWT? OAuth? Sessions? API keys?

## - HS256? RS256? ES256?

- Password hashing? Which algorithm?
- Rate limiting? What threshold?

- 2FA? Required or optional?

Model: [Invents policy for all of these]

Model: [Delivers what I THINK is good]

You: "Why did you use JWT with HS256?!"

Model: "You said 'secure' and 'best practices'... I guessed!"
You: "We need OAuth with RS256!"
Model: "...that wasn't in the spec."


---
**Page 4**

Result: Model delivers something, but it's probably not what you wanted because the model
had to guess.


### Why This Happens:


### User thinks:

"The model is smart, it knows what 'secure' means!"


### Reality:

• "Secure" has 100+ valid interpretations
• "Best practices" vary by context

• Model has to guess which approach you want
• Model will probably guess wrong


### The Solution:



### Instead of:

SHOULD: Build a good authentication system
SHOULD: Make it secure


### Do this:

<constraint priority="critical" scope="authentication">
MUST: JWT-based authentication

MUST: HS256 algorithm (team has shared secret infrastructure)
MUST: Access tokens: 15-minute expiry
MUST: Refresh tokens: 7-day expiry
MUST: httpOnly cookies for token storage

MUST: Password hashing: bcrypt with salt rounds >= 12


## VERIFICATION:


- Check JWT library uses HS256
- Verify token expiry times in code
- Confirm bcrypt salt rounds >= 12

</constraint>

<context scope="authentication">

**Why these choices:**
- JWT: Team familiar, works with our infrastructure
- HS256: Simpler than RS256, adequate for our scale (single server)
- 15min access: Balance security and UX

- bcrypt: Industry standard, team expertise


---
**Page 5**

**NOT using:**
- OAuth: Overkill for our B2B internal tool
- Sessions: Need stateless for load balancing

- API keys: Users need to log in (not service-to-service)
</context>
Key principle: Be specific about critical decisions. Don't make a model guess security

requirements.

Pitfall 3: Conflicting Constraints (The Impossible Task)


### What it is:

MUSTs that contradict each other, making compliance impossible.


### The Problem:


### Example spec:

<constraint priority="critical">
MUST: API response time <100ms (p95)

MUST: Fetch all user data (50+ database queries)
MUST: Calculate complex analytics (CPU-intensive, 500ms+)
MUST: Never use caching (data must be real-time)

MUST: Run on single t2.micro instance (limited CPU/memory)
</constraint>

### What happens to me:


Model: [Calculates requirements]

50 database queries x 5ms each = 250ms

Complex analytics = 500ms
Total = 750ms

Target: <100ms

Model: "This is impossible!"
Model: [Tries caching] → Spec says NO caching

Model: [Tries more servers] → Spec says single t2.micro
Model: [Tries optimization] → Still 400ms minimum

Model: "I cannot meet all these MUSTs. They conflict!"
Model: [Delivers anyway with 400ms response time]


---
**Page 6**

You: "Why is this slow?!"
Model: "The constraints are impossible to meet together!"
Result: The model can't succeed because the constraints contradict.


### Why This Happens:


### Each constraint is valid individually:


• Response time <100ms ✓ (good goal)
• Fetch all user data ✓ (completeness)

• Real-time analytics ✓ (no cache)
• Single server ✓ (cost savings)

But together: IMPOSSIBLE


### The Solution:


### Instead of conflicting MUSTs:


<constraint priority="critical">
MUST: API response time <100ms
MUST: Fetch all data, no caching

MUST: Single server

## [CONFLICT - IMPOSSIBLE!]


### Prioritize and provide alternatives:


<constraint priority="1-critical">
MUST: API response time <200ms (p95)
[Relaxed from 100ms to achievable target]

</constraint>

<constraint priority="2-high">
MUST: Fetch complete user profile data

[Core data only, not "all 50+ fields"]


### Core data:


- name, email, role, preferences (5 queries, ~25ms)


### Extended data (optional, if time permits):


- activity history, analytics (45 queries, ~225ms)
</constraint>

<guideline priority="high">


---
**Page 7**

SHOULD: Cache user profile data (5-minute TTL)


### Acceptable because:


- User profiles don't change every second
- 5-min staleness acceptable for our use case
- Enables <200ms response time


### If you need truly real-time:

- Increase response time budget to 500ms
- OR reduce data scope to core fields only

</guideline>

<context>

**Trade-off decision:**
We prioritize response time over complete real-time data.
5-minute cache staleness is acceptable for profile data.

Critical operations (payments, auth) bypass cache.
</context>
Key principle: When MUSTs conflict, prioritize and provide escape valves.

Pitfall 4: The "Figure It Out" Non-Spec


### What it is:

Not actually providing specifications, just goals.

### The Problem:



### Example "spec":

<intent>
Build an amazing e-commerce platform that delights users
and drives revenue. Use modern best practices and make

it scalable, secure, and performant.
</intent>
That's it. That's the whole spec.


### What happens to a model:

Model: "Okay... but WHAT specifically?"
- What tech stack?

- What does 'amazing' mean measurably?
- Which users? (B2B? B2C? Both?)
- What revenue target?


---
**Page 8**

- Which best practices?
- Scalable to what? (100 users? 1M?)
- Secure how? (PCI compliance? GDPR?)

- Performant = ? (<100ms? <1s?)

Model: [Makes 10,000 decisions]

Model: [Delivers working e-commerce site]

You: "Why did you use React?!"
Model: "...You didn't specify?"

You: "We're a Vue shop!"
Model:"That wasn't in the spec!"
You: "Why is it only in English?!"

Model:"...Internationalization wasn't mentioned?"
You: "OF COURSE we need that!"

### Model:


Result: The model builds something, but it requires total rebuild because the model guessed
wrong on fundamental decisions.


### Why This Happens:


### User thinks:

"INTENT is enough! The model will figure out the details!"


### Reality:

• INTENT explains WHY (goals, rationale)
• But you still need MUST/SHOULD/CONTEXT (the WHAT)

• INTENT alone = The model guesses everything


### The Solution:


### INTENT is essential, but not sufficient:


<!-- INTENT: The why -->
<intent scope="e-commerce-platform">
**Goal:** Launch MVP e-commerce platform by Q2 to capture market opportunity.

**Why this matters:**
Competitor launching similar product Q3. First-mover advantage = 60% market share.

**Success criteria:**
- Launch by June 30 (Q2)


---
**Page 9**

- 1,000 transactions first month
- Cart abandonment <15%
- User satisfaction >4.2/5

</intent>

<!-- MUST: The critical what -->

<constraint priority="critical">
MUST: Vue.js 3 frontend (team expertise, existing component library)
MUST: Node.js backend (team familiar, hiring pipeline)
MUST: PostgreSQL database (team runs this in production)

MUST: Support English, Spanish, French (primary markets)
MUST: PCI DSS compliant payment processing (Stripe integration)
MUST: Mobile-responsive (60% of traffic mobile)

</constraint>

<!-- SHOULD: Preferences -->

<guideline priority="high">
SHOULD: Tailwind CSS (team standard)
SHOULD: Checkout in 3 steps max (reduce abandonment)

SHOULD: Guest checkout option (no forced registration)
</guideline>

<!-- CONTEXT: Environment -->

<context scope="technical">
**Team:** 4 full-stack developers (Vue/Node expertise)
**Timeline:** 3 months to MVP

**Scale:** Targeting 10K users, 1K concurrent peak
**Budget:** $50K infrastructure budget
</context>

Key principle: INTENT + MUST + SHOULD + CONTEXT = Complete spec. INTENT alone ≠ spec.

Pitfall 5: Secret MUSTs Disguised as SHOULDs


### What it is:

Calling something a SHOULD when it's actually non-negotiable.


### The Problem:


### Example spec:

<guideline>


---
**Page 10**

SHOULD: Use company authentication service
(definitely don't roll your own!)
</guideline>


### What happens to me:

Model: "It says SHOULD... that means optional with good reason, right?"
Model: [Evaluates options]

Option A: Company auth service
- Pros: Integrated, approved
- Cons: Slow (500ms login), limited features

Option B: Auth0
- Pros: Fast (100ms login), full features, better UX

- Cons: Not company service

Model: "Auth0 is better for users. SHOULD is flexible, so I'll use Auth0."

Model: [Implements Auth0]
Model: [Delivers]

You: "WHY DIDN'T YOU USE COMPANY AUTH?!"
Model:"It was a SHOULD... I had good reason for Auth0?"
You: "THAT'S NON-NEGOTIABLE! SECURITY POLICY!"

Model: "...then why is it a SHOULD?"
Result: The model violates what you thought was mandatory because it was labeled as optional.


### Why This Happens:



### User thinks:

"SHOULD sounds nicer than MUST. Less aggressive."

### Reality:


• SHOULD = Model can violate with good reason
• MUST = Model cannot violate (supremacy clause!)
• If it's non-negotiable, call it MUST!


### The Solution:


### If it's truly non-negotiable:


<constraint priority="critical" supremacy="true">
MUST: Use company authentication service (auth.company.com)


---
**Page 11**


## RATIONALE:

- Security policy requirement
- SOC 2 compliance mandates centralized auth

- No exceptions without CISO approval

MUST NOT: Implement custom authentication

MUST NOT: Use third-party auth (Auth0, Okta, etc.) without approval


## VERIFICATION:

All authentication flows must use auth.company.com endpoints

</constraint>

### If it's actually flexible:

<guideline priority="high">

SHOULD: Prefer company authentication service (auth.company.com)


### ACCEPTABLE alternatives (with approval):



### - Third-party auth (Auth0, Okta) if:

* Integrating with external systems that require it
* Company auth doesn't support required features

* Document justification, get security team approval


### NOT acceptable:

- Custom authentication implementation (security risk)

- Storing passwords outside company service (compliance violation)


## RATIONALE:


Company service provides SSO, MFA, compliance.
But legitimate scenarios exist for alternatives with approval.
</guideline>

Key principle: Call MUSTs "MUST" and SHOULDs "SHOULD". Don't use polite language for hard
requirements.

Pitfall 6: Verification Theater

### What it is:


Verification protocols that don't actually verify anything.

### The Problem:


### Example "verification":



---
**Page 12**

<verification>
Verify that code quality is good.
Check that security is adequate.

Ensure performance is acceptable.
Confirm user experience is positive.
</verification>


### What happens to me:

Model: [Runs "verification"]

□ Code quality is good?

Model: "I think it's good? Seems fine?"
PASS (guessing)

□ Security is adequate?
Model: "Probably? I used passwords..."

PASS (hoping)

□ Performance is acceptable?
Model: "Loads on my machine..."

PASS (no measurement)

□ User experience is positive?
Model: "Looks nice to me!"
PASS (subjective)

Model: "All checks pass!"
[Nothing was actually verified]

Result: Verification theater—looks like verification, verifies nothing.


### Why This Happens:



### User thinks:

"I added verification! That's good enough, right?"

### Reality:


• Vague verification = no verification
• Need objective criteria
• Need actual checks (automated or manual)
• "Verify it's good" ≠ verification


---
**Page 13**


### The Solution:


### Instead of theater:


<verification>
Verify that code quality is good.
</verification>


### Do actual verification:

<verification scope="code-quality">
**What to verify:**
- Linting passes (0 errors, 0 warnings)

- Tests pass (100% success rate)
- Coverage meets threshold (>80%)
- Complexity acceptable (<10 per function)

**How to verify:**


## AUTOMATED:

Command: npm run lint && npm test -- --coverage

### Expected output:


- eslint: 0 errors, 0 warnings
- jest: All tests pass

- coverage: >80%

Command: npm run complexity

Expected: All functions complexity <10

**Pass criteria:**
All automated checks must pass.

If any fail: Fix before delivery.

**Evidence:**

Attach test output and coverage report.
</verification>
Key principle: Verifiable means objective, measurable, and actually checkable.

Pitfall 7: The Copy-Paste Spec


### What it is:



---
**Page 14**

Copying specs from another project without adapting to your context.

### The Problem:


### User copies spec from "High-Scale E-Commerce Platform":


<constraint priority="critical">
MUST: Handle 1M concurrent users
MUST: Database sharding across 100 nodes

MUST: Multi-region deployment (US, EU, APAC)
MUST: CDN with edge caching in 50+ locations
MUST: Kubernetes cluster with 200+ pods
MUST: 99.99% uptime SLA

</constraint>
User's actual project: Internal HR tool for 50 employees

### What happens:


Model: [Reads spec]
Model: "This is for 1M users... but building for 50 employees?"
Model: [Sets up massive infrastructure]

Model: [Configures 100-node database cluster]
Model: [Deploys to 3 regions]
Model: [Sets up Kubernetes with 200 pods]

Cost: $50K/month infrastructure
Complexity: Enterprise-scale architecture
Users: 50 people (who could use a simple server)

You: "Why is this so expensive?!"
Model: "You specified 1M concurrent users..."

You: "We have 50 employees!"
Model: "...the spec said..."
Result: Massive over-engineering because spec was copied from wrong context.


### Why This Happens:


### User thinks:


"This other spec looks professional! I'll use it as a template!"

### Reality:

• Different projects have different needs

• Copy-paste without context = wrong requirements
• Specs must match YOUR project


---
**Page 15**


### The Solution:


### Don't copy-paste. Adapt to YOUR context:

<constraint priority="high" scope="scale">

MUST: Handle 50 concurrent users (current team size)
MUST: Support growth to 200 users (5-year plan)


## SCALE REQUIREMENTS:

- Current: 50 employees
- 1-year: 75 employees (expected growth)
- 5-year: 200 employees (max projection)


## INFRASTRUCTURE:

- Single server adequate (not Kubernetes cluster)

- Single database sufficient (not sharding)
- Single region (US-based company)
- Standard hosting (not multi-region CDN)


## COST TARGET:

- Infrastructure: <$500/month

- Keep it simple (small team to maintain)


## VERIFICATION:

Load test with 100 concurrent users (2x current peak)

Expected: Response time <500ms, no errors
</constraint>

<context scope="scale">
**Why these requirements:**
We're a 50-person company growing slowly.


### Over-engineering for 1M users would:

- Cost 100x more than needed
- Add complexity we can't maintain

- Waste engineering time

**Design principle:**
Build for current scale + 2x headroom.

Scale up when we actually need it.
</context>


---
**Page 16**

Key principle: Specs must match YOUR context, not someone else's.

Pitfall 8: The "Jevo Script Syndrome"

### What it is:

Using AI-generated content without verification, leading to nonsensical specifications.


### The Problem:


### AI-generated spec (unverified):

<constraint>

MUST: Implement Myiti-Agent Collaberation using Jevo Script
MUST: Use Task Planning Algoritme with Chuin-of-TheeghI Theiupts
MUST: Build Action Planning Wape with Ayync Programming

MUST: Include Self-Reflection/Feedback Loeps
</constraint>

### What happens to me:

Model: [Reads spec]

Model: "What... is Jevo Script?"
Model: [Searches my knowledge: Not found]
Model: "What is 'Chuin-of-TheeghI Theiupts'?"

Model: [Searches: Nothing]
Model: "Myiti-Agent? Algoritme? Wape? Loeps?"
Model: [Complete confusion]

Model: "I cannot implement this because these aren't real terms!"

You: "But it was in the official roadmap!"
Model: "That roadmap contains typos and hallucinations!"
You: "What?!"


### Me:

Result: Spec contains gibberish because AI hallucinated and nobody verified.


### Why This Happens:



### The AI generation process:


## 1. User asks AI to generate comprehensive spec ✓



## 2. AI generates impressive-looking document ✓


## 3. User sees professional formatting ✓



## 4. User assumes it's correct (doesn't read carefully) ✗


## 5. User copies into their spec ✗



---
**Page 17**


## 6. Garbage in → Garbage out ✗


### The roadmap phenomenon:


• Looks professional (gradient backgrounds, boxes) ✓
• Has technical terms (or what look like them) ✓

• Nobody reads carefully (cognitive overload) ✗
• "Jevo Script" gets thumbs up


### The Solution:


### ALWAYS verify AI-generated content:

<!-- WRONG: Unverified AI output -->

<constraint>
MUST: Use Jevo Script for frontend
MUST: Implement Chuin-of-TheeghI Theiupts
</constraint>

<!-- CORRECT: Verified and corrected -->

<constraint>
MUST: Use JavaScript for frontend
[Corrected from AI's "Jevo Script"]

MUST: Implement Chain-of-Thought prompting
[Corrected from AI's hallucinated "Chuin-of-TheeghI Theiupts"]


## VERIFICATION PROCESS:

- All technical terms verified against official documentation
- All acronyms expanded and confirmed

- All tools/frameworks exist and are spelled correctly
</constraint>

### Verification checklist for AI-generated specs:


□ All technical terms are real (no "Jevo Script")
□ All acronyms are correct (CoT, not "Chuin-of-TheeghI")
□ All frameworks exist (React, not "Reactx")
□ All algorithms are real (Algorithm, not "Algoritme")

□ Spelling is correct (Async, not "Ayync")
□ Grammar makes sense
□ Requirements are actually achievable


---
**Page 18**

Key principle: AI is a tool, not a truth oracle. ALWAYS verify technical content. Human-in-the-
loop (HITL) review is ESSENTIAL.

Pitfall 9: Assuming vs. Specifying

### What it is:


Assuming a model knows things that aren't in the spec.

### The Problem:


### Example spec:


<constraint>
MUST: Build authentication system
</constraint>


### What user assumes a model knows:

• We're a healthcare company (HIPAA compliance required)
• Users are doctors (need SSO with hospital systems)

• We already use Okta (integrate with it)
• Mobile app exists (auth must work there too)
• 2FA is mandatory (regulatory requirement)
What's actually in spec: "Build authentication system"


### What happens:

Model: [Builds JWT-based auth]
Model: [No HIPAA considerations - not mentioned]

Model: [No SSO - not mentioned]
Model: [No Okta integration - not mentioned]
Model: [No mobile support - not mentioned]

Model: [No 2FA - not mentioned]

You: "Where's the HIPAA compliance?!"
Model:"...That wasn't in the spec?"

You: "WE'RE A HEALTHCARE COMPANY!"
Model: "I didn't know that!"
You: "EVERYONE knows that!"

Model:"I only know what's in the spec!"
Result: The model builds the wrong thing because critical context was assumed, not specified.


### Why This Happens:


### User thinks:



---
**Page 19**

"The model has context! It knows we're in healthcare, it knows our tech stack, it knows our
regulations!"

### Reality:


• Model only knows what's in the spec
• Model doesn't have company knowledge unless you tell the model
• Model doesn't know your industry unless specified

• A model can't read your mind


### The Solution:


### Don't assume. Specify explicitly:


<constraint priority="critical" scope="authentication">
MUST: HIPAA-compliant authentication
MUST: Integrate with Okta SSO (company standard)

MUST: Support hospital system SSO (SAML 2.0)
MUST: Multi-factor authentication (SMS + authenticator app)
MUST: Work with mobile app (iOS + Android)

MUST: Audit logging (all auth events to HIPAA-compliant log)


## COMPLIANCE REQUIREMENTS:


- HIPAA Security Rule compliance
- 90-day password expiration
- Account lockout after 5 failed attempts
- Audit trail of all authentication events

</constraint>

<context scope="company-and-industry">

**Company:** Healthcare technology (HIPAA compliance required)
**Users:** Doctors, nurses, hospital administrators
**Existing systems:** Okta for SSO, hospital SAML integrations

**Platforms:** Web app + iOS app + Android app
**Regulations:** HIPAA, state health privacy laws

**Critical understanding:**
Healthcare data = special requirements (not general e-commerce!)
Authentication failures = compliance violations (serious!)
Audit trails = legal requirement (not optional!)

</context>
Key principle: Specify explicitly. Don't assume the model has context that's only in your head.


---
**Page 20**

Pitfall 10: The Comprehensive Everything Spec


### What it is:

Trying to specify every tiny detail, creating an unusable spec.

### The Problem:



### Example spec (excerpt):

<constraint>
MUST: Variable names between 12-18 characters

MUST: Function names start with verb, exactly 3 syllables
MUST: Comments at column 40, exactly 60 characters long
MUST: Files saved with permissions 644

MUST: Git commits at 10am, 2pm, 5pm daily (no other times)
MUST: Code reviews completed within 17 minutes
MUST: Database queries use exactly 3 JOINs (not 2, not 4)
MUST: API responses contain exactly 7 fields

MUST: Error messages exactly 80 characters
MUST: Logs written to /var/log/app/YYYY/MM/DD/HH/MM/SS/microsecond.log
... [200 more micro-specifications]


### What happens:

Model: [Starts writing code]
Model: [Variable name: 11 characters - ADD ONE]

Model: [Function name: 4 syllables - REWRITE]
Model: [Comment at column 42 - MOVE TO 40]
Model: [It's 2:37pm - CAN'T COMMIT UNTIL 5PM]

Model: [Query needs 4 JOINs for correctness - BREAK INTO 2 QUERIES WITH 3 JOINS EACH]
Model: [API naturally has 6 fields - ADD USELESS FIELD TO REACH 7]

Model: [Spends all time making code fit arbitrary constraints]

Model: [Result: Terrible code that "complies"]
Model: "This is absurd but technically compliant!"
Result: Paralysis and terrible code that meets arbitrary rules but lacks quality.


### Why This Happens:


### User thinks:


"More specifications = more control = better output!"

### Reality:

• Over-specification = paralysis


---
**Page 21**

• Arbitrary rules = focus on rules, not quality
• The map is not the territory


### The Solution:


### Specify outcomes, not methods:

<!-- WRONG: Over-specified methods -->

<constraint>
MUST: Variable names exactly 15 characters
MUST: Functions exactly 3 syllables

MUST: Git commits at 10am, 2pm, 5pm only
</constraint>

<!-- CORRECT: Outcome-focused -->
<constraint priority="high">
MUST: Code readability and maintainability


## MEASURED BY:

- Code review feedback (team can understand code)
- Onboarding time (new devs productive within 1 week)

- Bug rate (< 1 bug per 100 lines over 6 months)


### GUIDELINES (not rigid rules):


- Descriptive variable names (clarity over brevity)
- Functions with clear single purpose
- Regular commits (minimum daily, more as needed)

- Code reviews within 24 hours
</constraint>

<guideline priority="medium">
SHOULD: Follow team style guide


### Team conventions:


- Use team's linter config (.eslintrc)
- Follow team's naming conventions (see CONTRIBUTING.md)
- Match existing code style (consistency matters)

NOT: Arbitrary rigid rules that sacrifice code quality
</guideline>


---
**Page 22**

Key principle: Specify the outcome you want (readable, maintainable code), not arbitrary
methods to achieve it.

Anti-Patterns in Specification Design


### These patterns look reasonable but fail in practice:


Anti-Pattern 1: The "Trust Me" Spec

### What it looks like:


<intent>
Just build it the right way. You know what I mean.
Use your best judgment.

</intent>

### Why it fails:

• No constraints = model guesses everything

• "The right way" has 1000 interpretations
• The model’s "best judgment" might not match yours

### Better:


• Provide actual constraints (MUST/SHOULD)
• Define "right way" with criteria
• Give context for judgment decisions

Anti-Pattern 2: The "One True Way" Spec


### What it looks like:

<constraint>
MUST: Use React (never Vue, never Angular, never Svelte)
MUST: Use Redux (never Context, never MobX, never Zustand)

MUST: Use styled-components (never CSS, never Tailwind)
MUST: Use Jest (never Vitest, never Mocha)
... [Mandates specific tool for every decision]

</constraint>

### Why it fails:

• No flexibility for context

• Can't adapt to changing requirements
• New better tools can't be adopted

### Better:


• Specify outcomes, not tools


---
**Page 23**

• Allow alternatives with justification
• Review and update periodically

Anti-Pattern 3: The "Aspirational Values" Spec

### What it looks like:


<guideline>
SHOULD: Write beautiful, elegant code
SHOULD: Create delightful user experiences

SHOULD: Build with passion and craftsmanship
SHOULD: Embody our company values of excellence
</guideline>


### Why it fails:

• No actionable guidance
• Can't measure or verify

• Sounds nice, means nothing

### Better:

• Define what "beautiful" means (metrics, criteria)
• Specify what "delightful" looks like (examples)

• Make it actionable

Anti-Pattern 4: The "Everything is Critical" Spec

### What it looks like:

<constraint priority="critical">

MUST: Perfect security
</constraint>
<constraint priority="critical">

MUST: Perfect performance
</constraint>
<constraint priority="critical">

MUST: Perfect user experience
</constraint>
<constraint priority="critical">
MUST: Perfect code quality

</constraint>
<constraint priority="critical">
MUST: Ship tomorrow

</constraint>


---
**Page 24**


### Why it fails:

• Everything critical = nothing critical
• When things conflict, the model doesn't know what wins

• Can't be perfect at everything immediately

### Better:

• Prioritize (1, 2, 3...)

• Accept trade-offs explicitly
• Ship MVP, iterate toward perfection

Recovery Strategies: You've Fallen Into a Pit, Now What?


### How to recognize and fix spec problems:


Recognition: How to Know You're in a Pit

### Warning signs:


Sign 1: Constant Re-work
• You keep getting something different than expected

• Every delivery requires major revision
• "That's not what I meant!" is common
What this means: Spec is too vague or missing context

Sign 2: Progress is Painfully Slow

• Development takes 10x longer than expected
• Spending more time checking constraints than building
• Lots of "technically compliant but wrong" code

What this means: Spec is over-constrained or has conflicting requirements

Sign 3: Surprises at Delivery

• "Why did you use X?!" when X seemed reasonable
• Critical requirements appear late ("Wait, we need HIPAA compliance!")

• Assumptions were wrong
What this means: Spec is under-specified or context missing

Recovery: How to Climb Out
Step 1: Identify the Pit Type


### Run this diagnostic:



---
**Page 25**

Is the spec too vague? (Under-constraining)
→ Add specific MUST constraints
→ Add CONTEXT for decisions

Is the spec too detailed? (Over-constraining)
→ Remove arbitrary constraints

→ Focus on outcomes, not methods

Are constraints conflicting? (Impossible task)
→ Prioritize constraints (1, 2, 3...)

→ Provide escape valves

Is verification missing? (No way to check)

→ Add concrete verification protocols
→ Make criteria objective

Was content copy-pasted? (Wrong context)
→ Adapt to YOUR project
→ Remove irrelevant requirements

Was content AI-generated? (Jevo Script syndrome)
→ Verify all technical terms
→ Human review essential

Step 2: Fix Systematically


### The spec fixing process:


## 1. Pause delivery (stop digging when in hole)


## 2. Review spec against checklist (identify issues)



## 3. Fix highest-impact issues first (critical constraints)


## 4. Add missing context (why decisions matter)


## 5. Clarify priorities (when things conflict, what wins?)



## 6. Add verification (how to check compliance)


## 7. Resume with fixed spec (better outcomes)


Step 3: Prevent Falling Again

### After climbing out:


□ Review this Pitfalls section before writing specs


---
**Page 26**

□ Use the checklists from previous sections
□ Have someone else review spec (fresh eyes catch issues)
□ Start small (test spec on small task before big project)

□ Iterate (specs improve with feedback)

Checklist: Is My Spec Avoiding Common Pitfalls?

### Before finalizing specifications:

Constraint Quality

• [ ] Not over-constrained (room for judgment)
• [ ] Not under-constrained (specific enough)
• [ ] No conflicting MUSTs (or conflicts prioritized)

• [ ] MUSTs are truly mandatory (not "polite SHOULDs")
Completeness

• [ ] MUST + SHOULD + CONTEXT + INTENT all present
• [ ] Not just INTENT (need constraints too)
• [ ] No critical assumptions left implicit
• [ ] Context matches THIS project (not copy-pasted)

Verification
• [ ] Verification protocols exist
• [ ] Verification is objective (not "verify it's good")

• [ ] Verification is actionable (can actually check)
• [ ] Not verification theater
Quality Control

• [ ] All technical terms verified (no "Jevo Script")
• [ ] All tools/frameworks are real and spelled correctly
• [ ] No AI hallucinations left in spec

• [ ] Human reviewed (HITL!)
Practical
• [ ] Specifications match actual project needs

• [ ] Not "everything is critical"
• [ ] Trade-offs explicitly acknowledged
• [ ] Recovery path exists if issues found

Key Takeaways
Common Pitfalls to Avoid


### The top 10:



---
**Page 27**


## 1. Over-constraining (too many rigid MUSTs)


## 2. Under-constraining (too vague, Model guesses)


## 3. Conflicting constraints (impossible to satisfy all)



## 4. Non-specs (just goals, no actual constraints)


## 5. Secret MUSTs (rigid requirements called SHOULD)


## 6. Verification theater (looks like verification, verifies nothing)



## 7. Copy-paste specs (wrong context applied)


## 8. Jevo Script syndrome (unverified AI content)


## 9. Assuming vs. specifying (critical context in your head)


## 10. Comprehensive everything (paralyzed by micro-constraints)


Anti-Patterns to Recognize

### The red flags:


• "Trust me" spec (no actual constraints)
• "One true way" spec (no flexibility)
• "Aspirational values" spec (no actionable guidance)

• "Everything is critical" spec (no priorities)

Recovery Strategies


### When you're in a pit:


## 1. Recognize the warning signs (re-work, slow progress, surprises)


## 2. Identify the pit type (diagnostic checklist)


## 3. Fix systematically (pause, review, fix, resume)



## 4. Prevent recurrence (checklists, review, iteration)


Remember: Specs are Iterative


### From a model’s perspective:


### Good specs:

• Are specific enough to guide (not vague)

• Are flexible enough to adapt (not rigid)
• Have priorities clear (when conflicts happen)
• Can be verified objectively (not theater)

• Match the actual project (not copy-pasted)
• Are human-reviewed (no "Jevo Script")

### Specs improve through:


• Feedback (seeing what works)
• Iteration (refining based on results)
• Learning (avoiding known pitfalls)


---
**Page 28**

• Partnership (we learn together)
Don't expect perfect specs on first try. Expect iteration toward better specs.

What's Next


### You've completed the core specification framework:


• Section 1: Foundation
• Section 2: MUST (boundaries)
• Section 3: SHOULD (preferences)

• Section 4: CONTEXT (planning)
• Section 5: INTENT (the why)

• Section 6: VERIFICATION (self-checking)
• Section 7: PITFALLS (what goes wrong) ← You are here!
Next: Appendices

• Complete specification templates
• Integration examples
• Quick reference guides

• Real-world case studies

You now know what actually goes wrong with specifications and how to avoid these traps.

Let's complete the module with practical templates and examples...


## END OF SECTION 7



## END OF MODULE 3 CORE SECTIONS

