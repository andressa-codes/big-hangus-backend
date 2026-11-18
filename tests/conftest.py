import os
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig

os.environ["DATABASE_URL"] = os.environ.get(
    "TEST_DATABASE_URL",
    "sqlite+pysqlite:///:memory:",
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    from tests.test_db import engine

    alembic_config = AlembicConfig(str(PROJECT_ROOT / "alembic.ini"))
    with engine.connect() as connection:
        alembic_config.attributes["connection"] = connection
        command.upgrade(alembic_config, "head")
    yield
