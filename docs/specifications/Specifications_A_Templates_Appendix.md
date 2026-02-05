# Specifications_A_Templates_Appendix

*Converted from PDF: Specifications_A_Templates_Appendix.pdf*



---
**Page 1**

Appendix A: Complete Specification Templates

For: Quick-start specification writing with proven templates

When to use: Starting a new project or converting informal requirements to formal specs
What you get: Copy-paste ready templates for common domains

How to Use These Templates


### These templates provide:


• All five layers (MUST, SHOULD, CONTEXT, INTENT, VERIFICATION)

• Real-world structure and content

• Comments explaining each section
• Placeholders for customization [like this]


### To use a template:



## 1. Choose the template closest to your domain



## 2. Copy the entire template



## 3. Replace placeholders with your specifics



## 4. Delete sections that don't apply



## 5. Add domain-specific requirements



## 6. Review against Section 7 pitfalls


Remember: These are starting points, not rigid rules. Adapt to your needs.

Template 1: Web Application (E-commerce)
<!-- ============================================ -->


## <!-- COMPLETE SPECIFICATION: E-COMMERCE PLATFORM -->


<!-- ============================================ -->

<!-- MUST: Hard Boundaries (Non-negotiable) -->


---
**Page 2**

<constraint priority="critical" scope="security">

MUST: All payment processing PCI-DSS compliant (use Stripe or similar)

MUST: HTTPS only in production (no HTTP endpoints)
MUST: Password hashing with bcrypt (salt rounds >= 12)

MUST: User PII encrypted at rest (AES-256)

MUST: Authentication via JWT (HS256, 15-minute access token expiry)

MUST: Rate limiting (100 requests/minute per user)


## VERIFICATION:


- npm audit --audit-level=high (0 critical vulnerabilities)

- Check SSL certificate valid (expires > 30 days from now)

- Verify bcrypt usage: grep -r "bcrypt.hash" src/auth/

- Verify PII encryption in database schema

</constraint>

<constraint priority="critical" scope="performance">
MUST: API response time <200ms (p95) under normal load

MUST: Page load time <2 seconds (p95) on 3G connection

MUST: Checkout flow completes in <5 seconds total


## VERIFICATION:


- Load test: artillery run load-test.yml

- Lighthouse performance score >85

- Monitor production: DataDog alerts if p95 >200ms

</constraint>


---
**Page 3**

<constraint priority="critical" scope="functionality">

MUST: Support payment methods: Credit card, PayPal, Apple Pay

MUST: Real-time inventory tracking (prevent overselling)
MUST: Email confirmation within 5 minutes of order

MUST: Order cancellation within 1 hour of purchase


## VERIFICATION:


- Test each payment method in staging

- Inventory test: attempt concurrent purchases of last item

- Monitor email delivery: SendGrid success rate >99%

</constraint>

<!-- SHOULD: Flexible Preferences (Good to have) -->

<guideline priority="high" scope="ux">

SHOULD: Guest checkout option (no forced account creation)

SHOULD: Save payment methods for returning customers
SHOULD: One-click reorder for previous purchases

SHOULD: Mobile-responsive design (works well on 320px+ screens)


## ACCEPTABLE EXCEPTIONS:


- Guest checkout not available for high-value items (>$1000) - fraud prevention

- Payment saving requires explicit consent (privacy regulation)

WHEN VIOLATING: Document rationale and get product team approval

</guideline>


---
**Page 4**

<guideline priority="medium" scope="features">

SHOULD: Product recommendations based on browsing history

SHOULD: Wishlist functionality
SHOULD: Social sharing (share products on social media)

SHOULD: Live chat support during business hours


## RATIONALE:


These improve conversion but aren't critical for MVP launch.

Implement based on user feedback after launch.

</guideline>

<!-- CONTEXT: Planning Information -->

<context scope="business">

**Company Stage:** Series A startup, 18 months runway

**Current Status:** 500 beta users, launching to public Q2

**Target Market:** US consumers (18-45), fashion and accessories
**Revenue Model:** 15% commission on sales, $50K MRR goal by year-end

**Business Priorities (ranked):**


## 1. Launch on time (Q2 deadline is hard constraint - competitor launching Q3)



