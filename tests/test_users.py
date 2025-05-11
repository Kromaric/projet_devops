from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_user():
    # Test getting a user that exists
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"]  == 1

    # Test getting a user that does not exist
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
