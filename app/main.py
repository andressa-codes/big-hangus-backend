from fastapi import FastAPI

from app.api.v1 import ingrediente, user
from app.core.config import config
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title=config.app_name)


# Register routes
app.include_router(user.router, prefix="/api/v1")
app.include_router(ingrediente.router, prefix="/api/v1")
