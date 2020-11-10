import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core import config
from app.api.router import router

app = FastAPI(
    title=config.PROJECT_NAME, 
    openapi_url=f"{config.API_VERSION}/openapi.json"
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