## 2. Transaction reliability (failed transactions = lost revenue)



## 3. User experience (conversion rate target: >3% vs 2% industry average)



## 4. Operational efficiency (small team, must be maintainable)


**Key Metrics:**

- Cart abandonment: Target <15% (industry average 20%)


---
**Page 5**

- Checkout completion: Target >80% (start to finish)

- Support ticket rate: Target <2% of orders

</context>

<context scope="technical">

**Technology Stack:**

- Frontend: React 18 + Next.js 14 (SSR for SEO)

- Backend: Node.js 20 + Express

- Database: PostgreSQL 15 (primary), Redis (session/cache)

- Hosting: AWS (us-east-1), CloudFront CDN

- Payment: Stripe (PCI compliance handled)

**Team:**

- 3 full-stack developers (strong React/Node)

- 1 designer (UX/UI)

- 1 product manager
- 2 co-founders (technical background)

**Infrastructure:**

- Deployment: Blue-green via GitHub Actions

- Monitoring: DataDog (metrics, logs, APM)

- Error tracking: Sentry

- Load: Expecting 1K concurrent users at launch, 10K within 6 months

**Constraints:**

- Budget: $5K/month infrastructure (need to scale efficiently)


---
**Page 6**

- Timeline: 3 months to MVP (aggressive but achievable)

- Technical debt: Acceptable if documented (speed to market priority)

</context>

<context scope="users">

**Primary Users:**

- Age: 18-45 (core: 25-35)

- Tech proficiency: High (comfortable with e-commerce)

- Device: 60% mobile, 40% desktop

- Location: 80% US urban/suburban

- Income: $40K-$100K (middle-class consumers)

**User Behavior:**

- Browse during commute/lunch (mobile)

- Purchase in evening (desktop, more time)

- Price sensitive (compare prices before buying)
- Expect fast shipping (Amazon Prime effect)

**Pain Points (from research):**

- Frustrated by slow checkout (abandon if >3 steps)

- Annoyed by forced account creation (want guest checkout)

- Concerned about payment security (need trust signals)

- Impatient with slow loading (abandon if >3 seconds)

**Success Criteria:**

- 90% can complete purchase without support


---
**Page 7**

- Average checkout time <2 minutes

- <5% report "confusing" in surveys

- >4.2/5 average satisfaction rating
</context>

<!-- INTENT: The Why -->

<intent scope="platform">

**Primary Goal:**

Launch competitive e-commerce platform in Q2 to capture market before

competitor launch in Q3. First-mover advantage = 60-70% market share in

our niche (fashion accessories).

**Why This Matters:**

**Market opportunity:** $50M addressable market in fashion accessories

**Competitor threat:** Well-funded competitor launching Q3 (3-month window)

**Revenue need:** Must hit $100K MRR within 12 months or fundraise again

**What Success Looks Like:**

- Launch by June 30 (Q2 deadline)

- 10K users first month (viral marketing planned)

- $20K MRR by end of Q3 (from launch)

- 15% month-over-month growth (sustainable)

- 4.5/5 user satisfaction (trust = repeat purchases)

**Why These Technical Choices:**


---
**Page 8**

**Why React/Next.js:**

- Team expertise (3 devs know React well)

- SEO critical (Next.js SSR solves this)
- Fast development (component library available)

- Hiring pipeline (React devs abundant)

**Why PostgreSQL:**

- Team experience (comfort level)

- Relational data fits (products, orders, users)

- Proven at scale (can grow with us)

- Cost effective (managed RDS reasonable)

**Why Stripe:**

- PCI compliance handled (huge time saver)

- Excellent UX (proven conversion rates)

- Apple Pay integration (mobile conversion boost)
- Cost acceptable (2.9% + $0.30 vs building custom)

**Trade-offs We Accept:**

**Speed over perfection:**

- MVP features only (recommendations, wishlists can wait)

- Technical debt acceptable if documented

- Iterate based on real user feedback

- RATIONALE: Market timing more critical than perfect product


---
**Page 9**

**Stripe cost vs build:**

- Stripe takes 2.9% + $0.30 per transaction

- Building custom would save fees but take 2 months + compliance
- DECISION: Stripe worth the cost for time-to-market

