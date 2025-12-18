# Tasks for RAG Textbook Platform (Phase 1: Backend RAG Foundation)

## Phase 1: Backend RAG Foundation

- [X] TASK-1.1: Setup FastAPI project skeleton
  - Description: Create the basic FastAPI application structure in `backend/rag_service.py`, including an initial `requirements.txt` file listing `fastapi` and `uvicorn`, and a `uvicorn_start.sh` script to run the application. This establishes the core backend service. (FR-003, FR-007)
  - Definition of Done:
    - `backend/rag_service.py` exists with a minimal FastAPI app.
    - `backend/requirements.txt` exists and includes `fastapi` and `uvicorn`.
    - `backend/uvicorn_start.sh` exists and can run the FastAPI app (e.g., `uvicorn rag_service:app --host 0.0.0.0 --port 8000`).
    - Running `sh backend/uvicorn_start.sh` starts the FastAPI server successfully.
  - Links: FR-003, FR-007

- [X] TASK-1.2: Implement basic health check endpoint
  - Description: Add a simple GET `/health` endpoint to `backend/rag_service.py` that returns a success message (e.g., `{"status": "ok"}`). This endpoint will be used to verify the application's runtime status. (SC-004)
  - Definition of Done:
    - The `/health` endpoint is implemented in `backend/rag_service.py`.
    - Sending a GET request to `/health` (e.g., `curl http://localhost:8000/health`) returns `{"status": "ok"}`.
  - Links: SC-004

- [X] TASK-1.3: Configure CORS middleware and environment variables
  - Description: Implement CORS middleware in `backend/rag_service.py` to allow all origins (`*`). Additionally, set up a `.env` file at the project root for initial secret management, including placeholders for Qdrant URL and LLM API keys. (FR-011, FR-012, SC-006)
  - Definition of Done:
    - CORS middleware is configured in `backend/rag_service.py` to allow all origins.
    - A `.env` file exists at the project root with placeholder entries like `QDRANT_URL=`, `QDRANT_API_KEY=`, `GEMINI_API_KEY=`, `OPENAI_API_KEY=`.
    - The FastAPI application starts without CORS-related errors when accessed from a different origin (can be tested by a simple JavaScript fetch from an HTML file).
  - Links: FR-011, FR-012, SC-006

## Next Steps for /sp.implement

These tasks represent the foundational work for the backend RAG platform. They should be implemented sequentially: first TASK-1.1, then TASK-1.2, and finally TASK-1.3. Before starting implementation, ensure you have chosen a hosting target (Render, Fly.io, Railway, or Vercel Functions) and have the necessary environment variables (Gemini/OpenAI API keys, Qdrant URL/API key, Neon URL) ready to be configured in the `.env` file.
