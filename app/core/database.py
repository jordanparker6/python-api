"""A database factory for creating database classes from config."""
from typing import Dict, Optional, List, Any
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from urllib.parse import quote
import pandas as pd

from app.core import config
from app.core.logging import Logger

class DatabaseFactory(Logger):
    """A database building class.
    """
    def __init__(self):
        super().__init__()
        if self.engine:
            self.Session = sqla.orm.sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            self._conn = None
        else:
            self.log.error("Engine not bound to database class. Run Database.build_engine(db) prior to initiating.")
            raise ValueError

    def __enter__(self):
        self._conn= self.Session()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._conn.close() # pylint: disable=E1101

    # //////////////////////////////
    # // Utility SQL Methods ///////
    # //////////////////////////////

    def execute(self, sql: str) -> pd.DataFrame:
        """Excute a SQL querry.

        Args:
            sql (str): SQL querry string.

        Returns:
            pd.DataFrame: Query result as a pandas dataframe.
        """
        result = self._conn.execute(sql).fetchall()
        return self._result_to_df(result)

    def select_all(self, orm: Any) -> List:
        return self._conn.query(orm).all()
    
    def insert(self, orm: Any, values: Dict[str, Any]):
        self._conn.execute(orm.__table__.insert(), values)

    def bulk_upsert(self, 
            orm: Any, 
            values: Dict[str, Any], 
            index_elements=List[str], 
            excluded_cols=[]
        ):
        insert_stmt = postgresql.insert(orm).values(values)
        update_columns = { col.name: col for col in insert_stmt.excluded if col.name not in excluded_cols }
        update_stmt = insert_stmt.on_conflict_do_update(index_elements=index_elements, set_=update_columns)
        self._conn.execute(update_stmt)

    def _orm_to_df(self, objs: List):
        result = []
        for obj in objs:
            result.append({ c.key: getattr(obj, c.key) for c in sqla.inspect(obj).mapper.column_attrs })
        return pd.DataFrame(result)

    def _result_to_df(self, result):
        if result:
            result = [{key: value for key, value in row.items()}
                        for row in result if row is not None]
        else:
            result = [{}]
        return pd.DataFrame(result)

    # //////////////////////////////
    # // Factory Methods ///////////
    # //////////////////////////////

    @classmethod
    def build_engine(cls, db):
        """Builds the URI and engine on the base class for initiation.

        Args:
            db (Dict): A dictionary containing the database parameters.

        Returns:
            [type]: [description]
        """
        cls.uri = cls._create_db_uri(db)
        cls.engine = sqla.create_engine(
            cls.uri, **cls._get_engine_params(config.DATABASE)
        )
        return cls
   
    @staticmethod
    def _create_db_uri(db: Dict) -> str:
        """Creates a database URI string from a dictionary.

        Args:
            db: A dictionary containing the database parameters.

        Returns:
            A URI string for the database.
        """
        db = {k : quote(str(v)) for k, v in db.items()}
        if db["type"] == "sqlite":
            return "sqlite:///{}".format(db["sqlite_path"])
        else:
            return "{}://{}:{}@{}:{}/{}".format(
                db["type"],
                db["username"],
                db["password"],
                db["host"],
                db["port"],
                db["database"]
            )

    @staticmethod
    def _get_engine_params(db: Dict) -> Dict:
        params = {"pool_pre_ping": True }
        if db["type"] == "sqlite":
            return { **params, "connect_args": {"check_same_thread": False} }
        else:
            return params

Base = declarative_base()
Database = DatabaseFactory.build_engine(config.DATABASE)