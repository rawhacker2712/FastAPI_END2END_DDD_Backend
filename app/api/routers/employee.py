from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, validate_api_key
from app.domain.dto.employee_dto import EmployeeCreateDTO, EmployeeOutDTO
from app.domain.entities import Employee as DomainEmployee
from app.infrastructure.repositories.repo import EmployeeRepository

router = APIRouter(
    
    tags=["Employees"]  # ✅ Centralized auth
)

@router.post("/", response_model=EmployeeOutDTO, status_code=status.HTTP_201_CREATED)
def create_employee(
    emp: EmployeeCreateDTO,
    db: Session = Depends(get_db)
):
    repo = EmployeeRepository(db)
    domain_emp = DomainEmployee.from_dto(emp)
    db_emp = repo.create(domain_emp)
    return db_emp

@router.get("/", response_model=list[EmployeeOutDTO])
def list_employees(
    db: Session = Depends(get_db)
):
    repo = EmployeeRepository(db)
    return repo.list()
