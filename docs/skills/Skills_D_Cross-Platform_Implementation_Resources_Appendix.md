# Skills_D_Cross-Platform_Implementation_Resources_Appendix

*Converted from PDF: Skills_D_Cross-Platform_Implementation_Resources_Appendix.pdf*



---
**Page 1**

Appendix D: Cross-Platform Implementation & Resources

Purpose: Brief guide to Skills across AI platforms with links to official resources
Note: Platforms evolve rapidly—always check official documentation for latest implementation
details

Introduction

Skills (also called "Instructions," "Agents," or "System Instructions" depending on platform) are
a universal concept in AI system design, but each platform implements them differently.


### This appendix provides:


• Universal principles that apply across all platforms

• Platform-specific implementation notes (brief)

• Terminology landscape (what each vendor calls Skills)
• Conversion guidance (adapting skills between platforms)

• Anthropic resources and repositories

Important: AI platforms are evolving rapidly. The popularity and ease-of-use of Anthropic's Skills
implementation is likely to influence how other platforms approach this concept. Always consult
official documentation for the latest implementation details.

Universal Principles


### Regardless of platform, effective agent knowledge documents share these characteristics:



## 1. Progressive Disclosure

Principle: Load only what's needed, when it's needed.


### Why it matters:


• Reduces cognitive load on the model

• Keeps context focused and relevant

• Enables larger knowledge bases without overload
• Improves performance by avoiding irrelevant information


---
**Page 2**

How Anthropic implements: Metadata-driven activation (skills load based on name and
description matching user intent)

How others might implement: Varies by platform (some load all instructions at startup, others
support dynamic loading)


## 2. Metadata-Driven Discovery


Principle: Name and description enable automatic activation.

### Why it matters:


• Models can discover and activate appropriate skills

• No manual switching required

• Enables skill composition (multiple skills active)

• Scales to large skill libraries

### Universal pattern:


name: skill-identifier

description: What this does and when to use it. Keywords: relevant, terms.

All platforms benefit from clear naming and descriptions, even if they don't use YAML
frontmatter.


## 3. Structured Decision Criteria

Principle: Use IF-THEN patterns for decision logic.


### Why it matters:


• Clear, parseable logic

• Models understand conditional execution

• Reduces ambiguity
• Enables verification


### Universal pattern:



### IF [observable condition]:


→ [Specific action]


---
**Page 3**

→ [Expected outcome]

This works across Anthropic, OpenAI, Google, and open-source implementations.


## 4. Cognitive Load Management


Principle: Don't overload the model's context window.


### Why it matters:


• Too much information degrades performance
• Context limits are real constraints

• Focus improves quality


### Best practices:


• Main file: 400-500 lines max (Anthropic SKILL.md)

• Extended content in separate reference files
• Progressive disclosure of details

• Clear unload conditions to prevent context bleed

Platform-Specific Implementations
Anthropic Claude (Skills)

Implementation approach: Progressive disclosure with metadata-driven activation

Claude.ai (Web/Mobile/Desktop)


### How to use:



## 1. Navigate to Settings → Capabilities → Skills


## 2. Upload skill as zip file (directory containing SKILL.md)



## 3. Skills activate automatically based on user intent



### File structure:


skill-name/
├── SKILL.md # Required: YAML frontmatter + Markdown

└── references/ # Optional: Supporting files

├── EXAMPLES.md


---
**Page 4**

└── GUIDE.md

Documentation: https://support.claude.com/en/articles/12580051

Claude API

How to use: Pass skills via the skills parameter in API requests.


### Example:

import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
model="claude-sonnet-4-5-20250929",

max_tokens=1024,

skills=[

{

"type": "text",
"text": "---\nname: example-skill\ndescription: Example\n---\n\n# Content"

}

],

messages=[

{"role": "user", "content": "Your prompt"}
]

)

Documentation: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

Claude Code

How to use: Install skills from the marketplace or create custom skills.

Marketplace: Browse and install community-created skills


---
**Page 5**

Custom skills: Place in ~/.claude/skills/ directory

Documentation: See Claude Code marketplace in terminal

Claude Desktop (Cowork)

How to use: Skills work with Cowork's autonomous task execution.

Note: Cowork is in research preview (as of January 2026). Skills integration capabilities are
evolving.

Status: Check official documentation for latest Cowork + Skills support

Documentation: https://support.claude.com (search "Cowork")

OpenAI / Microsoft (Instructions/Agents)

Implementation approach: Static instructions loaded at startup

File Pattern


### Typical files:

• AGENTS.md (at repository root)

• instructions.md (project-specific)

• .github/agents.md (GitHub-specific)

Format: Plain Markdown (no YAML frontmatter required)

### Characteristics:


• All instructions loaded when agent starts

• No progressive disclosure (everything in context)

• No metadata-driven activation

• Suitable for codebase-specific rules and conventions

### Example structure:


# Coding Standards

## Language Guidelines

[All coding rules for this repository]


---
**Page 6**

## Architecture Patterns
[All architectural decisions]

## Security Requirements

[All security policies]
When to use: Best for project-specific coding standards, repository conventions, and codebase

