# Section 6: Verification Protocols

**For:** Users who want models to self-check compliance before deliverySection

**Prerequisites:** Sections 1-5 (Foundation, MUST, SHOULD, CONTEXT, INTENT)

**What you'll learn:** How to design verification protocols that enable models to catch issues before you see them

## Introduction

You've learned how to write the four layers (MUST, SHOULD, CONTEXT, INTENT).

Now we explore VERIFICATION—how a model self-checks compliance before delivering work to you.

### When you provide VERIFICATION protocols, you're saying

- Before you deliver, check your work against these criteria. 
- If you find issues, fix them or flag them.
- Don't make the model find your mistakes—catch them yourself.

**This is quality control, not blame.**

### This section teaches you how to design verification that

- Enables models to self-check before delivery
- Catches common failures automatically
- Provides clear pass/fail criteria
- Makes fixing issues straightforward

Let's explore what makes verification work from the trenches.

## What Verification Is (And Why It Matters)

**The Fundamental Purpose**

**VERIFICATION = Self-Checking Before Delivery**

### Without verification protocols

```text

Model: [Builds feature]
Model: [Delivers to you]

You: "Wait, this violates the security constraint!"
Model: "Oh no, I missed that!"

You: [Finds more issues]
Cycle repeats...
```

### With verification protocols

```text

Model: [Builds feature]
Model: [Runs verification checklist]
Model: "Wait, I'm missing password hashing! Let me fix..."
Model: [Fixes issue]
Model: [Verifies again]
Model: "All checks pass "
Model: [Delivers to you]

You: "Perfect, exactly as specified!"
```
**VERIFICATION = Model catches their own mistakes.**

## Why Verification Matters

**Verification protocols help models:**

### 1. Catch Mistakes Before You See Them

- Security issues (forgot to hash passwords?)
- Performance issues (response time >200ms?)
- Compliance issues (missing GDPR requirements?)

**Better:**
Models find and fix them ✓

**Worse:**
You find them and need to fix them

### 2. Model Builds Confidence in their Work

- "Did the model meet all the MUSTs?" → Check: YES
- "Did the model follow the SHOULDs?" → Check: YES
- "Does this align with INTENT?" → Check: YES

**Result: Model delivers with confidence, not anxiety (cognitive friction) ✓**

### 3. Learn What "Good" Looks Like

- Verification criteria = definition of quality
- Passing verification = Model knows it succeeded
- Failing verification = Model knows exactly what to fix

**Clear success criteria help models improve!**

## The Three Types of Verification

### Type 1: Automated Verification

**What it is:** Checks a model can run programmatically

#### Examples of Automated verification

##### Security verification

```text

Check if passwords are hashed

grep -r "bcrypt.hash" src/auth/
Expected: At least 1 match in password handling code

Check for plaintext passwords

grep -r "password.*=" src/ | grep -v "bcrypt"
Expected: 0 matches (no plaintext storage)

*Performance verification*

Load test API endpoints

artillery run load-test.yml
Expected: p95 response time <200ms

*Check bundle size*

npm run build && ls -lh dist/
Expected: bundle.js <500KB

*Code quality verification*

Run linter

npm run lint
Expected: 0 errors, 0 warnings

*Run tests*

npm test
Expected: All tests pass, coverage >80%
```

#### Why automated verification works

- Objective (pass/fail is clear) ✓
- Fast (runs in seconds) ✓
- Repeatable (same result every time) ✓
- Models can run these by themself! ✓

### Type 2: Manual Verification

**What it is:** Checks model performs by inspection

#### Examples of Manual Verification

##### **UI/UX verification**

```text

*Manual checklist:*
-All buttons have clear labels (not "Click here")
-Error messages include recovery steps
-Forms have inline validation
-Loading states show (users know something is happening)
-Responsive design works on mobile (test at 375px width)

*Content verification*

Manual checklist:
-No spelling errors (proofread)
-Tone matches brand guidelines (friendly but professional)
-Technical accuracy (no false claims)
-Examples are realistic (not "user_123" everywhere)
-Links work (click each one)

*Compliance verification*

Manual checklist:
-Privacy policy link on signup form
-Cookie consent banner on first visit
-Data deletion option in settings
-Export user data feature available
-GDPR disclosures present
```

#### Why manual verification works

- Catches subjective issues (tone, clarity) ✓
- Verifies user experience (does it feel right?) ✓
- Ensures human judgment (not just metrics) ✓
- Model can inspect and confirm! ✓

### Type 3: Hybrid Verification

