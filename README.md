🚀 FastAPI E2E Backend – Domain-Driven Design Architecture
This project is a scalable and testable end-to-end backend system built with FastAPI, implementing Domain-Driven Design (DDD) architecture, complete CRUD functionality, API Key security, and full test coverage using pytest.

🧱 Project Highlights
✅ Clean and maintainable structure using DDD principles
✅ Modular separation of domain, infrastructure, and application layers
✅ Full CRUD for Employee and Task entities
✅ RESTful APIs with FastAPI and automatic Swagger docs
✅ 100% test coverage using Pytest
✅ Designed for future extensibility (JWT, Redis, Docker, CI/CD)

🛠️ Tech Stack
Area	                     Tech Used
Framework	                  FastAPI
Language                   	Python
ORM	                        SQLAlchemy
Architecture	              Domain-Driven Design (DDD)
Testing	                    Pytest
DB (Development)	          SQLite
Auth	                      API Key Middleware
Future Ready	              PostgreSQL, Redis, Docker


📁 Project Structure (Domain-Driven Design - DDD)


project-root/
│
├── .pytest_cache/              # Pytest cache directory
├── .vscode/                    # VSCode editor config
│   └── settings.json
├── app/                        # Main application package
│   ├── api/                    # API routers
│   │   ├── __init__.py
│   ├── core/                   # Core utilities
│   │   ├── __init__.py
│   │   ├── auth.py             # API Key middleware
│   │   └── logger.py
│   ├── domain/                 # Domain layer (DDD)
│   │   ├── __init__.py
│   │   ├── aggregates.py       # Aggregates (core business logic)
│   │   ├── entities.py         # Domain entities
│   │   └── interfaces/         # Abstract interfaces (repositories)
│   │       └── __init__.py
│   ├── infrastructure/         # DB models & repo implementations
│   │   ├── __init__.py
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   └── models.py
│   │   └── repositories/       # Concrete SQLAlchemy repository
│   │       └── repo.py
│   └── main.py                 # FastAPI app entry point
│
├── assets/                     # Optional static/image resources
├── htmlcov/                    # Test coverage HTML report
├── tests/                      # Pytest test suite
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures (client, db setup)
│   ├── test_*.py               # Unit/integration test files
│
├── .env                        # Environment variables (API key etc.)
├── .coverage                   # Coverage CLI report file
├── app.db                      # SQLite DB file
├── report.html                 # HTML test coverage report
├── structure.txt               # Optional text file for folder structure
├── requirements.txt            # (if available, not visible)
└── venv/                       # Virtual environment (not pushed to Git)


🧠 About Domain-Driven Design (DDD)
DDD is an architectural approach where the core business logic (the "domain") is isolated from the framework and infrastructure logic.

🔍 Key Benefits:
Clean separation of concerns

Easier testing and mocking

Core logic is not tied to the database or FastAPI

🧩 DDD in This Project:
domain/ contains pure Python classes like Employee, Task, and abstract interfaces

infrastructure/ implements those interfaces using SQLAlchemy

api/ wires everything together via FastAPI routers and dependency injection

🔐 API Security
All endpoints are protected by a custom API Key middleware.

To access routes, include this header:X-API-Key: 123456
The key is validated via AuthMiddleware before reaching the route logic.

✅ Testing with Pytest
Testing is built using pytest with fixtures that manage a test database lifecycle.

🔧 Example Fixtures (tests/conftest.py):
@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def headers():
    return {"X-API-Key": "123456"}
    
🧪 Sample Test:
def test_request_with_valid_api_key(client, headers):
    r = client.get("/employees/", headers=headers)
    assert r.status_code == 200

📊 Coverage Report

Metric	Status
Total Tests	✅ 31
Coverage	✅ 100%
Framework	Pytest + pytest-cov



pytest --cov=app --cov-report=term-missing --cov-report=html
>> 
================================================================================ test session starts =================================================================================
platform win32 -- Python 3.12.10, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\Users\tanishq.sati\Desktop\TASK
plugins: anyio-4.9.0, asyncio-1.0.0, cov-6.2.1, html-4.1.1, metadata-3.1.1
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 31 items

tests\test_aggregates.py ..                                                                                                                                                     [  6%]
tests\test_auth_core_excluded.py ...                                                                                                                                            [ 16%]
tests\test_auth_middleware.py ....                                                                                                                                              [ 29%]
tests\test_deps.py ....                                                                                                                                                         [ 41%]
tests\test_employee.py ..                                                                                                                                                       [ 48%]
tests\test_logger.py ..                                                                                                                                                         [ 54%]
tests\test_repositories.py ......                                                                                                                                               [ 74%]
tests\test_session.py ..                                                                                                                                                        [ 80%]
tests\test_task.py .                                                                                                                                                            [ 83%]
tests\test_task_routes_errors.py .....                                                                                                                                          [100%]

=================================================================================== tests coverage =================================================================================== 
__________________________________________________________________ coverage: platform win32, python 3.12.10-final-0 __________________________________________________________________ 

Name                                             Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------
app\__init__.py                                      0      0   100%
app\api\__init__.py                                  0      0   100%
app\api\deps.py                                     15      0   100%
app\api\routers\__init__.py                          0      0   100%
app\api\routers\employee.py                         17      0   100%
app\api\routers\task.py                             32      0   100%
app\core\__init__.py                                 0      0   100%
app\core\auth.py                                    17      0   100%
app\core\logger.py                                   6      0   100%
app\domain\__init__.py                               0      0   100%
app\domain\aggregates.py                            11      0   100%
app\domain\dto\__init__.py                           0      0   100%
app\domain\dto\employee_dto.py                      12      0   100%
app\domain\dto\task_dto.py                          16      0   100%
app\domain\entities.py                              21      0   100%
app\domain\interfaces\__init__.py                    0      0   100%
app\domain\interfaces\repository_interfaces.py      16      0   100%
app\infrastructure\db\__init__.py                    0      0   100%
app\infrastructure\db\models.py                     16      0   100%
app\infrastructure\db\session.py                    12      0   100%
app\infrastructure\repositories\__init__.py          0      0   100%
app\infrastructure\repositories\repo.py             47      0   100%
------------------------------------------------------------------------------
TOTAL                                              238      0   100%
Coverage HTML written to dir htmlcov
================================================================================= 31 passed in 1.60s ================================================================================= 


📈 Future Enhancements

JWT-based authentication

Redis caching

Docker + Docker Compose support

PostgreSQL production-ready config

GitHub Actions for CI/CD

Alembic for DB migrations






