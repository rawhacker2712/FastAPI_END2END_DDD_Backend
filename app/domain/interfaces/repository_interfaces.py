from abc import ABC, abstractmethod
from typing import Any


class IEmployeeRepository(ABC):
    @abstractmethod
    def create(self, employee: Any): pass

    @abstractmethod
    def get(self, employee_id: int): pass

    @abstractmethod
    def list(self): pass


class ITaskRepository(ABC):
    @abstractmethod
    def create(self, task: Any): pass

    @abstractmethod
    def get(self, task_id: int): pass

    @abstractmethod
    def list(self): pass
