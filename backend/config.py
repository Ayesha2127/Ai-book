from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Central backend configuration loaded from environment variables / .env.

    Neon URL is optional at runtime so the API can start before DB is ready.
    """

    # Core app
    APP_NAME: str = "RAG Textbook Platform Backend"

    # Neon Postgres
    NEON_DATABASE_URL: Optional[str] = None

    # Qdrant
    QDRANT_URL: Optional[str] = None
    QDRANT_API_KEY: Optional[str] = None

    # LLM / embeddings
    GEMINI_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Cached settings instance so we only read env once.
    """
    return Settings()


