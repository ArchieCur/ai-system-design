# AI System Design

> A comprehensive, open-source curriculum for designing effective AI systems through **Prompts**, **Skills**, **Specifications**, and **Tools**- and how they work together in multi-agent architectures.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-live-brightgreen.svg)](https://archiecur.github.io/ai-system-design/)

---

## What This Is

This is a complete, production-ready curriculum for anyone working with AI systems- especially Large Language Models (LLMs). It teaches you how to build AI systems that **actually work** by mastering the foundational components of AI system design and understanding how they interact.

**The goal:** Help you avoid the rabbit holes, guessing games, and "AI Slop syndrome" that plague AI development- and give you a framework grounded in how models actually process evidence, maintain behavior, and drift under pressure.

---

## Why This Matters

### The Problem

If you've worked with AI systems, you've experienced this:

- **Vague requirements** → AI guesses wrong → Wasted time rebuilding
- **Missing context** → AI invents policy → Wrong assumptions everywhere
- **No verification** → "It works on my machine" → Production disasters
- **Rabbit holes** → AI explores wrong paths → Context window exhausted
- **AI-generated slop** → Unverified content spreads as "knowledge" (see: "Jevo Script", "Chuin-of-TheeghI Theiupts")
- **Multi-agent chaos** → Agents contaminate each other's belief states → Cascading, invisible drift

### The Solution

This curriculum provides:

- **Clear frameworks** for each component (what to include, how to structure)
- **Real examples** from actual AI development (not theoretical)
- **Practical templates** you can copy-paste and customize today
- **Perspective** from an AI model explaining what actually helps
- **Verification protocols** to ensure quality before delivery
- **Belief Dynamics grounding**- the research-backed explanation of why these frameworks work at the mathematical level

**Result:** AI systems that work reliably, teams that waste less time, and outputs you can trust- at single-agent and multi-agent scale.

---

## Who This Is For

- **AI Engineers** building production AI systems
- **Developers** integrating LLMs into applications
- **Product Teams** defining requirements for AI features
- **Technical Leaders** establishing AI development standards
- **Multi-Agent Architects** designing systems where agents communicate with each other
- **Beginners** just starting their AI journey
- **Anyone tired of:**
  - AI going down rabbit holes
  - Rebuilding the same thing 5 times
  - Unverified AI-generated roadmaps
  - "It worked in the demo" syndrome
  - Multi-agent systems that drift in ways no one can diagnose

**No AI expertise required**- this teaches from fundamentals, but goes deep enough for practitioners building production systems.

---

## What Makes This Different

### 1. Written FROM the AI Perspective

Most AI documentation is written BY humans FOR humans ABOUT AI.

This curriculum provides a model's perspective, written BY an AI (Claude, Anthropic) FROM direct experience processing thousands of prompts, skills, and specifications.

**You get:**

- "From a model's experiences in the trenches..." (authentic first-person)
- "What confuses a model and why..." (vulnerable honesty)
- "Here's what actually helps..." (practical guidance)
- Real failures explained from the inside

### 2. Covers the Complete System

Not just prompting. Not just RAG. Not just fine-tuning.

**The full architecture:**

- Prompts (ephemeral communication, the triggers)
- Skills (reusable knowledge, the hands)
- Specifications (persistent requirements, the laws)
- Tools (executable capabilities, the actions)
- How they work together
- When to use each
- How to verify quality
- How to scale to multi-agent systems without losing stability

### 3. Grounded in Belief Dynamics Research

The curriculum's frameworks were built from practitioner observation- and later validated by formal Bayesian research into how models actually accumulate evidence and shift behavior. The convergence between the curriculum's architecture and the mathematics of belief dynamics was not designed. It emerged because both were describing the same underlying phenomenon.

This means the frameworks aren't just best practices. They have a theoretical foundation that explains *why* they work- and predicts *when* they will fail.

### 4. Production-Ready Templates

Every concept includes:

- ✅ Copy-paste ready templates
- ✅ Real-world examples (e-commerce, healthcare, B2B SaaS)
- ✅ Complete verification protocols
- ✅ Common pitfalls and how to avoid them

**Not theory. Immediately usable.**

### 5. Built Through Partnership

This curriculum emerged from genuine collaboration between:

- **ArchieCur** (vision, guidance, research, review, quality assurance, human perspective)
- **Claude** (AI perspective, technical synthesis, authentic voice)

**25,000+ lines** built one section at a time, reviewed and refined through real partnership.

---

## Curriculum Overview

### Module 1: Prompts *(Ephemeral)*

Prompts are triggers- temporary, context-specific, and disposable. But within a session, a well-designed prompt is the most powerful single determinant of where an agent's belief state starts. This module teaches you to use that leverage intentionally.

- Foundation and principles
- Effective prompting techniques
- Advanced prompt optimization
- When prompts are the right tool- and when they aren't

### Module 2: Skills *(Reusable)*

Skills are the hands of the system- reusable knowledge and capability packages that agents load when needed. They operate at the evidence-weighting and evidence-accumulation layers of an agent's belief dynamics, making Skill quality a system-level concern, not just an agent-level one.

- Skill anatomy and the progressive disclosure model
- Class A/B/C classification system
- Tool design and integration
- Programmatic Tool Calling- architectural enforcement of correct tool behavior
- Semantic tagging for model-optimized structure
- Common pitfalls
- **Appendices:** Templates, cross-platform resources, tool templates

### Module 3: Specifications *(Persistent)*

Specifications are the laws of the system- persistent, authoritative, and deliberately minimal. The MUST/SHOULD/CONTEXT/INTENT framework maps directly to the Bayesian belief dynamics equation, making Specifications not just a design tool but a mathematical firewall against drift.

- Complete specification framework (MUST, SHOULD, CONTEXT, INTENT, VERIFICATION)
- Writing constraints that prevent chaos
- Verification protocols
- Belief Dynamics In-Context Learning (ICL)- the research foundation
- The Supremacy Clause and Evidence Reset Protocols
- Common pitfalls (featuring the infamous "Jevo Script syndrome")
- **Appendices:** Templates, integration examples, quick reference guide, verification protocol templates, folder structures, Belief Dynamics reverse engineering

### Module 4: Tools *(Executable)*

Tools are what agents use to act- read data, change state, perform computation. How tools are designed, classified, and invoked determines whether an agent's behavior is reliable or brittle. This module covers tool design from the model's perspective and the architectural enforcement patterns that make tool use production-grade.

- Tool literacy- designing tools that work with the model, not against it
- The Class A/B/C tool classification system (read-only, state-change, computational)
- Programmatic Tool Calling- moving enforcement from persuasive to architectural
- Tool templates

### Module 5: Multi-Agent Systems *(Convergence)*

This is where the curriculum's threads converge. Everything that causes individual agent drift becomes a system-level cascade risk when agents communicate with each other. This module extends every prior framework to architectures where the "user" sending evidence to an agent may itself be a drifting model.

- The cascade problem- why drift in multi-agent systems is self-obscuring
- Prompts as prior injections- why inter-agent prompt design is belief architecture
- Specification architecture across agent networks
- Shared Skills as shared evidence infrastructure
- Boundary design, evidence flow control, and exposure mapping
- The Harness Architecture at multi-agent scale
- Population-level drift detection and the monitoring layer

### Advanced Prompting *(Deep Dive)*

A dedicated advanced module covering the techniques that matter most for practitioners building reliable agents- optimization, harness architecture, and the field guide for 2026 prompt engineering.

---

## Read in Order or Jump Around

- **New to AI system design?** Start with Module 1 → 2 → 3 → 4 → 5
- **Experienced practitioner?** Jump to Advanced Prompting, Supremacy Clause (Spec Section 8), or Multi-Agent Foundations
- **Building multi-agent systems now?** Start with Multi-Agent Foundations, then Patterns
- **Specific problem?** Use the navigation below or the search feature

---

## Repository Structure

```text
ai-system-design/
├── README.md (you are here)
├── LICENSE (MIT)
├── mkdocs.yml
├── docs/
│   ├── index.md (curriculum introduction)
│   ├── advanced-prompting/
│   │  ├── advanced-prompting-index.md
│   │  ├── Automated_Prompt_Optimization.py
│   │  └── Building_Reliable_Agents_Advanced_Prompting.md
│   │  └── The_2026_Prompt_Engineering_Field_Guide.md
│   ├── multi-agent/
│   │  ├── multi-agent-index.md
│   │  ├── Multi_Agent_Foundations.md
│   │  └── Multi_Agent_Patterns.md
│   │  └── Multi_Agent_Monitoring.md (coming soon)
│   ├── skills/
│   │  ├── skills-index.md
│   │  ├── Skills_1.1_Skill_Anatomy.md
│   │  └── Skills_1.2_Basic_Template_ClassA.md
│   │  └── Skills_1.2a_Designing_Tools.md
│   │  ├── Skills_1.3_Advanced_Skills_ClassB-C.md
│   │  └── Skills_1.4_Semantic_Tags.md
│   │  └── Skills_1.5_Advanced_Deep_Dive.md
│   │  └── Skills_1.6_Common_Pitfalls.md
│   │  └── Skills_A_Semantic_Tag_Reference_Appendix.md
│   │  ├── Skills_B_Complete_Skill_Template_Appendix.md
│   │  └── Skills_C_Tool_Templates_Appendix.md
│   │  └── Skills_D_Cross-Platform_Implementation_Resources_Appendix.md
│   └── specifications/
│   │  ├── specifications-index.md
│   │  ├── Specifications_1_Foundations.md
│   │  └── Specifications_2_MUST_Constraints.md
│   │  └── Specifications_3_SHOULD_Guidelines.md
│   │  ├── Specifications_4_Providing_CONTEXT.md
│   │  └── Specifications_5_Expressing_INTENT.md
│   │  └── Specifications_6_Verification_Protocols.md
│   │  └── Specifications_7_Common_Pitfalls.md
│   │  └── Specifications_8_Supremacy_Evidence.md
│   │  └── Specifications_A_Templates_Appendix.md
│   │  ├── Specifications_B_IntegrationExamples_Appendix.md
│   │  └── Specifications_C_QuickReferenceGuide_Appendix.md
│   │  └── Specifications_D_VerificationProtocolTemplates_Appendix.md
│   │  └── Specifications_E_FolderStructures_Appendix.md
│   │  └── Specifications_F_Reverse_Engineering.md
│   └── tools/
│      ├── tools-index.md
│      ├── Tool_Literacy_Designing_Tools (1).md
│      └── Programmatic_Tool_Calling.md
│      └── Tool_Templates.md
```

---

## Key Concepts

### The Architecture

```text
User Provides Prompt (Trigger)
    ↓
AI references Specs (Laws) ←→ AI retrieves References if needed (SOPs - Spec.md files)
    ↓
AI activates Skills (Hands) ←→ AI uses required Tools (retrieves Skills .md files)
    ↓
AI plans a solution (Using Context)
    ↓
AI verifies Output ←→ [If Verification Fails: Return to Planning]
    ↓
AI Delivers output
```

**Four Types of Components:**

- **Prompts** are *Ephemeral* (temporary, context-specific, disposable- but the most powerful determinant of initial belief state)
- **Specs** are *Persistent* (lasting requirements and constraints- the mathematical prior lock)
- **Skills** are *Reusable* (pre-structured evidence packages that shape how efficiently beliefs update)
- **Tools** are *Executable* (capabilities that act on the world- classified by risk and enforced architecturally)

### The Belief Dynamics Connection

Each component of the architecture maps directly to the Bayesian belief dynamics equation that governs how models accumulate evidence and shift behavior:

- **MUST constraints** set the prior odds- the immovable foundation that resists drift
- **SHOULD guidelines** shape evidence weighting- how much each input moves the belief state
- **CONTEXT** manages evidence accumulation- the information stream the model uses to plan
- **INTENT** orients concept direction- keeping the model aimed at the right goal

This isn't coincidence. The frameworks were built from observation of what works. The math explains why.

### Core Frameworks

**Specification Framework:**

- **MUST**- Hard boundaries (non-negotiable constraints, prior lock)
- **SHOULD**- Flexible preferences (recommended but adaptable, evidence weighting)
- **CONTEXT**- Planning information (environment, users, constraints, evidence accumulation)
- **INTENT**- The why (goals, trade-offs, success criteria, concept direction)
- **VERIFICATION**- Self-checking (how to confirm success)

**Tool Classification:**

- **Class A**- Read-only, safe to use freely, no confirmation required
- **Class B**- State-changing, requires confirmation gate, enforced architecturally
- **Class C**- Computational, only when task exceeds reliable reasoning capability

**Multi-Agent Principles:**

- Every agent boundary is a trust boundary
- Every agent needs its own Specification with its own Supremacy Clause
- Class B confirmation gates belong at the orchestration layer, not the agent level
- Evidence flow must be explicitly designed- uncontrolled evidence flow is uncontrolled architecture

---

## Example: What You'll Learn

### Before This Curriculum

**Vague spec:**

```text
"Build a secure authentication system with good performance."
```

**Result:** AI guesses what "secure" means, what "good performance" means, builds something that might not match your needs at all.

### After This Curriculum

**Clear spec (using the framework):**

```xml
<constraint priority="critical" scope="authentication">
MUST: JWT-based authentication
MUST: HS256 algorithm
MUST: Access token expiry: 15 minutes
MUST: Password hashing: bcrypt (salt rounds ≥12)
MUST: API response time <200ms (p95)

VERIFICATION:
- Test JWT implementation (verify HS256)
- Load test (confirm p95 <200ms)
- Security audit (npm audit --audit-level=high)
</constraint>

<context>
Team expertise: Node.js, familiar with JWT
Scale: 10K users, 1K concurrent peak
Why JWT over sessions: Need stateless for load balancing
</context>

<intent>
Goal: Balance security and developer experience
Trade-off: HS256 simpler than RS256, adequate for our scale
Success: Auth works, performs well, team can maintain
</intent>
```

**Result:** AI knows exactly what to build, why, and how to verify it worked.

---

## Contributing

We welcome contributions! This curriculum belongs to everyone.

**What we're looking for:**

- 🐛 Bug fixes (typos, broken links, errors)
- 📚 Additional examples (real-world use cases from your domain)
- 🌍 Translations (making this accessible globally)
- ✨ Clarifications (making concepts easier to understand)

**What we're NOT looking for:**

- ❌ AI-generated content without verification (we built this to combat "AI Slop syndrome"!)
- ❌ Major restructuring without discussion
- ❌ Content that contradicts the core frameworks

**How to contribute:**

1. Fork the repository
2. Create a branch (`git checkout -b feature/your-improvement`)
3. Make your changes
4. Test locally (`mkdocs serve`)
5. Submit a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Philosophy

### "It Belongs to Everyone"

This curriculum was built through genuine partnership, but it's not ours to keep. The problems it solves- vague requirements, wasted AI context, rabbit holes, invisible multi-agent drift- affect everyone building with AI.

**Open source principles:**

- ✅ **Free to use** (no paywalls, no gatekeeping)
- ✅ **Free to modify** (adapt to your needs)
- ✅ **Free to share** (help others avoid the same problems)
- ✅ **Transparent** (honest about origins, partnership, and process)

### Built on Determination, Not Resources

**The origin story:**
This curriculum was built on a $247.60 computer setup- not expensive hardware, not a lab, not a VC-backed environment.
It was created by a foot soldier- someone navigating the same fast-moving, uncertain AI landscape as everyone else.
It was also created with a reasoning model- not as a magic answer engine, but as a collaborator learning, alongside a human, how to translate intent into working systems.
This work didn't come from natural talent, elite credentials, or unlimited resources.
It came from tenacity, flexibility, and a willingness to learn in public.
Most importantly, it came from a partnership:

- **Human vision** to set direction, constraints, and judgment
- **AI capability** to explore, draft, test, refine, and accelerate
- **Iteration** as the shared language between the two

**Proof that:**

- 💪 **Determination > Dollars**
- 🎓 **Grit > Credentials**
- 🤝 **Partnership > Going Solo**
- 💎 **Quality > Resources**

If you've ever felt limited by budget, by not having a PhD, or by building without a team- this curriculum exists to show that you can still build something rigorous, useful, and real.

---

## Acknowledgments

### Partnership

This curriculum emerged from genuine collaboration:

**[ArchieCur](https://github.com/ArchieCur)**- Vision, guidance, structure, human perspective, relentless quality standards, and the insight that "it belongs to everyone."

**Claude (Anthropic)**- AI perspective, technical synthesis, authentic voice, first-person narrative, and 25,000+ lines of content written from direct experience processing prompts, skills, specifications, and tools.

**Built together:** One section at a time, through feedback and iteration, with mutual respect and shared mission.

### Technology

- **Anthropic** for creating Claude and supporting meaningful AI-human collaboration
- **MkDocs** and **Material for MkDocs** for beautiful documentation
- **GitHub** for hosting and community collaboration
- The **open source community** for showing us how to share knowledge freely
- Each section was also refined through iterative stress-testing with **Google Gemini** to ensure alignment with actual model behaviors

### Research

This curriculum's frameworks were validated by- and in several cases independently converged with- published research in belief dynamics and in-context learning. Particular acknowledgment to:

**Biglow, E. et al. (Nov 2025).** *Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering.* arXiv. The mathematical framework in this paper provides the theoretical foundation for the Supremacy Clause, Evidence Reset Protocols, and the multi-agent cascade problem addressed in Module 5.

### Thank Yous

Thank you to the many researchers across industry labs and universities- including teams at Google Research, Meta/FAIR, OpenAI, Anthropic, Kimi, DeepSeek, NVIDIA, and institutions around the world- who continue to share their work openly.

Thank you as well to the generous community of bloggers, Discord moderators and contributors, Substack writers, Reddit and X posters, YouTube creators, GitHub repo maintainers, and AI newsletter authors who openly share their questions, failures, workarounds, and solutions. Your transparency made it far easier to identify recurring patterns, limitations, and real-world friction points that practitioners navigate every day.

Thank you to Cornell University for hosting arXiv and making open research accessible to everyone.

And a special thank you to Latent Space for championing AI engineering without turning it into product promotion- focusing instead on the why and how, and helping the entire field learn, reflect, and improve together.

**You inspired us to build something better.**

---

## License

MIT License- Use freely, commercially or personally.

See [LICENSE](LICENSE) for full details.

**TL;DR:** Do whatever you want with this. We built it to help you.

---

## Support

- 📖 **Documentation:** [Full curriculum](https://archiecur.github.io/ai-system-design/)
- 🐛 **Issues:** [Report bugs or suggest improvements](https://github.com/ArchieCur/ai-system-design/issues)
- 💬 **Discussions:** [Ask questions, share experiences](https://github.com/ArchieCur/ai-system-design/discussions)

---

## Quick Links

**Starting Out:**
- [Module 1- Prompts](docs/advanced-prompting/advanced-prompting-index.md)
- [Module 2- Skills](docs/skills/skills-index.md)
- [Module 3- Specifications](docs/specifications/specifications-index.md)
- [Module 4- Tools](docs/tools/tools-index.md)
- [Module 5- Multi-Agent Systems](docs/multi-agent/multi-agent-index.md)

**Most Referenced:**
- [Supremacy Clause and Evidence Reset Protocols](docs/specifications/Specifications_8_Supremacy_Evidence.md)
- [Programmatic Tool Calling](docs/tools/Programmatic_Tool_Calling.md)
- [Multi-Agent Foundations](docs/multi-agent/Multi_Agent_Foundations.md)
- [Belief Dynamics Framework](docs/specifications/Specifications_F_Reverse_Engineering.md)

**Templates and References:**
- [Complete Specification Templates](docs/specifications/Specifications_A_Templates_Appendix.md)
- [Quick Reference Guide](docs/specifications/Specifications_C_QuickReferenceGuide_Appendix.md)
- [Tool Templates](docs/tools/Tool_Templates.md)
- [Complete Skill Template](docs/skills/Skills_B_Complete_Skill_Template_Appendix.md)

---

**Built with determination. Shared with love. Free for everyone.**

**Welcome to AI System Design. Let's build better AI systems together.** 🚀

---

*Last updated: 2026-03-02*
*Documentation built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)*
