from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, order
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

app = FastAPI(
    title="FastAPI MongoDB Boilerplate",
    lifespan=lifespan
)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(order.router, prefix="/api/orders", tags=["orders"])

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