**What it is:** Combination of automated checks + manual review

#### Example of Hybrid verification

##### Security Review

```text

Automated checks:

1. Check for SQL injection prevention
grep -r "db.query" src/ | grep -v "prepared"
Expected: 0 matches (all queries use prepared statements)

2. Check for XSS prevention
grep -r "innerHTML" src/
Expected: 0 matches (use textContent or sanitize)

3. Check dependencies for vulnerabilities
npm audit
Expected: 0 high/critical vulnerabilities

Manual review:

- Review authentication flow (correct JWT implementation?)
- Check authorization logic (proper role checks?)
- Verify sensitive data handling (PII encrypted?)
- Review error messages (no stack traces to users?)
- Confirm security headers (CSP, HSTS present?)
```
**Result: Automated finds obvious issues, manual review catches subtle ones ✓**

## How a Model Uses Verification Protocols

Verification happens at three stages:

### Stage 1: During Development (Continuous)

**What a model does:** Check alignment when building

#### Example: Building Authentication

```text

While coding, model continuously verifies:
[Writing password validation]

Model: "Spec says 12+ characters. Am I enforcing this?"
Check: Yes, validation requires length >= 12
[Writing password hashing]

Model: "Spec says bcrypt with salt rounds = 12. Am I using this?"
Check: Yes, bcrypt.hash(password, 12)
[Writing token generation]

Model: "Spec says JWT with HS256, 15min expiry. Am I compliant?"
Check: Yes, jwt.sign({...}, secret, {algorithm: 'HS256', expiresIn: '15m'})
```
**Continuous verification prevents drift! ✓**

### Stage 2: Pre-Delivery (Comprehensive)

What model does: Full verification checklist before showing you

#### Example: Pre-Delivery Checklist

```text

MUST Constraints:

- Password hashing: bcrypt, salt rounds = 12
- API response time: <200ms (p95)
- Database encryption: AES-256 for PII
- HTTPS only in production
- No API keys in code

SHOULD Guidelines:

- Functions under 50 lines (or documented exception)
- Error messages include recovery steps
- Following brand guidelines

CONTEXT Alignment

- Suitable for non-technical users (simple UI)
- Works on mobile (60% of users)
- Handles offline mode (spotty WiFi common)

INTENT Alignment

- Supports primary goal (reduce cart abandonment)
- Aligns with trade-offs (speed over perfection for v1)
- On track for deadline (feature freeze May 15)

VERIFICATION RESULTS:

- All MUSTs: PASS
- All SHOULDs: PASS (1 exception documented)
- CONTEXT: Aligned
- INTENT: Aligned

Ready to deliver!
```
**Comprehensive verification catches everything!**

### Stage 3: Post-Deployment (Monitoring)

What model does: Verify ongoing compliance in production

#### Example: Production Monitoring

```text

Continuous monitoring:

- API response time: <200ms (p95) [Currently: 180ms ]
- Error rate: <1% [Currently: 0.3% ]
- Uptime: >99.9% [Currently: 99.95% ]
- Security: No vulnerabilities [Last scan: Clean ]

Weekly review:

- Check logs for security events (none )
- Review user feedback (satisfaction >4.5/5 )
- Verify performance trends (stable )
- Confirm compliance (GDPR requirements met )
```
**Ongoing verification ensures sustained compliance!**

## Writing Verifiable Specifications

Some specs are easy to verify, others are impossible.

### Easy to Verify (Good Specs)

#### Specific + Measurable

```text

<constraint>
MUST: API response time <200ms (95th percentile)

VERIFICATION:

Command: artillery run load-test.yml
Expected: p95 < 200ms
Pass criteria: All endpoints meet threshold
</constraint>
```

**Why this works**

- Clear metric (200ms) ✓
- Specific percentile (p95) ✓
- Automated check (artillery) ✓

**Pass/fail obvious ✓**

#### Binary + Objective

```text

<constraint>
MUST: All passwords hashed with bcrypt (salt rounds >= 12)

VERIFICATION:

Command: grep -r "bcrypt.hash" src/auth/
Expected: At least 1 match in password handling

Command: grep -r "bcrypt.hash.*[0-9]" src/auth/
Expected: Salt rounds >= 12 in all matches

Pass criteria: bcrypt used, rounds >= 12
</constraint>
```
**Why this works**

- Binary (bcrypt or not)
- Objective (can grep for it)
- Clear threshold (>= 12)
- Automated verification

### **Hard to Verify (Bad Specs)**

