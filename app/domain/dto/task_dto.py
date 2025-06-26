# app/domain/dto/task_dto.py

from pydantic import BaseModel
from typing import Optional
from app.domain.dto.employee_dto import EmployeeOutDTO

class TaskCreateDTO(BaseModel):
    title: str
    description: Optional[str] = None
    employee_id: int

class TaskUpdateDTO(TaskCreateDTO):
    pass

class TaskOutDTO(BaseModel):
    id: int
    title: str
    description: Optional[str]
    employee_id: int
    employee: EmployeeOutDTO       # ← nested

    model_config = {
        "from_attributes": True     # ← ensures SQLAlchemy model attributes map automatically
    }
