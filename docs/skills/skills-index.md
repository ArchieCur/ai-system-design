# Skills

## Overview

Skills are reusable AI capabilities that reduce cognitive friction by giving models persistent knowledge and tools. Rather than re-explaining the same information in every prompt, you create a skill once and the model can reference it whenever needed.

This section teaches you how to design, structure, and implement skills—from basic templates to advanced cross-platform implementations.

---

## What You'll Learn

### Fundamentals

**[Skill Anatomy](Skills_1.1_Skill_Anatomy.md)** - Understanding the components and structure of effective skills  
**[Basic Template (Class A)](Skills_1.2_Basic_Template_ClassA.md)** - Creating straightforward, foundational skills  
**[Designing Tools](Skills_1.2a_Designing_Tools.md)** - How to design tools that work within skills

### Advanced Concepts

**[Advanced Skills (Class B/C)](Skills_1.3_Advanced_Skills_ClassB-C.md)** - Complex skills for sophisticated use cases  
**[Semantic Tags](Skills_1.4_Semantic_Tags.md)** - Using semantic tagging for skill organization and discovery  
**[Advanced Deep Dive](Skills_1.5_Advanced_Deep_Dive.md)** - In-depth exploration of advanced skill techniques  
**[Common Pitfalls](Skills_1.6_Common_Pitfalls.md)** - Mistakes to avoid when building skills

### Practical Resources

**[Semantic Tag Reference](Skills_A_Semantic_Tag_Reference_Appendix.md)** - Complete reference for semantic tag usage  
**[Complete Skill Template Example](Skills_B_Complete_Skill_Template_Appendix.md)** - Full working example to learn from  
**[Fill in the Blank Tool Templates](Skills_C_Tool_Templates_Appendix.md)** - Ready-to-customize tool templates  
**[Cross-Platform Implementation](Skills_D_Cross-Platform_Implementation_Resources_Appendix.md)** - Implementing skills across different AI platforms and additional resources.

---

## Why Skills Matter

Every time you explain the same concept, provide the same context, or define the same requirements in a prompt, you're creating cognitive friction. The model must process and understand this information again.

Skills solve this by:

- **Reducing repetition** - Define once, reference many times
- **Enabling reusability** - Use the same skill across multiple tasks
- **Providing consistency** - Models apply the same knowledge reliably
- **Freeing context** - Save valuable context window space for actual work

---

## Skill Complexity Classes

Skills are classified by measurable complexity, which determines the appropriate template and architecture:

### Class A: Simple Skills

- **Scope**: Formatting rules, style guides, organizational constraints
- **Size**: < 100 lines typical
- **Tools**: Reasoning only OR 1-2 read-only tools
- **Verification**: User validates output
- **Architecture**: Single-file (SKILL.md only)
- **Examples**: "Use Oxford commas in documentation" | "Format dates as YYYY-MM-DD"

### Class B: Intermediate Skills

- **Scope**: Decision logic, conditional workflows
- **Size**: 100-500 lines typical
- **Tools**: 2-5 tools, may include state-change tools
- **Verification**: Tests or verification scripts helpful
- **Architecture**: Single-file with optional references/
- **Examples**: "Email formatting with contact directory lookup" | "Code review following team standards"

### Class C: Advanced Skills

- **Scope**: Complex multi-step workflows, verification-critical
- **Size**: 500+ lines (requires multi-file architecture)
- **Tools**: 5+ tools, complex orchestration, tool composition
- **Verification**: Automated verification essential
- **Architecture**: Multi-file (SKILL.md + references/ + scripts/)
- **Examples**: "SQL query optimization with automated verification" | "Security code review with vulnerability scanning"

**The classification determines which template to use:** Class A uses [Basic Template](Skills_1.2_Basic_Template_ClassA.md), while Classes B and C use [Advanced Skills](Skills_1.3_Advanced_Skills_ClassB-C.md) architecture.

---

## Getting Started

### New to Skills?

**Recommended path:**  
[Skill Anatomy](Skills_1.1_Skill_Anatomy.md) → [Basic Template (Class A)](Skills_1.2_Basic_Template_ClassA.md) → [Semantic Tags](Skills_1.4_Semantic_Tags.md)

Understand the structure first, then build basic skills before advancing.

### Need Something Specific?

- **Ready to build?** → [Complete Skill Template Example](Skills_B_Complete_Skill_Template_Appendix.md)
- **Need a tool?** → [Fill in the Blank Tool Templates](Skills_C_Tool_Templates_Appendix.md)
- **Cross-platform setup?** → [Cross-Platform Implementation](Skills_D_Cross-Platform_Implementation_Resources_Appendix.md)
- **Tag reference?** → [Semantic Tag Reference](Skills_A_Semantic_Tag_Reference_Appendix.md)
- **Avoiding mistakes?** → [Common Pitfalls](Skills_1.6_Common_Pitfalls.md)

---

## Key Principle

**Skills reduce cognitive friction by making knowledge reusable.** Well-designed skills help models work more efficiently and reliably by eliminating repetitive context processing.

---

*Ready to begin? Start with [Skill Anatomy](Skills_1.1_Skill_Anatomy.md) →*
