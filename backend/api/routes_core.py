from fastapi import APIRouter

from ..qdrant_service import ping_qdrant

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "RAG Textbook Platform Backend"}


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/health/qdrant")
async def qdrant_health():
    """
    Check if the backend can reach Qdrant using the configured URL/API key.
    """
    try:
        ok = ping_qdrant()
    except Exception as exc:  # noqa: BLE001
        return {"status": "error", "detail": str(exc)}

    return {"status": "ok" if ok else "error"}