**Mobile-first design:**

- 60% mobile traffic but desktop converts better (larger screens)

- Optimizing mobile first (where most users are)

- Desktop experience still good (just not primary)

- RATIONALE: Acquire on mobile, convert later

**Alignment Check:**

**We're on track if:**

- Feature freeze by May 15 (6 weeks for testing/polish)

- Checkout flow conversion >80% in testing

- Load tests pass (1K concurrent users, <200ms p95)
- Beta user feedback >4.0/5 (satisfaction)

**We're drifting if:**

- Adding features after May 15 (scope creep)

- Optimizing edge cases over common paths (wrong priorities)

- Building custom solutions for commodity problems (NIH syndrome)

- Delaying launch for perfection (market timing matters)

**Course Correction:**


### If behind schedule by April 15:



---
**Page 10**


## 1. Cut nice-to-have features (recommendations, social sharing)



## 2. Accept higher technical debt (document for later)



## 3. Simplify UI (standard patterns vs custom design)


## 4. Defer Android app (web mobile-first)


Priority: Ship Q2 > Ship perfect Q3

</intent>

<!-- VERIFICATION: Self-Checking -->

<verification scope="pre-delivery">

**What to verify before delivery:**


### SECURITY (Critical - must pass):


□ npm audit --audit-level=high returns 0 vulnerabilities

□ All API endpoints require authentication (except public routes)

□ Password hashing confirmed (bcrypt visible in code)
□ JWT tokens httpOnly cookies (not localStorage)

□ HTTPS only in production (SSL certificate valid)

□ Rate limiting active (test: 101st request returns 429)


### PERFORMANCE (Critical - must pass):


□ Load test passes: artillery run load-test.yml

- API p95 <200ms ✓

- No errors <1% ✓

- 1K concurrent users supported ✓

□ Lighthouse score >85 on key pages


---
**Page 11**

□ Page load <2s on 3G throttling (Chrome DevTools)


### FUNCTIONALITY (Critical - must pass):

□ All payment methods work in staging

- Credit card: Stripe test cards ✓

- PayPal: Sandbox account ✓

- Apple Pay: iOS simulator ✓

□ Inventory prevents overselling (concurrent purchase test)
□ Order confirmation email received <5 min

□ Checkout flow completes end-to-end (no blocking bugs)


### CODE QUALITY (High priority):


□ All tests pass: npm test (>80% coverage required)

□ Linter passes: npm run lint (0 errors, <10 warnings)

□ No console.log in production code

□ Environment variables not hardcoded


## PASS CRITERIA:


All CRITICAL checks must pass before delivery.

HIGH PRIORITY checks should pass (document exceptions).

If verification fails: Fix issues, re-verify, then deliver.

Do NOT deliver if CRITICAL checks fail.

</verification>


## <!-- END OF TEMPLATE -->



---
**Page 12**

Template 2: Mobile Application (Healthcare)
<!-- ================================================== -->


## <!-- COMPLETE SPECIFICATION: HEALTHCARE MOBILE APP -->


<!-- ================================================== -->

<!-- MUST: Hard Boundaries (Non-negotiable) -->

<constraint priority="critical" scope="compliance" supremacy="true">

MUST: HIPAA compliant (all PHI handling follows HIPAA Security Rule)

MUST: End-to-end encryption for all patient data in transit (TLS 1.3)
MUST: At-rest encryption for all PHI stored locally (AES-256)

MUST: Audit logging for all PHI access (who, what, when, where)

MUST: User authentication with MFA (SMS or authenticator app)

MUST: Auto-logout after 10 minutes of inactivity

MUST: No PHI in device logs, crash reports, or analytics

SUPREMACY CLAUSE: HIPAA compliance overrides all other requirements.

If any feature conflicts with HIPAA, HIPAA wins.


## VERIFICATION:


- HIPAA compliance checklist (all items confirmed)

- Penetration testing by certified firm (annual)

- Audit log review (random sampling, 100% capture verified)
- Manual code review for logging (no PHI in logs)

</constraint>


---
**Page 13**

<constraint priority="critical" scope="functionality">

MUST: Offline mode for core features (appointments, patient notes)

