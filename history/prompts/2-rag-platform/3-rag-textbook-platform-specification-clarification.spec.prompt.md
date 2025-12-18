---
id: 3
title: RAG Textbook Platform Specification Clarification
stage: spec
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: 2-rag-platform
branch: 1-rag-backend
user: unknown
command: /sp.clarify
labels: ["clarification", "spec"]
links:
  spec: specs/2-rag-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-rag-platform/spec.md
tests:
- None
---

## Prompt

```json
{
  "answers": {
    "Do we include BOTH Gemini and OpenAI in production, or only Gemini unless a fallback is triggered?":
      "Gemini is primary. OpenAI used only as automatic fallback if Gemini fails.",

    "Should the chatbot UI be visible on ALL Docusaurus pages or only on selected textbook pages?":
      "Chatbot UI should be globally available on all pages for maximum usability.",

    "For citations, do we reference by document name only, or include heading + paragraph?":
      "Include document name + heading only. Paragraph reference is optional.",

    "Will indexing be one-time manual script execution, or triggered automatically on GitHub push?":
      "Manual execution during build + optional reindex script if docs change.",

    "Should Better-Auth support social login (e.g., Google) or email/password only?":
      "Email/password only for MVP. Social login optional later.",

    "Is user personalization applied to entire chapters or only to specific sections?":
      "Only modify visible sections, not entire chapters.",

    "For Urdu translation, do we store translated content in DB or generate fresh each time?":
      "Generate dynamically at runtime. Do NOT store in DB.",

    "Should users be able to download personalization or translation results as a PDF?":
      "Not required for MVP. Consider later as a bonus."
  }
}
```

## Response snapshot

The feature specification `specs/2-rag-platform/spec.md` has been updated with clarifications on LLM usage, chatbot UI visibility, citations format, indexing, Better-Auth login, user personalization scope, Urdu translation storage, and PDF download functionality. The specification is now ready for the planning phase.

## Outcome

- ✅ Impact: Specification clarified and updated.
- 🧪 Tests: None.
- 📁 Files: specs/2-rag-platform/spec.md modified.
- 🔁 Next prompts: Ready for /sp.plan.
- 🧠 Reflection: Successfully integrated all user clarifications into the spec, addressing ambiguities and refining requirements. Faced continued issues with `pwsh` script execution, necessitating manual PHR creation.

## Evaluation notes (flywheel)

- Failure modes observed: `pwsh` command not found.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Implement a robust, cross-platform PHR creation mechanism that doesn't rely on `pwsh`.
