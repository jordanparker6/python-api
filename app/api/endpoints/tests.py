from fastapi import APIRouter, Depends

from app.api.schemas.core import HTTPSuccess
from app.services.service import Service

router = APIRouter()

@router.get(
    "/test",
    response_model=HTTPSuccess,
    response_description="Test sucesss."

)
async def test_connection() -> HTTPSuccess:
    """Tests the functionality of the API networking."""
    return { "message": "Hello World" }

@router.get(
    "/testDb",
    response_model=HTTPSuccess,
    response_description="Test sucesss."
)
async def test_db(
        service: Service = Depends(Service)
    ) -> HTTPSuccess:
    """Test the API to determine if the database is connected."""
    if service.test().__class__ is not None:
        return { "message": "Database connected." }
    else:
        return  {"message": "Database not connected." }