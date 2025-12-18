from typing import List, Optional, Dict

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/api/rag", tags=["rag"])


class RAGQueryRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None
    session_id: Optional[str] = None


class RAGQueryResponse(BaseModel):
    answer: str
    citations: List[Dict]
    latency_ms: Optional[int] = None
    language: str = "en"


@router.post("/query", response_model=RAGQueryResponse)
async def rag_query(payload: RAGQueryRequest):
    """
    Temporary stub implementation for the RAG query endpoint.
    This will later be wired to Qdrant + LLM; for now it returns a dummy answer.
    """
    dummy_answer = (
        "This is a placeholder answer. The real RAG pipeline is not implemented yet. "
        f"Your query was: {payload.query}"
    )

    return RAGQueryResponse(
        answer=dummy_answer,
        citations=[],
        latency_ms=None,
        language="en",
    )


