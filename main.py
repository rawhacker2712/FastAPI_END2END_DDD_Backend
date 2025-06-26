from dotenv import load_dotenv
load_dotenv()  # ✅ Load .env first!

from fastapi import FastAPI
from app.core.auth import AuthMiddleware
from fastapi.openapi.utils import get_openapi
from app.api.routers import employee, task
from app.infrastructure.db.session import engine, Base

API_KEY_NAME = "X-API-Key"

app = FastAPI()

Base.metadata.create_all(bind=engine)

# ✅ Now safe to add middleware
app.add_middleware(AuthMiddleware)

# ✅ Include routers
app.include_router(employee.router, prefix="/employees")
app.include_router(task.router)

# ✅ Fix Swagger to show API key auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Employee Task API",
        version="1.0.0",
        description="Protected by API Key",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "in": "header",
            "name": API_KEY_NAME,
        }
    }

    openapi_schema["security"] = [{"APIKeyHeader": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