MUST: Sync when connection available (automatic, background)
MUST: Conflict resolution for offline changes (last-write-wins with timestamp)

MUST: Works on iOS 15+ and Android 10+ (95% of user base)

MUST: Appointment scheduling with calendar sync

MUST: Prescription writing with drug interaction checking


## VERIFICATION:


- Offline test: Airplane mode, verify core features work

- Sync test: Go offline, make changes, go online, verify sync

- Device matrix: Test on iPhone 11, Pixel 5, iPad (minimum devices)

- Drug interaction: Test known interactions (aspirin + warfarin should warn)

</constraint>

<constraint priority="critical" scope="performance">
MUST: App launch time <2 seconds (cold start on target devices)

MUST: Patient record load time <1 second (from local cache)

MUST: Sync completion <10 seconds (for typical day's changes)

MUST: Works on slower devices (iPhone 11, not just iPhone 15)


## VERIFICATION:


- Test on iPhone 11 (3-year-old device)

- Measure with Xcode Instruments (cold launch time)

- Test with 100 patient records (typical physician load)

</constraint>


---
**Page 14**

<!-- SHOULD: Flexible Preferences -->

<guideline priority="high" scope="ux">
SHOULD: Touch ID / Face ID for quick login (after initial authentication)

SHOULD: Voice-to-text for note-taking (doctors prefer dictation)

SHOULD: Smart templates for common diagnoses (save time)

SHOULD: Integration with EHR systems (Epic, Cerner)


## ACCEPTABLE EXCEPTIONS:


- Biometric login optional (not all users want it)

- Voice-to-text may not work in noisy environments (ER)

- EHR integration may require IT approval (enterprise sales cycle)


## RATIONALE:


These improve workflow efficiency but aren't critical for compliance or core function.

</guideline>

<guideline priority="medium" scope="features">

SHOULD: Telemedicine video calls

SHOULD: Prescription refill requests from patients

SHOULD: Lab result notifications

SHOULD: Patient education materials


## RATIONALE:


Nice-to-have features for v2.0. Focus on core appointment/note-taking for v1.0.

Add based on physician feedback after launch.


---
**Page 15**

</guideline>

<!-- CONTEXT: Planning Information -->
<context scope="business">

**Company:** HealthTech startup (Series A), 15-person team

**Target Users:** Primary care physicians (5K target by year-end)

**Business Model:** $50/month per physician subscription

**Current Status:** Beta with 50 physicians, launching v1.0 in Q3

**Regulations:**

- HIPAA (US federal law - applies to all PHI)

- State medical board requirements (varies by state)

- App Store/Play Store healthcare app requirements

**Competitive Landscape:**

- Main competitor: Epic's mobile app (clunky, desktop-focused)
- Our advantage: Mobile-first design, offline capability

- Our challenge: Integration with existing EHR systems (complex)

</context>

<context scope="technical">

**Technology Stack:**

- Platform: React Native (iOS and Android from one codebase)

- Local database: WatermelonDB (optimized for mobile)

- Backend: Node.js + Express, PostgreSQL

- Cloud: AWS (HIPAA BAA signed), Cognito for auth


---
**Page 16**

- Encryption: react-native-encrypted-storage

**Team:**
- 2 mobile developers (React Native experts)

- 1 backend developer (Node.js)

- 1 designer (healthcare UX experience)

- 1 compliance officer (HIPAA specialist)

**Deployment:**

- iOS: TestFlight beta, App Store release

- Android: Internal testing, Play Store release

- Backend: AWS ECS (containerized)

</context>

<context scope="users">

**Primary Users:** Primary care physicians
- Age: 30-65 (broad range)

- Tech proficiency: Medium (comfortable with smartphones, not all tech-savvy)

- Work environment: Clinic, hospital, home visits

- Time pressure: High (seeing 20-30 patients per day)

- Connectivity: Variable (clinics usually good, home visits spotty)

**Usage Patterns:**

- Between patient visits (5-10 minutes per patient)

- End of day documentation (catch-up on notes)

- On-call scenarios (need quick access to patient history)


---
**Page 17**

**Pain Points:**

- Desktop EHRs slow and complex (clicks to do anything)
- Can't access records during home visits (no internet)

- Voice recognition in desktop systems is poor

- Too many steps to write prescriptions

**Success Criteria:**

- Physicians complete notes in <3 minutes (vs 8 minutes in EHR)

- 80% of physicians use offline mode regularly

- <2% need support calls (intuitive enough for busy doctors)

- >4.5/5 satisfaction (physicians are picky about tools)

</context>

<!-- INTENT: The Why -->

<intent scope="mobile-app">
**Primary Goal:**

Provide physicians with mobile-first tool that works better than desktop

EHRs for common tasks, especially when internet is unreliable.

**Why This Matters:**

**Physician pain:** Desktop EHRs are clunky, slow, require internet

**Patient impact:** Doctors spend more time on computers than with patients

**Market opportunity:** 200K primary care physicians in US, $50/month = $120M potential

**Why Mobile-First:**


---
**Page 18**

- Physicians carry phones everywhere (not laptops)

- Between-patient moments are 5-10 minutes (too short for desktop login)

- Home visits have no desktop access (mobile essential)
- Modern physicians expect mobile tools (grew up with smartphones)

**Why Offline-First:**

- Clinics have spotty WiFi (especially older buildings)

- Home visits have no reliable connection

- Can't wait for sync to document patient visit

- Must work reliably in any environment

**Why React Native:**

- One codebase for iOS and Android (small team can maintain)

- Native performance (vs web wrappers that feel slow)

- Can access native APIs (encryption, biometrics)

- Hiring pool adequate (React Native developers available)

**Trade-offs We Accept:**

**Mobile-first vs feature-complete:**

- Mobile can't do everything desktop can (smaller screen, touch interface)

- Focus on 20% of features that physicians use 80% of time

- Complex workflows stay on desktop (rare, can wait)

- RATIONALE: Better to excel at core tasks than be mediocre at everything

**React Native vs native:**


---
**Page 19**

- Native (Swift/Kotlin) would be slightly faster

- React Native good enough for our use case

- 2 codebases = 2x maintenance (small team can't afford)
- RATIONALE: Speed to market and maintainability over marginal performance

**Last-write-wins vs complex conflict resolution:**

- Sophisticated merging would be better but complex

- Last-write-wins simpler, good enough for single-physician use

- Conflicts rare (physicians don't share patients in our model)

- RATIONALE: Simplicity over edge case perfection

**Alignment Check:**

**We're on track if:**

- Beta physicians using app daily (>80% daily active)

- Offline mode working reliably (no data loss reports)
- HIPAA audit passes (compliance confirmed)

- Note-taking time <3 minutes (vs 8 minutes in EHR)

**We're drifting if:**

- Adding desktop features to mobile (wrong platform)

- Requiring internet for core features (breaks offline promise)

- Optimizing for rare workflows (ignoring 80/20 rule)

</intent>

<!-- VERIFICATION: Self-Checking -->


---
**Page 20**

<verification scope="pre-delivery">

**HIPAA COMPLIANCE (Critical - must pass):**

□ PHI encrypted in transit (TLS 1.3 confirmed)
□ PHI encrypted at rest (AES-256 confirmed)

□ Audit logging captures all PHI access

□ No PHI in logs, analytics, crash reports (manual code review)

□ Auto-logout after 10 minutes (tested)

□ MFA required (tested with SMS and authenticator)

□ Penetration test passed (certified firm report)

**FUNCTIONALITY (Critical - must pass):**

□ Offline mode works (core features accessible without internet)

□ Sync works (offline changes sync when online)

□ Works on iOS 15+ and Android 10+ (device matrix tested)

□ Drug interaction checking works (test cases passed)

□ Appointment scheduling syncs with calendar

**PERFORMANCE (Critical - must pass):**

□ Cold launch <2 seconds on iPhone 11

□ Patient record load <1 second from cache

□ Sync completes <10 seconds for typical day

□ No crashes on target devices (crash-free rate >99.9%)

**CODE QUALITY (High priority):**

□ Tests pass (>80% coverage)

□ No console.logs or debug code in production


---
**Page 21**

□ Code signing certificates valid

□ App Store/Play Store requirements met


## PASS CRITERIA:


ALL HIPAA checks must pass (non-negotiable).

ALL functionality and performance checks must pass.

Code quality should pass (document exceptions).

If HIPAA check fails: STOP. Fix immediately. Re-verify.

Do NOT submit to App Store until ALL critical checks pass.

</verification>


## <!-- END OF TEMPLATE -->


Template 3: API Service (B2B SaaS)
<!-- ========================================= -->


## <!-- COMPLETE SPECIFICATION: B2B API SERVICE -->


<!-- ========================================= -->

<!-- MUST: Hard Boundaries -->

<constraint priority="critical" scope="api-contract">

MUST: RESTful API design (standard HTTP methods, status codes)

MUST: API versioning in URL path (/api/v1/, /api/v2/)
MUST: Backward compatibility for 12 months (v1 supported until v3 release)

MUST: Response time <200ms (p95) for standard operations

MUST: OpenAPI 3.0 documentation (auto-generated from code)


---
**Page 22**

MUST: Rate limiting per API key (1000 requests/hour standard tier)


## VERIFICATION:

- OpenAPI spec validates (swagger-cli validate)

- Backward compatibility test suite (v1 tests pass on v2)

- Load test: k6 run load-test.js (p95 <200ms)

- Rate limiting test: 1001st request returns 429

</constraint>

<constraint priority="critical" scope="reliability">

MUST: 99.9% uptime SLA (< 43.8 minutes downtime per month)

MUST: Graceful degradation (partial service better than full outage)

MUST: Circuit breakers for external dependencies (fail fast, not slow)

MUST: Health check endpoint (/health returns 200 if operational)

MUST: Database connection pooling (prevent connection exhaustion)


## VERIFICATION:


- Monitor uptime: UptimeRobot tracking

- Test circuit breaker: Disable dependency, verify graceful handling

- Load test connection pool: 1000 concurrent connections, no exhaustion

- Health check responds <50ms

</constraint>

<constraint priority="critical" scope="security">

MUST: API key authentication (unique per customer)

MUST: HTTPS only (no HTTP endpoints in production)


---
**Page 23**

MUST: Rate limiting per API key (prevent abuse)

MUST: Input validation on all endpoints (prevent injection)

MUST: No sensitive data in logs (API keys, passwords, PII)


## VERIFICATION:


- Security scan: OWASP ZAP automated scan

- Manual review: No API keys or passwords in logs

- Input validation test: SQL injection, XSS payloads rejected

- HTTP endpoint test: All HTTP requests redirect to HTTPS

</constraint>

<!-- SHOULD: Flexible Preferences -->

<guideline priority="high" scope="api-design">

SHOULD: Pagination for list endpoints (limit=100 default, max=1000)

SHOULD: Filtering and sorting query parameters (standard conventions)

SHOULD: Webhook notifications for async operations
SHOULD: Idempotency keys for POST/PUT operations (prevent duplicate processing)


## RATIONALE:


These improve API usability and prevent common integration issues.

All are standard B2B API practices customers expect.

WHEN VIOLATING: Document why (e.g., endpoint returns <100 items always)

</guideline>

<guideline priority="medium" scope="developer-experience">


---
**Page 24**

SHOULD: Code examples in docs (curl, Python, JavaScript, Ruby)

SHOULD: Sandbox environment for testing (free tier, no credit card)

SHOULD: Detailed error messages (what went wrong, how to fix)
SHOULD: SDKs for popular languages (Python, JavaScript to start)


## RATIONALE:


Developer experience drives adoption. Better docs = more customers.

</guideline>

<!-- CONTEXT: Planning Information -->

<context scope="business">

**Company:** B2B SaaS (Series B), 40-person team

**Product:** [REPLACE: Data enrichment API / Payment processing / etc.]

**Customers:** Other software companies (B2B, not end users)

**Pricing:** Freemium (1K free requests/month, then $0.01 per request)

**Current Status:** 500 customers, $80K MRR, growing 15% month-over-month

**Revenue Model:**

- Free tier: Marketing (developers test before buying)

- Standard tier: $99/month + overage ($0.01/request beyond 10K)

- Enterprise tier: Custom pricing (volume discounts, SLA guarantees)

**Competitors:**

- [REPLACE: Competitor A - cheaper but less reliable]

- [REPLACE: Competitor B - expensive but full-featured]

- Our niche: Balance of price, reliability, and ease of use


---
**Page 25**

</context>

<context scope="technical">
**Technology Stack:**

- API: Node.js 20 + Express (REST)

- Database: PostgreSQL 15 (primary), Redis (cache)

- Queue: RabbitMQ (async processing)

- Hosting: AWS multi-region (us-east-1, eu-west-1)

- CDN: CloudFront (reduce latency globally)

**Team:**

- 6 backend engineers (Node.js, Python)

- 2 DevOps engineers (AWS, Kubernetes)

- 2 QA engineers (API testing specialists)

- 1 technical writer (API documentation)

**Scale:**

- Current: 10M requests/month

- Target: 100M requests/month within 1 year

- Peak: 5K requests/second (during business hours)

**Constraints:**

- Multi-region complexity (data consistency challenges)

- Cost sensitivity (margins on $0.01/request are thin)

- Performance critical (customers integrate us in their critical paths)

</context>


---
**Page 26**

<context scope="customers">

**Primary Users:** Software developers at B2B companies
- Tech proficiency: High (professional developers)

- Industries: Fintech, e-commerce, SaaS platforms

- Company size: 10-500 employees (small to mid-size)

- Use cases: [REPLACE: Data validation / Payment processing / etc.]

**Integration Patterns:**

- Server-side integration (Node.js, Python, Ruby)

- Batch processing (nightly jobs)

- Real-time processing (user-facing features)

**Pain Points:**

- Competitor APIs unreliable (frequent downtime)

- Poor documentation (hard to integrate)
- Slow support response (blocked developers)

- Unexpected rate limits (no warning, just 429s)

**Success Criteria:**

- Integration time <4 hours (from signup to first API call)

- Support ticket rate <1% of customers

- API satisfaction >4.5/5 (NPS survey)

- Zero unplanned downtime (99.9% uptime)

</context>


---
**Page 27**

<!-- INTENT: The Why -->

<intent scope="api-service">

**Primary Goal:**
Provide reliable, easy-to-integrate API that developers love, driving

adoption and revenue growth in competitive B2B market.

**Why This Matters:**

**Market:** $500M addressable market in [REPLACE: data enrichment / payments]

**Competition:** Established players but opportunities in developer experience

**Revenue:** Need 100M requests/month to reach profitability ($1M MRR)

**Why These Choices:**

**Why RESTful over GraphQL:**

- REST more familiar to our target developers (smaller learning curve)

- Easier to cache (CloudFront works well with REST)
- Simpler infrastructure (less complexity to operate)

- GraphQL adds value for complex data models (ours is simple)

**Why Node.js:**

- Team expertise (6 engineers strong in Node)

- Async I/O good for API workloads

- npm ecosystem strong (libraries for everything)

- Hiring pipeline good (Node developers plentiful)

**Why Multi-region:**


---
**Page 28**

- Global customers need low latency

- Compliance requires EU data in EU

- Redundancy improves uptime (one region down, others continue)

**Trade-offs We Accept:**

**REST vs GraphQL:**

- GraphQL would give clients more flexibility

- But adds complexity for both us and customers

- Our API is simple enough for REST

- RATIONALE: Simplicity over flexibility for our use case

**Multi-region complexity:**

- Simpler to run single region (lower operational burden)

- But latency matters for our customers (API in critical path)

- Eventual consistency acceptable (not financial transactions)
- RATIONALE: Better customer experience worth operational complexity

**Freemium vs paid-only:**

- Paid-only would be simpler (no free tier abuse)

- But free tier is marketing (developers test before buying)

- Free tier abuse preventable (rate limits, usage monitoring)

- RATIONALE: Customer acquisition through developer trial

**Alignment Check:**


---
**Page 29**

**We're on track if:**

- Uptime consistently >99.9% (SLA met)

- P95 response time <200ms (performance target met)
- Customer churn <5% monthly (satisfaction high)

- Documentation rated >4.5/5 (easy to integrate)

**We're drifting if:**

- Adding features that slow down API (performance regression)

- Downtime increasing (reliability declining)

- Support tickets growing faster than customers (poor docs/DX)

- Optimizing for enterprise edge cases (ignoring SMB majority)

</intent>

<!-- VERIFICATION: Self-Checking -->

<verification scope="pre-deployment">

**API CONTRACT (Critical - must pass):**
□ OpenAPI spec valid (swagger-cli validate openapi.yaml)

□ Backward compatibility tests pass (v1 clients work with v2)

□ All endpoints documented (no undocumented routes)

□ Rate limiting works (1001st request returns 429)

**PERFORMANCE (Critical - must pass):**

□ Load test passes: k6 run load-test.js

- P95 response time <200ms ✓

- P99 response time <500ms ✓

- 5K requests/second sustained (no errors) ✓


---
**Page 30**

□ Database connection pool stable under load

□ Circuit breakers trigger correctly (dependency failure test)

**RELIABILITY (Critical - must pass):**

□ Health check endpoint responds <50ms

□ Graceful shutdown works (no dropped connections)

□ Database failover tested (primary fails, replica takes over)

□ Multi-region failover tested (one region down, others serve traffic)

**SECURITY (Critical - must pass):**

□ API key authentication required on all endpoints

□ HTTPS enforced (HTTP redirects or rejects)

□ Input validation prevents injection (OWASP ZAP scan clean)

□ No sensitive data in logs (audit log files)

□ Rate limiting prevents abuse

**DEVELOPER EXPERIENCE (High priority):**

□ Documentation complete (all endpoints, examples)

□ Sandbox environment working (free testing)

□ Error messages helpful (what + why + how to fix)

□ Code examples tested (curl examples work)


## PASS CRITERIA:


ALL critical checks must pass before production deployment.

High priority checks should pass (document exceptions).


---
**Page 31**

If critical check fails: Fix, re-verify, then deploy.

Monitor post-deployment: Response times, error rates, uptime.

</verification>


## <!-- END OF TEMPLATE -->


Quick Customization Guide


### To adapt these templates:



## 1. Replace Placeholders


### Look for [REPLACE: ...] markers and fill in your specifics:


• Technology stack

• Business domain

• User types

• Competitors


## 2. Remove Irrelevant Sections



### Delete entire sections that don't apply:


• E-commerce template has payments → Not needed for internal tool
• Healthcare template has HIPAA → Not needed for non-healthcare

• API template has multi-region → Not needed for single-region service


## 3. Add Domain-Specific Requirements



### Include specialized needs:


• Financial services: SOX compliance, audit trails

• Education: FERPA compliance, accessibility (WCAG 2.1)

• Gaming: Low latency (<50ms), high throughput, anti-cheat

## 4. Adjust Priorities



### Change priority levels based on your context:


• Startup MVP: Performance "high" not "critical" (ship fast, optimize later)


---
**Page 32**

• Enterprise: Compliance "critical" (non-negotiable)

• Internal tool: Documentation "medium" (team knows the system)


## 5. Customize Verification


### Adapt verification to your tools and processes:


• Different testing framework? Update commands

• Different hosting? Update deployment verification

• Different monitoring? Update production checks

Common Patterns Across Domains

### All good specifications should have:


Security constraints (appropriate to risk level)

Performance targets (with measurement criteria)

Verification protocols (objective pass/fail)

Business context (why we're building this)

User context (who will use this, how)

Technical context (stack, team, infrastructure) Intent (the why, trade-offs, alignment
check)


### Avoid these anti-patterns:


Vague constraints ("secure", "fast", "good" without definition)

Missing context (constraints without rationale)

No verification (can't check if requirements met)

Copy-paste without adaptation (wrong domain assumptions)

Over-constraining (too many rigid MUSTs)

Next Steps


### After choosing and customizing a template:



---
**Page 33**


## 1. Review against Section 7 pitfalls (avoid common mistakes)



## 2. Get team review (fresh eyes catch issues)



## 3. Test with small scope (validate spec on small feature first)


## 4. Iterate based on results (specs improve with feedback)



### Remember:


• Templates are starting points, not straitjackets

• Adapt to your specific needs

• Specifications improve over time through iteration

• When in doubt, be specific (under-constraining is common pitfall)


## END OF APPENDIX A


Document Version: 1.0.0
Last Updated: 2026-02-02
Three complete templates ready for immediate use Copy, customize, and deploy
