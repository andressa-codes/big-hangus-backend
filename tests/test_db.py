from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import config

# The test database URL is resolved in tests/conftest.py before the app is imported.
if config.db_url.startswith("sqlite"):
    engine = create_engine(
        config.db_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    engine = create_engine(config.db_url, pool_pre_ping=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
