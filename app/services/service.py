from fastapi import Depends

from app.core.logging import Logger
from app.loaders.database import load_db, Database

class Service(Logger):

    def __init__(self, db: Database = Depends(load_db)):
        super().__init__()
        self._db = db

    def test(self):
        result = self._db.execute("SELECT 1;")
        self.log.info("Executed Test: \n%s", str(result))
        return result
