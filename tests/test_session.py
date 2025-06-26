# tests/test_session.py

import pytest
from sqlalchemy import inspect
from app.infrastructure.db.session import engine, get_db

def test_base_metadata_has_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "employees" in tables
    assert "tasks" in tables

def test_get_db_yields_session_and_closes():
    gen = get_db()
    session = next(gen)
    from sqlalchemy.orm import Session
    assert isinstance(session, Session)
    # finish the generator to close it
    with pytest.raises(StopIteration):
        next(gen)
