from typing import Generator
import pytest
from fastapi.testclient import TestClient

from app.loaders import Database
from app.main import app

@pytest.fixture(scope="session")
def db() -> Generator:
    yield Database()

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
