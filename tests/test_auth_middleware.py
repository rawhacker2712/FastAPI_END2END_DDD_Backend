def test_request_without_api_key(client):
    r = client.get("/tasks/middleware-test")  # No header
    assert r.status_code == 403

def test_request_with_invalid_api_key(client):
    r = client.get("/tasks/middleware-test", headers={"X-API-Key": "wrong-key"})
    assert r.status_code == 403

def test_request_with_valid_api_key(client, headers):
    r = client.get("/employees/", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_middleware_test_valid_key(client, headers):
    response = client.get("/tasks/middleware-test", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
