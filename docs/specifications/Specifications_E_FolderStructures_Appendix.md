# Appendix E: Organizing Specifications with Folders

**For:** Projects with complex policies, regulations, or extensive context

**When to use:** Multi-file organization keeps SPEC.md focused and maintainable

## When to Use Spec Folders

Use folders when you have:

- Multiple compliance requirements (GDPR, SOC2, HIPAA, PCI-DSS)
- Detailed policies (security, data retention, privacy)
- Extensive context (brand guidelines, business documentation)
- Shared specifications across teams (reference common policies)

Keep it simple when you have:

- Single project with straightforward requirements
- All constraints fit comfortably in SPEC.md
- No compliance or policy documents to reference
Rule of thumb: If SPEC.md exceeds 500 lines, consider splitting into folders.

## Basic Folder Structure

```text

/project-specs/
├── SPEC.md # Main specification (MUST, SHOULD, CONTEXT, INTENT)
├── policies/ # Internal policies
│ ├── security-policy.md
│ ├── data-retention-policy.md
│ └── access-control-policy.md
├── regulations/ # External compliance requirements
│ ├── GDPR-requirements.md
│ ├── SOC2-controls.md
│ └── PCI-DSS-requirements.md
└── context/ # Background information
├── brand-guidelines.md
├── business-priorities.md
└── technical-environment.md
```

## Example: E-commerce Platform

SPEC.md (Main Specification)
Reference external documents instead of duplicating content

```text

<constraint priority="critical" scope="security">
MUST: Follow security policy (see policies/security-policy.md)
MUST: Comply with PCI-DSS (see regulations/PCI-DSS-requirements.md)
MUST: Implement access controls (see policies/access-control-policy.md)
</constraint>

<constraint priority="critical" scope="data-privacy">
MUST: Comply with GDPR (see regulations/GDPR-requirements.md)
MUST: Follow data retention policy (see policies/data-retention-policy.md)
</constraint>

<guideline priority="high">
SHOULD: Follow brand guidelines (see context/brand-guidelines.md)
SHOULD: Align with business priorities (see context/business-priorities.md)
</guideline>

<context>
**For detailed context, see:**
- Technical environment: context/technical-environment.md
- User research: context/user-personas.md
- Competitive analysis: context/market-position.md

</context>
policies/security-policy.md
- Security Policy

Password Requirements
- Minimum 12 characters
- Must include: 1 uppercase, 1 lowercase, 1 number, 1 special character
- No password reuse (last 5 passwords)
- Bcrypt hashing (salt rounds = 12)

Authentication
- JWT tokens (HS256 algorithm)
- Access token expiry: 15 minutes
- Refresh token expiry: 7 days
- httpOnly cookies for token storage

Encryption
- All PII encrypted at rest (AES-256)
- TLS 1.2+ for data in transit
- Database encryption enabled

Access Control
- Role-based access control (RBAC)
- Principle of least privilege
- Multi-factor authentication for admin access

regulations/GDPR-requirements.md
GDPR Compliance Requirements

User Consent
- Explicit opt-in for data collection
- Clear purpose explanation
- Easy withdrawal of consent

Right to Access
- Users can request all data we hold
- Provide data in machine-readable format (JSON)
- Response within 30 days

Right to Deletion
- Users can request data deletion
- Complete deletion within 30 days
- Maintain audit log (anonymized)

Data Portability
- Export user data in common format
- Include all personal data
- Transferable to other services

Breach Notification
- Notify users within 72 hours
- Notify supervisory authority
- Document all breaches

context/brand-guidelines.md
Brand Guidelines

Colors
- Primary: #2563EB (blue)
- Secondary: #10B981 (green)
- Accent: #F59E0B (amber)
- Error: #EF4444 (red)

Typography
- Headings: Inter, sans-serif
- Body: Inter, sans-serif
- Code: JetBrains Mono, monospace

Tone of Voice
- Friendly but professional
- Clear and concise
- Avoid jargon with non-technical users
- Positive and solution-focused

UI Patterns
- Primary buttons: Blue with white text
- Secondary buttons: White with blue border
- Cards: White background, subtle shadow
- Forms: Inline validation, clear error messages

Referencing from SPEC.md

 Keep references concise in SPEC.md:

Don't Duplicate:
<constraint>
MUST: Passwords minimum 12 characters with 1 uppercase, 1 lowercase,
1 number, 1 special character, no reuse of last 5 passwords,
bcrypt hashing with salt rounds = 12...
[Repeating entire security policy in SPEC.md]
</constraint>

Reference Instead:

<constraint priority="critical">
MUST: Follow security policy (see policies/security-policy.md)

Key requirements enforced:
- Password complexity and hashing
- Authentication token management
- Encryption standards
- Access controls

Refer to policy document for complete details.
</constraint>
```