rules.

Documentation: Check OpenAI/Microsoft official documentation for latest patterns

Google (System Instructions)

Implementation approach: Manifest-based with dynamic loading

Configuration Pattern

File: No standard filename (configured in Vertex AI or AI Studio)

### Format Options:


• JSON manifest (structured configuration)

• Plain text (simple instructions)

• Dynamic registration (API-based)

### Characteristics:


• Registered in Google Cloud platform

• Can support progressive disclosure (platform-dependent)

• Context-based activation rules

• Integration with Vertex AI ecosystem
When to use: For Google Cloud integrated workflows, Vertex AI agents, or AI Studio projects.

Documentation: https://cloud.google.com/vertex-ai/docs (search "system instructions")

Open Source Implementations

Implementation approach: Varies widely (no standard)


---
**Page 7**

Common Patterns


### Files used:

• README.md (instructions in project readme)

• INSTRUCTIONS.md (dedicated instruction file)

• .ai/ directory (custom conventions)

• Custom filenames (project-specific)

### Formats:


• Markdown (most common)

• Plain text


## • JSON/YAML


• Platform-specific formats

### Characteristics:


• No standard (each framework different)

• Often simpler than enterprise platforms

• Community-driven conventions

• Evolving rapidly
When to use: For open-source AI frameworks, custom implementations, or experimental

setups.
Documentation: Check specific framework documentation (LangChain, AutoGPT, etc.)

The Terminology Landscape


### Different vendors use different terms for the same concept:


Vendor Term File Name Key Characteristics

Progressive disclosure,
Anthropic Skills SKILL.md metadata-driven activation,

YAML frontmatter

Instructions or AGENTS.md, Static file at repo root, all loaded
OpenAI/Microsoft
Agents instructions.md at startup


---
**Page 8**

Vendor Term File Name Key Characteristics

System Manifest-based, registered in
Google No standard
Instructions platform, dynamic activation
README.md,
No standard, community
Open Source Varies INSTRUCTIONS.md,
conventions
custom
Universal concept: Providing specialized knowledge to AI agents

Platform-specific: How that knowledge is structured, loaded, and activated

Converting Skills Between Platforms

From Anthropic SKILL.md → OpenAI AGENTS.md


### Steps:



## 1. Remove YAML frontmatter (OpenAI doesn't use it)


## 2. Keep Markdown body (instructions remain the same)



## 3. Flatten structure (no progressive disclosure—everything loads at once)



## 4. Add to repository root as AGENTS.md



### Example:



### Anthropic SKILL.md:

---

name: coding-standards

description: Enforce coding standards for this repository

---

# Coding Standards

<decision_criteria>


### IF code violates standard X:

→ Request correction


---
**Page 9**

</decision_criteria>


### OpenAI AGENTS.md:

# Coding Standards

## When to Apply

Apply coding standards when reviewing or writing code.

## Decision Logic


### IF code violates standard X:


→ Request correction

[Rest of instructions...]

Trade-off: Lose progressive disclosure (all instructions always in context), but gain

OpenAI/Microsoft platform compatibility.

From OpenAI AGENTS.md → Anthropic SKILL.md


### Steps:



### 1. Add YAML frontmatter:

2. ---name: repository-coding-standardsdescription: > Coding standards and conventions

for this repository. Use when reviewing code or writing new code. Keywords: code
review, standards, conventions, style guide.---


## 3. Keep Markdown body unchanged



### 4. Add semantic tags (optional but recommended):


o Wrap decision logic in <decision_criteria>
o Add <critical> for must-follow rules

o Include <unload_condition> for when to stop


## 5. Place in skills directory (or zip for upload)


Benefit: Gain progressive disclosure (only loads when needed), reducing context overhead.


---
**Page 10**

From Anthropic SKILL.md → Google System Instructions

### Steps:



## 1. Extract core instructions (remove Anthropic-specific metadata if needed)



### 2. Convert to required format:


o JSON manifest (if using structured config)

o Plain text (if using simple instructions)

### 3. Register in Vertex AI or AI Studio:


o Define activation triggers

o Configure context rules


## 4. Test activation in Google platform

Note: Specific conversion depends on Google's current implementation. Check Vertex AI

documentation.

Universal Conversion Tips


### When converting between platforms:



## 1. Preserve core logic: Decision criteria, patterns, examples translate across platforms



## 2. Adapt metadata: Each platform has different frontmatter/config requirements


## 3. Consider activation: Some platforms auto-activate (Anthropic), others load all at once


(OpenAI)


## 4. Test thoroughly: Platform differences can affect behavior


## 5. Document origin: Note if skill was converted (aids future updates)


Best practice: Maintain skills in platform-agnostic format (Markdown body), then adapt

metadata/structure for each platform.

Anthropic Resources

Official Repositories


---
**Page 11**


## 1. Anthropic Skills Repository


URL: https://github.com/anthropics/skills

### What it contains:


• Anthropic's official implementation of Skills for Claude

• Example skills demonstrating best practices

• Reference implementations

### When to use:


• Study well-crafted skill examples

• Understand Anthropic's approach to skill design

