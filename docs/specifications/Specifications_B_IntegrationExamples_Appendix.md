# Appendix B: Integration Examples

**For:** Understanding how all five layers work together in practice

**When to use:** After learning individual layers, to see complete integration

**What you get:** Real-world examples showing MUST, SHOULD, CONTEXT, INTENT, and
VERIFICATION working as a cohesive system

## Introduction

You've learned each layer individually. Now see how they work together to create clear, actionable specifications that prevent common failures.

**This appendix shows:**

- Complete specifications with all 5 layers integrated
- How layers reinforce each other (not conflict)
- How layers answer different questions (WHAT vs WHY vs HOW)
- What good integration looks like (vs poor integration)

**Each example demonstrates:**

- All layers present (MUST, SHOULD, CONTEXT, INTENT, VERIFICATION)
- Layers aligned (no contradictions)
- Layers complete (answer all key questions)
- Integration that works

### Example 1: E-commerce Checkout Flow

**Scenario: Building checkout for fashion e-commerce startup**

**The Complete Integrated Specification**

All five layers working together

```text

Layer 1: MUST (Hard Boundaries)

<constraint priority="critical" scope="checkout-security">
MUST: PCI-DSS compliant payment processing (Stripe integration)
MUST: HTTPS only for all checkout pages
MUST: Cart data encrypted in session (AES-256)
MUST: Payment information never stored locally (Stripe handles)
MUST: 3D Secure authentication for transactions >$100

RATIONALE:

PCI compliance is legal requirement. Stripe handles most complexity,
but we still must ensure secure transmission and proper integration.

VERIFICATION:

- Stripe integration test: Process test payment successfully
- HTTPS check: All checkout URLs return 200 on HTTPS, redirect on HTTP
- Session encryption: Verify encrypted cart data in Redis
- 3DSecure: Test with high-value transaction, verify challenge appears
</constraint>

<constraint priority="critical" scope="checkout-performance">
MUST: Checkout completion time <60 seconds total (from cart to confirmation)
MUST: Each step loads in <2 seconds (p95)
MUST: Payment processing completes in <5 seconds (Stripe API call)

RATIONALE:

Research shows cart abandonment increases 10% for every additional second.
60 seconds total = aggressive but achievable with optimization.

VERIFICATION:

- Timed test: Complete checkout from cart to confirmation
- Load test: Measure step load times under realistic traffic
- Monitor Stripe API: P95 response time from Stripe
</constraint>

<constraint priority="critical" scope="checkout-functionality">
MUST: Support guest checkout (no forced account creation)
MUST: Save cart state for 7 days (logged in users)
MUST: Email order confirmation within 5 minutes
MUST: Inventory reserved during checkout (prevent overselling)

VERIFICATION:

- Guest checkout test: Complete purchase without creating account
- Cart persistence test: Add items, logout, login 3 days later (cart intact)
- Email test: Monitor SendGrid delivery (all confirmations <5 min)
- Inventory test: Concurrent purchase attempt of last item (second user gets "out of stock")
</constraint>

Layer 2: SHOULD (Flexible Preferences

<guideline priority="high" scope="checkout-ux">
SHOULD: Single-page checkout (all steps visible, no page reloads)
SHOULD: Real-time validation (inline errors as user types)
SHOULD: Save payment methods for logged-in users (optional, requires consent)
SHOULD: Autocomplete for address fields (Google Places API)
SHOULD: Mobile-optimized (large touch targets, minimal typing)

RATIONALE:

Single-page checkout reduces friction (fewer page loads = less abandonment).
Real-time validation catches errors early (better UX than submit-time errors).
Saved payment methods improve returning customer experience.

ACCEPTABLE EXCEPTIONS:

- Multi-page acceptable if single-page performs poorly (heavy JavaScript)
- Real-time validation can be submit-time if performance suffers
- Payment saving optional (privacy concerns for some users)

WHEN VIOLATING:

Document performance trade-off or privacy concern.
Ensure alternative approach still meets INTENT (frictionless checkout).
</guideline>

<guideline priority="medium" scope="checkout-features">
SHOULD: Display security badges (Norton, McAfee, etc.)
SHOULD: Show estimated delivery date before purchase
SHOULD: Offer expedited shipping options
SHOULD: Display order summary throughout checkout (sticky sidebar)

RATIONALE:

Security badges build trust (especially for first-time buyers).

Delivery dates manage expectations (reduce "where's my order?" support).
Shipping options increase conversion (some users need fast delivery).

Order summary prevents confusion (user always sees what they're buying).

ACCEPTABLE TO SKIP:

- Security badges if brand is well-known (Apple doesn't need Norton badge)
- Delivery dates if shipping is always fast (2-day standard)
- Expedited shipping if margins don't support it
</guideline>

Layer 3: CONTEXT (Planning Information)

<context scope="business">

**Company:** Fashion accessories e-commerce, Series A startup
**Current Status:** 500 beta users, launching public Q2 2026
**Revenue Model:** 15% commission on sales, targeting $50K MRR by year-end
**Competitive Position:** Competing on curation and UX (not price)
**Key Business Metrics:**

- Current cart abandonment: 25% (industry average: 20%)
- Target cart abandonment: <15% (best in class)
- Average order value: $75 (targeting $100 with upsells)
- Conversion rate: 2.5% (targeting 3.5%)

**Critical Success Factors:**

1. Launch on time (Q2 deadline - competitor launching Q3)
2. Lower abandonment (revenue directly correlates)
3. Mobile conversion (60% traffic but only 1.5% conversion)
4. Trust signals (new brand, need to build credibility)

**Constraints:**

- Budget: $5K/month infrastructure (must be efficient)
- Timeline: 3 months to launch (aggressive)
- Team: 3 developers (limited resources)
</context>

<context scope="technical">

**Technology Stack:**

- Frontend: React 18 + Next.js 14 (SSR for SEO)
- Backend: Node.js 20 + Express
- Database: PostgreSQL 15 (products, orders), Redis (sessions, cart)
- Payment: Stripe (handles PCI compliance)
- Email: SendGrid (transactional emails)
- Hosting: AWS (us-east-1), CloudFront CDN

**Performance Budget:**

- Target devices: iPhone 15+ (3-year-old phones)
- Connection: 3G minimum (many users on mobile data)
- Bundle size: <300KB JavaScript (fast load on 3G)

**Team Expertise:**

- Strong in React/Node (comfort zone)
- Limited DevOps experience (keep infrastructure simple)
- No payment processing experience (Stripe essential)

**Existing Systems:**

- Product catalog (done)
- User authentication (done)
- Cart (done, needs checkout integration)
</context>

<context scope="users">

**Primary Users:** Fashion-conscious consumers

- Age: 25-45 (core: 28-35 female)
- Tech proficiency: Medium-high (comfortable with e-commerce)
- Device: 60% mobile, 40% desktop
- Location: 80% urban/suburban US
- Income: $40K-$100K (price-conscious but willing to pay for quality)

**User Behavior Patterns:**

- Browse on mobile (during commute, breaks)
- Purchase on desktop (evening, more time to decide)
- Comparison shop (visit 3-5 sites before buying)
- Influenced by reviews and social proof

**Pain Points (from user research):**

- Frustrated by forced account creation (want guest checkout)
- Annoyed by slow loading (abandon if >3 seconds)
- Concerned about payment security (need trust signals)
- Impatient with multi-step forms (want quick checkout)

**Trust Indicators That Work:**

- SSL certificate (HTTPS = secure)
- Recognizable payment logos (Visa, Mastercard, PayPal)
- Clear return policy (visible during checkout)
- Customer reviews (social proof)
</context>

Layer 4: INTENT (The Why)

<intent scope="checkout-flow">

**Primary Goal:**

Create frictionless checkout that converts browsers into buyers by
minimizing steps, building trust, and optimizing for mobile.

**Why This Matters:**

**Market opportunity:** Current 2.5% conversion = $40K MRR. Target 3.5% = $56K MRR.

**Cart abandonment:** 25% abandon = lost revenue. Reduce to 15% = $8K/month recovered.

**Competitive pressure:** Competitor launching Q3. Must launch Q2 with superior UX.

**What Success Looks Like:**

- Cart abandonment <15% (from current 25%)
- Mobile conversion 2.5% (from current 1.5%)
- Checkout completion time <60 seconds average
- Customer satisfaction >4.5/5 for checkout experience
- Zero payment security incidents

**Why These Technical Choices:**

**Why Single-Page Checkout:**
Research shows:

- Multi-page checkout: 25% abandonment between pages
- Single-page checkout: 15% abandonment (10% improvement)
- User testing: "I can see everything, no surprises"

Trade-off: Heavier JavaScript (300KB) but worth conversion lift

**Why Guest Checkout:**
Data shows:

- Forced account creation: 23% abandon at that step
- Guest checkout option: Only 8% abandon (15% improvement)
- 35% of guests create account AFTER purchase (easier conversion)

Trade-off: Miss some user data upfront, but gain more conversions

**Why Stripe:**

- Handles PCI compliance (we can't afford full compliance audit)
- Excellent mobile UX (Apple Pay, Google Pay)
- Developer-friendly (small team can integrate quickly)
- Cost: 2.9% + $0.30 vs building custom (months + compliance risk)

Trade-off: Pay per transaction, but worth time-to-market and compliance

**Why Real-Time Validation:**
User research shows:

- Submit-time errors: Users frustrated, often abandon
- Real-time errors: Users fix immediately, higher completion
- Example: "This email is invalid" while typing = fix now vs frustrated later

Trade-off: More complex frontend, but better UX and conversion

**Trade-offs We Accept:**

**Speed to Market vs Feature Completeness:**

- Launching with core checkout only (no wishlist, no gift wrapping)
- Can add features post-launch based on user feedback
- RATIONALE: Q2 deadline more critical than perfect feature set

**Single-Page vs Performance:**

- 300KB JavaScript is heavy (3-4s load on 3G)
- But single-page reduces steps (fewer page loads overall)
- Optimizing with code splitting (load critical path first)
- RATIONALE: Conversion lift outweighs load time hit

**Stripe Cost vs Control:**

- 2.9% + $0.30 per transaction = $22/month at current volume
- Custom would save fees but cost $50K+ to build + maintain

RATIONALE: Stripe worth cost for compliance and time-to-market

**Mobile-First vs Desktop Revenue:**

- 60% traffic mobile but 40% revenue desktop
- Optimizing mobile first (where traffic is)
- Desktop gets good experience (but not primary focus)

RATIONALE: Mobile conversion has more upside (1.5% → 2.5% = huge)

**Alignment Check (How to Know We're On Track):**

**We're on track if:**

- Cart abandonment trending toward 15% (measured weekly)
- Mobile conversion improving (1.5% → 2.0% → 2.5%)
- Checkout completion time <60s average (analytics)
- Payment processing errors <1% (Stripe metrics)
- User feedback >4.0/5 for checkout (post-purchase survey)

**We're drifting if:**

- Adding steps to checkout (scope creep increasing friction)
- Abandonment increasing (new features hurting conversion)
- Load times increasing (JavaScript bloat from new features)
- Focusing on desktop at expense of mobile (wrong priority)
- Optimizing for edge cases over common paths (wrong focus)

**Course Correction Triggers:**

If abandonment >20% two weeks pre-launch:

1. Remove non-essential fields (minimize typing)
2. Simplify validation (less aggressive error messages)
3. A/B test single-page vs two-page (data over assumptions)

If mobile conversion not improving:

1. Profile mobile performance (find bottlenecks)
2. Reduce JavaScript bundle (code splitting more aggressive)
3. Simplify mobile layout (maybe different from desktop)

If checkout time >75 seconds:

1. Remove optional fields (keep only required)
2. Improve autocomplete (fewer manual entries)
3. Optimize Stripe integration (reduce API roundtrips)

**Decision Framework for Trade-offs:**
When features conflict, priority order:

1. Security (MUST never compromise - legal + trust)
2. Conversion rate (primary business goal)
3. Mobile experience (where users are)
4. Speed to market (Q2 deadline critical)
5. Feature completeness (nice-to-have)

Example application:

- Request: "Add gift wrapping option"
- Analysis: Adds field to checkout (more friction), only 5% users want it
- Decision: NO for v1 (hurts conversion, low demand). Revisit post-launch if >100 requests.
- Rationale: Conversion (#2) outweighs feature (#5)
</intent>

Layer 5: VERIFICATION (Self-Checking)

<verification scope="checkout-complete">

**Pre-Launch Verification (Must Pass All):**

SECURITY (Critical - No Exceptions):
Stripe integration validated (test mode payments succeed)
All checkout pages HTTPS (HTTP redirects to HTTPS)
Cart data encrypted in Redis (inspect session storage)
No payment data stored locally (code review confirms)
3D Secure triggers for >$100 (test transaction)
PCI SAQ-A completed (Stripe handles PCI, we document)

PERFORMANCE (Critical - Must Meet Targets):

Checkout load time <2s per step (3G simulation, Chrome DevTools)
Total checkout time <60s (timed manual test)
Stripe API p95 <5s (load test 100 concurrent users)
JavaScript bundle <300KB (webpack-bundle-analyzer)

FUNCTIONALITY (Critical - Must Work):
Guest checkout completes (test without login)
Logged-in checkout saves cart 7 days (test persistence)
Order confirmation email <5 min (monitor SendGrid)
Inventory reserved during checkout (concurrent purchase test)
Payment methods save for returning users (test with consent)

USER EXPERIENCE (High Priority):
Mobile usable (test on iPhone 11, Pixel 5)
Real-time validation works (test invalid email, see immediate error)
Autocomplete works (test address fields)
Order summary visible throughout (sticky sidebar confirmed)
Error messages helpful (test various error states)

CODE QUALITY (High Priority):

All tests pass (npm test, >80% coverage)
Linter passes (npm run lint, 0 errors)
No console.logs in production code
Stripe test mode disabled in production (environment check)

**Pass Criteria:**

- ALL Security checks: MUST PASS (non-negotiable)
- ALL Performance checks: MUST PASS (business critical)
- ALL Functionality checks: MUST PASS (required features)
- User Experience: 90%+ pass (document exceptions)
- Code Quality: 90%+ pass (document tech debt)

**If Critical Check Fails:**

STOP. Do not launch. Fix immediately. Re-verify.

**Post-Launch Monitoring (Continuous):**

- Cart abandonment rate (target: <15%, alert if >18%)
- Checkout completion time (target: <60s, alert if >75s)
- Payment error rate (target: <1%, alert if >2%)
- Mobile conversion rate (target: 2.5%, alert if <2.0%)
- Email delivery rate (target: >99%, alert if <95%)

**Weekly Review:**

Abandonment trend (improving or declining?)
Conversion trend (improving or declining?)
User feedback scores (>4.0/5 satisfaction?)
Payment processing health (error rate low?)
Performance metrics (load times acceptable?)
If trends negative: Initiate course correction per INTENT framework.
</verification>
```

