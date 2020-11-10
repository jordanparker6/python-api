from fastapi import APIRouter

from app.api.endpoints import hello_world

router = APIRouter()
router.include_router(hello_world.router, tags=["test"])
