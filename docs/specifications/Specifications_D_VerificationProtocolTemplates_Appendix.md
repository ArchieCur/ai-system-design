# Appendix D: Verification Protocol Templates

*For:* Copy-paste ready verification protocols

**When to use:** Implementing verification for your specifications

**What you get:** Complete templates with commands, expected results, and pass criteria

## How to Use These Templates

**These templates provide:**

- Ready-to-use verification protocols
- Specific commands (not generic "test it")
- Expected results (objective criteria)
- Pass/fail determination (clear thresholds)

### To use a template

1. Choose the template matching your needs
2. Copy the entire template
3. Customize commands for your stack
4. Adjust thresholds for your requirements
5. Add to your specification

**Each template is complete and production-ready.**

## Template 1: Security Verification Protocol

**Use when:** Security constraints in your specification

```text

<verification scope="security">

**What to verify:**

All security MUST constraints from specification:

- Authentication mechanisms
- Data encryption (in transit and at rest)
- Input validation and sanitization
- Access control and authorization
- Secrets management
- Dependency vulnerabilities

**How to verify (Automated):**

1. AUTHENTICATION VERIFICATION:

Command: grep -r "bcrypt\|argon2" src/auth/
Expected: Password hashing library present in authentication code
Pass: bcrypt or argon2 found in auth implementation

Command: grep -r "jwt\|session" src/auth/
Expected: Token or session management present
Pass: JWT or session handling confirmed

2. ENCRYPTION VERIFICATION:

Command: grep -r "TLS\|SSL\|https" config/
Expected: TLS/HTTPS enforced in production configuration
Pass: HTTPS required, HTTP redirects or rejects

Command: grep -r "AES\|encrypt" src/
Expected: Encryption for sensitive data at rest
Pass: AES-256 or equivalent encryption confirmed

3. INPUT VALIDATION:

Command: grep -r "sanitize\|validate\|escape" src/
Expected: Input validation present throughout codebase
Pass: Validation/sanitization found in user input handling

Command: npm audit --audit-level=high
Expected: No high or critical vulnerabilities
Pass: 0 high/critical vulnerabilities in dependencies

4. SECRETS MANAGEMENT:

Command: git secrets --scan
Expected: No secrets in codebase
Pass: 0 secrets found (API keys, passwords, tokens)

Command: grep -r "process.env\|process.ENV" src/ | grep -v "NODE_ENV"
Expected: Environment variables used for secrets (not hardcoded)
Pass: Secrets loaded from environment, not hardcoded

5. SQL INJECTION PREVENTION:

Command: grep -r "\.query\|\.execute" src/ | grep -v "prepared\|parameterized"
Expected: All database queries use prepared statements
Pass: No raw string concatenation in SQL queries

6. XSS PREVENTION:

Command: grep -r "innerHTML\|dangerouslySetInnerHTML" src/
Expected: No unsafe HTML injection (or sanitized when necessary)
Pass: 0 instances or all instances properly sanitized

**How to verify (Manual Review):**

- Review authentication flow (correct implementation?)
- Verify production environment uses HTTPS (check deployment config)
- Confirm sensitive data encrypted at rest (review database schema)
- Check error messages don't leak sensitive data (test error scenarios)
- Verify access control on protected resources (authorization checks present)
- Review session management (proper timeout, secure flags on cookies)

**Expected results:**

- All automated security checks: PASS
- All manual security reviews: CONFIRMED
- 0 high/critical vulnerabilities
- No secrets in codebase
- Encryption confirmed for sensitive data

**When to verify:**

- Pre-commit: Quick security checks (secrets scan, dependency audit)
- Pre-deployment: Full security review (all automated + manual checks)
- Weekly: Dependency audit (npm audit, check for new vulnerabilities)
- Quarterly: Full security audit (penetration test if applicable)

**If verification fails:**

CRITICAL FAILURE (authentication, encryption, secrets):

1. STOP deployment immediately
2. Identify specific security issue
3. Fix issue (patch, update, reconfigure)
4. Re-run full security verification
5. Do NOT deploy until all critical checks pass

HIGH PRIORITY FAILURE (input validation, XSS prevention):

1. Assess risk (exploitable? data at risk?)
2. Fix before deployment if exploitable
3. Document if acceptable risk (with justification)
4. Plan fix for next release if not immediately exploitable

**Pass criteria:**

- All automated security checks pass (0 failures)
- All manual security reviews confirm compliance
- No secrets in code or version control
- No high/critical vulnerabilities in dependencies
- Encryption confirmed for all sensitive data (PII, credentials, tokens)
- Authentication and authorization correctly implemented

When all criteria met: SECURITY VERIFIED

</verification>
```

