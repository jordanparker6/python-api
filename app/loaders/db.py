from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib import parse

from app.core import config

def create_db_uri(db):
    return parse("{}://{}:{}@{}:{}/{}".format(db["type"], db["username"], db["password"], db["host"], db["port"], db["database"]))

db_uri = create_db_uri(config.DATABASE)
engine = create_engine(db_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()