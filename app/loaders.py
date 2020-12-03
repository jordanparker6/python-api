"""Loading functions for use in FastAPI's depedency injection."""
from typing import Generator

from app.core.database import Database

async def load_db() -> Generator:
    with Database() as db:
        yield db