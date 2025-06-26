from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.session import Base  # <- Make sure this Base is used consistently

class EmployeeORM(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    tasks = relationship("TaskORM", back_populates="employee")

class TaskORM(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("EmployeeORM", back_populates="tasks")
