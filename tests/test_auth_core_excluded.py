# tests/test_auth_core_excluded.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("path", ["/docs", "/openapi.json", "/redoc"])
def test_excluded_paths(path):
    r = client.get(path)
    assert r.status_code == 200  # ✅ These paths are meant to be public
