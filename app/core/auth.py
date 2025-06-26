# app/core/auth.py

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_403_FORBIDDEN
from fastapi import HTTPException

API_KEY_NAME = "X-API-Key"
API_KEY = "123456"  
# should match with deps.py

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        api_key_expected = API_KEY
        api_key_provided = request.headers.get(API_KEY_NAME)

        # Optional: you may want to exclude docs or health check routes
        if request.url.path.startswith(("/docs", "/redoc", "/openapi", "/health")):
                 return await call_next(request)


        if api_key_provided != api_key_expected:
            return Response(
                content='{"detail": "Invalid or missing API Key"}',
                status_code=HTTP_403_FORBIDDEN,
                media_type="application/json"
            )

        return await call_next(request)