END OF INTEGRATED SPECIFICATION

## How the Layers Work Together

**See how each layer answers different questions**

### MUST Answers: "What boundaries exist?"

- PCI compliance required (legal boundary)
- <60 second checkout (performance boundary)
- Guest checkout supported (functionality boundary)

### SHOULD Answers: "What's preferred?"

- Single-page checkout preferred (can flex to multi-page)
- Real-time validation preferred (can do submit-time)
- Saved payment methods preferred (can skip if privacy concerns)

### CONTEXT Answers: "Why these boundaries and preferences?"

- Series A startup = limited resources (Stripe vs custom)
- 60% mobile traffic = mobile-first focus
- Cart abandonment 25% = urgent need to optimize
- Q2 deadline = speed over perfection

### INTENT Answers: "What are we trying to achieve and why?"

- Primary goal: Reduce abandonment 25% → 15%
- Why single-page: 10% conversion lift per research
- Why Stripe: PCI compliance + time-to-market
- Trade-offs: Paying Stripe fees worth compliance + speed

### VERIFICATION Answers: "How do we know we succeeded?"

- Security: Stripe test payments work
- Performance: Load tests show <2s per step
- Functionality: Guest checkout completes
- Success: Abandonment trending toward 15%

## How Layers Reinforce Each Other

