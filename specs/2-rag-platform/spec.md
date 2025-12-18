# Feature Specification: RAG Textbook Platform

**Feature Branch**: `2-rag-platform`
**Created**: 2025-12-02
**Status**: Draft

## User Scenarios & Testing

### User Story 1 - View Textbook and Interact with Chatbot (Priority: P1)

As a user, I want to browse the Docusaurus textbook and ask questions related to its content through an embedded chatbot, so that I can easily find information and clarify concepts.

**Why this priority**: This covers the core functionality of both the textbook display and the RAG chatbot interaction.

**Independent Test**: Can be tested by navigating the Docusaurus site, and then sending queries to the embedded chatbot and verifying responses are grounded in the textbook content and include citations.

**Acceptance Scenarios**:

1.  **Given** the Docusaurus textbook is published and the chatbot is active, **When** I navigate to a textbook page, **Then** I can view the content and see an embedded chatbot interface.
2.  **Given** the chatbot is running, **When** I ask a question (e.g., "What are the main components of ROS 2?"), **Then** the chatbot returns an answer based on the textbook content, including citations.
3.  **Given** the chatbot is running, **When** I ask a question that is not in the textbook content, **Then** the chatbot replies: "Information unavailable in the textbook."

### Edge Cases

- What happens if the backend API for the chatbot is unavailable?
- How does the system handle very long or complex user queries?
- What is the behavior if no relevant chunks are found by Qdrant for a query?

## Requirements

### Functional Requirements

- **FR-001**: The system MUST publish a Docusaurus textbook on GitHub Pages.
- **FR-002**: The Docusaurus frontend MUST embed a chatbot UI globally available on all pages using a backend REST API.
- **FR-003**: The chatbot MUST be built using FastAPI.
- **FR-004**: The RAG chatbot MUST answer ONLY from the textbook content.
- **FR-005**: The chatbot responses MUST include citations (document + heading only. Paragraph reference is optional).
- **FR-006**: The system MUST use Spec-Kit Plus & Claude Code for architectural development.
- **FR-007**: The project MUST reside in a single unified GitHub repository.
- **FR-008**: The system MUST use Gemini API for LLM generation. OpenAI will be used only as an automatic fallback if Gemini fails.
- **FR-009**: The system MUST use Qdrant Cloud Free Tier for all textbook embeddings and vector search.
- **FR-010**: The system MUST use Neon Serverless Postgres for persisting all user data (auth records, hardware/software background, personalization preferences).
- **FR-011**: All secrets MUST be stored in `.env` files and not hardcoded.
- **FR-012**: CORS middleware allowing all origins (`*`) MUST be implemented in the backend.
- **FR-013**: The RAG indexing process MUST use markdown docs from `/my-ai-book/docs/**` and be manually executed during build, with an optional reindex script for doc changes.
- **FR-014**: The RAG chunking process MUST use a chunk size of 1000 characters with 200 characters overlap (RecursiveTextSplitter).
- **FR-015**: The RAG indexing process MUST store chunks in Qdrant.
- **FR-016**: The RAG retrieval process MUST return the top 4 chunks for every query.
- **FR-017**: The RAG retrieval process MUST prioritize `selected_text` provided by the user as context.
- **FR-018**: The RAG generation system prompt MUST ensure the AI acts as an expert tutor and uses ONLY the provided context.
- **FR-019**: If the answer is not in the provided context, the AI MUST reply: "Information unavailable in the textbook."

### Key Entities

-   **Textbook**: Docusaurus-based content published on GitHub Pages.
-   **Chatbot**: FastAPI service providing RAG functionality.
-   **User Query**: The question or input from the user.
-   **Context**: Textual information (from vector search or user-provided) used by the LLM.
-   **Embeddings**: Vector representations of textbook chunks stored in Qdrant.
-   **User Data**: Authentication records, user profile (skills, hardware experience), and personalization preferences stored in Neon Postgres.
-   **Citations**: References to the document and heading from which information was retrieved.

## Success Criteria

### Measurable Outcomes

