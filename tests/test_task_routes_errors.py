
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
HEADERS = {"X-API-Key": "123456"}

def test_get_nonexistent_task_returns_404():
    r = client.get("/tasks/9999", headers=HEADERS)
    assert r.status_code == 404
    assert r.json() == {"detail": "Task not found"}

def test_delete_nonexistent_task_returns_404():
    r = client.delete("/tasks/9999", headers=HEADERS)
    assert r.status_code == 404
    assert r.json() == {"detail": "Task not found"}

def test_delete_and_reget_task_flow():
    # create employee
    er = client.post("/employees/", json={"name":"X","email":"x@x.com"}, headers=HEADERS)
    emp_id = er.json()["id"]
    # create task
    tr = client.post("/tasks/", json={"title":"T","description":"D","employee_id":emp_id}, headers=HEADERS)
    task_id = tr.json()["id"]
    # delete
    dr = client.delete(f"/tasks/{task_id}", headers=HEADERS)
    assert dr.status_code == 204
    # now get it
    gr = client.get(f"/tasks/{task_id}", headers=HEADERS)
    assert gr.status_code == 404



def test_create_task_missing_fields():
    # Missing employee_id
    task_data = {"title": "Incomplete", "description": "Missing employee_id"}
    response = client.post("/tasks/", json=task_data, headers=HEADERS)
    assert response.status_code == 422  # Unprocessable Entity


def test_list_tasks(client, headers):
    response = client.get("/tasks/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
