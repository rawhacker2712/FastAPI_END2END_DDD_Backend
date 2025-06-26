def test_create_and_get_task(client, headers):
    # First create an employee
    emp_resp = client.post(
        "/employees/",
        json={"name": "Task Tester", "email": "task@example.com"},
        headers=headers
    )
    assert emp_resp.status_code in [200, 201]
    emp_data = emp_resp.json()
    emp_id = emp_data["id"]

    # Create a task for that employee
    task_resp = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "This is a test task",
            "employee_id": emp_id
        },
        headers=headers
    )
    assert task_resp.status_code in [200, 201]
    task_data = task_resp.json()
    assert task_data["title"] == "Test Task"
    assert task_data["employee_id"] == emp_id

    # Get the task with employee details
    task_id = task_data["id"]
    get_resp = client.get(f"/tasks/{task_id}", headers=headers)
    assert get_resp.status_code == 200
    full_data = get_resp.json()
    assert full_data["employee"]["email"] == "task@example.com"
