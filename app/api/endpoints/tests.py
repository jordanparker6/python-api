from fastapi import APIRouter, Depends

from app.services.service import Service

router = APIRouter()

@router.get("/testApi")
async def test_api():
    return { "message": "Hello World" }

@router.get("/testDb")
async def test_db(service: Service = Depends(Service)):
    if service.test().__class__ is not None:
        return { "message": "Database connected." }
    else:
        return { "message": "Database not connected."}