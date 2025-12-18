---
id: 5
title: RAG Textbook Platform Phase 1 Tasks
stage: tasks
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: 2-rag-platform
branch: 1-rag-backend
user: unknown
command: /sp.tasks
labels: ["tasks", "backend", "fastapi"]
links:
  spec: specs/2-rag-platform/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/2-rag-platform/tasks.md
tests:
- None
---

## Prompt

```text
You are Spec-Kit’s task slicer for the “RAG Textbook Platform”.

Use:
- .specify/memory/constitution.md (v0.2.0)
- specs/2-rag-platform/spec.md
- The latest /sp.plan for feature branch 2-rag-platform

Your job: turn the *current phase of the plan* into a small set of concrete, engineer-ready tasks that Claude Code can implement next.

Constraints (must respect all of these):
- Architecture & tech must follow the constitution:
  - Frontend: Docusaurus v3+ in my-ai-book/, GitHub Pages deployment, chatbot embedded via backend REST API.
  - Backend: single FastAPI service in backend/ (rag_service.py as main app, plus indexing_script.py, auth_db_service.py, optional personalization.py and translation.py).
  - RAG: markdown from my-ai-book/docs/**, 1000-char chunks with 200-char overlap, Qdrant Cloud Free Tier, Top K = 4, selected_text priority, expert tutor system prompt, and exact fallback string: “Information unavailable in the textbook.”
  - Data: Neon Postgres for auth/user data/chat history; .env for all secrets; CORS *.
  - LLM: Gemini as primary, OpenAI only as automatic fallback.
- All tasks must trace back to FR-### / SC-### in specs/2-rag-platform/spec.md where possible.

Task-slicing requirements:

1. Focus on the *next executable phase* from the plan only (do NOT explode the entire project at once).
   - If Phase 1 is not complete, generate tasks for:
     - Backend FastAPI skeleton in backend/rag_service.py
     - Basic routing + /health endpoint
     - Environment config loading from .env
     - CORS * setup
   - If Phase 1 is complete, move to the next phase (e.g., indexing pipeline, then RAG query endpoint, etc.).

2. For each task, provide:
   - A unique *TASK_ID* (e.g., TASK-1.1, TASK-1.2).
   - A short, action-oriented *title* (e.g., “Create FastAPI app skeleton in backend/rag_service.py”).
   - 2–4 sentence *description*:
     - What needs to be done.
     - Which files/folders to touch (backend/, my-ai-book/, specs/2-rag-platform/spec.md).
     - Any specific behaviors or constraints from the constitution/spec (e.g., chunk size, Top K, exact error message).
   - A *“Definition of Done”* bullet list that is testable (e.g., curl example, pytest hint, or Docusaurus page behavior).
   - A short *“Links”* line listing relevant FR-### / SC-### IDs.

3. Make tasks *small, independent, and Claude-Code friendly*:
   - Aim for 1–3 hour chunks for a single engineer.
   - Avoid multi-day “mega-tasks”.
   - Keep cross-file edits within a task logically tight (e.g., “Implement query endpoint and unit tests”, not “build backend and frontend together”).

4. Prioritize *critical-path tasks*:
   - Backend foundation before Docusaurus integration.
   - Indexing before answering real queries.
   - Core RAG answering (with citations + no-answer behavior) before personalization or Urdu translation extras.
   - Neon schema + minimal chat history before advanced user personalization.

5. At the end, output a short *“Next Steps for /sp.implement”* section:
   - One paragraph explaining how these tasks should be fed into /sp.implement (e.g., implement TASK-1.1 → TASK-1.2 → TASK-1.3).
   - Clarify any environment pre-setup needed (Gemini/OpenAI keys, Qdrant URL/API key, Neon URL/user/password) before implementation can start.

Output format:
- Use Markdown.
- List tasks as:

  - TASK-ID: Title
    - Description: …
    - Definition of Done:
      - …
    - Links: FR-###, SC-###
```

## Response snapshot

Generated implementation tasks for Phase 1 (Backend RAG Foundation) of the "RAG Textbook Platform" plan, including setting up the FastAPI project skeleton, implementing a basic health check, and configuring CORS middleware and environment variables. The tasks are detailed with descriptions, definitions of done, and links to relevant functional requirements and success criteria. A "Next Steps for /sp.implement" section provides guidance for sequential implementation and environment setup.

## Outcome

- ✅ Impact: Phase 1 tasks for RAG Textbook Platform generated and saved.
- 🧪 Tests: None.
- 📁 Files: specs/2-rag-platform/tasks.md created.
- 🔁 Next prompts: Ready for /sp.implement.
- 🧠 Reflection: Successfully generated tasks for the first phase of the plan, adhering to all constraints and formatting requirements. Continued to encounter `pwsh` execution issues, requiring manual PHR creation.

## Evaluation notes (flywheel)

- Failure modes observed: `pwsh` command not found.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Resolve `pwsh` execution or implement a pure-bash alternative for PHR generation.
