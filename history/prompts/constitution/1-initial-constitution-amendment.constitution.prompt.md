A. Core Objectives (Must Deliver)
1️ Publish a Docusaurus textbook on GitHub Pages.
2️ Fully functional RAG chatbot answering ONLY from textbook content.
3️ Clean, scalable, spec-driven architecture using Spec-Kit Plus & Claude Code.
4️ Single unified GitHub repository.

------------------------------------------------
B. Technology & Architecture Rules

 Frontend
- Framework: Docusaurus v3+
- Build: Static GitHub Pages deployment
- Must embed chatbot using backend REST API

 Backend
- FastAPI (single backend service)
- Hosted on Render / Fly.io / Railway / Vercel Functions

 Embeddings + LLM
Allowed Models:
✔ Gemini API (Recommended)
✔ OpenAI (fallback if needed)

 Databases
1️ Qdrant Cloud Free Tier → All textbook embeddings + vector search required
2️ Neon Serverless Postgres → All user data must persist:
   - Auth records (Better-Auth.com)
   - User hardware/software background
   - Personalization preferences

 Secure Config
- ALL secrets must use .env
- No hardcoded keys anywhere

 Communication
- CORS middleware required (* → allow all origins)

------------------------------------------------
C. RAG Pipeline Requirements

Indexing
- Use markdown docs from `/my-ai-book/docs/**`
- Chunking: 1000 chars, 200 char overlap (RecursiveTextSplitter)
- Store in Qdrant

Retrieval
- Top 4 chunks for every query
- If user provides `selected_text`, prioritize that context

Generation
System Prompt must include:
“You are an expert tutor. Use ONLY the provided context.  
If the answer is not in the context, reply: 'Information unavailable in the textbook.' ”

Response Format
- Provide answer + citations (document + heading)

------------------------------------------------
D. Bonus Feature Requirements (Optional but HIGH SCORE)

1️⃣ Reusable Intelligence (50 pts)
- Implement Claude Skills or Subagents inside book workflow
- Example: Chapter summaries, quizzes, glossary generator

2️⃣ Authentication (50 pts)
- Use https://better-auth.com/
- Signup must collect background profile:
  • Software Skills Level (Beginner → Advanced)
  • Hardware Experience (Robotics? Sensors? GPU access?)

3️⃣ Personalized Content (50 pts)
- Chapter page shows “Personalize for Me” button (only if logged in)
- Backend generates modified intro/explainer based on user profile
- Must update DB so content remains consistent when revisiting

4️⃣ Urdu Translation (50 pts)
- “Translate to Urdu” button (logged-in users)
- Translate only visible page content
- Urdu text must be scrollable + toggle back to English

------------------------------------------------
E. Development Flow Rules
✔ Follow the Spec-Kit Development Cycle
/sp.constitution → /sp.specify → /sp.plan → /sp.task → /sp.implement

✔ All new features MUST be implemented as tasks in Claude Code

------------------------------------------------
F. Mandatory Folder Structure

/
├── .env
├── README.md
├── my-ai-book/                 # Docusaurus Frontend
│   ├── docs/                   # All textbook content (.md)
│   └── src/
└── backend/
    ├── requirements.txt
    ├── rag_service.py          # Main FastAPI app (core)
    ├── indexing_script.py      # Qdrant indexer
    ├── auth_db_service.py      # Neon + Better-Auth Helpers
    ├── personalization.py      # Bonus feature logic (optional)
    ├── translation.py          # Urdu feature logic (optional)
    └── uvicorn_start.sh