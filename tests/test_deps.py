import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, validate_api_key, API_KEY
from app.infrastructure.db.session import SessionLocal, engine

def test_engine_and_session_local():
    # engine should be usable
    assert hasattr(engine, "connect")
    db = SessionLocal()
    assert hasattr(db, "query")
    db.close()

def test_get_db_yields_and_closes(monkeypatch):
    closed = False

    class DummySession:
        def close(self):
            nonlocal closed
            closed = True

    def fake_session_local():
        return DummySession()

    monkeypatch.setattr("app.api.deps.SessionLocal", fake_session_local)

    gen = get_db()
    session = next(gen)
    assert isinstance(session, DummySession)
    # closing
    try:
        next(gen)
    except StopIteration:
        pass
    assert closed is True

def test_validate_api_key_valid():
    # should return the key back
    assert validate_api_key(API_KEY) == API_KEY

def test_validate_api_key_invalid():
    with pytest.raises(HTTPException) as exc:
        validate_api_key("bad-key")
    assert exc.value.status_code == 403
    assert exc.value.detail == "Invalid API Key"
