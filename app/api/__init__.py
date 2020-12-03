"""Unifies all the API endpoints into a single APIRouter()"""
from fastapi import APIRouter

from app.api.endpoints import tests

router = APIRouter()
router.include_router(tests.router, tags=["Tests"])