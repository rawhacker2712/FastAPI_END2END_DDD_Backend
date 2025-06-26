# app/api/deps.py

from fastapi import HTTPException, status, Header
from typing import Optional
from app.infrastructure.db.session import SessionLocal
from sqlalchemy.orm import Session

# Match your .env/API key
API_KEY = "123456"

from typing import Generator

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def validate_api_key(
    x_api_key: Optional[str] = Header(None, alias="X-API-Key")
) -> str:
    """
    API key header is optional at Pydantic level.
    We then enforce presence+correctness here, raising 403.
    """
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key"
        )
    return x_api_key
