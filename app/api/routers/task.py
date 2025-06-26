# app/api/routers/task.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, validate_api_key
from app.domain.dto.task_dto import TaskCreateDTO, TaskOutDTO
from app.domain.entities import Task as DomainTask
from app.infrastructure.repositories.repo import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.get("/middleware-test", dependencies=[Depends(validate_api_key)])
def test_middleware_route():
    return {"message": "success"}

@router.post("/", response_model=TaskOutDTO, status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreateDTO,
    db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    domain_task = DomainTask.from_dto(task)
    return repo.create(domain_task)

@router.get("/", response_model=list[TaskOutDTO])
def list_tasks(db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    return repo.list()

@router.get("/{task_id}", response_model=TaskOutDTO)
def get_task_with_employee(
    task_id: int,
    db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    db_task = repo.get_with_employee(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    repo = TaskRepository(db)
    success = repo.delete(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

