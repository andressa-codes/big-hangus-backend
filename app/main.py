from fastapi import FastAPI

from app.api.v1 import ingrediente, user
from app.core.config import config
from app.core.logging import setup_logging

from fastapi.middleware.cors import CORSMiddleware

setup_logging()

app = FastAPI(
    title="Big Hangus Estoque",
    description="API do controle de estoque da Big Hangus. CRUD de ingredientes.",
    version="1.0.0",
)


# Register routes
app.include_router(user.router, prefix="/api/v1")
app.include_router(ingrediente.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
