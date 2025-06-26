import pytest
from sqlalchemy.orm import Session

from app.infrastructure.repositories.repo import EmployeeRepository, TaskRepository
from app.domain.entities import Employee as DE, Task as DT


@pytest.fixture
def dummy_session():
    class Dummy:
        def __init__(self):
            pass
        def add(self, obj): pass
        def commit(self): pass
        def refresh(self, obj): setattr(obj, "id", 1)
        def query(self, model): return self
        def filter(self, *args): return self
        def first(self): return None
        def all(self): return []
        def delete(self, obj): pass
        # add this stub so .options() won’t blow up
        def options(self, *args, **kwargs): return self

    return Dummy()

def test_employee_repo_delete_nonexistent(dummy_session):
    repo = EmployeeRepository(dummy_session)
    assert repo.delete(12345) is False

def test_task_repo_delete_nonexistent(dummy_session):
    repo = TaskRepository(dummy_session)
    assert repo.delete(6789) is False

def test_task_repo_get_nonexistent(dummy_session):
    repo = TaskRepository(dummy_session)
    assert repo.get_with_employee(9999) is None


def test_employee_repo_delete_success(dummy_session):
    class DummyEmployee:
        id = 123

    dummy_session.query = lambda model: dummy_session
    dummy_session.filter = lambda *args: dummy_session
    dummy_session.first = lambda: DummyEmployee()

    repo = EmployeeRepository(dummy_session)
    assert repo.delete(123) is True

def test_task_repo_list_empty(dummy_session):
    repo = TaskRepository(dummy_session)
    assert repo.list() == []

def test_task_repo_get(dummy_session):
    class DummyTask:
        id = 1

    dummy_session.query = lambda model: dummy_session
    dummy_session.filter = lambda *args: dummy_session
    dummy_session.first = lambda: DummyTask()

    repo = TaskRepository(dummy_session)
    task = repo.get(1)
    assert task.id == 1