### **Example: Guest Checkout**

```text

MUST says: Support guest checkout (hard requirement)

SHOULD says: Encourage account creation after purchase (preference)

CONTEXT explains why:
User research: 23% abandon at forced account creation
Business need: Convert browsers to buyers first
User preference: 35% create account post-purchase anyway

INTENT clarifies trade-off:
Priority: Conversion > User data collection
Trade-off: Miss some upfront data, gain more sales
Philosophy: Easy first purchase, encourage repeat organically

VERIFICATION confirms:
Test: Guest checkout completes without errors
Metric: Abandonment at checkout step <10%
Success: 35%+ guests create account post-purchase
```
**All layers aligned, reinforcing the decision!**

### What Good Integration Looks Like

**Characteristics of this integrated spec:**

No Contradictions:

- MUST says <60s checkout
- CONTEXT explains why (abandonment research)
- INTENT prioritizes this (conversion critical)
- VERIFICATION measures it (timed tests)

 **All layers support the same goal**

**Answers All Questions:**

- WHAT to build (MUST/SHOULD)
- WHY build it (CONTEXT/INTENT)
- HOW to verify (VERIFICATION)
- WHEN to course-correct (INTENT alignment check)

**Clear Priorities:**

- When features conflict, INTENT provides decision framework
- Security (#1) > Conversion (#2) > Mobile (#3) > Features (#5)
- No ambiguity about what wins

**Measurable Success:**

- Specific metrics (abandonment <15%, conversion 2.5%)
- Clear verification (load tests, user tests)
- Monitoring plan (weekly reviews, alerts)

**Flexibility Where Needed:**

- SHOULD allows alternatives (multi-page if single-page performs poorly)
- INTENT explains acceptable trade-offs
- CONTEXT justifies exceptions

### Example 2: Healthcare Patient Portal (Mobile App)

**Scenario: HIPAA-compliant mobile app for physician-patient communication**

The Complete Integrated Specification

PATIENT PORTAL MOBILE APP SPECIFICATION

All five layers working together

```text

Layer 1: MUST (Hard Boundaries)

<constraint priority="critical" scope="hipaa-compliance" supremacy="true">
MUST: HIPAA Security Rule compliance (all PHI handling)
MUST: End-to-end encryption for messages (TLS 1.3 in transit, AES-256 at rest)
MUST: Audit logging for all PHI access (who, what, when, where)
MUST: User authentication with MFA (SMS or authenticator app)
MUST: Auto-logout after 10 minutes inactivity
MUST: No PHI in device logs, crash reports, or analytics
MUST: Data deletion within 30 days of account closure

SUPREMACY CLAUSE:

HIPAA compliance overrides ALL other requirements including performance,
features, and user convenience. If any requirement conflicts with HIPAA,
HIPAA wins without exception.

VERIFICATION:

- HIPAA audit checklist (all 45 items confirmed)
- Penetration test (certified HIPAA auditor, annual)
- Encryption verification (TLS 1.3 handshake, AES-256 file inspection)
- Audit log review (100% PHI access captured)
- Auto-logout test (10 minutes idle = logged out)
- Code review (no PHI in logs, analytics confirmed)
</constraint>

<constraint priority="critical" scope="offline-functionality">

MUST: Core features work offline (appointments view, message drafts)
MUST: Automatic sync when connection available (background, no user action)
MUST: Conflict resolution for offline changes (last-write-wins with timestamp)
MUST: Clear offline/online status indicator (user knows connection state)

RATIONALE:

Physicians work in hospitals with spotty WiFi (basement exam rooms, elevators).
Patients may have limited data plans or be in areas with poor coverage.
App must be reliable regardless of connectivity.

VERIFICATION:

- Airplane mode test (core features accessible without internet)
- Sync test (offline changes sync when reconnected)
- Conflict test (simultaneous offline edits resolve correctly)
- Status indicator test (airplane mode shows offline state)
</constraint>

Layer 2: SHOULD (Flexible Preferences)

<guideline priority="high" scope="user-experience">
SHOULD: Biometric login (Touch ID / Face ID) after initial MFA
SHOULD: Push notifications for new messages (with PHI-free preview)
SHOULD: In-app messaging (patient-doctor communication)
SHOULD: Appointment reminders (24 hours before, configurable)

RATIONALE:

Biometric login balances security (still have MFA initially) with convenience.

Push notifications improve engagement (patients see messages faster).
In-app messaging keeps communication in one place (vs email scattered).

ACCEPTABLE EXCEPTIONS:

- Biometric optional (not all users want it, some devices lack it)
- Push notifications opt-in (some users prefer no notifications)
- Appointment reminders can be email if push not available

WHEN VIOLATING:

Ensure alternative meets INTENT (timely communication, secure access).
Document why exception made (technical limitation, user preference).
</guideline>

<CONTEXT (Planning Information)

<context scope="healthcare-regulations">

**Regulatory Environment:**

- HIPAA Security Rule (federal, applies to all PHI)
- State medical privacy laws (varies by state, most stricter than HIPAA)
- FDA guidance on mobile medical apps (not a "medical device" but follows best practices)
- App Store requirements for health apps (privacy policy, clear data handling)

**Compliance Complexity:**

- Multi-state practice (patients in different states = multiple laws)
- Telemedicine regulations (vary by state, evolving)
- Minor patient data (COPPA + HIPAA for patients <18)

**Audit Requirements:**

- Annual HIPAA security assessment (required by law)
- Breach notification within 60 days (if PHI compromised)
- Business associate agreements (any vendors handling PHI)
</context>

<context scope="users">

**Patient Users:**

- Age: Wide range (18-80+, app must be accessible)
- Tech proficiency: Low to medium (many not tech-savvy)
- Health conditions: Chronic conditions (diabetes, hypertension, frequent users)
- Usage: Appointment scheduling, message doctor, view test results

**Physician Users:**

- Age: 35-65 (established practices)
- Tech proficiency: Medium (comfortable with smartphones, not always with apps)
- Work environment: Busy (seeing 25-30 patients/day, limited time per patient)
- Usage: Review messages between patients, update notes, confirm appointments

**Key User Needs:**

- Patients: Easy access to doctor, no phone tag, see test results quickly
- Physicians: Efficient communication (reduce phone calls), accessible anywhere
</context>

Layer 4: INTENT (The Why)

<intent scope="patient-portal">

**Primary Goal:**
Improve patient-physician communication while maintaining strict HIPAA
compliance, reducing administrative burden on both patients and staff.

**Why This Matters:**

**Current state:** Phone tag (patients call clinic, leave message, wait for callback)

**Pain points:** 40% of calls are simple questions, waste 2-3 hours/day of staff time

**Opportunity:** Async messaging reduces phone calls 60%, improves patient satisfaction

**Why HIPAA Supremacy:**

- Legal requirement (non-negotiable)
- Trust requirement (patients must trust app with health data)
- Breach consequences (fines $100-$50,000 per violation, reputational damage)

RATIONALE: No feature worth risking compliance violation

**Why Offline-First:**

- Physicians in hospitals (basement exam rooms, spotty WiFi)
- Patients in rural areas (limited connectivity)
- App reliability matters more than real-time sync (delayed sync acceptable, broken app not)

**Trade-offs:**

- Security > Convenience (10-min auto-logout annoying but required)
- Compliance > Features (can't add feature that risks HIPAA)
- Reliability > Real-time (offline works > live updates)

**Success:**

- 60% reduction in phone calls to clinic
- >4.5/5 patient satisfaction with communication
- Zero HIPAA violations
- Physicians use app daily (not abandoned)
</intent>

VERIFICATION (Self-Checking)

<verification scope="pre-launch">

**HIPAA COMPLIANCE (Critical - No Launch Without):**

All 45 HIPAA Security Rule items verified
Penetration test passed (certified auditor report)
Business associate agreements signed (all vendors)
Encryption confirmed (TLS 1.3, AES-256)
Audit logging captures 100% of PHI access
No PHI in logs, crash reports, analytics (code review)
Auto-logout works (10-min idle test)

**FUNCTIONALITY (Critical):**
Offline mode works (airplane mode test)
Sync works (offline changes sync when online)
Authentication works (MFA, biometrics)
Messaging works (send, receive, notifications)

**USABILITY (High Priority):**
Accessible (WCAG 2.1 AA, VoiceOver tested)
Works on older devices (iPhone 15, tested)
Low-literacy readable (8th grade level, Flesch-Kincaid)

PASS CRITERIA:

- HIPAA: 100% pass (non-negotiable)
- Functionality: 100% pass (required)
- Usability: 90%+ pass (document exceptions)

IF HIPAA FAILS: STOP. Fix immediately. No launch until 100% compliant.
</verification>
```

END OF INTEGRATED SPECIFICATION

#### How Layers Work Together (Healthcare Example)

#### SUPREMACY CLAUSE in action

**Scenario: User requests "Remember Me" feature (stay logged in for 30 days)**

How layers interact:

```text

MUST says: Auto-logout after 10 minutes (HIPAA requirement)
User request: "Remember Me" = stay logged in 30 days

CONTEXT explains: HIPAA Security Rule requires "automatic logoff"

INTENT clarifies: Compliance > Convenience (supremacy clause)

Decision: NO to "Remember Me" feature

Alternative: Biometric login (SHOULD) = quick re-auth without compromising security

VERIFICATION confirms: 10-minute auto-logout tested and working
```
**All layers aligned to protect compliance!**


### Example 3: API Service Rate Limiting

Scenario: B2B SaaS API implementing fair usage limits

The Complete Integrated Specification

API RATE LIMITING SPECIFICATION
All five layers working together
**MUST, SHOULD, CONTEXT, INTENT, VERIFICATION**

`<constraint priority="critical" scope="rate-limiting">`
MUST: Rate limits enforced per API key
MUST: Standard tier: 1,000 requests/hour
MUST: Enterprise tier: 10,000 requests/hour
MUST: Return 429 status code when limit exceeded
MUST: Include Retry-After header (seconds until reset)
MUST: Include rate limit headers (X-RateLimit-Limit, X-RateLimit-Remaining)

VERIFICATION:

- Test 1001st request (returns 429)
- Test headers present (all three headers in response)
- Test Retry-After accuracy (wait time, then retry succeeds)
`</constraint>`

`<guideline priority="high" scope="rate-limit-flexibility">`
SHOULD: Burst allowance (20% over limit for 1 minute)
SHOULD: Different limits for read vs write operations
SHOULD: Whitelist for status/health endpoints (no rate limit)

RATIONALE:

Burst handles traffic spikes (e.g., cron jobs at hour boundary).

Reads cheaper than writes (GET vs POST/PUT/DELETE).

Health checks shouldn't count toward limit (monitoring needs).
`</guideline>`

`<context scope="business">`

**Customers:** Other software companies (B2B)

**Pricing:** Standard $99/month, Enterprise custom

**Current Scale:** 10M requests/month total

**Target Scale:** 100M requests/month (10x growth)

**Why Rate Limiting:**

- Prevent abuse (one customer can't starve others)
- Cost control (our infrastructure costs scale with usage)
- Fair usage (ensure quality for all customers)
`</context>`

`<intent scope="rate-limiting">`

**Goal:** Fair resource allocation while allowing legitimate bursts.

**Why 1,000/hour for Standard:**

- Covers 90% of customer usage patterns
- Allows 24K/day (typical small business volume)
- Bursts to 1,200/hour (traffic spikes covered)

**Why burst allowance:**

- Customer cron jobs often run at hour boundaries
- 20% burst = 1,200 requests in 1 minute okay
- Prevents false positives (legitimate use blocked)

**Trade-off:** Complex to implement, but worth it for customer experience
`</intent>`

`<verification scope="rate-limiting">`

- 1001st request returns 429 (limit enforced)
- Burst of 1,200 in 1 minute succeeds (burst works)
- Headers accurate (limit, remaining, reset correct)
- Retry-After works (wait time, then success)

PASS: All tests pass. Rate limiting works correctly.
`</verification>`

### How Layers Prevent Conflicts

Potential conflict: "Customer wants unlimited API calls"

How layers resolve:

MUST: 1,000/hour limit (prevents resource exhaustion)

SHOULD: Burst allowance (handles legitimate spikes)

CONTEXT: Cost control needed (infrastructure scales with usage)

INTENT: Fair usage (one customer can't hurt others)

VERIFICATION: Test confirms limit enforced but burst works

Resolution: Limit enforced (MUST), but burst makes it flexible (SHOULD), for business reasons (CONTEXT), aligned with fairness goal (INTENT), proven working (VERIFICATION).

**Conflict resolved through layer integration!**

## Key Integration Principles

From these three examples, we see:

1. Each Layer Has a Job
MUST: What's required (boundaries)
SHOULD: What's preferred (flexibility)
CONTEXT: Why these choices (environment)
INTENT: What we're achieving (goals)
VERIFICATION: How we check (validation)

Don't make one layer do another's job!
2. Layers Reinforce, Not Contradict
Good integration:
MUST says "guest checkout required"
CONTEXT explains "23% abandon at forced signup"
INTENT clarifies "conversion > data collection"
All layers support the decision

Poor integration:
MUST says "checkout <60 seconds"
CONTEXT says "users prefer thoroughness over speed"
INTENT says "conversion through trust, not speed"
Layers contradict!
3. Supremacy Clauses Resolve Conflicts
When layers might conflict:
Declare supremacy (HIPAA > all else)
Makes priorities explicit
Prevents paralysis when trade-offs needed

Example: HIPAA supremacy means "Remember Me" declined even though users want it.
4. Verification Proves Integration
Good verification tests:
That MUST constraints are met
That SHOULD preferences are honored (or exceptions documented)
That CONTEXT assumptions are valid
That INTENT goals are achieved
Verification is the proof that integration works!
5. Context Informs Everything
Context shapes:
Which MUSTs matter (HIPAA critical for healthcare, not for games)
Which SHOULDs to prioritize (mobile-first if 60% mobile traffic)
What INTENT focuses on (conversion if abandonment high)
How to VERIFY (healthcare needs compliance audit, e-commerce needs conversion
metrics)
Context is the lens through which all other layers are viewed.

## Integration Checklist

Before finalizing your integrated specification:

Completeness

[ ] All 5 layers present (MUST, SHOULD, CONTEXT, INTENT, VERIFICATION)
[ ] Each layer answers its question (WHAT, PREFER, WHY, GOAL, VERIFY)
[ ] No layer trying to do another layer's job

Alignment

[ ] MUST constraints align with INTENT goals
[ ] SHOULD preferences support INTENT priorities
[ ] CONTEXT justifies MUST choices
[ ] VERIFICATION tests MUST compliance and INTENT achievement

No Contradictions

[ ] MUSTs don't conflict with each other
[ ] MUSTs don't conflict with INTENT
[ ] CONTEXT doesn't contradict constraints
[ ] If conflicts exist, supremacy clause declares winner

Priorities Clear

[ ] When constraints conflict, priority order stated
[ ] Trade-offs explicitly acknowledged
[ ] Decision framework provided (what wins when)

Measurable

[ ] Success criteria in INTENT are specific
[ ] Verification has objective pass/fail
[ ] Metrics defined (not vague "good" or "fast")

## Common Integration Mistakes

Watch out for these:

### Missing Layers

**Problem:** Only MUST and VERIFICATION, no CONTEXT or INTENT

**Why it fails:** Can verify compliance but don't understand WHY these constraints exist or what we're trying to achieve.

**Fix:** Add CONTEXT (explains environment) and INTENT (explains goals).

### Contradictory Layers

**Problem:**
• MUST: Response time <100ms
• INTENT: Thorough data validation more important than speed

**Why it fails:**  Can't satisfy both. Need to prioritize.

**Fix:** Choose priority (speed OR thoroughness), adjust layers to align.

### Vague Integration

**Problem:**
MUST: "Be secure"
CONTEXT: "We're a tech company"
INTENT: "Build a good product"

**Why it fails:** All layers vague = no actionable guidance.

**Fix:** Be specific in each layer. Define terms.

### INTENT Doesn't Match MUST

**Problem:**
MUST: Stripe integration (specific tool)
INTENT: "Maximize control and minimize cost"

**Why it fails:** Stripe reduces control and costs per-transaction (conflicts with INTENT).

**Fix:** Either change MUST (custom payment) or change INTENT (prioritize compliance and time-to-market).

## Summary

Integration means:

- All 5 layers present and complete
- Each layer doing its job (not another's)
- Layers aligned and reinforcing
- No contradictions (or supremacy clause resolves)
- Measurable and verifiable

Good integration enables:

- Clear requirements (no guessing)
- Aligned decisions (INTENT guides)
- Conflict resolution (priorities clear)
- Successful verification (all layers support testing)

Use these examples as templates for your own integrated specifications.

END OF APPENDIX B

Document Version: 1.0.0
Last Updated: 2026-0218
Three complete integration examples showing all layers working together

