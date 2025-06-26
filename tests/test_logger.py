# tests/test_logger.py

import json
import pytest
from app.core.logger import setup_logging, logger

def test_setup_logging_and_json_output(capsys):
    # Initialize both stdlib logging and structlog
    setup_logging()

    # Emit a structured log event
    logger.info("hello-world", user="tester", value=42)

    # Capture stdout/stderr (structlog writes to stdout by default)
    captured = capsys.readouterr().out.strip()

    # It should be valid JSON
    data = json.loads(captured)

    # Core keys from your JSONRenderer
    assert data["event"] == "hello-world"
    assert data["user"] == "tester"
    assert data["value"] == 42

    # And timestamp should be present
    assert "timestamp" in data

def test_logger_is_bound_and_has_methods():
    # Without reconfiguring, logger should still work
    # (i.e. it exposes the standard methods)
    for level in ("debug", "info", "warn", "error"):
        assert hasattr(logger, level)
        # calling should not raise
        getattr(logger, level)("a message")

    # Binding extra context produces a new logger
    bound = logger.bind(session="xyz")
    assert hasattr(bound, "info")
    bound.info("with-session")  # smoke test
