# tests/conftest.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
load_dotenv()  # ✅ Ensure .env loads before app is imported

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from main import app
from app.infrastructure.db.session import Base, get_db, SessionLocal, engine

# ================================
# DATABASE SETUP / TEARDOWN
# ================================

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """⚠️ Drops and recreates all tables before each test"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # Optional: clean-up after test
    Base.metadata.drop_all(bind=engine)

from typing import Generator

@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function", autouse=True)
def override_get_db(db_session):
    app.dependency_overrides[get_db] = lambda: db_session

# ================================
# TEST CLIENT + HEADERS
# ================================

@pytest.fixture(scope="function")
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def headers():
    api_key = os.getenv("API_KEY", "missing")
    assert api_key == "123456", f"Expected API_KEY to be 123456, got {api_key}"
    return {"X-API-Key": api_key}