• Find inspiration for your own skills

Note: For information about the Agent Skills open standard, see agentskills.io


## 2. Skill Creator Skill


URL: https://github.com/anthropics/skills/tree/main/skills/skill-creator


### What it contains:


• A skill that helps create other skills!
• Automated best practice checking

• Guidance on effective skill design


### When to use:


• Creating a new skill from scratch

• Updating an existing skill
• Want automated validation of skill quality

• Need guidance on skill structure

How it works: Activate the skill-creator skill, describe what you want your skill to do, and it
guides you through creation with best practices built in.

Official Documentation


---
**Page 12**


## 1. Claude Support: Skills Guide


URL: https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-
using-skills


### What it covers:


• How to create skills
• How to upload skills to Claude.ai

• Best practices for skill design

• Troubleshooting common issues

Audience: All users (beginner to advanced)


## 2. Anthropic Blog: Equipping Agents for the Real World


URL: https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills


### What it covers:


• The vision behind Agent Skills
• Why skills matter for AI agents

• Real-world use cases

• The open standard approach

Audience: Anyone interested in the "why" behind Skills


## 3. Claude API Documentation: Agent Skills


URL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview


### What it covers:


• Using skills via the Claude API

• Skills parameter format
• API examples with skills

• Integration patterns

Audience: Developers integrating Claude API


---
**Page 13**

Agent Skills Open Standard

Specification Website
URL: https://agentskills.io/specification


### What it contains:


• Complete open standard specification

• Platform-agnostic skill format

• Technical specification details
• Governance and contribution guidelines


### Why it matters:


• Skills are not proprietary to Anthropic

• Other platforms can adopt the standard

• Enables skill portability across AI platforms
• Community-driven evolution

When to reference: For precise technical details about the skill specification format.

Platform Evolution Note
Important reminder: AI platforms are evolving rapidly, especially around agent capabilities and

knowledge integration.

### What this means for Skills:


Anthropic's Influence

The ease-of-use and effectiveness of Anthropic's Skills implementation is likely to influence how

### other platforms approach this concept. Features like:


• Progressive disclosure

• Metadata-driven activation

• Structured semantic tags

• User Intent Change detection
...may appear in other platforms' implementations over time.

Checking for Updates


---
**Page 14**


### Always consult official documentation:


• Anthropic: https://docs.claude.com and https://support.claude.com
• OpenAI: https://platform.openai.com/docs

• Google: https://cloud.google.com/vertex-ai/docs

• Open Source: Check specific framework documentation


### What to watch for:


• New skill formats or standards
• Changes to activation mechanisms

• Enhanced metadata fields

• Progressive disclosure support in other platforms

• Interoperability improvements
This Curriculum's Approach


### This curriculum teaches Anthropic's implementation in depth because:



## 1. It's the most mature and well-documented



## 2. It's based on an open standard (agentskills.io)



## 3. The principles transfer to other platforms


## 4. It represents best practices for agent knowledge design


Adapting to other platforms: Use the principles and patterns taught here, then adjust metadata
and structure to match your target platform's requirements.

Quick Reference: When to Use Which Platform

Scenario Recommended Platform Why

General-purpose AI assistant Progressive disclosure, mature
Anthropic Claude (Skills)
work implementation
Simple file at repo root, loads with
Codebase-specific rules OpenAI (AGENTS.md)
context

Google Cloud integrated Google (System
Native Vertex AI integration
workflows Instructions)


---
**Page 15**

Scenario Recommended Platform Why

Custom/experimental setups Open Source Flexibility, community innovation

Agent Skills Standard
Maximum portability Platform-agnostic format
(agentskills.io)

Summary


### Key takeaways:



## 1. Skills are universal: The concept applies across platforms, implementations vary



## 2. Anthropic leads: Most mature implementation with open standard



## 3. Principles transfer: Progressive disclosure, metadata-driven activation, structured logic

work everywhere


## 4. Platforms evolve: Check official docs for latest implementation details


## 5. Conversion is possible: Skills can be adapted between platforms with some effort



## 6. Open standard exists: agentskills.io provides platform-agnostic specification


For this curriculum: We teach Anthropic's approach in depth, knowing the principles apply
broadly and the implementation is likely to influence the field.


### Your next steps:



## 1. Master Skills using Anthropic's implementation (Sections 1.1-1.6)



## 2. Apply principles to your platform of choice



## 3. Contribute to the open standard evolution


## 4. Share your skills with the community



### Resources at a glance:



### GitHub:


• Anthropic Skills Repo: https://github.com/anthropics/skills
• Skill Creator: https://github.com/anthropics/skills/tree/main/skills/skill-creator


### Documentation:


• Skills Guide: https://support.claude.com/en/articles/12580051


---
**Page 16**

• Blog Post: https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-
skills

• API Docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview


### Standard:


• Open Specification: https://agentskills.io/specification


## END OF APPENDIX C


Document Version: 1.0.0
Last Updated: 2026-01-30
Note:* Platforms evolve rapidly—verify current implementation details in official

documentation*
Key Principle:* Skills concepts are universal; implementations are platform-specific*
