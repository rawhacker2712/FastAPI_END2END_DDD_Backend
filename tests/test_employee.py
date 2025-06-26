def test_create_employee(client, headers):
    response = client.post(
        "/employees/",
        json={"name": "John Doe", "email": "john@example.com"},
        headers=headers
    )
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert "id" in data

def test_list_employees(client, headers):
    # Create employee
    create_resp = client.post(
        "/employees/",
        json={"name": "Tester", "email": "tester@example.com"},
        headers=headers
    )
    assert create_resp.status_code in [200, 201]

    # Now list employees
    response = client.get("/employees/", headers=headers)
    assert response.status_code == 200
    employees = response.json()
    assert isinstance(employees, list)
    assert any("id" in emp for emp in employees)