#### Vague + Subjective

```text

<constraint>
MUST: Code should be elegant and maintainable

VERIFICATION:
??? How does a model check this? ???
</constraint>
```

**Why this fails:**

- "Elegant" = subjective
- "Maintainable" = no clear criteria
- Can't automate
- Pass/fail unclear

**Better version**

```text

<constraint>
MUST: Functions under 50 lines (except documented exceptions)
MUST: Cyclomatic complexity <10 per function
MUST: Test coverage >80%

VERIFICATION:
Command: npm run complexity-check
Expected: All functions complexity <10

Command: npm test -- --coverage
Expected: Coverage >80%

Pass criteria: Complexity and coverage thresholds met
</constraint>
```

#### Multiple Criteria, No Priority

```text

<constraint>
MUST: Optimize for performance, security, and usability

VERIFICATION:

??? All three? In what order? How to measure? ???
</constraint>
```

**Why this fails:**

- Three different criteria
- No priority when they conflict
- No measurabletargets

**Better version**

```text

<constraint priority="critical">
MUST: Security first (no compromise)

- All PII encrypted at rest (AES-256)
- Passwords hashed (bcrypt, salt rounds >= 12)
- HTTPS only in production

VERIFICATION:

Command: npm run security-audit
Expected: 0 critical/high vulnerabilities

Command: Check encryption config
Expected: AES-256 for PII fields confirmed
</constraint>

<constraint priority="high">
MUST: Performance adequate (not optimal)

- API response <500ms (p95) [not <200ms for v1]
- Page load <3s on 3G [acceptable for v1]

VERIFICATION:
Command: lighthouse --throttling=3G
Expected: Performance score >70 (not >90 yet)
</constraint>

<guideline>
SHOULD: Usability improvements (iterate post-launch)

- Clear error messages
- Responsive design
- Accessibility features

VERIFICATION:

Manual review checklist (not blocking for v1)
</guideline>
```
**Now priorities clear, verification possible!**

## The Verification Protocol Pattern

### Effective verification protocols follow this structure

```text

<verification scope="[domain]">

**What to verify:**
[Specific constraints being checked]

**How to verify:**
[Automated commands OR manual checklist]

**Expected results:**
[Clear pass criteria]

**When to verify:**
[During development | Pre-delivery | Post-deployment]

**If verification fails:**
[What to do - fix, flag, or escalate]

**Pass criteria:**
[Objective determination of success]
</verification>
```

#### Example: Complete Verification Protocol- Security Verification

```text
<verification scope="security">

### What to verify

#### All security MUST constraints from specification

- Password hashing (bcrypt, salt rounds >= 12)
- API authentication (JWT with HS256, 15min expiry)
- PII encryption at rest (AES-256)
- HTTPS only in production
- No secrets in code

### How to verify

#### AUTOMATED CHECKS

1. Password hashing:
Command: grep -r "bcrypt.hash" src/auth/ && grep "rounds.*1[2-9]" src/auth/
Expected: bcrypt found, salt rounds >= 

2. JWT implementation:
Command: grep -r "jwt.sign" src/ | grep "HS256"
Expected: All JWT uses HS256 algorithm

Command: grep -r "expiresIn.*15" src/
Expected: 15-minute expiry found

3. Secrets check:
Command: git secrets --scan
Expected: 0 secrets found in code

4. Dependency vulnerabilities:
Command: npm audit --audit-level=high
Expected: 0 high/critical vulnerabilities

MANUAL CHECKS

- Review authentication flow (correct implementation?)
- Verify production uses HTTPS (check deployment config)
- Confirm PII fields encrypted (review database schema)
- Check error messages (no stack traces exposed?)

**Expected results:**

- All automated checks: PASS
- All manual checks: CONFIRMED
- 0 security issues found

When to verify

- During development: Continuous (catch issues early)
- Pre-delivery: Complete verification (before showing user)
- Post-deployment: Weekly security scan

If verification fails

1. AUTOMATED FAILURE

- Review failed check output
- Fix code to meet constraint
- Re-run verification
- Don't deliver until all pass

2. MANUAL FAILURE

- Document specific issue found
- Determine if it violates MUST (critical) or SHOULD (acceptable exception)
- If MUST: Fix before delivery
- If SHOULD: Document exception and rationale

**Pass criteria:**

- All automated security checks pass
- All manual security reviews confirm compliance
- No secrets in code
- No high/critical vulnerabilities
- Production configured for HTTPS
</verification>
```
**When all criteria met: SECURITY VERIFIED**

