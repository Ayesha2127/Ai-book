# Feature Specification: Physical AI & Humanoid Robotics RAG Backend

**Feature Branch**: `1-rag-backend`
**Created**: 2025-12-01
**Status**: Draft
**Input**: User description: "The system requires two components: an Indexer script and a RAG Service.

## Component 1: Indexing Script (indexing_script.py)

1.  *Input Data:* The script must be able to read one or more Markdown (.md) files representing the textbook chapters. We will use a mock file for initial testing.
2.  *Chunking:* Use a recursive text splitter to divide the content into chunks of *1000 characters* with an *overlap of 200 characters*.
3.  *Embedding:* Use the OpenAI embedding model (text-embedding-3-small) to generate 1536-dimensional vectors for each chunk.
4.  *Vector DB:* Connect to *Qdrant Cloud* using environment variables (QDRANT_URL, QDRANT_API_KEY).
5.  *Collection:* Create or use a Qdrant collection named physical_ai_textbook. Store the text content, the chapter source, and the chunk number as metadata alongside the vector.

## Component 2: FastAPI RAG Service (rag_service.py)

1.  *Server:* Create a FastAPI application running on Uvicorn.
2.  *CORS:* Apply CORS middleware allowing * origins for development simplicity.
3.  *Endpoint:* Define a POST endpoint /api/rag_query that accepts a JSON body with a single field: query (string).
4.  *Retrieval:*
    * Embed the incoming query.
    * Search the physical_ai_textbook collection in Qdrant for the *top 4 most similar vectors*.
    * Extract the raw text content from the retrieved chunks.
5.  *Generation (Synthesis):*
    * Construct a detailed prompt for the LLM (using the OpenAI API, assumed to be available to the agent) that includes the user's original query and the retrieved context chunks.
    * *System Prompt/Instruction:* "You are an expert tutor for a university-level course on Physical AI & Humanoid Robotics. Use ONLY the provided context to answer the student's question. If the context does not contain the answer, state clearly, 'I cannot find the answer in the textbook content.'"
    * Return the LLM's final generated answer along with the source chunks (as citations)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Index Textbook Content (Priority: P1)

As a data administrator, I want to index Markdown textbook chapters into the Qdrant Vector DB so that the RAG service can retrieve relevant information.

**Why this priority**: This is the foundational step; without indexed content, the RAG service cannot function.

**Independent Test**: The indexing script can be run with a mock Markdown file, and the Qdrant collection can be verified to contain the embedded chunks with correct metadata.

**Acceptance Scenarios**:

1.  **Given** a Markdown textbook chapter file and configured environment variables for Qdrant and OpenAI, **When** the indexing script is executed with the file, **Then** the `physical_ai_textbook` collection in Qdrant contains chunks with 1536-dimensional embeddings, original text content, chapter source, and chunk number as metadata.
2.  **Given** a Markdown file with multiple chapters, **When** the indexing script is executed, **Then** all chapters are chunked, embedded, and stored in Qdrant, maintaining chapter source and chunk numbers.

---

### User Story 2 - Query RAG Service for Textbook Answers (Priority: P1)

As a student, I want to ask questions about the Physical AI & Humanoid Robotics textbook via an API endpoint and receive answers based *only* on the textbook content, with citations to the source chunks.

**Why this priority**: This is the core functionality that delivers value to the end-user (student) and validates the RAG service.

**Independent Test**: The FastAPI RAG service can be deployed locally, and a POST request to `/api/rag_query` can be made with a test query to verify a coherent answer based on retrieved context and correct citations.

**Acceptance Scenarios**:

1.  **Given** the RAG service is running and the Qdrant collection is populated, **When** a POST request is made to `/api/rag_query` with a relevant question, **Then** the service returns a generated answer based *only* on the retrieved textbook context and includes source chunk citations.
2.  **Given** a question for which the answer is *not* present in the indexed textbook content, **When** a POST request is made to `/api/rag_query`, **Then** the service returns the specific message "I cannot find the answer in the textbook content."
3.  **Given** a question with multiple relevant sections in the textbook, **When** a POST request is made to `/api/rag_query`, **Then** the service retrieves the top 4 most similar vectors and uses them for generation.

---

### Edge Cases

- What happens when an invalid Markdown file is provided to the indexing script? (e.g., corrupted, non-existent) - *Assume script should gracefully handle, possibly log error and skip.*
- How does the system handle very long queries to the RAG service? - *Assume embedding model has limits, queries beyond a certain length might be truncated or rejected.*
- What if Qdrant or OpenAI APIs are unavailable during indexing or querying? - *Assume appropriate error handling and logging should be implemented.*
- What if a query has no relevant context in Qdrant? - *Handled by system prompt: "I cannot find the answer in the textbook content."*

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The Indexing Script MUST read one or more Markdown (.md) files as input.
- **FR-002**: The Indexing Script MUST chunk content using a recursive text splitter with 1000 characters per chunk and 200 characters overlap.
- **FR-003**: The Indexing Script MUST generate 1536-dimensional embeddings for each chunk using the OpenAI embedding model (text-embedding-3-small).
- **FR-004**: The Indexing Script MUST connect to Qdrant Cloud using `QDRANT_URL` and `QDRANT_API_KEY` environment variables.
- **FR-005**: The Indexing Script MUST create or use a Qdrant collection named `physical_ai_textbook`.
- **FR-006**: The Indexing Script MUST store the chunk's text content, chapter source, and chunk number as metadata in Qdrant.
- **FR-007**: The RAG Service MUST be a FastAPI application running on Uvicorn.
- **FR-008**: The RAG Service MUST include CORS middleware allowing `*` origins.
- **FR-009**: The RAG Service MUST define a POST endpoint `/api/rag_query` accepting a JSON body with a `query` (string) field.
- **FR-010**: The RAG Service MUST embed the incoming query using an OpenAI embedding model.
- **FR-011**: The RAG Service MUST search the `physical_ai_textbook` collection in Qdrant for the top 4 most similar vectors.
- **FR-012**: The RAG Service MUST extract raw text content from the retrieved chunks.
- **FR-013**: The RAG Service MUST construct a detailed prompt for the LLM including the user's query and retrieved context chunks, with the system prompt: "You are an expert tutor for a university-level course on Physical AI & Humanoid Robotics. Use ONLY the provided context to answer the student's question. If the context does not contain the answer, state clearly, 'I cannot find the answer in the textbook content.'"
- **FR-014**: The RAG Service MUST return the LLM's generated answer along with the source chunks as citations.

### Key Entities

- **Textbook Chunk**: Represents a segment of text from a textbook chapter. Attributes: `content` (string), `chapter_source` (string, e.g., filename), `chunk_number` (integer).
- **Query**: Represents the user's question to the RAG service. Attributes: `text` (string).
- **RAG Response**: The output from the RAG service. Attributes: `answer` (string), `citations` (list of strings, representing source chunks).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The indexing process for a typical textbook chapter (e.g., 50 pages) completes within [NEEDS CLARIFICATION: indexing time not specified - e.g., 5 minutes].
- **SC-002**: The RAG service responds to 95% of queries within 2 seconds.
- **SC-003**: The RAG service provides accurate answers for 90% of in-scope questions, as judged by human review.
- **SC-004**: When the answer is not in the context, the RAG service explicitly states "I cannot find the answer in the textbook content." 100% of the time.
- **SC-005**: All sensitive credentials (API keys) are loaded securely from environment variables, preventing hardcoding.