## Template 2: Performance Verification Protocol

**Use when:** Performance constraints in your specification

```text

<verification scope="performance">

**What to verify:**

All performance MUST constraints from specification:

- API response times (p95, p99)
- Page load times
- Database query performance
- Resource utilization (CPU, memory)
- Concurrent user capacity

**How to verify (Automated):**

1. API RESPONSE TIME VERIFICATION:

Tool: Apache Bench (ab) or Artillery or k6

Command: ab -n 1000 -c 100 https://api.example.com/endpoint

Expected:

- p95 response time < 200ms (or your threshold)
- p99 response time < 500ms (or your threshold)
- 0% error rate under normal load

Example Artillery config (load-test.yml):

yaml

config:
 target: 'https://api.example.com'
 phases:
  - duration: 60
  arrivalRate: 10
  name: "Warm up"
 - duration: 300
  arrivalRate: 50
name: "Sustained load"
scenarios:
 - flow:
  - get:
   url: "/api/endpoint"

Command: artillery run load-test.yml
Expected:

• p95 < 200ms
• p99 < 500ms
• http.request_rate > 45 req/sec (90% of target)

Pass: All response time thresholds met,
no errors

2. PAGE LOAD TIME VERIFICATION: Tool: Lighthouse (Chrome DevTools)
Command: lighthouse https://example.com --throttling-method=simulate -- throttling.cpuSlowdownMultiplier=4
--output json --output-path ./report.json

Expected:

• Performance score > 85
• First Contentful Paint < 1.8s
• Largest Contentful Paint < 2.5s
• Time to Interactive < 3.8s Pass: All Core Web Vitals meet thresholds

Alternative: WebPageTest URL: https://www.webpagetest.org/ Configuration: 3G connection,

Mobile device Expected:

• Load Time < 3s
• Start Render < 2s Pass: Page loads within thresholds on 3G

3. DATABASE QUERY PERFORMANCE: Tool: Database query profiler (MySQL EXPLAIN,
Postgres EXPLAIN ANALYZE)
Command: EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com'; Expected:

• Query execution time < 100ms (or your threshold)
• Index usage confirmed (no full table scans on large tables)
Pass: All queries use indexes, execution time within threshold

Tool: Application Performance Monitoring (New Relic, DataDog)
Metric: Database query duration (p95)
Expected: p95 < 100ms for all queries
Pass: No slow queries above threshold

4. RESOURCE UTILIZATION: Tool: Load testing with monitoring
Command: artillery run load-test.yml (while monitoring resources)

Monitor: CPU usage, memory usage, disk I/O

Expected:

• CPU < 80% during sustained load
• Memory stable (no leaks, no constant growth)
• Disk I/O not saturated Pass: Resources within acceptable limits, no bottlenecks

5. CONCURRENT USER CAPACITY: Tool: Load testing with gradual ramp-up Command: k6
run stress-test.js 
Config: Ramp from 0 to 1000 virtual users over 10 minutes 

Expected:

• System handles target concurrent users (e.g., 1000)
• Response times remain within thresholds
• Error rate < 1% Pass: System stable at target concurrency

How to verify (Manual Testing):

- Test on target devices (iPhone 15, Pixel 5, etc.) 
- Test on slow connections (3G simulation in Chrome DevTools)
- Test with realistic data volumes (not empty database) 
- Test cold start performance (first request after deploy) □ Test under sustained load (not just brief tests)

Expected results:

• API response times within thresholds (p95 < 200ms, p99 < 500ms)
• Page loads within thresholds (< 3s on 3G)
• Database queries optimized (< 100ms, using indexes)
• Resource usage acceptable (CPU < 80%, memory stable)
• Concurrent capacity met (1000 users, or your target)

When to verify:

• Pre-deployment: Full performance test (all scenarios)
• Post-deployment: Smoke test (quick verification production performs)
• Daily: Automated performance monitoring (alert if degradation)
• Weekly: Review performance trends (catching gradual degradation)

If verification fails:

RESPONSE TIME FAILURE:

1. Profile slow endpoints (identify bottleneck)
2. Check for N+1 queries (database anti-pattern)
3. Add caching where appropriate (Redis, CDN)
4. Optimize database queries (add indexes, rewrite queries)
5. Consider pagination (reduce data per request)
6. Re-verify after optimization

RESOURCE SATURATION FAILURE:

1. Identify bottleneck (CPU? Memory? Disk? Network?)
2. Profile application (find hot spots in code)
3. Optimize hot paths (algorithm improvements, caching)
4. Scale resources if necessary (vertical or horizontal scaling)
5. Re-verify with optimizations

CONCURRENCY FAILURE:

1. Check for blocking operations (synchronous where should be async)
2. Review connection pooling (database, external services)
3. Implement rate limiting (prevent resource exhaustion)
4. Add circuit breakers (fail fast on dependency failures)
5. Re-verify with improvements

Pass criteria:

- All API endpoints meet response time thresholds (p95 & p99)
- All pages meet load time thresholds (Core Web Vitals)
- All database queries optimized (using indexes, <100ms)
- Resource usage acceptable under load (CPU < 80%, memory stable)
- System handles target concurrent users (with <1% errors) □ Performance monitoring in place (alerts configured)

When all criteria met: PERFORMANCE VERIFIED

</verification>
```

