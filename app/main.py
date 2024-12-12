from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.core.config import settings
from app.database.mongodb import MongoDB
from app.routes.api import api_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up...")
    await MongoDB.connect_to_database()
    yield
    # Shutdown
    logger.info("Shutting down...")
    await MongoDB.close_database_connection()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan,
    )

    # Set CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_CREDENTIALS,
        allow_methods=settings.CORS_METHODS,
        allow_headers=settings.CORS_HEADERS,
    )

    # Add routes
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get("/")
    async def root():
        return {
            "message": f"Welcome to {settings.APP_NAME}",
            "docs": {"Swagger UI": "/docs", "ReDoc": "/redoc"},
            "api": {"base_url": settings.API_V1_STR, "version": "v1"},
        }

    return app


app = create_app()
