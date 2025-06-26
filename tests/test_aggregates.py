from app.domain.aggregates import EmployeeAggregate, TaskAggregate
from app.domain.entities import Employee as DE, Task as DT

def test_employee_aggregate_basic():
    entity = DE(id=None, name="Alice", email="alice@example.com")
    agg = EmployeeAggregate(entity)
    assert agg.get_entity() is entity  # ✅ changed from agg.entity

def test_task_aggregate_status_transitions():
    entity = DT(id=None, title="Write tests", description="", employee_id=1)
    agg = TaskAggregate(entity)
    assert agg.get_entity().status == "new"  # ✅ access status through the entity