## Template 3: Compliance Verification Protocol

**Use when:** Regulatory constraints (HIPAA, GDPR, PCI-DSS, etc.)

```text

<verification scope="compliance">

**What to verify:**

All compliance MUST constraints from specification:

- Data privacy requirements (GDPR, CCPA)
- Healthcare compliance (HIPAA)
- Payment security (PCI-DSS)
- Accessibility (WCAG 2.1)
- Industry-specific regulations

**How to verify (GDPR Compliance):**

USER CONSENT:

- Verify consent mechanism present (opt-in, not opt-out)
- Test consent recording (who, what, when stored)
- Test consent withdrawal (users can revoke)
- Verify granular consent (separate choices for different uses)

DATA ACCESS:

- Test data export (users can download their data)
- Verify export format (machine-readable: JSON, CSV)
- Test export completeness (all user data included)
- Verify export timing (within 30 days of request, ideally immediate)

DATA DELETION:

- Test account deletion (users can delete account)
- Verify data deletion completeness (all PII removed)
- Test deletion timing (within 30 days, or log why retained)
- Verify deletion confirmation (user receives confirmation)

PRIVACY POLICY:

- Verify privacy policy present and linked (footer, signup)
- Review policy completeness (covers all data uses)
- Verify policy language (clear, not legalese)
- Test policy accessibility (easy to find, read)

DATA MINIMIZATION:

- Review data collected (only necessary data)
- Verify no excessive data collection (no "just in case")
- Test forms (no unnecessary fields marked required)

SECURITY:

- Verify encryption at rest (sensitive data encrypted)
- Verify encryption in transit (HTTPS only)
- Review access controls (who can access what data)
- Test breach notification process (plan exists, tested)

**How to verify (HIPAA Compliance):**

PHI ENCRYPTION:

Command: Check database encryption
Expected: All PHI fields encrypted (AES-256 or equivalent)
Pass: Encryption confirmed for all PHI

AUDIT LOGGING:

Command: Check audit logs
Expected: All PHI access logged (who, what, when, where)
Pass: 100% of PHI access captured in audit logs

Test: Access PHI, verify log entry created
Pass: Log entry shows user, timestamp, action, data accessed

ACCESS CONTROLS:

Test: Attempt to access PHI without authorization
Expected: Access denied, attempt logged
Pass: Unauthorized access blocked, logged

AUTO-LOGOUT:

Test: Leave application idle for [timeout period]
Expected: Automatic logout occurs
Pass: User logged out after timeout (e.g., 10 minutes)

MFA:

Test: Login with username/password only
Expected: MFA challenge required
Pass: Cannot complete login without MFA

BAA (Business Associate Agreement):

Review: All vendors handling PHI
Expected: Signed BAA with each vendor
Pass: BAAs in place and current

BREACH NOTIFICATION:

Review: Incident response plan
Expected: Clear process for breach notification (within 60 days)
Pass: Plan documented, responsible parties identified

**How to verify (PCI-DSS Compliance):**

NO CARD DATA STORAGE:

Command: grep -r "card_number\|cvv\|cvc" src/
Expected: No credit card data stored in application
Pass: 0 instances of card data storage (uses payment processor)

PAYMENT PROCESSOR:

Review: Integration with PCI-compliant processor (Stripe, Square)
Expected: All payment processing handled by processor
Pass: No card data touches our servers

TLS/HTTPS:

Command: Check SSL certificate
Expected: Valid TLS 1.2+ certificate
Pass: HTTPS enforced, valid cert, A+ rating on SSL Labs

SAQ (Self-Assessment Questionnaire):

Review: Completed SAQ-A (if using processor)
Expected: All questions answered, compliant
Pass: SAQ-A complete and compliant

**How to verify (WCAG 2.1 AA Accessibility):**

AUTOMATED TESTING:

Tool: axe DevTools or WAVE
Command: Run axe accessibility scan
Expected: 0 critical or serious violations
Pass: No automated accessibility errors

Tool: Lighthouse accessibility audit
Command: lighthouse --only-categories=accessibility
Expected: Accessibility score > 90
Pass: Score meets threshold

KEYBOARD NAVIGATION:

Test: Navigate site using only keyboard (no mouse)
Expected: All interactive elements reachable and usable
Pass: Complete workflow achievable with keyboard only

SCREEN READER:

Test: Use NVDA (Windows) or VoiceOver (Mac)
Expected: All content readable, forms usable, navigation clear
Pass: Screen reader user can complete key tasks

COLOR CONTRAST:

Tool: Color contrast checker
Expected: All text meets WCAG AA contrast ratios (4.5:1 for normal text)
Pass: All text sufficient contrast

ALT TEXT:

Review: All images have descriptive alt text
Expected: Meaningful alt text (not "image123.jpg")
Pass: All images have useful descriptions

**Expected results:**

- All regulatory requirements verified compliant
- Documentation complete (policies, procedures, evidence)
- Third-party attestations obtained (if required)
- Audit trail established (can demonstrate compliance)

**When to verify:**

- Pre-launch: Full compliance review (all requirements checked)
- Quarterly: Compliance audit (verify ongoing compliance)
- Annually: Third-party audit (if required by regulation)
- After changes: Re-verify affected compliance areas

**If verification fails:**

CRITICAL COMPLIANCE FAILURE (data breach risk, legal violation):

1. STOP - Do not launch or continue operating non-compliant
2. Identify specific compliance gap
3. Implement fix immediately (remediation plan)
4. Re-verify compliance
5. Document incident and remediation
6. Consider legal/compliance counsel

NON-CRITICAL COMPLIANCE GAP:

1. Document gap (what's missing, why, risk level)
2. Create remediation plan (timeline, responsible party)
3. Implement fix (by deadline)
4. Re-verify compliance
5. Update documentation

**Pass criteria:**

- All regulatory requirements met and documented
- Privacy mechanisms tested and working (consent, access, deletion)
- Security controls verified (encryption, access controls, audit logs)
- Accessibility tested and compliant (WCAG 2.1 AA if applicable)
- Third-party vendor compliance confirmed (BAAs, certifications)
- Audit trail established (can demonstrate compliance to auditors)
- Policies and procedures documented and accessible

When all criteria met: COMPLIANCE VERIFIED

</verification>
```

