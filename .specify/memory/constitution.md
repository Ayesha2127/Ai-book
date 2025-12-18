<!--
Sync Impact Report:
Version change: 0.1.0 -> 0.2.0 (MINOR: New principles and sections added)
Modified principles: None
Added sections: Technology & Architecture Rules, RAG Pipeline Requirements, Development Flow Rules, Mandatory Folder Structure
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
- README.md ⚠ pending
- docs/quickstart.md ⚠ pending
Follow-up TODOs: TODO(RATIFICATION_DATE): Original adoption date unknown
-->
# Physical AI Textbook & RAG Chatbot Constitution

## Core Principles

### I. Docusaurus Textbook Publication
The project MUST publish a Docusaurus v3+ textbook on GitHub Pages, embedding the chatbot using the backend REST API.

### II. Fully Functional RAG Chatbot
The project MUST include a fully functional RAG chatbot that answers ONLY from the textbook content.

### III. Spec-Driven Architecture
The project MUST utilize a clean, scalable, spec-driven architecture using Spec-Kit Plus and Claude Code.

### IV. Unified GitHub Repository
The entire project MUST be contained within a single unified GitHub repository.

## Technology & Architecture Rules

**Frontend**:
- Framework: Docusaurus v3+
- Build: Static GitHub Pages deployment
- Integration: Must embed chatbot using backend REST API

**Backend**:
- Framework: FastAPI (single backend service)
- Hosting: Render / Fly.io / Railway / Vercel Functions

**Embeddings + LLM**:
- Allowed Models: Gemini API (Recommended), OpenAI (fallback if needed)

**Databases**:
- Qdrant Cloud Free Tier: All textbook embeddings + vector search required
- Neon Serverless Postgres: All user data must persist (Auth records (Better-Auth.com), User hardware/software background, Personalization preferences)

**Secure Config**: ALL secrets MUST use .env, no hardcoded keys anywhere.

**Communication**: CORS middleware required (* → allow all origins).

## RAG Pipeline Requirements

**Indexing**:
- Source: Use markdown docs from `/my-ai-book/docs/**`
- Chunking: 1000 chars, 200 char overlap (RecursiveTextSplitter)
- Storage: Store in Qdrant

**Retrieval**:
- Top K: Top 4 chunks for every query
- Context Priority: If user provides `selected_text`, prioritize that context

**Generation**:
- System Prompt: "You are an expert tutor. Use ONLY the provided context. If the answer is not in the context, reply: 'Information unavailable in the textbook.'"

**Response Format**: Provide answer + citations (document + heading)

## Development Flow Rules

- Follow the Spec-Kit Development Cycle: /sp.constitution → /sp.specify → /sp.plan → /sp.task → /sp.implement
- All new features MUST be implemented as tasks in Claude Code.

## Mandatory Folder Structure

- /
    - .env
    - README.md
    - my-ai-book/                 # Docusaurus Frontend
        - docs/                   # All textbook content (.md)
        - src/
    - backend/
        - requirements.txt
        - rag_service.py          # Main FastAPI app (core)
        - indexing_script.py      # Qdrant indexer
        - auth_db_service.py      # Neon + Better-Auth Helpers
        - personalization.py      # Bonus feature logic (optional)
        - translation.py          # Urdu feature logic (optional)
        - uvicorn_start.sh

## Governance
This constitution supersedes all other project practices and documentation. Amendments require explicit documentation, stakeholder approval, and a migration plan if changes are breaking. All pull requests and code reviews MUST verify compliance with these principles. Complexity MUST be justified, adhering to the principle of simplicity. Refer to the `CLAUDE.md` file for runtime development guidance.

**Version**: 0.2.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date unknown | **Last Amended**: 2025-12-02
