---
id: 2
title: RAG Textbook Platform Specification
stage: spec
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: 2-rag-platform
branch: 1-rag-backend
user: unknown
command: /sp.specify
labels: ["rag", "platform", "docusaurus", "fastapi"]
links:
  spec: specs/2-rag-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-rag-platform/spec.md
- specs/2-rag-platform/checklists/requirements.md
tests:
- None
---

## Prompt

```json
{
  "name": "RAG Textbook Platform Specification",
  "objectives": [
    "Publish a Docusaurus textbook on GitHub Pages",
    "Build a FastAPI RAG chatbot that answers ONLY using textbook content with citations",
    "Use Spec-Kit Plus & Claude Code for a clean, scalable architecture",
    "Maintain a single unified GitHub repository"
  ],
  "tech_stack": {
    "frontend": "Docusaurus v3+ static site with embedded REST API chatbot",
    "backend": "FastAPI deployed on Render / Railway / Fly.io / Vercel",
    "llm": "Gemini preferred, OpenAI fallback",
    "vector_db": "Qdrant Cloud Free Tier",
    "auth_db": "Neon Serverless Postgres"
  },
  "security_rules": [
    "All secrets in .env only",
    "No hardcoded tokens",
    "CORS allow all"
  ],
  "rag_requirements": {
    "source_path": "/my-ai-book/docs/**",
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "retrieval_top_k": 4,
    "grounding_rule": "Reply 'Information unavailable in the textbook' when no context match",
    "citations_required": true
  },
  "bonus_features": [
    "Claude Skills or Subagents for summaries / quizzes / glossary",
    "Better-Auth signup collecting background + preferences",
    "Personalized textbook view stored in DB",
    "Urdu translation toggle for logged-in users"
  ],
  "repo_structure": [
    "/my-ai-book/docs",
    "/backend/rag_service.py",
    "/backend/indexing_script.py",
    "/backend/auth_db_service.py",
    "/backend/personalization.py",
    "/backend/translation.py"
  ],
  "grading_rules": [
    "Strict grounding, no hallucinations",
    "Qdrant embeddings required",
    "User data must persist in Postgres"
  ]
}
```

## Response snapshot

The feature specification for "RAG Textbook Platform Specification" has been successfully created and validated. The feature branch `2-rag-platform` has been set up, and the specification document `specs/2-rag-platform/spec.md` along with its validation checklist `specs/2-rag-platform/checklists/requirements.md` (all checks passed) are now available. The specification is ready for the planning phase.

## Outcome

- ✅ Impact: New feature specification created and validated.
- 🧪 Tests: None.
- 📁 Files: specs/2-rag-platform/spec.md, specs/2-rag-platform/checklists/requirements.md created.
- 🔁 Next prompts: Ready for /sp.plan.
- 🧠 Reflection: Successfully parsed JSON input and generated a comprehensive feature specification. Handled manual file creation due to script execution issues.

## Evaluation notes (flywheel)

- Failure modes observed: `pwsh` command not found, JSON escaping issues in bash.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Improve robust JSON parsing for bash and ensure `pwsh` availability or provide a pure-bash alternative for `create-new-feature.ps1`.
