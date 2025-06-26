from typing import Optional
from app.domain.dto.employee_dto import EmployeeCreateDTO
from app.domain.dto.task_dto import TaskCreateDTO

class Employee:
    def __init__(self, id: Optional[int], name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def from_dto(cls, dto: EmployeeCreateDTO):
        return cls(
            id=None,
            name=dto.name,
            email=dto.email
        )

class Task:
    def __init__(self, id: Optional[int], title: str, description: Optional[str], employee_id: int, status: str = "new"):
        self.id = id
        self.title = title
        self.description = description
        self.employee_id = employee_id
        self.status = status

    @classmethod
    def from_dto(cls, dto: TaskCreateDTO):
        return cls(
            id=None,
            title=dto.title,
            description=dto.description,
            employee_id=dto.employee_id,
            status="new"  # Optional: explicitly set here too
        )
