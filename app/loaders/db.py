from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

from app.core import config

def create_db_uri(db):
    db = {k : quote(v) for k, v in db.items()}
    return "{}://{}:{}@{}:{}/{}".format(
        db["type"],
        db["username"],
        db["password"],
        db["host"],
        db["port"],
        db["database"]
    )

DB_URI = create_db_uri(config.DATABASE)
engine = create_engine(DB_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
