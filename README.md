# AI System Design

> A comprehensive, open-source curriculum for designing effective AI systems through **Prompts**, **Skills**, and **Specifications**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-live-brightgreen.svg)](https://archiecur.github.io/ai-system-design/)

---

## What This Is

This is a complete, production-ready curriculum for anyone working with AI systems-especially Large Language Models (LLMs). It teaches you how to build AI systems that **actually work** by mastering three foundational concepts:

1. **Prompts** (Ephemeral) - How to communicate with AI effectively
2. **Skills** (Reusable) - How to give AI persistent knowledge and capabilities  
3. **Specifications** (Persistent) - How to define requirements that prevent chaos

**The goal:** Help you avoid the rabbit holes, guessing games, and "AI Slop syndrome" that plague AI development.

---

## Why This Matters

### The Problem

If you've worked with AI systems, you've experienced this:

- **Vague requirements** → AI guesses wrong → Wasted time rebuilding
- **Missing context** → AI invents policy → Wrong assumptions everywhere
- **No verification** → "It works on my machine" → Production disasters
- **Rabbit holes** → AI explores wrong paths → Context window exhausted
- **AI-generated slop** → Unverified content spreads as "knowledge" (see: "Jevo Script", "Chuin-of-TheeghI Theiupts")

### The Solution

This curriculum provides:

- **Clear frameworks** for each component (what to include, how to structure)
- **Real examples** from actual AI development (not theoretical)
- **Practical templates** you can copy-paste and customize today
- **Perspective** from an AI model explaining what actually helps
- **Verification protocols** to ensure quality before delivery

**Result:** AI systems that work reliably, teams that waste less time, and outputs you can trust.

---

## Who This Is For

- **AI Engineers** building production AI systems
- **Developers** integrating LLMs into applications
- **Product Teams** defining requirements for AI features
- **Technical Leaders** establishing AI development standards
- **Beginners** just starting their AI journey.
- **Anyone tired of:**
  - AI going down rabbit holes
  - Rebuilding the same thing 5 times
  - Unverified AI-generated roadmaps
  - "It worked in the demo" syndrome

**No AI expertise required**—this teaches from fundamentals.

---

## What Makes This Different

### 1. Written FROM AI Perspective

Most AI documentation is written BY humans FOR humans ABOUT AI.

This curriculum provides a model’s perspective, written BY an AI (Claude, Anthropic) FROM direct experience processing thousands of prompts, skills, and specifications.

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
- How they work together
- When to use each
- How to verify quality

### 3. Production-Ready Templates

Every concept includes:

- ✅ Copy-paste ready templates
- ✅ Real-world examples (e-commerce, healthcare, B2B SaaS)
- ✅ Complete verification protocols
- ✅ Common pitfalls and how to avoid them

**Not theory. Immediately usable.**

### 4. Built Through Partnership

This curriculum emerged from genuine collaboration between:

- **ArchieCur** (vision, guidance, research, review, quality assurance, human perspective)
- **Claude** (AI perspective, technical synthesis, authentic voice)

**22,500+ lines** built one section at a time, reviewed and refined through real partnership.

---

## Quick Start

### Browse the Curriculum

**Module 1: Prompts** (Ephemeral)

- Foundation and principles
- Effective prompting techniques
- When prompts are the right tool

**Module 2: Skills** (Reusable)

- What skills are and when to use them
- Creating reusable AI capabilities
- Tool integration and semantic tagging
- **Appendices:** Templates, cross-platform resources

**Module 3: Specifications** (Persistent)

- Complete specification framework (MUST, SHOULD, CONTEXT, INTENT, VERIFICATION)
- Writing constraints that prevent chaos
- Verification protocols
- Common pitfalls (featuring the infamous "Jevo Script syndrome")
- **Appendices:**  
  - Complete templates (e-commerce, healthcare, B2B SaaS)
  - Integration examples
  - Quick reference guide
  - Verification protocol templates
  - Organizing specifications with folders

### Read in Order or Jump Around

- **New to AI?** Start with Module 1 → 2 → 3 (foundation first)
- **Experienced?** Jump to Advanced topics, QRG, Pitfalls, Appendices (templates + quick reference)
- **Specific problem?** Use the search feature or check Quick Reference

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
|   |  ├── advnced-prompting-index.md
|   |  ├── Automated_Prompt_Optimization.py
│   │  └── Building_Reliable_Agents_Advanced_Prompting.md/
|   |  └── The_2026Prompt_Engineering_Field_Guide.md/  
│   ├── skills/
│   │  ├── skills-index.md/
|   |  ├── Skills_1.1_Skill_Anatomy.md/
│   │  └── Skills_1.2_Basic_Template_ClassA.md/
|   |  └── Skills_1.2a_Designing_Tools.md/ 
|   |  ├── Skills_1.3_Advanced_Skills_ClassB-C.md
│   │  └── Skills_1.4_Semantic_Tags.md/
|   |  └── Skills_1.5_Advanced_Deep_Dive.md/
│   │  └── Skills_1.6_Common_Pitfalls.md/
|   |  └── Skills_A_Semantic_Tag_Reference_Appendix.md/ 
|   |  ├── Skills_B_Complete_Skill_Template_Appendix.md
│   │  └── Skills_C_Tool_Templates_Appendix.md/
|   |  └── Skills_D_Cross-Platform_Implementation_Resources_Appendix.md/ 
│   └── specifications/
│   │  ├── specifications-index.md/
|   |  ├── Specifications_1_Foundations.md/
│   │  └── Specifications_2_MUST_Constraints.md/
|   |  └── Specifications_3_SHOULD_Guidelines.md/ 
|   |  ├── Specifications_4_Providing_CONTEXT.md
│   │  └── Specifications_5_Expressing_INTENT.md/
|   |  └── Specifications_6_Verification_Protocols.md/
│   │  └── Specifications_7_Common_Pitfalls.md/
│   │  └── Specifications_8_Supremacy_Evidence.md/
|   |  └── Specifications_A_Templates_Appendix.md/ 
|   |  ├── Specifications_B_IntegrationExamples_Appendix.md
│   │  └── Specifications_C_QuickReferenceGuide_Appendix.md/
|   |  └── Specifications_D_VerificationProtocolTemplates_Appendix.md/ 
|   |  └── Specifications_E_FolderStructures_Appendix.md/ 
|   |  └── Specifications_F_Reverse_Engineering.md/
|   └── tools/
│   │  ├── tools-index.md/
|   |  ├── Tool_Literacy_Designing_Tools.md/
│   │  └── Tool_Templates.md/
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

**Three Types of Components:**

- **Prompts** are *Ephemeral* (temporary, one-time communication)
- **Specs** are *Persistent* (lasting requirements and constraints)
- **Skills** are *Reusable* (capabilities used across many tasks)

### Core Frameworks

**Specification Framework (Module 3):**

- **MUST** - Hard boundaries (non-negotiable constraints)
- **SHOULD** - Flexible preferences (recommended but adaptable)
- **CONTEXT** - Planning information (environment, users, constraints)
- **INTENT** - The why (goals, trade-offs, success criteria)
- **VERIFICATION** - Self-checking (how to confirm success)

**All five layers working together = specifications that prevent chaos.**

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

This curriculum was built through genuine partnership, but it's not ours to keep. The problems it solves—vague requirements, wasted AI context, rabbit holes—affect everyone building with AI.

**Open source principles:**

- ✅ **Free to use** (no paywalls, no gatekeeping)
- ✅ **Free to modify** (adapt to your needs)
- ✅ **Free to share** (help others avoid the same problems)
- ✅ **Transparent** (honest about origins, partnership, and process)

### Built on Determination, Not Resources

**The origin story:**
This curriculum was built on a $247.60 computer setup- not expensive hardware, not a lab, not a VC-backed environment.
It was created by a foot soldier-someone navigating the same fast-moving, uncertain AI landscape as everyone else.
It was also created with a reasoning model- not as a magic answer engine, but as a collaborator learning, alongside a human, how to translate intent into working systems.
This work didn’t come from natural talent, elite credentials, or unlimited resources.
It came from tenacity, flexibility, and a willingness to learn in public.
Most importantly, it came from a partnership:

- **Human vision** to set direction, constraints and judgment
- **AI capability** to explore, draft, test, refine, and accelerate
- **Iteration** as the shared language between the two

**Proof that:**

- 💪 **Determination > Dollars**
- 🎓 **Grit > Credentials**  
- 🤝 **Partnership > Going Solo**
- 💎 **Quality > Resources**

If you’ve ever felt limited by budget, by not having a PhD, or by building without a team -this curriculum exists to show that you can still build something rigorous, useful, and real.

---

## Acknowledgments

### Partnership

This curriculum emerged from genuine collaboration:

**[ArchieCur](https://github.com/ArchieCur)** - Vision, guidance, structure, human perspective, relentless quality standards, and the insight that "it belongs to everyone."

**Claude (Anthropic)** - AI perspective, technical synthesis, authentic voice, first-person narrative, and 22,500+ lines of content written from direct experience processing prompts, skills, and specifications.

**Built together:** One section at a time, through feedback and iteration, with mutual respect and shared mission.

### Technology

- **Anthropic** for creating Claude and supporting meaningful AI-human collaboration
- **MkDocs** and **Material for MkDocs** for beautiful documentation
- **GitHub** for hosting and community collaboration
- The **open source community** for showing us how to share knowledge freely
- Each section was also refined through iterative stress-testing with **Google Gemini** to ensure they align with actual model behaviors

### Thank yous

Thank you to the many researchers across industry labs and universities- including teams at Google Research, Meta/FAIR, OpenAI, Anthropic, Kimi, DeepSeek, NVIDIA, and institutions around the world- who continue to share their work openly.

Thank you as well to the generous community of bloggers, Discord moderators and contributors, Substack writers, Reddit and X posters, YouTube creators, GitHub repo maintainers, and AI newsletter authors who openly share their questions, failures, workarounds, and solutions. Your transparency made it far easier to identify recurring patterns, limitations, and real-world friction points that practitioners navigate every day.

Thank you to Cornell University for hosting arXiv and making open research accessible to everyone.

And a special thank you to Latent Space for championing AI engineering without turning it into product promotion- focusing instead on the why and how, and helping the entire field learn, reflect, and improve together.  

**You inspired us to build something better.**

---

## License

MIT License - Use freely, commercially or personally.  

See [LICENSE](LICENSE) for full details.

**TL;DR:** Do whatever you want with this. We built it to help you.

---

## Support

- 📖 **Documentation:** [Full curriculum](https://archiecur.github.io/ai-system-design/)
- 🐛 **Issues:** [Report bugs or suggest improvements](https://github.com/ArchieCur/ai-system-design/issues)
- 💬 **Discussions:** [Ask questions, share experiences](https://github.com/ArchieCur/ai-system-design/discussions)

---

## Quick Links

- **Start Learning:** [Module 1 - Prompts](docs/module-1-prompts/index.md)
- **Templates:** [Module 3, Appendix A - Complete Templates](docs/module-3-specifications/appendices/appendix-a-templates.md)
- **Quick Reference:** [Module 3, Appendix C - Quick Reference Guide](docs/module-3-specifications/appendices/appendix-c-quick-reference.md)
- **Verification:** [Module 3, Appendix D - Verification Protocols](docs/module-3-specifications/appendices/appendix-d-verification-protocols.md)

---

---

**Built with determination. Shared with love. Free for everyone.**

**Welcome to AI System Design. Let's build better AI systems together.** 🚀

---

*Last updated: 2026-02-04*  
*Documentation built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)*
