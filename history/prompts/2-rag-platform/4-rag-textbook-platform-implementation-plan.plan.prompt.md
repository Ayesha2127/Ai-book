---
id: 4
title: RAG Textbook Platform Implementation Plan
stage: plan
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: 2-rag-platform
branch: 1-rag-backend
user: unknown
command: /sp.plan
labels: ["plan", "architecture"]
links:
  spec: specs/2-rag-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-rag-platform/plan.md
tests:
- None
---

## Prompt

```text
You are Spec-Kit’s planning agent for the “RAG Textbook Platform”.

Use:
- .specify/memory/constitution.md (v0.2.0)
- specs/2-rag-platform/spec.md

Your job: break this feature into a *small, coherent set of implementation-ready tasks* that Claude Code can execute next, respecting the Spec-Kit flow: /sp.constitution → /sp.specify → /sp.plan → /sp.task → /sp.implement.

Plan requirements:

1. Organize tasks into *phases*:
   - Phase 1: Backend RAG foundation (FastAPI skeleton, environment, healthcheck).
   - Phase 2: RAG indexing pipeline (from my-ai-book/docs/** → chunking → embeddings → Qdrant).
   - Phase 3: RAG query endpoint(s) with citations and “Information unavailable in the textbook.” behavior.
   - Phase 4: Docusaurus integration (embed chatbot UI on all pages and wire it to the backend).
   - Phase 5: Neon Postgres integration for auth/user data/chat history (MVP level).
   - Phase 6: Optional personalization + Urdu translation features (as separate follow-on tasks).

2. For each phase, produce *numbered tasks* with:
   - A clear, action-oriented title (e.g., “Implement FastAPI app skeleton in backend/rag_service.py”).
   - A 1–3 sentence description of what to do.
   - Direct references to relevant files/folders (e.g., backend/, my-ai-book/, specs/2-rag-platform/spec.md).
   - Links back to specific *FR-###* and *SC-###* IDs from the spec wherever applicable.

3. Explicitly enforce *constitution + spec constraints* in the tasks:
   - FastAPI backend in backend/ only, deployable to Render/Fly.io/Railway/Vercel Functions.
   - RAG rules: Qdrant Cloud, 1000-char chunks with 200-char overlap, Top K = 4, selected_text priority, expert-tutor system prompt, and the exact no-answer text: “Information unavailable in the textbook.”
   - LLM: Gemini as primary, OpenAI only as automatic fallback.
   - CORS *, .env for all secrets, Neon for user data and chat history.
   - Chatbot UI embedded on *all* Docusaurus pages via REST API.

4. Make tasks *small, concrete, and parallelizable*, suitable to become /sp.task tickets:
   - Avoid giant “do everything” tasks.
   - Prefer 1–3 hour chunks of work per task for a single engineer.
   - Include at least:
     - One task for setting up backend project structure per constitution (rag_service.py, indexing_script.py, auth_db_service.py, etc.).
     - One task for wiring Docusaurus frontend to call the FastAPI endpoint and render responses + citations.
     - One task for Urdu query/response handling.
     - One task for Neon schema and basic CRUD for chat history and user profile.

5. Add a short *“Dependencies & Sequencing”* section:
   - Describe which tasks must be done first (e.g., backend skeleton before Docusaurus integration, indexing before production queries).
   - Note any environment setup preconditions (Gemini/OpenAI keys, Qdrant URL/key, Neon URL).

6. Add a concise *“Ready for /sp.task when…”* checklist:
   - List the conditions that, once met, mean we can safely convert each planned item into /sp.task tickets (e.g., architecture validated, env vars defined, hosting target chosen).

Output format:
- Use Markdown with headings for each phase.
- Under each phase, list tasks as - [ ] TASK_ID: Short title followed by a brief description and references to FR/SC IDs.
```

## Response snapshot

The implementation plan for the "RAG Textbook Platform" is complete and has been saved to `specs/2-rag-platform/plan.md`. The plan outlines phases for backend RAG foundation, indexing, query endpoints, Docusaurus integration, and Neon Postgres integration, with detailed, actionable tasks and adherence to constitution and spec constraints. Dependencies, sequencing, and a readiness checklist are also included.

## Outcome

- ✅ Impact: Comprehensive implementation plan created.
- 🧪 Tests: None.
- 📁 Files: specs/2-rag-platform/plan.md created.
- 🔁 Next prompts: Ready for /sp.task.
- 🧠 Reflection: Successfully generated a detailed plan that breaks down the feature into manageable tasks, adhering to all specified constraints. Encountered persistent `pwsh` execution failures, requiring manual PHR creation.

## Evaluation notes (flywheel)

- Failure modes observed: `pwsh` command not found.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Address `pwsh` availability or provide a pure-bash alternative for `create-phr.sh`.
