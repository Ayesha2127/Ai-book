from typing import Optional

from qdrant_client import QdrantClient

from .config import get_settings


_client: Optional[QdrantClient] = None


def get_qdrant_client() -> QdrantClient:
    """
    Lazy-init Qdrant client using env vars from Settings.
    """
    global _client
    if _client is None:
        settings = get_settings()
        if not settings.QDRANT_URL:
            raise RuntimeError("QDRANT_URL is not set in environment/.env")

        _client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )
    return _client


def ping_qdrant() -> bool:
    """
    Simple connectivity check: list collections.
    Returns True if Qdrant responds without raising.
    """
    client = get_qdrant_client()
    _ = client.get_collections()
    return True