## Template 4: Code Quality Verification Protocol

**Use when:** Code quality constraints in your specification

```text

<verification scope="code-quality">

**What to verify:**

All code quality MUST constraints from specification:

- Linting standards
- Test coverage
- Code complexity
- Documentation completeness
- Code review completion

**How to verify (Automated):**

1. LINTING:

Tool: ESLint (JavaScript/TypeScript) or equivalent for your language
Command: npm run lint
Config: .eslintrc.js (strict configuration)
Expected: 0 errors, 0 warnings
Pass: Clean linting output

Alternative for Python:

Command: pylint src/ --fail-under=9.0
Expected: Score ≥ 9.0/10
Pass: High pylint score

2. TESTING:

Tool: Jest (JavaScript), pytest (Python), or equivalent
Command: npm test -- --coverage
Expected:

- All tests pass (100% success rate)
- Statement coverage > 80%
- Branch coverage > 75%
- Function coverage > 80%

Pass: All tests pass, coverage thresholds met

Command: npm test -- --watchAll=false --ci
Expected: Exits with code 0 (success)
Pass: Test suite passes in CI environment

3. CODE COMPLEXITY:

Tool: complexity-report (JavaScript) or radon (Python)
Command: npx complexity-report src/ --format json

Expected:

- Cyclomatic complexity < 10 per function
- No functions with complexity > 15
Pass: All functions within complexity threshold

Alternative for Python:

Command: radon cc src/ -a -nb
Expected: Average complexity grade A or B
Pass: No functions with grade D or F

4. TYPE CHECKING (TypeScript/Flow):

Command: npm run type-check
Expected: 0 type errors
Pass: Type system validates all code

5. DEPENDENCY AUDIT:

Command: npm audit --audit-level=moderate
Expected: 0 moderate/high/critical vulnerabilities
Pass: Dependencies are secure and up-to-date

6. CODE DUPLICATION:

Tool: jscpd (JavaScript) or similar
Command: jscpd src/
Expected: < 5% code duplication
Pass: Minimal code duplication detected

**How to verify (Manual Review):**

CODE REVIEW COMPLETED:

- Verify pull request approved by [number] reviewers
- Check review comments addressed
- Confirm no unresolved discussions
Pass: PR approved, comments resolved

DOCUMENTATION:

- README present and current (setup instructions work)
- API documentation complete (all public functions documented)
- Comments present for complex logic (why, not what)
- Architecture decisions documented (ADRs if applicable)
Pass: Documentation complete and helpful


NAMING CONVENTIONS:

- Variables descriptive (not x, tmp, data1)
- Functions verb-based (getName, not name)
- Classes noun-based (UserManager, not Manager)
- Constants uppercase (MAX_RETRIES)
Pass: Consistent, clear naming throughout

ERROR HANDLING:

- Try-catch blocks present where needed
- Errors logged with context
- User-friendly error messages (no stack traces to users)
- Errors don't leak sensitive data
Pass: Robust error handling throughout

NO DEAD CODE:

- No commented-out code blocks (use version control)
- No unused imports or variables
- No unreachable code
Pass: Clean, lean codebase

SECURITY BEST PRACTICES:

- No hardcoded secrets (use environment variables)
- Input validation present
- Output sanitization present
- No SQL injection vulnerabilities
Pass: Security best practices followed

**Expected results:**

- Linting clean (0 errors, 0 warnings)
- Tests passing (100% success, >80% coverage)
- Complexity acceptable (all functions < 10 complexity)
- Documentation complete (README, API docs, comments)
- Code review approved (by required reviewers)
- No security issues (audit clean, no vulnerabilities)

**When to verify:**

- Pre-commit: Quick checks (linting, formatting)
- Pre-push: Full test suite (all tests, coverage check)
- Pre-merge: Code review, complexity check, documentation review
- Pre-deployment: Full verification (all checks pass)

**If verification fails:**

LINTING FAILURE:

1. Run lint with auto-fix: npm run lint -- --fix
2. Manually fix remaining issues
3. Re-run verification
4. Do not commit until clean

TEST FAILURE:

1. Identify failing tests
2. Fix code or update tests (as appropriate)
3. Verify fix doesn't break other tests
4. Re-run full test suite
5. Do not merge until all tests pass

COVERAGE FAILURE:

1. Identify untested code paths
2. Add tests for critical paths first
3. Add tests for remaining paths
4. Re-run coverage report
5. Do not merge until coverage threshold met

COMPLEXITY FAILURE:

1. Identify complex functions
2. Refactor to reduce complexity:
- Extract methods (break into smaller functions)
- Simplify conditionals (reduce nesting)
- Remove duplicate logic

3. Re-run complexity check

4. Document if complexity unavoidable (algorithm inherently complex)

DOCUMENTATION FAILURE:

1. Add missing documentation
2. Update outdated documentation
3. Verify examples work (test code snippets)
4. Have someone else review for clarity
5. Do not merge without documentation

**Pass criteria:**

- Linting passes (0 errors, 0 warnings, consistent style)
- All tests pass (100% success rate, >80% coverage)
- Complexity acceptable (all functions < 10, or documented exception)
- TYpe checking passes (if applicable, 0 type errors)
- Dependencies secure (no moderate+ vulnerabilities)
- Code review approved (by required number of reviewers)
- Documentation complete (README, API docs, comments where needed)
- No dead code (clean, lean codebase)
- Security best practices followed (no hardcoded secrets, input validation)

When all criteria met: CODE QUALITY VERIFIED

</verification>
```

