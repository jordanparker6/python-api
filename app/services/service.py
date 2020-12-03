from fastapi import Depends

from app.core.logging import Logger
from app.core.database import Database
from app.loaders import load_db

class Service(Logger):

    def __init__(self, db: Database = Depends(load_db)):
        super().__init__()
        self.db = db

    def test(self):
        result = self.db.execute("SELECT 1;")
        self.log.info("Executed Test: \n%s", str(result))
        return result
