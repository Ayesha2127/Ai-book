from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .api.routes_core import router as core_router
from .api.routes_rag import router as rag_router

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)

origins = [
    "*",  # Allow all origins for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(core_router)
app.include_router(rag_router)