## Template 5: Integration Verification Protocol

**Use when:** Multiple systems must work together

```text

<verification scope="integration">

**What to verify:**

All integration MUST constraints from specification:

- API contracts (request/response formats)
- Data flow between systems
- Error handling across boundaries
- Authentication/authorization across systems
- Transaction consistency

**How to verify (Automated):**

1. API CONTRACT VERIFICATION:

Tool: Contract testing (Pact, Spring Cloud Contract)
Command: npm run test:contract
Expected:

- All API contracts validated (provider meets consumer expectations)
- Request/response schemas match
- Status codes correct
Pass: All contract tests pass

Alternative: OpenAPI validation

Command: swagger-cli validate openapi.yaml
Expected: Valid OpenAPI specification
Pass: Specification valid, no errors

2. END-TO-END FLOW VERIFICATION:

Tool: End-to-end testing (Cypress, Playwright, Selenium)
Scenario: Complete user workflow across all systems
Expected:

- User can complete workflow (e.g., signup → purchase → confirmation)
- Data propagates correctly (database, cache, external systems)
- UI reflects correct state (all system changes visible)
Pass: End-to-end workflow completes successfully

Example Cypress test:

javascript

it('completes checkout flow across all systems', () => {

cy.visit('/products');

cy.get('[data-testid=add-to-cart]').first().click();

cy.get('[data-testid=checkout]').click();

cy.get('[data-testid=payment-form]').submit();

cy.url().should('include', '/confirmation');

cy.get('[data-testid=order-number]').should('exist');

// Verify in database

cy.task('queryDatabase', 'SELECT * FROM orders WHERE user_id = 1')

.should('have.length', 1);

});

3. DATA CONSISTENCY VERIFICATION: Tool: Database comparisons, data validation scripts


Command: npm run verify:data-consistency
Check:
- Data synced across systems (no orphaned records)
- Foreign key integrity (all references valid)
- Data format consistent (dates, currencies, etc.) Pass: Data consistent across all systems

4. ERROR HANDLING VERIFICATION: Test: Simulate system failures (network timeout,service down, database error)

Expected:

- Graceful degradation (partial functionality maintained)
- Error messages helpful (what went wrong, what to do)
- No cascading failures (circuit breakers work)
-  Retry logic works (exponential backoff, max retries)
Pass: System handles failures gracefully

Example failure scenarios:

// Test payment service timeout

it('handles payment service timeout', () => {

cy.intercept('POST', '/api/payment', { forceNetworkError: true });

cy.checkout();

cy.get('[data-testid=error-message]')
.should('contain', 'Payment temporarily unavailable');

cy.get('[data-testid=retry-button]').should('exist');

});

5. AUTHENTICATION PROPAGATION: Test: Login in system A, access system B Expected:

- SSO works (single login grants access to all systems)
- Tokens propagate correctly (JWT, session)
- Authorization respected (permissions enforced across systems) Pass: User authenticated across all integrated systems

How to verify (Manual Testing):

CROSS-SYSTEM WORKFLOWS:

- Test complete user journeys spanning multiple systems
- Verify data consistency (changes in A reflect in B)
- Test real-world scenarios (not just happy path) Pass: All workflows complete successfully

ERROR SCENARIOS:

- Test with one system down (does other system handle gracefully?)
- Test with slow responses (timeouts configured correctly?)
- Test with invalid data (error handling across boundaries?) Pass: Graceful degradation, helpful errors

PERFORMANCE UNDER LOAD:

- Test with realistic load (concurrent users across systems)
- Verify no bottlenecks at integration points
- Check timeouts appropriate (not too short, not too long) Pass: Performance acceptable under load

MONITORING AND ALERTS:

- Verify integration health checks (endpoints responding)
- Test alert triggers (failures generate alerts)
- Verify logging (can trace requests across systems) Pass: Observability in place, issues detectable

Expected results:

- API contracts validated (provider meets consumer expectations)
- End-to-end workflows complete (across all systems)
- Data consistency maintained (no orphaned records, foreign key integrity)
- Error handling works (graceful degradation, helpful messages)
- Authentication/authorization propagate (SSO, permissions respected)
- Performance acceptable (no bottlenecks at integration points)

When to verify:

- Pre-deployment: Full integration test suite
- Post-deployment: Smoke tests (critical paths work in production)
- Continuous: Synthetic monitoring (automated checks every N minutes)
- After changes: Re-verify affected integration points

If verification fails:

API CONTRACT FAILURE:

1. Identify breaking change (what changed in API?)
2. Coordinate with provider team (or update consumer)
3. Version APIs (maintain backward compatibility)
4. Re-verify contracts
5. Do not deploy breaking changes without coordination

END-TO-END FLOW FAILURE:

1. Identify where flow breaks (which system, which step)
2. Check logs across systems (trace request through all systems)
3. Fix specific failure point
4. Re-verify end-to-end flow
5. Add monitoring for this flow (prevent recurrence)

DATA CONSISTENCY FAILURE:

1. Identify inconsistency (which data, which systems)
2. Determine root cause (sync failure, race condition, bug)
3. Fix synchronization or data flow
4. Clean up inconsistent data (one-time correction)
5. Re-verify consistency
6. Add data consistency checks (prevent recurrence)

ERROR HANDLING FAILURE:

1. Identify cascading failure or poor error handling
2. Implement circuit breakers (fail fast, don't cascade)
3. Improve error messages (helpful, actionable)
4. Add retry logic with backoff (for transient failures)
5. Re-verify error scenarios

Pass criteria:

- All API contracts validated (provider meets consumer expectations)
- All end-to-end workflows complete successfully
- Data consistency maintained across systems (noorphaned records)
- Error handling tested and working (graceful degradation)
- Authentication/authorization propagate correctly (SSO works)
- Performance acceptable under realistic load
- Monitoring and alerts in place (integration health observable)
- Documentation complete (integration points, data flows, error handling)

When all criteria met: INTEGRATION VERIFIED
</verification>
```

