from fastapi.testclient import TestClient
from app.core import config

def test_hello_world(client: TestClient) -> None:
    r = client.get(f"{config.API_VERSION}/")
    message = r.json()
    assert r.status_code == 200
    assert message["message"] == "Hello World"