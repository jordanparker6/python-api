from pydantic import BaseModel

class ORMBase(BaseModel):
    class Config:
        orm_mode = True

class HTTPSuccess(BaseModel):
    message: str

class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }

class ItemNotFoundError(HTTPError):
    class Config:
        schema_extra = {
            "example": {"detail": "Item not found."},
        }