## Spec Folders vs. Skills Folders

Important distinction:

## Skills Folders (Detailed Procedures)

```text

/mnt/skills/docx/
├── SKILL.md # HOW to create Word documents
├── examples/ # Step-by-step examples
├── templates/ # Reusable templates
└── troubleshooting/ # Common issues and fixes

Purpose: Teach HOW to do things (SOPs, procedures)
Scope: Reusable across many projects
Depth: Comprehensive, detailed
```

### Spec Folders (Reference Documents)

```text

/project-specs/
├── SPEC.md # WHAT constraints and context apply
├── policies/ # WHAT policies govern this project
├── regulations/ # WHAT regulations must be followed
└── context/ # WHAT background informs decisions

Purpose: Define WHAT rules apply (policies, constraints)
Scope: Specific to this project
Depth: Brief, referenced from SPEC.md
```

### Key difference between Spec and Skills folders

• Skills = HOW (procedures, methods, SOPs)
• Specs = WHAT (rules, policies, context)

## Best Practices

1- **Keep SPEC.md as Hub**
SPEC.md should be the single entry point:
- Contains all MUST/SHOULD constraints
- References external documents
- Provides high-level CONTEXT and INTENT
**External files provide details, but SPEC.md is authoritative.**

2- **Organize by Concern**
- policies/ # Internal rules you control
- regulations/ # External compliance you must follow
- context/ # Background information that informs decisions
**This separation makes maintenance easier.**

3- **Keep Reference Files Updated**
When policies change:
- Update the specific file (e.g., security-policy.md)
- SPEC.md references remain valid
**No need to regenerate entire specification**

4- **Don't Over-Organize**

**Good (simple, clear):**

```text

/specs/
├── SPEC.md
├── policies/security-policy.md
└── regulations/GDPR-requirements.md
```
**Bad (over-engineered):**

```text

/specs/
├── SPEC.md
├── policies/
│ ├── security/
│ │ ├── authentication/
│ │ │ ├── passwords/
│ │ │ │ ├── requirements.md
│ │ │ │ ├── hashing.md
│ │ │ │ └── storage.md
[... 50 more nested folders ...]
```
**Keep it simple. 2-3 levels maximum.**

## When to Use Single SPEC.md vs. Adding Spec Folders

**Use Single SPEC.md When:**

- Project is straightforward (< 500 lines total)
- No external compliance requirements
- No shared policies across teams
- Quick iteration and changes expected

**Use Folders When:**

- Multiple compliance requirements (GDPR + SOC2 + PCI-DSS)
- Detailed policies to reference (security, privacy, data retention)
- Shared specs across projects (company-wide policies)
- SPEC.md would exceed 500 lines

## Template: Minimal Spec Folder

For projects that need folders but want to keep it simple:

```text

/project-specs/
├── SPEC.md
│ # Main specification with MUST, SHOULD, CONTEXT, INTENT
│ # References external documents where needed
│
├── policies/
│ └── security-policy.md
│ # Password, auth, encryption, access control
│
├── regulations/
│ └── compliance-requirements.md
│ # GDPR, SOC2, or other applicable regulations
│
└── context/
└── project-context.md
| #Technical environment, users, business priorities
```
**Start here. Add more files only if needed.**

## Key Takeaways

**Spec folders are:**

- References (not procedures)
- Project-specific (not reusable SOPs)
- Simple organization (policies, regulations, context)
- Complementary to SPEC.md (not replacements)

**Keep it simple:**

- Reference from SPEC.md rather than duplicate
- 2-3 levels deep maximum
- Add folders only when SPEC.md gets unwieldy (>500 lines)
- Update referenced files independently

**Unlike Skills folders (which teach HOW), Spec folders define WHAT (policies, compliance, context).**

END OF APPENDIX E

Document Version: 1.0.0

Last Updated: 2026-02-28

Organizing specifications with simple folder structures for complex projects

