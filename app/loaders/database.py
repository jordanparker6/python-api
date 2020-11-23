"""Database dependancy loader for use in depedency injection."""
from typing import Generator, Dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
import pandas as pd

from app.core import config

async def load_db() -> Generator:
    with Database() as db:
        yield db

class Database:
    def __init__(self):
        self.uri = self._create_db_uri(config.DATABASE)
        self.engine = create_engine(self.uri, pool_pre_ping=True)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self._db = None
    
    def __enter__(self):
        self._db = self.session()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._db.close() # pylint: disable=E1101
            
    def _create_db_uri(self, db: Dict) -> str:
        """Creates a database URI string from a dictionary.

        Args:
            db: A dictionary containing the database parameters.

        Returns:
            A URI string for the database.
        """
        db = {k : quote(str(v)) for k, v in db.items()}
        return "{}://{}:{}@{}:{}/{}".format(
            db["type"],
            db["username"],
            db["password"],
            db["host"],
            db["port"],
            db["database"]
        )

    def execute(self, sql: str) -> pd.DataFrame:
        result = self._db.execute(sql).fetchall() # pylint: disable=E1101
        if result is not None:
            result = [{key: value for key, value in row.items()} for row in result if row is not None]
        else:
            result = [{}]
        return pd.DataFrame(result)

