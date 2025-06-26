from app.domain.entities import Employee, Task


class EmployeeAggregate:
    def __init__(self, employee: Employee):
        self.employee = employee

    def get_entity(self):
        return self.employee


class TaskAggregate:
    def __init__(self, task: Task):
        self.task = task

    def get_entity(self):
        return self.task
