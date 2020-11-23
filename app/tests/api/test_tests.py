from fastapi.testclient import TestClient
from app.core import config

def test_testApi(client: TestClient) -> None:
    r = client.get(f"{config.API_VERSION}/testApi")
    message = r.json()
    assert r.status_code == 200
    assert message["message"] == "Hello World"

def test_testDb(client: TestClient) -> None:
    r = client.get(f"{config.API_VERSION}/testDb")
    message = r.json()
    assert r.status_code == 200
    assert message["message"] == "Database connected."