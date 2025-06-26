from sqlalchemy.orm import Session, joinedload
from typing import List
from app.infrastructure.db.models import EmployeeORM as EmployeeModel, TaskORM as TaskModel
from app.domain.entities import Employee as DomainEmployee, Task as DomainTask
from app.domain.interfaces.repository_interfaces import IEmployeeRepository, ITaskRepository


class EmployeeRepository(IEmployeeRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, emp: DomainEmployee) -> EmployeeModel:
        db_emp = EmployeeModel(
            name=emp.name,
            email=emp.email
        )
        self.db.add(db_emp)
        self.db.commit()
        self.db.refresh(db_emp)
        return db_emp

    def list(self) -> List[EmployeeModel]:
        return self.db.query(EmployeeModel).all()

    def get(self, emp_id: int) -> EmployeeModel | None:
        return self.db.query(EmployeeModel).filter(EmployeeModel.id == emp_id).first()

    def delete(self, emp_id: int) -> bool:
        emp = self.get(emp_id)
        if emp:
            self.db.delete(emp)
            self.db.commit()
            return True
        return False


class TaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: DomainTask) -> TaskModel:
        db_task = TaskModel(
            title=task.title,
            description=task.description,
            employee_id=task.employee_id
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def list(self) -> List[TaskModel]:
        return self.db.query(TaskModel).all()

    def get(self, task_id: int) -> TaskModel | None:
        return self.db.query(TaskModel).filter(TaskModel.id == task_id).first()

    def get_with_employee(self, task_id: int) -> TaskModel | None:
        return (
            self.db.query(TaskModel)
            .options(joinedload(TaskModel.employee))
            .filter(TaskModel.id == task_id)
            .first()
        )

    def delete(self, task_id: int) -> bool:
        task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        return False
