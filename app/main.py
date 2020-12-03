"""Entrypoint for the API.
"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from app.core import config
from app.core.database import Base, Database
from app.api import router

import app.models.model

Base.metadata.create_all(bind=Database.engine)

tags_metadata = [
    { "name": "Tests", "description": "A collection of API testing endpoints."},
]

app = FastAPI(
    docs_url=f"{config.API_VERSION}/docs",
    redoc_url=f"{config.API_VERSION}/redocs",
)

# Set all CORS enabled origins
if config.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in config.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix=config.API_VERSION)

# OpenAPI spec overides
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=config.PROJECT_NAME,
        version=config.API_VERSION,
        description="A Python API template.",
        routes=app.routes,
        tags=tags_metadata
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
        "href": "https://fastapi.tiangolo.com/"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