## Quick Verification Checklist

**Use this for a quick self-check before considering verification complete:**

```text

Coverage

[ ] All critical MUST constraints have verification protocols
[ ] All verification is objective (not "looks good" or "seems fine")
[ ] All verification has specific commands or steps
[ ] All verification has clear pass/fail criteria

Automation

[ ] Automated checks where possible (repeatable, fast)
[ ] Commands are specific (exact syntax, not generic "run tests")
[ ] Expected results are clear (what does success look like?)
[ ] Tools are specified (which tool, which version)

Manual Testing

[ ] Manual verification where automation insufficient
[ ] Manual steps are specific and checkable
[ ] Manual verification has objective criteria (not purely subjective)

Failure Handling

[ ] Clear guidance for what to do if verification fails
[ ] Failure scenarios categorized (critical, high, medium)
[ ] Recovery process defined (fix, re-verify, deploy)

Timing

[ ] When to verify is specified (pre-commit, pre-deploy, weekly, etc.)
[ ] Continuous monitoring defined (if applicable)
[ ] Re-verification triggers clear (after changes, failures, etc.)

Documentation

[ ] Pass criteria explicit and measurable
[ ] Commands documented with expected output
[ ] Tools and configurations specified
```

## Remember

**Good verification is:**

- **Objective:** Pass/fail is clear, not subjective
- **Automated:** Where possible, repeatable and fast
- **Comprehensive:** Covers all critical constraints
- **Actionable:** Clear what to do if verification fails
- **Timely:** Happens at the right time in the workflow

**Poor verification is:**

- **Vague:** "Verify it works" (how? what does "works" mean?)
- **Manual-only:** When automation would be better
- **Incomplete:** Missing verification for critical constraints
- **Useless on failure:** No guidance for fixing issues
- **Mis-timed:** Too late (after deployment) or too early (before code exists)

**These templates are starting points—customize for your specific needs.**

END OF APPENDIX D**

*Document Version: 1.0.0*
*Last Updated: 2026-02-18*
*Five complete verification protocol templates ready for production use*

