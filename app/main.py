from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routes.index import router as v1_router
from app.database import connect_to_mongo, close_mongo_connection

@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    print("""
🚀 Server is running!

📚 API Documentation:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc
   
🔗 API Base URL: http://127.0.0.1:8000/api

Press CTRL+C to stop the server
    """)
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()

def init_routers(app: FastAPI):
    app.include_router(v1_router, prefix="/api")
    logging.info("Routers initialized")

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI MongoDB Boilerplate",
        lifespan=lifespan
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    init_routers(app=app)
    return app

app = create_app()

@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI MongoDB Boilerplate",
        "docs": {
            "Swagger UI": "/docs",
            "ReDoc": "/redoc"
        },
        "server_urls": {
            "local": "http://localhost:8000",
            "api_base": "/api"
        }
    }