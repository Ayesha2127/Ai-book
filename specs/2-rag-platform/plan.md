# Implementation Plan: RAG Textbook Platform

**Branch**: `2-rag-platform` | **Date**: 2025-12-02 | **Spec**: specs/2-rag-platform/spec.md
**Input**: Feature specification from `/specs/2-rag-platform/spec.md`

## Summary

This plan outlines the implementation for the "RAG Textbook Platform", which aims to publish a Docusaurus textbook on GitHub Pages and integrate a FastAPI RAG chatbot. The chatbot will answer questions based solely on the textbook content, providing citations, and will be built with a clean, scalable, spec-driven architecture within a single unified GitHub repository.

## Technical Context

**Language/Version**: Python 3.11 (for backend), JavaScript/TypeScript (for frontend Docusaurus)
**Primary Dependencies**: FastAPI, QdrantClient, AsyncOpenAI (for Gemini/OpenAI), Docusaurus
**Storage**: Qdrant Cloud Free Tier (vector embeddings), Neon Serverless Postgres (user data, auth records, personalization preferences)
**Testing**: Pytest (backend), Docusaurus testing utilities (frontend)
**Target Platform**: Linux server (FastAPI backend), Web (Docusaurus frontend deployed to GitHub Pages)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: `/chat` endpoint responds within 3 seconds (SC-001)
**Constraints**: CORS allow all origins, `.env` for all secrets, single unified GitHub repository
**Scale/Scope**: Process 95% of user queries with relevant answers, ensure persistent user data storage.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **I. Docusaurus Textbook Publication**: Plan includes tasks for Docusaurus setup and GitHub Pages deployment, embedding the chatbot via REST API (FR-001, FR-002, SC-001).
- [X] **II. Fully Functional RAG Chatbot**: Core phases are dedicated to RAG backend, indexing, query endpoints, and Docusaurus integration for chatbot functionality (FR-003, FR-004, FR-005, FR-008, FR-016, FR-017, FR-018, FR-019, SC-002, SC-003).
- [X] **III. Spec-Driven Architecture**: Adhering to the Spec-Kit Plus and Claude Code development cycle, as evidenced by this plan (FR-006, SC-004).
- [X] **IV. Unified GitHub Repository**: The plan assumes a single repository structure as defined (FR-007).
- [X] **Technology & Architecture Rules**: All specified technologies (FastAPI, Docusaurus, Gemini/OpenAI, Qdrant Cloud, Neon Postgres) and rules (.env for secrets, CORS) are incorporated into the plan and tasks (FR-008, FR-009, FR-010, FR-011, FR-012, SC-005, SC-006).
- [X] **RAG Pipeline Requirements**: Indexing (source, chunking, storage), retrieval (top K, context priority), and generation (system prompt, response format, no-answer text) are explicitly defined in tasks (FR-013, FR-014, FR-015, FR-016, FR-017, FR-018, FR-019, SC-002, SC-003).
- [X] **Development Flow Rules**: This plan adheres to the specified development cycle, and tasks will be implemented via Claude Code.
- [X] **Mandatory Folder Structure**: The plan respects the required folder structure (backend/, my-ai-book/docs/, etc.).

## Project Structure

### Documentation (this feature)

```text
specs/2-rag-platform/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
my-ai-book/                 # Docusaurus Frontend
├── docs/                   # All textbook content (.md)
└── src/

backend/
├── requirements.txt
├── rag_service.py          # Main FastAPI app (core)
├── indexing_script.py      # Qdrant indexer
├── auth_db_service.py      # Neon + Better-Auth Helpers
├── personalization.py      # Bonus feature logic (optional)
├── translation.py          # Urdu feature logic (optional)
└── uvicorn_start.sh
```

**Structure Decision**: The project will use a split frontend/backend structure with Docusaurus for the frontend (`my-ai-book/`) and FastAPI for the backend (`backend/`), adhering to the mandatory folder structure outlined in the constitution.

## Phase 1: Backend RAG Foundation

- [ ] 1.1: Setup FastAPI project skeleton. Create the basic FastAPI application structure in `backend/rag_service.py` including `requirements.txt` and `uvicorn_start.sh`. (FR-003, FR-007)
- [ ] 1.2: Implement basic health check endpoint. Add a simple `/health` endpoint to `backend/rag_service.py` to verify the application is running. (SC-004)
- [ ] 1.3: Configure CORS middleware and environment variables. Implement CORS middleware allowing all origins (`*`) in `backend/rag_service.py` and set up `.env` file for initial secret management (e.g., Qdrant URL, LLM API keys). (FR-011, FR-012, SC-006)

## Phase 2: RAG Indexing Pipeline

- [ ] 2.1: Implement document loading and chunking. Develop logic to load markdown documents from `my-ai-book/docs/**` and chunk them using RecursiveTextSplitter with 1000 characters and 200 character overlap. (FR-013, FR-014)
- [ ] 2.2: Generate embeddings and store in Qdrant. Convert document chunks into vector embeddings and implement logic to store these in Qdrant Cloud Free Tier. (FR-009, FR-015)
- [ ] 2.3: Create indexing script (`indexing_script.py`). Develop a standalone script `backend/indexing_script.py` to orchestrate the document loading, chunking, embedding generation, and Qdrant storage. This script will support manual execution. (FR-013, FR-015)