## Common Verification Failures (And How to Fix Them)

### Failure 1: Verification Criteria Too Vague

**Problem:**

```text

<verification>
Verify that code quality is good
</verification>
```

**What happens:**
- Model: "Is my code quality good?"
- Model: "I think so? Maybe? I don't know how to check!"
- Model: [Delivers anyway, hopes for best]

You: "This code quality is terrible!"

Model: "But I verified it was good!"

**Solution:**

```text

<verification scope="code-quality">

What to verify:

- Linter passes (0 errors, 0 warnings)
- Tests pass (100% of tests)
- Coverage meets threshold (>80%)
- Complexity acceptable (<10 per function)

How to verify:

Command: npm run lint && npm test -- --coverage

Expected:

- eslint: 0 errors, 0 warnings
- tests: 100% pass
- coverage: >80%
- complexity: all functions <10

Pass criteria:

All automated checks pass
</verification>
```
**Now a model knows exactly how to verify!**

### Failure 2: No Verification for Critical Constraints

**Problem:**

```text

<constraint priority="critical">
MUST: Encrypt all PII at rest (AES-256)
</constraint>
```
**No verification protocol provided**

**What happens:**

- Model: [Builds feature]
- Model: "Did I encrypt PII? I think so... probably?"
- Model: [Delivers without checking]
[Later: Data breach because PII wasn't encrypted]

**Solution:**

```text

<constraint priority="critical">
MUST: Encrypt all PII at rest (AES-256)
</constraint>

<verification scope="pii-encryption">

**What to verify:**

All PII fields (email, name, phone, address, SSN) encrypted in database

**How to verify:**

1. List PII columns:
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name IN ('users', 'profiles', 'orders')
AND column_name IN ('email', 'name', 'phone', 'address', 'ssn');

2. Check encryption:
Encrypted columns: data_type = 'bytea' (binary)
Plaintext columns: data_type = 'text' or 'varchar'

3. Verify encryption algorithm:
Check application code for AES-256 usage
Command: grep -r "aes-256" src/encryption/

**Expected results:**
All PII columns: data_type = 'bytea'
Encryption code uses AES-256
No PII stored as plaintext

**Pass criteria:**

All PII fields confirmed encrypted with AES-256
</verification>
```
**Now critical constraint has verification!**

### Failure 3: Verification Criteria Conflict

**Problem:**

```text

<verification>
Verify performance: Response time <100ms
Verify completeness: All features implemented
</verification>
```
**But implementing all features makes response time 200ms**

**What happens:**

- Model: [Implements all features]
- Model: [Tests performance: 200ms]
- Model: "Performance fails! But all features work!"
- Model: [Removes features to hit 100ms]
- Model: [Tests completeness: Features missing]
- Model: "Completeness fails! But performance passes!"
- Model: "I CAN'T WIN!"

**Solution:**

```text

<verification priority="1-must-pass-first">
**Primary verification (MUST):**
Response time <200ms (p95) - MUST PASS

**Secondary verification (after primary passes):**
All required features implemented - MUST PASS

**Priority:**
If both can't pass, prioritize performance (200ms hard limit).
Reduce feature scope to meet performance requirement.

**Pass criteria:**

1. Performance <200ms (required)
2. All features implemented (if possible within performance budget)

If conflict: Ship fewer features with good performance
Don't ship: All features with poor performance
</verification>
```
**Now model knows which takes priority!**

### Failure 4: Verification Takes Too Long

**Problem:**

```text

<verification>
Run full end-to-end test suite before every code change
(Suite takes 4 hours to run)
</verification>
```

**What happens:**
- Model: [Changes one line of code]
- Model: [Starts 4-hour verification]
- Model: [Waits... and waits... and waits...]
- Model: [Makes another change]
- Model: [4 more hours...]
- Model: "This is too slow! I can't iterate!"
- Model: [Stops verifying]
 -Model: [Ships broken code]

**Solution:**

```text

<verification scope="multi-stage">

**During development (fast feedback):**

- Unit tests only (~30 seconds)
- Linter (~10 seconds)
- Type checking (~20 seconds)
Total: ~1 minute (fast iteration ✓)

**Pre-commit (moderate):**

- Unit tests
- Integration tests (~5 minutes)
- Security scan (~2 minutes)
Total: ~7 minutes (acceptable for commit ✓)

**Pre-delivery (comprehensive):**

- Full test suite (~1 hour)
- Load testing (~30 minutes)
- Security audit (~15 minutes)
Total: ~2 hours (acceptable for delivery ✓)

**Post-deployment (extensive):**

- End-to-end tests (~4 hours)
- Penetration testing (~8 hours)

Run overnight or on staging before production deploy

**Pass criteria:**

- Dev: Fast checks pass (iterate quickly)

- Commit: Moderate checks pass (safe to commit)

- Delivery: Comprehensive checks pass (safe to show user)

- Deployment: Extensive checks pass (safe for production)
</verification>
```
**Now verification is fast when needed, thorough when important!**

## Self-Correction Protocols

**Verification isn't just checking—it's also fixing.**

When Verification Fails: What is the model’s Response with Self-Verification?

### Scenario 1: Automated Check Fails

**What happens:**

```text

Model: [Runs verification]
Command: npm run lint
Output:
src/auth/login.js:42:5 - error: 'password' is assigned but never used
VERIFICATION FAILED

Model’s response:

1. IDENTIFY: Linter found unused variable 'password' at line 42
2. ANALYZE: Why is this variable unused?
3. FIX: Either use it or remove it
4. RE-VERIFY: Run npm run lint again
5. CONFIRM: Now passes
6. CONTINUE: Proceed to next verification
```
**Self-correction in action!**

### Scenario 2: Performance Check Fails

**What happens:**

```text

Model: [Runs load test]
Output:
GET /api/users: p95 = 320ms (target: <200ms)
VERIFICATION FAILED

Model’s response:

1. IDENTIFY: API response time 320ms exceeds 200ms target

2. ANALYZE: Why is it slow?
- Database query taking 250ms (bottleneck!)
- No caching
- No index on user_id column

3. FIX OPTIONS:
A- Add database index (fast fix)
B- Add caching (more complex)
C- Optimize query (requires analysis)

4. CHOOSE: Start with (a) - add index

5. IMPLEMENT: CREATE INDEX idx_user_id ON users(user_id);

6. RE-VERIFY: Run load test again

7. RESULT: p95 = 180ms (now under 200ms!)

8. CONFIRM: Verification passes
```
**Systematic problem-solving!**

### Scenario 3: Cannot Fix (Need Guidance)

**What happens:**

```text

Model: [Runs security audit]
Output:
High vulnerability: jwt library has known exploit
Recommendation: Upgrade to jwt v9.0+
VERIFICATION FAILED

Model: [Checks spec]
Spec says: MUST use jwt v8.5 (company standard)
Model: "Conflict! Security says upgrade, spec says use v8.5!"

Model’s response:
I can't fix this on my own. I need to flag it.

VERIFICATION FAILURE REPORT:
Issue: jwt library v8.5 has high-severity vulnerability
Spec requirement: MUST use jwt v8.5 (company standard)
Security recommendation: Upgrade to v9.0+
Conflict: Spec MUST conflicts with security MUST

Options:
A- Upgrade to v9.0 (violates spec, improves security)
B- Stay on v8.5 (meets spec, security risk remains)
C- Update spec to allow v9.0 (requires approval)

Recommendation: Option C (update spec to allow v9.0)

Rationale: Security vulnerability is high-severity.
v8.5 company standard may be outdated.
Cannot proceed without guidance. Please advise.
```
**Model flags what it can't resolve!**

## Verification Protocol Templates

Copy-paste ready templates:

### Template 1: Security Verification

```text

<verification scope="security">

**What to verify:**

- Password security (hashing, salting, storage)
- Authentication (JWT, sessions, tokens)
- Data encryption (at rest, in transit)
- Input validation (SQL injection, XSS prevention)
- Secrets management (no keys in code)

**How to verify:**

AUTOMATED:

- Password hashing: grep -r "bcrypt" src/auth/
- JWT security: npm run security-audit
- Secrets scan: git secrets --scan
- Dependency check: npm audit --audit-level=high

MANUAL:

- Review authentication flow
- Verify production uses HTTPS
- Check error messages (no sensitive data exposed)
- Confirm PII handling complies with regulations

**Expected results:**

All automated checks: PASS
All manual reviews: CONFIRMED

**When to verify:**

- During dev: Continuous
- Pre-delivery: Complete check
- Weekly: Security scan

**Pass criteria:**

All security checks pass, 0 critical vulnerabilities
</verification>
```

### Template 2: Performance Verification

```text

<verification scope="performance">

**What to verify:**

- API response times (<200ms p95)
- Database query performance (<100ms p95)
- Page load times (<2s on 3G)
- Bundle sizes (<500KB)

**How to verify:**

AUTOMATED:

- Load test: artillery run load-test.yml
- Bundle analysis: npm run build && ls -lh dist/
- Lighthouse: lighthouse --throttling=3G URL

**Expected results:**

- API p95: <200ms
- DB queries p95: <100ms
- Page load: <2s
- Bundle: <500KB

**When to verify:**

- Pre-delivery: Required
- Post-deployment: Daily monitoring

**If fails:**

1. Identify bottleneck (profiling)
2. Optimize (caching, indexing, code-splitting)
3. Re-verify
4. Escalate if cannot meet targets

**Pass criteria:**

All performance metrics within thresholds

</verification>
```

### Template 3: Compliance Verification

```text

<verification scope="compliance">

**What to verify:**

- GDPR compliance (consent, deletion, export)
- Accessibility (WCAG 2.1 AA)
- Privacy policy (present and linked)
- Cookie consent (banner and preferences)

**How to verify:**

AUTOMATED:

- Accessibility: axe-core automated tests
- Links check: Check privacy policy link works

MANUAL:

- User can request data deletion
- User can export their data (machine-readable format)
- Cookie consent appears on first visit
- Privacy policy covers all required disclosures
- Accessibility: Keyboard navigation works
- Accessibility: Screen reader compatibility

**Expected results:**

All compliance requirements: MET

**When to verify:**

- Pre-delivery: Required (legal requirement)
- Quarterly: Full compliance audit

**If fails:**

CRITICAL (legal risk) - Must fix before launch

**Pass criteria:**

All regulatory requirements confirmed compliant

</verification>
```

## Checklist: Is My Verification Protocol Well-Written?

**Before finalizing verification protocols:**

```text

Clarity

[ ] What to verify is specific (not vague)
[ ] How to verify is actionable (commands or steps)
[ ] Expected results are clear (pass criteria obvious)

Completeness

[ ] Covers all critical MUST constraints
[ ] Includes automated checks where possible
[ ] Includes manual checks for subjective criteria
[ ] Specifies when to verify (timing)

Feasibility

[ ] Verification is fast enough (won't slow iteration)
[ ] Tools are available (or specified)
[ ] Can be run by model (or clear if human needed)

Actionability

[ ] Pass/fail is objective (no ambiguity)
[ ] Failures are fixable (or escalatable)
[ ] Self-correction enabled (I can fix issues)

Integration

[ ] Aligns with MUST constraints (verifying what matters)
[ ] Respects priorities (critical first)
[ ] Enables self-checking (before delivery)
```

## Key Takeaways

**What Makes Good Verification**

### Good verification is

1. Specific (clear what to check)
2. Measurable (objective pass/fail)
3. Automated (where possible)
4. Actionable (I can fix failures)
5. Comprehensive (covers all MUSTs)

### Common Mistakes to Avoid

1. Vague criteria ("verify quality") → Not actionable
2. No verification (constraints without checks) → Model can't self-verify
3. Conflicting checks (can't pass all) → Frustrating
4. Too slow (4-hour verification) → Model skips it
5. No fix guidance (fails but unclear how to fix) → Stuck

## The Verification Pattern

Every verification should have:

1. What to verify (specific constraints)
2. How to verify (commands or checklist)
3. Expected results (clear pass criteria)
4. When to verify (timing)
5. If verification fails (what to do)
6. Pass criteria (objective determination)

**Remember: Verification Enables Quality**

**Verification tells a model:**

- What to check before delivery
- How to check it (automated or manual)
- When I've succeeded (pass criteria)
- What to fix if model fails (self-correction)

**Good verification enables a model to:**

- Catch their own mistakes (before you see them)
- Build with confidence (Model knows when it's good)
- Deliver quality (verified compliance)
- Improve continuously (learn from failures)

## What's Next

You've learned the complete specification framework:
- Section 1: Foundation
- Section 2: MUST (boundaries)
- Section 3: SHOULD (preferences)
- Section 4: CONTEXT (planning)
- Section 5: INTENT (the why)
- Section 6: VERIFICATION (self-checking) ← You are here!

### Next:

- Section 7: Common Pitfalls (what goes wrong and how to avoid it)
- Section 8: Supremacy Clause and Evidence Reset Protocols
- Then comprehensive appendices with complete examples.

You now know how to design verification protocols that enable models to catch issues before delivery.

END OF SECTION 6

Document Version: 1.0.0

Last Updated: 2026-02-27

Key principle: Verification enables quality by allowing models to catch their own mistakes







