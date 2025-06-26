![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)


# 🚀 FastAPI E2E Backend – Domain-Driven Design Architecture

This project is a scalable and testable **end-to-end backend system** built with FastAPI, implementing **Domain-Driven Design (DDD)** architecture, full CRUD functionality, API Key security, and test coverage using `pytest`.

---

## 🧱 Project Highlights

- ✅ Clean and maintainable structure using **DDD principles**
- ✅ Modular separation of domain, infrastructure, and application layers
- ✅ Full CRUD for `Employee` and `Task` entities
- ✅ RESTful APIs with FastAPI and automatic Swagger docs
- ✅ 100% test coverage using **Pytest**
- ✅ Designed for future extensibility (JWT, Redis, Docker, CI/CD)

---

## 🛠️ Tech Stack

| Area               | Tech Used                  |
|--------------------|----------------------------|
| Framework          | FastAPI                    |
| Language           | Python                     |
| ORM                | SQLAlchemy                 |
| Architecture       | Domain-Driven Design (DDD) |
| Testing            | Pytest                     |
| DB (Development)   | SQLite                     |
| Auth               | API Key Middleware         |
| Future Ready       | PostgreSQL, Redis, Docker  |

---

## 📁 Project Structure (Domain-Driven Design - DDD)

project-root/
├── .pytest_cache/
├── .vscode/
│ └── settings.json
├── app/
│ ├── api/
│ ├── core/
│ │ ├── auth.py
│ │ └── logger.py
│ ├── domain/
│ │ ├── aggregates.py
│ │ ├── entities.py
│ │ └── interfaces/
│ ├── infrastructure/
│ │ ├── db/
│ │ │ ├── session.py
│ │ │ └── models.py
│ │ └── repositories/
│ └── main.py
├── htmlcov/
├── assets/
├── tests/
│ ├── conftest.py
│ ├── test_*.py
├── .env
├── .coverage
├── app.db
├── report.html
├── requirements.txt
└── venv/




---

## 🧠 About Domain-Driven Design (DDD)

DDD is an architectural approach where the **core business logic (domain)** is isolated from infrastructure and application concerns.

### 🔍 Key Benefits

- Clean separation of concerns
- Easier testing and mocking
- Domain logic not tied to FastAPI or database

### 🧩 In This Project

- `domain/` – Pure Python classes like `Employee`, `Task`, and abstract interfaces
- `infrastructure/` – SQLAlchemy implementations of repositories
- `api/` – FastAPI routers with dependency injection

---

## 🔐 API Security

All endpoints are protected via a **custom API Key middleware**.

Use this header to access the API: 123456


---

## ✅ Testing with Pytest

- Testing is done with `pytest`
- Fixtures handle test database setup and teardown

### 🧪 Example Fixture

```python
@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def headers():
    return {"X-API-Key": "123456"}


def test_request_with_valid_api_key(client, headers):
    response = client.get("/employees/", headers=headers)
    assert response.status_code == 200


📊 Coverage Report
Metric	Status
Total Tests	✅ 31
Coverage	✅ 100%
Framework	Pytest + pytest-cov


📈 Future Enhancements
🔑 JWT-based authentication

⚡ Redis caching

🐳 Docker & Docker Compose

🐘 PostgreSQL integration

🔁 GitHub Actions CI/CD

📦 Alembic for migrations