## Phase 3: RAG Query Endpoint(s)

- [ ] 3.1: Implement Qdrant retrieval logic. Develop functionality to query Qdrant, returning the top 4 relevant chunks based on the user's query, prioritizing `selected_text` if provided. (FR-003, FR-016, FR-017, SC-002)
- [ ] 3.2: Integrate Gemini LLM (with OpenAI fallback) and system prompt. Initialize AsyncOpenAI with the Gemini Bridge Pattern and configure the system prompt: "You are an expert tutor. Use ONLY the provided context." Implement automatic fallback to OpenAI if Gemini fails. (FR-008, FR-018)
- [ ] 3.3: Format AI response with citations and "Information unavailable in the textbook." text. Ensure AI-generated responses include citations (document + heading) and explicitly return "Information unavailable in the textbook." if the answer is not in the context. (FR-005, FR-019, SC-003)
- [ ] 3.4: Create `/chat` endpoint in `rag_service.py`. Implement the `POST /chat` endpoint in `backend/rag_service.py` to handle incoming queries, orchestrate retrieval and generation, and return the formatted AI response. (FR-002, SC-001)

## Phase 4: Docusaurus Integration

- [ ] 4.1: Setup Docusaurus project. Initialize the Docusaurus project in `my-ai-book/` and configure it for GitHub Pages deployment. (FR-001, SC-001)
- [ ] 4.2: Embed chatbot UI on all Docusaurus pages. Develop a Docusaurus component or theme modification to embed the chatbot UI, ensuring global availability across all pages. (FR-002)
- [ ] 4.3: Wire frontend to call FastAPI `/chat` endpoint and render responses. Implement JavaScript/TypeScript logic within Docusaurus to send user queries to the `POST /chat` endpoint and display the AI's responses, including citations, within the UI. (FR-002, FR-005, SC-002)

## Phase 5: Neon Postgres Integration

- [ ] 5.1: Define Neon Postgres schema for auth/user data/chat history. Design the database schema for storing user authentication records, hardware/software background, personalization preferences, and chat history in Neon Serverless Postgres. (FR-010, SC-005)
- [ ] 5.2: Implement basic CRUD operations in `auth_db_service.py`. Develop functions in `backend/auth_db_service.py` for creating, reading, updating, and deleting user data in Neon Postgres. (FR-010, SC-005)
- [ ] 5.3: Integrate user data storage with chatbot/authentication (MVP). Wire up the basic authentication flow (email/password only for MVP) and user profile storage/retrieval with the FastAPI backend. (FR-010, FR-011, Bonus Feature: Authentication)

## Phase 6: Optional Features (Follow-on Tasks)

- [ ] 6.1: Implement Better-Auth signup with profile collection. Integrate Better-Auth.com for user signup, collecting software skills level and hardware experience using email/password only for MVP. (Bonus Feature: Authentication)
- [ ] 6.2: Implement personalized content logic. Develop backend logic (`backend/personalization.py`) to generate modified introductions/explainers based on user profiles, applied only to visible sections, with consistency maintained across visits via database updates. (Bonus Feature: Personalized Content)
- [ ] 6.3: Implement Urdu translation. Develop functionality (`backend/translation.py`) for logged-in users to dynamically generate visible page content translation to Urdu at runtime, with scrollable text and a toggle back to English. (Bonus Feature: Urdu Translation)

## Dependencies & Sequencing

-   **Backend Foundation (Phase 1)** must be completed before starting any other backend-dependent phases.
-   **RAG Indexing Pipeline (Phase 2)** must be completed and an initial index created before the RAG Query Endpoint (Phase 3) can return meaningful results.
-   **RAG Query Endpoint (Phase 3)** must be functional before Docusaurus Integration (Phase 4) can fully wire the chatbot UI.
-   **Neon Postgres Integration (Phase 5)** can begin in parallel with other backend phases, but its integration with authentication (Task 5.3) depends on basic auth setup.
-   **Optional Features (Phase 6)** are independent follow-on tasks and should only commence after the core RAG Textbook Platform (Phases 1-5) is stable and functional.

**Environment Setup Preconditions**:
-   Access to Gemini API key (`.env`).
-   Access to OpenAI API key (for fallback, `.env`).
-   Qdrant Cloud URL and API key (`.env`).
-   Neon Serverless Postgres connection URL (`.env`).

## Ready for /sp.task when…

- [ ] The overall architectural approach for each phase has been validated.
- [ ] All necessary environment variables (LLM keys, Qdrant, Neon URLs) are defined and accessible.
- [ ] A hosting target (Render, Fly.io, Railway, or Vercel Functions) has been chosen for the FastAPI backend.
- [ ] Basic project repositories (if separate for frontend/backend beyond the unified repo) are initialized.
- [ ] No further critical ambiguities exist that would significantly alter task scope.