-   **SC-001**: The Docusaurus textbook is successfully published and accessible on GitHub Pages.
-   **SC-002**: The embedded chatbot successfully processes 95% of user queries, providing relevant answers grounded in the textbook content.
-   **SC-003**: Chatbot responses consistently include accurate citations.
-   **SC-004**: The overall architecture demonstrates cleanliness, scalability, and adherence to spec-driven development principles.
-   **SC-005**: User data for authentication, background profile, and personalization is persistently stored in Neon Serverless Postgres.
-   **SC-006**: All secrets are securely managed using `.env` files, with no hardcoded credentials found in the codebase.

## Assumptions

- A GitHub Pages environment is available and configured for Docusaurus deployment.
- The selected backend hosting platform (Render/Fly.io/Railway/Vercel) provides the necessary environment for FastAPI deployment.
- API keys for Gemini and OpenAI are securely provided via environment variables.
- Qdrant Cloud Free Tier provides sufficient capacity for textbook embeddings.
- Neon Serverless Postgres is accessible and configured for user data storage.
- Users will interact with the textbook and chatbot via a web browser.

## Clarifications

### Session 2025-12-02
- Q: Do we include BOTH Gemini and OpenAI in production, or only Gemini unless a fallback is triggered? → A: Gemini is primary. OpenAI used only as automatic fallback if Gemini fails.
- Q: Should the chatbot UI be visible on ALL Docusaurus pages or only on selected textbook pages? → A: Chatbot UI should be globally available on all pages for maximum usability.
- Q: For citations, do we reference by document name only, or include heading + paragraph? → A: Include document name + heading only. Paragraph reference is optional.
- Q: Will indexing be one-time manual script execution, or triggered automatically on GitHub push? → A: Manual execution during build + optional reindex script if docs change.
- Q: Should Better-Auth support social login (e.g., Google) or email/password only? → A: Email/password only for MVP. Social login optional later.
- Q: Is user personalization applied to entire chapters or only to specific sections? → A: Only modify visible sections, not entire chapters.
- Q: For Urdu translation, do we store translated content in DB or generate fresh each time? → A: Generate dynamically at runtime. Do NOT store in DB.
- Q: Should users be able to download personalization or translation results as a PDF? → A: Not required for MVP. Consider later as a bonus.

## Technical Considerations

**Frontend (`my-ai-book/`)**:
- Docusaurus v3+ setup for documentation.
- Integration point for the FastAPI chatbot via REST API.

**Backend (`backend/`)**:
- FastAPI application (`rag_service.py`) for the core chatbot logic.
- Separate script (`indexing_script.py`) for Qdrant indexing.
- Authentication and database helpers (`auth_db_service.py`) for Neon Postgres and Better-Auth.com integration.
- Optional modules for personalization (`personalization.py`) and translation (`translation.py`).
- `requirements.txt` for Python dependencies.
- `uvicorn_start.sh` for running the FastAPI application.

**RAG Pipeline**:
- **Indexing**: RecursiveTextSplitter for chunking markdown files, Qdrant for vector storage. Indexing will be a manual execution during build, with an optional reindex script for doc changes.
- **Retrieval**: Top-k search in Qdrant, with prioritization of user-provided `selected_text`.
- **Generation**: AsyncOpenAI (Gemini Bridge Pattern) with specific system prompt.

**Security**:
- Use of `.env` for all sensitive configurations.
- CORS configuration to allow all origins.

**Deployment**:
- Frontend: GitHub Pages.
- Backend: Cloud platform (Render, Fly.io, Railway, or Vercel Functions).

## Bonus Features

- **Reusable Intelligence**: Potential integration of Claude Skills or Subagents for advanced features like chapter summaries, quizzes, or glossary generation.
- **Authentication**: Implementation of Better-Auth.com for user signup using email/password only for MVP, collecting software skills level and hardware experience.
- **Personalized Content**: Backend logic to generate modified introductions/explainers based on user profiles, applied only to visible sections (not entire chapters), with consistency maintained across visits via database updates.
- **Urdu Translation**: Functionality for logged-in users to dynamically generate visible page content translation to Urdu at runtime (not stored in DB), with scrollable text and toggle back to English.
- **PDF Download**: Downloading personalization or translation results as a PDF is not required for MVP and will be considered later as a bonus.

